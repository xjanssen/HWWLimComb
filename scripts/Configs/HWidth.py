#!/usr/bin/env python


cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/HWidth/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'HWidth'
channels = {

'HWidth' : {

  'hwidth_hww0jof_shape' : {
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  , 
                               'dir' : 'datacards' , 'subdir' : '.' , 'card' : 'hww-19.47fb.mH125.of_0j_shape.txt'  } ,
                    } ,

  'hwidth_hww0jof_shape_kFac' : {
                    '8TeV' : { 'tag' : 'of0j' , 'prod' : 'ggH' , 'branch' : 'hww' , 'decay' : '2l2v' , 'energy' : 8 , 'method' : 'shape' , 'mrange' : [123,127]  , 
                               'dir' : 'datacards' , 'subdir' : '.' , 'card' : 'hww-19.47fb.mH125.of_0j_shape_kFac.txt'  } ,
                    } ,



 }
}

combinations = {

#
# HWidth
#
   'hwidth_hww0j' :
                        {
                          'energies' : [ '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'HWW 0j'
                        } ,

   'hwidth_hww0j_kFac' :
                        {
                          'energies' : [ '8TeV' ] ,
                          'channels' : [ 'hwidth_hww0jof_shape_kFac' ] ,
                          'purposes' : [ 'smhiggs' , 'hwidth' ] ,
                          'legend'   : 'HWW 0j'
                        } ,



} 
