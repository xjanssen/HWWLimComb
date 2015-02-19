#!/usr/bin/env python

homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWWLimComb/'
workspace   = homedir+'workspace/'
jobdir      = homedir+'jobs/'
crabdir     = homedir+'crab/'
plotsdir    = homedir+'plots/'

cardbase    = homedir+'cmshcg/trunk/'
combscripts = homedir+'cmshcg/trunk/summer2013/scripts/'

# Load Basic Disctionary
from Configs.CardTypes  import *
from Configs.PhysModels import *
from Configs.preProc    import *
from Configs.Extrapol   import *
from Configs.Targets    import *

# Empty Dictionary: Filled afterwards 
DefaultVersion   = 'None'
channels         = {}
combinations     = {}

# Plot Axis range et al.
plotStyle = {

  'Limit' :
     {
       #'Default'        : { 'linY' : [0.0 ,50.] , 'logY' : [0.01,500.] } ,
       'Default'        : { 'linY' : [0.0 ,50.] , 'logY' : [0.1,5000.] } ,
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
       'hbb'          : { 'linY' : [0.0 ,6.] , 'logY' : [0.05,100.] } ,
       'vhbb'          : { 'linY' : [0.0 ,6.] , 'logY' : [0.05,100.] } ,
       'tthbb'          : { 'linY' : [0.0 ,15.] , 'logY' : [0.05,100.] } ,
       'vbfbb'          : { 'linY' : [0.0 ,15.] , 'logY' : [0.05,100.] } ,
       'vbfbbsplit'          : { 'linY' : [0.0 ,15.] , 'logY' : [0.05,100.] } ,
       'hww2l2v_01jof_EWKS' :  {'linY' : [0.0 ,15.] , 'logY' : [0.5,100.] } ,
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
       'hbb'          : { 'linY' : [0.0 ,6.] , 'logY' : [0.05,100.] } ,
     },
  'Sign'  :
     {
       'Default'        : { 'linY' : [0.0 ,25.] , 'logY' : [0.1,200.] } ,
       'vbfbb'          : { 'linY' : [0.0 , 1.] , 'logY' : [0.01,5.]  } ,
       'hbb'          : { 'linY' : [0.0 , 5.] , 'logY' : [0.01,5.]  } ,
       'vbfbbsplit'          : { 'linY' : [0.0 , 1.] , 'logY' : [0.01,5.]  } ,
     }

}
