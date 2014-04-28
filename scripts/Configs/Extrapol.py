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
                                           600 : [580] ,
                                           700 : [650] ,
                                           800 : [750] ,
                                           900 : [850] ,
                                           1000: [950]  
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
                                           600 : [580] ,
                                           700 : [650] ,
                                           800 : [750] ,
                                           900 : [850] ,
                                           1000: [950]  
                                        } , 
                             },
                   'HiMassEff' : {
                               '7TeV' : {
                                           150 : { 0: { 'From' : [150,150] , 'To' : [145,146,147,148,149]  }, 
                                                   1: { 'From' : [150,160] , 'To' : [151,152,153,154,155,] }, },
                                           160 : { 0: { 'From' : [150,160] , 'To' : [156,157,158,159] }, },
                                           170 : { 0: { 'From' : [160,170] , 'To' : [165] }, },
                                           180 : { 0: { 'From' : [170,180] , 'To' : [175] }, },
                                           190 : { 0: { 'From' : [180,190] , 'To' : [185] }, },
                                           200 : { 0: { 'From' : [190,200] , 'To' : [195] }, 
                                                   1: { 'From' : [200,200] , 'To' : [205,210,215,220] }, },
                                           250 : { 0: { 'From' : [200,250] , 'To' : [225,230,235,240,245] },  
                                                   1: { 'From' : [250,250] , 'To' : [255,260,265,270]      }, },
                                           300 : { 0: { 'From' : [300,300] , 'To' : [275,280,285,290,295] }, 
                                                   1: { 'From' : [300,350] , 'To' : [310,320] }, },
                                           350 : { 0: { 'From' : [300,350] , 'To' : [330,340] }, 
                                                   1: { 'From' : [350,400] , 'To' : [360,370] }, },
                                           400 : { 0: { 'From' : [350,400] , 'To' : [380,390] }, 
                                                   1: { 'From' : [400,450] , 'To' : [420]     }, },
                                           450 : { 0: { 'From' : [400,450] , 'To' : [440] }, 
                                                   1: { 'From' : [450,500] , 'To' : [460] }, },
                                           500 : { 0: { 'From' : [450,500] , 'To' : [480] }, 
                                                   1: { 'From' : [500,550] , 'To' : [520] }, },
                                           550 : { 0: { 'From' : [500,550] , 'To' : [540] }, 
                                                   1: { 'From' : [550,600] , 'To' : [560] }, },
                                           600 : { 0: { 'From' : [550,600] , 'To' : [580] } },
                                           700 : { 0: { 'From' : [700,700] , 'To' : [650] } },
                                           800 : { 0: { 'From' : [700,800] , 'To' : [750] } },
                                           900 : { 0: { 'From' : [800,900] , 'To' : [850] } },
                                           1000: { 0: { 'From' : [900,1000], 'To' : [950] } },
                                        } ,
                               '8TeV' : {
                                           145 : { 0: { 'From' : [145,150] , 'To' : [146,147] }, },
                                           150 : { 0: { 'From' : [145,150] , 'To' : [148,149] }, 
                                                   1: { 'From' : [150,155] , 'To' : [151,152] }, },
                                           155 : { 0: { 'From' : [150,155] , 'To' : [153,154] },
                                                   1: { 'From' : [155,160] , 'To' : [156,157] }, },
                                           160 : { 0: { 'From' : [155,160] , 'To' : [158,159] }, },  
                                           170 : { 0: { 'From' : [160,170] , 'To' : [165] }, },
                                           180 : { 0: { 'From' : [170,180] , 'To' : [175] }, },
                                           190 : { 0: { 'From' : [180,190] , 'To' : [185] }, },
                                           200 : { 0: { 'From' : [190,200] , 'To' : [195] },
                                                   1: { 'From' : [200,250] , 'To' : [205,210,215,220] }, },
                                           250 : { 0: { 'From' : [200,250] , 'To' : [225,230,235,240,245] },
                                                   1: { 'From' : [250,250] , 'To' : [255,260,265,270]      }, },
                                           300 : { 0: { 'From' : [300,300] , 'To' : [275,280,285,290,295] },
                                                   1: { 'From' : [300,350] , 'To' : [310,320] }, },
                                           350 : { 0: { 'From' : [300,350] , 'To' : [330,340] },
                                                   1: { 'From' : [350,400] , 'To' : [360,370] }, },
                                           400 : { 0: { 'From' : [350,400] , 'To' : [380,390] },
                                                   1: { 'From' : [400,450] , 'To' : [420]     }, },
                                           450 : { 0: { 'From' : [400,450] , 'To' : [440] },
                                                   1: { 'From' : [450,500] , 'To' : [460] }, },
                                           500 : { 0: { 'From' : [450,500] , 'To' : [480] },
                                                   1: { 'From' : [500,550] , 'To' : [520] }, },
                                           550 : { 0: { 'From' : [500,550] , 'To' : [540] },
                                                   1: { 'From' : [550,600] , 'To' : [560] }, },
                                           600 : { 0: { 'From' : [550,600] , 'To' : [580] } },
                                           700 : { 0: { 'From' : [700,700] , 'To' : [650] } },
                                           800 : { 0: { 'From' : [700,800] , 'To' : [750] } },
                                           900 : { 0: { 'From' : [800,900] , 'To' : [850] } },
                                           1000: { 0: { 'From' : [900,1000], 'To' : [950] } },
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
