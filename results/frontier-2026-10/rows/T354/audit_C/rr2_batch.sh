#!/bin/bash
cd "$(dirname "$0")"
out=rr2_runs.txt
python -X utf8 rr_exact_two_special.py 0.5 0.999 9 -1 -1 >> $out
for b1 in 0 0.5 0.9; do for b2 in 0.9995 0.999 0.998; do
python -X utf8 rr_exact_two_special.py $b1 $b2 6 2 -1 >> $out
done; done
python -X utf8 rr_exact_two_special.py 0 0.999 6 2 -1 240 >> $out
echo DONE >> $out
