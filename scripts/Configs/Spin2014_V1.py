cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/Spin2014/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'Spin2014_V1_noqq'
channels = {
 'Spin2014_V1_noqq' :
 {

  # ============ H --> WW 0/1-jet JCP = 0m ===================
  'hww0jof_jcp_0m'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0m' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 
                                     'dir' : '.' , 'subdir' : '0m' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_0m'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0m' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0m' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 0ph ===================
  'hww0jof_jcp_0ph'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0ph' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0ph' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_0ph'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0ph' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '0ph' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 1m ===================
  'hww0jof_jcp_1m'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1m_old' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1m_old' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1m'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1m_old' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1m_old' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 1p ===================
  'hww0jof_jcp_1p'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1p_old' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1p_old' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_1p'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1p_old' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '1p_old' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2bp ===================
  'hww0jof_jcp_2bp'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2bp' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2bp' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2bp'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2bp' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2bp' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2hp ===================
  'hww0jof_jcp_2hp'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hp' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hp' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2hp'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hp' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hp' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2hp ===================
  'hww0jof_jcp_qq2hp'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hp' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hp' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2hp'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hp' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hp' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2hm ===================
  'hww0jof_jcp_2hm'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hm' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hm' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2hm'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hm' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2hm' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2hm ===================
  'hww0jof_jcp_qq2hm'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hm' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hm' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2hm'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hm' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2hm' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2ph2 ===================
  'hww0jof_jcp_2ph2'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph2' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph2' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph2'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph2' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph2' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2ph2 ===================
  'hww0jof_jcp_qq2ph2'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph2' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph2' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2ph2'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph2' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph2' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2ph3 ===================
  'hww0jof_jcp_qq2ph3'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph3' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph3' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2ph3'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph3' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph3' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2ph6 ===================
  'hww0jof_jcp_2ph6'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph6' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph6' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2ph6'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph6' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2ph6' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2ph6 ===================
  'hww0jof_jcp_qq2ph6'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph6' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph6' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2ph6'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph6' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2ph6' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2mh9 ===================
  'hww0jof_jcp_2mh9'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh9' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh9' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2mh9'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh9' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh9' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = 2mh10 ===================
  'hww0jof_jcp_2mh10'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh10' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh10' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_2mh10'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh10' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : '2mh10' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,

  # ============ H --> WW 0/1-jet JCP = qq2mh10 ===================
  'hww0jof_jcp_qq2mh10'    : {
                          '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2mh10' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2mh10' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                        } ,
  'hww1jof_jcp_qq2mh10'    : {
                          '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2mh10' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                          '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  ,
                                     'dir' : '.' , 'subdir' : 'qq2mh10' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                        } ,



 }
}


combinations = {

 'hww01jet_jcp_0m'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_0m' ,  'hww1jof_jcp_0m'  ] , 'purposes' : [ 'jcp' ] , 
                         'legend' : '0^{-}'
                       } ,

 'hww01jet_jcp_0ph'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_0ph' ,  'hww1jof_jcp_0ph'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '0^{+}_{h}'
                       } ,

 'hww01jet_jcp_1p'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1p' ,  'hww1jof_jcp_1p'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{+}'
                       } ,

 'hww01jet_jcp_1m'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_1m' ,  'hww1jof_jcp_1m'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '1^{-}'
                       } ,

 'hww01jet_jcp_2bp'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2bp' ,  'hww1jof_jcp_2bp'  ] , 'purposes' : [ 'jcp','jcpnoqq' ] ,
                         'legend' : '2^{+}_{m}'
                       } ,

 'hww01jet_jcp_2hp'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hp' ,  'hww1jof_jcp_2hp'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}'
                       } ,

 'hww01jet_jcp_qq2hp'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2hp' ,  'hww1jof_jcp_qq2hp'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h}(q#bar{q})'
                       } ,

 'hww01jet_jcp_2hm'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2hm' ,  'hww1jof_jcp_2hm'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h}'
                       } ,

 'hww01jet_jcp_qq2hm'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2hm' ,  'hww1jof_jcp_qq2hm'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h}(q#bar{q})'
                       } ,

 'hww01jet_jcp_2ph2'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph2' ,  'hww1jof_jcp_2ph2'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h2}'
                       } ,

 'hww01jet_jcp_qq2ph2' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2ph2' ,  'hww1jof_jcp_qq2ph2'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h2}(q#bar{q})'
                       } ,
 'hww01jet_jcp_qq2ph3' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2ph3' ,  'hww1jof_jcp_qq2ph3'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h3}(q#bar{q})'
                       } ,
 'hww01jet_jcp_2ph6'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2ph6' ,  'hww1jof_jcp_2ph6'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h6}'
                       } ,
 'hww01jet_jcp_qq2ph6' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2ph6' ,  'hww1jof_jcp_qq2ph6'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{+}_{h6}(q#bar{q})'
                       } ,
 'hww01jet_jcp_2mh9'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh9' ,  'hww1jof_jcp_2mh9'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h9}'
                       } ,
 'hww01jet_jcp_2mh10'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2mh10' ,  'hww1jof_jcp_2mh10'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h10}'
                       } ,
 'hww01jet_jcp_qq2mh10' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_qq2mh10' ,  'hww1jof_jcp_qq2mh10'  ] , 'purposes' : [ 'jcp' ] ,
                         'legend' : '2^{-}_{h10}(q#bar{q})'
                       } ,

# TEST
 'hww01jet_jcp_2bp_fixWW'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp_2bp' ,  'hww1jof_jcp_2bp'  ] , 'purposes' : [ 'jcp','jcpnoqq' ] ,
                         'legend' : '2^{+}_{m}'
                       } ,


}

