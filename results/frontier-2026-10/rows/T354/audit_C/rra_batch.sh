#!/bin/bash
# Exact roots for the unequal-curvature RR next-order term, eps 0 and 1 (agent C, 20 Oct 2026)
cd "$(dirname "$0")"
out=rra_runs.txt
rm -f $out rra_jobs.txt
for a in "4 0.5 0.5" "1 1 2" "0.5 2 1"; do for eps in 0 1; do for b1 in 0 0.9; do for b2 in 0.9995 0.999 0.998; do
echo "$b1 $b2 $eps 6 2 -1 $a" >> rra_jobs.txt
done; done; done; done
echo "0 0.999 1 6 2 -1 4 0.5 0.5 240" >> rra_jobs.txt
xargs -P 4 -L 1 python -X utf8 rr_exact_two_special_a.py < rra_jobs.txt >> $out
echo DONE >> $out
