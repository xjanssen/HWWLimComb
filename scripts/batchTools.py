#!/usr/bin/env python
import sys, re, os, os.path

from Config import *
import combTools

class batchJobs :
   def __init__ (self,prefix,combList,energyList,PhysModelList,TargetList,batchSplit,masses,unblind,Version):
      self.jobsDic={}
      self.jobsList=[]
      self.prefix=prefix
      if self.prefix != '' : self.prefix+='__'
      for iComb in combList:
        if not 'Comb' in batchSplit and len(combList)>1 :
          kComb = 'AllComb'
        else:
          kComb = iComb 
        self.jobsDic[iComb] = {}
        # Model Split ?
        for iModel in PhysModelList:
          if not 'Model' in batchSplit and len(PhysModelList)>1 :    
            kModel = 'AllModel'
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
                else:
                  kTarget = iTarget
                # More than one job ?
                self.jobsDic[iComb][iModel][iMass][iTarget] = {}
                if iTarget in targets and 'NJobs' in targets[iTarget]:
                  NJobs = targets[iTarget]['NJobs']
                else:
                  NJobs = 1 
                # Toys ?
                ToysList = []
                if iTarget in targets:
                  if 'Toys' in targets[iTarget]: 
                    ToysList = combTools.getToys(iComb,iTarget,iMass,workspace,Version,cardtypes,physmodels,targets)
                    NJobs=len(ToysList)
                for iJob in xrange(1,NJobs+1):        
                  jName = self.prefix+kComb+'__'+kModel+'__'+kMass+'__'+kTarget+'__'+str(iJob)
                  self.jobsDic[iComb][iModel][iMass][iTarget][iJob] = jName
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

   def Add (self,iComb,iModel,iMass,iTarget,iJob,command) :
     jName= self.jobsDic[iComb][iModel][iMass][iTarget][iJob]
     jFile = open(jobdir+'/'+jName+'.sh','a')
     jFile.write(command+'\n')
     jFile.close()

#     print jName,  command

   def Sub(self):
     os.system('cd '+jobdir)
     for jName in self.jobsList:
        errFile=jobdir+'/'+jName+'.err'
        outFile=jobdir+'/'+jName+'.out'
        jidFile=jobdir+'/'+jName+'.jid'
        jFile = open(jobdir+'/'+jName+'.sh','a')
        jFile.write('mv '+jidFile+' '+jidFile.replace('.jid','.done') )
        jFile.close()
        jidFile=jobdir+'/'+jName+'.jid'
        jobid=os.system('cd '+jobdir+'; bsub -q 8nh -o '+outFile+' -e '+errFile+' '+jName+'.sh | grep submitted > '+jidFile)




