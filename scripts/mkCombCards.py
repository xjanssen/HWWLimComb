#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

import ROOT
from ROOT import *

import combTools
import batchTools

from Config import *
from manipDataCard import card as cardTools
from copy import deepcopy 


# ---------------------------------------------------- WJetFix() ------------------------------------------
def WJetFix(cardIn,cardForWJ):
    if not iChannel in preProc['WJetFix']['ChannelList'] :
      return cardIn
    cardWJ =cardForWJ.replace(cardDir,'couplings').replace(str(iMass),(preProc['WJetFix']['massWJ']).replace('$MASS',str(iMass))).replace('_hsm','')
    cardOut=cardIn.replace(os.path.splitext(cardIn)[1],'_WJetFix'+os.path.splitext(cardIn)[1] )  
    print 'WJetFix IN  :', cardIn 
    print 'WJetFix WJet:', cardWJ
    print 'WJetFix OUT :', cardOut 

    
    dcIn = cardTools(cardIn)
    dcWJ = cardTools(cardWJ)
    
   
    for iBin in dcIn.content['block1']['bin']:
      ProcList=[]
      iPosProc=-1
      for jBin in dcIn.content['block2']['bin']:   
        iPosProc += 1
        Proc=dcIn.content['block2']['process'][iPosProc] 
        ProcList.append(Proc) 
      for iProc in preProc['WJetFix']['processList'] :
        if iProc in ProcList:
          #print iProc
          dcIn.setRate(bin=iBin,process=iProc,value=dcWJ.getCol(bin=iBin,process=iProc)['block2']['rate']) 
          for iSystType in dcIn.content['systs']:
            for iSyst in dcIn.content['systs'][iSystType]:
              dcIn.setSyst(bin=iBin,process=iProc,syst=iSystType, tag=iSyst , value='-')
          for iSystType in dcWJ.content['systs']:
            if iSystType in dcIn.content['systs']:        
              for iSyst in dcWJ.content['systs'][iSystType]:
                if iSyst in dcIn.content['systs'][iSystType]: 
                  dcIn.setSyst(bin=iBin,process=iProc,syst=iSystType, tag=iSyst , value= dcWJ.getSyst(bin=iBin,process=iProc,syst=iSystType, tag=iSyst))
          #print len(dcIn.content['header2']) , '-->' , dcIn.content['header2']
          if len(dcIn.content['header2']) > 0:
            for iShape in dcWJ.content['header2']: 
              #print  dcWJ.content['header2'][iShape][1] 
              if dcWJ.content['header2'][iShape][1] == '*' or dcWJ.content['header2'][iShape][1] == 'iProc':
                #print 'Replace' 
                Shape=dcWJ.content['header2'][iShape]
                #print cardDir
                FileWJ=cardWJ.replace(cardWJ.split('/')[-1],Shape[3])
                if len(Shape) == 5 : dcIn.addShape(iProc,Shape[2],FileWJ,Shape[4])
                if len(Shape) == 6 : dcIn.addShape(iProc,Shape[2],FileWJ,Shape[4],Shape[5])
  
          #print len(dcIn.content['header2']) , '-->' , dcIn.content['header2']

    os.system('rm '+cardOut)
    dcIn.write(cardOut) 
    return cardOut

# ---------------------------------------------------SMToys() -------------------------------------------
def SMToys(cardIn):
    dirName=os.path.dirname(cardIn)
    cardOut=cardIn.replace(os.path.splitext(cardIn)[1],'_SMToys'+os.path.splitext(cardIn)[1] )  
    dcIn  = cardTools(cardIn)
    dcOut = cardTools(cardIn)
    for iBin in dcIn.content['block1']['bin']:
      iPosProc=-1
      INJList=[]
      SMXList=[]
      ShapeProc={}

      # Copy rate and syst from *_SM to Signal 
      for jBin in dcIn.content['block2']['bin']:
        iPosProc += 1
        Proc=dcIn.content['block2']['process'][iPosProc] 
        PrId=dcIn.content['block2']['processId'][iPosProc]
        if iBin == jBin and '_SM' in Proc:
          INJList.append(Proc)
        if iBin == jBin and int(PrId) <= 0:
          SMXList.append(Proc)
      for iProc in SMXList:
        #print iProc
        if iProc+'_SM' in INJList:
          jProc=iProc+'_SM'
          dcOut.setRate(bin=iBin,process=iProc,value=dcIn.getCol(bin=iBin,process=jProc)['block2']['rate']) 
          SkipList=[]
          for iSystType in dcOut.content['systs']:
            for iSyst in dcOut.content['systs'][iSystType]:
              dcOut.setSyst(bin=iBin,process=iProc,syst=iSystType, tag=iSyst , value='-')
              if '_SM' in iSyst :
                jSyst=iSyst.replace('_SM','')
                SkipList.append(jSyst)
          for iSystType in dcIn.content['systs']:
            for iSyst in dcIn.content['systs'][iSystType]:
              jSyst=iSyst
              if '_SM' in iSyst and iSystType != 'shape' and iSystType != 'shapeN2' :
                jSyst=iSyst.replace('_SM','')
                #print iSyst , '->' , jSyst , iSystType
              if jSyst in dcOut.content['systs'][iSystType] and iSyst not in SkipList : 
                dcOut.setSyst(bin=iBin,process=iProc,syst=iSystType, tag=jSyst , value= dcIn.getSyst(bin=iBin,process=jProc,syst=iSystType, tag=iSyst))
          if len(dcIn.content['header2']) > 0:
            dcOut.remShape(jProc) 
            for iShape in dcIn.content['header2']: 
              if ( dcIn.content['header2'][iShape][1] == '*' or dcIn.content['header2'][iShape][1] == jProc ) and ( dcIn.content['header2'][iShape][2] == '*' or dcIn.content['header2'][iShape][2] == iBin ) :
                if iProc not in ShapeProc:
                  ShapeProc[iProc] = deepcopy(dcIn.content['header2'][iShape])
                else:
                  if ShapeProc[iProc][1] == '*' or ShapeProc[iProc][2] == '*' : ShapeProc[iProc] = deepcopy(dcIn.content['header2'][iShape]) 
        else:
          sys.exit('ERROR: Missing process to inject : '+iProc)

      # Add Shape lines if needed  
      for sProc in ShapeProc:
        ShapeProc[sProc][1] = sProc
        ShapeProc[sProc][2] = iBin
        ShapeProc[sProc][4] = ShapeProc[sProc][4].replace('$PROCESS',sProc+'_SM')
        ShapeProc[sProc][5] = ShapeProc[sProc][5].replace('$PROCESS',sProc+'_SM')
        dcOut.addShape(sProc,iBin,ShapeProc[sProc][3],ShapeProc[sProc][4],ShapeProc[sProc][5]) 

      # Remove *_SM process
      for jProc in INJList:
        dcOut.remCol(bin=iBin,process=jProc)

    # Fix lnU systematic
    if 'lnU' in dcOut.content['systs']:
      print dcOut.content['systs']['lnU']
      for iSyst in dcOut.content['systs']['lnU']:
        for i in xrange(0,len(dcOut.content['systs']['lnU'][iSyst])-1):
          dcOut.content['systs']['lnU'][iSyst][i] = '-'
      print dcOut.content['systs']['lnU']


    os.system('rm '+cardOut)
    dcOut.write(cardOut) 
    return cardOut

# ---------------------------------------------------SMInject() -------------------------------------------
def SMInject(cardIn,rmSMProc=True):
    dirName=os.path.dirname(cardIn)
    cardOut=cardIn.replace(os.path.splitext(cardIn)[1],'_SMInject'+os.path.splitext(cardIn)[1] )  
    dcIn  = cardTools(cardIn)
    dcOut = cardTools(cardIn)
    #dcIn.write()
    #print dcIn.content['block1']
    #print dcIn.content['block2']
    iPosBin=-1
    for iBin in dcIn.content['block1']['bin']:
      iPosBin+=1
      iPosProc=-1
      RateBG=0.
      RateSM=0.
      ProcList=[]
      INJList=[]
      for jBin in dcIn.content['block2']['bin']:
        iPosProc += 1
        Proc=dcIn.content['block2']['process'][iPosProc] 
        PrId=dcIn.content['block2']['processId'][iPosProc]
        if iBin == jBin and '_SM' in Proc:
          INJList.append(Proc)
          ProcList.append(Proc)
          RateSM+=float(dcIn.getRate(bin=iBin,process=Proc))
        if iBin == jBin and int(PrId) > 0 and '_SM' not in Proc:
          ProcList.append(Proc)
          RateBG+=float(dcIn.getRate(bin=iBin,process=Proc))
      RateInj=RateSM+RateBG
      #print ProcList , RateInj , RateSM , RateBG
      dcOut.content['block1']['observation'][iPosBin] = str(int(round(RateInj,0)))      
      if len(dcIn.content['header2']) > 0:
        dcOut.remShape('data_obs') 
        ShapeData=[]
        ShapeProc={}
        for iShape in dcIn.content['header2']: 
          #print  'SHAPE:' , dcIn.content['header2'][iShape] 
          if dcIn.content['header2'][iShape][1] == 'data_obs' and ( dcIn.content['header2'][iShape][2] == '*' or dcIn.content['header2'][iShape][2] == iBin ) :
            if len(ShapeData) == 0 :
              ShapeData=deepcopy(dcIn.content['header2'][iShape]) 
            else :
              if ShapeData[2] == '*' : ShapeData=deepcopy(dcIn.content['header2'][iShape]) 
          for Proc in ProcList:
            if ( dcIn.content['header2'][iShape][1] == '*' or dcIn.content['header2'][iShape][1] == Proc ) and ( dcIn.content['header2'][iShape][2] == '*' or dcIn.content['header2'][iShape][2] == iBin ) :
              if Proc not in ShapeProc:
                ShapeProc[Proc] = deepcopy(dcIn.content['header2'][iShape]) 
              else:
                if ShapeProc[Proc][1] == '*' or ShapeProc[Proc][2] == '*' : ShapeProc[Proc] = deepcopy(dcIn.content['header2'][iShape]) 
        # Create Pseudo-data
        PseudoDataFirst = False
        for sProc in ShapeProc:
          fileName=dirName+'/'+ShapeProc[sProc][3]
          histName=ShapeProc[sProc][4].replace('$PROCESS',sProc)
          fHist = TFile.Open(fileName)
          Hist  = fHist.Get(histName)
          gROOT.cd() 
          if not PseudoDataFirst :
            PseudoDataFirst = True
            PseudoData = Hist.Clone("histo_PseudoData")
            PseudoData.SetTitle("histo_PseudoData")
          else :
            PseudoData.Add(Hist)          
          fHist.Close()

        # round Pseudo-data (including under/over-flow)
        for i in xrange(0,PseudoData.GetNbinsX()+2):
          val = round(PseudoData.GetBinContent(i),0)
          if val>0 : err=sqrt(val)
          else     : err=0     
          PseudoData.SetBinContent(i,val)
          PseudoData.SetBinError(i,err)
        dcOut.content['block1']['observation'][iPosBin] = str(int(round(PseudoData.Integral(),0)))       
 
        fileShape=ShapeData[3] 
        fileShape=fileShape.replace(os.path.splitext(fileShape)[1],'_pseudodata_'+iBin+os.path.splitext(fileShape)[1] )       
        fHist = TFile.Open(dirName+'/'+fileShape,'RECREATE')
        PseudoData.Write() 
        fHist.Close()
        
        dcOut.addShape('data_obs',iBin,fileShape,'histo_PseudoData')


      # Remove *_SM process
      if rmSMProc:
        for jProc in INJList:
          dcOut.remCol(bin=iBin,process=jProc)


        #print PseudoData.Integral() , PseudoData.IsA().GetName() , fileShape
        #print ShapeProc

       

    print dcIn.content['block1'] , '--->' ,dcOut.content['block1']
    os.system('rm '+cardOut)
    dcOut.write(cardOut) 
    return cardOut

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-c", "--combs",      dest="combs",       help="Produce all combinations", default=[], type='string' , action='callback' , callback=combTools.list_maker('combs',','))
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-z", "--zip",        dest="zip",         help="compress output datacard", default=False, action="store_true")
parser.add_option("-P", "--purpose",    dest="purpose",     help="purpose of the datacard (couplings, searches, mass, ...)", default="searches", metavar="PATTERN")
parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )


(options, args) = parser.parse_args()

print '==== Data Cards Version : ',options.Version
combList   = combTools.CombList_Filter(combinations,options.combs).get()
cardDir    = combTools.CardDir_Filter(cardtypes,options.purpose).get()
energyList = combTools.EnergyList_Filter(options.energy).get()


# Build combinations
for iComb in combList:
   # Validate Combination Energy
   isValidEnergy=False
   for iEnergy in combinations[iComb]['energies']:
     if (options.energy == 7 or options.energy == 0) and iEnergy == '7TeV' : 
       isValidEnergy=True
     if (options.energy == 8 or options.energy == 0) and iEnergy == '8TeV' : 
       isValidEnergy=True
     if (options.energy == 13) and iEnergy == '13TeV' : 
       isValidEnergy=True
   # Validate Combination Purpose
   isValidPurpose=False
   for purpose in combinations[iComb]['purposes']:
     if options.purpose == purpose :
       isValidPurpose=True
   # Process if valid 
   if isValidEnergy and isValidPurpose :
     massList   = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,options.purpose,options.masses,iComb,energyList).get()
     print '---------------------- Building cards for combination: '+iComb
     if 'targetdir' in cardtypes[options.purpose]:
       TargetDir=workspace+'/'+options.Version+'/'+cardtypes[options.purpose]['targetdir']+'/'+iComb
     else:
       TargetDir=workspace+'/'+options.Version+'/'+cardDir+'/'+iComb
     print 'Target Dir : '+TargetDir
     print 'Masses List: '+str(massList)
     for iMass in massList:
       toCombine = []  
       #toMove = [] 
       for iChannel in  combinations[iComb]['channels']:
         for iEnergy in energyList :
           if (iEnergy in channels[options.Version][iChannel]) :
             if (iMass >= channels[options.Version][iChannel][iEnergy]['mrange'][0]) and (iMass <= channels[options.Version][iChannel][iEnergy]['mrange'][1]) : 
               if 'hcp2012' in channels[options.Version][iChannel][iEnergy]['dir'] :
                 card=cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMass))+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('$MASS',str(iMass))   
               else:
                 card=cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMass))+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('$MASS',str(iMass))   
               tag= "%s%s_%dTeV_%s" % (channels[options.Version][iChannel][iEnergy]['branch'],channels[options.Version][iChannel][iEnergy]['decay'],channels[options.Version][iChannel][iEnergy]['energy'],channels[options.Version][iChannel][iEnergy]['tag'])
               # Fix ZH card name for _hsm !!!
               if cardtypes[options.purpose]['dir'] == 'searches' and 'zh3l2j' in iChannel : card=card.replace('zh3l2j_','zh3l2j_hsm_')
               # Here we can manipulate cards
               print '  ' , tag, ' --> ', card
               if 'preProc' in cardtypes[options.purpose] :
                 for iPreProc in cardtypes[options.purpose]['preProc'] :
                   cardOri = card
                   print 'preProc : ' , iPreProc
                   if iPreProc == 'WJetFix'  : card = WJetFix(card)
                   if iPreProc == 'SMInject' : 
                     card = SMInject(card)
                     card = WJetFix(card,cardOri)
                   if iPreProc == 'SMToys'   : 
                     card = SMInject(card,False)
                     card = SMToys(card)
                     card = WJetFix(card,cardOri)

               if os.path.exists(card): toCombine.append((tag,card))
               else                   : print "WARNING: "+card+" does not exist !!!" 
               
       # And now the real combination
       if len(toCombine):
         print  iMass , "-->" , [Tag[0] for Tag in toCombine]
         outname = iComb 
         if options.energy != 0: outname += '_' + str(options.energy) + 'TeV'
         #else                  : outname += '_CombTeV' 
         outname += ".txt"
         pipe = ""
         if options.zip:
           pipe = " | gzip"; outname += ".gz"
         command =  'cd '+TargetDir+'/'+str(iMass)+' && '
         command += "combineCards.py -S "
         command += " ".join(["%s=%s" %(C,D) for (C,D) in toCombine])
         command += pipe
         command += " > "+outname
         if options.pretend: 
           print command
         else: 
           os.system('mkdir -p '+TargetDir+'/'+str(iMass)) 
           os.system(command)
