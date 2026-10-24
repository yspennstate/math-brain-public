"""Exact self-checks for FOURIER_EXTENSION.md; Python standard library only.

The global proof is analytic. These checks independently verify its finite
algebraic core, Fourier-channel atom formula, and selected curvature values.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb
from pathlib import Path
import json
from verify_shuffle_obstruction import log_bounds, scale, enclose_decimal

NN = 6

class Poly:
    """Sparse rational polynomial in a,b,x,y,u,v."""
    def __init__(self, value=0):
        self.c = value if isinstance(value, dict) else {(0,)*NN: F(value)}
        self.c = {k:F(v) for k,v in self.c.items() if v}
    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = self.c.copy()
        for k,v in other.c.items(): out[k] = out.get(k,0)+v
        return Poly(out)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-v for k,v in self.c.items()})
    def __sub__(self,other): return self+-aspoly(other)
    def __rsub__(self,other): return aspoly(other)+-self
    def __mul__(self,other):
        other=aspoly(other);out={}
        for k,v in self.c.items():
            for l,w in other.c.items():
                q=tuple(a+b for a,b in zip(k,l));out[q]=out.get(q,0)+v*w
        return Poly(out)
    __rmul__=__mul__
    def __truediv__(self,other): return self*F(1,other)
    def __pow__(self,n):
        out=Poly(1)
        for _ in range(n):out=out*self
        return out
    def diff(self,i):
        out={}
        for k,v in self.c.items():
            if k[i]:
                q=list(k);q[i]-=1;out[tuple(q)]=v*k[i]
        return Poly(out)
    def at(self,values):
        ans=F(0)
        for k,v in self.c.items():
            for x,n in zip(values,k):v*=x**n
            ans+=v
        return ans


def aspoly(v):return v if isinstance(v,Poly) else Poly(v)
checks=[]
def identity(label,left,right):
    assert not (aspoly(left)-right).c,label
    checks.append(label)


def count(ps):
    out=[Poly(1)]
    for p in ps:
        nxt=[Poly() for _ in range(len(out)+1)]
        for i,q in enumerate(out):nxt[i]+=q*(1-p);nxt[i+1]+=q*p
        out=nxt
    return out


# Gaussian rationals as pairs: no floating-point complex arithmetic.
def ga(a,b):return (a[0]+b[0],a[1]+b[1])
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gd(M):
    ans=(F(0),F(0))
    for p in permutations(range(len(M))):
        z=(F((-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))),F(0))
        for i,j in enumerate(p):z=gm(z,M[i][j])
        ans=ga(ans,z)
    return ans


def logsum(terms,rational=F(0)):
    ans=[rational,rational]
    for coeff,arg in terms:
        lo,hi=scale(coeff,log_bounds(arg));ans[0]+=lo;ans[1]+=hi
    return ans


def main():
    variables=[]
    for i in range(6):
        k=[0]*6;k[i]=1;variables.append(Poly({tuple(k):1}))
    a,b,x,y,u,v=variables;r=x*x;s=y*y;A=a*(1-a);B=b*(1-b)
    lam=[a+x,b+y,a-x,b-y];slopes=[u,v,-u,-v]
    f=count(lam);q=[p/comb(4,k) for k,p in enumerate(f)]
    g=[Poly() for _ in range(4)];h=[Poly() for _ in range(3)]
    for i in range(4):
        for k,p in enumerate(count([lam[j] for j in range(4) if j!=i])):g[k]+=slopes[i]*p
        for j in range(4):
            if i==j:continue
            for k,p in enumerate(count([lam[l] for l in range(4) if l not in [i,j]])):h[k]+=slopes[i]*slopes[j]*p
    def d(p):return u*p.diff(2)+v*p.diff(3)
    for k in range(5):
        identity('first count derivative '+str(k),d(f[k]),(g[k-1] if k else 0)-(g[k] if k<4 else 0))
        identity('second count derivative '+str(k),d(d(f[k])),(h[k] if k<3 else 0)-2*(h[k-1] if 1<=k<=3 else 0)+(h[k-2] if k>=2 else 0))
    U=count([a+x,a-x]);V=count([b+y,b-y]);O=U[1]*V[1]/4
    P=(U[1]*V[1]+2*U[2]*V[0]+2*U[0]*V[2])/8
    Delta=2*(r+s-(a-b)**2);M11=B+s;M22=A+r;M12=2*x*y
    mw=M11*u*u+2*M12*u*v+M22*v*v
    identity('opposite atom',O,(A+r)*(B+s))
    identity('pair count mass',f[2],4*P+2*O)
    identity('imbalance',Delta,8*(O-P))
    identity('middle acceleration',h[1],-4*mw)
    identity('pair mass Hessian',d(d(f[2])),12*mw-2*(u*u+v*v))
    identity('imbalance Hessian',d(d(Delta)),4*(u*u+v*v))
    identity('positive matrix determinant decomposition',M11*M22-M12*M12,(A-r)*(B-s)+2*r*(B-s)+2*s*(A-r))
    identity('atom inequality decomposition',3*O*P*P-(2*P+O)*q[1]*q[3],O*(P*P-q[1]*q[3])+2*P*(O*P-q[1]*q[3]))

    # Independently reconstruct all atoms via exact Fourier projection minors.
    roots=[(F(1,2),F(0)),(F(0),F(1,2)),(F(-1,2),F(0)),(F(0),F(-1,2))]
    Fourier=[[roots[(i*j)%4] for j in range(4)] for i in range(4)]
    atom_polys=[];channel_entries=0
    for mask in range(16):
        S=[i for i in range(4) if mask>>i&1];p=Poly()
        for T in combinations(range(4),len(S)):
            z=gd([[Fourier[i][j] for j in T] for i in S]);weight=z[0]**2+z[1]**2
            prod=Poly(weight)
            for i in range(4):prod*=lam[i] if i in T else 1-lam[i]
            p+=prod;channel_entries+=1
        if len(S)!=2:expected=q[len(S)]
        else:expected=O if (S[1]-S[0])%2==0 else P
        identity('Fourier atom '+str(mask),p,expected);atom_polys.append(p)

    cases=[('49/100','49/100','48/100','47/100'),
           ('47/100','47/100','1/100','2/100'),
           ('1/2','1/2','49/100','1/3'),
           ('3/4','3/4','1/5','1/6'),
           ('9/10','4/5','9/100','19/100'),
           ('7/10','3/10','1/5','1/5'),
           ('2/5','2/5','0','0')]
    records=[]
    for base in cases:
        for velocity in [(1,1),(1,-1),(2,3)]:
            values=list(map(F,base))+list(map(F,velocity))
            fv=[p.at(values) for p in f];qv=[p.at(values) for p in q]
            gv=[p.at(values) for p in g];hv=[p.at(values) for p in h]
            Pv=P.at(values);Ov=O.at(values);Dv=Delta.at(values);ff=fv[2]
            assert all(0<p.at(values)<1 for p in lam)
            assert sum(p.at(values) for p in atom_polys)==1
            assert Pv*Pv>=qv[1]*qv[3] and Pv*Ov>=qv[1]*qv[3]
            assert hv[1]<=0
            fisher=sum(d(p).at(values)**2/p.at(values) for p in f)
            Qk=[gv[k]**2/fv[k]-2*gv[k]*gv[k+1]/fv[k+1]+gv[k+1]**2/fv[k+2] for k in range(3)]
            assert all(z>=0 for z in Qk)
            assert fisher==gv[0]**2/fv[1]+gv[3]**2/fv[3]+sum(Qk)
            for k in range(3):
                assert hv[k]*(fv[k+1]**2-fv[k]*fv[k+2])<=2*gv[k]*gv[k+1]*fv[k+1]-gv[k]**2*fv[k+2]-gv[k+1]**2*fv[k]
            z=Dv/(2*ff);m= mw.at(values);norm=sum(F(w)**2 for w in velocity)
            argR=6*Ov*Pv**2/(ff*qv[1]*qv[3]);assert argR>=1
            square=(d(Delta).at(values)-2*z*d(f[2]).at(values))**2/(8*ff*(1+z)*(1-z/2))
            bound=logsum([(4*m,argR),(-2*norm,1-z/2)],square)
            full=logsum([(d(d(p)).at(values),p.at(values)) for p in atom_polys],sum(d(p).at(values)**2/p.at(values) for p in atom_polys))
            # Exact enclosure of the difference, reducing cancellation by
            # treating it as one expression rather than subtracting intervals.
            gap=logsum([(d(d(p)).at(values),p.at(values)) for p in atom_polys]+[(-4*m,argR),(2*norm,1-z/2)],sum(d(p).at(values)**2/p.at(values) for p in atom_polys)-square)
            if Dv>0:assert bound[0]>0 and full[0]>0
            if any(values[i] for i in [2,3]):assert gap[0]>0
            else:assert full[0]<=0<=full[1]
            records.append(dict(base=list(base),velocity=velocity,Delta=str(Dv),curvature=enclose_decimal(full),compensated_lower_bound=enclose_decimal(bound),discarded_nonnegative_remainder=enclose_decimal(gap)))
    out=dict(status='PASS: exact self-checks; restricted analytic proof, not an independent audit',polynomial_identities=checks,polynomial_identity_count=len(checks),Fourier_channel_entries=channel_entries,rational_curvature_cases=records)
    Path(__file__).with_name('fourier_extension_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status=out['status'],polynomial_identity_count=len(checks),Fourier_channel_entries=channel_entries,rational_curvature_case_count=len(records)),indent=2))


if __name__=='__main__':main()
