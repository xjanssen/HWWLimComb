from ROOT import TFile, TH1D, TCanvas, TChain, THStack, TLegend, TGraph, TLine, TMultiGraph, TLatex
from array import array
import rootlogonTDR


def file2map(x):
        ret = {}; headers = []
        for x in open(x,"r"):
            cols = x.split()
            if len(cols) < 2: continue
            if "mH" in x:
                headers = [i.strip() for i in cols[1:]]
            else:
                fields = [ float(i) for i in cols ]
                ret[fields[0]] = dict(zip(headers,fields[1:]))
        return ret

def test():

    iEnergy='8TeV'
    cLimits = TCanvas('limits')
    cLimits.cd()
    path   = '/afs/cern.ch/work/x/xjanssen/cms/vbfHbbCards/CMSSW_6_1_1'+'/src/HiggsAnalysis/CombinedLimit/data/'
    xs_ggH = file2map(path+'lhc-hxswg/sm/xs/'+iEnergy+'/'+iEnergy+'-ggH.txt')

    #print xs_ggH
    n=len(xs_ggH.keys())
    x=[]
    y=[]
    for iMass in sorted(xs_ggH.keys()):
      x.append(iMass)
      y.append(xs_ggH[iMass]['XS_pb'])

    gr = TGraph(n,array('f',x),array('f',y));
    gr.Draw("AC*");
    cLimits.WaitPrimitive()

test()
