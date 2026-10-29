#!/bin/bash
# n-sweep for rr_exact_m2.py, one output file per run (parallel appends to one file splice lines on Windows).
cd "$(dirname "$0")"
jobs=""
for d in 0.01 0.005 0.002; do
  for nd in 0.1 0.5 1 2 5; do
    n=$(python -c "print(int(round($nd/$d/10))*10)"); [ "$n" -lt 10 ] && continue
    b2=$(python -c "print(round(1-$d,6))")
    jobs="$jobs $n:$b2"
  done
done
jobs="$jobs 2000:0.99 1000:0.98"
echo $jobs | tr ' ' '\n' | xargs -P 2 -I{} bash -c 'n=${1%%:*}; b=${1##*:}; f=rrm_out/n${n}_b2${b}.txt; [ -s $f ] || python rr_exact_m2.py $n $b 0 > $f 2>&1' _ {}
for f in rrm_out/*.txt; do cat $f; done | sort -t' ' -k5,5 -k3,3n > rrm_runs.txt; echo DONE >> rrm_runs.txt
