# Auto generated configuration file
# using: 
# Revision: 1.381.2.27 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: reco -s DIGI,L1,DIGI2RAW,HLT:7E33v2,RAW2DIGI,L1Reco,RECO --conditions START53_V23::All --pileup 2012_Summer_50ns_PoissonOOTPU --datamix NODATAMIXER --eventcontent FEVTSIM
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_7E33v2_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:///afs/cern.ch/user/h/hinzmann/workspace/RSGravitonToWW_kMpl01_M-2500_Tune23_8TeV-herwigpp-Summer12_DR53X-PU_S10_START53_V7A-v1-GENSIM-0454C808-0DBD-E211-886D-0025904886E6.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.27 $'),
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.FEVTSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.FEVTSIMEventContent.outputCommands,
    fileName = cms.untracked.string('/tmp/hinzmann/reco_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU_v2_corHCALcluster.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V23::All', '')

process.mix.input.fileNames = cms.untracked.vstring("root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/746680C6-202A-E211-A6F7-001A9281174A.root",
           "root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/8E0656B2-EB29-E211-B8CA-0025905822B6.root",
           "root://eoscms//eos/cms/store/relval/CMSSW_5_3_6-START53_V14/RelValMinBias/GEN-SIM-DIGI-RAW-HLTDEBUG/v2/00000/DC77FAB5-1F2A-E211-8A41-003048FF86CA.root")
#process.mix.input.nbPileupEvents.probValue = cms.vdouble(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

### MODIFY PF ALGORITHM
process.particleFlowClusterHCAL.nNeighbours=4 #mod=8, red=4, cor=4
process.particleFlowClusterHCAL.posCalcNCrystal=5 #mod=9, red=-1, cor=5
process.particleFlowClusterHCAL.useCornerCells=False #cor=False

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTSIMoutput_step = cms.EndPath(process.FEVTSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.FEVTSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions
