import math
import numpy as np
import sympy as sp

SEED = 20260916
rng = np.random.default_rng(SEED)

def topd_sq(X, d):
    sq = X * X
    return np.partition(sq, -d, axis=1)[:, -d:].sum(axis=1)

print("PROB20-19 near-isotropy self-check")
print("seed", SEED)

# 1. Scalar density-ratio expansion through t^2.
t, a, x = sp.symbols("t a x")
R = (1+t*a)**sp.Rational(-1,2) * sp.exp(
    -sp.Rational(1,2)*x**2*((1+t*a)**-1 - 1)
)
series = sp.series(R, t, 0, 3).removeO().expand()
L1 = sp.Rational(1,2)*(a*x**2-a)
L2 = sp.Rational(1,4)*a**2 - sp.Rational(1,2)*a**2*x**2
claimed = (1+t*L1+t**2*(L2+sp.Rational(1,2)*L1**2)).expand()
print("density_t2_symbolic_residual", sp.simplify(series-claimed))

# 2. Exact algebraic tensor reduction with formal invariants.
A4, B = sp.symbols("A4 B")
d11,d22,d33,o12,o13,o23 = sp.symbols("d11 d22 d33 o12 o13 o23")
D2 = d11**2+d22**2+d33**2
Dcross = d11*d22+d11*d33+d22*d33
O2 = o12**2+o13**2+o23**2
lhs = A4*D2 + 2*B*Dcross + 4*B*O2
tr = d11+d22+d33
tr2 = D2+2*O2
rhs = B*tr**2 + 2*B*tr2 + (A4-3*B)*D2
print("tensor_reduction_symbolic_residual", sp.expand(lhs-rhs))

# 3. Quartic orbit identities.
th, hi, hj = sp.symbols("th hi hj", real=True)
c, s = sp.cos(th), sp.sin(th)
pairD = (hi*c**2 + hj*s**2)**2 + (hi*s**2 + hj*c**2)**2
pairD2 = sp.simplify(sp.diff(pairD, th, 2).subs(th,0))
print("pair_D_second_derivative", pairD2)

# 4. p=4,d=2 estimate of Delta = E[f(G)(G1^4-3G1^2G2^2)].
N = 4_000_000
batch = 200_000
sumv = 0.0
sumv2 = 0.0
n = 0
for _ in range(N//batch):
    G = rng.standard_normal((batch,4))
    f = topd_sq(G,2)
    v = f*(G[:,0]**4 - 3*G[:,0]**2*G[:,1]**2)
    sumv += v.sum()
    sumv2 += np.dot(v,v)
    n += batch
delta = sumv/n
delta_se = math.sqrt((sumv2/n-delta*delta)/n)
print("delta_4_2_mc", delta, "se", delta_se, "z", delta/delta_se)

# 5. Arbitrary fixed spectral shape: paired eigenbasis vs strongly mixed orientation.
Hdiag = np.array([-1.0,-0.2,0.4,1.3])
tval = 0.03
evals = 1+tval*Hdiag
Q = 0.5*np.array([
    [1,1,1,1],
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
], dtype=float)
D_eig = float(np.dot(Hdiag,Hdiag))
A_mix = Q @ np.diag(Hdiag) @ Q.T
D_mix = float(np.dot(np.diag(A_mix), np.diag(A_mix)))
N2 = 2_000_000
batch2 = 200_000
sd = sd2 = 0.0
nn = 0
S0 = np.diag(np.sqrt(evals))
S1 = Q @ np.diag(np.sqrt(evals)) @ Q.T
for _ in range(N2//batch2):
    G = rng.standard_normal((batch2,4))
    f0 = topd_sq(G @ S0, 2)
    f1 = topd_sq(G @ S1.T, 2)
    v = f0-f1
    sd += v.sum()
    sd2 += np.dot(v,v)
    nn += batch2
gap = sd/nn
gap_se = math.sqrt((sd2/nn-gap*gap)/nn)
ratio = gap/(tval*tval*(D_eig-D_mix))
print("spectral_shape_D_eig", D_eig)
print("spectral_shape_D_mix", D_mix)
print("paired_KL_minus_mixed_gap", gap, "se", gap_se, "z", gap/gap_se)
print("gap_over_t2_Dgap", ratio)
print("delta_over_8_mc", delta/8)

# 6. Balanced negative-spike score Hessian near isotropy, lambda=0.9.
lam = 0.9
alpha = 1/lam - 1
N3 = 2_000_000
batch3 = 200_000
sh = sh2 = 0.0
nn = 0
control = 3.3
for _ in range(N3//batch3):
    W,A,Bb,Cc = rng.standard_normal((4,batch3))
    Dd = math.sqrt(lam)*W
    T = Dd*Dd + A*A + Bb*Bb + Cc*Cc
    f = 0.5*T + np.maximum.reduce([
        np.abs(Dd*A + Bb*Cc),
        np.abs(Dd*Bb + A*Cc),
        np.abs(Dd*Cc + A*Bb),
    ])
    score2 = alpha*(Dd*Dd-A*A) + alpha*alpha*Dd*Dd*A*A
    v = (f-control)*score2  # exact constant control variate since E score2 = 0
    sh += v.sum()
    sh2 += np.dot(v,v)
    nn += batch3
hess = sh/nn
hess_se = math.sqrt((sh2/nn-hess*hess)/nn)
print("balanced_hessian_lambda_0.9_mc", hess, "se", hess_se, "z", hess/hess_se)
