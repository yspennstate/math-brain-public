#!/bin/sh
# Reproducibility recipe. Each simulator is single threaded; commands are serial.
set -eu
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
python3 environment_check.py > environment_check.txt
clang -O2 -Wall -Wextra independent_sim.c -lm -o independent_sim
clang -O2 -Wall -Wextra synchronous_sim.c -lm -o synchronous_sim
python3 exact_checks.py > exact_checks.txt
python3 analytic_checks.py > analytic_checks.txt
./independent_sim cycle 4 1000 20000 384758 > cycles4_t1000.csv
./independent_sim cycle 6 1000 10000 671283 > cycles6_t1000.csv
./independent_sim cycle 10 1000 6000 107384 > cycles10_t1000.csv
./independent_sim cycle 20 1000 3000 207384 > cycles20_t1000.csv
./independent_sim cycle 50 1000 2000 507384 > cycles50_t1000.csv
./independent_sim cycle 100 1000 1000 1007384 > cycles100_t1000.csv
./independent_sim cycle 400 1000 200 4007384 > cycles400_t1000.csv
./independent_sim cycle 400 1000 1000 124007384 > cycles400_t1000_repeat.csv
./independent_sim cycle 4 10000 2000 4384758 > cycles4_t10000.csv
./independent_sim cycle 6 10000 2000 6671283 > cycles6_t10000.csv
./independent_sim cycle 10 10000 1000 10107384 > cycles10_t10000.csv
./independent_sim cycle 20 10000 500 20207384 > cycles20_t10000.csv
./independent_sim cycle 50 10000 400 50507384 > cycles50_t10000.csv
./independent_sim cycle 100 10000 200 10010073 > cycles100_t10000.csv
./independent_sim cycle 100 10000 1000 1210010073 > cycles100_t10000_repeat.csv
./independent_sim cycle 4 .25 100000 222345 > smallgraph_C4.csv
./independent_sim graph .25 100000 332345 > smallgraph_K4.csv
./independent_sim line 32768 1000 16 9918273 8192 > line32768.csv
./synchronous_sim 4 2000 10000 762783 > synchronous4.csv
./synchronous_sim 100 1000 1000 8762783 > synchronous100.csv
python3 vector_check.py > vector_check.txt
python3 summarize_checks.py > simulation_summary.txt
