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

from Config import *
import combTools

gROOT.SetBatch()
#gROOT.ProcessLine(".x tdrstyle.cc")
gROOT.ProcessLine('.L '+combscripts+'contours.cxx')
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)

CMSText=["CMS Preliminary","#bf{CMS}"] 
LumText=["4.9 fb^{-1} (7 TeV) + 19.4 fb^{-1} (8 TeV)","#sqrt{s} = 7 TeV, L = 4.9 fb^{-1}","#sqrt{s} = 8 TeV, L = 19.5 fb^{-1}"]
#LumText=["#sqrt{s} = 7 TeV, L = 4.9 fb^{-1} ; #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}","#sqrt{s} = 7 TeV, L = 4.9 fb^{-1}","#sqrt{s} = 8 TeV, L = 19.5 fb^{-1}"]

class combPlot :
   def __init__(self,Version,blind=True,postFix='',logX=False,logY=False):
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
   
       x1=0.10
       y1=0.92
       x2=0.99
       y2=0.98
       if iCMS == 0 :
         fontSize = 0.04 
         if self.isSquareCanvas : fontSize = 0.027 
       else:
         fontSize = 0.04 
         if self.isSquareCanvas : fontSize = 0.033
   
       self.cmsprel = TPaveText(x1,y1,x2,y2,"brtlNDC");  
       self.cmsprel.SetTextSize(fontSize);
       self.cmsprel.SetFillColor(0)
       self.cmsprel.SetFillStyle(0)
       self.cmsprel.SetLineStyle(0)
       self.cmsprel.SetLineWidth(0)
       self.cmsprel.SetTextAlign(11)
       self.cmsprel.SetTextFont(42);
       self.cmsprel.AddText(CMSText[iCMS]);
       self.cmsprel.SetBorderSize(0);
       self.cmsprel.Draw("same");

       self.lumi = TPaveText(x1,y1,x2,y2,"brtlNDC");  
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
       os.system('convert '+self.plotsdir+'/'+Name+pF+'.pdf '+self.plotsdir+'/'+Name+pF+'.png') 
       os.system('convert '+self.plotsdir+'/'+Name+pF+'.pdf '+self.plotsdir+'/'+Name+pF+'.gif') 

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

   def readResults(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],iTarget='BestFit'):

       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb
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
           fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
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
           fileCmd  = 'ls '+TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
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

   def readMDFGrid(self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFGridObs'):
       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       for iMass in massList :
         fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
         fileName += '_'+iModel+'_'+iTarget+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
         print  fileName   
         
         if   physmodels[iModel]['MDFTree']['NDim'] == 2 :
           try:
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
             if iModel == 'cVcF' and iTarget== 'MDFGridObs' : ROOT.h2d.Fill(0.67,1.5399999,2.30)
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
             self.Obj2Plot['h2d__'+objName]['Obj'].GetXaxis().SetRangeUser(minXP,maxXP)
             self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
             self.Obj2Plot['h2d__'+objName]['Obj'].GetYaxis().SetRangeUser(minYP,maxYP)
             self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
             self.Obj2Plot['h2d__'+objName]['Obj'].GetZaxis().SetRangeUser(0.00001,20.)
             #for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineColor(kRed) 
             for X in TIter(self.Obj2Plot['c68__'+objName]['Obj']) : X.SetLineWidth(3) 
             #for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineColor(kRed) 
             for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineWidth(3) 
             for X in TIter(self.Obj2Plot['c95__'+objName]['Obj']) : X.SetLineStyle(2) 
             #self.Obj2Plot['gr0__'+objName]['Obj'].SetMarkerColor(kRed) 
             gROOT.ProcessLine('fTree->Close()') 
           except:
             print 'WARNING: Specified root file doesn\'t exist --> Putting ZERO'

       return

   def readMDFVal(self,iComb='hww01jet_shape',iEnergy=0,iModel='rVrFXSH',massFilter=[],iTarget='MDFCrossExp68',algo='Single'):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
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
               print '2D:', VarName[0] , Result[VarName[0]][0] , '+' ,  Result[VarName[0]+'_Left'][0]-Result[VarName[0]][0] , '-' , Result[VarName[0]][0]-Result[VarName[0]+'_Right'][0]
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
       obj.SetLineWidth(2)
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
               self.Obj2Plot[X]['Obj'].Draw("AL")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("L") 

       self.c1.Update() 

   def plotObjLeg(self,Order=[],Title='',Position='TopRight'):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot] 
       if   'Right' in Position :
         x1 = 0.47
         x2 = 0.8  
       elif 'Left'  in Position :
         x1 = 0.17
         x2 = 0.47  
       if   'Top'   in Position :
         y1 = 0.87-(len(Order)+1)*.040
         y2 = 0.87 
       elif 'Bottom' in Position : 
         y1 = 0.50-(len(Order)+1)*.040
         y2 = 0.50 
       #self.Legend = TLegend(0.50,0.65,0.85,0.85)   
       self.Legend = TLegend(x1,y1,x2,y2)
       self.Legend.SetTextSize(0.033)
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

   def plotOneLimit(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],bInject=True):

       self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp')
       if not self.blind : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsObs')
       if bInject        : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsSMToysNoSyst')
       #plot.readResults(comb,0,'SMInject',[],'ACLsObs')

       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       if (bInject) : self.postFix += '_inj125'
       
       if (self.logX) : gPad.SetLogx()
       if (self.logY) : gPad.SetLogy()
       if (self.logX) : self.postFix += '_logX'
       if (self.logY) : self.postFix += '_logY'
 
       self.xAxisTitle = "Higgs boson mass [GeV]"
       self.yAxisTitle = "95% CL limit on #sigma/#sigma_{SM}"

 
       aMass         = self.Results[iComb][iEnergy][iModel]['ACLsExp']['mass']
       aMedExpLimit  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['Val']
       aExpLimit68D  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['68D']
       aExpLimit68U  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['68U'] 
       aExpLimit95D  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['95D']
       aExpLimit95U  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['95U']

       if bInject :        
         aMedInjLimit  = self.Results[iComb][iEnergy][iModel]['ACLsSMToysNoSyst']['Val']
         aInjLimit68D  = self.Results[iComb][iEnergy][iModel]['ACLsSMToysNoSyst']['68D']
         aInjLimit68U  = self.Results[iComb][iEnergy][iModel]['ACLsSMToysNoSyst']['68U'] 
         aInjLimit95D  = self.Results[iComb][iEnergy][iModel]['ACLsSMToysNoSyst']['95D']
         aInjLimit95U  = self.Results[iComb][iEnergy][iModel]['ACLsSMToysNoSyst']['95U']
         #aMedInjFast   = self.Results[iComb][iEnergy]['SMInject']['ACLsObs']['Val']

       if (not self.blind ) :  aObsLimit = self.Results[iComb][iEnergy][iModel]['ACLsObs']['Val']

       self.plotHorizBand('95CL', aMass , aMedExpLimit , aExpLimit95U , aExpLimit95D ,  90 , 1001 , 'Expected #pm 2#sigma')
       self.plotHorizBand('68CL', aMass , aMedExpLimit , aExpLimit68U , aExpLimit68D , 211 , 1001 , 'Expected #pm 1#sigma')
       self.plotHorizCurve('Exp', aMass , aMedExpLimit , kBlack , 2          ,  2          ,     'Median Expected')

       if (not self.blind ) : self.plotHorizCurve('Obs', aMass , aObsLimit , kBlack , 1  , 3 , 'Observed')

       if  bInject :  
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
       self.plotHorizLine('Line', lMass , 1. , kBlack , 1    , 'CL=1')


       self.SetRange('Limit',iComb)
       self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(aMass[0],aMass[-1])
       self.plotAllObj(['95CL','68CL','Exp','95CLInj','68CLInj','Inj','Obs','Line'])
       self.plotObjLeg(['Obs','Exp','68CL','95CL','Inj','68CLInj','95CLInj'],combinations[iComb]['legend'])
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'Limit',iComb)
       self.addTitle() 
       #self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
       #self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.1,500.)
       #self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
       self.c1.Update() 
       self.Save('limit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)
       #self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
       self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
       #self.Save('limit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel+'_zoom')
       
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
       
       self.SetRange('BestFit',iComb)
       self.plotAllObj(['68CL','Obs','Line'])
       self.plotObjLeg(['Obs'],combinations[iComb]['legend']) 
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
       self.plotObjLeg(['Exp','Obs'],combinations[iComb]['legend']) 
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

       LCol = [ kBlack , kBlack , kBlack , kBlue , kBlue , kBlue , kRed , kRed ]
       LTyp = [    1   ,    2   ,   3    ,   1   ,   2   ,   3   ,   2  ,   3  ]      

       iLC=0 
       for iComb in CombList:
          self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp')
          aMass         = self.Results[iComb][iEnergy][iModel]['ACLsExp']['mass']
          aMedExpLimit  = self.Results[iComb][iEnergy][iModel]['ACLsExp']['Val']
          self.plotHorizCurve(iComb, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC]  , 2  , combinations[iComb]['legend'] )
          iLC+=1
      
       aMass = [110,600] 
       self.plotHorizLine('Line', aMass , 1. , kRed , 1    , 'CL=1')
  
       #self.c1.SetLogy()
       #self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.05,200.)

       self.SetRange('LimitExp',CombList[0])
       toPlot = dc(CombList)
       toPlot.append('Line')
       self.plotAllObj(toPlot)
       self.plotObjLeg(CombList)
       if (self.logX) : self.plotLogXAxis(aMass[0],aMass[-1],'LimitExp',CombList[0])


       self.addTitle() 
       self.c1.Update() 
       self.Save('ExpLimits_'+self.EnergyName(iEnergy)+'_'+iModel)
  

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
          self.plotHorizCurve(iComb, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC] , 2 , combinations[iComb]['legend'] )
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

   def plotMuChannel(self,CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape'],iEnergy=0,iModel='SMHiggs',massFilter=[125]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetLeftMargin(0.4) 
       self.c1.SetGridx(1)

       BestFit='BestFit'

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
         label = '#splitline{   '+combinations[CombList[iChann]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
         frame.GetYaxis().SetBinLabel(iChann, label  );
         #frame.GetYaxis().SetBinLabel(iChann,  combinations[CombList[iChann]]['legend'] );
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
       label = '#splitline{   '+combinations[CombList[0]]['legend']+'}{                    #scale[0.8]{'+muTxt+'}  }'
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
 
       self.addTitle() 
       self.c1.Update() 
       self.Save('MuCC_'+self.EnergyName(iEnergy)+'_'+iModel+'_'+str(massFilter[0]).replace('.','d'))
       self.Wait()

   def MDF2DSum(self,iComb,iEnergy,iModel,massFilter,bFast=False):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       Fast=''
       if bFast  : Fast='Fast'
       TargetList= ['MDFGrid'+Fast+'Exp'+self.postFix]
       if (not self.blind ) : TargetList.append('MDFGrid'+Fast+'Obs'+self.postFix)     

       for iTarget in TargetList:
         for iMass in massList:
           fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
           fileName += '_'+iModel+'_'+iTarget+'_Points*.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
           fileCmd = 'ls '+fileName 
           proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
           out, err = proc.communicate()
           FileList=string.split(out)
           #print FileList
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

   def MDF2D(self,iComb,iEnergy,iModel,massFilter,bFast=False):
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
       #self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFSnglExp68',algo='Single')
       #self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFCrossExp68',algo='Cross')
       self.readMDFGrid(iComb,iEnergy,iModel,massFilter,iTarget='MDFGrid'+Fast+'Exp'+self.postFix)
       objNameExp=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+'MDFGrid'+Fast+'Exp'+self.postFix
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetXaxis().SetRangeUser(minXP,maxXP)
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetYaxis().SetRangeUser(minYP,maxYP)
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
       self.Obj2Plot['h2d__'+objNameExp]['Obj'].Draw("colz")  
       self.Obj2Plot['c68__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['c95__'+objNameExp]['Obj'].Draw("same")  
       self.Obj2Plot['gr0__'+objNameExp]['Obj'].Draw("samep")  
       #objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFSnglExp68_Single'
       #self.Obj2Plot['c1d__'+objName]['Obj'].Draw("lp")
       #objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFCrossExp68_Cross'
       #self.Obj2Plot['c2d__'+objName]['Obj'].Draw("p")
       self.addTitle() 
       self.c1.Update() 
       self.Save(objNameExp)
       #self.Wait()

       # Observed 
       if (not self.blind ) : 
         #self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFSnglObs68',algo='Single')
         #self.readMDFVal(iComb,iEnergy,iModel,massFilter,iTarget='MDFCrossObs68',algo='Cross')
         self.readMDFGrid(iComb,iEnergy,iModel,massFilter,iTarget='MDFGrid'+Fast+'Obs'+self.postFix) 
         objNameObs=iComb+'_'+str(iEnergy)+'_'+iModel+'_'+'MDFGrid'+Fast+'Obs'+self.postFix
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetTitle(self.xAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetTitle(self.yAxisTitle) 
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetTitle("-2 #Delta ln L")
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetXaxis().SetRangeUser(minXP,maxXP)
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetYaxis().SetRangeUser(minYP,maxYP)
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].GetZaxis().SetRangeUser(0.00001,10.)
         self.Obj2Plot['h2d__'+objNameObs]['Obj'].Draw("colz")  
         self.Obj2Plot['c68__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['c95__'+objNameObs]['Obj'].Draw("same")  
         self.Obj2Plot['gr0__'+objNameObs]['Obj'].Draw("samep")  
         #objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFSnglObs68_Single'
         #self.Obj2Plot['c1d__'+objName]['Obj'].Draw("lp")
         #objName=iComb+'_'+str(iEnergy)+'_'+iModel+'_MDFCrossObs68_Cross'
         #self.Obj2Plot['c2d__'+objName]['Obj'].Draw("p")
         self.addTitle() 
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
       LegList = ['c68__'+objNameExp,'c68__'+objNameExp,'c95__'+objNameExp]
    
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
         self.plotObjLeg(LegList,combinations[iComb]['legend'],'TopRight')
       else:
         self.plotObjLeg(LegList,combinations[iComb]['legend'],'TopLeft')
       

       self.addTitle() 
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

   def JCPSum(self,iComb,iEnergy,iModel,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       iTarget='JCP' 
       for iMass in massList:
         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
         for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
           for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :

             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             fileName += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.*.root'
             fileCmd = 'ls '+fileName 
             proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
             out, err = proc.communicate()
             FileList=string.split(out)
             #print FileList
             os.system('cd /tmp/xjanssen/ ; rm JCPToys.tmp.root')
             isFileFirst=True
             for iFile in FileList:
               isFileOk=True
               try:
                 if isFileFirst : os.system('cd /tmp/xjanssen/ ; hadd JCPToys.tmp.root '+iFile+' > /dev/null')
                 else           : os.system('cd /tmp/xjanssen/ ; hadd JCPToys.tmp.root JCPToys.root '+iFile+' > /dev/null')
               except:  
                 isFileOk=False
               if isFileOk :
                 os.system('cd /tmp/xjanssen/ ; mv JCPToys.tmp.root JCPToys.root') 
                 isFileFirst=False 

             fileTarget  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             fileTarget += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
             print fileTarget
             os.system('cd /tmp/xjanssen/ ; mv JCPToys.root '+fileTarget) 

   def JCPFit(self,iComb,iEnergy,iModel,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       iTarget='JCP' 
       for iMass in massList:
         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
         for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
           for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :

             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             fileName += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.'+targets[iTarget]['method']+'.mH'+str(iMass)+'.root'
             fileTarget  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             fileTarget += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.qmu.FloatMu.mH'+str(iMass)+'.root'
             print 'Fitting :',fileName    
             os.system('root -q -b '+fileName+' "${CMSSW_BASE}/src/HiggsAnalysis/CombinedLimit/test/plotting/hypoTestResultTree.cxx(\\"'+fileTarget+'\\",'+str(iMass)+',1,\\"x\\")"')



   def JCPPlt(self,iComb,iEnergy,iModel,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+self.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+self.Version+'/'+cardDir+'/'+iComb

       iTarget='JCP' 

       jcp='undef'
       if '2pm' in iComb : jcp='2pm'
       if '0m'  in iComb : 
         jcp='0m'
         targets[iTarget]['JobsParam']['FQQ'] = [0.]

       for iMass in massList:
         # 'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } }
         for iFITNUIS in targets[iTarget]['JobsParam']['FITNUIS'] :

           tableName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
           tableName += '_'+iModel+'_'+iTarget+'_FITNUIS'+str(iFITNUIS)+'.ResultsSummary.mH'+str(iMass)+'.txt' 
           subfile = open(tableName,'w')
           subfile.write('#Fqq     sObsSM   sExpSM  sObsALT  sExpALT CLsRatio     qObs   MeanSM medianSM   qSM68m   qSM68p   qSM95m   qSM95p  MeanALTmedianALT  qALT68m  qALT68p  qALT95m  qALT95p \n')

           for iFQQ in targets[iTarget]['JobsParam']['FQQ'] :
             unblind=1
             workDir   = TargetDir+'/'+str(iMass) 
             print workDir
             fileName  = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             fileName += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.qmu.FloatMu.mH'+str(iMass)+'.root'
             logName   = TargetDir+'/'+str(iMass)+'/higgsCombine_'+iComb
             logName  += '_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)+'.Results.mH'+str(iMass)+'.txt'
             os.system('cd '+workDir+'; root -q -b /afs/cern.ch/user/x/xjanssen/cms/HWW2012/ToolBox/SignalSeparation/extractSignificanceStats.C+"(\\"'+fileName+'\\",2,'+str(unblind)+')" > '+logName)
             baseName  = 'sigsep_'+iModel+'_'+iTarget+'_FQQ'+str(iFQQ).replace('.','d')+'_FITNUIS'+str(iFITNUIS)
             baseName  = baseName.replace('.','_')
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.eps  '+workDir+'/'+baseName+'.epf') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.png  '+workDir+'/'+baseName+'.png') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.pdf  '+workDir+'/'+baseName+'.pdf') 
             os.system('cd '+workDir+';mv '+workDir+'/sigsep_combine.root '+workDir+'/'+baseName+'.root') 
             if jcp == '0m':
               if iFQQ == 0.   : mText = '0^{-}'
               #if iFQQ == 0.25 : mText = '0^{-}(f_{q#bar{q}}=25%)'
               #if iFQQ == 0.50 : mText = '0^{-}(f_{q#bar{q}}=50%)'
               #if iFQQ == 0.75 : mText = '0^{-}(f_{q#bar{q}}=75%)'
               #if iFQQ == 1.   : mText = '0^{-}(f_{q#bar{q}}=100%)'
             if jcp == '2pm':
               if iFQQ == 0.   : mText = '2^{+}_{min}(f_{q#bar{q}}=0%)'
               if iFQQ == 0.25 : mText = '2^{+}_{min}(f_{q#bar{q}}=25%)'
               if iFQQ == 0.50 : mText = '2^{+}_{min}(f_{q#bar{q}}=50%)'
               if iFQQ == 0.75 : mText = '2^{+}_{min}(f_{q#bar{q}}=75%)'
               if iFQQ == 1.   : mText = '2^{+}_{min}(f_{q#bar{q}}=100%)'

             if iFITNUIS == -1 :
               os.system('cd '+workDir+'; root -q -b /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/plotting/extractSignificanceStats.C+"(false,\\"'+mText+'\\",\\"'+jcp+'\\",\\"'+fileName+'\\")" ')
             else :
               os.system('cd '+workDir+'; root -q -b /afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/summer2013/scripts/plotting/extractSignificanceStats.C+"(true,\\"'+mText+'\\",\\"'+jcp+'\\",\\"'+fileName+'\\")" > /dev/null')
             for line in open(logName):
               if "RESULTS_SUMMARY" in line:
                 print "%-4s %s"%(str(iFQQ),line.replace('RESULTS_SUMMARY',''))
                 subfile.write("%-4s %s"%(str(iFQQ),line.replace('RESULTS_SUMMARY','')))

           subfile.close()
           print  tableName,unblind,'25.'
           if jcp != '0m' :  
            if iFITNUIS == 0 :
             self.plotFqqLim(tableName,0,'25.',massFilter[0],jcp) 
            else:
             self.plotFqqLim(tableName,unblind,'25.',massFilter[0],jcp) 

   def plotFqqLim(self,limFile,unblind,lumi,mass,jcp):
  
     mText = 'Undef'
     if jcp == '0m'  : mText = '0^{-}'
     if jcp == '2pm' : mText = '2^{+}_{min}'
 
     print "limFile = "+limFile
     self.squareCanvas(False,False)  
     self.c1.cd()
     self.c1.SetLeftMargin(0.15) 

     pt = TPaveText(0.1,0.91,0.45,0.99,"NDC");
     pt.SetTextAlign(12);
     pt.SetTextSize(0.04);
     pt.SetFillColor(0);
     pt.AddText("CMS Preliminary");
     pt.SetBorderSize(0);
     pt2 = TPaveText(0.55,0.91,0.9,0.99,"NDC");
     pt2.SetTextAlign(32);
     pt2.SetTextSize(0.035);
     pt2.SetFillColor(0);
     #pt2.AddText(" #sqrt{s} = 7 TeV, L = 5.051 fb^{-1}; #sqrt{s} = 8 TeV, L = 30.0 fb^{-1}");
     if float(lumi)<10.:
       pt2.AddText(" #sqrt{s} = 7 TeV, L = 4.9 fb^{-1}");
     elif float(lumi)<20.:
       pt2.AddText(" #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}");
     else:
       pt2.AddText(" #sqrt{s} = 7 TeV, L = 4.9 fb^{-1}; #sqrt{s} = 8 TeV, L = 19.5 fb^{-1}"); 
     pt2.SetBorderSize(0);
   
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
         grSM.SetPoint(p,float(vec[0])*100.,float(vec[iSM]))
         grSM68.SetPoint(p,float(vec[0])*100.,float(vec[iSM]))
         grSM95.SetPoint(p,float(vec[0])*100.,float(vec[iSM]))
         grSM68.SetPointError(p,0.,0.,abs(float(vec[iSM])-float(vec[9])),abs(float(vec[iSM])-float(vec[10])))
         grSM95.SetPointError(p,0.,0.,abs(float(vec[iSM])-float(vec[11])),abs(float(vec[iSM])-float(vec[12])))
         grGRAV.SetPoint(p,float(vec[0])*100.,float(vec[iGR]))
         grGR68.SetPoint(p,float(vec[0])*100.,float(vec[iGR]))
         grGR95.SetPoint(p,float(vec[0])*100.,float(vec[iGR]))
         grGR68.SetPointError(p,0.,0.,abs(float(vec[iGR])-float(vec[15])),abs(float(vec[iGR])-float(vec[16])))
         grGR95.SetPointError(p,0.,0.,abs(float(vec[iGR])-float(vec[17])),abs(float(vec[iGR])-float(vec[18])))
         grData.SetPoint(p,float(vec[0])*100.,float(vec[6]))
         p+=1
   
     grData.SetMarkerStyle(kFullCircle)
     grData.SetLineWidth(2)
     
     grSM.SetMarkerStyle(kFullSquare)
     grSM.SetMarkerColor(kRed)
     #grSM.SetLineStyle(kDashed)
     grSM.SetLineWidth(2)
     grSM.SetLineColor(kRed)
   
     grSM95.SetLineColor(kYellow)
     grSM95.SetFillColor(kYellow)
     grSM68.SetLineColor(kGreen)
     grSM68.SetFillColor(kGreen)
   
     grGRAV.SetMarkerStyle(kFullTriangleUp)
     grGRAV.SetMarkerColor(kBlue)
     #grGRAV.SetLineStyle(kDashed)
     grGRAV.SetLineWidth(2)
     grGRAV.SetLineColor(kBlue)
   
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
     grGR95.SetFillStyle(3356)
   
     ymin=-10.
     ymax=40.
    
     dummyHist = TH1F("d",";f_{q#bar{q}} (%);-2 ln (L_{"+mText+"}/L_{0^{+}}) ",100,0,100)
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
   
     leg = TLegend(0.20,0.65,0.40,0.89);
     leg.SetHeader("WW #rightarrow 2l2#nu + 0/1-jet")
     leg.SetLineColor(0);
     leg.SetFillColor(0);
     leg.SetTextSize(0.033)
     leg.SetFillStyle(0)
     leg.SetBorderSize(0)
     leg.SetTextFont (42)


      
     #leg.AddEntry(grSM,"X#rightarrow#gamma#gamma 0^{+}","lp");
     #leg.AddEntry(grSM,"Y #rightarrow WW where Y=0^{+}","lp");
     leg.AddEntry(grSM,"0^{+}","lp");
     leg.AddEntry(grSM68,"#pm 1#sigma expected","f");
     leg.AddEntry(grSM95,"#pm 2#sigma expected","f");
     #leg.AddEntry(grGRAV,"X#rightarrow#gamma#gamma 2^{+}_{m}","lp");
     #leg.AddEntry(grGRAV,"Y #rightarrow WW where Y=2^{+}_{min}","lp");
     leg.AddEntry(grGRAV,mText,"lp");
     leg.AddEntry(grGR68,"#pm 1#sigma expected","f");
     leg.AddEntry(grGR95,"#pm 2#sigma expected","f");

     if unblind: leg.AddEntry(grData,"Observed","lp")

     TlMH=TLatex()
     TlMH.SetTextSize(0.03);
     TlMH.SetNDC()
     TlMH.DrawLatex(0.72,0.87,'m_{H} = '+str(mass)+' GeV')

   
     grSM95.Draw("E3same")
     grSM68.Draw("E3same")
     grGRAV.Draw("LPsame")
     grSM.Draw("LPsame")
     grGR95.Draw("E3same")
     grGR68.Draw("E3same")
     if unblind: grData.Draw("LPsame")
     leg.Draw("SAME")
     f = TF1('f','0.',0.,100.)
     f.SetLineColor(kBlack)
     f.SetLineWidth(2)
     f.SetLineStyle(kDashed)
     f.Draw("same")
     #pt.Draw("same")
     #pt2.Draw("same")
     self.addTitle()
     dummyHist.Draw("AXISGsame")
     self.c1.Update()
     #if not options.isBatch: raw_input("Looks ok?")
     self.c1.Update()
     self.c1.Print(limFile.replace('txt','png'))
     self.c1.Print(limFile.replace('txt','pdf'))
   
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


   def MUMHSum(self,iComb,iEnergy,iModel,massFilter):
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
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
      
      self.Results = {}

      if 'ACLsExp' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsExp') 
      if 'SExpPre' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'SExpPre') 

      if (not self.blind ) :
        if 'ACLsObs' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'ACLsObs') 
        if 'SObs'    in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'SObs') 
        if 'BestFit' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFit')
        if 'BestFitG' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFitG')
        if 'BestFitT' in printList : self.readResults(iComb,iEnergy,iModel,massFilter,'BestFitT')

      # build Mass List
      allList = []
      for iTarget in self.Results[iComb][iEnergy][iModel]: allList.extend(self.Results[iComb][iEnergy][iModel][iTarget]['mass'])
      AllMass = sorted(list(set(allList)))
     
      # Files
      txtFile=''
 
      # Header
      txtPrint='| mH  '
      texPrint=''
      if 'ACLsObs' in printList : 
         txtPrint+='| CLsObs '
      if 'ACLsExp' in printList : 
         txtPrint+='| CLsExp | 95Do | 68Do | 68Up | 95Up '
      if 'SObs'    in printList : 
         txtPrint+='| SObs '
      if 'SExpPre' in printList : 
         txtPrint+='| SExp '
      if 'BestFit' in printList : 
         txtPrint+='| BestFit '
      if 'BestFitG' in printList : 
         txtPrint+='| BestFitG '
      if 'BestFitT' in printList : 
         txtPrint+='| BestFitT '


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
        if 'ACLsExp' in printList :
            Val=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','Val')
            d95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','95D')
            d68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','68D')
            u68=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','68U')
            u95=self.findResValbyM(iComb,iEnergy,iModel,iMass,'ACLsExp','95U')
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

  
        print txtPrint 

      #print self.Results

      

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
