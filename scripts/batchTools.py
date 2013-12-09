#!/usr/bin/env python
import sys, re, os, os.path

from Config import *
import combTools
import subprocess
import string
import os.path
from optparse import OptionParser

class batchJobs :
   def __init__ (self,prefix,combList,energyList,PhysModelList,TargetList,batchSplit,masses,unblind,Version,AltModel=['NONE']):
      self.jobsDic={}
      self.jobsList=[]
      self.prefix=prefix
      if self.prefix != '' : self.prefix+='__'
      for iComb in combList:
        if not 'Comb' in batchSplit and len(combList)>1 :
          kComb = 'AllComb'
          for jComb in combList: kComb+='-'+jComb
        else:
          kComb = iComb 
        self.jobsDic[iComb] = {}
        # Model Split ?
        for iModel in PhysModelList:
          if not 'Model' in batchSplit and len(PhysModelList)>1 :    
            kModel = 'AllModel'
            for jModel in PhysModelList: kModel+='-'+jModel
          else:
            kModel = iModel
          self.jobsDic[iComb][iModel] = {}  
          # Mass Split ?     
          massList  = combTools.MassList_Filter(cardtypes,channels[Version],combinations,physmodels[iModel]['cardtype'],masses,iComb,energyList).get()
          for iMass in massList:
            if not 'Mass' in batchSplit and len(massList)>1 :
              kMass = 'AllMass'
            else: 
              kMass = str(iMass)  
            self.jobsDic[iComb][iModel][iMass] = {}
            # Target Split ?  
            for iTarget in TargetList:
              if unblind or targets[iTarget]['notblind'] : 
                if not 'Target' in batchSplit and len(TargetList)>1 :
                  kTarget = 'AllTarget'
                  for jTarget in TargetList: kTarget+='-'+jTarget
                else:
                  kTarget = iTarget
                # More than one job ?
                self.jobsDic[iComb][iModel][iMass][iTarget] = {}
                if iTarget in targets and 'NJobs' in targets[iTarget]:
                  NJobs = targets[iTarget]['NJobs']
                else:
                  NJobs = 1 
                # Job Multiple parameter ?
                if iTarget in targets and 'JobsParam' in targets[iTarget]:
                  NParam=1
                  for iJobParam in targets[iTarget]['JobsParam']:
                    NParam*=len(targets[iTarget]['JobsParam'][iJobParam]) 
                  NJobs=NJobs*NParam
                for iAltModel in AltModel:
                  self.jobsDic[iComb][iModel][iMass][iTarget][iAltModel] = {}
                  # Toys ?
                  ToysList = []
                  if iTarget in targets:
                    if 'Toys' in targets[iTarget]: 
                      if   len( energyList ) > 1 : iEnergy = 0 
                      elif '7TeV' in energyList : iEnergy = 7
                      elif '8TeV' in energyList : iEnergy = 8
                      ToysList = combTools.getToys(iComb,iTarget,iEnergy,iMass,workspace,Version,cardtypes,physmodels,targets,iAltModel)
                      NJobs=len(ToysList)
                  for iJob in xrange(1,NJobs+1):        
                    jName = self.prefix+kComb+'_'+iAltModel+'__'+kModel+'__'+kMass+'__'+kTarget+'__'+str(iJob)
                    self.jobsDic[iComb][iModel][iMass][iTarget][iAltModel][iJob] = jName
                    if not jName in self.jobsList: self.jobsList.append(jName)

      #print self.jobsDic
      #print self.jobsList
      #print len(self.jobsList)

      if not os.path.exists(jobdir) : os.system('mkdir -p '+jobdir)
      CMSSW=os.environ["CMSSW_BASE"]
      for jName in self.jobsList:
        jFile = open(jobdir+'/'+jName+'.sh','w')
        jFile.write('#!/bin/bash\n')
        jFile.write('#$ -N '+jName+'\n')
        jFile.write('#$ -q all.q\n')
        jFile.write('#$ -cwd\n')
        jFile.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n') 
        jFile.write('cd '+CMSSW+'\n')
        jFile.write('eval `scramv1 ru -sh`\n')
        jFile.close()
        os.system('chmod +x '+jobdir+'/'+jName+'.sh')

   def Add (self,iComb,iModel,iMass,iTarget,iJob,command,iAltModel) :
     jName= self.jobsDic[iComb][iModel][iMass][iTarget][iAltModel][iJob]
     jFile = open(jobdir+'/'+jName+'.sh','a')
     jFile.write(command+'\n')
     jFile.close()

#     print jName,  command

   def Sub(self,queue='8nh'):
     os.system('cd '+jobdir)
     for jName in self.jobsList:
        errFile=jobdir+'/'+jName+'.err'
        outFile=jobdir+'/'+jName+'.out'
        jidFile=jobdir+'/'+jName+'.jid'
        jFile = open(jobdir+'/'+jName+'.sh','a')
        jFile.write('mv '+jidFile+' '+jidFile.replace('.jid','.done') )
        jFile.close()
        jidFile=jobdir+'/'+jName+'.jid'
        print 'Submit',jName
        jobid=os.system('cd '+jobdir+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName+'.sh | grep submitted > '+jidFile)

def batchResub():
    fileCmd = 'ls '+jobdir+'/'+'*.sh'
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    FileList=string.split(out)
    os.system('cd '+jobdir)
    for iFile in FileList:
      jidFile=iFile.replace('.sh','.jid')
      doneFile=iFile.replace('.sh','.done')
      if not ( os.path.isfile(jidFile) or os.path.isfile(doneFile) ) :
        print 'Resubmit',iFile
        errFile=iFile.replace('.sh','.err')
        outFile=iFile.replace('.sh','.out')
        jobid=os.system('cd '+jobdir+'; bsub -q 8nh -o '+outFile+' -e '+errFile+' '+iFile+' | grep submitted > '+jidFile)

def batchClean():
    fileCmd = 'ls '+jobdir+'/'+'*.sh'
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    FileList=string.split(out)
    for iFile in FileList:
      doneFile=iFile.replace('.sh','.done')
      if os.path.isfile(doneFile):
        cleanFile=iFile.replace('.sh','.*')
        print 'Clean',cleanFile
        os.system('cd '+jobdir+'; rm '+cleanFile)

def batchStatus():
    fileCmd = 'ls '+jobdir+'/'+'*.sh'
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    FileList=string.split(out)
    for iFile in FileList:
      jidFile=iFile.replace('.sh','.jid')
      if os.path.isfile(jidFile):
        print 'Status', jidFile
        os.system('cat '+jidFile+' | awk \'{print $2}\' | awk -F\'<\' \'{print $2}\' | awk -F\'>\' \'{print $1}\' | xargs -n 1 bjobs')  

