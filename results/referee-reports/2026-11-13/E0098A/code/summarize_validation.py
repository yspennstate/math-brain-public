"""Report the independent-seed, adaptively selected Bernoulli validation separately."""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import collections
import csv
import math
from pathlib import Path
import numpy as np
from scipy.stats import kstest

ROOT=Path(__file__).resolve().parents[1]
groups=collections.defaultdict(list)
for row in csv.DictReader((ROOT/'data/validation_samples.csv').open()):
    groups[(int(row['n']),row['region'])].append(float(row['scaled_min']))
summary=[]
for (n,region),values in sorted(groups.items()):
    x=np.array(values)
    test=kstest(x,'expon',args=(0,math.sqrt(math.pi/2)))
    row=dict(n=n,region=region,samples=len(x),mean=float(x.mean()),
        mean_se=float(x.std(ddof=1)/math.sqrt(len(x))),
        ks_distance=float(test.statistic),ks_pvalue=float(test.pvalue))
    summary.append(row)
    print(row)
with (ROOT/'data/validation_summary.csv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(summary[0]))
    writer.writeheader()
    writer.writerows(summary)
