#!/usr/bin/env python


cardbase    = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/'
combscripts = '/afs/cern.ch/work/x/xjanssen/cms/HWW2012/HWWLimComb/cmshcg/trunk/highmass2014/scripts/'

DefaultVersion = 'VBFBB'
channels = {

'VBFBB' : {

  'vbfbb' :{
             '8TeV' : { 'tag' : 'vbfbb' , 'prod' : 'qqH' , 'branch' : 'hbb' , 'decay' : 'bb' , 'energy' : 8 , 'method' : 'fit' , 'mrange' : [115 ,135] ,
             'dir' : 'cmshcg/trunk/cadi/HIG-14-004' , 'subdir' : 'vbfbb/$MASS' , 'card' : 'vbfbb_8TeV.txt'  } ,
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

} 
