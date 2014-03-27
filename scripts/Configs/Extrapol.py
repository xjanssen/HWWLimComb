#!/usr/bin/env python

extrapolations = { 'LoMass'  : {
                               #125 : [125.5,126,126.5,127] ,
                               #130 : [129.5,129,128.5,128,127.5] ,
                               125 : [124.5,124.6,124.7,124.8,124.9,125.1,125.2,125.3,125.4,125.5,125.6,125.7,125.8,125.9,126,126.1,126.2,126.3,126.4,126.5,127],
                               #125 : [127]
                             } ,
                   'HiMass': {
                               '7TeV' : { 
                                           150 : [145,146,147,148,149,151,152,153,154] ,
                                           160 : [155,156,157,158,159] ,  
                                           170 : [165] ,
                                           180 : [175] ,
                                           190 : [185] ,
                                           200 : [195,205,210,215,220] ,
                                           250 : [225,230,235,240,245,255,260,265,270] ,
                                           300 : [275,280,285,290,295,310,320] ,
                                           350 : [330,340,360,370] ,
                                           400 : [380,390,420] ,
                                           450 : [440,460] ,
                                           500 : [480,520] ,
                                           550 : [540,560] ,
                                           600 : [580]
                                        } ,
                               '8TeV' : {
                                           145 : [146,147] ,
                                           150 : [148,149,151,152], 
                                           155 : [153,154,156,157] ,
                                           160 : [158,159] ,
                                           170 : [165] ,
                                           180 : [175] ,
                                           190 : [185] ,
                                           200 : [195,205,210,215,220] ,
                                           250 : [225,230,235,240,245,255,260,265,270] ,
                                           300 : [275,280,285,290,295,310,320] ,
                                           350 : [330,340,360,370] ,
                                           400 : [380,390,420] ,
                                           450 : [440,460] ,
                                           500 : [480,520] ,
                                           550 : [540,560] ,
                                           600 : [580]
                                        } , 
                             },
                   '13TeV' : {
                               'Energy' : '8TeV' ,
                               'Lumi'   : {
                                           'Origin'  : 19.4 ,
                                           'Targets' : [30,120,300,3000] ,
                                          } ,

                             } ,
                 }