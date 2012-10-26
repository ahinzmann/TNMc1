#-------------------------------------------------------------------------
# Created: Wed Apr 25 17:42:36 2012 by /data1/sezen/CMSSW_5_2_5/src/Ntuples/TNMc1/python/ntuple_cfi.py
# Ntuples used by Dijet and RazorBT analyses, for 2012 data and MC
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               #analyzerName = cms.untracked.string("TNMc1analyzer.cc"),
               analyzerName = cms.untracked.string("rzrBTanalyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'edmEventHelper',
    'edmEventHelperExtra',
    'GenEventInfoProduct',
    'GenRunInfoProduct',
    'LHEEventProduct',
    'LHEEventProductHelper',
    'patJetHelper',
    'patJet0Helper',
    'patJet1Helper',
    'patJet2Helper',
    'patJet3Helper',
    'patMET',
    'patMET1',
    'patElectronHelper',
    'patMuonHelper',
    'patTau',
    'recoVertex',
    'sdouble',
    'PileupSummaryInfo',
    'recoGenParticleHelper',
    'edmTriggerResultsHelper',
    'edmTriggerResultsHelper1',
    'sint',
    'cmgBaseMET',
    'cmgBaseMET1',
    'cmgElectron',
    'cmgElectron1',
    'cmgMuon',
    'cmgMuon1',
    'cmgTau',
    'cmgTau1',
    'recoLeafCandidate',
    'hcalFilter'
    ),
               edmEventHelper =
               cms.untracked.
               vstring(
    'edmEventHelper                  info                              1',
    #---------------------------------------------------------------------
    '   bool  isRealData()',
    '   int   run()',
    '   int   event()',
    '   int   luminosityBlock()',
    '   int   bunchCrossing()',
    '   int   orbitNumber()'
    ),
               edmEventHelperExtra =
               cms.untracked.
               vstring(
    'edmEventHelperExtra             info                              1',
    #---------------------------------------------------------------------
    # custom methods
    '   double  dijet_invmass()',
    '   double  dijetCHS_invmass()',
    '   double  dijetCHSpruned_invmass()',
    '   double  wj1_pt()',
    '   double  wj1_eta()',
    '   double  wj1_phi()',
    '   double  wj1_energy()',
    '   double  wj1_mass()',
    '   double  wj1_nconst()',
    '   double  wj2_pt()',
    '   double  wj2_eta()',
    '   double  wj2_phi()',
    '   double  wj2_energy()',
    '   double  wj2_mass()',
    '   double  wj2_nconst()',
    '   double  wj1wj2_nconst()',
    '   double  wj1wj2_invmass()',
    '   double  wj1CHS_pt()',
    '   double  wj1CHS_eta()',
    '   double  wj1CHS_phi()',
    '   double  wj1CHS_energy()',
    '   double  wj1CHS_mass()',
    '   double  wj1CHS_nconst()',
    '   double  wj2CHS_pt()',
    '   double  wj2CHS_eta()',
    '   double  wj2CHS_phi()',
    '   double  wj2CHS_energy()',
    '   double  wj2CHS_mass()',
    '   double  wj2CHS_nconst()',
    '   double  wj1wj2CHS_nconst()',
    '   double  wj1wj2CHS_invmass()',
    ),
               GenEventInfoProduct =
               cms.untracked.
               vstring(
    'GenEventInfoProduct             generator                         1',
    #---------------------------------------------------------------------
    'double  weight()',
    'unsigned int  signalProcessID()',
    'double  qScale()',
    'double  alphaQCD()',
    'double  alphaQED()',
    'bool  hasPDF()',
    'bool  hasBinningValues()'
    ),
               GenRunInfoProduct =
               cms.untracked.
               vstring(
    'GenRunInfoProduct               generator                         1',
    #---------------------------------------------------------------------
    'double  filterEfficiency()',
    'double  crossSection()'
    ),
               LHEEventProduct =
               cms.untracked.
               vstring(
    'LHEEventProduct                 source                            1',
    #---------------------------------------------------------------------
    'int  hepeup().NUP',
    'int  hepeup().IDPRUP',
    'double  hepeup().XWGTUP',
    'double  hepeup().SCALUP',
    'double  hepeup().AQEDUP',
    'double  hepeup().AQCDUP'
    ),
               LHEEventProductHelper =
               cms.untracked.                          
               vstring(
    'LHEEventProductHelper            source                            1',
    #---------------------------------------------------------------------
    'double  mt1()',
    'double  mz1()',
    ),
               patJetHelper =
               cms.untracked.
               vstring(
    'patJetHelper                    selectedPatJetsCHS              200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  correctedJet("Uncorrected").energy() uncor_energy',
    'double  et()',
    'double  correctedJet("Uncorrected").et() uncor_et',
    'double  pt()',
    'double  correctedJet("Uncorrected").pt() uncor_pt',
    'double  phi()',
    'double  eta()',
    'double  rapidity()',
    'double  mass()',
    'float  jetArea()',
    'float  jetCharge()',
    #'float  jetID("PassTightJetID")',
    #'float  jetID("PassLooseJetID")',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    'float  photonEnergyFraction()',
    'float  muonEnergyFraction()',
    'int  chargedMultiplicity()',
    'int  nConstituents()',
    'double  genJet()->energy()',
    'double  genJet()->pt()',
    'double  genJet()->phi()',
    'double  genJet()->eta()',
    'double  genJet()->rapidity()',
    'int  genParton()->pdgId()',
    'int  partonFlavour()',
    #-- btagging variables -----------------------------------------------
    'float   bDiscriminator("trackCountingHighEffBJetTags") trackCountingHighEffBJetTags',
    'float   bDiscriminator("trackCountingHighPurBJetTags") trackCountingHighPurBJetTags',
    'float   bDiscriminator("jetProbabilityBJetTags") jetProbabilityBJetTags',
    'float   bDiscriminator("jetBProbabilityBJetTags") jetBProbabilityBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighEffBJetTags") simpleSecondaryVertexHighEffBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighPurBJetTags") simpleSecondaryVertexHighPurBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexBJetTags") combinedSecondaryVertexBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexMVABJetTags") combinedSecondaryVertexMVABJetTags',
    #'float   bDiscriminator("ghostTrackBJetTags") ghostTrackBJetTags',
    #'float   bDiscriminator("softElectronByIP3dBJetTags") softElectronByIP3dBJetTags',
    #'float   bDiscriminator("softElectronByPtBJetTags") softElectronByPtBJetTags',
    #'float   bDiscriminator("softMuonBJetTags") softMuonBJetTags',
    #'float   bDiscriminator("softMuonByIP3dBJetTags") softMuonByIP3dBJetTags',
    #'float   bDiscriminator("softMuonByPtBJetTags") softMuonByPtBJetTags',
    #-- pujetid variables -----------------------------------------------
    #'float puJetId_dRMean()',
    #'float puJetId_nParticles()',
    #'float puJetId_nCharged()',
    #'float puJetId_leadChFrac()',
    #'float puJetId_secondChFrac()',
    #'float puJetId_thirdChFrac()',
    #'float puJetId_fourthChFrac()',
    #'float puJetId_leadNeutFrac()',
    #'float puJetId_secondNeutFrac()',
    #'float puJetId_thirdNeutFrac()',
    #'float puJetId_fourthNeutFrac()',
    #'float puJetId_dRLeadCent()',
    #'float puJetId_dRLead2nd()',
    #'float puJetId_dRMean()',
    #'float puJetId_dR2Mean()',
    #'float puJetId_ptD()',
    #'float puJetId_ptMean()',
    #'float puJetId_ptRMS()',
    #'float puJetId_pt2A()',
    #'float puJetId_sumPt()',
    #'float puJetId_frac01()',
    #'float puJetId_frac02()',
    #'float puJetId_frac03()',
    #'float puJetId_frac04()',
    #'float puJetId_frac05()',
    #-- n-subjettiness variables ------------------------------------------
    'float tau1()',
    'float tau2()',
    'float tau3()',
    ),
               patJet0Helper =
               cms.untracked.
               vstring(
    'patJetHelper                    selectedPatJetsAK7CHS              200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  correctedJet("Uncorrected").energy() uncor_energy',
    'double  et()',
    'double  correctedJet("Uncorrected").et() uncor_et',
    'double  pt()',
    'double  correctedJet("Uncorrected").pt() uncor_pt',
    'double  phi()',
    'double  eta()',
    'double  rapidity()',
    'double  mass()',
    'float  jetArea()',
    'float  jetCharge()',
    #'float  jetID("PassTightJetID")',
    #'float  jetID("PassLooseJetID")',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    'float  photonEnergyFraction()',
    'float  muonEnergyFraction()',
    'int  chargedMultiplicity()',
    'int  nConstituents()',
    'double  genJet()->energy()',
    'double  genJet()->pt()',
    'double  genJet()->phi()',
    'double  genJet()->eta()',
    'double  genJet()->rapidity()',
    'int  genParton()->pdgId()',
    'int  partonFlavour()',
    #-- btagging variables -----------------------------------------------
    'float   bDiscriminator("trackCountingHighEffBJetTags") trackCountingHighEffBJetTags',
    'float   bDiscriminator("trackCountingHighPurBJetTags") trackCountingHighPurBJetTags',
    'float   bDiscriminator("jetProbabilityBJetTags") jetProbabilityBJetTags',
    'float   bDiscriminator("jetBProbabilityBJetTags") jetBProbabilityBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighEffBJetTags") simpleSecondaryVertexHighEffBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighPurBJetTags") simpleSecondaryVertexHighPurBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexBJetTags") combinedSecondaryVertexBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexMVABJetTags") combinedSecondaryVertexMVABJetTags',
    #'float   bDiscriminator("ghostTrackBJetTags") ghostTrackBJetTags',
    #'float   bDiscriminator("softElectronByIP3dBJetTags") softElectronByIP3dBJetTags',
    #'float   bDiscriminator("softElectronByPtBJetTags") softElectronByPtBJetTags',
    #'float   bDiscriminator("softMuonBJetTags") softMuonBJetTags',
    #'float   bDiscriminator("softMuonByIP3dBJetTags") softMuonByIP3dBJetTags',
    #'float   bDiscriminator("softMuonByPtBJetTags") softMuonByPtBJetTags',
    #-- pujetid variables -----------------------------------------------
    #'float puJetId_dRMean()',
    #'float puJetId_nParticles()',
    #'float puJetId_nCharged()',
    #'float puJetId_leadChFrac()',
    #'float puJetId_secondChFrac()',
    #'float puJetId_thirdChFrac()',
    #'float puJetId_fourthChFrac()',
    #'float puJetId_leadNeutFrac()',
    #'float puJetId_secondNeutFrac()',
    #'float puJetId_thirdNeutFrac()',
    #'float puJetId_fourthNeutFrac()',
    #'float puJetId_dRLeadCent()',
    #'float puJetId_dRLead2nd()',
    #'float puJetId_dRMean()',
    #'float puJetId_dR2Mean()',
    #'float puJetId_ptD()',
    #'float puJetId_ptMean()',
    #'float puJetId_ptRMS()',
    #'float puJetId_pt2A()',
    #'float puJetId_sumPt()',
    #'float puJetId_frac01()',
    #'float puJetId_frac02()',
    #'float puJetId_frac03()',
    #'float puJetId_frac04()',
    #'float puJetId_frac05()',
    #-- n-subjettiness variables ------------------------------------------
    'float tau1()',
    'float tau2()',
    'float tau3()',
    ),
               patJet1Helper =
               cms.untracked.
               vstring(
    'patJetHelper                    selectedPatJets                200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  correctedJet("Uncorrected").energy() uncor_energy',
    'double  et()',
    'double  correctedJet("Uncorrected").et() uncor_et',
    'double  pt()',
    'double  correctedJet("Uncorrected").pt() uncor_pt',
    'double  phi()',
    'double  eta()',
    'double  rapidity()',
    'double  mass()',
    'float  jetArea()',
    'float  jetCharge()',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    'float  photonEnergyFraction()',
    'float  muonEnergyFraction()',
    'int  chargedMultiplicity()',
    'int  nConstituents()',
    'double  genJet()->energy()',
    'double  genJet()->pt()',
    'double  genJet()->phi()',
    'double  genJet()->eta()',
    'double  genJet()->rapidity()',
    'int  genParton()->pdgId()',
    'int  partonFlavour()',
    #-- btagging variables -----------------------------------------------
    'float   bDiscriminator("trackCountingHighEffBJetTags") trackCountingHighEffBJetTags',
    'float   bDiscriminator("trackCountingHighPurBJetTags") trackCountingHighPurBJetTags',
    'float   bDiscriminator("jetProbabilityBJetTags") jetProbabilityBJetTags',
    'float   bDiscriminator("jetBProbabilityBJetTags") jetBProbabilityBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighEffBJetTags") simpleSecondaryVertexHighEffBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighPurBJetTags") simpleSecondaryVertexHighPurBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexBJetTags") combinedSecondaryVertexBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexMVABJetTags") combinedSecondaryVertexMVABJetTags',
    #'float   bDiscriminator("ghostTrackBJetTags") ghostTrackBJetTags',
    #'float   bDiscriminator("softElectronByIP3dBJetTags") softElectronByIP3dBJetTags',
    #'float   bDiscriminator("softElectronByPtBJetTags") softElectronByPtBJetTags',
    #'float   bDiscriminator("softMuonBJetTags") softMuonBJetTags',
    #'float   bDiscriminator("softMuonByIP3dBJetTags") softMuonByIP3dBJetTags',
    #'float   bDiscriminator("softMuonByPtBJetTags") softMuonByPtBJetTags',
    #-- pujetid variables -----------------------------------------------
    #'float puJetId_dRMean()',
    #'float puJetId_nParticles()',
    #'float puJetId_nCharged()',
    #'float puJetId_leadChFrac()',
    #'float puJetId_secondChFrac()',
    #'float puJetId_thirdChFrac()',
    #'float puJetId_fourthChFrac()',
    #'float puJetId_leadNeutFrac()',
    #'float puJetId_secondNeutFrac()',
    #'float puJetId_thirdNeutFrac()',
    #'float puJetId_fourthNeutFrac()',
    #'float puJetId_dRLeadCent()',
    #'float puJetId_dRLead2nd()',
    #'float puJetId_dRMean()',
    #'float puJetId_dR2Mean()',
    #'float puJetId_ptD()',
    #'float puJetId_ptMean()',
    #'float puJetId_ptRMS()',
    #'float puJetId_pt2A()',
    #'float puJetId_sumPt()',
    #'float puJetId_frac01()',
    #'float puJetId_frac02()',
    #'float puJetId_frac03()',
    #'float puJetId_frac04()',
    #'float puJetId_frac05()',
    #-- n-subjettiness variables ------------------------------------------
    'float tau1()',
    'float tau2()',
    'float tau3()',
    ),
               patJet2Helper =
               cms.untracked.
               vstring(
    'patJetHelper                      selectedPatJetsCHSpruned      200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  correctedJet("Uncorrected").energy() uncor_energy',
    'double  et()',
    'double  correctedJet("Uncorrected").et() uncor_et',
    'double  pt()',
    'double  correctedJet("Uncorrected").pt() uncor_pt',
    'double  phi()',
    'double  eta()',
    'double  rapidity()',
    'double  mass()',
    'float  jetArea()',
    'float  jetCharge()',
    # The following don't work
    #'float  chargedHadronEnergyFraction()',
    #'float  neutralHadronEnergyFraction()',
    #'float  chargedEmEnergyFraction()',
    #'float  neutralEmEnergyFraction()',
    #'float  photonEnergyFraction()',
    #'float  muonEnergyFraction()',
    #'int  chargedMultiplicity()',
    'int  nConstituents()',
    'double  genJet()->energy()',
    'double  genJet()->pt()',
    'double  genJet()->phi()',
    'double  genJet()->eta()',
    'double  genJet()->rapidity()',
    'int  genParton()->pdgId()',
    'int  partonFlavour()',
    #-- btagging variables -----------------------------------------------
    'float   bDiscriminator("trackCountingHighEffBJetTags") trackCountingHighEffBJetTags',
    'float   bDiscriminator("trackCountingHighPurBJetTags") trackCountingHighPurBJetTags',
    'float   bDiscriminator("jetProbabilityBJetTags") jetProbabilityBJetTags',
    'float   bDiscriminator("jetBProbabilityBJetTags") jetBProbabilityBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighEffBJetTags") simpleSecondaryVertexHighEffBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighPurBJetTags") simpleSecondaryVertexHighPurBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexBJetTags") combinedSecondaryVertexBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexMVABJetTags") combinedSecondaryVertexMVABJetTags',
    #'float   bDiscriminator("ghostTrackBJetTags") ghostTrackBJetTags',
    #'float   bDiscriminator("softElectronByIP3dBJetTags") softElectronByIP3dBJetTags',
    #'float   bDiscriminator("softElectronByPtBJetTags") softElectronByPtBJetTags',
    #'float   bDiscriminator("softMuonBJetTags") softMuonBJetTags',
    #'float   bDiscriminator("softMuonByIP3dBJetTags") softMuonByIP3dBJetTags',
    #'float   bDiscriminator("softMuonByPtBJetTags") softMuonByPtBJetTags',
    # Substructure-related:
    'size_t  numberOfDaughters()',
    'double  daughter(0)->energy()',
    'double  daughter(0)->pt()',
    'double  daughter(0)->eta()',
    'double  daughter(0)->rapidity()',
    'double  daughter(0)->phi()',
    'double  daughter(0)->mass()',
    'float  daughter(0)->chargedHadronEnergyFraction()',
    'float  daughter(0)->neutralHadronEnergyFraction()',
    'float  daughter(0)->chargedEmEnergyFraction()',
    'float  daughter(0)->neutralEmEnergyFraction()',
    'float  daughter(0)->photonEnergyFraction()',
    'float  daughter(0)->muonEnergyFraction()',
    'int  daughter(0)->chargedMultiplicity()',
    'int  daughter(0)->nConstituents()',
    'double  daughter(1)->energy()',
    'double  daughter(1)->pt()',
    'double  daughter(1)->eta()',
    'double  daughter(1)->rapidity()',
    'double  daughter(1)->phi()',
    'double  daughter(1)->mass()',
    'float  daughter(1)->chargedHadronEnergyFraction()',
    'float  daughter(1)->neutralHadronEnergyFraction()',
    'float  daughter(1)->chargedEmEnergyFraction()',
    'float  daughter(1)->neutralEmEnergyFraction()',
    'float  daughter(1)->photonEnergyFraction()',
    'float  daughter(1)->muonEnergyFraction()',
    'int  daughter(1)->chargedMultiplicity()',
    'int  daughter(1)->nConstituents()',
    #-- pujetid variables -----------------------------------------------
    #'float daughter_0_puJetId_dRMean()',
    #'float daughter_0_puJetId_nParticles()',
    #'float daughter_0_puJetId_nCharged()',
    #'float daughter_0_puJetId_dRLeadCent()',
    #'float daughter_0_puJetId_dRLead2nd()',
    #'float daughter_0_puJetId_dRMean()',
    #'float daughter_0_puJetId_dR2Mean()',
    #'float daughter_0_puJetId_ptD()',
    #'float daughter_0_puJetId_ptMean()',
    #'float daughter_0_puJetId_ptRMS()',
    #'float daughter_0_puJetId_pt2A()',
    #'float daughter_0_puJetId_sumPt()',
    #'float daughter_0_puJetId_frac01()',
    #'float daughter_0_puJetId_frac02()',
    #'float daughter_0_puJetId_frac03()',
    #'float daughter_0_puJetId_frac04()',
    #'float daughter_0_puJetId_frac05()',
    #'float daughter_1_puJetId_dRMean()',
    #'float daughter_1_puJetId_nParticles()',
    #'float daughter_1_puJetId_nCharged()',
    #'float daughter_1_puJetId_dRLeadCent()',
    #'float daughter_1_puJetId_dRLead2nd()',
    #'float daughter_1_puJetId_dRMean()',
    #'float daughter_1_puJetId_dR2Mean()',
    #'float daughter_1_puJetId_ptD()',
    #'float daughter_1_puJetId_ptMean()',
    #'float daughter_1_puJetId_ptRMS()',
    #'float daughter_1_puJetId_pt2A()',
    #'float daughter_1_puJetId_sumPt()',
    #'float daughter_1_puJetId_frac01()',
    #'float daughter_1_puJetId_frac02()',
    #'float daughter_1_puJetId_frac03()',
    #'float daughter_1_puJetId_frac04()',
    #'float daughter_1_puJetId_frac05()',
    #-- n-subjettiness variables ------------------------------------------
    'float tau1()',
    'float tau2()',
    'float tau3()',
    #-- jet charge --------------------------------------------------------
    'float daughter_0_jetCharge()',
    'float daughter_1_jetCharge()',
    ),
               patJet3Helper =
               cms.untracked.
               vstring(
    'patJetHelper                      selectedPatJetsAK7CHSpruned      200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  correctedJet("Uncorrected").energy() uncor_energy',
    'double  et()',
    'double  correctedJet("Uncorrected").et() uncor_et',
    'double  pt()',
    'double  correctedJet("Uncorrected").pt() uncor_pt',
    'double  phi()',
    'double  eta()',
    'double  rapidity()',
    'double  mass()',
    'float  jetArea()',
    'float  jetCharge()',
    # The following don't work
    #'float  chargedHadronEnergyFraction()',
    #'float  neutralHadronEnergyFraction()',
    #'float  chargedEmEnergyFraction()',
    #'float  neutralEmEnergyFraction()',
    #'float  photonEnergyFraction()',
    #'float  muonEnergyFraction()',
    #'int  chargedMultiplicity()',
    'int  nConstituents()',
    'double  genJet()->energy()',
    'double  genJet()->pt()',
    'double  genJet()->phi()',
    'double  genJet()->eta()',
    'double  genJet()->rapidity()',
    'int  genParton()->pdgId()',
    'int  partonFlavour()',
    #-- btagging variables -----------------------------------------------
    'float   bDiscriminator("trackCountingHighEffBJetTags") trackCountingHighEffBJetTags',
    'float   bDiscriminator("trackCountingHighPurBJetTags") trackCountingHighPurBJetTags',
    'float   bDiscriminator("jetProbabilityBJetTags") jetProbabilityBJetTags',
    'float   bDiscriminator("jetBProbabilityBJetTags") jetBProbabilityBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighEffBJetTags") simpleSecondaryVertexHighEffBJetTags',
    'float   bDiscriminator("simpleSecondaryVertexHighPurBJetTags") simpleSecondaryVertexHighPurBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexBJetTags") combinedSecondaryVertexBJetTags',
    'float   bDiscriminator("combinedSecondaryVertexMVABJetTags") combinedSecondaryVertexMVABJetTags',
    #'float   bDiscriminator("ghostTrackBJetTags") ghostTrackBJetTags',
    #'float   bDiscriminator("softElectronByIP3dBJetTags") softElectronByIP3dBJetTags',
    #'float   bDiscriminator("softElectronByPtBJetTags") softElectronByPtBJetTags',
    #'float   bDiscriminator("softMuonBJetTags") softMuonBJetTags',
    #'float   bDiscriminator("softMuonByIP3dBJetTags") softMuonByIP3dBJetTags',
    #'float   bDiscriminator("softMuonByPtBJetTags") softMuonByPtBJetTags',
    # Substructure-related:
    'size_t  numberOfDaughters()',
    'double  daughter(0)->energy()',
    'double  daughter(0)->pt()',
    'double  daughter(0)->eta()',
    'double  daughter(0)->rapidity()',
    'double  daughter(0)->phi()',
    'double  daughter(0)->mass()',
    'float  daughter(0)->chargedHadronEnergyFraction()',
    'float  daughter(0)->neutralHadronEnergyFraction()',
    'float  daughter(0)->chargedEmEnergyFraction()',
    'float  daughter(0)->neutralEmEnergyFraction()',
    'float  daughter(0)->photonEnergyFraction()',
    'float  daughter(0)->muonEnergyFraction()',
    'int  daughter(0)->chargedMultiplicity()',
    'int  daughter(0)->nConstituents()',
    'double  daughter(1)->energy()',
    'double  daughter(1)->pt()',
    'double  daughter(1)->eta()',
    'double  daughter(1)->rapidity()',
    'double  daughter(1)->phi()',
    'double  daughter(1)->mass()',
    'float  daughter(1)->chargedHadronEnergyFraction()',
    'float  daughter(1)->neutralHadronEnergyFraction()',
    'float  daughter(1)->chargedEmEnergyFraction()',
    'float  daughter(1)->neutralEmEnergyFraction()',
    'float  daughter(1)->photonEnergyFraction()',
    'float  daughter(1)->muonEnergyFraction()',
    'int  daughter(1)->chargedMultiplicity()',
    'int  daughter(1)->nConstituents()',
    #-- pujetid variables -----------------------------------------------
    #'float daughter_0_puJetId_dRMean()',
    #'float daughter_0_puJetId_nParticles()',
    #'float daughter_0_puJetId_nCharged()',
    #'float daughter_0_puJetId_dRLeadCent()',
    #'float daughter_0_puJetId_dRLead2nd()',
    #'float daughter_0_puJetId_dRMean()',
    #'float daughter_0_puJetId_dR2Mean()',
    #'float daughter_0_puJetId_ptD()',
    #'float daughter_0_puJetId_ptMean()',
    #'float daughter_0_puJetId_ptRMS()',
    #'float daughter_0_puJetId_pt2A()',
    #'float daughter_0_puJetId_sumPt()',
    #'float daughter_0_puJetId_frac01()',
    #'float daughter_0_puJetId_frac02()',
    #'float daughter_0_puJetId_frac03()',
    #'float daughter_0_puJetId_frac04()',
    #'float daughter_0_puJetId_frac05()',
    #'float daughter_1_puJetId_dRMean()',
    #'float daughter_1_puJetId_nParticles()',
    #'float daughter_1_puJetId_nCharged()',
    #'float daughter_1_puJetId_dRLeadCent()',
    #'float daughter_1_puJetId_dRLead2nd()',
    #'float daughter_1_puJetId_dRMean()',
    #'float daughter_1_puJetId_dR2Mean()',
    #'float daughter_1_puJetId_ptD()',
    #'float daughter_1_puJetId_ptMean()',
    #'float daughter_1_puJetId_ptRMS()',
    #'float daughter_1_puJetId_pt2A()',
    #'float daughter_1_puJetId_sumPt()',
    #'float daughter_1_puJetId_frac01()',
    #'float daughter_1_puJetId_frac02()',
    #'float daughter_1_puJetId_frac03()',
    #'float daughter_1_puJetId_frac04()',
    #'float daughter_1_puJetId_frac05()',
    #-- n-subjettiness variables ------------------------------------------
    'float tau1()',
    'float tau2()',
    'float tau3()',
    #-- jet charge --------------------------------------------------------
    'float daughter_0_jetCharge()',
    'float daughter_1_jetCharge()',
    ),
               patMET =
               cms.untracked.
               vstring(
    'patMET                          patMETs                         200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  sumEt()',
    'double  mEtSig()',
    'double  significance()'
    ),
               patMET1 =                               
               cms.untracked.
               vstring(
    'patMET                          patMETsRaw                      200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  sumEt()',
    'double  mEtSig()',
    'double  significance()'
    ),
               patElectronHelper =
               cms.untracked.
               vstring(
    'patElectronHelper            patElectronsWithTrigger            200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'int  charge()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
    'bool  isEB()',
    'bool  isEE()',
    'float  scSigmaIEtaIEta()',
    'float  hadronicOverEm()',
    'double  superCluster()->energy()',
    'unsigned short  gsfTrack()->trackerExpectedHitsInner().numberOfHits()',
    'float  electronID("simpleEleId80relIso") simpleEleId80relIso',
    'float  electronID("simpleEleId95relIso") simpleEleId95relIso',
    'float   trackIso()',
    'float   ecalIso()',
    'float   hcalIso()',
    'float   caloIso()',
    # custom methods:
    'double  dxywrtPV()',
    'double  dzwrtPV()',
    ),
               patMuonHelper =
               cms.untracked.
               vstring(
    'patMuonHelper            patMuonsWithTrigger                    200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'int  charge()',
    #'bool  isGood(std::string)',
    'float  muonID("TMOneStationTight") TMOneStationTight',
    'bool  isGlobalMuon()',
    'bool  isTrackerMuon()',
    'bool  isPFMuon()',
    'unsigned short  track()->hitPattern().trackerLayersWithMeasurement()',
    'unsigned short  innerTrack()->hitPattern().pixelLayersWithMeasurement()',
    'double  innerTrack()->normalizedChi2()',
    'double  globalTrack()->normalizedChi2()',
    'unsigned short  globalTrack()->hitPattern().numberOfValidMuonHits()',
    'int  numberOfMatchedStations()',
    'double dB()',
    'unsigned short  innerTrack()->hitPattern().numberOfValidPixelHits()',
    'float  pfIsolationR04().sumChargedHadronPt',
    'float  pfIsolationR04().sumChargedParticlePt',
    'float  pfIsolationR04().sumNeutralHadronEt',
    'float  pfIsolationR04().sumPhotonEt',
    'float  pfIsolationR04().sumNeutralHadronEtHighThreshold',
    'float  pfIsolationR04().sumPhotonEtHighThreshold',
    'float  pfIsolationR04().sumPUPt',
    # custom methods
    'double  dxywrtPV()',
    'double  dzwrtPV()',
    ),
               patTau =
               cms.untracked.
               vstring(
    'patTau                          selectedPatTaus                 200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  tauID("byLooseCombinedIsolationDeltaBetaCorr") byLooseCombinedIsolationDeltaBetaCorr',
    'float  tauID("byMediumCombinedIsolationDeltaBetaCorr") byMediumCombinedIsolationDeltaBetaCorr',
    'float   trackIso()',
    'float   ecalIso()',
    'float   hcalIso()',
    'float   caloIso()',
    ),
               recoVertex =
               cms.untracked.
               vstring(
    'recoVertex                      offlinePrimaryVertices          2',
    #---------------------------------------------------------------------
    'bool  isFake()',
    'double  chi2()',
    'double  ndof()',
    'double  x()',
    'double  y()',
    'double  z()',
    'double  xError()',
    'double  yError()',
    'double  zError()',
    'double  position().Rho()'                         
    ),
               sdouble =
               cms.untracked.
               vstring(
    'sdouble                         kt6PFJets_rho                     1',
    #---------------------------------------------------------------------
    'double value()'
    ),
               recoGenParticleHelper =
               cms.untracked. 
               vstring(
    'recoGenParticleHelper           genParticles                    200',
    #---------------------------------------------------------------------
    '    int   firstMother()',
    '    int   lastMother()',
    '    int   firstDaughter()',
    '    int   lastDaughter()',
    '    int   charge()',
    '    int   pdgId()',
    '    int   status()',
    ' double   pt()',
    ' double   eta()',
    ' double   phi()',
    ' double   mass()'
    ),
               PileupSummaryInfo =
               cms.untracked.
               vstring(
    'PileupSummaryInfo               addPileupInfo                   200',
    #---------------------------------------------------------------------
    'int  getPU_NumInteractions()',
    'int  getBunchCrossing()',
    'float  getTrueNumInteractions()'
    ),
               edmTriggerResultsHelper1 =
               cms.untracked.
               vstring(
    #"edmTriggerResultsHelper          TriggerResults                    1",
    # If this doesn't work, try to specify the label as shown below:
    "edmTriggerResultsHelper          TriggerResults::PAT               1",
    #----------------------------------------------------------------------
    '   int   value("totalKinematicsFilterPath")  totalKinematicsFilterPath',
    '   int   value("EcalDeadCellBoundaryEnergyFilterPath")  EcalDeadCellBoundaryEnergyFilterPath',
    '   int   value("simpleDRfilterPath")  simpleDRfilterPath',
    '   int   value("EcalDeadCellTriggerPrimitiveFilterPath")  EcalDeadCellTriggerPrimitiveFilterPath',
    '   int   value("greedyMuonPFCandidateFilterPath")  greedyMuonPFCandidateFilterPath',
    '   int   value("hcalLaserEventFilterPath")  hcalLaserEventFilterPath',
    '   int   value("inconsistentMuonPFCandidateFilterPath")  inconsistentMuonPFCandidateFilterPath',
    '   int   value("trackingFailureFilterPath")  trackingFailureFilterPath',
    '   int   value("CSCTightHaloFilterPath")  CSCTightHaloFilterPath',
    '   int   value("HBHENoiseFilterPath")  HBHENoiseFilterPath',
    '   int   value("primaryVertexFilterPath")  primaryVertexFilterPath',
    '   int   value("noscrapingFilterPath")  noscrapingFilterPath',
    '   int   value("metNoiseCleaningPath")  metNoiseCleaningPath',
    ),
               edmTriggerResultsHelper =
               cms.untracked.
               vstring( 
    #"edmTriggerResultsHelper          TriggerResults                    1",
    # If this doesn't work, try to specify the label as shown below:
    "edmTriggerResultsHelper          TriggerResults::HLT               1",
    #---------------------------------------------------------------------
    # HLT_PFJet
    '   int   value("HLT_PFJet320_v3...11")',
    '   int   prescale("HLT_PFJet320_v3...11")',
    '   int   value("HLT_PFJet400_v3...11")',
    '   int   prescale("HLT_PFJet400_v3...11")',
    # HLT_HT
    '   int   value("HLT_HT450_v1...9")',
    '   int   prescale("HLT_HT450_v1...9")',
    '   int   value("HLT_HT500_v1...9")',
    '   int   prescale("HLT_HT500_v1...9")',
    '   int   value("HLT_HT550_v1...9")',
    '   int   prescale("HLT_HT550_v1...9")',
    '   int   value("HLT_HT650_v1...9")',
    '   int   prescale("HLT_HT650_v1...9")',
    '   int   value("HLT_HT750_v1...9")',
    '   int   prescale("HLT_HT750_v1...9")',
    # HLT_PFHT
    '   int   value("HLT_PFHT650_v5...11")',
    '   int   prescale("HLT_PFHT650_v5...11")',
    '   int   value("HLT_PFHT700_v5...11")',
    '   int   prescale("HLT_PFHT700_v5...11")',
    '   int   value("HLT_PFHT750_v5...11")',
    '   int   prescale("HLT_PFHT750_v5...11")',
    # HLT_PFNoPUHT
    '   int   value("HLT_PFNoPUHT650_v1...6")',
    '   int   prescale("HLT_PFNoPUHT650_v1...6")',
    '   int   value("HLT_PFNoPUHT700_v1...6")',
    '   int   prescale("HLT_PFNoPUHT700_v1...6")',
    '   int   value("HLT_PFNoPUHT750_v1...6")',
    '   int   prescale("HLT_PFNoPUHT750_v1...6")',
    # HLT_FatDiPFJetMass_DR_Deta
    '   int   value("HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2...12")',
    '   int   prescale("HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v2...12")',
    # HLT_DiPFJetAve
    '   int   value("HLT_DiPFJetAve320_v2...12")',
    '   int   prescale("HLT_DiPFJetAve320_v2...12")',
    '   int   value("HLT_DiPFJetAve400_v2...12")',
    '   int   prescale("HLT_DiPFJetAve400_v2...12")',
    ),
               sint =
               cms.untracked.
               vstring(
    'sint                            simpleGenInfo                     1',
    #---------------------------------------------------------------------
    'int value()'
    ),
               cmgBaseMET =
               cms.untracked.
               vstring(
    'cmgBaseMET                      razorMJMetDown                  200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',                                 
    'double  pt()',
    'double  phi()',
    'double  sumEt()'
    ),
               cmgBaseMET1 =
               cms.untracked.
               vstring(
    'cmgBaseMET                      razorMJMetUp                    200',
    #---------------------------------------------------------------------
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  sumEt()'
    ),
               cmgElectron =
               cms.untracked.
               vstring(
    'cmgElectron                     razorMJElectronLoose            200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()'                                    
    ),
               cmgElectron1 =
               cms.untracked.
               vstring(
    'cmgElectron                     razorMJElectronTight            200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               cmgMuon =
               cms.untracked.
               vstring(
    'cmgMuon                         razorMJMuonLoose                200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               cmgMuon1 =
               cms.untracked.
               vstring(
    'cmgMuon                         razorMJMuonTight                200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               cmgTau =
               cms.untracked.
               vstring(
    'cmgTau                          razorMJTauLoose                 200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  tauID("byLooseCombinedIsolationDeltaBetaCorr") byLooseCombinedIsolationDeltaBetaCorr'
    ),
               cmgTau1 =
               cms.untracked.
               vstring(
    'cmgTau                          razorMJTauTight                 200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  tauID("byTightCombinedIsolationDeltaBetaCorr") byTightCombinedIsolationDeltaBetaCorr'
    ),
               recoLeafCandidate =
               cms.untracked.
               vstring(
    'recoLeafCandidate               topGenInfo                      200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  energy()',
    'double  et()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               hcalFilter =
               cms.untracked.
               vstring(
    'sint                             hcallasereventfilter2012         1',
    #---------------------------------------------------------------------
    'int value()'
    )
               )
