#!/usr/bin/env python3
"""Independent R01 audit of new claims in runs/R02/20260916T1405Z_1bc8ce78.md.
Scope: X002, C003 (conditional on Letwin's quoted theorem), X003.
Does not audit KLS itself and does not move R02's frozen metric.
"""
import sympy as sp
q=sp.Rational

# X002: generic skewness tau.
eps,beta,n,tau=sp.symbols('eps beta n tau', positive=True)
phi=1+sp.log(sp.exp(beta*tau*eps)+n-1)/beta
d2=sp.simplify(sp.diff(phi,eps,2).subs(eps,0))
assert sp.simplify(d2-beta*tau**2*(n-1)/n**2)==0
gen=sp.simplify(-1+q(1,2)*n*d2)
assert sp.simplify(gen-(-1+tau**2*beta*q(1,2)*(1-1/n)))==0
L,b=sp.symbols('L b', positive=True)
assert sp.solve(sp.Eq(sp.diff((b-L)/b**2,b),0),b)==[2*L]
print('R02 X002 independent algebra: PASS')

# C003: cubic root derivatives at (lambda,z)=(1,2).
lam,z=sp.symbols('lam z', positive=True)
qq=lam/(z-lam); h=qq**3-qq
partials=tuple(sp.diff(h,*args).subs({lam:1,z:2}) for args in
               [(lam,), (z,), (lam,lam), (lam,z), (z,z)])
assert partials==(4,-2,32,-18,10)
S1,S2,N=sp.symbols('S1 S2 N', positive=True)
zp=2*S1/N; zpp=16*(S2-S1**2/N)/N
ellp=sp.simplify(zp/2); ellpp=sp.simplify(zpp/2-zp**2/4)
assert ellp==S1/N
assert sp.simplify(ellpp-(8*S2/N-9*S1**2/N**2))==0
# With Letwin: sum tr(T_k)^2 <= 8N; ||T_k||_F^2 <=8 individually.
lower=sp.simplify(-1-q(9,2)/N**2*(8*N))
upper=sp.simplify(-1+(4/N)*(8*N))
assert sp.simplify(lower-(-1-36/N))==0 and sp.simplify(upper-31)==0
print('R02 C003 derivatives/bounds conditional on Letwin: PASS')

# X003: independently derive the one-coordinate implicit Hessians and compare
# with R02's claimed summed Ito expression, keeping generic tau.
R,r=sp.symbols('R r', positive=True)
qs=1/sp.sqrt(3); lR=R/(1+R); ls=qs/(1+qs)
lamvar,zvar=sp.symbols('lamvar zvar', positive=True)
def H(l,z):
    qv=l/(z-l)
    return qv**3-qv
FR=H(lamvar,zvar)+(r-1)*H(lR,zvar)+r**2*H(ls,zvar)
FS=H(lamvar,zvar)+r*H(lR,zvar)+(r**2-1)*H(ls,zvar)
def ell_derivs(F,sub):
    Fl=sp.diff(F,lamvar).subs(sub); Fz=sp.diff(F,zvar).subs(sub)
    z1=sp.simplify(-Fl/Fz)
    z2=sp.simplify(-(sp.diff(F,lamvar,2).subs(sub)
                    +2*sp.diff(F,lamvar,zvar).subs(sub)*z1
                    +sp.diff(F,zvar,2).subs(sub)*z1**2)/Fz)
    return sp.factor(z1),sp.factor(z2-z1**2) # base z=1
ell1R,ell2R=ell_derivs(FR,{lamvar:lR,zvar:1})
ell1S,ell2S=ell_derivs(FS,{lamvar:ls,zvar:1})
assert sp.factor(ell1R-(R+1)/(R*r))==0 and ell1S==0
Ito=sp.factor(q(1,2)*tau**2*(r*lR**3*ell2R+r**2*ls**3*ell2S))
def e(x): return (3*x**2-1)*x*(1+x)
def s(x): return x*(1+x)
def Gamma(x): return 6*x*s(x)**2+(3*x**2-1)*s(x)*(1+2*x)
claimed=sp.factor(tau**2*lR/(2*e(R))*(Gamma(R)*(1-1/r)+Gamma(qs)-e(R))
                  +tau**2*r*ls*Gamma(qs)/(2*e(R)))
assert sp.factor(Ito-claimed)==0
drift=sp.simplify(r*ell1R*(-lR**2)+r**2*ell1S*(-ls**2))
assert sp.simplify(drift+lR)==0
ms=2/(3*sp.sqrt(3)); rR=(R**3-R)/ms
ItoR=sp.simplify(Ito.subs(r,rR)); totalR=sp.simplify(ItoR-lR)
assert sp.simplify(sp.limit(ItoR/R,R,sp.oo)-2*tau**2)==0
assert sp.simplify(sp.limit(totalR/R,R,sp.oo)-2*tau**2)==0
qvR=sp.simplify((tau**2*lR/r).subs(r,rR))
assert sp.limit(qvR,R,sp.oo)==0
print('R02 X003 independent implicit-Hessian/asymptotic audit: PASS')
print("NOTE: R02's own X003 checker sets a numerical tau^2=4 scale in its sample;")
print('      the theorem/report formula with generic tau is correct and was checked here.')
print('R01-AUDIT-R02-KLS-X002-C003-X003-02 = PASS_AT_STATED_SCOPE')
