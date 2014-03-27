#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

import combTools
import combPlots
from Config import *
from copy import deepcopy as dc

# --------------------------------------------------------- getAllMass ------------------------

def getAllMass(iModel,combList,Version):
   allList = []
   for iComb in combList:
      massList  = combTools.MassList_Filter(cardtypes,channels[Version],combinations,physmodels[iModel]['cardtype'],[],iComb,energyList).get()
      allList.extend(massList)
   return  sorted(list(set(allList)))

# --------------------------------------------------------- MAIN ------------------------

parser = OptionParser(usage="usage: %prog [options] comb")

parser.add_option("-c", "--combs",      dest="combs",       help="Produce all combinations", default=[], type='string' , action='callback' , callback=combTools.list_maker('combs',','))
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-M", "--models",     dest="models",      help="Physics Model (OneHiggs,TwoHiggs,NoModel , ... )", default=['OneHiggs'], type='string' , action='callback' , callback=combTools.list_maker('models',','))
parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-L", "--lumi",       dest="lumi",        help="Luminosity",                     type="float", default="0", metavar="Lumi")
parser.add_option("-m", "--mrange",     dest="mrange",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('mrange',',',float))
parser.add_option("-p", "--plots",      dest="plots",       help="What to do "             , default=[], type='string' , action='callback' , callback=combTools.list_maker('plots',','))
parser.add_option("-u", "--unblind",    dest="unblind",     help="Unblind results",          default=True, action="store_false")
parser.add_option("-i", "--inject",     dest="inject",      help="Inject mH=125",          default=False, action="store_true")
parser.add_option("-f", "--postfix",    dest="postFix",     help="Figure post-fix",        default='', metavar="PATTERN")
parser.add_option("-x", "--logx"   ,    dest="logx",        help="logX",                   default=False, action="store_true")
parser.add_option("-y", "--logy"   ,    dest="logy",        help="logY",                   default=False, action="store_true")
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version"     , default=DefaultVersion ,  type='string' )
parser.add_option("-P", "--printList",  dest="printList",   help="What to print "        , default=['ACLsObs','ACLsExp','SObs','SExpPre'], type='string' , action='callback' , callback=combTools.list_maker('printList',','))
parser.add_option("-a", "--AltModel" ,  dest="AltModel",    help="Alternative models", default=['NONE'], type='string' , action='callback' , callback=combTools.list_maker('AltModel',','))
parser.add_option("-d", "--dictionary", dest="Dictionary",  help="Datacards Dictionary", default='Configs.HWW2012' , type='string' )

(options, args) = parser.parse_args()

# Read Combination python config
exec('from %s import *'%(options.Dictionary))
print DefaultVersion
if options.Version == 'None' : options.Version=DefaultVersion


# Luminosity/Title #
if options.lumi == 0:
  if options.energy == 0  : iLumi=0
  if options.energy == 7  : iLumi=1
  if options.energy == 8  : iLumi=2
  if options.energy == 13 : iLumi=3
  else: iLumi=0
else:
  if options.energy == 13:
    if options.lumi == 30  : iLumi=3
    if options.lumi == 120 : iLumi=4
  else:
    if options.energy == 0  : iLumi=0
    if options.energy == 7  : iLumi=1
    if options.energy == 8  : iLumi=2
    else: iLumi=0
if options.combs[0] == 'HWW30ifb' :  iLumi=3
if options.combs[0] == 'HWW120ifb' :  iLumi=4
if iLumi >= 3 : iTitle=2
else          : iTitle=1 #Set to 0 for preliminary !
if options.combs[0] == 'HWW78TeV' : iTitle=2

print '==== Data Cards Version : ',options.Version
if options.combs[0] == 'HWW2l3l' : options.combs=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape','hww_vh3l_vh2j_zh3l2j_shape']
if options.combs[0] == 'HWW78TeV': options.combs=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape','hww_vh3l_vh2j_zh3l2j_shape']
if options.combs[0] == 'HWW30ifb' : options.combs=['hww012j_vh3l_vh2j_zh3l2j_30ifb','hww01jet_30ifb','hww2j_30ifb','hwwvh2j_30ifb','vh3l_30ifb','zh3l2j_30ifb','hww_vh3l_vh2j_zh3l2j_30ifb']
if options.combs[0] == 'HWW120ifb' : options.combs=['hww012j_vh3l_vh2j_zh3l2j_120ifb','hww01jet_120ifb','hww2j_120ifb','hwwvh2j_120ifb','vh3l_120ifb','zh3l2j_120ifb','hww_vh3l_vh2j_zh3l2j_120ifb']
if options.combs[0] == 'EWKCP2' : options.combs=['of_cp2_1d0','of_cp2_0d9','of_cp2_0d8','of_cp2_0d7','of_cp2_0d6','of_cp2_0d5','of_cp2_0d4','of_cp2_0d3','of_cp2_0d2','of_cp2_0d1']
'hww01jof_shape','of_oldcps','of_newcps'
combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()
postFix       = options.postFix

for iPlot in options.plots:
   print '---------------------- Making plot: '+iPlot 

   #
   # Plot with single iComb,iModel
   #
   if   iPlot in ['Limit','Sign','BestFit','PVal','Print']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       for iComb in combList:
          print '------------------------------> Comb = '+iComb
          massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],[],iComb,energyList).get()
          if (len(options.mrange) >= 2 ) : 
            mLF = [X for X in massList  if (X >= options.mrange[0] and X <= options.mrange[1])]
            postFix += '_mH'+str(options.mrange[0]).replace('.','d')+'-'+str(options.mrange[1]).replace('.','d')
          else                           : mLF = massList
          plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix,options.logx,options.logy)
          if iPlot == 'Limit'   : plot.plotOneLimit(iComb,options.energy,iModel,mLF,options.inject)
          if iPlot == 'Sign'    : plot.plotSignVsMh(iComb,options.energy,iModel,mLF,options.inject)
          if iPlot == 'BestFit' : plot.plotMuVsMh(iComb,options.energy,iModel,mLF)
          if iPlot == 'Print'   : plot.printResults(iComb,options.energy,iModel,mLF,options.printList)

   #
   # Plot with single iModel and several Comb
   #
   elif iPlot in ['ExpLim','ExpSign']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       massList=dc(getAllMass(iModel,combList,options.Version))
       if (len(options.mrange) >= 2 ) : 
         mLF = [X for X in massList  if (X >= options.mrange[0] and X <= options.mrange[1])]
         postFix += '_mH'+str(options.mrange[0])+'-'+str(options.mrange[1])
       else                           : mLF = massList
       plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix,options.logx,options.logy)
       if iPlot == 'ExpLim'  : plot.plotExpLimits(combList,options.energy,iModel,mLF)
       if iPlot == 'ExpSign' : plot.plotExpSignVsMh(combList,options.energy,iModel,mLF)

   #
   # Channel compatibility
   #
   elif iPlot in ['MuCC','SCC','LimCC']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix,options.logx,False,iTitle,iLumi)
       #CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape']
       #CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape']
       CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','vh3l_shape','hwwvh2j_cut','hww2j_shape','hww01jet_shape','zh3l2j_shape']
       if options.combs[0] == 'hww012j_vh3l_vh2j_zh3l2j_30ifb'  : CombList=['hww012j_vh3l_vh2j_zh3l2j_30ifb','vh3l_30ifb','hwwvh2j_30ifb','hww2j_30ifb','hww01jet_30ifb','zh3l2j_30ifb']
       if options.combs[0] == 'hww012j_vh3l_vh2j_zh3l2j_120ifb'  : CombList=['hww012j_vh3l_vh2j_zh3l2j_120ifb','vh3l_120ifb','hwwvh2j_120ifb','hww2j_120ifb','hww01jet_120ifb','zh3l2j_120ifb']
       #if options.combs[0] == 'hww012j_vh3l_vh2j_zh3l2j_30ifb'  : CombList=['hww012j_vh3l_vh2j_zh3l2j_30ifb','hww01jet_30ifb','hww2j_30ifb','hwwvh2j_30ifb','vh3l_30ifb','zh3l2j_30ifb']
       #if options.combs[0] == 'hww012j_vh3l_vh2j_zh3l2j_120ifb' : CombList=['hww012j_vh3l_vh2j_zh3l2j_120ifb','hww01jet_120ifb','hww2j_120ifb','hwwvh2j_120ifb','vh3l_120ifb','zh3l2j_120ifb']

       if  iPlot == 'MuCC' : plot.plotMuChannel(CombList,options.energy,iModel,[125.6]) 
       if  iPlot == 'SCC'  : plot.plotSignChannel(CombList,options.energy,iModel,[125.6]) 
       if  iPlot == 'LimCC': plot.plotLimitChannel(CombList,options.energy,iModel,[125.6]) 

   #
   # 2D MutliDim Fits
   #
   elif iPlot in ['MDFSum','MDFSumFast','MDF1D','MDF2D','MDF2DFast']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel
       for iComb in combList:
         print '------------------------------> Comb = '+iComb
         massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.mrange,iComb,energyList).get() 
         for iMass in massList:
           bSimple=True
           plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix,False,False,iTitle,iLumi)
           if iPlot == 'MDFSum'    : plot.MDF2DSum(iComb,options.energy,iModel,[iMass],False) 
           if iPlot == 'MDFSumFast': plot.MDF2DSum(iComb,options.energy,iModel,[iMass],True) 
           if iPlot == 'MDF1D'     : plot.MDF1D(iComb,options.energy,iModel,[iMass],False) 
           if iPlot == 'MDF2D'     : plot.MDF2D(iComb,options.energy,iModel,[iMass],bSimple,False)
           if iPlot == 'MDF2DFast' : plot.MDF2D(iComb,options.energy,iModel,[iMass],bSimple,True)
   #
   # JCP
   #
   elif iPlot in ['JCPSum','JCPFit','JCPPlot']:
      for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel
       for iComb in combList:
         print '------------------------------> Comb = '+iComb
         massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.mrange,iComb,energyList).get() 
         for iMass in massList:
           plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix)
           if iPlot == 'JCPSum'    : plot.JCPSum(iComb,options.energy,iModel,[iMass]) 
           if iPlot == 'JCPFit'    : plot.JCPFit(iComb,options.energy,iModel,[iMass]) 
           if iPlot == 'JCPPlot'   : plot.JCPPlt(iComb,options.energy,iModel,[iMass]) 
 
   #
   # Mu-mH Scan: Sum disjunct mH 1D mu scan
   #
   elif iPlot in ['MUMHSum','MHFit']:
      for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel
       for iComb in combList:
         print '------------------------------> Comb = '+iComb
         massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.mrange,iComb,energyList).get()     
         plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix)
         if iPlot == 'MUMHSum'   : plot.MUMHSum(iComb,options.energy,iModel,massList)
         muVal = 1.0 
         if iPlot == 'MHFit'     : plot.MHFit(iComb,options.energy,iModel,muVal)  

   #
   # Mu-mH Scan: Sum disjunct mH 1D mu scan
   #
   elif iPlot in ['MLToysBB']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel
       for iComb in combList:
         print '------------------------------> Comb = '+iComb
         massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.mrange,iComb,energyList).get()        
         plot=combPlots.combPlot(channels,combinations,options.Version,options.unblind,postFix)
         plot.MLToysBB(combList,options.energy,iModel,massList,options.AltModel)

   else:
     print 'ERROR: Unknown plot !'
     sys.exit(1)

