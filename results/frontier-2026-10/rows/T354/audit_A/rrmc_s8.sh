#!/bin/bash
# reruns of the two n d 20 rows and n500 .99 at 4x the epochs of rrmc_batch.sh, seed 8
cd "$(dirname "$0")"
for job in 1000:0.98:80 500:0.99:400 2000:0.99:100; do
  IFS=: read n b2 me <<< "$job"
  python rrm_mc_cv.py $n $b2 4000 $me 8 > rrmc_out/n${n}_b2${b2}_s8.txt 2>&1
done
echo DONE > rrmc_out/DONE_s8
