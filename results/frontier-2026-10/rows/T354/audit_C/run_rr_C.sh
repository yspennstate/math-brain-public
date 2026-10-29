#!/bin/sh
# validation by simulation, then every enclosure of remainder_rr_mom.py and remainder_rr_eps.py (agent C, T354 audit)
cd "$(dirname "$0")"
for a in "0.5 0.9 1 0.05" "0.9 0.9 3 0.2" "0.9 0.95 0 0.1" "0.99 0.9 1 0.1"; do python -X utf8 rr_sim_check.py $a; done > rr_sim_check.txt 2>&1
for a in "0.9 0.9999 0" "0.9 0.999 0" "0.5 0.999 0" "0.9 0.99 0" "0 0.999 1" "0 0.999 3" "0 0.999 10" "0 0.99 0" "0 0.99 1" "0 0.99 3" "0 0.99 10" "0.9 0.999 0 320"; do
  python -X utf8 rr_exact_mom_eps.py $a; done > rr_exact_runs.txt 2>&1
echo done >> rr_exact_runs.txt
