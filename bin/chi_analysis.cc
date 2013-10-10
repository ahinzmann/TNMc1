//-----------------------------------------------------------------------------
// File:        analyzer.cc
// Description: Analyzer for ntuples created by TheNtupleMaker
// Created:     Thu May 31 21:49:25 2012 by mkntanalyzer.py
// Author:      Andreas Hinzmann
//-----------------------------------------------------------------------------
#include "chi_analysis.h"

#ifdef PROJECT_NAME
#include "PhysicsTools/TheNtupleMaker/interface/pdg.h"
#else
#include "pdg.h"
#endif

#include "DataFormats/Math/interface/deltaR.h"
#include "TLorentzVector.h"

#include "Ntuples/TNMc1/plugins/HcalLaserEventFilter2012.cc"

#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include <vector>

#include "TLorentzVector.h"

using namespace std;
//-----------------------------------------------------------------------------
int main(int argc, char** argv)
{
  // Get file list and histogram filename from command line

  commandLine cmdline;
  decodeCommandLine(argc, argv, cmdline);

  // Get names of ntuple files to be processed and open chain of ntuples

  vector<string> filenames = getFilenames(cmdline.filelist);
  itreestream stream(filenames, "Events");
  if ( !stream.good() ) error("unable to open ntuple file(s)");

  // Get number of events to be read

  int nevents = stream.size();
  cout << "Number of events: " << nevents << endl;

  // Select variables to be read

  //selectVariables(stream);

  stream.select("edmEventHelper_info.bunchCrossing", eventhelper_bunchCrossing);
  stream.select("edmEventHelper_info.event", eventhelper_event);
  stream.select("edmEventHelper_info.isRealData", eventhelper_isRealData);
  stream.select("edmEventHelper_info.luminosityBlock", eventhelper_luminosityBlock);
  stream.select("edmEventHelper_info.orbitNumber", eventhelper_orbitNumber);
  stream.select("edmEventHelper_info.run", eventhelper_run);
  stream.select("edmEventHelperExtra_info.numberOfPrimaryVertices", eventhelperextra_numberOfPrimaryVertices);
  stream.select("GenEventInfoProduct_generator.weight", geneventinfoproduct_weight);
  stream.select("cmgBaseMET_cmgPFMET.et", met2_et);
  stream.select("cmgBaseMET_cmgPFMET.sumEt", met2_sumEt);
  stream.select("PileupSummaryInfo_addPileupInfo.getBunchCrossing", pileupsummaryinfo_getBunchCrossing);
  stream.select("PileupSummaryInfo_addPileupInfo.getPU_NumInteractions", pileupsummaryinfo_getPU_NumInteractions);
  stream.select("PileupSummaryInfo_addPileupInfo.getTrueNumInteractions", pileupsummaryinfo_getTrueNumInteractions);
  stream.select("sdouble_kt6PFJets_rho.value", sdouble_kt6PFJets_rho_value);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v1", triggerresultshelper_HLT_HT450_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v2", triggerresultshelper_HLT_HT450_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v3", triggerresultshelper_HLT_HT450_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v4", triggerresultshelper_HLT_HT450_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v5", triggerresultshelper_HLT_HT450_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v6", triggerresultshelper_HLT_HT450_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v7", triggerresultshelper_HLT_HT450_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v8", triggerresultshelper_HLT_HT450_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT450_v9", triggerresultshelper_HLT_HT450_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v1", triggerresultshelper_HLT_HT750_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v2", triggerresultshelper_HLT_HT750_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v3", triggerresultshelper_HLT_HT750_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v4", triggerresultshelper_HLT_HT750_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v5", triggerresultshelper_HLT_HT750_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v6", triggerresultshelper_HLT_HT750_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v7", triggerresultshelper_HLT_HT750_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v8", triggerresultshelper_HLT_HT750_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v9", triggerresultshelper_HLT_HT750_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v1", triggerresultshelper_HLT_PFHT650_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v2", triggerresultshelper_HLT_PFHT650_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v3", triggerresultshelper_HLT_PFHT650_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v4", triggerresultshelper_HLT_PFHT650_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v5", triggerresultshelper_HLT_PFHT650_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v6", triggerresultshelper_HLT_PFHT650_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v7", triggerresultshelper_HLT_PFHT650_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v8", triggerresultshelper_HLT_PFHT650_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v9", triggerresultshelper_HLT_PFHT650_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v10", triggerresultshelper_HLT_PFHT650_v10);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v11", triggerresultshelper_HLT_PFHT650_v11);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v1", triggerresultshelper_HLT_PFNoPUHT650_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v2", triggerresultshelper_HLT_PFNoPUHT650_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v3", triggerresultshelper_HLT_PFNoPUHT650_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v4", triggerresultshelper_HLT_PFNoPUHT650_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v5", triggerresultshelper_HLT_PFNoPUHT650_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFNoPUHT650_v6", triggerresultshelper_HLT_PFNoPUHT650_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v1", triggerresultshelper_HLT_DiPFJetAve400_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v2", triggerresultshelper_HLT_DiPFJetAve400_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v3", triggerresultshelper_HLT_DiPFJetAve400_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v4", triggerresultshelper_HLT_DiPFJetAve400_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v5", triggerresultshelper_HLT_DiPFJetAve400_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v6", triggerresultshelper_HLT_DiPFJetAve400_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v7", triggerresultshelper_HLT_DiPFJetAve400_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v8", triggerresultshelper_HLT_DiPFJetAve400_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v9", triggerresultshelper_HLT_DiPFJetAve400_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v10", triggerresultshelper_HLT_DiPFJetAve400_v10);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v11", triggerresultshelper_HLT_DiPFJetAve400_v11);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_DiPFJetAve400_v12", triggerresultshelper_HLT_DiPFJetAve400_v12);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v1", triggerresultshelper_HLT_PFJet400_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v2", triggerresultshelper_HLT_PFJet400_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v3", triggerresultshelper_HLT_PFJet400_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v4", triggerresultshelper_HLT_PFJet400_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v5", triggerresultshelper_HLT_PFJet400_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v6", triggerresultshelper_HLT_PFJet400_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v7", triggerresultshelper_HLT_PFJet400_v7);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v8", triggerresultshelper_HLT_PFJet400_v8);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v9", triggerresultshelper_HLT_PFJet400_v9);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v10", triggerresultshelper_HLT_PFJet400_v10);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFJet400_v11", triggerresultshelper_HLT_PFJet400_v11);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.hcalLaserEventFilterPath", triggerresultshelper_hcalLaserEventFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.noscrapingFilterPath", triggerresultshelper_noscrapingFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.primaryVertexFilterPath", triggerresultshelper_primaryVertexFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.trackingFailureFilterPath", triggerresultshelper_trackingFailureFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.CSCTightHaloFilterPath", triggerresultshelper_CSCTightHaloFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.EcalDeadCellBoundaryEnergyFilterPath", triggerresultshelper_EcalDeadCellBoundaryEnergyFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.EcalDeadCellTriggerPrimitiveFilterPath", triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.HBHENoiseFilterPath", triggerresultshelper_HBHENoiseFilterPath);
  stream.select("sint_hcallasereventfilter2012.value", triggerresultshelper_hcallasereventfilter2012);

  stream.select("cmgPFJet_cmgPFJetSelCHS.energy", jethelper3_energy);
  stream.select("cmgPFJet_cmgPFJetSelCHS.eta", jethelper3_eta);
  stream.select("cmgPFJet_cmgPFJetSelCHS.rapidity", jethelper3_rapidity);
  stream.select("cmgPFJet_cmgPFJetSelCHS.mass", jethelper3_mass);
  stream.select("cmgPFJet_cmgPFJetSelCHS.phi", jethelper3_phi);
  stream.select("cmgPFJet_cmgPFJetSelCHS.pt", jethelper3_pt);
  stream.select("cmgPFJet_cmgPFJetSelCHS.nConstituents", jethelper3_nConstituents);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_0_fraction", jethelper3_component_0_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_0_number", jethelper3_component_0_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_1_fraction", jethelper3_component_1_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_1_number", jethelper3_component_1_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_2_fraction", jethelper3_component_2_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_2_number", jethelper3_component_2_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_3_fraction", jethelper3_component_3_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_3_number", jethelper3_component_3_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_4_fraction", jethelper3_component_4_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_4_number", jethelper3_component_4_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_5_fraction", jethelper3_component_5_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_5_number", jethelper3_component_5_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_6_fraction", jethelper3_component_6_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_6_number", jethelper3_component_6_number);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_7_fraction", jethelper3_component_7_fraction);
  stream.select("cmgPFJet_cmgPFJetSelCHS.component_7_number", jethelper3_component_7_number);

  stream.select("sdouble_vertexWeightSummer12MC53X2012ABCDData.value", vertexWeight);

  // The root application is needed to make canvases visible during
  // program execution. If this is not needed, just comment out the following
  // line

  TApplication app("analyzer", &argc, argv);

  /*
	 Notes:
	
	 1. Use
	   ofile = outputFile(cmdline.outputfile, stream)
	
	 to skim events to output file in addition to writing out histograms.
	
	 2. Use
	   ofile.addEvent(event-weight)
	
	 to specify that the current event is to be added to the output file.
	 If omitted, the event-weight is defaulted to 1.
	
	 3. Use
	    ofile.count(cut-name, event-weight)
	
	 to keep track, in the count histogram, of the number of events
	 passing a given cut. If omitted, the event-weight is taken to be 1.
	 If you want the counts in the count histogram to appear in a given
	 order, specify the order, before entering the event loop, as in
	 the example below
	 
	    ofile.count("NoCuts", 0)
		ofile.count("GoodEvent", 0)
		ofile.count("Vertex", 0)
		ofile.count("MET", 0)
  */
  
  outputFile ofile(cmdline.outputfilename);

  //---------------------------------------------------------------------------
  // Declare histograms
  //---------------------------------------------------------------------------

  std::vector<double> massBins = {1500,1900,2400,3000,3600,4200,7000};

  TCanvas c1("c1","c1",200,200);
  TH1F* h1=new TH1F("dijet_mass","M_{jj}",76,400,8000);
  h1->Sumw2();
  TH1F* h1_ref=new TH1F("dijet_mass_ref","M_{jj}",76,400,8000);
  h1_ref->Sumw2();
  TH1F* h1_trig=new TH1F("dijet_mass_trig","M_{jj}",76,400,8000);
  h1_trig->Sumw2();
  
  std::vector<TH1F*> hists;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "chi";
      hists.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      hists[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsnopu;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "nopu";
      histsnopu.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histsnopu[j]->Sumw2();
  }
  
  std::vector<TH1F*> histspu0;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "pu0";
      histspu0.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histspu0[j]->Sumw2();
  }
  
  std::vector<TH1F*> histspu10;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "pu10";
      histspu10.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histspu10[j]->Sumw2();
  }
  
  std::vector<TH1F*> histspu20;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "pu20";
      histspu20.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histspu20[j]->Sumw2();
  }
  
  std::vector<TH1F*> histspt1;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "pt1";
      histspt1.push_back(new TH1F(name.str().c_str(),name.str().c_str(),30,0,3000));
      histspt1[j]->Sumw2();
  }
  
  std::vector<TH1F*> histspt2;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "pt2";
      histspt2.push_back(new TH1F(name.str().c_str(),name.str().c_str(),30,0,3000));
      histspt2[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsy1;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "y1";
      histsy1.push_back(new TH1F(name.str().c_str(),name.str().c_str(),25,-2.5,2.5));
      histsy1[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsy2;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "y2";
      histsy2.push_back(new TH1F(name.str().c_str(),name.str().c_str(),25,-2.5,2.5));
      histsy2[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsyboost;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "yboost";
      histsyboost.push_back(new TH1F(name.str().c_str(),name.str().c_str(),12,0,1.2));
      histsyboost[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsmetsumet;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "metsumet";
      histsmetsumet.push_back(new TH1F(name.str().c_str(),name.str().c_str(),100,0,1.00001));
      histsmetsumet[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsmptsumpt;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "mptsumpt";
      histsmptsumpt.push_back(new TH1F(name.str().c_str(),name.str().c_str(),50,0,1.00001));
      histsmptsumpt[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsdpt;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "dpt";
      histsdpt.push_back(new TH1F(name.str().c_str(),name.str().c_str(),50,0,1));
      histsdpt[j]->Sumw2();
  }
  
  std::vector<TH1F*> histsdphi;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "dphi";
      histsdphi.push_back(new TH1F(name.str().c_str(),name.str().c_str(),20,0,3.15));
      histsdphi[j]->Sumw2();
  }
/*
  std::vector<std::string> eventlist;
  std::ifstream infile_;
  char a[80];
  infile_.open("data/ecalLaserFilter_HT_Run2012A.txt");
  while(!infile_.eof())
  {
      infile_>>a;
      eventlist.push_back(a);
  }
  infile_.close();
  infile_.open("data/ecalLaserFilter_JetHT_Run2012B.txt");
  while(!infile_.eof())
  {
      infile_>>a;
      eventlist.push_back(a);
  }
  edm::ParameterSet parameters;
  parameters.addUntrackedParameter<std::vector<std::string>>("EventList",eventlist);
  HcalLaserEventFilter2012 laserfilter(parameters);
*/
// Instantiate uncertainty sources
int nsrc = 22; /////////////////////////////
const char* srcnames[22] =
  {"Absolute", "HighPtExtra", /*"SinglePion",*/ "SinglePionECAL"/*new*/, "SinglePionHCAL"/*new*/,
   "FlavorQCD", "Time",
   "RelativeJEREC1", "RelativeJEREC2", "RelativeJERHF",
   "RelativePtBB"/*new*/, "RelativePtEC1"/*new*/, "RelativePtEC2"/*new*/, "RelativePtHF"/*new*/,
   "RelativeStatEC2", "RelativeStatHF", "RelativeFSR", /*"RelativeSample",*/ /*new*/
   "PileUpDataMC", /*"PileUpOOT",*/ "PileUpBias", /*"PileUpJetRate"*/
   /*"PileUpPt",*/ "PileUpPtBB"/*new*/, "PileUpPtEC"/*new*/, "PileUpPtHF"/*new*/, "Total"};
std::vector<JetCorrectionUncertainty*> vsrc(nsrc);

for (int isrc = 0; isrc < nsrc; isrc++) {

   const char *name = srcnames[isrc];
   JetCorrectorParameters *p = new JetCorrectorParameters("data/Summer13_V4_DATA_UncertaintySources_AK5PFchs.txt", name);
   JetCorrectionUncertainty *unc = new JetCorrectionUncertainty(*p);
   vsrc[isrc] = unc;
} // for isrc

  std::vector<std::vector<TH1F*> > histsJECup;
for (int isrc = 0; isrc < nsrc; isrc++) {
  std::vector<TH1F*> histsJ;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "chi_JECup" << isrc;
      histsJ.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histsJ[j]->Sumw2();
  }
  histsJECup.push_back(histsJ);
}
  std::vector<std::vector<TH1F*> > histsJECdown;
for (int isrc = 0; isrc < nsrc; isrc++) {
  std::vector<TH1F*> histsJ;
  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      std::stringstream name;
      name << "dijet_" << massBins[j] << "_" << massBins[j+1] << "_" << "chi_JECdown" << isrc;
      histsJ.push_back(new TH1F(name.str().c_str(),name.str().c_str(),15,1,16));
      histsJ[j]->Sumw2();
  }
  histsJECdown.push_back(histsJ);
}
  
  //---------------------------------------------------------------------------
  // Loop over events
  //---------------------------------------------------------------------------

  std::cout << "event..." << std::endl;

  bool hcallasereventfilter2012active=false;
  bool datafiltersactive=false;

  for(int entry=0; entry < nevents; ++entry)
	{

	  // Read event into memory
	  stream.read(entry);

	  // Uncomment the following line if you wish to copy variables into
	  // structs. See the header file analyzer.h to find out what structs
	  // are available. Each struct contains the field "selected", which
	  // can be set as needed. Call saveSelectedObjects() before a call to
	  // addEvent if you wish to save only the selected objects.
	  
	  // fillObjects();
	 
	  if(((entry<100000)&&(entry%10000==0))||(entry%100000==0)) std::cout << entry << "..." << std::endl;

          TLorentzVector Jet1;
	  Jet1.SetPtEtaPhiE(jethelper3_pt[0],jethelper3_eta[0],jethelper3_phi[0],jethelper3_energy[0]);
          TLorentzVector Jet2;
	  Jet2.SetPtEtaPhiE(jethelper3_pt[1],jethelper3_eta[1],jethelper3_phi[1],jethelper3_energy[1]);
          double DijetMass = (Jet1+Jet2).M();
	  
	  // ---------------------
	  // -- event selection --
	  // ---------------------

          if (triggerresultshelper_hcallasereventfilter2012!=0)
	     hcallasereventfilter2012active=true;

	  if((triggerresultshelper_primaryVertexFilterPath!=0)&&
	     (triggerresultshelper_noscrapingFilterPath!=0)&&
	     (triggerresultshelper_trackingFailureFilterPath!=0)&&
	     (triggerresultshelper_hcalLaserEventFilterPath!=0)&&
	     (triggerresultshelper_HBHENoiseFilterPath!=0)&&
	     (triggerresultshelper_CSCTightHaloFilterPath!=0)//&&
	     //(triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath!=0)
	     )
	     datafiltersactive=true;

	  bool noiseRemoval = (((sdouble_kt6PFJets_rho_value<40)&&
	       (triggerresultshelper_primaryVertexFilterPath!=0)&&
	       (triggerresultshelper_noscrapingFilterPath!=0)&&
	       (triggerresultshelper_trackingFailureFilterPath!=0)&&
	       (triggerresultshelper_hcalLaserEventFilterPath!=0)&&
	       (triggerresultshelper_HBHENoiseFilterPath!=0)&&
	       (triggerresultshelper_CSCTightHaloFilterPath!=0)//&&
	       //(triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath!=0)
	       )||
	      (datafiltersactive==false))&&
	    ((triggerresultshelper_hcallasereventfilter2012!=0)||(hcallasereventfilter2012active==false));
           
	  if(!((jethelper3_pt.size()>=2)&&
	     (jethelper3_pt[0]>30)&&
	     (jethelper3_pt[1]>30)&&
	     (fabs(jethelper3_rapidity[0])<2.5)&&
	     (fabs(jethelper3_rapidity[1])<2.5)&&
             (fabs(jethelper3_rapidity[0]+jethelper3_rapidity[1])/2.<1.11)&&
             (exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1]))<16)&&
	     (DijetMass>500)&&
	     
	     (jethelper3_component_3_fraction[0]<0.80)&&
	     //(jethelper3_component_5_fraction[0]<0.99)&&
	     (jethelper3_component_5_fraction[0]<0.90)&&
	     //(jethelper3_component_4_fraction[0]<0.99)&&
	     (jethelper3_component_4_fraction[0]<0.90)&&
	     (jethelper3_nConstituents[0]>1)&&
	     ((fabs(jethelper3_eta[0])>2.4)||
	      ((jethelper3_component_1_fraction[0]>0.01)&&
	       (jethelper3_component_1_number[0]+jethelper3_component_2_number[0]+jethelper3_component_2_number[0]>0)&&
	       (jethelper3_component_2_fraction[0]<0.99)))&&
	     
	     (jethelper3_component_3_fraction[1]<0.80)&&
	     //(jethelper3_component_5_fraction[1]<0.99)&&
	     (jethelper3_component_5_fraction[1]<0.90)&&
	     //(jethelper3_component_4_fraction[1]<0.99)&&
	     (jethelper3_component_4_fraction[1]<0.90)&&
	     (jethelper3_nConstituents[1]>1)&&
	     ((fabs(jethelper3_eta[1])>2.4)||
	      ((jethelper3_component_1_fraction[1]>0.01)&&
	       (jethelper3_component_1_number[1]+jethelper3_component_2_number[1]+jethelper3_component_3_number[1]>0)&&
	       (jethelper3_component_2_fraction[1]<0.99)))
	     
	     &&
	     (noiseRemoval)
	    )) continue;

	  //if(!laserfilter.filter(eventhelper_run,eventhelper_luminosityBlock,eventhelper_event)) continue;
	   
	  // ---------------------
	  // -- fill histograms --
	  // ---------------------	  

          double weight=1;
          if(geneventinfoproduct_weight>0)
	      weight=geneventinfoproduct_weight;
          if(vertexWeight==0)
	      vertexWeight=1;
	  else
	      weight*=vertexWeight;

          h1->Fill(DijetMass, weight);
	  
	  if ((triggerresultshelper_HLT_HT450_v1>0)||
	      (triggerresultshelper_HLT_HT450_v2>0)||
	      (triggerresultshelper_HLT_HT450_v3>0)||
	      (triggerresultshelper_HLT_HT450_v4>0)||
	      (triggerresultshelper_HLT_HT450_v5>0)||
	      (triggerresultshelper_HLT_HT450_v6>0)||
	      (triggerresultshelper_HLT_HT450_v7>0)||
	      (triggerresultshelper_HLT_HT450_v8>0)||
	      (triggerresultshelper_HLT_HT450_v9>0))
              h1_ref->Fill(DijetMass, weight);

	  if(((triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11>0)||
	      (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12>0)||
	      (triggerresultshelper_HLT_PFHT650_v1>0)||
	      (triggerresultshelper_HLT_PFHT650_v2>0)||
	      (triggerresultshelper_HLT_PFHT650_v3>0)||
	      (triggerresultshelper_HLT_PFHT650_v4>0)||
	      (triggerresultshelper_HLT_PFHT650_v5>0)||
	      (triggerresultshelper_HLT_PFHT650_v6>0)||
	      (triggerresultshelper_HLT_PFHT650_v7>0)||
	      (triggerresultshelper_HLT_PFHT650_v8>0)||
	      (triggerresultshelper_HLT_PFHT650_v9>0)||
	      (triggerresultshelper_HLT_PFHT650_v10>0)||
	      (triggerresultshelper_HLT_PFHT650_v11>0)||
	      (triggerresultshelper_HLT_PFJet400_v1>0)||
	      (triggerresultshelper_HLT_PFJet400_v2>0)||
	      (triggerresultshelper_HLT_PFJet400_v3>0)||
	      (triggerresultshelper_HLT_PFJet400_v4>0)||
	      (triggerresultshelper_HLT_PFJet400_v5>0)||
	      (triggerresultshelper_HLT_PFJet400_v6>0)||
	      (triggerresultshelper_HLT_PFJet400_v7>0)||
	      (triggerresultshelper_HLT_PFJet400_v8>0)||
	      (triggerresultshelper_HLT_PFJet400_v9>0)||
	      (triggerresultshelper_HLT_PFJet400_v10>0)||
	      (triggerresultshelper_HLT_PFJet400_v11>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v1>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v2>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v3>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v4>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v5>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v6>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v7>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v8>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v9>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v10>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v11>0)||
	      (triggerresultshelper_HLT_DiPFJetAve400_v12>0)||
	      (triggerresultshelper_HLT_HT750_v1>0)||
	      (triggerresultshelper_HLT_HT750_v2>0)||
	      (triggerresultshelper_HLT_HT750_v3>0)||
	      (triggerresultshelper_HLT_HT750_v4>0)||
	      (triggerresultshelper_HLT_HT750_v5>0)||
	      (triggerresultshelper_HLT_HT750_v6>0)||
	      (triggerresultshelper_HLT_HT750_v7>0)||
	      (triggerresultshelper_HLT_HT750_v8>0)||
	      (triggerresultshelper_HLT_HT750_v9>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v1>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v2>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v3>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v4>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v5>0)||
	      (triggerresultshelper_HLT_PFNoPUHT650_v6>0))&&
	     ((triggerresultshelper_HLT_HT450_v1>0)||
	      (triggerresultshelper_HLT_HT450_v2>0)||
	      (triggerresultshelper_HLT_HT450_v3>0)||
	      (triggerresultshelper_HLT_HT450_v4>0)||
	      (triggerresultshelper_HLT_HT450_v5>0)||
	      (triggerresultshelper_HLT_HT450_v6>0)||
	      (triggerresultshelper_HLT_HT450_v7>0)||
	      (triggerresultshelper_HLT_HT450_v8>0)||
	      (triggerresultshelper_HLT_HT450_v9>0)))
              h1_trig->Fill(DijetMass, weight);
          /*
	  if(((triggerresultshelper_HLT_HT650_v1>0)||
	      (triggerresultshelper_HLT_HT650_v2>0)||
	      (triggerresultshelper_HLT_HT650_v3>0)||
	      (triggerresultshelper_HLT_HT650_v4>0)||
	      (triggerresultshelper_HLT_HT650_v5>0)||
	      (triggerresultshelper_HLT_HT650_v6>0)||
	      (triggerresultshelper_HLT_HT650_v7>0)||
	      (triggerresultshelper_HLT_HT650_v8>0)||
	      (triggerresultshelper_HLT_HT650_v9>0))&&
	     ((triggerresultshelper_HLT_HT450_v1>0)||
	      (triggerresultshelper_HLT_HT450_v2>0)||
	      (triggerresultshelper_HLT_HT450_v3>0)||
	      (triggerresultshelper_HLT_HT450_v4>0)||
	      (triggerresultshelper_HLT_HT450_v5>0)||
	      (triggerresultshelper_HLT_HT450_v6>0)||
	      (triggerresultshelper_HLT_HT450_v7>0)||
	      (triggerresultshelper_HLT_HT450_v8>0)||
	      (triggerresultshelper_HLT_HT450_v9>0)))
              h1_trig->Fill(DijetMass, weight);
          */
          for ( size_t j = 0; j < (massBins.size()-1); ++j )
          {
              if((DijetMass>=massBins[j])&&
	         (DijetMass<massBins[j+1]))
              {
                  hists[j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
                  histsnopu[j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight/vertexWeight);
		  if((eventhelperextra_numberOfPrimaryVertices>=0)&&(eventhelperextra_numberOfPrimaryVertices<10))
                    histspu0[j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
		  if((eventhelperextra_numberOfPrimaryVertices>=10)&&(eventhelperextra_numberOfPrimaryVertices<20))
                    histspu10[j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
		  if((eventhelperextra_numberOfPrimaryVertices>=20))
                    histspu20[j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
                  histspt1[j]->Fill(jethelper3_pt[0], weight);
                  histspt2[j]->Fill(jethelper3_pt[1], weight);
                  histsy1[j]->Fill(jethelper3_rapidity[0], weight);
                  histsy2[j]->Fill(jethelper3_rapidity[1], weight);
                  histsyboost[j]->Fill(fabs(jethelper3_rapidity[0]+jethelper3_rapidity[1])/2., weight);
                  histsmetsumet[j]->Fill(met2_et/met2_sumEt, weight);
		  TLorentzVector spt1;
		  spt1.SetPtEtaPhiE(jethelper3_pt[0],jethelper3_eta[0],jethelper3_phi[0],jethelper3_energy[0]);
		  TLorentzVector spt2;
		  spt2.SetPtEtaPhiE(jethelper3_pt[1],jethelper3_eta[1],jethelper3_phi[1],jethelper3_energy[1]);
                  histsmptsumpt[j]->Fill((spt1+spt2).Pt()/(jethelper3_pt[0]+jethelper3_pt[1]), weight);
                  histsdpt[j]->Fill((jethelper3_pt[0]-jethelper3_pt[1])/(jethelper3_pt[0]+jethelper3_pt[1]));
                  histsdphi[j]->Fill(fabs(reco::deltaPhi(jethelper3_phi[0],jethelper3_phi[1])));
              }
for (int isrc = 0; isrc < nsrc; isrc++) {
              double shift;
	      vsrc[isrc]->setJetPt(jethelper3_pt[0]);
              vsrc[isrc]->setJetEta(jethelper3_eta[0]);
	      shift=1.0+vsrc[isrc]->getUncertainty(true);
	      TLorentzVector jet1UpAbsolute;
	      jet1UpAbsolute.SetPtEtaPhiE(jethelper3_pt[0]*shift,jethelper3_eta[0],jethelper3_phi[0],jethelper3_energy[0]*shift);
              vsrc[isrc]->setJetPt(jethelper3_pt[1]);
              vsrc[isrc]->setJetEta(jethelper3_eta[1]);
	      shift=1.0+vsrc[isrc]->getUncertainty(true);
	      TLorentzVector jet2UpAbsolute;
	      jet2UpAbsolute.SetPtEtaPhiE(jethelper3_pt[1]*shift,jethelper3_eta[1],jethelper3_phi[1],jethelper3_energy[1]*shift);
              if(((jet1UpAbsolute+jet2UpAbsolute).M()>=massBins[j])&&
	         ((jet1UpAbsolute+jet2UpAbsolute).M()<massBins[j+1]))
                  histsJECup[isrc][j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
}
for (int isrc = 0; isrc < nsrc; isrc++) {
              double shift;
	      vsrc[isrc]->setJetPt(jethelper3_pt[0]);
              vsrc[isrc]->setJetEta(jethelper3_eta[0]);
	      shift=1.0-vsrc[isrc]->getUncertainty(false);
	      TLorentzVector jet1UpAbsolute;
	      jet1UpAbsolute.SetPtEtaPhiE(jethelper3_pt[0]*shift,jethelper3_eta[0],jethelper3_phi[0],jethelper3_energy[0]*shift);
              vsrc[isrc]->setJetPt(jethelper3_pt[1]);
              vsrc[isrc]->setJetEta(jethelper3_eta[1]);
	      shift=1.0-vsrc[isrc]->getUncertainty(false);
	      TLorentzVector jet2UpAbsolute;
	      jet2UpAbsolute.SetPtEtaPhiE(jethelper3_pt[1]*shift,jethelper3_eta[1],jethelper3_phi[1],jethelper3_energy[1]*shift);
              if(((jet1UpAbsolute+jet2UpAbsolute).M()>=massBins[j])&&
	         ((jet1UpAbsolute+jet2UpAbsolute).M()<massBins[j+1]))
                  histsJECdown[isrc][j]->Fill(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])), weight);
}
          }
	  
	  if((DijetMass>4000)||((DijetMass>3000)&&(exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1]))<2)))
  std::cout << eventhelper_run << ':' << eventhelper_luminosityBlock << ':' << eventhelper_event << " m=" << DijetMass << " chi=" << exp(fabs(jethelper3_rapidity[0]-jethelper3_rapidity[1])) << " y_boost= " << fabs(jethelper3_rapidity[0]+jethelper3_rapidity[1])/2. << " deltaPhi=" << fabs(reco::deltaPhi(jethelper3_phi[0],jethelper3_phi[1])) << std::endl;
  
	}

  std::cout << "done" << std::endl;

  h1->Write();
  h1->Draw("histe");
  gPad->SetLogy(true);
  c1.SaveAs((cmdline.outputfilename.substr(0,cmdline.outputfilename.size()-5)+"_mass.pdf").c_str());

  h1_ref->Write();
  h1_trig->Write();

  for ( size_t j = 0; j < (massBins.size()-1); ++j )
  {
      hists[j]->Write();
      histsnopu[j]->Write();
      histspu0[j]->Write();
      histspu10[j]->Write();
      histspu20[j]->Write();
      histspt1[j]->Write();
      histspt2[j]->Write();
      histsy1[j]->Write();
      histsy2[j]->Write();
      histsyboost[j]->Write();
      histsmetsumet[j]->Write();
      histsmptsumpt[j]->Write();
      histsdpt[j]->Write();
      histsdphi[j]->Write();
      hists[j]->Draw("histe");
for (int isrc = 0; isrc < nsrc; isrc++) {
      histsJECup[isrc][j]->Write();
      histsJECdown[isrc][j]->Write();
}
      std::stringstream name;
      name << cmdline.outputfilename.substr(0,cmdline.outputfilename.size()-5) << "_" << massBins[j] << "_" << massBins[j+1] << "_" << "chi.pdf";
      gPad->SetLogy(false);
      c1.SaveAs(name.str().c_str());
  }

  stream.close();
  ofile.close();

  return 0;
}
