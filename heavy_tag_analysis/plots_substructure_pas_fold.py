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

 theory=False
 runSet=2

 if runSet==1:
  gStyle.SetPalette(1)
  samples = ["~/workspace/substructure/substructure_pas_QCD500.root",
             "~/workspace/substructure/substructure_pas_QCD1000.root",
             "~/workspace/substructure/substructure_pas_QCDHerwig.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8170.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8300.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8470.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8600.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8800.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81400.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81800.root",
            ]
  colors=[1,2,4,6,1]
  styles=[1,1,2,3,1]
  widths=[2,2,2,2,2]
  sets=[""]

  names = ["tau21",
	   "tau21_afterprunedmass",
	   "tau21_aftermass",
	   ]
  plots = [("GenJet1Nsub:Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600))","gen(#tau_{2}/#tau_{1})", ),
           ("GenJet1Nsub:Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1Mass>60)&&(Jet1Mass<100))","gen(#tau_{2}/#tau_{1})", ),
           ("GenJet1Nsub:Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1UnGroomedMass>60)&&(Jet1UnGroomedMass<100))","gen(#tau_{2}/#tau_{1})", ),
           ]

 if runSet==2:
  samples = ["~/workspace/substructure/substructure_pas_ReRun2012ABCD.root",
             "~/workspace/substructure/substructure_pas_QCD500.root",
             "~/workspace/substructure/substructure_pas_QCD1000.root",
             "~/workspace/substructure/substructure_pas_QCDHerwig.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8170.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8300.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8470.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8600.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8800.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81400.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81800.root",
             "~/workspace/substructure/substructure_pas_ReRun2012ABCD.root",
            ]
  colors=[1,2,4,6,1]
  styles=[1,1,2,3,1]
  widths=[2,2,2,2,2]
  sets=[""]

  names = ["tau21",
	   "tau21_afterprunedmass",
	   "tau21_aftermass",
	   ]
  plots = [("Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600))","#tau_{2}/#tau_{1}", ),
           ("Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1Mass>60)&&(Jet1Mass<100))","#tau_{2}/#tau_{1}", ),
           ("Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1UnGroomedMass>60)&&(Jet1UnGroomedMass<100))","#tau_{2}/#tau_{1}", ),
           ]

 if runSet==3:
  samples = ["~/workspace/substructure/substructure_pas_QCD500.root",
             "~/workspace/substructure/substructure_pas_QCD1000.root",
             "~/workspace/substructure/substructure_pas_QCDHerwig.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8170.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8300.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8470.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8600.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8800.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81400.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81800.root",
            ]
  colors=[1,2,4,6,1]
  styles=[1,1,2,3,1]
  widths=[2,2,2,2,2]
  sets=[""]

  names = ["tau21",
	   "tau21_afterprunedmass",
	   "tau21_aftermass",
	   ]
  plots = [("GenJet1Nsub","weight*vertexWeight*((abs(GenJet1eta)<2.4)&&(Gendeta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600))","#tau_{2}/#tau_{1}", ),
           ("GenJet1Nsub","weight*vertexWeight*((abs(GenJet1eta)<2.4)&&(Gendeta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600)&&(GenJet1Mass>60)&&(GenJet1Mass<100))","#tau_{2}/#tau_{1}", ),
           ("GenJet1Nsub","weight*vertexWeight*((abs(GenJet1eta)<2.4)&&(Gendeta<1.3)&&(GenDijetMass>890)&&(GenJet1pt>400)&&(GenJet1pt<600)&&(GenJet1UnGroomedMass>60)&&(GenJet1UnGroomedMass<100))","#tau_{2}/#tau_{1}", ),
           ]

 if runSet==4:
  samples = ["~/workspace/substructure/substructure_pas_ReRun2012ABCD.root",
             "~/workspace/substructure/substructure_pas_QCD500.root",
             "~/workspace/substructure/substructure_pas_QCD1000.root",
             "~/workspace/substructure/substructure_pas_QCDHerwig.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8170.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8300.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8470.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8600.root",
             "~/workspace/substructure/substructure_pas_QCDPythia8800.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81000.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81400.root",
             "~/workspace/substructure/substructure_pas_QCDPythia81800.root",
             "~/workspace/substructure/substructure_pas_ReRun2012ABCD.root",
            ]
  colors=[1,2,4,6,1]
  styles=[1,1,2,3,1]
  widths=[2,2,2,2,2]
  sets=[""]

  names = ["tau21",
	   "tau21_afterprunedmass",
	   "tau21_aftermass",
	   ]
  plots = [("-0.0247301+0.949227*Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600))","#tau_{2}/#tau_{1}", ),
           ("-0.0306497+0.914939*Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1Mass>60)&&(Jet1Mass<100))","#tau_{2}/#tau_{1}", ),
           ("-0.00606509+0.923065*Jet1Nsub","weight*vertexWeight*((abs(Jet1eta)<2.4)&&(deta<1.3)&&(DijetMass>890)&&(Jet1pt>400)&&(Jet1pt<600)&&(Jet1UnGroomedMass>60)&&(Jet1UnGroomedMass<100))","#tau_{2}/#tau_{1}", ),
           ]

 results=[]
 for plot in plots:
  if runSet==2 or runSet==4:
    canvas = TCanvas("","",0,0,200,260)
    canvas.Divide(1,2,0,0,0)
    canvas.GetPad(1).SetPad(0.0,0.28,1.0,1.0)
    canvas.GetPad(1).SetLeftMargin(0.15)
    canvas.GetPad(1).SetRightMargin(0.08)
    canvas.GetPad(1).SetTopMargin(0.08)
    canvas.GetPad(1).SetBottomMargin(0.05)
    canvas.GetPad(2).SetPad(0.0,0.0,1.0,0.28)
    canvas.GetPad(2).SetLeftMargin(0.15)
    canvas.GetPad(2).SetRightMargin(0.08)
    canvas.GetPad(2).SetTopMargin(0.08)
    canvas.GetPad(2).SetBottomMargin(0.45)
    canvas.cd(1)
    canvas.GetPad(1).SetLogy(False)
  else:
    canvas = TCanvas("","",0,0,200,200)
    canvas.SetLogy(False)
  if runSet==2 or runSet==4:
    legend=TLegend(0.45,0.7,0.85,0.9)
  else:
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
    if runSet==6 and not gen=="Gen" and s==1:
       continue
    if runSet==6 and not "Gen" in gen and (s==2):
       continue
    if runSet==6 and "Gen" in gen and s==3:
       continue
    if runSet==6 and "PUcorrected" in gen and plot[0]!="Jet1Nsub":
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
       if runSet==3 or runSet==11 or runSet==12 or runSet==13 or runSet==14:
          hist=TH1F(histname,histname,40,0,3000);
       elif runSet==2 or runSet==4:
          hist=TH1F(histname,histname,40,300,700);
       else:
          hist=TH1F(histname,histname,40,300,700);
       hist.GetYaxis().SetRangeUser(0.001,50000)
       if runSet==2 or runSet==4:
         canvas.GetPad(1).SetLogy(True)
       else:
         canvas.SetLogy(True)
    if "pruned jet mass" in plot[2]:
       hist=TH1F(histname,histname,50,0,150);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]== "jet mass (GeV)":
       hist=TH1F(histname,histname,100,0,300);
       hist.GetYaxis().SetRangeUser(0,50000)
    if plot[2]=="mass drop":
       hist=TH1F(histname,histname,20,0,1);
       hist.GetYaxis().SetRangeUser(0,60000)
       if "aftermass" in names[plots.index(plot)]:
           hist.GetYaxis().SetRangeUser(0,6000)
    if "gen(#tau_{2}/#tau_{1})" in plot[2]:
       hist=TH2F(histname,histname,20,0,1,20,0,1);
       hist.GetZaxis().SetRangeUser(0,75000)
    elif "#tau_{2}/#tau_{1}" in plot[2]:
       hist=TH1F(histname,histname,20,0,1);
       hist.GetYaxis().SetRangeUser(0,75000)
       if "aftermass" in names[plots.index(plot)]:
           hist.GetYaxis().SetRangeUser(0,5000)
    hist.Sumw2()
    
    if gen=="lowPU":
        variable,cutstring=plot[0],plot[1]+"&&(nPU<17)"
    #elif runSet==3 and s!=1 and s!=13:
    #    variable,cutstring="0.121048+1.01384*GenJet1Nsub-0.212977*GenJet1Nsub*GenJet1Nsub",plot[1]
    elif gen=="Subjet":
        variable,cutstring="Jet1MassSubjet",plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","")
    elif gen=="Angle":
        variable,cutstring="Jet1MassGenSubjetAngle",plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","")
    elif gen=="Pt":
        variable,cutstring="Jet1MassGenSubjetPt",plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","")
    elif gen=="Mass":
        variable,cutstring="Jet1MassGenSubjetMass",plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","")
    elif gen=="MassWindow":
        variable,cutstring=plot[0],plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","&&(Jet1pt>1100)&&(Jet1pt<1700)")+"&&(Jet1Mass>40)&&(Jet1Mass<60)"
    elif runSet==11 or runSet==12 or runSet==13 or runSet==14:
        variable,cutstring=gen+plot[0],plot[1].replace("&&(Jet1pt>400)&&(Jet1pt<600)","&&(Jet1pt>1100)&&(Jet1pt<1700)")
    elif runSet==4 and (counter==1 or counter==3):
        variable,cutstring=plot[0],plot[1]+"&&(abs(Jet1eta)<1.0)"
    elif gen=="GenPt2":
        variable,cutstring="Gen"+plot[0]+"Pt2",plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif gen=="GenCHS" and plot[0]=="Jet1nConstituents":
        variable,cutstring="GenJet1NCHS",plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif gen=="GenCHS":
        variable,cutstring="Gen"+plot[0]+"CHS",plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif gen=="GenPUcorrected":
        variable,cutstring="Gen"+plot[0]+"PUcorrected",plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif gen=="GenPUcorrectedCHS":
        variable,cutstring="Gen"+plot[0]+"PUcorrectedCHS",plot[1].replace("Jet","GenJet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    elif runSet==7 and s==3 and gen=="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet",gen+"Jet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")+"&&(Jet1genWcharge<0)"
    elif runSet==7 and s==3 and gen!="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet",gen+"Jet")+"&&(Jet1genWcharge<0)"
    elif runSet==7 and s==4 and gen=="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet",gen+"Jet").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")+"&&(Jet1genWcharge>0)"
    elif runSet==7 and s==4 and gen!="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet",gen+"Jet")+"&&(Jet1genWcharge>0)"
    elif gen=="Gen":
        variable,cutstring=gen+plot[0],plot[1].replace("Jet",gen+"Jet").replace(gen+"Jet1genWcharge","Jet1genWcharge").replace("DijetMass","GenDijetMass").replace("deta","Gendeta")
    else:
        variable,cutstring=plot[0],plot[1]
    
    if runSet==9 and gen=="gluon":
        cutstring+="&&(Jet1quarkgluon==2)"
    if runSet==9 and gen=="":
        cutstring+="&&(Jet1quarkgluon==1)"

    print histname,variable,cutstring
    tree.Project(histname,variable,cutstring)
    if "QCD" in sample:
        originalIntegral[histname]=hist.Integral()
    hist.SetTitle("")
    hist.SetFillStyle(0)
    hist.SetMarkerStyle(20)
    #hist.SetMarkerSize(2)
    if runSet==2 or runSet==4:
      hist.GetXaxis().SetTitle("")
      hist.GetXaxis().SetLabelColor(0)
      hist.GetYaxis().SetTitle("Events")
      if "pruned jet mass" in plot[2]:
          hist.GetYaxis().SetTitle("Events / (3 GeV)")
    elif runSet==1:
      hist.GetXaxis().SetTitle(plot[2])
      hist.GetYaxis().SetTitle(plot[2].replace("gen","reco"))
    else:
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

    if runSet==1:
       for bx in range(hist.GetXaxis().GetNbins()):
          sumy=0
	  for by in range(hist.GetYaxis().GetNbins()):
	      sumy+=hist.GetBinContent(bx+1,by+1)
	  if sumy==0: sumy=1
	  for by in range(hist.GetXaxis().GetNbins()):
	      hist.SetBinContent(bx+1,by+1,hist.GetBinContent(bx+1,by+1)/sumy)
	      hist.SetBinError(bx+1,by+1,hist.GetBinError(bx+1,by+1)/sumy)
	      if hist.GetBinContent(bx+1,by+1)<=hist.GetBinError(bx+1,by+1)*2:
   	          hist.SetBinContent(bx+1,by+1,0)
	  print str([hist.GetBinContent(bx+1,by+1) for by in range(hist.GetYaxis().GetNbins())]).replace("[","{").replace("]","}")+","
    
       fit=TF1("fit","pol1",0,3)
       fit.SetLineColor(colors[counter])
       fit.SetLineStyle(styles[counter])        
       fit.SetLineWidth(widths[counter])
       hists+=[fit]
       hist.ProfileX().Fit("fit","N0")
    else:
       for bx in range(hist.GetXaxis().GetNbins()):
           print hist.GetXaxis().GetBinLowEdge(bx+1),hist.GetXaxis().GetBinUpEdge(bx+1),hist.GetBinContent(bx+1)/hist.Integral(),hist.GetBinError(bx+1)/hist.Integral(),hist.GetBinError(bx+1)/hist.Integral()
    
    if counter==0:
      firsthist=hist
      if "Run" in sample:
        hist.Draw("pe")
      elif "Gen" in gen:
        hist.Draw("chist")
      elif runSet==1:
        hist.Draw("COLZ")
	fit.Draw("lsame")
      else:
        hist.Draw("hist")
    else:
      if "Run" in sample:
        hist.Draw("pesame")
      elif "Gen" in gen and not runSet==6:
        hist.Draw("csame")
      elif runSet==1:
	fit.Draw("lsame")
      else:
        hist.Draw("histsame")

    if hist.GetMaximum()>maximum and hist.GetMaximum()<hist.Integral():
        maximum=hist.GetMaximum()

    if "jet p_{T}" in plot[2] and (runSet==2 or runSet==4):
  	firsthist.GetYaxis().SetRangeUser(100,maximum*20.0)
    elif "jet p_{T}" in plot[2]:
  	firsthist.GetYaxis().SetRangeUser(0.001,maximum*20.0)
    elif "gen(#tau_{2}/#tau_{1})" in plot[2]:
        firsthist.GetYaxis().SetRangeUser(0,1)
        firsthist.GetZaxis().SetRangeUser(0,maximum*2.0)
    else:
        firsthist.GetYaxis().SetRangeUser(0,maximum*2.0)

    if runSet==2 or runSet==4:
      canvas.cd(2)
      ratio=hist.Clone(hist.GetName()+"clone")
      hists+=[ratio]
      ratio.Divide(hist,hists[0])
      for b in range(hist.GetNbinsX()):
        if hists[0].GetBinContent(b+1)>0:
          ratio.SetBinError(b+1,hists[0].GetBinError(b+1)/hists[0].GetBinContent(b+1))
      ratio.GetYaxis().SetTitle("Sim / Data")
      ratio.GetYaxis().SetTitleSize(0.13)
      ratio.GetYaxis().SetTitleOffset(0.5)
      ratio.SetMarkerSize(0.1)
      ratio.GetYaxis().SetLabelSize(0.14)
      ratio.GetYaxis().SetRangeUser(0,2)
      ratio.GetYaxis().SetNdivisions(503)
      ratio.GetXaxis().SetLabelColor(1)
      ratio.GetXaxis().SetTitle(plot[2])
      ratio.GetXaxis().SetTitleSize(0.16)
      ratio.GetXaxis().SetTitleOffset(0.8)
      ratio.GetXaxis().SetLabelSize(0.14)
      if counter==0:
        ratio.Draw("histe")
      else:
        ratio.Draw("histsame")
      #line=TLine(ratio.GetXaxis().GetBinLowEdge(1),1,ratio.GetXaxis().GetBinLowEdge(ratio.GetNbinsX()+1),1)
      #hists+=[line]
      #line.Draw("same")
      canvas.cd(1)
      firsthist.GetYaxis().SetTitleOffset(1.2)

    if "Run" in sample and counter==0:
      legend.AddEntry(hist,"data","ple")
    if "QCD1000" in sample:
        legend.AddEntry(hist,"QCD MG+Pythia6","l")
    if "QCDHerwig" in sample:
        legend.AddEntry(hist,"QCD Herwig++","l")
    if "QCDPythia8" in sample:
        legend.AddEntry(hist,"QCD Pythia8","l")
    if "WWBulk" in sample or "WWPy6" in sample:
        legend.AddEntry(hist,"X #rightarrow W_{L}W_{L} Pythia6","l")
    if "WWHpp" in sample:
        legend.AddEntry(hist,"X #rightarrow W_{T}W_{T} Herwig++","l")
    counter+=1

  legend.SetTextSize(0.036)
  legend.SetFillStyle(0)
  legend.Draw("same")

  legend4=TLegend(0.23,0.85,0.5,0.9,"CA R=0.8")
  legend4.SetTextSize(0.03)
  legend4.SetFillStyle(0)
  legend4.Draw("same")

  legend2=TLegend(0.17,0.8,0.5,0.85,"400 < p_{T} < 600 GeV")
  legend2.SetTextSize(0.03)
  legend2.SetFillStyle(0)
  legend2.Draw("same")

  #if runSet==11:
  #  legend2=TLegend(0.17,0.8,0.5,0.85,"1.4 < p_{T} < 1.6 TeV")
  #  legend2.SetTextSize(0.03)
  #  legend2.SetFillStyle(0)
  #  legend2.Draw("same")

  legend2a=TLegend(0.24,0.75,0.5,0.8,"|#eta|<2.4")
  legend2a.SetTextSize(0.03)
  legend2a.SetFillStyle(0)
  legend2a.Draw("same")

  if runSet==2 or runSet==4:
    banner = TLatex(0.27,0.93,"CMS Preliminary, 19.6 fb^{-1}, #sqrt{s} = 8 TeV, dijets");
  elif runSet==6 and theory:
    banner = TLatex(0.32,0.93,"Pythia6, #sqrt{s} = 8 TeV, dijets");
  else:
    banner = TLatex(0.24,0.93,"CMS Preliminary Simulation, #sqrt{s} = 8 TeV, dijets");
  banner.SetNDC()
  banner.SetTextSize(0.04)
  banner.Draw();  

  if "aftermass" in names[plots.index(plot)]:
     legend3=TLegend(0.17,0.7,0.5,0.75,"60 < m_{j} < 100 GeV")
     legend3.SetTextSize(0.03)
     legend3.SetFillStyle(0)
     legend3.Draw("same")

  canvas.SaveAs("substructure_pas_"+names[plots.index(plot)]+"_fold"+str(runSet)+".png")
  canvas.SaveAs("substructure_pas_"+names[plots.index(plot)]+"_fold"+str(runSet)+".pdf")
  canvas.SaveAs("substructure_pas_"+names[plots.index(plot)]+"_fold"+str(runSet)+".root")
  canvas.SaveAs("substructure_pas_"+names[plots.index(plot)]+"_fold"+str(runSet)+".C")
  canvas.SaveAs("substructure_pas_"+names[plots.index(plot)]+"_fold"+str(runSet)+".eps")
