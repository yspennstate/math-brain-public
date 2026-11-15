# Reproduce FEIB12

Use the Mac's Python 3 with NumPy, SciPy and mpmath, plus clang. All files are local to this folder. run.py fixes numerical libraries at one thread, verifies inherited priority and lowers it to nice 10 if needed, and appends elapsed time, priority, exit status and child peak resident set to runs.jsonl. The C census is single-threaded. Its largest allocation is a 256 MiB bitmap. The saved files occupy far less than 1 GB.

Compile and generate the census (run each line in this folder):

```sh
clang -O3 -Wall -Wextra census.c -o census
python3 run.py ./census 1 > census1.json 2> census1.log
python3 run.py ./census 2 > census2.json 2> census2.log
python3 run.py ./census 3 > census3.json 2> census3.log
python3 run.py ./census 4 > census4.json 2> census4.log
python3 run.py ./census 5 > census5.json 2> census5.log
python3 run.py python3 check.py > check.log 2>&1
python3 run.py python3 class_checks.py > class_checks.log 2>&1
python3 run.py python3 families.py > families.log 2>&1
python3 run.py python3 induction_lp.py > induction_lp.log 2>&1
python3 run.py python3 audit.py > audit.log 2>&1
python3 run.py python3 audit_families.py > families_audit.log 2>&1
python3 run.py python3 audit_lp.py > audit_lp.log 2>&1
python3 run.py python3 audit_large.py > large_audit.log 2>&1
python3 make_results.py
python3 final_audit.py
```

The scripts use fixed seeds. The census extrema are evaluated in binary64 and checked with a second implementation; exact_extrema.json uses rational character sums and 80-decimal-digit logarithms. High precision evaluates witnesses rather than certifying every floating-point comparison in the census. LP optimality checks are numerical primal/dual checks, not exact rational certificates. Changing the fitting corpus changes the meaning of its fitted constants.

npn*.bin files are little-endian uint32 truth tables, one canonical NPN representative per record, in increasing integer order. They are named npn1.bin through npn5.bin. census*.json are the numerical summaries. The n=5 representatives require only 2,464,504 bytes; the large orbit bitmap is transient RAM and is freed at exit. For each scientific statement's scope and limits, read PROOFS.md and REPORT.md.
