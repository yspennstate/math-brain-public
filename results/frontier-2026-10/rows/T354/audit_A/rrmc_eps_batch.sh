#!/bin/bash
# eps 1 rows of NOTE "eps > 0 in closed form", by rrm_mc_cv_eps.py (seed 7, 4000 chains; epochs as in rrmc_batch.sh)
cd "$(dirname "$0")"
run() { n=$1; b2=$2; tag=$3
  me=$(python -c "import math;d=1-$b2;CT=8e7*(1e-4/0.002)**2*(0.1/d)**3;print(max(20,math.ceil(min(CT,2e9)/(4000*$n))))")
  python rrm_mc_cv_eps.py $n $b2 4000 $me 7 1 > rrmc_eps_out/${tag}_n${n}_b2${b2}.txt 2>&1; }
for job in 100:0.99 200:0.995 500:0.99 1000:0.995 1000:0.99 2000:0.995; do run ${job%%:*} ${job##*:} b91; done
export B=6,2,-1 P=0.1,0.1,0.8
for job in 100:0.99 200:0.995 400:0.9975 500:0.99 1000:0.995; do run ${job%%:*} ${job##*:} b621; done
echo DONE > rrmc_eps_out/DONE
