"""Separate rational reconstruction; no import of the symbolic curve producer."""
import datetime
import hashlib
import json
import pathlib
import math
import time
from fractions import Fraction as F
import uniform_local_fast_independent_check as q

ROOT=pathlib.Path(__file__).resolve().parent
name='c5over4_Lhalf'
started=time.monotonic()
def load(phase):
    d=json.loads((ROOT/f'local_curve_{name}_{phase}.json').read_text())
    return {tuple(e):F(v) for e,v in d['poly']},d
raw,meta=load('raw')
C,L,delta=map(F,(meta['C'],meta['lambda_upper'],meta['retained_drift_fraction']))
current=raw;scales=[]
for axis in (0,1):
    nxt,_=load('bern'+str(axis+1))
    scales.append(q.axis_check(current,nxt,axis,meta['degrees'][axis]));current=nxt
assert all(v>0 for v in current.values())
assert len(current)==127
# Reconstruct quadratic dependence on M from three exact scalar values.
# The independently written unsummed ledger has degree<=2 in M, by its
# displayed expression P=(1-delta)gD^3-M A-M^2 B.
p0=q.expected_numerator(F(0),delta)
pp=q.expected_numerator(F(1),delta)
pm=q.expected_numerator(F(-1),delta)
p1=q.scale(q.add(pp,q.scale(pm,-1)),F(1,2))
p2=q.scale(q.add(pp,pm,q.scale(p0,-2)),F(1,2))
minus=q.add(q.ONE,q.scale(q.ELL,-1));plus=q.add(q.ONE,q.ELL)
m=q.scale(q.mul(minus,minus),C)
expected=q.add(p0,q.mul(m,p1),q.mul(m,m,p2))
restored={key:v*F(meta['raw_content_divided_out'])/F(meta['raw_common_multiplier'])/L**key[0]
          for key,v in raw.items()}
D=q.add(q.ONE,q.scale(q.mul(q.ELL,q.ELL),-1))
den={(0,0):F(meta['denominator_content'])}
for factor,poly in (('l',q.ELL),('1-l',minus),('1+l',plus)):
    for _ in range(meta['denominator_factors'][factor]):den=q.mul(den,poly)
assert q.mul(restored,D,D,D)==q.mul(den,expected)
checks=[]
for d in (4,9,16,25,49,100,225,400):
    ell=F(1,math.isqrt(d));assert ell<=L
    M=C*(1-ell)**2
    for k in sorted({2,3,d//2,d}):
        if k<2:continue
        A,B,g=q.direct_recursion(d,k)
        gap=(1-delta)*g-M*A-M*M*B
        assert gap>=0
        rr=F(k-2,d-2)
        assert q.evaluate(expected,ell,rr)==(1-ell*ell)**3*gap
        checks.append({'d':d,'k':k,'M':str(M),'gap':str(gap)})
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'status':'PASS same-worker separate rational reconstruction; no independent mathematical audit',
     'C':str(C),'lambda_upper':str(L),'margin':str(delta),
     'full_cross_multiplied_polynomial_identity':True,
     'degrees':meta['degrees'],'positive':len(current),
     'implicit_zeros':(meta['degrees'][0]+1)*(meta['degrees'][1]+1)-len(current),
     'axis_scales':scales,'unsummed_controls':checks,
     'seconds':time.monotonic()-started,
     'sha256':{f'local_curve_{name}_{phase}.json':hashlib.sha256((ROOT/f'local_curve_{name}_{phase}.json').read_bytes()).hexdigest()
               for phase in ('raw','bern1','bern2','report')}}
for source in ('replay_local_curve.py','uniform_local_fast_independent_check.py'):
    out['sha256'][source]=hashlib.sha256((ROOT/source).read_bytes()).hexdigest()
path=ROOT/'local_curve_c5over4_Lhalf_replay.json';assert not path.exists()
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ('status','degrees','positive','implicit_zeros','seconds')}),flush=True)
