#!/usr/bin/env python

homedir     = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/'
#homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWW13TeV/HWWLimComb/'
#homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/'
#homedir     = '/Users/xjanssen/cms/HWW2012/HWWLimComb/'

workspace   = homedir+'workspace/'
jobdir      = homedir+'jobs/'
plotsdir    = homedir+'plots/'
cardbase    = homedir+'cmshcg/trunk/'
combscripts = homedir+'cmshcg/trunk/summer2013/scripts/'

cardtypes = {
  #
  # SM Higgs: Coupling/Limit/Toys
  #
  'couplings' : { 'dir' : 'couplings' , 'masses' : [125.6] 
                } ,
  'couplings2': { 'dir' : 'couplings' , 'masses' : [125.7] 
                } ,
  'smhiggs'   : { 'dir' : 'couplings' , 'targetdir' : 'smhiggs' ,
                  'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] 
                  #'masses' : [125, 125.5,126,126.5,127 , 127.5 , 128 , 128.5 ,129 ,129.5 , 130] 
                  #'masses' : [125,127] 
                  #'masses' : [125] 
                  #'masses' : [400,500,600]
                } ,
  'ewksinglet': { 'dir' : 'ewksinglet' , 'targetdir' : 'ewksinglet' ,
                  #'masses' : [110, 115, 120, 125, 130, 135, 140, 150,160,170,180,190,200,250,300,350,400,450,500,550,600,700,800,900,1000]
                  'masses' : [200,250,300,350,400,450,500,550,600,700,800,900,1000]

                } ,   
  'smhiggs2'  : { 'dir' : 'couplings' , 'targetdir' : 'smhiggs' ,
                  #'masses' : [125,125.5,126,126.5,127,127.5,128,128.5,129,129.5,130]
                  'masses' : 
                            #[124.5,124.6,124.7,124.8,124.9,125.1,125.2,125.3,125.4,125.5,125.6,125.7,125.8,125.9,126,126.1,126.2,126.3,126.4,126.5
                            #,115, 120, 125, 130, 135,127,127.5,128,128.5,129,129.5
                            #]
                             [
                              #115, 
                              120, 
                              124.5,124.6,124.7,124.8,124.9, 
                              125,
                              125.1,125.2,125.3,125.4,125.5,125.6,125.7,125.8,125.9,126,126.1,126.2,126.3,126.4,126.5,  
                              127,127.5,128,128.5,129,129.5, 
                              130, 
                              #135
                             ]
                } ,
  'sminject'  : { 'dir' : 'searches'  , 'targetdir' : 'sminject', 
                  'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] ,
                  'preProc' : ['SMInject'] 
                } ,
  'smtoys'    : { 'dir' : 'searches'  , 'targetdir' : 'smtoys'  , 
                  'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] ,
                  'preProc' : ['SMToys'] 
                } ,
  #
  # Second Higgs
  #
  'searches'  : { 'dir' : 'searches'  ,                           
                  #'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] 
                  'masses' : [250,300,350,400,450,500,550,600]
                } ,
  # 
  # Mass Scan
  #
  'mass'      : { 'dir' : 'couplings' , 'targetdir' : 'mass'    , 
                  'masses' : [
                              #110, 110.5, 111, 111.5, 112, 112.5, 113, 113.5, 114, 114.5, 115, 115.5, 116, 116.5, 117, 117.5, 118, 118.5, 119, 119.5,
                              #120, 120.5, 121, 121.5, 122, 122.5, 123, 123.5, 124, 124.5, 125, 125.5, 126, 126.5, 127, 127.5, 128, 128.5, 129, 129.5,
                              #130, 130.5, 131, 131.5, 132, 132.5, 133, 133.5, 134, 134.5, 135, 135.5, 136, 136.5, 137, 137.5, 138, 138.5, 139, 139.5,
                              # 1 GeV
                              110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
                              120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
                              130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 
                              140
                              #140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
                              #150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 
                              #160 
                              # 5 GeV
                              #110, 115, 120, 125, 130, 135, 140 , 145 , 150 , 155 , 160 
                             ] 
                }, 
  'masssminj' : { 'dir' : 'searches' , 'targetdir' : 'masssminj'    , 
                  'masses' : [
                              #110, 110.5, 111, 111.5, 112, 112.5, 113, 113.5, 114, 114.5, 115, 115.5, 116, 116.5, 117, 117.5, 118, 118.5, 119, 119.5,
                              #120, 120.5, 121, 121.5, 122, 122.5, 123, 123.5, 124, 124.5, 125, 125.5, 126, 126.5, 127, 127.5, 128, 128.5, 129, 129.5,
                              #130, 130.5, 131, 131.5, 132, 132.5, 133, 133.5, 134, 134.5, 135, 135.5, 136, 136.5, 137, 137.5, 138, 138.5, 139, 139.5,
                              # 1 GeV
                              110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
                              120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
                              130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
                              140
                              #140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
                              #150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 
                              #160 
                              # 5 Gev
                              # 110, 115, 120, 125, 130, 135, 140 , 145 , 150 , 155 , 160
                             ] ,
                  'preProc' : ['SMInject'] 
                } , 

  #
  # Spin/Parity
  #  
  'jcp'       : { 'dir' : 'jcp'       , 'masses' : [125.6] 
                } , 
  #  
  # Old stuff
  #
# 'custom'    : { 'dir' : 'couplings' , 'masses' : [125] } , 
#  'wjetfix'   : { 'dir' : 'searches'  , 'targetdir' : 'wjetfix' , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] , 'preProc' : ['WJetFix'] } , 
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 500, 600] } ,
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250 , 300 ] } ,
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200 ] } ,
}

preProc = {
  'WJetFix'  : { 'ChannelList' : [
                                  'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_cut' , 'hww1jof_cut' , 
                                  'hww0jof_shape' , 'hww1jof_shape' , 
                                  'hww2jof_cut' , 'hww2jsf_cut' , 
                                  'vh3l_sssf_cut'  , 'vh3l_ossf_cut'  
                                  'vh3l_sssf_shape'  , 'vh3l_ossf_shape'  
                                 ] , 
                 'processList' : ['WjetsM','WjetsE','Wjets'] , 'massWJ' : '$MASS'  } ,
  'SMInject' : {} ,
  
}

extrapolations = { 'Mass'  : { 
                               #125 : [125.5,126,126.5,127] ,
                               #130 : [129.5,129,128.5,128,127.5] ,
                               125 : [124.5,124.6,124.7,124.8,124.9,125.1,125.2,125.3,125.4,125.5,125.6,125.7,125.8,125.9,126,126.1,126.2,126.3,126.4,126.5,127],
                               #125 : [127]

                             } ,
                   '13TeV' : {
                               'Energy' : '8TeV' ,
                               'Lumi'   : { 
                                           'Origin'  : 19.4 ,
                                           'Targets' : [30,120,300,3000] ,
                                          } ,
   
                             } ,
                 }


# V3 Most results
# V4 Debug version for KV,KF 
# V5 MHFit 100  mu points + 125 Injection
# V6 MHFit 120  mu points
# V7 MHFit 1000 mu points

# V8: Pixel lumi

DefaultVersion = '13TeV'
DefaultVersion = 'VBFBB'
channels = { 

'EWKSinglet' : {

  'of0j_oldcps':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'oldcps' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_oldcps':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'oldcps' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,

  'of0j_newcps':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'newcps' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_newcps':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'newcps' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,

  'of0j_smbkgd':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'smbkgd' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_smbkgd':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'smbkgd' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,

  # ------- CP2

  # C^2 =  
  'of0j_cp2_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d9':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_0d9':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d8':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_0d8':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d7':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_0d7':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d6':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_0d6':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d5':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_0d5':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d4':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_0d4':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d3':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_0d3':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d2':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_0d2':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_0d1':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_0d1':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkcp2' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2

  # C^2 =  
  'of0j_cp2_7TeV_1d0':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_1d0':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d9':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d9':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d8':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d8':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d7':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d7':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d6':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d6':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d5':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d5':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d4':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d4':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d3':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d3':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d2':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d2':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_7TeV_0d1':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_7TeV_0d1':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of' , 'card' : 'hww-4.94fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2 -- Approximation

  # C^2 =  
  'of0j_cp2_app_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_app_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d9':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d9':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d8':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d8':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d7':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d7':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d6':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d6':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d5':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d5':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d4':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d4':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d3':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d3':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d2':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d2':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_app_0d1':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_app_0d1':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkapp' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2 -- Approximation

  # C^2 =  
  'of0j_cp2_bwo_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d9':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d9':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d8':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d8':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d7':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d7':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d6':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d6':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d5':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d5':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d4':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d4':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d3':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d3':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d2':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d2':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_bwo_0d1':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_bwo_0d1':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkbwo' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2 -- Approximation

  # C^2 =  
  'of0j_cp2_ext_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d9':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d9':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d8':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d8':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d7':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d7':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d6':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d6':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d5':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d5':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d4':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d4':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d3':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d3':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d2':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d2':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ext_0d1':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_ext_0d1':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2 -- Approximation

  # C^2 =  
  'sf0j_cp2_ext_1d0':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_1d0':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d9':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d9':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d8':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d8':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d7':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d7':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d6':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d6':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d5':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d5':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d4':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d4':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d3':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d3':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d2':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d2':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf0j_cp2_ext_0d1':{
               '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'sf1j_cp2_ext_0d1':{
               '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkextsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,


  # ------- CP2 -- Approximation

  # C^2 =  
  'of0j_cp2_ovf_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d9':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d9':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d8':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d8':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d7':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d7':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d6':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d6':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d5':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d5':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d4':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d4':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d3':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d3':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d2':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d2':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of0j_cp2_ovf_0d1':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,
  'of1j_cp2_ovf_0d1':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkovf' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,

  # ------- CP2 -- Approximation

  # C^2 =  
  'of0j_cp2_lom_1d0':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewklom' , 'card' : 'hww-19.47fb.mH$MASS.of_0j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,
  'of1j_cp2_lom_1d0':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewklom' , 'card' : 'hww-19.47fb.mH$MASS.of_1j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 =  
  'of0j_inj_lom':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_inj_lom':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,


  # C^2 =  
  'of0j_inj_ext':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injext' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_inj_ext':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injext' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,

  # C^2 =  
  'of0j_inj_lom_pt30':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom_pt30' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_inj_lom_pt30':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom_pt30' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,

  # C^2 =
  'of0j_inj_lom_pt30_mth80':{
               '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  ,
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom_pt30_mth80' , 'card' : 'hww-19.47fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_inj_lom_pt30_mth80':{
               '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  ,
                          'dir' : 'EWKSinglet', 'subdir' : 'injlom_pt30_mth80' , 'card' : 'hww-19.47fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,


### 7 TEV

  'of0j_sm_7TeV':{
               '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  ,
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of_paper' , 'card' : 'hww-4.94fb.mH$MASS.of_0j_shape.txt'  } ,
             } ,
  'of1j_sm_7TeV':{
               '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110, 600]  ,
                          'dir' : 'EWKSinglet', 'subdir' : 'sm7of_paper' , 'card' : 'hww-4.94fb.mH$MASS.of_1j_shape.txt'  } ,
             } ,



### VBF


  # ------- CP2

  # C^2 =  
  'of2j_cp2_1d0':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d9':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d8':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d7':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d6':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d5':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d4':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d3':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d2':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_0d1':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,

  #### 7 TeV


  # ------- CP2

  # C^2 =  
  'of2j_cp2_7TeV_1d0':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d9':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d8':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d7':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d6':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d5':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d4':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d3':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d2':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_cp2_7TeV_0d1':{
               '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [160,600]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'vbf7of' , 'card' : 'hww-4.92fb.mH$MASS.of_2j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,



  # ------- CP2

  # C^2 =  
  'of2jnew_cp2_1d0':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d9':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d8':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d7':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d6':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d5':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d4':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d3':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d2':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2jnew_cp2_0d1':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfnew' , 'card' : 'hww-19.36fb.mH$MASS.of_2j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,

  # C^2 = 
  'of2j_paper':{
               '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'smpvbf' , 'card' : 'hww-19.36fb.mH$MASS.of_2j_shape.txt'  } ,
             } ,

  'sf2j_paper':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'smpvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j_shape.txt'  } ,
             } ,

  # ------- CP2

  # C^2 =  
  'sf2j_cp2_1d0':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_1d0_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d9':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d9_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d8':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d8_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d7':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d7_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d6':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d6_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d5':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d5_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d4':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d4_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d3':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d3_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d2':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
                          'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d2_shape.txt'  } ,
             } ,

  # C^2 = 
  'sf2j_cp2_0d1':{
               '8TeV' : { 'tag' : 'sf2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [160,1000]  , 
		       'dir' : 'EWKSinglet', 'subdir' : 'ewkvbfsf' , 'card' : 'hww-19.47fb.mH$MASS.sf_2j.EWKSinglet_CP2_0d1_shape.txt'  } ,
             } ,




},

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

  'vbfbbsplit' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbbtoys/$MASS' , 'card' : 'vbfbb_8TeV_split.txt' ,  
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

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      },
           } ,


  'vbfbbsplit_bias' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115,135] ,
                        'dir' : 'summer2013' , 'subdir' : 'vbfbb_bias' , 'card' : 'datacard_split_mbbParton_m$MASS_CATMIN1_Binned.txt' ,  
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

                                     #'Bernstein4' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein4_Hsel_$CHANNEL']} , 
                                     #'Bernstein5' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein5_Hsel_$CHANNEL']} , 
                                     #'Bernstein6' : { 'qcd': ['*','mbbShapes_Hsel_$MASS_tight.root','workspace:QCD_Bernstein6_Hsel_$CHANNEL']} , 
                                     }           
                      } ,              
           } ,



},

'13TeV' : {


# =========== 13 TeV Projection @ 30 fb-1 ====================== 

  # ============ H -> WW 0/1-jet SF cut-based ================== 
  'hww0jsf_30ifb' : { 
                    '13TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwsf_0j_cut_8TeV.txt'} ,  
                    } ,
  'hww1jsf_30ifb' : {
                    '13TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwsf_1j_cut_8TeV.txt'} ,
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_30ifb' : {
                    '13TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_30ifb'  : {
                    '13TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } , 
  # ============ H -> WW VBF SF Cut Based =====================
  'hww2jsf_30ifb' :   {
                    '13TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 13 , 'method' : 'cut'  , 'mrange' : [110,600] , 
                                'dir' : '13TeV'   ,  'subdir' : '30ifb' , 'card' : 'hwwsf_2j_cut_8TeV.txt'},
                    } ,
  # ============ H -> WW VBF OF Shape Based =====================
  'hww2jof_30ifb' : {
                    '13TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 13 , 'method' : 'shape'  , 'mrange' : [110,600] ,
                                'dir' : '13TeV'   ,  'subdir' : '30ifb' , 'card' : 'hwwof_2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_2j_shape.root'] },
                    } ,

  # ============ VH -> WW 3l shape-based ==================
  'vh3l_sssf_30ifb' :  {
                    '13TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200] , 
                                'dir' : '13TeV' , 'subdir' : '30ifb', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_30ifb' : {
                    '13TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200] , 
                                'dir' : '13TeV' , 'subdir' : '30ifb', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
                    } ,

  # ============ VH -> WW 2j SF cut-based ==================
  'hwwvh2jsf_30ifb' : {
                    '13TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwsf_vh2j_cut_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.sf_vh2j_shape.root'] }
                    } ,

  # ============ VH -> WW 2j DF shape-based ================== 
  'hwwvh2jof_30ifb' : {
                    '13TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'hwwof_vh2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape_mll.root'] }
                    } ,
  # ============ ZH -> WW 3l 2j shape-based ================
  'zh3l2j_eee_30ifb': {
                    '13TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'zh3l2j_shape_eee_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_8TeV.root'] } ,
                    } ,
  'zh3l2j_eem_30ifb': {
                    '13TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  ,
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'zh3l2j_shape_eem_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_8TeV.root'] } ,
                    } ,
  'zh3l2j_emm_30ifb': {
                    '13TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'zh3l2j_shape_emm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_8TeV.root'] } ,
                    } ,
  'zh3l2j_mmm_30ifb': {
                    '13TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '30ifb' , 'card' : 'zh3l2j_shape_mmm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_8TeV.root'] } ,
                    } ,


# =========== 13 TeV Projection @ 120 fb-1 ====================== 

  # ============ H -> WW 0/1-jet SF cut-based ================== 
  'hww0jsf_120ifb' : { 
                    '13TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwsf_0j_cut_8TeV.txt'} ,  
                    } ,
  'hww1jsf_120ifb' : {
                    '13TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwsf_1j_cut_8TeV.txt'} ,
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_120ifb' : {
                    '13TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_120ifb'  : {
                    '13TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,600]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } , 
  # ============ H -> WW VBF SF Cut Based =====================
  'hww2jsf_120ifb' :   {
                    '13TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 13 , 'method' : 'cut'  , 'mrange' : [110,600] , 
                                'dir' : '13TeV'   ,  'subdir' : '120ifb' , 'card' : 'hwwsf_2j_cut_8TeV.txt'},
                    } ,
  # ============ H -> WW VBF OF Shape Based =====================
  'hww2jof_120ifb' : {
                    '13TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 13 , 'method' : 'shape'  , 'mrange' : [110,600] ,
                                'dir' : '13TeV'   ,  'subdir' : '120ifb' , 'card' : 'hwwof_2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_2j_shape.root'] },
                    } ,

  # ============ VH -> WW 3l shape-based ==================
  'vh3l_sssf_120ifb' :  {
                    '13TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200] , 
                                'dir' : '13TeV' , 'subdir' : '120ifb', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_120ifb' : {
                    '13TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200] , 
                                'dir' : '13TeV' , 'subdir' : '120ifb', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
                    } ,

  # ============ VH -> WW 2j SF cut-based ==================
  'hwwvh2jsf_120ifb' : {
                    '13TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 13 , 'method' : 'cut' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwsf_vh2j_cut_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.sf_vh2j_shape.root'] }
                    } ,

  # ============ VH -> WW 2j DF shape-based ================== 
  'hwwvh2jof_120ifb' : {
                    '13TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'hwwof_vh2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape_mll.root'] }
                    } ,
  # ============ ZH -> WW 3l 2j shape-based ================
  'zh3l2j_eee_120ifb': {
                    '13TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'zh3l2j_shape_eee_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_8TeV.root'] } ,
                    } ,
  'zh3l2j_eem_120ifb': {
                    '13TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  ,
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'zh3l2j_shape_eem_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_8TeV.root'] } ,
                    } ,
  'zh3l2j_emm_120ifb': {
                    '13TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'zh3l2j_shape_emm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_8TeV.root'] } ,
                    } ,
  'zh3l2j_mmm_120ifb': {
                    '13TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 13 , 'method' : 'shape' , 'mrange' : [110,200]  , 
                                'dir' : '13TeV' , 'subdir' : '120ifb' , 'card' : 'zh3l2j_shape_mmm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_8TeV.root'] } ,
                    } ,

},


# ============ V2: Cards for HWW Paper (datacrds from comb svn) ==========================

'V8' : {


  # ============ H --> WW 0/1-jet JCP=0m ===================
  'hww0jof_jcp0m_0pInj': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v_0pInj' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v_0pInj' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp0m_0pInj': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v_0pInj' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v_0pInj' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } ,
#


  # ============ H --> WW 0/1-jet JCP=0m ===================
  'hww0jof_jcp0m': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp0m': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '0m/hww2l2v' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } ,
#


  # ============ H --> WW 0/1-jet JCP=2+m ===================
  'hww0jof_jcp2pm': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '2+m/hww2l2v' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '2+m/hww2l2v' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp2pm': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '2+m/hww2l2v' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '2+m/hww2l2v' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } , 
  # ============ H -> WW 0/1-jet cut-based ================== 
  'hww0jof_cut' :   { 
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_8TeV.txt'} ,  
                    } ,
  'hww1jof_cut' :   {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_8TeV.txt'} ,
                    } ,
  'hww0jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_8TeV.txt'} ,
                    } ,
  'hww1jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_8TeV.txt'} ,
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_shape' : {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_shape'  : {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } , 
  
  # ============ H -> WW VBF Cut Based =====================
  'hww2jof_cut' :   {
                    '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_2j_cut_7TeV.txt'},
                    '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_2j_cut_8TeV.txt'},
                    } ,
  'hww2jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_2j_cut_7TeV.txt'},
                    '8TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_2j_cut_8TeV.txt'},
                    } ,

  # ============ H -> WW VBF Shape Based =====================
  'hww2jof_shape' : {
                    '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'shape'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_2j_shape_7TeV.txt' , 'files' : ['shapes/hww-4.92fb.mH$MASS.of_2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'shape'  , 'mrange' : [110,600] , 'dir' : 'summer2013'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_2j_shape.root'] },
                    } ,

  # ============ VH -> WW 3l cut-based ==================
  'vh3l_sssf_cut' :  {
                    '7TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 7 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_cut_7TeV.txt' } ,  
                    '8TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 8 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_cut_8TeV.txt' } ,
                    } ,
  'vh3l_ossf_cut' :  {
                    '7TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 7 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_cut_7TeV.txt' } ,  
                    '8TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 8 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_cut_8TeV.txt' } ,
                    } ,

  # ============ VH -> WW 3l shape-based ==================
  'vh3l_sssf_shape' :  {
                    '7TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_7TeV.txt' , 'files' : ['vh3l1_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : '3l1'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_shape' : {
                    '7TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_7TeV.txt' , 'files' : ['vh3l2_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : '3l2'   , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
                    } ,
 
  # ============ VH -> WW 2j cut-based ==================
  'hwwvh2jsf_cut' : {
                    '7TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwsf_vh2j_cut_7TeV.txt' , 'files' : ['shapes/hww-4.92fb.mH$MASS.sf_vh2j_shape.root']  },
                    '8TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwsf_vh2j_cut_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.sf_vh2j_shape.root'] }
                    } ,
  'hwwvh2jof_cut' : {
                    '7TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwof_vh2j_cut_7TeV.txt' , 'files' : ['shapes/hww-4.92fb.mH$MASS.of_vh2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwof_vh2j_cut_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape.root'] }
                    } ,

  # ============ VH -> WW 2j shape-based ================== ( 7TeV -> cut-based )
  'hwwvh2jof_shape' : {
                    '7TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,190]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwof_vh2j_cut_7TeV.txt'   , 'files' : ['shapes/hww-4.92fb.mH$MASS.of_vh2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '2l2nu2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'hwwof_vh2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape_mll.root'] }
                    } ,

  # ============ ZH -> WW 3l 2j cut-based ================
  'zh3l2j_eee_cut'  : {
                    '7TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_eee_7TeV.txt' } ,
                    '8TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_eee_8TeV.txt' } ,
                    } ,
  'zh3l2j_eem_cut'  : {
                    '7TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_eem_7TeV.txt' } ,
                    '8TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_eem_8TeV.txt' } ,
                    } ,
  'zh3l2j_emm_cut'  : {
                    '7TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_emm_7TeV.txt' } ,
                    '8TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_emm_8TeV.txt' } ,
                    } ,
  'zh3l2j_mmm_cut'  : {
                    '7TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_mmm_7TeV.txt' } ,
                    '8TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_cut_mmm_8TeV.txt' } ,
                    } ,


  # ============ ZH -> WW 3l 2j cut-based ================
  'zh3l2j_eee_shape': {
                    '7TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_eee_7TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_7TeV.root'] } ,
                    '8TeV' : { 'tag' : '3l2jeee', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_eee_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_8TeV.root'] } ,
                    } ,
  'zh3l2j_eem_shape': {
                    '7TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_eem_7TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_7TeV.root'] } ,
                    '8TeV' : { 'tag' : '3l2jeem', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_eem_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_8TeV.root'] } ,
                    } ,
  'zh3l2j_emm_shape': {
                    '7TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_emm_7TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_7TeV.root'] } ,
                    '8TeV' : { 'tag' : '3l2jemm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_emm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_8TeV.root'] } ,
                    } ,
  'zh3l2j_mmm_shape': {
                    '7TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_mmm_7TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_7TeV.root'] } ,
                    '8TeV' : { 'tag' : '3l2jmmm', 'prod' : 'VH' , 'branch' : 'vhww' , 'decay' : '3l2j'   , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS' , 'card' : 'zh3l2j_shape_mmm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_8TeV.root'] } ,
                    } ,

},



# ============ V1: Cards for HWW Paper (local datacards) ==========================

'V1' : {
  # ============ H -> WW 0/1-jet cut-based ================== 
  'hww0jof_cut' :   { 
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_0j_cut_8TeV.txt'} ,  
                    } ,
  'hww1jof_cut' :   {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_1j_cut_8TeV.txt'} ,
                    } ,
  'hww0jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_0j_cut_8TeV.txt'} ,
                    } ,
  'hww1jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_1j_cut_8TeV.txt'} ,
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_shape' : {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_0j_shape_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_shape'  : {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_1j_shape_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } , 
  
  # ============ H -> WW VBF Cut Based =====================
  'hww2jof_cut' :   {
                    '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwof_2j_cut_7TeV.txt'},
                    '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwof_2j_cut_8TeV.txt'},
                    } ,
  'hww2jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwsf_2j_cut_7TeV.txt'},
                    '8TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwsf_2j_cut_8TeV.txt'},
                    } ,

  # ============ H -> WW VBF Shape Based =====================
  'hww2jof_shape' : {
                    '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'shape'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwof_2j_shape_7TeV.txt' , 'files' : ['shapes/hww-4.92fb.mH$MASS.of_2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'shape'  , 'mrange' : [110,600] , 'dir' : 'HWWPaper2013'   ,  'subdir' : '$MASS' , 'card' : 'hwwof_2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_2j_shape.root'] },
                    } ,

  # ============ VH -> WW 3l cut-based ==================
  'vh3l_sssf_cut' :  {
                    '7TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l1_cut_7TeV.txt' } ,  
                    '8TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l1_cut_8TeV.txt' } ,
                    } ,
  'vh3l_ossf_cut' :  {
                    '7TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l2_cut_7TeV.txt' } ,  
                    '8TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'cut'   , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l2_cut_8TeV.txt' } ,
                    } ,

  # ============ VH -> WW 3l shape-based ==================
  'vh3l_sssf_shape' :  {
                    '7TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l1_shape_7TeV.txt' , 'files' : ['vh3l1_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_shape' : {
                    '7TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l2_shape_7TeV.txt' , 'files' : ['vh3l2_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
                    } ,
 
  # ============ VH -> WW 2j cut-based ==================
  'hwwvh2jsf_cut' : {
                    '7TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_vh2j_cut_7TeV.txt' , 'files' : ['cuts/hww-4.92fb.mH$MASS.sf_vh2j_shape.root']  },
                    '8TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwsf_vh2j_cut_8TeV.txt' , 'files' : ['cuts/hww-19.47fb.mH$MASS.sf_vh2j_shape.root'] }
                    } ,
  'hwwvh2jof_cut' : {
                    '7TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_vh2j_cut_7TeV.txt' , 'files' : ['cuts/hww-4.92fb.mH$MASS.of_vh2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_vh2j_cut_8TeV.txt' , 'files' : ['cuts/hww-19.47fb.mH$MASS.of_vh2j_shape.root'] }
                    } ,

  # ============ VH -> WW 2j shape-based ================== ( 7TeV -> cut-based )
  'hwwvh2jof_shape' : {
                    '7TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,190]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_vh2j_cut_7TeV.txt'   , 'files' : ['cuts/hww-4.92fb.mH$MASS.of_vh2j_shape.root'] },
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'hwwof_vh2j_shape_8TeV.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape.root'] }
                    } ,

  # ============ ZH -> WW 3l 2j cut-based ================
  'zh3l2j_eee_cut'  : {
                    '7TeV' : { 'tag' : 'eee', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_eee_7TeV.txt' } ,
                    '8TeV' : { 'tag' : 'eee', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_eee_8TeV.txt' } ,
                    } ,
  'zh3l2j_eem_cut'  : {
                    '7TeV' : { 'tag' : 'eem', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_eem_7TeV.txt' } ,
                    '8TeV' : { 'tag' : 'eem', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_eem_8TeV.txt' } ,
                    } ,
  'zh3l2j_emm_cut'  : {
                    '7TeV' : { 'tag' : 'emm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_emm_7TeV.txt' } ,
                    '8TeV' : { 'tag' : 'emm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_emm_8TeV.txt' } ,
                    } ,
  'zh3l2j_mmm_cut'  : {
                    '7TeV' : { 'tag' : 'mmm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_mmm_7TeV.txt' } ,
                    '8TeV' : { 'tag' : 'mmm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_cut_mmm_8TeV.txt' } ,
                    } ,


  # ============ ZH -> WW 3l 2j cut-based ================
  'zh3l2j_eee_shape': {
                    '7TeV' : { 'tag' : 'eee', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_eee_7TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'eee', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_eee_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eee_8TeV.root'] } ,
                    } ,
  'zh3l2j_eem_shape': {
                    '7TeV' : { 'tag' : 'eem', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_eem_7TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'eem', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_eem_8TeV.txt' , 'files' : ['zh3l2j_input_shape_eem_8TeV.root'] } ,
                    } ,
  'zh3l2j_emm_shape': {
                    '7TeV' : { 'tag' : 'emm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_emm_7TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'emm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_emm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_emm_8TeV.root'] } ,
                    } ,
  'zh3l2j_mmm_shape': {
                    '7TeV' : { 'tag' : 'mmm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_mmm_7TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'mmm', 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'zh3l2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200]  , 'dir' : 'HWWPaper2013' , 'subdir' : '$MASS' , 'card' : 'zh3l2j_shape_mmm_8TeV.txt' , 'files' : ['zh3l2j_input_shape_mmm_8TeV.root'] } ,
                    } ,

},

# ============ V0: Test Cards from combination area =============

'V0' : {

  # ============ H -> WW 0/1-jet cut-based ================== 
  #'hww0jof_cut' :   { 
  #                  '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_8TeV.txt'}   
  #                  } ,
  #'hww1jof_cut' :   {
  #                  '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_8TeV.txt'}
  #                  } ,
  'hww0jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_8TeV.txt' }
                    } ,
  'hww1jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_8TeV.txt'}
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_shape' : {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] }
                    } ,
  'hww1jof_shape'  : {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] }
                    } , 
  # ============ H -> WW 0/1-jet Mr Fit =================
  # 'hww0jof_mrfit'  : {
  #                  '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_mrfit_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_mrfit_8TeV.txt'}
  #                } ,
  # 'hww1jof_mrfit'  : {
  #                  '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_mrfit_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013_V0' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_mrfit_8TeV.txt'}
  #                } ,
  # ============ H -> WW VBF cut-based (OLD HCP RESULT) ==================
  'hww2j_hcp' :     {
                    '7TeV' : { 'tag' : '2j'    , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'hcp2012'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hww_2j_cut_7TeV.txt'},
                    } ,  
  'hww2jof_hcp' :   {
                    '8TeV' : { 'tag' : '2jof'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'hcp2012'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_2j_cut_8TeV.txt'},
                    } ,
  'hww2jsf_hcp' :   {
                    '8TeV' : { 'tag' : '2jsf'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [110,600] , 'dir' : 'hcp2012'   ,  'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_2j_cut_8TeV.txt'},
                    } ,


  # ============ VH -> WW 3l shape-based ==================
  'vh3l_sssf_shape' :  {
                    '7TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013_V0' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_7TeV.txt' , 'files' : ['vh3l1_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013_V0' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_shape' :  {
                    '7TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013_V0' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_7TeV.txt' , 'files' : ['vh3l2_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013_V0' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
                    } ,
 
  # ============ VH -> WW 2j cut-based ==================
  'hwwvh2jsf_cut' : {
                    '7TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'vh2jPrivate/' , 'subdir' : 'vh2j/cutbase_7TeV' , 'card' : 'hww-7.TeV.mH$MASS.sf_vh_shape.txt'  },
                    '8TeV' : { 'tag' : 'sf' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,300]  , 'dir' : 'vh2jPrivate/' , 'subdir' : 'vh2j/cutbase' , 'card' : 'hww-19.47fb.mH$MASS.sf_vh2j_shape.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.sf_vh2j_shape.root'] }
                    } ,
  'hwwvh2jof_cut' : {
                    '7TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [120,190]  , 'dir' : 'vh2jPrivate/' , 'subdir' : 'vh2j/cutbase_7TeV' , 'card' : 'hww-7.TeV.mH$MASS.of_vh_shape.txt'  },
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,300]  , 'dir' : 'vh2jPrivate/' , 'subdir' : 'vh2j/cutbase' , 'card' : 'hww-19.47fb.mH$MASS.of_vh2j_shape.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape.root'] }
                    } ,
  # ============ VH -> WW 2j mll shape ==================
  'hwwvh2jof_shape' : {
                    '8TeV' : { 'tag' : 'of' , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh2j' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,300]  , 'dir' : 'vh2jPrivate/' , 'subdir' : 'vh2j/mllshape' , 'card' : 'hww-19.47fb.mH$MASS.of_vh2j_shape.txt' , 'files' : ['shapes/hww-19.47fb.mH$MASS.of_vh2j_shape.root'] }
                    } ,
 
},

}
    
combinations = {
#
# 0/1 jet separated
#
# 'hww0jsf'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut'                   ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0-jet (SF)'} ,
# 'hww0jof'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [                 'hww0jof_shape' ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys'  , 'smhiggs' , 'mass' , 'masssminj' ] , 'legend' : 'HWW 0-jet (DF)'} ,
#
# 0+1 jet: SF and DF separated
#
  'hww01jof_shape' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [                                 'hww0jof_shape' , 'hww1jof_shape' ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' , 'mass' , 'masssminj' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (DF)'  } ,
  'hww01jsf_shape' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut'                                     ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (SF)'  } ,
#
#
# Single channel (as in PASes/ paper section)
#
  'hww0jet_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_shape' ] ,                                   
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0-jet (2d)'    } ,
  'hww0jet_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_cut'   ] ,                                   
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0-jet (Cut)'   } ,
  'hww1jet_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww1jsf_cut' , 'hww1jof_shape' ] ,                                   
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 1-jet (2d)'    } ,
  'hww1jet_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww1jsf_cut' , 'hww1jof_cut'   ] ,                                   
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 1-jet (Cut)'   } ,
  'hww01jet_shape' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_shape' , 'hww1jof_shape' ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet' 
                       'legend' : '2l2#nu + 0/1-jet' 
                     } ,
  'hww01jet_cut'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_cut'   , 'hww1jof_cut'   ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'WW 0/1-jet (Cut)' } ,
  'hww2j_hcp'      : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2j_hcp' , 'hww2jsf_hcp' , 'hww2jof_hcp' ] ,                       
                       'purposes' : [ 'searches' , 'couplings' ] , 'legend' : 'HWW 2j (HCP)' } ,
  'hww2j_cut'      : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jof_cut' , 'hww2jsf_cut' ]  ,                                  
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VBF H #rightarrow WW #rightarrow 2l2#nu (Cut)' }, 
  'hww2j_shape'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jof_shape' , 'hww2jsf_cut' ]  ,                                 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'VBF H #rightarrow WW #rightarrow 2l2#nu'
                       'legend' : '2l2#nu + 2-jets, VBF tag'
                     },  
  'hww2jof_shape'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jof_shape' ]  ,                                 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'VBF H #rightarrow WW #rightarrow 2l2#nu'
                       'legend' : '2l2#nu + 2-jets, VBF tag'
                     },  

  'hww2jsf_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jsf_cut' ]  ,                                 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'VBF H #rightarrow WW #rightarrow 2l2#nu'
                       'legend' : '2l2#nu + 2-jets, VBF tag'
                     },  



  'vh3l_cut'       : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'vh3l_sssf_cut'    , 'vh3l_ossf_cut'    ] ,                           
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 3l (Cut)'     } ,
  'vh3l_shape'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'vh3l_sssf_shape'  , 'vh3l_ossf_shape'  ] ,                          
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'WH #rightarrow 3l3#nu'  
                       'legend' : '3l3#nu, WH tag'  
                     } ,
  'hwwvh2j_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ] ,                               
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'VH #rightarrow 2q2l2#nu'  
                       'legend' : '2l2#nu + 2-jets, VH tag'  
                     } ,
  'hwwvh2j_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hwwvh2jsf_shape' , 'hwwvh2jof_shape' ] ,                            
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 2-jet (Shape)'} ,
  'zh3l2j_cut'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'zh3l2j_eee_cut'  , 'zh3l2j_eem_cut'  , 'zh3l2j_emm_cut'  , 'zh3l2j_mmm_cut'   ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'ZHWW 3l2j (Cut)'  } ,
  'zh3l2j_shape'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'zh3l2j_eee_shape', 'zh3l2j_eem_shape', 'zh3l2j_emm_shape', 'zh3l2j_mmm_shape' ] ,
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       #'legend' : 'ZH #rightarrow ZWW #rightarrow 3l2q#nu'
                       'legend' : '3l#nu + 2-jets, ZH tag'
                     } ,
#
# All VH
#

  'hww_vh3l_vh2j_zh3l2j_cut' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'vh3l_sssf_cut'  , 'vh3l_ossf_cut' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ,
                                         'zh3l2j_eee_cut', 'zh3l2j_eem_cut', 'zh3l2j_emm_cut', 'zh3l2j_mmm_cut' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : '0/1/2-jet + VH3l + VH2j + ZH3l2j (Cut)'
                        } ,


  'hww_vh3l_vh2j_zh3l2j_shape' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ,
                                         'zh3l2j_eee_shape', 'zh3l2j_eem_shape', 'zh3l2j_emm_shape', 'zh3l2j_mmm_shape' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          #'legend'   : '0/1/2-jet + VH3l + VH2j + ZH3l2j (Shape)'
                          'legend'   : 'VH #rightarrow VWW #rightarrow 2l2#nuqq/3l(3#nu)(#nu qq)'
                        } ,

#
# JCP
#
  'hww01jet_jcp0m' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp0m' ,  'hww1jof_jcp0m'  ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,
  'hww01jet_jcp0m_0pInj' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp0m_0pInj' ,  'hww1jof_jcp0m_0pInj'  ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,
  'hww01jet_jcp2pm': { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp2pm' , 'hww1jof_jcp2pm' ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,
#
# Combination of channels (old Moriond)
#
#  'hww_01jet_2jhcp_vh3l_vh2j' :  { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_shape' , 'hww1jsf_cut' , 'hww1jof_shape' , 'hww2j_hcp' , 'hww2jsf_hcp' , 'hww2jof_hcp' , 'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ] , 'purposes' : [ 'searches' , 'couplings' ] , 'legend' : '0/1-jet + 2j (HCP) + VH3l + VH2j'} ,
#
#  'hww_01jet_vh3l_vh2j' :  { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_shape' , 'hww1jsf_cut' , 'hww1jof_shape' , 'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ] , 'purposes' : [ 'searches' , 'couplings' ] , 'legend' : '0/1-jet + VH3l + VH2j'} ,


#
# Combination of channels (Paper)
#
  'hww012j_vh3l_vh2j_cut' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_cut' , 'hww1jof_cut' , 
                                         'hww2jof_cut' , 'hww2jsf_cut' , 
                                         'vh3l_sssf_cut'  , 'vh3l_ossf_cut' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : '0/1/2-jet + VH3l + VH2j (Cut)'
                        } ,
                                 
  'hww012j_vh3l_vh2j_shape' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_shape' , 'hww1jof_shape' , 
                                         'hww2jof_shape' , 'hww2jsf_cut' , 
                                         'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : '0/1/2-jet + VH3l + VH2j (Shape)'
                        } ,

  'hww012j_vh3l_vh2j_zh3l2j_cut' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_cut' , 'hww1jof_cut' , 
                                         'hww2jof_cut' , 'hww2jsf_cut' , 
                                         'vh3l_sssf_cut'  , 'vh3l_ossf_cut' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ,
                                         'zh3l2j_eee_cut', 'zh3l2j_eem_cut', 'zh3l2j_emm_cut', 'zh3l2j_mmm_cut' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : '0/1/2-jet + VH3l + VH2j + ZH3l2j (Cut)'
                        } ,

  'hww012j_vh3l_vh2j_zh3l2j_shape' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_shape' , 'hww1jof_shape' , 
                                         'hww2jof_shape' , 'hww2jsf_cut' , 
                                         'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ,
                                         'zh3l2j_eee_shape', 'zh3l2j_eem_shape', 'zh3l2j_emm_shape', 'zh3l2j_mmm_shape' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          #'legend'   : '0/1/2-jet + VH3l + VH2j + ZH3l2j (Shape)'
                          #'legend'   : '(V)H #rightarrow (V)WW #rightarrow 2l/3l'
                          'legend'   : 'H #rightarrow WW (all channels)'
                        } ,

  'hww012j_vh3l_vh2j_zh3l2j_marco' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] , 
                          'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_shape' , 'hww1jof_shape' , 
                                         'hww2jof_shape' , 'hww2jsf_cut' , 
                                         'vh3l_sssf_shape'  , 'vh3l_ossf_shape' , 
                                         'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ,
                                         'zh3l2j_eee_shape', 'zh3l2j_eem_shape', 'zh3l2j_emm_shape', 'zh3l2j_mmm_shape' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          #'legend'   : '0/1/2-jet + VH3l + VH2j + ZH3l2j (Shape)'
                          'legend'   : '(V)H #rightarrow (V)WW #rightarrow 2l/3l'
                        } ,

#
# 13 TeV Projection, 30 fb-1
#

  'hww01jet_30ifb' : { 'energies' : [ '13TeV' ] , 'channels' : [ 'hww0jsf_30ifb' , 'hww1jsf_30ifb' , 'hww0jof_30ifb' , 'hww1jof_30ifb' ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 0/1-jet' 
                     } ,


  'hww2j_30ifb'    : { 'energies' : [ '13TeV' ] , 'channels' : [ 'hww2jof_30ifb' , 'hww2jsf_30ifb' ]  ,                                 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 2-jets, VBF tag'
                     }, 

  'vh3l_30ifb'     : { 'energies' : [ '13TeV' ] , 'channels' : [ 'vh3l_sssf_30ifb'  , 'vh3l_ossf_30ifb'  ] ,                          
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '3l3#nu, WH tag'  
                     } ,

  'hwwvh2j_30ifb'  : { 'energies' : [ '13TeV' ] , 'channels' : [ 'hwwvh2jsf_30ifb' , 'hwwvh2jof_30ifb' ] ,                               
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 2-jets, VH tag'  
                     } ,

  'zh3l2j_30ifb'   : { 'energies' : [ '13TeV' ] , 'channels' : [ 'zh3l2j_eee_30ifb', 'zh3l2j_eem_30ifb', 'zh3l2j_emm_30ifb', 'zh3l2j_mmm_30ifb' ] ,
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '3l#nu + 2-jets, ZH tag'
                     } ,

  'hww_vh3l_vh2j_zh3l2j_30ifb' :
                        {
                          'energies' : [ '13TeV' ] , 
                          'channels' : [ 'vh3l_sssf_30ifb'  , 'vh3l_ossf_30ifb' , 
                                         'hwwvh2jsf_30ifb' , 'hwwvh2jof_30ifb' ,
                                         'zh3l2j_eee_30ifb', 'zh3l2j_eem_30ifb', 'zh3l2j_emm_30ifb', 'zh3l2j_mmm_30ifb' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'H #rightarrow WW (all channels)'
                        } ,
 

  'hww012j_vh3l_vh2j_zh3l2j_30ifb' :
                        {
                          'energies' : [ '13TeV' ] , 
                          'channels' : [ 'hww0jsf_30ifb' , 'hww1jsf_30ifb' , 'hww0jof_30ifb' , 'hww1jof_30ifb' , 
                                         'hww2jof_30ifb' , 'hww2jsf_30ifb' , 
                                         'vh3l_sssf_30ifb'  , 'vh3l_ossf_30ifb' , 
                                         'hwwvh2jsf_30ifb' , 'hwwvh2jof_30ifb' ,
                                         'zh3l2j_eee_30ifb', 'zh3l2j_eem_30ifb', 'zh3l2j_emm_30ifb', 'zh3l2j_mmm_30ifb' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'H #rightarrow WW (all channels)'
                        } ,

#
# 13 TeV Projection, 120 fb-1
#

  'hww01jet_120ifb': { 'energies' : [ '13TeV' ] , 'channels' : [ 'hww0jsf_120ifb' , 'hww1jsf_120ifb' , 'hww0jof_120ifb' , 'hww1jof_120ifb' ] , 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 0/1-jet' 
                     } ,


  'hww2j_120ifb'   : { 'energies' : [ '13TeV' ] , 'channels' : [ 'hww2jof_120ifb' , 'hww2jsf_120ifb' ]  ,                                 
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 2-jets, VBF tag'
                     }, 

  'vh3l_120ifb'    : { 'energies' : [ '13TeV' ] , 'channels' : [ 'vh3l_sssf_120ifb'  , 'vh3l_ossf_120ifb'  ] ,                          
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '3l3#nu, WH tag'  
                     } ,

  'hwwvh2j_120ifb' : { 'energies' : [ '13TeV' ] , 'channels' : [ 'hwwvh2jsf_120ifb' , 'hwwvh2jof_120ifb' ] ,                               
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '2l2#nu + 2-jets, VH tag'  
                     } ,

  'zh3l2j_120ifb'  : { 'energies' : [ '13TeV' ] , 'channels' : [ 'zh3l2j_eee_120ifb', 'zh3l2j_eem_120ifb', 'zh3l2j_emm_120ifb', 'zh3l2j_mmm_120ifb' ] ,
                       'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 
                       'legend' : '3l#nu + 2-jets, ZH tag'
                     } ,

  'hww_vh3l_vh2j_zh3l2j_120ifb' :
                        {
                          'energies' : [ '13TeV' ] , 
                          'channels' : [ 'vh3l_sssf_120ifb'  , 'vh3l_ossf_120ifb' , 
                                         'hwwvh2jsf_120ifb' , 'hwwvh2jof_120ifb' ,
                                         'zh3l2j_eee_120ifb', 'zh3l2j_eem_120ifb', 'zh3l2j_emm_120ifb', 'zh3l2j_mmm_120ifb' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'H #rightarrow WW (all channels)'
                        } ,


  'hww012j_vh3l_vh2j_zh3l2j_120ifb' :
                        {
                          'energies' : [ '13TeV' ] , 
                          'channels' : [ 'hww0jsf_120ifb' , 'hww1jsf_120ifb' , 'hww0jof_120ifb' , 'hww1jof_120ifb' , 
                                         'hww2jof_120ifb' , 'hww2jsf_120ifb' , 
                                         'vh3l_sssf_120ifb'  , 'vh3l_ossf_120ifb' , 
                                         'hwwvh2jsf_120ifb' , 'hwwvh2jof_120ifb' ,
                                         'zh3l2j_eee_120ifb', 'zh3l2j_eem_120ifb', 'zh3l2j_emm_120ifb', 'zh3l2j_mmm_120ifb' 
                                       ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,  
                          'legend'   : 'H #rightarrow WW (all channels)'
                        } ,

#
# EWKSinglet
#



  'of_oldcps' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'of0j_oldcps' , 'of1j_oldcps'
                                       ] ,
                          'purposes' : [ 'ewksinglet' ] ,
                          'legend'   : 'H #rightarrow WW (DF 0/1-jet), Old CPS'
                        } ,

  'of_newcps' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'of0j_newcps' , 'of1j_newcps'
                                       ] ,
                          'purposes' : [ 'ewksinglet' ] ,
                          'legend'   : 'H #rightarrow WW (DF 0/1-jet), SM'
                        } ,

  'of_smbkgd' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'of0j_smbkgd' , 'of1j_smbkgd'
                                       ] ,
                          'purposes' : [ 'ewksinglet' ] ,
                          'legend'   : 'H #rightarrow WW (DF 0/1-jet) + 125 GeV'
                        } ,


  'of_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_1d0' , 'of1j_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'of_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d9' , 'of1j_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'of_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d8' , 'of1j_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'of_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d7' , 'of1j_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'of_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d6' , 'of1j_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'of_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d5' , 'of1j_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'of_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d4' , 'of1j_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'of_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d3' , 'of1j_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'of_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d2' , 'of1j_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'of_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_0d1' , 'of1j_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,

  'of_cp2_7TeV_1d0' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_1d0' , 'of1j_cp2_7TeV_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'of_cp2_7TeV_0d9' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d9' , 'of1j_cp2_7TeV_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'of_cp2_7TeV_0d8' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d8' , 'of1j_cp2_7TeV_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'of_cp2_7TeV_0d7' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d7' , 'of1j_cp2_7TeV_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'of_cp2_7TeV_0d6' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d6' , 'of1j_cp2_7TeV_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'of_cp2_7TeV_0d5' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d5' , 'of1j_cp2_7TeV_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'of_cp2_7TeV_0d4' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d4' , 'of1j_cp2_7TeV_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'of_cp2_7TeV_0d3' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d3' , 'of1j_cp2_7TeV_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'of_cp2_7TeV_0d2' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d2' , 'of1j_cp2_7TeV_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'of_cp2_7TeV_0d1' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_cp2_7TeV_0d1' , 'of1j_cp2_7TeV_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,


  'of_cp2_app_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_1d0' , 'of1j_cp2_app_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 (Approx.)' } ,
  'of_cp2_app_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d9' , 'of1j_cp2_app_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9 (Approx.)' } ,
  'of_cp2_app_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d8' , 'of1j_cp2_app_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8 (Approx.)' } ,
  'of_cp2_app_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d7' , 'of1j_cp2_app_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7 (Approx.)' } ,
  'of_cp2_app_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d6' , 'of1j_cp2_app_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6 (Approx.)' } ,
  'of_cp2_app_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d5' , 'of1j_cp2_app_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5 (Approx.)' } ,
  'of_cp2_app_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d4' , 'of1j_cp2_app_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4 (Approx.)' } ,
  'of_cp2_app_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d3' , 'of1j_cp2_app_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3 (Approx.)' } ,
  'of_cp2_app_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d2' , 'of1j_cp2_app_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2 (Approx.)' } ,
  'of_cp2_app_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_app_0d1' , 'of1j_cp2_app_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1 (Approx.)' } ,


  'of_cp2_bwo_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_1d0' , 'of1j_cp2_bwo_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 (BW Only)' } ,
  'of_cp2_bwo_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d9' , 'of1j_cp2_bwo_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9 (BW Only)' } ,
  'of_cp2_bwo_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d8' , 'of1j_cp2_bwo_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8 (BW Only)' } ,
  'of_cp2_bwo_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d7' , 'of1j_cp2_bwo_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7 (BW Only)' } ,
  'of_cp2_bwo_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d6' , 'of1j_cp2_bwo_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6 (BW Only)' } ,
  'of_cp2_bwo_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d5' , 'of1j_cp2_bwo_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5 (BW Only)' } ,
  'of_cp2_bwo_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d4' , 'of1j_cp2_bwo_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4 (BW Only)' } ,
  'of_cp2_bwo_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d3' , 'of1j_cp2_bwo_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3 (BW Only)' } ,
  'of_cp2_bwo_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d2' , 'of1j_cp2_bwo_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2 (BW Only)' } ,
  'of_cp2_bwo_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_bwo_0d1' , 'of1j_cp2_bwo_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1 (BW Only)' } ,

  'of_cp2_ext_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_1d0' , 'of1j_cp2_ext_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 ' } ,
  'of_cp2_ext_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d9' , 'of1j_cp2_ext_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9 ' } ,
  'of_cp2_ext_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d8' , 'of1j_cp2_ext_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8 ' } ,
  'of_cp2_ext_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d7' , 'of1j_cp2_ext_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7 ' } ,
  'of_cp2_ext_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d6' , 'of1j_cp2_ext_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6 ' } ,
  'of_cp2_ext_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d5' , 'of1j_cp2_ext_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5 ' } ,
  'of_cp2_ext_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d4' , 'of1j_cp2_ext_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4 ' } ,
  'of_cp2_ext_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d3' , 'of1j_cp2_ext_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3 ' } ,
  'of_cp2_ext_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d2' , 'of1j_cp2_ext_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2 ' } ,
  'of_cp2_ext_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d1' , 'of1j_cp2_ext_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1 ' } ,

  'sf_cp2_ext_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_1d0' , 'sf1j_cp2_ext_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 ' } ,
  'sf_cp2_ext_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d9' , 'sf1j_cp2_ext_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9 ' } ,
  'sf_cp2_ext_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d8' , 'sf1j_cp2_ext_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8 ' } ,
  'sf_cp2_ext_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d7' , 'sf1j_cp2_ext_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7 ' } ,
  'sf_cp2_ext_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d6' , 'sf1j_cp2_ext_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6 ' } ,
  'sf_cp2_ext_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d5' , 'sf1j_cp2_ext_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5 ' } ,
  'sf_cp2_ext_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d4' , 'sf1j_cp2_ext_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4 ' } ,
  'sf_cp2_ext_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d3' , 'sf1j_cp2_ext_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3 ' } ,
  'sf_cp2_ext_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d2' , 'sf1j_cp2_ext_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2 ' } ,
  'sf_cp2_ext_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d1' , 'sf1j_cp2_ext_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1 ' } ,


  'of_cp2_ovf_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_1d0' , 'of1j_cp2_ovf_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,
  'of_cp2_ovf_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d9' , 'of1j_cp2_ovf_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9 Ovf' } ,
  'of_cp2_ovf_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d8' , 'of1j_cp2_ovf_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8 Ovf' } ,
  'of_cp2_ovf_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d7' , 'of1j_cp2_ovf_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7 Ovf' } ,
  'of_cp2_ovf_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d6' , 'of1j_cp2_ovf_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6 Ovf' } ,
  'of_cp2_ovf_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d5' , 'of1j_cp2_ovf_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5 Ovf' } ,
  'of_cp2_ovf_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d4' , 'of1j_cp2_ovf_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4 Ovf' } ,
  'of_cp2_ovf_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d3' , 'of1j_cp2_ovf_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3 Ovf' } ,
  'of_cp2_ovf_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d2' , 'of1j_cp2_ovf_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2 Ovf' } ,
  'of_cp2_ovf_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ovf_0d1' , 'of1j_cp2_ovf_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1 Ovf' } ,

  'of_cp2_lom_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_lom_1d0' , 'of1j_cp2_lom_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,

  'of_inj_lom' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_inj_lom' , 'of1j_inj_lom' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,
  'of_inj_ext' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_inj_ext' , 'of1j_inj_ext' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,
  'of_inj_lom_pt30' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_inj_lom_pt30' , 'of1j_inj_lom_pt30' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,
  'of_inj_lom_pt30_mth80' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_inj_lom_pt30_mth80' , 'of1j_inj_lom_pt30_mth80' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0 Ovf' } ,



   'of0j_sm_7TeV' :  { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_sm_7TeV' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'SM' } ,
   'of1j_sm_7TeV' :  { 'energies' : [ '7TeV' ] , 'channels' : [ 'of1j_sm_7TeV' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'SM' } ,
   'of_sm_7TeV' :  { 'energies' : [ '7TeV' ] , 'channels' : [ 'of0j_sm_7TeV' , 'of1j_sm_7TeV' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'SM' } ,



  'vbfof_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'vbfof_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'vbfof_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'vbfof_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'vbfof_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'vbfof_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'vbfof_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'vbfof_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'vbfof_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'vbfof_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,

  'vbfof_cp2_7TeV_1d0' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'vbfof_cp2_7TeV_0d9' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'vbfof_cp2_7TeV_0d8' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'vbfof_cp2_7TeV_0d7' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'vbfof_cp2_7TeV_0d6' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'vbfof_cp2_7TeV_0d5' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'vbfof_cp2_7TeV_0d4' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'vbfof_cp2_7TeV_0d3' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'vbfof_cp2_7TeV_0d2' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'vbfof_cp2_7TeV_0d1' : { 'energies' : [ '7TeV' ] , 'channels' : [ 'of2j_cp2_7TeV_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,


  'vbfofnew_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'vbfofnew_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'vbfofnew_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'vbfofnew_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'vbfofnew_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'vbfofnew_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'vbfofnew_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'vbfofnew_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'vbfofnew_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'vbfofnew_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2jnew_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,

  'vbfsf_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'vbfsf_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'vbfsf_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'vbfsf_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'vbfsf_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'vbfsf_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'vbfsf_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'vbfsf_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'vbfsf_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'vbfsf_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,


  'vbfof_paper' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of2j_paper' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'vbfsf_paper' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf2j_paper' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,



  'hwwof_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_1d0' , 'of1j_cp2_ext_1d0' , 'of2jnew_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'hwwof_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d9' , 'of1j_cp2_ext_0d9' , 'of2jnew_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'hwwof_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d8' , 'of1j_cp2_ext_0d8' , 'of2jnew_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'hwwof_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d7' , 'of1j_cp2_ext_0d7' , 'of2jnew_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'hwwof_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d6' , 'of1j_cp2_ext_0d6' , 'of2jnew_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'hwwof_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d5' , 'of1j_cp2_ext_0d5' , 'of2jnew_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'hwwof_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d4' , 'of1j_cp2_ext_0d4' , 'of2jnew_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'hwwof_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d3' , 'of1j_cp2_ext_0d3' , 'of2jnew_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'hwwof_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d2' , 'of1j_cp2_ext_0d2' , 'of2jnew_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'hwwof_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d1' , 'of1j_cp2_ext_0d1' , 'of2jnew_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,

  'hwwsf_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_1d0' , 'sf1j_cp2_ext_1d0' , 'sf2j_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'hwwsf_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d9' , 'sf1j_cp2_ext_0d9' , 'sf2j_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'hwwsf_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d8' , 'sf1j_cp2_ext_0d8' , 'sf2j_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'hwwsf_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d7' , 'sf1j_cp2_ext_0d7' , 'sf2j_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'hwwsf_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d6' , 'sf1j_cp2_ext_0d6' , 'sf2j_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'hwwsf_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d5' , 'sf1j_cp2_ext_0d5' , 'sf2j_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'hwwsf_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d4' , 'sf1j_cp2_ext_0d4' , 'sf2j_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'hwwsf_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d3' , 'sf1j_cp2_ext_0d3' , 'sf2j_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'hwwsf_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d2' , 'sf1j_cp2_ext_0d2' , 'sf2j_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'hwwsf_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'sf0j_cp2_ext_0d1' , 'sf1j_cp2_ext_0d1' , 'sf2j_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,

  'hww_cp2_1d0' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_1d0' , 'of1j_cp2_ext_1d0' , 'of2jnew_cp2_1d0' , 'sf0j_cp2_ext_1d0' , 'sf1j_cp2_ext_1d0' , 'sf2j_cp2_1d0' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=1.0' } ,
  'hww_cp2_0d9' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d9' , 'of1j_cp2_ext_0d9' , 'of2jnew_cp2_0d9' , 'sf0j_cp2_ext_0d9' , 'sf1j_cp2_ext_0d9' , 'sf2j_cp2_0d9' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.9' } ,
  'hww_cp2_0d8' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d8' , 'of1j_cp2_ext_0d8' , 'of2jnew_cp2_0d8' , 'sf0j_cp2_ext_0d8' , 'sf1j_cp2_ext_0d8' , 'sf2j_cp2_0d8' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.8' } ,
  'hww_cp2_0d7' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d7' , 'of1j_cp2_ext_0d7' , 'of2jnew_cp2_0d7' , 'sf0j_cp2_ext_0d7' , 'sf1j_cp2_ext_0d7' , 'sf2j_cp2_0d7' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.7' } ,
  'hww_cp2_0d6' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d6' , 'of1j_cp2_ext_0d6' , 'of2jnew_cp2_0d6' , 'sf0j_cp2_ext_0d6' , 'sf1j_cp2_ext_0d6' , 'sf2j_cp2_0d6' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.6' } ,
  'hww_cp2_0d5' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d5' , 'of1j_cp2_ext_0d5' , 'of2jnew_cp2_0d5' , 'sf0j_cp2_ext_0d5' , 'sf1j_cp2_ext_0d5' , 'sf2j_cp2_0d5' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.5' } ,
  'hww_cp2_0d4' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d4' , 'of1j_cp2_ext_0d4' , 'of2jnew_cp2_0d4' , 'sf0j_cp2_ext_0d4' , 'sf1j_cp2_ext_0d4' , 'sf2j_cp2_0d4' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.4' } ,
  'hww_cp2_0d3' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d3' , 'of1j_cp2_ext_0d3' , 'of2jnew_cp2_0d3' , 'sf0j_cp2_ext_0d3' , 'sf1j_cp2_ext_0d3' , 'sf2j_cp2_0d3' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.3' } ,
  'hww_cp2_0d2' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d2' , 'of1j_cp2_ext_0d2' , 'of2jnew_cp2_0d2' , 'sf0j_cp2_ext_0d2' , 'sf1j_cp2_ext_0d2' , 'sf2j_cp2_0d2' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.2' } ,
  'hww_cp2_0d1' : { 'energies' : [ '8TeV' ] , 'channels' : [ 'of0j_cp2_ext_0d1' , 'of1j_cp2_ext_0d1' , 'of2jnew_cp2_0d1' , 'sf0j_cp2_ext_0d1' , 'sf1j_cp2_ext_0d1' , 'sf2j_cp2_0d1' ] , 'purposes' : [ 'ewksinglet' ] , 'legend'   : 'C\'^{2}=0.1' } ,



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

   'vbfbbbias' :
                        {
                          'energies' : [ '8TeV' ] , 
                          'channels' : [ 'vbfbbsplit_bias' ] ,
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

physmodels = {
  'SMValid'  : { 'model' : 'HiggsAnalysis.CombinedLimit.PhysicsModel:strictSMLikeHiggs' , 'cardtype' : 'smhiggs' } ,
  'NoModel'  : { 'cardtype' : 'couplings' } ,
  'EWKSinglet':{ 'cardtype' : 'ewksinglet' } ,
  '125dot6'  : { 'cardtype' : 'couplings' } ,
  '125dot7'  : { 'cardtype' : 'couplings2' } ,
  'SMHiggs'  : { 'cardtype' : 'smhiggs'   } ,
  'MH125BG'  : { 'cardtype' : 'searches'  } ,
#
  'OneHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:justOneHiggs'            , 'cardtype' : 'searches' } ,
  'TwoHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:twoHiggsUnconstrained'   , 'cardtype' : 'searches' } ,
#
  'SMInject' : { 'cardtype' : 'sminject' } ,
  'SMToys'   : { 'cardtype' : 'smtoys' } ,
#
# Couplings
#
  'rVrFXSH'  : { 'model' : 'HiggsAnalysis.CombinedLimit.PhysicsModel:rVrFXSHiggs' , 'cardtype' : 'couplings' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['RV','RF'] , 'AxisTitle' : ['#mu_{VBF,VH}','#mu_{ggH}'] , 
                               #'Min' : [-2.,-2.] , 'Max' : [4.,4.] ,  'MinPlt' : [0.,0.] , 'MaxPlt' : [2.5,2.5]  } } ,
                               'Min' : [-2.,-2.] , 'Max' : [4.,4.] ,  'MinPlt' : [-2.,-2.] , 'MaxPlt' : [4.,4.]  } } ,
  'cVcF'     : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsCouplings:cVcF'      , 'cardtype' : 'couplings' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['CV','CF'] , 'AxisTitle' : ['#kappa_{V}','#kappa_{f}'] , 'Min' : [0.,-2.] , 'Max' : [2.,2.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.5,2.]  }  } ,
                 #'MDFTree' : { 'NDim' : 2 , 'Keys' : ['CV','CF'] , 'AxisTitle' : ['#kappa_{V}','#kappa_{f}'] , 'Min' : [0.,-2.] , 'Max' : [2.,2.] , 'MinPlt' : [0.66,1.52] , 'MaxPlt' : [.68,1.56]  }  } ,
#
# mu(ggH,VBF,VH) 
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
# mu(ggH,VBF)
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
# BR(Invisible)
#
  'BRInv'  : { 'model' : "HiggsAnalysis.CombinedLimit.HiggsCouplings:c7 --PO verbose" , 'cardtype' : 'couplings' ,
                 'MDFTree' : { 'TargetBase' : 'BRInv' , 'POISetKeys'  : ['BRInv'] ,   
                               'BRInv' :  { 'NDim' : 1 , 'Keys' : ['BRInvUndet'] , 'AxisTitle' : ['BR_{BSM}'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,8.]  } ,
                             } 
               }, 

# 'cVcFBRInv': { 'model' : "HiggsAnalysis.CombinedLimit.HiggsCouplings:cVcFBRInv --PO verbose" , 'cardtype' : 'couplings' ,
#                'MDFTree' : { 'TargetBase' : 'BRInv' , 'POISetKeys'  : ['BRInv'] ,   
#                              'BRInv' :  { 'NDim' : 1 , 'Keys' : ['BRInvUndet'] , 'AxisTitle' : ['BR_{BSM}'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,8.]  } ,
#                            } 
#              }, 

  'HWWInv'   : { 'model' : "HiggsAnalysis.CombinedLimit.HWWModels:HWWInv  --PO verbose" , 'cardtype' : 'couplings' ,
                 'MDFTree' : { 'TargetBase' : 'BRInv' , 'POISetKeys'  : ['BRInv'] ,   
                               'BRInv' :  { 'NDim' : 1 , 'Keys' : ['BRInvUndet'] , 'AxisTitle' : ['BR_{BSM}'] , 'Min' : [0.] , 'Max' : [1.] , 'MinPlt' : [0.,0.] , 'MaxPlt' : [1.,8.]  } ,
                             } 
               }, 

#
# Mass/mu scan from Histo cards
#
  'mHmuHist' : { 'cardtype' : 'mass' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['mh','r'] , 'AxisTitle' : ['Higgs Mass [GeV]','#mu'] , 'Min' : [110.,0.] , 'Max' : [140,3.] , 'MinPlt' : [110.,0.] , 'MaxPlt' : [140.,3.]  }  } ,
  'mHmuHistSMInj' : { 'cardtype' : 'masssminj' , 
                 'MDFTree' : { 'NDim' : 2 , 'Keys' : ['mh','r'] , 'AxisTitle' : ['Higgs Mass [GeV]','#mu'] , 'Min' : [110.,0.] , 'Max' : [140,3.] , 'MinPlt' : [110.,0.] , 'MaxPlt' : [140.,3.]  }  } ,
#
# Spin
#
  'JCP'      : { 'model' : 'HiggsAnalysis.CombinedLimit.HiggsJPC:twoHypothesisHiggs  --PO=fqqFloating' , 'cardtype' : 'jcp' } 
#  'Test'     : { 'model' : '' , 'cardtype' : 'searches' } , 
}

targets = { 
  #
  # p-value 
  #
  'PVObs'       : { 'notblind' : False , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue' , 'treeKeys' : ['Val'] } , 
  'PVExpPre'    : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue --expectSignal=1 -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov' , 'treeKeys' : ['Val'] } ,  
  'PVExpPost'   : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --pvalue --expectSignal=1 -t -1 --X-rtd TMCSO_AdaptivePseudoAsimov --toysFreq'  , 'treeKeys' : ['Val'] } ,  
  #
  # significance
  #
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
  #                                            'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} }
  #
  # Limits: Standard
  #
  'ACLsObs'      : { 'notblind' : False , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'treeKeys' : ['Val'] } ,
  'ACLsExp'      : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run expected' , 'treeKeys' : ['95D','68D','Val','68U','95U'] } ,
  'ACLsExpPost'  : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run expected -t -1 --expectSignal=0 --toysFreq' , 'treeKeys' : ['95D','68D','Val','68U','95U'] } ,
  'ACLsInjPre'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1' , 'treeKeys' : ['Val']  },
  'ACLsInjPost'  : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1 --toysFreq' , 'treeKeys' : ['Val']  },
  #
  # ACLs SM Higgs Injection
  # 
  'ACLsSMToysNoSyst'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 500 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysNoSyst50' : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 50 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysSyst'     : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysSyst' , 'NToysJob' : 500 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysSyst50'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysSyst' , 'NToysJob' : 50 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysAsimov'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysAsimov' , 'NToysJob' : -1  } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  #
  # BestFit
  #
  #'BestFitG'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 --X-rtd FITTER_DYN_STEP ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitG'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
#  'BestFitT'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --signalPdfNames=\'*ZH*,*WH*,*qqH*,*ggH*\' --backgroundPdfNames=\'*qqWW*,*ggWW*,*VV*,*Top*,*Zjets*,*Wjets*,*Wgamma*,*Wg3l*,*Ztt*\' --saveNorm --rMin=-5 --rMax=20 --robustFit=1 ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitT'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --robustFit=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  #'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-2 --rMax=4 --robustFit=1 --X-rtd FITTER_DYN_STEP -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFit'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2  --plot --rMin=-5 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitX'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-5 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --plot --rMin=-5 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001  -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] , 'AltModel' : 'Gen' },
  'BestFitExpT'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-10 -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  #
  # Toys
  # 
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
  #

  ## VBF BB Toys

  'ToysBB'       : { 'notblind' : True  , 'method' : 'GenerateOnly'     , 'options' : '-t 250  --saveToys -s -1 --expectSignal=$MUEXP' ,
                     'NJobs' : 4  ,
                     'AltModel' : 'Gen' , 
                     'FreezeNuis' : {1:['lnU','*']} ,
                     'JobsParam' : { 'MUEXP' : [0,1] }
                   },
  'MLToysBB'     : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '--expectSignal=1 --noErrors --minos none --rMin=-40 --rMax=40' , 
                     'Toys' : { 'Model' : 'SMHiggs' , 'Target' : 'ToysBB' , 'NToysJob' : 250  } ,
                     'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} ,
                     'AltModel' : 'Use' 
                   },
  'MLToysBB1Step': { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-t 250  -s -1 --expectSignal=1 --toysFrequentist --noErrors --minos none --rMin=-40 --rMax=40' ,
                     'NJobs' : 4 ,
                     'AltModel' : 'Gen' 
                     },

  'ToysBBA'      : { 'notblind' : True  , 'method' : 'GenerateOnly'     , 'options' : '-t -1 --saveToys --expectSignal=1 --rMin=-20 --rMax=20' ,
                     'NJobs' : 2  ,
                     'AltModel' : 'Gen' ,
                     'FreezeNuis' : {1:['lnU','*']} 
                   },

  'MLToysBBA'     : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '--expectSignal=1 --noErrors --minos none --rMin=-20 --rMax=20 --plot' , 
                     'Toys' : { 'Model' : 'SMHiggs' , 'Target' : 'ToysBBA' , 'NToysJob' : -1  } ,
                     'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} ,
                     'AltModel' : 'Use' 
                    },

  'MLToysBBA1Step': { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-t -1  --expectSignal=1 --noErrors --minos none --rMin=-20 --rMax=20' ,
                     'NJobs' : 1 ,
                     'AltModel' : 'Gen' 
                    },



  # MultiDim Fit
  #
  'MDF1DObs'     : {'notblind' : False , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1 --rMin=0 --rMax=3' , 'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 1000 }},
  'MDF1DExp'     : {'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v -1 -t -1 --expectSignal=1' , 'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100 }}, 
  #
  # MultiDim Fit
  #
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
  #
  # JCP
  #
  'JCP'         : {'notblind' : True  , 'method' : 'HybridNew'   , 
                      'options' : '--testStat=TEV --generateExt=1 --generateNuis=0 --fitNuis=$FITNUIS --singlePoint 1 --saveHybridResult -i 1 --clsAcc 0 --fullBToys -s -1 --setPhysicsModelParameters fqq=$FQQ --freezeNuisances fqq -T 1000' , 'NJobs' : 1 , 
                      'JobsParam' : { 'FQQ' : [0.,0.25,0.5,0.75,1.] , 'FITNUIS' : [0,1] } },
                      #'JobsParam' : { 'FQQ' : [0.0] , 'FITNUIS' : [0,1] } },

  #
  # Fit 3 Mu: ggH, VBH, VH
  #                     
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

  #
  # Fit 2 Mu: ggH, VBH
  #    
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

  #
  # BR(Invisible)
  #
  # --> Expected Fixing Others 
  'BRInvExpFix' :   { 'notblind' : True  , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P BRInvUndet --floatOtherPOI=0 -t -1 --expectSignal=1' , 
                      'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
  # --> Expectes Floating Others  
  'BRInvExp'    :   { 'notblind' : True , 'method' : 'MultiDimFit' , 'options' : '--algo=grid -v 2 -P BRInvUndet --floatOtherPOI=1 -t -1 --expectSignal=1' , 
                      'NJobs' : 1 , 'MDFGridParam' :{ 'NPOINTS' : 100} },
           
}

toys = {
  'SExp'        : { },
}

# Plot Axis range et al.
plotStyle = {

  'Limit' : 
     { 
       'Default'        : { 'linY' : [0.0 ,50.] , 'logY' : [0.01,500.] } ,
       'hww0jet_shape'  : { 'linY' : [0.0 , 5.] , 'logY' : [0.01, 50.] } ,
       'hww0jet_cut'    : { 'linY' : [0.0 , 5.] , 'logY' : [0.01, 50.] } ,
       'hww1jet_shape'  : { 'linY' : [0.0 , 5.] , 'logY' : [0.01, 50.] } ,
       'hww1jet_cut'    : { 'linY' : [0.0 , 5.] , 'logY' : [0.01, 50.] } ,
       'hww01jet_shape' : { 'linY' : [0.0 , 5.] , 'logY' : [0.02, 50.] } ,
       'hww01jet_cut'   : { 'linY' : [0.0 , 5.] , 'logY' : [0.02, 50.] } ,
       'hww2j_hcp'      : { 'linY' : [0.0 ,10.] , 'logY' : [0.05,100.] } ,
       'hww2j_cut'      : { 'linY' : [0.0 ,20.] , 'logY' : [0.05,100.] } ,
       'hww2j_shape'    : { 'linY' : [0.0 ,20.] , 'logY' : [0.05,100.] } ,
       'vh3l_cut'       : { 'linY' : [0.0 ,20.] , 'logY' : [0.01,500.] } ,
       'vh3l_shape'     : { 'linY' : [0.0 ,20.] , 'logY' : [0.01,500.] } ,
       'hwwvh2j_cut'    : { 'linY' : [0.0 ,50.] , 'logY' : [0.01,500.] } ,
       'hwwvh2j_shape'  : { 'linY' : [0.0 ,50.] , 'logY' : [0.01,500.] } ,
       'zh3l2j_cut'     : { 'linY' : [0.0 ,150.] , 'logY' : [0.5,700.] } ,
       'zh3l2j_shape'   : { 'linY' : [0.0 ,150.] , 'logY' : [0.5,700.] } ,
       'hww012j_vh3l_vh2j_shape'        : { 'linY' : [0.0 , 5.] , 'logY' : [0.02,50.] } ,
       'hww012j_vh3l_vh2j_zh3l2j_shape' : { 'linY' : [0.0 , 5.] , 'logY' : [0.02,50.] } ,
       'vbfbb'          : { 'linY' : [0.0 ,15.] , 'logY' : [0.05,100.] } ,
       'vbfbbsplit'          : { 'linY' : [0.0 ,15.] , 'logY' : [0.05,100.] } ,
     },

  'LimitExp' : 
     { 
       'Default'        : { 'linY' : [0.0 ,70.] , 'logY' : [0.05,200.] } ,
       'of_cp2_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.5,300.] } ,
       'of_cp2_ext_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.2,300.] } ,
       'sf_cp2_ext_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.5,300.] } ,
       'vbfof_cp2_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.5,300.] } ,
       'vbfofnew_cp2_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.5,300.] } ,
       'vbfsf_cp2_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.8,300.] } ,
       'hww_cp2_1d0'     : { 'linY' : [0.0 ,30.] , 'logY' : [0.2,300.] } ,
       'hww01jof_shape'     : { 'linY' : [0.0 ,70.] , 'logY' : [0.3,10.] } ,
       'of_oldcps'     : { 'linY' : [0.0 ,70.] , 'logY' : [0.3,10.] } ,
     },

  'Sign'  :
     { 
       'Default'        : { 'linY' : [0.0 ,25.] , 'logY' : [0.1,200.] } ,
       'vbfbb'          : { 'linY' : [0.0 , 1.] , 'logY' : [0.01,5.]  } ,
       'vbfbbsplit'          : { 'linY' : [0.0 , 1.] , 'logY' : [0.01,5.]  } ,
     }

}


