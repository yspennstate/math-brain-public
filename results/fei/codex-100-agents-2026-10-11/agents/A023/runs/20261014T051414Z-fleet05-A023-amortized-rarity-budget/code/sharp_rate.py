from pathlib import Path
from fractions import Fraction as Q
import json,importlib.util,time
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
sp=importlib.util.spec_from_file_location('own_exact',ROOT/'runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget/code/check_block.py');h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
start=time.perf_counter();best=None;winner=None;ties=0;comparisons=0
rows=json.loads((RUN/'out/results.json').read_text())
for row in rows:
    ic=Q(row['control_I'])
    if not ic:continue
    e={int(p):Q(c) for p,c in row['actual_entropy_increment'].items()}
    ratio=h.add((1/ic,e),(-1/ic,h.rational(Q(row['R_star']))))
    if best is None:best=ratio;winner=row;ties=1
    else:
        sign=h.sign(h.add((1,ratio),(-1,best)));comparisons+=1
        if sign>0:best=ratio;winner=row;ties=1
        elif sign==0:ties+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen sixty-second postprocess cap')
upper=None
for k in range(1,12):
    if h.sign(h.add((1,best),(-1,h.rational(Q(k,2)))))<=0:upper=Q(k,2);break
assert upper is not None
out={'status':'PASS','cases':len(rows),'exact_ratio_vector':{str(p):str(c) for p,c in best.items()},
    'extremizer':winner,'ties':ties,'rational_upper':str(upper),
    'comparisons':comparisons,'certificates':len(h.SIGNS),'elapsed_seconds':time.perf_counter()-start,
    'scope':'Exactly saved finite domain; no universal rate'}
(RUN/'out/sharp_rate.json').write_text(json.dumps(out,indent=2)+'\n')
(RUN/'out/rate_certificates.json').write_text(json.dumps(list(h.SIGNS.values()),indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['extremizer','exact_ratio_vector']}))
