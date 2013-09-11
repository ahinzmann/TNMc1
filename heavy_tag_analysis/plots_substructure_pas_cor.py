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
gStyle.SetPadRightMargin(0.15)
gStyle.SetMarkerSize(0.5)
gStyle.SetHistLineWidth(1)
#gStyle.SetStatFontSize(0.020)
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetNdivisions(506, "XYZ")
gStyle.SetLegendBorderSize(0)
gStyle.SetPalette(1)

TGaxis.SetMaxDigits(3)

if __name__ == '__main__':

 scenarios=[("","WW"),
            ("_Gen_prunedmass","WW"),
            ("_Gen_mass","WW"),
            ("_Gen","WW"),
            ]

 for scenario,particle in scenarios:

  samples = [#"~/workspace/substructure/substructure_pas_QCD500.root",
             #"~/workspace/substructure/substructure_pas_QCD1000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8170.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8300.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8470.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8600.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8800.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81400.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81800.root",
            ]

  if particle=="WW":
     samples+=["substructure_pas_WWPy61000.root",]
  if particle=="ZZ":
     samples+=["substructure_pas_ZZPy61000.root",]

  selection="(abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)"
  selection_mass="&&(Jet1Mass>60)&&(Jet1Mass<100)"
  plots=[("Jet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"Jet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,False),
        ("Jet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"Jet1C2beta10","C_{2} (#beta=1.0)",10,0,0.6,False),
        ("Jet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"Jet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ("Jet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,"Jet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ]

  names = ["tau21C2beta05",
	  "tau21C2beta10",
	  "tau21C2beta20",
	  "C2beta05C2beta20",
	  ]

  colors=[1,2,4,6,7,1,2,4,6,7]
  widths=[2,2,2,2,2,1,1,1,1,1]
  styles=[1,1,1,1,1,2,2,2,2,2]
           
  if scenario=="_Gen":
   selection_mass=""
   selection="(abs(GenJet1eta)<2.4)&&(deta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600)"
   plots=[("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta10","C_{2} (#beta=1.0)",10,0,0.6,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ("Jet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,"Jet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ]

  if scenario=="_Gen_mass":
   if particle=="ZZ":
      selection_mass="&&(GenJet1UnGroomedMass>80)&&(GenJet1UnGroomedMass<100)"
   if particle=="WW":
      selection_mass="&&(GenJet1UnGroomedMass>70)&&(GenJet1UnGroomedMass<90)"
   selection="(abs(GenJet1eta)<2.4)&&(deta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600)"
   plots=[("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta10","C_{2} (#beta=1.0)",10,0,0.6,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ("Jet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,"Jet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ]

  if scenario=="_Gen_prunedmass":
   if particle=="ZZ":
      selection_mass="&&(GenJet1Mass>70)&&(GenJet1Mass<110)"
   if particle=="WW":
      selection_mass="&&(GenJet1Mass>60)&&(GenJet1Mass<100)"
   selection="(abs(GenJet1eta)<2.4)&&(deta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600)"
   plots=[("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta10","C_{2} (#beta=1.0)",10,0,0.6,False),
        ("GenJet1Nsub","#tau_{2}/#tau_{1}",10,0,1,"GenJet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ("Jet1C2beta05","C_{2} (#beta=0.5)",10,0,0.5,"Jet1C2beta20","C_{2} (#beta=2.0)",10,0,1,False),
        ]

  results=[]

  canvas = TCanvas("","",0,0,200,200)
  canvas.SetLogz(True)

  for plot in plots:
   originalIntegral={}
   hists=[]
   s=0
   for sample in samples:
    s+=1
    f=TFile.Open(sample)
    tree=f.Get("dijetWtag")
    histname="plot"+names[plots.index(plot)]+str(s)
    hist=TH2F(histname,histname,plot[7],plot[8],plot[9],plot[2],plot[3],plot[4]);
    print sample,plot[0],plot[5],selection+selection_mass
    tree.Project(histname,plot[0]+":"+plot[5],selection+selection_mass)
    if "QCD" in sample:
        originalIntegral[histname]=hist.Integral()
    integral=1.
    if hist.Integral()>0:
        hist.Scale(integral/hist.Integral())
    hists+=[hist]
    if "QCDPythia8" in sample and not "170" in sample:
        samplenames=["170","300","470","600","800","1000","1400","1800"]
	samplenumbers=[800046,490042,500051,492988,400059,400050,200070,194313]
	samplecrossections=[37974.99,1938.868,124.8942,29.55049,3.871308,0.8031018,0.03637225,0.00197726]
	samplenumber=0
        for samplename in samplenames:
          if samplename in sample:
            samplenumber=samplenames.index(samplename)
        histnameFirst="plot"+names[plots.index(plot)]+str(s-samplenumber)
        for his in reversed(hists):
	    if histnameFirst==his.GetName():
	        oldIntegral=his.Integral()
		if his.Integral()>0:
                    his.Scale(originalIntegral[histnameFirst]/his.Integral())
		if hist.Integral()>0:
                    hist.Scale(originalIntegral[histname]/hist.Integral())
                weight=samplecrossections[samplenumber]/samplenumbers[samplenumber]*samplenumbers[0]/samplecrossections[0]
	        his.Add(hist,weight)
		if oldIntegral>0:
		    originalIntegral[histnameFirst]=his.Integral()
                    his.Scale(oldIntegral/his.Integral())
		elif his.Integral()>0:
		    originalIntegral[histnameFirst]=his.Integral()
                    his.Scale(integral/his.Integral())
 	        hist=his
		break
    if "QCDPythia8" in sample and not "1800" in sample:
        continue

    hist.GetYaxis().SetTitle(plot[1])
    hist.GetXaxis().SetTitle(plot[6])
    hist.SetTitle("")
    correlation=hist.GetCorrelationFactor()
    print "correlation",correlation
    hist2=hist.Clone(hist.GetName()+"norm")
    for x in range(hist.GetNbinsX()):
      norm=0
      for y in range(hist.GetNbinsY()):
        norm+=hist.GetBinContent(x+1,y+1)
      if norm==0: continue
      for y in range(hist.GetNbinsY()):
	#hist.SetBinContent(x+1,y+1,hist.GetBinContent(x+1,y+1)/norm)
        pass
    hist.Draw("colz")
    hist.GetZaxis().SetRangeUser(0.0005,0.5)
    hist2.ProfileX().Draw("lesame")
    
    legend4=TLegend(0.70,0.25,0.9,0.3,"CA R=0.8")
    legend4.SetTextSize(0.03)
    legend4.SetFillStyle(0)
    legend4.Draw("same")

    legend2=TLegend(0.62,0.2,0.9,0.25,"400 < p_{T} < 600 GeV")
    legend2.SetTextSize(0.03)
    legend2.SetFillStyle(0)
    legend2.Draw("same")

    legend2a=TLegend(0.70,0.15,0.9,0.2,"|#eta|<2.4")
    legend2a.SetTextSize(0.03)
    legend2a.SetFillStyle(0)
    legend2a.Draw("same")
    
    if "QCD" in sample:
      legend3a=TLegend(0.62,0.3,0.9,0.35,"QCD Pythia8")
    elif "WW" in sample:
      legend3a=TLegend(0.62,0.3,0.9,0.35,"W_{L} Pythia6")
    elif "ZZ" in sample:
      legend3a=TLegend(0.62,0.3,0.9,0.35,"Z Pythia6")
    legend3a.SetTextSize(0.03)
    legend3a.SetFillStyle(0)
    legend3a.Draw("same")

    legend4a=TLegend(0.62,0.35,0.9,0.4,"corr.=%.2f" % correlation)
    legend4a.SetTextSize(0.03)
    legend4a.SetFillStyle(0)
    legend4a.Draw("same")
    
    if "Gen" in scenario:
     banner = TLatex(0.24,0.93,"#sqrt{s} = 8 TeV");
    else:
     banner = TLatex(0.24,0.93,"CMS Preliminary Simulation, #sqrt{s} = 8 TeV");
    banner.SetNDC()
    banner.SetTextSize(0.04)
    banner.Draw();  

    canvas.SaveAs("substructure_pas_"+particle+"cor"+scenario+names[plots.index(plot)]+str(s)+".png")
    canvas.SaveAs("substructure_pas_"+particle+"cor"+scenario+names[plots.index(plot)]+str(s)+".pdf")
    canvas.SaveAs("substructure_pas_"+particle+"cor"+scenario+names[plots.index(plot)]+str(s)+".root")
    canvas.SaveAs("substructure_pas_"+particle+"cor"+scenario+names[plots.index(plot)]+str(s)+".C")
    canvas.SaveAs("substructure_pas_"+particle+"cor"+scenario+names[plots.index(plot)]+str(s) +".eps")
