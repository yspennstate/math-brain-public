#!/bin/bash
# Balanced-ratio annealing over many transitive groups (sequential: one heavy process at a time).
cd "$(dirname "$0")"
LOG=../logs/anneal_batch1.log
for G in Z8 Z9 Z10 Z11 Z12 Z13 Z14 K5 K6 B34 B44 B35 W44 W35 W53 W45 W54 AGL11 AGL13 AGL17 AGL19 PSL7 PSL11 PSL13 PSL17 PSL19 T4 K33x2 Z15 Z16 H3_6; do
  python anneal.py $G bal 150000 4 1 0.05 >> $LOG 2>&1
done
echo BATCH1 DONE >> $LOG
