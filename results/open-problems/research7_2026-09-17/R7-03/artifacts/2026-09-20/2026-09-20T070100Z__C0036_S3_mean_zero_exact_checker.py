#!/usr/bin/env python3
"""Exact certificate for the R7-03/C0036 S3 z0=0 midpoint theorem.

No floating point arithmetic is used. The script:
  * builds S3 as D3 = <r,s | r^3=s^2=1, srs=r^-1>;
  * enumerates left-translation subset orbits and all invariant upper sets;
  * constructs the general Hermitian equivariant kernel on the face
        x0+x1+x2=0  (equivalently z0=0 in the A3-Fourier block);
  * constructs the simultaneous quotient-sign geometric midpoint G;
  * computes every invariant-event difference by exact inclusion-exclusion;
  * reduces by |z|^2 = 3(X^2+XY+Y^2)=a1*a2*(1-rho^2);
  * minimizes the remaining orientation quadratic exactly;
  * reparameterizes the feasible trace/determinant region by a unit cube;
  * verifies nonnegativity through exact multivariate Bernstein coefficients.
"""
from itertools import product
from math import comb
from collections import defaultdict
import sympy as sp

# ---------- group and subset orbits ----------
def mul(g,h):
    k,e=g; l,f=h
    return ((k + ((-1)**e)*l) % 3, (e+f) % 2)

def inv(g):
    for h in ELS:
        if mul(g,h)==(0,0) and mul(h,g)==(0,0):
            return h
    raise AssertionError

ELS=[(k,e) for e in (0,1) for k in range(3)]
IDX={g:i for i,g in enumerate(ELS)}
ALLSUB=[frozenset(i for i in range(6) if (mask>>i)&1) for mask in range(64)]

def left_translate(S,g):
    return frozenset(IDX[mul(g,ELS[i])] for i in S)

seen=set(); ORBITS=[]
for S in ALLSUB:
    if S in seen:
        continue
    orb={left_translate(S,g) for g in ELS}
    ORBITS.append(tuple(sorted(orb,key=lambda z:(len(z),tuple(z)))))
    seen |= orb
assert len(ORBITS)==16

le=[[False]*len(ORBITS) for _ in ORBITS]
for i,Oi in enumerate(ORBITS):
    for j,Oj in enumerate(ORBITS):
        le[i][j]=any(S.issubset(T) for S in Oi for T in Oj)

UPPERS=[]
for mask in range(1<<len(ORBITS)):
    U={i for i in range(len(ORBITS)) if (mask>>i)&1}
    if all(not le[i][j] or j in U for i in U for j in range(len(ORBITS))):
        UPPERS.append(U)
assert len(UPPERS)==76

# ---------- exact spatial kernels ----------
a0,a1,a2,rho,X,Y=sp.symbols('a0 a1 a2 rho X Y', real=True)
sq3=sp.sqrt(3); I=sp.I
u,v,vc,x0,x1,x2=sp.symbols('u v vc x0 x1 x2')

def q_symbol(g):
    k,e=g
    return [u,v,vc][k] if e==0 else [x0,x1,x2][k]

Qraw=sp.Matrix([[q_symbol(mul(inv(g),h)) for h in ELS] for g in ELS])

u0=(a0+a1+a2)/3
vre=(2*a0-a1-a2)/6
vim=(a2-a1)/(2*sq3)
v0=vre+I*vim
vc0=vre-I*vim
Q=sp.simplify(Qraw.subs({u:u0,v:v0,vc:vc0,x0:-X-Y,x1:X,x2:Y}))

ug=(a0+rho*a1+rho*a2)/3
vgre=(2*a0-rho*a1-rho*a2)/6
vgim=rho*(a2-a1)/(2*sq3)
vg=vgre+I*vgim
vcg=vgre-I*vgim
G=sp.simplify(Qraw.subs({u:ug,v:vg,vc:vcg,x0:0,x1:0,x2:0}))

# ---------- principal minors and event inclusion-exclusion ----------
def pdet(M,S):
    if not S:
        return sp.Integer(1)
    inds=sorted(S)
    return sp.factor(M.extract(inds,inds).det())

DQ={S:pdet(Q,S) for S in ALLSUB}
DG={S:pdet(G,S) for S in ALLSUB}

def event_coeffs(Uorb):
    Usubs=set()
    for i in Uorb:
        Usubs.update(ORBITS[i])
    out={}
    for T in ALLSUB:
        c=sum((-1)**(len(T)-len(S)) for S in Usubs if S.issubset(T))
        if c:
            out[T]=sp.Integer(c)
    return out

def event_delta(Uorb):
    return sp.factor(sum(c*(DQ[T]-DG[T]) for T,c in event_coeffs(Uorb).items()))

DELTAS=[event_delta(U) for U in UPPERS]

# ---------- exact face reduction and orientation minimization ----------
# |z|^2 = 3(X^2+XY+Y^2) = a1*a2*(1-rho^2).
rel=3*(X**2+X*Y+Y**2)-a1*a2*(1-rho**2)
GB=sp.groebner([rel],X,Y,a0,a1,a2,rho,order='lex')
REDS=[]
for dlt in DELTAS:
    num,den=sp.together(dlt).as_numer_denom()
    rem=GB.reduce(sp.expand(num))[1]
    REDS.append(sp.factor(rem/den))

# qform is always B*X*Y + C*Y^2 after reduction. Relative to
# s=X^2+XY+Y^2, the exact ranges are
#   XY/s in [-1,1/3], Y^2/s in [0,4/3], (XY+Y^2)/s in [-1/3,1].
def sign_on_unit(expr):
    """Certify a fixed sign on a0 in [0,1] via exact Bernstein coefficients."""
    expr=sp.expand(expr)
    if expr==0:
        return 0
    P=sp.Poly(expr,a0,domain='QQ')
    n=max(0,P.degree())
    coeff=P.as_dict()
    vals=[]
    for k in range(n+1):
        val=sp.Rational(0)
        for (j,),c in coeff.items():
            if j<=k:
                val += c*sp.Rational(comb(k,j),comb(n,j))
        vals.append(sp.factor(val))
    if all(v>=0 for v in vals):
        return 1
    if all(v<=0 for v in vals):
        return -1
    raise AssertionError((expr, vals))

def lambda_min(Acoef,Bcoef,Ccoef):
    assert Acoef==0
    if Bcoef==0 and Ccoef==0:
        return sp.Integer(0)
    if Ccoef==0:
        s=sign_on_unit(Bcoef)
        return -Bcoef if s>=0 else Bcoef/3
    if Bcoef==0:
        s=sign_on_unit(Ccoef)
        return sp.Integer(0) if s>=0 else sp.Rational(4,3)*Ccoef
    if sp.simplify(Bcoef-Ccoef)==0:
        s=sign_on_unit(Bcoef)
        return -Bcoef/3 if s>=0 else Bcoef
    raise AssertionError((Acoef,Bcoef,Ccoef))

LOWERS=[]
for de in REDS:
    num,den=sp.together(de).as_numer_denom()
    P=sp.Poly(sp.expand(num),X,Y)
    assert P.coeff_monomial(X)==0 and P.coeff_monomial(Y)==0
    Acoef=sp.factor(P.coeff_monomial(X**2)/den)
    Bcoef=sp.factor(P.coeff_monomial(X*Y)/den)
    Ccoef=sp.factor(P.coeff_monomial(Y**2)/den)
    const=sp.factor(P.coeff_monomial(1)/den)
    lam=lambda_min(Acoef,Bcoef,Ccoef)
    s=a1*a2*(1-rho**2)/3
    LOWERS.append(sp.factor(const+lam*s))

# ---------- symmetric trace/determinant variables ----------
qtr,det,h=sp.symbols('qtr det h', real=True)
m=sp.Symbol('m', positive=True, real=True)

def to_qm(expr):
    sym,rem,mapping=sp.symmetrize(sp.expand(expr),[a1,a2],formal=True)
    assert rem==0
    s1,s2=[p[0] for p in mapping]
    return sp.factor(sym.subs({s1:qtr,s2:m}))
CERT=[]
for L in LOWERS:
    Lqm=to_qm(L)
    # det = a1*a2*rho^2, h = rho*(a1+a2)
    E=sp.cancel(Lqm.subs({rho:h/qtr,m:det*qtr**2/h**2}))
    N=sp.factor(3*h**2*E)
    if N==0:
        CERT.append(sp.Integer(0))
        continue
    quo,rem=sp.div(sp.Poly(sp.expand(N),qtr),sp.Poly(qtr-h,qtr))
    assert rem.as_expr()==0
    CERT.append(sp.factor(quo.as_expr()))

# Feasible 2x2 contraction domain:
#   0<=det<=1, 2*sqrt(det)<=h<=qtr<=1+det.
# Put det=T^2,
#     h=2T+U(1-T)^2,
#     qtr=h+V(1+T^2-h),   A=a0,
# with A,T,U,V in [0,1].
A,T,U,V=sp.symbols('A T U V', real=True)
hcube=2*T+U*(1-T)**2
qcube=hcube+V*(1+T**2-hcube)
dcube=T**2
CUBE=[sp.expand(C.subs({a0:A,det:dcube,h:hcube,qtr:qcube})) for C in CERT]

# ---------- exact Bernstein coefficients ----------
def bernstein_coeffs(poly,vars,degrees):
    P=sp.Poly(sp.expand(poly),*vars,domain='QQ')
    coeff=P.as_dict()
    out={}
    for k in product(*[range(n+1) for n in degrees]):
        val=sp.Rational(0)
        for j,a in coeff.items():
            if all(jj<=kk for jj,kk in zip(j,k)):
                fac=sp.Rational(1)
                for jj,kk,n in zip(j,k,degrees):
                    fac*=sp.Rational(comb(kk,jj),comb(n,jj))
                val+=a*fac
        out[k]=sp.factor(val)
    return out

# Deduplicate exact certificate polynomials.
groups=defaultdict(list)
for i,C in enumerate(CUBE):
    groups[sp.srepr(C)].append(i)

negative=[]; total=0; zeros=0; smallest=None; nonzero_groups=0
for inds in groups.values():
    C=CUBE[inds[0]]
    if C==0:
        continue
    nonzero_groups+=1
    P=sp.Poly(C,A,T,U,V,domain='QQ')
    deg=tuple(P.degree(z) for z in (A,T,U,V))
    bc=bernstein_coeffs(C,(A,T,U,V),deg)
    for key,val in bc.items():
        total+=1
        if val<0:
            negative.append((inds,key,val))
        elif val==0:
            zeros+=1
        elif smallest is None or val<smallest:
            smallest=val

print(f"SUBSET_ORBITS={len(ORBITS)}")
print(f"INVARIANT_UPPER_SETS={len(UPPERS)}")
print(f"NONZERO_EVENT_LOWER_BOUNDS={sum(1 for x in LOWERS if x!=0)}")
print(f"UNIQUE_NONZERO_BERNSTEIN_CERTIFICATES={nonzero_groups}")
print(f"TOTAL_BERNSTEIN_COEFFICIENTS={total}")
print(f"ZERO_BERNSTEIN_COEFFICIENTS={zeros}")
print(f"NEGATIVE_BERNSTEIN_COEFFICIENTS={len(negative)}")
print(f"SMALLEST_POSITIVE_BERNSTEIN_COEFFICIENT={smallest}")
if negative:
    for row in negative[:20]:
        print("NEGATIVE",row)
    raise SystemExit(1)
assert len(ORBITS)==16
assert len(UPPERS)==76
assert sum(1 for x in LOWERS if x!=0)==73
assert nonzero_groups==33
assert total==5269
assert zeros==2362
assert smallest==sp.Rational(1,45)
print("ALL_EXACT_CERTIFICATES_PASS")
