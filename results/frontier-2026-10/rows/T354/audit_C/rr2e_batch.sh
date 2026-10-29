#!/bin/bash
cd "$(dirname "$0")"
out=rr2e_runs.txt
for eps in 1 10; do for b1 in 0 0.5 0.9; do for b2 in 0.9995 0.999 0.998; do
python -X utf8 rr_exact_two_special_eps.py $b1 $b2 $eps 6 2 -1 >> $out
done; done; done
python -X utf8 rr_exact_two_special_eps.py 0 0.999 10 6 2 -1 240 >> $out
echo DONE >> $out
