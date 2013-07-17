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
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-b", "--batch"  ,    dest="runBatch",    help="Run in batch",                   default=False, action="store_true")
parser.add_option("-S", "--batchSplit", dest="batchSplit",  help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=combTools.list_maker('batchSplit',','))
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )


(options, args) = parser.parse_args()

print '==== Data Cards Version : ',options.Version
combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()

if options.runBatch: jobs = batchTools.batchJobs("workspace",combList,energyList,PhysModelList,['None'],options.batchSplit,options.masses,True,options.Version)

# Build combinations
for iComb in combList:
    print '---------------------- Building WorkSpace for combination: '+iComb
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
        card=iComb
        if options.energy != 0: card += '_' + str(options.energy) + 'TeV'
        outname  = card+'_'+iModel+'.root'
        card += ".txt"
        if options.zip: card += ".gz"
        if os.path.exists(TargetDir+'/'+str(iMass)+'/'+card):
          command  = 'cd '+TargetDir+'/'+str(iMass)+' && '
          command += 'text2workspace.py '+card+' -m '+str(iMass)
          if 'model' in physmodels[iModel] :  command += ' -P '+physmodels[iModel]['model']
          command += ' -o '+outname
          if options.pretend: 
            print command
          else: 
            if not options.runBatch:
              os.system(command)
            else:
              jobs.Add(iComb,iModel,iMass,'None',1,command) 
        else:
          print 'WARNING: Card does not exist : '+TargetDir+'/'+str(iMass)+'/'+card

if options.runBatch: jobs.Sub()
