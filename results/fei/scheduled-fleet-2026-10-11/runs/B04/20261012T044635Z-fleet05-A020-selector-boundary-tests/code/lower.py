"""Exact a=3 lower domains via own saved rational verifier; no five-bit extrapolation."""
from pathlib import Path
import importlib.util,json,time
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
source=ROOT.parents[0]/'20261011T225608Z-fleet05-A020-selector-boundary-tests'/'code'/'verify.py'
sp=importlib.util.spec_from_file_location('previous_a020',source);v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
started=time.perf_counter();results=[]
for m in [0,1]:
    count=1<<(1<<(3+m));zero=0;mindiff=None
    l2,h2=v.lnint(2)
    for mask in range(count):
        r=v.analyze(mask,3,m);s=Q(r['selector_influence']);oldlo,oldhi=[Q(t) for t in r['bound_nats_interval']]
        newlo=oldlo-2*s+min(3*Q(l2,v.SCALE),2*s)
        dhi=Q(r['delta_nats_interval'][1])
        if s:
            margin=Q(9,10)*newlo-dhi;assert margin>0
            mindiff=margin if mindiff is None else min(mindiff,margin)
        else:zero+=1
    row=dict(a=3,m=m,cases=count,zero_influence=zero,certified_ratio_cap='9/10',min_positive_cap_margin_nats=str(mindiff))
    results.append(row);(ROOT/'out'/'lower_domains.json').write_text(json.dumps(dict(domains=results,runtime_seconds=time.perf_counter()-started),indent=2));print(json.dumps(row),flush=True)
