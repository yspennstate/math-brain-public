#!/bin/bash
# 30 exact roots for vec_hi_rr.py, two at a time, one output file per run (parallel >> to one file splices lines on Windows);
# then vec_hi_rr_runs.txt = the files concatenated in order.
cd "$(dirname "$0")"
for M in A B; do for be in "0 0" "0.9 0" "0 1" "0.9 1" "0.5 1"; do set -- $be
  for b2 in 0.9995 0.999 0.998; do echo "$M $1 $b2 $2"; done; done; done |
  xargs -P 2 -L 1 bash -c 'f=vec_hi_out/$0_b1$1_b2$2_e$3.txt; [ -s $f ] || python vec_hi_rr.py $0 $1 $2 $3 > $f 2>&1'
for M in A B; do for be in "0 0" "0.9 0" "0 1" "0.9 1" "0.5 1"; do set -- $be
  for b2 in 0.9995 0.999 0.998; do cat vec_hi_out/${M}_b1$1_b2${b2}_e$2.txt; done; done; done > vec_hi_rr_runs.txt
echo DONE >> vec_hi_rr_runs.txt
