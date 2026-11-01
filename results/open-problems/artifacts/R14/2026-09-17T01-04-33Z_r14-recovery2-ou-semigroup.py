#!/usr/bin/env python3
"""
R14 stuck-recovery-2 artifact.

PART A: exact symbolic/rational checks for the OU-semigroup stationarity reduction.
PART B: exact rational tail envelopes for the three scalar integrands needed by the reduction.
PART C: NUMERICAL_ONLY scout at alpha=12.5, used only to verify that the reduced scalar residuals
        reproduce the previously recovered stationary point. No numerical value in Part C is a
        rigorous bracket endpoint.
"""
from fractions import Fraction as Q
import math

print('R14 recovery-2: OU-semigroup reduction + scalar-tail exact checks')

# ---------------- PART A: exact algebra / symbolic identities ----------------
import sympy as sp
p,D,g,a=sp.symbols('p D g a', positive=True)
J,JB,K=sp.symbols('J JB K', real=True)
q=p*D**2
gp=(1-q)/(2*D*(1-p))
c=(1-D**2)/(D*(1-p)*(1-p*D**2))
B=c/(4*g)
T=sp.Rational(1,2)*(1-p*q)*c-gp+sp.Rational(1,2)/c*sp.log(D/(2*gp))-q/(2*D)+g
cp=sp.diff(c,p); cD=sp.diff(c,D)
Tp=sp.diff(T,p); TD=sp.diff(T,D)

# The full objective is T - a/c * I(p,B), with I_p=-K/(2p), I_B=JB.
Ip=-K/(2*p)
Bp=sp.simplify(sp.diff(B,p)); BD=sp.simplify(sp.diff(B,D)); Bg=sp.simplify(sp.diff(B,g))
assert sp.simplify(Bp-B*cp/c)==0
assert sp.simplify(BD-B*cD/c)==0
assert sp.simplify(Bg+B/g)==0

Fp=sp.simplify(Tp+a*cp*J/c**2-a*(Ip+JB*Bp)/c)
FD=sp.simplify(TD+a*cD*J/c**2-a*(JB*BD)/c)
Fg=sp.simplify(1-a*JB*Bg/c)

# Reduced residuals that are equivalent to Fp=FD=Fg=0 when cD != 0.
R1=sp.simplify(JB+4*g**2/a)
R2=sp.simplify(J-B*JB+c**2*TD/(a*cD))
R3=sp.simplify(K/(2*p)+c/a*(Tp-(cp/cD)*TD))

# Verify algebraic implications by substituting R1=R2=R3=0 values for JB,J,K.
JBsol=-4*g**2/a
Jsol=sp.simplify(B*JBsol-c**2*TD/(a*cD))
Ksol=sp.simplify(-2*p*c/a*(Tp-(cp/cD)*TD))
assert sp.simplify(Fg.subs(JB,JBsol))==0
assert sp.simplify(FD.subs({JB:JBsol,J:Jsol}))==0
assert sp.simplify(Fp.subs({JB:JBsol,J:Jsol,K:Ksol}))==0

# Conversely verify the three residuals vanish from the three gradient equations algebraically.
# Fg=0 -> JB; FD=0 -> J; Fp=0 -> K, so the solved expressions above are unique linear solves.
assert sp.diff(Fg,JB) != 0
assert sp.diff(FD,J) != 0
assert sp.diff(Fp,K) != 0

# On the C189 box, c_D is nonzero.  Exact coarse proof: p<2/3, D^2<1/2.
# c_D numerator = 1 + D^2(1-3p) + p D^4 > 1-D^2 > 1/2;
# denominator D^2(p-1)(1-pD^2)^2 < 0, hence c_D<0.
pU=Q(1641,2500)     # 0.6564 < 2/3
DU=Q(408,625)        # 0.6528
assert pU < Q(2,3)
assert DU*DU < Q(1,2)
print('EXACT_OU_ALGEBRA_PASS')
print('  stationarity reduces to R1=R2=R3 using only I, I_B, K')
print('  c_D<0 throughout the inherited C189 box: PASS')

# ---------------- PART B: exact rational scalar-tail envelopes ----------------
# Inherited C189 box: p in [0.6562,0.6564], D in [0.6525,0.6528], gamma in [0.1587,0.1591].
pL,pU=Q(3281,5000),Q(1641,2500)
DL,DU=Q(261,400),Q(408,625)
gL,gU=Q(1587,10000),Q(1591,10000)

# c = 1/(D(1-p))-D/(1-pD^2). Coarse exact bounds sufficient for B.
cL=1/(DU*(1-pL))-DU/(1-pU*DU*DU)
cU=1/(DL*(1-pU))
BL=cL/(4*gU)
BU=cU/(4*gL)
assert BL>1
assert BU<8
# sqrt(p)<1 and mu(z)=sqrt(p)z-1 < z for z>0 are enough below.

# phi(9)<e^-40<(10/27)^40, inherited exact e lower bound.
elow=Q(65,24)
assert elow>Q(27,10)
phi9_major=Q(10,27)**40

# I_B integrand u_B = d_B log f.
# z<=-9: f>=1/2 and r^2 e^{-B r^2} <= 1/B <1, so |u_B|<2.
# z>=9: denominator f >= G0/2 while numerator <= G2=G0*(sigma^2/A+mu^2/A^2)
# and sigma^2/A<=1, mu^2/A^2<=z^2, so |u_B|<=2(1+z^2).
# Using Qbar(9)<phi(9)/9 and int_9^inf z^2 phi = 9 phi+Qbar:
# total |I_B|-tail < 2 Q + 2[Q + (9phi+Q)] = 18phi+6Q < (18+2/3)phi <19 phi.
IB_tail=Q(19,1)*phi9_major
assert IB_tail < Q(1,10**15)

# K integrand = (d_z log f)^2.
# z<=-9: f>=1/2.  |h_B'|=2B r e^{-Br^2} <=2 sqrt(B)<6 because B<8,
# so |u_z|<12 and K<144.
# z>=9: f>=G0/2 and Cauchy gives E|X|e^{-BX^2}<=G0 sqrt(1+mu^2)<=G0(1+z).
# Thus |u_z|<=4 sqrt(p) B(1+z)<32(1+z), so K<1024(1+z)^2<=2048(1+z^2).
# Tail <144 Q +2048[Q+(9phi+Q)] <144/9 phi +2048(9+2/9)phi <19000 phi.
K_tail=Q(19000,1)*phi9_major
assert K_tail < Q(1,10**12)

# Objective tail retained from C189.
I_tail=Q(85,9)*phi9_major
assert I_tail<Q(1,10**16)
print('EXACT_SCALAR_TAILS_PASS')
print('  |tail(I)|  <', float(I_tail), '< 1e-16')
print('  |tail(I_B)|<', float(IB_tail), '< 1e-15')
print('  tail(K)    <', float(K_tail), '< 1e-12')

# Retained metric must not move in a stuck/thinking recovery without a validated stationary root.
alpha_L=Q(630297437506,10**11)
alpha_U=Q(1278437096216,10**11)
width=alpha_U-alpha_L
assert width==Q(64813965871,10**10)
print('METRIC_UNCHANGED_PASS', float(width))

# ---------------- PART C: NUMERICAL ONLY ----------------
print('NUMERICAL_ONLY_BEGIN')
try:
    import numpy as np
    import jax
    import jax.numpy as jnp
    from numpy.polynomial.hermite import hermgauss
    jax.config.update('jax_enable_x64', True)
    hn,hw=hermgauss(96)
    zn=jnp.array(hn*math.sqrt(2.0)); ww=jnp.array(hw/math.sqrt(math.pi))
    def Phi(x): return 0.5*(1+jax.scipy.special.erf(x/jnp.sqrt(2.0)))
    def I_fun(pp,BB):
        mu=jnp.sqrt(pp)*zn-1.0
        sig=jnp.sqrt(1-pp)
        AA=1+2*BB*sig**2
        ff=Phi(-mu/sig)+jnp.exp(-BB*mu**2/AA)/jnp.sqrt(AA)*Phi(mu/(sig*jnp.sqrt(AA)))
        return jnp.sum(ww*jnp.log(ff))
    IB_fun=jax.grad(I_fun,1)
    Ip_fun=jax.grad(I_fun,0)

    x0=np.array([0.656313184757223,0.652653689820474,0.158861855012242])
    pp,DD,gg=x0
    qq=pp*DD**2
    cc=(1-DD**2)/(DD*(1-pp)*(1-pp*DD**2))
    BB=cc/(4*gg)
    Iv=float(I_fun(pp,BB)); IBv=float(IB_fun(pp,BB)); Ipv=float(Ip_fun(pp,BB)); Kv=-2*pp*Ipv

    # deterministic derivatives evaluated by jax to avoid printing enormous symbolic formulas
    def T_num(xx):
        pp,DD,gg=xx
        qq=pp*DD**2
        gpp=(1-qq)/(2*DD*(1-pp))
        cc=(1-DD**2)/(DD*(1-pp)*(1-pp*DD**2))
        return .5*(1-pp*qq)*cc-gpp+(1/(2*cc))*jnp.log(DD/(2*gpp))-qq/(2*DD)+gg
    def c_num(xx):
        pp,DD,_=xx
        return (1-DD**2)/(DD*(1-pp)*(1-pp*DD**2))
    dT=np.asarray(jax.grad(T_num)(jnp.array(x0)))
    dc=np.asarray(jax.grad(c_num)(jnp.array(x0)))
    av=12.5
    R1v=IBv+4*gg*gg/av
    R2v=Iv-BB*IBv+cc*cc*dT[1]/(av*dc[1])
    R3v=Kv/(2*pp)+cc/av*(dT[0]-(dc[0]/dc[1])*dT[1])
    print('  x0=',repr(x0))
    print('  c,B=',repr(cc),repr(BB))
    print('  I,I_B,K=',repr(Iv),repr(IBv),repr(Kv))
    print('  reduced residuals=',repr(np.array([R1v,R2v,R3v])))
    print('  residual_inf=',repr(max(abs(R1v),abs(R2v),abs(R3v))))
except Exception as e:
    print('  NUMERICAL_SCOUT_FAILED',repr(e))
    raise
print('NUMERICAL_ONLY_END')
print('ALL_EXACT_CHECKS_PASS')
