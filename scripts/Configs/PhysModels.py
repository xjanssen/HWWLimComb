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
  'HiMassAll': { 'cardtype' : 'himassall' } ,
  'EWKS'     : { 'cardtype' : 'ewks'      } ,  
  'EWKSAll'  : { 'cardtype' : 'ewksall'   } ,  
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
  'rVrF'     : { 'model' : 'HiggsAnalysis.CombinedLimit.PhysicsModel:rVrFXSHiggs' , 'cardtype' : 'smhiggs' } ,
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
#  'JCP'      : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs ' , 'cardtype' : 'jcp' } ,
  'JCP'      : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=muFloating'  , 'cardtype' : 'jcp' ,
                'MDFTree' : { 'TargetBase' : 'fJP' , 'POISetKeys'  : [ 'x' ] ,
                              'x' : { 'NDim' : 1 , 'Keys' : ['x'] , 'AxisTitle' : ['f(J^{P})'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,12.]  } ,
                            }
#                  'MDFTree' : { 'TargetBase' : 'JPMU' , 'POISetKeys'  : [ 'MU_SM' , 'MU_ALT'  ] ,
#                                'MU_SM' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_SM' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
#                                'MU_ALT' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_ALT' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
#                             }
               } ,

  'JCPFQQ'   : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating' , 'cardtype' : 'jcp' ,
                  'MDFTree' : { 'TargetBase' : 'fJP' , 'POISetKeys'  : [ 'x_fqq0' , 'x_fqq1' ] , 
                                'x_fqq0' : { 'NDim' : 1 , 'Keys' : ['x'] , 'Ext' : '_fqq0' , 'AxisTitle' : ['f(J^{P})'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,12.]  } ,
                                'x_fqq1' : { 'NDim' : 1 , 'Keys' : ['x'] , 'Ext' : '_fqq1' , 'AxisTitle' : ['f(J^{P})'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,12.]  } ,
                             }
#                'MDFTree' : { 'TargetBase' : 'JPMU' , 'POISetKeys'  : [ 'MU_SM' , 'MU_fqq0' ,  'MU_fqq1' ] ,
#                              'MU_SM' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_SM' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
#                              'MU_fqq0' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_fqq0' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
#                              'MU_fqq1' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_fqq1' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
#                           }
               } ,

  'JCPFQQMH' : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO higgsMassRange=120,130' , 'cardtype' : 'jcp' ,
#                'MDFTree' : { 'TargetBase' : 'JPMH' , 'POISetKeys'  : [ 'MH_SM' , 'MH_fqq0' ,  'MH_fqq1' ] ,
#                              'MH_SM' : { 'NDim' : 1 , 'Keys' : ['MH'] , 'Ext' : '_SM' , 'AxisTitle' : ['m_{H} [GeV]'] , 'Min' : [120.] , 'Max' : [130.] , 'MinPlt' : [120.,0.] , 'MaxPlt' : [130.,10.]  } ,
#                              'MH_fqq0' : { 'NDim' : 1 , 'Keys' : ['MH'] , 'Ext' : '_fqq0' , 'AxisTitle' : ['m_{X} [GeV]'] , 'Min' : [120.] , 'Max' : [130.] , 'MinPlt' : [120.,0.] , 'MaxPlt' : [130.,10.]  } ,
#                              'MH_fqq1' : { 'NDim' : 1 , 'Keys' : ['MH'] , 'Ext' : '_fqq1' , 'AxisTitle' : ['m_{X} [GeV]'] , 'Min' : [120.] , 'Max' : [130.] , 'MinPlt' : [120.,0.] , 'MaxPlt' : [130.,10.]  } ,
#                            }
                  'MDFTree' : { 'TargetBase' : 'JPMU' , 'POISetKeys'  : [ 'MU_SM' , 'MU_fqq0' ,  'MU_fqq1' ] ,
                                'MU_SM' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_SM' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
                                'MU_fqq0' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_fqq0' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
                                'MU_fqq1' : { 'NDim' : 1 , 'Keys' : ['r'] , 'Ext' : '_fqq1' , 'AxisTitle' : ['#mu'] , 'Min' : [0.] , 'Max' : [4.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [3.,10.]  } ,
                             }

               } , 

  #'JCPFQQ2Mu': { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO verbose --PO \'map=hzz4l.*/([WZV]|gg|qq|tt)H:r_zz[1,0,3]\' --PO \'map=hww.*/([WZV]|gg|qq|tt)H:r_ww[1,0,3]\' ' , 'cardtype' : 'jcp' } ,
  'JCPFQQ2Mu': { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO TwoMu ' , 'cardtype' : 'jcp' } ,
  'JCPFQQDEC': { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO=hzz4lDecCard' , 'cardtype' : 'jcp' } ,
  'JCPFQQ2MuDEC': { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO=hzz4lDecCard --PO TwoMu' , 'cardtype' : 'jcp' } ,
  'JCPFQQ3MuDEC': { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs --PO=fqqFloating --PO=hzz4lDecCard --PO ThreeMu' , 'cardtype' : 'jcp' } ,

#
# HWidth
#

  'HWidth2l2nu' : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsWidth:higgswidth --PO=is2l2nu' , 'cardtype' : 'hwidth' ,
                    'MDFTree': { 'TargetBase' : 'HWidth' , 'POISetKeys'  : ['Width'] , # ,'WidthFloatMu'] ,
                                 'Width'      : { 'NDim' : 1 , 'Keys' : ['CMS_zz4l_GGsm'] , 'Ext' : '_Width' , 'AxisTitle' : ['#Gamma/#Gamma_{SM}'] , 
                                                  'Min' : [0.] , 'Max' : [60.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [60., 10.]  } ,
                                 'WidthFloatMu'      : { 'NDim' : 1 , 'Keys' : ['CMS_zz4l_GGsm'] , 'Ext' : '_WidthFloatMu' , 'AxisTitle' : ['#Gamma/#Gamma_{SM}'] , 
                                                  'Min' : [0.] , 'Max' : [60.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [60., 10.]  } ,

                              } 
                  } , 

}
