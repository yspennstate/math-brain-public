#!/bin/bash
# independent large-n roots, one file per run (no shared appends)
cd "$(dirname "$0")"
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2
lane() { for c in "$@"; do set -- $c; python -X utf8 rrm_indep.py $1 $2 $3 $4 > rrmi_out/n$1_b2$2_s$3.txt 2>/dev/null; done; }
lane "10 0.99 200 2400" "50 0.99 200 2400" "200 0.99 200 2400" "500 0.99 200 2400" "1000 0.99 200 2400" "2000 0.99 200 2400" &
lane "20 0.995 200 2400" "100 0.995 200 2400" "200 0.995 200 2400" "400 0.995 200 2400" "1000 0.995 200 2400" "2000 0.995 200 2400" &
lane "50 0.998 200 2400" "250 0.998 200 2400" "500 0.998 200 2400" "1000 0.998 200 2400" "2500 0.998 200 2400" &
lane "500 0.99 320 4000" "4000 0.995 200 2400" &
wait; echo DONE > rrmi_out/DONE
