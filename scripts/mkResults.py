#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

import combTools
from Config import *
import batchTools

parser = OptionParser(usage="usage: %prog [options] comb")

parser.add_option("-c", "--combs",      dest="combs",       help="Produce all combinations", default=[], type='string' , action='callback' , callback=combTools.list_maker('combs',','))
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-z", "--zip",        dest="zip",         help="compress output datacard", default=False, action="store_true")
parser.add_option("-M", "--models",     dest="models",      help="Physics Model (OneHiggs,TwoHiggs,NoModel , ... )", default=['OneHiggs'], type='string' , action='callback' , callback=combTools.list_maker('models',','))
parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',int))
parser.add_option("-T", "--targets",    dest="targets",     help="What to do ( PVSObs, BestFit, ... )", default=[], type='string' , action='callback' , callback=combTools.list_maker('targets',','))
parser.add_option("-u", "--unblind",    dest="unblind",     help="Unblind results",                default=False, action="store_true")
parser.add_option("-b", "--batch"  ,    dest="runBatch",    help="Run in batch",                   default=False, action="store_true")
parser.add_option("-S", "--batchSplit", dest="batchSplit",  help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=combTools.list_maker('batchSplit',','))
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default="V1" ,  type='string' )


(options, args) = parser.parse_args()

print '==== Data Cards Version : ',options.Version

combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()
TargetList    = combTools.TargetList_Filter(targets,options.targets).get()

if options.runBatch: jobs = batchTools.batchJobs("results",combList,energyList,PhysModelList,TargetList,options.batchSplit,options.masses,options.unblind,options.Version)

#Run Combine
for iComb in combList:
    print '---------------------- Computing results for combination: '+iComb
    for iModel in PhysModelList:
      print '---------------------------> Model = '+iModel 
      cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
      massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.masses,iComb,energyList).get()
      if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
        TargetDir=workspace+'/'+options.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
      else:
        TargetDir=workspace+'/'+options.Version+'/'+cardDir+'/'+iComb
      print 'Target Dir : '+TargetDir
      print 'Masses List: '+str(massList)
      for iMass in massList:
        print '------------------------------> Mass = '+str(iMass)        
        wspace=iComb
        if options.energy != 0: wspace += '_' + str(options.energy) + 'TeV'
        #else                  : wspace += '_78TeV' 
        wspace += '_'+iModel
        outname = '_'+wspace
        logbase = wspace
        wspace += '.root' 
        if os.path.exists(TargetDir+'/'+str(iMass)+'/'+wspace):
          
          for iTarget in TargetList:
            if options.unblind or targets[iTarget]['notblind'] : 
              print '---------------------------------> Target = '+iTarget        
              # Many Jobs ?
              if 'NJobs' in targets[iTarget]:
                NJobs = targets[iTarget]['NJobs']
              else:
                NJobs = 1
              # Toys ?
              ToysList = []
              if 'Toys' in targets[iTarget]: 
                ToysList = combTools.getToys(iComb,iTarget,iMass,workspace,options.Version,cardtypes,physmodels,targets)
                NJobs=len(ToysList)
              
              for iJob in xrange(1,NJobs+1):
                if NJobs == 1 : logfile  = logbase+'_'+iTarget+'.mH'+str(iMass)+'.log' 
                else          : logfile  = logbase+'_'+iTarget+'.mH'+str(iMass)+'_'+str(iJob)+'.log' 
                command  = 'cd '+TargetDir+'/'+str(iMass)+' && '
                command += 'combine '+wspace+' -M '+targets[iTarget]['method']+' -n '+outname+'_'+iTarget+' -m '+str(iMass)+' '+targets[iTarget]['options']
                if len(ToysList) > 0:
                  command += ' -t '+str(targets[iTarget]['Toys']['NToysJob'])+' --toysFile='+ToysList[iJob-1]+' -s '+os.path.splitext(os.path.splitext(ToysList[iJob-1])[0])[1].replace('.','')
                command += ' 2>&1 | tee '+logfile
                if options.pretend: 
                  print command
                else: 
                  if not options.runBatch:
                    os.system(command)
                  else:
                    jobs.Add(iComb,iModel,iMass,iTarget,iJob,command) 
        else:
          print 'WARNING: Workspace does not exist : '+TargetDir+'/'+str(iMass)+'/'+wspace


if options.runBatch: jobs.Sub()
