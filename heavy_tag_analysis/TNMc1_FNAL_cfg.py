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


# Get Will's SUSY MJ objects/sequences:
process.load("Configuration.StandardSequences.GeometryDB_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

# Run on MC or data

runOnMC = True
runPATCMG = True
recalibrateCMGJets = False
runAK7jets = False
runPrunedAK7jets = False
runCA8jets = True
runAK5genjets = True
runPrunedAK5jets = True
runQJets = False
runOnVVtuples = False
runOnCMGp = False

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

process.load("Ntuples.TNMc1.ntuple_cfi")

#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/X_WW_lvjj_SM600p-narrow-JHU.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_10_1_CVX.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_11_1_AXp.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_12_1_UQ9.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_13_1_ZCW.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_14_1_hdp.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_15_1_M2J.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_16_1_GPi.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_17_1_PSr.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_18_1_tnK.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_19_1_3R5.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_1_1_Sky.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_20_1_AjR.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_21_1_Cb5.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_22_1_1BJ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_23_1_7Bs.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_24_1_bPt.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_25_1_zpg.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_26_1_4PH.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_27_1_IGs.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_28_1_jxl.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_29_1_tWx.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_2_1_qeQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_30_1_rz5.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_31_1_UFn.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_32_1_lYT.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_33_1_6LD.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_34_1_awf.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_35_1_mtG.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_36_1_dTB.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_37_1_fyO.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_38_1_F78.root',
#'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_39_1_SCo.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_3_1_mQr.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_40_1_L4F.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_41_1_t9n.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_42_1_rpW.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_43_1_A1R.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_44_1_Z6B.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_45_1_3Ed.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_46_1_NDW.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_47_1_oUK.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_48_1_lCv.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_49_1_Lkb.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_4_1_JZX.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_50_1_j4g.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_51_1_eGA.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_5_1_Q4m.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_6_1_qmQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_7_1_Mo4.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_8_1_oSG.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM600p-narrow-JHU/X_WW_lvjj_SM600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_9_1_F6o.root',
#)
process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/X_WW_lvjj_PS2000m-narrow-JHU.root")
process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_34_1_NKS.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_35_1_pUc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_36_1_ZRj.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_37_1_Mr2.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_38_1_0fu.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_39_1_xaz.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_3_1_GHb.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_40_1_gsW.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_41_1_alh.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_42_1_SRT.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_43_1_QDK.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_44_1_SoQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_45_1_gP7.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_46_1_HBM.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_47_1_iqo.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_48_1_ry0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_49_1_7C0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_4_1_5TE.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_50_1_44T.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_51_1_8xU.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_5_1_nDl.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_6_1_8FN.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_7_1_QVh.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_8_1_c6a.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_9_1_QEg.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_10_1_iPc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_11_1_Ix0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_12_1_R9o.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_13_1_dMt.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_14_1_ZGH.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_15_1_582.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_16_1_t8g.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_17_1_nNb.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_18_1_x8l.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_19_1_X3s.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_1_1_fP6.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_20_1_EdG.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_21_1_i7G.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_22_1_Bis.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_23_1_d1y.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_24_1_d2E.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_25_1_BZX.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_26_1_U5H.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_27_1_cOj.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_28_1_VDy.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_29_1_tFm.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_2_1_aJN.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_30_1_JLo.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_31_1_mKh.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_32_1_iPL.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS2000m-narrow-JHU/X_WW_lvjj_PS2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_33_1_nIc.root',
)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/X_WW_lvjj_SM2000m-narrow-JHU.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_10_1_mZ7.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_11_1_GFc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_12_1_rzw.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_13_1_dFH.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_14_1_MMZ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_15_1_5tR.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_16_1_Kmq.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_17_1_ubc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_18_1_adg.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_19_1_COS.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_1_1_kx5.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_20_1_pGo.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_21_1_Hii.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_22_1_WEM.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_23_1_7Q0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_24_1_Pj8.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_25_1_i0p.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_26_1_RY0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_27_1_EJC.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_28_1_Mb1.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_29_1_jWA.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_2_1_vQK.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_30_1_Kpl.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_31_1_ddz.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_32_1_5lu.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_33_1_FvQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_34_1_PUG.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_35_1_9hW.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_36_1_BGk.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_37_1_QKv.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_38_1_hhQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_39_1_tjU.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_3_1_XKM.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_40_1_vQO.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_41_1_1pa.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_42_1_gUL.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_43_1_FOS.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_44_1_fUs.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_45_1_N9n.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_46_1_GFn.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_47_1_H7U.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_48_1_o6S.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_49_1_6HJ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_4_1_sWZ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_50_1_kuN.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_5_1_keQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_6_1_bIO.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_7_1_ubq.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_8_1_zHN.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_SM2000m-narrow-JHU/X_WW_lvjj_SM2000m-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_9_1_08W.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/X_WW_lvjj_PS600p-narrow-JHU.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_10_1_9YH.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_11_1_mdh.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_12_1_otN.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_13_1_I3J.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_14_1_bws.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_15_1_SKR.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_16_1_bGm.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_17_1_zQY.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_18_1_HU8.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_19_1_rjy.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_1_1_P28.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_20_1_Yq5.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_21_1_rqj.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_22_1_Z54.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_23_1_WXh.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_24_1_Mj1.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_25_1_XlD.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_26_1_pY4.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_27_1_H0F.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_28_1_gwU.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_29_1_NFs.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_2_1_lwP.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_30_1_UkZ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_31_1_M7r.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_32_1_p27.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_33_1_OOc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_34_1_Fus.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_35_1_9Bm.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_36_1_c1f.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_37_1_S2G.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_38_1_Tpq.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_39_1_UOH.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_3_1_5Cy.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_40_1_ZGi.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_41_1_Ax0.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_42_1_EwQ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_43_1_ZVc.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_44_1_wCw.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_45_1_6Gd.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_46_1_vxM.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_47_1_Qbz.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_48_1_pzS.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_49_1_051.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_4_1_x1H.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_50_1_woP.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_51_1_saJ.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_5_1_OGS.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_6_1_qpg.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_7_1_8Ij.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_8_1_pRu.root',
'root://xrootd.unl.edu//store/user/ntran/X_WW_lvjj_PS600p-narrow-JHU/X_WW_lvjj_PS600p-narrow-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/XWW_JHUGen_AODSIM_9_1_FxY.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_10_1_Mvy.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_11_1_voa.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_1_1_jar.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_12_1_HEX.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_13_1_yvO.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_14_1_tFW.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_15_1_3Ji.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_16_1_zCN.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_17_1_Vzw.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_18_1_YLy.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_19_1_iF5.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_20_1_yaa.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_2_1_7S9.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_3_1_oFF.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_4_1_LMz.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_5_1_1eu.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_6_1_6tt.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_7_1_d4t.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_8_1_bhk.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_1TeV_9_1_HYK.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_10_1_hbQ.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_11_1_y7o.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_1_1_K3X.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_12_1_Bik.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_13_1_YJe.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_14_1_ZjZ.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_15_1_OdQ.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_16_1_Kmo.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_17_1_ATD.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_18_1_g4b.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_19_1_s5w.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_20_1_qyp.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_2_1_qJI.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_3_1_f6F.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_4_1_Pok.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_5_1_S53.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_6_1_eyc.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_7_1_pUD.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_8_1_pJh.root',
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2TeV/MadGraph_PYTHIA6_FastSim53X_RadionToHH_Hbb_2TeV_9_1_6kk.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/RadionToHH_4b_1500GeV_Herwig_FastSim53X.root',")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_10_1_QUW.root',  
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_4_1_WDi.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_7_1_RXh.root', 
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_2_1_DSg.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_5_1_H00.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_8_1_vza.root', 
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_3_1_ZMD.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_6_1_71E.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_1500GeV_4b_Herwig/RadionToHH_4b_1500GeV_Herwig_FastSim53X_9_1_BWK.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/RadionToHH_4b_2500GeV_Herwig_FastSim53X.root',")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_10_1_FoT.root',  
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_4_1_lIg.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_8_1_JCN.root', 
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_1_1_TMQ.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_5_1_U7G.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_9_1_rVZ.root', 
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_2_1_Tpe.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_6_1_buH.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_3_1_zJp.root',   
'root://xrootd.unl.edu//store/user/sertac/2012/Radion/MR_2500GeV_4b_Herwig/RadionToHH_4b_2500GeV_Herwig_FastSim53X_7_1_GBx.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/BulkG_WW_jjjj_c0p2_M1000-JHU_2.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_15_1_nd0.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_16_1_9ro.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_17_1_4uF.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_18_1_yTd.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_19_1_4H2.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_1_1_xcQ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_20_1_Ezk.root',
#'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_21_1_z2J.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_22_1_N4h.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_23_1_IJk.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_24_1_sCz.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_25_1_auH.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_26_1_pXH.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_27_1_3cu.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_28_1_hIx.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_29_1_cew.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_2_1_zlO.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_30_1_bJd.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_31_1_2BS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_32_1_Fto.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_33_1_wS6.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_34_1_GkS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_35_1_XIM.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_36_1_O3l.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_37_1_PiT.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_38_1_JiH.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_39_1_79E.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_3_1_iY3.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_40_1_Y1z.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_41_1_vHU.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_42_1_gUa.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_43_1_Ros.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_44_1_qrZ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_45_1_FKt.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_46_1_MrG.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_47_1_2RH.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_48_1_UGo.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_49_1_saA.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_4_1_L4N.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_50_1_bae.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_51_1_Uyv.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_5_1_Ihl.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_6_1_Bxn.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_7_1_JuP.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_8_1_AB3.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_9_1_wN1.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_10_1_gYX.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_11_1_BXv.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_12_1_YXF.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_13_1_4HJ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1000-JHU/BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_14_1_Qe5.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/BulkG_WW_jjjj_c0p2_M1500-JHU_2.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_10_2_sHf.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_11_2_dAs.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_12_2_xbE.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_13_2_7fy.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_14_2_rhN.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_15_2_tdF.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_16_2_wvv.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_17_2_sVS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_18_2_WRG.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_19_1_W9C.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_20_2_fyA.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_21_2_uru.root',
#'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_22_2_gWo.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_23_2_0xU.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_24_2_f6J.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_25_2_HT8.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_26_2_siM.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_27_2_rWf.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_28_2_34a.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_29_2_Drt.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_2_2_uu7.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_30_2_rdQ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_31_2_i3B.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_32_2_1BS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_33_2_QKf.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_34_2_g5a.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_35_2_e7I.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_37_2_IUu.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_38_2_D0j.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_39_2_FUT.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_3_2_eb7.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_40_2_AQP.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_42_2_LOZ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_43_2_hqS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_44_2_Vxz.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_45_2_8j2.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_47_2_N66.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_48_2_Ed8.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_49_2_GvK.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_4_2_FHX.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_50_2_xJA.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_51_1_ZyD.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_5_2_7EG.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_6_2_xiB.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_7_2_OUD.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_8_2_t5N.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M1500-JHU/BulkG_WW_jjjj_c0p2_M1500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_9_2_q8T.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/BulkG_WW_jjjj_c0p2_M2000-JHU_2.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_10_1_S3h.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_11_1_2XZ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_12_1_dLo.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_13_1_SRq.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_14_1_9oU.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_15_1_o8x.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_16_1_1Jp.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_17_1_Ok4.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_18_1_Qn2.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_19_1_tJF.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_1_1_wKH.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_20_1_J8f.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_21_1_g7b.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_22_1_hbo.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_23_1_aB8.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_24_1_FKs.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_25_1_Y1L.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_26_1_5li.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_27_1_eON.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_28_1_01X.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_29_1_Boe.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_2_1_nh6.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_30_1_LTh.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_31_1_n8M.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_32_1_L9T.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_33_1_Wvb.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_34_1_qeW.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_35_1_KiM.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_36_1_7tT.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_37_1_fLi.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_38_1_IAX.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_39_1_pn1.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_3_1_q1Z.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_40_1_grw.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_41_1_sLE.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_42_1_L3l.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_43_1_jan.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_44_1_Wq6.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_45_1_hfY.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_47_1_HMl.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_48_1_xLD.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_49_1_sCL.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_4_1_ZTB.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_50_1_P75.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_51_1_2H1.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_5_1_eiT.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_6_1_CmM.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_7_1_9rI.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_8_1_CFf.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2000-JHU/BulkG_WW_jjjj_c0p2_M2000-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_9_1_ldU.root',
#)
#process.demo.ntupleName=cms.untracked.string("/tmp/hinzmann/BulkG_WW_jjjj_c0p2_M2500-JHU_2.root")
#process.source.fileNames=cms.untracked.vstring(
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_10_1_GNK.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_11_1_ek8.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_12_1_HcZ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_13_1_qHz.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_14_1_Pww.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_15_1_KcS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_16_1_aki.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_17_1_XAw.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_18_1_Adx.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_19_1_NsS.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_1_1_HaL.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_20_1_c11.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_21_1_BsB.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_22_1_cFG.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_23_1_ecT.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_24_1_47A.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_25_1_LQs.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_26_1_Day.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_27_1_7UZ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_28_1_PmC.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_29_1_vcJ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_2_1_GdJ.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_30_1_eBB.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_31_1_5Hf.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_32_1_5PX.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_33_1_foM.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_34_1_MeN.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_35_1_3hV.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_37_1_z9n.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_38_1_nCI.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_39_1_nBx.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_3_1_VrB.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_40_1_c6s.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_42_1_kdD.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_43_1_lPt.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_44_1_KXO.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_45_1_NTx.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_47_1_OzI.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_48_1_g2g.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_49_1_uiP.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_4_1_y3q.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_50_1_GTI.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_51_1_bLi.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_5_1_6pK.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_6_1_N46.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_7_1_vro.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_8_1_s0W.root',
'root://xrootd.unl.edu//store/user/qili/BulkG_WW_jjjj_c0p2_M2500-JHU/BulkG_WW_jjjj_c0p2_M2500-JHU-AODSIM/c8f8ed334db8a7d6f56c62266b1dfa5b/RSWW_AODSIM_9_1_G7y.root',
#)

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

if runOnVVtuples:
    process.demo.patJetHelperAK5[0]=process.demo.patJetHelperAK5[0].replace("patJetsWithVar","selectedPatJets")
    process.demo.patJetHelperAK5CHS[0]=process.demo.patJetHelperAK5CHS[0].replace("patJetsWithVarCHS","selectedPatJetsCHS")
    process.demo.buffers.remove("edmEventHelperExtra")

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

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
if not runOnMC:
    process.PATCMGJetSequenceCA8CHS.remove( process.jetMCSequenceCA8CHS )
    process.patJetsCA8CHS.addGenJetMatch = False
    process.patJetsCA8CHS.addGenPartonMatch = False
    process.patJetCorrFactorsCA8CHS.levels.append('L2L3Residual')
    process.PATCMGJetSequenceCA8CHSpruned.remove( process.jetMCSequenceCA8CHSpruned )
    process.patJetsCA8CHSpruned.addGenJetMatch = False
    process.patJetsCA8CHSpruned.addGenPartonMatch = False
    process.patJetCorrFactorsCA8CHSpruned.levels.append('L2L3Residual')

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
if runPATCMG:
  process.load('CMGTools.Common.PAT.addFilterPaths_cff')
  process.p = cms.Path(
    process.PATCMGSequence + 
    process.PATCMGJetCHSSequence 
  )
  if runOnMC:
    process.demo.buffers.remove('edmTriggerResultsHelper2')
  if not runOnMC:
    process.demo.buffers.remove('edmTriggerResultsHelper1')
  from CMGTools.Common.PAT.patCMGSchedule_cff import getSchedule
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
