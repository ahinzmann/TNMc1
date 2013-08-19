#ifndef ANALYZER_H
#define ANALYZER_H
//-----------------------------------------------------------------------------
// File:        analyzer.h
// Description: Analyzer header for ntuples created by TheNtupleMaker
// Created:     Thu May 31 21:49:25 2012 by mkanalyzer.py
// Author:      Andreas Hinzmann
//-----------------------------------------------------------------------------
// -- System

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>

#ifdef PROJECT_NAME
#include "PhysicsTools/TheNtupleMaker/interface/treestream.h"
#include "PhysicsTools/TheNtupleMaker/interface/pdg.h"
#else
#include "treestream.h"
#include "pdg.h"
#endif

// -- Root

#include "TROOT.h"
#include "TApplication.h"
#include "TDirectory.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TKey.h"
#include "TH1F.h"
#include "TH2F.h"
//-----------------------------------------------------------------------------
// -- Declare variables to be read
//-----------------------------------------------------------------------------
std::vector<float>	electronhelper_caloIso(10,0);
std::vector<int>	electronhelper_charge(10,0);
std::vector<float>	electronhelper_deltaEtaSuperClusterTrackAtVtx(10,0);
std::vector<float>	electronhelper_deltaPhiSuperClusterTrackAtVtx(10,0);
std::vector<double>	electronhelper_dxywrtPV(10,0);
std::vector<double>	electronhelper_dzwrtPV(10,0);
std::vector<float>	electronhelper_eSuperClusterOverP(10,0);
std::vector<float>	electronhelper_ecalIso(10,0);
std::vector<double>	electronhelper_energy(10,0);
std::vector<double>	electronhelper_et(10,0);
std::vector<double>	electronhelper_eta(10,0);
std::vector<unsigned short>	electronhelper_gsfTrack_trackerExpectedHitsInner_numberOfHits(10,0);
std::vector<float>	electronhelper_hadronicOverEm(10,0);
std::vector<float>	electronhelper_hcalIso(10,0);
std::vector<int>	electronhelper_isEB(10,0);
std::vector<int>	electronhelper_isEE(10,0);
std::vector<double>	electronhelper_phi(10,0);
std::vector<double>	electronhelper_pt(10,0);
std::vector<float>	electronhelper_scSigmaIEtaIEta(10,0);
std::vector<float>	electronhelper_simpleEleId80relIso(10,0);
std::vector<float>	electronhelper_simpleEleId95relIso(10,0);
std::vector<double>	electronhelper_superCluster_energy(10,0);
std::vector<float>	electronhelper_trackIso(10,0);
int	eventhelper_bunchCrossing;
int	eventhelper_event;
int	eventhelper_isRealData;
int	eventhelper_luminosityBlock;
int	eventhelper_orbitNumber;
int	eventhelper_run;
double	geneventinfoproduct_alphaQCD;
double	geneventinfoproduct_alphaQED;
int	geneventinfoproduct_hasBinningValues;
int	geneventinfoproduct_hasPDF;
double	geneventinfoproduct_qScale;
unsigned int	geneventinfoproduct_signalProcessID;
double	geneventinfoproduct_weight;
std::vector<int>	genparticlehelper_charge(200,0);
std::vector<double>	genparticlehelper_eta(200,0);
std::vector<int>	genparticlehelper_firstDaughter(200,0);
std::vector<int>	genparticlehelper_firstMother(200,0);
std::vector<int>	genparticlehelper_lastDaughter(200,0);
std::vector<int>	genparticlehelper_lastMother(200,0);
std::vector<double>	genparticlehelper_mass(200,0);
std::vector<int>	genparticlehelper_pdgId(200,0);
std::vector<double>	genparticlehelper_phi(200,0);
std::vector<double>	genparticlehelper_pt(200,0);
std::vector<int>	genparticlehelper_status(200,0);
double	genruninfoproduct_crossSection;
double	genruninfoproduct_filterEfficiency;
std::vector<float>	jethelper3_combinedSecondaryVertexBJetTags(10,0);
std::vector<float>	jethelper3_combinedSecondaryVertexMVABJetTags(10,0);
std::vector<double>	jethelper3_energy(10,0);
std::vector<double>	jethelper3_et(10,0);
std::vector<double>	jethelper3_eta(10,0);
std::vector<double>	jethelper3_rapidity(10,0);
std::vector<double>	jethelper3_genJet_energy(10,0);
std::vector<double>	jethelper3_genJet_eta(10,0);
std::vector<double>	jethelper3_genJet_phi(10,0);
std::vector<double>	jethelper3_genJet_pt(10,0);
std::vector<int>	jethelper3_genParton_pdgId(10,0);
std::vector<float>	jethelper3_jetArea(10,0);
std::vector<float>	jethelper3_jetBProbabilityBJetTags(10,0);
std::vector<float>	jethelper3_jetProbabilityBJetTags(10,0);
std::vector<double>	jethelper3_mass(10,0);
std::vector<int>	jethelper3_nConstituents(10,0);
std::vector<int>	jethelper3_partonFlavour(10,0);
std::vector<double>	jethelper3_phi(10,0);
std::vector<double>	jethelper3_pt(10,0);
std::vector<float>	jethelper3_simpleSecondaryVertexHighEffBJetTags(10,0);
std::vector<float>	jethelper3_simpleSecondaryVertexHighPurBJetTags(10,0);
std::vector<float>	jethelper3_trackCountingHighEffBJetTags(10,0);
std::vector<float>	jethelper3_trackCountingHighPurBJetTags(10,0);
std::vector<double>	jethelper3_uncor_energy(10,0);
std::vector<double>	jethelper3_uncor_et(10,0);
std::vector<double>	jethelper3_uncor_pt(10,0);
std::vector<double>	jethelper3_component_0_fraction(10,0);
std::vector<double>	jethelper3_component_0_number(10,0);
std::vector<double>	jethelper3_component_1_fraction(10,0);
std::vector<double>	jethelper3_component_1_number(10,0);
std::vector<double>	jethelper3_component_2_fraction(10,0);
std::vector<double>	jethelper3_component_2_number(10,0);
std::vector<double>	jethelper3_component_3_fraction(10,0);
std::vector<double>	jethelper3_component_3_number(10,0);
std::vector<double>	jethelper3_component_4_fraction(10,0);
std::vector<double>	jethelper3_component_4_number(10,0);
std::vector<double>	jethelper3_component_5_fraction(10,0);
std::vector<double>	jethelper3_component_5_number(10,0);
std::vector<double>	jethelper3_component_6_fraction(10,0);
std::vector<double>	jethelper3_component_6_number(10,0);
std::vector<double>	jethelper3_component_7_fraction(10,0);
std::vector<double>	jethelper3_component_7_number(10,0);

double	met2_energy;
double	met2_et;
double	met2_mEtSig;
double	met2_phi;
double	met2_pt;
double	met2_significance;
double	met2_sumEt;
double	met_energy;
double	met_et;
double	met_mEtSig;
double	met_phi;
double	met_pt;
double	met_significance;
double	met_sumEt;
std::vector<float>	muonhelper_TMOneStationTight(10,0);
std::vector<int>	muonhelper_charge(10,0);
std::vector<double>	muonhelper_dB(10,0);
std::vector<double>	muonhelper_dxywrtPV(10,0);
std::vector<double>	muonhelper_dzwrtPV(10,0);
std::vector<double>	muonhelper_energy(10,0);
std::vector<double>	muonhelper_et(10,0);
std::vector<double>	muonhelper_eta(10,0);
std::vector<unsigned short>	muonhelper_globalTrack_hitPattern_numberOfValidMuonHits(10,0);
std::vector<double>	muonhelper_globalTrack_normalizedChi2(10,0);
std::vector<unsigned short>	muonhelper_innerTrack_hitPattern_numberOfValidPixelHits(10,0);
std::vector<unsigned short>	muonhelper_innerTrack_hitPattern_pixelLayersWithMeasurement(10,0);
std::vector<double>	muonhelper_innerTrack_normalizedChi2(10,0);
std::vector<int>	muonhelper_isGlobalMuon(10,0);
std::vector<int>	muonhelper_isPFMuon(10,0);
std::vector<int>	muonhelper_isTrackerMuon(10,0);
std::vector<int>	muonhelper_numberOfMatchedStations(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumChargedHadronPt(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumChargedParticlePt(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumNeutralHadronEt(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumNeutralHadronEtHighThreshold(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumPUPt(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumPhotonEt(10,0);
std::vector<float>	muonhelper_pfIsolationR04_sumPhotonEtHighThreshold(10,0);
std::vector<double>	muonhelper_phi(10,0);
std::vector<double>	muonhelper_pt(10,0);
std::vector<unsigned short>	muonhelper_track_hitPattern_trackerLayersWithMeasurement(10,0);
int	nelectronhelper;
int	ngenparticlehelper;
int	njethelper3;
int	nmuonhelper;
int	ntau;
int	nvertex;
int	pileupsummaryinfo_getBunchCrossing;
int	pileupsummaryinfo_getPU_NumInteractions;
float	pileupsummaryinfo_getTrueNumInteractions;
double	sdouble_kt6PFJets_rho_value;
std::vector<float>	tau_byLooseCombinedIsolationDeltaBetaCorr(10,0);
std::vector<float>	tau_byMediumCombinedIsolationDeltaBetaCorr(10,0);
std::vector<float>	tau_caloIso(10,0);
std::vector<float>	tau_ecalIso(10,0);
std::vector<double>	tau_energy(10,0);
std::vector<double>	tau_et(10,0);
std::vector<double>	tau_eta(10,0);
std::vector<float>	tau_hcalIso(10,0);
std::vector<double>	tau_phi(10,0);
std::vector<double>	tau_pt(10,0);
std::vector<float>	tau_trackIso(10,0);
int	triggerresultshelper_CSCTightHaloFilterPath;
int	triggerresultshelper_EcalDeadCellBoundaryEnergyFilterPath;
int	triggerresultshelper_EcalDeadCellTriggerPrimitiveFilterPath;
int	triggerresultshelper_HBHENoiseFilterPath;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v11;
int	triggerresultshelper_HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v12;
int	triggerresultshelper_HLT_HT200_v1;
int	triggerresultshelper_HLT_HT200_v2;
int	triggerresultshelper_HLT_HT200_v3;
int	triggerresultshelper_HLT_HT250_v1;
int	triggerresultshelper_HLT_HT250_v2;
int	triggerresultshelper_HLT_HT250_v3;
int	triggerresultshelper_HLT_HT300_v1;
int	triggerresultshelper_HLT_HT300_v2;
int	triggerresultshelper_HLT_HT300_v3;
int	triggerresultshelper_HLT_HT350_v1;
int	triggerresultshelper_HLT_HT350_v2;
int	triggerresultshelper_HLT_HT350_v3;
int	triggerresultshelper_HLT_HT400_v1;
int	triggerresultshelper_HLT_HT400_v2;
int	triggerresultshelper_HLT_HT400_v3;
int	triggerresultshelper_HLT_HT450_v1;
int	triggerresultshelper_HLT_HT450_v2;
int	triggerresultshelper_HLT_HT450_v3;
int	triggerresultshelper_HLT_HT450_v4;
int	triggerresultshelper_HLT_HT450_v5;
int	triggerresultshelper_HLT_HT450_v6;
int	triggerresultshelper_HLT_HT450_v7;
int	triggerresultshelper_HLT_HT450_v8;
int	triggerresultshelper_HLT_HT450_v9;
int	triggerresultshelper_HLT_HT500_v1;
int	triggerresultshelper_HLT_HT500_v2;
int	triggerresultshelper_HLT_HT500_v3;
int	triggerresultshelper_HLT_HT550_v1;
int	triggerresultshelper_HLT_HT550_v2;
int	triggerresultshelper_HLT_HT550_v3;
int	triggerresultshelper_HLT_HT650_v1;
int	triggerresultshelper_HLT_HT650_v2;
int	triggerresultshelper_HLT_HT650_v3;
int	triggerresultshelper_HLT_HT650_v4;
int	triggerresultshelper_HLT_HT650_v5;
int	triggerresultshelper_HLT_HT650_v6;
int	triggerresultshelper_HLT_HT650_v7;
int	triggerresultshelper_HLT_HT650_v8;
int	triggerresultshelper_HLT_HT650_v9;
int	triggerresultshelper_HLT_HT750_v1;
int	triggerresultshelper_HLT_HT750_v2;
int	triggerresultshelper_HLT_HT750_v3;
int	triggerresultshelper_HLT_HT750_v4;
int	triggerresultshelper_HLT_HT750_v5;
int	triggerresultshelper_HLT_HT750_v6;
int	triggerresultshelper_HLT_HT750_v7;
int	triggerresultshelper_HLT_HT750_v8;
int	triggerresultshelper_HLT_HT750_v9;
int	triggerresultshelper_HLT_PFHT350_v1;
int	triggerresultshelper_HLT_PFHT350_v2;
int	triggerresultshelper_HLT_PFHT350_v3;
int	triggerresultshelper_HLT_PFHT350_v4;
int	triggerresultshelper_HLT_PFHT350_v5;
int	triggerresultshelper_HLT_PFHT350_v6;
int	triggerresultshelper_HLT_PFHT650_v1;
int	triggerresultshelper_HLT_PFHT650_v2;
int	triggerresultshelper_HLT_PFHT650_v3;
int	triggerresultshelper_HLT_PFHT650_v4;
int	triggerresultshelper_HLT_PFHT650_v5;
int	triggerresultshelper_HLT_PFHT650_v6;
int	triggerresultshelper_HLT_PFHT650_v7;
int	triggerresultshelper_HLT_PFHT650_v8;
int	triggerresultshelper_HLT_PFHT650_v9;
int	triggerresultshelper_HLT_PFHT650_v10;
int	triggerresultshelper_HLT_PFHT650_v11;
int	triggerresultshelper_HLT_PFHT700_v1;
int	triggerresultshelper_HLT_PFHT700_v2;
int	triggerresultshelper_HLT_PFHT700_v3;
int	triggerresultshelper_HLT_PFHT700_v4;
int	triggerresultshelper_HLT_PFHT700_v5;
int	triggerresultshelper_HLT_PFHT700_v6;
int	triggerresultshelper_HLT_PFHT700_v7;
int	triggerresultshelper_HLT_PFHT700_v8;
int	triggerresultshelper_HLT_PFHT700_v9;
int	triggerresultshelper_HLT_PFHT750_v1;
int	triggerresultshelper_HLT_PFHT750_v2;
int	triggerresultshelper_HLT_PFHT750_v3;
int	triggerresultshelper_HLT_PFHT750_v4;
int	triggerresultshelper_HLT_PFHT750_v5;
int	triggerresultshelper_HLT_PFHT750_v6;
int	triggerresultshelper_HLT_PFHT750_v7;
int	triggerresultshelper_HLT_PFHT750_v8;
int	triggerresultshelper_HLT_PFHT750_v9;
int	triggerresultshelper_HLT_PFNoPUHT650_v1;
int	triggerresultshelper_HLT_PFNoPUHT650_v2;
int	triggerresultshelper_HLT_PFNoPUHT650_v3;
int	triggerresultshelper_HLT_PFNoPUHT650_v4;
int	triggerresultshelper_HLT_PFNoPUHT650_v5;
int	triggerresultshelper_HLT_PFNoPUHT650_v6;
int	triggerresultshelper_HLT_DiPFJetAve400_v1;
int	triggerresultshelper_HLT_DiPFJetAve400_v2;
int	triggerresultshelper_HLT_DiPFJetAve400_v3;
int	triggerresultshelper_HLT_DiPFJetAve400_v4;
int	triggerresultshelper_HLT_DiPFJetAve400_v5;
int	triggerresultshelper_HLT_DiPFJetAve400_v6;
int	triggerresultshelper_HLT_DiPFJetAve400_v7;
int	triggerresultshelper_HLT_DiPFJetAve400_v8;
int	triggerresultshelper_HLT_DiPFJetAve400_v9;
int	triggerresultshelper_HLT_DiPFJetAve400_v10;
int	triggerresultshelper_HLT_DiPFJetAve400_v11;
int	triggerresultshelper_HLT_DiPFJetAve400_v12;
int	triggerresultshelper_HLT_PFJet140_v1;
int	triggerresultshelper_HLT_PFJet140_v2;
int	triggerresultshelper_HLT_PFJet140_v3;
int	triggerresultshelper_HLT_PFJet200_v1;
int	triggerresultshelper_HLT_PFJet200_v2;
int	triggerresultshelper_HLT_PFJet200_v3;
int	triggerresultshelper_HLT_PFJet260_v1;
int	triggerresultshelper_HLT_PFJet260_v2;
int	triggerresultshelper_HLT_PFJet260_v3;
int	triggerresultshelper_HLT_PFJet320_v1;
int	triggerresultshelper_HLT_PFJet320_v2;
int	triggerresultshelper_HLT_PFJet320_v3;
int	triggerresultshelper_HLT_PFJet320_v4;
int	triggerresultshelper_HLT_PFJet320_v5;
int	triggerresultshelper_HLT_PFJet400_v1;
int	triggerresultshelper_HLT_PFJet400_v2;
int	triggerresultshelper_HLT_PFJet400_v3;
int	triggerresultshelper_HLT_PFJet400_v4;
int	triggerresultshelper_HLT_PFJet400_v5;
int	triggerresultshelper_HLT_PFJet400_v6;
int	triggerresultshelper_HLT_PFJet400_v7;
int	triggerresultshelper_HLT_PFJet400_v8;
int	triggerresultshelper_HLT_PFJet400_v9;
int	triggerresultshelper_HLT_PFJet400_v10;
int	triggerresultshelper_HLT_PFJet400_v11;
int	triggerresultshelper_HLT_PFJet40_v1;
int	triggerresultshelper_HLT_PFJet40_v2;
int	triggerresultshelper_HLT_PFJet40_v3;
int	triggerresultshelper_HLT_PFJet80_v1;
int	triggerresultshelper_HLT_PFJet80_v2;
int	triggerresultshelper_HLT_PFJet80_v3;
int	triggerresultshelper_greedyMuonPFCandidateFilterPath;
int	triggerresultshelper_hcalLaserEventFilterPath;
int	triggerresultshelper_hcalLaserFilterFromAODPath;
int	triggerresultshelper_inconsistentMuonPFCandidateFilterPath;
int	triggerresultshelper_noscrapingFilterPath;
int	triggerresultshelper_hcallasereventfilter2012;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v1;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v4;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v5;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v6;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v7;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v8;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v9;
int	triggerresultshelper_prescaleHLT_FatDiPFJetMass750_DR1p1_Deta1p5_v10;
int	triggerresultshelper_prescaleHLT_HT200_v1;
int	triggerresultshelper_prescaleHLT_HT200_v2;
int	triggerresultshelper_prescaleHLT_HT200_v3;
int	triggerresultshelper_prescaleHLT_HT250_v1;
int	triggerresultshelper_prescaleHLT_HT250_v2;
int	triggerresultshelper_prescaleHLT_HT250_v3;
int	triggerresultshelper_prescaleHLT_HT300_v1;
int	triggerresultshelper_prescaleHLT_HT300_v2;
int	triggerresultshelper_prescaleHLT_HT300_v3;
int	triggerresultshelper_prescaleHLT_HT350_v1;
int	triggerresultshelper_prescaleHLT_HT350_v2;
int	triggerresultshelper_prescaleHLT_HT350_v3;
int	triggerresultshelper_prescaleHLT_HT400_v1;
int	triggerresultshelper_prescaleHLT_HT400_v2;
int	triggerresultshelper_prescaleHLT_HT400_v3;
int	triggerresultshelper_prescaleHLT_HT450_v1;
int	triggerresultshelper_prescaleHLT_HT450_v2;
int	triggerresultshelper_prescaleHLT_HT450_v3;
int	triggerresultshelper_prescaleHLT_HT450_v4;
int	triggerresultshelper_prescaleHLT_HT450_v5;
int	triggerresultshelper_prescaleHLT_HT450_v6;
int	triggerresultshelper_prescaleHLT_HT450_v7;
int	triggerresultshelper_prescaleHLT_HT450_v8;
int	triggerresultshelper_prescaleHLT_HT450_v9;
int	triggerresultshelper_prescaleHLT_HT500_v1;
int	triggerresultshelper_prescaleHLT_HT500_v2;
int	triggerresultshelper_prescaleHLT_HT500_v3;
int	triggerresultshelper_prescaleHLT_HT550_v1;
int	triggerresultshelper_prescaleHLT_HT550_v2;
int	triggerresultshelper_prescaleHLT_HT550_v3;
int	triggerresultshelper_prescaleHLT_HT650_v1;
int	triggerresultshelper_prescaleHLT_HT650_v2;
int	triggerresultshelper_prescaleHLT_HT650_v3;
int	triggerresultshelper_prescaleHLT_HT750_v1;
int	triggerresultshelper_prescaleHLT_HT750_v2;
int	triggerresultshelper_prescaleHLT_HT750_v3;
int	triggerresultshelper_prescaleHLT_PFHT350_v1;
int	triggerresultshelper_prescaleHLT_PFHT350_v2;
int	triggerresultshelper_prescaleHLT_PFHT350_v3;
int	triggerresultshelper_prescaleHLT_PFHT350_v4;
int	triggerresultshelper_prescaleHLT_PFHT350_v5;
int	triggerresultshelper_prescaleHLT_PFHT350_v6;
int	triggerresultshelper_prescaleHLT_PFHT650_v1;
int	triggerresultshelper_prescaleHLT_PFHT650_v2;
int	triggerresultshelper_prescaleHLT_PFHT650_v3;
int	triggerresultshelper_prescaleHLT_PFHT650_v4;
int	triggerresultshelper_prescaleHLT_PFHT650_v5;
int	triggerresultshelper_prescaleHLT_PFHT650_v6;
int	triggerresultshelper_prescaleHLT_PFHT650_v7;
int	triggerresultshelper_prescaleHLT_PFHT650_v8;
int	triggerresultshelper_prescaleHLT_PFHT700_v1;
int	triggerresultshelper_prescaleHLT_PFHT700_v2;
int	triggerresultshelper_prescaleHLT_PFHT700_v3;
int	triggerresultshelper_prescaleHLT_PFHT700_v4;
int	triggerresultshelper_prescaleHLT_PFHT700_v5;
int	triggerresultshelper_prescaleHLT_PFHT700_v6;
int	triggerresultshelper_prescaleHLT_PFHT750_v1;
int	triggerresultshelper_prescaleHLT_PFHT750_v2;
int	triggerresultshelper_prescaleHLT_PFHT750_v3;
int	triggerresultshelper_prescaleHLT_PFHT750_v4;
int	triggerresultshelper_prescaleHLT_PFHT750_v5;
int	triggerresultshelper_prescaleHLT_PFHT750_v6;
int	triggerresultshelper_prescaleHLT_PFJet140_v1;
int	triggerresultshelper_prescaleHLT_PFJet140_v2;
int	triggerresultshelper_prescaleHLT_PFJet140_v3;
int	triggerresultshelper_prescaleHLT_PFJet200_v1;
int	triggerresultshelper_prescaleHLT_PFJet200_v2;
int	triggerresultshelper_prescaleHLT_PFJet200_v3;
int	triggerresultshelper_prescaleHLT_PFJet260_v1;
int	triggerresultshelper_prescaleHLT_PFJet260_v2;
int	triggerresultshelper_prescaleHLT_PFJet260_v3;
int	triggerresultshelper_prescaleHLT_PFJet320_v1;
int	triggerresultshelper_prescaleHLT_PFJet320_v2;
int	triggerresultshelper_prescaleHLT_PFJet320_v3;
int	triggerresultshelper_prescaleHLT_PFJet320_v4;
int	triggerresultshelper_prescaleHLT_PFJet320_v5;
int	triggerresultshelper_prescaleHLT_PFJet400_v1;
int	triggerresultshelper_prescaleHLT_PFJet400_v2;
int	triggerresultshelper_prescaleHLT_PFJet400_v3;
int	triggerresultshelper_prescaleHLT_PFJet400_v4;
int	triggerresultshelper_prescaleHLT_PFJet400_v5;
int	triggerresultshelper_prescaleHLT_PFJet400_v6;
int	triggerresultshelper_prescaleHLT_PFJet400_v7;
int	triggerresultshelper_prescaleHLT_PFJet400_v8;
int	triggerresultshelper_prescaleHLT_PFJet400_v9;
int	triggerresultshelper_prescaleHLT_PFJet40_v1;
int	triggerresultshelper_prescaleHLT_PFJet40_v2;
int	triggerresultshelper_prescaleHLT_PFJet40_v3;
int	triggerresultshelper_prescaleHLT_PFJet80_v1;
int	triggerresultshelper_prescaleHLT_PFJet80_v2;
int	triggerresultshelper_prescaleHLT_PFJet80_v3;
int	triggerresultshelper_primaryVertexFilterPath;
int	triggerresultshelper_simpleDRfilterPath;
int	triggerresultshelper_totalKinematicsFilterPath;
int	triggerresultshelper_trackingFailureFilterPath;
std::vector<double>	vertex_chi2(200,0);
std::vector<int>	vertex_isFake(200,0);
std::vector<double>	vertex_ndof(200,0);
std::vector<double>	vertex_position_Rho(200,0);
std::vector<double>	vertex_x(200,0);
std::vector<double>	vertex_xError(200,0);
std::vector<double>	vertex_y(200,0);
std::vector<double>	vertex_yError(200,0);
std::vector<double>	vertex_z(200,0);
std::vector<double>	vertex_zError(200,0);

//-----------------------------------------------------------------------------
// --- Structs can be filled by calling fillObjects()
// --- after the call to stream.read(...)
//-----------------------------------------------------------------------------
struct electronhelper_s
{
  bool	selected;
  double	energy;
  double	et;
  double	pt;
  double	phi;
  double	eta;
  int	charge;
  float	eSuperClusterOverP;
  float	deltaEtaSuperClusterTrackAtVtx;
  float	deltaPhiSuperClusterTrackAtVtx;
  int	isEB;
  int	isEE;
  float	scSigmaIEtaIEta;
  float	hadronicOverEm;
  double	superCluster_energy;
  unsigned short	gsfTrack_trackerExpectedHitsInner_numberOfHits;
  float	simpleEleId80relIso;
  float	simpleEleId95relIso;
  float	trackIso;
  float	ecalIso;
  float	hcalIso;
  float	caloIso;
  double	dxywrtPV;
  double	dzwrtPV;
};
std::vector<electronhelper_s> electronhelper(10);

std::ostream& operator<<(std::ostream& os, const electronhelper_s& o)
{
  char r[1024];
  os << "electronhelper" << std::endl;
  sprintf(r, "  %-32s: %f\n", "energy", (double)o.energy); os << r;
  sprintf(r, "  %-32s: %f\n", "et", (double)o.et); os << r;
  sprintf(r, "  %-32s: %f\n", "pt", (double)o.pt); os << r;
  sprintf(r, "  %-32s: %f\n", "phi", (double)o.phi); os << r;
  sprintf(r, "  %-32s: %f\n", "eta", (double)o.eta); os << r;
  sprintf(r, "  %-32s: %f\n", "charge", (double)o.charge); os << r;
  sprintf(r, "  %-32s: %f\n", "eSuperClusterOverP", (double)o.eSuperClusterOverP); os << r;
  sprintf(r, "  %-32s: %f\n", "deltaEtaSuperClusterTrackAtVtx", (double)o.deltaEtaSuperClusterTrackAtVtx); os << r;
  sprintf(r, "  %-32s: %f\n", "deltaPhiSuperClusterTrackAtVtx", (double)o.deltaPhiSuperClusterTrackAtVtx); os << r;
  sprintf(r, "  %-32s: %f\n", "isEB", (double)o.isEB); os << r;
  sprintf(r, "  %-32s: %f\n", "isEE", (double)o.isEE); os << r;
  sprintf(r, "  %-32s: %f\n", "scSigmaIEtaIEta", (double)o.scSigmaIEtaIEta); os << r;
  sprintf(r, "  %-32s: %f\n", "hadronicOverEm", (double)o.hadronicOverEm); os << r;
  sprintf(r, "  %-32s: %f\n", "superCluster_energy", (double)o.superCluster_energy); os << r;
  sprintf(r, "  %-32s: %f\n", "gsfTrack_trackerExpectedHitsInner_numberOfHits", (double)o.gsfTrack_trackerExpectedHitsInner_numberOfHits); os << r;
  sprintf(r, "  %-32s: %f\n", "simpleEleId80relIso", (double)o.simpleEleId80relIso); os << r;
  sprintf(r, "  %-32s: %f\n", "simpleEleId95relIso", (double)o.simpleEleId95relIso); os << r;
  sprintf(r, "  %-32s: %f\n", "trackIso", (double)o.trackIso); os << r;
  sprintf(r, "  %-32s: %f\n", "ecalIso", (double)o.ecalIso); os << r;
  sprintf(r, "  %-32s: %f\n", "hcalIso", (double)o.hcalIso); os << r;
  sprintf(r, "  %-32s: %f\n", "caloIso", (double)o.caloIso); os << r;
  sprintf(r, "  %-32s: %f\n", "dxywrtPV", (double)o.dxywrtPV); os << r;
  sprintf(r, "  %-32s: %f\n", "dzwrtPV", (double)o.dzwrtPV); os << r;
  return os;
}
//-----------------------------------------------------------------------------
struct genparticlehelper_s
{
  bool	selected;
  int	firstMother;
  int	lastMother;
  int	firstDaughter;
  int	lastDaughter;
  int	charge;
  int	pdgId;
  int	status;
  double	pt;
  double	eta;
  double	phi;
  double	mass;
};
std::vector<genparticlehelper_s> genparticlehelper(200);

std::ostream& operator<<(std::ostream& os, const genparticlehelper_s& o)
{
  char r[1024];
  os << "genparticlehelper" << std::endl;
  sprintf(r, "  %-32s: %f\n", "firstMother", (double)o.firstMother); os << r;
  sprintf(r, "  %-32s: %f\n", "lastMother", (double)o.lastMother); os << r;
  sprintf(r, "  %-32s: %f\n", "firstDaughter", (double)o.firstDaughter); os << r;
  sprintf(r, "  %-32s: %f\n", "lastDaughter", (double)o.lastDaughter); os << r;
  sprintf(r, "  %-32s: %f\n", "charge", (double)o.charge); os << r;
  sprintf(r, "  %-32s: %f\n", "pdgId", (double)o.pdgId); os << r;
  sprintf(r, "  %-32s: %f\n", "status", (double)o.status); os << r;
  sprintf(r, "  %-32s: %f\n", "pt", (double)o.pt); os << r;
  sprintf(r, "  %-32s: %f\n", "eta", (double)o.eta); os << r;
  sprintf(r, "  %-32s: %f\n", "phi", (double)o.phi); os << r;
  sprintf(r, "  %-32s: %f\n", "mass", (double)o.mass); os << r;
  return os;
}

//-----------------------------------------------------------------------------
// -- Utilities
//-----------------------------------------------------------------------------
void
error(std::string message)
{
  std::cout << "** error ** " << message << std::endl;
  exit(0);
}

std::string 
strip(std::string line)
{
  int l = line.size();
  if ( l == 0 ) return std::string("");
  int n = 0;
  while (((line[n] == 0)    ||
	  (line[n] == ' ' ) ||
	  (line[n] == '\n') ||
	  (line[n] == '\t')) && n < l) n++;

  int m = l-1;
  while (((line[m] == 0)    ||
	  (line[m] == ' ')  ||
	  (line[m] == '\n') ||
	  (line[m] == '\t')) && m > 0) m--;
  return line.substr(n,m-n+1);
}

std::string
nameonly(std::string filename)
{
  int i = filename.rfind("/");
  int j = filename.rfind(".");
  if ( j < 0 ) j = filename.size();
  return filename.substr(i+1,j-i-1);
}
//-----------------------------------------------------------------------------
struct outputFile
{
  outputFile(std::string filename)
   : filename_(filename),
	 file_(new TFile(filename_.c_str(), "recreate")),
	 tree_(0),
	 b_weight_(0),
	 entry_(0),
	 SAVECOUNT_(50000)
  {
	file_->cd();
	hist_ = new TH1F("counts", "", 1,0,1);
	hist_->SetBit(TH1::kCanRebin);
	hist_->SetStats(0);
  }

  outputFile(std::string filename, itreestream& stream, int savecount=50000) 
   : filename_(filename),
	 file_(new TFile(filename.c_str(), "recreate")),
	 tree_(stream.tree()->CloneTree(0)),
	 b_weight_(tree_->Branch("eventWeight", &weight_, "eventWeight/D")),
	 entry_(0),
	 SAVECOUNT_(savecount)
  {
	std::cout << "events will be skimmed to file "
			  << filename_ << std::endl;
	file_->cd();
	hist_ = new TH1F("counts", "", 1,0,1);
	hist_->SetBit(TH1::kCanRebin);
	hist_->SetStats(0);
  }

  void addEvent(double weight=1)
  {
    if ( tree_ == 0 ) return;
	
    weight_ = weight;
	file_   = tree_->GetCurrentFile();
	file_->cd();
	tree_->Fill();

	entry_++;
	if ( entry_ % SAVECOUNT_ == 0 )
	  tree_->AutoSave("SaveSelf");
  }

  void count(std::string cond, int w=1)
  {
    hist_->Fill(cond.c_str(), w);
  }
  
  void close()
  {
  	std::cout << "==> histograms saved to file " << filename_ << std::endl;
    if ( tree_ != 0 )
	  {
	    std::cout << "==> events skimmed to file " << filename_ << std::endl;
	    file_ = tree_->GetCurrentFile();
	  }
	file_->cd();
	//file_->Write("", TObject::kWriteDelete);
	file_->Write();
	file_->ls();
	file_->Close();
  }

  std::string filename_;  
  TFile* file_;
  TTree* tree_;
  TH1F*  hist_;
  TBranch* b_weight_;
  double     weight_;
  int    entry_;
  int    SAVECOUNT_;
};

struct commandLine
{
  std::string progname;
  std::string filelist;
  std::string outputfilename;
};


void
decodeCommandLine(int argc, char** argv, commandLine& cl)
{
  cl.progname = std::string(argv[0]);

  // 1st (optional) argument
  if ( argc > 1 )
	cl.filelist = std::string(argv[1]);
  else
	cl.filelist = std::string("filelist.txt");

  // 2nd (optional) command line argument
  if ( argc > 2 ) 
	cl.outputfilename = std::string(argv[2]);
  else
	cl.outputfilename = cl.progname + std::string("_histograms");

  // Make sure extension is ".root"
  std::string name = cl.outputfilename;
  if ( name.substr(name.size()-5, 5) != std::string(".root") )
    cl.outputfilename += std::string(".root");
}

// Read ntuple filenames from file list

std::vector<std::string>
getFilenames(std::string filelist)
{
  std::ifstream stream(filelist.c_str());
  if ( !stream.good() ) error("unable to open file: " + filelist);

  // Get list of ntuple files to be processed

  std::vector<std::string> v;
  std::string filename;
  while ( stream >> filename )
	if ( strip(filename) != "" ) v.push_back(filename);
  return v;
}

#endif
