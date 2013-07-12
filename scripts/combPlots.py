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

#gROOT.SetBatch()
#gROOT.ProcessLine(".x tdrstyle.cc")
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)

CMSText=["CMS Preliminary","CMS"] 
LumText=["#sqrt{s} = 7 TeV, L #leq 4.9 fb^{-1} ; #sqrt{s} = 8 TeV, L #leq 19.5 fb^{-1}","#sqrt{s} = 7 TeV, L #leq 4.9 fb^{-1}","#sqrt{s} = 8 TeV, L #leq 19.5 fb^{-1}"]

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
   
   def addTitle(self,iCMS=0,iLumi=0):
       self.c1.cd()
   
       x1=0.13
       y1=0.93
       x2=0.99
       y2=0.98
       fontSize = 0.04 
       if self.isSquareCanvas : fontSize = 0.025
   
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

   def treeAccess(self,tree):
        tree.SetBranchStatus('*',0)

        _lm = numpy.array(1,'d')
        _mh = numpy.array(1,'d')

        tree.SetBranchStatus('limit',1)
        tree.SetBranchStatus('mh'   ,1)
        tree.SetBranchAddress('limit',_lm)
        tree.SetBranchAddress('mh',   _mh)

        return _lm, _mh

   def readResults(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],iTarget='BestFit'):

       # Get info from comfig
       cardDir   = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
       energyList= combTools.EnergyList_Filter(iEnergy).get()
       massList  = combTools.MassList_Filter(cardtypes,channels[self.Version],combinations,physmodels[iModel]['cardtype'],massFilter,iComb,energyList).get()
       if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]:
         TargetDir=workspace+'/'+Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
       else:
         TargetDir=workspace+'/'+Version+'/'+cardDir+'/'+iComb
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
       
   def plotAllObj(self,Order=[]):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot]  
       for X in Order: 
         if X in self.Obj2Plot:    
           if   self.Obj2Plot[X]['Type'] == 'Band':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].GetXaxis().SetTitle(self.xAxisTitle)
               self.Obj2Plot[X]['Obj'].GetYaxis().SetTitle(self.yAxisTitle)
               self.Obj2Plot[X]['Obj'].Draw("A3")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("3")   
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             if iFirst: 
               iFirst=False
               self.Obj2Plot[X]['Obj'].GetXaxis().SetTitle(self.xAxisTitle)
               self.Obj2Plot[X]['Obj'].GetYaxis().SetTitle(self.yAxisTitle)
               self.Obj2Plot[X]['Obj'].Draw("AL")
             else: 
               self.Obj2Plot[X]['Obj'].Draw("L") 
       self.c1.Update() 

   def plotObjLeg(self,Order=[],Title=''):
       if len( self.Obj2Plot ) == 0 : return
       self.c1.cd()
       iFirst=True
       if len( Order ) == 0 : Order = [X for X in self.Obj2Plot] 
       self.Legend = TLegend(0.50,0.65,0.85,0.85)   
       self.Legend.SetTextSize(0.035)
       self.Legend.SetFillColor(0)
       self.Legend.SetFillStyle(0)
       self.Legend.SetBorderSize(0)
       for X in Order: 
         if X in self.Obj2Plot:    
           if   self.Obj2Plot[X]['Type'] == 'Band':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'f')
           elif self.Obj2Plot[X]['Type'] == 'Curve':
             self.Legend.AddEntry(self.Obj2Plot[X]['Obj'],self.Obj2Plot[X]['Legend'],'l')
       self.Legend.SetHeader(Title)
       self.Legend.Draw('same')

   def EnergyName(self,iEnergy):
       if   iEnergy == 0 : return '7and8TeV'
       elif iEnergy == 7 : return '7TeV'
       elif iEnergy == 8 : return '8TeV'
       else              : return 'UndefE'

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
 
       self.xAxisTitle = "Higgs mass [GeV/c^{2}]"
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

       self.plotHorizBand('95CL', aMass , aMedExpLimit , aExpLimit95U , aExpLimit95D ,  90 , 1001 , 'CL_{S} Expected #pm 2#sigma')
       self.plotHorizBand('68CL', aMass , aMedExpLimit , aExpLimit68U , aExpLimit68D , 211 , 1001 , 'CL_{S} Expected #pm 1#sigma')
       self.plotHorizCurve('Exp', aMass , aMedExpLimit , kBlack , 2          ,  2          ,     'CL_{S} Expected')

       if (not self.blind ) : self.plotHorizCurve('Obs', aMass , aObsLimit , kBlack , 1  , 3 , 'CL_{S} Observed')

       if  bInject :  
         self.plotHorizBand('95CLInj', aMass , aMedInjLimit , aInjLimit95U , aInjLimit95D , kBlue , 3356 , 'CL_{S} Injected #pm 2#sigma')
         self.plotHorizBand('68CLInj', aMass , aMedInjLimit , aInjLimit68U , aInjLimit68D , kRed  , 3356 , 'CL_{S} Injected #pm 1#sigma')
         self.plotHorizCurve('Inj'   , aMass , aMedInjLimit , kRed  , 1            , 2            , 'm_{H}=125 GeV #pm 1(2)#sigma_{stat}')
         #self.plotHorizCurve('InjFast', aMass , aMedInjLimit , kRed , 1                        , 'CL_{S} Injected')
         #self.plotHorizCurve('Inj68D'   , aMass , aInjLimit68D , kBlue , 2                        , 'CL_{S} Injected')
         #self.plotHorizCurve('Inj95D'   , aMass , aInjLimit95D , kBlue , 3                        , 'CL_{S} Injected')
         #self.plotHorizCurve('Inj68U'   , aMass , aInjLimit68U , kBlue , 2                        , 'CL_{S} Injected')
         #self.plotHorizCurve('Inj95U'   , aMass , aInjLimit95U , kBlue , 3                        , 'CL_{S} Injected')

       lMass=[]
       lMass.append(100.)
       lMass.append(aMass[-1]+1)
       self.plotHorizLine('Line', lMass , 1. , kBlack , 1    , 'CL=1')



       self.plotAllObj(['95CL','68CL','Exp','95CLInj','68CLInj','Inj','Inj68D','Inj95D','Inj68U','Inj95U','Obs','Line'])
       self.plotObjLeg(['Obs','Exp','68CL','95CL','Inj'],combinations[iComb]['legend'])

       self.addTitle() 
       self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
       self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
       self.c1.Update() 
       self.Save('limit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)
       #self.Obj2Plot['95CL']['Obj'].GetXaxis().SetRangeUser(110.,200.)
       self.Obj2Plot['95CL']['Obj'].GetYaxis().SetRangeUser(0.,20.)
       #self.Save('limit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel+'_zoom')
       
   def plotMuVsMh(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[]):

       self.readResults(iComb,iEnergy,iModel,massFilter,'BestFit')

       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs mass [GeV/c^{2}]"
       self.yAxisTitle = "best fit for #mu"

       aMass    = self.Results[iComb][iEnergy][iModel]['BestFit']['mass']
       muVal    = self.Results[iComb][iEnergy][iModel]['BestFit']['Val']
       mu68U    = self.Results[iComb][iEnergy][iModel]['BestFit']['68U']
       mu68D    = self.Results[iComb][iEnergy][iModel]['BestFit']['68D']

       if (self.blind) : return

       self.plotHorizBand('68CL', aMass , muVal , mu68U , mu68D , 211 , 1001 , '#mu #pm 1#sigma' )
       self.plotHorizCurve('Obs', aMass , muVal , kBlack ,2    , 3           , '#mu #pm 1#sigma' )

       lMass=[]
       lMass.append(100.)
       lMass.append(aMass[-1]+1)  
       self.plotHorizLine('Line', lMass , 1. , kBlack , 1    , '#mu=1')
       
       self.plotAllObj(['68CL','Obs','Line'])
       self.plotObjLeg(['Obs'],combinations[iComb]['legend']) 

       self.addTitle() 
       self.c1.Update() 
       self.Save('MuVsMh_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotSignVsMh(self,iComb='hww01jet_shape',iEnergy=0,iModel='OneHiggs',massFilter=[],fitType='Pre',bInject=False):

       plot.readResults(iComb,iEnergy,iModel,massFilter,'SExp'+fitType)
       if (not self.blind ) : plot.readResults(iComb,iEnergy,iModel,massFilter,'SObs')
 
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs mass [GeV/c^{2}]"
       self.yAxisTitle = "significance"

       aMass    = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['mass']
       SExp     = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['Val']
       if (not self.blind) : SObs     = self.Results[iComb][iEnergy][iModel]['SObs']['Val']
       #self.plotHorizLine('3Sig', aMass , 3. , kBlack , 3    , 'S=3')
       #self.plotHorizLine('5Sig', aMass , 5. , kRed   , 3    , 'S=5')

       self.plotHorizCurve('Exp', aMass , SExp , kBlack ,2    , 2    , 'Expected' ) 
       if (not self.blind) :  self.plotHorizCurve('Obs', aMass , SObs , kBlack ,1   , 3     , 'Observed' ) 

       self.plotAllObj(['Exp','Obs'])
       self.plotObjLeg(['Exp','Obs'],combinations[iComb]['legend']) 

       self.addTitle() 
       self.c1.Update() 
       self.Save('SignVsMh_'+fitType+'Fit_'+iComb+'_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotExpLimits(self,CombList=['hww01jet_shape'],iEnergy=0,iModel='OneHiggs',massFilter=[]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs mass [GeV/c^{2}]"
       self.yAxisTitle = "95% CL expected limit on #sigma/#sigma_{SM}"

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
  
       self.c1.SetLogy()
       self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.05,200.)


       toPlot = dc(CombList)
       toPlot.append('Line')
       self.plotAllObj(toPlot)
       self.plotObjLeg(CombList)

       self.addTitle() 
       self.c1.Update() 
       self.Save('ExpLimits_'+self.EnergyName(iEnergy)+'_'+iModel)
  

   def plotExpSignVsMh(self,CombList=['hww01jet_shape'],iEnergy=0,iModel='OneHiggs',massFilter=[],fitType='Pre'):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()

       self.xAxisTitle = "Higgs mass [GeV/c^{2}]"
       self.yAxisTitle = "Expected significance"

       LCol = [ kBlack , kBlack , kBlack , kBlue , kBlue , kBlue , kRed , kRed ]
       LTyp = [    1   ,    2   ,   3    ,   1   ,   2   ,   3   ,   2  ,   3  ]      

       iLC=0 
       for iComb in CombList:
          self.readResults(iComb,iEnergy,iModel,massFilter,'SExp'+fitType)
          aMass         = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['mass']
          aMedExpLimit  = self.Results[iComb][iEnergy][iModel]['SExp'+fitType]['Val']
          self.plotHorizCurve(iComb, aMass , aMedExpLimit , LCol[iLC] , LTyp[iLC] , 2 , combinations[iComb]['legend'] )
          iLC+=1
      
       #aMass = [110,600] 
       #self.plotHorizLine('Line', aMass , 1. , kRed , 1    , 'CL=1')
  
       #self.c1.SetLogy()
       self.Obj2Plot[CombList[0]]['Obj'].GetYaxis().SetRangeUser(0.0,25.)


       toPlot = dc(CombList)
       #toPlot.append('Line')
       self.plotAllObj(toPlot)
       self.plotObjLeg(CombList)

       self.addTitle() 
       self.c1.Update() 
       self.Save('ExpSign_'+fitType+'Fit_'+self.EnergyName(iEnergy)+'_'+iModel)

   def plotMuChannel(self,CombList=['hww012j_vh3l_vh2j_zh3l2j_shape','hww01jet_shape','hww2j_shape','hwwvh2j_cut','vh3l_shape','zh3l2j_shape'],iEnergy=0,iModel='SMHiggs',massFilter=[125]):
       self.squareCanvas(False,False)
       self.c1.cd()
       self.resetPlot()
       self.c1.SetLeftMargin(0.4) 
       self.c1.SetGridx(1)

       if len(massFilter) != 1 : return
       nChann=len(CombList)-1
       if nChann == 0 : return

       for iComb in CombList:
         self.readResults(iComb,iEnergy,iModel,massFilter,'BestFit')

       frame = TH2F("frame",";best fit #sigma/#sigma_{SM};",1,-1,5,nChann,0,nChann);
       frame.GetXaxis().SetTitleSize(0.05);
       frame.GetXaxis().SetLabelSize(0.04);
       frame.GetYaxis().SetLabelSize(0.06);
       #frame.GetXaxis().SetNdivisions(505)
       frame.Draw()

       globalFitBand = TBox(self.Results[CombList[0]][iEnergy][iModel]['BestFit']['68D'][0], 0, self.Results[CombList[0]][iEnergy][iModel]['BestFit']['68U'][0] , nChann);
       globalFitBand.SetFillStyle(3013);
       globalFitBand.SetFillColor(65);
       globalFitBand.SetLineStyle(0);
       globalFitBand.Draw("same");

       Val = self.Results[CombList[0]][iEnergy][iModel]['BestFit']['Val'][0]
       globalFitLine = TLine (Val, 0, Val, nChann);
       globalFitLine.SetLineWidth(4);
       globalFitLine.SetLineColor(214);
       globalFitLine.Draw("same");

       points = TGraphAsymmErrors (nChann)
       TlMu=TLatex()
       TlMu.SetTextAlign(23);
       TlMu.SetTextSize(0.03);
       for iChann in xrange(1,nChann+1):
         Val = self.Results[CombList[iChann]][iEnergy][iModel]['BestFit']['Val'][0]
         eDo = self.Results[CombList[iChann]][iEnergy][iModel]['BestFit']['Val'][0] - self.Results[CombList[iChann]][iEnergy][iModel]['BestFit']['68D'][0]
         eUp = self.Results[CombList[iChann]][iEnergy][iModel]['BestFit']['68U'][0] - self.Results[CombList[iChann]][iEnergy][iModel]['BestFit']['Val'][0]
         if eUp > 100 : eUp=100
         print Val, eDo, eUp
         points.SetPoint(iChann-1,      Val , iChann-0.5);
         points.SetPointError(iChann-1, eDo, eUp , 0, 0);
         frame.GetYaxis().SetBinLabel(iChann,  combinations[CombList[iChann]]['legend'] );
         #frame.GetYaxis().SetBinLabel(iChann-.5,'#mu = 0.76^{+0.19}_{-0.19}')
         #TlMu.DrawLatex(0.2,0.95,'#mu = 0.76^{+0.19}_{-0.19}')

       points.SetLineColor(kRed);
       points.SetLineWidth(3);
       points.SetMarkerStyle(21);
       points.Draw("PSAME");
    
       self.addTitle() 
       self.c1.Update() 
       self.Wait()

   def printResults(self):
      print self.Results

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
