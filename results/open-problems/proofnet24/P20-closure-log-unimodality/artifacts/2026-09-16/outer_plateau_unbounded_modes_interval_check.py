#!/usr/bin/env python3
"""P20/I0081: certified outer-scale finite core.

Section A certifies the two universal outer-plateau model roots and the
opposite derivative signs used in the unbounded-mode induction.

Section B certifies two additional positive-side derivative sign pairs
for the inherited asymmetric six-level witness, using scaled subordination
variables to avoid tiny-coordinate ill-conditioning.

Discovery (mp.findroot) is not evidence; all asserted roots/signs are
certified by strict interval Krawczyk/contraction enclosures.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 180
mp.iv.dps = 130
iv = mp.iv

def txt(x):
    return mp.nstr(x, 190)

def point(z):
    return iv.mpc(iv.mpf(txt(mp.re(z))), iv.mpf(txt(mp.im(z))))

def box(z, r):
    rr = iv.mpf(txt(r)).b
    a = iv.mpf(txt(mp.re(z)))
    b = iv.mpf(txt(mp.im(z)))
    return iv.mpc([a.a-rr, a.b+rr], [b.a-rr, b.b+rr])

def abs2(z):
    return z.real**2 + z.imag**2

def modup(z):
    return iv.sqrt(abs2(z)).b

def pos(x):
    return x.a > 0

def neg(x):
    return x.b < 0

def lt(x, c):
    return x.b < iv.mpf(str(c))

def strict_contains(O, I):
    return (O.real.a < I.real.a and I.real.b < O.real.b
            and O.imag.a < I.imag.a and I.imag.b < O.imag.b)

def inv2(a,b,c,d):
    det = a*d-b*c
    return ((d/det,-b/det),(-c/det,a/det))

print("P20 I0081 outer-scale interval certificate")
print("mpmath", mp.__version__, "iv.dps", mp.iv.dps)

# ----------------------------------------------------------------------
# A. Universal outer-plateau model
#   L(xi)=-log(1-xi), xi^2=tau L(xi)
#   D(tau)=pi^{-1} Im[L'(xi)*(-tau L(xi)/(2xi-tau L'(xi)))]
# ----------------------------------------------------------------------

def Ls(x):
    return -mp.log(1-x)
def Lps(x):
    return 1/(1-x)

MODEL_SEEDS = {
    100: mp.mpc("5.050183213", "17.77049124"),
    10:  mp.mpc("2.055620165", "4.39419539"),
}
MODEL_SIGN = {100: 1, 10: -1}
model_ok = True

print("SECTION A: universal model")
for tau in (100, 10):
    t = mp.mpf(tau)
    f = lambda x: x*x - t*Ls(x)
    fp = lambda x: 2*x - t*Lps(x)
    x = mp.findroot(f, MODEL_SEEDS[tau], tol=mp.mpf("1e-165"), maxsteps=100)
    x0 = point(x)
    X = box(x, mp.mpf("1e-38"))
    Ti = iv.mpf(tau)
    LI = -iv.log(1-X)
    LPI = 1/(1-X)
    f0 = x0*x0 - Ti*(-iv.log(1-x0))
    fp0 = 2*x - t*Lps(x)
    C = point(1/fp0)
    A = 1 - C*(2*X - Ti*LPI)
    K = x0 - C*f0 + A*(X-x0)
    incl = strict_contains(X,K)
    contract = modup(A) < 1
    simple = pos(abs2(2*X - Ti*LPI))
    upper = pos(X.imag)
    branch = neg((1-X).imag)
    D = iv.im(LPI * (-Ti*LI/(2*X-Ti*LPI))) / iv.pi
    signok = pos(D) if MODEL_SIGN[tau] > 0 else neg(D)
    limdens = iv.im(LI)/iv.pi
    densok = pos(limdens)
    ok = all((incl, contract, simple, upper, branch, signok, densok))
    model_ok &= ok
    print("tau", tau)
    print("  root", txt(x))
    print("  krawczyk", incl, "contract", contract, "simple", simple,
          "upper", upper, "branch", branch, "lim-density+", densok)
    print("  D", D, "required-sign", MODEL_SIGN[tau], "PASS", ok)

assert model_ok
print("UNIVERSAL_MODEL_PASS")

# ----------------------------------------------------------------------
# B. Inherited asymmetric six-level witness: certify overlooked remote
#    signs at y=112,140,230,238 using q=e^{-R*}x, r=e^{-R*}z.
# ----------------------------------------------------------------------

RADII=(10,20,28,50,80,130)
WM=(5000000,15000000,5000000,10000,10,1)
WN=(5000001,15000000,5000000,10000,10,1)
RM=tuple(zip(RADII,WM)); RN=tuple(zip(RADII,WN))
NM=2*sum(R*w for R,w in RM)
NN=2*sum(R*w for R,w in RN)
assert (NM,NN)==(981001860,981001880)
assert 2*sum(Fraction(R*w,NM) for R,w in RM)==1
assert 2*sum(Fraction(R*w,NN) for R,w in RN)==1

def plateau(weights,N):
    c=[Fraction(w,N) for w in weights]
    h=[sum(c[j:]) for j in range(len(c))]
    assert all(h[j]>h[j+1] for j in range(len(h)-1)) and h[-1]>0
    return h
plateau(WM,NM); plateau(WN,NN)

def Fs(R,z):
    return 2*R-mp.log(1-z*mp.e**R)+mp.log(1-z*mp.e**(-R))
def Fps(R,z):
    return mp.e**R/(1-z*mp.e**R)-mp.e**(-R)/(1-z*mp.e**(-R))
def scalar_transform(rats,N):
    def M(z):
        return sum(w*Fs(R,z) for R,w in rats)/N
    def Mp(z):
        return sum(w*Fps(R,z) for R,w in rats)/N
    def eta(z):
        return 1-1/M(z)
    def etap(z):
        m=M(z); return Mp(z)/m**2
    return M,eta,etap
_,em,emp=scalar_transform(RM,NM)
_,en,enp=scalar_transform(RN,NN)

def Fi(R,z):
    R=iv.mpf(R); ep=iv.exp(R); eneg=iv.exp(-R)
    return 2*R-iv.log(1-z*ep)+iv.log(1-z*eneg)
def Fpi(R,z):
    R=iv.mpf(R); ep=iv.exp(R); eneg=iv.exp(-R)
    return ep/(1-z*ep)-eneg/(1-z*eneg)
def interval_transform(rats,N):
    def M(z):
        a=iv.mpc(0)
        for R,w in rats:
            a += w*Fi(R,z)
        return a/N
    def Mp(z):
        a=iv.mpc(0)
        for R,w in rats:
            a += w*Fpi(R,z)
        return a/N
    def eta(z):
        m=M(z); return 1-1/m
    def etap(z):
        m=M(z); return Mp(z)/m**2
    return M,eta,etap
MM,EM,EMP=interval_transform(RM,NM)
MN,EN,ENP=interval_transform(RN,NN)

# (y, Rstar, seed_x, seed_z, sign, cscale)
EXTRA = [
 (112,80,
  mp.mpc("493479.221416974567333","12837151.90863570428986"),
  mp.mpc("493479.847335110349574","12837157.36686036533916"),
  1, mp.mpf(10)/NM),
 (140,80,
  mp.mpc("0.707521250225028356774","5.907738991485477288756"),
  mp.mpc("0.707521409566387383868","5.907739761248129471440"),
  -1, mp.mpf(10)/NM),
 (230,130,
  mp.mpc("37.69013101523837664","248.2087542776767495"),
  mp.mpc("37.69014383942676629","248.2087809515403811"),
  1, mp.mpf(1)/NM),
 (238,130,
  mp.mpc("1.4273244727677298066","2.25099347200947843036"),
  mp.mpc("1.42732456068673093338","2.25099349473790565994"),
  -1, mp.mpf(1)/NM),
]

extra_ok=True
print("SECTION B: overlooked remote signs")
for y,Rstar,sx,sz,sgn,cscale in EXTRA:
    a=mp.e**(-Rstar)
    k=mp.e**(2*Rstar-y)
    def F1(x,z):
        return (em(a*x)-en(a*z))/cscale
    def F2(x,z):
        return x*z-k*em(a*x)
    x,z=mp.findroot((F1,F2),(sx,sz),tol=mp.mpf("1e-160"),maxsteps=100)
    # point Jacobian
    j11=a*emp(a*x)/cscale
    j12=-a*enp(a*z)/cscale
    j21=z-k*a*emp(a*x)
    j22=x
    C=inv2(j11,j12,j21,j22)
    x0,z0=point(x),point(z)
    X,Z=box(x,mp.mpf("1e-34")),box(z,mp.mpf("1e-34"))
    ai=iv.exp(-iv.mpf(Rstar))
    ki=iv.exp(iv.mpf(2*Rstar-y))
    ci=iv.mpf(txt(cscale))
    q=ai*X; r=ai*Z
    mM,mN=MM(q),MN(r)
    wm=EM(q); wn=EN(r)
    epm=EMP(q); epn=ENP(r)
    f0=((EM(ai*x0)-EN(ai*z0))/ci,
        x0*z0-ki*EM(ai*x0))
    J=((ai*epm/ci, -ai*epn/ci),
       (Z-ki*ai*epm, X))
    Ci=((point(C[0][0]),point(C[0][1])),
        (point(C[1][0]),point(C[1][1])))
    CJ=((Ci[0][0]*J[0][0]+Ci[0][1]*J[1][0],
         Ci[0][0]*J[0][1]+Ci[0][1]*J[1][1]),
        (Ci[1][0]*J[0][0]+Ci[1][1]*J[1][0],
         Ci[1][0]*J[0][1]+Ci[1][1]*J[1][1]))
    A=((1-CJ[0][0],-CJ[0][1]),(-CJ[1][0],1-CJ[1][1]))
    cf=(Ci[0][0]*f0[0]+Ci[0][1]*f0[1],
        Ci[1][0]*f0[0]+Ci[1][1]*f0[1])
    dx,dz=X-x0,Z-z0
    Kx=x0-cf[0]+A[0][0]*dx+A[0][1]*dz
    Kz=z0-cf[1]+A[1][0]*dx+A[1][1]*dz
    incl=strict_contains(X,Kx) and strict_contains(Z,Kz)
    contract=(modup(A[0][0])+modup(A[0][1])<1 and
              modup(A[1][0])+modup(A[1][1])<1)
    detJ=J[0][0]*J[1][1]-J[0][1]*J[1][0]
    jac=pos(abs2(detJ))
    branch=True
    for Q in (q,r):
        for RR in RADII:
            ep=iv.exp(iv.mpf(RR)); eneg=iv.exp(-iv.mpf(RR))
            branch &= neg((1-Q*ep).imag) and neg((1-Q*eneg).imag)
    denom=pos(abs2(mM)) and pos(abs2(mN)) and pos(abs2(wm))
    physical=pos(q.imag) and pos(r.imag) and lt(abs2(wm),1) and pos(abs2(1-wm))
    # y derivative in scaled system:
    # J [x_y,z_y]^T = -[0, k*w]^T.
    invJ01=-J[0][1]/detJ
    xy=-invJ01*ki*wm
    wy=ai*epm*xy
    g=iv.im(1/(1-wm))/iv.pi
    gp=iv.im(wy/(1-wm)**2)/iv.pi
    dens=pos(g)
    signok=pos(gp) if sgn>0 else neg(gp)
    ok=all((incl,contract,jac,branch,denom,physical,dens,signok))
    extra_ok &= ok
    print("y",y,"R*",Rstar)
    print("  x",txt(x))
    print("  z",txt(z))
    print("  krawczyk",incl,"contract",contract,"jac",jac,
          "branch",branch,"denom",denom,"physical",physical,"density+",dens)
    print("  gprime",gp,"required-sign",sgn,"PASS",ok)

assert extra_ok
print("ASYMMETRIC_REMOTE_SIGNS_PASS")
print("ALL_INTERVAL_CHECKS_PASS")
