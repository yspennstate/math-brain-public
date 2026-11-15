#!/bin/zsh
# Run from the F0129A directory. Every numerical job runs sequentially.
set -eu
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1
clang++ -O3 -std=c++17 code/polymer.cpp -o code/polymer
code/polymer --self-test > data/self_test.txt
code/polymer data/main.csv 0.02 0.05 8192 48 0.02 129000 > data/main.stdout.txt 2> data/main.stderr.txt
code/polymer data/refine_coarse.csv 0.02 0.05 1024 32 0.005 229000 > data/refine_coarse.stdout.txt 2> data/refine_coarse.stderr.txt
code/polymer data/refine_space.csv 0.02 0.025 1024 32 0.005 229000 > data/refine_space.stdout.txt 2> data/refine_space.stderr.txt
code/polymer data/refine_fine.csv 0.005 0.025 1024 32 0.005 229000 > data/refine_fine.stdout.txt 2> data/refine_fine.stderr.txt
POLYMER_KERNELS=annular,bump code/polymer data/stiff_refine.csv 0.0005 0.025 1024 32 0.0005 329000 > data/stiff_refine.stdout.txt 2> data/stiff_refine.stderr.txt
POLYMER_KERNELS=zero,sign,spline,bump,two_bump code/polymer data/main_fine.csv 0.005 0.025 8192 64 0.005 429000 > data/main_fine.stdout.txt 2> data/main_fine.stderr.txt
POLYMER_KERNELS=annular code/polymer data/annular_short.csv 0.00005 0.0125 256 32 0.00005 529000 > data/annular_short.stdout.txt 2> data/annular_short.stderr.txt
python3 code/audit_math.py > data/math_audit.stdout.txt
python3 code/analyze.py > data/analysis.stdout.txt
