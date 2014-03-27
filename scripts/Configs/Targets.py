targets = { 

###########
# p-value 
###########

  'PVObs'       : { 'notblind' : False , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue' , 'treeKeys' : ['Val'] } , 
  'PVExpPre'    : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue --expectSignal=1 -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov' , 'treeKeys' : ['Val'] } ,  
  'PVExpPost'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue --expectSignal=1 -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov --toysFreq'  , 'treeKeys' : ['Val'] } ,  

###############
# significance
###############

  'SObs'       : { 'notblind' : False , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 'treeKeys' : ['Val'] } , 
  'SExpPre'    : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --expectSignal=1 -t -1 --minimizerAlgo=Minuit' , 'treeKeys' : ['Val'] } ,  
  'SExpPost'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --expectSignal=1 -t -1 --minimizerAlgo=Minuit  --toysFreq'  , 'treeKeys' : ['Val'] } ,  

  #
  # significance SM Higgs Injection
  #
  #'SObsSMToysNoSyst'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
  #                                            'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 500 } ,
  #                                            'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  #'SObsSMToysNoSyst50' : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
  #                                            'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 50 } ,
  #                                            'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  #'SObsSMToysSyst'     : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
  #                                            'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysSyst' , 'NToysJob' : 500 } ,
  #                                            'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} }
  #'SObsSMToysSyst50'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
  #                                            'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysSyst' , 'NToysJob' : 50 } ,
  #                                            'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} }
  #'SObsSMToysAsimov'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
  #                                            'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysAsimov' , 'NToysJob' : -1 } ,

###################
# Limits: Standard
###################

  'ACLsObs'      : { 'notblind' : False , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'treeKeys' : ['Val'] } ,
  'ACLsExp'      : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run expected' , 'treeKeys' : ['95D','68D','Val','68U','95U'] } ,
  'ACLsInjPre'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1' },
  'ACLsInjPost'  : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1 --toysFreq' },

#############################
# Limits: SM Higgs Injection
#############################

  'ACLsSMToysNoSyst'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 500 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysSyst'     : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysSyst'   , 'NToysJob' : 500 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysAsimov'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysAsimov' , 'NToysJob' : -1  } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },

##########
# BestFit
##########

  #'BestFitG'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 --X-rtd FITTER_DYN_STEP ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitG'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
#  'BestFitT'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitT'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --robustFit=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  #'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-2 --rMax=4 --robustFit=1 --X-rtd FITTER_DYN_STEP -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFit'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2  --rMin=-5 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitX'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-5 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit --rMin=-2 --rMax=4 -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] , 'AltModel' : 'Gen' },
  'BestFitExpT'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-10 -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D'
,'68U'] },

##########
# Toys
########## 

  'ToysNoSyst'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 500 --toysNoSystematics --saveToys --expectSignal=1 -s -1' , 'NJobs' : 10 },
  'ToysSyst'      : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 500 --saveToys --expectSignal=1 -s -1' , 'NJobs' : 10 },
  'ToysAsimov'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t -1 --saveToys --expectSignal=1' },

  #
  # Toys Debug
  #
  #'ToysAsymNoSyst'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t -1 --toysNoSystematics  --saveToys --expectSignal=1' },
  #'ToysAsym'          : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t -1 --saveToys --expectSignal=1' },
  #'ToysFull'          : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 2 --saveToys --expectSignal=1 --toysFrequentist' },
  #'ToysFullNoSyst'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 2 --toysNoSystematics --saveToys --expectSignal=1' },
  #'ToysNoSyst'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 1000 --toysNoSystematics --saveToys --expectSignal=1' },
  #'ToysFreq'      : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 1000 --saveToys --expectSignal=1 --toysFreq' },
  #'ACLsToys'     : { 'notblind' : True  , 'method' : 'Asymptotic'   , 'options' : '-t 200 --saveToys --expectSignal=1 --run observed'} ,
  #'MLToys'        : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '--expectSignal=1 --saveNormalizations --noErrors --minos none --verbose 1 -t 100 --saveToys' } ,
  #'MLToysB'       : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '--saveNormalizations --noErrors --minos none --verbose 1 -t 100 --saveToys' } ,


################
# MultiDim Fit
################

  'MDF1DObs'     : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1 --rMin=0 --rMax=3' , 'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 1000 }},
  'MDF1DExp'     : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1 -t -1 --expectSignal=1' , 'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100 }}, 
  # Central value (no errors)
  'MDFObs'         : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '-v 2'},
  'MDFExp'         : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '-v 2 -t -1 --expectSignal=1'},
  # 1D Errors (other parameter fixed to fit value)
  'MDFSnglObs68'   : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=singles -v 2 --minimizerAlgo=Minuit --cl=0.68 ' },
  #'MDFSnglObs95'   : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=singles -v 2 --minimizerAlgo=Minuit --cl=0.95 ' },
  'MDFSnglExp68'   : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=singles -v 2 --minimizerAlgo=Minuit --cl=0.68 -t -1 --expectSignal=1' },
  #'MDFSnglExp95'   : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=singles -v 2 --minimizerAlgo=Minuit --cl=0.95 -t -1 --expectSignal=1' },
  # MultiDim "Cross" Errors (other parameter fixed to fit value)
  'MDFCrossObs68'  : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=cross -v 2 --minimizerAlgo=Minuit --cl=0.68 ' },
  #'MDFCrossObs95'  : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=cross -v 2 --minimizerAlgo=Minuit --cl=0.95 ' },
  'MDFCrossExp68'  : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=cross -v 2 --minimizerAlgo=Minuit --cl=0.68 -t -1 --expectSignal=1' },
  #'MDFCrossExp95'  : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=cross -v 2 --minimizerAlgo=Minuit --cl=0.95 -t -1 --expectSignal=1' },
  # Full Grid Scan
  'MDFGridObs'     : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1' , 'NJobs' : 50 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},
  'MDFGridExp'     : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1 -t -1 --expectSignal=1' , 'NJobs' : 50 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},
  'MDFGridFastObs' : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid --fastScan -v -1' , 'NJobs' : 40 , 'MDFGridParam' :{ 'NPOINTS' : 100000 }},
  'MDFGridFastExp' : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid --fastScan -v -1 -t -1 --expectSignal=1' , 'NJobs' : 40 , 'MDFGridParam' :{ 'NPOINTS' : 100000 }},
  'MDFGridObsMZOptNoFloat': {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 --robustFit=1 --minimizerToleranceForMinos=0.0001 --X-rtd FITTER_DYN_STEP' , 'NJobs' : 100 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},
  'MDFGridObsMZOptFloat'  : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 --robustFit=1 --minimizerToleranceForMinos=0.0001 --X-rtd FITTER_DYN_STEP --floatOtherPOIs=1 ' , 'NJobs' : 100 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},
  'MDFGridExpMZOptNoFloat': {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -t -1 --expectSignal=1 --robustFit=1 --minimizerToleranceForMinos=0.0001 --X-rtd FITTER_DYN_STEP ' , 'NJobs' : 100 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},
  'MDFGridExpMZOptFloat'  : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -t -1 --expectSignal=1 --robustFit=1 --minimizerToleranceForMinos=0.0001 --X-rtd FITTER_DYN_STEP --floatOtherPOIs=1 ' , 'NJobs' : 100 , 'MDFGridParam' :{ 'NPOINTS' : 10000 }},


######
# JCP
######

  'JCP'         : {'notblind' : True  , 'method' : 'HybridNew'   , 
                      'options' : '--testStat=TEV --generateExt=1 --generateNuis=0 --fitNuis=$FITNUIS --singlePoint 1 --saveHybridResult -i 1 --clsAcc 0 --fullBToys -s -1 --setPhysicsModelParameters fqq=$FQQ --freezeNuisances fqq -T 1000' , 'NJobs' : 50 , 
                      #'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } },
                      'JobsParam' : { 'FQQ' : [0.0] , 'FITNUIS' : [0,1] } },

########################
# Fit 3 Mu: ggH, VBH, VH
########################

  # --> Expected Fixing Others
  'Fit3MuExpFix_ggH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_ggH --floatOtherPOI=0 -t -1 --expectSignal=1' ,
                         'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuExpFix_qqH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_qqH --floatOtherPOI=0 -t -1 --expectSignal=1' ,
                         'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuExpFix_VH' :  { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_VH  --floatOtherPOI=0 -t -1 --expectSignal=1' ,
                         'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  # --> Expected Floating Others
  'Fit3MuExp_ggH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_ggH --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuExp_qqH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_qqH --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuExp_VH' :  { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_VH  --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  # --> Observed Floating Others
  'Fit3MuObs_ggH' : { 'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_ggH --floatOtherPOI=1 ' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuObs_qqH' : { 'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_qqH --floatOtherPOI=1 ' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit3MuObs_VH' :  { 'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_VH  --floatOtherPOI=1 ' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },

#####################
# Fit 2 Mu: ggH, VBH
#####################

  # --> Expected Floating Others
  'Fit2MuExp_ggH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_ggH --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit2MuExp_qqH' : { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_qqH --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  # --> Observed Floating Others
  'Fit2MuObs_ggH' : { 'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_ggH --floatOtherPOI=1 ' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  'Fit2MuObs_qqH' : { 'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P r_qqH --floatOtherPOI=1 ' ,
                      'NJobs' : 4 , 'MDFGridParam' :{ 'NPOINTS' : 100} },

#################
# BR(Invisible)
#################

  # --> Expected Fixing Others
  'BRInvExpFix' :   { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P BRInvUndet --floatOtherPOI=0 -t -1 --expectSignal=1' ,
                      'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  # --> Expectes Floating Others
  'BRInvExp'    :   { 'notblind' : True , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P BRInvUndet --floatOtherPOI=1 -t -1 --expectSignal=1' ,
                      'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
                                    
}