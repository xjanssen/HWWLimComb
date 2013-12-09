#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess

#---
class list_maker:
    def __init__(self, var, sep=',', type=None ):
        self._type= type
        self._var = var
        self._sep = sep

    def __call__(self,option, opt_str, value, parser):
        if not hasattr(parser.values,self._var):
               setattr(parser.values,self._var,[])

        try:
           array = value.split(self._sep)
           if self._type:
               array = [ self._type(e) for e in array ]
           setattr(parser.values, self._var, array)

        except:
           print 'Malformed option (comma separated list expected):',value

#--- channelList Filter
class ChannelList_Filter:
    def __init__(self, channels , channelFilter):
        self.channels      = channels
        self.channelFilter = channelFilter
        self.channelList   = []
        self.found      = False
        if len(self.channelFilter) == 0:
          self.found    = True
          self.channelList = [X for X in self.channels ]  
        else:
          self.channelList = [X for X in self.channelFilter if (X in self.channels)]    
          if  len(self.channelList):  self.found    = True 

    def get(self):
        if not self.found:
          print 'Unknown combination : '
          print self.channelFilter
          sys.exit(2)
        else:      
          return self.channelList



#--- CombList Filter
class CombList_Filter:
    def __init__(self, combinations , combFilter):
        self.combinations = combinations
        self.combFilter   = combFilter
        self.combList     = [] 
        self.found        = False
        if len(self.combFilter) == 0:
          self.found    = True
          self.combList = [X for X in self.combinations ]    
        else:
          #self.combList = [X for X in self.combinations if (X in self.combFilter)]    
          self.combList = [X for X in self.combFilter if (X in self.combinations)]    
          if  len(self.combList):  self.found    = True 

    def get(self):
        if not self.found:
          print 'Unknown combination : '
          print self.combFilter
          sys.exit(2)
        else:      
          return self.combList


#--- CardDir Filter
class CardDir_Filter:
    def __init__(self, cardtypes , purpose):
        self.cardtypes  = cardtypes
        self.purpose    = purpose
        self.found      = False
        self.CardDir    = ""
        for iPurpose in self.cardtypes: 
           if iPurpose == self.purpose:
             self.found   = True
             self.CardDir = self.cardtypes[iPurpose]['dir'] 

    def get(self):
        if not self.found:
          print 'Unknown purpose : '+self.purpose 
          sys.exit(2)
        else:      
          return self.CardDir

#--- Mass List Filter
class MassList_Filter:
    def __init__(self, cardtypes , channels , combinations , purpose , massFilter, iComb, energyList):
        self.cardtypes  = cardtypes
        self.purpose    = purpose
        self.massFilter = massFilter
        self.massList   = []
        self.found      = False
        for iPurpose in self.cardtypes: 
           if iPurpose == self.purpose:
             self.found = True
             massMin = 9999999
             massMax = 0
             for iChannel in combinations[iComb]['channels'] : 
               for iEnergy in energyList :
                  if iEnergy in channels[iChannel]:
                    #print iChannel, iEnergy, channels[iChannel][iEnergy]['mrange'] 
                    if channels[iChannel][iEnergy]['mrange'][0] < massMin : massMin = channels[iChannel][iEnergy]['mrange'][0]
                    if channels[iChannel][iEnergy]['mrange'][1] > massMax : massMax = channels[iChannel][iEnergy]['mrange'][1]
             #print massMin, massMax
             if len(self.massFilter) == 0:
               self.massList=[X for X in self.cardtypes[iPurpose]['masses'] if ( X >= massMin and X<= massMax ) ]
             else:
               self.massList=[X for X in self.cardtypes[iPurpose]['masses'] if ( (X >= massMin and X<= massMax) and (X in self.massFilter) )]

    def get(self):
        if not self.found:
          print 'Unknown purpose : '+self.purpose
          sys.exit(2)
        else:      
          return self.massList               

#--- Mass List Filter
class MassList_Filter_Chann:
    def __init__(self, cardtypes , channels , purpose , massFilter, iChannel , energyList):
        self.cardtypes  = cardtypes
        self.purpose    = purpose
        self.massFilter = massFilter
        self.massList   = []
        self.found      = False
        for iPurpose in self.cardtypes: 
           if iPurpose == self.purpose:
             self.found = True
             massMin = 9999999
             massMax = 0
             #for iChannel in combinations[iComb]['channels'] : 
             for iEnergy in energyList :
               if iEnergy in channels[iChannel]:
                    #print iChannel, iEnergy, channels[iChannel][iEnergy]['mrange'] 
                    if channels[iChannel][iEnergy]['mrange'][0] < massMin : massMin = channels[iChannel][iEnergy]['mrange'][0]
                    if channels[iChannel][iEnergy]['mrange'][1] > massMax : massMax = channels[iChannel][iEnergy]['mrange'][1]
             #print massMin, massMax
             if len(self.massFilter) == 0:
               self.massList=[X for X in self.cardtypes[iPurpose]['masses'] if ( X >= massMin and X<= massMax ) ]
             else:
               self.massList=[X for X in self.cardtypes[iPurpose]['masses'] if ( (X >= massMin and X<= massMax) and (X in self.massFilter) )]

    def get(self):
        if not self.found:
          print 'Unknown purpose : '+self.purpose
          sys.exit(2)
        else:      
          return self.massList           

#--- energy List
class EnergyList_Filter:
    def __init__(self, iEnergy ):
        self.iEnergy    = iEnergy
        self.energyList = []
        if   self.iEnergy == 7 :
          self.energyList = ['7TeV']
        elif self.iEnergy == 8 :
          self.energyList = ['8TeV']
        elif self.iEnergy == 0 :
          self.energyList = ['7TeV','8TeV']
        elif  self.iEnergy == 13 :
          self.energyList = ['13TeV']
        else:
          print 'Unknown Energy !!!!'
          sys.exit(2)
     
    def get(self):
        return self.energyList


#--- PhysModelList Filter
class PhysModelList_Filter:
    def __init__(self, physmodels , modFilter):
        self.physmodels    = physmodels
        self.modFilter     = modFilter
        self.found         = False
        self.PhysModelList = []

        if len(self.modFilter) == 0:
          self.found         = True
          self.PhysModelList = [X for X in self.physmodels ]    
        else:
          self.PhysModelList = [X for X in self.physmodels  if (X in self.modFilter)]    
          if  len(self.PhysModelList):  self.found    = True 

    def get(self):
        if not self.found:
          print 'Unknown combination : '
          print self.modFilter
          sys.exit(2)
        else:      
          return self.PhysModelList


#--- TargetList Filter
class TargetList_Filter:
    def __init__(self, targets , targetFilter):
        self.targets      = targets
        self.targetFilter = targetFilter
        self.found        = False
        self.TargetList   = []

        if len(self.targetFilter) == 0:
          self.found         = True
          self.TargetList = [X for X in self.targets ]    
        else:
          self.TargetList = [X for X in self.targets  if (X in self.targetFilter)]    
          if  len(self.TargetList):  self.found    = True 

    def get(self):
        if not self.found:
          print 'Unknown combination : '
          print self.targetFilter
          sys.exit(2)
        else:      
          return self.TargetList

# ---- Toys List
def getToys(iComb,iTarget,iEnergy,iMass,workspace,Version,cardtypes,physmodels,targets,AltMod='NONE'):
    ToysList=[]
    if not 'Toys' in targets[iTarget]: return ToysList

    iModel=targets[iTarget]['Toys']['Model']
    cardDir   = CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()  
    if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
      toysDir=workspace+'/'+Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb+'/'+str(iMass)
    else:
      toysDir=workspace+'/'+Version+'/'+cardDir+'/'+iComb+'/'+str(iMass)
    print toysDir
    Energy=''
    if iEnergy == 7 : Energy = '_7TeV'
    if iEnergy == 8 : Energy = '_8TeV'
    if AltMod == 'NONE' : toyname='_'+iComb+Energy+'_'+iModel+'_'+targets[iTarget]['Toys']['Target']+'.job*.'+targets[targets[iTarget]['Toys']['Target']]['method']+'.mH'+str(iMass)+'.*.root'
    else                : toyname='_'+iComb+Energy+'_'+AltMod+'_'+iModel+'_'+targets[iTarget]['Toys']['Target']+'.job*.'+targets[targets[iTarget]['Toys']['Target']]['method']+'.mH'+str(iMass)+'.*.root'
 
    command='ls '+toysDir+'/higgsCombine'+toyname
    print command
    proc=subprocess.Popen(command, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    ToysList=string.split(out)

    return ToysList
