"""Frozen follow-up: independent exact local seed and original bank checks."""
from pathlib import Path
from fractions import Fraction as F
import json, time
from check_reference import walsh, chi, log, add, mul, ent, eq
root=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
g=[-1]+[1]*7; bh=walsh(g); P=[x*x for x in bh]
assert bh==[F(3,4)]+[F(-1,4)]*7; checks+=1
assert ent(P)==add(mul(4,log(F(2))),mul(F(-9,8),log(F(3)))); checks+=1
for v in range(8):
    ell=[mul(-1,log(p)) for p in P]
    J=add(mul(F(1,8),add(*ell)),mul(-g[v],add(*(mul(bh[s]*chi(s,v),ell[s]) for s in range(8)))))
    assert J==mul(F(-7,4) if v==0 else F(5,4),log(F(3))); checks+=1
    edge=sum(g[v]*g[v^(1<<i)] for i in range(3))
    assert edge==(-3 if v==0 else 1 if v.bit_count()==1 else 3); checks+=1
assert 3**9>2**14 and 3**5<2**8; checks+=2
for t in range(2,21):
    for alpha in [F(0),F(1,16),F(1,4),F(1,2),F(3,4),F(1)]:
        for U in [F(0),F(t,128),F(t,64)]:
            assert F(3*t,4)-F(alpha,8**t)*(44*t+6)-U>=0; checks+=1
result={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,
        'domain':'g local all 8 vertices; t=2..20, six alpha endpoints/interior values, three old-booking values; integer log inequalities',
        'arithmetic':'exact Fraction, formal prime logs, integers',
        'rung':'all-dimensional analytic proof in REPORT; this finite replay is author verification'}
(root/'out/bank_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
