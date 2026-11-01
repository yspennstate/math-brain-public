"""Independent integer-radical and Boolean reconstruction, no check.py import."""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import json, time
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A085-independent-integer-radical-v1','family':'AND2 exact spectrum; incoming compatible reference brackets','parameter_domain':'m=4..160 fixed','case_count':157,'symmetry':'none','arithmetic':'integer squares and Fraction','memory_estimate_mb':40,'maximum_runtime_seconds':20}
(R/'out/INDEPENDENT_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
t0=time.perf_counter(); count=0
def ck(x):
 global count
 count+=1
 assert x, count
 assert time.perf_counter()-t0<20
rows=json.loads((R/'out/DYADIC_BRACKETS.json').read_text(encoding='utf-8'))
first=None
for row in rows:
 m=row['m']; D=1<<m
 k=(7*D-isqrt(24*D*D))//12
 if (7*D-12*k)**2<24*D*D: k-=1
 ck(7*D-12*(k+1)>0)
 ck((7*D-12*k)**2>24*D*D>(7*D-12*(k+1))**2)
 low=Fraction(k,D); high=Fraction(k+1,D)
 ck(str(low)==row['lo'] and str(high)==row['hi'])
 # Integer polynomial directly on numerator; no log or radical approximation.
 def v(j): return 27*j*(3*D-4*j)**2-25*D**3
 ck(v(k)<0<v(k+1))
 ck((float(low)==float(high))==row['same_binary64'])
 if float(low)==float(high) and first is None: first=m
ck(first==58)
# Tensor-product characters explicitly, separate from parity-mask transform.
inputs=[(-1,-1),(-1,1),(1,-1),(1,1)]
vals=[-1,1,1,1]
coefs=[]
for choose in [(0,0),(0,1),(1,0),(1,1)]:
 v=sum(y*(x[0] if choose[0] else 1)*(x[1] if choose[1] else 1) for x,y in zip(inputs,vals))
 coefs.append(Fraction(v,4))
ck([x*x for x in coefs]==[Fraction(1,4)]*4)
ck(sum((sum(ch) * c*c for ch,c in zip([(0,0),(0,1),(1,0),(1,1)],coefs)),Fraction(0))==1)
for sigma in [-1,1]:
 child=[vals[inputs.index((sigma,x))] for x in [-1,1]]
 c0=Fraction(sum(child),2);c1=Fraction(child[1]-child[0],2)
 ck(sorted([c0*c0,c1*c1])==[0,1])
out={'status':'PASS','exact_assertions':count,'brackets':len(rows),'first_binary64_alias':first,'seconds':time.perf_counter()-t0,'imports_primary_or_author_code':False}
(R/'out/INDEPENDENT_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
