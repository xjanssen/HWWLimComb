#!/usr/bin/env python
import ROOT
from ROOT import *
from optparse import OptionParser
from copy import deepcopy as dc
import os,sys
import numpy
from array import *
from math import *
import subprocess
import string
from scipy.stats.mstats import mquantiles
import rootlogonTDR
from collections import OrderedDict

from Config import *
import combTools

#homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/'
#workspace   = homedir+'workspace/'
#jobdir      = homedir+'jobs/'
#plotsdir    = homedir+'plots/'
#cardbase    = homedir+'cmshcg/trunk/'

gROOT.SetBatch()
#gROOT.ProcessLine(".x tdrstyle.cc")
#gROOT.ProcessLine('.L '+combscripts+'contours.cxx')
gROOT.ProcessLine('.L /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/contours.cxx')
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)

CMSText=["CMS preliminary","CMS","CMS Projection"] 
LumText=["4.9 fb^{-1} (7 TeV) + 19.4 fb^{-1} (8 TeV)","#sqrt{s} = 7 TeV, L = 4.9 fb^{-1}","#sqrt{s} = 8 TeV, L = 19.5 fb^{-1}","#sqrt{s} = 13 TeV, L = 30 fb^{-1}","#sqrt{s} = 13 TeV, L = 120 fb^{-1}"]
LumText=["19.4 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)","4.9 fb^{-1} (7 TeV)","19.4 fb^{-1} (8 TeV)","#sqrt{s} = 13 TeV, L = 30 fb^{-1}","#sqrt{s} = 13 TeV, L = 120 fb^{-1}"]
#LumText=["#sqrt{s} = 7 TeV, L = 4.9 fb^{-1} ; #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}","#sqrt{s} = 7 TeV, L = 4.9 fb^{-1}","#sqrt{s} = 8 TeV, L = 19.5 fb^{-1}"]

class combPlot :
   def __init__(self,channels,combinations,Version,ConfDic,blind=True,postFix='',logX=False,logY=False,iTitle=0,iLumi=0):
       exec('from %s import *'%(ConfDic))

       self.channels = channels
       self.combinations = combinations
       self.Version = Version
       self.blind   = blind
       self.postFix = postFix
       self.logX    = logX
       self.logY    = logY
       self.Results = {}
       self.Obj2Plot= {} 
       self.resetPlot()
       self.c1      = TCanvas("c1","c1",800,800)
       self.Legend  = TLegend()
       self.isSquareCanvas=False
       self.plotsdir= plotsdir+'/'+self.Version
       os.system('mkdir -p '+self.plotsdir)
       gStyle.SetPalette(1) 
       #rootlogonTDR.set_palette("gray")
       self.iLumi  = iLumi
       self.iTitle = iTitle

   def SetBatch():
       gROOT.SetBatch()

   def resetPlot(self):
       self.Obj2Plot= {} 
       self.xAxisTitle = ""
       self.yAxisTitle = ""
       self.yMin = 'AUTO'
       self.yMax = 'AUTO'
       self.xMin = 'AUTO'
       self.xMax = 'AUTO'

   def squareCanvas(self,gridx=True,gridy=True) :
       self.c1.Close()
       self.c1 = TCanvas("c1","c1",700,700);
       self.c1.cd()
       self.c1.SetRightMargin(0.05)
       self.c1.SetTopMargin(0.07)
       self.c1.SetGridy(gridy)
       self.c1.SetGridx(gridx)
       self.isSquareCanvas = True;

   def rectangleCanvas(self,gridx=True,gridy=True):
       self.c1.Close()
       self.c1 = TCanvas("c1","c1",1200,700)
       self.c1.cd()
       #self.c1.SetRightMargin(0.05)
       self.c1.SetGridy(gridy)
       self.c1.SetGridx(gridx)
       self.isSquareCanvas = False


   def defHist(self):
       self.c1.cd()
       self.h=TH1F()
       self.h.Draw()

   
   def addTitle(self,iCMS=1,iLumi=0):
       self.c1.cd()
       print 'addTitle ' , iCMS , iLumi  
 
       x1=0.09
       y1=0.90
       x2=0.99
       y2=0.98
       if iCMS == 0 :
         fontSize = 0.04 
         if self.isSquareCanvas : fontSize = 0.027 
       else:
         fontSize = 0.04 
         if self.isSquareCanvas : fontSize = 0.033
   
       self.cmsprel = TPaveText(x1,y1,x2,y2,"brtlNDC");  
       self.cmsprel.SetTextSize(fontSize*1.3);
       self.cmsprel.SetFillColor(0)
       self.cmsprel.SetFillStyle(0)
       self.cmsprel.SetLineStyle(0)
       self.cmsprel.SetLineWidth(0)
       self.cmsprel.SetTextAlign(11)
       self.cmsprel.SetTextFont(61);
       #self.cmsprel.AddText(CMSText[iCMS]);
       self.cmsprel.AddText("CMS");
       self.cmsprel.SetBorderSize(0);
       self.cmsprel.Draw("same");

       self.status = TPaveText(x1*2.1,y1*1.01,x2,y2,"brtlNDC");
       self.status.SetTextSize(fontSize);
       self.status.SetFillColor(0)
       self.status.SetFillStyle(0)
       self.status.SetLineStyle(0)
       self.status.SetLineWidth(0)
       self.status.SetTextAlign(11)
       self.status.SetTextFont(52);
       #self.status.AddText(CMSText[iCMS]);
       self.status.AddText("Unpublished");
       self.status.SetBorderSize(0);
       self.status.Draw("same");


       self.lumi = TPaveText(x1,y1*1.01,x2,y2,"brtlNDC");  
       self.lumi.SetTextSize(fontSize);
       self.lumi.SetFillColor(0)
       self.lumi.SetFillStyle(0)
       self.lumi.SetLineStyle(0)
       self.lumi.SetLineWidth(0)
       self.lumi.SetTextAlign(31)
       self.lumi.SetTextFont(42);
       self.lumi.AddText(LumText[iLumi]);
       self.lumi.SetBorderSize(0);
       self.lumi.Draw("same");

   def addAxisTitle(self,titleX,titleY):
       self.c1.cd()
       c1.ls()

   def Wait(self):
       self.c1.WaitPrimitive() 

   def Save(self,Name):
       if len(self.postFix) > 0 and self.postFix[0] != '_' : pF = '_'+self.postFix
       else                     : pF = self.postFix
       self.c1.SaveAs(self.plotsdir+'/'+Name+pF+'.pdf')
       self.c1.SaveAs(self.plotsdir+'/'+Name+pF+'.png')
       self.c1.SaveAs(self.plotsdir+'/'+Name+pF+'.root')
       self.c1.SaveAs(self.plotsdir+'/'+Name+pF+'.C')
       #os.system('convert '+self.plotsdir+'/'+Name+pF+'.pdf '+self.plotsdir+'/'+Name+pF+'.png') 
       #os.system('convert '+self.plotsdir+'/'+Name+pF+'.pdf '+self.plotsdir+'/'+Name+pF+'.gif') 

   def treeAccess(self,tree,var=[]):
        tree.SetBranchStatus('*',0)

        _lm = numpy.array(0,'d')
        _mh = numpy.array(0,'d')
        _var=[]
        for iVar in range(len(var)): _var.append(numpy.array(0,'f'))

        tree.SetBranchStatus('limit',1)
        tree.SetBranchStatus('mh'   ,1)
        tree.SetBranchAddress('limit',_lm)
        tree.SetBranchAddress('mh',   _mh)
        if len(var)>0:
          for iVar in range(len(var)):
            tree.SetBranchStatus (var[iVar],1)
            tree.SetBranchAddress(var[iVar],_var[iVar])

          return _lm, _mh, _var 
        else:
          return _lm, _mh

#double findCrossingOfScan1D(TGraph *graph, double threshold, bool leftSide, double xmin=-9e99, double xmax=9e99) {
#    double *x = graph->GetX();
#    double *y = graph->GetY();
#    int imin = 0, n = graph->GetN();
#    for (int i = 1; i < n; ++i) {
#        if (x[i] < xmin || x[i] > xmax) continue;
#        if (y[i] < y[imin]) imin = i;
#    }
#    int imatch = -1;
#    if (leftSide) {
#        for (int i = imin; i >= 0; --i) {
#            if (x[i] < xmin || x[i] > xmax) continue;
#            if (y[i] > threshold && y[i+1] < threshold) {
#                imatch = i; break;
#            }
#        }
#        if (imatch == -1) return x[0];
#    } else {
#        for (int i = imin; i < n; ++i) {
#            if (x[i] < xmin || x[i] > xmax) continue;
#            if (y[i-1] < threshold && y[i] > threshold) {
#                imatch = i-1; break;
#            }
#        }
#        if (imatch == -1) return x[n-1];
#    }
#    double d1 = fabs(y[imatch] - threshold), d2 = fabs(y[imatch+1] - threshold);
#    return (x[imatch]*d2 + x[imatch+1]*d1)/(d1+d2);
#}

   def find2DNLLScan1D(self,graph,parVal,xmin=-9e99,xmax=9e99):

       x = graph.GetX();
       y = graph.GetY();
       n = graph.GetN()
       
       val = -999
       dx  =  999 
       for i in range(1,n):
         if abs(x[i]-parVal) < dx :
            dx  = abs(x[i]-parVal) 
            val = y[i]

       return val
 
   def findCrossingOfScan1D(self,graph,threshold,leftSide,xmin=-9e99,xmax=9e99):
       x = graph.GetX();
       y = graph.GetY();
       imin = 0

       n = graph.GetN()
       for i in range(1,n):
         if (x[i] >= xmin and x[i] <= xmax): 
           if (y[i] < y[imin]):imin = i

       print leftSide,imin,n
       imatch = -1 
       if (leftSide) :
         for i in range(imin , 0 , -1):
           if (x[i] >= xmin and x[i] <= xmax): 
             if (y[i] > threshold and y[i+1] < threshold):
               imatch = i
               break
       else:
         if imin==0:imin=1
         for i in range(imin , n ):
           if (x[i] >= xmin and x[i] <= xmax): 
             if (y[i-1] < threshold and y[i] > threshold):
               imatch = i-1 
               break


       if imatch >= 0 :
         print imatch,x[imatch]
         d1 = fabs(y[imatch] - threshold)
         d2 = fabs(y[imatch+1] - threshold) 
         return (x[imatch]*d2 + x[imatch+1]*d1)/(d1+d2) 
       else :
         return -999.

   def ParamSet_Maker(self,iModel='OneHiggs',iTarget='NONE' ):
       paramSet = {}
       if 'params' in cardtypes[physmodels[iModel]['cardtype']] : 
         print cardtypes[physmodels[iModel]['cardtype']]['params']
         for iEntry in cardtypes[physmodels[iModel]['cardtype']]['params']:
           paramSet[iEntry] = cardtypes[physmodels[iModel]['cardtype']]['params'][iEntry]
       elif iTarget in targets and 'JobsParam' in targets[iTarget] :
         print targets[iTarget]['JobsParam'] 
         paramSet['values'] = []
         paramSet['names']  = []
         paramSet['rules']  = {}
         for iEntry in targets[iTarget]['JobsParam'] :
           paramSet['names'].append(iEntry)
         if len(paramSet['names']) == 1 :
           for iPar in xrange(0,len(targets[iTarget]['JobsParam'][paramSet['names'][0]])) : 
             arr=[]
             arr.append(targets[iTarget]['JobsParam'][paramSet['names'][0]][iPar])
             paramSet['values'].append(arr)
         elif len(paramSet['names']) == 2 : 
           for iPar1 in xrange(0,len(targets[iTarget]['JobsParam'][paramSet['names'][0]])) :
             for iPar2 in xrange(0,len(targets[iTarget]['JobsParam'][paramSet['names'][1]])) :
               arr=[]
               arr.append(targets[iTarget]['JobsParam'][paramSet['names'][0]][iPar1])
               arr.append(targets[iTarget]['JobsParam'][paramSet['names'][1]][iPar2])
               paramSet['values'].append(arr)
       else:

         paramSet['values'] = [[]]
         paramSet['names']  = []
         paramSet['rules']  = {}
       return paramSet  

   def readResults(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],iTarget='BestFit'):

       #print 'reading ',iComb,' ',iEnergy,' ',iModel,' ',iTarget

       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       paramSet = self.ParamSet_Maker(iModel)
       for iSet in range(0,len(paramSet['values'])) : 
         extSet=''
         for iPar in range(0,len(paramSet['names'])) :
           #print paramSet['names'][iPar]
           parVal=str(paramSet['values'][iSet][iPar])
           parVal = parVal.replace('.','d')
           for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
           #print parVal
           extSet+='_' + paramSet['names'][iPar] + '_' + parVal
         print extSet

         Result   = {}
         Result['mass'] = massList
  
         # Create Keys
         if   'treeKeys' in targets[iTarget]:
           for iKey in targets[iTarget]['treeKeys']:
             Result[iKey] = []
         elif 'quantile' in targets[iTarget]:
           #qProb=[]
           for iKey in targets[iTarget]['quantile']:
             Result[iKey] = []
             #qProb.append(targets[iTarget]['quantile'][iKey]) 
  
         
         # Fetch results from trees (treeKeys)
         if   'treeKeys' in targets[iTarget]:
           for iMass in massList :
             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb+extSet
             if iEnergy != 0: fileName += '_' + str(iEnergy) + 'TeV'           
             fileName += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
             #print fileName
             if not os.path.exists(fileName):
               print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO :',fileName
               for iKey in targets[iTarget]['treeKeys']:
                  Result[iKey].append(0.)
             else:
               try:
                 fTree = TFile.Open(fileName)
                 tree = fTree.Get('limit')
                 nentries = tree.GetEntries()         
                 lm, mh = self.treeAccess(tree)
                 for ientry in range(nentries):
                   tree.GetEntry(ientry)
                   if ientry < len(targets[iTarget]['treeKeys']) :
                      Result[targets[iTarget]['treeKeys'][ientry]].append(dc(lm))
                 fTree.Close()  
               except:
                 print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
                 for iKey in targets[iTarget]['treeKeys']:
                    Result[iKey].append(0.)
  
         elif 'quantile' in targets[iTarget]:
           for iMass in massList :
             fileCmd  = 'ls '+TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb+extSet
             if iEnergy != 0: fileCmd += '_' + str(iEnergy) + 'TeV'
             fileCmd += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'*.root'
             proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
             out, err = proc.communicate()
             FileList=string.split(out)
             vLim=[]
             for iFile in FileList:
               try:
                 fTree = TFile.Open(iFile)
                 tree = fTree.Get('limit')
                 nentries = tree.GetEntries()         
                 lm, mh = self.treeAccess(tree)
                 for ientry in range(nentries):
                   tree.GetEntry(ientry)
                   vLim.append(float(dc(lm)))
                 fTree.Close()  
               except:
                 print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
             # quantile
             if len(vLim) > 0 : 
               for iKey in targets[iTarget]['quantile']:
                 p=[]
                 p.append(targets[iTarget]['quantile'][iKey])
                 q = mquantiles(vLim,p) 
                 #print iKey, p, q
                 Result[iKey].append(q[0])
             else:
               print 'WARNING: No Limit vector --> Putting ZERO'+str(iMass)
               for iKey in targets[iTarget]['quantile']:
                  Result[iKey].append(0.)
  
  
             #print fileCmd
             #print FileList
  
         #print Result,massList
         #return
        
         # Store in global dictionary 
         CombKey  = iComb+extSet
         isNewKey = True  
         if len(self.Results) != 0 : 
           for iDicKey in self.Results : 
             if iDicKey == CombKey : isNewKey = False
         if isNewKey : self.Results[CombKey] = {} 
         isNewKey = True
         if len(self.Results[CombKey]) !=0 : 
           for iDicKey in self.Results[CombKey] : 
             if iDicKey == iEnergy : isNewKey = False
         if isNewKey : self.Results[CombKey][iEnergy] = {} 
         isNewKey = True
         if len(self.Results[CombKey][iEnergy]) != 0 :
           for iDicKey in self.Results[CombKey][iEnergy] :
             if iDicKey == iModel : isNewKey = False
         if isNewKey : self.Results[CombKey][iEnergy][iModel] = {}    
         self.Results[CombKey][iEnergy][iModel][iTarget] = Result

       #print self.Results

   def readMDF1D(self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFGridObs',iDic={}):
       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       for iMass in massList :
         fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
         fileName += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
         print  fileName   
       
         if iDic['NDim'] == 1 :
           try:
             gROOT.ProcessLine('TFile* fTree = TFile::Open("'+fileName+'")')
             gROOT.ProcessLine('TTree*  tree = (TTree*)  fTree->Get("limit")')
             keyX=iDic['Keys'][0]
             minX=str(iDic['Min'][0])
             maxX=str(iDic['Max'][0])
             minXP=str(iDic['MinPlt'][0])
             maxXP=str(iDic['MaxPlt'][0])

             print minX,maxX,minXP,maxXP

             objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+iTarget
             print objName

             # Scan
             gROOT.ProcessLine('gROOT->cd()')
             gROOT.ProcessLine('int n = tree->Draw("2*deltaNLL:'+keyX+'", TCut("abs(deltaNLL) > 0. && abs(deltaNLL) < 999") );')
             gROOT.ProcessLine('TGraph *gr = (TGraph*) gROOT->FindObject("Graph")->Clone("gr");')
             ROOT.gr.SetName('gr_'+objName);
             ROOT.gr.Sort();
             self.Obj2Plot['gr__'+objName] = { 'Obj' : ROOT.gr.Clone('gr_'+objName) , 'Type' : 'Curve' , 'Legend' : ''}
             gROOT.ProcessLine('delete gr')

             # Best Fit
             gROOT.ProcessLine('int n = tree->Draw("2*deltaNLL:'+keyX+'", TCut("abs(deltaNLL) == 0.") );')
             gROOT.ProcessLine('TGraph *gr0 = (TGraph*) gROOT->FindObject("Graph")->Clone("gr0");')
             ROOT.gr0.SetName('gr0_'+objName);
             ROOT.gr0.Sort();
             ROOT.gr0.Print()
             self.Obj2Plot['gr0__'+objName] = { 'Obj' : ROOT.gr0.Clone('gr0_'+objName) , 'Type' : 'Point' , 'Legend' : ''}
             gROOT.ProcessLine('delete gr0')

             # Set some Default Style and Legend
             self.Obj2Plot['gr__'+objName]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
             #self.Obj2Plot['gr__'+objName]['Obj'].GetXaxis().SetRangeUser(minXP,maxXP)
             self.Obj2Plot['gr__'+objName]['Obj'].GetYaxis().SetTitle("-2 #Delta ln L")
             #self.Obj2Plot['gr__'+objName]['Obj'].GetYaxis().SetRangeUser(0.00001,20.)
             #self.Obj2Plot['gr0__'+objName]['Obj'].SetMarkerColor(kRed) 

             gROOT.ProcessLine('fTree->Close()') 


           except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
 

   def readMDFGrid(self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFGridObs'):
       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       for iMass in massList :
         fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
         fileName += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
         print  fileName   
         
         if   physmodels[iModel]['MDFTree']['NDim'] == 2 :
           #try:
             gROOT.ProcessLine('TFile* fTree = TFile::Open("'+fileName+'")')
             gROOT.ProcessLine('TTree*  tree = (TTree*)  fTree->Get("limit")')
             keyX=physmodels[iModel]['MDFTree']['Keys'][0]
             keyY=physmodels[iModel]['MDFTree']['Keys'][1]
             minX=str(physmodels[iModel]['MDFTree']['Min'][0])
             minY=str(physmodels[iModel]['MDFTree']['Min'][1])
             maxX=str(physmodels[iModel]['MDFTree']['Max'][0])
             maxY=str(physmodels[iModel]['MDFTree']['Max'][1])
             print minX,maxX
             print minY,maxY

             minXP=str(physmodels[iModel]['MDFTree']['MinPlt'][0])
             minYP=str(physmodels[iModel]['MDFTree']['MinPlt'][1])
             maxXP=str(physmodels[iModel]['MDFTree']['MaxPlt'][0])
             maxYP=str(physmodels[iModel]['MDFTree']['MaxPlt'][1])
             print minXP,maxXP
             print minYP,maxYP

             objName=keyX+'-'+keyY
             gROOT.ProcessLine('gROOT->cd()')
             gROOT.ProcessLine('TH2* h2d=0')
             gROOT.ProcessLine('TGraph *gr0=0')
             gROOT.ProcessLine('TList* c68')
             gROOT.ProcessLine('TList* c95')
             print 'h2d = treeToHist2D(tree,"'+keyX+'","'+keyY+'","'+objName+'",TCut(""),'+minX+','+maxX+','+minY+','+maxY+')'
             gROOT.ProcessLine('h2d = treeToHist2D(tree,"'+keyX+'","'+keyY+'","'+objName+'",TCut(""),'+minX+','+maxX+','+minY+','+maxY+')')
             #if iModel == 'cVcF' and iTarget== 'MDFGridObs' : ROOT.h2d.Fill(0.67,1.5399999,2.30)
             gROOT.ProcessLine('c68 = contourFromTH2(h2d,2.30)')
             gROOT.ProcessLine('c95 = contourFromTH2(h2d,5.99)')
             gROOT.ProcessLine('gr0 = bestFit(tree,"'+keyX+'","'+keyY+'",TCut(""))')
             ROOT.gr0.Print()
             objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+iTarget
             self.Obj2Plot['h2d__'+objName] = { 'Obj' : ROOT.h2d.Clone('h2d'+objName) , 'Type' : 'TH2D'  , 'Legend' : ''}
             self.Obj2Plot['c68__'+objName] = { 'Obj' : ROOT.c68.Clone('c68'+objName) , 'Type' : 'TList' , 'Legend' : ''}
             self.Obj2Plot['c95__'+objName] = { 'Obj' : ROOT.c95.Clone('c95'+objName) , 'Type' : 'TList' , 'Legend' : ''}
             self.Obj2Plot['gr0__'+objName] = { 'Obj' : ROOT.gr0.Clone('gr0'+objName) , 'Type' : 'Point' , 'Legend' : ''}
             print self.Obj2Plot['h2d__'+objName],self.Obj2Plot['h2d__'+objName]['Obj']
             gROOT.ProcessLine('delete h2d')
             gROOT.ProcessLine('delete c68')
             gROOT.ProcessLine('delete c95')
             gROOT.ProcessLine('delete gr0')
             # Set some Default Style and Legend
             self.Obj2Plot['h2d__'+objName]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
             self.Obj2Plot['h2d__'+objName]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
             self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
             self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
             self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
             self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetRangeUser(0.00001,20.)
             #for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineColor(kRed) 
             for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineWidth(3) 
             #for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineColor(kRed) 
             for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineWidth(3) 
             for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineStyle(2) 
             #self.Obj2Plot['gr0__'+objName]['Obj'].SetMarkerColor(kRed) 
             gROOT.ProcessLine('fTree->Close()') 
           #except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'

       return

   def readMDFVal(self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFCrossExp68',algo='Single'):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       Result   = {}
       Result['mass'] = massList
       VarName = physmodels[iModel]['MDFTree']['Keys']
       for iVarName in VarName:
         if   algo == 'Single' :
           Result[iVarName]       = []
           Result[iVarName+'_Do'] = []
           Result[iVarName+'_Up'] = []
         elif algo == 'Cross' :
           Result[iVarName]          = []
           Result[iVarName+'_Top']   = []
           Result[iVarName+'_Floor'] = []
           Result[iVarName+'_Left']  = []
           Result[iVarName+'_Right'] = []
         else:
           print 'readMDFVal: Invalid Algo !!!!!'
           return 

       for iMass in massList :
         fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
         fileName += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
         print  fileName   
      
         if   physmodels[iModel]['MDFTree']['NDim'] == 2 :
           try:
             fTree = TFile.Open(fileName)
             tree = fTree.Get('limit')
             nentries = tree.GetEntries()   
             
             lm, mh, var = self.treeAccess(tree,VarName)
             for ientry in range(nentries):
               tree.GetEntry(ientry)
               if  algo == 'Single' : 
                 if   ientry == 0 : 
                    Result[VarName[0]].append(dc(var[0]))        
                    Result[VarName[1]].append(dc(var[1]))        
                 elif ientry == 1 : Result[VarName[0]+'_Do'].append(dc(var[0]))
                 elif ientry == 2 : Result[VarName[0]+'_Up'].append(dc(var[0]))
                 elif ientry == 3 : Result[VarName[1]+'_Do'].append(dc(var[1]))
                 elif ientry == 4 : Result[VarName[1]+'_Up'].append(dc(var[1]))
               elif algo == 'Cross' :
                 if   ientry == 0 : PF=''
                 elif ientry == 1 : PF='_Left'
                 elif ientry == 2 : PF='_Right'
                 elif ientry == 3 : PF='_Floor'
                 elif ientry == 4 : PF='_Top'
                 if ientry <= 5:
                   Result[VarName[0]+PF].append(dc(var[0]))        
                   Result[VarName[1]+PF].append(dc(var[1])) 

             if   algo == 'Single' :
               print '1D:', VarName[0] , Result[VarName[0]][0] , '+' ,  Result[VarName[0]+'_Up'][0]-Result[VarName[0]][0] , '-' , Result[VarName[0]][0]-Result[VarName[0]+'_Do'][0]
               print '1D:', VarName[1] , Result[VarName[1]][0] , '+' ,  Result[VarName[1]+'_Up'][0]-Result[VarName[1]][0] , '-' , Result[VarName[1]][0]-Result[VarName[1]+'_Do'][0]
             elif algo == 'Cross' :
               print '2D:', VarName[0] , Result[VarName[0]][0] , '+' ,  Result[VarName[0]+'_Right'][0]-Result[VarName[0]][0] , '-' , Result[VarName[0]][0]-Result[VarName[0]+'_Left'][0]
               print '2D:', VarName[1] , Result[VarName[1]][0] , '+' ,  Result[VarName[1]+'_Top'][0]-Result[VarName[1]][0] , '-' , Result[VarName[1]][0]-Result[VarName[1]+'_Floor'][0]

           except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
             if  algo == 'Single' : 
               Result[VarName[0]].append(0)        
               Result[VarName[1]].append(0)  
               Result[VarName[0]+'_Do'].append(0)        
               Result[VarName[1]+'_Do'].append(0)  
               Result[VarName[0]+'_Up'].append(0)        
               Result[VarName[1]+'_Up'].append(0)  
             elif  algo == 'Cross' :
               Result[VarName[0]].append(0)        
               Result[VarName[1]].append(0)  
               Result[VarName[0]+'_Top'].append(0)        
               Result[VarName[1]+'_Top'].append(0)  
               Result[VarName[0]+'_Floor'].append(0)        
               Result[VarName[1]+'_Floor'].append(0)  
               Result[VarName[0]+'_Left'].append(0)        
               Result[VarName[1]+'_Left'].append(0)  
               Result[VarName[0]+'_Right'].append(0)        
               Result[VarName[1]+'_Right'].append(0)  
 

       # Store in global dictionary 
       isNewKey = True  
       if len(self.Results) != 0 : 
         for iDicKey in self.Results : 
           if iDicKey == iComb : isNewKey = False
       if isNewKey : self.Results[iComb] = {} 
       isNewKey = True
       if len(self.Results[iComb]) !=0 : 
         for iDicKey in self.Results[iComb] : 
           if iDicKey == iEnergy : isNewKey = False
       if isNewKey : self.Results[iComb][iEnergy] = {} 
       isNewKey = True
       if len(self.Results[iComb][iEnergy]) != 0 :
         for iDicKey in self.Results[iComb][iEnergy] :
           if iDicKey == iModel : isNewKey = False
       if isNewKey : self.Results[iComb][iEnergy][iModel] = {}    
       self.Results[iComb][iEnergy][iModel][iTarget] = Result

       # Default Plot
       objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+iTarget+'_'+algo
       if (algo == 'Single' ) :
         print  Result[VarName[0]] , Result[VarName[1]] , Result[VarName[0]+'_Do'] , Result[VarName[0]+'_Up'] , Result[VarName[1]+'_Do'] , Result[VarName[1]+'_Up']
         self.plotPoint('c1d__'+objName, Result[VarName[0]] , Result[VarName[1]] , Result[VarName[0]+'_Do'] , Result[VarName[0]+'_Up'] , Result[VarName[1]+'_Do'] , Result[VarName[1]+'_Up'] , kBlack , 20 , '1#sigma Cross (1D)')
       if (algo == 'Cross' ) :
         vX = []
         vY = []
         vX.append(Result[VarName[0]+'_Right'][0])
         vY.append(Result[VarName[1]+'_Right'][0])
         vX.append(Result[VarName[0]+'_Left'][0])
         vY.append(Result[VarName[1]+'_Left'][0])
         vX.append(Result[VarName[0]+'_Top'][0])
         vY.append(Result[VarName[1]+'_Top'][0])
         vX.append(Result[VarName[0]+'_Floor'][0])
         vY.append(Result[VarName[1]+'_Floor'][0])
         print vX,vY
         self.plotPoint('c2d__'+objName, vX , vY ,  vX , vX , vY , vY  , kRed , 20 , '1#sigma Cross (2D)')


       return


   def plotHorizCurve(self,Name='Curv',vX=[],vCent=[],Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       if len(vCent) != nP : sys.error("plotHorizBand: size mismatch")   
       obj =  TGraph( nP , array('d',vX) ,array('d',vCent) )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(Width)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotHorizLine(self,Name='Curv',vX=[],vCent=1,Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       obj =  TGraph( nP , array('d',vX) ,array('d',[vCent]*nP) )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(Width)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotVertLine(self,Name='Curv', vCent=1, vY=[] ,Color=kBlack,Style=0,Width=2,Legend='None'):
       nP    = len(vY)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       obj =  TGraph( nP , array('d',[vCent]*nP) , array('d',vY)  )
       obj.SetLineColor(Color)
       obj.SetMarkerColor(Color)
       obj.SetLineWidth(2)
       obj.SetLineStyle(Style)
       obj.SetMarkerStyle(0)
       obj.SetMarkerSize(0)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Curve' , 'Legend' : Legend }

   def plotHorizBand(self,Name='Band',vX=[],vCent=[],vUp=[],vDown=[],Color=90,Style=1001,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotHorizBand: ZERO size")
       if len(vCent) != nP : sys.error("plotHorizBand: size mismatch")   
       if len(vUp)   != nP : sys.error("plotHorizBand: size mismatch")   
       if len(vDown) != nP : sys.error("plotHorizBand: size mismatch")   
       obj = TGraphAsymmErrors( nP , array('d',vX) , array('d',vCent) , array('d',[0.]*nP), array('d',[0.]*nP) , array('d',[vCent[i]-vDown[i] for i in range(nP)]) , array('d',[vUp[i]-vCent[i] for i in range(nP)]) )
       print obj.GetFillStyle()
       obj.SetFillStyle(Style)
       obj.SetFillColor(Color)
       obj.SetLineColor(Color) 
       obj.SetLineWidth(2) 
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Band' , 'Legend' : Legend }

   def plotPoint(self,Name='Point',vX=[],vY=[],vLeft=[],vRight=[],vDown=[],vUp=[],Color=kBlack,Style=20,Legend='None'):
       nP    = len(vX)
       if nP == 0 : sys.error("plotPoint: ZERO size")
       if len(vY)    != nP : sys.error("plotPoint: size mismatch")   
       if len(vUp)   != nP : sys.error("plotPoint: size mismatch")   
       if len(vDown) != nP : sys.error("plotPoint: size mismatch")  
       if len(vLeft) != nP : sys.error("plotPoint: size mismatch")  
       if len(vRight)!= nP : sys.error("plotPoint: size mismatch")  
       obj = TGraphAsymmErrors( nP , array('d',vX) , array('d',vY) , array('d',[vX[i]-vLeft[i] for i in range(nP)]) , array('d',[vRight[i]-vX[i] for i in range(nP)] ) ,  array('d',[vY[i]-vDown[i] for i in range(nP)]) , array('d',[vUp[i]-vY[i] for i in range(nP)]) )
       obj.SetLineColor(Color) 
       obj.SetLineWidth(2) 
       obj.SetMarkerStyle(Style)
       obj.SetMarkerColor(Color)
       self.Obj2Plot[Name] = { 'Obj' : obj , 'Type' : 'Point' , 'Legend' : Legend }

 
   def plotAllObj(self,Order=[],onTop=False):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if onTop:iFirst=False
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot]  
       for X in Order: 
         if X in self.Obj2Plot:    
           if iFirst: 
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitle(self.xAxisTitle)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitle(self.yAxisTitle)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetLabelFont (   42)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetLabelFont (   42)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleFont (   42)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleFont (   42)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleOffset( 1.2)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleOffset( 1.2)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetTitleSize (0.050)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetTitleSize (0.050)
             self.Obj2Plot[X]['Obj'].GetXaxis().SetLabelSize (0.045)
             self.Obj2Plot[X]['Obj'].GetYaxis().SetLabelSize (0.045)
           if   self.Obj2Plot[X]['Type'] == 'Band':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].Draw("A3")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("3")   
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].Draw("ALP")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("LP") 

       self.c1.Update() 

   def plotObjLeg(self,Order=[],Title='',Position='TopRight',Ncol=1):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot] 
       NLeg = len( Order ) / Ncol
       if   'Right' in Position :
         x1 = 0.47
         x2 = 0.8  
       elif 'Left'  in Position :
         x1 = 0.17
         x2 = 0.47  
         if 'Large' in Position : x2 = 0.6
       if   'Top'   in Position :
         y1 = 0.87-(NLeg+1)*.040
         if 'Large' in Position : y1 = 0.87-(NLeg+1)*.060
         y2 = 0.87 
       elif 'Bottom' in Position : 
         y1 = 0.50-(NLeg+1)*.040
         y2 = 0.50 
       #self.Legend = TLegend(0.50,0.65,0.85,0.85)   
       self.Legend = TLegend(x1,y1,x2,y2)
       if ( Ncol > 1 ) : self.Legend.SetNColumns(Ncol); 
       self.Legend.SetTextSize(0.033)
       if 'Large' in Position : self.Legend.SetTextSize(0.04)
       self.Legend.SetFillColor(0)
       self.Legend.SetFillStyle(0)
       self.Legend.SetBorderSize(0)
       self.Legend.SetTextFont (42)
       for X in Order: 
         if X in self.Obj2Plot:    
           if   self.Obj2Plot[X]['Type'] == 'Band':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'f')
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'l')
           elif self.Obj2Plot[X]['Type'] == 'Point' :
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'p')
           elif self.Obj2Plot[X]['Type'] == 'TList':
             iFirst=1
             for I in TIter(self.Obj2Plot[X]['Obj']):
               if iFirst == 1:
                 self.Legend.AddEntry(I,self.Obj2Plot[X]['Legend'],'l')
                 iFirst=0
       if not Title == '' : self.Legend.SetHeader(Title)
       self.Legend.Draw('same')

   def SetRange(self,PlotType,iComb): 
       keyComb='None'
       if PlotType in plotStyle:
         if   iComb in plotStyle[PlotType]      : keyComb=iComb
         elif 'Default' in plotStyle[PlotType]  : keyComb='Default' 
         else :
           print 'WARNING: No Default in  plotStyle for PlotType : ',PlotType
           return
       else :
         print 'WARNING: No PlotType in plotStyle : ',PlotType
         return

       print PlotType, keyComb , plotStyle[PlotType][keyComb] 
       if (self.logY) and 'logY' in plotStyle[PlotType][keyComb] :
         yMin =  plotStyle[PlotType][keyComb]['logY'][0] 
         yMax =  plotStyle[PlotType][keyComb]['logY'][1] 
       elif 'linY' in plotStyle[PlotType][keyComb] :
         yMin =  plotStyle[PlotType][keyComb]['linY'][0] 
         yMax =  plotStyle[PlotType][keyComb]['linY'][1] 
       else:
         print 'WARNING: No Y range !!! '
         return

       for X in self.Obj2Plot: self.Obj2Plot[X]['Obj'].GetYaxis().SetRangeUser(yMin,yMax)   

   def EnergyName(self,iEnergy):
       if   iEnergy == 0 : return '7and8TeV'
       elif iEnergy == 7 : return '7TeV'
       elif iEnergy == 8 : return '8TeV'
       elif iEnergy == 13 : 
         if self.iLumi==3:
           return '13TeV_30ifb'
         if self.iLumi==4:
           return '13TeV_120ifb'
         else: 
           return '13TeV'
       else              : return 'UndefE'

   def plotLogXAxis(self,mhMin,mhMax,PlotType,iComb):
       self.c1.cd()

       keyComb='UNDEFINED'
       if PlotType in plotStyle:
         if   iComb in plotStyle[PlotType]      : keyComb=iComb
         elif 'Default' in plotStyle[PlotType]  : keyComb='Default' 
       if keyComb != 'UNDEFINED':
         if (self.logY) and 'logY' in plotStyle[PlotType][keyComb] :
           uymin =  plotStyle[PlotType][keyComb]['logY'][0] 
           uymax =  plotStyle[PlotType][keyComb]['logY'][1] 
         elif 'linY' in plotStyle[PlotType][keyComb] :
           uymin =  plotStyle[PlotType][keyComb]['linY'][0] 
           uymax =  plotStyle[PlotType][keyComb]['linY'][1] 
       else:
         uymin = self.c1.GetUymin();
         uymax = self.c1.GetUymax();
       dy = uymax-uymin

       # Remove Original Axis
       for X in self.Obj2Plot:
         self.Obj2Plot[X]['Obj'].GetXaxis().SetNdivisions(0) 
         self.Obj2Plot[X]['Obj'].GetXaxis().SetRangeUser(mhMin,mhMax) 
         
       
       # Create New Axis Tick
       self.AXtick = TLine();
       self.AXtick.SetLineWidth(1);
       self.AXtick.SetLineColor(1); 
       for iMass in range(90,1000,10):
         if iMass >= mhMin and iMass <= mhMax:
           xx=float(iMass)
           if self.logY:
             if iMass%100 == 0 : yMax = log10(uymin) + log10(dy)*0.08
             else              : yMax = log10(uymin) + log10(dy)*0.04
             self.AXtick.DrawLine(xx, uymin , xx, pow(10,yMax))
           else:
             yMax = uymin
             if iMass%100 == 0 : yMax+=0.04*dy
             else              : yMax+=0.02*dy 
             self.AXtick.DrawLine(xx, uymin, xx, yMax)

       # Create New Label
       ylatex = uymin - 0.035*dy
       if self.logY: 
         ylatex = log10(uymin) - log10(dy)*0.07 
         ylatex = pow(10,ylatex)
       xbins=[100,200,300,400,500,600]
       while (mhMin > xbins[0]) : xbins[0] += 10
       self.AXLabel = [] 
       for i in range(0,6) :
         if (xbins[i] >= mhMin and xbins[i] <= mhMax):
           self.AXLabel.append(TLatex(xbins[i], ylatex, str(xbins[i])))          
           self.AXLabel[-1].SetTextAlign(  22);
           self.AXLabel[-1].SetTextFont (  42);
           self.AXLabel[-1].SetTextSize (0.045);
           self.AXLabel[-1].Draw("same");

   def plotOneLimit(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],bInject=True,bAsimov=True):

       self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp')
       if not self.blind : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsObs')
       if bInject        : 
         if bAsimov:
           self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsInjPre')
         else:
           self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsSMToysNoSyst')
      
       if (bInject) : self.postFix += '_inj125'
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'
 
       paramSet = self.ParamSet_Maker(iModel) 
       print paramSet
       for iSet in range(0,len(paramSet['values'])) :
         extSet=''
         for iPar in range(0,len(paramSet['names'])) :
           print paramSet['names'][iPar]
           parVal=str(paramSet['values'][iSet][iPar])
           parVal = parVal.replace('.','d')
           for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
           #print parVal
           extSet+='_' + paramSet['names'][iPar] + '_' + parVal
         CombKey = iComb+extSet
         print CombKey      
#        self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp')
       
 
         self.squareCanvas(False,False)
         self.c1.cd()
         self.resetPlot()
  
         
         if (self.logX) : gPad.SetLogx()
         if (self.logY) : gPad.SetLogy()
   
         self.xAxisTitle = "Higgs boson mass [GeV]"
         self.yAxisTitle = "95% CL limit on #sigma/#sigma_{SM}"
  
   
         aMass         = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['mass']
         aMedExpLimit  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['Val']
         aExpLimit68D  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['68D']
         aExpLimit68U  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['68U'] 
         aExpLimit95D  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['95D']
         aExpLimit95U  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['95U']
  
         if bInject :        
           if bAsimov:
             aMedInjLimit  = self.Results[CombKey][iEnergy][iModel]['ACLsInjPre']['Val']
           else:
             aMedInjLimit  = self.Results[CombKey][iEnergy][iModel]['ACLsSMToysNoSyst']['Val']
             aInjLimit68D  = self.Results[CombKey][iEnergy][iModel]['ACLsSMToysNoSyst']['68D']
             aInjLimit68U  = self.Results[CombKey][iEnergy][iModel]['ACLsSMToysNoSyst']['68U'] 
             aInjLimit95D  = self.Results[CombKey][iEnergy][iModel]['ACLsSMToysNoSyst']['95D']
             aInjLimit95U  = self.Results[CombKey][iEnergy][iModel]['ACLsSMToysNoSyst']['95U']
           #aMedInjFast   = self.Results[CombKey][iEnergy]['SMInject']['ACLsObs']['Val']
  
         if (not self.blind ) :  aObsLimit = self.Results[CombKey][iEnergy][iModel]['ACLsObs']['Val']
  
         self.plotHorizBand('95CL', aMass , aMedExpLimit , aExpLimit95U , aExpLimit95D ,  90 , 1001 , 'Expected #pm 2#sigma')
         self.plotHorizBand('68CL', aMass , aMedExpLimit , aExpLimit68U , aExpLimit68D , 211 , 1001 , 'Expected #pm 1#sigma')
         self.plotHorizCurve('Exp', aMass , aMedExpLimit , kBlack , 2          ,  2          ,     'Median Expected')
  
         if (not self.blind ) : self.plotHorizCurve('Obs', aMass , aObsLimit , kBlack , 1  , 3 , 'Observed')
  
         if  bInject :  
           if bAsimov:
             self.plotHorizCurve('Inj'   , aMass , aMedInjLimit , kRed  , 1            , 2            , 'm_{H} Injected')
           else:
             self.plotHorizBand('95CLInj', aMass , aMedInjLimit , aInjLimit95U , aInjLimit95D , kBlue , 3356 , 'Injected #pm 2#sigma_{stat}')
             self.plotHorizBand('68CLInj', aMass , aMedInjLimit , aInjLimit68U , aInjLimit68D , kRed  , 3356 , 'Injected #pm 1#sigma_{stat}')
             self.plotHorizCurve('Inj'   , aMass , aMedInjLimit , kRed  , 1            , 2            , 'm_{H}=125 GeV Injected')
           #self.plotHorizCurve('InjFast', aMass , aMedInjLimit , kRed , 1                        , 'CL_{S} Injected')
           #self.plotHorizCurve('Inj68D'   , aMass , aInjLimit68D , kBlue , 2                        , 'CL_{S} Injected')
           #self.plotHorizCurve('Inj95D'   , aMass , aInjLimit95D , kBlue , 3                        , 'CL_{S} Injected')
           #self.plotHorizCurve('Inj68U'   , aMass , aInjLimit68U , kBlue , 2                        , 'CL_{S} Injected')
           #self.plotHorizCurve('Inj95U'   , aMass , aInjLimit95U , kBlue , 3                        , 'CL_{S} Injected')
  
         lMass=[]
         lMass.append(100.)
         lMass.append(aMass[-1]+1)
         self.plotHorizLine('Line', lMass , 1. , kBlack , 1  , 2  , 'CL=1')
  
         self.Obj2Plot['Exp']['Obj'].SetMarkerStyle(20)
         self.Obj2Plot['Exp']['Obj'].SetMarkerSize(.8)
         if (not self.blind ) :
           self.Obj2Plot['Obs']['Obj'].SetMarkerStyle(20)
           self.Obj2Plot['Obs']['Obj'].SetMarkerSize(.8)
  
     
         self.SetRange('Limit',CombKey)
         self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(aMass[0],aMass[-1])
         self.plotAllObj(['95CL','68CL','Exp','95CLInj','68CLInj','Inj','Obs','Line'])
         self.plotObjLeg(['Obs','Exp','68CL','95CL','Inj','68CLInj','95CLInj'],self.combinations[iComb]['legend'])
         if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'Limit',CombKey)
         self.addTitle(self.iTitle,self.iLumi) 
         #self.addTitle() 
         #self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
         #self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.1,500.)
         #self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
         self.c1.Update() 
         self.Save('limit_'+CombKey+'_'+self.EnergyName(iEnergy)+'_'+iModel)
         #self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
         self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
         #self.Save('limit_'+CombKey+'_'+self.EnergyName(iEnergy)+'_'+iModel+'_zoom')
       
   def plotMuVsMh(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[]):

       BestFit='BestFit'
       self.readResults(iComb,iEnergy,iModel,massFilter,BestFit)

       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs boson mass [GeV]"
       #self.yAxisTitle = "Best fit for #mu"
       self.yAxisTitle = "Best fit for #sigma/#sigma_{SM}"

       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'

       aMass    = self.Results[iComb][iEnergy][iModel][BestFit]['mass']
       muVal    = self.Results[iComb][iEnergy][iModel][BestFit]['Val']
       mu68U    = self.Results[iComb][iEnergy][iModel][BestFit]['68U']
       mu68D    = self.Results[iComb][iEnergy][iModel][BestFit]['68D']

       if (self.blind) : return

       self.plotHorizBand('68CL', aMass , muVal , mu68U , mu68D , 211 , 1001 , '#mu #pm 1#sigma' )
       self.plotHorizCurve('Obs', aMass , muVal , kBlack ,2    , 3           , '#mu #pm 1#sigma' )

       lMass=[]
       lMass.append(100.)
       lMass.append(aMass[-1]+1)  
       self.plotHorizLine('Line', lMass , 1. , kBlack , 1    , '#mu=1')

       self.Obj2Plot['Obs']['Obj'].SetMarkerStyle(20)
       self.Obj2Plot['Obs']['Obj'].SetMarkerSize(.8)
 
       self.SetRange('BestFit',iComb)
       self.plotAllObj(['68CL','Obs','Line'])
       self.plotObjLeg(['Obs'],self.combinations[iComb]['legend']) 
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'BestFit',iComb)

       self.addTitle() 
       self.c1.Update() 
       self.Save('MuVsMh_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotSignVsMh(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],bInject=False,fitType='Pre'):

       self.readResults(iComb,iEnergy,iModel,massFilter,'SExp'+fitType)
       if (not self.blind ) : self.readResults(iComb,iEnergy,iModel,massFilter,'SObs')
 
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs boson mass [GeV]"
       self.yAxisTitle = "Significance"

       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'

       aMass    = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['mass']
       SExp     = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['Val']
       if (not self.blind) : SObs     = self.Results[iComb][iEnergy][iModel]['SObs']['Val']
       #self.plotHorizLine('3Sig', aMass , 3. , kBlack , 3    , 'S=3')
       #self.plotHorizLine('5Sig', aMass , 5. , kRed   , 3    , 'S=5')

 
       self.plotHorizCurve('Exp', aMass , SExp , kBlack ,2    , 2    , 'Expected' ) 
       if (not self.blind) :  self.plotHorizCurve('Obs', aMass , SObs , kBlack ,1   , 3     , 'Observed' ) 

       self.SetRange('Sign',iComb)
       self.plotAllObj(['Exp','Obs'])
       self.plotObjLeg(['Exp','Obs'],self.combinations[iComb]['legend']) 
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'Sign',iComb)


       self.addTitle() 
       self.c1.Update() 
       self.Save('SignVsMh_'+fitType+'Fit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotExpLimits(self,CombList=['hww01jet_shape'],iEnergy=0,iModel='OneHiggs',massFilter=[]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs boson mass [GeV]"
       self.yAxisTitle = "95% CL expected limit on #sigma/#sigma_{SM}"

       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'

       LCol = [ kBlack , kBlack , kBlack , kBlue , kBlue , kBlue , kRed , kRed , kMagenta , kMagenta , kMagenta , kGreen , kGreen ]
       LTyp = [    1   ,    2   ,   3    ,   1   ,   2   ,   3   ,   2  ,   3  ,  1  ,  2  ,  3 , 1 , 2 ]      

       LCol = [ kBlack , kBlack , kBlue , kBlue ,  kRed , kRed , kMagenta , kMagenta ,  kGreen , kGreen , kOrange , kOrange ]
       LTyp = [    1   ,    2   ,   1   ,   2   ,   1   ,  2   ,    1     ,    2     ,     1   ,   2    ,    1    ,   2     ]

       iLC=0 
       toPlot = []
       for iComb in CombList:
         self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp')
         for iKey in self.Results : print iKey
         paramSet = self.ParamSet_Maker(iModel)
         print paramSet
         for iSet in range(0,len(paramSet['values'])) :
           extSet=''
           for iPar in range(0,len(paramSet['names'])) :
             print paramSet['names'][iPar]
             parVal=str(paramSet['values'][iSet][iPar])
             parVal = parVal.replace('.','d')
             for iRule in paramSet['rules'] : parVal = parVal.replace(iRule,paramSet['rules'][iRule])
             #print parVal
             extSet+='_' + paramSet['names'][iPar] + '_' + parVal
           CombKey = iComb+extSet
           print CombKey
           toPlot.append(CombKey)
           aMass         = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['mass']
           aMedExpLimit  = self.Results[CombKey][iEnergy][iModel]['ACLsExp']['Val']
           print self.Results[CombKey][iEnergy][iModel]['ACLsExp']['Val'] 
           if 'EWKS' in CombKey : self.plotHorizCurve(CombKey, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC]  , 2  , extSet )
           else                 : self.plotHorizCurve(CombKey, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC]  , 2  , self.combinations[iComb]['legend'] )
           iLC+=1
      
       CombListAll = dc(toPlot)
       aMass = [110,1000] 
       self.plotHorizLine('Line', aMass , 1. , kRed , 1  , 2  , 'CL=1')
  
       #self.c1.SetLogy()
       #self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.05,200.)

       self.SetRange('LimitExp',CombList[0])
       toPlot.append('Line')
       self.plotAllObj(toPlot)
       LT=''
       LP='TopRight'
       Ncol=1
       PF=''
       if ( 'EWKS' in CombList[0] ) :
         LT   = self.combinations[CombList[0]]['legend']  
         self.addTitle(0,2) 
         PF   = '_'+CombList[0] 

       elif    ( CombList[0] == 'of_cp2_ext_1d0' ) : 
         LT   = 'H #rightarrow WW (DF 0/1-jet), BR_{Inv} = 0' 
         LP   = 'TopLeftLarge'
         Ncol = 2
         self.addTitle(0,2) 
         PF= '_01jof' 
       elif  ( CombList[0] == 'sf_cp2_ext_1d0' ) : 
         LT   = 'H #rightarrow WW (SF 0/1-jet), BR_{Inv} = 0' 
         LP   = 'TopLeftLarge'
         Ncol = 2
         self.addTitle(0,2)  
         PF= '_01jsf' 
       elif  ( CombList[0] == 'vbfofnew_cp2_1d0' ) :
         LT   = 'VBF H #rightarrow WW (DF) , BR_{Inv} = 0' 
         LP   = 'TopLeftLarge'
         Ncol = 2
         self.addTitle(0,2) 
         PF= '_2jof' 
       elif  ( CombList[0] == 'vbfsf_cp2_1d0' ) :
         LT   = 'VBF H #rightarrow WW (SF) , BR_{Inv} = 0' 
         LP   = 'TopLeftLarge'
         Ncol = 2
         self.addTitle(0,2) 
         PF= '_2jsf' 
       elif  ( CombList[0] == 'hww_cp2_1d0' ) :
         LT   = 'H #rightarrow WW (0/1/2-jet) , BR_{Inv} = 0' 
         LP   = 'TopLeftLarge'
         Ncol = 2
         self.addTitle(0,2) 
         PF= '_012j' 

       else:
         self.addTitle() 
       self.plotObjLeg(CombListAll,LT,LP,Ncol)
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'LimitExp',CombList[0])


       self.c1.Update() 
       self.Save('ExpLimits_'+self.EnergyName(iEnergy)+'_'+iModel+PF)
  

   def plotExpSignVsMh(self,CombList=['hww01jet_shape'],iEnergy=0,iModel='OneHiggs',massFilter=[],fitType='Pre'):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       if CombList[0] == 'HWW' : CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape']

       self.xAxisTitle = "Higgs boson mass [GeV]"
       self.yAxisTitle = "Expected Significance"

       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'

       LCol = [ kBlack , kBlack , kBlack , kBlue , kBlue , kBlue , kRed , kRed ]
       LTyp = [    1   ,    2   ,   3    ,   1   ,   2   ,   3   ,   2  ,   3  ]      

       iLC=0 
       for iComb in CombList:
          self.readResults(iComb,iEnergy,iModel,massFilter,'SExp'+fitType)
          aMass         = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['mass']
          aMedExpLimit  = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['Val']
          self.plotHorizCurve(iComb, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC] , 2 , self.combinations[iComb]['legend'] )
          iLC+=1
      
       aMass = [110,600] 
       #self.plotHorizLine('Line', aMass , 1. , kRed , 1    , 'CL=1')
  
       #self.c1.SetLogy()
       #self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.0,25.)

       self.SetRange('Sign',CombList[0])
       toPlot = dc(CombList)
       #toPlot.append('Line')
       self.plotAllObj(toPlot)
       self.plotObjLeg(CombList)
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'Sign',CombList[0])


       self.addTitle() 
       self.c1.Update() 
       self.Save('ExpSign_'+fitType+'Fit_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotExpPvalVsMh(self,CombList=['hww01jet_shape'],iEnergy=0,iModel='OneHiggs',massFilter=[],fitType='Pre'):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       if CombList[0] == 'HWW' : CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape']

       self.xAxisTitle = "Higgs boson mass [GeV]"
       self.yAxisTitle = "Expected p-value"

       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'

       LCol = [ kBlack , kBlack , kBlack , kBlue , kBlue , kBlue , kRed , kRed ]
       LTyp = [    1   ,    2   ,   3    ,   1   ,   2   ,   3   ,   2  ,   3  ]      

       iLC=0 
       for iComb in CombList:
          self.readResults(iComb,iEnergy,iModel,massFilter,'PVExp'+fitType)
          aMass         = self.Results[iComb][iEnergy][iModel]['PVExp'+fitType]['mass']
          aMedExpLimit  = self.Results[iComb][iEnergy][iModel]['PVExp'+fitType]['Val']
          self.plotHorizCurve(iComb, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC] , 2 , self.combinations[iComb]['legend'] )
          iLC+=1
      
       aMass = [110,600] 
       #self.plotHorizLine('Line', aMass , 1. , kRed , 1    , 'CL=1')
  
       #self.c1.SetLogy()
       #self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.0,25.)

       self.SetRange('Pval',CombList[0])
       toPlot = dc(CombList)
       #toPlot.append('Line')
       self.plotAllObj(toPlot)
       self.plotObjLeg(CombList)
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'Pval',CombList[0])

		 # sigma lines
       self.c1.Update()
       sinfo = []
       for nsigma in range(8): 
		val = (1.-TMath.Erf(nsigma/sqrt(2.)))/2.
                print val , self.yMin
		if val < self.yMin: break
                print val
		sline = TF1("%dsigma"%nsigma,"%.8f"%val,self.xMin,self.xMax)
		sline.SetLineColor(kRed)
		sline.SetLineWidth(2)
		sline.Draw("same")
		sinfo += [sline]
		sname = TPaveText(1.0-gPad.GetRightMargin()-0.05,val*0.85,1.-gPad.GetRightMargin()-0.01,val*0.85)
		sname.SetTextFont(42)
		sname.SetTextSize(gStyle.GetPadTopMargin()*2.5/4.)
		sname.SetBorderSize(0)
		sname.SetFillStyle(-1)
		sname.SetTextAlign(32)
		sname.SetTextColor(kRed)
		sname.AddText("%d#sigma"%nsigma)
		sname.Draw()
		sinfo += [sline]

       self.addTitle() 
       self.c1.Update() 
       self.Save('ExpPval_'+fitType+'Fit_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotMuChannel(self,CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape'],iEnergy=0,iModel='SMHiggs',massFilter=[125]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetLeftMargin(0.4) 
       self.c1.SetGridx(1)

       #if False:
       BestFit='BestFit'
       #else:
       #  BestFit='BestFitExp'

       if len(massFilter) != 1 : return
       nChann=len(CombList)-1
       if nChann == 0 : return

       for iComb in CombList:
         self.readResults(iComb,iEnergy,iModel,massFilter,BestFit)


       MuMin=-1.
       MuMax=3.
       frame = TH2F("frame",";Best fit for #sigma/#sigma_{SM};",1,MuMin,MuMax,nChann+1,0,nChann+1);
       #frame.GetXaxis().SetTitleSize(0.05);
       #frame.GetXaxis().SetLabelSize(0.04);
       #frame.GetYaxis().SetLabelSize(0.06);
       #frame.GetXaxis().SetNdivisions(505)
       frame.GetXaxis().SetLabelFont (   42)
       frame.GetYaxis().SetLabelFont (   42)
       frame.GetXaxis().SetTitleFont (   42)
       frame.GetYaxis().SetTitleFont (   42)
       frame.GetXaxis().SetTitleOffset( 1.2)
       frame.GetYaxis().SetTitleOffset( 1.2)
       frame.GetXaxis().SetTitleSize (0.050)
       frame.GetYaxis().SetTitleSize (0.050)
       frame.GetXaxis().SetLabelSize (0.045)
       frame.GetYaxis().SetLabelSize (0.055)
       frame.GetXaxis().SetNdivisions(505)


       frame.Draw()

       print self.Results[CombList[0]][iEnergy][iModel][BestFit]['68D'][0]
       print self.Results[CombList[0]][iEnergy][iModel][BestFit]['68U'][0]
       globalFitBand = TBox(self.Results[CombList[0]][iEnergy][iModel][BestFit]['68D'][0], 0, self.Results[CombList[0]][iEnergy][iModel][BestFit]['68U'][0] , nChann+1);
       globalFitBand.SetFillStyle(3013);
       globalFitBand.SetFillColor(65);
       globalFitBand.SetLineStyle(0);
       globalFitBand.Draw("same");

       Val = self.Results[CombList[0]][iEnergy][iModel][BestFit]['Val'][0]
       globalFitLine = TLine (Val, 0, Val, nChann+1);
       globalFitLine.SetLineWidth(4);
       globalFitLine.SetLineColor(214);
       globalFitLine.Draw("same");

       points = TGraphAsymmErrors (nChann+1)
       invpts = TGraphAsymmErrors (nChann)
       TlMu=TLatex()
       TlMu.SetTextAlign(23);
       TlMu.SetTextSize(0.03);

       asymTolerance = 0.15
       for iChann in xrange(1,nChann+1):
         Val = self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['Val'][0]
         eDo = self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['Val'][0] - self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['68D'][0]
         eUp = self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['68U'][0] - self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['Val'][0]
         if eUp > 100 : eUp=100
         print Val, eDo, eUp
         if Val <= MuMax : 
           points.SetPoint(iChann-1,      Val , iChann-0.5);
           points.SetPointError(iChann-1, eDo, eUp , 0, 0);
           invpts.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
         else:
           invVal=MuMax
           inveDo=MuMax - self.Results[CombList[iChann]][iEnergy][iModel][BestFit]['68D'][0]
           inveUp=0.
           invpts.SetPoint(iChann-1,      invVal , iChann-0.5);
           invpts.SetPointError(iChann-1, inveDo, inveUp , 0, 0);
           points.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
 
         #muTxt = '#mu = '+str(round(Val,2))+'^{ +'+str(round(eUp,2))+'}_{ -'+str(round(eDo,2))+'}'
         muTxt = '#sigma/#sigma_{SM} = %.2f^{ + %.2f}_{  - %.2f}'%(Val,eUp,eDo)
         label = '#splitline{   '+self.combinations[CombList[iChann]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
         frame.GetYaxis().SetBinLabel(iChann, label  );
         #frame.GetYaxis().SetBinLabel(iChann,  self.combinations[CombList[iChann]]['legend'] );
         #frame.GetYaxis().SetBinLabel(iChann-.5,'#mu = 0.76^{+0.19}_{-0.19}')
         #TlMu.DrawLatex(0.2,0.95,'#mu = 0.76^{+0.19}_{-0.19}')
       frame.GetYaxis().LabelsOption("v")
       # ... Combined result 
       Val = self.Results[CombList[0]][iEnergy][iModel][BestFit]['Val'][0]
       eDo = self.Results[CombList[0]][iEnergy][iModel][BestFit]['Val'][0] - self.Results[CombList[0]][iEnergy][iModel][BestFit]['68D'][0]
       eUp = self.Results[CombList[0]][iEnergy][iModel][BestFit]['68U'][0] - self.Results[CombList[0]][iEnergy][iModel][BestFit]['Val'][0]
       points.SetPoint(nChann,      Val , nChann+0.5);
       points.SetPointError(iChann, eDo, eUp , 0, 0);
       muTxt = '#sigma/#sigma_{SM} = %.2f^{ + %.2f}_{  - %.2f}'%(Val,eUp,eDo) 
       #label = '#splitline{   Combined}{                    #scale[0.8]{'+muTxt+'}  }'
       label = '#splitline{   '+self.combinations[CombList[0]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
       frame.GetYaxis().SetBinLabel(nChann+1, label  );
       sepLine = TLine (MuMin, nChann, MuMax, nChann);
       sepLine.SetLineWidth(2);
       sepLine.SetLineStyle(2);
       sepLine.Draw("same")

       #frame.GetYaxis().SetTickLength(0);


       TlMH=TLatex()
       TlMH.SetTextSize(0.03);
       TlMH.SetNDC()
       TlMH.DrawLatex(0.72,0.89,'m_{H} = '+str(massFilter[0])+' GeV')

       points.SetLineColor(kRed);
       points.SetLineWidth(3);
       points.SetMarkerStyle(21);
       points.Draw("PSAME");

       invpts.SetLineColor(kRed);
       invpts.SetLineWidth(3);
       invpts.SetMarkerStyle(0);
       invpts.Draw("PSAME");
 
       self.addTitle(self.iTitle,self.iLumi) 
       self.c1.Update() 
       self.Save('MuCC_'+self.EnergyName(iEnergy)+'_'+iModel+'_'+str(massFilter[0]).replace('.','d'))
       self.Wait()


   def plotSignChannel(self,CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape'],iEnergy=0,iModel='SMHiggs',massFilter=[125]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetLeftMargin(0.4) 
       self.c1.SetGridx(1)

       if len(massFilter) != 1 : return
       nChann=len(CombList)-1
       if nChann == 0 : return

       SignExp='SExpPre'
       SignObs='SObs'
       for iComb in CombList:
         self.readResults(iComb,iEnergy,iModel,massFilter,SignExp)
         if (not self.blind ) : self.readResults(iComb,iEnergy,iModel,massFilter,SignObs)


       MuMin=0.
       MuMax=16.
       frame = TH2F("frame",";Significance;",1,MuMin,MuMax,nChann+1,0,nChann+1);
       #frame.GetXaxis().SetTitleSize(0.05);
       #frame.GetXaxis().SetLabelSize(0.04);
       #frame.GetYaxis().SetLabelSize(0.06);
       #frame.GetXaxis().SetNdivisions(505)
       frame.GetXaxis().SetLabelFont (   42)
       frame.GetYaxis().SetLabelFont (   42)
       frame.GetXaxis().SetTitleFont (   42)
       frame.GetYaxis().SetTitleFont (   42)
       frame.GetXaxis().SetTitleOffset( 1.2)
       frame.GetYaxis().SetTitleOffset( 1.2)
       frame.GetXaxis().SetTitleSize (0.050)
       frame.GetYaxis().SetTitleSize (0.050)
       frame.GetXaxis().SetLabelSize (0.045)
       frame.GetYaxis().SetLabelSize (0.055)
       frame.GetXaxis().SetNdivisions(505)


       frame.Draw()

       points = TGraphAsymmErrors (nChann+1)
       invpts = TGraphAsymmErrors (nChann)
       opoints = TGraphAsymmErrors (nChann+1)
       oinvpts = TGraphAsymmErrors (nChann)
       TlMu=TLatex()
       TlMu.SetTextAlign(23);
       TlMu.SetTextSize(0.03);



       asymTolerance = 0.15
       for iChann in xrange(1,nChann+1):
         Val = self.Results[CombList[iChann]][iEnergy][iModel][SignExp]['Val'][0]
         eDo = Val
         eUp = 0.
         if Val <= MuMax : 
           points.SetPoint(iChann-1,      Val , iChann-0.5);
           points.SetPointError(iChann-1, eDo, eUp , 0.15,0.15);
           invpts.SetPoint(iChann-1,      MuMax+1.  , iChann-0.15);
         else:
           invVal=MuMax
           inveDo=MuMax
           inveUp=0.
           invpts.SetPoint(iChann-1,      invVal , iChann-0.5);
           invpts.SetPointError(iChann-1, inveDo, inveUp , 0.15,0.15);
           points.SetPoint(iChann-1,      MuMax+1.  , iChann-0.15);
     
         #muTxt = '#mu = '+str(round(Val,2))+'^{ +'+str(round(eUp,2))+'}_{ -'+str(round(eDo,2))+'}'
         muTxt = 'S_{exp} = %.1f'%(Val)
         if (not self.blind ) :
           Val = self.Results[CombList[iChann]][iEnergy][iModel][SignObs]['Val'][0]
           eDo = 0.
           eUp = 0.
           if Val <= MuMax : 
             opoints.SetPoint(iChann-1,      Val , iChann-0.5);
             opoints.SetPointError(iChann-1, eDo, eUp , 0.,0.);
             oinvpts.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
           else:
             invVal=MuMax
             inveDo=0.
             inveUp=0.
             oinvpts.SetPoint(iChann-1,      invVal , iChann-0.5);
             oinvpts.SetPointError(iChann-1, inveDo, inveUp , 0.,0.);
             points.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
           muTxt += ' ; S_{obs} = %.1f'%(Val)
         

         if (self.blind) : label = '#splitline{   '+self.combinations[CombList[iChann]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
         else            : label = '#splitline{   '+self.combinations[CombList[iChann]]['legend']+'}{           #scale[0.8]{'+muTxt+'}  }'
         frame.GetYaxis().SetBinLabel(iChann, label  );

       frame.GetYaxis().LabelsOption("v")
       # ... Combined result 
       Val = self.Results[CombList[0]][iEnergy][iModel][SignExp]['Val'][0]
       eDo = Val
       eUp = 0.
       points.SetPoint(nChann,      Val , nChann+0.5);
       points.SetPointError(iChann, eDo, eUp , 0.15,0.15);
       muTxt = 'S_{exp} = %.1f'%(Val) 
       if (not self.blind ) :
         Val = self.Results[CombList[0]][iEnergy][iModel][SignObs]['Val'][0]
         eDo = 0.
         eUp = 0.
         opoints.SetPoint(nChann,      Val , nChann+0.5);
         opoints.SetPointError(iChann, eDo, eUp , 0.,0.);
         muTxt += ' ; S_{obs} = %.1f'%(Val)

       if (self.blind) : label = '#splitline{   '+self.combinations[CombList[0]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
       else            : label = '#splitline{   '+self.combinations[CombList[0]]['legend']+'}{           #scale[0.8]{'+muTxt+'}  }'
       frame.GetYaxis().SetBinLabel(nChann+1, label  );
       sepLine = TLine (MuMin, nChann, MuMax, nChann);
       sepLine.SetLineWidth(2);
       sepLine.SetLineStyle(2);
       sepLine.Draw("same")


       TlMH=TLatex()
       TlMH.SetTextSize(0.03);
       TlMH.SetNDC()
       TlMH.DrawLatex(0.72,0.89,'m_{H} = '+str(massFilter[0])+' GeV')

       points.SetFillColor(38);
       points.Draw("2SAME");
       invpts.SetFillColor(38);
       invpts.Draw("2SAME");

       if (not self.blind ) :
         opoints.SetMarkerColor(kRed);
         opoints.Draw("PSAME");
         oinvpts.SetMarkerColor(kRed);
         oinvpts.Draw("PSAME");

 
       self.addTitle(self.iTitle,self.iLumi) 
       self.c1.Update() 
       self.Save('SignCC_'+self.EnergyName(iEnergy)+'_'+iModel+'_'+str(massFilter[0]).replace('.','d'))
       self.Wait()


   def plotLimitChannel(self,CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape'],iEnergy=0,iModel='SMHiggs',massFilter=[125]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetLeftMargin(0.4) 
       self.c1.SetGridx(1)

       if (self.logX) : self.postFix += '_logX'

       if len(massFilter) != 1 : return
       nChann=len(CombList)-1
       if nChann == 0 : return

       LimExp='ACLsExp'
       LimObs='ACLsObs'

       for iComb in CombList:
         self.readResults(iComb,iEnergy,iModel,massFilter,LimExp)
         if (not self.blind ) : self.readResults(iComb,iEnergy,iModel,massFilter,LimObs)


       if (not self.logX) :  
         MuMin=0.
         MuMax=3.
       else:
         MuMin=0.01
         MuMax=20.

       frame = TH2F("frame",";95% limit on #sigma/#sigma_{SM};",1,MuMin,MuMax,nChann+1,0,nChann+1);
       #frame.GetXaxis().SetTitleSize(0.05);
       #frame.GetXaxis().SetLabelSize(0.04);
       #frame.GetYaxis().SetLabelSize(0.06);
       #frame.GetXaxis().SetNdivisions(505)
       frame.GetXaxis().SetLabelFont (   42)
       frame.GetYaxis().SetLabelFont (   42)
       frame.GetXaxis().SetTitleFont (   42)
       frame.GetYaxis().SetTitleFont (   42)
       frame.GetXaxis().SetTitleOffset( 1.2)
       frame.GetYaxis().SetTitleOffset( 1.2)
       frame.GetXaxis().SetTitleSize (0.050)
       frame.GetYaxis().SetTitleSize (0.050)
       frame.GetXaxis().SetLabelSize (0.045)
       frame.GetYaxis().SetLabelSize (0.055)
       frame.GetXaxis().SetNdivisions(505)

       frame.Draw()
       if (self.logX) : gPad.SetLogx()

       points   = TGraphAsymmErrors (nChann+1)
       points95 = TGraphAsymmErrors (nChann+1)
       pexp     = TGraphAsymmErrors (nChann+1)
       invpts   = TGraphAsymmErrors (nChann)
       invpts95 = TGraphAsymmErrors (nChann)
       pobs     = TGraphAsymmErrors (nChann+1)
       TlMu=TLatex()
       TlMu.SetTextAlign(23);
       TlMu.SetTextSize(0.03);

       asymTolerance = 0.15
       for iChann in xrange(1,nChann+1):
         Val   = self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['Val'][0]
         eDo   = self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['Val'][0] - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['68D'][0]
         eUp   = self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['68U'][0] - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['Val'][0]
         eDo95 = self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['Val'][0] - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['95D'][0]
         eUp95 = self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['95U'][0] - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['Val'][0]

         if eUp   > 100 : eUp=100
         if eUp95 > 100 : eUp95=100
         print Val, eDo, eUp
         if Val <= MuMax : 
           pexp  .SetPoint(iChann-1,      Val , iChann-0.5);
           pexp  .SetPointError(iChann-1, 0. , 0.  , 0.4, 0.4);
           points.SetPoint(iChann-1,      Val , iChann-0.5);
           points.SetPointError(iChann-1, eDo, eUp , 0.4, 0.4);
           points95.SetPoint(iChann-1,      Val , iChann-0.5);
           points95.SetPointError(iChann-1, eDo95, eUp95 , 0.4, 0.4);
           invpts.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
           invpts95.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
         else:
           invVal=MuMax
           inveDo=MuMax - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['68D'][0]
           inveUp=0.
           inveDo95=MuMax - self.Results[CombList[iChann]][iEnergy][iModel][LimExp]['68D'][0]
           inveUp95=0.
           invpts.SetPoint(iChann-1,      invVal , iChann-0.5);
           invpts.SetPointError(iChann-1, inveDo, inveUp , 0.4, 0.4);
           invpts95.SetPoint(iChann-1,      invVal , iChann-0.5);
           invpts95.SetPointError(iChann-1, inveDo95, inveUp95 , 0.4, 0.4);
           pexp  .SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
           points.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
           points95.SetPoint(iChann-1,      MuMax+1.  , iChann-0.5);
         if (not self.blind ) :
           Val   = self.Results[CombList[iChann]][iEnergy][iModel][LimObs]['Val'][0]
           if Val <= MuMax : 
             pobs.SetPoint(iChann-1,      Val , iChann-0.5);
             pobs.SetPointError(iChann-1, 0. , 0.  , 0.4, 0.4);
 
         #muTxt = '#mu = '+str(round(Val,2))+'^{ +'+str(round(eUp,2))+'}_{ -'+str(round(eDo,2))+'}'
         muTxt = '#sigma/#sigma_{SM} < %.2f^{ + %.2f}_{  - %.2f}'%(Val,eUp,eDo)
         label = '#splitline{   '+self.combinations[CombList[iChann]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
         frame.GetYaxis().SetBinLabel(iChann, label  );
         #frame.GetYaxis().SetBinLabel(iChann,  self.combinations[CombList[iChann]]['legend'] );
         #frame.GetYaxis().SetBinLabel(iChann-.5,'#mu = 0.76^{+0.19}_{-0.19}')
         #TlMu.DrawLatex(0.2,0.95,'#mu = 0.76^{+0.19}_{-0.19}')
       frame.GetYaxis().LabelsOption("v")
       # ... Combined result 
       Val = self.Results[CombList[0]][iEnergy][iModel][LimExp]['Val'][0]
       eDo = self.Results[CombList[0]][iEnergy][iModel][LimExp]['Val'][0] - self.Results[CombList[0]][iEnergy][iModel][LimExp]['68D'][0]
       eUp = self.Results[CombList[0]][iEnergy][iModel][LimExp]['68U'][0] - self.Results[CombList[0]][iEnergy][iModel][LimExp]['Val'][0]
       eDo95 = self.Results[CombList[0]][iEnergy][iModel][LimExp]['Val'][0] - self.Results[CombList[0]][iEnergy][iModel][LimExp]['95D'][0]
       eUp95 = self.Results[CombList[0]][iEnergy][iModel][LimExp]['95U'][0] - self.Results[CombList[0]][iEnergy][iModel][LimExp]['Val'][0]
       pexp  .SetPoint(nChann,      Val , nChann+0.5);
       pexp  .SetPointError(iChann, 0. , 0.  , 0.4, 0.4);
       points.SetPoint(nChann,      Val , nChann+0.5);
       points.SetPointError(iChann, eDo, eUp , 0.4, 0.4);
       points95.SetPoint(nChann,      Val , nChann+0.5);
       points95.SetPointError(iChann, eDo95, eUp95 , 0.4, 0.4);
       if (not self.blind ) :
           Val   = self.Results[CombList[0]][iEnergy][iModel][LimObs]['Val'][0]
           if Val <= MuMax : 
             pobs.SetPoint(nChann,      Val , nChann+0.5);
             pobs.SetPointError(nChann, 0. , 0.  , 0.4, 0.4);
 

       muTxt = '#sigma/#sigma_{SM} < %.2f^{ + %.2f}_{  - %.2f}'%(Val,eUp,eDo) 
       #label = '#splitline{   Combined}{                    #scale[0.8]{'+muTxt+'}  }'
       label = '#splitline{   '+self.combinations[CombList[0]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
       frame.GetYaxis().SetBinLabel(nChann+1, label  );
       sepLine = TLine (MuMin, nChann, MuMax, nChann);
       sepLine.SetLineWidth(2);
       sepLine.SetLineStyle(2);
       sepLine.Draw("same")

       #frame.GetYaxis().SetTickLength(0);


       TlMH=TLatex()
       TlMH.SetTextSize(0.03);
       TlMH.SetNDC()
       TlMH.DrawLatex(0.72,0.89,'m_{H} = '+str(massFilter[0])+' GeV')

       points95.SetFillColor(kYellow);
       points95.Draw("2SAME");
       invpts95.SetFillColor(kYellow);
       invpts95.Draw("2SAME");


       points.SetFillColor(kGreen);
       points.Draw("2SAME");
       invpts.SetFillColor(kGreen);
       invpts.Draw("2SAME");
 
       pexp.SetLineWidth(2) 
       pexp.SetLineStyle(2) 
       pexp.SetMarkerStyle(0) 
       pexp.Draw("PSAME");

       if (not self.blind ) :
         pobs.SetLineWidth(2) 
         pobs.SetLineStyle(1) 
         #pobs.SetMarkerStyle(0) 
         pobs.Draw("PSAME");

       

       #self.plotVertLine('One', 1. , [0,nChann+1] , kRed , 1    , 'One')
       #self.plotAllObj('One')

 
       self.addTitle(self.iTitle,self.iLumi) 
       self.c1.Update() 
       self.Save('LimitCC_'+self.EnergyName(iEnergy)+'_'+iModel+'_'+str(massFilter[0]).replace('.','d'))
       self.Wait()

   def MLToysBB(self,CombList=['vbfbbsplit'],iEnergy=0,iModel='SMHiggs',massFilter=[125],AltModels=['NONE']):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetGridx(1)
       gStyle.SetOptTitle(1)
       gStyle.SetOptStat(1)

       hPull={}
       hBias={}
       hPullSum={}
       hBiasSum={}
       hPullSumErr={}
       hBiasSumErr={}


       for iComb in CombList:
         hPull[iComb] = {}
         hBias[iComb] = {}
         hPullSum[iComb] = {}
         hBiasSum[iComb] = {}
         hPullSumErr[iComb] = {}
         hBiasSumErr[iComb] = {}
         cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
         energyList= combTools.EnergyList_Filter(iEnergy).get()
         energyList=['ALL']
         if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
           TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
         else:
           TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
         print iComb, cardDir, energyList,TargetDir
         for iEnergy in energyList:     
           hPull[iComb][iEnergy] = {}
           hBias[iComb][iEnergy] = {}
           hPullSum[iComb][iEnergy] = {}
           hBiasSum[iComb][iEnergy] = {}
           hPullSumErr[iComb][iEnergy] = {}
           hBiasSumErr[iComb][iEnergy] = {}

           nMass= len(massFilter)
           mMin = massFilter[0]-2.5
           mMax = massFilter[-1]+2.5   
           for iAltModel in AltModels:
             AMFix=''
             if iAltModel != 'NONE' : AMFix= '_Use-'+iAltModel
             pullName='PullSummary_'+iComb+'_'+iEnergy+AMFix+'_'+iModel
             biasName='BiasSummary_'+iComb+'_'+iEnergy+AMFix+'_'+iModel
             hPullSum[iComb][iEnergy][iAltModel] = TH1F(pullName,pullName,nMass,mMin,mMax)
             hBiasSum[iComb][iEnergy][iAltModel] = TH1F(biasName,biasName,nMass,mMin,mMax)
             hPullSumErr[iComb][iEnergy][iAltModel] = TH1F(pullName+'_Err',pullName+'_Err',nMass+2,mMin,mMax)
             hBiasSumErr[iComb][iEnergy][iAltModel] = TH1F(biasName+'_Err',biasName+'_Err',nMass+2,mMin,mMax)

           for iMass in massFilter:
             self.c1.SetGridx(1)
             hPull[iComb][iEnergy][iMass] = {}
             hBias[iComb][iEnergy][iMass] = {}
             for iAltModel in AltModels:
               AMFix=''
               if iAltModel != 'NONE' : AMFix= '_Use-'+iAltModel
               pullName = 'Pull_'+iComb+'_'+iEnergy+AMFix+'_'+iModel+'_'+str(iMass)
               biasName = 'Bias_'+iComb+'_'+iEnergy+AMFix+'_'+iModel+'_'+str(iMass)
               hPull[iComb][iEnergy][iMass][iAltModel] = TH1F(pullName,pullName,100,-10,10)
               hBias[iComb][iEnergy][iMass][iAltModel] = TH1F(biasName,biasName,100,-40,40)
               print AMFix
               if iEnergy == 'ALL' : 
                 fileCmd = 'ls '+TargetDir+'/'+str(iMass)+'/jobs*/higgsCombine_'+iComb+'_'+iModel+AMFix+'_MLToysBB1EXP.job*.MaxLikelihoodFit.mH'+str(iMass)+'.*.root'
               else:
                 fileCmd = 'ls '+TargetDir+'/'+str(iMass)+'/jobs*/higgsCombine_'+iComb+'_'+iEnergy+'_'+iModel+AMFix+'_MLToysBB1EXP.job*.MaxLikelihoodFit.mH'+str(iMass)+'.*.root'
               
               print fileCmd               
               proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
               out, err = proc.communicate()
               FileList=string.split(out)
               print FileList
               for iFile in FileList:
                 try:
                   print iFile
                   fTree = TFile(iFile,'READ')
                   tTree = fTree.Get("limit")
                   for iEv in tTree:
                     print iEv.limit,iEv.limitErr
                     if (iEv.limitErr>0) :
                          hBias[iComb][iEnergy][iMass][iAltModel].Fill(iEv.limit-1.) 
                     if (iEv.limitErr>0) : hPull[iComb][iEnergy][iMass][iAltModel].Fill((iEv.limit-1.)/iEv.limitErr)
                   fTree.Close()
                 except:
                  print 'Could not read ', iFile

               hBias[iComb][iEnergy][iMass][iAltModel].Draw()
               self.Save('Bias_'+iComb+'_'+iEnergy+AMFix+'_'+iModel+'_'+str(iMass))
               hPull[iComb][iEnergy][iMass][iAltModel].Draw()
               self.Save('Pull_'+iComb+'_'+iEnergy+AMFix+'_'+iModel+'_'+str(iMass))

               # Bias Results
               mean      = hBias[iComb][iEnergy][iMass][iAltModel].GetMean();
               errorMean = hBias[iComb][iEnergy][iMass][iAltModel].GetMeanError(); 
               meanRMS   = hBias[iComb][iEnergy][iMass][iAltModel].GetRMS(); 
               iBin = hPullSum[iComb][iEnergy][iAltModel].FindBin(iMass)
               hBiasSum[iComb][iEnergy][iAltModel].SetBinContent(iBin,mean)
               hBiasSum[iComb][iEnergy][iAltModel].SetBinError(iBin,errorMean)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinContent(iBin,0.)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinError(iBin,meanRMS)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinContent(iBin+1,0.)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinContent(iBin+2,0.)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinError(iBin+1,meanRMS)
               hBiasSumErr[iComb][iEnergy][iAltModel].SetBinError(iBin+2,meanRMS)
               # Pull Results
               mean      = hPull[iComb][iEnergy][iMass][iAltModel].GetMean();
               errorMean = hPull[iComb][iEnergy][iMass][iAltModel].GetMeanError(); 
               meanRMS   = hPull[iComb][iEnergy][iMass][iAltModel].GetRMS(); 
               iBin = hPullSum[iComb][iEnergy][iAltModel].FindBin(iMass)
               hPullSum[iComb][iEnergy][iAltModel].SetBinContent(iBin,mean)
               hPullSum[iComb][iEnergy][iAltModel].SetBinError(iBin,errorMean)
               hPullSumErr[iComb][iEnergy][iAltModel].SetBinContent(iBin,0.)
               hPullSumErr[iComb][iEnergy][iAltModel].SetBinError(iBin,meanRMS)

 
           # Bias Summary plot
           Cols=[kBlack,kRed,kBlue,kMagenta,kGreen]
           self.c1.SetGridy(1)
           First=True
           iPos=0
           leg = TLegend(0.20,0.65,0.40,0.89);
           leg.SetLineColor(0);
           leg.SetFillColor(0);
           leg.SetTextSize(0.028)
           leg.SetFillStyle(0)
           leg.SetBorderSize(0)
           leg.SetTextFont (42)


           for iPlot in hPullSum[iComb][iEnergy]:
             if First :
               hBiasSumErr[iComb][iEnergy][iPlot].GetYaxis().SetRangeUser(-5,5)
               hBiasSumErr[iComb][iEnergy][iPlot].GetYaxis().SetRangeUser(-10,10)
               hBiasSumErr[iComb][iEnergy][iPlot].GetYaxis().SetRangeUser(-15,15)
               hBiasSumErr[iComb][iEnergy][iPlot].GetYaxis().SetRangeUser(-20,20)
               hBiasSumErr[iComb][iEnergy][iPlot].SetLineColor(kYellow)
               hBiasSumErr[iComb][iEnergy][iPlot].SetFillColor(kYellow)
               hBiasSumErr[iComb][iEnergy][iPlot].SetMarkerSize(0)
               hBiasSumErr[iComb][iEnergy][iPlot].Draw("e3")
               leg.AddEntry(hBiasSumErr[iComb][iEnergy][iPlot],"RMS","f"); 
               First=False
             #hBiasSum[iComb][iEnergy][iPlot].SetLineColor(Cols[iPos])
             hBiasSum[iComb][iEnergy][iPlot].SetMarkerColor(Cols[iPos])
             hBiasSum[iComb][iEnergy][iPlot].SetMarkerStyle(20+iPos)
             hBiasSum[iComb][iEnergy][iPlot].Draw("psame")
             LEG=iPlot
             if 'altlegend' in self.channels[self.Version][self.combinations[iComb]['channels'][0]][self.combinations[iComb]['energies'][0]] :
               if iPlot in self.channels[self.Version][self.combinations[iComb]['channels'][0]][self.combinations[iComb]['energies'][0]]['altlegend'] : 
                 LEG = self.channels[self.Version][self.combinations[iComb]['channels'][0]][self.combinations[iComb]['energies'][0]]['altlegend'][iPlot]
             leg.AddEntry(hBiasSum[iComb][iEnergy][iPlot],LEG,"p")
             iPos+=1

           leg.Draw("same")
           self.Save('BiasSummary_'+iComb+'_'+iEnergy+'_'+iModel)


   def MDF2DSum(self,iComb,iEnergy,iModel,massFilter,bFast=False):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       Fast=''
       if bFast  : Fast='Fast'
       TargetBase = 'MDFGrid'
       if 'TargetBase' in physmodels[iModel]['MDFTree'] : TargetBase=physmodels[iModel]['MDFTree']['TargetBase']
       if 'POISetKeys' in physmodels[iModel]['MDFTree'] :  
         TargetList=[]
         for iPOISetKey in physmodels[iModel]['MDFTree']['POISetKeys']: 
           Ext             = ''
           if 'Ext' in physmodels[iModel]['MDFTree'][iPOISetKey] : Ext=physmodels[iModel]['MDFTree'][iPOISetKey]['Ext']
           TargetList.append (TargetBase+Fast+'Exp'+Ext+self.postFix)
           if (not self.blind ) : TargetList.append(TargetBase+Fast+'Obs'+Ext+self.postFix)
       else:
         TargetList= [TargetBase+Fast+'Exp'+self.postFix]
         if (not self.blind ) : TargetList.append(TargetBase+Fast+'Obs'+self.postFix)     

       print TargetList

       for iTarget in TargetList:
         for iMass in massList:
           fileName  = TargetDir+'/'+str(iMass)+'/jobs*/higgsCombine_'+iComb
           #fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
           if iEnergy != 0: fileName += '_' + str(iEnergy) + 'TeV'
           fileName += '_'+iModel+'_'+iTarget+'_Points*.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
           fileCmd = 'ls '+fileName 
           print fileCmd
           proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
           out, err = proc.communicate()
           FileList=string.split(out)
           print FileList
           os.system('cd /tmp/xjanssen/ ; rm MDFGrid.tmp.root')
           isFileFirst=True
           for iFile in FileList:
             isFileOk=True
             try:
               if isFileFirst : os.system('cd /tmp/xjanssen/ ; hadd MDFGrid.tmp.root '+iFile+' > /dev/null')
               else           : os.system('cd /tmp/xjanssen/ ; hadd MDFGrid.tmp.root MDFGrid.root '+iFile+' > /dev/null')
             except:  
               isFileOk=False
             if isFileOk :
               os.system('cd /tmp/xjanssen/ ; mv MDFGrid.tmp.root MDFGrid.root') 
               isFileFirst=False 

           fileTarget  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
           fileTarget += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
           print fileTarget
           os.system('cd /tmp/xjanssen/ ; mv MDFGrid.root '+fileTarget) 

   def MDF1D(self,iComb,iEnergy,iModel,massFilter,bFast=False,bSigma=False):
       y2Sigma=3.84
       if bSigma : y2Sigma=4.
       print 'MDF1D',iComb,iEnergy,iModel,massFilter
       Fast=''
       if bFast : Fast='Fast'
       TargetBase = 'MDFGrid'
       if 'TargetBase' in physmodels[iModel]['MDFTree'] : TargetBase=physmodels[iModel]['MDFTree']['TargetBase']
       PlotDic={}
       if 'POISetKeys' in physmodels[iModel]['MDFTree'] :  
         for iPOISetKey in physmodels[iModel]['MDFTree']['POISetKeys']:
           if physmodels[iModel]['MDFTree'][iPOISetKey]['NDim'] == 1 : PlotDic[iPOISetKey] = physmodels[iModel]['MDFTree'][iPOISetKey]
       elif physmodels[iModel]['MDFTree']['NDim'] == 1 : PlotDic['NONE'] = physmodels[iModel]['MDFTree'] 

       for iPlot in PlotDic: 
         print iPlot,' : ',PlotDic[iPlot]
         self.squareCanvas(False,False)
         self.c1.cd()
         self.resetPlot()
         self.xAxisTitle = PlotDic[iPlot]['AxisTitle'][0]
         self.yAxisTitle = '-2 #Delta ln L'
         minXP           = PlotDic[iPlot]['MinPlt'][0]
         maxXP           = PlotDic[iPlot]['MaxPlt'][0]
         minYP           = PlotDic[iPlot]['MinPlt'][1]
         maxYP           = PlotDic[iPlot]['MaxPlt'][1]
         dX              = maxXP-minXP

         Ext             = ''
         if 'Ext' in PlotDic[iPlot] : Ext= PlotDic[iPlot]['Ext']

         # Expected         
         self.readMDF1D(iComb,iEnergy,iModel,massFilter,TargetBase+Fast+'Exp'+Ext+self.postFix,PlotDic[iPlot])
         objNameExp=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+'Exp'+Ext+self.postFix

         # Observed
         if (not self.blind ) : 
         #if (False) : 
           self.readMDF1D(iComb,iEnergy,iModel,massFilter,TargetBase+Fast+'Obs'+Ext+self.postFix,PlotDic[iPlot])
           objNameObs=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+'Obs'+Ext+self.postFix

         # Plot 
         frame = TH1F("Frame","Frame",5,float(minXP),float(maxXP))
         frame.GetXaxis().SetTitle(self.xAxisTitle) 
         frame.GetYaxis().SetTitle(self.yAxisTitle) 
         frame.GetYaxis().SetRangeUser(float(minYP),float(maxYP))
         frame.GetXaxis().SetNdivisions(505)
         frame.GetYaxis().SetNdivisions(505)
         frame.Draw()

         LegList=[]
         if (not self.blind ) : 
         #if (False) :
           self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineWidth(2)
           self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineStyle(1)
           self.Obj2Plot['gr__'+objNameObs]['Obj'].SetLineColor(kBlack)
           self.Obj2Plot['gr__'+objNameObs]['Obj'].Draw("samel") 
           self.Obj2Plot['gr__'+objNameObs]['Legend']= 'Observed'
           LegList.append('gr__'+objNameObs)

         self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineWidth(2)
         self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineStyle(2)
         self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineColor(kBlack)
         self.Obj2Plot['gr__'+objNameExp]['Obj'].Draw("samel")
         self.Obj2Plot['gr__'+objNameExp]['Legend']= 'Expected'
         LegList.append('gr__'+objNameExp)

         Lines=['One','Four']
         self.plotHorizLine('One' , [float(minXP),float(maxXP)] , 1 , kBlack , 9    , 1 , '1sigma')
         self.plotHorizLine('Four', [float(minXP),float(maxXP)] , y2Sigma , kBlack , 9 , 1 , '2sigma')

         # Fing 1/2 Sigma X-ing
         if self.blind : gr = self.Obj2Plot['gr__'+objNameExp]['Obj']
         else          : gr = self.Obj2Plot['gr__'+objNameObs]['Obj']
         hi68 = self.findCrossingOfScan1D(gr, 1.00, False, minXP, maxXP);
         lo68 = self.findCrossingOfScan1D(gr, 1.00, True,  minXP, maxXP);
         hi95 = self.findCrossingOfScan1D(gr, y2Sigma, False, minXP, maxXP);
         lo95 = self.findCrossingOfScan1D(gr, y2Sigma, True,  minXP, maxXP);
         dnll = self.find2DNLLScan1D(gr,1.,minXP, maxXP)

         gr = self.Obj2Plot['gr__'+objNameExp]['Obj']
         hi68Exp = self.findCrossingOfScan1D(gr, 1.00, False, minXP, maxXP);
         lo68Exp = self.findCrossingOfScan1D(gr, 1.00, True,  minXP, maxXP);
         hi95Exp = self.findCrossingOfScan1D(gr, y2Sigma, False, minXP, maxXP);
         lo95Exp = self.findCrossingOfScan1D(gr, y2Sigma, True,  minXP, maxXP);
         dnllExp = self.find2DNLLScan1D(gr,1.,minXP, maxXP)

#        if hi68 >= minXP and hi68 <= maxXP:
#           self.plotVertLine('X1R', hi68 , [0,1] , kRed , 1    , '1sigmaR')
#           Lines.append('X1R')
#        if lo68 >= minXP and lo68 <= maxXP:
#           self.plotVertLine('X1L', lo68 , [0,1] , kRed , 1    , '1sigmaL')
#           Lines.append('X1L')
#        if hi95 >= minXP and hi95 <= maxXP:
#           self.plotVertLine('X2R', hi95 , [0,y2Sigma] , kRed , 1    , '2sigmaR')
#           Lines.append('X2R')
#        if lo95 >= minXP and lo95 <= maxXP:
#           self.plotVertLine('X2L', lo95 , [0,y2Sigma] , kRed , 1    , '2sigmaL')
#           Lines.append('X2L')


         self.plotAllObj(Lines,True)
         if 'jcp' in iComb:
           Decay = 'WW'
           if 'hgg_' in iComb : Decay = '#gamma#gamma'
           Prod = ''
           if '_1' in iComb : Prod = 'q#bar{q}'
           else : 
             if 'fqq0' in TargetBase+Fast+Ext :  Prod = 'gg'
             if 'fqq1' in TargetBase+Fast+Ext :  Prod = 'q#bar{q}'
           if 'SM' in TargetBase+Fast+Ext:
             self.plotObjLeg(LegList,'H #rightarrow '+Decay,'TopLeftLarge')
           else:
             self.plotObjLeg(LegList,Prod+' #rightarrow X('+self.combinations[iComb]['legend']+') #rightarrow '+Decay,'TopLeftLarge')
         else:
           self.plotObjLeg(LegList,self.combinations[iComb]['legend'],'TopLeftLarge')
         self.addTitle(self.iTitle,self.iLumi) 

         self.c1.cd()
         pt = TPaveText(minXP+0.04*dX,1.05,minXP+0.12*dX,1.5);
         pt.SetBorderSize(0);
         pt.SetFillColor(0);
         pt.SetFillStyle(0);
         pt.SetTextFont(42);
         pt.SetTextSize(0.025);
         text = pt.AddText("68% CL");
         pt.Draw();

         pt2 = TPaveText(minXP+0.04*dX,3.94,minXP+0.12*dX,4.3);
         pt2.SetBorderSize(0);
         pt2.SetFillColor(0);
         pt2.SetFillStyle(0);
         pt2.SetTextFont(42);
         pt2.SetTextSize(0.025);
         text = pt2.AddText("95% CL");
         pt2.Draw();

         #self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")
         #self.Obj2Plot['gr0__'+objNameObs]['Obj'].Print()

         PF=''
         if 'PlotPF' in PlotDic[iPlot] : PF= PlotDic[iPlot]['PlotPF']
         self.c1.Update() 
         self.Save(iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+Ext+PF)

         # Save values
         cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype'],'target').get()
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb+'/'+str(massFilter[0])+'/'
         limFile= TargetDir+iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+Ext+PF+'.txt' 
         print limFile
         subfile = open(limFile,'w')
         subfile.write ('Exp  '+ str(lo95Exp) + ' ' + str(lo68Exp) + ' ' + str(hi68Exp) + ' ' + str(hi95Exp)+'\n')
         if not self.blind : 
           subfile.write ('Obs  '+ str(lo95)    + ' ' + str(lo68)    + ' ' + str(hi68)    + ' ' + str(hi95) +'\n' ) 
           subfile.write ('Best '+ str(self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+' '+str(hi68-self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+' '+str(lo68-self.Obj2Plot['gr0__'+objNameObs]['Obj'].GetX()[0])+'\n')
           #subfile.write ('Test '+ str(dnllExp)+' '+str(dnll) +'\n')
         subfile.close()
         self.Wait()

   def MDF1DExp(self,CombList,iEnergy,iModel,massFilter,bFast=False,bSigma=False):
       y2Sigma=3.84
       if bSigma : y2Sigma=4.
       print 'MDF1D',CombList,iEnergy,iModel,massFilter
       Fast=''
       if bFast : Fast='Fast'
       TargetBase = 'MDFGrid'
       if 'TargetBase' in physmodels[iModel]['MDFTree'] : TargetBase=physmodels[iModel]['MDFTree']['TargetBase']
       PlotDic={}
       if 'POISetKeys' in physmodels[iModel]['MDFTree'] :
         for iPOISetKey in physmodels[iModel]['MDFTree']['POISetKeys']:
           if physmodels[iModel]['MDFTree'][iPOISetKey]['NDim'] == 1 : PlotDic[iPOISetKey] = physmodels[iModel]['MDFTree'][iPOISetKey]
       elif physmodels[iModel]['MDFTree']['NDim'] == 1 : PlotDic['NONE'] = physmodels[iModel]['MDFTree']

       for iPlot in PlotDic:
         print iPlot,' : ',PlotDic[iPlot]
         self.squareCanvas(False,False)
         self.c1.cd()
         self.resetPlot()
         self.xAxisTitle = PlotDic[iPlot]['AxisTitle'][0]
         self.yAxisTitle = '-2 #Delta ln L'
         minXP           = PlotDic[iPlot]['MinPlt'][0]
         maxXP           = PlotDic[iPlot]['MaxPlt'][0]
         minYP           = PlotDic[iPlot]['MinPlt'][1]
         maxYP           = PlotDic[iPlot]['MaxPlt'][1]
         dX              = maxXP-minXP

         Ext             = ''
         if 'Ext' in PlotDic[iPlot] : Ext= PlotDic[iPlot]['Ext']


         LCol = [ kBlack , kBlack , kBlue , kBlue ,  kRed , kRed , kMagenta , kMagenta ,  kGreen , kGreen , kOrange , kOrange ]
         LTyp = [    1   ,    2   ,   1   ,   2   ,   1   ,  2   ,    1     ,    2     ,     1   ,   2    ,    1    ,   2     ]

         iLC=0
         LegList=[]
         List='Exp'
         for iComb in CombList: 
           List+='_'+iComb
           self.readMDF1D(iComb,iEnergy,iModel,massFilter,TargetBase+Fast+'Exp'+Ext+self.postFix,PlotDic[iPlot])
           objNameExp=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+'Exp'+Ext+self.postFix

           self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineWidth(2)
           self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineStyle( LTyp[iLC] )
           self.Obj2Plot['gr__'+objNameExp]['Obj'].SetLineColor( LCol[iLC] )
           #self.Obj2Plot['gr__'+objNameExp]['Obj'].Draw("samel")
           self.Obj2Plot['gr__'+objNameExp]['Legend']= self.combinations[iComb]['legend']
           LegList.append('gr__'+objNameExp) 
           iLC+=1 

         # Plot
         frame = TH1F("Frame","Frame",5,float(minXP),float(maxXP))
         frame.GetXaxis().SetTitle(self.xAxisTitle)
         frame.GetYaxis().SetTitle(self.yAxisTitle)
         frame.GetYaxis().SetRangeUser(float(minYP),float(maxYP))
         frame.GetXaxis().SetNdivisions(505)
         frame.GetYaxis().SetNdivisions(505)
         frame.Draw()


         Lines=['One','Four']
         self.plotHorizLine('One' , [float(minXP),float(maxXP)] , 1 , kBlack , 9    , 1 , '1sigma')
         self.plotHorizLine('Four', [float(minXP),float(maxXP)] , y2Sigma , kBlack , 9 , 1 , '2sigma')

         self.plotAllObj(LegList,True)
         self.plotAllObj(Lines,True)
         self.plotObjLeg(LegList,'Expected','TopLeftLarge')
         self.addTitle(self.iTitle,self.iLumi)
         
         self.c1.cd()
         pt = TPaveText(minXP+0.04*dX,1.05,minXP+0.12*dX,1.5);
         pt.SetBorderSize(0);
         pt.SetFillColor(0);
         pt.SetFillStyle(0);
         pt.SetTextFont(42);
         pt.SetTextSize(0.025);
         text = pt.AddText("68% CL");
         pt.Draw();

         pt2 = TPaveText(minXP+0.04*dX,3.94,minXP+0.12*dX,4.3);
         pt2.SetBorderSize(0);
         pt2.SetFillColor(0);
         pt2.SetFillStyle(0);
         pt2.SetTextFont(42);
         pt2.SetTextSize(0.025);
         text = pt2.AddText("95% CL");
         pt2.Draw();

         PF=''
         if 'PlotPF' in PlotDic[iPlot] : PF= PlotDic[iPlot]['PlotPF']
         self.c1.Update()
         self.Save(List+'_'+str(iEnergy)+'_'+iModel+'_'+TargetBase+Fast+Ext+PF) 





   def MDF2D(self,iComb,iEnergy,iModel,massFilter,bSimple=False,bFast=False):
       print 'MDF2D',iComb,iEnergy,iModel,massFilter
       Fast=''
       if bFast : Fast='Fast'

       self.squareCanvas(False,False)
       self.c1.cd()
       self.c1.SetLeftMargin(0.15) 
       self.c1.SetRightMargin(0.2) 
       self.c1.SetTopMargin(0.07) 
       #self.c1.SetLogz()
       self.resetPlot()
       
       self.xAxisTitle = physmodels[iModel]['MDFTree']['AxisTitle'][0]
       self.yAxisTitle = physmodels[iModel]['MDFTree']['AxisTitle'][1]

       minXP=physmodels[iModel]['MDFTree']['MinPlt'][0]
       minYP=physmodels[iModel]['MDFTree']['MinPlt'][1]
       maxXP=physmodels[iModel]['MDFTree']['MaxPlt'][0]
       maxYP=physmodels[iModel]['MDFTree']['MaxPlt'][1]

       # Expected
       if bSimple:
         self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFSnglExp68',algo='Single')
         self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFCrossExp68',algo='Cross')     
       self.readMDFGrid(iComb,iEnergy,iModel,massFilter,iTarget='MDFGrid'+Fast+'Exp'+self.postFix)
       objNameExp=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+'MDFGrid'+Fast+'Exp'+self.postFix
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].Draw("colz")  
       self.Obj2Plot['c68__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['c95__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].Draw("samep")  
       if bSimple:
          objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFSnglExp68_Single'
          self.Obj2Plot['c1d__'+objName]['Obj'].Draw("lp")
          objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFCrossExp68_Cross'
          self.Obj2Plot['c2d__'+objName]['Obj'].Draw("p")
       self.addTitle(self.iTitle,self.iLumi) 
       self.c1.Update() 
       self.Save(objNameExp)
       #self.Wait()

       # Observed 
       if (not self.blind ) : 
         if bSimple:
           self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFSnglObs68',algo='Single')
           self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFCrossObs68',algo='Cross')
         self.readMDFGrid(iComb,iEnergy,iModel,massFilter,iTarget='MDFGrid'+Fast+'Obs'+self.postFix) 
         objNameObs=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+'MDFGrid'+Fast+'Obs'+self.postFix
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetRangeUser(float(minXP),float(maxXP))
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetRangeUser(float(minYP),float(maxYP))
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].Draw("colz")  
         self.Obj2Plot['c68__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['c95__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")  
         if bSimple:
            objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFSnglObs68_Single'
            self.Obj2Plot['c1d__'+objName]['Obj'].Draw("lp")
            objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFCrossObs68_Cross'
            self.Obj2Plot['c2d__'+objName]['Obj'].Draw("p")
         self.addTitle(self.iTitle,self.iLumi) 
         self.c1.Update() 
         self.Save(objNameObs)
         #self.Wait()

       
       self.c1.SetRightMargin(0.05)
       self.c1.SetLogz(False)
       minXP=physmodels[iModel]['MDFTree']['MinPlt'][0]
       minYP=physmodels[iModel]['MDFTree']['MinPlt'][1]
       maxXP=physmodels[iModel]['MDFTree']['MaxPlt'][0]
       maxYP=physmodels[iModel]['MDFTree']['MaxPlt'][1]

       frame = TH1F("Frame","Frame",5,float(minXP),float(maxXP))
       frame.GetXaxis().SetTitle(self.xAxisTitle) 
       frame.GetYaxis().SetTitle(self.yAxisTitle) 
       frame.GetYaxis().SetRangeUser(float(minYP),float(maxYP))
       frame.GetXaxis().SetNdivisions(505)
       frame.GetYaxis().SetNdivisions(505)
       frame.Draw()
       self.Obj2Plot['c68__'+objNameExp]['Legend'] = '68% CL Expected'
       self.Obj2Plot['c95__'+objNameExp]['Legend'] = '95% CL Expected'
       self.Obj2Plot['c68__'+objNameExp]['Obj'].Draw("same")  
       for X in TIter(self.Obj2Plot['c95__'+objNameExp]['Obj']) : X.SetLineStyle(2) 
       self.Obj2Plot['c95__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].SetMarkerStyle(22)
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].Draw("samep")  
       self.Obj2Plot['gr0__'+objNameExp]['Legend']= 'Exp. for SM H'
       LegList = ['gr0__'+objNameExp,'c68__'+objNameExp,'c95__'+objNameExp]
    
       if (not self.blind ) :
         self.Obj2Plot['c68__'+objNameObs]['Legend'] = '68% CL Observed'
         self.Obj2Plot['c95__'+objNameObs]['Legend'] = '95% CL Observed'
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].SetMarkerColor(kRed)  
         for X in TIter(self.Obj2Plot['c68__'+objNameObs]['Obj']) : X.SetLineColor(kRed) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineColor(kRed) 
         for X in TIter(self.Obj2Plot['c68__'+objNameObs]['Obj']) : X.SetLineWidth(3) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineWidth(3) 
         for X in TIter(self.Obj2Plot['c95__'+objNameObs]['Obj']) : X.SetLineStyle(2) 
         self.Obj2Plot['c68__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['c95__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")  
         self.Obj2Plot['gr0__'+objNameObs]['Legend']= 'Observed'
         LegList = ['gr0__'+objNameObs,'c68__'+objNameObs,'c95__'+objNameObs,'gr0__'+objNameExp,'c68__'+objNameExp,'c95__'+objNameExp]
       

       if iModel == "rVrFXSH" :
         self.plotObjLeg(LegList,self.combinations[iComb]['legend'],'TopRight')
       else:
         self.plotObjLeg(LegList,self.combinations[iComb]['legend'],'TopLeft')
       

       self.addTitle(self.iTitle,self.iLumi) 
       self.c1.Update() 
       self.Save(iComb+'_'+str(iEnergy)+'_'+iModel+'_'+'MDFGrid'+Fast)
 


      # for iObj in self.Obj2Plot:
      #   print iObj, self.Obj2Plot[iObj]['Obj']  
      

       return


   def findResValbyM(self,iComb='hww012j_vh3l_vh2j_zh3l2j_shape',iEnergy=0,iModel='SMHiggs',mass=125.,iTarget='ACLsExp',what='Val'):
       iPos=-1
       for iMass in self.Results[iComb][iEnergy][iModel][iTarget]['mass']:
         iPos+=1
         if iMass == mass and what in self.Results[iComb][iEnergy][iModel][iTarget] : 
           return self.Results[iComb][iEnergy][iModel][iTarget][what][iPos]
       return -99.

   def JCPSum(self,iComb,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       #iTarget=iModel
       #iTarget='JCPFQQFixRange'
       #iTarget='JCPfixmu'
       #iTarget='JCP'
       os.system('mkdir -p /tmp/xjanssen/'+iComb)
       for iMass in massList:
         paramSet = self.ParamSet_Maker(iModel,iTarget)
         for iSet in range(0,len(paramSet['values'])) :
             ParString=''
             for iPar in range(0,len(paramSet['names'])) :
               parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
               ParString += '_'+paramSet['names'][iPar]+str(parVal)

         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
         #for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
           #for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :


             FileList=[]
             dirName = TargetDir+'/'+str(iMass)+'/'
             dirCmd  = 'ls '+dirName+' | grep jobs | sed "s:/::" '
             proc=subprocess.Popen(dirCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
             out, err = proc.communicate()
             DirList=string.split(out)
             for iDir in DirList:
               fileName  = TargetDir+'/'+str(iMass)+'/'+iDir+'/higgsCombine_'+iComb
               if iEnergy == 7 : fileName += '_7TeV'
               if iEnergy == 8 : fileName += '_8TeV'
               fileName += '_'+iModel+'_'+iTarget+ParString+'.job*.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.*.root'
               fileCmd = 'ls '+fileName # +' '+fileName.replace('higgsCombine','jobs*/higgsCombine')  
               proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
               out, err = proc.communicate()
               FileList+=string.split(out)
             FileListGood = {}
             #print fileCmd
             print FileList
             os.system('cd /tmp/xjanssen/'+iComb+'/ ; rm JCPToys.tmp.root')
             isFileFirst=True
             iCount = 0
             for iFile in FileList:
               isFileOk=True
               fileCmd='ls -l '+iFile+' | awk \'{print $5}\' '
               proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
               out, err = proc.communicate()
               #print int(out)
               if int(out) > 1400: 
                 iCount +=1
                 iBlock = (iCount/500)
                 if not iBlock in FileListGood : FileListGood[iBlock] = []
                 FileListGood[iBlock].append(iFile)
#                try:
#                  if isFileFirst : os.system('cd /tmp/xjanssen/'+iComb+'/ ; hadd JCPToys.tmp.root '+iFile+' > /dev/null')
#                  else           : os.system('cd /tmp/xjanssen/'+iComb+'/ ; hadd JCPToys.tmp.root JCPToys.root '+iFile+' > /dev/null')
#                except:  
#                  isFileOk=False
#                if isFileOk :
#                  os.system('cd /tmp/xjanssen/'+iComb+'/ ; mv JCPToys.tmp.root JCPToys.root') 
#                  isFileFirst=False 

             os.system('cd /tmp/xjanssen/'+iComb+'/ ; rm hi*' ) 
             for iBlock in FileListGood:
               fileTarget  = 'higgsCombine_'+iComb
               if iEnergy == 7 : fileTarget += '_7TeV'
               if iEnergy == 8 : fileTarget += '_8TeV'
               fileTarget += '_'+iModel+'_'+iTarget+ParString+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.Block'+str(iBlock)+'.root'
               print fileTarget 
               command = 'cd /tmp/xjanssen/'+iComb+'/ ; hadd -f '+fileTarget
               for iFile in FileListGood[iBlock] : command += ' '+iFile 
               print '---------------------'
               #print command 
               os.system(command)



             fileTarget  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : fileTarget += '_7TeV'
             if iEnergy == 8 : fileTarget += '_8TeV'
             fileTarget += '_'+iModel+'_'+iTarget+ParString+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
             command = 'cd /tmp/xjanssen/'+iComb+'/ ; hadd -f '+fileTarget 
             for iBlock in FileListGood: 
               fileSource  = 'higgsCombine_'+iComb
               if iEnergy == 7 : fileSource += '_7TeV'
               if iEnergy == 8 : fileSource += '_8TeV'
               fileSource += '_'+iModel+'_'+iTarget+ParString+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.Block'+str(iBlock)+'.root'
               command += ' '+fileSource
             os.system(command) 

#            print fileTarget
#            os.system('cd /tmp/xjanssen/'+iComb+'/ ; mv JCPToys.root '+fileTarget) 


   def JCPClean(self,iComb,iEnergy,iModel,iTarget,massFilter):

       # First Sum to avoid catastrophy !
       self.JCPSum(iComb,iEnergy,iModel,iTarget,massFilter)

       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       os.system('mkdir -p /tmp/xjanssen/'+iComb)
       for iMass in massList:
         paramSet = self.ParamSet_Maker(iModel,iTarget)
         for iSet in range(0,len(paramSet['values'])) :
             ParString=''
             for iPar in range(0,len(paramSet['names'])) :
               parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
               ParString += '_'+paramSet['names'][iPar]+str(parVal)

             FileList=[]
             dirName = TargetDir+'/'+str(iMass)+'/'
             dirCmd  = 'ls '+dirName+' | grep jobs | sed "s:/::" '
             proc=subprocess.Popen(dirCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
             out, err = proc.communicate()
             DirList=string.split(out)
             for iDir in DirList:
               if iDir != 'jobsSum' :
                 os.system('rm '+TargetDir+'/'+str(iMass)+'/'+iDir+'/*.log')
                 fileName  = TargetDir+'/'+str(iMass)+'/'+iDir+'/higgsCombine_'+iComb
                 if iEnergy == 7 : fileName += '_7TeV'
                 if iEnergy == 8 : fileName += '_8TeV'
                 fileName += '_'+iModel+'_'+iTarget+ParString+'.job*.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.*.root'
                 fileCmd = 'ls '+fileName # +' '+fileName.replace('higgsCombine','jobs*/higgsCombine')  
                 proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
                 out, err = proc.communicate()
                 FileList+=string.split(out)
             FileListGood = {}
             #print fileCmd
             print FileList

             for iFile in FileList:
               isFileOk=True
               fileCmd='ls -l '+iFile+' | awk \'{print $5}\' '
               proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
               out, err = proc.communicate()
               if int(out) > 1400: os.system('rm '+iFile)

             # Save Previous Toys 

             fileSource  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : fileSource += '_7TeV'
             if iEnergy == 8 : fileSource += '_8TeV'
             fileSource += '_'+iModel+'_'+iTarget+ParString+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'

             fileTarget  = TargetDir+'/'+str(iMass)+'/jobsSum/higgsCombine_'+iComb
             if iEnergy == 7 : fileTarget += '_7TeV'
             if iEnergy == 8 : fileTarget += '_8TeV'
             fileTarget += '_'+iModel+'_'+iTarget+ParString+'.jobSum.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.PreviousRuns.root'
             os.system('mkdir -p '+TargetDir+'/'+str(iMass)+'/jobsSum')
             os.system('cp '+fileSource+' '+fileTarget)

   def JCPFit(self,iComb,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       #iTarget=iModel
       #iTarget='JCPFQQFixRange'
       #iTarget='JCP'
       #iTarget='JCPfixmu'
       for iMass in massList:
         paramSet = self.ParamSet_Maker(iModel,iTarget)
         for iSet in range(0,len(paramSet['values'])) :
             ParString=''
             for iPar in range(0,len(paramSet['names'])) :
               parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
               ParString += '_'+paramSet['names'][iPar]+str(parVal)
         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
         #for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
         #  for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :

             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : fileName += '_7TeV'
             if iEnergy == 8 : fileName += '_8TeV'
             fileName += '_'+iModel+'_'+iTarget+ParString+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
             fileTarget  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : fileTarget += '_7TeV'
             if iEnergy == 8 : fileTarget += '_8TeV'
             fileTarget += '_'+iModel+'_'+iTarget+ParString+'_qmu_mH'+str(iMass).replace('.','d')+'.root'
             print 'Fitting :',fileName    
             os.system('root -q -b '+fileName+' "${CMSSW_BASE}/src/HiggsAnalysis/CombinedLimit/test/plotting/hypoTestResultTree.cxx(\\"'+fileTarget+'\\",'+str(iMass)+',1,\\"x\\")"')



   def JCPPlt(self,iComb,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb


       #jcp='undef'
       #if '2pm' in iComb : jcp='2pm'
       #if '0m'  in iComb : 
       #  jcp='0m'
#      #  targets[iTarget]['JobsParam']['FQQ'] = [0.]
       #print iComb , iComb.split('_')[-1]
       jcp=iComb.split('_')[-1] 

       #iTarget=iModel
       #iTarget='JCPFQQFixRange'
       #iTarget='JCPfixmu'
       #iTarget='JCP'
       for iMass in massList:
         paramSet = self.ParamSet_Maker(iModel,iTarget)
         iFITNUIS = -1
         iFQQ = 0.0
         for iSet in range(0,len(paramSet['values'])) :
           ParString=''
           ParSummTxt=''
           for iPar in range(0,len(paramSet['names'])) :
             parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
             ParString += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal) 
             if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
             if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]

#      for iMass in massList:
         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
#        for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :

           if not iFITNUISnew == iFITNUIS :
             iFITNUIS = iFITNUISnew
             tableName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : tableName += '_7TeV'
             if iEnergy == 8 : tableName += '_8TeV'
             tableName += '_'+iModel+'_'+iTarget+ParSummTxt+'_ResultsSummary_mH'+str(iMass).replace('.','d')+'.txt' 
             subfile = open(tableName,'w')
             subfile.write('#Fqq     sObsSM   sExpSM  sObsALT  sExpALT CLsRatio     qObs   MeanSM medianSM   qSM68m   qSM68p   qSM95m   qSM95p  MeanALTmedianALT  qALT68m  qALT68p  qALT95m  qALT95p \n')

           #for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
           if True :
             unblind=0
             if not self.blind : unblind=1
             workDir   = TargetDir+'/'+str(iMass) 
             print workDir
             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : fileName += '_7TeV'
             if iEnergy == 8 : fileName += '_8TeV'
             fileName += '_'+iModel+'_'+iTarget+ParString+'_qmu_mH'+str(iMass).replace('.','d')+'.root'
             logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             if iEnergy == 7 : logName += '_7TeV'
             if iEnergy == 8 : logName += '_8TeV'
             logName  += '_'+iModel+'_'+iTarget+ParString+'.Results.mH'+str(iMass)+'.txt'
             os.system('cd '+workDir+'; root -q -b /afs/cern.ch/user/x/xjanssen/cms/HWW2012/ToolBox/SignalSeparation/extractSignificanceStats.C+"(\\"'+fileName+'\\",2,'+str(unblind)+')" > '+logName)
             energyExt = ''
             if iEnergy == 7 : energyExt += '_7TeV'
             if iEnergy == 8 : energyExt += '_8TeV'
             baseName  = 'sigsep_'+iModel+'_'+iTarget+energyExt+ParString
             baseName  = baseName.replace('.','_')
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.eps  '+workDir+'/'+baseName+'.epf') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.png  '+workDir+'/'+baseName+'.png') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.pdf  '+workDir+'/'+baseName+'.pdf') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.root '+workDir+'/'+baseName+'.root') 

             mText  = self.combinations[iComb]['legend']
             if jcp == '1hzz' or jcp == '1qqb' :
               if   iFQQ == 0.   : mText = '1^{-}'
               elif iFQQ == 1.   : mText = '1^{+}'

             #if jcp == '0m':
             #  if iFQQ == 0.   : mText = '0^{-}'
               #if iFQQ == 0.25 : mText = '0^{-}(f_{q#bar{q}}=25%)'
               #if iFQQ == 0.50 : mText = '0^{-}(f_{q#bar{q}}=50%)'
               #if iFQQ == 0.75 : mText = '0^{-}(f_{q#bar{q}}=75%)'
               #if iFQQ == 1.   : mText = '0^{-}(f_{q#bar{q}}=100%)'
             #if jcp == '2pm':
             #  if iFQQ == 0.   : mText = '2^{+}_{min}(f_{q#bar{q}}=0%)'
             #  if iFQQ == 0.25 : mText = '2^{+}_{min}(f_{q#bar{q}}=25%)'
             #  if iFQQ == 0.50 : mText = '2^{+}_{min}(f_{q#bar{q}}=50%)'
             #  if iFQQ == 0.75 : mText = '2^{+}_{min}(f_{q#bar{q}}=75%)'
             #  if iFQQ == 1.   : mText = '2^{+}_{min}(f_{q#bar{q}}=100%)'
             #else : mText = 'ALT'
             #if iEnergy == 7 : mText += '_7TeV'
             #if iEnergy == 8 : mText += '_8TeV'
             print "-----------------------------------------------------------------------"
             os.system('echo \'---------------------------- Andre Macro ------------------------\' >> '+logName)  
             iLumiLocal=0

             print jcp , iFQQ

             chText  = ''
             chText2 = ''
             if jcp == '1hzz' or jcp == '1qqb' or jcp == '1m' or jcp == '1p' or jcp == '1mix' : 
               chText += 'q#bar{q} #rightarrow X('+mText+') #rightarrow '
               chText2 += 'q#bar{q} #rightarrow X('+mText+') #rightarrow '
             else: 
               if   iFQQ == 1. or jcp == 'qqb'  : chText += 'q#bar{q} #rightarrow X('+mText+') #rightarrow '
               elif iFQQ == 0.   : chText += 'gg #rightarrow X('+mText+') #rightarrow '
               else              : chText += 'gg/q#bar{q}(f_{q#bar{q}}='+str(iFQQ)+') #rightarrow X('+mText+') #rightarrow '   
               #if jcp == 'qqb' : chText += 'q#bar{q} #rightarrow X('+mText+') #rightarrow '
               chText2 += 'X('+mText+') #rightarrow ' 

             if   'hgghzzhww' in iComb : 
               chText  += 'ZZ + WW + #gamma#gamma'
               chText2 += 'ZZ + WW + #gamma#gamma'
               iLumiLocal=1 
             elif   'hwwhzz' in iComb : 
               #chText += 'ZZ #rightarrow 4l + WW #rightarrow 2l2#nu'
               chText  += 'ZZ + WW'
               chText2 += 'ZZ + WW'
               iLumiLocal=1 
             elif 'hww'    in iComb : 
               chText  += 'WW'
               chText2 += 'WW'
               if iEnergy == 7 : iLumiLocal = 7
               if iEnergy == 8 : iLumiLocal = 8
               iLumiLocal = 0
             elif 'hzz'    in iComb : 
               chText  += 'ZZ'
               chText2 += 'ZZ'
               iLumiLocal=1 
             elif 'hgg'    in iComb :
               chText  += '#gamma#gamma'
               chText2 += '#gamma#gamma'
               iLumiLocal=1

             # Status: 0=Published 1=Unpub 2=Prel   
             iStatus=1
             iStatus2=1
             if 'float' in iTarget :
               if    'hgghzzhww' in iComb :
                 if '_gg'  in iComb : iStatus=2
                 if '_dec' in iComb : iStatus2=0
               elif  'hwwhzz'    in iComb :
                 if  '1hzz' in iComb :
                   # 1+ in paper
                   if iFQQ == 1. : iStatus=0
                 if  '2pm'  in iComb :
                   # gg->X + fqq scan
                   if '_gg'  in iComb : iStatus=0
                   if '_dec' in iComb : iStatus2=0
                 if  '2ph2'  in  iComb :
                   # gg->X
                   if '_dec' in  iComb :
                     if iFQQ == 0. : iStatus=0 
                   if '_gg'  in  iComb : iStatus=0
               elif  'hww01'    in iComb :
                 if  '1p'    in  iComb : iStatus=0
                 if  '2ph2'  in  iComb :
                   if iFQQ == 0. : iStatus=0 
                   iStatus2=0
                 

             if iFITNUIS == -1 :
               os.system('cd '+workDir+'; root -q -b /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/plotting/extractSignificanceStats.C+"(false,\\"'+mText+'\\",\\"'+jcp+'\\",\\"'+fileName+'\\",\\"'+fileName.replace('.root','')+'\\",\\"'+chText+'\\",'+str(iLumiLocal)+','+str(iStatus)+')" ')
             else :
               if self.blind : 
                 os.system('cd '+workDir+'; root -q -b /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/plotting/extractSignificanceStats.C+"(false,\\"'+mText+'\\",\\"'+jcp+'\\",\\"'+fileName+'\\",\\"'+fileName.replace('.root','')+'\\",\\"'+chText+'\\",'+str(iLumiLocal)+','+str(iStatus)+')" >>'+logName)
               else:
                 os.system('cd '+workDir+'; root -q -b /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/plotting/extractSignificanceStats.C+"(true,\\"'+mText+'\\",\\"'+jcp+'\\",\\"'+fileName+'\\",\\"'+fileName.replace('.root','')+'\\",\\"'+chText+'\\",'+str(iLumiLocal)+','+str(iStatus)+')" >>'+logName)
             for line in open(logName):
               if "RESULTS_SUMMARY" in line:
                 print "%-4s %s"%(str(iFQQ),line.replace('RESULTS_SUMMARY',''))
                 subfile.write("%-4s %s"%(str(iFQQ),line.replace('RESULTS_SUMMARY','')))

           if not 'FQQ' in targets[iTarget]['JobsParam'] :
             subfile.close()
           
           if 'FQQ' in targets[iTarget]['JobsParam'] :
             if iFQQ == targets[iTarget]['JobsParam']['FQQ'][-1] :
              subfile.close()
              if iFITNUIS == 0 :
               self.plotFqqLim(tableName,0,iLumiLocal,massFilter[0],jcp,mText,chText2,iStatus2) 
              else:
               self.plotFqqLim(tableName,unblind,iLumiLocal,massFilter[0],jcp,mText,chText2,iStatus2) 

   def plotFqqLim(self,limFile,unblind,iLumiLocal,mass,jcp,mText,title,iStatus,iRange=1):
  
     print "limFile = "+limFile
     self.squareCanvas(False,False)  
     self.c1.cd()
     self.c1.SetLeftMargin(0.15) 


     pt = TPaveText(0.15,0.93,0.45,0.99,"NDC");
     pt.SetBorderSize(0);
     pt.SetTextAlign(12);
     pt.SetFillStyle(0);
     pt.SetTextFont(61);
     pt.SetTextSize(0.045);
     pt.AddText(0.01,0.45,"CMS");

     pt2 = TPaveText(0.85,0.93,0.45,0.99,"NDC");
     pt2.SetBorderSize(0);
     pt2.SetTextAlign(12);
     pt2.SetFillStyle(0);
     pt2.SetTextFont(42);
     pt2.SetTextSize(0.030); 
     if   iLumiLocal == 0 : pt2.AddText(0.25,0.35,"19.4 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)")
     elif iLumiLocal == 1 : pt2.AddText(0.25,0.35,"19.7 fb^{-1} (8 TeV) + 5.1 fb^{-1} (7 TeV)")
     elif iLumiLocal == 7 : pt2.AddText(0.45,0.35,"4.9 fb^{-1} (7 TeV)")
     elif iLumiLocal == 8 : pt2.AddText(0.45,0.35,"19.5 fb^{-1} (8 TeV)")

     pt3= TPaveText(0.250,0.91,0.45,0.99,"NDC");
     pt3.SetBorderSize(0);
     pt3.SetTextAlign(12);
     pt3.SetFillStyle(0);
     pt3.SetTextFont(52);
     pt3.SetTextSize(0.03);
     if ( iStatus == 1 ) : pt3.AddText(0.01,0.5,"Unpublished");
     if ( iStatus == 2 ) : pt3.AddText(0.01,0.5,"Preliminary");

#    pt = TPaveText(0.15,0.91,0.45,0.99,"NDC");
#    pt.SetTextAlign(12);
#    pt.SetTextSize(0.045);
#    pt.SetFillColor(0);
#    pt.SetTextFont(61);
#    pt.AddText("CMS");
#    pt.SetBorderSize(0);
#    pt2 = TPaveText(0.85,0.91,0.9,0.99,"NDC");
#    pt2.SetTextAlign(42);
#    pt2.SetTextSize(0.035);
#    pt2.SetFillColor(0);
#    if   iLumiLocal == 0 : pt2.AddText("19.4 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)")
#    elif iLumiLocal == 1 : pt2.AddText("19.7 fb^{-1} (8 TeV) + 5.1 fb^{-1} (7 TeV)")
#    elif iLumiLocal == 7 : pt2.AddText("4.9 fb^{-1} (7 TeV)")
#    elif iLumiLocal == 8 : pt2.AddText("19.5 fb^{-1} (8 TeV)")

     #pt2.AddText(" #sqrt{s} = 7 TeV, L = 5.051 fb^{-1}; #sqrt{s} = 8 TeV, L = 30.0 fb^{-1}");
     #if float(lumi)<10.:
     #  pt2.AddText(" #sqrt{s} = 7 TeV, L = 4.9 fb^{-1}");
     #elif float(lumi)<20.:
     #  pt2.AddText(" #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}");
     #else:
     #  pt2.AddText(" #sqrt{s} = 7 TeV, L = 4.9 fb^{-1}; #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}"); 
     #pt2.AddText("19.5 fb^{-1} (8 TeV)");
     #pt2.SetBorderSize(0);
   
     grSM = TGraph()
     grSM68 = TGraphAsymmErrors()
     grSM95 = TGraphAsymmErrors()
     grGRAV = TGraph()
     grGR68 = TGraphAsymmErrors()
     grGR95 = TGraphAsymmErrors()
     grData = TGraph()
   
     # Mean
     #iSM=8
     #iGR=14
     # Median
     iSM=8
     iGR=14
     p=0
     for line in open(limFile):
       if not "#" in line: 
         vec = line.split()
         grSM.SetPoint(p,float(vec[0]),float(vec[iSM]))
         grSM68.SetPoint(p,float(vec[0]),float(vec[iSM]))
         grSM95.SetPoint(p,float(vec[0]),float(vec[iSM]))
         grSM68.SetPointError(p,0.,0.,abs(float(vec[iSM])-float(vec[9])),abs(float(vec[iSM])-float(vec[10])))
         grSM95.SetPointError(p,0.,0.,abs(float(vec[iSM])-float(vec[11])),abs(float(vec[iSM])-float(vec[12])))
         grGRAV.SetPoint(p,float(vec[0]),float(vec[iGR]))
         grGR68.SetPoint(p,float(vec[0]),float(vec[iGR]))
         grGR95.SetPoint(p,float(vec[0]),float(vec[iGR]))
         grGR68.SetPointError(p,0.,0.,abs(float(vec[iGR])-float(vec[15])),abs(float(vec[iGR])-float(vec[16])))
         grGR95.SetPointError(p,0.,0.,abs(float(vec[iGR])-float(vec[17])),abs(float(vec[iGR])-float(vec[18])))
         grData.SetPoint(p,float(vec[0]),float(vec[6]))
         p+=1
   
     grData.SetMarkerStyle(kFullCircle)
     grData.SetLineWidth(2)
     grData.SetMarkerSize(1.8)
     
     grSM.SetMarkerStyle(kFullSquare)
     grSM.SetMarkerColor(kRed)
     #grSM.SetLineStyle(kDashed)
     grSM.SetLineWidth(2)
     grSM.SetLineColor(kRed)
     grSM.SetMarkerSize(1.8)  
 
     grSM95.SetLineColor(kYellow)
     grSM95.SetFillColor(kYellow)
     grSM68.SetLineColor(kGreen)
     grSM68.SetFillColor(kGreen)
       

     grGRAV.SetMarkerStyle(kFullTriangleUp)
     grGRAV.SetMarkerColor(kBlue)
     #grGRAV.SetLineStyle(kDashed)
     grGRAV.SetLineWidth(2)
     grGRAV.SetLineColor(kBlue)
     grGRAV.SetMarkerSize(1.8)   

     grGR68.SetMarkerColor(kRed)
     grGR68.SetLineWidth(2)
     grGR68.SetLineColor(kRed)
     grGR68.SetFillColor(kRed)
     grGR68.SetLineStyle(kDashed)
     grGR68.SetFillStyle(3356)
   
     grGR95.SetMarkerColor(kBlack)
     grGR95.SetLineWidth(2)
     grGR95.SetLineColor(kBlue)
     grGR95.SetFillColor(kBlack)
     grGR95.SetLineStyle(kDotted)
     grGR95.SetFillStyle(3365)
   
     ymin=-20.
     ymax=50.
     if iRange == 2:
       ymin=-40.
       ymax=70.
     if iRange == 3:
       ymin=-50.
       ymax=100.  
 
     if 'jcp_2' in limFile : fText= 'f(q#bar{q})' 
     else : fText= 'f_{b2}^{WW}'
     #dummyHist = TH1F("d",";f(q#bar{q}) ;-2 ln (L_{"+mText+"}/L_{0^{+}}) ",100,0,1)
     dummyHist = TH1F("d",";"+fText+" ;-2 #times ln (L_{J^{P}}/L_{0^{+}}) ",100,0,1)
     dummyHist.SetMinimum(ymin)
     dummyHist.SetMaximum(ymax)
     dummyHist.SetStats(0)
     dummyHist.GetXaxis().SetLabelFont (   42)
     dummyHist.GetYaxis().SetLabelFont (   42)
     dummyHist.GetXaxis().SetTitleFont (   42)
     dummyHist.GetYaxis().SetTitleFont (   42)
     dummyHist.GetXaxis().SetTitleOffset( 1.2)
     dummyHist.GetYaxis().SetTitleOffset( 1.2)
     dummyHist.GetXaxis().SetTitleSize (0.050)
     dummyHist.GetYaxis().SetTitleSize (0.050)
     dummyHist.GetXaxis().SetLabelSize (0.045)
     dummyHist.GetYaxis().SetLabelSize (0.045)

     dummyHist.Draw("AXIS")
   
     #leg = TLegend(0.20,0.65,0.40,0.89);
     #if   'hgghzzhww' in limFile : leg.SetHeader("#gamma#gamma + ZZ #rightarrow 4l + WW #rightarrow 2l2#nu ")
     #elif 'hwwhzz'    in limFile : leg.SetHeader("ZZ #rightarrow 4l + WW #rightarrow 2l2#nu ")
     #elif 'hww'       in limFile : leg.SetHeader("WW #rightarrow 2l2#nu ")
     #elif 'hzz'       in limFile : leg.SetHeader("ZZ #rightarrow 4l ")
     #elif 'hgg'       in limFile : leg.SetHeader("#gamma#gamma ")


     pt4 = TPaveText(0.53,0.83,0.88,0.93,"brNDC");
     if 'hww01' in limFile : pt4 = TPaveText(0.62,0.83,0.88,0.93,"brNDC");
     if 'hwwhzz_' in limFile : pt4 = TPaveText(0.62,0.83,0.88,0.93,"brNDC");
     pt4.SetBorderSize(0);
     pt4.SetFillStyle(0);
     pt4.SetTextAlign(12);
     pt4.SetTextFont(42);
     pt4.SetTextSize(0.04);
     pt4.AddText(0,0.5,title);

     leg1 = TLegend(0.20,0.68,0.50,0.80)
     leg1.SetLineColor(0);
     leg1.SetFillColor(0);
     leg1.SetTextSize(0.035)
     leg1.SetFillStyle(0)
     leg1.SetBorderSize(0)
     leg1.SetTextFont (42)

     leg2 = TLegend(0.56,0.68,0.86,0.84)
     leg2.SetLineColor(0);
     leg2.SetFillColor(0);
     leg2.SetTextSize(0.035)
     leg2.SetFillStyle(0)
     leg2.SetBorderSize(0)
     leg2.SetTextFont (42)


      
     leg1.AddEntry(grSM,"0^{+}","lp");
     leg1.AddEntry(grSM95,"Expected at 95% CL","f");
     leg1.AddEntry(grSM68,"Expected at 68% CL","f");
     
     
     if unblind: leg2.AddEntry(grData,"Observed","lp")
     leg2.AddEntry(grGRAV,"J^{P}","lp");
     leg2.AddEntry(grGR95,"Expected at 95% CL","f");
     leg2.AddEntry(grGR68,"Expected at 68% CL","f");


     #TlMH=TLatex()
     #TlMH.SetTextSize(0.03);
     #TlMH.SetNDC()
     #TlMH.DrawLatex(0.72,0.87,'m_{H} = '+str(mass)+' GeV')

   
     grSM95.Draw("E3same")
     grSM68.Draw("E3same")
     grGR95.Draw("E3same")
     grGR68.Draw("E3same")
     grSM.Draw("LPsame")
     grGRAV.Draw("LPsame")
     if unblind: grData.Draw("LPsame")
     leg1.Draw("SAME")
     leg2.Draw("SAME")
     f = TF1('f','0.',0.,100.)
     f.SetLineColor(kBlack)
     f.SetLineWidth(2)
     f.SetLineStyle(kDashed)
     f.Draw("same")
     pt.Draw("same")
     pt2.Draw("same")
     pt3.Draw("same")
     pt4.Draw("same")
     #self.addTitle()
     dummyHist.Draw("AXISGsame")
     self.c1.Update()
     #if not options.isBatch: raw_input("Looks ok?")
     self.c1.Update()
     self.c1.Print(limFile.replace('txt','png'))
     self.c1.Print(limFile.replace('txt','pdf'))
     self.c1.Print(limFile.replace('txt','root'))
     self.c1.Print(limFile.replace('txt','C'))
   
   # grSM.SetName('fqqSM')
   # grGRAV.SetName('fqqGRAV')
   # grSM95.SetName('fqqSM95')
   # grSM68.SetName('fqqSM68')
   # grData.SetName('fqqData')
   # outf.cd()
   # grSM.Write()
   # grGRAV.Write()
   # grSM95.Write()
   # grSM68.Write()
   # if unblind: grData.Write()
   # canv.SetName('fqq')
   # canv.Write()  

   def JCPFB2(self,combList,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,combList[0],energyList).get()
     
       tComb = 'hww01jet_jcp_1hww'  
       for iMass in massList:
         ParSummTxt='_FITNUIS1'
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+tComb+'/'+str(iMass)
         os.system('mkdir -p '+TargetDir)
         tableName  = TargetDir+'/higgsCombine_'+tComb
         if iEnergy == 7 : tableName += '_7TeV'
         if iEnergy == 8 : tableName += '_8TeV'
         tableName += '_'+iModel+'_'+iTarget+ParSummTxt+'_ResultsSummary_mH'+str(iMass).replace('.','d')+'.txt' 
         subfile = open(tableName,'w')
         print tableName

         for iComb in combList :
           if '1mix' in iComb : iFQQ = 0.5
           elif '1m' in iComb : iFQQ = 0.0
           elif '1p' in iComb : iFQQ = 1.0
           TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb+'/'+str(iMass)
           limFile = TargetDir+'/higgsCombine_'+iComb
           if iEnergy == 7 : limFile += '_7TeV'
           if iEnergy == 8 : limFile += '_8TeV'
           limFile += '_'+iModel+'_'+iTarget+ParSummTxt+'_ResultsSummary_mH'+str(iMass).replace('.','d')+'.txt'
           print limFile
           for line in open(limFile):
             if "#" not in line:
               print line.replace("0.0",str(iFQQ))
               subfile.write(line.replace("0.0",str(iFQQ)))
         subfile.close()
         self.plotFqqLim(tableName,1,0,massFilter[0],'1hww','1','q#bar{q} #rightarrow X #rightarrow WW',0)
       #for iMass in massList:
       #  limFile = 'hww_spin1_limFile.txt'
       #  for iComb in combList :
       #    iFQQ = -1.
       #    if   '1mix' in iComb : iFQQ = 0.5
       #    elif '1m'   in iComb : iFQQ = 0.0
       #    elif '1p'   in iComb : iFQQ = 1.0

       #limFile = '/afs/cern.ch/work/x/xjanssen/cms/HWWLimComb/workspace/Spin2014_V3/jcp/hww_spin1_limFile.txt'
       #self.plotFqqLim(limFile,1,0,massFilter[0],'1hww','1') 

   def JCPFQQ(self,iComb,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       for iMass in massList:
         paramSet = self.ParamSet_Maker(iModel,iTarget)
         iFITNUIS = -1
         iFQQ = 0.0
         for iSet in range(0,len(paramSet['values'])) :
           ParString=''
           ParSummTxt=''
           for iPar in range(0,len(paramSet['names'])) :
             parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
             ParString += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal) 
             if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
             if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]

         if 'hww01' in iComb or '_dec' in iComb :
           jcp=iComb.split('_')[-1] 
           tableName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
           if iEnergy == 7 : tableName += '_7TeV'
           if iEnergy == 8 : tableName += '_8TeV'
           tableName += '_'+iModel+'_'+iTarget+ParSummTxt+'_ResultsSummary_mH'+str(iMass).replace('.','d')+'.txt' 
         else:
           print 'MIXING'
           jcp='mix'
           baseDir  = workspace+'/'+self.Version+'/'+cardDir+'/'  
           endStr     = ''
           if iEnergy == 7 : endStr += '_7TeV'
           if iEnergy == 8 : endStr += '_8TeV' 
           endStr  +='_'+iModel+'_'+iTarget+ParSummTxt+'_ResultsSummary_mH'+str(iMass).replace('.','d')+'.txt'
           tableGG  = baseDir+iComb                      +'/'+str(iMass)+'/higgsCombine_'+iComb                      +endStr.replace('JCPFQQf','JCPGGf')
           tableFQQ = baseDir+iComb.replace('_gg','_dec')+'/'+str(iMass)+'/higgsCombine_'+iComb.replace('_gg','_dec')+endStr
           tableQQB = baseDir+iComb.replace('_gg','_qqb')+'/'+str(iMass)+'/higgsCombine_'+iComb.replace('_gg','_qqb')+endStr.replace('JCPFQQf','JCPQQBf')
           tableMIX = baseDir+iComb.replace('_gg','_mix')+'/'+str(iMass)+'/higgsCombine_'+iComb.replace('_gg','_mix')+endStr
           os.system('mkdir -p '+baseDir+iComb.replace('_gg','_mix')+'/'+str(iMass))
           print tableFQQ
           print tableMIX
           subfile = open(tableMIX,'w')          
           for line in open(tableGG): 
             if "#" not in line: subfile.write(line)
           for line in open(tableFQQ):
             if "#" not in line: 
               vec = line.split()
               if float(vec[0])>0.0 and float(vec[0]) < 1.0: subfile.write(line)
           for line in open(tableQQB):
             if "#" not in line: subfile.write(line.replace('0.0','1.0'))
           subfile.close()
           tableName = tableMIX

         unblind=0
         if not self.blind : unblind=1
         iLumiLocal=0
         mText = self.combinations[iComb]['legend']
         chText2 = 'X('+mText+') #rightarrow ' 

         iRange=1
         if   'hgghzzhww' in iComb : 
            chText2 += 'ZZ + WW + #gamma#gamma'
            iLumiLocal=1 
            iRange=2
         elif   'hwwhzz' in iComb : 
            if '2pm' not in iComb : iRange=3
            if '2bp' in iComb : iRange=2
            if '2mh9' in iComb : iRange=2
            if '2ph2' in iComb : iRange=2
            if '2ph3' in iComb : iRange=2
            chText2 += 'ZZ + WW'
            iLumiLocal=1 
         elif 'hww'    in iComb : 
            chText2 += 'WW'
            if iEnergy == 7 : iLumiLocal = 7
            if iEnergy == 8 : iLumiLocal = 8
            iLumiLocal = 0
         elif 'hzz'    in iComb : 
            chText2 += 'ZZ'
            iLumiLocal=1 
         elif 'hgg'    in iComb :
            chText2 += '#gamma#gamma'
            iLumiLocal=1

         iStatus2=1
         if 'float' in iTarget :
           if    'hgghzzhww' in iComb :
             iStatus2=0
             if '_gg' in iComb : iStatus2=0
           elif  'hwwhzz'    in iComb :
             if  '2pm'  in iComb :
               if '_dec' in iComb : iStatus2=0
               if '_gg' in iComb : iStatus2=0
             if  '2ph2'  in  iComb :
                   # gg->X
                if '_dec' in  iComb : iStatus2=0
           elif  'hww01'    in iComb :
                 if  '2ph2'  in  iComb :
                   iStatus2=0
 

         self.plotFqqLim(tableName,unblind,iLumiLocal,massFilter[0],jcp,mText,chText2,iStatus2,iRange) 
         #print tableName,unblind,iLumiLocal,massFilter[0],jcp,mText,chText2,iStatus2,iRange



   def JCPTable(self,combList,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,combList[0],energyList).get()

       for iMass in massList:

         tableContent = OrderedDict()

         for iComb in combList :

# Spin 1

           if '1hzz' in iComb or '1m'   in iComb or '1p'   in iComb:
             if    '1hzz' in iComb :
               iModelS1 = iModel.replace('DEC','')
               iTargetS1 = iTarget.replace('JCPGGfloatmu','JCPFQQfloatmu').replace('JCPQQBfloatmu','JCPFQQfloatmu')
             elif  '1m'   in iComb :
               iModelS1  = 'JCP'
               iTargetS1 = iTarget.replace('FQQ','')
             
             elif  '1p'   in iComb :
               iModelS1  = 'JCP'
               iTargetS1 = iTarget.replace('FQQ','')

             paramSet = self.ParamSet_Maker(iModelS1,iTargetS1)
             print 'param'
             print paramSet
             iFITNUIS = -1
             iFQQ = 0.0
             for iSet in range(0,len(paramSet['values'])) :
               ParString=''
               ParSummTxt=''
               for iPar in range(0,len(paramSet['names'])) :
                 parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
                 ParString += '_'+paramSet['names'][iPar]+str(parVal)
                 if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal)
                 if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
                 if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]
  
               if not iFITNUISnew == iFITNUIS :
                 iFITNUIS = iFITNUISnew
  
               if iFQQ == 0 or iFQQ == 1 :
                 print ParString
                 print iComb
                 if 'targetdir' in cardtypes[physmodels[iModelS1]['cardtype']]:
                   TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModelS1]['cardtype']]['targetdir']+'/'+iComb
                 else:
                   TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
                 print TargetDir
                 logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb  
                 if iEnergy == 7 : logName += '_7TeV'
                 if iEnergy == 8 : logName += '_8TeV'
                 logName  += '_'+iModelS1+'_'+iTargetS1+ParString+'.Results.mH'+str(iMass)+'.txt'
                 print logName

                 legend=''
                 legend = 'q\\bar{q}\\rightarrow '
                 if   iFQQ == 0 : legend = '1^{-}'
                 elif iFQQ == 1 : legend = '1^{+}'
                 if  '1m'   in iComb: legend = '1^{-}' 
                 if  '1p'   in iComb: legend = '1^{+}' 
                 if  '1mix' in iComb: legend = '1mix' 

                 #legend += self.combinations[iComb]['legend']
                 print legend
  
                 tableContent[legend] = {}
                 if   'float' in iTarget : 
                   muType = 'FloatMu'
                 else : 
                   muType = 'FixMu'
                 tableContent[legend][muType]   = {} 
  
                 for line in open(logName):
                   if   "Toys generated SM" in line:
                     values=line.split()
                     tableContent[legend][muType]['nToys'] =  values[3]
                   elif "Separation from histograms" in line :
                     values=line.split()
                     tableContent[legend][muType]['HistSep'] = values[4]
                   elif "RESULTS_SUMMARY" in line:
                     values=line.split()
                     tableContent[legend][muType]['sSMObs'] = values[1]
                     tableContent[legend][muType]['sSMExp'] = values[2]
                     tableContent[legend][muType]['sJPObs'] = values[3]
                     tableContent[legend][muType]['sJPExp'] = values[4]
                     tableContent[legend][muType]['CLs']    = values[5]

                     

                 if  muType == 'FloatMu' :
                   if    'hww01'   in iComb : logName = logName.replace('floatmu','fixmu')
                   elif  'hwwhzz_' in iComb : logName = logName.replace('floatmu','fix2mu')
                   print  logName
                   muType = 'FixMu' 
                   tableContent[legend][muType]   = {}
  
                   for line in open(logName):
                     if   "Toys generated SM" in line:
                       values=line.split()
                       tableContent[legend][muType]['nToys'] =  values[3]
                     elif "Separation from histograms" in line :
                       values=line.split()
                       tableContent[legend][muType]['HistSep'] = values[4]
                     elif "RESULTS_SUMMARY" in line:
                       values=line.split()
                       tableContent[legend][muType]['sSMObs'] = values[1]
                       tableContent[legend][muType]['sSMExp'] = values[2]
                       tableContent[legend][muType]['sJPObs'] = values[3]
                       tableContent[legend][muType]['sJPExp'] = values[4]
                       tableContent[legend][muType]['CLs']    = values[5]
  
                 if 'hww01' in iComb :
                   logName = TargetDir+'/'+str(iMass)+'/'+iComb+'_0_JCP_fJP.txt'  
                   if os.path.isfile(logName) :
                     tableContent[legend]['fJP'] = {} 
                     
                     for line in open(logName):    
                       if 'Exp' in line:
                         values=line.split()
                         print values, min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Exp68hi'] = min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Exp95hi'] = min(1,abs(float(values[4])))
                         tableContent[legend]['fJP']['Exp68lo'] = max(0,float(values[2]))
                         tableContent[legend]['fJP']['Exp95lo'] = max(0,float(values[1]))
                       if 'Obs' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['Obs68hi'] = min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Obs95hi'] = min(1,abs(float(values[4])))
                         tableContent[legend]['fJP']['Obs68lo'] = max(0,float(values[2]))
                         tableContent[legend]['fJP']['Obs95lo'] = max(0,float(values[1]))
                       if 'Best' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['Best'] = float(values[1])
                         tableContent[legend]['fJP']['BestUp'] = tableContent[legend]['fJP']['Obs68hi'] - tableContent[legend]['fJP']['Best']
                         tableContent[legend]['fJP']['BestDo'] = tableContent[legend]['fJP']['Best'] - tableContent[legend]['fJP']['Obs68lo']
                       if 'Test' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['CExp'] = sqrt(float(values[1]))
                         tableContent[legend]['fJP']['CObs'] = sqrt(float(values[2]))
                     print 'TEST' , tableContent[legend]['fJP']  
# Spin 2


         paramSet = self.ParamSet_Maker(iModel,iTarget)
         print paramSet
         iFITNUIS = -1
         iFQQ = 0.0
         for iSet in range(0,len(paramSet['values'])) :
           ParString=''
           ParSummTxt=''
           for iPar in range(0,len(paramSet['names'])) :
             parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
             ParString += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
             if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]

           if not iFITNUISnew == iFITNUIS :
             iFITNUIS = iFITNUISnew

           if iFQQ == 0 or iFQQ == 1 :

             print ParString
             for iComb in combList : 
              if not ( '1hzz' in iComb or '1m' in iComb or '1p' in iComb ) : 
               print iComb
               if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
                 TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
               else:
                 TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
               print TargetDir
               logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
               if iEnergy == 7 : logName += '_7TeV'
               if iEnergy == 8 : logName += '_8TeV'
               logName  += '_'+iModel+'_'+iTarget+ParString+'.Results.mH'+str(iMass)+'.txt'
               print logName
              
               legend=''
               if   iFQQ == 0 : legend = 'gg\\rightarrow '
               elif iFQQ == 1 : legend = 'q\\bar{q}\\rightarrow '
               if 'QQB' in iTarget : 
                 legend = 'q\\bar{q}\\rightarrow '
                 iFQQ == 1

               legend += self.combinations[iComb]['legend']
               print legend

               tableContent[legend] = {}
               if   'float' in iTarget : 
                 muType = 'FloatMu'
               else : 
                 muType = 'FixMu'
               tableContent[legend][muType]   = {} 

               tableContent[legend][muType]['nToys'] = 0 
               for line in open(logName):
                 if   "Toys generated SM" in line:
                   values=line.split()
                   tableContent[legend][muType]['nToys'] =  values[3]
                 elif "Separation from histograms" in line :
                   values=line.split()
                   tableContent[legend][muType]['HistSep'] = values[4]
                 elif "RESULTS_SUMMARY" in line:
                   values=line.split()
                   tableContent[legend][muType]['sSMObs'] = values[1]
                   tableContent[legend][muType]['sSMExp'] = values[2]
                   tableContent[legend][muType]['sJPObs'] = values[3]
                   tableContent[legend][muType]['sJPExp'] = values[4]
                   tableContent[legend][muType]['CLs']    = values[5]

               if  muType == 'FloatMu' :
                 if    'hww01'   in iComb : logName = logName.replace('floatmu','fixmu')
                 if    'hgg_'    in iComb : logName = logName.replace('floatmu','fixmu')
                 elif  'hwwhzz_' in iComb : logName = logName.replace('floatmu','fix2mu')
                 elif  'hgghzzhww_' in iComb : logName = logName.replace('floatmu','fix3mu')
                 print  logName
                 muType = 'FixMu' 
                 tableContent[legend][muType]   = {}

                 tableContent[legend][muType]['nToys'] = '0'
                 tableContent[legend][muType]['HistSep'] = '0'

                 if os.path.isfile(logName) : 
                  for line in open(logName):
                   if   "Toys generated SM" in line:
                     values=line.split()
                     tableContent[legend][muType]['nToys'] =  values[3]
                   elif "Separation from histograms" in line :
                     values=line.split()
                     tableContent[legend][muType]['HistSep'] = values[4]
                   elif "RESULTS_SUMMARY" in line:
                     values=line.split()
                     tableContent[legend][muType]['sSMObs'] = values[1]
                     tableContent[legend][muType]['sSMexp'] = values[2]
                     tableContent[legend][muType]['sJPObs'] = values[3]
                     tableContent[legend][muType]['sJPExp'] = values[4]
                     tableContent[legend][muType]['CLs']    = values[5]

               if 'hww01' in iComb :
                   logName = TargetDir+'/'+str(iMass)+'/'+iComb
                   if iFQQ == 0 : logName  += '_0_JCPFQQ_fJP_fqq0.txt'
                   if iFQQ == 1 : logName  += '_0_JCPFQQ_fJP_fqq1.txt'
                   if os.path.isfile(logName) :
                     tableContent[legend]['fJP'] = {}

                     for line in open(logName):
                       if 'Exp' in line:
                         values=line.split()
                         print values, min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Exp68hi'] = min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Exp95hi'] = min(1,abs(float(values[4])))
                         tableContent[legend]['fJP']['Exp68lo'] = max(0,float(values[2]))
                         tableContent[legend]['fJP']['Exp95lo'] = max(0,float(values[1]))
                       if 'Obs' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['Obs68hi'] = min(1,abs(float(values[3])))
                         tableContent[legend]['fJP']['Obs95hi'] = min(1,abs(float(values[4])))
                         tableContent[legend]['fJP']['Obs68lo'] = max(0,float(values[2]))
                         tableContent[legend]['fJP']['Obs95lo'] = max(0,float(values[1]))
                       if 'Best' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['Best'] = float(values[1])
                         tableContent[legend]['fJP']['BestUp'] = tableContent[legend]['fJP']['Obs68hi'] - tableContent[legend]['fJP']['Best']
                         tableContent[legend]['fJP']['BestDo'] = tableContent[legend]['fJP']['Best'] - tableContent[legend]['fJP']['Obs68lo']
                       if 'Test' in line:
                         values=line.split()
                         tableContent[legend]['fJP']['CExp'] = sqrt(float(values[1])) 
                         tableContent[legend]['fJP']['CObs'] = sqrt(float(values[2])) 
                     print tableContent[legend]['fJP']

         # Make table



         print tableContent

         targetFile='aTable'
         if   'hww01' in   combList[0] : targetFile+= '_hww'
         if   'hgg_'  in   combList[0] : targetFile+= '_hgg'
         elif 'hwwhzz_' in combList[0] : 
           targetFile+= '_hzzhww'
           if '_2'    in   combList[0] :
             if '_dec'  in   combList[0] : targetFile+= '_decay'
             if '_gg'  in   combList[0] : targetFile+= '_gg'
             if '_qqb'  in   combList[0] : targetFile+= '_qqb'
         elif 'hgghzzhww_' in combList[0] :
           targetFile+= '_hgghzzhww' 
           if '_dec'  in   combList[0] : targetFile+= '_decay'
           if '_gg'  in   combList[0] : targetFile+= '_gg'
           if '_qqb'  in   combList[0] : targetFile+= '_qqb'
         if   '_1'    in   combList[0] : targetFile+= '_spin1'
         else : targetFile+= '_spin2'

         targetFile+='.txt'
         fo = open(targetFile, "w")
         fo.write("\documentclass{article}\n")
         fo.write("\usepackage[margin=0.5cm]{geometry}\n")
         fo.write("\\begin{document}\n")
         fo.write("\\begin{table}\n")
         fo.write("\\begin{center} \n")
         if 'hww01' in   combList[0] :
           fo.write("\\begin{tabular}{l|c|c|c|c|c|c|c|c}\n")
           fo.write("$Model$ & n. of Toys & Expected & Obs. $0^+$ & Obs. $J^P$ & CL$_s$ & fJP 95\\% CL & fJP best fit & Compatibilty \\\\ \n")    
         else:
           fo.write("\\begin{tabular}{l|c|c|c|c|c}\n")
           fo.write("$Model$ & n. of Toys & Expected & Obs. $0^+$ & Obs. $J^P$ & CL$_s$  \\\\ \n")    
         fo.write("\hline \n") 
         for iLeg in tableContent:
           fo.write( "$"+iLeg+"$" + " & " + str(tableContent[iLeg]['FloatMu']['nToys']) + " (" +  str(tableContent[iLeg]['FixMu']['nToys']) +") & " )
           fo.write( str(round(abs(float(tableContent[iLeg]['FloatMu']['HistSep'])),1)) + "$\\sigma$ (" +  str(round(abs(float(tableContent[iLeg]['FixMu']['HistSep'])),1)) +"$\\sigma$) &")
           fo.write( str(round(float(tableContent[iLeg]['FloatMu']['sSMObs']),1))  + "$\\sigma$ & " +  str(round(float(tableContent[iLeg]['FloatMu']['sJPObs']),1))  + "$\\sigma$ & " )
           fo.write( str(float(tableContent[iLeg]['FloatMu']['CLs'])*100) + ' \\% ' ) 
           if 'fJP' in tableContent[iLeg] :
             fo.write( '& $<$'+str(round(tableContent[iLeg]['fJP']['Obs95hi'],2)) + " (" + str(round(tableContent[iLeg]['fJP']['Exp95hi'],2)) +") & " )
             fo.write( str(round(tableContent[iLeg]['fJP']['Best'],2)) )
             fo.write('$^{+'+str(round(tableContent[iLeg]['fJP']['BestUp'],2))+'}')
             fo.write('_{-'+str(round(tableContent[iLeg]['fJP']['BestDo'],2))+'}$ &')
             #fo.write(str(round(tableContent[iLeg]['fJP']['CObs'],1)) )
             #fo.write(str(round(tableContent[iLeg]['fJP']['CObs'],1)) + ' (' + str(round(tableContent[iLeg]['fJP']['CExp'],1)) + ')')
             #fo.write("["+str(round(abs(float(tableContent[iLeg]['FixMu']['sJPExp'])),1))+"]")
           fo.write( "\\\\ \n")
           
         fo.write("\hline \n")
         fo.write("\end{tabular}  \n")
         fo.write("\end{center} \n")
         fo.write("\end{table} \n")
         fo.write("\end{document} \n")
         fo.close()
         os.system("latex "+targetFile)
         os.system("dvipdf "+targetFile.replace(".txt",".dvi"))
         os.system("dvipng "+targetFile.replace(".txt",".dvi"))
         os.system("mv "+targetFile.replace(".txt","1.png")+" "+targetFile.replace(".txt",".png"))

   def JCPView(self,combList,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,combList[0],energyList).get()
       
       for iMass in massList:

         plotContent = OrderedDict()
         plotContent['q#bar{q}'] = OrderedDict()
         plotContent['gg production']  = OrderedDict()
         plotContent['q#bar{q} production'] = OrderedDict()

# Spin 1

         for iComb in combList :
           if '1hzz' in iComb or '1m'   in iComb or '1p'   in iComb:
             if    '1hzz' in iComb :
               iModelS1 = iModel.replace('DEC','')
               iTargetS1 = iTarget.replace('JCPGGfloatmu','JCPFQQfloatmu').replace('JCPQQBfloatmu','JCPFQQfloatmu')
             elif  '1m'   in iComb : 
               iModelS1  = 'JCP'
               iTargetS1 = iTarget.replace('FQQ','')
             elif  '1p'   in iComb :
               iModelS1  = 'JCP'
               iTargetS1 = iTarget.replace('FQQ','')

             paramSet = self.ParamSet_Maker(iModelS1,iTargetS1)
             print paramSet
             iFITNUIS = -1
             iFQQ = 0.0
             for iSet in range(0,len(paramSet['values'])) :
               ParString=''
               ParSummTxt=''
               for iPar in range(0,len(paramSet['names'])) :
                 parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
                 ParString += '_'+paramSet['names'][iPar]+str(parVal)
                 if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal)
                 if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
                 if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]
  
               if not iFITNUISnew == iFITNUIS :
                 iFITNUIS = iFITNUISnew
  
               if iFQQ == 0 or iFQQ == 1 :
                 print ParString
                 print iComb
                 if 'targetdir' in cardtypes[physmodels[iModelS1]['cardtype']]:
                   TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModelS1]['cardtype']]['targetdir']+'/'+iComb
                 else:
                   TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
                 print TargetDir
                 logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb  
                 if iEnergy == 7 : logName += '_7TeV'
                 if iEnergy == 8 : logName += '_8TeV'
                 logName  += '_'+iModelS1+'_'+iTargetS1+ParString+'.Results.mH'+str(iMass)+'.txt'
                 print logName
                 for line in open(logName):
                   if "RESULTS_SUMMARY" in line:
                     print line
                     values=line.split()
                     print values
                     legend=''
                     if   iFQQ == 0 : legend = '1^{-}'
                     elif iFQQ == 1 : legend = '1^{+}'
                     if  '1m'   in iComb: legend = '1^{-}' 
                     if  '1p'   in iComb: legend = '1^{+}' 
                     type = 'q#bar{q}'
                     #legend += self.combinations[iComb]['legend']
                     print legend
                     plotContent[type][legend] = [
  # observed
                                             values[6] ,
  # median
                                             values[8] ,
                                             values[14] ,
  # mean
                                             values[7] ,
                                             values[13] ,
  # 68%
                                             -float(values[ 9])+float(values[7]) ,
                                              float(values[10])-float(values[7]) ,
                                             -float(values[15])+float(values[13]) ,
                                              float(values[16])-float(values[13]) ,
  # 95%
                                             -float(values[11])+float(values[7]) ,
                                              float(values[12])-float(values[7]) ,
                                             -float(values[17])+float(values[13]) ,
                                              float(values[18])-float(values[13]) ,
  # 99%
                                             -float(values[19])+float(values[7]) ,
                                              float(values[20])-float(values[7]) ,
                                             -float(values[21])+float(values[13]),
                                              float(values[22])-float(values[13])
  
                                           ]
  
                     plotContent[type][legend] = [float(X) for X in plotContent[type][legend]]

         print plotContent
         
# Spin 2


         paramSet = self.ParamSet_Maker(iModel,iTarget)
         iFITNUIS = -1
         iFQQ = 0.0
         for iSet in range(0,len(paramSet['values'])) :
           ParString=''
           ParSummTxt=''
           for iPar in range(0,len(paramSet['names'])) :
             parVal=str(paramSet['values'][iSet][iPar]).replace('.','d')
             ParString += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : ParSummTxt += '_'+paramSet['names'][iPar]+str(parVal)
             if paramSet['names'][iPar] == 'FITNUIS' : iFITNUISnew = paramSet['values'][iSet][iPar]
             if paramSet['names'][iPar] == 'FQQ'     : iFQQ     = paramSet['values'][iSet][iPar]

           if not iFITNUISnew == iFITNUIS :
             iFITNUIS = iFITNUISnew

           if iFQQ == 0 or iFQQ == 1 :

             print ParString
             for iComb in combList : 
              if not ( '1hzz' in iComb or '1m' in iComb or '1p' in iComb ) : 
               print iComb
               iTargetS1 = iTarget
               if '_qqb' in iComb :
                  iTargetS1 = iTarget.replace('JCPGGfloatmu','JCPQQBfloatmu')
               if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
                 TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
               else:
                 TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
               print TargetDir
               logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
               if iEnergy == 7 : logName += '_7TeV'
               if iEnergy == 8 : logName += '_8TeV'
               logName  += '_'+iModel+'_'+iTargetS1+ParString+'.Results.mH'+str(iMass)+'.txt'
               print logName
               for line in open(logName):
                 if "RESULTS_SUMMARY" in line:
                   print line
                   values=line.split() 
                   print values
                   legend=''
                   type=''
                   #if   iFQQ == 0 : legend = 'gg#rightarrow '
                   #elif iFQQ == 1 : legend = 'q#bar{q}#rightarrow '
                   if   iFQQ == 0 : type = 'gg production'
                   if   iFQQ == 1 or '_qqb' in iComb : type = 'q#bar{q} production'
                   legend += self.combinations[iComb]['legend']
                   print legend
                   plotContent[type][legend] = [ 
# observed
                                           values[6] ,  
# median
                                           values[8] ,
                                           values[14] ,
# mean
                                           values[7] ,
                                           values[13] ,
# 68%
                                           -float(values[ 9])+float(values[7]) ,
                                            float(values[10])-float(values[7]) ,
                                           -float(values[15])+float(values[13]) ,
                                            float(values[16])-float(values[13]) ,
# 95%
                                           -float(values[11])+float(values[7]) ,
                                            float(values[12])-float(values[7]) ,
                                           -float(values[17])+float(values[13]) ,
                                            float(values[18])-float(values[13]) ,
# 99%
                                           -float(values[19])+float(values[7]) ,
                                            float(values[20])-float(values[7]) ,
                                           -float(values[21])+float(values[13]),
                                            float(values[22])-float(values[13])

                                         ]

                   plotContent[type][legend] = [float(X) for X in plotContent[type][legend]]


         print plotContent
         hwwOnly=True
         Extra='_hww'
         if 'hwwhzz_' in combList[0] :
          hwwOnly=False
          Extra='_hzzhww'
          if '_dec' in combList[1] : Extra+='_decay'
          if '_qqb' in combList[1] : Extra+='_ggqqb'
          if '_gg'  in combList[1] : Extra+='_ggqqb'
 
         self.plotSummary_properties('./',plotContent,hwwOnly,Extra)

#      if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
#        TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
#      else:
#        TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
#      print TargetDir



   def plotSummary_properties(self,plotDir,plotContent,hwwOnly=True,Extra='_hww'):

        nentries=0
	plotContentKeys = OrderedDict()
        for iType in plotContent: 
       	  nentries += len(plotContent[iType].keys())
          plotContentKeys[iType] = plotContent[iType].keys()

	plotContentEntries = ['yObserved','ySmMedian','yAltMedian','ySm','yAlt','ySmErrM','ySmErrP','yAltErrM','yAltErrP','ySmErr2M','ySmErr2P','yAltErr2M','yAltErr2P','ySmErr3M','ySmErr3P','yAltErr3M','yAltErr3P']

	xyVals = OrderedDict() 
	#for key,val in plotContent.iteritems():
	#	# sanity check
	#	if not len(val)==17: sys.exit('Set %s doesn\'t have 17 entries.'%key)

	# predefined
	xyVals['xObserved']    = array('f',[ 5 + 10*i    for i in range(nentries)])
	xyVals['xSm']          = array('f',[ 2.75 + 10*i for i in range(nentries)])
	xyVals['xAlt']         = array('f',[ 7.25 + 10*i for i in range(nentries)])
	xyVals['xObservedErr'] = array('f',[4.5]*nentries)
	xyVals['yObservedErr'] = array('f',[0.0]*nentries)     
	xyVals['xErr']         = array('f',[2.25]*nentries)
        xyVals['labels']       = []
        for iType in plotContent:
	  xyVals['labels']       += plotContentKeys[iType]
        for entry in plotContentEntries : xyVals[entry] = array('f',[0.0]*nentries)

	# fill from content
        iLabel = 0
        for iType in plotContent:
          for Label in plotContentKeys[iType] :
	    for ientry,entry in enumerate(plotContentEntries): 
              xyVals[entry][iLabel] = plotContent[iType][Label][ientry]
            iLabel +=1
	      #xyVals[entry] = array('f',[plotContent[iType][x][ientry] for x in plotContentKeys[iType]])

	baseHisto = TH1F("Base Histo", "", nentries, 0, nentries*10)
	baseHisto.SetStats(0)
	baseHisto.GetXaxis().SetLabelSize(0.05)
	baseHisto.GetXaxis().SetTickLength(0)
	baseHisto.GetYaxis().SetTickLength(0.01)
	baseHisto.GetXaxis().SetTitleFont(42)
	baseHisto.GetYaxis().SetTitleFont(42)
	baseHisto.GetXaxis().SetTitleOffset(1.7)
	baseHisto.GetYaxis().SetTitleOffset(0.7)
	baseHisto.GetYaxis().SetTitle("-2 #times ln(L_{J^{P}} / L_{0^{+}})")
# CL_{S} (J^{P}_{ALT}
# J^{P}
	if (hwwOnly) : baseHisto.SetAxisRange(-30,  60, "Y")
	else         : baseHisto.SetAxisRange(-65, 120, "Y")

	observed = TGraphErrors(nentries, xyVals['xObserved'], xyVals['yObserved'], xyVals['xObservedErr'], xyVals['yObservedErr'])
	observed.SetMarkerColor(1)
	observed.SetMarkerStyle(20)
	observed.SetMarkerSize(2)
	observed.SetLineWidth(1)

	MedianSM = TGraphErrors(nentries, xyVals['xSm'], xyVals['ySmMedian'], xyVals['xErr'], xyVals['yObservedErr'])
	MedianSM.SetLineColor(1)
	MedianSM.SetMarkerColor(1)
#	MedianSM.SetMarkerSize(0)
#	MedianSM.SetMarkerStyle(1)
	MedianSM.SetLineWidth(1)
	MedianSM.SetLineStyle(2)
	
	MedianALT = TGraphErrors(nentries, xyVals['xAlt'], xyVals['yAltMedian'], xyVals['xErr'], xyVals['yObservedErr'])
	MedianALT.SetLineColor(1)
	MedianALT.SetMarkerColor(1)
#	MedianALT.SetMarkerSize(3)
#	MedianALT.SetMarkerStyle(1)
	MedianALT.SetLineWidth(1)
	MedianALT.SetLineStyle(2)
	
	SM = TGraphAsymmErrors(nentries, xyVals['xSm'], xyVals['ySm'], xyVals['xErr'], xyVals['xErr'], xyVals['ySmErrM'], xyVals['ySmErrP'])
	SM.SetFillColor(kOrange+7)
	SM.SetLineColor(kOrange+7)
#	SM.SetMarkerColor(kAzure+1)
	SM.SetMarkerSize(3)
	SM.SetMarkerStyle(1)
	SM.SetFillStyle(1001)
	SM.SetLineWidth(1)
	SM.SetLineStyle(1)
	
	ALT = TGraphAsymmErrors(nentries, xyVals['xAlt'], xyVals['yAlt'], xyVals['xErr'], xyVals['xErr'], xyVals['yAltErrM'], xyVals['yAltErrP'])
	ALT.SetFillColor(kAzure-3)
	ALT.SetLineColor(kAzure-3)
#	ALT.SetMarkerColor(kOrange+1)
	ALT.SetMarkerSize(0)
	ALT.SetMarkerStyle(1)
	ALT.SetFillStyle(1001)
	ALT.SetLineWidth(1)
	ALT.SetLineStyle(1)
	
	SM2 = TGraphAsymmErrors(nentries, xyVals['xSm'], xyVals['ySm'], xyVals['xErr'], xyVals['xErr'], xyVals['ySmErr2M'], xyVals['ySmErr2P'])
	SM2.SetFillColor(kOrange+1)
	SM2.SetLineColor(kOrange+1)
#	SM2.SetMarkerColor(kAzure+1)
	SM2.SetMarkerSize(0)
	SM2.SetMarkerStyle(1)
#	SM2.SetFillStyle(1001)
	SM2.SetLineWidth(1)
	SM2.SetLineStyle(1)

	ALT2 = TGraphAsymmErrors(nentries, xyVals['xAlt'], xyVals['yAlt'], xyVals['xErr'], xyVals['xErr'], xyVals['yAltErr2M'], xyVals['yAltErr2P'])
	ALT2.SetFillColor(kAzure+1)
	ALT2.SetLineColor(kAzure+1)
#	ALT2.SetMarkerColor(kOrange+1)
	ALT2.SetMarkerSize(0)
	ALT2.SetMarkerStyle(1)
#	ALT2.SetFillStyle(1001)
	ALT2.SetLineWidth(1)
	ALT2.SetLineStyle(1)
	
	SM3 = TGraphAsymmErrors(nentries, xyVals['xSm'], xyVals['ySm'], xyVals['xErr'], xyVals['xErr'], xyVals['ySmErr3M'], xyVals['ySmErr3P'])
	SM3.SetFillColor(kOrange-9)
	SM3.SetLineColor(kOrange-9)
#	SM3.SetMarkerColor(kAzure+1)
	SM3.SetMarkerSize(0)
	SM3.SetMarkerStyle(1)
#	SM3.SetFillStyle(1001)
	SM3.SetLineWidth(1)
	SM3.SetLineStyle(1)
	
	ALT3 = TGraphAsymmErrors(nentries, xyVals['xAlt'], xyVals['yAlt'], xyVals['xErr'], xyVals['xErr'], xyVals['yAltErr3M'], xyVals['yAltErr3P'])
	ALT3.SetFillColor(kAzure-9)
	ALT3.SetLineColor(kAzure-9)
#	ALT3.SetMarkerColor(kOrange+1)
	ALT3.SetMarkerSize(0)
	ALT3.SetMarkerStyle(1)
#	ALT3.SetFillStyle(1001)
	ALT3.SetLineWidth(1)
	ALT3.SetLineStyle(1)

	SM3.SetHistogram(baseHisto)

	vLine = [None]*(nentries-1)
	hLine = [None]*4
	for iv in range(nentries-1):
		if hwwOnly : vLine[iv] = TLine(10*(iv+1), -30, 10*(iv+1),  60)
		else       : vLine[iv] = TLine(10*(iv+1), -65, 10*(iv+1), 120)
		vLine[iv].SetLineStyle(3)
        if hwwOnly :
          hLine[0] = TLine( 0, 0.158655,  60, 0.158655)
          hLine[1] = TLine( 0, 0.022750,  60, 0.022750)
          hLine[2] = TLine( 0, 0.001349,  60, 0.001349)
          hLine[3] = TLine( 0, 0.000032,  60, 0.000032)
        else:
	  hLine[0] = TLine( 0, 0.158655, 120, 0.158655)
	  hLine[1] = TLine( 0, 0.022750, 120, 0.022750)
	  hLine[2] = TLine( 0, 0.001349, 120, 0.001349)
	  hLine[3] = TLine( 0, 0.000032, 120, 0.000032)
	for h in hLine: 
		h.SetLineStyle(8)
		h.SetLineColor(kRed)
	
	textSigma = [None]*4
	textSigma[0] = TLatex(.92, .80, "1#sigma")
	textSigma[1] = TLatex(.92, .80, "2#sigma")
	textSigma[2] = TLatex(.92, .80, "3#sigma")
	textSigma[3] = TLatex(.92, .80, "4#sigma")
	for t in textSigma:
		t.SetNDC(kTRUE)
		t.SetTextFont(42)
		t.SetTextSize(0.04)
		t.SetTextColor(kRed)
	for i in range(nentries): baseHisto.GetXaxis().SetBinLabel(i+1,xyVals['labels'][i])
	baseHisto.SetTitleFont(82)
	baseHisto.GetXaxis().LabelsOption("v")

	canvas = TCanvas("Summary plot canvas", "", 1680, 900)
#	canvas.SetLogy()
	canvas.SetTicks(1,1)
	gPad.SetBottomMargin(0.2)
	gPad.SetTopMargin(0.1)
	gPad.SetLeftMargin(0.1)
	SM3.Draw("za2")
	ALT3.Draw("z2")
	SM2.Draw("z2")
	ALT2.Draw("z2")
	SM.Draw("samez2")
	ALT.Draw("samez2")
	observed.Draw("zp")
	MedianALT.Draw("samez")
	MedianSM.Draw("samez")
	baseHisto.Draw("sameaxis")

	for v in vLine: v.Draw("same")

	pt = TPaveText(0.055, 0.9, 0.99, 0.95, "NDC")
	pt.SetBorderSize(0)
	pt.SetTextAlign(12)
	pt.SetFillStyle(0)
	pt.SetTextFont(61)
	pt.SetTextSize(0.045)
	textCMS = pt.AddText( 0, 0.6, "CMS" )
	pt.Draw("same")

        ptl = TPaveText(0.055, 0.9, 0.99, 0.95, "NDC")
        ptl.SetBorderSize(0)
        ptl.SetTextAlign(12)
        ptl.SetFillStyle(0)
        ptl.SetTextFont(42)
        ptl.SetTextSize(0.035)
	if hwwOnly : textCMS = ptl.AddText(0.69, 0.5,"19.4 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)")
	else       : textCMS = ptl.AddText(0.69, 0.5,"19.7 fb^{-1} (8 TeV) + 5.1 fb^{-1} (7 TeV)")
	ptl.Draw("same")

        pt2 = TPaveText(0.055, 0.9, 0.99, 0.95, "NDC")
        pt2.SetBorderSize(0)
        pt2.SetTextAlign(12)
        pt2.SetFillStyle(0)
        pt2.SetTextFont(42)
        pt2.SetTextSize(0.035)  
        if not hwwOnly : textCMS = pt2.AddText(0.40, 0.5,"X #rightarrow ZZ + WW")
        else:            textCMS = pt2.AddText(0.40, 0.5,"X #rightarrow WW")
        pt2.Draw()
	
	legData = TLegend( 0.13, 0.84, 0.4, 0.895 )
	legData.SetNColumns(2)
	legData.SetFillColor(0)
	legData.SetLineColor(0)
	legData.SetBorderSize(0)
	legData.SetFillStyle(1001)
	legData.SetTextFont(42)
	legData.AddEntry(observed, "Observed", "lp" )
	legData.AddEntry(MedianSM, "Expected", "l" )
	legData.Draw()
	
	leg = TLegend( 0.13, 0.7, 0.4, 0.84 )
	leg.SetNColumns(2)
	leg.SetFillColor(0)
	leg.SetLineColor(0)
	leg.SetBorderSize(0)
	leg.SetFillStyle(1001)
	leg.SetTextFont(42)
	leg.AddEntry(SM, "0^{+} #pm 1#sigma","f")
	leg.AddEntry(ALT, "J^{P} #pm 1#sigma","f")
	leg.AddEntry(SM2, "0^{+} #pm 2#sigma","f")
	leg.AddEntry(ALT2, "J^{P} #pm 2#sigma","f")
	leg.AddEntry(SM3, "0^{+} #pm 3#sigma","f")
	leg.AddEntry(ALT3, "J^{P} #pm 3#sigma","f")
	leg.Draw()

	for i in range(nentries): baseHisto.GetXaxis().SetBinLabel(i+1,'')
 	l = TLatex();
	l.SetTextSize(0.047);#	//0.047
	l.SetTextFont(132);
	l.SetTextAlign(12);
	l.SetTextAngle(90);
        for i in range(nentries):
          if hwwOnly : l.DrawLatex(xyVals['xObserved'][i], -40 ,xyVals['labels'][i]) 
          else:        l.DrawLatex(xyVals['xObserved'][i], -86 ,xyVals['labels'][i]) 

        iProd = 0
        nProd = len(plotContent)
        nlen  = 0
        ptV = {}
        pl_separator_c = {}
        for iType in plotContent : 
          iProd+=1
          nold = nlen
          nlen += len(plotContent[iType]) 
          print iProd
          if iProd < nProd : 
            pointx = array('f',[0]*2)
            pointy = array('f',[0]*2)
            pointx[0] = nlen*10 
            pointx[1] = nlen*10 
            if hwwOnly :
              pointy[0] = -60 
              pointy[1] = -30
            else:
              pointy[0] = -140
              pointy[1] = -65
            pl_separator_c[iProd] = TPolyLine(2, pointx, pointy, "");
            pl_separator_c[iProd].SetUniqueID(1000+iProd);
            pl_separator_c[iProd].SetLineColor(1);
            pl_separator_c[iProd].SetLineStyle(3);
            pl_separator_c[iProd].SetLineWidth(1);
            pl_separator_c[iProd].Draw("same");

          if hwwOnly : ptV[iProd] = ( TPaveText(nold*10,-50 ,nlen*10,-45) )
          else:        ptV[iProd] = ( TPaveText(nold*10,-115 ,nlen*10,-87) ) 
          ptV[iProd].SetBorderSize(0)
          #ptV[iProd].SetTextAlign(12)
          ptV[iProd].SetFillStyle(0)
          ptV[iProd].SetTextFont(42)
          ptV[iProd].SetTextSize(0.035) 
          ptV[iProd].AddText(0.50, 0.5,iType)
          ptV[iProd].Draw("same")

	canvas.Modified()
	canvas.SaveAs(plotDir + "JP_SummaryPlot"+Extra+".pdf")
	canvas.SaveAs(plotDir + "JP_SummaryPlot"+Extra+".png")
	canvas.SaveAs(plotDir + "JP_SummaryPlot"+Extra+".root")
	canvas.SaveAs(plotDir + "JP_SummaryPlot"+Extra+".C")

   def FJPView(self,combList,iEnergy,iModel,iTarget,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get()
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,combList[0],energyList).get()
   
       for iMass in massList:

         
         plotContent = OrderedDict()
         #plotContent['q#bar{q}'] = OrderedDict()
         if ('1m' in combList[0] or '1p' in combList[0] or '1mix' in combList[0] ) : 
            #plotContent['q#bar{q}'] = OrderedDict()
            plotContent[' '] = OrderedDict()
         plotContent['gg production']  = OrderedDict()
         plotContent['q#bar{q} production'] = OrderedDict()

         for iComb in combList:
          
           # Spin 1:
           if ( '1m' in iComb or '1p' in iComb or '1mix' in iComb ) :
             iTargetS = 'JCP'
             TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['dir']+'/'+iComb+'/'+str(iMass)
             print   TargetDir
             legend = self.combinations[iComb]['legend']
             if '1mix' in iComb: legend = 'f_{b2}^{WW}=0.5' 
             #elif '1m' in iComb: legend = 'f_{b2}=0' 
             #elif '1p' in iComb: legend = 'f_{b2}=1' 
             logName   = TargetDir+'/'+iComb+'_0_'+iTargetS+'_fJP.txt'
             print logName  
             #iKey = 'q#bar{q}'
             iKey = ' '
             plotContent[iKey][legend] = {} 
             for line in open(logName):
                 values=line.split()
                 if 'Exp'  in values[0] : plotContent[iKey][legend]['Exp']  = [ values[1] ,  values[2] ,  values[3] ,  values[4] ]
                 if 'Obs'  in values[0] : plotContent[iKey][legend]['Obs']  = [ values[1] ,  values[2] ,  values[3] ,  values[4] ]
                 if 'Best' in values[0] : plotContent[iKey][legend]['Best'] = [ values[1] ]

 
           # Spin 2:
           if not ( '1hzz' in iComb or '1m' in iComb or '1p' in iComb or '1mix' in iComb ) :
             TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['dir']+'/'+iComb+'/'+str(iMass)
             print   TargetDir
             legend = self.combinations[iComb]['legend']
             for iFQQ in ['0','1'] :
               logName   = TargetDir+'/'+iComb+'_0_'+iTarget+'_fJP_fqq'+iFQQ+'.txt'
               print logName  
               iKey = 'NONE'
               if iFQQ == '0' : iKey =  'gg production'
               if iFQQ == '1' : iKey =  'q#bar{q} production'
               plotContent[iKey][legend] = {} 
               for line in open(logName):
                 values=line.split()
                 if 'Exp'  in values[0] : plotContent[iKey][legend]['Exp']  = [ values[1] ,  values[2] ,  values[3] ,  values[4] ]
                 if 'Obs'  in values[0] : plotContent[iKey][legend]['Obs']  = [ values[1] ,  values[2] ,  values[3] ,  values[4] ]
                 if 'Best' in values[0] : plotContent[iKey][legend]['Best'] = [ values[1] ]
                                                              

       #print plotContent
       if ( '1m' in combList[0] or '1p' in combList[0] or '1mix' in combList[0] ) : 
         self.plotSummary_fJP('all',plotContent)
       else:
         self.plotSummary_fJP('spin2',plotContent)
       
   def plotSummary_fJP(self,plotDir,plotContent,hwwOnly=True,Extra='_hww'):
  
        Green  = 211
        Yellow = 90 
 
        nentries=0
        for iType in plotContent: 
          print iType
          nentries += len( plotContent[iType] )  
 
        #vnames       = array('c',['2^+_m']*nentries)
    
        vexp_95CL_up = array('f',[0.]*nentries)
        vexp_68CL_up = array('f',[0.]*nentries)
        vexp_95CL_do = array('f',[0.]*nentries)
        vexp_68CL_do = array('f',[0.]*nentries)


        vobs_95CL_up = array('f',[0.]*nentries)
        vobs_68CL_up = array('f',[0.]*nentries)
        vobs_95CL_do = array('f',[0.]*nentries)
        vobs_68CL_do = array('f',[0.]*nentries)
        vobs         = array('f',[0.]*nentries)
     
        # fill from content
        iLabel = 0
        for iType in plotContent:
          for Label in plotContent[iType] :
            vexp_95CL_do [iLabel] = max(0.,float(plotContent[iType][Label]['Exp'][0] ))
            vexp_68CL_do [iLabel] = max(0.,float(plotContent[iType][Label]['Exp'][1] ))
            vexp_68CL_up [iLabel] = min(1.,abs(float(plotContent[iType][Label]['Exp'][2] )))
            vexp_95CL_up [iLabel] = min(1.,abs(float(plotContent[iType][Label]['Exp'][3] )))

            vobs         [iLabel] = max(0.,float(plotContent[iType][Label]['Best'][0])) 

            vobs_95CL_do [iLabel] = max(0.,float(plotContent[iType][Label]['Obs'][0] ))
            vobs_68CL_do [iLabel] = max(0.,float(plotContent[iType][Label]['Obs'][1] ))
            vobs_68CL_up [iLabel] = min(1.,abs(float(plotContent[iType][Label]['Obs'][2] )))
            vobs_95CL_up [iLabel] = min(1.,abs(float(plotContent[iType][Label]['Obs'][3] )))

            print Label, vexp_68CL_up[iLabel] , vexp_95CL_up[iLabel]
            iLabel+=1
   


	canvas = TCanvas("Summary plot canvas", "", 1200, 400)
	canvas.SetTicks(1,0)
	gPad.SetBottomMargin(0.22)
	gPad.SetTopMargin(0.06)
	gPad.SetLeftMargin(0.07)
	gPad.SetRightMargin(0.01)

 

        baseHisto = TH1F("Base Histo", "", nentries, 0. , nentries+1.5)
	baseHisto.SetStats(0)
	baseHisto.GetXaxis().SetTickLength(0)
	baseHisto.GetYaxis().SetTickLength(0.03)
	baseHisto.GetXaxis().SetTitleFont(42)
	baseHisto.GetYaxis().SetTitleFont(42)
	baseHisto.GetXaxis().SetTitleOffset(1.7)
	baseHisto.GetYaxis().SetTitleOffset(0.3)
	baseHisto.GetYaxis().SetLabelOffset(0.005)
	baseHisto.GetYaxis().SetTitleSize( 0.08 );
	baseHisto.GetYaxis().SetLabelSize( 0.035 );

        baseHisto.GetYaxis().SetRangeUser(0,1)

        #baseHisto.GetYaxis().SetTitleSize(0.2)
	baseHisto.GetYaxis().SetTitle("f(J^{P})")
        baseHisto.Draw()
 
        pointx = array('f',[0]*5)
        pointy = array('f',[0]*5)
   
        pl_separator = {}
        pl_95CL = {} 
        pl_68CL = {} 
        pl_obs95 = {}
        pl_obs68 = {}
        pl_obs68u = {}
        pl_obs68d = {}
        pm_obs = {}
   
        for i in range(nentries) :
       
           # Model separator
           pointx[0] = 1.5 + i + 1;
           pointx[1] = 1.5 + i + 1;
           pointy[0] = 0;
           pointy[1] = 1;
    
           pl_separator[i] = TPolyLine(2, pointx, pointy, "");
           pl_separator[i].SetLineColor(1);
           pl_separator[i].SetLineStyle(2);
           pl_separator[i].SetLineWidth(1);
           pl_separator[i].Draw("same");
   
           # Expected @ 95% CL  
           pointx[0] = 0.7 + i + 1;
           pointx[1] = 0.7 + i + 1;
           pointx[2] = 1.3 + i + 1;
           pointx[3] = 1.3 + i + 1;
           pointy[0] = 0.0025;
           pointy[1] = vexp_95CL_up[i];
           pointy[2] = vexp_95CL_up[i];
           pointy[3] = 0.0025;
   
           pl_95CL[i] = TPolyLine(4, pointx, pointy, "");
           pl_95CL[i].SetFillColor(Yellow);
           pl_95CL[i].Draw("f");
   
           # Expected @ 95% CL  
           pointx[0] = 0.7 + i + 1;
           pointx[1] = 0.7 + i + 1;
           pointx[2] = 1.3 + i + 1;
           pointx[3] = 1.3 + i + 1;
           pointy[0] = 0.0025;
           pointy[1] = vexp_68CL_up[i];
           pointy[2] = vexp_68CL_up[i];
           pointy[3] = 0.0025;
   
           pl_68CL[i] = TPolyLine(4, pointx, pointy, "");
           pl_68CL[i].SetFillColor(Green);
           pl_68CL[i].Draw("f");
   
           # Observation @ 95% CL (Filled area) 
           if vobs_95CL_up[i] < 1 :
             pointx[0] = 0.6 + i + 1;
             pointx[1] = 0.6 + i + 1;
             pointx[2] = 1.4 + i + 1;
             pointx[3] = 1.4 + i + 1;
             pointy[0] = vobs_95CL_up[i];
             pointy[1] = 0.9975;
             pointy[2] = 0.9975;
             pointy[3] = vobs_95CL_up[i];
   
             pl_obs95[i] = TPolyLine(4, pointx, pointy, "");
             pl_obs95[i].SetFillColor(kBlack);
             pl_obs95[i].SetFillStyle(3254);
             pl_obs95[i].SetLineStyle(2);
             pl_obs95[i].Draw("f");
   
           # Observation @ 68% CL (error line)
           pointx[0] = 1 + i + 1;
           pointx[1] = 1 + i + 1;
           pointy[0] = vobs_68CL_do[i];
           pointy[1] = vobs_68CL_up[i];
       
           pl_obs68[i] = TPolyLine(2, pointx, pointy, "");
           pl_obs68[i].SetLineColor(kBlack);
           pl_obs68[i].SetLineStyle(1);
           pl_obs68[i].SetLineWidth(1);
           pl_obs68[i].SetLineStyle(1);
           pl_obs68[i].Draw("same");
          
           pointx[0] = 0.7 + i + 1;
           pointx[1] = 1.3 + i + 1;
           pointy[0] = vobs_68CL_do[i];
           pointy[1] = vobs_68CL_do[i];
   
           pl_obs68d[i] = TPolyLine(2, pointx, pointy, "");
           pl_obs68d[i].SetLineColor(kBlack);
           pl_obs68d[i].SetLineStyle(1);
           pl_obs68d[i].SetLineWidth(1);
           pl_obs68d[i].SetLineStyle(1);
           pl_obs68d[i].Draw("same");
   
           pointx[0] = 0.7 + i + 1;
           pointx[1] = 1.3 + i + 1;
           pointy[0] = vobs_68CL_up[i];
           pointy[1] = vobs_68CL_up[i];
   
           pl_obs68u[i] = TPolyLine(2, pointx, pointy, "");
           pl_obs68u[i].SetLineColor(kBlack);
           pl_obs68u[i].SetLineStyle(1);
           pl_obs68u[i].SetLineWidth(1);
           pl_obs68d[i].SetLineStyle(1);
           pl_obs68u[i].Draw("same");
   
           # Observation (Point)
   
           pointx[0] = 0.6 + i + 1;
           pointx[1] = 1.4 + i + 1;
           pointy[0] = vobs[i];
           pointy[1] = vobs[i];
   
           pointx[0] = 0.5*pointx[0] + 0.5*pointx[1];
           pointy[0] = 0.5*pointy[0] + 0.5*pointy[0];
   
           pm_obs[i] = TMarker(pointx[0], pointy[0], 8);
           pm_obs[i].SetMarkerColor(kBlack);
           pm_obs[i].SetMarkerStyle(8);
           pm_obs[i].SetMarkerSize(1.0);
           pm_obs[i].Draw("same");
   
        # Title
  
	CP = TLatex();
	CP.SetNDC(kTRUE);
	CP.SetTextSize(0.045);
	CP.SetTextAlign(31);
	CP.SetTextFont(61);
	CP.SetTextAlign(11);
	CP.DrawLatex( 0.07, 0.95, "CMS" );

	CP2 = TLatex();
	CP2.SetNDC(kTRUE);
	CP2.SetTextSize(0.040);
	CP2.SetTextAlign(31);
	CP2.SetTextFont(42);
	CP2.SetTextAlign(11);
	if hwwOnly : 
          CP2.DrawLatex( 0.5, 0.95, "H #rightarrow WW" );
	  CP2.DrawLatex( 0.82 , 0.95, "19.4 fb^{-1} (8 TeV) + 4.9 fb^{-1} (7 TeV)" );
 
	CP3 = TLatex();
	CP3.SetNDC(kTRUE);
	CP3.SetTextSize(0.040);
	CP3.SetTextAlign(31);
	CP3.SetTextFont(52);
	CP3.SetTextAlign(11);
        #CP3.DrawLatex( 0.105, 0.95, "Unpublished" );



        # Legend
        legendx = array('f',[0]*5)
        legendy = array('f',[0]*5)


	
	# Frame coordinates
	legendx[0] = -0.050*(nentries+1)-0.5;
	legendx[1] = -0.050*(nentries+1)-0.5;
	legendx[2] = 0.05*(nentries+1)-0.5;
	legendx[3] = 0.05*(nentries+1)-0.5;
	legendx[4] = legendx[0];
	legendy[0] = -0.295;
	legendy[1] = -0.05;
	legendy[2] = -0.05;
	legendy[3] = -0.295;
	legendy[4] = legendy[0];

        # Observed: Text
     	pointx[0] = (legendx[2] - legendx[0])*0.04 + legendx[0];
	pointx[1] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointy[0] = legendy[0] + 0.21;
	pointy[1] = legendy[0] + 0.21;

	legend_entries2 = TLatex();
	legend_entries2.SetTextSize(0.04);
	legend_entries2.SetTextFont(132);
	legend_entries2.SetTextAlign(12);
	legend_entries2.DrawLatex(pointx[1]+(legendx[2] - legendx[0])*0.02, pointy[0], "Best fit #pm 1#sigma");

        lpl_obs = TPolyLine(2, pointx, pointy, "");
	lpl_obs.SetFillColor(kBlack);
	lpl_obs.SetLineColor(kBlack);
	lpl_obs.SetLineStyle(1);
	lpl_obs.SetLineWidth(2);
	lpl_obs.Draw("same");

        # Observed: Dot
	pointx[0] = 0.5*pointx[0] + 0.5*pointx[1];
	pointy[0] = 0.5*pointy[0] + 0.5*pointy[1];
	lpm_obs = TMarker(pointx[0], pointy[0], 8);
	lpm_obs.SetMarkerColor(kBlack);
	lpm_obs.SetMarkerStyle(8);
	lpm_obs.SetMarkerSize(1.0);
	lpm_obs.Draw("f");

 
	# 95% Onserved exclusion entry coordinates
	pointx[0] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[1] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[2] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointx[3] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointy[0] = legendy[0] + 0.15 - 0.025;
	pointy[1] = legendy[0] + 0.15 + 0.025;
	pointy[2] = legendy[0] + 0.15 + 0.025;
	pointy[3] = legendy[0] + 0.15 - 0.025;

	lpl95 = TPolyLine(4, pointx, pointy, "");
	lpl95.SetFillColor(kBlack);
	lpl95.SetFillStyle(3254);
	lpl95.SetLineStyle(2);
	lpl95.Draw("f");

	legend_entries = TText();
	legend_entries.SetTextSize(0.04);
	legend_entries.SetTextFont(132);
	legend_entries.SetTextAlign(12);
	legend_entries.SetText(pointx[2]+(legendx[2] - legendx[0])*0.02, 0.5*pointy[0] + 0.5*pointy[1],	"Excluded at 95% CL");
	legend_entries.Draw("same");
 
        # Expected 95 CI coordinates
	pointx[0] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[1] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[2] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointx[3] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointy[0] = legendy[0] + 0.09 - 0.025;
	pointy[1] = legendy[0] + 0.09 + 0.025;
	pointy[2] = legendy[0] + 0.09 + 0.025;
	pointy[3] = legendy[0] + 0.09 - 0.025;
	
	lpl_95CL = TPolyLine(4, pointx, pointy, "");
	lpl_95CL.SetUniqueID(3000);
	lpl_95CL.SetFillColor(Yellow);
	lpl_95CL.SetLineStyle(2);
	lpl_95CL.Draw("f");
	
	legend_entries4 = TLatex();
	legend_entries4.SetTextSize(0.04);
	legend_entries4.SetTextFont(132);
	legend_entries4.SetTextAlign(12);
	legend_entries4.DrawLatex(pointx[2]+(legendx[2] - legendx[0])*0.02, 0.5*pointy[0] + 0.5*pointy[1], "Expected at 95% CL");
	
 	# Expected 68 CI coordinates
	pointx[0] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[1] = (legendx[2] - legendx[0])*0.05 + legendx[0];
	pointx[2] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointx[3] = (legendx[2] - legendx[0])*0.20 + legendx[0];
	pointy[0] = legendy[0] + 0.03 - 0.025;
	pointy[1] = legendy[0] + 0.03 + 0.025;
	pointy[2] = legendy[0] + 0.03 + 0.025;
	pointy[3] = legendy[0] + 0.03 - 0.025;
	
	lpl_1s = TPolyLine(4, pointx, pointy, "");
	lpl_1s.SetUniqueID(3000);
	lpl_1s.SetFillColor(Green);
	lpl_1s.SetLineStyle(2);
	lpl_1s.Draw("f");
	
	legend_entries3 = TLatex();
	legend_entries3.SetTextSize(0.04);
	legend_entries3.SetTextFont(132);
	legend_entries3.SetTextAlign(12);
	legend_entries3.DrawLatex(pointx[2]+(legendx[2] - legendx[0])*0.02, 0.5*pointy[0] + 0.5*pointy[1], "Expected at 68% CL");
	
 

        # X-axis

        for i in range(nentries): baseHisto.GetXaxis().SetBinLabel(i+1,'')
        l = TLatex();
	l.SetTextSize(0.058);#	//0.047
	l.SetTextFont(132);
	l.SetTextAlign(12);
	l.SetTextAngle(90);
        l2 = TLatex();
	l2.SetTextSize(0.052);#	//0.047
	l2.SetTextFont(132);
	l2.SetTextAlign(12);
	l2.SetTextAngle(90);

        iLabel=0
        for iType in plotContent:
          for Label in plotContent[iType] :
            pointx[0] = 1 + iLabel + 1;
            pointy[0] = -0.14
            if 'b2' in Label:
              l2.DrawLatex(pointx[0], -0.29 , Label )
            elif '1^' in  Label:
              l.DrawLatex(pointx[0], -0.11 , Label)
            else:
              l.DrawLatex(pointx[0], pointy[0] , Label )
            iLabel += 1

        # Groups

        iProd = 0
        nProd = len(plotContent)
        nlen  = 0
        ptV = {}
        pl_separator_c = {}
        for iType in plotContent : 
          iProd+=1
          nold = nlen
          nlen += len(plotContent[iType]) 
          print iProd
          if iProd < nProd : 
            pointx[0] = nlen+1.5 
            pointx[1] = nlen+1.5 
            pointy[0] = -0.3
            pointy[1] = 0 
            pl_separator_c[iProd] = TPolyLine(2, pointx, pointy, "");
            pl_separator_c[iProd].SetUniqueID(1000+iProd);
            pl_separator_c[iProd].SetLineColor(1);
            pl_separator_c[iProd].SetLineStyle(2);
            pl_separator_c[iProd].SetLineWidth(1);
            pl_separator_c[iProd].Draw("same");

          ptV[iProd] = ( TPaveText(nold+1.5,-0.25 ,nlen+1.5,-0.14) ) 


          ptV[iProd].SetBorderSize(0)
          #ptV[iProd].SetTextAlign(12)
          ptV[iProd].SetFillStyle(0)
          ptV[iProd].SetTextFont(42)
          ptV[iProd].SetTextSize(0.05) 
          ptV[iProd].AddText(0.50, 0.1,iType)
          ptV[iProd].Draw("same")


        #canvas.WaitPrimitive() 
        
        canvas.Modified()
        canvas.SaveAs(plotDir + "NIS_SummaryPlot"+Extra+".pdf")
        canvas.SaveAs(plotDir + "NIS_SummaryPlot"+Extra+".png")
        canvas.SaveAs(plotDir + "NIS_SummaryPlot"+Extra+".root")
        canvas.SaveAs(plotDir + "NIS_SummaryPlot"+Extra+".C")



   def MUMHSum(self,iComb,iEnergy,iModel,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,self.channels[self.Version],self.combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
 
       iTarget = 'MDF1DObs'
       VarName = ['r','deltaNLL','quantileExpected']
       self.TreeContent = {}

       # ---- Load all tree in memory
       for iMass in massList:
         fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
         fileName += '_'+iModel+'_'+iTarget+'_Points*.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
         fileCmd = 'ls '+fileName 
         print fileName 
         proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
         out, err = proc.communicate()
         FileList=string.split(out)
         Result = {}
         Result ['rfit'] = 0
         Result ['scan'] = {}
         for iFile in FileList :
           #print 'Opening :',iFile
           try:
             fTree = TFile.Open(iFile)
             tree = fTree.Get('limit')
             nentries = tree.GetEntries()  
             lm, mh, var = self.treeAccess(tree,VarName)
             for ientry in range(nentries):
               tree.GetEntry(ientry)
               if var[2] != 1 :
                 Result['scan'][dc(var[0])] = dc(var[1])
               else:
                 Result ['rfit'] = dc(var[0])
             fTree.Close() 
           except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'
         self.TreeContent[iMass] = Result

       # ---- Find Some basic values
       unsortMu   = []
       for iMu in self.TreeContent[massList[0]]['scan']: unsortMu.append(iMu) 
       Mu = sorted(unsortMu)
       minMu=Mu[0]
       maxMu=Mu[-1]
       nMu=len(Mu)
       deltaMu = (maxMu-minMu) / nMu

#      # ---- apply shift "bad events" --> Andrea not foing it nDo == 0 !!!
#      Origin='scan' 

#      #for iMass in massList:
#      #  hObs = TH1F("Frame","Frame",len(Mu),Mu[0],Mu[-1])
#      #  for iMu in Mu: 
#      #    if iMu in self.TreeContent[iMass][Origin]: 
#      #      hObs.Fill(iMu,2*self.TreeContent[iMass]['scan'][iMu])
#      #  hObs.Draw()
#      #  self.c1.Update()
#      #  self.Wait() 

#      MuRef20= 99.
#      MuRef15= 99.
#      MuRef10= 99.
#      MuRef05= 99.
#      MuRef01= 99.
#      MuRef02= 99.
#      for iMu in Mu:
#        if abs(iMu-2.0) < abs(MuRef20-2.0) : MuRef20 = iMu
#        if abs(iMu-1.5) < abs(MuRef15-1.5) : MuRef15 = iMu
#        if abs(iMu-1.0) < abs(MuRef10-1.0) : MuRef10 = iMu
#        if abs(iMu-0.5) < abs(MuRef05-0.5) : MuRef05 = iMu
#        if abs(iMu-0.1) < abs(MuRef01-0.1) : MuRef01 = iMu
#        if abs(iMu-0.2) < abs(MuRef02-0.2) : MuRef02 = iMu
#      MuRef = []
#      #MuRef.append(Mu[0])
#      #MuRef.append(Mu[1])
#      #if ( MuRef01 < 99 ) :  MuRef.append( MuRef01 )
#      #if ( MuRef02 < 99 ) :  MuRef.append( MuRef02 )
#      #if ( MuRef05 < 99 ) :  MuRef.append( MuRef05 )
#      #if ( MuRef10 < 99 ) :  MuRef.append( MuRef10 )
#      #if ( MuRef15 < 99 ) :  MuRef.append( MuRef15 )
#      #if ( MuRef20 < 99 ) :  MuRef.append( MuRef20 )
#      MuRef.append(Mu[-1])

#      MuRef2 = []
#      MuRef2.append(Mu[0])
#      MuRef2.append( MuRef05 )
#      MuRef2.append( MuRef10 )
#      MuRef2.append( MuRef15 )

#      Tolerance =  [0.02 , 0.50]
#      ToleranceM = [110  , 135 ]
#      CorrFactor= {}
#      iPass = 0
#      Pass = 'scan'
#      for iMu in MuRef:        
#        iPass+=1
#        CorrFactor[iPass] = [1.]
#        print "MuRef = ",iMu
#        hFit  = TH1F("Scan","Scan",len(massList),massList[0],massList[-1])
#        jMass=-1
#        for iMass in massList:
#          jMass+=1
#          if iMu in self.TreeContent[iMass][Origin]:
#              
#            if iMass==massList[0]: 
#              hFit.Fill(iMass,self.TreeContent[iMass][Pass][iMu])
#            else:
#              Actual   = self.TreeContent[iMass][Pass][iMu]             * CorrFactor[iPass][jMass-1]
#              Previous = self.TreeContent[massList[jMass-1]][Pass][iMu] * CorrFactor[iPass][jMass-1]
#              Delta    = abs(Actual-Previous)
#              DeltaRel = Delta/Previous

#              print jMass, Actual, Previous, Delta , Delta/Previous
#              if DeltaRel > Tolerance[iPass-1] and iMass > ToleranceM[iPass-1] : 
#                if   jMass == 1 : nPFit = 1
#                elif jMass == 2 : nPFit = 2
#                elif jMass == 3 : nPFit = 3
#                else            : nPFit = 4
#                fit = TF1("pol1","[0]*x+[1]",massList[jMass-nPFit],massList[jMass-1])
#                hFit.Fit(fit,"R")
#                A = fit.GetParameter(0)
#                B = fit.GetParameter(1)
#                hFit.Draw()
#                self.c1.Update()
#                self.Wait()
#                Corrected = A*iMass+B
#                #shift = self.TreeContent[massList[0]][Origin][Mu[0]] - self.TreeContent[iMass][Origin][Mu[0]]
#                #Corrected = Actual + shift + 0.1
#                print '-->', Corrected , abs(Corrected-Previous) , abs(Corrected-Previous)/Previous
#              else: 
#                Corrected = Actual
#              CorrFactor[iPass].append(CorrFactor[iPass][jMass-1]*Corrected/Actual)               
#              hFit.Fill(iMass,Corrected)

#        jMass=-1
#        for iMass in massList:
#          jMass+=1
#          PassNew='mufit_'+str(iPass)
#          self.TreeContent[iMass][PassNew] = {} 
#          for iMu in Mu: 
#            if iMu in self.TreeContent[iMass][Origin]:  
#              self.TreeContent[iMass][PassNew][iMu] = self.TreeContent[iMass][Pass][iMu]*CorrFactor[iPass][jMass-1]
#        Pass = PassNew

#       hCor  = TH1F("Scan","Scan",len(massList),massList[0],massList[-1])
#       jMass=-1
#       for iMass in massList:
#         jMass +=1
#         hCor.Fill(iMass,self.TreeContent[iMass]['scan'][Mu[0]]*CorrFactor[jMass])
#         self.TreeContent[iMass]['mu0fit'] = {}    
#         for iMu in Mu: 
#           if iMu in self.TreeContent[iMass][Origin]:  
#             self.TreeContent[iMass]['mu0fit'][iMu] = self.TreeContent[iMass][Origin][iMu]*CorrFactor[jMass]
#
#       hCor.Draw()
#       self.c1.Update()
#       self.Wait() 
#
#       for iMu in MuRef2:        
#         print "MuRef = ",iMu
#         hScan = TH1F("Scan","Scan",len(massList),massList[0],massList[-1])
#         hCor  = TH1F("cor" ,"cor" ,len(massList),massList[0],massList[-1])
#         jMass=-1
#         for iMass in massList:
#           jMass+=1
#           if iMu in self.TreeContent[iMass][Origin]: 
#             hScan.Fill(iMass,self.TreeContent[iMass]['scan'][iMu])
#             hCor.Fill(iMass,self.TreeContent[iMass]['mu0fit'][iMu])
#         print iMu
#         hScan.Draw()
#         self.c1.Update()
#         self.Wait() 
#
#         hCor.Draw("same")
#         self.c1.Update()
#         self.Wait() 


       # ---- apply shift for mu=0 same performance ----
       Origin='scan'
       for iMass in massList:
         #print   iMass, self.TreeContent[iMass][Origin][Mu[1]] 
         shift = self.TreeContent[massList[0]][Origin][Mu[1]] - self.TreeContent[iMass][Origin][Mu[1]] + 0.1 # 0.1 arbitrary
         self.TreeContent[iMass]['mu0corr'] = {}  
         print "mu0corr = ", shift 
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]: 
             self.TreeContent[iMass]['mu0corr'][iMu] = self.TreeContent[iMass][Origin][iMu] + shift
    
       # ---- Fit Mu close to zero
       Origin='scan'
       C0 = 0.
       for iMass in massList: 
         hFit = TH1F("Fit" ,"Fit" ,len(Mu),0,3.)
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]: 
             hFit.Fill(iMu,self.TreeContent[iMass][Origin][iMu])
         hFit.Draw()
         fit = TF1("pol2","[0]*x*x+[1]*x+[2]",0,0.5)
         hFit.Fit(fit,"R")
         C = fit.GetParameter(2)
         if iMass == massList[0] : 
           C0    = C
           shift = 1
         else:
           shift = C0 - C
         print "mu0fit  = ", shift 
         self.TreeContent[iMass]['mu0fit'] = {}  

         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]: 
             self.TreeContent[iMass]['mu0fit'][iMu] = self.TreeContent[iMass][Origin][iMu] + shift
         #self.c1.Update()
         #self.Wait() 

       # ---- Average -------

       Origin='mu0fit' 
       for iMass in massList:
         self.TreeContent[iMass]['Average'] = {} 
         cMu    =0
         nMuAvg =0
         Mu2Avg =[]
         NLL2Avg=0
         MuNew  =[]
         for iMu in Mu:
           cMu+=1 
           if cMu == 1 : Mu2Avg.append(dc(iMu))
           if cMu ==10 : Mu2Avg.append(dc(iMu))
           if iMu in self.TreeContent[iMass][Origin]: 
             nMuAvg+=1
             NLL2Avg+= self.TreeContent[iMass][Origin][iMu]
           if cMu ==10 :
             NLLAvg= NLL2Avg/nMuAvg 
             MuAvg = Mu2Avg[0]+(Mu2Avg[1]-Mu2Avg[0])/2 
             self.TreeContent[iMass]['Average'][MuAvg] = NLLAvg
             if not MuAvg in MuNew : MuNew.append(dc(MuAvg))
             cMu    =0
             nMuAvg =0
             Mu2Avg =[]
             NLL2Avg=0
       print Mu
       #Mu = MuNew
       print Mu


       # ---- apply shift for minLL = 0 ----
       Origin='mu0corr'
       Origin='mu0fit' 
       #Origin='Average'
       minZ  = 9999
       muMin = -1
       mhMin = -1
       for iMass in massList:
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]:  
             if self.TreeContent[iMass][Origin][iMu] < minZ :
               minZ  = self.TreeContent[iMass][Origin][iMu]
               muMin = iMu
               mhMin = iMass
       for iMass in massList:
         self.TreeContent[iMass]['minLLcorr'] = {} 
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]: 
             self.TreeContent[iMass]['minLLcorr'][iMu] = self.TreeContent[iMass][Origin][iMu] - minZ
      
       # ---- repair mu=0.5 plo2 behaviour ----
       Origin='minLLcorr'
       MuRef=99
       DMU=99
       for iMu in Mu:
         if abs(iMu-0.2) < DMU:
           DMU=abs(iMu-0.2) 
           MuRef=iMu
       hFit  = TH1F("Scan","Scan",len(massList),massList[0]-0.5,massList[-1]+0.5) 
       hOri  = TH1F("Scan","Scan",len(massList),massList[0]-0.5,massList[-1]+0.5) 
       hFit.Fill(massList[-1],self.TreeContent[massList[-1]][Origin][MuRef])
       jMass=-1
       CorrFac=[1.]
       for iMass in massList:
         jMass+=1
         print self.TreeContent[iMass][Origin][MuRef],CorrFac[jMass],self.TreeContent[iMass][Origin][MuRef]*CorrFac[jMass]
         hFit.Fill(iMass,self.TreeContent[iMass][Origin][MuRef]*CorrFac[jMass])
         hOri.Fill(iMass,self.TreeContent[iMass][Origin][MuRef])
         if iMass < 120 :
           CorrFac.append(1.)
         else:
           fit = TF1("pol2","[0]*x*x+[1]*x+[2]",115,massList[-1]+0.5)
           hFit.Fit(fit,"R")
           #hFit.Draw()
           #self.c1.Update()
           if jMass+1 < len(massList) :
            A = fit.GetParameter(0)
            B = fit.GetParameter(1)
            C = fit.GetParameter(2)
            X = massList[jMass+1] 
            Y = A*X*X+B*X+C
            V = self.TreeContent[massList[jMass+1]][Origin][MuRef]*CorrFac[jMass]
            print jMass , iMass , massList[jMass+1] , Y , V , abs(1-V/Y)      
            if abs(1-V/Y)>0.10: 
             print '--> Need Correction '
             CorrFac.append(CorrFac[jMass]*Y/V)
             #CorrFac.append(CorrFac[jMass-1])
            else:
             CorrFac.append(CorrFac[jMass])

            #self.Wait() 
           #  if  abs(V/Y) > .20:
           #    CorrFac.append(CorrFac[jMass])
           #  else:
           #    CorrFac.append(CorrFac[jMass])

       hFit.Draw()
       hOri.Draw("histsame")
       self.c1.Update()
       self.Wait() 

       jMass=-1
       for iMass in massList:
         jMass+=1
         self.TreeContent[iMass]['mu05pol2'] = {} 
         for iMu in self.TreeContent[iMass][Origin]: 
           #if iMu in self.TreeContent[iMass][Origin]:
           print iMass, iMu , self.TreeContent[iMass][Origin][iMu]
           self.TreeContent[iMass]['mu05pol2'][iMu] = self.TreeContent[iMass][Origin][iMu] * CorrFac[jMass]

       # ---- re-apply shift for minLL = 0 ----
       Origin='mu05pol2'
       minZ  = 9999
       muMin = -1
       mhMin = -1
       for iMass in massList:
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]:  
             if self.TreeContent[iMass][Origin][iMu] < minZ :
               minZ  = self.TreeContent[iMass][Origin][iMu]
               muMin = iMu
               mhMin = iMass
       for iMass in massList:
         self.TreeContent[iMass]['minLLcorr2'] = {} 
         for iMu in Mu: 
           if iMu in self.TreeContent[iMass][Origin]: 
             self.TreeContent[iMass]['minLLcorr2'][iMu] = self.TreeContent[iMass][Origin][iMu] - minZ
      


 
       # --- Write 2D Tree
       Origin='scan'
       #Origin='mu0corr'
       Origin='minLLcorr'
       #Origin='minLLcorr2'
       #Origin='mu0fit'
       #Origin=Pass
       fModel = 'mHmuHist'
       if   iModel == 'mHmuHist' :
         fTarget = 'MDFGridObs'
       elif iModel == 'mHmuHistSMInj' :
         fTarget = 'MDFGridExp'
         TargetDir = TargetDir.replace('masssminj','mass')
       else:
         return

       fileName =  TargetDir+'/125/higgsCombine_'+iComb+'_'+fModel+'_'+fTarget+'.MultiDimFit.mH125.root'
       print fileName
       f = TFile(fileName,'RECREATE')
       t = TTree('limit','My test tree')
       gROOT.ProcessLine(\
              "struct MyStruct{\
                Float_t mh;\
                Float_t limit;\
                Float_t r;\
                Float_t deltaNLL;\
                Float_t quantileExpected;\
               };")  
       from ROOT import MyStruct 
       s = MyStruct()
       t.Branch('mh',AddressOf(s,'mh'),'mh/F')
       t.Branch('limit',AddressOf(s,'limit'),'limit/F')
       t.Branch('r',AddressOf(s,'r'),'r/F')
       t.Branch('deltaNLL',AddressOf(s,'deltaNLL'),'deltaNLL/F')
       t.Branch('quantileExpected',AddressOf(s,'quantileExpected'),'quantileExpected/F')
       s.limit = 0
       for iMass in massList:
         s.mh       = iMass 
         s.r        = self.TreeContent[iMass]['rfit']
         s.deltaNLL = 0
         s.quantileExpected = 1 
         t.Fill()
         for iMu in Mu:
           if iMu in self.TreeContent[iMass][Origin]:
             s.mh       = iMass 
             s.r        = iMu
             s.deltaNLL =  self.TreeContent[iMass][Origin][iMu]
             s.quantileExpected = 0 
             t.Fill()
    
       f.Write()
       f.Close()
       

       #print  self.TreeContent[125]['minLLcorr']
       #print  self.TreeContent[130]['minLLcorr']


   
   def MHFit(self,iComb,iEnergy,iModel,muVal):
      
       self.squareCanvas(False,False)  
       self.c1.cd()

       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       if self.blind : 
         iTarget = 'MDFGridExp'
       else:
         iTarget = 'MDFGridObs'

       fileName =  TargetDir+'/125/higgsCombine_'+iComb+'_'+iModel+'_'+iTarget+'.MultiDimFit.mH125.root'
       VarName = ['r','deltaNLL','quantileExpected','mh']
       
       fTree = TFile.Open(fileName)
       fTree.ls()
       tree = fTree.Get('limit')
       tree.Print()
       nentries = tree.GetEntries()  
       lm, mh, var = self.treeAccess(tree,VarName)
       Result  = {}
       usmList = []
       MU =99.
       DMU=99.
       for ientry in range(nentries):
         tree.GetEntry(ientry)
         if abs(dc(var[0])-muVal) < DMU and var[1] != 0:
           MU  = dc(var[0])
           DMU = abs(dc(var[0])-muVal)
       for ientry in range(nentries):
         tree.GetEntry(ientry)
         if var[0] == MU : 
           print var[0], var[3] , var[1] 
           usmList.append(dc(var[3])) 
           Result[dc(var[3])] = dc(var[1]) 
       fTree.Close()
       mList = sorted(usmList)

       minXP = mList[0]  - 0.5
       maxXP = mList[-1] + 0.5
       hObs = TH1F("Frame","Frame",len(mList),float(minXP),float(maxXP))
       for iMass in mList :
         hObs.Fill(iMass,2*Result[iMass])
       hObs.GetXaxis().SetRangeUser(109.5,135.5)
       hObs.GetYaxis().SetRangeUser(0,15)
       hObs.GetXaxis().SetTitle("Higgs boson mass [GeV]")
       hObs.GetYaxis().SetTitle("-2 #Delta ln L")

       hObs.GetXaxis().SetLabelFont (   42)
       hObs.GetYaxis().SetLabelFont (   42)
       hObs.GetXaxis().SetTitleFont (   42)
       hObs.GetYaxis().SetTitleFont (   42)
       hObs.GetXaxis().SetTitleOffset( 1.2)
       hObs.GetYaxis().SetTitleOffset( 1.2)
       hObs.GetXaxis().SetTitleSize (0.050)
       hObs.GetYaxis().SetTitleSize (0.050)
       hObs.GetXaxis().SetLabelSize (0.045)
       hObs.GetYaxis().SetLabelSize (0.045)


       hObs.SetFillStyle(0)
       hObs.SetLineWidth(2)
       hObs.Draw("hist")
       fit = TF1("pol2","[0]*x*x+[1]*x+[2]",109.5,135.5)
       fit.SetLineWidth(3)
       fit.SetLineColor(kBlue)
       hObs.Fit(fit,"R")
       fMin = fit.GetMinimum()
       
       self.c1.Update()
       self.Wait()

       A = fit.GetParameter(0)
       B = fit.GetParameter(1)
       C = fit.GetParameter(2)
       M = C-B*B/(4*A)

       # Offset to ZERO 
       for i in xrange(1,hObs.GetNbinsX()+1):
         V = hObs.GetBinContent(i)
         hObs.SetBinContent(i,V-M) 

       #Draw
       gStyle.SetOptFit(0)
       hObs.Draw("hist")
       fit.SetParameter(2,C-M)
       C = C-M
       fit.Draw("same")
       self.c1.Update()
       fMin = 0.
       
       # find X Zero-intercept
       X0 = 0
       DY = 99.
       for X in numpy.arange(110,140,0.1):
          Y = A*X*X+B*X+C
          if abs(Y) < DY : 
            DY = Y
            X0 = X
       
       # find 1/2 Sigma
       X1L = 0
       X2L = 0
       DY1L = 99.
       DY2L = 99.
       for X in numpy.arange(110,140,0.05):
         Y = A*X*X+B*X+C
         if X < X0:
           if abs(Y-1) < DY1L:
             DY1L = Y-1
             X1L  = X
           if abs(Y-4) < DY2L:
             DY2L = Y-4
             X2L  = X
       X1R = X0 + abs(X0-X1L) 
       X2R = X0 + abs(X0-X2L) 
       #print X0, X1L , X1R , X2L , X2R 
       print 'MH = ', X0 , ' +- ' , abs(X0-X1L) 


       lMass=[]
       lMass.append(100.)
       lMass.append(150.)
       self.plotHorizLine('Zero', lMass , fMin ,   kRed , 1    , 'Zero')
       self.plotHorizLine('One' , lMass , fMin+1 , kRed , 1    , '1sigma')
       self.plotHorizLine('Four', lMass , fMin+4 , kRed , 1    , '2sigma')
       self.plotAllObj(['One','Four'],True)

       NLL1=[0,1]       
       NLL2=[0,4]       
       self.plotVertLine('X2L', X2L , NLL2 , kRed , 1    , '1sigma')
       self.plotVertLine('X1L', X1L , NLL1 , kRed , 1    , '1sigma')
       self.plotVertLine('X1R', X1R , NLL1 , kRed , 1    , '1sigma')
       self.plotVertLine('X2R', X2R , NLL2 , kRed , 1    , '1sigma')
       self.plotAllObj(['X2L','X1L','X1R','X2R'],True)        


       self.addTitle()

       self.c1.Update()
       self.Wait()
       if self.blind : 
         self.Save("mhfit_SMInj_"+iComb+'_'+self.EnergyName(iEnergy)+'_mu'+str(muVal).replace('.','d') )
       else:
         self.Save("mhfit_"+iComb+'_'+self.EnergyName(iEnergy)+'_mu'+str(muVal).replace('.','d') )


   def printResults(self,iComb='hww012j_vh3l_vh2j_zh3l2j_shape',iEnergy=0,iModel='SMHiggs',massFilter=[125],printList=[]):
     
      self.squareCanvas(False,False)  
      self.Results = {}

      if 'ACLsExp'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp') 
      if 'ACLsBlind'in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsBlind') 
      if 'RVACLsBlind'in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'RVACLsBlind') 
      if 'RFACLsBlind'in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'RFACLsBlind') 
      if 'ACLsExpPost'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExpPost') 
      if 'ACLsInjPre'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsInjPre') 
      if 'ACLsBkgOnly' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsBkgOnly')
      if 'SExpPre'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'SExpPre') 
      if 'PVExpPre' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'PVExpPre') 
      if 'SExpPost'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'SExpPost')
      if 'PVExpPost' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'PVExpPost')
      if 'BestFitExp' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFitExp')

      if (not self.blind ) :
        if 'ACLs'    in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLs'   ) 
        if 'ACLsObs' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsObs') 
        if 'SObs'    in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'SObs') 
        if 'PVObs'    in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'PVObs') 
        if 'BestFit'  in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFit')
        if 'BestFitG' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFitG')
        if 'BestFitT' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFitT')
 
      #print self.Results

      # build Mass List
      allList = []
      #print iComb , self.Results
      #print self.Results[iComb][iEnergy][iModel]
      for iTarget in self.Results[iComb][iEnergy][iModel]: allList.extend(self.Results[iComb][iEnergy][iModel][iTarget]['mass'])
      AllMass = sorted(list(set(allList)))
     
      # Files
      txtFile=''
 
      # Header
      txtPrint='| mH  '
      texPrint=''
      if 'ACLsObs' in printList : 
         txtPrint+='| CLsObs '
      if 'ACLs'    in printList :
         txtPrint+='|CLsObsVH'
      if 'ACLsInjPre'  in printList :
         txtPrint+='| CLsInj '
      if 'ACLsBkgOnly'  in printList :
         txtPrint+='| CLsInjBkg '
      if 'ACLsExp' in printList : 
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'ACLsBlind' in printList :
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'RVACLsBlind' in printList :
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'RFACLsBlind' in printList :
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'ACLsExpPost' in printList : 
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'SObs'    in printList : 
         txtPrint+='| SObs '
      if 'SExpPre' in printList : 
         txtPrint+='| SExpPre '
      if 'SExpPost' in printList :
         txtPrint+='| SExpPost '
      if 'PVObs'    in printList : 
         txtPrint+='| pVal Obs '
      if 'PVExpPre' in printList : 
         txtPrint+='| pVal ExpPre '
      if 'PVExpPost' in printList :
         txtPrint+='| pVal ExpPost '
      if 'BestFit' in printList : 
         txtPrint+='| BestFit '
      if 'BestFitG' in printList : 
         txtPrint+='| BestFitG '
      if 'BestFitT' in printList : 
         txtPrint+='| BestFitT '
      if 'BestFitExp' in printList : 
         txtPrint+='| BestFitExp '


      print txtPrint
      # Loop on mass and print values
      for iMass in AllMass:
        txtPrint='| '+str(iMass)+' '
        texPrint='  '+str(iMass)
        if 'ACLsObs' in printList :
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsObs','Val')
            txtPrint+='| '+str(round(Val,2))+' '  
          else:
            txtPrint+='|  X  ' 
        if 'ACLs'    in printList :
          if (not self.blind ) :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLs'   ,'Val')
            txtPrint+='| '+str(round(Val,2))+' '
          else:
            txtPrint+='|  X  '
        if 'ACLsInjPre' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsInjPre','Val')
          txtPrint+='| '+str(round(Val,2))+' '  
        if 'ACLsBkgOnly' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBkgOnly','Val')
          txtPrint+='| '+str(round(Val,2))+' '
        if 'ACLsExp' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','95U')
            txtPrint+='| '+str(round(Val,2))+' | '+str(round(d95,2))+' | '+str(round(d68,2))+' | '+str(round(u68,2))+' | '+str(round(u95,2)) 
        if 'ACLsBlind' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBlind','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBlind','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBlind','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBlind','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsBlind','95U')
            txtPrint+='| '+str(round(Val,2))+' | '+str(round(d95,2))+' | '+str(round(d68,2))+' | '+str(round(u68,2))+' | '+str(round(u95,2)) 
        if 'RVACLsBlind' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RVACLsBlind','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RVACLsBlind','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RVACLsBlind','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RVACLsBlind','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RVACLsBlind','95U')
            txtPrint+='| '+str(round(Val,2))+' | '+str(round(d95,2))+' | '+str(round(d68,2))+' | '+str(round(u68,2))+' | '+str(round(u95,2))
        if 'RFACLsBlind' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RFACLsBlind','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RFACLsBlind','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RFACLsBlind','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RFACLsBlind','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'RFACLsBlind','95U')
            txtPrint+='| '+str(round(Val,2))+' | '+str(round(d95,2))+' | '+str(round(d68,2))+' | '+str(round(u68,2))+' | '+str(round(u95,2))
        if 'ACLsExpPost' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExpPost','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExpPost','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExpPost','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExpPost','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExpPost','95U')
            txtPrint+='| '+str(round(Val,2))+' | '+str(round(d95,2))+' | '+str(round(d68,2))+' | '+str(round(u68,2))+' | '+str(round(u95,2)) 
        if 'SObs'     in printList :
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'SObs','Val')
            txtPrint+='| '+str(round(Val,2))+' '  
          else:
            txtPrint+='|  X  ' 
        if 'SExpPre' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'SExpPre','Val')
          txtPrint+='| '+str(round(Val,2))+' '  
        if 'SExpPost' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'SExpPost','Val')
          txtPrint+='| '+str(round(Val,2))+' '
        if 'PVObs'     in printList :
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'PVObs','Val')
            txtPrint+='| '+str(round(Val,5))+' '  
          else:
            txtPrint+='|  X  ' 
        if 'PVExpPre' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'PVExpPre','Val')
          txtPrint+='| '+str(round(Val,5))+' ' 
        if 'PVExpPost' in printList :
          Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'PVExpPost','Val')
          txtPrint+='| '+str(round(Val,5))+' '
        if 'BestFit' in printList : 
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFit','Val')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFit','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFit','68U')
            ed=Val-d68
            eu=u68-Val 
            #print Val, u68, d68
            txtPrint+='| '+str(round(Val,2))+' - '+str(round(ed,2))+' + '+str(round(eu,2))+' '
        if 'BestFitG' in printList : 
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitG','Val')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitG','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitG','68U')
            ed=Val-d68
            eu=u68-Val 
            #print Val, u68, d68
            txtPrint+='| '+str(round(Val,3))+' - '+str(round(ed,2))+' + '+str(round(eu,2))+' '
        if 'BestFitT' in printList : 
          if (not self.blind ) : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitT','Val')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitT','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitT','68U')
            ed=Val-d68
            eu=u68-Val 
            #print Val, u68, d68
            txtPrint+='| '+str(round(Val,3))+' - '+str(round(ed,2))+' + '+str(round(eu,2))+' '
        if 'BestFitExp' in printList : 
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitExp','Val')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitExp','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'BestFitExp','68U')
            ed=Val-d68
            eu=u68-Val 
            #print Val, u68, d68
            txtPrint+='| '+str(round(Val,3))+' - '+str(round(ed,2))+' + '+str(round(eu,2))+' '

  
        print txtPrint 

      #print self.Results

      self.c1.Close()
 

def Test():

  plot = combPlot(False)
  
  #model='TwoHiggs'
  #model='MH125BG'
  model='SMHiggs'
  comList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape']
  
  plot.plotExpSignVsMh(comList,0,model,[])
  plot.Wait()
  plot.plotExpLimits(comList,0,model,[])
  plot.Wait()
  sys.exit()
  
  
  #comb='hww0jet_shape'
  #comb='hww1jet_shape'
  #comb='hww01jet_shape'
  #comb='hwwvh2j_cut'
  #comb='hwwvh3l_shape'
  #comb='hww2j_hcp'
  #comb='hww_01jet_vh3l_vh2j'
  #comb='hww_01jet_2jhcp_vh3l_vh2j'
  
  comb='hww012j_vh3l_vh2j_zh3l2j_shape'
  comb='hww012j_vh3l_vh2j_shape'
  #comb='zh3l2j_shape'
  #comb='hwwvh2j_cut'
  #comb='vh3l_shape'
  comb='hww2j_shape'
  comb='hww2j_cut'
  comb='hww01jet_shape'
  
  
  #model='OneHiggs'
  #model='TwoHiggs'
  #model='MH125BG'
  model='SMHiggs'
  
  
  
  #plot.printResults()
  #plot.plotOneLimit(comb,0,model,[110,115,120,125,130,140,150,160,170,180,190,200])
  #plot.Wait()
  #plot.plotMuVsMh(comb,0,model,[])
  #plot.Wait()
  plot.plotSignVsMh(comb,0,model,[],'Pre')
  plot.Wait()
  #plot.plotSignVsMh(comb,0,model,[],'Post')
  #plot.Wait()
  
  
  #plot.plotLimit()
  
  #plot.squareCanvas()
  #plot.defHist() 
  #plot.addTitle()
  #plot.Wait()
  #plot.Save("sq")
  
  #plot.rectangleCanvas()
  #plot.defHist() 
  #plot.addTitle()
  #plot.Wait()
  #plot.addAxisTitle("x","Y")
  #plot.Save("rec")
