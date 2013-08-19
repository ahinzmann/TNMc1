import FWCore.ParameterSet.Config as cms

# JETS PRUNED AK5 ----------------------------

from RecoJets.JetProducers.ak5PFJetsPruned_cfi import ak5PFJetsPruned
ak5PFJetsChSpruned = ak5PFJetsPruned.clone(
    src = 'pfNoPileUp',
    jetPtMin = cms.double(30.0),
    doAreaFastjet = cms.bool(True),
    )

jetSource = 'ak5PFJetsChSpruned'

# corrections 
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import *
patJetCorrFactorsAK5CHSpruned = patJetCorrFactors.clone()
patJetCorrFactorsAK5CHSpruned.src = jetSource
# will need to add L2L3 corrections in the cfg
patJetCorrFactorsAK5CHSpruned.levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
patJetCorrFactorsAK5CHSpruned.payload = 'AK5PFchs'
patJetCorrFactorsAK5CHSpruned.useRho = True

# parton and gen jet matching

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import *
patJetPartonMatchAK5CHSpruned = patJetPartonMatch.clone()
patJetPartonMatchAK5CHSpruned.src = jetSource
patJetGenJetMatchAK5CHSpruned = patJetGenJetMatch.clone()
patJetGenJetMatchAK5CHSpruned.src = jetSource
patJetGenJetMatchAK5CHSpruned.matched = 'ak5GenJetsNoNu'

from PhysicsTools.PatAlgos.mcMatchLayer0.jetFlavourId_cff import *
patJetPartonAssociationAK5CHSpruned = patJetPartonAssociation.clone()
patJetPartonAssociationAK5CHSpruned.jets = jetSource

# pat jets

from RecoJets.JetAssociationProducers.ak5JTA_cff import *
ak5CHSprunedJetTracksAssociatorAtVertex=ak5JetTracksAssociatorAtVertex.clone()
ak5CHSprunedJetTracksAssociatorAtVertex.jets=jetSource
from RecoBTag.Configuration.RecoBTag_cff import * # btagging sequence
impactParameterTagInfosAK5CHSpruned=impactParameterTagInfos.clone()
impactParameterTagInfosAK5CHSpruned.jetTracks='ak5CHSprunedJetTracksAssociatorAtVertex'
secondaryVertexTagInfosAK5CHSpruned=secondaryVertexTagInfos.clone()
secondaryVertexTagInfosAK5CHSpruned.trackIPTagInfos='impactParameterTagInfosAK5CHSpruned'
combinedSecondaryVertexBJetTagsAK5CHSpruned=combinedSecondaryVertexBJetTags.clone()
combinedSecondaryVertexBJetTagsAK5CHSpruned.tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5CHSpruned"),
    cms.InputTag("secondaryVertexTagInfosAK5CHSpruned"))
btaggingAK5CHSpruned=cms.Sequence(ak5CHSprunedJetTracksAssociatorAtVertex+impactParameterTagInfosAK5CHSpruned+secondaryVertexTagInfosAK5CHSpruned+combinedSecondaryVertexBJetTagsAK5CHSpruned)

from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import *
patJetsAK5CHSpruned = patJets.clone()
patJetsAK5CHSpruned.jetSource = jetSource
patJetsAK5CHSpruned.addJetCharge = False
patJetsAK5CHSpruned.embedCaloTowers = False
patJetsAK5CHSpruned.embedPFCandidates = False
patJetsAK5CHSpruned.addAssociatedTracks = False
patJetsAK5CHSpruned.addBTagInfo = True
patJetsAK5CHSpruned.addDiscriminators = True
patJetsAK5CHSpruned.tagInfoSources = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK5CHSpruned"))
patJetsAK5CHSpruned.trackAssociationSource = cms.InputTag("ak5CHSprunedJetTracksAssociatorAtVertex")
patJetsAK5CHSpruned.discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTagsAK5CHSpruned"))
patJetsAK5CHSpruned.getJetMCFlavour = False
patJetsAK5CHSpruned.jetCorrFactorsSource = cms.VInputTag(cms.InputTag('patJetCorrFactorsAK5CHSpruned'))
patJetsAK5CHSpruned.genPartonMatch = cms.InputTag('patJetPartonMatchAK5CHSpruned')
patJetsAK5CHSpruned.genJetMatch = cms.InputTag('patJetGenJetMatchAK5CHSpruned')

from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
selectedPatJetsAK5CHSprunedPre = selectedPatJets.clone()
selectedPatJetsAK5CHSprunedPre.src = 'patJetsAK5CHSpruned'
selectedPatJetsAK5CHSprunedPre.cut = 'pt()>30'

from RecoJets.Configuration.RecoGenJets_cff import ak5GenJetsNoNu
ak5PrunedGenJetsNoNu = ak5GenJetsNoNu.clone()
ak5PrunedGenJetsNoNu.doAreaFastjet = True
ak5PrunedGenJetsNoNu.usePruning = cms.bool(True)
ak5PrunedGenJetsNoNu.useExplicitGhosts = cms.bool(True)
ak5PrunedGenJetsNoNu.writeCompound = cms.bool(True)
ak5PrunedGenJetsNoNu.jetCollInstanceName = cms.string("SubJets")
ak5PrunedGenJetsNoNu.nFilt = cms.int32(2)
ak5PrunedGenJetsNoNu.zcut = cms.double(0.1)
ak5PrunedGenJetsNoNu.rcut_factor = cms.double(0.5)
ak5PrunedGenJetsNoNu.jetPtMin = 30

patGenJetsAK5CHSpruned = patJets.clone()
patGenJetsAK5CHSpruned.jetSource = 'ak5PrunedGenJetsNoNu'
patGenJetsAK5CHSpruned.addGenJetMatch = False
patGenJetsAK5CHSpruned.addGenPartonMatch = False
patGenJetsAK5CHSpruned.addJetCharge = False
patGenJetsAK5CHSpruned.embedCaloTowers = False
patGenJetsAK5CHSpruned.embedPFCandidates = False
patGenJetsAK5CHSpruned.addAssociatedTracks = False
patGenJetsAK5CHSpruned.addBTagInfo = False
patGenJetsAK5CHSpruned.addDiscriminators = False
patGenJetsAK5CHSpruned.getJetMCFlavour = False
patGenJetsAK5CHSpruned.addJetCorrFactors = False

#### Adding subjet b-tagging

from RecoJets.JetAssociationProducers.ak5JTA_cff import *
ak5CHSprunedSubjetsJetTracksAssociatorAtVertex=ak5JetTracksAssociatorAtVertex.clone()
ak5CHSprunedSubjetsJetTracksAssociatorAtVertex.jets=cms.InputTag('ak5PFJetsChSpruned','SubJets')
from RecoBTag.Configuration.RecoBTag_cff import * # btagging sequence
impactParameterTagInfosAK5CHSprunedSubjets=impactParameterTagInfos.clone()
impactParameterTagInfosAK5CHSprunedSubjets.jetTracks='ak5CHSprunedSubjetsJetTracksAssociatorAtVertex'
secondaryVertexTagInfosAK5CHSprunedSubjets=secondaryVertexTagInfos.clone()
secondaryVertexTagInfosAK5CHSprunedSubjets.trackIPTagInfos='impactParameterTagInfosAK5CHSprunedSubjets'
combinedSecondaryVertexBJetTagsAK5CHSprunedSubjets=combinedSecondaryVertexBJetTags.clone()
combinedSecondaryVertexBJetTagsAK5CHSprunedSubjets.tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfosAK5CHSprunedSubjets"),
    cms.InputTag("secondaryVertexTagInfosAK5CHSprunedSubjets"))
btaggingAK5CHSprunedSubjets=cms.Sequence(ak5CHSprunedSubjetsJetTracksAssociatorAtVertex+impactParameterTagInfosAK5CHSprunedSubjets+secondaryVertexTagInfosAK5CHSprunedSubjets+combinedSecondaryVertexBJetTagsAK5CHSprunedSubjets)

patJetsAK5CHSprunedSubjets = patJets.clone()
patJetsAK5CHSprunedSubjets.jetSource = cms.InputTag('ak5PFJetsChSpruned','SubJets')
patJetsAK5CHSprunedSubjets.addGenJetMatch = False
patJetsAK5CHSprunedSubjets.addGenPartonMatch = False
patJetsAK5CHSprunedSubjets.addJetCharge = False
patJetsAK5CHSprunedSubjets.embedCaloTowers = False
patJetsAK5CHSprunedSubjets.embedPFCandidates = False
patJetsAK5CHSprunedSubjets.addAssociatedTracks = False
patJetsAK5CHSprunedSubjets.addBTagInfo = True
patJetsAK5CHSprunedSubjets.addDiscriminators = True
patJetsAK5CHSprunedSubjets.tagInfoSources = cms.VInputTag(cms.InputTag("secondaryVertexTagInfosAK5CHSprunedSubjets"))
patJetsAK5CHSprunedSubjets.trackAssociationSource = cms.InputTag("ak5CHSprunedSubjetsJetTracksAssociatorAtVertex")
patJetsAK5CHSprunedSubjets.discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexBJetTagsAK5CHSprunedSubjets"))
patJetsAK5CHSprunedSubjets.getJetMCFlavour = False
patJetsAK5CHSprunedSubjets.addJetCorrFactors = False

selectedPatJetsAK5CHSpruned = cms.EDProducer("BoostedJetMerger",
                                                      jetSrc=cms.InputTag("selectedPatJetsAK5CHSprunedPre"),
                                                      subjetSrc=cms.InputTag("patJetsAK5CHSprunedSubjets")
    )

from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJetsNoNu
jetMCSequenceAK5CHSpruned = cms.Sequence(
    patJetPartonMatchAK5CHSpruned +
    genParticlesForJetsNoNu +
    ak5PrunedGenJetsNoNu +
    patGenJetsAK5CHSpruned +
    patJetGenJetMatchAK5CHSpruned
    )

PATCMGJetSequenceAK5CHSpruned = cms.Sequence(
    ak5PFJetsChSpruned +
    jetMCSequenceAK5CHSpruned +
    patJetCorrFactorsAK5CHSpruned +
    btaggingAK5CHSpruned +
    patJetsAK5CHSpruned +
    selectedPatJetsAK5CHSprunedPre +
    btaggingAK5CHSprunedSubjets +
    patJetsAK5CHSprunedSubjets +
    selectedPatJetsAK5CHSpruned
    )

ak5Jets = cms.Sequence( PATCMGJetSequenceAK5CHSpruned )
