#!/bin/bash
cd "$(dirname "$0")"
python ro_fp.py 6.4548 C0 > ../logs/ro_C0.out 2>&1
python run_policy.py ../logs/ro_C0.npz and,xor,g7,npn3,npn4 ro_small 16 > ../logs/policy_ro_small.out 2>&1
W307_WARM=../logs/ro_C0.npz python thresh_run.py g7 G7 6.4548 5 1e-6 > ../logs/thresh_G7.out 2>&1
python control_bump.py > ../logs/control_bump.out 2>&1
