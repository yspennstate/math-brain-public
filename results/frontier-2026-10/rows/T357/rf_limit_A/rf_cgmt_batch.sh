#!/bin/bash
# T357 finite-alpha RF fixed point: (1) the rf_cross_run1 grid (d 200, alpha 3, beta 2, N/d 0.5-8, rf_cross's own F seeds);
# (2) the alpha sweep at d 1000, N/d 1, beta 2 and 5, one F draw.
# 17:4x 20 Oct: relaunched without nice (BelowNormal starved it to ~7 pct of a core on a saturated box); psi 1 already done.
cd "$(dirname "$0")"
for psi in 0.5 2 3 4 8; do python rf_cgmt.py 2 3 $psi 200 3 > rf_cgmt_b2_a3_psi${psi}_d200.txt 2>&1; done
for b in 2 5; do for a in 3 10 30 100 300 1000; do python rf_cgmt.py $b $a 1 1000 1 > rf_cgmt_b${b}_a${a}_psi1_d1000.txt 2>&1; done; done
echo done > rf_cgmt_batch.done
