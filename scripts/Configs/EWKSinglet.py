cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/2HWW/cmshcg/trunk/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'EWKS_V0'
channels = {
 'EWKS_V0' : 
 {
   ###### Paper ( OLD CPS+Interf.) ####### 

   # ============ H -> WW 0/1-jet cut-based ================== 
   'hww2l2v_0jsf_cut_Paper' :   
      {
         '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_7TeV_Paper.txt'} ,
         '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_8TeV_Paper.txt'} ,
      } ,

   'hww2l2v_1jsf_cut_Paper' :   
      {
         '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_7TeV_Paper.txt'} ,
         '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_8TeV_Paper.txt'} ,
      } ,

   # ============ H -> WW 0/1-jet shape-based ==================
   'hww2l2v_0jof_shape_Paper' :
      {
         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_7TeV_Paper.txt'} ,
         '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_8TeV_Paper.txt'} ,
      } ,

   'hww2l2v_1jof_shape_Paper' :
      {
         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_7TeV_Paper.txt'} ,
         '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_8TeV_Paper.txt'} ,
      } ,

  # ============ H -> WW VBF Cut Based =====================
  'hww2l2v_2jsf_cut_Paper' :   
      {
         '7TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_7TeV_Paper.txt'},
         '8TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_8TeV_Paper.txt'},
      } ,

  # ============ H -> WW VBF Shape Based =====================
  'hww2l2v_2jof_shape_Paper' : 
      {
         '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'shape'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_7TeV_Paper.txt' },
         '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'shape'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_8TeV_Paper.txt' },
      } ,

   ###### SM (NEW CPS+Interf.) ####### 

   # ============ H -> WW 0/1-jet cut-based ================== 
   'hww2l2v_0jsf_cut_SM' :   
      {
         '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_7TeV_SM.txt'} ,
         '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_8TeV_SM.txt'} ,
      } ,

   'hww2l2v_1jsf_cut_SM' :   
      {
         '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_7TeV_SM.txt'} ,
         '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_8TeV_SM.txt'} ,
      } ,

   # ============ H -> WW 0/1-jet shape-based ==================
   'hww2l2v_0jof_shape_SM' :
      {
         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_7TeV_SM.txt'} ,
         '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_8TeV_SM.txt'} ,
      } ,

   'hww2l2v_1jof_shape_SM' :
      {
         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_7TeV_SM.txt'} ,
         '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_8TeV_SM.txt'} ,
      } ,

  # ============ H -> WW VBF Cut Based =====================
  'hww2l2v_2jsf_cut_SM' :   
      {
         '7TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_7TeV_SM.txt'},
         '8TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_8TeV_SM.txt'},
      } ,

  # ============ H -> WW VBF Shape Based =====================
  'hww2l2v_2jof_shape_SM' : 
      {
         '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'shape'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_7TeV_SM.txt' },
         '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'shape'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_8TeV_SM.txt' },
      } ,


   ###### SI125 (NEW CPS+Interf.) ####### 

   # ============ H -> WW 0/1-jet cut-based ================== 
   'hww2l2v_0jsf_cut_SI125' :   
      {
         '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_7TeV_SI125.txt'} ,
         '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_0j_cut_8TeV_SI125.txt'} ,
      } ,

   'hww2l2v_1jsf_cut_SI125' :   
      {
         '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [145,600]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_7TeV_SI125.txt'} ,
         '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [145,1000]  , 
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_1j_cut_8TeV_SI125.txt'} ,
      } ,

   # ============ H -> WW 0/1-jet shape-based ==================
   'hww2l2v_0jof_shape_SI125' :
      {
         '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_7TeV_SI125.txt'} ,
         '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_0j_shape_8TeV_SI125.txt'} ,
      } ,

   'hww2l2v_1jof_shape_SI125' :
      {
         '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [145,600]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_7TeV_SI125.txt'} ,
         '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [145,1000]  ,
                    'dir' : 'highmass2014' , 'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_1j_shape_8TeV_SI125.txt'} ,
      } ,

  # ============ H -> WW VBF Cut Based =====================
  'hww2l2v_2jsf_cut_SI125' :   
      {
         '7TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'cut'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_7TeV_SI125.txt'},
         '8TeV' : { 'tag' : 'sf2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'cut'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwsf_2j_cut_8TeV_SI125.txt'},
      } ,

  # ============ H -> WW VBF Shape Based =====================
  'hww2l2v_2jof_shape_SI125' : 
      {
         '7TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 7 , 'method' : 'shape'  , 'mrange' : [145,600] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_7TeV_SI125.txt' },
         '8TeV' : { 'tag' : 'of2j'  , 'prod' : 'qqH', 'branch' : 'hww' , 'decay' : '2l2v'    , 'energy' : 8 , 'method' : 'shape'  , 'mrange' : [145,1000] , 
                    'dir' : 'highmass2014'   ,  'subdir' : 'hww2l2v/$MASS/cpsq10_brnew00' , 'card' : 'hwwof_2j_shape_8TeV_SI125.txt' },
      } ,

 }
}



combinations = { 

  # ============= Paper ( OLD CPS+Interf.)  ===============
  'hww2l2v_0jsf_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_Paper' ] , 
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j SF '   } ,
  'hww2l2v_1jsf_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jsf_cut_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j SF '   } ,
  'hww2l2v_0jof_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j DF '   } ,
  'hww2l2v_1jof_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j DF '   } ,
  'hww2l2v_2jsf_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF '   } ,
  'hww2l2v_2jof_Paper'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j DF '   } ,
  'hww2l2v_01j_Paper'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_Paper'   , 'hww2l2v_1jsf_cut_Paper' ,
                                                                            'hww2l2v_0jof_shape_Paper' , 'hww2l2v_1jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1j SF+DF '   } ,
  'hww2l2v_2j_Paper'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_Paper'   , 'hww2l2v_2jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF+DF '   } ,
  'hww2l2v_of_Paper'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_Paper' , 'hww2l2v_1jof_shape_Paper' , 'hww2l2v_2jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j DF '   } ,
  'hww2l2v_sf_Paper'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_Paper'   , 'hww2l2v_1jsf_cut_Paper'   , 'hww2l2v_2jsf_cut_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF '   } ,
  'hww2l2v_Paper'        : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_Paper'   , 'hww2l2v_1jsf_cut_Paper' , 
                                                                            'hww2l2v_0jof_shape_Paper' , 'hww2l2v_1jof_shape_Paper' , 
                                                                            'hww2l2v_2jsf_cut_Paper'   , 'hww2l2v_2jof_shape_Paper' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF+DF '   } ,

  # ============= SM ===============
  'hww2l2v_0jsf_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j SF '   } ,
  'hww2l2v_1jsf_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jsf_cut_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j SF '   } ,
  'hww2l2v_0jof_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j DF '   } ,
  'hww2l2v_1jof_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j DF '   } ,
  'hww2l2v_2jsf_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF '   } ,
  'hww2l2v_2jof_SM'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j DF '   } ,
  'hww2l2v_01j_SM'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SM'   , 'hww2l2v_1jsf_cut_SM' ,
                                                                            'hww2l2v_0jof_shape_SM' , 'hww2l2v_1jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1j SF+DF '   } ,
  'hww2l2v_2j_SM'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_SM'   , 'hww2l2v_2jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF+DF '   } ,
  'hww2l2v_of_SM'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_SM' , 'hww2l2v_1jof_shape_SM' , 'hww2l2v_2jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j DF '   } ,
  'hww2l2v_sf_SM'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SM'   , 'hww2l2v_1jsf_cut_SM'   , 'hww2l2v_2jsf_cut_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF '   } ,
  'hww2l2v_SM'        : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SM'   , 'hww2l2v_1jsf_cut_SM' ,
                                                                            'hww2l2v_0jof_shape_SM' , 'hww2l2v_1jof_shape_SM' ,
                                                                            'hww2l2v_2jsf_cut_SM'   , 'hww2l2v_2jof_shape_SM' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF+DF '   } ,

  # ============= SI125 ===============
  'hww2l2v_0jsf_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j SF '   } ,
  'hww2l2v_1jsf_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jsf_cut_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j SF '   } ,
  'hww2l2v_0jof_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0j DF '   } ,
  'hww2l2v_1jof_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_1jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 1j DF '   } ,
  'hww2l2v_2jsf_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF '   } ,
  'hww2l2v_2jof_SI125'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j DF '   } ,
  'hww2l2v_01j_SI125'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SI125'   , 'hww2l2v_1jsf_cut_SI125' ,
                                                                            'hww2l2v_0jof_shape_SI125' , 'hww2l2v_1jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1j SF+DF '   } ,
  'hww2l2v_2j_SI125'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_2jsf_cut_SI125'   , 'hww2l2v_2jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 2j SF+DF '   } ,
  'hww2l2v_of_SI125'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jof_shape_SI125' , 'hww2l2v_1jof_shape_SI125' , 'hww2l2v_2jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j DF '   } ,
  'hww2l2v_sf_SI125'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SI125'   , 'hww2l2v_1jsf_cut_SI125'   , 'hww2l2v_2jsf_cut_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF '   } ,
  'hww2l2v_SI125'        : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2l2v_0jsf_cut_SI125'   , 'hww2l2v_1jsf_cut_SI125' ,
                                                                            'hww2l2v_0jof_shape_SI125' , 'hww2l2v_1jof_shape_SI125' ,
                                                                            'hww2l2v_2jsf_cut_SI125'   , 'hww2l2v_2jof_shape_SI125' ] ,
                          'purposes' : [ 'himass','himassall' ] , 'legend' : 'HWW 0/1/2j SF+DF '   } ,

}

