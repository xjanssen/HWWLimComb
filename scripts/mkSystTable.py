#!/usr/bin/env python

import sys, re, os, os.path
from optparse import OptionParser

import ROOT
from ROOT import *

import combTools
import batchTools

from Config import *
from copy import deepcopy 
from helperFunctions import *
from string import Template
from collections import OrderedDict 

####################################################################################################

skipFields = ["imax","jmax","kmax","bin","shapes","observation","process","rate","Combination"]
### groupRegex = {
### 		"Wj0b|Wj1b|Wj2b|Zj0b|Zj1b|Zj2b|VVLF|s_Top":"Vj",
### 		"eff_e|eff_m":"eff",
### 		"CAT[0-9]{1}":"CAT",
### 		"sel[A-Z]{3}":"sel",
### 		"mean|sigma":"ms",
### 		"_res|_scale":"JEx",
### 		"top|zjets":"bkg",
### 		"qqH|ggH":"prod1",
### 		"qqh|ggh":"prod3",
### 		"_QCDscale|_pdf":"typ1",
### 		"btag|qgl|trigger":"typ2",
### 		"ANNbin[0-9]{1,2}":"ANN",
### 		"0p|1p|2p":"np",
### 		"VHF|VLF":"typ3",
### 		"Stats1|Stats2":"typ4",
### 		"Err1|Err2":"typ5",
### 		"eff|fake":"efffake",
### 		"ttZ|ttbar|ttbb|ttb|ttcc|VV|ttW|ttH|QCD|VH":"tt",
### 		"bb|cc":"quark",
### 		"7TeV|8TeV":"TeV",
### 		"gg|qg|qqbar":"prod2",
### 		"Loose|Tight":"LT",
### 		"Zee|Zmm":"Zll",
### 		"LowPt|HighPt|MidPt":"Pt",
### 		"bin[0-9]{1,2}":"vhbin",
### 		"Wenu|Wenu2|Wmunu|Wmunu2|Znunu_1|Znunu_2":"Vnu",
### 		#"Wen|Wmn":"Wk",
### 		"Znn|Zll|Wtn":"Zjj",
### 		"SF_1|SF_2":"SF",
### 		}
### groupTranslate = {
### 		("CAT0","CAT1","CAT2","CAT3","CAT4","CAT5","CAT6"):'CAT{0,6}',
### 		("selNOM","selVBF"):"sel{NOM,VBF}",
### 		("mean","sigma"):"{mean,sigma}",
### 		("_res","_scale"):"_{res,scale}",
### 		("ggH","qqH"):"{qqH,ggH}",
### 		("_QCDscale","_pdf"):"_{pdf,QCDscale}",
### 		("top","zjets"):"{top,zjets}",
### 		("Top","Z"):"{Top,Z}",
### 		("btag","qgl","trigger"):"{btag,qgl,trigger}",
### 		("VHF","VLF"):"{VHF,VLF}",
### 		("eff","fake"):"{eff,fake}",
### 		}
### groupSubString = [
### 		"ANNbin",
### 		"p",
### 		"Stats",
### 		"Err",
### 		"bin",
### 		]

####################################################################################################
### def useSubString(array,ss):
### 	if list(array)[0][0:len(ss)] == ss: short = ss+"{"
### 	else: short = "{"
### 	for a in sorted(array):
### 		short += a.replace(ss,'')
### 		short += ","
### 	short = short[:-1]
### 	if list(array)[0][0:len(ss)] == ss: short += "}"
### 	else: short += "}"+ss
### 	return short
### 
### ####################################################################################################
### def matchRegex(r,k):
### 	ntag = 0 
### 	while re.search("(#TAG[0-9]*#).*"*(ntag+1),k):
### 		ntag += 1
### 	if re.search(r,k,re.IGNORECASE):
### 		pre,match,post = re.search('(.{0,})(%s)(.{0,})'%r,k,re.IGNORECASE).groups()
### 		out1 = ''.join([pre,"#TAG%d#"%(ntag),post])
### 		out2 = match
### 	else:
### 		out1 = k
### 		out2 = None
### 	return out1,out2
### 
### ####################################################################################################
### def groupKeys(keys):
### 	groupedKeys = {}
### 	rout = {}
### 	for k in keys:
### 		in1 = k
### 		rfull = ()
### 		#for ri,(r,rv) in enumerate(sorted(groupRegex.iteritems(),key=lambda (x,y):(y))):
### 		for ri,(r,rv) in enumerate(groupRegex.iteritems()):
### 			out1,out2 = matchRegex(r,in1)
### 			if out2: 
### 				rfull = rfull + (rv,)
### 			in1 = out1
### 		in2 = k
### 		#for ri,(r,rv) in enumerate(sorted(groupRegex.iteritems(),key=lambda (x,y):(y))):
### 		for ri,(r,rv) in enumerate(groupRegex.iteritems()):
### 			out3,out4 = matchRegex(r,in2)
### 			if out4:
### 				if not out1 in rout: rout[out1] = OrderedDict() 
### 				if not rv in rout[out1]: rout[out1][rv] = [] 
### 				rout[out1][rv] += [out4]
### 			in2 = out3
### 		if not out1 in groupedKeys: groupedKeys[out1] = [rfull]
### 	for k,v in rout.iteritems():
### 		for k2,v2 in v.iteritems():
### 			groupedKeys[k] += [groupTranslate[tuple(sorted(set(v2)))] if tuple(sorted(set(v2))) in groupTranslate else "".join(set(v2)) if len(set(v2))<2 else useSubString(set(v2),[x for x in groupSubString if x in v2[0]][0]) if any([x in v2[0] for x in groupSubString]) else '{'+','.join(list(sorted(set(v2))))+'}']
### 	overGroupedKeys = []
### 	for k,v in sorted(groupedKeys.iteritems()):
### 		kprint = k
### 		for ii,vi in enumerate(v[1:]): kprint = kprint.replace("#TAG%d#"%ii,vi,1)
### #		print kprint
### 		overGroupedKeys += [kprint]
### 	return overGroupedKeys

####################################################################################################
def parseCard2(card,iComb,iMass,iEnergy):
	f = open(card,'r+')
	fields = []
	fieldsDict = {'CMS_vbfbb':{},'CMS_vhbb':{},'CMS_ttH':{},'nonspecific':{}}
# read
	for line in f.read().split('\n'):
		if line=="" or "-----" in line: continue
		fields += [line.split()]
# sort
	for ii,ifields in enumerate(fields): 
		if ifields[0]=="bin" and fields[ii+1][0]=="observation":
			headBin1  = ifields
			headObs   = fields[ii+1]
		if ifields[0]=="bin" and fields[ii+1][0]=="process":
			headBin2  = ifields
			headProc  = fields[ii+1]
			headProcN = fields[ii+2]
			headRate  = fields[ii+3]
# sort
	for ifields in fields:
		if ifields[0] in skipFields: continue
		addTo='nonspecific'
		for key in fieldsDict.keys():
			if key in ifields[0]: 
				addTo=key
				break
		if not ifields[1] in fieldsDict[addTo]: fieldsDict[addTo][ifields[1]] = []
		fieldsDict[addTo][ifields[1]] += [ifields]
# output
	return fieldsDict,headBin1,headObs,headBin2,headProc,headProcN,headRate

####################################################################################################
### def parseCard(card,iComb,iMass,iEnergy):
### 	f = open(card,'r+')
### 	fields = []
### 	fieldsOut = {}
### # read
### 	for line in f.read().split('\n'):
### 		if line=="": continue
### 		elif "-----" in line: continue
### 		fields += [line.split()[0:2]]
### # sort
### 	for ifield,field in enumerate(sorted(fields)):
### 		tag = "_".join([iComb,str(iMass),iEnergy,field[1]])
### 		if field[0] in skipFields: continue
### 		if not tag in fieldsOut: fieldsOut[tag] = []
### 		fieldsOut[tag] += [field[0]]
### # eliminate duplicates
### 	for k,v in fieldsOut.iteritems():
### 		fieldsOut[k] = list(set(v))
### # output
### 	return fieldsOut 

####################################################################################################
### def printTable(table):
### 	keys = table.keys()
### 	combs    = list(set([x.split('_')[0] for x in keys]))
### 	masses   = list(set([x.split('_')[1] for x in keys]))
### 	energies = list(set([x.split('_')[2] for x in keys]))
### 	keytypes = list(set([x.split('_')[3] for x in keys]))
### 	maxkeys  = len(keytypes)
### 	maxcombs = len(combs) 
### 	combfield = "%%%ds"%(11*maxkeys-1)
### 	
### 	for iEnergy in energies:
### 		for iMass in masses:
### 			tableLine = [""]*(maxcombs*maxkeys) 
### 			tableLocation = {}
### 
### 			print " "*80,"|",																# col1
### 			for iComb in combs: 
### 				print combfield%(iComb+" ("+iEnergy+")"),"|",					# production mode
### 			print	
### 			print " "*80,"|",																# col1
### 			for iiComb,iComb in enumerate(combs):
### 				for iiKey,iKey in enumerate(keytypes): 
### 					print "%10s"%iKey,													# key type
### 					tableLocation[(iComb,iKey)] = iiComb*maxkeys+iiKey
### 				print "|",
### 			print
### 			print "-"*((maxcombs*maxkeys*12) + 82)
### 	
### 			for k,v in sorted(table.iteritems(),key=lambda (x,y):('param' in x,not 'lnN' in x,not 'lnU' in x,not 'shape' in x,x)):
### 				if not iEnergy in k: continue
### 				print k
### 				iComb,iMass,iEnergy,iKey = k.split('_')
### 				vGrouped = groupKeys(v)
### 				for v2 in sorted(vGrouped):
### 					thisLine = deepcopy(tableLine)
### 					thisLocation = tableLocation[(iComb,iKey)]
### 					thisLine[thisLocation] = "x"
### 					print "%80s |"%v2,
### 					for ientry,entry in enumerate(thisLine): 
### 						print "%10s"%entry,												# actual line
### 						if ientry+1 in range(0,maxkeys*maxcombs+1,maxkeys): print "|",
### 					print
### 				print "-"*((maxcombs*maxkeys*12) + 82)
### 		print
### 
####################################################################################################

parser = OptionParser(usage="usage: %prog [options] comb")

parser.add_option("-c", "--combs",      dest="combs",       help="Produce all combinations", default=[], type='string' , action='callback' , callback=combTools.list_maker('combs',','))
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-M", "--models",     dest="models",      help="Physics Model (OneHiggs,TwoHiggs,NoModel , ... )", default=['OneHiggs'], type='string' , action='callback' , callback=combTools.list_maker('models',','))
#parser.add_option("-P", "--purpose",    dest="purpose",     help="purpose of the datacard (couplings, searches, mass, ...)", default="searches", metavar="PATTERN")
parser.add_option("-e", "--energy",     dest="energy",      help="energy (7,8,0=all)",             type="int", default="0", metavar="SQRT(S)")
parser.add_option("-m", "--masses",     dest="masses",      help="Run only these mass points", default=[]      , type='string' , action='callback' , callback=combTools.list_maker('masses',',',float))
parser.add_option("-b", "--batch"  ,    dest="runBatch",    help="Run in batch",                   default=False, action="store_true")
parser.add_option("-S", "--batchSplit", dest="batchSplit",  help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=combTools.list_maker('batchSplit',','))
parser.add_option("-v", "--version",    dest="Version",     help="Datacards version" , default=DefaultVersion ,  type='string' )
parser.add_option("-d", "--dictionary", dest="Dictionary",  help="Datacards Dictionary", default='Configs.HWW2012' , type='string' )

(options, args) = parser.parse_args()

# Read Combination python config
exec('from %s import *'%(options.Dictionary))
#print DefaultVersion
if options.Version == 'None' : options.Version=DefaultVersion

print '==== Data Cards Version : ',options.Version
combList      = combTools.CombList_Filter(combinations,options.combs).get()
energyList    = combTools.EnergyList_Filter(options.energy).get()
PhysModelList = combTools.PhysModelList_Filter(physmodels,options.models).get()

####################################################################################################

table = {}

for iComb in combList:
	print "\n\n"
	info(0,"Combination:",iComb)
	for iModel in PhysModelList:
		info(1,"Model:",iModel)
		cardDir       = combTools.CardDir_Filter(cardtypes,physmodels[iModel]['cardtype']).get() 
		if 'targetdir' in cardtypes[physmodels[iModel]['cardtype']]: TargetDir=workspace+options.Version+'/'+cardtypes[physmodels[iModel]['cardtype']]['targetdir']+'/'+iComb
		else:                                                        TargetDir=workspace+options.Version+'/'+cardDir+'/'+iComb
	
	 	massList  = combTools.MassList_Filter(cardtypes,channels[options.Version],combinations,physmodels[iModel]['cardtype'],options.masses,iComb,energyList).get()
		info(2,"MassList:",massList)
		paramSet   = combTools.ParamSet_Maker(cardtypes,channels[options.Version],physmodels[iModel]['cardtype'],options.masses,'NONE',energyList).get()
		for iSet in range(0,len(paramSet['values'])):
			iMass = paramSet['values'][iSet][0]
			for iEnergy in energyList:
				for iChannel in  combinations[iComb]['channels']:
					if (iEnergy in channels[options.Version][iChannel]):
						if (iMass >= channels[options.Version][iChannel][iEnergy]['mrange'][0]) and (iMass <= channels[options.Version][iChannel][iEnergy]['mrange'][1]): 
							#info(3,"Channel:",iChannel,"@ Energy:",iEnergy)
							info(3,"Energy:",iEnergy)
	      
							card = iComb
							for iPar in range(1,len(paramSet['names'])):
								parVal=str(paramSet['values'][iSet][iPar])
								parVal = parVal.replace('.','d')
								for iRule in paramSet['rules']: parVal = parVal.replace(iRule,paramSet['rules'][iRule])
								card += '_' + paramSet['names'][iPar] + '_' + parVal
							if options.energy != 0: card += '_' + str(options.energy) + 'TeV'
							card += ".txt"
							card = "/".join([TargetDir,str(iMass),card])
	
							if os.path.exists(card):
								info(4,card)
###								subTable = parseCard(card,iComb,iMass,iEnergy)
###								for k,v in subTable.iteritems():
###									if not k in table:
###										table[k] = v
###									else:
###										for v2 in v:
###											if not v2 in table[k]: table[k] += [v2]
###											#else: error(v2,"exists in sub-table",k)
								cardDicts,hBin1,hObs,hBin2,hProc,hProcN,hRate = parseCard2(card,iComb,iMass,iEnergy)
								for k0,cardDict in sorted(cardDicts.iteritems(),key=lambda (x,y):(not 'nonspecific' in x)):
									print '='*180
									# loop type
									for k,v in sorted(cardDict.iteritems()):
										print '='*75
										info(1,k,'(%s)'%k0)	
										# loop elements
										for v2 in sorted(v): 
											print "%s%-55s%s"%(bold,v2[0],defcol),
											ip=0
											for i in range(2,len(v2)):
												if not v2[i]=="-": 
													if v2[1]=='lnN' or v2[1]=='lnU': 
														out = "%s > %s (%s),"%(hBin2[i-1].replace('hbbbb_8TeV','').strip('_'),hProc[i-1],v2[i])
														print "%50s"%out.strip(),
														ip += 1
													elif v2[1]=='shape' or v2[1]=='shape?':
														out = "%s > %s"%(hBin2[i-1].replace('hbbbb_8TeV','').strip('_'),hProc[i-1])
														if not float(v2[i])==1.0: out += " (%s)"%v2[i]
														print "%50s"%out.strip(),	
														ip += 1
													else:
														print "%15s"%v2[i].strip(),
													if ip>3: 
														print "\n%55s"%"",	
														ip=0
											print 
										print 
								print '='*180
					break
###
###		printTable(table)

	print "\n\nDone.\n"

