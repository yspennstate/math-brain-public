#!/usr/bin/env python3
import sympy as sp
import numpy as np
from fractions import Fraction

# Exact symbolic variables
K,k,x,th = sp.symbols("K k x th", positive=True)
D = 2*K*k

# 1. Spectral 2x2 block for A = C_L C_R + C_R C_L.
block = sp.Matrix([
    [x-2*K, sp.sqrt(x)*(k-1)],
    [sp.sqrt(x)*(K-1), x-2*k],
])
char = sp.factor(block.charpoly().as_expr())
disc = sp.factor((sp.trace(block))**2 - 4*block.det())
assert sp.simplify(disc - 4*((K-k)**2 + x*(K-1)*(k-1))) == 0
lam_plus = sp.simplify(x-(K+k)+sp.sqrt((K-k)**2+x*(K-1)*(k-1)))
lam_minus = sp.simplify(x-(K+k)-sp.sqrt((K-k)**2+x*(K-1)*(k-1)))

# Concrete (9,3): K=8,k=2, Ramanujan bulk x in [2,18].
lp18 = sp.simplify(lam_plus.subs({K:8,k:2,x:18}))
assert lp18 == 8+9*sp.sqrt(2)
beta = sp.simplify(lp18/32)
gap = sp.simplify(1-beta)
assert gap == sp.Rational(3,4)-9*sp.sqrt(2)/32

# 2. Interior radial rows for ancestor edge-distance.
# Type L and type R counts at increments -2,-1,+1,+2.
rowL = {-2:1, -1:k-1, 1:(K-1)*k, 2:K*k}
rowR = {-2:1, -1:K-1, 1:(k-1)*K, 2:K*k}
assert sp.simplify(sum(rowL.values())-D) == 0
assert sp.simplify(sum(rowR.values())-D) == 0

mL = sp.factor(sum(delta*cnt for delta,cnt in rowL.items())/D)
mR = sp.factor(sum(delta*cnt for delta,cnt in rowR.items())/D)
v_count = sp.factor((mL+mR)/2)
assert v_count == (3*K*k-K-k-1)/(2*K*k)

# 3. Tilted jump matrix and exact continuous-time cumulants.
a = (sp.exp(-2*th)+K*k*sp.exp(2*th))/D
bL = ((k-1)*sp.exp(-th)+(K-1)*k*sp.exp(th))/D
bR = ((K-1)*sp.exp(-th)+(k-1)*K*sp.exp(th))/D
Mth = sp.Matrix([[a,bL],[bR,a]])
lambda_pf = a + sp.sqrt(bL*bR)  # Perron branch near theta=0.
v = sp.factor(sp.diff(lambda_pf,th).subs(th,0).replace(sp.Abs, lambda z: z))
sigma2 = sp.factor(sp.diff(lambda_pf,th,2).subs(th,0).replace(sp.Abs, lambda z: z))
# Sympy may leave Abs(K*k-1); impose K*k>1.
v = sp.factor(v.xreplace({sp.Abs(K*k-1):K*k-1}))
sigma2 = sp.factor(sigma2.xreplace({sp.Abs(K*k-1):K*k-1}))
assert v == (3*K*k-K-k-1)/(2*K*k)
assert sigma2 == (5*K**2*k**2-K**2-k**2-3)/(2*K*k*(K*k-1))

v82 = sp.simplify(v.subs({K:8,k:2}))
s282 = sp.simplify(sigma2.subs({K:8,k:2}))
assert v82 == sp.Rational(37,32)
assert s282 == sp.Rational(403,160)
tau2 = sp.factor(s282/v82**3)
assert tau2 == sp.Rational(412672,253265)
profile_L_var = sp.factor(2*tau2)  # scale sqrt(log_16 n), since ell=2 log_16 n.
assert profile_L_var == sp.Rational(825344,253265)

# 4. Exact finite operator sanity check on incidence bigraph of K4:
# (K+1,k+1)=(3,2), girth 6. The Hermitianized macro-NBRW graph is simple 4-regular.
verts = list(range(4))
redges = [(i,j) for i in verts for j in verts if i<j]
inc = []
for l in verts:
    for ri,(i,j) in enumerate(redges):
        if l in (i,j):
            inc.append((l,ri))
nE = len(inc)
CL = np.zeros((nE,nE), dtype=int)
CR = np.zeros((nE,nE), dtype=int)
for p,(l,r) in enumerate(inc):
    for q,(l2,r2) in enumerate(inc):
        if p==q:
            continue
        if l==l2:
            CL[p,q]=1
        if r==r2:
            CR[p,q]=1
A = CL@CR + CR@CL
assert np.all(np.diag(A)==0)
assert set(np.unique(A)).issubset({0,1})
assert np.all(A.sum(axis=1)==4)
spec = np.linalg.eigvalsh(A)
target = np.array([-2]*5 + [0]*3 + [2]*3 + [4], dtype=float)
assert np.max(np.abs(np.sort(spec)-target)) < 1e-10

# 5. Concrete branching mismatch and radial row.
rowL82 = {d:int(sp.N(c.subs({K:8,k:2}) if hasattr(c,'subs') else c))
          for d,c in rowL.items()}
rowR82 = {d:int(sp.N(c.subs({K:8,k:2}) if hasattr(c,'subs') else c))
          for d,c in rowR.items()}
assert rowL82 == {-2:1,-1:1,1:14,2:16}
assert rowR82 == {-2:1,-1:7,1:8,2:16}
assert 16 < 31  # universal shell branching vs degree-32 tree benchmark.

print("spectral_charpoly =", char)
print("spectral_discriminant =", disc)
print("K8_k2_bulk_top =", lp18)
print("K8_k2_beta =", beta)
print("K8_k2_gap =", gap, "=", float(gap))
print("radial_row_L =", rowL82)
print("radial_row_R =", rowR82)
print("v =", v82)
print("sigma2 =", s282)
print("tau2_natural_sqrt_ell =", tau2)
print("profile_variance_sqrt_log16n =", profile_L_var)
print("profile_inverse_sd_coefficient =", float(sp.sqrt(1/profile_L_var)))
print("finite_K4_incidence_spectrum =", [round(float(z),12) for z in spec])
print("branching_check = 16 < 31")
print("P26_T08_HERMITIAN_NBRW_BERRY_GREEN_EXACT_PASS")
