"""Sequential, seeded Monte Carlo. Each row is saved as soon as it completes."""
import csv
import subprocess
from pathlib import Path

header = ['family','n','alpha','level','reps','seed','gaussian','mean','se','mean_over_n','se_over_n']
jobs = []
# Small cases cross-check the actual simulator against exact equations.
for fam, alpha in [('BR',0), ('BR',1), ('FP',-1)]:
    jobs.append((fam,8,alpha,60000,0))
for n, reps in [(64,20000),(256,15000),(1024,10000),(4096,5000),(16384,2500),(65536,1200)]:
    for fam, alpha in [('BR',0),('BR',1),('FP',-1)]:
        jobs.append((fam,n,alpha,reps,0))
# Gaussian increments: sampled Slepian crossing, giving a discretization-biased
# approximation from above to the bridge constant. These are not certified bounds.
for n, reps in [(256,15000),(1024,12000),(4096,8000)]:
    for alpha in (0,1):
        jobs.append(('BR',n,alpha,reps,1))
with Path('data/monte_carlo.csv').open('w') as f:
    f.write(','.join(header)+'\n')
    for i, (family,n,alpha,reps,gaussian) in enumerate(jobs):
        seed=820000+i
        row=subprocess.check_output(['code/simulate',family,str(n),str(alpha),str(reps),str(seed),str(gaussian)],text=True)
        f.write(row); f.flush()
        print(row.strip(),flush=True)
