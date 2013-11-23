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
    f=file(samplename+"_GEN.log")
    crosssection="?"
    for l in f.readlines():
       if "| sum" in l:
          crosssection=float(l.split(" ")[-4])*1e9
    print samplename,crosssection
    