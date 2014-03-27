#!/usr/bin/env python

physmodels = {
#
# Workspace Convention Validation
#
  'SMValid'  : { 'model'    : 'HiggsAnalysis.CombinedLimit.PhysicsModel:strictSMLikeHiggs' , 
                 'cardtype' : 'smhiggs' 
               } ,
#
# Basic 
#
  'NoModel'  : { 'cardtype' : 'couplings' } ,
  '125dot6'  : { 'cardtype' : 'couplings' } ,
  '125dot7'  : { 'cardtype' : 'couplings' } ,
  'SMHiggs'  : { 'cardtype' : 'smhiggs'   } ,
  'MH125BG'  : { 'cardtype' : 'searches'  } ,
  'HiMass'   : { 'cardtype' : 'himass'    } ,
#
# TwoHiggsModels
#
  'OneHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:justOneHiggs'            ,
                 'cardtype' : 'searches' 
               } ,
  'TwoHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:twoHiggsUnconstrained'   , 
                 'cardtype' : 'searches' 
               } ,
#
# Custom injection&toys cards
#
  'SMInject' : { 'cardtype' : 'sminject' } ,
  'SMToys'   : { 'cardtype' : 'smtoys' } ,
#
# Couplings
#
# ... (muVBF+VH,mu_ggH+ttH)
#
  'rVrFXSH'  : { 'model' : 'HiggsAnalysis.CombinedLimit.PhysicsModel:rVrFXSHiggs' , 
                 'cardtype' : 'couplings' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['RV','RF'] , 'AxisTitle' : ['#mu_{VBF,VH}','#mu_{ggH}'] , 
                               'Min' : [-2.,-2.] , 'Max' : [4.,4.] ,  'MinPlt' : [0.,0.] , 'MaxPlt' : [2.5,2.5]  } 
               } ,
#
# ... (kV,kF)
#
  'cVcF'     : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsCouplings:cVcF'      , 
                 'cardtype' : 'couplings' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['CV','CF'] , 'AxisTitle' : ['#kappa_{V}','#kappa_{f}'] , 
                               'Min' : [0.,-2.] , 'Max' : [2.,2.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.5,2.]  }  
               } ,
#
# ... 3 mu (ggH+ttH,VBF,VH)
#
  'Fit3Mu'   : { 'model' : "HiggsAnalysis.CombinedLimit.PhysicsModel:floatingXSHiggs --PO verbose --PO 'modes=ggH,qqH,VH' --PO 'ttH=ggH'  --PO 'ggHRange=0:2' --PO 'qqHRange=0:5' --PO 'VHRange=0:5'" ,
                 'cardtype' : 'couplings',
                 'MDFTree' : { 'TargetBase' : 'Fit3Mu' , 'POISetKeys'  : [ 'ggH','qqH','VH' ] ,
                               #'ParNames' : [ '#mu_{ggH}' , '#mu_{VBF}' , '#mu_{VH}' ] ,
                               'ggH'   : { 'NDim' : 1 , 'Keys' : ['r_ggH'] , 'Ext' : '_ggH' , 'AxisTitle' : ['#mu_{ggH}'] , 'Min' : [0.] , 'Max' : [2.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [2.,8.]  } ,
                               'qqH'   : { 'NDim' : 1 , 'Keys' : ['r_qqH'] , 'Ext' : '_qqH' , 'AxisTitle' : ['#mu_{VBF}'] , 'Min' : [0.] , 'Max' : [5.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [4.,8.]  } ,
                               'VH'    : { 'NDim' : 1 , 'Keys' : ['r_VH']  , 'Ext' : '_VH'  , 'AxisTitle' : ['#mu_{VH}']  , 'Min' : [0.] , 'Max' : [5.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [6.,8.]  } ,
                             }
               },
#
# ... 2 mu (ggH+ttH,VBF+VH)
#
  'Fit2Mu'   : { 'model' : "HiggsAnalysis.CombinedLimit.PhysicsModel:floatingXSHiggs --PO verbose --PO 'modes=ggH,qqH' --PO 'ttH=ggH'  --PO 'ggHRange=0:2' --PO 'qqHRange=0:5'" ,
                 'cardtype' : 'couplings',
                 'MDFTree' : { 'TargetBase' : 'Fit2Mu' , 'POISetKeys'  : [ 'ggH','qqH', ] ,
                               #'ParNames' : [ '#mu_{ggH}' , '#mu_{VBF}' , '#mu_{VH}' ] ,
                               'ggH'   : { 'NDim' : 1 , 'Keys' : ['r_ggH'] , 'Ext' : '_ggH' , 'AxisTitle' : ['#mu_{ggH}'] , 'Min' : [0.] , 'Max' : [2.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [2.,8.]  } ,
                               'qqH'   : { 'NDim' : 1 , 'Keys' : ['r_qqH'] , 'Ext' : '_qqH' , 'AxisTitle' : ['#mu_{VBF}'] , 'Min' : [0.] , 'Max' : [5.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [4.,8.]  } ,
                             }
               },

#
# ... BR(Invisible) + Profiling all others
#
  'BRInv'  :   { 'model' : "HiggsAnalysis.CombinedLimit.HiggsCouplings:c7 --PO verbose" , 
                 'cardtype' : 'couplings' ,
                 'MDFTree' : { 'TargetBase' : 'BRInv' , 'POISetKeys'  : ['BRInv'] ,
                               'BRInv' :  { 'NDim' : 1 , 'Keys' : ['BRInvUndet'] , 'AxisTitle' : ['BR_{BSM}'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,8.]  } ,
                             }
               },
#
# Mass/mu scan from Histo cards  ---> This does not really work nicely !!! 
#
  'mHmuHist' : { 'cardtype' : 'mass' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['mh','r'] , 'AxisTitle' : ['Higgs Mass [GeV]','#mu'] , 'Min' : [110.,0.] , 'Max' : [140,3.] , 'MinPlt' : [110.,0.] , 'MaxPlt' : [140.,3.]  }  } ,
  'mHmuHistSMInj' : { 'cardtype' : 'masssminj' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['mh','r'] , 'AxisTitle' : ['Higgs Mass [GeV]','#mu'] , 'Min' : [110.,0.] , 'Max' : [140,3.] , 'MinPlt' : [110.,0.] , 'MaxPlt' : [140.,3.]  }  } ,
#
# Spin
#
  'JCP'      : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs  --PO=fqqFloating' , 'cardtype' : 'jcp' } 

}
