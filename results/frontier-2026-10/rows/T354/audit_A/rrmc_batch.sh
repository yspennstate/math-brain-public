#!/bin/bash
# second audit of the large-n rows (agent_B/rrm_runs.txt), one output file per run
cd "$(dirname "$0")"
for job in 1000:0.98 500:0.99 100:0.99 10:0.99 200:0.99 2000:0.99 1000:0.995 500:0.998 50:0.998 2500:0.998 2500:0.98; do
  n=${job%%:*}; b2=${job##*:}
  me=$(python -c "import math;d=1-$b2;CT=8e7*(1e-4/0.002)**2*(0.1/d)**3;print(max(20,math.ceil(min(CT,2e9)/(4000*$n))))")
  python rrm_mc_cv.py $n $b2 4000 $me 7 > rrmc_out/n${n}_b2${b2}.txt 2>&1
done
echo DONE > rrmc_out/DONE
