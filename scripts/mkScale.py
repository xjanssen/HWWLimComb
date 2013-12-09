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

# ----------------------------------------------------- Read YR values from combination area --------------

def file2map(x): 
        ret = {}; headers = []
        for x in open(x,"r"):
            cols = x.split()
            if len(cols) < 2: continue
            if "mH" in x: 
                headers = [i.strip() for i in cols[1:]]
            else:
                fields = [ float(i) for i in cols ]
                ret[fields[0]] = dict(zip(headers,fields[1:]))
        return ret

# ------------------------------------------------------- MASS Extrapolation ------------------------------

def ExtrapolateMass(iChannel,iEnergy,card,TargetCard,iMass,iMassExtra):
    #print 'ExtrapolateMass: ',iChannel,card,TargetCard,iMass,iMassExtra

    dcIn  = cardTools(card)
    dcOut = cardTools(card)
     
    print channels[options.Version][iChannel][iEnergy]
 
    # Load YR Data 
    #path   = os.environ['CMSSW_BASE']+"/src/HiggsAnalysis/CombinedLimit/data/"
    path   = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/CMSSW_6_1_1'+'/src/HiggsAnalysis/CombinedLimit/data/'
    xs_ggH = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-ggH.txt')
    xs_qqH = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-vbfH.txt')
    xs_WH  = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-WH.txt')
    xs_ZH  = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-ZH.txt')
    xs_ttH = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-ttH.txt')
    br_VV  = file2map(path+'lhc-hxswg/sm/br/BR.txt')
    br_ff  = file2map(path+'lhc-hxswg/sm/br/BR1.txt')

    # Scale Yields 
    for iBin in xrange(0 , len( dcIn.content['block2']['bin'] ) ):
      jBin=dcIn.content['block2']['bin'][iBin]
      iProc=dcIn.content['block2']['process'][iBin]
      # X-section
      xs_Scale = 1.
      if dcIn.content['block2']['process'][iBin] == 'ggH' : xs_Scale = xs_ggH[iMassExtra]['XS_pb']/xs_ggH[iMass]['XS_pb']
      if dcIn.content['block2']['process'][iBin] == 'qqH' : xs_Scale = xs_qqH[iMassExtra]['XS_pb']/xs_qqH[iMass]['XS_pb']
      if dcIn.content['block2']['process'][iBin] == 'WH'  : xs_Scale = xs_WH[iMassExtra]['XS_pb']/xs_WH[iMass]['XS_pb']
      if dcIn.content['block2']['process'][iBin] == 'ZH'  : xs_Scale = xs_ZH[iMassExtra]['XS_pb']/xs_ZH[iMass]['XS_pb']
      if dcIn.content['block2']['process'][iBin] == 'ttH' : xs_Scale = xs_ttH[iMassExtra]['XS_pb']/xs_ttH[iMass]['XS_pb']
      # BR
      br_Scale = 1.
      if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']: 
        if channels[options.Version][iChannel][iEnergy]['tag'] == 'vbfbb' : br_Scale = br_ff[iMassExtra]['H_bb']/br_ff[iMass]['H_bb']
        else :
          print 'ERROR: Unknown BR for :', iChannel
          exit()
      YieldIn= float(dcIn.getRate(bin=jBin,process=iProc))
      YieldOut= float(dcIn.getRate(bin=jBin,process=iProc))*xs_Scale*br_Scale
      print jBin,iProc,dcIn.getRate(bin=jBin,process=iProc) , '-->' , str(YieldIn*xs_Scale*br_Scale)
      dcOut.setRate(bin=jBin,process=iProc,value=YieldOut) 

    # Modify Workspace : vbfbb -> change mass of H template
    if channels[options.Version][iChannel][iEnergy]['tag'] == 'vbfbb':
      for iEntry in dcIn.content['header2']:
        if  dcIn.content['header2'][iEntry][1] == 'qqH' and (dcIn.content['header2'][iEntry][2] == iBin or dcIn.content['header2'][iEntry][2] == '*') :
          fName = card.replace(channels[options.Version][iChannel][iEnergy]['card'],dcIn.content['header2'][iEntry][3])
          wName = dcIn.content['header2'][iEntry][4].split(':')[0]
          wFile = TFile.Open(fName,'READ') 
          wTmp  = wFile.Get(wName)
          gROOT.ProcessLine('gROOT->cd()')
          w     = wTmp.Clone()
          wTmp.Delete()
          wFile.Close()

      MassList=[115, 120, 125, 130, 135]
      MassFit = {}
      MassExt = {}
      for iBin in  dcIn.content['block1']['bin'] : 
        MassFit[iBin] = { } 
        for jMass in massList:
          MassFit[iBin][jMass] = w.obj('CMS_vbfbb_mean_m'+str(jMass)+'_'+iBin).getVal()       

      for iBin in  dcIn.content['block1']['bin'] : 
        h = TH1F('hMassFit','hMassFit',5,112.5,137.5)
        for jMass in MassList:
          h.Fill(jMass, MassFit[iBin][jMass])
        pol1=TF1("pol1","[0]+[1]*x",110,140.)
        fit = h.Fit("pol1","0")
        p0 = pol1.GetParameter(0);
        p1 = pol1.GetParameter(1); 
        h.Delete()
        pol1.Delete()
        fit.Delete()
        MassExt[iBin] = round(p0 + p1 * iMassExtra,3) 
        print iMassExtra, MassExt[iBin]
        
      for iBin in  dcIn.content['block1']['bin'] :
        w.obj('CMS_vbfbb_mean_m'+str(iMass)+'_'+iBin).setVal(MassExt[iBin])
        dcOut.content['systs']['param']['CMS_vbfbb_mean_m'+str(iMass)+'_'+iBin][0] = str(MassExt[iBin])
      
        print 'CMS_vbfbb_mean_m'+str(iMass)+'_'+iBin , ':' , dcIn.content['systs']['param']['CMS_vbfbb_mean_m'+str(iMass)+'_'+iBin] , ' --> ' , dcOut.content['systs']['param']['CMS_vbfbb_mean_m'+str(iMass)+'_'+iBin]

      fOutName = fName.replace(str(iMass),str(iMassExtra)).replace('.root','_m'+str(iMass)+'Extrapolated.root')
      fOut = TFile(fOutName,"RECREATE")
      w.Write()
      w.Delete()
      fOut.Close()
      print fOutName
      

      for iEntry in dcOut.content['header2']:
        if dcOut.content['header2'][iEntry][1] in ['qqH','ggH']:
          dcOut.content['header2'][iEntry][3] = dcOut.content['header2'][iEntry][3].replace('.root','_m'+str(iMass)+'Extrapolated.root')





    os.system('rm '+TargetCard)
    dcOut.write(TargetCard) 


# ------------------------------------------------------- PDFSplit(iChannel,iEnergy,card,TargetCard,iMass)

def PDFSplit(iChannel,iEnergy,card,TargetCard,iMass):

    dcIn  = cardTools(card)
    dcOut = cardTools(card)


    if channels[options.Version][iChannel][iEnergy]['tag'] == 'vbfbb':


      print dcIn.content['header1']
      dcOut.remShape('background','*')
      dcOut.addShape('bkg_qcd' ,'*','CMS_vbfbb_data_workspace.root','w:bkg_$CHANNEL') 
      dcOut.addShape('bkg_Z','*','CMS_vbfbb_data_workspace.root','w:CMS_vbfbb_Z_model_$CHANNEL') 
      dcOut.addShape('bkg_top' ,'*','CMS_vbfbb_data_workspace.root','w:Top_model_$CHANNEL') 
      #print '----'
      #print dcOut.content['header2']

      print dcIn.content['block2']
      print dcIn.content['systs']
      dcOut.remCol(process='background') 
      dcOut.addSystLine(systtype='lnN',tag='CMS_vbfbb_bkg_Z_norm')
      dcOut.addSystLine(systtype='lnN',tag='CMS_vbfbb_bkg_Top_norm')
      for iBin in xrange(0 , len( dcIn.content['block2']['bin'] ) ):
        jBin=dcIn.content['block2']['bin'][iBin]
        iProc=dcIn.content['block2']['process'][iBin]
        if iProc == 'background' :
          YieldIn= float(dcIn.getRate(bin=jBin,process=iProc))
          print jBin,iProc, YieldIn
          sZjet = dcIn.content['systs']['param']['CMS_vbfbb_nzjet_'+jBin]
          sTop  = dcIn.content['systs']['param']['CMS_vbfbb_ntop_'+jBin]
          dcOut.remSystLine(systtype='param',tag='CMS_vbfbb_nzjet_'+jBin)
          dcOut.remSystLine(systtype='param',tag='CMS_vbfbb_ntop_'+jBin)
          nQCD = YieldIn - float(sTop[0]) - float(sZjet[0])
          dcOut.addCol(jBin,'bkg_qcd' ,'1',str(nQCD),'-1')
          dcOut.addCol(jBin,'bkg_Z','2',sZjet[0] ,'-1')
          dcOut.addCol(jBin,'bkg_top' ,'3',sTop[0]  ,'-1')
          dcOut.addSystLine(systtype='lnU',tag='CMS_vbfbb_nqcd_'+jBin)
          #dcOut.addSystLine(systtype='lnN',tag='CMS_vbfbb_nzjet_'+jBin)
          #dcOut.addSystLine(systtype='lnN',tag='CMS_vbfbb_ntop_'+jBin)
          Zsyst=1.+round(float(sZjet[1])/float(sZjet[0]),3)
          Tsyst=1.+round(float(sTop[1])/float(sTop[0]),3)
          dcOut.setSyst(bin=jBin, processId='1', syst='lnU', tag='CMS_vbfbb_nqcd_'+jBin ,value='1.05')
          #dcOut.setSyst(bin=jBin, processId='2', syst='lnN', tag='CMS_vbfbb_nzjet_'+jBin ,value=str(Zsyst)) 
          #dcOut.setSyst(bin=jBin, processId='3', syst='lnN', tag='CMS_vbfbb_ntop_'+jBin  ,value=str(Tsyst)) 
          dcOut.setSyst(bin=jBin, processId='2', syst='lnN', tag='CMS_vbfbb_bkg_Z_norm' ,value=str(Zsyst)) 
          dcOut.setSyst(bin=jBin, processId='3', syst='lnN', tag='CMS_vbfbb_bkg_Top_norm' ,value=str(Tsyst)) 

      dcOut.content['header1']['jmax'] = '*'
      dcOut.content['header1']['imax'] = '*'
      print dcOut.content['systs']


    else:
      print 'PDFSplit UNDEFINED for channel : ' , channels[options.Version][iChannel][iEnergy]['tag']


    os.system('rm '+TargetCard)
    dcOut.write(TargetCard)

# ------------------------------------------------------- Split Card in categories
def CATSplit(card):
    dcIn  = cardTools(card)
 
    CATS=dcIn.content['block1']['bin']
    print CATS
    print dcIn.content['block2']
    for iBin in dcIn.content['block1']['bin']:
      TargetCard=card.replace('.txt','_'+iBin+'.txt')
      print TargetCard
      dcOut = cardTools(card)
      for jBin in CATS:
        if not iBin == jBin : 
          pkBin = -1
          for kBin in dcIn.content['block2']['bin']: 
            pkBin += 1
            if kBin == jBin : 
              print 'remove' , dcIn.content['block2']['bin'][pkBin],dcIn.content['block2']['process'][pkBin]
              dcOut.remCol(bin=kBin,process=dcIn.content['block2']['process'][pkBin])
      
          for iSysType in dcIn.content['systs']:
            for iSyst in dcIn.content['systs'][iSysType]:
               if jBin in iSyst : 
                 if iSyst in dcOut.content['systs'][iSysType]:
                   dcOut.remSystLine(systtype=iSysType,tag=iSyst)

      dcOut.content['header1']['jmax'] = '*'
      dcOut.content['header1']['imax'] = '1'
      os.system('rm '+TargetCard)
      dcOut.write(TargetCard)


            
      



# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )
parser.add_option("-c", "--channel",    dest="channels",       help="channel set to scale", default=[], type='string' , action='callback' , callback=combTools.list_maker('channels',','))
parser.add_option("-P", "--purpose",    dest="purpose",     help="purpose of the datacard (couplings, searches, mass, ...)", default="smhiggs", metavar="PATTERN")

parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-T", "--Type"  ,     dest="Type"  ,      help="Extrapolation Type (Mass,13TeV)" , default="PDFSplit" , type='string' )


(options, args) = parser.parse_args()

print '==== Data Cards Version : ',options.Version
channelList = combTools.ChannelList_Filter(channels[options.Version],options.channels).get()
cardDir     = combTools.CardDir_Filter(cardtypes,options.purpose).get()
energyList = combTools.EnergyList_Filter(options.energy).get()

for iChannel in channelList:
  # Validate Energy 
  isValidEnergy=False
  for iEnergy in channels[options.Version][iChannel]:
    if (options.energy == 7 or options.energy == 0) and iEnergy == '7TeV' : 
      isValidEnergy=True
    if (options.energy == 8 or options.energy == 0) and iEnergy == '8TeV' : 
      isValidEnergy=True
    if (options.energy == 13) and iEnergy == '13TeV' : 
      isValidEnergy=True
  # Validate Combination Purpose
  isValidPurpose=False
  purposeList = ['smhiggs']
  for purpose in purposeList :
     if options.purpose == purpose :
       isValidPurpose=True
  # Process if valid 
  if isValidEnergy and isValidPurpose :
     massList   = combTools.MassList_Filter_Chann(cardtypes,channels[options.Version],options.purpose,options.masses,iChannel,energyList).get()
     print '---------------------- Building extrapolation for cards: '+iChannel 
     print 'Masses List: '+str(massList)
     for iMass in massList:
       card=cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMass))+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('$MASS',str(iMass))
       print '--------------------> Card: ',card

       # Mass extrapolation
       if options.Type == 'Mass':
        if iMass in extrapolations[options.Type]:
         for iMassExtra in extrapolations[options.Type][iMass] :
           print '------------------------> Extrapolating to: ',iMassExtra
           TargetDir =cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMassExtra))
           TargetCard=TargetDir+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('$MASS',str(iMassExtra))
           print 'TargetCard = ',TargetCard
           os.system('mkdir -p '+ TargetDir)
           ExtrapolateMass(iChannel,iEnergy,card,TargetCard,iMass,iMassExtra)

       # Mass extrapolation
       if options.Type == 'PDFSplit':
         TargetDir =cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMass))

         TargetCard=TargetDir+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('.','_pdfsplit.')

         print TargetCard
         PDFSplit(iChannel,iEnergy,card,TargetCard,iMass)

       # Category Split
       if options.Type == 'CATSplit':
         CATSplit(card)

