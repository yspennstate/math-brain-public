"""Exact rational certificate: the determinant-product/parity span cannot certify K.

No floating point is used in the proof. Natural logarithms of positive rationals
are enclosed by an atanh series, then rounded outwards to 10^-20 rationals.
"""
from fractions import Fraction as F
from itertools import product
import json

class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def co(x): return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=I.co(x); return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self+-I.co(x)
    def __rsub__(self,x): return I.co(x)+-self
    def __mul__(self,x):
        x=I.co(x); z=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.co(x); assert not x.lo<=0<=x.hi
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x): return I.co(x)/self
    def square(self):
        return I(0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi),max(self.lo*self.lo,self.hi*self.hi))
    def bounds(self,digits=12):
        n=10**digits
        a=(self.lo*n).__floor__(); b=(self.hi*n).__ceil__()
        def st(v):
            sign='-' if v<0 else ''; v=abs(v)
            return f'{sign}{v//n}.{v%n:0{digits}d}'
        return [st(a),st(b)]

def log_series(y,N=32):
    assert F(1)<=y<=F(2)
    z=(y-1)/(y+1)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    err=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    return I(lo,lo+err)

def log_rat(x):
    x=F(x); assert x>0
    k=0
    while x<1: x*=2;k-=1
    while x>=2: x/=2;k+=1
    val=log_series(x)+k*log_series(F(2))
    n=10**20
    return I(F((val.lo*n).__floor__(),n),F((val.hi*n).__ceil__(),n))

def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def trace(a): return sum(a[i][i] for i in range(3))

def adj(a):
    # Transposed signed cofactors.
    out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            rr=[k for k in range(3) if k!=j]; cc=[k for k in range(3) if k!=i]
            row.append((-1)**(i+j)*(a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]))
        out.append(row)
    return out

K=[[F(z,1000) for z in row] for row in [[997,25,-29],[25,600,465],[-29,465,455]]]
IK=[[(int(i==j)-K[i][j]) for j in range(3)] for i in range(3)]
minorsK=[K[0][0],K[0][0]*K[1][1]-K[0][1]**2,det(K)]
minorsIK=[IK[0][0],IK[0][0]*IK[1][1]-IK[0][1]**2,det(IK)]
assert min(minorsK+minorsIK)>0
atoms=list(product([0,1],repeat=3)); probs={}
for x in atoms:
    Q=[[K[i][j]-int(i==j)*(1-x[i]) for j in range(3)] for i in range(3)]
    probs[x]=(-1)**(3-sum(x))*det(Q)
assert min(probs.values())>0 and sum(probs.values())==1
p0=probs[(0,0,0)]
d=[]; dr=[]
for i in range(3):
    j,k=[z for z in range(3) if z!=i]
    ej=tuple(int(z==j) for z in range(3));ek=tuple(int(z==k) for z in range(3))
    ejk=tuple(int(z in (j,k)) for z in range(3))
    ratio=probs[ej]*probs[ek]/(p0*probs[ejk]);dr.append(ratio)
    d.append(log_rat(ratio))
taurat=F(1)
# tau=sum (-1)^(3-|x|) [-log p_x]
for x,p in probs.items(): taurat*=p**((-1)**(4-sum(x)))
tau=log_rat(taurat)
assert tau.lo>0 and min(z.lo for z in d)>0
M=[[tau*K[i][j]+(d[i] if i==j else 0) for j in range(3)] for i in range(3)]
delta=det(M);assert delta.lo>0
raw=[]
for x in atoms:
    z=sum(d[j]*d[k]*x[i] for i,j,k in [(0,1,2),(1,0,2),(2,0,1)])
    z+=tau*sum(d[k]*x[i]*x[j] for i,j,k in [(0,1,2),(0,2,1),(1,2,0)])
    z+=tau.square()*x[0]*x[1]*x[2]
    raw.append(z/delta)
p=[probs[x] for x in atoms]
mean=sum(px*z for px,z in zip(p,raw))
g=[z-mean for z in raw]
hraw=[(-1)**(3-sum(x)) for x in atoms]
mu=sum(px*h for px,h in zip(p,hraw));h=[z-mu for z in hraw]
V=sum(px*z.square() for px,z in zip(p,g))
cv=sum(px*z*y for px,z,y in zip(p,g,h))
vh=sum(px*z*z for px,z in zip(p,h))
W=[[2*K[i][j]-int(i==j) for j in range(3)] for i in range(3)]
assert det(W)==mu
G=[[2*z for z in row] for row in adj(W)]
MG=matmul(M,G);trC=trace(MG);normC=trace(matmul(MG,MG))
J11=3+delta*V;J12=delta*cv+trC;J22=delta*vh+normC
Jdet=J11*J22-J12.square()
assert J11.lo>0 and Jdet.lo>0
u1=I(3);u2=trC
# A two-dimensional positive matrix is equivalent to u^T J^-1 u < 2.
B11=2*J11-u1.square();B12=2*J12-u1*u2;B22=2*J22-u2.square()
Bdet=B11*B22-B12.square()
assert B11.lo>0 and Bdet.lo>0
umin=(u1.square()*J22-2*u1*u2*J12+u2.square()*J11)/Jdet
minimum=3-umin
assert minimum.lo>F(1095,1000)
fixed=delta*V-delta.square()*cv.square()/J22
output={
 'proof_uses_floating_point':False,
 'K_leading_principal_minors':list(map(str,minorsK)),
 'I_minus_K_leading_principal_minors':list(map(str,minorsIK)),
 'atom_probabilities':{''.join(map(str,x)):str(p) for x,p in probs.items()},
 'd_log_arguments':list(map(str,dr)), 'tau_log_argument':str(taurat),
 'd_intervals':[z.bounds() for z in d], 'tau_interval':tau.bounds(),
 'delta_interval':delta.bounds(),
 'J_intervals':[[J11.bounds(),J12.bounds()],[J12.bounds(),J22.bounds()]],
 'u_intervals':[u1.bounds(),u2.bounds()],
 'J_determinant_interval':Jdet.bounds(),
 '2J_minus_uuT_first_diagonal_interval':B11.bounds(),
 '2J_minus_uuT_determinant_interval':Bdet.bounds(),
 'optimized_span_objective_interval':minimum.bounds(),
 'fixed_identity_plus_parity_objective_interval':fixed.bounds(),
 'exact_proof':'All endpoint arithmetic uses fractions.Fraction. Each logarithm uses 32 atanh-series terms, the explicit geometric tail bound, and outward rounding to denominator 10^20. Positive leading minors certify 0<K<I. Positive leading minors of 2J-uu^T prove min objective>1. The final interval strengthens this to >1.095.'
}
print(json.dumps(output,indent=2))
