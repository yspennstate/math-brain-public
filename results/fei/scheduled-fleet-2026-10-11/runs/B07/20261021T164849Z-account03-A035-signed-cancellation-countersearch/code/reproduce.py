from fractions import Fraction as Q
from pathlib import Path
import json,itertools,time
START=time.perf_counter(); checks=0
def ck(v):
 global checks
 assert v;checks+=1
# Independent direct character sums: no transform, imported family or interval code.
def f(x):
 r,v,a,b,z=[(x>>h)&1 for h in range(5)]
 return (-1)**(r+a*b+(1-r)*(1-v)*(1-a)*(1-b)*z)
tab=[f(x) for x in range(32)]
for x in range(32):
 r,v,a,b,z=[(x>>h)&1 for h in range(5)]
 # Evaluate the original seven-bit family at private x0=0, core y0=1.
 p=(1+r)%2
 original=(-1)**(r+a*b+p*(1-v)*(1-a)*(1-b)*z)
 ck(tab[x]==original)
coef=[Q(sum(tab[x]*(-1)**((x&s).bit_count()%2) for x in range(32)),32) for s in range(32)]
ck(set(tab)=={-1,1});ck(sum(a*a for a in coef)==1)
for U in range(32):ck(sum(coef[s]*coef[s^U] for s in range(32))==(1 if U==0 else 0))
d=sum(coef[s]**2 for s in range(32) if s&16)
ck(d==Q(1,16));ck(coef[0]==-Q(1,16));ck(coef[16]==Q(1,16))
off=[s for s in range(16) if not s&1]
mu=sum(coef[s|16]**2/d for s in off)
ref=sum(coef[s]**2+coef[s|16]**2 for s in off)
ck(mu==Q(1,2));ck(ref==Q(1,16))
ck((mu/ref)*((1-mu)/(1-ref))==Q(64,15))
ck(Q(64,15)>4) # binary flag KL = log2(64/15)/2 > 1 bit
for s in off:ck(coef[s]==-coef[s|16])
I=sum(Q(sum(tab[x]!=tab[x^(1<<j)] for x in range(32)),32) for j in range(5))
ck(I==sum(s.bit_count()*a*a for s,a in enumerate(coef)))
out=dict(checks=checks,runtime_seconds=time.perf_counter()-START,dimension=5,d=str(d),signed_pair=[str(coef[0]),str(coef[16])],zero_core_mu=str(mu),zero_core_reference=str(ref),I=str(I),full_signed_convolution_shifts=32,binary_flag_KL='log2(64/15)/2 > 1',original_physical_reach='1/4',reached_flag_credit_lower_bound='1/64')
(Path(__file__).resolve().parents[1]/'out/reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
