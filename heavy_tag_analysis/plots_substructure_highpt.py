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

 runSet=31
 
 names = ["pt",
	   "eta",
	   "mass",
	   "trimmedmass",
	   "ungroomedmass",
	   "tau21_aftermass",
	   "nconstituents",
	   ]

 plots = [("Jet1pt","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","jet p_{T} (GeV)"),
           ("Jet1eta","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","jet #eta"),
           ("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ("Jet1MassTrimmed","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","trimmed jet mass (GeV)"),
           ("Jet1UnGroomedMass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","jet mass (GeV)"),
           ("Jet1Nsub","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700)&&(Jet1Mass>60)&&(Jet1Mass<100))","#tau_{2}/#tau_{1}", ),
           ("Jet1nConstituents","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","jet constituents", ),
           ]

 if runSet==1:
  samples = ["substructure_pas_WWHpp1000.root",
             "substructure_pas_WWHpp3000.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","1","pruned jet mass (GeV)"),
           ]
  colors=[1,4,4,6,2,2]
  styles=[2,1,3,2,1,3]
  widths=[2,1,1,2,1,1]
  sets=["","barrel","endcap"]

 if runSet==2:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   "correctedmass",
	   "ungroomedmass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ("Jet1CorrectedPrunedMass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ("Jet1UnGroomedMass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","jet mass (GeV)"),
           ]
  colors=[1,2,3,4,6,7,8,9,15]
  styles=[2,2,2,3,4,1,1,1,1]
  widths=[1,1,1,2,2,2,2,2,2]
  sets=["","CHF1","CHF2","CHF3","CHF4"]

 if runSet==3:
  samples = ["substructure_pas_WWHppPFg2500.root",
             "substructure_pas_WWHppCalo2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ]
  colors=[1,2,3,4,6,7,8,9,15]
  styles=[2,2,2,3,4,1,1,1,1]
  widths=[1,1,1,2,2,2,2,2,2]
  sets=["Gen","GenJet1TrackMass","GenJet1CaloMass005","GenJet1CaloMassPF005","GenJet1CaloMassPFcorrect005","Jet1TrackMass","","Jet1CorrectedPrunedMass"]

 if runSet==31:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700)&&(abs(parton_dR_1)<0.14))","pruned jet mass (GeV)"),
           ]
  colors=[1,1,4,4,2,2,6,6,7,7]
  styles=[2,1,2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2,1,1]
  sets=["Jet1PrunedMass","Jet1TrackMass","Jet1CorrectedPrunedMass"]

 if runSet==32:
  samples = ["substructure_pas_WWHppRePF2500.root",
             "substructure_pas_WWHppRePFnoHCALcluster2500.root",
             "substructure_pas_WWHppRePFredHCALcluster2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700)&&(abs(parton_dR_1)<0.14))","pruned jet mass (GeV)"),
           ]
  #colors=[4,4,4,2,2,2,6,6,6]
  #styles=[2,1,3,2,1,3,2,1,3]
  #widths=[2,1,1,2,1,1,2,1,1]
  colors=[4,4,2,2,6,6]
  styles=[2,1,2,1,2,1]
  widths=[2,1,2,1,2,1]
  sets=["Jet1PrunedMass","Jet1SplitBlockPrunedMass"]#,"Jet1CorrectedPrunedMass"

 if runSet==4:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ]
  colors=[1,1,4,4,2,2,6,6,7,7]
  styles=[2,1,2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2,1,1]
  sets=["Gen","GenJet1TrackMass","GenJet1CaloMassPFcorrect001","GenJet1CaloMassPFcorrect002","GenJet1CaloMassPFcorrect005","GenJet1CaloMassPFcorrect01","GenJet1CaloMassPFcorrect02"]

 if runSet==5:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700)&&(Jet1CaloMassPF005<40))","pruned jet mass (GeV)"),
           ]
  colors=[1,1,4,4,2,2,6,6,7,7]
  styles=[2,1,2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2,1,1]
  sets=["Gen","GenJet1TrackMass","GenJet1CaloMassPF001","GenJet1CaloMassPF002","GenJet1CaloMassPF005","GenJet1CaloMassPF01","GenJet1CaloMassPF02"]

 if runSet==6:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ]
  colors=[1,1,4,4,2,2,6,6,7,7]
  styles=[2,1,2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2,1,1]
  sets=["Gen","GenJet1TrackMass","GenJet1CaloMassPF001","GenJet1CaloMassPF002","GenJet1CaloMassPF005","GenJet1CaloMassPF01","GenJet1CaloMassPF02"]

 if runSet==7:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  names = ["mass",
	   ]
  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)"),
           ]
  colors=[1,1,4,4,2,2,6,6,7,7]
  styles=[2,1,2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2,1,1]
  sets=["Gen","GenJet1TrackMass","GenJet1CaloMass001","GenJet1CaloMass002","GenJet1CaloMass005","GenJet1CaloMass01","GenJet1CaloMass02"]

 if runSet==8:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["Gen","Dr01","Dr05","Dr10"]

 if runSet==9:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["Gen","","EtaWindow"]

 if runSet==10:
  samples = ["substructure_pas_WWHppPFg2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["Gen","","PtWindow"]

 if runSet==11:
  samples = ["substructure_pas_WWHppPFg2500.root",
             "substructure_pas_WWHppCalo2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["","MassWindow"]

 if runSet==12:
  samples = ["substructure_pas_WWHppPFg2500.root",
             "substructure_pas_WWHppCalo2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["Gen",""]

 if runSet==13:
  samples = ["substructure_pas_WWHpp3000.root",
             #"substructure_pas_WWHppCalo2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["Gen","","Subjet","Angle","Pt","Mass"]

  plots = [("Jet1Mass","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","pruned jet mass (GeV)", ),
           ]

  names = ["PrunedMass",
	   ]

 if runSet==14:
  samples = ["substructure_pas_WWHpp3000.root",
             #"substructure_pas_WWHppCalo2500.root",
             ]
  colors=[1,1,4,4,2,2,6,6]
  styles=[2,1,2,1,2,1,2,1]
  widths=[1,1,2,2,1,1,2,2]
  sets=["","MassWindow"]

  plots = [("Jet1Sj1AngleResolution","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","sj angular resolution", ),
           ("Jet1Sj1PtResolution","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","sj p_{T} resolution (GeV)", ),
           ("Jet1Sj1MassResolution","((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>2000)&&(Jet1pt>1100)&&(Jet1pt<1700))","sj mass resolution (GeV)", ),
           ]

  names = ["Sj1AngleResolution",
	   "Sj1PtResolution",
	   "Sj1MassResolution",
	   ]

 results=[]
 for plot in plots:
  canvas = TCanvas("","",0,0,200,200)
  canvas.SetLogy(False)
  legend=TLegend(0.45,0.6,0.85,0.9)
  dataPlotted=False
  counter=0
  integral=1
  originalIntegral={}
  maximum=0
  s=0
  hists=[]
  firsthist=None
  for sample in samples:
   s+=1
   for gen in sets:
    if (names[plots.index(plot)]=="pt" or names[plots.index(plot)]=="eta" or names[plots.index(plot)]=="npu" or names[plots.index(plot)]=="npv" or "costheta" in names[plots.index(plot)] or "Phi" in names[plots.index(plot)] or "dR" in names[plots.index(plot)]) and gen=="Gen":
       continue
    if names[plots.index(plot)]=="npu" and s==2:
       continue
    if (names[plots.index(plot)]=="pt" or names[plots.index(plot)]=="eta") and gen=="lowPU":
       continue
    if (runSet==2 or runSet==3) and gen!="" and s==2:
       continue
    print sample, gen

    f=TFile.Open(sample)
    tree=f.Get("dijetWtag")

    signal = "Hpp" in sample or "Py6" in sample
    histname="plot"+names[plots.index(plot)]+gen+str(s)
    if "sj angular resolution" in plot[2]:
       hist=TH1F(histname,histname,25,0,0.2);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "sj p_{T} resolution (GeV)" in plot[2]:
       hist=TH1F(histname,histname,25,-1000,1000);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "sj mass resolution (GeV)" in plot[2]:
       hist=TH1F(histname,histname,25,-50,50);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "cos #theta" in plot[2]:
       hist=TH1F(histname,histname,25,0,1);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "#Phi" in plot[2]:
       hist=TH1F(histname,histname,25,-3.15,3.15);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "#Delta R" in plot[2]:
       hist=TH1F(histname,histname,25,0,3);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="pileup interactions":
       hist=TH1F(histname,histname,25,0,50);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="number of vertices":
       hist=TH1F(histname,histname,25,0,50);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="jet #eta":
       hist=TH1F(histname,histname,25,-2.4,2.4);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "C_{2}" in plot[2]:
       hist=TH1F(histname,histname,25,0,0.8);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "jet charge (#kappa=0.3)" in plot[2]:
       hist=TH1F(histname,histname,25,-4,4);
       hist.GetYaxis().SetRangeUser(0,50000)
       hist.GetXaxis().SetRangeUser(-4,4)
    if "jet charge (#kappa=0.5)" in plot[2]:
       hist=TH1F(histname,histname,25,-2,2);
       hist.GetYaxis().SetRangeUser(0,50000)
       hist.GetXaxis().SetRangeUser(-2,2)
    if "jet charge (#kappa=1.0)" in plot[2]:
       hist=TH1F(histname,histname,25,-1,1);
       hist.GetYaxis().SetRangeUser(0,50000)
       hist.GetXaxis().SetRangeUser(-1,1)
    if plot[2]=="jet constituents":
       hist=TH1F(histname,histname,25,0,200);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="charged particles (p_{T}^{rel}>0.1)":
       hist=TH1F(histname,histname,25,0,25);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="neutral particles (p_{T}^{rel}>0.1)":
       hist=TH1F(histname,histname,25,0,25);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="3rd charged particle p_{T}":
       hist=TH1F(histname,histname,25,0,250);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="3rd particle p_{T}":
       hist=TH1F(histname,histname,25,0,250);
       hist.GetYaxis().SetRangeUser(0,50000)
    if "jet p_{T}" in plot[2]:
       hist=TH1F(histname,histname,40,0,3000);
       hist.GetYaxis().SetRangeUser(0.001,50000)
       canvas.SetLogy(True)
    if "pruned jet mass" in plot[2] or "trimmed jet mass" in plot[2]:
       hist=TH1F(histname,histname,50,0,150);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]== "jet mass (GeV)":
       hist=TH1F(histname,histname,50,0,300);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="mass drop":
       hist=TH1F(histname,histname,20,0,1);
       hist.GetYaxis().SetRangeUser(0,60000)
       if "aftermass" in names[plots.index(plot)]:
           hist.GetYaxis().SetRangeUser(0,6000)
    if "#tau_{2}/#tau_{1}" in plot[2]:
       hist=TH1F(histname,histname,20,0,1);
       hist.GetYaxis().SetRangeUser(0,75000)
       if "aftermass" in names[plots.index(plot)]:
           hist.GetYaxis().SetRangeUser(0,5000)

    if gen=="lowPU":
        variable,cutstring=plot[0],plot[1]+"&&(nPU<17)"
    elif gen=="Subjet":
        variable,cutstring="Jet1MassSubjet",plot[1].replace("&&(Jet1pt>1100)&&(Jet1pt<1700)","")
    elif gen=="Angle":
        variable,cutstring="Jet1MassGenSubjetAngle",plot[1].replace("&&(Jet1pt>1100)&&(Jet1pt<1700)","")
    elif gen=="Pt":
        variable,cutstring="Jet1MassGenSubjetPt",plot[1].replace("&&(Jet1pt>1100)&&(Jet1pt<1700)","")
    elif gen=="Mass":
        variable,cutstring="Jet1MassGenSubjetMass",plot[1].replace("&&(Jet1pt>1100)&&(Jet1pt<1700)","")
    elif gen=="CHF1":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1CHF<0.4)"
    elif gen=="CHF2":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1CHF>0.4)&&(Jet1CHF<0.6)"
    elif gen=="CHF3":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1CHF>0.6)&&(Jet1CHF<0.8)"
    elif gen=="CHF4":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1CHF>0.8)"
    elif gen=="MassWindow":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1Mass>40)&&(Jet1Mass<60)"
    elif gen=="PtWindow":
        variable,cutstring=plot[0],plot[1]+"&&(Jet1pt>1500)"
    elif gen=="barrel":
        variable,cutstring=plot[0],plot[1]+"&&(abs(Jet1eta)<1.0)"
    elif gen=="endcap":
        variable,cutstring=plot[0],plot[1]+"&&(abs(Jet1eta)>1.0)"
    elif gen=="EtaWindow":
        variable,cutstring=plot[0],plot[1]+"&&(abs(Jet1eta)<0.5)"
    elif gen=="Dr01":
        variable,cutstring=plot[0],plot[1]+"&&(abs(parton_dR_1)>0.01)&&(abs(parton_dR_1)<0.14)"
    elif gen=="Dr05":
        variable,cutstring=plot[0],plot[1]+"&&(abs(parton_dR_1)>0.14)&&(abs(parton_dR_1)<0.28)"
    elif gen=="Dr10":
        variable,cutstring=plot[0],plot[1]+"&&(abs(parton_dR_1)>0.28)&&(abs(parton_dR_1)<1.0)"
    elif "TrackMass" in gen or "CaloMass" in gen or "PrunedMass" in gen:
        variable,cutstring=gen,plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif gen=="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    else:
        variable,cutstring=gen+plot[0],plot[1]
    
    print histname,variable,cutstring
    tree.Project(histname,variable,cutstring)
    if runSet==32:
       hist.Rebin(2)
    if "QCD" in sample:
        originalIntegral[histname]=hist.Integral()
    hist.SetTitle("")
    hist.SetFillStyle(0)
    hist.SetMarkerStyle(20)
    #hist.SetMarkerSize(2)
    hist.GetXaxis().SetTitle(plot[2])
    hist.GetYaxis().SetTitle("Normalized Distribution")
    if "Run" in sample:
        integral=hist.Integral()
    if hist.Integral()>0:
        hist.Scale(integral/hist.Integral())

    print "mean",hist.GetMean()

    hists+=[hist]

    if "QCD1000" in sample:
        histname500="plot"+names[plots.index(plot)]+gen+str(s-1)
        for his in reversed(hists):
	    if histname500==his.GetName():
	        oldIntegral=his.Integral()
		if his.Integral()>0:
                    his.Scale(originalIntegral[histname500]/his.Integral())
		if hist.Integral()>0:
                    hist.Scale(originalIntegral[histname]/hist.Integral())
		weight=204.0/13798133*30522161/8426.0
	        his.Add(hist,weight)
		if oldIntegral>0:
                    his.Scale(oldIntegral/his.Integral())
		else:
                    his.Scale(integral/his.Integral())
 	        hist=his
 	        break
    if "QCD500" in sample:
	continue
    
    if "QCDPythia8" in sample and not "170" in sample:
        samplenames=["170","300","470","600","800","1000","1400","1800"]
	samplenumbers=[800046,490042,500051,492988,400059,400050,200070,194313]
	samplecrossections=[37974.99,1938.868,124.8942,29.55049,3.871308,0.8031018,0.03637225,0.00197726]
	samplenumber=0
        for samplename in samplenames:
          if samplename in sample:
            samplenumber=samplenames.index(samplename)
        histnameFirst="plot"+names[plots.index(plot)]+gen+str(s-samplenumber)
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

    hist.SetLineColor(colors[counter])
    hist.SetLineStyle(styles[counter])        
    hist.SetLineWidth(widths[counter])
    
    if counter==0:
      firsthist=hist
      if "Run" in sample:
        hist.Draw("pe")
      elif "Gen" in gen:
        hist.Draw("chist")
      else:
        hist.Draw("hist")
    else:
      if "Run" in sample:
        hist.Draw("pesame")
      elif "Gen" in gen:
        hist.Draw("csame")
      else:
        hist.Draw("histsame")

    if hist.GetMaximum()>maximum and hist.GetMaximum()<hist.Integral():
        maximum=hist.GetMaximum()

    if "jet p_{T}" in plot[2]:
  	firsthist.GetYaxis().SetRangeUser(0.001,maximum*20.0)
    else:
        firsthist.GetYaxis().SetRangeUser(0,maximum*2.0)

    if "WW" in sample:
      if gen=="Gen" and "Hpp" in  sample:
        legend.AddEntry(hist,"X #rightarrow W_{T}W_{T} Herwig++","l")
      elif gen=="Gen" and "Py6" in  sample:
        legend.AddEntry(hist,"X #rightarrow W_{T}W_{T} Pythia6","l")
      elif runSet==1 and gen=="" and s==1:
        legend.AddEntry(hist,"X #rightarrow W_{T}W_{T} 1 TeV","l")
      elif runSet==1 and gen=="" and s==2:
        legend.AddEntry(hist,"X #rightarrow W_{T}W_{T} 3 TeV","l")
      elif runSet==1 and "barrel" in gen:
        legend.AddEntry(hist,"|eta|<1.0","l")
      elif runSet==1 and "endcap" in gen:
        legend.AddEntry(hist,"|eta|>1.0","l")
      elif runSet==2 and "CHF1" in gen:
        legend.AddEntry(hist,"CHF < 0.4","l")
      elif runSet==2 and "CHF2" in gen:
        legend.AddEntry(hist,"0.4 < CHF < 0.6","l")
      elif runSet==2 and "CHF3" in gen:
        legend.AddEntry(hist,"0.6 < CHF < 0.8","l")
      elif runSet==2 and "CHF4" in gen:
        legend.AddEntry(hist,"CHF > 0.8 ","l")
      elif runSet==2 and "X #rightarrow W_{T}W_{T} Herwig++" in gen:
        legend.AddEntry(hist,"","l")
      elif runSet==3 and "Track" in gen:
        legend.AddEntry(hist,"gen tracks","l")
      elif runSet==3 and "CaloMass005" in gen:
        legend.AddEntry(hist,"gen calo","l")
      elif runSet==3 and "CaloMassPF005" in gen:
        legend.AddEntry(hist,"gen calo+PF","l")
      elif runSet==3 and "CaloMassPFcorrect005" in gen:
        legend.AddEntry(hist,"gen calo+PFv2","l")
      elif runSet==3 and "TrackMass" in gen:
        legend.AddEntry(hist,"reco tracks","l")
      elif runSet==3 and "CorrectedPrunedMass" in gen:
        legend.AddEntry(hist,"reco PFv2","l")
      elif runSet==3 and s==1:
        legend.AddEntry(hist,"reco PF","l")
      elif runSet==3 and s==2:
        legend.AddEntry(hist,"reco calo","l")
      elif runSet==31 and "Track" in gen:
        legend.AddEntry(hist,"charged PF","l")
      elif runSet==31 and "CorrectedPrunedMass" in gen:
        legend.AddEntry(hist,"improved PF","l")
      elif runSet==31 and "PrunedMass" in gen:
        legend.AddEntry(hist,"reco PF","l")
      elif runSet==31 and "" in gen:
        legend.AddEntry(hist,"reco PF","l")
      elif runSet==32 and "SplitBlockPrunedMass" in gen:
        legend.AddEntry(hist," + split block","l")
      elif runSet==32 and "CorrectedPrunedMass" in gen:
        legend.AddEntry(hist," + improved PF","l")
      elif runSet==32 and "PrunedMass" in gen and s==1:
        legend.AddEntry(hist,"default PF","l")
      elif runSet==32 and "PrunedMass" in gen and s==2:
        legend.AddEntry(hist,"no HCAL cluster","l")
      elif runSet==32 and "PrunedMass" in gen and s==3:
        legend.AddEntry(hist,"modified HCAL cluster","l")
      elif runSet==3 and "CorrectedPrunedMass" in gen:
        legend.AddEntry(hist,"reco PFv2","l")
      elif runSet<8 and "Track" in gen:
        legend.AddEntry(hist,"charged particles","l")
      elif runSet<8 and "0002" in gen:
        legend.AddEntry(hist,"calo cell size 0.002","l")
      elif runSet<8 and "0005" in gen:
        legend.AddEntry(hist,"calo cell size 0.005","l")
      elif runSet<8 and "001" in gen:
        legend.AddEntry(hist,"calo cell size 0.01","l")
      elif runSet<8 and "002" in gen:
        legend.AddEntry(hist,"calo cell size 0.02","l")
      elif runSet<8 and "005" in gen:
        legend.AddEntry(hist,"calo cell size 0.05","l")
      elif runSet<8 and "01" in gen:
        legend.AddEntry(hist,"calo cell size 0.1","l")
      elif runSet<8 and "02" in gen:
        legend.AddEntry(hist,"calo cell size 0.2","l")
      elif runSet<8 and "05" in gen:
        legend.AddEntry(hist,"calo cell size 0.5","l")
      elif runSet<8 and "1" in gen:
        legend.AddEntry(hist,"calo cell size 1.0","l")
      elif runSet==8 and gen=="":
        legend.AddEntry(hist," all","l")
      elif runSet==8 and gen=="Dr01":
        legend.AddEntry(hist," dR(partons) < 0.14","l")
      elif runSet==8 and gen=="Dr05":
        legend.AddEntry(hist," 0.14 < dR(partons) < 0.28","l")
      elif runSet==8 and gen=="Dr10":
        legend.AddEntry(hist," 0.28 < dR(partons) < 1.0","l")
      elif runSet==9 and gen=="":
        legend.AddEntry(hist," all","l")
      elif runSet==9 and gen=="EtaWindow":
        legend.AddEntry(hist," |#eta| < 0.5","l")
      elif runSet==10 and gen=="":
        legend.AddEntry(hist," all","l")
      elif runSet==10 and gen=="PtWindow":
        legend.AddEntry(hist," p_T > 1.5 TeV","l")
      elif runSet==11 and gen=="":
        legend.AddEntry(hist," all","l")
      elif runSet==11 and gen=="MassWindow":
        legend.AddEntry(hist," 40 < m_{j} < 60 GeV","l")
      elif runSet==12 and s==1:
        legend.AddEntry(hist," + sim. PF","l")
      elif runSet==12 and s==2:
        legend.AddEntry(hist," + sim. Calo","l")
      elif runSet==13 and gen=="":
        legend.AddEntry(hist," reco fatjet","l")
      elif runSet==13 and gen=="Subjet":
        legend.AddEntry(hist," reco subjets","l")
      elif runSet==13 and gen=="Angle":
        legend.AddEntry(hist," gen sj-angles","l")
      elif runSet==13 and gen=="Pt":
        legend.AddEntry(hist," gen sj-energies","l")
      elif runSet==13 and gen=="Mass":
        legend.AddEntry(hist," gen sj-mass","l")
	firsthist.GetYaxis().SetRangeUser(0,0.3)
      elif runSet==14 and gen=="":
        legend.AddEntry(hist," all","l")
      elif runSet==14 and gen=="MassWindow":
        legend.AddEntry(hist," 40 < m_{j} < 60 GeV","l")
      else:
        legend.AddEntry(hist," + <PU>=22 + sim.","l")
    counter+=1

  legend.SetTextSize(0.036)
  legend.SetFillStyle(0)
  legend.Draw("same")

  legend4=TLegend(0.23,0.85,0.5,0.9,"CA R=0.8")
  legend4.SetTextSize(0.03)
  legend4.SetFillStyle(0)
  legend4.Draw("same")

  legend2=TLegend(0.17,0.8,0.5,0.85,"1.1 < p_{T} < 1.7 TeV")
  legend2.SetTextSize(0.03)
  legend2.SetFillStyle(0)
  legend2.Draw("same")

  legend2a=TLegend(0.24,0.75,0.5,0.8,"|#eta|<2.4")
  legend2a.SetTextSize(0.03)
  legend2a.SetFillStyle(0)
  legend2a.Draw("same")

  if runSet==31 or runSet==32:
    legend2b=TLegend(0.17,0.7,0.5,0.75,"dR(partons) < 0.14")
    legend2b.SetTextSize(0.03)
    legend2b.SetFillStyle(0)
    legend2b.Draw("same")

  banner = TLatex(0.24,0.93,"CMS Preliminary Simulation, #sqrt{s} = 8 TeV, dijets");
  banner.SetNDC()
  banner.SetTextSize(0.04)
  banner.Draw();  

  if "aftermass" in names[plots.index(plot)]:
     legend3=TLegend(0.17,0.7,0.5,0.75,"60 < m_{j} < 100 GeV")
     legend3.SetTextSize(0.03)
     legend3.SetFillStyle(0)
     legend3.Draw("same")

  canvas.SaveAs("substructure_highpt_"+names[plots.index(plot)]+"_"+str(runSet)+".png")
  canvas.SaveAs("substructure_highpt_"+names[plots.index(plot)]+"_"+str(runSet)+".pdf")
  canvas.SaveAs("substructure_highpt_"+names[plots.index(plot)]+"_"+str(runSet)+".root")
  canvas.SaveAs("substructure_highpt_"+names[plots.index(plot)]+"_"+str(runSet)+".C")
  canvas.SaveAs("substructure_highpt_"+names[plots.index(plot)]+"_"+str(runSet)+".eps")
