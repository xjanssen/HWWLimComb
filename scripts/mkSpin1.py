#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

from array import array
import ROOT
from ROOT import *

import combTools
import batchTools

from Config import *
from manipDataCard import card as cardTools
from copy import deepcopy 

TargetDir = '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1hzzlike/'
Config    = {  
              'hwwof_0j_7TeV.txt' : { '1p' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1p/' , '1m' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1m/' }  ,
              'hwwof_1j_7TeV.txt' : { '1p' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1p/' , '1m' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1m/' }  ,
              'hwwof_0j_8TeV.txt' : { '1p' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1p/' , '1m' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1m/' }  ,
              'hwwof_1j_8TeV.txt' : { '1p' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1p/' , '1m' : '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/V4/jcp/1m/' }
            }



for iComb in Config:

  dc1p =   cardTools(Config[iComb]['1p']+iComb)
  dc1m =   cardTools(Config[iComb]['1m']+iComb)
  dcOut =  cardTools(Config[iComb]['1m']+iComb)

  # Copy 1p to ggH_ALT2
  dcOut.addCol(  dc1p.content['block2']['bin'][1] , 'ggH_ALT2' , -6 , dc1p.content['block2']['rate'][1] , dc1p.content['block1']['observation'][0] )
  #print dcOut.content['block1']  
  #print dcOut.content['block2'] 

  # Set systematics
  for iType in dc1p.content['systs'] : 
    #print iType
    for iSyst in dc1p.content['systs'][iType]:
      #print iSyst, dc1p.getSyst( bin=dc1p.content['block2']['bin'][1] , process='ggH_ALT' , syst=iType , tag=iSyst ) 
      if not 'StatBound' in iSyst:
        dcOut.setSyst( bin=dc1p.content['block2']['bin'][1] , process='ggH_ALT2' , syst=iType , tag=iSyst , value=dc1p.getSyst( bin=dc1p.content['block2']['bin'][1] , process='ggH_ALT' , syst=iType , tag=iSyst ) )
      elif 'ggH_ALT' in iSyst:
        dcOut.addSystLine( systtype=iType , tag=iSyst.replace('ggH_ALT','ggH_ALT2') )
        dcOut.setSyst( bin=dc1p.content['block2']['bin'][1] , process='ggH_ALT2' , syst=iType , tag=iSyst.replace('ggH_ALT','ggH_ALT2') , value=dc1p.getSyst( bin=dc1p.content['block2']['bin'][1] , process='ggH_ALT' , syst=iType , tag=iSyst ) )

  os.system('mkdir -p '+TargetDir) 
  os.system('rm '+TargetDir+iComb) 
  dcOut.write(TargetDir+iComb)

  # Also make root file OFC

  os.system(' cp '+Config[iComb]['1m']+dc1m.content['header2']['0'][3]+' '+TargetDir)

  fIn  = TFile.Open(Config[iComb]['1p']+dc1p.content['header2']['0'][3],'READ')
  fOut = TFile.Open(TargetDir+dc1m.content['header2']['0'][3],'UPDATE')
  Hists = [X.GetName() for X in fIn.GetListOfKeys()]
  for iHist in Hists :
    if 'ggH_ALT' in iHist:
      print iHist
      H = fIn.Get(iHist).Clone(iHist.replace('ggH_ALT','ggH_ALT2'))
      H.SetTitle(iHist.replace('ggH_ALT','ggH_ALT2'))
      print H
      fOut.cd()
      H.Write()

  fIn.Close()
  fOut.Close()



