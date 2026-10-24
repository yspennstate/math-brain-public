"""Exact independent leading-term audit of the written all-m limit."""
from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parents[1]
def plus(a,b):
    d=dict(a)
    for k,v in b.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def times(a,b):
    d={}
    for i,x in a.items():
        for j,y in b.items():d[i+j]=d.get(i+j,F(0))+x*y
    return {k:v for k,v in d.items() if v}
class Q:
    def __init__(self,n,d=None):self.n=n if isinstance(n,dict) else ({0:F(n)} if n else {});self.d={0:F(1)} if d is None else d
    def __add__(a,b):
        if not isinstance(b,Q):b=Q(b)
        return Q(plus(times(a.n,b.d),times(b.n,a.d)),times(a.d,b.d))
    __radd__=__add__
    def __neg__(a):return Q({k:-v for k,v in a.n.items()},a.d)
    def __sub__(a,b):return a+-asq(b)
    def __rsub__(a,b):return asq(b)+-a
    def __mul__(a,b):b=asq(b);return Q(times(a.n,b.n),times(a.d,b.d))
    __rmul__=__mul__
    def __truediv__(a,b):b=asq(b);assert b.n;return Q(times(a.n,b.d),times(a.d,b.n))
    def __rtruediv__(a,b):return asq(b)/a
    def __pow__(a,n):
        out=Q(1)
        for _ in range(n):out=out*a
        return out
def asq(x):return x if isinstance(x,Q) else Q(x)
def leading(q):
    assert q.n and q.d
    i,j=min(q.n),min(q.d)
    return i-j,q.n[i]/q.d[j]
s=Q({1:F(1)});e=s*s;k=1-s;mu=1-2*s;v=4*s*(1-s)
Rj=v*(1-s**2-s**6)+4*s**8
beta=2*(1-2*s)/(s**2*(1-s+s**4*(1-2*s)))
qj=s**2*(4-3*s);u=k*Rj+s**3
p0=(1-4*s+2*s**2)**2;o0=(mu+s**2)**2+u*(2*s-s**2)**2/qj
ar=(k*8*s**8+2*s**3)/(k*beta*8*s**8+4*s**3)
dr=(k*v*s**2+2*s**3)/(k*beta*v*s**2+4*s**3)
cr=(1+u/qj)/4
tests=[('o0-1',o0-1,(2,F(-3))),('p0-1',p0-1,(1,F(-8))),('beta',beta,(-2,F(2))),('u',u,(1,F(4))),('active_ratio',ar,(0,F(1,2))),('dummy_ratio',dr,(2,F(3,4))),('control_ratio',cr,(-1,F(1,4))),('control_mass',(1/s-1)*4*s**4,(3,F(4))),('active_mass',(1/(2*s)-1)*4*qj,(1,F(8))),('special_dummy_mass',4*s**3,(3,F(4))),('other_dummy_mass',(1/(2*s)-1)*4*s**3,(2,F(2)))]
out=[]
for name,q,target in tests:
    got=leading(q);assert got==target,(name,got,target)
    out.append({'name':name,'leading_exponent':got[0],'leading_coefficient':str(got[1])})
(R/'out/POLYNOMIAL_AUDIT.json').write_text(json.dumps({'status':'EXACT_PASS','assertions':len(tests),'rows':out},indent=2)+'\n',encoding='utf-8')
print('Exact polynomial leading-term audit:',len(tests),'PASS')
