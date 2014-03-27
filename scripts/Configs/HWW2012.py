
homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/'

workspace   = homedir+'workspace/'
jobdir      = homedir+'jobs/'
plotsdir    = homedir+'plots/'
cardbase    = homedir+'cmshcg/trunk/'
combscripts = homedir+'cmshcg/trunk/summer2013/scripts/'



DefaultVersion = 'V8'
channels = { 

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


  # ============ H --> WW 0/1-jet JCP=1m ===================
  'hww0jof_jcp1m': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1m/hww2l2v' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1m/hww2l2v' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp1m': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1m/hww2l2v' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1m/hww2l2v' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } ,
#

  # ============ H --> WW 0/1-jet JCP=1p ===================
  'hww0jof_jcp1p': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1p/hww2l2v' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1p/hww2l2v' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp1p': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1p/hww2l2v' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1p/hww2l2v' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
                    } ,
#

  # ============ H --> WW 0/1-jet JCP=1mix ===================
  'hww0jof_jcp1mix': {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1mix/hww2l2v' , 'card' : 'hwwof_0j_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1mix/hww2l2v' , 'card' : 'hwwof_0j_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] } ,
                    } ,
  'hww1jof_jcp1mix': {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1mix/hww2l2v' , 'card' : 'hwwof_1j_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [120,130]  , 'dir' : 'summer2013' , 'subdir' : '1mix/hww2l2v' , 'card' : 'hwwof_1j_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] } ,
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


  'hww01jet_jcp1m' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp1m' ,  'hww1jof_jcp1m'  ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,
  'hww01jet_jcp1p' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp1p' ,  'hww1jof_jcp1p'  ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,
  'hww01jet_jcp1mix' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jof_jcp1mix' ,  'hww1jof_jcp1mix'  ] , 'purposes' : [ 'jcp' ] , 'legend' : 'H #rightarrow WW #rightarrow 2l2#nu 0/1-jet (2d)'  } ,

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


}
