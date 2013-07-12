#!/bin/bash
#

inputcard=$1
rmProcList="ZH_SM WH_SM qqH_SM ggH_SM"

 
outputcard="split_SM_${inputcard%".txt"}.txt"
outputcard_ALT="split_SpinTwo_${inputcard%".txt"}.txt"
 
if [ -f $outputcard ]; then rm $outputcard; fi
if [ -f $outputcard_ALT ]; then rm $outputcard_ALT; fi

# Store all lines
OIFS=$IFS ; IFS=$'\n' ; read -d '' -r -a lines < $inputcard ; IFS=$OIFS

# Find process to remove
for line in "${lines[@]}"
do
  line=`(echo "$line" | sed "s:  ::g")`
  if  [[ `(echo "$line" | awk '{print $1}')` == "process" ]] && [[ "$line" != *-1* ]]  ; then OIFS=$IFS ; IFS=' ' ; read -a ProcName <<< ${line#"process"} ; IFS=$OIFS ; fi 
  if  [[ `(echo "$line" | awk '{print $1}')` == "process" ]] && [[ "$line" == *-1* ]]  ; then OIFS=$IFS ; IFS=' ' ; read -a ProcNums <<< ${line#"process"} ; IFS=$OIFS ; fi
done

iProc=0
for Proc in "${ProcName[@]}" ; do
 ProcAct[$iProc]=1
 for rmProc in $rmProcList ; do
    if [[ $Proc == $rmProc ]] ; then ProcAct[$iProc]=0 ; fi
 done
 iProc=`expr $iProc + 1`
done 

# Renumerotate Procs
iProc=0
iNum=1
for Proc in "${ProcNums[@]}" ; do
  if [ $Proc -gt "0" ] ; then
    if [ "${ProcAct[$iProc]}" -gt "0" ] ; then
      ProcNums[$iProc]=$iNum
      iNum=`expr $iNum + 1`
    else
      ProcNums[$iProc]='X'  
    fi
  fi
  iProc=`expr $iProc + 1`
done
iNum=0
for (( iProc=${#ProcNums[@]}-1 ; iProc>=0; iProc--)); do
 if [[ ${ProcNums[$iProc]} != "X" ]] ; then
   if [ "${ProcNums[$iProc]}" -le "0" ] ; then
     if [ "${ProcAct[$iProc]}" -gt "0" ] ; then
      ProcNums[$iProc]=$iNum
      iNum=`expr $iNum - 1`
     else
      ProcNums[$iProc]='X'
     fi
   fi
 fi
done

#echo proc ${ProcName[@]}
#echo proc ${ProcNums[@]}
#echo proc ${ProcAct[@]}

tmpFile=`mktemp`
for line in "${lines[@]}"
do
  #echo "$line"
  #echo "$line"

  # LineType: 0:Header 1:bin/process/rate 2:syst 3:gmN 
  if    [[ `(echo "$line" | awk '{print $1}')` == "bin"     ]] ; then LineType=1
  elif  [[ `(echo "$line" | awk '{print $1}')` == "process" ]] ; then LineType=1
  elif  [[ `(echo "$line" | awk '{print $1}')` == "rate"    ]] ; then LineType=1
  elif  [[ `(echo "$line" | awk '{print $2}')` == shape*    ]] ; then LineType=2
  elif  [[ `(echo "$line" | awk '{print $2}')` == "lnN"     ]] ; then LineType=2
  elif  [[ `(echo "$line" | awk '{print $2}')` == "lnU"     ]] ; then LineType=2
  elif  [[ `(echo "$line" | awk '{print $2}')` == "gmN"     ]] ; then LineType=3
  else  LineType=0 ; fi

  if [ "$LineType" -eq 0 ] ; then echo "$line" ; fi
  if [ "$LineType" -gt 0 ] ; then
    line=`(echo $line | sed "s:  ::g")`
    unset vOLine
    unset vNLine
    OIFS=$IFS ; IFS=' ' ; read -a vOLine <<< $line ; IFS=$OIFS
    vNLine[0]=${vOLine[0]}
    iProc=0
    iPrint=0
    if   [ "$LineType" -eq 1 ] ; then 
      iPrint=1
      vNLine[1]="REMME"
      iPNew=2
      iPOld=1
    elif [ "$LineType" -eq 2 ] ; then
      vNLine[1]=${vOLine[1]} 
      iPNew=2
      iPOld=2
    elif [ "$LineType" -eq 3 ] ; then
      vNLine[1]=${vOLine[1]}
      vNLine[2]=${vOLine[2]}
      iPNew=3
      iPOld=3
    fi
    for Proc in "${ProcAct[@]}" ; do
      if [ "${ProcAct[$iProc]}" -gt "0" ] ; then  
        if  [[ `(echo "$line" | awk '{print $1}')` == "process" ]] && [[ "$line" == *-1* ]]  ; then 
          vNLine[$iPNew]=${ProcNums[$iProc]} 
        else
          vNLine[$iPNew]=${vOLine[$iPOld]}
        fi
        if [ "${vNLine[$iPNew]}" != "-" ] ; then iPrint=1 ; fi 
        iPNew=`expr $iPNew + 1`
      fi 
      iProc=`expr $iProc + 1`
      iPOld=`expr $iPOld + 1`
    done
    if [ "$iPrint" -gt 0 ] ; then echo "${vNLine[@]}" >> $tmpFile ; fi
  fi

done 

cat $tmpFile | column -t | sed "s:REMME:     :"
rm  $tmpFile
