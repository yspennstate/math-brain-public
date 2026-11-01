#!/bin/bash
cd "$(dirname "$0")"
for obj in L3 L3tail L4 T1 L6 L5 pw_a pw_c; do
  for n in 9 11; do
    timeout 1200 python anneal_lemmas.py $obj $n 1500 $((n*7+1)) > ../logs/anneal_${obj}_n${n}.log 2>&1
  done
done
echo done > ../logs/anneal_batch.done
