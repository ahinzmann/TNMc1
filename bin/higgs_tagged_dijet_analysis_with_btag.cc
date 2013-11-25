//-----------------------------------------------------------------------------
// File:        analyzer.cc
// Description: Analyzer for ntuples created by TheNtupleMaker
// Created:     Wed Sept 18 
// Author:      Andreas Hinzmann / Tijs Karskens
//-----------------------------------------------------------------------------

#include "higgs_tagged_dijet_analysis.h"



#ifdef PROJECT_NAME
#include "PhysicsTools/TheNtupleMaker/interface/pdg.h"
#else
#include "pdg.h"
#endif

#include "TLorentzVector.h"

using namespace std;


Double_t fnc_dscb(Double_t *xx, Double_t *pp)
{
  Double_t x   = xx[0];
  Double_t N   = pp[0];
  Double_t mu  = pp[1];
  Double_t sig = pp[2];
  Double_t a1  = pp[3];
  Double_t p1  = pp[4];
  Double_t a2  = pp[5];
  Double_t p2  = pp[6];

  Double_t u   = (x-mu)/sig;
  Double_t A1  = TMath::Power(p1/TMath::Abs(a1),p1)*TMath::Exp(-a1*a1/2);
  Double_t A2  = TMath::Power(p2/TMath::Abs(a2),p2)*TMath::Exp(-a2*a2/2);
  Double_t B1  = p1/TMath::Abs(a1) - TMath::Abs(a1);
  Double_t B2  = p2/TMath::Abs(a2) - TMath::Abs(a2);

  Double_t result=N;
  if (u<-a1)
      result *= A1*TMath::Power(B1-u,-p1);
  else if (u<a2)
      result *= TMath::Exp(-u*u/2);
  else
      result *= A2*TMath::Power(B2+u,-p2);
  return result;
}

	inline float deltaPhi(float phi1, float phi2) 
	{ 
   		float result = phi1 - phi2;
     	while (result > float(M_PI)) result -= float(2*M_PI);
     	while (result <= -float(M_PI)) result += float(2*M_PI);
     	return result;
    }
    
	inline float deltaR(float eta1, float eta2, float dphi12) 
    {
    	float deta = eta1 - eta2;
    	float dr = sqrt( deta*deta + dphi12*dphi12 );
    	return dr;
    } 

     

//-----------------------------------------------------------------------------
int main(int argc, char** argv)
{
  // Get file list and histogram filename from command line

  cout << "Start program" << endl;

  commandLine cmdline;
  decodeCommandLine(argc, argv, cmdline);

  // Get names of ntuple files to be processed and open chain of ntuples

  vector<string> filenames = getFilenames(cmdline.filelist);
  cout << "Open file stream" << endl;
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
  stream.select("edmEventHelperExtra_info.dijetCHS_invmass", eventhelperextra_dijetCHS_invmass);
  stream.select("edmEventHelperExtra_info.dijet_invmass", eventhelperextra_dijet_invmass);
  stream.select("edmEventHelperExtra_info.wj1CHS_energy", eventhelperextra_wj1CHS_energy);
  stream.select("edmEventHelperExtra_info.wj1CHS_eta", eventhelperextra_wj1CHS_eta);
  stream.select("edmEventHelperExtra_info.wj1CHS_mass", eventhelperextra_wj1CHS_mass);
  stream.select("edmEventHelperExtra_info.wj1CHS_nconst", eventhelperextra_wj1CHS_nconst);
  stream.select("edmEventHelperExtra_info.wj1CHS_phi", eventhelperextra_wj1CHS_phi);
  stream.select("edmEventHelperExtra_info.wj1CHS_pt", eventhelperextra_wj1CHS_pt);
  stream.select("edmEventHelperExtra_info.wj1_energy", eventhelperextra_wj1_energy);
  stream.select("edmEventHelperExtra_info.wj1_eta", eventhelperextra_wj1_eta);
  stream.select("edmEventHelperExtra_info.wj1_mass", eventhelperextra_wj1_mass);
  stream.select("edmEventHelperExtra_info.wj1_nconst", eventhelperextra_wj1_nconst);
  stream.select("edmEventHelperExtra_info.wj1_phi", eventhelperextra_wj1_phi);
  stream.select("edmEventHelperExtra_info.wj1_pt", eventhelperextra_wj1_pt);
  stream.select("edmEventHelperExtra_info.wj1wj2CHS_invmass", eventhelperextra_wj1wj2CHS_invmass);
  stream.select("edmEventHelperExtra_info.wj1wj2CHS_nconst", eventhelperextra_wj1wj2CHS_nconst);
  stream.select("edmEventHelperExtra_info.wj1wj2_invmass", eventhelperextra_wj1wj2_invmass);
  stream.select("edmEventHelperExtra_info.wj1wj2_nconst", eventhelperextra_wj1wj2_nconst);
  stream.select("edmEventHelperExtra_info.wj2CHS_energy", eventhelperextra_wj2CHS_energy);
  stream.select("edmEventHelperExtra_info.wj2CHS_eta", eventhelperextra_wj2CHS_eta);
  stream.select("edmEventHelperExtra_info.wj2CHS_mass", eventhelperextra_wj2CHS_mass);
  stream.select("edmEventHelperExtra_info.wj2CHS_nconst", eventhelperextra_wj2CHS_nconst);
  stream.select("edmEventHelperExtra_info.wj2CHS_phi", eventhelperextra_wj2CHS_phi);
  stream.select("edmEventHelperExtra_info.wj2CHS_pt", eventhelperextra_wj2CHS_pt);
  stream.select("edmEventHelperExtra_info.wj2_energy", eventhelperextra_wj2_energy);
  stream.select("edmEventHelperExtra_info.wj2_eta", eventhelperextra_wj2_eta);
  stream.select("edmEventHelperExtra_info.wj2_mass", eventhelperextra_wj2_mass);
  stream.select("edmEventHelperExtra_info.wj2_nconst", eventhelperextra_wj2_nconst);
  stream.select("edmEventHelperExtra_info.wj2_phi", eventhelperextra_wj2_phi);
  stream.select("edmEventHelperExtra_info.wj2_pt", eventhelperextra_wj2_pt);
  stream.select("GenEventInfoProduct_generator.weight", geneventinfoproduct_weight);
  
  stream.select("patJetHelper_patJetsWithVar.chargedEmEnergyFraction", jethelperNoCHS_chargedEmEnergyFraction);
  stream.select("patJetHelper_patJetsWithVar.chargedHadronEnergyFraction", jethelperNoCHS_chargedHadronEnergyFraction);
  stream.select("patJetHelper_patJetsWithVar.chargedMultiplicity", jethelperNoCHS_chargedMultiplicity);
  stream.select("patJetHelper_patJetsWithVar.energy", jethelperNoCHS_energy);
  stream.select("patJetHelper_patJetsWithVar.eta", jethelperNoCHS_eta);
  stream.select("patJetHelper_patJetsWithVar.rapidity", jethelperNoCHS_rapidity);
  stream.select("patJetHelper_patJetsWithVar.mass", jethelperNoCHS_mass);
  stream.select("patJetHelper_patJetsWithVar.muonEnergyFraction", jethelperNoCHS_muonEnergyFraction);
  stream.select("patJetHelper_patJetsWithVar.nConstituents", jethelperNoCHS_nConstituents);
  stream.select("patJetHelper_patJetsWithVar.neutralEmEnergyFraction", jethelperNoCHS_neutralEmEnergyFraction);
  stream.select("patJetHelper_patJetsWithVar.neutralHadronEnergyFraction", jethelperNoCHS_neutralHadronEnergyFraction);
  stream.select("patJetHelper_patJetsWithVar.phi", jethelperNoCHS_phi);
  stream.select("patJetHelper_patJetsWithVar.pt", jethelperNoCHS_pt);
  stream.select("patJetHelper_patJetsWithVarCHS.chargedEmEnergyFraction", jethelper_chargedEmEnergyFraction);
  stream.select("patJetHelper_patJetsWithVarCHS.chargedHadronEnergyFraction", jethelper_chargedHadronEnergyFraction);
  stream.select("patJetHelper_patJetsWithVarCHS.chargedMultiplicity", jethelper_chargedMultiplicity);
  stream.select("patJetHelper_patJetsWithVarCHS.combinedSecondaryVertexBJetTags", jethelper_combinedSecondaryVertexBJetTags);
  stream.select("patJetHelper_patJetsWithVarCHS.combinedSecondaryVertexMVABJetTags", jethelper_combinedSecondaryVertexMVABJetTags);
  stream.select("patJetHelper_patJetsWithVarCHS.energy", jethelper_energy);
  stream.select("patJetHelper_patJetsWithVarCHS.eta", jethelper_eta);
  stream.select("patJetHelper_patJetsWithVarCHS.rapidity", jethelper_rapidity);
  stream.select("patJetHelper_patJetsWithVarCHS.jetBProbabilityBJetTags", jethelper_jetBProbabilityBJetTags);
  stream.select("patJetHelper_patJetsWithVarCHS.jetProbabilityBJetTags", jethelper_jetProbabilityBJetTags);
  stream.select("patJetHelper_patJetsWithVarCHS.mass", jethelper_mass);
  stream.select("patJetHelper_patJetsWithVarCHS.muonEnergyFraction", jethelper_muonEnergyFraction);
  stream.select("patJetHelper_patJetsWithVarCHS.nConstituents", jethelper_nConstituents);
  stream.select("patJetHelper_patJetsWithVarCHS.neutralEmEnergyFraction", jethelper_neutralEmEnergyFraction);
  stream.select("patJetHelper_patJetsWithVarCHS.neutralHadronEnergyFraction", jethelper_neutralHadronEnergyFraction);
  stream.select("patJetHelper_patJetsWithVarCHS.phi", jethelper_phi);
  stream.select("patJetHelper_patJetsWithVarCHS.pt", jethelper_pt);
  
  
  stream.select("cmgPFJet_cmgPFJetSelCHS.pt", cmgPFJet_cmgPFJetSelCHS_pt);
  stream.select("cmgPFJet_cmgPFJetSelCHS.eta", cmgPFJet_cmgPFJetSelCHS_eta);
  stream.select("cmgPFJet_cmgPFJetSelCHS.phi", cmgPFJet_cmgPFJetSelCHS_phi);
  stream.select("cmgPFJet_cmgPFJetSelCHS.energy", cmgPFJet_cmgPFJetSelCHS_energy);
  stream.select("cmgPFJet_cmgPFJetSelCHS.mass", cmgPFJet_cmgPFJetSelCHS_mass);
  stream.select("cmgPFJet_cmgPFJetSelCHS.combinedSecondaryVertexBJetTags", cmgPFJet_cmgPFJetSelCHS_combinedSecondaryVertexBJetTags);
  
  
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.pt", jethelperAK5_pt);
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.eta", jethelperAK5_eta);
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.phi", jethelperAK5_phi);
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.energy", jethelperAK5_energy);
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.mass", jethelperAK5_mass);
  stream.select("patJetHelper_selectedPatJetsAK5CHSpruned.combinedSecondaryVertexBJetTags", jethelperAK5_combinedSecondaryVertexBJetTags);
  
  
  stream.select("npatJetHelper_selectedPatJetsCA8CHSwithQjets", njethelperCA8);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.combinedSecondaryVertexBJetTags", jethelperCA8_combinedSecondaryVertexBJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.combinedSecondaryVertexMVABJetTags", jethelperCA8_combinedSecondaryVertexMVABJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.energy", jethelperCA8_energy);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.et", jethelperCA8_et);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.eta", jethelperCA8_eta);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.jetArea", jethelperCA8_jetArea);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.jetBProbabilityBJetTags", jethelperCA8_jetBProbabilityBJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.jetProbabilityBJetTags", jethelperCA8_jetProbabilityBJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.mass", jethelperCA8_mass);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.nConstituents", jethelperCA8_nConstituents);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.partonFlavour", jethelperCA8_partonFlavour);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.chargedEmEnergyFraction", jethelperCA8_chargedEmEnergyFraction);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.chargedHadronEnergyFraction", jethelperCA8_chargedHadronEnergyFraction);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.chargedMultiplicity", jethelperCA8_chargedMultiplicity);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.muonEnergyFraction", jethelperCA8_muonEnergyFraction);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.neutralEmEnergyFraction", jethelperCA8_neutralEmEnergyFraction);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.neutralHadronEnergyFraction", jethelperCA8_neutralHadronEnergyFraction);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.phi", jethelperCA8_phi);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.pt", jethelperCA8_pt);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.trackCountingHighEffBJetTags", jethelperCA8_trackCountingHighEffBJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.trackCountingHighPurBJetTags", jethelperCA8_trackCountingHighPurBJetTags);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.uncor_energy", jethelperCA8_uncor_energy);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.uncor_et", jethelperCA8_uncor_et);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.uncor_pt", jethelperCA8_uncor_pt);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.tau1", jethelperCA8_tau1);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.tau2", jethelperCA8_tau2);
  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.C2beta17", jethelperCA8_C2beta17);
  stream.select("npatJetHelper_selectedPatJetsCA8CHSpruned", njethelperCA8pruned);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.mass", jethelperCA8pruned_mass);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.phi", jethelperCA8pruned_phi);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.eta", jethelperCA8pruned_eta);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.pt", jethelperCA8pruned_pt);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.energy", jethelperCA8pruned_energy); // was selectedPatJetsCA8CHSpruned.pt earlier -> is that correct?
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.uncor_pt", jethelperCA8pruned_uncor_pt);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.numberOfDaughters", jethelperCA8pruned_numberOfDaughters);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_energy", jethelperCA8pruned_daughter_0_energy);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_eta", jethelperCA8pruned_daughter_0_eta);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_mass", jethelperCA8pruned_daughter_0_mass);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_phi", jethelperCA8pruned_daughter_0_phi);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_pt", jethelperCA8pruned_daughter_0_pt);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_0_combinedSecondaryVertexBJetTags", jethelperCA8pruned_daughter_0_combinedSecondaryVertexBJetTags);
  
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_energy", jethelperCA8pruned_daughter_1_energy);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_eta", jethelperCA8pruned_daughter_1_eta);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_mass", jethelperCA8pruned_daughter_1_mass);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_phi", jethelperCA8pruned_daughter_1_phi);
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_pt", jethelperCA8pruned_daughter_1_pt);
  
  stream.select("patJetHelper_selectedPatJetsCA8CHSpruned.daughter_1_combinedSecondaryVertexBJetTags", jethelperCA8pruned_daughter_1_combinedSecondaryVertexBJetTags);

  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.combinedSecondaryVertexBJetTags", jethelperAK7_combinedSecondaryVertexBJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.combinedSecondaryVertexMVABJetTags", jethelperAK7_combinedSecondaryVertexMVABJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.energy", jethelperAK7_energy);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.et", jethelperAK7_et);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.eta", jethelperAK7_eta);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.jetArea", jethelperAK7_jetArea);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.jetBProbabilityBJetTags", jethelperAK7_jetBProbabilityBJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.jetProbabilityBJetTags", jethelperAK7_jetProbabilityBJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.mass", jethelperAK7_mass);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.nConstituents", jethelperAK7_nConstituents);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.partonFlavour", jethelperAK7_partonFlavour);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.phi", jethelperAK7_phi);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.pt", jethelperAK7_pt);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.trackCountingHighEffBJetTags", jethelperAK7_trackCountingHighEffBJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.trackCountingHighPurBJetTags", jethelperAK7_trackCountingHighPurBJetTags);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.uncor_energy", jethelperAK7_uncor_energy);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.uncor_et", jethelperAK7_uncor_et);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.uncor_pt", jethelperAK7_uncor_pt);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.tau1", jethelperAK7_tau1);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.tau2", jethelperAK7_tau2);
  stream.select("patJetHelper_selectedPatJetsAK7CHSwithQjets.C2beta17", jethelperAK7_C2beta17);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.mass", jethelperAK7pruned_mass);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.pt", jethelperAK7pruned_pt);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.uncor_pt", jethelperAK7pruned_uncor_pt);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.numberOfDaughters", jethelperAK7pruned_numberOfDaughters);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_0_energy", jethelperAK7pruned_daughter_0_energy);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_0_eta", jethelperAK7pruned_daughter_0_eta);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_0_mass", jethelperAK7pruned_daughter_0_mass);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_0_phi", jethelperAK7pruned_daughter_0_phi);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_0_pt", jethelperAK7pruned_daughter_0_pt);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_1_energy", jethelperAK7pruned_daughter_1_energy);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_1_eta", jethelperAK7pruned_daughter_1_eta);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_1_mass", jethelperAK7pruned_daughter_1_mass);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_1_phi", jethelperAK7pruned_daughter_1_phi);
  stream.select("patJetHelper_selectedPatJetsAK7CHSpruned.daughter_1_pt", jethelperAK7pruned_daughter_1_pt);

  stream.select("patMET_patMETsRaw.et", met2_et);
  stream.select("patMET_patMETsRaw.sumEt", met2_sumEt);
  stream.select("nrecoVertex_offlinePrimaryVertices", nvertex);
  stream.select("edmEventHelperExtra_info.numberOfPrimaryVertices", eventhelperextra_numberOfPrimaryVertices);
  stream.select("sdouble_vertexWeightSummer12MC53X2012ABCDData.value", vertexWeight);
  stream.select("PileupSummaryInfo_addPileupInfo.getBunchCrossing", pileupsummaryinfo_getBunchCrossing);
  stream.select("PileupSummaryInfo_addPileupInfo.getPU_NumInteractions", pileupsummaryinfo_getPU_NumInteractions);
  stream.select("PileupSummaryInfo_addPileupInfo.getTrueNumInteractions", pileupsummaryinfo_getTrueNumInteractions);
  stream.select("sdouble_kt6PFJets_rho.value", sdouble_kt6PFJets_rho_value);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8);                                                                                                        // 
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11);                                                                                                        //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12", triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12);                                                                                                        // <--
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT500_v1", triggerresultshelper_HLT_HT500_v1); 
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT500_v2", triggerresultshelper_HLT_HT500_v2); 
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT500_v3", triggerresultshelper_HLT_HT500_v3); 
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v1", triggerresultshelper_HLT_HT550_v1); // <--
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v2", triggerresultshelper_HLT_HT550_v2); // trigger moniteur
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v3", triggerresultshelper_HLT_HT550_v3); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v4", triggerresultshelper_HLT_HT550_v4); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v5", triggerresultshelper_HLT_HT550_v5); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v6", triggerresultshelper_HLT_HT550_v6); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v7", triggerresultshelper_HLT_HT550_v7); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v8", triggerresultshelper_HLT_HT550_v8); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT550_v9", triggerresultshelper_HLT_HT550_v9); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v1", triggerresultshelper_HLT_HT650_v1); // <--
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v2", triggerresultshelper_HLT_HT650_v2); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v3", triggerresultshelper_HLT_HT650_v3); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v4", triggerresultshelper_HLT_HT650_v4); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v5", triggerresultshelper_HLT_HT650_v5); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v6", triggerresultshelper_HLT_HT650_v6); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v7", triggerresultshelper_HLT_HT650_v7); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v8", triggerresultshelper_HLT_HT650_v8); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT650_v9", triggerresultshelper_HLT_HT650_v9); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v1", triggerresultshelper_HLT_HT750_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v2", triggerresultshelper_HLT_HT750_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_HT750_v3", triggerresultshelper_HLT_HT750_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v1", triggerresultshelper_HLT_PFHT650_v1); // <--
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v2", triggerresultshelper_HLT_PFHT650_v2); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v3", triggerresultshelper_HLT_PFHT650_v3); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v4", triggerresultshelper_HLT_PFHT650_v4); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v5", triggerresultshelper_HLT_PFHT650_v5); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v6", triggerresultshelper_HLT_PFHT650_v6); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v7", triggerresultshelper_HLT_PFHT650_v7); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v8", triggerresultshelper_HLT_PFHT650_v8); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v9", triggerresultshelper_HLT_PFHT650_v9); //
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v10", triggerresultshelper_HLT_PFHT650_v10);//
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT650_v11", triggerresultshelper_HLT_PFHT650_v11);//
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v1", triggerresultshelper_HLT_PFHT700_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v2", triggerresultshelper_HLT_PFHT700_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v3", triggerresultshelper_HLT_PFHT700_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v4", triggerresultshelper_HLT_PFHT700_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v5", triggerresultshelper_HLT_PFHT700_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT700_v6", triggerresultshelper_HLT_PFHT700_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v1", triggerresultshelper_HLT_PFHT750_v1);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v2", triggerresultshelper_HLT_PFHT750_v2);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v3", triggerresultshelper_HLT_PFHT750_v3);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v4", triggerresultshelper_HLT_PFHT750_v4);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v5", triggerresultshelper_HLT_PFHT750_v5);
  stream.select("edmTriggerResultsHelper_TriggerResults_HLT.HLT_PFHT750_v6", triggerresultshelper_HLT_PFHT750_v6);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.hcalLaserEventFilterPath", triggerresultshelper_hcalLaserEventFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.noscrapingFilterPath", triggerresultshelper_noscrapingFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.primaryVertexFilterPath", triggerresultshelper_primaryVertexFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.trackingFailureFilterPath", triggerresultshelper_trackingFailureFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.CSCTightHaloFilterPath", triggerresultshelper_CSCTightHaloFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.EcalDeadCellBoundaryEnergyFilterPath", triggerresultshelper_EcalDeadCellBoundaryEnergyFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.EcalDeadCellTriggerPrimitiveFilterPath", triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath);
  stream.select("edmTriggerResultsHelper_TriggerResults_PAT.HBHENoiseFilterPath", triggerresultshelper_HBHENoiseFilterPath);
  stream.select("sint_hcallasereventfilter2012.value", triggerresultshelper_hcallasereventfilter2012);

  stream.select("nrecoGenParticleHelper_genParticles", ngenparticlehelper);
  stream.select("recoGenParticleHelper_genParticles.firstDaughter", genparticlehelper_firstDaughter);
  stream.select("recoGenParticleHelper_genParticles.firstMother", genparticlehelper_firstMother);
  stream.select("recoGenParticleHelper_genParticles.lastDaughter", genparticlehelper_lastDaughter);
  stream.select("recoGenParticleHelper_genParticles.lastMother", genparticlehelper_lastMother);
  stream.select("recoGenParticleHelper_genParticles.pdgId", genparticlehelper_pdgId);

  stream.select("recoGenParticleHelper_genParticles.eta", genparticlehelper_eta);
  stream.select("recoGenParticleHelper_genParticles.phi", genparticlehelper_phi);
  stream.select("recoGenParticleHelper_genParticles.pt", genparticlehelper_pt);
  stream.select("recoGenParticleHelper_genParticles.mass", genparticlehelper_mass);
  stream.select("npatJetHelper_patGenJetsCA8CHS", njethelperGenCA8);
  stream.select("patJetHelper_patGenJetsCA8CHS.mass", jethelperGenCA8_mass);
  stream.select("patJetHelper_patGenJetsCA8CHS.eta", jethelperGenCA8_eta);
  stream.select("patJetHelper_patGenJetsCA8CHS.phi", jethelperGenCA8_phi);
  stream.select("patJetHelper_patGenJetsCA8CHS.pt", jethelperGenCA8_pt);
  stream.select("patJetHelper_patGenJetsCA8CHS.et", jethelperGenCA8_et);
  stream.select("npatJetHelper_patGenJetsCA8CHSpruned", njethelperGenCA8pruned);
  stream.select("patJetHelper_patGenJetsCA8CHSpruned.mass", jethelperGenCA8pruned_mass);
  stream.select("patJetHelper_patGenJetsCA8CHSpruned.eta", jethelperGenCA8pruned_eta);
  stream.select("patJetHelper_patGenJetsCA8CHSpruned.phi", jethelperGenCA8pruned_phi);
  stream.select("patJetHelper_patGenJetsCA8CHSpruned.pt", jethelperGenCA8pruned_pt);
  
//  stream.select("patJetHelper_patJetsWithVarCHS.combinedSecondaryVertexBJetTags"
  stream.select("patJetHelper_patJetsWithVarCHS.combinedSecondaryVertexBJetTags", jethelper_combinedSecondaryVertexBJetTags);


 // stream.select("patJetHelper_patGenJetsAK5.pt", jethelperGenAK5_pt);
//  stream.select("patJetHelper_selectedPatJetsCA8CHSwithQjets.et", jethelperCA8_et);
/*
  stream.select("cmgPFJet_cmgPFJetSel.energy", jethelperCMG_energy);
  stream.select("cmgPFJet_cmgPFJetSel.eta", jethelperCMG_eta);
  stream.select("cmgPFJet_cmgPFJetSel.rapidity", jethelperCMG_rapidity);
  stream.select("cmgPFJet_cmgPFJetSel.mass", jethelperCMG_mass);
  stream.select("cmgPFJet_cmgPFJetSel.phi", jethelperCMG_phi);
  stream.select("cmgPFJet_cmgPFJetSel.pt", jethelperCMG_pt);
*/
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

  const int NBINS = 104;
  Double_t BOUNDARIES[NBINS] = {1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325,
  354, 386, 419, 453, 489, 526, 565, 606, 649, 693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687,
  1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509,
  4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7060, 7320, 7589, 7866, 8152, 8447, 8752, 9067, 9391, 9726, 10072, 10430, 
  10798, 11179, 11571, 11977, 12395, 12827, 13272, 13732, 14000};

  TH1F* mass_0mtag=new TH1F("dijet_mass_0mtag","M_{jj}",8000,0,8000);                               // declaration
  mass_0mtag->Sumw2();                                                                              // 
  TH1F* mass_1mtag_1lptag=new TH1F("dijet_mass_1mtag_1lptag","M_{jj}",8000,0,8000);                 // of the event
  mass_1mtag_1lptag->Sumw2();                                                                       //
  TH1F* mass_1mtag_1hptag=new TH1F("dijet_mass_1mtag_1hptag","M_{jj}",8000,0,8000);                 // categories,
  mass_1mtag_1hptag->Sumw2();                                                                       //
  TH1F* mass_2mtag_2lptag=new TH1F("dijet_mass_2mtag_2lptag","M_{jj}",8000,0,8000);                 // see the part
  mass_2mtag_2lptag->Sumw2();                                                                       //
  TH1F* mass_2mtag_1hptag_1lptag=new TH1F("dijet_mass_2mtag_1hptag_1lptag","M_{jj}",8000,0,8000);   // "fill histograms"
  mass_2mtag_1hptag_1lptag->Sumw2();                                                                //
  TH1F* mass_2mtag_2hptag=new TH1F("dijet_mass_2mtag_2hptag","M_{jj}",8000,0,8000);                 // below
  mass_2mtag_2hptag->Sumw2();                                                                       //
  
  TH1F* mass=new TH1F("dijet_mass","M_{jj}",8000,0,8000);                                           // histogram of the masses of all the ranked events
  mass->Sumw2();                                                                                    //

  Double_t mgg;
  Double_t evWeight = 1.0;
  Int_t categories;
  Int_t categoriesNS;
  double weight=1.0;
  const double pi=3.141592654;

  //TTree *TCVARS = new TTree("TCVARS", "VV selection");                       // create the TCVARS tree (ranked, mgg>890, deta<1.3)                     
  //TCVARS->Branch("mgg",&mgg,"mgg/D");                                         // as well as its branches.
  //TCVARS->Branch("evWeight",&evWeight,"evWeight/D");                          //
  //TCVARS->Branch("Weight",&weight,"Weight/D");                                // 
  //TCVARS->Branch("categories",&categories,"categories/I");                    //
  //TCVARS->Branch("categoriesNS",&categoriesNS,"categoriesNS/I");              //

  double DijetMass;
  double DijetMassNoCHS;
  double DijetMassCA8;
  double deta;
  double cteta;
  double Ht;
  double njets;
  double njetsCA8;  
  double Jet1pt;
  double Jet2pt;
  double Jet1eta;
  double Jet2eta;
  double Jet1phi;
  double Jet2phi;
  double dphi;
  double met;
  double Jet1CA8_prunedmass;
  double Jet2CA8_prunedmass;
    
  double Jet_NonFatVar_eta;
  double Jet_NonFatVar_pruned_eta;
  double Jet_NonFatVar_pruned_phi;
  
  double Jet_NonFatVar_pt;		
  double Jet_NonFatVar_pruned_pt;
  double Jet_NonFatVar_phi;
  double Jet_SecondNonFatVar_bjetness_pruned_eta;
  double Jet_SecondNonFatVar_bjetness_pruned_phi;

  double Jet_SecondNonFatVar_HighestPt_pruned_eta;
  double Jet_SecondNonFatVar_HighestPt_pruned_phi;
	// some new variables by tijs
  double nNrMoreJetsEvents;
  double Jet3CA8_prunedmass;
  double Jet2plus3CA8Mass;
  double Jet2plus3CA8Massb;
  double Jet2plus3CA8Massc;
  
  double Highestpt13;
  double HighestptJetnr13;
  double Highestpt10;
  double HighestptJetnr10;
  double Highestpt08;
  double HighestptJetnr08;
  double HighestptUsed;
  double JetXeta;                         
  double JetXphi;
  double JetXpt;  
  double JetXCA8_prunedmass ;
  double Jet2plusXCA8Mass;
  double Jet2plusXCA8Massc;
  double deltaR2X08;
  double deltaR2X13;
  double deltaR2X10;
  double Jet2AK7mass;
  double deltaR2Xb;
  double JetXCA8Nsub;
  double NrJetsInHiggsWindow;
  double JetYCA8Nsub;
  double JetYCA8_prunedmass;
  double WhichJetInHiggsWindow;
  double FattieNumber;
  double JetFatCA8_prunedmass;
  	double Jet_NonFat;
	double Jet_NonFat_Number;
	double Jet_NonFatCA8_pruned_mass;
	double Jet_NonFat_pt;
	double Jet_NonFat_eta;
	double Jet_NonFat_phi;			
	double deltaRFatNonFat;
	double JetFatphi;
	double JetFateta;
	double Jet_SecondNonFat_HighestPt;
	double Jet_SecondNonFat_HighestPt_Number;
	double Jet_SecondNonFat_pt;
	double	Jet_SecondNonFat_eta;
      	double	Jet_SecondNonFat_phi;
      	double	Jet_SecondNonFatCA8_pruned_mass;
//      	double Jet_NonFat_plus_SecondNonFatCA8Mass;
//      	double Jet_NonFat_plus_SecondNonFatCA8Massc;
      	double deltaRNonFatSecondNonFat;
      	double Jet_SecondNonFatCA8Nsub;
      	double Jet_NonFatCA8Nsub;
      	double NonFatbJetness;
      	double FatbJetness;
//      	double Jet_NonFat_plus_SecondNonFatCA8Massc_NonFatBelow50;
//      	double Jet_NonFat_plus_SecondNonFatCA8Massc_NonFatBelow80;
//      	double Jet_NonFat_plus_SecondNonFatCA8Massc_NonFatBelow70;
      	
      	
//      		double Jet_NonFat_plus_SecondNonFatCA8Mass_pruned;
      		double Jet_NonFatVarMass;
		double deltaRNonFatNonFatVar;
		double Jet_NonFatAK5Mass;
		double Jet_NonFatAK5eta;
		double Jet_NonFatAK5phi;
    		double Jet_NonFatAK5pt;
		double deltaRNonFatNonFatAK5;
		double HighestNonFatAK5Pt;
		double HighestNonFatAK5PtJetNr;
		double deltaRVarNonVarSmallestDr_jetnumber;
		double deltaRVarNonVarSmallestDr_dummy;
  		double deltaRVarNonVarSmallestDr;
  		double Jet_NonFatVar_bjetness;

		double twojetsmass2;
		double twojetsmass1;
		double Jet_SecondNonFatVar_Number;
		double	Jet_NonFatVar_Number;
		double deltaR_NonFatVar_SecondNonFatVar;
				

  		double deltaR_SecondNonFatVar_CA8_Smallest;
  		double deltaR_SecondNonFatVar_CA8_Jetnumber;
  		double Jet_SecondNonFatVar_prunedCA8Mass;

  		
  		
  		double dphi_Fat_NonFatVar;
  		double HighestNonFatVarPt;
		double HighestNonFatVarPt_Number;
		double deltaR_Fat_NonFatVar;
		double Jet_SecondNonFatVar_bjetness;
		double Jet_SecondNonFatVar_bjetness_Number;
		double deltaR_NonFatVar_SecondNonFatVar_bjetness;
		double Jet_SecondNonFatVar_HighestPt;
		double Jet_SecondNonFatVar_HighestPt_Number;
		double deltaR_NonFatVar_SecondNonFatVar_HighestPt;
		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness;
		double	Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt;
  		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness;
		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt;		
//		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_approx_bjetness;
//		double	Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_approx_HighestPt;
//		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness_bjetcut_medium;
//		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt_bjetcut_medium;
//		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness_bjetcut_tight;
//		double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt_bjetcut_tight;
  		double bjetness_Jet0;
  		double bjetness_Jet1;
  		double bjetness_Jet2;
  		double bjetness_Jet3;
  		double bjetness_Jet4;
  		double bjetness_Jet5;
  		double bjetness_Jet6;
  		double bjetness_Jet7;
  		double Jet_SecondNonFatVar_HighestPt_mass;
		double Jet_SecondNonFatVar_bjetness_mass;
		double Jet_NonFatVar_mass;
		double Jet_NonFatCA8_mass;
		
		double Jet_SecondNonFat_pruned_pt;
		double	Jet_SecondNonFat_pruned_eta;
    	      	double Jet_SecondNonFat_pruned_phi;
 //   	      	double Jet_NonFat_plus_SecondNonFatCA8Massc_pruned;
    	      	
    	      	double Jet_NonFat_pruned;
		double Jet_NonFat_pruned_Number;
		double Jet_NonFat_pruned_bjetness;
    	      	
    	      	double JetFatsub;

    	      	double Jet_NonFat_bjetness;
    	      	double Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness;
    		double Jet_NonFat_plus_SecondNonFat_CA8Massc_bjetness;
    		double Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness;
    		double Jet_NonFat_plus_SecondNonFat_CA8Massc_pruned_bjetness;
    		double Jet_SecondNonFatCA8_pruned_bjetness_mass;
    		double Jet_SecondNonFat_bjetness_pt;
		double Jet_SecondNonFat_bjetness_eta;
    	      	double Jet_SecondNonFat_bjetness_phi;
   	      	double Jet_SecondNonFat_bjetness_pruned_pt;
		double Jet_SecondNonFat_bjetness_pruned_eta;
    	      	double Jet_SecondNonFat_bjetness_pruned_phi;
		double deltaR_NonFat_SecondNonFat_bjetness;
    	      	double Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt;
    		double Jet_NonFat_plus_SecondNonFat_CA8Massc_HighestPt;
    		double Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt;
    		double Jet_NonFat_plus_SecondNonFat_CA8Massc_pruned_HighestPt;
    		double Jet_SecondNonFatCA8_pruned_HighestPt_mass;
    		double Jet_SecondNonFat_HighestPt_pt;
		double Jet_SecondNonFat_HighestPt_eta;
    	      	double Jet_SecondNonFat_HighestPt_phi;
   	      	double Jet_SecondNonFat_HighestPt_pruned_pt;
		double Jet_SecondNonFat_HighestPt_pruned_eta;
    	      	double Jet_SecondNonFat_HighestPt_pruned_phi;
		double deltaR_NonFat_SecondNonFat_HighestPt;   
		

    	      	double Jet_NonFat_pruned_eta;
		double Jet_NonFat_pruned_phi;
    		double Jet_NonFat_pruned_pt;
    	      	
    	      	double Jet_SecondNonFat_bjetness;
		double Jet_SecondNonFat_bjetness_Number;
		double TwoFatJet_2hp_mass;
		double TwoFatJet_dEta;		
		double Resonancemass_HighestPt;
		double Resonancemass_HighestPt_pruned;		
		double Resonancemass_bjetness;
		double Resonancemass_bjetness_pruned;
		double Resonancemass_AK5_bjetness;
		double Resonancemass_AK5_HighestPt;

  double JetFat_daughter1_bjetness;
  double JetFat_daughter0_bjetness;
  
  //double dEta_Fat_RecH_pruned_HighestPt;
  double dEta_Fat_AK5RecH_bjetness;
  double dEta_Fat_AK5RecH_pruned_bjetness;
  double dEta_Fat_AK5RecH_HighestPt ;
  double dEta_Fat_AK5RecH_pruned_HighestPt;
  double dEta_Fat_CA8RecH_pruned_HighestPt;
  double dEta_Fat_CA8RecH_HighestPt;
  double dEta_Fat_CA8RecH_pruned_bjetness;
  double dEta_Fat_CA8RecH_bjetness;
			

  double Jet0_daughter0_bjetness;
  double Jet0_daughter1_bjetness;
  double Jet1_daughter0_bjetness;
  double Jet1_daughter1_bjetness;

  
  		
  		
  double Jet1CA8MassDrop;
  double Jet2CA8MassDrop;
  double Jet1CA8Nsub;
  double Jet2CA8Nsub;
  double Jet3CA8Nsub;
  double dphi1;
  double dphi2;
  double Jet1dr;
  double Jet2dr;
  int nbvert;
  double Jet1CA8C2beta17;
  double Jet2CA8C2beta17;
  double Jet1mef;
  double Jet1nhef;
  double Jet1neef;
  int Jet1nbcons;
  double Jet1chef;
  double Jet1ceef;
  double Jet1cmult;
  double Jet2mef;
  double Jet2nhef;
  double Jet2neef;
  int  Jet2nbcons;
  double Jet2chef;
  double Jet2ceef;
  double Jet2cmult;
  int fat;
  int ht550;
  int ht650;
  int pfht650;

  
  double dphiparttogenij;
  double detaparttogenij;
  double drparttogenij;
  double drparttogeni;
  int jparttogeni;
  double genjetmass1;
  double genjetphi1;
  double genjeteta1;
  double genjetpt1;
  double genjetmass2;
  double genjetphi2;
  double genjeteta2;
  double genjetpt2;
  double prunedgenjetmass1;
  double prunedgenjetphi1;
  double prunedgenjeteta1;
  double prunedgenjetpt1;
  double prunedgenjetmass2;
  double prunedgenjetphi2;
  double prunedgenjeteta2;
  double prunedgenjetpt2;
  double recojetmass1;
  double recojetphi1;
  double recojeteta1;
  double recojetpt1;
  double recojetmass2;
  double recojetphi2;
  double recojeteta2;
  double recojetpt2;
  double prunedrecojetmass1;
  double prunedrecojetphi1;
  double prunedrecojeteta1;
  double prunedrecojetpt1;
  double prunedrecojetmass2;
  double prunedrecojetphi2;
  double prunedrecojeteta2;
  double prunedrecojetpt2;
  double dphigentoprunedgeni1;
  double detagentoprunedgeni1;
  double drgentoprunedgeni1;
  double dphigentoprunedgeni2;
  double detagentoprunedgeni2;
  double drgentoprunedgeni2;
  int igentoprunedgen1;
  double drgentoprunedgen1;
  int igentoprunedgen2;
  double drgentoprunedgen2;
  double dmgentoprunedgen1;
  double dmgentoprunedgen2;
  double dpgentoprunedgen1;
  double dpgentoprunedgen2;
  double dphigentorecoi1;
  double detagentorecoi1;
  double drgentorecoi1;
  double dphigentorecoi2;
  double detagentorecoi2;
  double drgentorecoi2;
  int igentoreco1;
  double drgentoreco1;
  int igentoreco2;
  double drgentoreco2;
  double dmgentoreco1;
  double dmgentoreco2;
  double dpgentoreco1;
  double dpgentoreco2;
  double dphirecotoprunedrecoi1;
  double detarecotoprunedrecoi1;
  double drrecotoprunedrecoi1;
  double dphirecotoprunedrecoi2;
  double detarecotoprunedrecoi2;
  double drrecotoprunedrecoi2;
  int irecotoprunedreco1;
  double drrecotoprunedreco1;
  int irecotoprunedreco2;
  double drrecotoprunedreco2;
  double dmrecotoprunedreco1;
  double dmrecotoprunedreco2;
  double dprecotoprunedreco1;
  double dprecotoprunedreco2;
  double dphiprunedgentoprunedreco1;
  double detaprunedgentoprunedreco1;
  double dphiprunedgentoprunedreco2;
  double detaprunedgentoprunedreco2;
  double drprunedgentoprunedreco1;
  double drprunedgentoprunedreco2;
  double dmprunedgentoprunedreco1;
  double dmprunedgentoprunedreco2;
  double dpprunedgentoprunedreco1;
  double dpprunedgentoprunedreco2;
  
  double dEta_Fat_NonFat_pruned;
  double dEta_Fat_NonFat;


  
  double HighestNonFatVarPt_pruned;
  double HighestNonFatVarPt_pruned_Number;
  double deltaR_Fat_NonFatVar_pruned;
  double dphi_Fat_NonFatVar_pruned;
  double Jet_NonFatVar_pruned_bjetness;
  double Jet_NonFatVar_pruned_mass;
  double Jet_SecondNonFatVar_pruned_bjetness;
  double Jet_SecondNonFatVar_pruned_bjetness_Number;
  double Jet_SecondNonFatVar_pruned_HighestPt;
  double Jet_SecondNonFatVar_pruned_HighestPt_Number;
  double deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness;
  double deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt;
  double Jet_SecondNonFatVar_pruned_HighestPt_mass;
  double Jet_SecondNonFatVar_pruned_bjetness_mass;

//  double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_approx_bjetness;
//  double Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_approx_HighestPt;
  double Resonancemass_AK5_pruned_bjetness;
  double Resonancemass_AK5_pruned_HighestPt;

  double deltaR_SecondNonFatVar_pruned_bjetness_SecondNonFatVar_pruned_HighestPt;
  double dEta_Fat_SecondNonFatVar_pruned;
  double dEta_Fat_NonFatVar_pruned;
  double dEta_NonFatVar_SecondNonFatVar_pruned;
  double Jet0daughter0_pt;
  double Jet0daughter1_pt;
  double Jet1daughter0_pt;
  double Jet1daughter1_pt;
  double Jet0daughter0_eta;
  double Jet0daughter1_eta;
  double Jet1daughter0_eta;
  double Jet1daughter1_eta;


TTree *Fullmassspectrum = new TTree("Fullmassspectrum", "Fullmassspectrum");

Fullmassspectrum->Branch("Jet0daughter0_pt", &Jet0daughter0_pt, "Jet0daughter0_pt/D");
Fullmassspectrum->Branch("Jet0daughter1_pt", &Jet0daughter1_pt, "Jet0daughter1_pt/D");
Fullmassspectrum->Branch("Jet1daughter0_pt", &Jet1daughter0_pt, "Jet1daughter0_pt/D");
Fullmassspectrum->Branch("Jet1daughter1_pt", &Jet1daughter1_pt, "Jet1daughter1_pt/D");
Fullmassspectrum->Branch("Jet0daughter0_eta", &Jet0daughter0_eta, "Jet0daughter0_eta/D");
Fullmassspectrum->Branch("Jet0daughter1_eta", &Jet0daughter1_eta, "Jet0daughter1_eta/D");
Fullmassspectrum->Branch("Jet1daughter0_eta", &Jet1daughter0_eta, "Jet1daughter0_eta/D");
Fullmassspectrum->Branch("Jet1daughter1_eta", &Jet1daughter1_eta, "Jet1daughter1_eta/D");

Fullmassspectrum->Branch("Jet1CA8Nsub", &Jet1CA8Nsub, "Jet1CA8Nsub/D");
Fullmassspectrum->Branch("Jet2CA8Nsub", &Jet2CA8Nsub, "Jet2CA8Nsub/D");
Fullmassspectrum->Branch("Jet1CA8_prunedmass", &Jet1CA8_prunedmass, "Jet1CA8_prunedmass/D");
Fullmassspectrum->Branch("Jet2CA8_prunedmass", &Jet2CA8_prunedmass, "Jet2CA8_prunedmass/D");
Fullmassspectrum->Branch("Jet0_daughter0_bjetness",&Jet0_daughter0_bjetness,"Jet0_daughter0_bjetness/D");   
Fullmassspectrum->Branch("Jet0_daughter1_bjetness",&Jet0_daughter1_bjetness,"Jet0_daughter1_bjetness/D");   		
Fullmassspectrum->Branch("Jet1_daughter0_bjetness",&Jet1_daughter0_bjetness,"Jet1_daughter0_bjetness/D");     
Fullmassspectrum->Branch("Jet1_daughter1_bjetness",&Jet1_daughter1_bjetness,"Jet1_daughter1_bjetness/D"); 


Fullmassspectrum->Branch("DijetMassCA8",&DijetMassCA8,"DijetMassCA8/D");
Fullmassspectrum->Branch("deta",&deta,"deta/D");   
Fullmassspectrum->Branch("Jet0_daughter0_bjetness",&Jet0_daughter0_bjetness,"Jet0_daughter0_bjetness/D");   
Fullmassspectrum->Branch("Jet0_daughter1_bjetness",&Jet0_daughter1_bjetness,"Jet0_daughter1_bjetness/D");   		
Fullmassspectrum->Branch("Jet1_daughter0_bjetness",&Jet1_daughter0_bjetness,"Jet1_daughter0_bjetness/D");     
Fullmassspectrum->Branch("Jet1_daughter1_bjetness",&Jet1_daughter1_bjetness,"Jet1_daughter1_bjetness/D");     
                                   //
Fullmassspectrum->Branch("cteta",&cteta,"cteta/D");                                 // addition of cos teta* just for the lulz
Fullmassspectrum->Branch("Ht",&Ht,"Ht/D");                                          //
Fullmassspectrum->Branch("Jet1pt",&Jet1pt,"Jet1pt/D");                              // addition of Ht: sum of the pt 
Fullmassspectrum->Branch("Jet2pt",&Jet2pt,"Jet2pt/D");                              // 
Fullmassspectrum->Branch("Jet1eta",&Jet1eta,"Jet1eta/D");                           // addition of dphi = delta phi and met = MET / sum Et
Fullmassspectrum->Branch("Jet2eta",&Jet2eta,"Jet2eta/D");                           // 
Fullmassspectrum->Branch("Jet1phi",&Jet1phi,"Jet1phi/D");                           //
Fullmassspectrum->Branch("Jet2phi",&Jet2phi,"Jet2phi/D");                           // 
Fullmassspectrum->Branch("dphi",&dphi,"dphi/D");                                    //
Fullmassspectrum->Branch("met",&met,"met/D");   









TTree *Threejet_analysis_CA8 = new TTree("Threejet_analysis_CA8", "Threejet_analysis_CA8");
Threejet_analysis_CA8->Branch("dEta_Fat_NonFat_pruned", &dEta_Fat_NonFat_pruned, "dEta_Fat_NonFat_pruned/D");
Threejet_analysis_CA8->Branch("dEta_Fat_NonFat", &dEta_Fat_NonFat, "dEta_Fat_NonFat/D");
Threejet_analysis_CA8->Branch("dEta_Fat_CA8RecH_bjetness", &dEta_Fat_CA8RecH_bjetness, "dEta_Fat_CA8RecH_bjetness/D");
Threejet_analysis_CA8->Branch("dEta_Fat_CA8RecH_pruned_bjetness", &dEta_Fat_CA8RecH_pruned_bjetness, "dEta_Fat_CA8RecH_pruned_bjetness/D");
Threejet_analysis_CA8->Branch("dEta_Fat_CA8RecH_pruned_HighestPt", &dEta_Fat_CA8RecH_pruned_HighestPt, "dEta_Fat_CA8RecH_pruned_HighestPt/D");
Threejet_analysis_CA8->Branch("dEta_Fat_CA8RecH_HighestPt", &dEta_Fat_CA8RecH_HighestPt, "dEta_Fat_CA8RecH_HighestPt/D");
Threejet_analysis_CA8->Branch("JetFat_daughter1_bjetness", &JetFat_daughter1_bjetness, "JetFat_daughter1_bjetness/D");
Threejet_analysis_CA8->Branch("JetFat_daughter0_bjetness", &JetFat_daughter0_bjetness, "JetFat_daughter0_bjetness/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_bjetness", &Jet_NonFat_bjetness, "Jet_NonFat_bjetness/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_bjetness", &Jet_SecondNonFat_bjetness, "Jet_SecondNonFat_bjetness/D");
Threejet_analysis_CA8->Branch("JetFatsub", &JetFatsub, "JetFatsub/D");
Threejet_analysis_CA8->Branch("dEta_Fat_CA8RecH_pruned_HighestPt", &dEta_Fat_CA8RecH_pruned_HighestPt, "dEta_Fat_CA8RecH_pruned_HighestPt/D");

Threejet_analysis_CA8->Branch("JetFatCA8_prunedmass", &JetFatCA8_prunedmass, "JetFatCA8_prunedmass/D");
Threejet_analysis_CA8->Branch("Jet_NonFatCA8_pruned_mass", &Jet_NonFatCA8_pruned_mass, "Jet_NonFatCA8_pruned_mass/D");

Threejet_analysis_CA8->Branch("Resonancemass_HighestPt_pruned", &Resonancemass_HighestPt_pruned, "Resonancemass_HighestPt_pruned/D");
Threejet_analysis_CA8->Branch("Resonancemass_HighestPt", &Resonancemass_HighestPt, "Resonancemass_HighestPt/D");
Threejet_analysis_CA8->Branch("Resonancemass_bjetness_pruned", &Resonancemass_bjetness_pruned, "Resonancemass_bjetness_pruned/D");
Threejet_analysis_CA8->Branch("Resonancemass_bjetness", &Resonancemass_bjetness, "Resonancemass_bjetness/D");

Threejet_analysis_CA8->Branch("Jet_NonFat_pruned_bjetness", &Jet_NonFat_pruned_bjetness, "Jet_NonFat_pruned_bjetness/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_pruned_pt", &Jet_NonFat_pruned_pt, "Jet_NonFat_pruned_pt/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_pruned_eta", &Jet_NonFat_pruned_eta, "Jet_NonFat_pruned_eta/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_pruned_phi", &Jet_NonFat_pruned_phi, "Jet_NonFat_pruned_phi/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_HighestPt_pruned_pt", &Jet_SecondNonFat_HighestPt_pruned_pt, "Jet_SecondNonFat_HighestPt_pruned_pt/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_HighestPt_pruned_eta", &Jet_SecondNonFat_HighestPt_pruned_eta, "Jet_SecondNonFat_HighestPt_pruned_eta/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_HighestPt_pruned_phi", &Jet_SecondNonFat_HighestPt_pruned_phi, "Jet_SecondNonFat_HighestPt_pruned_phi/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_bjetness_pruned_pt", &Jet_SecondNonFat_bjetness_pruned_pt, "Jet_SecondNonFat_bjetness_pruned_pt/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_bjetness_pruned_eta", &Jet_SecondNonFat_bjetness_pruned_eta, "Jet_SecondNonFat_bjetness_pruned_eta/D");
Threejet_analysis_CA8->Branch("Jet_SecondNonFat_bjetness_pruned_phi", &Jet_SecondNonFat_bjetness_pruned_phi, "Jet_SecondNonFat_bjetness_pruned_phi/D");



Threejet_analysis_CA8->Branch("Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt", &Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt, "Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt", &Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt, "Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness", &Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness, "Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness/D");
Threejet_analysis_CA8->Branch("Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness", &Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness, "Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness/D");


Threejet_analysis_CA8->Branch("deltaRFatNonFat", &deltaRFatNonFat, "deltaRFatNonFat/D");
Threejet_analysis_CA8->Branch("deltaR_NonFat_SecondNonFat_bjetness", &deltaR_NonFat_SecondNonFat_bjetness, "deltaR_NonFat_SecondNonFat_bjetness/D");
Threejet_analysis_CA8->Branch("deltaR_NonFat_SecondNonFat_HighestPt", &deltaR_NonFat_SecondNonFat_HighestPt, "deltaR_NonFat_SecondNonFatVar_HighestPt/D");


TTree *Threejet_analysis_AK5 = new TTree("Threejet_analysis_AK5", "Threejet_analysis_AK5");
Threejet_analysis_AK5->Branch("JetFatsub", &JetFatsub, "JetFatsub/D");
Threejet_analysis_AK5->Branch("JetFateta", &JetFateta, "JetFateta/D");
Threejet_analysis_AK5->Branch("JetFatphi", &JetFatphi, "JetFatphi/D");
Threejet_analysis_AK5->Branch("JetFat_daughter1_bjetness", &JetFat_daughter1_bjetness, "JetFat_daughter1_bjetness/D");
Threejet_analysis_AK5->Branch("JetFat_daughter0_bjetness", &JetFat_daughter0_bjetness, "JetFat_daughter0_bjetness/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_bjetness", &Jet_NonFatVar_bjetness, "Jet_NonFatVar_bjetness/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_bjetness", &Jet_SecondNonFatVar_bjetness, "Jet_SecondNonFatVar_bjetness/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_pruned_bjetness", &Jet_SecondNonFatVar_pruned_bjetness, "Jet_SecondNonFatVar_pruned_bjetness/D");

Threejet_analysis_AK5->Branch("JetFatCA8_prunedmass", &JetFatCA8_prunedmass, "JetFatCA8_prunedmass/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_mass", &Jet_NonFatVar_mass, "Jet_NonFatVar_mass/D");

Threejet_analysis_AK5->Branch("Resonancemass_AK5_bjetness", &Resonancemass_AK5_bjetness, "Resonancemass_AK5_bjetness/D");
Threejet_analysis_AK5->Branch("Resonancemass_AK5_HighestPt", &Resonancemass_AK5_HighestPt, "Resonancemass_AK5_HighestPt/D");
Threejet_analysis_AK5->Branch("Resonancemass_AK5_pruned_bjetness", &Resonancemass_AK5_pruned_bjetness, "Resonancemass_AK5_pruned_bjetness/D");
Threejet_analysis_AK5->Branch("Resonancemass_AK5_pruned_HighestPt", &Resonancemass_AK5_pruned_HighestPt, "Resonancemass_AK5_pruned_HighestPt/D");

Threejet_analysis_AK5->Branch("Jet_NonFatVar_eta", &Jet_NonFatVar_eta, "Jet_NonFatVar_eta/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_phi", &Jet_NonFatVar_phi, "Jet_NonFatVar_phi/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_pt", &Jet_NonFatVar_pt, "Jet_NonFatVar_pt/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_pruned_pt;", &Jet_NonFatVar_pruned_pt, "Jet_NonFatVar_pruned_pt/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_pruned_eta;", &Jet_NonFatVar_pruned_eta, "Jet_NonFatVar_pruned_eta/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_pruned_phi;", &Jet_NonFatVar_pruned_phi, "Jet_NonFatVar_pruned_phi/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_bjetness_pruned_eta;", &Jet_SecondNonFatVar_bjetness_pruned_eta, "Jet_SecondNonFatVar_bjetness_pruned_eta/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_bjetness_pruned_phi;", &Jet_SecondNonFatVar_bjetness_pruned_phi, "Jet_SecondNonFatVar_bjetness_pruned_phi/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_HighestPt_pruned_eta;", &Jet_SecondNonFatVar_HighestPt_pruned_eta, "Jet_SecondNonFatVar_HighestPt_pruned_eta/D");
Threejet_analysis_AK5->Branch("Jet_SecondNonFatVar_HighestPt_pruned_phi;", &Jet_SecondNonFatVar_HighestPt_pruned_phi, "Jet_SecondNonFatVar_HighestPt_pruned_phi/D");

Threejet_analysis_AK5->Branch("dEta_Fat_AK5RecH_bjetness", &dEta_Fat_AK5RecH_bjetness, "dEta_Fat_AK5RecH_bjetness/D");
Threejet_analysis_AK5->Branch("dEta_Fat_AK5RecH_pruned_bjetness", &dEta_Fat_AK5RecH_pruned_bjetness, "dEta_Fat_AK5RecH_pruned_bjetness/D");
Threejet_analysis_AK5->Branch("dEta_Fat_AK5RecH_HighestPt", &dEta_Fat_AK5RecH_HighestPt, "dEta_Fat_AK5RecH_HighestPt/D");
Threejet_analysis_AK5->Branch("dEta_Fat_AK5RecH_pruned_HighestPt", &dEta_Fat_AK5RecH_pruned_HighestPt, "dEta_Fat_AK5RecH_pruned_HighestPt/D");
Threejet_analysis_AK5->Branch("dEta_NonFatVar_SecondNonFatVar_pruned", &dEta_NonFatVar_SecondNonFatVar_pruned, "dEta_NonFatVar_SecondNonFatVar_pruned/D");
Threejet_analysis_AK5->Branch("dEta_Fat_NonFatVar_pruned", &dEta_Fat_NonFatVar_pruned, "dEta_Fat_NonFatVar_pruned/D");
Threejet_analysis_AK5->Branch("dEta_Fat_SecondNonFatVar_pruned", &dEta_Fat_SecondNonFatVar_pruned, "dEta_Fat_SecondNonFatVar_pruned/D");
Threejet_analysis_AK5->Branch("deltaR_Fat_NonFatVar", &deltaR_Fat_NonFatVar, "deltaR_Fat_NonFatVar/D");
Threejet_analysis_AK5->Branch("deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt", &deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt, "deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt/D");
Threejet_analysis_AK5->Branch("deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness", &deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness, "deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness/D");
Threejet_analysis_AK5->Branch("deltaR_SecondNonFatVar_pruned_bjetness_SecondNonFatVar_pruned_HighestPt", &deltaR_SecondNonFatVar_pruned_bjetness_SecondNonFatVar_pruned_HighestPt, "deltaR_SecondNonFatVar_pruned_bjetness_SecondNonFatVar_pruned_HighestPt/D");

Threejet_analysis_AK5->Branch("deltaR_NonFatVar_SecondNonFatVar_bjetness", &deltaR_NonFatVar_SecondNonFatVar_bjetness, "deltaR_NonFatVar_SecondNonFatVar_bjetness/D");
Threejet_analysis_AK5->Branch("deltaR_NonFatVar_SecondNonFatVar_HighestPt", &deltaR_NonFatVar_SecondNonFatVar_HighestPt, "deltaR_NonFatVar_SecondNonFatVar_HighestPt/D");



Threejet_analysis_AK5->Branch("Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness", &Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness, "Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt", &Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt, "Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness", &Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness, "Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness/D");
Threejet_analysis_AK5->Branch("Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt", &Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt, "Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt/D");

  TTree *dijetWtag = new TTree("dijetWtag", "dijetWtag");                      // creates the dijetWtag tree (ranked, mgg>890) and its branches
  //dijetWtag->Branch("DijetMass",&DijetMass,"DijetMass/D");
  //dijetWtag->Branch("DijetMassNoCHS",&DijetMassNoCHS,"DijetMassNoCHS/D");
  dijetWtag->Branch("DijetMassCA8",&DijetMassCA8,"DijetMassCA8/D");
  //dijetWtag->Branch("DijetMassAK7",&DijetMassAK7,"DijetMassAK7/D");
  dijetWtag->Branch("deta",&deta,"deta/D");   
  dijetWtag->Branch("Jet0_daughter0_bjetness",&Jet0_daughter0_bjetness,"Jet0_daughter0_bjetness/D");   
  dijetWtag->Branch("Jet0_daughter1_bjetness",&Jet0_daughter1_bjetness,"Jet0_daughter1_bjetness/D");   		
  dijetWtag->Branch("Jet1_daughter0_bjetness",&Jet1_daughter0_bjetness,"Jet1_daughter0_bjetness/D");     
  dijetWtag->Branch("Jet1_daughter1_bjetness",&Jet1_daughter1_bjetness,"Jet1_daughter1_bjetness/D");     
                                   //
  dijetWtag->Branch("cteta",&cteta,"cteta/D");                                 // addition of cos teta* just for the lulz
  dijetWtag->Branch("Ht",&Ht,"Ht/D");                                          //
  dijetWtag->Branch("Jet1pt",&Jet1pt,"Jet1pt/D");                              // addition of Ht: sum of the pt 
  dijetWtag->Branch("Jet2pt",&Jet2pt,"Jet2pt/D");                              // 
  dijetWtag->Branch("Jet1eta",&Jet1eta,"Jet1eta/D");                           // addition of dphi = delta phi and met = MET / sum Et
  dijetWtag->Branch("Jet2eta",&Jet2eta,"Jet2eta/D");                           // 
  dijetWtag->Branch("Jet1phi",&Jet1phi,"Jet1phi/D");                           //
  dijetWtag->Branch("Jet2phi",&Jet2phi,"Jet2phi/D");                           // 
  dijetWtag->Branch("dphi",&dphi,"dphi/D");                                    //
  dijetWtag->Branch("met",&met,"met/D");                                       // 
  dijetWtag->Branch("Jet1CA8_prunedmass",&Jet1CA8_prunedmass,"Jet1CA8_prunedmass/D");               // MassDrop: the mass of the biggest subjet divided by the mass of the jet
  dijetWtag->Branch("Jet2CA8_prunedmass",&Jet2CA8_prunedmass,"Jet2CA8_prunedmass/D");
  dijetWtag->Branch("Jet1CA8MassDrop",&Jet1CA8MassDrop,"Jet1CA8MassDrop/D");   // 
  dijetWtag->Branch("Jet2CA8MassDrop",&Jet2CA8MassDrop,"Jet2CA8MassDrop/D");   // Nsub measures the proximity of the jet to a color monopole with regard
  dijetWtag->Branch("Jet1CA8Nsub",&Jet1CA8Nsub,"Jet1CA8Nsub/D");               // to a color dipole 
  dijetWtag->Branch("Jet2CA8Nsub",&Jet2CA8Nsub,"Jet2CA8Nsub/D");               // the smaller Nsub, the purer the jet, ie the closest to a dipole
  dijetWtag->Branch("Jet1dr",&Jet1dr,"Jet1dr/D");                              //
  dijetWtag->Branch("Jet2dr",&Jet2dr,"Jet2dr/D");                              // addition of dr: distance between the 2 subjets in each jet
  dijetWtag->Branch("nbvert",&nbvert,"nbvert/I");                              //
  dijetWtag->Branch("Jet1mef",&Jet1mef,"Jet1mef/D");                           // addition of nbvert: number of primary vertices                         
  dijetWtag->Branch("Jet1nhef",&Jet1nhef,"Jet1nhef/D");                        //                                                     
  dijetWtag->Branch("Jet1neef",&Jet1neef,"Jet1neef/D");                        // addition of mef: muon energy fraction     
  dijetWtag->Branch("Jet1nbcons",&Jet1nbcons,"Jet1nbcons/I");                  //      
  dijetWtag->Branch("Jet1chef",&Jet1chef,"Jet1chef/D");                        // addition of nhef: neutral hadron energy fraction       
  dijetWtag->Branch("Jet1ceef",&Jet1ceef,"Jet1ceef/D");                        // 
  dijetWtag->Branch("Jet1cmult",&Jet1cmult,"Jet1cmult/D");                     // addition of neef: neutral EM  energy fraction  
  dijetWtag->Branch("Jet2mef",&Jet2mef,"Jet2mef/D");                           //                                                 
  dijetWtag->Branch("Jet2nhef",&Jet2nhef,"Jet2nhef/D");                        // addition of nhef: neutral hadron energy fraction  
  dijetWtag->Branch("Jet2neef",&Jet2neef,"Jet2neef/D");                        //      
  dijetWtag->Branch("Jet2nbcons",&Jet2nbcons,"Jet2nbcons/I");                  // addition of nbcons: number of constituants     
  dijetWtag->Branch("Jet2chef",&Jet2chef,"Jet2chef/D");                        //      
  dijetWtag->Branch("Jet2ceef",&Jet2ceef,"Jet2ceef/D");                        // addition of chef: charged hadron energy fraction
  dijetWtag->Branch("Jet2cmult",&Jet2cmult,"Jet2cmult/D");                     // 
  dijetWtag->Branch("fat",&fat,"fat/I");                                       // addition of ceef: charged EM energy fraction
  dijetWtag->Branch("ht550",&ht550,"ht550/I");                                 // 
  dijetWtag->Branch("ht650",&ht650,"ht650/I");                                 // addition of cmult: charged multiplicity
  dijetWtag->Branch("pfht650",&pfht650,"pfht650/I");                           // 
  dijetWtag->Branch("weight",&weight,"weight/D");                              // addition of the trigger booleans FAT, HT550, HT650 & PFHT650
  dijetWtag->Branch("categories",&categories,"categories/I");                  // 
                                                                                







  //---------------------------------------------------------------------------
  // Loop over events
  //---------------------------------------------------------------------------

  bool hcallasereventfilter2012active=false;
  bool datafiltersactive=false;
	  
  for(int entry=0; entry < nevents; ++entry)
	{
	  // Read event into memory
	  stream.read(entry);
	
	if(!(entry%1000))
	{
	cout << entry << "/" << nevents << endl;
	}
	
	
	
	  // Uncomment the following line if you wish to copy variables into
	  // structs. See the header file analyzer.h to find out what structs
	  // are available. Each struct contains the field "selected", which
	  // can be set as needed. Call saveSelectedObjects() before a call to
	  // addEvent if you wish to save only the selected objects.
	  
	  // fillObjects();
	  
	  // ---------------------
	  // -- event selection --
	  // ---------------------

	  if(!((jethelperCA8_pt.size()>=2)))                     // if you have less than 2 jets (CA), get out
	      continue;

          njets=0;                                               // counts the jets with a pt above 100
	  for(unsigned n=0;n<jethelper_pt.size();n++)            // 
	    if(jethelper_pt[n]>30)                              // what for? It's never used afterward
	         njets++;                                        
          njetsCA8=0;
	  for(unsigned n=0;n<jethelperCA8_pt.size();n++)         // 
	     if(jethelperCA8_pt[n]>30)                          // ditto with CA
	         njetsCA8++;                                     // 
          

          TLorentzVector Jet1;
          TLorentzVector Jet2;


	  Jet1.SetPtEtaPhiE(jethelper_pt[0],jethelper_eta[0],jethelper_phi[0],jethelper_energy[0]);                           //
	  Jet2.SetPtEtaPhiE(jethelper_pt[1],jethelper_eta[1],jethelper_phi[1],jethelper_energy[1]);                           // useless because no CA?
          DijetMass = (Jet1+Jet2).M();                                                                                        //

	  Jet1.SetPtEtaPhiE(jethelperNoCHS_pt[0],jethelperNoCHS_eta[0],jethelperNoCHS_phi[0],jethelperNoCHS_energy[0]);       //
	  Jet2.SetPtEtaPhiE(jethelperNoCHS_pt[1],jethelperNoCHS_eta[1],jethelperNoCHS_phi[1],jethelperNoCHS_energy[1]);       // useless because noCHS?
          DijetMassNoCHS = (Jet1+Jet2).M();                                                                                   //

                                                                                                                      


	  // ------------------ Dijet Mass to be used -----------------

	  Jet1.SetPtEtaPhiE(jethelperCA8_pt[0],jethelperCA8_eta[0],jethelperCA8_phi[0],jethelperCA8_energy[0]);
	  Jet2.SetPtEtaPhiE(jethelperCA8_pt[1],jethelperCA8_eta[1],jethelperCA8_phi[1],jethelperCA8_energy[1]);
          DijetMassCA8 = (Jet1+Jet2).M();

          deta = fabs(jethelperCA8_eta[0]-jethelperCA8_eta[1]);  //
          cteta = tanh(deta/2);                                  //
	  Ht=0;                                                  // 
	  for(unsigned n=0;n<jethelper_pt.size();n++)           
	    Ht = Ht +jethelper_pt[n];
          Jet1pt = jethelperCA8_pt[0];                           //
          Jet2pt = jethelperCA8_pt[1];                           // computes the jets  
          Jet1eta = jethelperCA8_eta[0];                         // dynamics variables
          Jet2eta = jethelperCA8_eta[1];                         //
          Jet1phi = jethelperCA8_phi[0];                         //
          Jet2phi = jethelperCA8_phi[1];                         //

	  if (Jet1phi>Jet2phi)                                   //                                                   
	    dphi = Jet1phi - Jet2phi - pi;                       //                                                    
	  if (Jet1phi<Jet2phi)                                   //                                                   
	    dphi = Jet2phi - Jet1phi-pi;                         //                                                  
	  met = (met2_et/met2_sumEt);
	  dphi1 = jethelperCA8pruned_daughter_0_phi[0]-jethelperCA8pruned_daughter_1_phi[0];
	  if (dphi1 < -pi)
	    dphi1 = dphi1 + (2*pi);
	  if (dphi1 > pi)
	    dphi1 = dphi1 - (2*pi);
	  dphi2 = jethelperCA8pruned_daughter_0_phi[1]-jethelperCA8pruned_daughter_1_phi[1];
	  if (dphi2 < -pi)
	    dphi2 = dphi2 + (2*pi);
	  if (dphi2 > pi)
	    dphi2 = dphi2 - (2*pi);

	  Jet1dr = sqrt(((jethelperCA8pruned_daughter_0_eta[0]-jethelperCA8pruned_daughter_1_eta[0])*(jethelperCA8pruned_daughter_0_eta[0]-jethelperCA8pruned_daughter_1_eta[0])) + ((dphi1)*(dphi1)));
	  Jet2dr = sqrt(((jethelperCA8pruned_daughter_0_eta[1]-jethelperCA8pruned_daughter_1_eta[1])*(jethelperCA8pruned_daughter_0_eta[1]-jethelperCA8pruned_daughter_1_eta[1])) + ((dphi2)*(dphi2)));

          

	  Jet1CA8_prunedmass = jethelperCA8pruned_mass[0];              // computes the jets mass and massdrop
          Jet2CA8_prunedmass = jethelperCA8pruned_mass[1];              //

          Jet1CA8MassDrop = max(jethelperCA8pruned_daughter_0_mass[0],jethelperCA8pruned_daughter_1_mass[0])/Jet1CA8_prunedmass/jethelperCA8pruned_uncor_pt[0]*jethelperCA8pruned_pt[0];                                           //
          Jet2CA8MassDrop = max(jethelperCA8pruned_daughter_0_mass[1],jethelperCA8pruned_daughter_1_mass[1])/Jet2CA8_prunedmass/jethelperCA8pruned_uncor_pt[1]*jethelperCA8pruned_pt[1];                                           //

	  if ((jethelperCA8pruned_daughter_0_mass[0]<0.0001)||(jethelperCA8pruned_daughter_1_mass[0]<0.0001)) Jet1CA8MassDrop = 2;  // eliminates the bad
	  if ((jethelperCA8pruned_daughter_0_mass[1]<0.0001)||(jethelperCA8pruned_daughter_1_mass[1]<0.0001)) Jet2CA8MassDrop = 2;  // clustering cases

          Jet1CA8Nsub = jethelperCA8_tau2[0]/jethelperCA8_tau1[0];   // computes the purity
          Jet2CA8Nsub = jethelperCA8_tau2[1]/jethelperCA8_tau1[1];   // variable  Nsub

	  nbvert=eventhelperextra_numberOfPrimaryVertices;

	  Jet1mef = jethelperCA8_muonEnergyFraction[0];
	  Jet1nhef = jethelperCA8_neutralHadronEnergyFraction[0];
	  Jet1neef = jethelperCA8_neutralEmEnergyFraction[0];
	  Jet1nbcons = jethelperCA8_nConstituents[0];
	  Jet1chef = jethelperCA8_chargedHadronEnergyFraction[0];
	  Jet1cmult = jethelperCA8_chargedMultiplicity[0];
	  Jet1ceef = jethelperCA8_chargedEmEnergyFraction[0];
	  Jet2mef = jethelperCA8_muonEnergyFraction[1];
	  Jet2nhef = jethelperCA8_neutralHadronEnergyFraction[1];
	  Jet2neef = jethelperCA8_neutralEmEnergyFraction[1];
	  Jet2nbcons = jethelperCA8_nConstituents[1];
	  Jet2chef = jethelperCA8_chargedHadronEnergyFraction[1];
	  Jet2cmult = jethelperCA8_chargedMultiplicity[1];
	  Jet2ceef = jethelperCA8_chargedEmEnergyFraction[1];
	  
	  if ((triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11==1) or (triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12==1))
	    fat=1;
	  else
	    fat=0;
	    
	  if ((triggerresultshelper_HLT_HT550_v1==1) || (triggerresultshelper_HLT_HT550_v2==1) || (triggerresultshelper_HLT_HT550_v3==1) || (triggerresultshelper_HLT_HT550_v4==1) || (triggerresultshelper_HLT_HT550_v5==1) || (triggerresultshelper_HLT_HT550_v6==1) || (triggerresultshelper_HLT_HT550_v7==1) || (triggerresultshelper_HLT_HT550_v8==1) || (triggerresultshelper_HLT_HT550_v9==1))
	    ht550=1;
	  else
	    ht550=0;

	  if ((triggerresultshelper_HLT_HT650_v1==1) or (triggerresultshelper_HLT_HT650_v2==1) or (triggerresultshelper_HLT_HT650_v3==1) or (triggerresultshelper_HLT_HT650_v4==1) or (triggerresultshelper_HLT_HT650_v5==1) or (triggerresultshelper_HLT_HT650_v6==1) or (triggerresultshelper_HLT_HT650_v7==1) or (triggerresultshelper_HLT_HT650_v8==1) or (triggerresultshelper_HLT_HT650_v9==1))
	    ht650=1;
	  else
	    ht650=0;

	  if ((triggerresultshelper_HLT_PFHT650_v1==1) or (triggerresultshelper_HLT_PFHT650_v2==1) or (triggerresultshelper_HLT_PFHT650_v3==1) or (triggerresultshelper_HLT_PFHT650_v4==1) or (triggerresultshelper_HLT_PFHT650_v5==1) or (triggerresultshelper_HLT_PFHT650_v6==1) or (triggerresultshelper_HLT_PFHT650_v7==1) or (triggerresultshelper_HLT_PFHT650_v8==1) or (triggerresultshelper_HLT_PFHT650_v9==1) or (triggerresultshelper_HLT_PFHT650_v10==1) or (triggerresultshelper_HLT_PFHT650_v11==1))
	    pfht650=1;
	  else
	    pfht650=0;
	  
	  Jet1CA8C2beta17 = jethelperCA8_C2beta17[0];                // honestly I don't care, they're
          Jet2CA8C2beta17 = jethelperCA8_C2beta17[1];                // never used afterward
 
           
          if (triggerresultshelper_hcallasereventfilter2012!=0)                       //
	    hcallasereventfilter2012active=true;                                      //
                                                                                      //
	  if((triggerresultshelper_primaryVertexFilterPath!=0)&&                      //
	     (triggerresultshelper_noscrapingFilterPath!=0)&&                         //  eliminates the
	     (triggerresultshelper_trackingFailureFilterPath!=0)&&                    //  detector noise
	     (triggerresultshelper_hcalLaserEventFilterPath!=0)&&                     //
	     (triggerresultshelper_HBHENoiseFilterPath!=0)&&                          //
	     (triggerresultshelper_CSCTightHaloFilterPath!=0)&&                       //
	     (triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath!=0))        //
	    datafiltersactive=true;                                                   //

          //if(DijetMass>1600)
          //    cout << "every " << eventhelper_run << ":" << eventhelper_luminosityBlock << ":" << eventhelper_event << endl;

	  bool Jet1_Kinematic_Selection = (Jet1pt>30) && (fabs(Jet1eta)<2.5);                       // jets with pt<30 are not 
	  bool Jet2_Kinematic_Selection = (Jet2pt>30) && (fabs(Jet2eta)<2.5);                       //
                                                                                                    // measurable anyway
	  bool Jets_Kinematic_Selection = Jet1_Kinematic_Selection && Jet2_Kinematic_Selection;     //

	  bool Jet1_Tight_Id =   (jethelperCA8_muonEnergyFraction[0]<0.80)&&        //
	    (jethelperCA8_neutralHadronEnergyFraction[0]<0.90)&&                    //
	    (jethelperCA8_neutralEmEnergyFraction[0]<0.90)&&                        //
	    (jethelperCA8_nConstituents[0]>1)&&                                     //
	    ((fabs(jethelper_eta[0])>2.4)||                                         //
	     ((jethelperCA8_chargedHadronEnergyFraction[0]>0.01)&&                  //
	      (jethelperCA8_chargedMultiplicity[0]>0)&&                             //
	      (jethelperCA8_chargedEmEnergyFraction[0]<0.99)));                     //
                                                                                    // 
	  bool Jet2_Tight_Id  = (jethelperCA8_muonEnergyFraction[1]<0.80)&&         // background
	     (jethelperCA8_neutralHadronEnergyFraction[1]<0.90)&&                   // filtering?
	     (jethelperCA8_neutralEmEnergyFraction[1]<0.90)&&                       //
	     (jethelperCA8_nConstituents[1]>1)&&                                    //
	     ((fabs(jethelperCA8_eta[1])>2.4)||                                     //
	      ((jethelperCA8_chargedHadronEnergyFraction[1]>0.01)&&                 //
	       (jethelperCA8_chargedMultiplicity[1]>0)&&                            //
	       (jethelperCA8_chargedEmEnergyFraction[1]<0.99)));                    //
	                                                                            //
	  bool Jets_Id_Selection =  Jet1_Tight_Id && Jet2_Tight_Id;                 //


	  bool Jets_Selection = Jets_Kinematic_Selection && Jets_Id_Selection;

	  bool noiseRemoval = (((sdouble_kt6PFJets_rho_value<40)&&                                             //
	       (triggerresultshelper_primaryVertexFilterPath!=0)&&                                             //
	       (triggerresultshelper_noscrapingFilterPath!=0)&&                                                //
	       (triggerresultshelper_trackingFailureFilterPath!=0)&&                                           //
	       (triggerresultshelper_hcalLaserEventFilterPath!=0)&&                                            // eliminates the
	       (triggerresultshelper_HBHENoiseFilterPath!=0)&&                                                 // detector noise
	       (triggerresultshelper_CSCTightHaloFilterPath!=0)&&                                              //
	       (triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath!=0))||                             //
	      (datafiltersactive==false))&&                                                                    //
	    ((triggerresultshelper_hcallasereventfilter2012!=0)||(hcallasereventfilter2012active==false));     //


	  bool centralitySelection = deta<1.3;                 // centrality condition

	  if(!(noiseRemoval && Jets_Selection)) continue;

	Jet0_daughter0_bjetness = jethelperCA8pruned_daughter_0_combinedSecondaryVertexBJetTags[0];
	Jet0_daughter1_bjetness = jethelperCA8pruned_daughter_1_combinedSecondaryVertexBJetTags[0];
	Jet1_daughter0_bjetness = jethelperCA8pruned_daughter_0_combinedSecondaryVertexBJetTags[1];
	Jet1_daughter1_bjetness = jethelperCA8pruned_daughter_1_combinedSecondaryVertexBJetTags[1];
	
	Jet0daughter0_pt = jethelperCA8pruned_daughter_0_pt[0];
	Jet0daughter1_pt = jethelperCA8pruned_daughter_1_pt[0];
	Jet1daughter0_pt = jethelperCA8pruned_daughter_0_pt[1];
	Jet1daughter1_pt = jethelperCA8pruned_daughter_1_pt[1];

	Jet0daughter0_eta = jethelperCA8pruned_daughter_0_eta[0];
	Jet0daughter1_eta = jethelperCA8pruned_daughter_1_eta[0];
	Jet1daughter0_eta = jethelperCA8pruned_daughter_0_eta[1];
	Jet1daughter1_eta = jethelperCA8pruned_daughter_1_eta[1];


	Fullmassspectrum->Fill();
// ********************************************************************************************************
//			
//		FAT JET + NON-MERGED JET TOPOLOGY ANALYSIS STARTS HERE
//		
//	Consists of:
//	Part 1) analysis by taking events with EXACTLY 1 fat jet in higgs window, then
//		1.A taking highest pt AK5jet away from fat jet. Then recombine dijet mass of:
//			- AK5jet + highest pt in dr~1.3 cone
//			- AK5jet + highest bjetness in dr~1.3 cone
//		1.B taking highest pt jet (except fat) and plot NonFat parameters
//
//
// ********************************************************************************************************


	// look for how many fat jets * 
	nNrMoreJetsEvents = njetsCA8;
	NrJetsInHiggsWindow = 0;
	WhichJetInHiggsWindow = -1;
	FattieNumber = -1;
	for(int zz=0;zz<njetsCA8;zz++) 
	{
		TLorentzVector JetY;
    		JetY.SetPtEtaPhiE(jethelperCA8_pt[zz],jethelperCA8_eta[zz],jethelperCA8_phi[zz],jethelperCA8_energy[zz]);
        	JetYCA8_prunedmass = jethelperCA8pruned_mass[zz];
		JetYCA8Nsub = jethelperCA8_tau2[zz]/jethelperCA8_tau1[zz];  
		if((JetYCA8_prunedmass>110)&&(JetYCA8_prunedmass<135)) 
		{
			NrJetsInHiggsWindow++; // counting fat jets
			WhichJetInHiggsWindow = zz; // and saving the index nr of that jet
		}
	}


	 // from here on only using 1-fat events  
		 // having a special look at 2-jet events with 1 fat  

	if((NrJetsInHiggsWindow==1) && (njetsCA8 > 1)) // we're only using 1-fat events to completely exclude this work from simon's
	{
		FattieNumber = WhichJetInHiggsWindow; 
	
		// setting mass / variables of fat jet * 
		TLorentzVector JetFat; 			
		JetFat.SetPtEtaPhiE(jethelperCA8_pt[FattieNumber],jethelperCA8_eta[FattieNumber],jethelperCA8_phi[FattieNumber],jethelperCA8_energy[FattieNumber]); 						
		TLorentzVector JetFat_pruned; 		
		JetFat_pruned.SetPtEtaPhiE(jethelperCA8pruned_pt[FattieNumber],jethelperCA8pruned_eta[FattieNumber],jethelperCA8pruned_phi[FattieNumber],jethelperCA8pruned_energy[FattieNumber]);
		JetFatCA8_prunedmass = jethelperCA8pruned_mass[FattieNumber];
		JetFateta = jethelperCA8_eta[FattieNumber];
		JetFatphi = jethelperCA8_phi[FattieNumber];
		JetFatsub = jethelperCA8_tau2[FattieNumber]/jethelperCA8_tau1[FattieNumber];


		JetFat_daughter0_bjetness = jethelperCA8pruned_daughter_0_combinedSecondaryVertexBJetTags[FattieNumber]; 
		JetFat_daughter1_bjetness = jethelperCA8pruned_daughter_1_combinedSecondaryVertexBJetTags[FattieNumber];

	
	
// ****************************************************
//			START OF PART 1.A  (AK5)
// ****************************************************

		 // Looking for highest pt jet AK5 away from fat jet  
		HighestNonFatVarPt = -1;			
		HighestNonFatVarPt_Number = -1;		
		deltaR_Fat_NonFatVar = -1;	
		Jet_NonFatVar_bjetness =-1;	
		Jet_NonFatVar_mass = 0;	
		Jet_NonFatVar_pruned_mass = 0;
		HighestNonFatVarPt_pruned=0;
		HighestNonFatVarPt_pruned_Number=-1;
		dEta_Fat_NonFatVar_pruned = -10;
		
		Jet_NonFatVar_eta = -10;
		Jet_NonFatVar_pruned_eta = -10;
		Jet_NonFatVar_pruned_phi = -10;
		Jet_NonFatVar_phi = -10;
		Jet_NonFatVar_pt = -10;
		Jet_NonFatVar_pruned_pt = -10;

		for(int aa=0;aa<njets;aa++) 		
		{	
			TLorentzVector Jet_NonFatVar_dummy;
			Jet_NonFatVar_dummy.SetPtEtaPhiE(cmgPFJet_cmgPFJetSelCHS_pt[aa],cmgPFJet_cmgPFJetSelCHS_eta[aa],cmgPFJet_cmgPFJetSelCHS_phi[aa],cmgPFJet_cmgPFJetSelCHS_energy[aa]);
			dphi_Fat_NonFatVar = deltaPhi(JetFatphi, cmgPFJet_cmgPFJetSelCHS_phi[aa]);
			
			TLorentzVector Jet_NonFatVar_pruned_dummy;
			Jet_NonFatVar_pruned_dummy.SetPtEtaPhiE(jethelperAK5_pt[aa],jethelperAK5_eta[aa],jethelperAK5_phi[aa],jethelperAK5_energy[aa]);
			dphi_Fat_NonFatVar_pruned = deltaPhi(JetFatphi, jethelperAK5_phi[aa]);
			
			if((dphi_Fat_NonFatVar > (float)pi/2) && (cmgPFJet_cmgPFJetSelCHS_pt[aa] > HighestNonFatVarPt)) //they need to be back-to-back-ish (dphi>pi/2)
			{
				HighestNonFatVarPt = cmgPFJet_cmgPFJetSelCHS_pt[aa];
				HighestNonFatVarPt_Number = aa;
				deltaR_Fat_NonFatVar = deltaR(JetFateta, cmgPFJet_cmgPFJetSelCHS_eta[aa], dphi_Fat_NonFatVar); // saving the values for highest pt
				Jet_NonFatVar_bjetness = cmgPFJet_cmgPFJetSelCHS_combinedSecondaryVertexBJetTags[HighestNonFatVarPt_Number];	
				Jet_NonFatVar_mass = cmgPFJet_cmgPFJetSelCHS_mass[HighestNonFatVarPt_Number];
				Jet_NonFatVar_eta = jethelperAK5_eta[HighestNonFatVarPt_Number];
				Jet_NonFatVar_phi = jethelperAK5_phi[HighestNonFatVarPt_Number];
				Jet_NonFatVar_pt = jethelperAK5_pt[HighestNonFatVarPt_Number];
			}
			if((dphi_Fat_NonFatVar_pruned > (float)pi/2) && (jethelperAK5_pt[aa] > HighestNonFatVarPt_pruned)) //they need to be back-to-back-ish (dphi>pi/2)
			{
				HighestNonFatVarPt_pruned = jethelperAK5_pt[aa];
				HighestNonFatVarPt_pruned_Number = aa;
				deltaR_Fat_NonFatVar_pruned = deltaR(JetFateta, jethelperAK5_eta[aa], dphi_Fat_NonFatVar_pruned); // saving the values for highest pt
				Jet_NonFatVar_pruned_bjetness = jethelperAK5_combinedSecondaryVertexBJetTags[HighestNonFatVarPt_pruned_Number];	
				Jet_NonFatVar_pruned_mass = jethelperAK5_mass[HighestNonFatVarPt_pruned_Number];
				dEta_Fat_NonFatVar_pruned = fabs(JetFateta - jethelperAK5_eta[HighestNonFatVarPt_pruned_Number]);
				Jet_NonFatVar_pruned_eta = jethelperAK5_eta[HighestNonFatVarPt_pruned_Number];
				Jet_NonFatVar_pruned_phi = jethelperAK5_phi[HighestNonFatVarPt_pruned_Number];
				Jet_NonFatVar_pruned_pt = jethelperAK5_pt[HighestNonFatVarPt_pruned_Number];				
			}
		}

		//index highest pt jet (nonfatvar) saved as HighestNonFatVarPt_Number
		//Looking for highest pt and b-jetness AK5 in dr<1.3 cone from nonfatvar
			//resetting parameters
		Jet_SecondNonFatVar_bjetness = -1;		
		Jet_SecondNonFatVar_bjetness_Number = -1;	
		Jet_SecondNonFatVar_HighestPt = -1;
		Jet_SecondNonFatVar_HighestPt_Number = -1;
		deltaR_NonFatVar_SecondNonFatVar_bjetness = -1;	
		deltaR_NonFatVar_SecondNonFatVar_HighestPt = -1;	
		

		Jet_SecondNonFatVar_bjetness_pruned_eta = -10;
		Jet_SecondNonFatVar_bjetness_pruned_phi = -10;

		Jet_SecondNonFatVar_HighestPt_pruned_eta = -10;
		Jet_SecondNonFatVar_HighestPt_pruned_phi = -10;
		
		Jet_SecondNonFatVar_pruned_bjetness = -1;		
		Jet_SecondNonFatVar_pruned_bjetness_Number = -1;	
		Jet_SecondNonFatVar_pruned_HighestPt = -1;
		Jet_SecondNonFatVar_pruned_HighestPt_Number = -1;
		deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness = -1;	
		deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt = -1;	
		dEta_Fat_SecondNonFatVar_pruned=-10;
		dEta_NonFatVar_SecondNonFatVar_pruned = -10;
		if(HighestNonFatVarPt_Number!=-1 && HighestNonFatVarPt_pruned_Number!=-1)
		{
			for(int bb=0;bb<njets;bb++) 			
			{	
			
				//check all jets in dr<1.3 cone (not itself though)
				if((bb!= HighestNonFatVarPt_Number)  && deltaR(cmgPFJet_cmgPFJetSelCHS_eta[bb], cmgPFJet_cmgPFJetSelCHS_eta[HighestNonFatVarPt_Number], deltaPhi(cmgPFJet_cmgPFJetSelCHS_phi[bb], cmgPFJet_cmgPFJetSelCHS_phi[HighestNonFatVarPt_Number])) < 1.3 )
				{
					//highest b-jetness
					if((cmgPFJet_cmgPFJetSelCHS_combinedSecondaryVertexBJetTags[bb] > Jet_SecondNonFatVar_bjetness) && (cmgPFJet_cmgPFJetSelCHS_combinedSecondaryVertexBJetTags[bb] >0))
					{			
						Jet_SecondNonFatVar_bjetness = cmgPFJet_cmgPFJetSelCHS_combinedSecondaryVertexBJetTags[bb];
						Jet_SecondNonFatVar_bjetness_Number = bb;
						deltaR_NonFatVar_SecondNonFatVar_bjetness = deltaR(cmgPFJet_cmgPFJetSelCHS_eta[HighestNonFatVarPt_Number], cmgPFJet_cmgPFJetSelCHS_eta[bb], deltaPhi(cmgPFJet_cmgPFJetSelCHS_phi[HighestNonFatVarPt_Number], cmgPFJet_cmgPFJetSelCHS_phi[bb]));
					}
					//saving  highest pt
					if((cmgPFJet_cmgPFJetSelCHS_pt[bb] > Jet_SecondNonFatVar_HighestPt) && (cmgPFJet_cmgPFJetSelCHS_pt[bb] >0))
					{
						Jet_SecondNonFatVar_HighestPt = cmgPFJet_cmgPFJetSelCHS_pt[bb];
						Jet_SecondNonFatVar_HighestPt_Number = bb;
						deltaR_NonFatVar_SecondNonFatVar_HighestPt = deltaR(cmgPFJet_cmgPFJetSelCHS_eta[HighestNonFatVarPt_Number], cmgPFJet_cmgPFJetSelCHS_eta[bb], deltaPhi(cmgPFJet_cmgPFJetSelCHS_phi[HighestNonFatVarPt_Number], cmgPFJet_cmgPFJetSelCHS_phi[bb]));
					}
				}
				
				//same check, but now for pruned: check all jets in dr<1.3 cone (not itself though)
				if((bb!= HighestNonFatVarPt_pruned_Number)  && deltaR(jethelperAK5_eta[bb], jethelperAK5_eta[HighestNonFatVarPt_pruned_Number], deltaPhi(jethelperAK5_phi[bb], jethelperAK5_phi[HighestNonFatVarPt_pruned_Number])) < 1.3 )
				{
					//highest b-jetness
					if((jethelperAK5_combinedSecondaryVertexBJetTags[bb] > Jet_SecondNonFatVar_pruned_bjetness) && (jethelperAK5_combinedSecondaryVertexBJetTags[bb] > 0))
					{			
						Jet_SecondNonFatVar_pruned_bjetness = jethelperAK5_combinedSecondaryVertexBJetTags[bb];
						Jet_SecondNonFatVar_pruned_bjetness_Number = bb;
						deltaR_NonFatVar_SecondNonFatVar_pruned_bjetness = deltaR(jethelperAK5_eta[HighestNonFatVarPt_pruned_Number], jethelperAK5_eta[bb], deltaPhi(jethelperAK5_phi[HighestNonFatVarPt_pruned_Number], jethelperAK5_phi[bb]));
					}
					//saving  highest pt
					if((jethelperAK5_pt[bb] > Jet_SecondNonFatVar_pruned_HighestPt) && (jethelperAK5_pt[bb] > 0 ))
					{
						Jet_SecondNonFatVar_pruned_HighestPt = jethelperAK5_pt[bb];
						Jet_SecondNonFatVar_pruned_HighestPt_Number = bb;
						deltaR_NonFatVar_SecondNonFatVar_pruned_HighestPt = deltaR(jethelperAK5_eta[HighestNonFatVarPt_pruned_Number], jethelperAK5_eta[bb], deltaPhi(jethelperAK5_phi[HighestNonFatVarPt_pruned_Number], jethelperAK5_phi[bb]));
						dEta_Fat_SecondNonFatVar_pruned = fabs(JetFateta-jethelperAK5_eta[bb]);
						dEta_NonFatVar_SecondNonFatVar_pruned = fabs(jethelperAK5_eta[bb] - jethelperAK5_eta[HighestNonFatVarPt_pruned_Number]);
					}
				}
				
			}
			//Setting the used jets
				//NonFatVar jet
			TLorentzVector Jet_NonFatVar; 
			Jet_NonFatVar.SetPtEtaPhiE(cmgPFJet_cmgPFJetSelCHS_pt[HighestNonFatVarPt_Number],cmgPFJet_cmgPFJetSelCHS_eta[HighestNonFatVarPt_Number],cmgPFJet_cmgPFJetSelCHS_phi[HighestNonFatVarPt_Number],cmgPFJet_cmgPFJetSelCHS_energy[HighestNonFatVarPt_Number]);// Setting Non Fat Var Jet
			TLorentzVector Jet_NonFatVar_pruned; 
			Jet_NonFatVar_pruned.SetPtEtaPhiE(jethelperAK5_pt[HighestNonFatVarPt_pruned_Number],jethelperAK5_eta[HighestNonFatVarPt_pruned_Number],jethelperAK5_phi[HighestNonFatVarPt_pruned_Number],jethelperAK5_energy[HighestNonFatVarPt_pruned_Number]);
				//SecondNonFatVar bjet-selected jet
			TLorentzVector Jet_SecondNonFatVar_bjetness; 
			Jet_SecondNonFatVar_bjetness.SetPtEtaPhiE(cmgPFJet_cmgPFJetSelCHS_pt[Jet_SecondNonFatVar_bjetness_Number],cmgPFJet_cmgPFJetSelCHS_eta[Jet_SecondNonFatVar_bjetness_Number],cmgPFJet_cmgPFJetSelCHS_phi[Jet_SecondNonFatVar_bjetness_Number],cmgPFJet_cmgPFJetSelCHS_energy[Jet_SecondNonFatVar_bjetness_Number]); 
			
			TLorentzVector Jet_SecondNonFatVar_pruned_bjetness; 
			Jet_SecondNonFatVar_pruned_bjetness.SetPtEtaPhiE(jethelperAK5_pt[Jet_SecondNonFatVar_pruned_bjetness_Number],jethelperAK5_eta[Jet_SecondNonFatVar_pruned_bjetness_Number],jethelperAK5_phi[Jet_SecondNonFatVar_pruned_bjetness_Number],jethelperAK5_energy[Jet_SecondNonFatVar_pruned_bjetness_Number]); 
			
			Jet_SecondNonFatVar_bjetness_pruned_eta = jethelperAK5_eta[Jet_SecondNonFatVar_pruned_bjetness_Number];
			Jet_SecondNonFatVar_bjetness_pruned_phi = jethelperAK5_phi[Jet_SecondNonFatVar_pruned_bjetness_Number];
			
				//SecondNonFatVar pt-selected jet
			TLorentzVector Jet_SecondNonFatVar_HighestPt; 
			Jet_SecondNonFatVar_HighestPt.SetPtEtaPhiE(cmgPFJet_cmgPFJetSelCHS_pt[Jet_SecondNonFatVar_HighestPt_Number],cmgPFJet_cmgPFJetSelCHS_eta[Jet_SecondNonFatVar_HighestPt_Number],cmgPFJet_cmgPFJetSelCHS_phi[Jet_SecondNonFatVar_HighestPt_Number],cmgPFJet_cmgPFJetSelCHS_energy[Jet_SecondNonFatVar_HighestPt_Number]); 
			
			TLorentzVector Jet_SecondNonFatVar_pruned_HighestPt; 
			Jet_SecondNonFatVar_pruned_HighestPt.SetPtEtaPhiE(jethelperAK5_pt[Jet_SecondNonFatVar_pruned_HighestPt_Number],jethelperAK5_eta[Jet_SecondNonFatVar_pruned_HighestPt_Number],jethelperAK5_phi[Jet_SecondNonFatVar_pruned_HighestPt_Number],jethelperAK5_energy[Jet_SecondNonFatVar_pruned_HighestPt_Number]); 
			
			Jet_SecondNonFatVar_HighestPt_pruned_eta = jethelperAK5_eta[Jet_SecondNonFatVar_pruned_HighestPt_Number];
			Jet_SecondNonFatVar_HighestPt_pruned_phi = jethelperAK5_phi[Jet_SecondNonFatVar_pruned_HighestPt_Number];
			
			
			deltaR_SecondNonFatVar_pruned_bjetness_SecondNonFatVar_pruned_HighestPt = deltaR(jethelperAK5_eta[Jet_SecondNonFatVar_pruned_HighestPt_Number], jethelperAK5_eta[Jet_SecondNonFatVar_pruned_bjetness_Number], deltaPhi(jethelperAK5_phi[Jet_SecondNonFatVar_pruned_HighestPt_Number], jethelperAK5_phi[Jet_SecondNonFatVar_pruned_bjetness_Number]));
			
			// resetting mass parameters
			Jet_SecondNonFatVar_HighestPt_mass = 0;
			Jet_SecondNonFatVar_bjetness_mass = 0;
			Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness =0;
			Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt =0;

			Resonancemass_AK5_bjetness = 0;
			Resonancemass_AK5_HighestPt = 0;

			Jet_SecondNonFatVar_pruned_HighestPt_mass = 0;
			Jet_SecondNonFatVar_pruned_bjetness_mass = 0;
			Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness =0;
			Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt =0;

			Resonancemass_AK5_pruned_bjetness = 0;
			Resonancemass_AK5_pruned_HighestPt = 0;
			dEta_Fat_AK5RecH_bjetness =-10;
			dEta_Fat_AK5RecH_pruned_bjetness=-10;
			dEta_Fat_AK5RecH_HighestPt =-10;
			dEta_Fat_AK5RecH_pruned_HighestPt=-10;

			// only reconstruct if third jet is found
				// for highest pt
			if(Jet_SecondNonFatVar_HighestPt_Number != -1)
			{
				Jet_SecondNonFatVar_HighestPt_mass = cmgPFJet_cmgPFJetSelCHS_mass[Jet_SecondNonFatVar_HighestPt_Number];	
				Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_HighestPt = (Jet_SecondNonFatVar_HighestPt + Jet_NonFatVar).M();
				dEta_Fat_AK5RecH_HighestPt = fabs((Jet_NonFatVar + Jet_SecondNonFatVar_HighestPt).Eta() - JetFateta);
				Resonancemass_AK5_HighestPt = (JetFat + Jet_NonFatVar + Jet_SecondNonFatVar_HighestPt).M();
			}
				// and for bjetness
			if(Jet_SecondNonFatVar_bjetness_Number != -1)
			{
				Jet_SecondNonFatVar_bjetness_mass = cmgPFJet_cmgPFJetSelCHS_mass[Jet_SecondNonFatVar_bjetness_Number];
				Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_bjetness = (Jet_SecondNonFatVar_bjetness + Jet_NonFatVar).M(); 
				dEta_Fat_AK5RecH_bjetness = fabs((Jet_NonFatVar + Jet_SecondNonFatVar_bjetness).Eta() - JetFateta);
				Resonancemass_AK5_bjetness = (JetFat + Jet_NonFatVar + Jet_SecondNonFatVar_bjetness).M();				
			}
			
			// PRUNED only reconstruct if third jet is found
				// for highest pt
			if(Jet_SecondNonFatVar_pruned_HighestPt_Number != -1)
			{
				Jet_SecondNonFatVar_pruned_HighestPt_mass = jethelperAK5_mass[Jet_SecondNonFatVar_pruned_HighestPt_Number];	
				Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_HighestPt = (Jet_SecondNonFatVar_pruned_HighestPt + Jet_NonFatVar_pruned).M();				
				
				dEta_Fat_AK5RecH_pruned_HighestPt = fabs((Jet_NonFatVar_pruned + Jet_SecondNonFatVar_pruned_HighestPt).Eta() - JetFateta);
				Resonancemass_AK5_pruned_HighestPt = (JetFat + Jet_NonFatVar_pruned + Jet_SecondNonFatVar_pruned_HighestPt).M();
			}
				// and for bjetness
			if(Jet_SecondNonFatVar_pruned_bjetness_Number != -1)
			{
				Jet_SecondNonFatVar_pruned_bjetness_mass = jethelperAK5_mass[Jet_SecondNonFatVar_pruned_bjetness_Number];
				Jet_NonFatVar_plus_SecondNonFatVar_AK5mass_pruned_bjetness = (Jet_SecondNonFatVar_pruned_bjetness + Jet_NonFatVar_pruned).M();
				dEta_Fat_AK5RecH_pruned_bjetness = fabs((Jet_NonFatVar_pruned + Jet_SecondNonFatVar_pruned_bjetness).Eta() - JetFateta);
				Resonancemass_AK5_pruned_bjetness = (JetFat + Jet_NonFatVar_pruned + Jet_SecondNonFatVar_pruned_bjetness).M();
			}
			
			
			//Threejet_analysis_AK5->Fill(); // only filled when there is an AK5 jet away from fat found
		}

// ****************************************************
//			START OF PART 1.B  (CA8)
// ****************************************************	

		 // checking for highest pt non-fat jet CA8  
		Jet_NonFat = 0;
		Jet_NonFat_Number = -1;
		Jet_NonFat_pruned = 0;
		Jet_NonFat_pruned_Number = -1;
		for(int aa=0;aa<njetsCA8;aa++) 							// Checking for highest pt non-fat jet CA8
		{
			if((aa!= FattieNumber) && (jethelperCA8_pt[aa] > Jet_NonFat)) // by looping over all jets (except fat index nr) 
			{	
					Jet_NonFat = jethelperCA8_pt[aa]; 			// and saving highest pt
					Jet_NonFat_Number = aa;	
					Jet_NonFat_bjetness = jethelperCA8_combinedSecondaryVertexBJetTags[Jet_NonFat_Number];	
			}
			if((aa!= FattieNumber) && (jethelperCA8pruned_pt[aa] > Jet_NonFat_pruned)) // by looping over all jets (except fat index nr) 
			{	
					Jet_NonFat_pruned = jethelperCA8pruned_pt[aa]; 			// and saving highest pt
					Jet_NonFat_pruned_Number = aa;	
					Jet_NonFat_pruned_bjetness = jethelperCA8_combinedSecondaryVertexBJetTags[Jet_NonFat_pruned_Number];	
			}
		} 	


		
		if(( Jet_NonFat_Number != -1) & (Jet_NonFat_pruned_Number != -1))
		{	
			 // saving NonFat parameters (both pruned and non-pruned)  
			TLorentzVector Jet_NonFat;		
			Jet_NonFat.SetPtEtaPhiE(jethelperCA8_pt[Jet_NonFat_Number],jethelperCA8_eta[Jet_NonFat_Number],jethelperCA8_phi[Jet_NonFat_Number],jethelperCA8_energy[Jet_NonFat_Number]);
			Jet_NonFatCA8_mass = jethelperCA8_mass[Jet_NonFat_Number];
		
			TLorentzVector Jet_NonFat_pruned;		
			Jet_NonFat_pruned.SetPtEtaPhiE(jethelperCA8pruned_pt[Jet_NonFat_pruned_Number],jethelperCA8pruned_eta[Jet_NonFat_pruned_Number],jethelperCA8pruned_phi[Jet_NonFat_pruned_Number],jethelperCA8pruned_energy[Jet_NonFat_pruned_Number]);
			Jet_NonFatCA8_pruned_mass = jethelperCA8pruned_mass[Jet_NonFat_pruned_Number];
		
			Jet_NonFat_eta = jethelperCA8_eta[Jet_NonFat_Number];
			Jet_NonFat_phi = jethelperCA8_phi[Jet_NonFat_Number]; 
	    		Jet_NonFat_pt = jethelperCA8_pt[Jet_NonFat_Number];
	
	    		Jet_NonFat_pruned_eta = jethelperCA8pruned_eta[Jet_NonFat_pruned_Number];
			Jet_NonFat_pruned_phi = jethelperCA8pruned_phi[Jet_NonFat_pruned_Number]; 
	    		Jet_NonFat_pruned_pt = jethelperCA8pruned_pt[Jet_NonFat_pruned_Number];
	    		
			deltaRFatNonFat = deltaR(JetFateta, Jet_NonFat_eta, deltaPhi(JetFatphi, Jet_NonFat_phi)); // check if they're back-to-back
			Jet_NonFatCA8Nsub = jethelperCA8_tau2[Jet_NonFat_Number]/jethelperCA8_tau1[Jet_NonFat_Number];  
			dEta_Fat_NonFat_pruned = fabs(JetFateta - Jet_NonFat_pruned_eta);
			dEta_Fat_NonFat = (fabs(JetFateta - Jet_NonFat_eta));
	
			 // checking for second highest pt non-fat jet CA8  
			Jet_SecondNonFat_HighestPt = -1;
			Jet_SecondNonFat_HighestPt_Number = -1;
			Jet_SecondNonFat_bjetness = -1;		
			Jet_SecondNonFat_bjetness_Number = -1;	
	
			//deltaRNonFatSecondNonFat = -1;
				
			for(int bb=0;bb<njetsCA8;bb++)
			{
				if( (deltaR(Jet_NonFat_eta, jethelperCA8_eta[bb], deltaPhi(Jet_NonFat_phi, jethelperCA8_phi[bb])) < 1.3) && (bb!=Jet_NonFat_Number))
				{ 
       	 			if(jethelperCA8_pt[bb] > Jet_SecondNonFat_HighestPt) 
       	       		{
              				Jet_SecondNonFat_HighestPt = jethelperCA8_pt[bb];
						Jet_SecondNonFat_HighestPt_Number = bb;
						//deltaR_NonFat_SecondNonFat_HighestPt = deltaR(jethelperCA8_eta[Jet_NonFat_Number], jethelperCA8_eta[bb], deltaPhi(jethelperCA8_phi[Jet_NonFat_Number], jethelperCA8_phi[bb]));
						
              			}
			
					if(jethelperCA8_combinedSecondaryVertexBJetTags[bb] > Jet_SecondNonFat_bjetness)
					{
						Jet_SecondNonFat_bjetness = jethelperCA8_combinedSecondaryVertexBJetTags[bb];
						Jet_SecondNonFat_bjetness_Number = bb;
						//deltaR_NonFat_SecondNonFat_bjetness = deltaR(jethelperCA8_eta[Jet_NonFat_Number], jethelperCA8_eta[bb], deltaPhi(jethelperCA8_phi[Jet_NonFat_Number], jethelperCA8_phi[bb]));
					}
				}
			}

//    			Jet_NonFat_plus_SecondNonFat_CA8Mass = 0;
//    			Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned = 0;

			Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt = 0;
	    		Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt = 0;

	    		Jet_SecondNonFat_HighestPt_pt=-1;
			Jet_SecondNonFat_HighestPt_eta=-10;
	    	      	Jet_SecondNonFat_HighestPt_phi=-10;
	    	      		
	    	      	Jet_SecondNonFat_HighestPt_pruned_pt=-1;
			Jet_SecondNonFat_HighestPt_pruned_eta=-10;
	    	      	Jet_SecondNonFat_HighestPt_pruned_phi=-10;
	
			deltaR_NonFat_SecondNonFat_HighestPt = -1;
			Resonancemass_HighestPt = 0;
			Resonancemass_HighestPt_pruned = 0;
			dEta_Fat_CA8RecH_pruned_HighestPt = -10;
			dEta_Fat_CA8RecH_HighestPt = -10;
	    		
			if(Jet_NonFat_Number != -1 && Jet_SecondNonFat_HighestPt_Number != -1) 
			{    	
//				cout << FattieNumber << " " << Jet_NonFat_Number << " " << Jet_SecondNonFat_HighestPt_Number << endl;
				 // setting second-non-fat parameters, pruned and non-pruned  			
		    		TLorentzVector Jet_SecondNonFat_HighestPt; 
	    			Jet_SecondNonFat_HighestPt.SetPtEtaPhiE(jethelperCA8_pt[Jet_SecondNonFat_HighestPt_Number],jethelperCA8_eta[Jet_SecondNonFat_HighestPt_Number],jethelperCA8_phi[Jet_SecondNonFat_HighestPt_Number],jethelperCA8_energy[Jet_SecondNonFat_HighestPt_Number]);
    			
  	  			TLorentzVector Jet_SecondNonFat_HighestPt_pruned; 
	    			Jet_SecondNonFat_HighestPt_pruned.SetPtEtaPhiE(jethelperCA8pruned_pt[Jet_SecondNonFat_HighestPt_Number],jethelperCA8pruned_eta[Jet_SecondNonFat_HighestPt_Number],jethelperCA8pruned_phi[Jet_SecondNonFat_HighestPt_Number],jethelperCA8pruned_energy[Jet_SecondNonFat_HighestPt_Number]);
   	 			Jet_SecondNonFatCA8_pruned_HighestPt_mass = jethelperCA8pruned_mass[Jet_SecondNonFat_HighestPt_Number];
    			
   	 			Jet_SecondNonFat_HighestPt_pt = jethelperCA8_pt[Jet_SecondNonFat_HighestPt_Number];
				Jet_SecondNonFat_HighestPt_eta = jethelperCA8_eta[Jet_SecondNonFat_HighestPt_Number];                         
    		      		Jet_SecondNonFat_HighestPt_phi = jethelperCA8_phi[Jet_SecondNonFat_HighestPt_Number];  
    	      		
   	 	      		Jet_SecondNonFat_HighestPt_pruned_pt = jethelperCA8pruned_pt[Jet_SecondNonFat_HighestPt_Number];
				Jet_SecondNonFat_HighestPt_pruned_eta = jethelperCA8pruned_eta[Jet_SecondNonFat_HighestPt_Number];                         
  	  	      		Jet_SecondNonFat_HighestPt_pruned_phi = jethelperCA8pruned_phi[Jet_SecondNonFat_HighestPt_Number];

    		      		Jet_NonFat_plus_SecondNonFat_CA8Mass_HighestPt = (Jet_NonFat+Jet_SecondNonFat_HighestPt).M(); 
    		      		Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_HighestPt = (Jet_NonFat_pruned+Jet_SecondNonFat_HighestPt_pruned).M();    	      		
    		      		
    		      		dEta_Fat_CA8RecH_HighestPt = fabs((Jet_NonFat_pruned + Jet_SecondNonFat_HighestPt).Eta() - JetFateta);    		    
    		      		dEta_Fat_CA8RecH_pruned_HighestPt = fabs((Jet_NonFat_pruned + Jet_SecondNonFat_HighestPt_pruned).Eta() - JetFateta);
				deltaR_NonFat_SecondNonFat_HighestPt = deltaR(Jet_NonFat_eta, Jet_SecondNonFat_HighestPt_eta, deltaPhi(Jet_NonFat_phi, Jet_SecondNonFat_HighestPt_phi));
				Resonancemass_HighestPt = (JetFat + Jet_NonFat + Jet_SecondNonFat_HighestPt).M();
				Resonancemass_HighestPt_pruned = (JetFat_pruned + Jet_NonFat_pruned + Jet_SecondNonFat_HighestPt_pruned).M();


			}
		
			Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness = 0;
    			Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness = 0;
    			Jet_SecondNonFat_bjetness_pt=-1;
			Jet_SecondNonFat_bjetness_eta=-10;
    		      	Jet_SecondNonFat_bjetness_phi=-10;
    		      	Resonancemass_bjetness = 0;
			Resonancemass_bjetness_pruned = 0;
    	      		
    		      	Jet_SecondNonFat_bjetness_pruned_pt=-1;
			Jet_SecondNonFat_bjetness_pruned_eta=-10;
    		      	Jet_SecondNonFat_bjetness_pruned_phi=-10;
			deltaR_NonFat_SecondNonFat_bjetness = -10;
			dEta_Fat_CA8RecH_pruned_bjetness=-10;
			dEta_Fat_CA8RecH_bjetness=-10;			
			if(Jet_NonFat_Number != -1 && Jet_SecondNonFat_bjetness_Number != -1) 
			{    		
				 // setting second-non-fat parameters, pruned and non-pruned  	  			
		    		TLorentzVector Jet_SecondNonFat_bjetness; 
    				Jet_SecondNonFat_bjetness.SetPtEtaPhiE(jethelperCA8_pt[Jet_SecondNonFat_bjetness_Number],jethelperCA8_eta[Jet_SecondNonFat_bjetness_Number],jethelperCA8_phi[Jet_SecondNonFat_bjetness_Number],jethelperCA8_energy[Jet_SecondNonFat_bjetness_Number]);
    			
    				TLorentzVector Jet_SecondNonFat_pruned_bjetness; 
    				Jet_SecondNonFat_pruned_bjetness.SetPtEtaPhiE(jethelperCA8pruned_pt[Jet_SecondNonFat_bjetness_Number],jethelperCA8pruned_eta[Jet_SecondNonFat_bjetness_Number],jethelperCA8pruned_phi[Jet_SecondNonFat_bjetness_Number],jethelperCA8pruned_energy[Jet_SecondNonFat_bjetness_Number]);
    				Jet_SecondNonFatCA8_pruned_bjetness_mass = jethelperCA8pruned_mass[Jet_SecondNonFat_bjetness_Number];
    			
    				Jet_SecondNonFat_bjetness_pt = jethelperCA8_pt[Jet_SecondNonFat_bjetness_Number];
				Jet_SecondNonFat_bjetness_eta = jethelperCA8_eta[Jet_SecondNonFat_bjetness_Number];                         
    	  	    		Jet_SecondNonFat_bjetness_phi = jethelperCA8_phi[Jet_SecondNonFat_bjetness_Number];  
    	      		
    	 	     		Jet_SecondNonFat_bjetness_pruned_pt = jethelperCA8pruned_pt[Jet_SecondNonFat_bjetness_Number];
				Jet_SecondNonFat_bjetness_pruned_eta = jethelperCA8pruned_eta[Jet_SecondNonFat_bjetness_Number];                         
    	  	    		Jet_SecondNonFat_bjetness_pruned_phi = jethelperCA8pruned_phi[Jet_SecondNonFat_bjetness_Number];

    	    	  		Jet_NonFat_plus_SecondNonFat_CA8Mass_bjetness = (Jet_NonFat+Jet_SecondNonFat_bjetness).M(); 
    	    	  		Jet_NonFat_plus_SecondNonFat_CA8Mass_pruned_bjetness = (Jet_NonFat_pruned+Jet_SecondNonFat_pruned_bjetness).M();      	
		    	
				deltaR_NonFat_SecondNonFat_bjetness = deltaR(Jet_NonFat_eta, Jet_SecondNonFat_bjetness_eta, deltaPhi(Jet_NonFat_phi, Jet_SecondNonFat_bjetness_phi));
				
				dEta_Fat_CA8RecH_bjetness = fabs((Jet_NonFat_pruned + Jet_SecondNonFat_bjetness).Eta() - JetFateta);
				dEta_Fat_CA8RecH_pruned_bjetness = fabs((Jet_NonFat_pruned + Jet_SecondNonFat_pruned_bjetness).Eta() - JetFateta);	
				
				Resonancemass_bjetness = (JetFat + Jet_NonFat + Jet_SecondNonFat_bjetness).M();
				Resonancemass_bjetness_pruned = (JetFat_pruned + Jet_NonFat_pruned + Jet_SecondNonFat_pruned_bjetness).M();
			}
			
			//Threejet_analysis_CA8->Fill();   // filled whenever 1 higgs is found
		}
	}



	  //_____________________________________________________________________
  


	  // ---------------------
	  // -- fill histograms --
	  // ---------------------	  

          if(geneventinfoproduct_weight>0)
	      weight=geneventinfoproduct_weight;
	  else
	      weight=1;

	  weight = weight*vertexWeight;
         categories=-1;
          categoriesNS=-1;

          mgg = DijetMassCA8;
          


	  mass->Fill(DijetMassCA8, weight);                                                        // histogram of the masses of all the ranked events

	  if((!((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135)))&&                                           // no jet in the
	     (!((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))))                                            // mass window
	  {
              mass_0mtag->Fill(DijetMassCA8, weight);
	      categories = 5;
	  }
	  if(((((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135)&&(Jet1CA8Nsub<0.75)&&(Jet1CA8Nsub>0.5)))&&    // 1 unpure jet in 
	      (!((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))))||                                         // the mass window,
 	     ((((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135)&&(Jet2CA8Nsub<0.75)&&(Jet2CA8Nsub>0.5)))&&    // the other out of 
	      (!((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135)))))                                          // the mass window
	  {
              mass_1mtag_1lptag->Fill(DijetMassCA8, weight);
	      categories = 4;
	  }
	  if(((((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135)&&(Jet1CA8Nsub<0.5)))&&                        // 1 pure jet in
	      (!((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))))||                                         // the mass window
 	     ((((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135)&&(Jet2CA8Nsub<0.5)))&&                        // the other out of
	      (!((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135)))))                                          // the mass window
	  {
              mass_1mtag_1hptag->Fill(DijetMassCA8, weight);
	      categories = 3;
	  }
	  if(((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135))&&                                              // the 2 jets are 
	     ((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))&&                                              // unpure but in 
	     ((Jet1CA8Nsub<0.75)&&(Jet2CA8Nsub<0.75)&&(Jet1CA8Nsub>0.5)&&(Jet2CA8Nsub>0.5)))       // the mass window
	  {
              mass_2mtag_2lptag->Fill(DijetMassCA8, weight);
	      categories = 2;
	  }
	  if(((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135))&&                                              // the 2 jets are in 
	     ((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))&&                                              // the mass window
	     (((Jet1CA8Nsub<0.75)&&(Jet1CA8Nsub>0.5)&&(Jet2CA8Nsub<0.5))||                         // but one is pure
	      ((Jet1CA8Nsub<0.5)&&(Jet2CA8Nsub<0.75)&&(Jet2CA8Nsub>0.5))))                         // and the other unpure
	  {
              mass_2mtag_1hptag_1lptag->Fill(DijetMassCA8, weight);
	      categories = 1;
	  }


	  if(((Jet1CA8_prunedmass>110)&&(Jet1CA8_prunedmass<135))&&                                              // the 2 jets are
	     ((Jet2CA8_prunedmass>110)&&(Jet2CA8_prunedmass<135))&&                                              // pure and in
	     ((Jet1CA8Nsub<0.5)&&(Jet2CA8Nsub<0.5)))                                               // the mass window
	  {
         	mass_2mtag_2hptag->Fill(DijetMassCA8, weight);
	      	categories = 0;
	  }

          if(mgg>890) {                                                                    // dijetWtag and missing mass gather 
	    // if (centralitySelection) TCVARS->Fill();                                    // all the ranked events with mgg>890.
//	    dijetWtag_weighted->Fill(weight);
	    //dijetWtag->Fill();                                                             // TCVARS gathers, among these events, those with deta<1.3

	  }
	}
  stream.close();
  ofile.close();

  return 0;
}
