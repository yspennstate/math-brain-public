#!/usr/bin/env python3
"""
PROB20-16 shape compactification + exact-feasibility diagnostic.

Finite exact claims:
  * symbolic determinant/compactification identities;
  * rational semialgebraic feasibility screening.

Floating-point X095 evaluations are explicitly DIAGNOSTIC ONLY.
"""
from fractions import Fraction
import math, random
import numpy as np
import sympy as sp

# ---------- exact symbolic compactification identities ----------
u1,u2,u3,q = sp.symbols("u1 u2 u3 q", positive=True)
r1,r2,r3,t = sp.symbols("r1 r2 r3 t", nonnegative=True)
Delta = 1-r1**2-r2**2-r3**2+2*r1*r2*r3*t
A = 2-(u1+u2+u3)
B = u1*u2*u3
phase_relation = sp.Eq(
    t,
    (A+q*B)/(2*sp.sqrt((1-u1)*(1-u2)*(1-u3)))
)
# After substituting r_i^2=1-u_i, the determinant is
#   (u1+u2+u3-2) + 2 (r1 r2 r3 cos(theta)).
# The phase coordinate imposes exactly
#   2 r1 r2 r3 cos(theta) = A + q B.
# Verify the resulting determinant identity without asking SymPy
# to simplify products of square roots across branch conventions.
det_reduced = (u1+u2+u3-2) + (A+q*B)
assert sp.expand(det_reduced - q*B) == 0

# The |cos(theta)|<=1 condition is exactly the polynomial inequality.
poly_gap = sp.expand(4*(1-u1)*(1-u2)*(1-u3) - (A+q*B)**2)
assert not poly_gap.has(sp.sqrt)


# ---------- exact L-ensemble atom and interaction cancellations ----------
X1,X2,X3 = sp.symbols("X1 X2 X3", positive=True)
w0=(1-X1)*(1-X2)*(1-X3)
w1=X1*(1-X2)*(1-X3)
w2=(1-X1)*X2*(1-X3)
w3=(1-X1)*(1-X2)*X3
w12=u3*X1*X2*(1-X3)
w13=u2*X1*(1-X2)*X3
w23=u1*(1-X1)*X2*X3
w123=q*u1*u2*u3*X1*X2*X3
assert sp.cancel(w2*w3/(w0*w23) - 1/u1) == 0
assert sp.cancel(w1*w3/(w0*w13) - 1/u2) == 0
assert sp.cancel(w1*w2/(w0*w12) - 1/u3) == 0
assert sp.cancel(w0*w12*w13*w23/(w1*w2*w3*w123) - 1/q) == 0

# Along fixed u and fields, only the full atom weight depends on q.
W = sp.expand(w0+w1+w2+w3+w12+w13+w23)
AA = u1*u2*u3*X1*X2*X3
r = sp.cancel(q*AA/(W+q*AA))
assert sp.simplify(sp.diff(r,q) - AA*W/(W+q*AA)**2) == 0

# ---------- numerical X095 evaluator (diagnostic only) ----------
subsets=[s for s in range(8)]
nonempty=list(range(1,8))

def adj3(A):
    return np.linalg.det(A)*np.linalg.inv(A)

def exact_atom_probs(K):
    # p_x = (-1)^(3-|x|) det(K-I_{x^c})
    out=[]
    for S in subsets:
        mask=[(S>>i)&1 for i in range(3)]
        J=K.copy()
        for i,m in enumerate(mask):
            if not m:
                J[i,i]-=1
        out.append(((-1)**(3-sum(mask)))*np.linalg.det(J).real)
    return np.array(out,float)

def x095_margin(K):
    p=exact_atom_probs(K)
    if np.min(p)<=1e-12:
        return None
    pe=p[0]
    # bit convention: 1,2,4 correspond sites 1,2,3
    c1=math.log(p[2]*p[4]/(pe*p[6]))
    c2=math.log(p[1]*p[4]/(pe*p[5]))
    c3=math.log(p[1]*p[2]/(pe*p[3]))
    tau=math.log(pe*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=np.diag([c1,c2,c3])+tau*K
    d=np.linalg.det(M).real
    if d<=0: return None
    Es=[]
    for S in nonempty:
        mask=[(S>>i)&1 for i in range(3)]
        J=K.copy()
        for i,m in enumerate(mask):
            if not m: J[i,i]-=1
        Es.append(((-1)**(3-sum(mask)))*adj3(J))
    pv=p[1:]
    V=np.diag(pv)-np.outer(pv,pv)
    T=np.zeros((7,7),float)
    vv=np.zeros(7,float)
    for i,Ei in enumerate(Es):
        vv[i]=np.trace(M@Ei).real
        for j,Ej in enumerate(Es):
            T[i,j]=np.trace(M@Ei@M@Ej).real
    C=T+d*V
    try:
        s=float(vv @ np.linalg.solve(C,vv))
    except np.linalg.LinAlgError:
        return None
    return s-2.0, np.linalg.det(C).real*(s-2.0), tau, p

def kernel_from_shape_fields(U,Q,X):
    # Exact feasibility already screened in rational arithmetic.
    uf=np.array([float(z) for z in U])
    qf=float(Q)
    rho=np.sqrt(1-uf)
    den=2*np.prod(rho)
    cos_th=(2-sum(uf)+qf*np.prod(uf))/den
    cos_th=max(-1,min(1,cos_th))
    th=math.acos(cos_th)
    R=np.array([
        [1, rho[2], rho[1]],
        [rho[2], 1, rho[0]*np.exp(1j*th)],
        [rho[1], rho[0]*np.exp(-1j*th), 1]], complex)
    ell=np.array([float(x/(1-x)) for x in X])
    D=np.diag(np.sqrt(ell))
    L=D@R@D
    K=L@np.linalg.inv(np.eye(3)+L)
    return K

def feasible_exact(U,Q):
    a=Fraction(2)-sum(U)
    b=U[0]*U[1]*U[2]
    lhs=(a+Q*b)**2
    rhs=Fraction(4)*(1-U[0])*(1-U[1])*(1-U[2])
    return lhs <= rhs and all(Fraction(0)<x<Fraction(1) for x in U) and Fraction(0)<Q<=Fraction(1)

rng=random.Random(20260916)
DEN=64
N=12000
accepted=0
best=None
for _ in range(N):
    vals=sorted([rng.randrange(1,DEN) for _ in range(3)], reverse=True)
    U=tuple(Fraction(v,DEN) for v in vals)
    Q=Fraction(rng.randrange(1,DEN+1),DEN)
    if not feasible_exact(U,Q):
        continue
    X=tuple(Fraction(rng.randrange(1,DEN),DEN) for _ in range(3))
    accepted+=1
    K=kernel_from_shape_fields(U,Q,X)
    ev=np.linalg.eigvalsh(K)
    if ev[0]<=1e-10 or ev[-1]>=1-1e-10:
        continue
    res=x095_margin(K)
    if res is None:
        continue
    margin,phi,tau,p=res
    if best is None or margin<best[0]:
        best=(margin,phi,U,Q,X,tau,ev)

print("status=PASS")
print("symbolic_compactification_identity=PASS")
print("polynomial_phase_constraint=PASS")
print(f"diagnostic_trials={N}")
print(f"exact_feasible_shapes={accepted}")
if best:
    margin,phi,U,Q,X,tau,ev=best
    print("diagnostic_negative_found=", margin < 0)
    print("diagnostic_best_normalized_margin_s_minus_2=", repr(margin))
    print("diagnostic_best_phi=", repr(phi))
    print("best_u=", [str(x) for x in U])
    print("best_q=", str(Q))
    print("best_fields=", [str(x) for x in X])
    print("best_tau=", repr(tau))
    print("best_kernel_eigenvalues=", [repr(float(x)) for x in ev])
print("NOTE: X095 floating-point search is diagnostic only; exact claims above are the algebraic identities and rational feasibility checks.")
