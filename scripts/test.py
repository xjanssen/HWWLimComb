from ROOT import TFile, TH1D, TCanvas, TChain, THStack, TLegend, TGraph, TLine, TMultiGraph, TLatex
from array import array
import rootlogonTDR

def test():

    cLimits = TCanvas('limits')
    frame = TH1D('frame','',1000,114,601+1)
    frame.SetMinimum(0)
    frame.SetMaximum(7.5)
    frame.SetDirectory(0)
    frame.SetStats(0)
    frame.SetFillColor(63)
    frame.SetLineStyle(0)
    frame.SetMarkerStyle(20)
    frame.GetYaxis().SetLabelSize(0.05);
    frame.GetYaxis().SetTitle('95% CL Limit on #sigma/#sigma_{SM}')
    frame.GetXaxis().SetTitle('m_{H} (GeV)')
    frame.Draw('  ')

    raw_input('type whatever to quit')

test()
