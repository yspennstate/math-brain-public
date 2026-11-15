"""Compare conditioned configurations with exact enumeration and direct G(n,m)."""
import collections
import csv
import itertools
import json
import random
import subprocess
from pathlib import Path
from scipy.stats import chisquare

ROOT = Path(__file__).resolve().parents[1]
n,m,reps = 6,10,20000
edges = list(itertools.combinations(range(n),2))
def eligible(mask):
    d = [0]*n
    for j,(u,v) in enumerate(edges):
        if mask >> j & 1:
            d[u] += 1
            d[v] += 1
    return min(d) >= 3
support = []
for ix in itertools.combinations(range(len(edges)),m):
    mask = sum(1<<j for j in ix)
    if eligible(mask):
        support.append(mask)
raw = subprocess.check_output(['code/sim_check','samplecheck',str(n),str(m),str(reps),'960666'])
(ROOT/'data/sampler_check.csv').write_bytes(raw)
observed = collections.Counter(int(r['mask']) for r in csv.DictReader(raw.decode().splitlines()))
assert set(observed) <= set(support)
stat,pvalue = chisquare([observed[x] for x in support])
rng = random.Random(961234)
direct = collections.Counter()
tries = 0
while sum(direct.values()) < reps:
    tries += 1
    mask = sum(1<<j for j in rng.sample(range(len(edges)),m))
    if eligible(mask):
        direct[mask] += 1
stat2,pvalue2 = chisquare([direct[x] for x in support])
output = dict(n=n,m=m,reps=reps,support_size=len(support),configuration_chisquare=float(stat),configuration_pvalue=float(pvalue),direct_chisquare=float(stat2),direct_pvalue=float(pvalue2),direct_attempts=tries,counts={str(x):dict(configuration=observed[x],direct=direct[x]) for x in support})
(ROOT/'data/sampler_check.json').write_text(json.dumps(output,indent=2))
print(json.dumps({k:v for k,v in output.items() if k!='counts'},indent=2))
