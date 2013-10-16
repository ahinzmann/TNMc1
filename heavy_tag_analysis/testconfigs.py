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
    os.system("cmsDriver.py Configuration/GenProduction/python/"+samplename+".py  --mc --eventcontent RAWSIM          --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1  --datatier GEN-SIM    --conditions POSTLS162_V1::All         --step GEN  --magField 38T_PostLS1   --geometry Extended2015    --dirout /tmp/hinzmann/    --python_filename "+samplename+"_GEN.py -n 1000 > "+samplename+"_GEN.log &")
    os.system("cmsDriver.py Configuration/GenProduction/python/"+samplename+".py  --mc --eventcontent RAWSIM          --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1  --datatier GEN-SIM    --conditions POSTLS162_V1::All         --step GEN,SIM  --magField 38T_PostLS1   --geometry Extended2015    --dirout /tmp/hinzmann/    --python_filename "+samplename+"_GEN_SIM.py -n 10 > "+samplename+"_GEN_SIM.log &")
