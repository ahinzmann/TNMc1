import os

signals=["WprimeToWZ","RSGravitonToWW_kMpl01","RSGravitonToZZ_kMpl01","QstarToQW","QstarToQZ"]
signalMasses={}
signalMasses["WprimeToWZ"]=[500,1000,1500,1700,1800,1900,2000,2500,3000,3500,4000,4500]
signalMasses["RSGravitonToWW_kMpl01"]=[500,1000,1500,1700,1800,1900,2000,2500,3000,3500,4000,4500]
signalMasses["RSGravitonToZZ_kMpl01"]=[500,1000,1500,1700,1800,1900,2000,2500,3000,3500,4000,4500]
signalMasses["QstarToQW"]=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500]
signalMasses["QstarToQZ"]=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500]

for signal in signals:
  for mass in signalMasses[signal]:
    samplename=signal+"_M_"+str(mass)+"_Tune4C_13TeV_pythia8_cfi"
    print samplename
    cfg=open(samplename+".py","w")
    cfg.writelines("""
import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(1e10),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
		processParameters = cms.vstring(
			'Main:timesAllowErrors    = 10000',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tauMax = 10',
			'Tune:pp 8',
			'Tune:ee 3',
""")
    if "WprimeToWZ" in signal:
      cfg.writelines("""
			'NewGaugeBoson:ffbar2Wprime = on',
			'Wprime:coup2WZ = 1',
			'34:m0 = """+str(mass)+"""',
			'34:onMode = off',
			'34:onIfAny = 23,24',
""")
    if "RSGravitonToWW_kMpl01" in signal:
      cfg.writelines("""
			'ExtraDimensionsG*:all = on',
			'ExtraDimensionsG*:kappaMG = 0.54',
			'5100039:m0 = """+str(mass)+"""',
			'5100039:onMode = off',
			'5100039:onIfAny = 24',
""")
    if "RSGravitonToZZ_kMpl01" in signal:
      cfg.writelines("""
			'ExtraDimensionsG*:all = on',
			'ExtraDimensionsG*:kappaMG = 0.54',
			'5100039:m0 = """+str(mass)+"""',
			'5100039:onMode = off',
			'5100039:onIfAny = 23',
""")
    if "QstarToQW" in signal:
      cfg.writelines("""
			'ExcitedFermion:dg2dStar = on',
			'ExcitedFermion:ug2uStar = on',
			'ExcitedFermion:Lambda = """+str(mass)+"""',
			'4000001:m0 = """+str(mass)+"""',
			'4000001:onMode = off',
			'4000001:onIfMatch = 2 24',
			'4000002:m0 = """+str(mass)+"""',
			'4000002:onMode = off',
			'4000002:onIfMatch = 1 24',
""")
    if "QstarToQZ" in signal:
      cfg.writelines("""
			'ExcitedFermion:dg2dStar = on',
			'ExcitedFermion:ug2uStar = on',
			'ExcitedFermion:Lambda = """+str(mass)+"""',
			'4000001:m0 = """+str(mass)+"""',
			'4000001:onMode = off',
			'4000001:onIfMatch = 1 23',
			'4000002:m0 = """+str(mass)+"""',
			'4000002:onMode = off',
			'4000002:onIfMatch = 2 23',
""")
    cfg.writelines("""
		),
		parameterSets = cms.vstring('processParameters')
	)
)

ProductionFilterSequence = cms.Sequence(generator)
""")
    cfg.close()
