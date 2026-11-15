"""Monte Carlo audit of the degree-3 edge-count change under cycle planting."""
import json
import math
import os
from pathlib import Path
import resource
import struct
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(960333)
results = []
for tag in ('155','175'):
    raw = (ROOT / f'data/sweep_n100000_c{tag}_0.bin').read_bytes()
    n,m = struct.unpack_from('=ii',raw)
    e = np.frombuffer(raw,dtype=np.int32,offset=8).reshape(-1,2)
    d = np.bincount(e.ravel(),minlength=n)
    S = (d == 3)
    u = int(S.sum())
    D = 2*m
    R = D-2*n
    # Membership flags suffice: stub labels within a degree class are irrelevant.
    original_flags = np.repeat(S,d)
    residual_flags = np.repeat(S,d-2)
    observed = []
    planted = []
    for _ in range(100):
        f = rng.permutation(original_flags)
        observed.append(int(np.count_nonzero(f[0::2] & f[1::2])))
        red = rng.permutation(S)
        f = rng.permutation(residual_flags)
        planted.append(int(np.count_nonzero(red & np.roll(red,1)))+int(np.count_nonzero(f[0::2] & f[1::2])))
    mean_p = (3*u)*(3*u-1)/(2*(D-1))
    mean_q = u*(u-1)/(n-1)+u*(u-1)/(2*(R-1))
    row = dict(n=n,m=m,u=u,repetitions=100,P_expected=mean_p,Q_expected=mean_q,gap=mean_q-mean_p)
    for label,values,pred in (('P',observed,mean_p),('Q',planted,mean_q)):
        mean = float(np.mean(values))
        se = float(np.std(values,ddof=1)/math.sqrt(len(values)))
        row[label+'_observed_mean'] = mean
        row[label+'_standard_error'] = se
        row[label+'_zscore'] = (mean-pred)/se
        row[label+'_observations'] = values
    results.append(row)
(ROOT / 'data/planted_check.json').write_text(json.dumps(dict(seed=960333,results=results,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,priority=os.getpriority(os.PRIO_PROCESS,0)),indent=2))
print(json.dumps([{k:v for k,v in r.items() if not k.endswith('observations')} for r in results],indent=2))
