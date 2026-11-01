#!/bin/bash
cd "$(dirname "$0")"
python run_policy.py ../../F1-biased-record/logs/vig_all10_Crec.npz and,xor,g7,restr:2-10 vg_restr 16 > ../logs/policy_vg_restr.out 2>&1
python run_policy.py ../../F1-biased-record/logs/vig_all10_Crec.npz npn3,npn4,mono5 vg_small 16 > ../logs/policy_vg_small.out 2>&1
