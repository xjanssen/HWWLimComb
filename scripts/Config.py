#!/usr/bin/env python

workspace = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/workspace/'
jobdir    = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/jobs/'
plotsdir  = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/plots/'
cardbase  = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/'


cardtypes = {
  'couplings' : { 'dir' : 'couplings' , 'masses' : [125,125.8] } ,
  'smhiggs'   : { 'dir' : 'smhiggs'   , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] } ,
  'searches'  : { 'dir' : 'searches'   , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 450, 500, 550, 600] } ,
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 500, 600] } ,
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250 , 300 ] } ,
# 'searches'  : { 'dir' : 'searches'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200 ] } ,
  'custom'    : { 'dir' : 'couplings' , 'masses' : [125] } , 
  'wjetfix'   : { 'dir' : 'searches'  , 'targetdir' : 'wjetfix' , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 500, 600] , 'preProc' : ['WJetFix'] } , 
  'sminject'  : { 'dir' : 'searches'  , 'targetdir' : 'sminject', 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 500, 600] , 'preProc' : ['SMInject'] } ,
  'smtoys'    : { 'dir' : 'searches'  , 'targetdir' : 'smtoys'  , 'masses' : [110, 115, 120, 125, 130, 135, 140, 150, 160, 170, 180, 190, 200, 250, 300, 350, 400, 500, 600] , 'preProc' : ['SMToys'] } ,
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

channels = { 

# ============ V1: Cards for HWW Paper ==========================

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
  #                  '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_cut_8TeV.txt'}   
  #                  } ,
  #'hww1jof_cut' :   {
  #                  '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_cut_8TeV.txt'}
  #                  } ,
  'hww0jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_0j_cut_8TeV.txt' }
                    } ,
  'hww1jsf_cut' :   {
                    '7TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_7TeV.txt'} ,
                    '8TeV' : { 'tag' : 'sf1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'cut' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwsf_1j_cut_8TeV.txt'}
                    } ,
  # ============ H -> WW 0/1-jet 2D shapes =================
  'hww0jof_shape' : {
                    '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_7TeV.txt' , 'files' : ['hwwof_0j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_shape_8TeV.txt' , 'files' : ['hwwof_0j.input_8TeV.root'] }
                    } ,
  'hww1jof_shape'  : {
                    '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_7TeV.txt' , 'files' : ['hwwof_1j.input_7TeV.root'] } ,
                    '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_shape_8TeV.txt' , 'files' : ['hwwof_1j.input_8TeV.root'] }
                    } , 
  # ============ H -> WW 0/1-jet Mr Fit =================
  # 'hww0jof_mrfit'  : {
  #                  '7TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_mrfit_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_0j_mrfit_8TeV.txt'}
  #                } ,
  # 'hww1jof_mrfit'  : {
  #                  '7TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 7 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_mrfit_7TeV.txt'} ,
  #                  '8TeV' : { 'tag' : 'of1j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'mrfit' , 'mrange' : [110,600]  , 'dir' : 'summer2013' , 'subdir' : 'hww2l2v/$MASS' , 'card' : 'hwwof_1j_mrfit_8TeV.txt'}
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
                    '7TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_7TeV.txt' , 'files' : ['vh3l1_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'sssf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l1_shape_8TeV.txt' , 'files' : ['vh3l1_input_8TeV.root'] } 
                    } ,
  'vh3l_ossf_shape' :  {
                    '7TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 7 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_7TeV.txt' , 'files' : ['vh3l2_input_7TeV.root'] } ,  
                    '8TeV' : { 'tag' : 'ossf'  , 'prod' : 'VH' , 'branch' : 'hww' , 'decay' : 'vh3l' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [110,200] , 'dir' : 'summer2013' , 'subdir' : 'vhww/$MASS', 'card' : 'vh3l2_shape_8TeV.txt' , 'files' : ['vh3l2_input_8TeV.root'] } 
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
 'hww0jof'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [                 'hww0jof_shape' ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys'  , 'smhiggs'] , 'legend' : 'HWW 0-jet (DF)'} ,

#
# Single channel (as in PASes/ paper section)
#
  'hww0jet_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_shape' ] ,                                   'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0-jet (2d)'    } ,
  'hww0jet_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww0jof_cut'   ] ,                                   'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0-jet (Cut)'   } ,
  'hww1jet_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww1jsf_cut' , 'hww1jof_shape' ] ,                                   'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 1-jet (2d)'    } ,
  'hww1jet_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww1jsf_cut' , 'hww1jof_cut'   ] ,                                   'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 1-jet (Cut)'   } ,
  'hww01jet_shape' : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_shape' , 'hww1jof_shape' ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0/1-jet (2d)'  } ,
  'hww01jet_cut'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww0jsf_cut' , 'hww1jsf_cut' , 'hww0jof_cut'   , 'hww1jof_cut'   ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 0/1-jet (Cut)' } ,
  'hww2j_hcp'      : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2j_hcp' , 'hww2jsf_hcp' , 'hww2jof_hcp' ] ,                       'purposes' : [ 'searches' , 'couplings' ] , 'legend' : 'HWW 2j (HCP)' } ,
  'hww2j_cut'      : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jof_cut' , 'hww2jsf_cut' ]  ,                                    'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 2j (Cut)'      } , 
  'hww2j_shape'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hww2jof_shape' , 'hww2jsf_cut' ]  ,                                  'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'HWW 2j (Shape)'    } , 
  'vh3l_cut'       : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'vh3l_sssf_cut'    , 'vh3l_ossf_cut'    ] ,                           'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 3l (Cut)'     } ,
  'vh3l_shape'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'vh3l_sssf_shape'  , 'vh3l_ossf_shape'  ] ,                           'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 3l (Shape)'   } ,
  'hwwvh2j_cut'    : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hwwvh2jsf_cut' , 'hwwvh2jof_cut' ] ,                                 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 2-jet (cut)'  } ,
  'hwwvh2j_shape'  : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'hwwvh2jsf_shape' , 'hwwvh2jof_shape' ] ,                             'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'VHWW 2-jet (Shape)'} ,
  'zh3l2j_cut'     : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'zh3l2j_eee_cut'  , 'zh3l2j_eem_cut'  , 'zh3l2j_emm_cut'  , 'zh3l2j_mmm_cut'   ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'ZHWW 3l2j (Cut)'  } ,
  'zh3l2j_shape'   : { 'energies' : [ '7TeV' , '8TeV' ] , 'channels' : [ 'zh3l2j_eee_shape', 'zh3l2j_eem_shape', 'zh3l2j_emm_shape', 'zh3l2j_mmm_shape' ] , 'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] , 'legend' : 'ZHWW 3l2j (Shape)'} ,

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
                          'legend'   : '0/1/2-jet + VH3l + VH2j (Cut)'
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
                          'legend'   : '0/1/2-jet + VH3l + VH2j (Shape)'
                        } ,

}

physmodels = {
  'NoModel'  : { 'cardtype' : 'couplings' } ,
  'SMHiggs'  : { 'cardtype' : 'smhiggs'   } ,
  'MH125BG'  : { 'cardtype' : 'searches'  } ,
#
  'OneHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:justOneHiggs'            , 'cardtype' : 'searches' } ,
  'TwoHiggs' : { 'model' : 'HiggsAnalysis.CombinedLimit.TwoHiggsModels:twoHiggsUnconstrained'   , 'cardtype' : 'searches' } ,
#
  'SMInject' : { 'cardtype' : 'sminject' } ,
  'SMToys'   : { 'cardtype' : 'smtoys' } ,
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
  'SObsSMToysNoSyst' : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
                                              'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 500 } ,
                                              'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'SObsSMToysNoSyst50' : { 'notblind' : True  , 'method' : 'ProfileLikelihood' , 'options' : '-v 2 --signif --minimizerAlgo=Minuit' , 
                                              'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 50 } ,
                                              'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  #
  # Limits: Standard
  #
  'ACLsObs'      : { 'notblind' : False , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'treeKeys' : ['Val'] } ,
  'ACLsExp'      : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run expected' , 'treeKeys' : ['95D','68D','Val','68U','95U'] } ,
  'ACLsInjPre'   : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1' },
  'ACLsInjPost'  : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed -t -1 --expectSignal=1 --toysFreq' },
  'ACLsSMToysNoSyst' : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 500 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  'ACLsSMToysNoSyst50' : { 'notblind' : True  , 'method' : 'Asymptotic' , 'options' : '-v 2 --run observed' , 'Toys' : { 'Model' : 'SMToys' , 'Target' : 'ToysNoSyst' , 'NToysJob' : 50 } ,
                         'quantile' :  {'95D':0.025,'68D':0.16,'Val':0.5,'68U':0.84,'95U':0.975} },
  #
  # BestFit
  #
  #'BestFit'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-2 --rMax=4 --robustFit=1 --X-rtd FITTER_DYN_STEP ' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  #'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --rMin=-2 --rMax=4 --robustFit=1 --X-rtd FITTER_DYN_STEP -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFit'      : { 'notblind' : False , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit --rMin=-2 --rMax=4' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  'BestFitExp'   : { 'notblind' : True  , 'method' : 'MaxLikelihoodFit' , 'options' : '-v 2 --stepSize=0.05 --preFitValue=0.1 --robustFit=1 --X-rtd FITTER_NEW_CROSSING_ALGO --minimizerAlgoForMinos=Minuit2 --minimizerToleranceForMinos=0.01 --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --minimizerAlgo=Minuit2 --minimizerStrategy=1 --minimizerTolerance=0.0001 --cminFallbackAlgo Minuit,0.001 --justFit --rMin=-2 --rMax=4 -t -1 --expectSignal=1' , 'method' : 'MaxLikelihoodFit' , 'treeKeys' : ['Val','68D','68U'] },
  #
  # Toys
  # 
  'ToysNoSyst'    : { 'notblind' : True  , 'method' : 'GenerateOnly' , 'options' : '-t 500 --toysNoSystematics --saveToys --expectSignal=1 -s -1' , 'NJobs' : 10 },
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
}

toys = {
  'SExp'        : { },
}



