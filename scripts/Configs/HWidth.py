#!/usr/bin/env python


cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/HWidth/cmshcg/trunk/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'HWidth_V4'
channels = {

'HWidth_V4' : {


### ZZ->4l
# on-shell cards  : - hzz4l_*_*TeV_0.txt -> 0+1 jet
#                   - hzz4l_*_*TeV_1.txt -> 2+ jets
# off-shell cards : hzz4l_*_*TeV.txt -> Inclusive in jet bins 

#........ -> 4mu

  'hzz_4mu_onshell_01j' : {
                         '7TeV' : { 'tag' : '4mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4muS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '4mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4muS_8TeV_0.txt' } ,
                        } ,

  'hzz_4mu_onshell_2j'  : {
                         '7TeV' : { 'tag' : '4mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4muS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '4mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4muS_8TeV_1.txt' } ,
                        } ,

  'hzz_4mu_onshell_01jc' : {
                         '7TeV' : { 'tag' : '4mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '4mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_8TeV_0.txt' } ,
                        } ,

  'hzz_4mu_onshell_2jc'  : {
                         '7TeV' : { 'tag' : '4mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '4mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_8TeV_1.txt' } ,
                        } ,


  'hzz_4mu_offshell'    : {
                         '7TeV' : { 'tag' : '4mu_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_7TeV.txt' } ,
                         '8TeV' : { 'tag' : '4mu_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4muS_8TeV.txt' } ,
                        } ,

#........ -> 4e

  'hzz_4e_onshell_01j' : {
                         '7TeV' : { 'tag' : '4e_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4eS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '4e_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4eS_8TeV_0.txt' } ,
                        } ,

  'hzz_4e_onshell_2j'  : {
                         '7TeV' : { 'tag' : '4e_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4eS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '4e_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_4eS_8TeV_1.txt' } ,
                        } ,

  'hzz_4e_onshell_01jc' : {
                         '7TeV' : { 'tag' : '4e_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '4e_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_8TeV_0.txt' } ,
                        } ,

  'hzz_4e_onshell_2jc'  : {
                         '7TeV' : { 'tag' : '4e_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '4e_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_8TeV_1.txt' } ,
                        } ,


  'hzz_4e_offshell'    : {
                         '7TeV' : { 'tag' : '4e_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_7TeV.txt' } ,
                         '8TeV' : { 'tag' : '4e_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_4eS_8TeV.txt' } ,
                        } ,


#........ -> 2e2mu

  'hzz_2e2mu_onshell_01j' : {
                         '7TeV' : { 'tag' : '2e2mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_2e2muS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '2e2mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_2e2muS_8TeV_0.txt' } ,
                        } ,

  'hzz_2e2mu_onshell_2j'  : {
                         '7TeV' : { 'tag' : '2e2mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_2e2muS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '2e2mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'summer2013/couplings/hzz4l' , 'subdir' : '$MASS' , 'card' : 'hzz4l_2e2muS_8TeV_1.txt' } ,
                        } ,

  'hzz_2e2mu_onshell_01jc' : {
                         '7TeV' : { 'tag' : '2e2mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_7TeV_0.txt' } ,
                         '8TeV' : { 'tag' : '2e2mu_onshell_01j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_8TeV_0.txt' } ,
                        } ,

  'hzz_2e2mu_onshell_2jc'  : {
                         '7TeV' : { 'tag' : '2e2mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_7TeV_1.txt' } ,
                         '8TeV' : { 'tag' : '2e2mu_onshell_2j' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_8TeV_1.txt' } ,
                        } ,


  'hzz_2e2mu_offshell'    : {
                         '7TeV' : { 'tag' : '2e2mu_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_7TeV.txt' } ,
                         '8TeV' : { 'tag' : '2e2mu_offshell' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz4l' , 'subdir' : '.' , 'card' : 'hzz4l_2e2muS_8TeV.txt' } ,
                        } ,






### ZZ->2l2nu

  'hzz_2l2nu'   : {
                     '8TeV' : { 'tag' : '2l2nu' , 'prod' : 'ggH' ,  'branch' : 'hzz' , 'decay' : '2l2nu' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                                    'dir' : 'cadi/HIG-14-002/hzz2l2nu' , 'subdir' : '.' , 'card' : 'card_incl.dat' } ,
                  },


### WW->2l2nu


  'hwidth_hww0jof_shape' : {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  , 
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-4.94fb.mH125.of_0j_shape.txt'  } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  , 
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-19.36fb.mH125.of_0j_shape.txt'  } ,
                    } ,

  'hwidth_hww1jof_shape' : {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-4.94fb.mH125.of_1j_shape.txt'  } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-19.36fb.mH125.of_1j_shape.txt'  } ,
                    } ,

  'hwidth_hww2jof_shape' : {
                    '7TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-4.94fb.mH125.of_2j_shape.txt'  } ,
                    '8TeV' : { 'tag' : 'of2j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  ,
                               'dir' : 'cadi/HIG-14-032' , 'subdir' : '.' , 'card' : 'hww-19.36fb.mH125.of_2j_shape.txt'  } ,
                    } ,


 }
}

combinations = {

#
# HWidth
#


# H->ZZ->4l


   'hwidth_hzz4l' :
                  { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   , 'hzz_4mu_offshell' ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    , 'hzz_4e_offshell' ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j' , 'hzz_2e2mu_offshell' ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 4l'
                  } ,

   'hwidth_hzz4lc' :
                  { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_onshell_01jc'   , 'hzz_4mu_onshell_2jc'   , 'hzz_4mu_offshell' ,
                                   'hzz_4e_onshell_01jc'    , 'hzz_4e_onshell_2jc'    , 'hzz_4e_offshell' ,
                                   'hzz_2e2mu_onshell_01jc' , 'hzz_2e2mu_onshell_2jc' , 'hzz_2e2mu_offshell' ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 4l'
                  } ,


   'offshell_hzz4l' :
                   { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_offshell' ,
                                   'hzz_4e_offshell' ,
                                   'hzz_2e2mu_offshell' ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 4l'
                  } ,



   'onshell_hzz4l' :
                  { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j' ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth'  ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 4l'
                  } ,

# H->ZZ-2l2nu (Use 4l on-shell for mu !)

   'hwidth_hzz2l2nu' :
                  { 'energies' : [ '8TeV' ] ,
                    'channels' : [ 'hzz_2l2nu' ,
                                   'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j'  
                                 ] ,
                    'purposes' : [ 'smhiggs' , 'hwidth'  ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 2l2v'
                  } ,

   'hwidth_hzz2l2nuc' :
                  { 'energies' : [ '8TeV' ] ,
                    'channels' : [ 'hzz_2l2nu' ,
                                   'hzz_4mu_onshell_01jc'   , 'hzz_4mu_onshell_2jc'   ,
                                   'hzz_4e_onshell_01jc'    , 'hzz_4e_onshell_2jc'    ,
                                   'hzz_2e2mu_onshell_01jc' , 'hzz_2e2mu_onshell_2jc'  
                                 ] ,
                    'purposes' : [ 'smhiggs' , 'hwidth'  ] ,
                    'legend'   : 'H #rightarrow ZZ #rightarrow 2l2v'
                  } ,



# H->ZZ

   'hwidth_hzz' :
                  { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   , 'hzz_4mu_offshell' ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    , 'hzz_4e_offshell' ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j' , 'hzz_2e2mu_offshell' ,
                                   'hzz_2l2nu' 
                                 ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                    'legend'   : 'H #rightarrow ZZ'
                  } ,


   'hwidth_hzzc' :
                  { 'energies' : [ '7TeV' , '8TeV' ] , 
                    'channels' : [ 'hzz_4mu_onshell_01jc'   , 'hzz_4mu_onshell_2jc'   , 'hzz_4mu_offshell' ,
                                   'hzz_4e_onshell_01jc'    , 'hzz_4e_onshell_2jc'    , 'hzz_4e_offshell' ,
                                   'hzz_2e2mu_onshell_01jc' , 'hzz_2e2mu_onshell_2jc' , 'hzz_2e2mu_offshell' ,
                                   'hzz_2l2nu' 
                                 ] ,  
                    'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                    'legend'   : 'H #rightarrow ZZ'
                  } ,




# H->WW->2l2nu


   'hwidth_hww0j' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow WW (0j)'
                        } ,


   'hwidth_hww1j' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww1jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow WW (1j)'
                        } ,

   'hwidth_hww2j' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww2jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow WW (2j)'
                        } ,

   'hwidth_hww01j' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' , 'hwidth_hww1jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow WW (0/1j)'
                        } ,

   'hwidth_hww' :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' , 'hwidth_hww1jof_shape' , 'hwidth_hww2jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow WW'
                        } ,


# HZZ->2l2v + HWW

   'hwidth_2l2nu' :    {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' , 'hwidth_hww1jof_shape' , 'hwidth_hww2jof_shape' ,
                                   'hzz_2l2nu' ,
                                   'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j' 
                                       ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow ZZ+WW #rightarrow 2l2nu '
                        } ,
 

# HZZ + HWW

   'hwidth_all' :    {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' , 'hwidth_hww1jof_shape' , 'hwidth_hww2jof_shape' ,
                                   'hzz_2l2nu' ,
                                   'hzz_4mu_onshell_01j'   , 'hzz_4mu_onshell_2j'   ,
                                   'hzz_4e_onshell_01j'    , 'hzz_4e_onshell_2j'    ,
                                   'hzz_2e2mu_onshell_01j' , 'hzz_2e2mu_onshell_2j' ,
                                   'hzz_4mu_offshell' ,
                                   'hzz_4e_offshell' ,
                                   'hzz_2e2mu_offshell'
                                       ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow ZZ+WW'
                        } ,
 

   'hwidth_allc' :    {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' , 'hwidth_hww1jof_shape' , 'hwidth_hww2jof_shape' ,
                                   'hzz_2l2nu' ,
                                   'hzz_4mu_onshell_01jc'   , 'hzz_4mu_onshell_2jc'   ,
                                   'hzz_4e_onshell_01jc'    , 'hzz_4e_onshell_2jc'    ,
                                   'hzz_2e2mu_onshell_01jc' , 'hzz_2e2mu_onshell_2jc' ,
                                   'hzz_4mu_offshell' ,
                                   'hzz_4e_offshell' ,
                                   'hzz_2e2mu_offshell'
                                       ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'H #rightarrow ZZ+WW'
                        } ,


} 
