ProductionTasks.py -w 'patTuple*.root' -c -N 5 -q 2nd -t NTUPLE_Feb15 --output_wildcard '[!h]*.root' --batch_user tnm_group --cfg TNMc1_Feb15_cfg.py --max_threads 100 `cat data/samples_Moriond.txt`

ProductionTasks.py -w 'cmgTuple*.root' -c -N 5 -q 2nd -t NTUPLE_Feb15 --output_wildcard '[!h]*.root' --batch_user tnm_group --cfg TNMc1_Feb15_cfg.py --max_threads 100 `cat data/samples_Moriond.txt`

ProductionTasks.py -w '*.root' -c -N 1 -q 2nd -t NTUPLE_Aug5 --output_wildcard '[!h]*.root' --batch_user tnm_group --cfg TNMc1_Feb15_cfg.py --max_threads 100 `cat data/samples_Moriond.txt`


cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_WJetsPt100 -o summer12_WJetsPt100
cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_WJetsPt70To100 -o summer12_WJetsPt70To100
cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_WJetsPt50To70 -o summer12_WJetsPt50To70
cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_WW -o summer12_WW
cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_TTBAR -o summer12_TTBAR
cmsBatch.py 5 TNMc1_Feb15_cfg.py -b 'bsub -q 1nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/summer12_RSG_WW_lvjj_c0p05_M1000 -o summer12_RSG_WW_lvjj_c0p05_M1000

cmsBatch.py 5 heavy_tag_analysis/TNMc1_FNAL_cfg.py -b './batchScript.sh &' -f -r /store/cmst3/user/hinzmann/NTUPLE/X_WW_lvjj_PS2000m-narrow-JHU -o X_WW_lvjj_PS2000m-narrow-JHU
cmsBatch.py 5 heavy_tag_analysis/TNMc1_FNAL_cfg.py -b './batchScript.sh &' -f -r /store/cmst3/user/hinzmann/NTUPLE/X_WW_lvjj_SM2000m-narrow-JHU -o X_WW_lvjj_SM2000m-narrow-JHU
cmsBatch.py 5 TNMc1_Feb15_FNAL_cfg.py -b 'bsub -q 2nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/X_WW_lvjj_PS600p-narrow-JHU -o X_WW_lvjj_PS600p-narrow-JHU
cmsBatch.py 5 TNMc1_Feb15_FNAL_cfg.py -b 'bsub -q 2nd < ./batchScript.sh' -f -r /store/cmst3/user/hinzmann/NTUPLE/X_WW_lvjj_SM600p-narrow-JHU -o X_WW_lvjj_SM600p-narrow-JHU
