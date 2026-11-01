#!/bin/bash
cd "$(dirname "$0")"
python run_policy.py ../logs/ro_C0.npz mono5 ro_mono5 16 > ../logs/policy_ro_mono5.out 2>&1
python node_test.py ../../F1-biased-record/logs/vig_all10_Crec.npz ../logs/policy_vg_restr.json 10 vgr > ../logs/node_test_vg_restr.out 2>&1
python node_test.py ../../F1-biased-record/logs/vig_all10_Crec.npz ../logs/policy_vg_small.json 10 vgs > ../logs/node_test_vg_small.out 2>&1
python node_test.py ../logs/ro_C0.npz ../logs/policy_ro_small.json 8 ros > ../logs/node_test_ro_small.out 2>&1
W307_WARM=../logs/ro_C0.npz python thresh_run.py restrtop:12 R12 6.4548 5 1e-6 > ../logs/thresh_R12.out 2>&1
