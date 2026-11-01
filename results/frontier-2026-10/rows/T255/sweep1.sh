#!/bin/sh
# T255 sweep 1: n-convergence at m=4, then m and gamma^2 dependence (Feller prediction (m-1)^2 > 2 gam^2), V0 = I vs corr 0.2
o=chain_sweep1.txt; : > $o
for n in 2000 8000; do python -X utf8 chain_blowup.py 4 0.5 $n 10 400 2>&1 | tail -1 >> $o; done
for g in 0.2 0.5 0.9; do python -X utf8 chain_blowup.py 2 $g 2000 20 400 2>&1 | tail -1 >> $o; done
python -X utf8 chain_blowup.py 3 0.5 2000 20 400 2>&1 | tail -1 >> $o
python -X utf8 chain_blowup.py 8 0.5 2000 20 400 2>&1 | tail -1 >> $o
python -X utf8 chain_blowup.py 4 0.5 2000 10 400 0.0 2>&1 | tail -1 >> $o
python -X utf8 chain_blowup.py 4 0.9 2000 10 400 2>&1 | tail -1 >> $o
echo DONE >> $o
