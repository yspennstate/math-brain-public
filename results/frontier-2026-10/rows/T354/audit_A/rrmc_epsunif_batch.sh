#!/bin/bash
# audit 2 of the eps>0 remainder uniform in n: rrm_mc_cv_eps.py at small n and at eps 3 (seed 7, 4000 chains; epochs as in rrmc_batch.sh)
cd "$(dirname "$0")"
run() { eps=$1; n=$2; b2=$3
  me=$(python -c "import math;d=1-$b2;CT=8e7*(1e-4/0.002)**2*(0.1/d)**3;print(max(20,math.ceil(min(CT,2e9)/(4000*$n))))")
  python rrm_mc_cv_eps.py $n $b2 4000 $me 7 $eps > rrmc_epsunif_out/e${eps}_n${n}_b2${b2}.txt 2>&1; }
for job in 1:10:0.99 1:20:0.99 3:100:0.99 3:500:0.99 1:10:0.999 3:10:0.999; do IFS=: read e n b <<< "$job"; run $e $n $b; done
echo DONE > rrmc_epsunif_out/DONE
