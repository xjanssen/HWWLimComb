#!/usr/bin/env python

#homedir     = '/afs/cern.ch/work/s/salderwe/private/2014/biasTF/HWWLimComb/'
homedir     = '/afs/cern.ch/work/x/xjanssen/cms/HWWLimComb/'

workspace   = homedir+'workspace/'
jobdir      = homedir+'jobs/'
plotsdir    = homedir+'plots/'
cardbase    = homedir+'datacards/'
#combscripts = homedir+'cmshcg/trunk/summer2013/scripts/'

DefaultVersion = 'VBFHBB_Sara_v3'
channels = {

  'VBFHBB_Sara_v3' : {


   # Constrained TF (POL1 for fit) + Bernstein 4 and 5 

              'vbfhbb_pol1_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL1.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol1_prk' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_POL1.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol1_cat5' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto5_POL1.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol1_cat6' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto6_POL1.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,


   # Constrained TF (POL2 for fit) + Bernstein 4 and 5 

              'vbfhbb_pol2_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL2.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol2_prk' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_POL2.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol2_cat5' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto5_POL2.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol2_cat6' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto6_POL2.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,


   # Constrained TF (POL3 for fit) + Bernstein 4 and 5 

              'vbfhbb_pol3_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL3.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol3_prk' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_POL3.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,



              'vbfhbb_pol3_cat5' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto5_POL3.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

              'vbfhbb_pol3_cat6' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATveto6_POL3.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

   # Constrained TF (POL1 for fit) + Bernstein 4 and 5 + merged 56

              'vbfhbb_pol1_prkmerged' :{
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' ,
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATmerge56_POL1.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        },
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }
                                         } ,
                                 } ,

   # Constrained TF (POL2 for fit) + Bernstein 4 and 5 + merged 56

              'vbfhbb_pol2_prkmerged' :{
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' ,
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATmerge56_POL2.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        },
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }
                                         } ,
                                 } ,

   # Constrained TF (POL3 for fit) + Bernstein 4 and 5 + merged56

              'vbfhbb_pol3_prkmerged' :{
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' ,
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT4-CAT6_CATmerge56_POL3.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        },
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_CATmerge56_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }
                                         } ,
                                 } ,
  
  # "free" TF (POL1 for fit) + Bernstein 4 and 5

              'vbfhbb_pol1_freeTF_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL1_freeTF.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,

  # "free" TF (POL2 for fit) + Bernstein 4 and 5

              'vbfhbb_pol2_freeTF_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL2_freeTF.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,


  # "free" TF (POL3 for fit) + Bernstein 4 and 5

              'vbfhbb_pol3_freeTF_nom' :{ 
                                '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 
                                           'mrange' : [115,135] ,
                                           'dir' : '.' , 'subdir' : '.' , 'card' : 'datacard_m$MASS_BRN5+4_CAT0-CAT3_POL3_freeTF.txt' ,
                                           'altlegend': {
                                                         'ALT1'     : 'Pol1 TF + Fix Bernstein',
                                                         'ALT2'     : 'Pol2 TF + Fix Bernstein',
                                                         'ALT3'     : 'Pol3 TF + Fix Bernstein',
                                                         'ALT4'     : 'Exp. TF + Fix Bernstein',
                                                        }, 
                                           'altmodel' : {
                                                         'ALT1'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:qcd_model_ALT1_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT1.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT2'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:qcd_model_ALT2_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT2.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT3'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:qcd_model_ALT3_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT3.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                         'ALT4'     : { 'qcd'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:qcd_model_ALT4_$CHANNEL' ],
                                                                        'data_obs' : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:data_hist_$CHANNEL'      ],
                                                                        'top'      : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Top_model_$CHANNEL'      ],
                                                                        'zjets'    : ['*','data_shapes_workspace_BRN5+4_ALT4.root','w:Z_model_$CHANNEL'        ],
                                                                      } ,
                                                        }   
                                         } ,    
				 } ,



		}
  }

combinations = {

# Contrained TF + Bernstein 4 and 5

                'vbfhbb_pol1_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol1_prk' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_prk' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol1_cat5' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_cat5' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol1_cat6' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_cat6' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,




# Contrained TF + Bernstein 4 and 5

                'vbfhbb_pol2_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol2_prk' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_prk' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol2_cat5' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_cat5' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol2_cat6' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_cat6' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,




 # Contrained TF + Bernstein 4 and 5 
	
                'vbfhbb_pol3_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol3_prk' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_prk' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

	       'vbfhbb_pol3_cat5' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_cat5' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol3_cat6' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_cat6' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,


 # Contrained TF + Bernstein 4 and 5


                'vbfhbb_pol1_prkmerged' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_prkmerged' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,


                'vbfhbb_pol2_prkmerged' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_prkmerged' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,




                'vbfhbb_pol3_prkmerged' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_prkmerged' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

# Free TF + Bernstein 4 and 5

                'vbfhbb_pol1_freeTF_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol1_freeTF_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol2_freeTF_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol2_freeTF_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,

                'vbfhbb_pol3_freeTF_nom' : {
                        'energies' : [ '8TeV' ] ,
                        'channels' : [ 'vbfhbb_pol3_freeTF_nom' ] ,
                        'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                        'legend'   : 'vbf H #rightarrow b#bar{b}'
                       } ,






}

