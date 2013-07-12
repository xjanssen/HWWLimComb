#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

import combTools
import combPlots
from Config import *
from copy import deepcopy as dc

# --------------------------------------------------------- getAllMass ------------------------

def getAllMass(iModel,combList):
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
parser.add_option("-m", "--mrange",     dest="mrange",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('mrange',',',int))
parser.add_option("-p", "--plots",      dest="plots",       help="What to do "             , default=[], type='string' , action='callback' , callback=combTools.list_maker('plots',','))
parser.add_option("-u", "--unblind",    dest="unblind",     help="Unblind results",          default=True, action="store_false")
parser.add_option("-i", "--inject",     dest="inject",      help="Inject mH=125",          default=False, action="store_true")
parser.add_option("-f", "--postfix",    dest="postFix",     help="Figure post-fix",        default='', metavar="PATTERN")
parser.add_option("-x", "--logx"   ,    dest="logx",        help="logX",                   default=False, action="store_true")
parser.add_option("-y", "--logy"   ,    dest="logy",        help="logY",                   default=False, action="store_true")
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default="V1" ,  type='string' )

(options, args) = parser.parse_args()

print '==== Data Cards Version : ',options.Version

combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()
postFix       = options.postFix

for iPlot in options.plots:
   print '---------------------- Making plot: '+iPlot 

   #
   # Plot with single iComb,iModel
   #
   if   iPlot in ['Limit','Sign','BestFit','PVal']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       for iComb in combList:
          print '------------------------------> Comb = '+iComb
          massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],[],iComb,energyList).get()
          if (len(options.mrange) >= 2 ) : 
            mLF = [X for X in massList  if (X >= options.mrange[0] and X <= options.mrange[1])]
            postFix += '_mH'+str(options.mrange[0])+'-'+str(options.mrange[1])
          else                           : mLF = massList
          plot=combPlots.combPlot(options.unblind,options.Version,postFix,options.logx,options.logy)
          if iPlot == 'Limit'   : plot.plotOneLimit(iComb,options.energy,iModel,mLF,options.inject)
          if iPlot == 'Sign'    : plot.plotSignVsMh(iComb,options.energy,iModel,mLF,options.inject)
          if iPlot == 'BestFit' : plot.plotMuVsMh(iComb,options.energy,iModel,mLF)

   #
   # Plot with single iModel and several Comb
   #
   elif iPlot in ['ExpLim','ExpSign']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       massList=dc(getAllMass(iModel,combList))
       if (len(options.mrange) >= 2 ) : 
         mLF = [X for X in massList  if (X >= options.mrange[0] and X <= options.mrange[1])]
         postFix += '_mH'+str(options.mrange[0])+'-'+str(options.mrange[1])
       else                           : mLF = massList
       plot=combPlots.combPlot(options.unblind,options.Version,postFix,options.logx,options.logy)
       if iPlot == 'ExpLim'  : plot.plotExpLimits(combList,options.energy,iModel,mLF)
       if iPlot == 'ExpSign' : plot.plotExpSignVsMh(combList,options.energy,iModel,mLF)
 
   elif iPlot in ['MuCC']:
     for iModel in PhysModelList:
       print '---------------------------> Model = '+iModel 
       plot=combPlots.combPlot(options.unblind,options.Version,postFix)
       plot.plotMuChannel() 


   else:
     print 'ERROR: Unknown plot !'
     sys.exit(1)

