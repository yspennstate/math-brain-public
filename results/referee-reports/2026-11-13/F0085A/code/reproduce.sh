#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1
python3 code/check_numerics.py > data/numerical_checks.json
python3 code/check_constants.py
python3 code/torus_allocation.py --L 32 --resolution 8 --seeds 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 --alphas .2 .4 .55 .6 .65 .675 .7 .725 .75 .8 .9 .95 --output torus_L32_r8.csv > data/progress_L32_r8.jsonl
python3 code/torus_allocation.py --L 64 --resolution 8 --seeds 100 101 102 103 104 105 106 107 108 109 110 111 --alphas .2 .4 .55 .6 .65 .675 .7 .725 .75 .8 .9 .95 --output torus_L64_r8.csv > data/progress_L64_r8.jsonl
python3 code/torus_allocation.py --L 96 --resolution 8 --seeds 100 101 102 103 104 105 106 107 --alphas .2 .4 .55 .6 .65 .675 .7 .725 .75 .8 .9 .95 --output torus_L96_r8.csv > data/progress_L96_r8.jsonl
python3 code/torus_allocation.py --L 64 --resolution 16 --seeds 100 101 102 103 104 105 106 107 --alphas .2 .4 .55 .6 .625 .65 .675 .7 .725 .75 .8 .9 .95 --output torus_L64_r16.csv > data/progress_L64_r16.jsonl
python3 code/summarize.py > data/summary_progress.txt
python3 code/plot_results.py
python3 code/audit_artifacts.py
