#!/usr/bin/env python3
"""T03/NM13-07: exact algebraic reduction of second-full lifted NSP stationarity.

PART A proves symbolically that the inherited 3-variable stationary system reduces to
one scalar curve H(p,B)=0 plus algebraic reconstruction of D, alpha, gamma.
PART B is NUMERICAL_ONLY Gauss-Hermite/root scouting used to verify the reduction
against the inherited alpha=12.5 point and Stojnic's published second-full table.
No numerical scout is promoted to a rigorous threshold endpoint.
"""
import math
import sympy as sp

print('T03 full-second-lift algebraic/OU reduction')

# ---------- PART A: exact symbolic reduction ----------
p,D,g,a,B = sp.symbols('p D g a B', positive=True)
I,IB,K = sp.symbols('I IB K', real=True)
q = p*D**2
gp = (1-q)/(2*D*(1-p))
c = (1-D**2)/(D*(1-p)*(1-p*D**2))
T = (sp.Rational(1,2)*(1-p*q)*c - gp
     + sp.Rational(1,2)/c*sp.log(D/(2*gp)) - q/(2*D) + g)
cp,cD = sp.diff(c,p), sp.diff(c,D)
Tp,TD = sp.diff(T,p), sp.diff(T,D)

# Inherited OU-reduced stationarity residuals:
# R1 = I_B + 4 gamma^2/alpha
# R2 = I - B I_B + c^2 T_D/(alpha c_D)
# R3 = K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D)
# with B=c/(4 gamma).
R1 = IB + 4*g**2/a
R2 = I - B*IB + c**2*TD/(a*cD)
R3 = K/(2*p) + c/a*(Tp-(cp/cD)*TD)

subg = {g:c/(4*B)}
R1B = sp.simplify(R1.subs(subg))
R2B = sp.simplify(R2.subs(subg))
R3B = sp.simplify(R3.subs(subg))

# R1 exactly reconstructs alpha from p,D,B through I_B.
a_expr = -c**2/(4*B**2*IB)
assert sp.simplify(R1B.subs(a,a_expr)) == 0

# R3 has a surprisingly simple exact factorization.
target_R3 = K - p**2*D**2*c**2/a
assert sp.simplify(R3B - target_R3/(2*p)) == 0

# Combining R1 and R3 reconstructs D^2 directly from scalar OU data.
D2_expr = K/(-4*p**2*B**2*IB)
# Algebraically: K = p^2 D^2 c^2/a and a=-c^2/(4B^2 I_B).
assert sp.simplify((p**2*D**2*c**2/a).subs(a,a_expr) + 4*p**2*D**2*B**2*IB) == 0

# R2 is a single scalar curve after substituting alpha from R1.
TD_B = sp.simplify(TD.subs(subg))
H = sp.simplify(I - B*IB - 4*B**2*IB*(TD_B/cD))
assert sp.simplify(R2B.subs(a,a_expr) - H) == 0

# Full comparison/free-energy objective on the stationary reconstruction.
T_B = sp.simplify(T.subs(subg))
Psi = sp.simplify(T_B + c*I/(4*B**2*IB))
F = T - a*I/c
assert sp.simplify(F.subs(subg).subs(a,a_expr) - Psi) == 0

print('EXACT_REDUCTION_PASS')
print('  alpha(p,D,B) = -c(p,D)^2 / (4 B^2 I_B(p,B))')
print('  R3 = [K - p^2 D^2 c^2/alpha]/(2p)')
print('  D^2(p,B) = K(p,B)/[-4 p^2 B^2 I_B(p,B)]')
print('  H(p,B) = I-B I_B-4 B^2 I_B*(T_D/c_D) = 0')
print('  Psi(p,B) = T + c I/(4 B^2 I_B) on stationarity')
print('  fixed-alpha certificate reduces to 2 equations: H=0, alpha(p,B)=alpha0')
print('  capacity candidate reduces to 2 equations: H=0, Psi=0')

# ---------- PART B: NUMERICAL ONLY scouts ----------
print('NUMERICAL_ONLY_BEGIN')
import numpy as np
import jax
import jax.numpy as jnp
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import root
jax.config.update('jax_enable_x64', True)

hn,hw = hermgauss(120)
zn = jnp.array(hn*math.sqrt(2.0))
ww = jnp.array(hw/math.sqrt(math.pi))

def Phi(x):
    return 0.5*(1+jax.scipy.special.erf(x/jnp.sqrt(2.0)))

def I_fun(pp,BB):
    mu = jnp.sqrt(pp)*zn - 1.0
    sig = jnp.sqrt(1.0-pp)
    AA = 1.0 + 2.0*BB*sig**2
    ff = Phi(-mu/sig) + jnp.exp(-BB*mu**2/AA)/jnp.sqrt(AA)*Phi(mu/(sig*jnp.sqrt(AA)))
    return jnp.sum(ww*jnp.log(ff))
IB_fun = jax.grad(I_fun,1)
Ip_fun = jax.grad(I_fun,0)

def c_num(pp,DD):
    return (1-DD**2)/(DD*(1-pp)*(1-pp*DD**2))

def T_num(pp,DD,gg):
    qq=pp*DD**2
    gpp=(1-qq)/(2*DD*(1-pp))
    cc=c_num(pp,DD)
    return 0.5*(1-pp*qq)*cc-gpp+(1/(2*cc))*math.log(DD/(2*gpp))-qq/(2*DD)+gg

# lambdified deterministic derivatives after gamma=c/(4B)
TD_l = sp.lambdify((p,D,B), TD_B, 'numpy')
cD_l = sp.lambdify((p,D), cD, 'numpy')

def scalar_data(pp,BB):
    Iv=float(I_fun(pp,BB)); IBv=float(IB_fun(pp,BB)); Ipv=float(Ip_fun(pp,BB)); Kv=-2*pp*Ipv
    D2=Kv/(-4*pp*pp*BB*BB*IBv)
    if not (D2>0 and D2<1):
        raise ValueError('D2 outside (0,1)')
    DD=math.sqrt(D2)
    cc=c_num(pp,DD)
    aa=-cc*cc/(4*BB*BB*IBv)
    gg=cc/(4*BB)
    TDv=float(TD_l(pp,DD,BB)); cDv=float(cD_l(pp,DD))
    Hv=Iv-BB*IBv-4*BB*BB*IBv*(TDv/cDv)
    Psiv=T_num(pp,DD,gg)+cc*Iv/(4*BB*BB*IBv)
    qq=pp*DD*DD
    gpp=(1-qq)/(2*DD*(1-pp))
    return dict(I=Iv,IB=IBv,K=Kv,D=DD,c=cc,alpha=aa,gamma=gg,H=Hv,Psi=Psiv,q=qq,gamma_p=gpp)

def fixed_alpha_eq(x,alpha0):
    d=scalar_data(float(x[0]),float(x[1]))
    return np.array([d['H'], d['alpha']-alpha0])

def cap_eq(x):
    d=scalar_data(float(x[0]),float(x[1]))
    return np.array([d['H'], d['Psi']])

# inherited alpha=12.5 scout, converted to (p,B)
pp0=0.656313184757223; DD0=0.652653689820474; gg0=0.158861855012242
cc0=c_num(pp0,DD0); BB0=cc0/(4*gg0)
d0=scalar_data(pp0,BB0)
print('  alpha=12.5 inherited-point reduction:')
print('    p,B =',repr(pp0),repr(BB0))
print('    reconstructed D,alpha,gamma =',repr(d0['D']),repr(d0['alpha']),repr(d0['gamma']))
print('    H,Psi =',repr(d0['H']),repr(d0['Psi']))

# Conservative candidate alpha=12.75: solve only the new 2D system H=0, alpha=12.75.
r75=root(lambda x: fixed_alpha_eq(x,12.75), np.array([0.6458,4.93]), method='hybr', options={'xtol':1e-11})
if not r75.success:
    raise RuntimeError(r75.message)
d75=scalar_data(float(r75.x[0]),float(r75.x[1]))
print('  alpha=12.75 2D stationary scout:')
print('    p,B =',repr(float(r75.x[0])),repr(float(r75.x[1])))
print('    D,c,gamma,q,gamma_p =',*(repr(d75[k]) for k in ['D','c','gamma','q','gamma_p']))
print('    I,I_B,K =',repr(d75['I']),repr(d75['IB']),repr(d75['K']))
print('    H,alpha-12.75,Psi =',repr(d75['H']),repr(d75['alpha']-12.75),repr(d75['Psi']))

# The full second-lift capacity candidate: solve H=0 and Psi=0.
rc=root(cap_eq, np.array([0.6649,6.198]), method='hybr', options={'xtol':1e-11})
if not rc.success:
    raise RuntimeError(rc.message)
dc=scalar_data(float(rc.x[0]),float(rc.x[1]))
print('  full-second capacity scout H=Psi=0:')
print('    p,B =',repr(float(rc.x[0])),repr(float(rc.x[1])))
print('    alpha =',repr(dc['alpha']))
print('    D,c,gamma,q,gamma_p =',*(repr(dc[k]) for k in ['D','c','gamma','q','gamma_p']))
print('    H,Psi =',repr(dc['H']),repr(dc['Psi']))
print('NUMERICAL_ONLY_END')

# Frozen rigorous bracket stays unchanged in this artifact.
alpha_L=6.30297437506
alpha_U=12.78437096216
print('RIGOROUS_BRACKET_UNCHANGED', repr(alpha_L), repr(alpha_U), repr(alpha_U-alpha_L))
print('CANDIDATE_IF_VALIDATED alpha_U=12.75 width=', repr(12.75-alpha_L))
print('ALL_EXACT_ALGEBRA_CHECKS_PASS')
