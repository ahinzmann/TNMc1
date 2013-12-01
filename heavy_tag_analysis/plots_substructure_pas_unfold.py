import os, sys
import array
from ROOT import * 
from os import path

#gROOT.Reset()
#gROOT.SetStyle("Plain")
gROOT.ProcessLine('.L tdrstyle.C')
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)
gStyle.SetTitleOffset(1.3,"Y")
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadBottomMargin(0.15)
gStyle.SetPadTopMargin(0.08)
gStyle.SetPadRightMargin(0.08)
gStyle.SetMarkerSize(0.5)
gStyle.SetHistLineWidth(1)
#gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(506, "XYZ")
gStyle.SetLegendBorderSize(0)

TGaxis.SetMaxDigits(3)

if __name__ == '__main__':

 samples=["","_aftermass","_afterprunedmass"]

 for sample in samples:
   print sample
   f1=TFile.Open("substructure_pas_tau21"+sample+"_fold4.root")
   f2=TFile.Open("substructure_pas_tau21"+sample+"_fold3.root")
   canvas1=f1.Get(";1")
   canvas2=f2.Get(";1")
   data=canvas1.GetListOfPrimitives()[0].GetListOfPrimitives()[1]
   pythia6_detector=canvas1.GetListOfPrimitives()[0].GetListOfPrimitives()[2]
   pythia6_raw=canvas2.GetListOfPrimitives()[1]
   herwigpp_detector=canvas1.GetListOfPrimitives()[0].GetListOfPrimitives()[3]
   herwigpp_raw=canvas2.GetListOfPrimitives()[2]
   pythia8_detector=canvas1.GetListOfPrimitives()[0].GetListOfPrimitives()[4]
   pythia8_raw=canvas2.GetListOfPrimitives()[3]
   for bx in range(data.GetXaxis().GetNbins()):
       norm=1.
       generators=1.
       if pythia6_detector.GetBinContent(bx+1)>0:
           norm+=pythia6_raw.GetBinContent(bx+1)/pythia6_raw.Integral()/pythia6_detector.GetBinContent(bx+1)*pythia6_detector.Integral()
	   generators+=1.
       if herwigpp_detector.GetBinContent(bx+1)>0:
           norm+=herwigpp_raw.GetBinContent(bx+1)/herwigpp_raw.Integral()/herwigpp_detector.GetBinContent(bx+1)*herwigpp_detector.Integral()
	   generators+=1.
       if pythia8_detector.GetBinContent(bx+1)>0:
           norm+=pythia8_raw.GetBinContent(bx+1)/pythia8_raw.Integral()/pythia8_detector.GetBinContent(bx+1)*pythia8_detector.Integral()
	   generators+=1.
       norm/=generators
       error=0.
       if pythia6_detector.GetBinContent(bx+1)>0:
           error=max(error,abs(pythia6_raw.GetBinContent(bx+1)/pythia6_raw.Integral()/pythia6_detector.GetBinContent(bx+1)*pythia6_detector.Integral()-norm))
       if herwigpp_detector.GetBinContent(bx+1)>0:
           error=max(error,abs(herwigpp_raw.GetBinContent(bx+1)/herwigpp_raw.Integral()/herwigpp_detector.GetBinContent(bx+1)*herwigpp_detector.Integral()-norm))
       if pythia8_detector.GetBinContent(bx+1)>0:
           error=max(error,abs(pythia8_raw.GetBinContent(bx+1)/pythia8_raw.Integral()/pythia8_detector.GetBinContent(bx+1)*pythia8_detector.Integral()-norm))
       if error==0.:
           error=1.
       #print norm, error
       if data.Integral()>0:
           norm/=data.Integral()
           error/=data.Integral()
       print data.GetXaxis().GetBinLowEdge(bx+1),data.GetXaxis().GetBinUpEdge(bx+1),\
             data.GetBinContent(bx+1)*norm, sqrt(pow(data.GetBinError(bx+1)*norm,2)+pow(data.GetBinContent(bx+1)*error,2)), sqrt(pow(data.GetBinError(bx+1)*norm,2)+pow(data.GetBinContent(bx+1)*error,2))
