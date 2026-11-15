#!/usr/bin/env python3
"""Check the explicit polygon family used in the diagonal coefficient bound."""
from itertools import permutations
from math import factorial
from pathlib import Path
import csv,json,time,resource
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic();checked=0
for m in range(2,9):
    count=0
    for tail in permutations(range(2,m+1)):
        word=tuple(range(1,m+1))+(-1,)+tuple(-j for j in tail)
        p=[0]*m;seen={tuple(p)}
        for i,a in enumerate(word,1):
            p[abs(a)-1]+=1 if a>0 else -1
            if i<2*m:
                assert tuple(p) not in seen
                seen.add(tuple(p))
            else:assert p==[0]*m
        count+=1
    assert count==factorial(m-1)
    checked+=count
with (ROOT/'data'/'lace_diagonal.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['m','walk_length','diagonal_coefficient_lower_bound'])
    for m in range(2,21):w.writerow([m,2*m,factorial(m-1)])
(ROOT/'data'/'lace_family_checks.json').write_text(json.dumps(dict(
    largest_m_checked=8,explicit_polygons_checked=checked,
    seconds=time.monotonic()-start,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    threads=1),indent=2)+'\n')
print('verified',checked,'explicit polygons for 2<=m<=8')
