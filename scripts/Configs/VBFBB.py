#!/usr/bin/env python


cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

#homedir     = '/afs/cern.ch/work/j/jlauwers/Toys/HWWLimComb/'

#workspace   = homedir+'workspace/'
#jobdir      = homedir+'jobs/'
#plotsdir    = homedir+'plots/'
#cardbase    = homedir+'cards/cmshcg/trunk/'
#combscripts = homedir+'cmshcg/trunk/summer2013/scripts/'

DefaultVersion = 'VBFBB'
channels = { 

'VBFBB' : {
  'vbfbb' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
             'dir' : 'summer2013' , 'subdir' : 'vbfbb/$MASS' , 'card' : 'vbfbb_8TeV.txt'  } ,              
           } ,
  #'vbfbbsplit' :{
  #           '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
  #           'dir' : 'summer2013' , 'subdir' : 'vbfbb/$MASS' , 'card' : 'vbfbb_8TeV_pdfsplit.txt'  } ,              
  #         } ,
  #'vbfbbkostas' : { 
  #            '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
  #           'dir' : 'summer2013' , 'subdir' : 'vbfbb/$MASS' , 'card' : 'datacard_split_mbbParton_m125_CATMIN1_Binned.txt'  } ,              
  #         } ,

# ----------------- Higgs NOM + VBF -------------------------
# 5th order Bernstein polynomial

  'vbfbbsplit_Higgs_CAT0_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT0' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT0.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_expPow_CAT0'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_modG_CAT0'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_tanh_CAT0'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_sin_order1_CAT0'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_Bernstein6_CAT0'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT1_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT1' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT1.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_expPow_CAT1'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_modG_CAT1'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_tanh_CAT1'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_sin_order1_CAT1'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_Bernstein6_CAT1'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT2_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT2' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT2.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_expPow_CAT2'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_modG_CAT2'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_tanh_CAT2'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_sin_order1_CAT2'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_Bernstein6_CAT2'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT3_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT3' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT3.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_expPow_CAT3'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_modG_CAT3'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_tanh_CAT3'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_sin_order1_CAT3'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_Bernstein6_CAT3'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT4_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT4.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_expPow_CAT4'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_modG_CAT4'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_tanh_CAT4'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_sin_order1_CAT4'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_Bernstein6_CAT4'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT5_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT5.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_expPow_CAT5'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_modG_CAT5'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_tanh_CAT5'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_sin_order1_CAT5'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_Bernstein6_CAT5'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT6_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT6.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_expPow_CAT6'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_modG_CAT6'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_tanh_CAT6'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_sin_order1_CAT6'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_Bernstein6_CAT6'    ]} ,
                                     }           
                      },
           } ,
                  
# 4th order Bernstein polynomial

  'vbfbbsplit_Higgs_CAT0_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT0.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_expPow_CAT0'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_modG_CAT0'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_tanh_CAT0'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_sin_order1_CAT0'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-205.root','w:QCD_Bernstein6_CAT0'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT1_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT1.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_expPow_CAT1'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_modG_CAT1'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_tanh_CAT1'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_sin_order1_CAT1'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-210.root','w:QCD_Bernstein6_CAT1'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT2_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT2.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_expPow_CAT2'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_modG_CAT2'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_tanh_CAT2'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_sin_order1_CAT2'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-220.root','w:QCD_Bernstein6_CAT2'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT3_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT3.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_expPow_CAT3'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_modG_CAT3'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_tanh_CAT3'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_sin_order1_CAT3'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-225.root','w:QCD_Bernstein6_CAT3'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT4_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT4.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_expPow_CAT4'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_modG_CAT4'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_tanh_CAT4'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_sin_order1_CAT4'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-200.root','w:QCD_Bernstein6_CAT4'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT5_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT5.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_expPow_CAT5'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_modG_CAT5'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_tanh_CAT5'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_sin_order1_CAT5'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-205.root','w:QCD_Bernstein6_CAT5'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT6_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT6.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_expPow_CAT6'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_modG_CAT6'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_tanh_CAT6'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_sin_order1_CAT6'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_Bernstein6_CAT6'    ]} ,
                                     }           
                      },
           } ,     
   
# all Categories
   
  'vbfbbsplit_Higgs_allCAT' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_allCat_m$MASS.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['ch6','newAltModels_CAT6_80-210.root','w:QCD_expPow_CAT6'    ], 
							 'bkg_QCD': ['ch7','newAltModels_CAT5_75-205.root','w:QCD_expPow_CAT5'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_modG_CAT6'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_tanh_CAT6'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_sin_order1_CAT6'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_Bernstein6_CAT6'    ]} ,
                                     }           
                      },
           } ,   
          
  'vbfbbsplit_Higgs_NOM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_NOM_m$MASS.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['ch6','newAltModels_CAT6_80-210.root','w:QCD_expPow_CAT6'    ],
                                                         'bkg_QCD': ['ch7','newAltModels_CAT5_75-205.root','w:QCD_expPow_CAT5'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_modG_CAT6'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_tanh_CAT6'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_sin_order1_CAT6'    ]} ,
                                      'Bern6'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-210.root','w:QCD_Bernstein6_CAT6'    ]} ,
                                     }
                      },
           } ,

 
# 160 GeV Range

'vbfbbsplit_Higgs_CAT0_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT0' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT0_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-235.root','w:QCD_expPow_CAT0'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-235.root','w:QCD_modG_CAT0'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-235.root','w:QCD_tanh_ext_CAT0'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT0_75-235.root','w:QCD_sin_order2_CAT0'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT1_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT1' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT1_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-240.root','w:QCD_expPow_Paolo_CAT1'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-240.root','w:QCD_modG_extb_CAT1'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-240.root','w:QCD_tanh_CAT1'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT1_80-240.root','w:QCD_sin_order2_CAT1'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT2_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT2' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT2_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-250.root','w:QCD_expPow_CAT2'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-250.root','w:QCD_modG_CAT2'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-250.root','w:QCD_tanh_CAT2'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT2_90-250.root','w:QCD_sin_order2_CAT2'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT3_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb_CAT3' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT3_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-255.root','w:QCD_expPow_CAT3'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-255.root','w:QCD_modG_CAT3'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-255.root','w:QCD_tanh_CAT3'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT3_95-255.root','w:QCD_sin_order1_CAT3'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT4_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT4_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-230.root','w:QCD_expPow_CAT4'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-230.root','w:QCD_modG_CAT4'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-230.root','w:QCD_tanh_CAT4'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT4_70-230.root','w:QCD_sin_order1_CAT4'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT5_brn4_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein4_CAT5_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-235.root','w:QCD_expPow_CAT5'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-235.root','w:QCD_modG_extb_CAT5'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-235.root','w:QCD_tanh_CAT5'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT5_75-235.root','w:QCD_sin_order1_CAT5'    ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Higgs_CAT6_brn5_160GeV' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'datacard_m$MASS_Bernstein5_CAT6_160GeV.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-240.root','w:QCD_expPow_CAT6'    ]} ,
                                      'modG'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-240.root','w:QCD_modG_CAT6'    ]} ,
                                      'tanh'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-240.root','w:QCD_tanh_CAT6'    ]} ,
                                      'sine'     : { 'bkg_QCD': ['*','newAltModels_CAT6_80-240.root','w:QCD_sin_order1_CAT6'    ]} ,
                                     }           
                      },
           } ,

                  
# ------------------------------------------------------------
           
  'vbfbbsplit_Zfit' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace.root','w:qcd_model_alt3'      ]} ,                                      
                                      'modG_ext'   : { 'qcd': ['*','newAltModels_Zfit.root','w:QCD_modG_Paolo_'      ]} ,
                                     }           
                      },
           } ,
           
  'vbfbbsplit_Zfit_70_250' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max250.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max250.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max250.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max250.root','w:qcd_model_alt3'      ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_max250.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max250.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_max250.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_180' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max180.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_180_brn7' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max180_brn7.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-180.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_70-200_MM.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-200_MM.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-200_MM.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-200_MM.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
    'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_brn3.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_brn4.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'modG_Paolo' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_Paolo_'      ]} ,
                                      '2Sine' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_sin_order2'      ]} ,
                                      'Bernstein5' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_Bernstein5_MM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_brn5.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'modG_Paolo' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_Paolo_'      ]} ,
                                      '2Sine' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_sin_order2'      ]} ,
                                      'Bernstein6' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_brn6_MM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_0xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_0xSM.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'modG_Paolo' : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_Paolo_'      ]} ,
                                      '2Sine' : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_sin_order2'      ]} ,
                                      'Bernstein6' : { 'bkg_QCD': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:qcd_model_brn6_MM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_2xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_2xSM.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'modG_Paolo' : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_Paolo_'      ]} ,
                                      '2Sine' : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_sin_order2'      ]} ,
                                      'Bernstein6' : { 'bkg_QCD': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:qcd_model_brn6_MM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn8' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_brn8.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'modG_Paolo' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_modG_Paolo_'      ]} ,
                                      '2Sine' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:QCD_sin_order2'      ]} ,
                                      'Bernstein6' : { 'bkg_QCD': ['*','newAltModels_Zfit_70-200_MM_dPhibb_2.root','w:qcd_model_brn6_MM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_invMM_dPhibb_2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_invMM_dPhibb_2.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM_dPhibb_2.root','w:qcd_model_alt2_invMM'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                      'Bernstein4'  : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM_dPhibb_2.root','w:QCD_Bernstein4__invMM'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_0xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_0xSM.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_2xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_dPhibb_2_2xSM.txt' ,  
                        'altmodel' : {
                                      'alt2'     : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:qcd_model_alt2_MM'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_ext'  : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_MM_dPhibb_2.root','w:QCD_tanh_ext_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_invMM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_invMM_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-200_invMM.root','w:QCD_tanh_Paolo_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_invMM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_invMM_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_70-200_$CHANNEL.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_70-200_$CHANNEL.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-200_$CHANNEL.root','w:QCD_tanh_Paolo_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_invMM_0xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_invMM_brn5_0xSM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_$CHANNEL.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_$CHANNEL.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_0xSM_70-200_$CHANNEL.root','w:QCD_tanh_Paolo_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_200_MM_invMM_2xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-200_MM_invMM_brn5_2xSM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_$CHANNEL.root','w:qcd_model_alt1'    ]} ,
                                      'modG_extb'   : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_$CHANNEL.root','w:QCD_modG_extb_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_2xSM_70-200_$CHANNEL.root','w:QCD_tanh_Paolo_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max160.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160_LL' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_LL.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160_LL_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_LL_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160_LL_brn4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_LL_brn4.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_LL.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext2'  : { 'qcd': ['*','newAltModels_Zfit_70-160_LL.root','w:QCD_expPow_ext2_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160_MM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_MM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_MM.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_MM.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_MM.root','w:qcd_model_alt3'      ]} ,
                                      'tanh'  : { 'qcd': ['*','newAltModels_Zfit_70-160_MM.root','w:QCD_tanh_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_70-160_MM.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
  'vbfbbsplit_Zfit_70_160_invMM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_invMM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt3'      ]} ,
                                      'modG'   : { 'qcd': ['*','newAltModels_Zfit_70-160_invMM.root','w:QCD_modG_'      ]} ,
                                      'tanh'  : { 'qcd': ['*','newAltModels_Zfit_70-160_invMM.root','w:QCD_tanh_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_70-160_invMM.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
    'vbfbbsplit_Zfit_70_160_MM_invMM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_70-160_MM_invMM.txt' ,  
                        'altmodel' : {
                                      #'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt1'    ]} ,
                                      #'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt2'      ]} ,
                                      #'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_70-160_invMM.root','w:qcd_model_alt3'      ]} ,
                                      #'tanh'  : { 'qcd': ['*','newAltModels_Zfit_70-160_MM.root','w:QCD_tanh_'      ]} ,
                                      #'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_70-160_MM.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,          
  'vbfbbsplit_Zfit_70_160_2xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max160_2xSM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max160_2xSM.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max160_2xSM.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max160_2xSM.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_max160_2xSM.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max160_2xSM.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_max160_2xSM.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
   'vbfbbsplit_Zfit_70_160_0xSM' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max160_0xSM.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max160_0xSM.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max160_0xSM.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max160_0xSM.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_max160_0xSM.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max160_0xSM.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_max160_0xSM.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
   'vbfbbsplit_Zfit_70_160_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max160_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max160.root','w:qcd_model_alt3'      ]} ,
                                      'modG_Paolo'   : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_modG_Paolo_'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_max160.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,    
   'vbfbbsplit_Zfit_70_140_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [125,125] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys' , 'card' : 'datacard_Z_noParSyst_max140_brn5.txt' ,  
                        'altmodel' : {
                                      'alt1'     : { 'qcd': ['*','dataZ_shapes_workspace_max140.root','w:qcd_model_alt1'    ]} ,
                                      'alt2'       : { 'qcd': ['*','dataZ_shapes_workspace_max140.root','w:qcd_model_alt2'      ]} ,
                                      'alt3'       : { 'qcd': ['*','dataZ_shapes_workspace_max140.root','w:qcd_model_alt3'      ]} ,
                                      'tanh_Paolo'  : { 'qcd': ['*','newAltModels_Zfit_max140.root','w:QCD_tanh_Paolo_'      ]} ,
                                      'expPow_ext1'  : { 'qcd': ['*','newAltModels_Zfit_max140.root','w:QCD_expPow_ext1_'      ]} ,
                                     }           
                      },
           } ,
           
  'vbfbbsplit_13TeV' :{
             '13TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 13 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_13TeV_split.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 
                                      
                                      'expPow_ext'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_ext2_$CHANNEL'    ]} ,
                                      'modG_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,
                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'modG_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_Paolo_$CHANNEL'      ]} ,
                                      'tanh_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_Paolo_$CHANNEL'      ]} ,
                                      
                                      'fourier'       : { 'qcd': ['*','newAltModels.root','w:QCD_sin_order2_$CHANNEL'      ]} ,

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_brn6' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_brn6.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
   'vbfbbsplit_noParSyst_min80' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min80.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                     }           
                      },
           } ,        
           
  'vbfbbsplit_noParSyst_min80_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min80_CAT1.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min80_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min80_CAT2.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min80_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min80_CAT3.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min80_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min80_CAT4.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_80.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_80.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_min85' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_min85.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_min85' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min85.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } ,        
           
  'vbfbbsplit_noParSyst_min85_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min85_CAT1.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min85_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min85_CAT2.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min85_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min85_CAT3.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min85_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min85_CAT4.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_85.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_85.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
   'vbfbbsplit_min90' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_min90.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } ,  
   'vbfbbsplit_noParSyst_min90' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min90.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } ,        
           
  'vbfbbsplit_noParSyst_min90_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min90_CAT1.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min90_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min90_CAT2.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min90_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min90_CAT3.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_min90_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_min90_CAT4.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Min_90.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      
                                      'modG_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'fourier'       : { 'qcd': ['*','newAltModels_Min_90.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max175' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max175.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } ,        
           
  'vbfbbsplit_noParSyst_max175_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max175_CAT1.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max175_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max175_CAT2.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max175_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max175_CAT3.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max175_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max175_CAT4.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_175.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max215' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max215.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } ,        
           
  'vbfbbsplit_noParSyst_max215_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max215_CAT1.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max215_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max215_CAT2.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max215_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max215_CAT3.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_noParSyst_max215_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_max215_CAT4.txt' ,  
                        'altmodel' : {
                                      'Kalt1'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','newWorkspace_Max_215.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                     }           
                      },
           } , 
           
  'vbfbbsplit_brn6' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_brn6.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_CAT1.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                      'expPow_ext'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_ext2_$CHANNEL'    ]} ,
                                      'modG_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,
                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'modG_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_Paolo_$CHANNEL'      ]} ,
                                      'tanh_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_Paolo_$CHANNEL'      ]} ,
                                                                            
                                      'fourier'       : { 'qcd': ['*','newAltModels.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_brn6_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_brn6_CAT1.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_CAT2.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                      'expPow_ext'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_ext2_$CHANNEL'    ]} ,
                                      'modG_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,
                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'modG_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_Paolo_$CHANNEL'      ]} ,
                                      'tanh_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_Paolo_$CHANNEL'      ]} ,
                                                                            
                                      'fourier'       : { 'qcd': ['*','newAltModels.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
   'vbfbbsplit_noParSyst_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_CAT3.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                      'expPow_ext'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_ext2_$CHANNEL'    ]} ,
                                      'modG_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,
                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'modG_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_Paolo_$CHANNEL'      ]} ,
                                      'tanh_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_Paolo_$CHANNEL'      ]} ,
                                                                            
                                      'fourier'       : { 'qcd': ['*','newAltModels.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
     'vbfbbsplit_noParSyst_brn6_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_brn6_CAT2.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
   'vbfbbsplit_noParSyst_brn6_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_brn6_CAT3.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,

   'vbfbbsplit_noParSyst_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_CAT4.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                      'expPow_ext'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_ext2_$CHANNEL'    ]} ,
                                      'modG_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_extb_$CHANNEL'      ]} ,
                                      'tanh_ext'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_ext_$CHANNEL'      ]} ,
                                      
                                      'expPow_Paolo'     : { 'qcd': ['*','newAltModels.root','w:QCD_expPow_Paolo_$CHANNEL'    ]} ,
                                      'modG_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_modG_Paolo_$CHANNEL'      ]} ,
                                      'tanh_Paolo'       : { 'qcd': ['*','newAltModels.root','w:QCD_tanh_Paolo_$CHANNEL'      ]} ,
                                                                            
                                      'fourier'       : { 'qcd': ['*','newAltModels.root','w:QCD_sin_order2_$CHANNEL'      ]} ,
                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_noParSyst_brn6_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_noParSyst_brn6_CAT4.txt' ,  
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern5'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein5_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,
           
  'vbfbbsplit_CAT1' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT1.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,



  'vbfbbsplit_CAT1_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT1_Brn5.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
           

  'vbfbbsplit_CAT2' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT2.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
           
  'vbfbbsplit_CAT2_brn6' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT2_Brn6.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
           
  'vbfbbsplit_CAT2_brn5' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT2_Brn5.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,

  'vbfbbsplit_CAT3' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT3.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
           
  'vbfbbsplit_CAT3_brn6' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT3_Brn6.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,

  'vbfbbsplit_CAT4' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT4.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} ,
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
  
  'vbfbbsplit_CAT4_brn6' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split_CAT4_Brn6.txt' ,
                        'altmodel' : {
                                      'expPow'     : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'modG'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'tanh'       : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'CexpPow'     : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_expPow_Hsel_$CHANNEL'    ]} ,
                                      'CmodG'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_modG_Hsel_$CHANNEL'      ]} ,
                                      'Ctanh'       : { 'qcd': ['*','CERN_mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_tanh_Hsel_$CHANNEL'      ]} ,

                                      'Kalt1'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate1_$CHANNEL'    ]} ,    
                                      'Kalt2'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate2_$CHANNEL'    ]} ,    
                                      'Kalt3'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_alternate3_$CHANNEL'    ]} , 
                                      'Bern6'       : { 'qcd': ['*','qcd_shapes_mbbParton_data_hard_workspace.root','w:qcd_model_bernstein6_$CHANNEL'    ]} , 

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,
},


}
    
combinations = {

#
# VBFBB
#
   'vbfbb' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbb' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,

   'vbfbbsplit' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                       
# ----------------- Higgs NOM + VBF -------------------------
#  5th order Bernstein polynomial  

   'vbfbbsplit_Higgs_CAT0_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT0_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT1_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT1_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT2_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT2_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Higgs_CAT3_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT3_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT4_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT4_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT5_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT5_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT6_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT6_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,  
                        
#  4th order Bernstein polynomial    

  'vbfbbsplit_Higgs_CAT0_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT0_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT1_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT1_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT2_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT2_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Higgs_CAT3_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT3_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT4_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT4_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT5_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT5_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT6_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT6_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,  
                        
# all Categories
   
  'vbfbbsplit_Higgs_allCAT' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_allCAT' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,  

 'vbfbbsplit_Higgs_NOM' :
                        {
                          'energies' : [ '8TeV' ] ,
                          'channels' : [ 'vbfbbsplit_Higgs_NOM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
                        
 'vbfbbsplit_Higgs_NOMX' :
                       {
                          'energies' : [ '8TeV' ] ,
                          'channels' : [ 'vbfbbsplit_Higgs_CAT0_brn5' , 'vbfbbsplit_Higgs_CAT1_brn5', 'vbfbbsplit_Higgs_CAT2_brn5' , 'vbfbbsplit_Higgs_CAT3_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,


#  extended range (160 GeV)    

  'vbfbbsplit_Higgs_CAT0_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT0_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT1_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT1_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT2_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT2_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Higgs_CAT3_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT3_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT4_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT4_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT5_brn4_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT5_brn4_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Higgs_CAT6_brn5_160GeV' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Higgs_CAT6_brn5_160GeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,                        
                        
  
# -------------------------------------------------------------                     
                        
   'vbfbbsplit_Zfit' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,                      
   'vbfbbsplit_Zfit_70_250' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_250' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Zfit_70_180' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_180' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,            
   'vbfbbsplit_Zfit_70_180_brn7' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_180_brn7' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,     
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_0xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_0xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_2xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn5_2xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn8' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_dPhibb_2_brn8' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_invMM_dPhibb_2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_invMM_dPhibb_2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,          
   'vbfbbsplit_Zfit_70_200_MM_invMM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_invMM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_invMM_0xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_invMM_0xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_MM_invMM_2xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_MM_invMM_2xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_200_invMM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_200_invMM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,                         
   'vbfbbsplit_Zfit_70_160_LL' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_LL' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Zfit_70_160_LL_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_LL_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,   
   'vbfbbsplit_Zfit_70_160_LL_brn4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_LL_brn4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Zfit_70_160_MM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_MM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_Zfit_70_160_invMM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_invMM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,
  'vbfbbsplit_Zfit_70_160_MM_invMM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_MM_invMM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_160' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,   
   'vbfbbsplit_Zfit_70_160_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } , 
   'vbfbbsplit_Zfit_70_160_2xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_2xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,   
   'vbfbbsplit_Zfit_70_160_0xSM' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_160_0xSM' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,  
   'vbfbbsplit_Zfit_70_140_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_Zfit_70_140_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf Z #rightarrow b#bar{b}'
                        } ,   
   'vbfbbsplit_13TeV' :
                        {
                          'energies' : [ '13TeV' ] , 
                          'channels' : [ 'vbfbbsplit_13TeV' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,

   'vbfbbsplit_noParSyst' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_min80' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min80' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,                 
   'vbfbbsplit_noParSyst_min80_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min80_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min80_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min80_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min80_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min80_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min80_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min80_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_min85' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_min85' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,         
   'vbfbbsplit_noParSyst_min85' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min85' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,                 
   'vbfbbsplit_noParSyst_min85_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min85_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min85_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min85_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min85_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min85_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min85_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min85_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   
   'vbfbbsplit_min90' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_min90' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,   
   'vbfbbsplit_noParSyst_min90' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min90' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,                 
   'vbfbbsplit_noParSyst_min90_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min90_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min90_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min90_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min90_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min90_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_min90_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_min90_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_max175' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max175' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,                 
   'vbfbbsplit_noParSyst_max175_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max175_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max175_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max175_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max175_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max175_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max175_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max175_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_max215' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max215' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,                 
   'vbfbbsplit_noParSyst_max215_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max215_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max215_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max215_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max215_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max215_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
   'vbfbbsplit_noParSyst_max215_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_max215_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_brn6' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_brn6' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_brn6' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_brn6' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
  'vbfbbsplit_noParSyst_brn6_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_brn6_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_brn6_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_brn6_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_brn6_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_brn6_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
   'vbfbbsplit_noParSyst_brn6_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_noParSyst_brn6_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,

   'vbfbbkostas' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbkostas' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,

   'vbfbbsplit_CAT1' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_CAT1' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                        
                        
   'vbfbbsplit_CAT1_brn5' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_CAT1_brn5' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,
                                

   'vbfbbsplit_CAT2' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_CAT2' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,


   'vbfbbsplit_CAT3' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_CAT3' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,


   'vbfbbsplit_CAT4' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_CAT4' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'vbf H #rightarrow b#bar{b}'
                        } ,




}

