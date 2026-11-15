#!/usr/bin/env python3
"""Audit all units and directions independently of the numerical optimizers."""
import json, math, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def entropy(q):return -q*math.log(q)-(1-q)*math.log1p(-q)
def first_moment_root(d):
    lo,hi=1e-16,.5
    for _ in range(90):
        q=(lo+hi)/2
        if entropy(q)<(1-2/d)*math.log(2):lo=q
        else:hi=q
    return d*(lo+hi)/4
rows=[]
for d in [3,4,5]:
    alpha=first_moment_root(d)
    lyons_min=d/(2*math.pi)*math.acos(2*math.sqrt(d-1)/d)
    a={'d':d,'target':d/2,'first_moment_min_lower':alpha,'first_moment_max_upper':d/2-alpha,'lyons_min_upper':lyons_min,'lyons_max_lower':d/2-lyons_min}
    upper_fraction={3:.923868,4:.867902,5:.834638}[d]
    a['max_upper_edge_fraction']=upper_fraction;a['max_upper']=upper_fraction*d/2
    a['min_upper']={3:.139822,4:1/3,5:.496488}[d]
    a['min_lower']={3:.103295,4:alpha,5:alpha}[d]
    a['max_lower']=d/2-lyons_min
    a['sum_lower']=a['max_lower']+a['min_lower'];a['sum_upper']=a['max_upper']+a['min_upper']
    a['contradiction']=a['sum_upper']<d/2 or a['sum_lower']>d/2
    assert not a['contradiction']
    rows.append(a)
(ROOT/'data'/'bounds_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(json.dumps(r))
