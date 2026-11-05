#!/bin/sh
# extra T238 seeds: d=32 seeds 2-4 (n=256), d=24 seeds 5-6 (n=144); the source's window.py unchanged
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2
for s in 2 3 4; do python -u ../window.py 32 256 $s 1e-3,1e-2,0.1 > t238_runs/w_32_$s.txt 2>&1; done
for s in 5 6; do python -u ../window.py 24 144 $s 1e-3,1e-2,0.1 > t238_runs/w_24_$s.txt 2>&1; done
