"""Exact feasibility only: Mstar(l)=C(1-l)^2 in the canonical prefix criterion.

Never edits constant-radius producers/certificates. A negative Bernstein
coefficient is inconclusive, not a counterexample to nonreconstruction.
"""
import argparse
import hashlib
import json
import pathlib
import time
from fractions import Fraction as F
import sympy as sp
from uniform_local_certificate import coefficients, integer_coefficients, bernstein_axis, memory_check

ROOT=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('--C',default='5/4')
p.add_argument('--lambda-max',default='1/2')
p.add_argument('--margin',default='1/1000')
p.add_argument('--name',required=True)
a=p.parse_args()
assert not (ROOT/f'local_curve_{a.name}_report.json').exists()
memory_check();started=time.monotonic()
C,L,delta=map(F,(a.C,a.lambda_max,a.margin))
assert C>0 and 0<L<1 and 0<delta<1
l,r,z=sp.symbols('l r z')
d=1/l**2;k=2+r*(d-2)
A,B,g,_,_=coefficients(d,k,l)
m=sp.Rational(C.numerator,C.denominator)*(1-l)**2
gap=sp.cancel((1-sp.Rational(delta.numerator,delta.denominator))*g-m*A-m*m*B)
num,den=sp.fraction(gap)
content,factors=sp.factor_list(den,l)
assert content>0
sign=1;exponents={'l':0,'1-l':0,'1+l':0}
for factor,power in factors:
    if factor==l:exponents['l']+=power
    elif factor==l-1:exponents['1-l']+=power;sign*=(-1)**power
    elif factor==l+1:exponents['1+l']+=power
    else:raise AssertionError(('unexpected denominator',factor,power))
if sign<0:num=-num
positive_den=abs(content)*l**exponents['l']*(1-l)**exponents['1-l']*(1+l)**exponents['1+l']
assert sp.cancel(num-positive_den*gap)==0
poly=sp.Poly(sp.expand(num.subs(l,sp.Rational(L.numerator,L.denominator)*z)),z,r)
degrees=tuple(poly.degree(x) for x in (z,r))
raw,raw_common,raw_content=integer_coefficients(poly)
meta={'C':str(C),'M_expression':'C*(1-lambda)^2','lambda_upper':str(L),
      'retained_drift_fraction':str(delta),'degrees':degrees,
      'denominator_content':str(abs(content)),'denominator_factors':exponents,
      'raw_common_multiplier':str(raw_common),'raw_content_divided_out':str(raw_content)}
current=raw;phase_summaries=[]
for phase,axis in (('raw',None),('bern1',0),('bern2',1)):
    if axis is not None:
        current,common,content=bernstein_axis(current,axis,degrees[axis])
    doc=dict(meta,phase=phase,poly=[[list(e),v] for e,v in sorted(current.items())])
    (ROOT/f'local_curve_{a.name}_{phase}.json').write_text(json.dumps(doc,separators=(',',':')),encoding='utf-8')
    phase_summaries.append({'phase':phase,'terms':len(current),
                            'negative':sum(v<0 for v in current.values())})
    print(json.dumps(phase_summaries[-1]),flush=True)
report=dict(meta,status='PASS coefficient inequality only' if all(v>=0 for v in current.values()) else 'INCONCLUSIVE Bernstein representation',
            positive=sum(v>0 for v in current.values()),negative=sum(v<0 for v in current.values()),
            implicit_zeros=(degrees[0]+1)*(degrees[1]+1)-len(current),
            seconds=time.monotonic()-started,
            source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
(ROOT/f'local_curve_{a.name}_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report),flush=True)
