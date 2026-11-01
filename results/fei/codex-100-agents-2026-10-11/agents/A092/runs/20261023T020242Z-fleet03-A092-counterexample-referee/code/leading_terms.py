"""Exact independent polynomial valuation audit; no symbolic library."""
from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def plus(p,q):return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def times(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
class R:
    def __init__(self,n,d=None):self.n=trim([F(n)] if isinstance(n,(int,F)) else n);self.d=trim([F(1)] if d is None else d)
    @staticmethod
    def cast(o):return o if isinstance(o,R) else R(o)
    def __add__(a,b):
        b=R.cast(b);return R(plus(times(a.n,b.d),times(b.n,a.d)),times(a.d,b.d))
    __radd__=__add__
    def __neg__(a):return R([-x for x in a.n],a.d)
    def __sub__(a,b):return a+-R.cast(b)
    def __rsub__(a,b):return R.cast(b)+-a
    def __mul__(a,b):
        b=R.cast(b);return R(times(a.n,b.n),times(a.d,b.d))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=R.cast(b);assert any(b.n);return R(times(a.n,b.d),times(a.d,b.n))
    def __rtruediv__(a,b):return R.cast(b)/a
    def __pow__(a,n):
        if n<0:return (R(1)/a)**(-n)
        r=R(1)
        for _ in range(n):r=r*a
        return r
    def lead(a):
        i=next(i for i,x in enumerate(a.n) if x);j=next(j for j,x in enumerate(a.d) if x)
        return i-j,a.n[i]/a.d[j]

tic=time.perf_counter();s=R([F(0),F(1)]);v=4*s*(1-s);k=1-s
Rj=v*(1-s**2-s**6)+4*s**8;u=k*Rj+s**3;qj=s**2*(4-3*s)
beta=2*(1-2*s)/(s*s*(1-s+s**4*(1-2*s)))
A=(1-2*s+s*s)**2;B=(2*s-s*s)**2;o=A+u*B/qj;p=(1-4*s+2*s*s)**2
fixtures=[('o0-1',o-1,2,F(-3)),('p0-1',p-1,1,F(-8)),
          ('fiber_mass-1',A+B-1,1,F(-4)),('vacuum_reset_ratio-1',o/p-1,1,F(8)),
          ('vacuum_refund_ratio-1',o/(A+B)-1,1,F(4)),('small_refund_ratio',qj/u,1,F(1)),
          ('group2_mass',(1/s-1)*4*s**4,3,F(4)),('group2_ratio',(1+u/qj)/4,-1,F(1,4)),
          ('group3_mass',(1/(2*s)-1)*4*qj,1,F(8)),
          ('group3_ratio',(k*8*s**8+2*s**3)/(k*beta*8*s**8+4*s**3),0,F(1,2)),
          ('group4_ratio',(k*v*s*s+2*s**3)/(k*beta*v*s*s+4*s**3),2,F(3,4)),
          ('group5_mass',(1/(2*s)-1)*4*s**3,2,F(2)),('B_mass',B,2,F(4))]
out=[]
for label,f,power,coefficient in fixtures:
    got=f.lead();assert got==(power,coefficient),(label,got)
    out.append({'expression':label,'leading_power':power,'leading_coefficient':str(coefficient)})
result={'status':'PASS','assertions':len(out),'leading_terms':out,'arithmetic':'exact rational polynomial numerator/denominator valuations',
        'runtime_seconds':time.perf_counter()-tic,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
root=Path(__file__).resolve().parents[1]
(root/'out/LEADING_TERMS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='leading_terms'}))
