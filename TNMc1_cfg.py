#$Revision: 1.10 $
import FWCore.ParameterSet.Config as cms

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
# See TheNtupleMaker twiki for a brief explanation
#process.MessageLogger.destinations = cms.untracked.vstring("cerr")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.cerr.default.limit = 5

# This is required in order to configure HLTConfigProducer
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")


# Get Will's SUSY MJ objects/sequences:
process.load("Configuration.StandardSequences.GeometryDB_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

# Run on MC or data

runOnMC = False

# Input file

dataset_user = 'cmgtools' 
#dataset_name = '/SingleMu/Run2012A-13Jul2012-v1/AOD/PAT_CMG_V5_6_0_B'
#dataset_name = '/TTJets_MassiveBinDECAY_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_6_0_B'
#dataset_name = '/HT/Run2012A-PromptReco-v1/RECO/PAT_CMG_V5_4_0_runrange_190605-194076'
dataset_name = '/JetHT/Run2012C-PromptReco-v1/AOD/PAT_CMG_V5_6_0_B'
#dataset_name = '/QCD_Pt-15to3000_TuneZ2star_Flat_8TeV_pythia6/Summer12-PU_S7_START52_V9-v5/AODSIM/V5/PAT_CMG_V5_4_0'
dataset_files = 'patTuple.*root'

from CMGTools.Production.datasetToSource import *
process.source = datasetToSource(
    dataset_user,
    dataset_name,
    dataset_files,
    )

print 'input:', process.source.fileNames

# set up JSON ---------------------------------------------------------------

if runOnMC==False:
    from CMGTools.Common.Tools.applyJSON_cff import *
    json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-204567_8TeV_PromptReco_Collisions12_JSON.txt'
    print 'json:', json
    applyJSON(process, json )

print 'runOnMC:', runOnMC

process.load("Ntuples.TNMc1.ntuple_cfi")

from CMGTools.External.pujetidsequence_cff import *

process.selectedPatJetspuJetId = pileupJetIdProducer.clone(
    produceJetIds = cms.bool(True),
    jetids = cms.InputTag(""),
    runMvas = cms.bool(False),
    jets = cms.InputTag("selectedPatJets"),
    vertexes = cms.InputTag("offlinePrimaryVertices"),
    algos = cms.VPSet(cutbased)
    )

process.selectedPatJetsCHSpuJetId = pileupJetIdProducer.clone(
    produceJetIds = cms.bool(True),
    jetids = cms.InputTag(""),
    runMvas = cms.bool(False),
    jets = cms.InputTag("selectedPatJetsCHS"),
    vertexes = cms.InputTag("offlinePrimaryVertices"),
    algos = cms.VPSet(cutbased)
    )

process.ak5PFJetsCHSprunedSubJetspuJetId = pileupJetIdProducer.clone(
    produceJetIds = cms.bool(True),
    jetids = cms.InputTag(""),
    runMvas = cms.bool(False),
    jets = cms.InputTag("ak5PFJetsCHSpruned:SubJets"),
    vertexes = cms.InputTag("offlinePrimaryVertices"),
    algos = cms.VPSet(cutbased)
    )

#process.p = cms.Path(process.selectedPatJetspuJetId * process.selectedPatJetsCHSpuJetId * process.ak5PFJetsCHSprunedSubJetspuJetId * process.demo)

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

GT = None
if runOnMC:
    GT = 'START53_V10::All' # for Summer12 MC
else:
    GT = 'GR_P_V41_AN1::All' # for run2012C
process.GlobalTag.globaltag = GT

print 'Global tag       : ', process.GlobalTag.globaltag

##### AK7 jets

process.load('CMGTools.Common.PAT.PATCMG_cff')
process.load("CMGTools.Common.PAT.jetSubstructure_cff")
if not runOnMC:
    process.PATCMGJetSequenceAK7CHSpruned.remove( process.jetMCSequenceAK7CHSpruned )
    process.patJetsAK7CHSpruned.addGenJetMatch = False
    process.patJetsAK7CHSpruned.addGenPartonMatch = False
    process.patJetCorrFactorsAK7CHSpruned.levels.append('L2L3Residual')

process.load("PAT_ak7jets_cff")
if not runOnMC:
    process.PATCMGJetSequenceAK7CHS.remove( process.jetMCSequenceAK7CHS )
    process.patJetsAK7CHS.addGenJetMatch = False
    process.patJetsAK7CHS.addGenPartonMatch = False
    process.patJetCorrFactorsAK7CHS.levels.append('L2L3Residual')

##### Razor stuff

process.load("CMGTools.Susy.RazorMultiJet.razorMultijet_cff")
process.load("CMGTools.Susy.common.susy_cff")

process.razorMJObjectSequence.remove(process.razorMJHemiSequence)
# This is the UCSB tau veto.  Need to remove for SMSs:
process.razorMJTauSequence.remove(process.razorMJTauVeto)

if not runOnMC:
    process.demo.buffers.remove('sint')
    process.demo.buffers.remove('recoLeafCandidate')

##### Sequence

if runOnMC==True:
    #process.p = cms.Path(process.PATCMGJetSequenceAK7CHS+process.PATCMGJetSequenceAK7CHSpruned+process.demo)
    process.p = cms.Path(process.razorMJObjectSequence+process.susyGenSequence+process.PATCMGJetSequenceAK7CHS+process.PATCMGJetSequenceAK7CHSpruned+process.demo)
else:
    #process.p = cms.Path(process.PATCMGJetSequenceAK7CHS+process.PATCMGJetSequenceAK7CHSpruned+process.demo)
    process.p = cms.Path(process.razorMJObjectSequence+process.PATCMGJetSequenceAK7CHS+process.PATCMGJetSequenceAK7CHSpruned+process.demo)
