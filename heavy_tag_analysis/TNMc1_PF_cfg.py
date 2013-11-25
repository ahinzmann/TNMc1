#$Revision: 1.29 $
import FWCore.ParameterSet.Config as cms

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
# See TheNtupleMaker twiki for a brief explanation
process.MessageLogger.destinations = cms.untracked.vstring("cerr")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.cerr.default.limit = 5

# This is required in order to configure HLTConfigProducer
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

# Run on MC or data

runOnMC = True
runPATCMG = True
runPF = True
runNoCHS = False
runCaloJets = False
recalibrateCMGJets = False
runAK7jets = False
runPrunedAK7jets = False
runCA8jets = True
runAK5genjets = True
runPrunedAK5jets = True
runQJets = False
runOnVVtuples = False
runOnCMGp = False
writePatTuple = True
runTrimmedCA8jets = True

if not runOnMC:
   runAK5genjets=False

# Input file

dataset_user = 'cmgtools' 
#dataset_name = '/SingleMu/Run2012D-22Jan2013-v1/AOD/CMGPF_V5_16_0'
dataset_name = '/RSGravitonToWW_kMpl01_M-1000_Tune23_8TeV-herwigpp/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_13_0'
#dataset_name = '/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_13_0'
#dataset_name = '/QCD_Pt-15to3000_Tune4C_Flat_8TeV_pythia8/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0'
#dataset_name = '/MultiJet/Run2012A-13Jul2012-v1/AOD/PAT_CMG_V5_12_0'
if runOnCMGp:
    dataset_files = 'cmgTuple.*root'
else:
    dataset_files = 'patTuple.*root'

if runPATCMG:
    dataset_user = 'cmgtools_group' 
    dataset_name = '/RSGravitonToWW_kMpl01_M-3000_Tune23_8TeV-herwigpp/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B'
    #dataset_user = 'CMS' 
    #dataset_name = '/JetHT/Run2012D-22Jan2013-v1/AOD'
    dataset_files = '.*root'

from CMGTools.Production.datasetToSource import *
process.source = datasetToSource(
    dataset_user,
    dataset_name,
    dataset_files,
    )

process.source.fileNames=cms.untracked.vstring('file:///afs/cern.ch/user/h/hinzmann/workspace/RSGravitonToWW_kMpl01_M-2500_Tune23_8TeV-herwigpp-Summer12_DR53X-PU_S10_START53_V7A-v1-A25D0992-00C1-E211-8D70-E0CB4E29C4D8.root')
if runPF:
    #process.source.fileNames=cms.untracked.vstring('file:///tmp/hinzmann/reco_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU_v2.root')
    #process.source.fileNames=cms.untracked.vstring('file:///tmp/hinzmann/reco_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU_v2_noHCALcluster.root')
    process.source.fileNames=cms.untracked.vstring('file:///tmp/hinzmann/reco_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU_v2_50PU.root')

if runOnVVtuples:
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_WJetsPt100_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_WJetsPt70To100_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_WJetsPt50To70_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_WW_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_TTBAR_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_RSG_WW_lvjj_c0p05_M1000_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_BulkG_WW_lvjj_c0p2_M1000_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_BulkG_WW_lvjj_c0p2_M1500_cff")
    #process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_BulkG_WW_lvjj_c0p2_M2000_cff")
    process.load("ExoDiBosonResonances/EDBRCommon/datasets/summer12_BulkG_WW_lvjj_c0p2_M2500_cff")
    runAK7jets=False
    runPrunedAK7jets=False
    runCA8jets=False

print 'input:', process.source.fileNames

# set up JSON ---------------------------------------------------------------

if runOnMC==False:
    from CMGTools.Common.Tools.applyJSON_cff import *
    # Run2012A+B 13Jul2012ReReco
    #json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt'
    # Run2012A 06Aug2012ReReco
    #json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190782-190949_8TeV_06Aug2012ReReco_Collisions12_JSON.txt'
    # Run2012C v1 Aug24ReReco
    #json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_198022-198523_8TeV_24Aug2012ReReco_Collisions12_JSON.txt'
    # Run2012C v1 Dec11ReReco
    #json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_201191-201191_8TeV_11Dec2012ReReco-recover_Collisions12_JSON.txt'
    # Run2012C v2 and Run2012D
    #json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
    # Jan22ReReco
    json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'
    print 'json:', json
    applyJSON(process, json )

print 'runOnMC:', runOnMC

process.load("Ntuples.TNMc1.ntuple_cfi")

if runOnVVtuples:
    process.demo.patJetHelperAK5[0]=process.demo.patJetHelperAK5[0].replace("patJetsWithVar","selectedPatJets")
    process.demo.patJetHelperAK5CHS[0]=process.demo.patJetHelperAK5CHS[0].replace("patJetsWithVarCHS","selectedPatJetsCHS")
    process.demo.buffers.remove("edmEventHelperExtra")

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X
#process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

GT = None
if runOnMC:
#    GT = 'START53_V15::All' # for Summer12 MC
    GT = 'START53_V23::All' # for Summer12 MC with ReReco data
else:
#    GT = 'GR_P_V39_AN3::All' # for Moriond data
    GT = 'FT_53_V21_AN4::All' # for Jan22ReReco data
process.GlobalTag.globaltag = GT

#### AK5 CHS jets
process.load('CMGTools.Common.PAT.PATCMG_cff')

if runOnMC is False:
    # removing MC stuff
    print 'removing MC stuff, as we are running on Data'

    process.patElectrons.addGenMatch = False
    process.makePatElectrons.remove( process.electronMatch )
    
    process.patMuons.addGenMatch = False
    process.makePatMuons.remove( process.muonMatch )
    
    process.PATCMGSequence.remove( process.PATCMGGenSequence )
    process.PATCMGJetSequence.remove( process.jetMCSequence )
    process.PATCMGJetSequence.remove( process.patJetFlavourId )
    process.patJets.addGenJetMatch = False
    process.patJets.addGenPartonMatch = False

    process.PATCMGTauSequence.remove( process.tauGenJets )
    process.PATCMGTauSequence.remove( process.tauGenJetsSelectorAllHadrons )
    process.PATCMGTauSequence.remove( process.tauGenJetMatch )
    process.PATCMGTauSequence.remove( process.tauMatch )
    process.patTaus.addGenJetMatch = False
    process.patTaus.addGenMatch = False

    process.patMETs.addGenMET = False 
    process.patMETsRaw.addGenMET = False 

    # adding L2L3Residual corrections
    process.patJetCorrFactors.levels.append('L2L3Residual')

#### AK5 CHS

print 'cloning the jet sequence to build PU chs jets'

from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet
process.PATCMGJetCHSSequence = cloneProcessingSnippet(process, process.PATCMGJetSequence, 'CHS')
process.PATCMGJetCHSSequence.insert( 0, process.ak5PFJetsCHS )
from CMGTools.Common.Tools.visitorUtils import replaceSrc
replaceSrc( process.PATCMGJetCHSSequence, 'ak5PFJets', 'ak5PFJetsCHS')
replaceSrc( process.PATCMGJetCHSSequence, 'particleFlow', 'pfNoPileUp')
process.patJetCorrFactorsCHS.payload = 'AK5PFchs'
process.selectedPatJetsCHS.cut = 'pt()>10'

#### Adding AK5 pruned jets

process.load("Ntuples.TNMc1.PAT_ak5jets_cff")
if not runPATCMG:
    process.patJetsAK5CHSpruned.addBTagInfo=False
    process.patJetsAK5CHSpruned.addDiscriminators=False
    process.PATCMGJetSequenceAK5CHSpruned.remove(process.btaggingAK5CHSpruned)
    process.patJetsAK5CHSprunedSubjets.addBTagInfo=False
    process.patJetsAK5CHSprunedSubjets.addDiscriminators=False
    process.PATCMGJetSequenceAK5CHSpruned.remove(process.btaggingAK5CHSprunedSubjets)
if not runOnMC:
    process.PATCMGJetSequenceAK5CHSpruned.remove( process.jetMCSequenceAK5CHSpruned )
    process.patJetsAK5CHSpruned.addGenJetMatch = False
    process.patJetsAK5CHSpruned.addGenPartonMatch = False
    process.patJetCorrFactorsAK5CHSpruned.levels.append('L2L3Residual')

#### Adding AK7 jets

process.load("Ntuples.TNMc1.PAT_ak7jets_cff")

if not runOnMC:
    process.PATCMGJetSequenceAK7CHS.remove( process.jetMCSequenceAK7CHS )
    process.patJetsAK7CHS.addGenJetMatch = False
    process.patJetsAK7CHS.addGenPartonMatch = False
    process.patJetCorrFactorsAK7CHS.levels.append('L2L3Residual')

#### Adding AK7 pruned jets

process.load("CMGTools.Common.PAT.jetSubstructure_cff")
#process.PATCMGSequence.remove(process.PATCMGJetSequenceCHSpruned) # don't produce the AK5 pruned collections
process.jetMCSequenceAK7CHSpruned.remove(process.ak7GenJetsNoNu) # don't cluster the ak7GenJetsNoNu twice
process.selectedPatJetsAK7CHSpruned.cut = 'pt()>30'

if not runOnMC:
    process.PATCMGJetSequenceAK7CHSpruned.remove( process.jetMCSequenceAK7CHSpruned )
    process.patJetsAK7CHSpruned.addGenJetMatch = False
    process.patJetsAK7CHSpruned.addGenPartonMatch = False
    process.patJetCorrFactorsAK7CHSpruned.levels.append('L2L3Residual')

#### Adding CA8 jets and CA8 pruned jets

process.load("Ntuples.TNMc1.PAT_ca8jets_cff")
if not runPATCMG:
    process.patJetsCA8CHS.addBTagInfo=False
    process.patJetsCA8CHS.addDiscriminators=False
    process.PATCMGJetSequenceCA8CHS.remove(process.btaggingCA8CHS)
    process.patJetsCA8CHSpruned.addBTagInfo=False
    process.patJetsCA8CHSpruned.addDiscriminators=False
    process.PATCMGJetSequenceCA8CHSpruned.remove(process.btaggingCA8CHSpruned)
    process.patJetsCA8CHSprunedSubjets.addBTagInfo=False
    process.patJetsCA8CHSprunedSubjets.addDiscriminators=False
    process.PATCMGJetSequenceCA8CHSpruned.remove(process.btaggingCA8CHSprunedSubjets)
    process.patJetsCA8CHStrimmed.addBTagInfo=False
    process.patJetsCA8CHStrimmed.addDiscriminators=False
    process.PATCMGJetSequenceCA8CHStrimmed.remove(process.btaggingCA8CHStrimmed)
if not runOnMC:
    process.PATCMGJetSequenceCA8CHS.remove( process.jetMCSequenceCA8CHS )
    process.patJetsCA8CHS.addGenJetMatch = False
    process.patJetsCA8CHS.addGenPartonMatch = False
    process.patJetCorrFactorsCA8CHS.levels.append('L2L3Residual')
    process.PATCMGJetSequenceCA8CHSpruned.remove( process.jetMCSequenceCA8CHSpruned )
    process.patJetsCA8CHSpruned.addGenJetMatch = False
    process.patJetsCA8CHSpruned.addGenPartonMatch = False
    process.patJetCorrFactorsCA8CHSpruned.levels.append('L2L3Residual')
    process.PATCMGJetSequenceCA8CHStrimmed.remove( process.jetMCSequenceCA8CHStrimmed )
    process.patJetsCA8CHStrimmed.addGenJetMatch = False
    process.patJetsCA8CHStrimmed.addGenPartonMatch = False
    process.patJetCorrFactorsCA8CHStrimmed.levels.append('L2L3Residual')

#### Adding Nsubjetiness

process.selectedPatJetsAK7CHSwithNsub = cms.EDProducer("NjettinessAdder",
                              src=cms.InputTag("selectedPatJetsAK7CHS"),
                              cone=cms.double(0.7)
                              )

#### Adding QJets

process.selectedPatJetsAK7CHSwithQjets = cms.EDProducer("QjetsAdder",
			   src=cms.InputTag("selectedPatJetsAK7CHSwithNsub"),
			   zcut=cms.double(0.1),
			   dcutfctr=cms.double(0.5),
			   expmin=cms.double(0.0),
			   expmax=cms.double(0.0),
			   rigidity=cms.double(0.1),
			   ntrial = cms.int32(50),
			   cutoff=cms.double(200.0),
			   jetRad= cms.double(0.7),
			   jetAlgo=cms.string("AK"),
			   preclustering = cms.int32(30),
			  )
if not runQJets:
    process.selectedPatJetsAK7CHSwithQjets.cutoff=100000.0
    process.selectedPatJetsCA8CHSwithQjets.cutoff=100000.0
else:    
    process.selectedPatJetsAK7CHSwithQjets.cutoff=400.0
    process.selectedPatJetsCA8CHSwithQjets.cutoff=400.0

######ADD PU JET ID

#from  CMGTools.External.pujetidsequence_cff import puJetId
#process.puJetIdAK7CHS = puJetId.clone(
#    jets ='selectedPatJetsAK7CHSwithQjets',
#    jec = 'AK7chs'
#    )
#process.PATCMGSequence += process.puJetIdAK7CHS
#process.puJetIdCA8CHS = puJetId.clone(
#    jets ='selectedPatJetsCA8CHSwithQjets',
#    jec = 'AK7chs'
#    )
#process.PATCMGSequence += process.puJetIdCA8CHS

###REMOVE CHS

if runNoCHS:
    process.ca8PFJetsCHS.src = cms.InputTag("particleFlow")
    process.ca8PFJetsCHSpruned.src = cms.InputTag("particleFlow")
    process.ca8PFJetsCHStrimmed.src = cms.InputTag("particleFlow")

###RUN CALO jets

if runCaloJets:
    process.ca8PFJetsCHS.src = cms.InputTag("towerMaker")
    process.ca8PFJetsCHS.srcPVs = cms.InputTag("offlinePrimaryVertices")
    process.ca8PFJetsCHS.jetType = cms.string("CaloJet")
    process.ca8PFJetsCHS.inputEtMin = cms.double(0.3)
    process.ca8PFJetsCHS.doPVCorrection = cms.bool(True)
    process.ca8PFJetsCHSpruned.src = cms.InputTag("towerMaker")
    process.ca8PFJetsCHSpruned.srcPVs = cms.InputTag("offlinePrimaryVertices")
    process.ca8PFJetsCHSpruned.jetType = cms.string("CaloJet")
    process.ca8PFJetsCHSpruned.inputEtMin = cms.double(0.3)
    process.ca8PFJetsCHSpruned.doPVCorrection = cms.bool(True)
    process.ca8PFJetsCHStrimmed.src = cms.InputTag("towerMaker")
    process.ca8PFJetsCHStrimmed.srcPVs = cms.InputTag("offlinePrimaryVertices")
    process.ca8PFJetsCHStrimmed.jetType = cms.string("CaloJet")
    process.ca8PFJetsCHStrimmed.inputEtMin = cms.double(0.3)
    process.ca8PFJetsCHStrimmed.doPVCorrection = cms.bool(True)

##### Razor stuff

process.load("CMGTools.Susy.RazorMultiJet.razorMultijet_cff")
process.load("CMGTools.Susy.common.susy_cff")

if runOnCMGp:
    process.razorMJJetSequence.remove(process.razorMJJetGirth)
    process.razorMJJetSequence.remove(process.razorMJJetGirthCharged)
    process.demo.buffers.remove('patJetHelperAK5')
    process.demo.buffers.remove('patJetHelperAK5CHS')
    process.demo.buffers.remove('patMET')
    process.demo.buffers.remove('patMET1')
    process.demo.buffers.remove('patTau')

process.razorMJObjectSequence.remove(process.razorMJHemiSequence)
process.susyGenSequence.remove(process.dumpPdfWeights)
process.razorMJHadTriggerInfo.printSelections=False

if not runOnMC:
    process.demo.buffers.remove('sint')
    process.demo.buffers.remove('recoLeafCandidate')
    process.demo.buffers.remove('vertexWeight')
    process.demo.buffers.remove('edmTriggerResultsHelper2')
    process.demo.buffers.remove('genJet')

if runOnMC:
    process.demo.buffers.remove('hcalFilter')
    process.demo.buffers.remove('edmTriggerResultsHelper')
    process.demo.buffers.remove('edmTriggerResultsHelper1')


##### Vertex weight

process.load("CMGTools.RootTools.utils.vertexWeight.vertexWeights2012_cfi")

##### Sequence

print 'Global tag       : ', process.GlobalTag.globaltag

process.p = cms.Path()
process.schedule = cms.Schedule(process.p)

#if runPF:
#     process.load('Configuration.StandardSequences.Digi_cff')
#     process.load('Configuration.StandardSequences.SimL1Emulator_cff')
#     process.load('Configuration.StandardSequences.DigiToRaw_cff')
#     process.load('Configuration.StandardSequences.RawToDigi_cff')
#     process.load('Configuration.StandardSequences.L1Reco_cff')
#     process.load('Configuration.StandardSequences.Reconstruction_cff')
#     process.mix.input.fileNames = cms.untracked.vstring("root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/746680C6-202A-E211-A6F7-001A9281174A.root",
#           "root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/8E0656B2-EB29-E211-B8CA-0025905822B6.root",
#           "root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/DC77FAB5-1F2A-E211-8A41-003048FF86CA.root")
#     process.p1 = cms.Path(process.mix+process.doAllDigi+process.addPileupInfo)
#     process.p2 = cms.Path(process.SimL1Emulator)
#     process.p3 = cms.Path(process.DigiToRaw)
#     process.p4 = cms.Path(process.RawToDigi)
#     process.p5 = cms.Path(process.L1Reco)
#     process.p6 = cms.Path(process.reconstruction)
#     process.schedule = cms.Schedule(process.p1,process.p2,process.p3,process.p4,process.p5,process.p6,process.p)
#     process.recoPFJets = cms.Sequence(process.kt6PFJets+process.ak5PFJets)
#     from CMGTools.Common.PFVertexProducer_cfi import particleFlow
#     process.pfvertex=particleFlow
#     process.PATCMGVertexSequence = cms.Sequence(process.pfvertex)
#     process.PATCMGSequence.remove(process.PATCMGElectronSequence)
#     process.PATCMGSequence.remove(process.PATCMGPhotonSequence)
#     process.pfPileUpIso.PFCandidates = cms.InputTag("particleFlowTmp")
#     process.pfNoPileUpIso.bottomCollection = cms.InputTag("particleFlowTmp")
#     process.elPFIsoDepositCharged.src = cms.InputTag("pfSelectedElectrons")
#     process.elPFIsoDepositChargedAll.src = cms.InputTag("pfSelectedElectrons")
#     process.elPFIsoDepositGamma.src = cms.InputTag("pfSelectedElectrons")
#     process.elPFIsoDepositNeutral.src = cms.InputTag("pfSelectedElectrons")
#     process.elPFIsoDepositPU.src = cms.InputTag("pfSelectedElectrons")
#     process.muPFIsoDepositCharged.src = cms.InputTag("muons1stStep")
#     process.muPFIsoDepositChargedAll.src = cms.InputTag("muons1stStep")
#     process.muPFIsoDepositGamma.src = cms.InputTag("muons1stStep")
#     process.muPFIsoDepositNeutral.src = cms.InputTag("muons1stStep")
#     process.muPFIsoDepositPU.src = cms.InputTag("muons1stStep")
#     process.ak5JetTracksAssociatorAtVertex.jets = cms.InputTag("ak5CaloJets")
#     process.softElectronTagInfos.jets = cms.InputTag("ak5CaloJets")
#     process.softMuonTagInfos.jets = cms.InputTag("ak5CaloJets")
#     process.ak5PFJetTracksAssociatorAtVertex.jets = cms.InputTag("ak5PFJets")
#     ### MODIFY PF ALGORITHM
#     #process.particleFlowClusterHCAL.nNeighbours=0

if runPATCMG:
  process.load('CMGTools.Common.PAT.addFilterPaths_cff')
  process.p += process.PATCMGSequence
  process.p += process.PATCMGJetCHSSequence
  if runOnMC:
    process.demo.buffers.remove('edmTriggerResultsHelper2')
  if not runOnMC:
    process.demo.buffers.remove('edmTriggerResultsHelper1')
  from CMGTools.Common.PAT.patCMGSchedule_cff import getSchedule
  #if not runPF:
  process.schedule = getSchedule(process, runOnMC, False)
  if runOnMC:
      process.metNoiseCleaningPath.remove(process.hcalfilter)
      process.trackIsolationMakerFilterPath.remove(process.trackIsolationFilter)
  del process.boolToIntSequence

process.tnmc1 = cms.Sequence(process.goodOfflinePrimaryVertices)
process.tnmc1 += process.razorMJObjectSequence
if runOnMC==True:
    process.tnmc1 += process.susyGenSequence
    process.tnmc1 += process.vertexWeightSummer12MC53X2012ABCDData
if runPrunedAK5jets:
    process.tnmc1 += process.PATCMGJetSequenceAK5CHSpruned
if runAK7jets:
    process.tnmc1 += process.PATCMGJetSequenceAK7CHS+process.selectedPatJetsAK7CHSwithNsub+process.selectedPatJetsAK7CHSwithQjets
if runPrunedAK7jets:
    process.tnmc1 += process.PATCMGJetSequenceAK7CHSpruned
if runCA8jets:
    process.tnmc1 += process.PATCMGJetSequenceCA8CHS+process.PATCMGJetSequenceCA8CHSpruned+process.selectedPatJetsCA8CHSwithNsub+process.selectedPatJetsCA8CHSwithQjets
if runTrimmedCA8jets:
    process.tnmc1 += process.PATCMGJetSequenceCA8CHStrimmed
if runAK5genjets:
    process.tnmc1 += process.genParticlesForJets+process.ak5GenJets
process.tnmc1 += process.demo
process.p += process.tnmc1

##### HCAL laser filter for 2012

if not runOnMC:
    process.load("Ntuples.TNMc1.hcallasereventfilter2012_cfi")
    print "load laser event list"
    from Ntuples.TNMc1.AllBadHCALLaser import eventlist
    process.hcallasereventfilter2012.EventList=eventlist
    process.hcallasereventfilter2012Path=cms.Path(process.hcallasereventfilter2012)
    process.schedule = cms.Schedule(process.hcallasereventfilter2012Path,*[p for p in process.schedule])

#### recalibrated jets
if recalibrateCMGJets:
  from CMGTools.Common.miscProducers.cmgPFJetCorrector_cfi import cmgPFJetCorrector
  process.cmgPFJetCor = cmgPFJetCorrector.clone(src='cmgPFJetSel',
					      payload='AK5PF')
  process.cmgPFJetCorCHS = cmgPFJetCorrector.clone(src='cmgPFJetSelCHS',
						 payload='AK5PFchs')
  from CMGTools.Common.skims.cmgPFJetSel_cfi import cmgPFJetSel
  process.cmgPFJetSel = cmgPFJetSel.clone(src='cmgPFJetCor',
					      cut='pt()>30')
  process.cmgPFJetSelCHS = cmgPFJetSel.clone(src='cmgPFJetCorCHS',
					      cut='pt()>30')
  if runOnMC:
    process.cmgPFJetCor.levels = cms.vstring('L1FastJet','L2Relative','L3Absolute')
    process.cmgPFJetCorCHS.levels = cms.vstring('L1FastJet','L2Relative','L3Absolute')
  else:
    process.cmgPFJetCor.levels = cms.vstring('L1FastJet','L2Relative','L3Absolute','L2L3Residual')
    process.cmgPFJetCorCHS.levels = cms.vstring('L1FastJet','L2Relative','L3Absolute','L2L3Residual')
  process.p.insert(0,process.cmgPFJetSelCHS)
  process.p.insert(0,process.cmgPFJetSel)
  process.p.insert(0,process.cmgPFJetCorCHS)
  process.p.insert(0,process.cmgPFJetCor)

#### evaluate speed

print 'Fastjet instances (dominating our processing time...):'
from CMGTools.Common.Tools.visitorUtils import SeqVisitor
v = SeqVisitor('FastjetJetProducer')
process.p.visit(v)

if writePatTuple:
  process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('/tmp/hinzmann/patTuple_50PU.root'),
                               # save only events passing the full path
                               SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               # save PAT Layer 1 output; you need a '*' to
                               # unpack the list of commands 'patEventContent'
                               outputCommands = cms.untracked.vstring('keep *')
                               )
  process.outpath = cms.EndPath(process.out)
  process.schedule.append(process.outpath)

process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/ntuple_rerunPF_50PU.root")
