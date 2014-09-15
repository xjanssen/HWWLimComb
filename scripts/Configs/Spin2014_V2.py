cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'Spin2014_V2'
channels = {
 'Spin2014_V2' :
 {

  # ============ H --> gg JCP = 2pm (LEGACY !!!!) ===================
  'hgg_jcp_2pm'    : {
                          '7TeV' : { 'tag' : 'inc' , 'prod' : 'ggH' , 'branch' : 'hgg' , 'decay' : '' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'Hgg' , 'subdir' : '2pm/$MASS' , 'card' : 'hgg_spin_card_7TeV_bernsteins.txt'  } ,
                          '8TeV' : { 'tag' : 'inc' , 'prod' : 'ggH' , 'branch' : 'hgg' , 'decay' : '' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'Hgg' , 'subdir' : '2pm/$MASS' , 'card' : 'hgg_spin_card_8TeV_bernsteins.txt'  } ,
                        } ,


  # ============ H --> WW 0/1-jet JCP = 0m ===================
  'hww0jof_jcp_0m'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0m' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 
                                     'dir' : 'V2' , 'subdir' : '0m' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_0m'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0m' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0m' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 0ph ===================
  'hww0jof_jcp_0ph'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0ph' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0ph' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_0ph'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0ph' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0ph' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 0l1 ===================
  'hww0jof_jcp_0l1'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0l1' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0l1' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_0l1'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0l1' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '0l1' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,


  # ============ H --> WW 0/1-jet JCP = 1m ===================
  'hww0jof_jcp_1m'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1m' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1m' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1m'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1m' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1m' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 1p ===================
  'hww0jof_jcp_1p'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1p' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1p' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1p'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1p' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1p' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 1mix ===================
  'hww0jof_jcp_1mix'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1mix' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1mix' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1mix'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1mix' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1mix' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 1 (HZZ style) ===================

  'hww0jof_jcp_1hzz'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1hzzlike' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1hzzlike' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1hzz'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '1hzzlike' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '1hzzlike' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,




  # ============ H --> WW 0/1-jet JCP = 2bp ===================
  'hww0jof_jcp_2bp'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2bp' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2bp' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2bp'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2bp' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2bp' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2hm ===================
  'hww0jof_jcp_2hm'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2hm' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2hm' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2hm'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2hm' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2hm' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,


  # ============ H --> WW 0/1-jet JCP = 2hp ===================
  'hww0jof_jcp_2hp'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2hp' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2hp' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2hp'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2hp' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2hp' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,


  # ============ H --> WW 0/1-jet JCP = 2pm ===================
  'hww0jof_jcp_2pm'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2pm'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2pm (LEGACY !!!!) ===================
  'hww0jof_jcp_2pm_legacy'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm_legacy/$MASS' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm_legacy/$MASS' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2pm_legacy'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm_legacy/$MASS' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2pm_legacy/$MASS' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,



  # ============ H --> WW 0/1-jet JCP = 2ph2 ===================
  'hww0jof_jcp_2ph2'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph2' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph2' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph2'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph2' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph2' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2ph3 ===================
  'hww0jof_jcp_2ph3'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph3' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph3' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph3'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph3' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph3' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2ph6 ===================
  'hww0jof_jcp_2ph6'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph6' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph6' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph6'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph6' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph6' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2ph7 ===================
  'hww0jof_jcp_2ph7'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph7' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph7' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph7'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2ph7' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2ph7' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2mh9 ===================
  'hww0jof_jcp_2mh9'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2mh9' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2mh9' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2mh9'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2mh9' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2mh9' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2mh10 ===================
  'hww0jof_jcp_2mh10'    : {
#                         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2mh10' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2mh10' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2mh10'    : {
#                         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
#                                    'dir' : 'V2' , 'subdir' : '2mh10' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : 'V2' , 'subdir' : '2mh10' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

###########
## HZZ  ###
########### 

  # ============ H --> ZZ JCP = 1qqb   ===================

  'hzz_4mu_jcp_1qqb' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_1qqb' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_1qqb' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_2mu2eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'spin1_qqb' , 'card' : 'hzz4l_2mu2eS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2b+ (qqb)   ===================

  

  'hzz_4mu_jcp_2bp_qqb' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2bp_qqb' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2bp_qqb' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_qqb_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


   # ============ H --> ZZ JCP = 2m+ (dec) (LEGACY !!!!)   ===================

  

  'hzz_4mu_jcp_2pm_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2pm_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2pm_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_pi2m+_legacy/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2b+ (dec)   ===================

  

  'hzz_4mu_jcp_2bp_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2bp_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2bp_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2b+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


   # ============ H --> ZZ JCP = 2h- (dec)   ===================


  'hzz_4mu_jcp_2hm_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2hm_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2hm_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


   # ============ H --> ZZ JCP = 2h+ (dec)   ===================


  'hzz_4mu_jcp_2hp_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2hp_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2hp_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2h2+ (dec)   ===================


  'hzz_4mu_jcp_2ph2_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2ph2_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2ph2_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h2+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


   # ============ H --> ZZ JCP = 2h3+ (dec)   ===================


  'hzz_4mu_jcp_2ph3_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2ph3_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2ph3_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h3+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2h6+ (dec)   ===================


  'hzz_4mu_jcp_2ph6_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2ph6_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2ph6_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h6+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


   # ============ H --> ZZ JCP = 2h7+ (dec)   ===================


  'hzz_4mu_jcp_2ph7_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2ph7_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2ph7_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h7+_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2h9- (dec)   ===================


  'hzz_4mu_jcp_2mh9_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2mh9_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2mh9_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h9-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,

   # ============ H --> ZZ JCP = 2h10- (dec)   ===================


  'hzz_4mu_jcp_2mh10_dec' : {
                         '7TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4mu' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4muS_8TeV_ALT.txt' } ,
                        } ,


  'hzz_4e_jcp_2mh10_dec' : {
                         '7TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '4e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_4eS_8TeV_ALT.txt' } ,
                        } ,

  'hzz_2mu2e_jcp_2mh10_dec' : {
                         '7TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_7TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_7TeV_ALT.txt' } ,
                         '8TeV' : { 'tag' : '2mu2e' , 'prod' : 'ggH' , 'branch' : 'hzz' , 'decay' : '4l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                    'dir' : 'HZZ' , 'subdir' : 'cards_2D_dec_gg_2h10-_8TeV/HCG/125.6/' , 'card' : 'hzz4l_2e2muS_8TeV_ALT.txt' } ,
                        } ,


 }
}


combinations = {

##############
#### Hgg #####
##############

 'hgg_jcp_2pm'      : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hgg_jcp_2pm' ]  , 'purposes' : [ 'jcp' ] , 'legend' : '2^{+}_{m}' } ,


##############
#### HWW #####
##############


 'hww01jet_jcp_0m'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_0m' ,  'hww1jof_jcp_0m'  ] , 'purposes' : [ 'jcp' ] , 
                         'legend' : '0^{-}'
                       } ,
 'hww01jet_jcp_0ph'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_0ph' ,  'hww1jof_jcp_0ph'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '0^{+}_{h}'
                       } ,
 'hww01jet_jcp_0l1'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_0l1' ,  'hww1jof_jcp_0l1'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '0_{l1}'
                       } ,



 'hww01jet_jcp_1p'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1p' ,  'hww1jof_jcp_1p'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{+}'
                       } ,

 'hww01jet_jcp_1m'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1m' ,  'hww1jof_jcp_1m'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{-}'
                       } ,

 'hww01jet_jcp_1mix'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1mix' ,  'hww1jof_jcp_1mix'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{mix}'
                       } ,



 'hww01jet_jcp_2bp'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2bp' ,  'hww1jof_jcp_2bp'  ] , 'purposes' : [ 'jcp','jcpnoqq' ] ,
                         'legend' : '2^{+}_{b}'
                       } ,

 'hww01jet_jcp_2hp'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hp' ,  'hww1jof_jcp_2hp'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}'
                       } ,

 'hww01jet_jcp_2hm'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hm' ,  'hww1jof_jcp_2hm'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h}'
                       } ,
 'hww01jet_jcp_2pm'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2pm' ,  'hww1jof_jcp_2pm'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                       } ,

 'hww01jet_jcp_2pm_legacy'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2pm_legacy' ,  'hww1jof_jcp_2pm_legacy'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                       } ,

 'hww01jet_jcp_2ph2'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph2' ,  'hww1jof_jcp_2ph2'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h2}'
                       } ,
 'hww01jet_jcp_2ph3'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph2' ,  'hww1jof_jcp_2ph2'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h3}'
                       } ,

 'hww01jet_jcp_2ph6'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph6' ,  'hww1jof_jcp_2ph6'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h6}'
                       } ,
 'hww01jet_jcp_2ph7'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph7' ,  'hww1jof_jcp_2ph7'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h7}'
                       } ,

 'hww01jet_jcp_2mh9'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh9' ,  'hww1jof_jcp_2mh9'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h9}'
                       } ,
 'hww01jet_jcp_2mh10'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh10' ,  'hww1jof_jcp_2mh10'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h10}'
                       } ,


 'hww_jcp_1hzz'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1hzz' ,  'hww1jof_jcp_1hzz' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(HZZ)'
                     } ,


##############
#### HZZ #####
##############

 'hzz_jcp_1qqb' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_1qqb' , 'hzz_4e_jcp_1qqb' , 'hzz_2mu2e_jcp_1qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(qqb)'
                  } ,

 'hzz_jcp_1qqb_canyou' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_1qqb' , 'hzz_4e_jcp_1qqb' , 'hzz_2mu2e_jcp_1qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(qqb)'
                  } ,



 'hzz_jcp_2bp_qqb' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2bp_qqb' , 'hzz_4e_jcp_2bp_qqb' , 'hzz_2mu2e_jcp_2bp_qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(qqb)'
                  } ,

 'hzz_jcp_2pm_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2pm_dec' , 'hzz_4e_jcp_2pm_dec' , 'hzz_2mu2e_jcp_2pm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                  } ,

 'hzz_jcp_2bp_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2bp_dec' , 'hzz_4e_jcp_2bp_dec' , 'hzz_2mu2e_jcp_2bp_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{b}'
                  } ,

 'hzz_jcp_2hm_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2hm_dec' , 'hzz_4e_jcp_2hm_dec' , 'hzz_2mu2e_jcp_2hm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}'
                  } ,

 'hzz_jcp_2hp_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2hp_dec' , 'hzz_4e_jcp_2hp_dec' , 'hzz_2mu2e_jcp_2hp_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}'
                  } ,

 'hzz_jcp_2ph2_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2ph2_dec' , 'hzz_4e_jcp_2ph2_dec' , 'hzz_2mu2e_jcp_2ph2_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h2}'
                  } ,

 'hzz_jcp_2ph3_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2ph3_dec' , 'hzz_4e_jcp_2ph3_dec' , 'hzz_2mu2e_jcp_2ph3_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h3}'
                  } ,

 'hzz_jcp_2ph6_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2ph6_dec' , 'hzz_4e_jcp_2ph6_dec' , 'hzz_2mu2e_jcp_2ph6_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h6}'
                  } ,

 'hzz_jcp_2ph7_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2ph7_dec' , 'hzz_4e_jcp_2ph7_dec' , 'hzz_2mu2e_jcp_2ph7_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h7}'
                  } ,

 'hzz_jcp_2mh9_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2mh9_dec' , 'hzz_4e_jcp_2mh9_dec' , 'hzz_2mu2e_jcp_2mh9_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h9}'
                  } ,

 'hzz_jcp_2mh10_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hzz_4mu_jcp_2mh10_dec' , 'hzz_4e_jcp_2mh10_dec' , 'hzz_2mu2e_jcp_2mh10_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h10}'
                  } ,


####################
#### HWW + HZZ #####
####################

 'hwwhzz_jcp_1p'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1p' ,  'hww1jof_jcp_1p' ,
                                                                         'hzz_4mu_jcp_1qqb' , 'hzz_4e_jcp_1qqb' , 'hzz_2mu2e_jcp_1qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{+}'
                     } ,


 'hwwhzz_jcp_1m'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1m' ,  'hww1jof_jcp_1m'  ,
                                                                         'hzz_4mu_jcp_1qqb' , 'hzz_4e_jcp_1qqb' , 'hzz_2mu2e_jcp_1qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{-}'
                     } ,

 'hwwhzz_jcp_1hzz'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1hzz' ,  'hww1jof_jcp_1hzz'  ,
                                                                         'hzz_4mu_jcp_1qqb' , 'hzz_4e_jcp_1qqb' , 'hzz_2mu2e_jcp_1qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(HZZ)'
                     } ,



 'hwwhzz_jcp_2bp_qqb' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2bp' ,  'hww1jof_jcp_2bp' ,
                                                                            'hzz_4mu_jcp_2bp_qqb' , 'hzz_4e_jcp_2bp_qqb' , 'hzz_2mu2e_jcp_2bp_qqb' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1(qqb)'
                  } ,


 'hwwhzz_jcp_2bp_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2bp' ,  'hww1jof_jcp_2bp' ,
                                                                            'hzz_4mu_jcp_2bp_dec' , 'hzz_4e_jcp_2bp_dec' , 'hzz_2mu2e_jcp_2bp_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{b}'
                  } ,

 'hwwhzz_jcp_2pm_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2pm' ,  'hww1jof_jcp_2pm' ,
                                                                            'hzz_4mu_jcp_2pm_dec' , 'hzz_4e_jcp_2pm_dec' , 'hzz_2mu2e_jcp_2pm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                  } ,


 'hwwhzz_jcp_2pm_dec_legacy' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2pm_legacy' ,  'hww1jof_jcp_2pm_legacy' ,
                                                                            'hzz_4mu_jcp_2pm_dec' , 'hzz_4e_jcp_2pm_dec' , 'hzz_2mu2e_jcp_2pm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                  } ,


#

 'hwwhzz_jcp_2hm_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hm' ,  'hww1jof_jcp_2hm' ,
                                                                            'hzz_4mu_jcp_2hm_dec' , 'hzz_4e_jcp_2hm_dec' , 'hzz_2mu2e_jcp_2hm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h}'
                  } ,

 'hwwhzz_jcp_2hp_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hp' ,  'hww1jof_jcp_2hp' ,
                                                                            'hzz_4mu_jcp_2hp_dec' , 'hzz_4e_jcp_2hp_dec' , 'hzz_2mu2e_jcp_2hp_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}'
                  } ,

 'hwwhzz_jcp_2ph2_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph2' ,  'hww1jof_jcp_2ph2' ,
                                                                            'hzz_4mu_jcp_2ph2_dec' , 'hzz_4e_jcp_2ph2_dec' , 'hzz_2mu2e_jcp_2ph2_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h2}'
                  } ,

 'hwwhzz_jcp_2ph3_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph3' ,  'hww1jof_jcp_2ph3' ,
                                                                            'hzz_4mu_jcp_2ph3_dec' , 'hzz_4e_jcp_2ph3_dec' , 'hzz_2mu2e_jcp_2ph3_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h3}'
                  } ,

 'hwwhzz_jcp_2ph6_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph6' ,  'hww1jof_jcp_2ph6' ,
                                                                            'hzz_4mu_jcp_2ph6_dec' , 'hzz_4e_jcp_2ph6_dec' , 'hzz_2mu2e_jcp_2ph6_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h6}'
                  } ,

 'hwwhzz_jcp_2ph7_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph7' ,  'hww1jof_jcp_2ph7' ,
                                                                            'hzz_4mu_jcp_2ph7_dec' , 'hzz_4e_jcp_2ph7_dec' , 'hzz_2mu2e_jcp_2ph7_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h7}'
                  } ,

 'hwwhzz_jcp_2mh9_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh9' ,  'hww1jof_jcp_2mh9' ,
                                                                            'hzz_4mu_jcp_2mh9_dec' , 'hzz_4e_jcp_2mh9_dec' , 'hzz_2mu2e_jcp_2mh9_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h9}'
                  } ,

 'hwwhzz_jcp_2mh10_dec' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh10' ,  'hww1jof_jcp_2mh10' ,
                                                                            'hzz_4mu_jcp_2mh10_dec' , 'hzz_4e_jcp_2mh10_dec' , 'hzz_2mu2e_jcp_2mh10_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h10}'
                  } ,


##########################
#### Hgg + HWW + HZZ #####
##########################

  'hgghzzhww_jcp_2pm_dec_legacy' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2pm_legacy' ,  'hww1jof_jcp_2pm_legacy' , 'hgg_jcp_2pm' ,
                                                                            'hzz_4mu_jcp_2pm_dec' , 'hzz_4e_jcp_2pm_dec' , 'hzz_2mu2e_jcp_2pm_dec' ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{m}'
                  } ,




}

