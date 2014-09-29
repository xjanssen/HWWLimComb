#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

import combTools
from Config import *
import batchTools
from manipDataCard import card as cardTools
from math import floor

parser = OptionParser(usage="usage: %prog [options] comb")

parser.add_option("-c", "--combs",      dest="combs",       help="Produce all combinations", default=[], type='string' , action='callback' , callback=combTools.list_maker('combs',','))
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-z", "--zip",        dest="zip",         help="compress output datacard", default=False, action="store_true")
parser.add_option("-M", "--models",     dest="models",      help="Physics Model (OneHiggs,TwoHiggs,NoModel , ... )", default=['OneHiggs'], type='string' , action='callback' , callback=combTools.list_maker('models',','))
parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-T", "--targets",    dest="targets",     help="What to do ( PVSObs, BestFit, ... )", default=[], type='string' , action='callback' , callback=combTools.list_maker('targets',','))
parser.add_option("-u", "--unblind",    dest="unblind",     help="Unblind results",                default=False, action="store_true")
parser.add_option("-b", "--batch"  ,    dest="runBatch",    help="Run in batch",                   default=False, action="store_true")
parser.add_option("-g", "--grid"   ,    dest="runGrid" ,    help="Run in  grid",                   default=False, action="store_true")
parser.add_option("-S", "--batchSplit", dest="batchSplit",  help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=combTools.list_maker('batchSplit',','))
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )
parser.add_option("-a", "--AltModel" ,  dest="AltModel",    help="Alternative models", default=['NONE'], type='string' , action='callback' , callback=combTools.list_maker('AltModel',','))
parser.add_option("-d", "--dictionary", dest="Dictionary",  help="Datacards Dictionary", default='Configs.HWW2012' , type='string' )
parser.add_option("-q", "--quiet",    dest="quiet",     help="Quiet logs",                default=False, action="store_true")

(options, args) = parser.parse_args()

# Read Combination python config
exec('from %s import *'%(options.Dictionary))
print DefaultVersion
if options.Version == 'None' : options.Version=DefaultVersion


print '==== Data Cards Version : ',options.Version

combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()
TargetList    = combTools.TargetList_Filter(targets,options.targets).get()

if options.runBatch or options.runGrid: 
  print 'Call BATV Tools Init'  
  jobs = batchTools.batchJobs(channels,combinations,'results',combList,energyList,PhysModelList,TargetList,options.batchSplit,options.masses,options.unblind,options.Version,options.AltModel,options.runGrid )

if options.runGrid:
  CrabDB = {}

#Run Combine
for iComb in combList:
    print '---------------------- Computing results for combination: '+iComb
    for iModel in PhysModelList:
      print '---------------------------> Model = '+iModel 
      cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
      massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.masses,iComb,energyList).get()
      if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
        TargetDir=workspace+'/'+options.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
        TargetDirGrid=workspace.split('/')[-2]+'/'+options.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
      else:
        TargetDir=workspace+'/'+options.Version+'/'+cardDir+'/'+iComb
        TargetDirGrid=workspace.split('/')[-2]+'/'+options.Version+'/'+cardDir+'/'+iComb
      print 'Target Dir : '+TargetDir
      print 'Masses List: '+str(massList)
      paramSet   = combTools.ParamSet_Maker(cardtypes,channels[options.Version],physmodels[iModel]['cardtype'],options.masses,'NONE',energyList).get()
      for iSet in range(0,len(paramSet['values'])) :
        iMass = paramSet['values'][iSet][0]
        print '------------------------------> Mass = '+str(iMass) + ' (Set: ' + str(paramSet['values'][iSet]) + ' )'       
        for iAltModel in options.AltModel:
          print '------------------------------> AltModel = '+iAltModel
          for iTarget in TargetList:
            wspace=iComb
            for iPar in range(1,len(paramSet['names'])) :
              parVal=str(paramSet['values'][iSet][iPar])
              parVal = parVal.replace('.','d')
              for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
              wspace += '_' + paramSet['names'][iPar] + '_' + parVal
            if options.energy != 0: wspace += '_' + str(options.energy) + 'TeV'
            if iAltModel != 'NONE' and 'AltModel' in targets[iTarget]  and targets[iTarget]['AltModel'] == 'Gen' : wspace += '_' + iAltModel 
            #else                  : wspace += '_78TeV' 
            wspace += '_'+iModel
            outname = '_'+wspace
            if iAltModel != 'NONE' and 'AltModel' in targets[iTarget]  and targets[iTarget]['AltModel'] == 'Use' : outname += '_Use-' + iAltModel 
            logbase = wspace
            wspace += '.root'   
            if os.path.exists(TargetDir+'/'+str(iMass)+'/'+wspace):
              if options.unblind or targets[iTarget]['notblind'] : 
                print '---------------------------------> Target = '+iTarget        
                # Many Jobs ?
                if 'NJobs' in targets[iTarget]:
                  NJobs = targets[iTarget]['NJobs']
                else:
                  NJobs = 1
                # Job Multiple parameter ?
                JobParamName=[]
                JobParamSize=[]
                NParam=1
                pTarget=iTarget
                if 'Toys' in targets[iTarget]: pTarget=targets[iTarget]['Toys']['Target']
                if 'JobsParam' in targets[pTarget]:
                  for iJobParam in targets[pTarget]['JobsParam']:
                    JobParamName.append(iJobParam)
                    JobParamSize.append(len(targets[pTarget]['JobsParam'][iJobParam])) 
                    NParam*=len(targets[pTarget]['JobsParam'][iJobParam]) 
                  NJobs=NJobs*NParam
                  print NParam, JobParamName , JobParamSize

                jJob=0
                for iParam in xrange(1,NParam+1):
                  # Toys ?
                  ToysList = []
                  TPF=''
                  if 'Toys' in targets[iTarget]: 
                    if 'JobsParam' in targets[pTarget] :
                      if len(JobParamSize) == 1:
                        iPar=iParam-1
                        TPF=TPF+'_'+JobParamName[0]+str(targets[pTarget]['JobsParam'][JobParamName[0]][iPar]).replace('.','d')
                        print TPF
                    if iAltModel != 'NONE' and 'AltModel' in targets[iTarget] and targets[iTarget]['AltModel'] == 'Use' :
                      ToysList = combTools.getToys(iComb,iTarget,options.energy,iMass,workspace,options.Version,cardtypes,physmodels,targets,iAltModel,TPF)
                    else:
                      ToysList = combTools.getToys(iComb,iTarget,options.energy,iMass,workspace,options.Version,cardtypes,physmodels,targets,'NONE',TPF)
                    NJobs=len(ToysList)
                    print   ToysList            
                  print NJobs
                for iJob in xrange(1,NJobs+1):
                    PF=''
                    subdir=''
                    if NJobs == 1 : logfile  = logbase+'_'+iTarget+TPF+'.mH'+str(iMass)+'.log' 
                    else          : 
                      logfile  = logbase+'_'+iTarget+TPF+'.mH'+str(iMass)+'_'+str(iJob)+'.log' 
                      if iAltModel != 'NONE' and 'AltModel' in targets[iTarget] and targets[iTarget]['AltModel'] == 'Use' :
                        logfile = logfile.replace(iTarget,iTarget+'_Use-'+iAltModel)
                      subdir = 'jobs'+str((iJob/250)*250)
                      os.system('mkdir -p '+TargetDir+'/'+str(iMass)+'/'+subdir) 
                    command =''
                    if not options.runGrid : command  += 'cd '+TargetDir+'/'+str(iMass)+'/'+subdir+' && '
                    command += 'combine '+TargetDir+'/'+str(iMass)+'/'+wspace+' -M '+targets[iTarget]['method']+' -m '+str(iMass)  #+' '+targets[iTarget]['options']
                    # Options
                    OPTS=targets[iTarget]['options']
                    if '$FitOptions' in OPTS:
                      print 'Using FitOptions: ' , FitOptions[FitOptDef]
                      FitOPTS=''
                      for iFitOpt in FitOptions[FitOptDef] : 
                        FitOPTS += ' '+iFitOpt
                      OPTS = OPTS.replace('$FitOptions',FitOPTS)
                    command += ' '+OPTS
                    # toys
                    if len(ToysList) > 0:
                      command += ' -t '+str(targets[iTarget]['Toys']['NToysJob'])+' --toysFile='+ToysList[iJob-1]+' -s '+os.path.splitext(os.path.splitext(ToysList[iJob-1])[0])[1].replace('.','')
                    # MultiDim Grid
                    if 'MDFGridParam' in targets[iTarget] :
                      NPJobs=int(targets[iTarget]['MDFGridParam']['NPOINTS']/NJobs)
                      FPoint=(iJob-1)*NPJobs
                      LPoint=(iJob)*NPJobs-1
                      command += ' --points='+str(targets[iTarget]['MDFGridParam']['NPOINTS'])
                      command += ' --firstPoint '+str(FPoint)+' --lastPoint '+str(LPoint)
                      #command += ' --rMin '+str(targets[iTarget]['MDFGridParam']['RMIN'])+' --rMax '+str(targets[iTarget]['MDFGridParam']['RMAX'])
                      PF='_Points'+str(FPoint)+'-'+str(LPoint)
                    # Job Multiple parameter
                    if 'JobsParam' in targets[iTarget] :
                      if len(JobParamSize) == 1:
                        #iPar=iParam-1
                        iPar=(iJob-1)/(targets[iTarget]['NJobs'])
                        #print iPar,iJob,JobParamSize[0],(iJob-1)/(targets[iTarget]['NJobs'])
                        print str(iJob), str(iPar) , JobParamName[0] , str(targets[iTarget]['JobsParam'][JobParamName[0]][iPar])
                        command=command.replace('$'+JobParamName[0],str(targets[iTarget]['JobsParam'][JobParamName[0]][iPar]))
                        PF=PF+'_'+JobParamName[0]+str(targets[iTarget]['JobsParam'][JobParamName[0]][iPar]).replace('.','d')
                      elif len(JobParamSize) == 2:  
                        iPar1=((iJob-1)/JobParamSize[0])%JobParamSize[0]
                        iPar2=(iJob-1)/(JobParamSize[0]*targets[iTarget]['NJobs'])
                        command=command.replace('$'+JobParamName[0],str(targets[iTarget]['JobsParam'][JobParamName[0]][iPar1]))
                        command=command.replace('$'+JobParamName[1],str(targets[iTarget]['JobsParam'][JobParamName[1]][iPar2]))
                        PF=PF+'_'+JobParamName[0]+str(targets[iTarget]['JobsParam'][JobParamName[0]][iPar1]).replace('.','d')
                        PF=PF+'_'+JobParamName[1]+str(targets[iTarget]['JobsParam'][JobParamName[1]][iPar2]).replace('.','d')
                      else : sys.exit() 
                    #  for iParam in range(0,len(JobsParam)):
                        
                    # Nuissance Freezing
                    if 'FreezeNuis' in targets[iTarget]:
                      toFreeze=[]
                      card=TargetDir+'/'+str(iMass)+'/'+iComb
                      if options.energy != 0: card += '_' + str(options.energy) + 'TeV'
                      if iAltModel != 'NONE' and 'AltModel' in targets[iTarget]  and targets[iTarget]['AltModel'] == 'Gen' : card += '_' + iAltModel 
                      card += ".txt"
                      dc = cardTools(card)  
                      #print dc.content['systs']
                      for iTF in targets[iTarget]['FreezeNuis']:
                        for iSystType in  dc.content['systs']: 
                          if targets[iTarget]['FreezeNuis'][iTF][0] ==  iSystType or  targets[iTarget]['FreezeNuis'][iTF][0] == '*' :
                            for iSyst in dc.content['systs'][iSystType]:
                              print iSystType , iSyst  
                              if targets[iTarget]['FreezeNuis'][iTF][1] in iSyst or  targets[iTarget]['FreezeNuis'][iTF][1]  == '*' :
                                print '-->Freeze'
                                toFreeze.append(iSyst)
                      if len(toFreeze) > 0 : command += ' --freezeNuisances '+toFreeze[0]
                      if len(toFreeze) > 1 : 
                        for iF in xrange(1,len(toFreeze) ): command += ','+toFreeze[iF]
  
                    # outfile
                    outname=outname
                    JobN = ''
                    if (NJobs) > 1 : JobN += '.job'+str(iJob)
                    command +=' -n '+outname+'_'+iTarget+PF+TPF+JobN
                    # logfile 
                    if options.quiet :
                      command += ' 2>&1 > /dev/null' 
                    else:
                      command += ' 2>&1 | tee '+logfile
                    jJob+=1
                    if options.pretend : print command
                    else :
                      if   options.runBatch:
                        print 'Add',iComb,iModel,iMass,iTarget,jJob,command,iAltModel
                        jobs.Add(iComb,iModel,iMass,iTarget,jJob,command,iAltModel) 
                      elif options.runGrid:
                        CrabDB[jJob] = {}
                        print str(iJob),' ',str(jJob)
                        print TargetDir+'/'+str(iMass)+'/'+wspace
                        print workspace.split('/')[-2]
                        print TargetDirGrid
                        print command 
                        CrabDB[jJob]['wspace']  = TargetDir+'/'+str(iMass)+'/'+wspace
                        CrabDB[jJob]['outdir']  = TargetDirGrid
                        CrabDB[jJob]['command'] = command
                        CrabDB[jJob]['files']   = []
                        gridWspace = TargetDir+'/'+str(iMass)+'/'+wspace
                        gridOutdir = TargetDirGrid
                        gridFiles  = []
                        jobs.AddGrid(iComb,iModel,iMass,iTarget,jJob,command,gridWspace,gridOutdir,gridFiles,iAltModel)
                      else:
                        os.system(command)
            else:
              print 'WARNING: Workspace does not exist : '+TargetDir+'/'+str(iMass)+'/'+wspace


if options.runBatch and not options.pretend: jobs.Sub()
if options.runGrid  and not options.pretend: jobs.SubCrab()

