#!/usr/bin/env python3
"""P20/I0081: exact+interval certificate for an asymmetric >=12-mode counterexample.

Distinct logarithmic staircase inputs use common radii (10,20,28,50,80,130)
and indicator weights
 mu=(5000000,15000000,5000000,10000,10,1),
 nu=(5000001,15000000,5000000,10000,10,1).
The script first finds high-precision approximations to the unequal-product
subordination system, then *certifies* each root and derivative sign by an
interval Krawczyk/contraction enclosure. Numerical discovery is not evidence;
only the interval inclusion and strict sign tests below are asserted.
"""
from fractions import Fraction
import mpmath as mp
mp.mp.dps=170
mp.iv.dps=115
iv=mp.iv

RADII=(10,20,28,50,80,130)
WM=(5000000,15000000,5000000,10000,10,1)
WN=(5000001,15000000,5000000,10000,10,1)
RM=tuple(zip(RADII,WM)); RN=tuple(zip(RADII,WN))
NM=2*sum(R*w for R,w in RM); NN=2*sum(R*w for R,w in RN)
assert (NM,NN)==(981001860,981001880) and RM!=RN

def plateau(weights,N):
    c=[Fraction(w,N) for w in weights]
    h=[sum(c[j:]) for j in range(len(c))]
    assert all(h[j]>h[j+1] for j in range(len(h)-1)) and h[-1]>0
    return h
HM,HN=plateau(WM,NM),plateau(WN,NN)
assert 2*sum(Fraction(R*w,NM) for R,w in RM)==1
assert 2*sum(Fraction(R*w,NN) for R,w in RN)==1

# Scalar transforms for discovery.
def Fs(R,z): return 2*R-mp.log(1-z*mp.e**R)+mp.log(1-z*mp.e**(-R))
def Fps(R,z): return mp.e**R/(1-z*mp.e**R)-mp.e**(-R)/(1-z*mp.e**(-R))
def scalar_transform(rats,N):
    def M(z): return sum(w*Fs(R,z) for R,w in rats)/N
    def Mp(z): return sum(w*Fps(R,z) for R,w in rats)/N
    def eta(z): return 1-1/M(z)
    def etap(z):
        m=M(z); return Mp(z)/m**2
    return M,eta,etap
_,em,emp=scalar_transform(RM,NM); _,en,enp=scalar_transform(RN,NN)

# Short seeds; findroot only discovers candidates. Interval Krawczyk proves them.
SEED={
 8:(1.302e-3+1.4689e-2j,1.302e-3+1.4689e-2j),
 18:(7.526e-6+7.272e-5j,7.526e-6+7.272e-5j),
 29:(2.961e-8+1.999e-7j,2.961e-8+1.999e-7j),
 37:(5.367e-10+2.052e-9j,5.367e-10+2.052e-9j),
 46:(3.771e-12+1.336e-11j,3.771e-12+1.336e-11j),
 48:(1.678e-12+4.017e-12j,1.678e-12+4.017e-12j),
 53:(4.28e-14+2.52e-14j,4.28e-14+2.52e-14j),
 54:(1.50e-14+2.27e-14j,1.50e-14+2.27e-14j),
 70:(3.0e-18+1.5e-18j,3.0e-18+1.5e-18j),
 86:(4.23e-22+9.73e-22j,4.23e-22+9.73e-22j),
 90:(4.15e-23+1.03e-24j,4.15e-23+1.03e-24j),
 95:(1.85e-25+1.35e-24j,1.85e-25+1.35e-24j),
}
SIGN={8:1,18:-1,29:1,37:-1,46:1,48:-1,53:1,54:-1,70:1,86:-1,90:1,95:-1}

# Interval transforms.
def Fi(R,z):
    R=iv.mpf(R); ep=iv.exp(R); emn=iv.exp(-R)
    return 2*R-iv.log(1-z*ep)+iv.log(1-z*emn)
def Fpi(R,z):
    R=iv.mpf(R); ep=iv.exp(R); emn=iv.exp(-R)
    return ep/(1-z*ep)-emn/(1-z*emn)
def interval_transform(rats,N):
    def M(z):
        a=iv.mpc(0)
        for R,w in rats: a+=w*Fi(R,z)
        return a/N
    def Mp(z):
        a=iv.mpc(0)
        for R,w in rats: a+=w*Fpi(R,z)
        return a/N
    def eta(z):
        m=M(z); return 1-1/m
    def etap(z):
        m=M(z); return Mp(z)/m**2
    return M,eta,etap
MM,EM,EMP=interval_transform(RM,NM); MN,EN,ENP=interval_transform(RN,NN)

def abs2(z): return z.real**2+z.imag**2
def pos(x): return x.a>0
def neg(x): return x.b<0
def lt(x,c): return x.b<iv.mpf(str(c))
def modup(z): return iv.sqrt(abs2(z)).b
def strict_contains(O,I):
    return O.real.a<I.real.a and I.real.b<O.real.b and O.imag.a<I.imag.a and I.imag.b<O.imag.b

def txt(x): return mp.nstr(x,175)
def point(z): return iv.mpc(iv.mpf(txt(z.real)),iv.mpf(txt(z.imag)))
def box(z,r=mp.mpf('1e-44')):
    a=iv.mpf(txt(z.real)); b=iv.mpf(txt(z.imag)); rr=iv.mpf(txt(r)).b
    return iv.mpc([a.a-rr,a.b+rr],[b.a-rr,b.b+rr])

def inv2(a,b,c,d):
    det=a*d-b*c
    return ((d/det,-b/det),(-c/det,a/det))

print('P20 I0081 asymmetric six-level >=12-mode interval certificate')
print('mpmath',mp.__version__,'iv.dps',mp.iv.dps)
print('NM',NM,'NN',NN,'exact masses PASS')
print('mu plateaus',HM)
print('nu plateaus',HN)
print('distinct inputs',RM!=RN)

allok=True
for y in sorted(SEED):
    s=mp.e**(-y)
    def G1(q,r): return em(q)-en(r)
    def G2(q,r): return q*r-s*em(q)
    q,r=mp.findroot((G1,G2),SEED[y],tol=mp.mpf('1e-150'),maxsteps=100)
    # point inverse Jacobian as Krawczyk preconditioner
    a=emp(q); b=-enp(r); c=r-s*emp(q); d=q
    C=inv2(a,b,c,d)
    q0,r0=point(q),point(r); Xq,Xr=box(q),box(r); si=iv.exp(-iv.mpf(y))
    branch=True
    for X in (Xq,Xr):
        for R in RADII:
            ep=iv.exp(iv.mpf(R)); eneg=iv.exp(-iv.mpf(R))
            branch &= neg((1-X*ep).imag) and neg((1-X*eneg).imag)
    mM,mN=MM(Xq),MN(Xr); w=EM(Xq); epm=EMP(Xq); epn=ENP(Xr)
    denom=pos(abs2(mM)) and pos(abs2(mN)) and pos(abs2(w))
    f0=(EM(q0)-EN(r0), q0*r0-si*EM(q0))
    J=((epm,-epn),(Xr-si*epm,Xq))
    Ci=((point(C[0][0]),point(C[0][1])),(point(C[1][0]),point(C[1][1])))
    CJ=((Ci[0][0]*J[0][0]+Ci[0][1]*J[1][0],Ci[0][0]*J[0][1]+Ci[0][1]*J[1][1]),
        (Ci[1][0]*J[0][0]+Ci[1][1]*J[1][0],Ci[1][0]*J[0][1]+Ci[1][1]*J[1][1]))
    A=((1-CJ[0][0],-CJ[0][1]),(-CJ[1][0],1-CJ[1][1]))
    cf=(Ci[0][0]*f0[0]+Ci[0][1]*f0[1],Ci[1][0]*f0[0]+Ci[1][1]*f0[1])
    dq,dr=Xq-q0,Xr-r0
    Kq=q0-cf[0]+A[0][0]*dq+A[0][1]*dr
    Kr=r0-cf[1]+A[1][0]*dq+A[1][1]*dr
    incl=strict_contains(Xq,Kq) and strict_contains(Xr,Kr)
    contract=(modup(A[0][0])+modup(A[0][1])<1 and modup(A[1][0])+modup(A[1][1])<1)
    detJ=J[0][0]*J[1][1]-J[0][1]*J[1][0]; jac=pos(abs2(detJ))
    invJ01=-J[0][1]/detJ
    qy=-invJ01*si*w; wy=epm*qy
    g=iv.im(1/(1-w))/iv.pi; gp=iv.im(wy/(1-w)**2)/iv.pi
    physbox=pos(Xq.imag) and pos(Xr.imag) and lt(abs2(w),1) and pos(abs2(1-w))
    dens=pos(g); sg=pos(gp) if SIGN[y]>0 else neg(gp)
    ok=all((branch,denom,incl,contract,jac,physbox,dens,sg)); allok &= ok
    print('y',y,'branch',branch,'denom',denom,'krawczyk',incl,'contract',contract,
          'jac',jac,'physical-box',physbox,'density+',dens,'gprime',gp,'sign',SIGN[y],'PASS',ok)

assert allok
print('ALL_INTERVAL_CHECKS_PASS')
print('Certified signs: +,-,+,-,+,-,+,-,+,-,+,- at 8,18,29,37,46,48,53,54,70,86,90,95')
