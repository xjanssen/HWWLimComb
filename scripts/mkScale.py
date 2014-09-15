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
from copy import deepcopy as dc 


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

# ----------------------------------------------------- Add point if needed to YR ------------------------

def GetYRVal(YRDic,iMass,Key):

    if iMass in YRDic : 
       #print iMass,YRDic[iMass][Key]
       return YRDic[iMass][Key]
    else:
       n=len(YRDic.keys())
       x=[]
       y=[]
       for jMass in sorted(YRDic.keys()):
         x.append(jMass)
         y.append(YRDic[jMass][Key])
       gr = TGraph(n,array('f',x),array('f',y));
       sp = TSpline3("YR",gr);
       #print iMass,sp.Eval(iMass)
       return sp.Eval(iMass)

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
      if dcIn.content['block2']['process'][iBin] == 'ggH' : xs_Scale = GetYRVal(xs_ggH,iMassExtra,'XS_pb')/GetYRVal(xs_ggH,iMass,'XS_pb')
      if dcIn.content['block2']['process'][iBin] == 'qqH' : xs_Scale = GetYRVal(xs_qqH,iMassExtra,'XS_pb')/GetYRVal(xs_qqH,iMass,'XS_pb')
      if dcIn.content['block2']['process'][iBin] == 'WH'  : xs_Scale = GetYRVal(xs_WH, iMassExtra,'XS_pb')/GetYRVal(xs_WH ,iMass,'XS_pb')
      if dcIn.content['block2']['process'][iBin] == 'ZH'  : xs_Scale = GetYRVal(xs_ZH, iMassExtra,'XS_pb')/GetYRVal(xs_ZH ,iMass,'XS_pb')
      if dcIn.content['block2']['process'][iBin] == 'ttH' : xs_Scale = GetYRVal(xs_ttH,iMassExtra,'XS_pb')/GetYRVal(xs_ttH,iMass,'XS_pb')
      # BR
      br_Scale = 1.
      if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']: 
        if channels[options.Version][iChannel][iEnergy]['tag'] == 'vbfbb'  : br_Scale = GetYRVal(br_ffr,iMassExtra,'H_bb')/GetYRVal(br_ff,iMass,'H_bb')
        if channels[options.Version][iChannel][iEnergy]['branch'] == 'hww' : br_Scale = GetYRVal(br_VV ,iMassExtra,'H_WW')/GetYRVal(br_VV,iMass,'H_WW')
        else :
          print 'ERROR: Unknown BR for :', iChannel, channels[options.Version][iChannel][iEnergy]['tag']
          exit()
      YieldIn= float(dcIn.getRate(bin=jBin,process=iProc))
      YieldOut= float(dcIn.getRate(bin=jBin,process=iProc))*xs_Scale*br_Scale
      #print xs_Scale , br_Scale
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

    # Modify Histograms for HWW2l2v 
    if channels[options.Version][iChannel][iEnergy]['branch'] == 'hww' and any(['shapes' in X for X in dcIn.content['header2'].itervalues()]) :  
      shFiles = []
      for iEntry in dcIn.content['header2'] : 
        if dcIn.content['header2'][iEntry][0] == 'shapes' and dcIn.content['header2'][iEntry][1] != 'data_obs' and not ':' in dcIn.content['header2'][iEntry][3]: 
          shFiles.append(dcIn.content['header2'][iEntry][3])
      shFiles = list(set(shFiles))
      print shFiles
      for iFile in shFiles:
        fileInName  = os.path.split(card)[0]+'/'+iFile 
        fileOutName = os.path.split(TargetCard)[0]+'/'+iFile
        print fileInName
        print fileOutName
        fIn   = TFile.Open(fileInName,'READ')
        fOut  = TFile.Open(fileOutName,'RECREATE')
        Hists = [X.GetName() for X in fIn.GetListOfKeys()]
        for iHist in Hists : 
          H = fIn.Get(iHist)
          isHiggs = False
          if   len(iHist.split('_')) == 2 : 
            if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] : isHiggs = True
          elif len(iHist.split('_')) > 2  :
            if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] and iHist.split('_')[2] != 'SM' : isHiggs = True
          if isHiggs : 
            xs_Scale = 1.
            if iHist.split('_')[1] == 'ggH' : xs_Scale = GetYRVal(xs_ggH,iMassExtra,'XS_pb')/GetYRVal(xs_ggH,iMass,'XS_pb')
            if iHist.split('_')[1] == 'qqH' : xs_Scale = GetYRVal(xs_qqH,iMassExtra,'XS_pb')/GetYRVal(xs_qqH,iMass,'XS_pb')
            if iHist.split('_')[1] == 'WH'  : xs_Scale = GetYRVal(xs_WH ,iMassExtra,'XS_pb')/GetYRVal(xs_WH ,iMass,'XS_pb')
            if iHist.split('_')[1] == 'ZH'  : xs_Scale = GetYRVal(xs_ZH ,iMassExtra,'XS_pb')/GetYRVal(xs_ZH ,iMass,'XS_pb')
            if iHist.split('_')[1] == 'ttH' : xs_Scale = GetYRVal(xs_ttH,iMassExtra,'XS_pb')/GetYRVal(xs_ttH,iMass,'XS_pb')
            #if len(iHist.split('_')) == 2 : 
            #  print H.Integral()
            #  print xs_Scale , br_Scale
            br_Scale = GetYRVal(br_VV,iMassExtra,'H_WW')/GetYRVal(br_VV,iMass,'H_WW')
            H.Scale(xs_Scale*br_Scale) 
            #if len(iHist.split('_')) == 2 : print H.Integral()
          fOut.cd()
          H.Write()
        fIn.Close()
        fOut.Close()

    os.system('rm '+TargetCard)
    dcOut.write(TargetCard) 


# ------------------------------------------------------- MASS Extrapolation + efficiency ------------------------------

def ExtrapolateMassEff(iChannel,iEnergy,card,cardLow,cardHigh,TargetCard,vMass,iMassExtra,HistExtraPol=False,ExtraPolMeth='Mix'):
    print 'ExtrapolateMassEff: ',iChannel,vMass,iMassExtra

    dcIn   = cardTools(card)
    dcLow  = cardTools(cardLow)
    dcHigh = cardTools(cardHigh)
    dcOut  = cardTools(card)
     
    #print channels[options.Version][iChannel][iEnergy]
 
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
    ScaleFactors = {}
    for iBin in xrange(0 , len( dcIn.content['block2']['bin'] ) ):
      jBin=dcIn.content['block2']['bin'][iBin]
      iProc=dcIn.content['block2']['process'][iBin]
      YieldIn= float(dcIn.getRate(bin=jBin,process=iProc))
      wLow  = 1.
      wHigh = 1.
      # No Efficiency interpolation
      if   vMass[0] == vMass[1] : 
        # X-section
        xs_Scale = 1.
        if dcIn.content['block2']['process'][iBin] == 'ggH' : xs_Scale = GetYRVal(xs_ggH,iMassExtra,'XS_pb')/GetYRVal(xs_ggH,iMass,'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'qqH' : xs_Scale = GetYRVal(xs_qqH,iMassExtra,'XS_pb')/GetYRVal(xs_qqH,iMass,'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'WH'  : xs_Scale = GetYRVal(xs_WH, iMassExtra,'XS_pb')/GetYRVal(xs_WH ,iMass,'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ZH'  : xs_Scale = GetYRVal(xs_ZH, iMassExtra,'XS_pb')/GetYRVal(xs_ZH ,iMass,'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ttH' : xs_Scale = GetYRVal(xs_ttH,iMassExtra,'XS_pb')/GetYRVal(xs_ttH,iMass,'XS_pb')
        # BR
        br_Scale = 1.
        if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']: 
          if channels[options.Version][iChannel][iEnergy]['branch'] == 'hww' : br_Scale = GetYRVal(br_VV ,iMassExtra,'H_WW')/GetYRVal(br_VV,iMass,'H_WW')
          else :
            print 'ERROR: Unknown BR for :', iChannel, channels[options.Version][iChannel][iEnergy]['tag']
            exit()
        YieldOut= float(dcIn.getRate(bin=jBin,process=iProc))*xs_Scale*br_Scale
        YieldLow =YieldOut
        YieldHigh=YieldOut
      elif vMass[0] < vMass[1] :
        wLow  = float(iMassExtra-vMass[0])/float(vMass[1]-vMass[0])
        wHigh = float(vMass[1]-iMassExtra)/float(vMass[1]-vMass[0])
        # X-section
        xs_Scale_Low =  1.
        if dcIn.content['block2']['process'][iBin] == 'ggH' : xs_Scale_Low  = GetYRVal(xs_ggH,iMassExtra,'XS_pb')/GetYRVal(xs_ggH,vMass[0],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'qqH' : xs_Scale_Low  = GetYRVal(xs_qqH,iMassExtra,'XS_pb')/GetYRVal(xs_qqH,vMass[0],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'WH'  : xs_Scale_Low  = GetYRVal(xs_WH, iMassExtra,'XS_pb')/GetYRVal(xs_WH ,vMass[0],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ZH'  : xs_Scale_Low  = GetYRVal(xs_ZH, iMassExtra,'XS_pb')/GetYRVal(xs_ZH ,vMass[0],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ttH' : xs_Scale_Low  = GetYRVal(xs_ttH,iMassExtra,'XS_pb')/GetYRVal(xs_ttH,vMass[0],'XS_pb')
        xs_Scale_High=  1.
        if dcIn.content['block2']['process'][iBin] == 'ggH' : xs_Scale_High = GetYRVal(xs_ggH,iMassExtra,'XS_pb')/GetYRVal(xs_ggH,vMass[1],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'qqH' : xs_Scale_High = GetYRVal(xs_qqH,iMassExtra,'XS_pb')/GetYRVal(xs_qqH,vMass[1],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'WH'  : xs_Scale_High = GetYRVal(xs_WH, iMassExtra,'XS_pb')/GetYRVal(xs_WH ,vMass[1],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ZH'  : xs_Scale_High = GetYRVal(xs_ZH, iMassExtra,'XS_pb')/GetYRVal(xs_ZH ,vMass[1],'XS_pb')
        if dcIn.content['block2']['process'][iBin] == 'ttH' : xs_Scale_High = GetYRVal(xs_ttH,iMassExtra,'XS_pb')/GetYRVal(xs_ttH,vMass[1],'XS_pb')
        # BR
        br_Scale_Low  = 1.
        br_Scale_High = 1.
        if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']:
          if channels[options.Version][iChannel][iEnergy]['branch'] == 'hww' : 
            br_Scale_Low  = GetYRVal(br_VV ,iMassExtra,'H_WW')/GetYRVal(br_VV,vMass[0],'H_WW')
            br_Scale_High = GetYRVal(br_VV ,iMassExtra,'H_WW')/GetYRVal(br_VV,vMass[1],'H_WW')
          else :
            print 'ERROR: Unknown BR for :', iChannel, channels[options.Version][iChannel][iEnergy]['tag']
            exit() 
        if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']:
          ScaleLow  = wLow *xs_Scale_Low *br_Scale_Low
          ScaleHigh = wHigh*xs_Scale_High*br_Scale_High
          if vMass[1] >= 350 and dcIn.content['block2']['process'][iBin] in ['WH','ZH','ttH']:
            YieldOut = xs_Scale_Low *br_Scale_Low*float(dcLow.getRate(bin=jBin,process=iProc))
            YieldLow = YieldOut
            YieldHigh= YieldOut
          else:
            YieldOut  = ScaleLow * float(dcLow.getRate(bin=jBin,process=iProc)) + ScaleHigh * float(dcHigh.getRate(bin=jBin,process=iProc))
            YieldLow  = xs_Scale_Low *br_Scale_Low*float(dcLow.getRate(bin=jBin,process=iProc))
            YieldHigh = xs_Scale_High*br_Scale_High*float(dcHigh.getRate(bin=jBin,process=iProc))
        else :
          YieldOut  = float(dcIn.getRate(bin=jBin,process=iProc)) 
      else:
        print 'ExtrapolateMassEff: ERROR in input masses',vMass,iMassExtra
        return

      #print xs_Scale , br_Scale
      if dcIn.content['block2']['process'][iBin] in ['ggH','qqH','WH','ZH','ttH']:
        print jBin,iProc,dcIn.getRate(bin=jBin,process=iProc) , '-->' , YieldOut , '(Low: ' , YieldLow , ' , High: ' , YieldHigh , ')' 
        dcOut.setRate(bin=jBin,process=iProc,value=YieldOut) 
        ScaleFactors[dcIn.content['block2']['process'][iBin]] = {} 
        ScaleFactors[dcIn.content['block2']['process'][iBin]]['Avg']  = YieldOut/YieldIn
        ScaleFactors[dcIn.content['block2']['process'][iBin]]['Low']  = wLow *(YieldLow /YieldIn)
        ScaleFactors[dcIn.content['block2']['process'][iBin]]['High'] = wHigh*(YieldHigh/YieldIn)

    # Modify Histograms for HWW2l2v 
    if channels[options.Version][iChannel][iEnergy]['branch'] == 'hww' and any(['shapes' in X for X in dcIn.content['header2'].itervalues()]) :  
      shFiles = []
      for iEntry in dcIn.content['header2'] : 
        if dcIn.content['header2'][iEntry][0] == 'shapes' and dcIn.content['header2'][iEntry][1] != 'data_obs' and not ':' in dcIn.content['header2'][iEntry][3]: 
          shFiles.append(dcIn.content['header2'][iEntry][3])
      shFiles = list(set(shFiles))
      print shFiles
      for iFile in shFiles:
        if not HistExtraPol or vMass[0] == vMass[1]:
          fileInName  = os.path.split(card)[0]+'/'+iFile 
          fileOutName = os.path.split(TargetCard)[0]+'/'+iFile
          print 'File IN : ',fileInName
          print 'File OUT: ',fileOutName
          fIn   = TFile.Open(fileInName,'READ')
          fOut  = TFile.Open(fileOutName,'RECREATE')
          Hists = [X.GetName() for X in fIn.GetListOfKeys()]
          for iHist in Hists : 
            H = fIn.Get(iHist)
            isHiggs = False
            if   len(iHist.split('_')) == 2 : 
              if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] : isHiggs = True
            elif len(iHist.split('_')) > 2  :
              if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] and iHist.split('_')[2] != 'SM' : isHiggs = True
            if isHiggs : 
              Scale = 1.
              if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] : Scale = ScaleFactors[iHist.split('_')[1]]['Avg']
              H.Scale(Scale) 
            fOut.cd()
            H.Write()
          fIn.Close()
          fOut.Close()
        elif ExtraPolMeth == 'Mix' :
          fileInName  = os.path.split(card)[0]+'/'+iFile 
          fileLowName  = os.path.split(cardLow)[0]+'/'+iFile
          fileHighName = os.path.split(cardHigh)[0]+'/'+iFile
          fileOutName  = os.path.split(TargetCard)[0]+'/'+iFile 
          print 'File IN : ',fileInName
          print 'File Low : ',fileLowName
          print 'File High: ',fileHighName
          print 'File OUT : ',fileOutName
          fIn   = TFile.Open(fileInName,'READ')
          fLow  = TFile.Open(fileLowName,'READ')
          fHigh = TFile.Open(fileHighName,'READ')
          fOut  = TFile.Open(fileOutName,'RECREATE')
          Hists = [X.GetName() for X in fIn.GetListOfKeys()]
          for iHist in Hists :
            HIn   = fIn.Get(iHist)
            HLow  = fLow.Get(iHist)
            HHigh = fHigh.Get(iHist)
            isHiggs = False 
            if   len(iHist.split('_')) == 2 :
              if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] : isHiggs = True
            elif len(iHist.split('_')) > 2  :
              if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] and iHist.split('_')[2] != 'SM' : isHiggs = True
            if isHiggs :
              if vMass[1] >= 350 and iHist.split('_')[1] in ['WH','ZH','ttH']:
                Scale = 1.
                if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] : Scale = ScaleFactors[iHist.split('_')[1]]['Avg']
                H = HIn.Clone()
                H.Scale(Scale)
              else :
                print HLow,HHigh
                ScaleLow  = 1.
                ScaleHigh = 1.
                if iHist.split('_')[1] in ['ggH','qqH','ZH','WH','ttH'] :
                  ScaleLow  = ScaleFactors[iHist.split('_')[1]]['Low']
                  ScaleHigh = ScaleFactors[iHist.split('_')[1]]['High']
                HLow.Scale(ScaleLow)
                HHigh.Scale(ScaleHigh)
                H = HLow.Clone()
                H.Add(HHigh)
            else :
              H = HLow.Clone()
            fOut.cd()
            H.Write()
          fIn.Close()
          fLow.Close()
          fHigh.Close()
          fOut.Close()  
        else:
          print 'Hist ExtraPolMeth UNDEFINED !!!! --> ',ExtraPolMeth
          exit()

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


# ------------------------------------------------------- Rename Syst

def RenameSyst(card,renameSyst):
    dcIn  = cardTools(card)
    dcOut = cardTools(card)
    print dcIn.content['block2']['bin']  
    TargetCard = os.path.split(card)[0] + '/' + (os.path.split(card)[1]) + '_rSyst'  
 
    # Set Systematic names       
    for iType in dcIn.content['systs'] :
      for iSyst in dcIn.content['systs'][iType]:
        for iRename in renameSyst:
          oSyst =  iRename.split(':')[0]
          tSyst =  iRename.split(':')[1]
          if iSyst == oSyst:  
            dcOut.content['systs'][iType][tSyst] = dc(dcIn.content['systs'][iType][iSyst])
            dcOut.linenumbers[(iType,tSyst)] = dcOut.linenumbers[(iType,iSyst)]
            del dcOut.content['systs'][iType][iSyst]
            del dcOut.linenumbers[(iType,iSyst)] 

    # Rename histograms
    shFiles = []
    for iEntry in dcIn.content['header2'] :
      if dcIn.content['header2'][iEntry][0] == 'shapes' and dcIn.content['header2'][iEntry][1] != 'data_obs' and not ':' in dcIn.content['header2'][iEntry][3]:
        shFiles.append(dcIn.content['header2'][iEntry][3])
    shFiles = list(set(shFiles))
    print shFiles
    for iFile in shFiles:
      fileInName  = os.path.split(card)[0]+'/'+iFile
      fileOutName = fileInName + '_rSyst'
      print fileInName 
      print fileOutName   
      fIn   = TFile.Open(fileInName,'READ')
      fOut  = TFile.Open(fileOutName,'RECREATE')
      Hists = [X.GetName() for X in fIn.GetListOfKeys()]
      for iHist in Hists :
        H = fIn.Get(iHist)
        if len(iHist.split('_')) > 2 :
          iSyst = '_'.join(iHist.split('_')[2:-1])+'_'+iHist.split('_')[-1].replace('Up','').replace('Down','')
          for iRename in renameSyst:
            oSyst =  iRename.split(':')[0]
            tSyst =  iRename.split(':')[1]
            if iSyst == oSyst: 
              #print H , H.GetTitle()
              H.SetName(iHist.replace(oSyst,tSyst))
              H.SetTitle(H.GetTitle().replace(oSyst,tSyst))
              #print H , H.GetTitle()
        fOut.cd()
        H.Write()

      fIn.Close()
      fOut.Close()
      keepFile = os.path.split(card)[0]+'/'+iFile + '_rKeep' 
      os.system('mv '+fileInName+' '+keepFile)
      os.system('mv '+fileOutName+' '+fileInName) 

    os.system('rm '+TargetCard)
    dcOut.write(TargetCard)
    keepCard = os.path.split(card)[0] + '/' + (os.path.split(card)[1]) + '_rKeep'
    os.system('mv '+card+' '+keepCard)
    os.system('mv '+TargetCard+' '+card) 

# ------------------------------------------------------- Renormalize Proc

def RenormProc(card,renormProc):
    dcIn  = cardTools(card)
    dcOut = cardTools(card)
    print dcIn.content['block2']['bin']  
    TargetCard = os.path.split(card)[0] + '_rProc/' + (os.path.split(card)[1])   
    os.system('mkdir -p '+os.path.split(card)[0] + '_rProc') 

    # Scale Yields 
    for iBin in xrange(0 , len( dcIn.content['block2']['bin'] ) ):
      jBin=dcIn.content['block2']['bin'][iBin]
      iProc=dcIn.content['block2']['process'][iBin]
      for iRenorm in renormProc:
        pRenorm = iRenorm.split(':')[0]
        fRenorm = float(iRenorm.split(':')[1])
        if pRenorm == iProc :
          YieldIn  = float(dcIn.getRate(bin=jBin,process=iProc))
          YieldOut = YieldIn*fRenorm
          print iProc, YieldIn , '--> ' , YieldOut
          dcOut.setRate(bin=jBin,process=iProc,value=YieldOut) 
 
    # Histograms

    shFiles = []
    for iEntry in dcIn.content['header2'] :
      if dcIn.content['header2'][iEntry][0] == 'shapes' and dcIn.content['header2'][iEntry][1] != 'data_obs' and not ':' in dcIn.content['header2'][iEntry][3]:
        shFiles.append(dcIn.content['header2'][iEntry][3])
    shFiles = list(set(shFiles))
    print shFiles
    for iFile in shFiles:
      fileInName  = os.path.split(card)[0]+'/'+iFile
      fileOutName = os.path.split(card)[0] + '_rProc/' +iFile
      print fileInName
      print fileOutName
      fIn   = TFile.Open(fileInName,'READ')
      fOut  = TFile.Open(fileOutName,'RECREATE')
      Hists = [X.GetName() for X in fIn.GetListOfKeys()] 
      for iHist in Hists :
        H = fIn.Get(iHist)
        for iRenorm in renormProc:
          pRenorm = iRenorm.split(':')[0]
          fRenorm = float(iRenorm.split(':')[1])
          if pRenorm in iHist : 
            H.Scale(fRenorm)
                     #print H , H.GetTitle()
        fOut.cd()
        H.Write()

      fIn.Close()
      fOut.Close()

    os.system('rm '+TargetCard)
    dcOut.write(TargetCard)

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )
parser.add_option("-c", "--channel",    dest="channels",       help="channel set to scale", default=[], type='string' , action='callback' , callback=combTools.list_maker('channels',','))
parser.add_option("-P", "--purpose",    dest="purpose",     help="purpose of the datacard (couplings, searches, mass, ...)", default="smhiggs", metavar="PATTERN")

parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default=0, metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-T", "--Type"  ,     dest="Type"  ,      help="Extrapolation Type (Mass,13TeV)" , default="PDFSplit" , type='string' )

parser.add_option("-d", "--dictionary", dest="Dictionary",  help="Datacards Dictionary", default='Configs.HWW2012' , type='string' )
parser.add_option("-r", "--renameSyst", dest="renameSyst",  help="Rename systematics"  , default=[] , type='string' , action='callback' , callback=combTools.list_maker('renameSyst',','))

(options, args) = parser.parse_args()

# Read Combination python config
exec('from %s import *'%(options.Dictionary))
if options.Version == 'None' : options.Version=DefaultVersion


print '==== Data Cards Version : ',options.Version
channelList = combTools.ChannelList_Filter(channels[options.Version],options.channels).get()
cardDir     = combTools.CardDir_Filter(cardtypes,options.purpose).get()
energyList = combTools.EnergyList_Filter(options.energy).get()

for iChannel in channelList:
  # Validate Energy 
  isValidEnergy=False
  for iEnergy in channels[options.Version][iChannel]:
    if (options.energy == 7) and iEnergy == '7TeV' : 
      isValidEnergy=True
      Energy=iEnergy
    if (options.energy == 8) and iEnergy == '8TeV' : 
      isValidEnergy=True
      Energy=iEnergy
    if (options.energy == 13) and iEnergy == '13TeV' : 
      isValidEnergy=True
      Energy=iEnergy
  # Validate Combination Purpose
  isValidPurpose=False
  purposeList = ['smhiggs','himass','ewks','jcp']
  for purpose in purposeList :
     if options.purpose == purpose :
       isValidPurpose=True
  # Process if valid 
  if isValidEnergy and isValidPurpose :
     massList   = combTools.MassList_Filter_Chann(cardtypes,channels[options.Version],options.purpose,options.masses,iChannel,energyList).get()
     print '---------------------- Building extrapolation for cards: '+iChannel + ' @ ' + Energy
     print 'Masses List: '+str(massList)
     paramSet   = combTools.ParamSet_Maker(cardtypes,channels[options.Version],options.purpose,options.masses,iChannel,energyList).get()
     print paramSet
     for iSet in range(0,len(paramSet['values'])) : 
       #print paramSet['values'][iSet]
       iMass = paramSet['values'][iSet][0]
       card=cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(iMass))+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(iMass))
       for iPar in range(1,len(paramSet['names'])) : 
         #print paramSet['names'][iPar]
         parVal=str(paramSet['values'][iSet][iPar])
         for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
         card=card.replace('$'+paramSet['names'][iPar],parVal)
       print '--------------------> Card: ',card
#    exit()
#    for iMass in massList:
#      card=cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(iMass))+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(iMass))
#      print '--------------------> Card: ',card
      
       # Mass extrapolation
       if options.Type == 'LoMass' :
        if iMass in extrapolations[options.Type]:
         for iMassExtra in extrapolations[options.Type][iMass] :
           print '------------------------> Extrapolating to: ',iMassExtra
           TargetDir =cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(iMassExtra))
           TargetCard=TargetDir+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(iMassExtra))
           for iPar in range(1,len(paramSet['names'])) :
                 parVal=str(paramSet['values'][iSet][iPar])
                 for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
                 TargetDir=TargetDir.replace('$'+paramSet['names'][iPar],parVal)
                 TargetCard=TargetCard.replace('$'+paramSet['names'][iPar],parVal)
           print 'TargetCard = ',TargetCard
           os.system('mkdir -p '+ TargetDir)
           ExtrapolateMass(iChannel,Energy,card,TargetCard,iMass,iMassExtra)

       # Mass extrapolation 
       if options.Type == 'HiMass' :
         if Energy in extrapolations[options.Type]:
           if iMass in extrapolations[options.Type][Energy]:
             for iMassExtra in extrapolations[options.Type][Energy][iMass] :
               print '------------------------> Extrapolating to: ',iMassExtra 
               TargetDir =cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(iMassExtra))
               TargetCard=TargetDir+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(iMassExtra))
               for iPar in range(1,len(paramSet['names'])) :
                 parVal=str(paramSet['values'][iSet][iPar])
                 for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
                 TargetDir=TargetDir.replace('$'+paramSet['names'][iPar],parVal)
                 TargetCard=TargetCard.replace('$'+paramSet['names'][iPar],parVal)
               print 'TargetCard = ',TargetCard
               os.system('mkdir -p '+ TargetDir)
               ExtrapolateMass(iChannel,Energy,card,TargetCard,iMass,iMassExtra)

       # Mass extrapolation with Efficiency mixing
       if options.Type == 'HiMassEff' :
         if Energy in extrapolations[options.Type]:
           if iMass in extrapolations[options.Type][Energy]:
            for iEntry in extrapolations[options.Type][Energy][iMass]:
              for iMassExtra in extrapolations[options.Type][Energy][iMass][iEntry]['To']:
                print '------------------------> Extrapolating to: ',iMassExtra
                cardLow   =cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(extrapolations[options.Type][Energy][iMass][iEntry]['From'][0]))+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(extrapolations[options.Type][Energy][iMass][iEntry]['From'][0])) 
                cardHigh  =cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(extrapolations[options.Type][Energy][iMass][iEntry]['From'][1]))+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(extrapolations[options.Type][Energy][iMass][iEntry]['From'][1])) 
                TargetDir =cardbase+channels[options.Version][iChannel][Energy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][Energy]['subdir'].replace('$MASS',str(iMassExtra))
                TargetCard=TargetDir+'/'+channels[options.Version][iChannel][Energy]['card'].replace('$MASS',str(iMassExtra))
                for iPar in range(1,len(paramSet['names'])) :
                  parVal=str(paramSet['values'][iSet][iPar])
                  for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
                  TargetDir=TargetDir.replace('$'+paramSet['names'][iPar],parVal)
                  cardLow=cardLow.replace('$'+paramSet['names'][iPar],parVal)
                  cardHigh=cardHigh.replace('$'+paramSet['names'][iPar],parVal)
                  TargetCard=TargetCard.replace('$'+paramSet['names'][iPar],parVal)
                print 'TargetCard = ',TargetCard
                os.system('mkdir -p '+ TargetDir)
                ExtrapolateMassEff(iChannel,Energy,card,cardLow,cardHigh,TargetCard,extrapolations[options.Type][Energy][iMass][iEntry]['From'],iMassExtra)

       # Mass extrapolation
       if options.Type == 'PDFSplit':
         TargetDir =cardbase+channels[options.Version][iChannel][iEnergy]['dir']+'/'+cardDir+'/'+channels[options.Version][iChannel][iEnergy]['subdir'].replace('$MASS',str(iMass))

         TargetCard=TargetDir+'/'+channels[options.Version][iChannel][iEnergy]['card'].replace('.','_pdfsplit.')

         print TargetCard
         PDFSplit(iChannel,iEnergy,card,TargetCard,iMass)

       # Category Split
       if options.Type == 'CATSplit':
         CATSplit(card)

       # Rename Systematics
       if options.Type == 'RenameSyst':
          print 'Rename Syst: ',options.renameSyst
          RenameSyst(card,options.renameSyst)

       # Renormalize process
       if options.Type == 'RenormProc':
          print 'Renormalize process ',options.renameSyst
          RenormProc(card,options.renameSyst)
