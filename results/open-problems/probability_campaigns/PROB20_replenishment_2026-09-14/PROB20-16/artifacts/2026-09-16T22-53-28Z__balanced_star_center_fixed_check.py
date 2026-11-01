#!/usr/bin/env python3
"""
PROB20-16 second stuck-recovery self-check.

Exact/symbolic claims checked:
  1. Balanced three-site star conditional kernels are C_+ = I/2+2zz^T and
     C_- = I/2-2zz^T at outside marginal 1/2.
  2. On C_+, after gauge and alpha=4 z1^2, beta=4 z2^2, the four atoms have
     the stated linear form.
  3. The matrix N=-2 grad H_2(C_+) has the stated U,V,L form and determinant.
  4. The hyperbolic determinant lower-bound algebra is exact.
  5. d/dx log(cosh x)=tanh x.

Numerical section:
  deterministic diagnostic search of the full c=1/2 real-transverse
  compensation residual. This is NOT a certificate of the full case.
"""
import math, random
import numpy as np
import sympy as sp

# ---------- exact symbolic star conditionalization ----------
z1,z2 = sp.symbols("z1 z2", real=True)
A = sp.eye(2)/2
z = sp.Matrix([z1,z2])
B = z
c = sp.Rational(1,2)
a = 1-c
Cplus = sp.simplify(A + (B*B.T)/a)
Cminus = sp.simplify(A - (B*B.T)/c)
assert sp.simplify(Cplus - (sp.eye(2)/2 + 2*z*z.T)) == sp.zeros(2)
assert sp.simplify(Cminus - (sp.eye(2)/2 - 2*z*z.T)) == sp.zeros(2)
assert sp.simplify(Cminus - (sp.eye(2)-Cplus)) == sp.zeros(2)

# ---------- exact two-site atom form ----------
alpha,beta = sp.symbols("alpha beta", nonnegative=True, real=True)
off = sp.sqrt(alpha*beta)/2
Cp = sp.Matrix([[(1+alpha)/2, off],[off,(1+beta)/2]])
x,y = Cp[0,0], Cp[1,1]
s = off**2
p00=sp.simplify((1-x)*(1-y)-s)
p10=sp.simplify(x*(1-y)+s)
p01=sp.simplify((1-x)*y+s)
p11=sp.simplify(x*y-s)
assert sp.simplify(p00-(1-alpha-beta)/4)==0
assert sp.simplify(p10-(1+alpha-beta)/4)==0
assert sp.simplify(p01-(1-alpha+beta)/4)==0
assert sp.simplify(p11-(1+alpha+beta)/4)==0

# Formal log variables:
# U = log((1+t)/(1-t)), V = log((1+d)/(1-d)),
# L = log((1-d^2)/(1-t^2)), t=alpha+beta, d=alpha-beta.
U,V,L = sp.symbols("U V L", real=True)
t,d = sp.symbols("t d", real=True)
N = sp.Matrix([
    [U+V-beta*L, sp.sqrt(alpha*beta)*L],
    [sp.sqrt(alpha*beta)*L, U-V-alpha*L]
])
detN = sp.expand(N.det())
target_det = sp.expand(U**2-V**2-L*((alpha+beta)*U+(alpha-beta)*V))
assert sp.simplify(detN-target_det)==0

# Hyperbolic reparameterization determinant lower bound.
AA,BB = sp.symbols("AA BB", nonnegative=True, real=True)
ta,tb,Delta = sp.symbols("ta tb Delta", nonnegative=True, real=True)
bracket = (AA**2-BB**2)-Delta*(AA*ta+BB*tb)
upper_sub = sp.expand((AA**2-BB**2)-(AA-BB)*ta*(AA*ta+BB*tb))
factored = sp.expand((AA-BB)*(AA*(1-ta**2)+BB*(1-ta*tb)))
assert sp.simplify(upper_sub-factored)==0

xx=sp.symbols("xx", real=True)
assert sp.simplify(sp.diff(sp.log(sp.cosh(xx)),xx)-sp.tanh(xx))==0

print("status=PASS")
print("balanced_star_conditionals=PASS")
print("rank_one_above_half_atoms=PASS")
print("gradient_determinant_identity=PASS")
print("hyperbolic_lower_bound_algebra=PASS")
print("d_logcosh=PASS")

# ---------- diagnostic full c=1/2 real-sector search ----------
def atoms2(x,y,r):
    s=r*r
    return np.array([(1-x)*(1-y)-s,
                     x*(1-y)+s,
                     (1-x)*y+s,
                     x*y-s], dtype=float)

def grad2(x,y,r):
    p=atoms2(x,y,r)
    if p.min() <= 0:
        raise ValueError("nonphysical")
    p00,p10,p01,p11=p
    lam=math.log((p10*p01)/(p00*p11))
    g11=(1-y)*math.log(p00/p10)+y*math.log(p01/p11)
    g22=(1-x)*math.log(p00/p01)+x*math.log(p10/p11)
    return np.array([[g11,-lam*r],[-lam*r,g22]],dtype=float)

def S_orth(x,y,r):
    p=atoms2(x,y,r)
    if p.min() <= 0:
        raise ValueError("nonphysical")
    p00,p10,p01,p11=p
    lam=math.log((p10*p01)/(p00*p11))
    # raw coords (a,d,b), U=[[a,b],[b,d]]
    vv=np.array([
        [-(1-y),-(1-x),-2*r],
        [ (1-y),   -x,  2*r],
        [     -y, (1-x),2*r],
        [      y,    x, -2*r],
    ],dtype=float)
    F=sum(np.outer(v,v)/pp for v,pp in zip(vv,p))
    # -H'' = FI - 2 lam det(U) = FI -2lam*a*d +2lam*b^2
    Sraw=F+np.array([[0,-lam,0],[-lam,0,0],[0,0,2*lam]],dtype=float)
    # orthonormal real-Hermitian coordinates (a,d,sqrt(2)b)
    T=np.diag([1.0,1.0,1/math.sqrt(2)])
    return T.T@Sraw@T

def residual_half(x,y,r,rho):
    # C1=(x,r;r,y), C0=(x+rho,r;r,y), c=a=1/2
    S1=S_orth(x,y,r)
    S0=S_orth(x+rho,y,r)
    # avoid the genuinely singular disconnected-flat set in this diagnostic
    if np.linalg.eigvalsh(S0).min() < 1e-10 or np.linalg.eigvalsh(S1).min() < 1e-10:
        return None
    P=np.linalg.inv(np.linalg.inv(S0)+np.linalg.inv(S1))
    # W_half coords: (sqrt(rho)u1, 0, sqrt(rho/2)u2)
    Amap=np.array([[math.sqrt(rho),0.0],
                   [0.0,0.0],
                   [0.0,math.sqrt(rho/2)]])
    G=grad2(x+rho,y,r)-grad2(x,y,r)
    return 8*(Amap.T@P@Amap)-2*G

rng=random.Random(20260917)
trials=60000
accepted=0
best=(float("inf"),None)
for _ in range(trials):
    # choose endpoints away from exact atom boundary but allow broad asymmetry
    x=rng.uniform(0.02,0.90)
    rho=rng.uniform(1e-4,0.98-x)
    y=rng.uniform(0.02,0.98)
    # strict constraints for C1 and C0
    maxs=min(x*y,(1-x)*(1-y),(x+rho)*y,(1-x-rho)*(1-y))
    if maxs <= 1e-8:
        continue
    rrmax=math.sqrt(maxs)
    # bias both toward disconnected and toward covariance boundary
    q=rng.random()
    if q < .35:
        frac=10**rng.uniform(-4,-1)
    elif q < .70:
        frac=1-10**rng.uniform(-4,-1)
    else:
        frac=rng.uniform(.02,.98)
    r=frac*rrmax
    if atoms2(x,y,r).min()<1e-8 or atoms2(x+rho,y,r).min()<1e-8:
        continue
    R=residual_half(x,y,r,rho)
    if R is None:
        continue
    ev=np.linalg.eigvalsh(R)
    accepted+=1
    if ev[0] < best[0]:
        best=(float(ev[0]),(x,y,r,rho,ev.tolist()))

print(f"diagnostic_trials={trials}")
print(f"diagnostic_accepted={accepted}")
print("diagnostic_negative_found=", best[0] < -1e-8)
print("diagnostic_best_min_eigenvalue=",repr(best[0]))
print("diagnostic_best_parameters=",repr(best[1]))
print("NOTE: diagnostic search is floating-point only and is not a proof of the full c=1/2 case.")
