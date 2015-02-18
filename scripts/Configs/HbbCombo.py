#!/usr/bin/env python


cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'HbbCombo'
channels = {

'HbbCombo' : {

  'vbfbb' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
             'dir' : 'cmshcg/trunk/cadi/HIG-14-004' , 'subdir' : 'vbfbb/$MASS' , 'card' : 'vbfbb_8TeV.txt'  } ,
           } ,

#vhbb_Wln_7TeV.txt  
#vhbb_Zll_7TeV.txt  
#vhbb_Znn_7TeV.txt

# vhbb_Wln_8TeV.txt  
# vhbb_Wtn_8TeV.txt  
# vhbb_Zll_8TeV.txt  
# vhbb_Znn_8TeV.txt

  'vhbb_Wln':{
              '7TeV' : { 'tag' : 'vhbb_Wln' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 7 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Wln_7TeV.txt'  } ,
              '8TeV' : { 'tag' : 'vhbb_Wln' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Wln_8TeV.txt'  } ,
             }, 

  'vhbb_Wtn':{
              '8TeV' : { 'tag' : 'vhbb_Wtn' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Wtn_8TeV.txt'  } ,
             },

  'vhbb_Zll':{
              '7TeV' : { 'tag' : 'vhbb_Zll' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 7 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Zll_7TeV.txt'  } ,
              '8TeV' : { 'tag' : 'vhbb_Zll' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Zll_8TeV.txt'  } ,
             },

  'vhbb_Znn':{
              '7TeV' : { 'tag' : 'vhbb_Znn' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 7 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Znn_7TeV.txt'  } ,
              '8TeV' : { 'tag' : 'vhbb_Znn' , 'prod' : 'VH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
              'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'vhbb/$MASS' , 'card' : 'vhbb_Znn_8TeV.txt'  } ,
             },

  'tthbb' :{
             '7TeV' : { 'tag' : 'tthbb' , 'prod' : 'ttH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 7 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
             'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'tth/125' , 'card' : 'ttH_7TeV.txt'  } ,
             '8TeV' : { 'tag' : 'tthbb' , 'prod' : 'ttH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
             'dir' : 'cmshcg/trunk/summer2013' , 'subdir' : 'tth/125' , 'card' : 'ttH_hbb_8TeV.txt'  } ,
           } ,

 }
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

#
# VHBB
#

  'vhbb'  :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'vhbb_Wln' , 'vhbb_Wtn' , 'vhbb_Zll' , 'vhbb_Znn' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                          'legend'   : 'VH #rightarrow b#bar{b}'
                        } ,

#
# ttHbb
#

 'tthbb'  :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'tthbb' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                          'legend'   : 'ttH #rightarrow b#bar{b}'
                        } ,
  
#
# HBB
#

  'hbb'  :
                        {
                          'energies' : [ '7TeV' , '8TeV' ] ,
                          'channels' : [ 'vbfbb' , 'vhbb_Wln' , 'vhbb_Wtn' , 'vhbb_Zll' , 'vhbb_Znn' , 'tthbb' ] ,
                          'purposes' : [ 'searches' , 'couplings' , 'wjetfix' , 'sminject' , 'smtoys' , 'smhiggs' ] ,
                          'legend'   : 'H #rightarrow b#bar{b}'
                        } ,


} 
