#!/usr/bin/env python3
"""
Exact/sanity checker for NM13-01 T08 Schreier-Hecke fiber transfer.

Exact core:
  * J=S4, H=< (12) >, |J/H|=12.
  * Three inverse-closed nontrivial H-double cosets give symmetric 2-regular
    orbital kernels K_A,K_B,K_C.
  * Their union refresh R=(K_A+K_B+K_C)/3 has exact gap 2/3.
  * K_A has one-sided gap 0 and [K_A,R] has norm sqrt(2)/3, so the
    cross kernel is neither a permutation/isometry nor a common-gap switch.
  * Degree/gap/cutoff/non-LRE constants are checked symbolically.

Finite numerical sanity only (NOT asymptotic evidence):
  * Base K7 = Cay(Z7,{±1,±2,±3}).
  * Output kernel P_H=(2/3) P_G⊗K_A +(1/3) I⊗R on 84 states.
  * Check the exact projected-base lower bound and the proved fiber upper
    bound at several continuous times.
"""
from itertools import permutations
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

def comp(p, q):
    # p o q
    return tuple(p[q[i]] for i in range(4))

def inv(p):
    ans = [0] * 4
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)

def trans(i, j):
    p = list(range(4))
    p[i], p[j] = p[j], p[i]
    return tuple(p)

J = list(permutations(range(4)))
e = tuple(range(4))
a = trans(0, 1)                     # (12)
H = {e, a}

def right_coset(g):
    return frozenset(comp(g, h) for h in H)

cosets = []
for g in J:
    C = right_coset(g)
    if C not in cosets:
        cosets.append(C)
assert len(cosets) == 12
cidx = {C: i for i, C in enumerate(cosets)}

rA = trans(0, 2)                    # (13)
rB = trans(0, 3)                    # (14)
rC = comp(trans(0, 2), trans(1, 3)) # (13)(24)

def double_coset(r):
    return {comp(comp(h1, r), h2) for h1 in H for h2 in H}

Ds = [double_coset(r) for r in (rA, rB, rC)]
assert [len(D) for D in Ds] == [4, 4, 4]
assert all(D == {inv(x) for x in D} for D in Ds)

def orbital(D):
    M = sp.zeros(12, 12)
    for i, C in enumerate(cosets):
        g = next(iter(C))
        counts = [0] * 12
        for d in D:
            counts[cidx[right_coset(comp(g, d))]] += 1
        for j, count in enumerate(counts):
            if count:
                M[i, j] = sp.Rational(count, len(D))
    return M

KA, KB, KC = [orbital(D) for D in Ds]
for K in (KA, KB, KC):
    assert K == K.T
    assert all(sum(K.row(i)) == 1 for i in range(12))
    assert {sum(1 for x in K.row(i) if x != 0) for i in range(12)} == {2}

# The three orbital supports are disjoint, so their union is simple 6-regular.
for i in range(12):
    for j in range(12):
        nz = sum(K[i, j] != 0 for K in (KA, KB, KC))
        assert nz <= 1

R = (KA + KB + KC) / 3
refresh_charpoly = sp.factor(R.charpoly().as_expr())
lam = sp.Symbol("lambda")
expected_refresh = sp.factor(
    lam**2 * (lam - 1) * (3*lam - 1)**3 * (3*lam + 1)**6 / 19683
)
assert sp.expand(refresh_charpoly - expected_refresh) == 0
# Eigenvalues: 1, 1/3 (mult 3), 0 (mult 2), -1/3 (mult 6).
eta = sp.Rational(2, 3)

# K_A itself has eigenvalue 1 of multiplicity 4, hence no positive one-sided gap.
KA_charpoly = sp.factor(KA.charpoly().as_expr())
assert sp.expand(KA_charpoly - (lam - 1)**4 * (2*lam + 1)**8 / 256) == 0

# Strong noncommutation.
C_AR = KA*R - R*KA
CAR_charpoly = sp.factor((C_AR.T*C_AR).charpoly().as_expr())
assert sp.expand(CAR_charpoly - lam**6*(9*lam - 2)**6 / 531441) == 0
comm_AR_norm = sp.sqrt(sp.Rational(2, 9))

pair_charpoly = None
for X, Y in ((KA, KB), (KA, KC), (KB, KC)):
    C = X*Y - Y*X
    cp = sp.factor((C.T*C).charpoly().as_expr())
    assert sp.expand(cp - lam**6*(2*lam - 1)**6 / 64) == 0
    pair_charpoly = cp

# Degree-six Ramanujan base; k=2 cross neighbors per generator, r=6 refresh.
d, k, r = 6, 2, 6
Dout = k*d + r
cross_rate = sp.Rational(k*d, Dout)  # 2/3
refresh_rate = sp.Rational(r, Dout)  # 1/3
gamma_base = 1 - 2*sp.sqrt(5)/6
gap_bound = sp.simplify(cross_rate * gamma_base)
assert gap_bound < refresh_rate*eta
assert sp.simplify(gap_bound - 2*(3-sp.sqrt(5))/9) == 0

# Base CT center (3/2) log_5 n; rescale by cross rate 2/3.
center_coeff = sp.simplify(sp.Rational(3, 2) / cross_rate)
assert center_coeff == sp.Rational(9, 4)

# Fiber error exp(-(b eta) T_H) = n^{-1/(2 ln 5)} up to fixed factor.
fiber_exponent = 1/(2*math.log(5))

# Non-LRE exponent at r=(1/2)log_17 N.
beta = 0.5*(1 - math.log(5)/math.log(17))
assert beta > 0

# Finite sanity model: K7 base, 84-state output.
nB = 7
PB = (np.ones((nB, nB)) - np.eye(nB))/6.0
KAn = np.array(KA.tolist(), dtype=float)
Rn = np.array(R.tolist(), dtype=float)
PH = (2/3)*np.kron(PB, KAn) + (1/3)*np.kron(np.eye(nB), Rn)
assert np.max(np.abs(PH-PH.T)) < 1e-12
assert np.max(np.abs(PH.sum(axis=1)-1)) < 1e-12
assert set(np.count_nonzero(row > 1e-12) for row in PH) == {18}
assert np.max(np.abs(PH[PH > 1e-12] - 1/18)) < 1e-12

def tv_from_zero(P, t):
    mu = expm(t*(P - np.eye(P.shape[0])))[0, :]
    pi = np.ones(P.shape[0])/P.shape[0]
    return 0.5*np.abs(mu-pi).sum()

print("S4/H states =", len(cosets))
print("double coset sizes =", [len(D) for D in Ds])
print("orbital row degree =", [2, 2, 2])
print("refresh charpoly =", refresh_charpoly)
print("refresh gap =", eta)
print("K_A charpoly =", KA_charpoly)
print("K_A one-sided gap = 0 (eigenvalue 1 has multiplicity 4)")
print("cross-refresh commutator CtC charpoly =", CAR_charpoly)
print("cross-refresh commutator operator norm =", comm_AR_norm)
print("pairwise orbital commutator CtC charpoly =", pair_charpoly)
print("pairwise orbital commutator operator norm =", sp.sqrt(sp.Rational(1,2)))
print("output degree d=6 =", Dout)
print("cross rate =", cross_rate, "refresh rate =", refresh_rate)
print("gap lower bound exact =", gap_bound)
print("gap lower bound numeric =", float(gap_bound))
print("cutoff center coefficient on log_5 n =", center_coeff)
print("fiber error exponent in n =", fiber_exponent)
print("non-LRE exponent beta =", beta)
print("finite toy states =", PH.shape[0], "degree = 18")
for t in (0.5, 1.0, 2.0, 4.0, 8.0):
    base_tv = tv_from_zero(PB, (2/3)*t)
    out_tv = tv_from_zero(PH, t)
    fiber_bound = 0.5*math.sqrt(11)*math.exp(-(2/9)*t)
    assert base_tv <= out_tv + 1e-10
    assert out_tv <= base_tv + fiber_bound + 1e-10
    print(
        f"toy t={t:.1f} baseTV={base_tv:.12f} "
        f"outTV={out_tv:.12f} fiberBound={fiber_bound:.12f}"
    )
print("ALL_EXACT_AND_SANITY_CHECKS_PASS")
