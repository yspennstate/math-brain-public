import itertools
import math
import numpy as np

# PROB20-16 checker for run 2026-09-15T16-43-36Z.
# Corroborative only: the analytic proof is in the report.
# Family: n=4 exchangeable core + two coherent 2-site satellites.

n = 4
u = np.ones(n, dtype=complex) / np.sqrt(n)
P = np.outer(u, u.conj())

C1 = np.array([[0.45, 0.08+0.03j],
               [0.08-0.03j, 0.55]], dtype=complex)
C2 = np.array([[0.52, -0.06+0.02j],
               [-0.06-0.02j, 0.42]], dtype=complex)
v1 = np.array([0.18+0.05j, 0.12-0.04j], dtype=complex)
v2 = np.array([0.15-0.03j, -0.10+0.06j], dtype=complex)
Cs = [C1, C2]
vs = [v1, v2]

endpoint0 = (0.32, 0.62, np.array([0.55+0.10j, 0.35-0.12j]))
endpoint1 = (0.48, 0.54, np.array([0.20-0.25j, 0.60+0.08j]))

def core(a, c):
    return a * (np.eye(n) - P) + c * P

def full_kernel(a, c, z):
    N = n + sum(C.shape[0] for C in Cs)
    K = np.zeros((N, N), dtype=complex)
    K[:n, :n] = core(a, c)
    off = n
    for zj, C, v in zip(z, Cs, vs):
        m = C.shape[0]
        K[:n, off:off+m] = zj * np.outer(u, v.conj())
        K[off:off+m, :n] = np.conj(zj) * np.outer(v, u.conj())
        K[off:off+m, off:off+m] = C
        off += m
    return K

def atom_probs(K):
    K = np.asarray(K, dtype=complex)
    N = K.shape[0]
    p = np.empty(1 << N, dtype=float)
    for mask in range(1 << N):
        M = K.copy()
        absent = [i for i in range(N) if not ((mask >> i) & 1)]
        for i in absent:
            M[i, i] -= 1
        val = ((-1) ** len(absent)) * np.linalg.det(M)
        assert abs(val.imag) < 2e-9
        p[mask] = val.real
    p[np.abs(p) < 1e-13] = 0.0
    assert p.min() > -2e-9
    assert abs(p.sum() - 1.0) < 2e-9
    return p

def entropy_kernel(K):
    p = atom_probs(K)
    q = p[p > 1e-15]
    return float(-(q * np.log(q)).sum())

def block_atom_data(C, v):
    m = C.shape[0]
    ans = []
    for mask in range(1 << m):
        absent = [i for i in range(m) if not ((mask >> i) & 1)]
        Q = C.copy()
        for i in absent:
            Q[i, i] -= 1
        q = (((-1) ** len(absent)) * np.linalg.det(Q)).real
        d = (v.conj() @ np.linalg.solve(Q, v)).real
        assert q > 0
        ans.append((mask, q, d))
    assert abs(sum(q for _, q, _ in ans) - 1.0) < 1e-12
    return ans

block_data = [block_atom_data(C, v) for C, v in zip(Cs, vs)]

def conditional_formula(a, c, z):
    s = np.abs(np.asarray(z)) ** 2
    total = sum(entropy_kernel(C) for C in Cs)
    for atom1 in block_data[0]:
        for atom2 in block_data[1]:
            weight = atom1[1] * atom2[1]
            cy = c - s[0] * atom1[2] - s[1] * atom2[2]
            total += weight * entropy_kernel(core(a, cy))
    return total

def entropy_strength(a, c, s):
    # Phase invariance allows positive square roots.
    return entropy_kernel(full_kernel(a, c, np.sqrt(np.asarray(s, dtype=float))))

def feasibility_margin(K):
    return min(np.linalg.eigvalsh(K).min(),
               np.linalg.eigvalsh(np.eye(K.shape[0]) - K).min())

# Exact physical-domain coefficients from Schur complements.
alphas = np.array([(v.conj() @ np.linalg.solve(C, v)).real
                   for C, v in zip(Cs, vs)])
betas = np.array([(v.conj() @ np.linalg.solve(np.eye(C.shape[0])-C, v)).real
                  for C, v in zip(Cs, vs)])

def domain_ok(a, c, z, tol=1e-12):
    s = np.abs(np.asarray(z))**2
    return (a >= -tol and a <= 1+tol
            and c - np.dot(alphas, s) >= -tol
            and 1-c - np.dot(betas, s) >= -tol)

# Check endpoint feasibility and direct-vs-conditional entropy identity.
max_conditional_residual = 0.0
min_margin = 1.0
for endpoint in [endpoint0, endpoint1]:
    a, c, z = endpoint
    K = full_kernel(a, c, z)
    assert domain_ok(a, c, z)
    min_margin = min(min_margin, feasibility_margin(K))
    res = abs(entropy_kernel(K) - conditional_formula(a, c, z))
    max_conditional_residual = max(max_conditional_residual, res)

# Check the conditional identity along the full chord.
for t in np.linspace(0.0, 1.0, 41):
    a = (1-t)*endpoint0[0] + t*endpoint1[0]
    c = (1-t)*endpoint0[1] + t*endpoint1[1]
    z = (1-t)*endpoint0[2] + t*endpoint1[2]
    K = full_kernel(a, c, z)
    assert domain_ok(a, c, z)
    min_margin = min(min_margin, feasibility_margin(K))
    res = abs(entropy_kernel(K) - conditional_formula(a, c, z))
    max_conditional_residual = max(max_conditional_residual, res)

H0 = entropy_kernel(full_kernel(*endpoint0))
H1 = entropy_kernel(full_kernel(*endpoint1))

# Jensen tests along the fixed endpoint chord.
min_jensen_gap = float("inf")
for t in np.linspace(0.0, 1.0, 101)[1:-1]:
    a = (1-t)*endpoint0[0] + t*endpoint1[0]
    c = (1-t)*endpoint0[1] + t*endpoint1[1]
    z = (1-t)*endpoint0[2] + t*endpoint1[2]
    Ht = entropy_kernel(full_kernel(a, c, z))
    gap = Ht - ((1-t)*H0 + t*H1)
    min_jensen_gap = min(min_jensen_gap, gap)
    assert gap > -2e-10

# Verify exact finite-gap decomposition at t=0.37.
t = 0.37
a0, c0, z0 = endpoint0
a1, c1, z1 = endpoint1
at = (1-t)*a0 + t*a1
ct = (1-t)*c0 + t*c1
zt = (1-t)*z0 + t*z1
s0 = np.abs(z0)**2
s1 = np.abs(z1)**2
st = np.abs(zt)**2
bar_s = (1-t)*s0 + t*s1
delta = bar_s - st
lam = np.divide(delta, bar_s, out=np.zeros_like(delta), where=bar_s > 0)

Ht = entropy_kernel(full_kernel(at, ct, zt))
HL = entropy_strength(at, ct, bar_s)
Gamma = Ht - ((1-t)*H0 + t*H1)
J_end = HL - ((1-t)*H0 + t*H1)

ERH = 0.0
E_information = 0.0
for bits in itertools.product([0, 1], repeat=2):
    probability = 1.0
    sR = bar_s.copy()
    for j, bit in enumerate(bits):
        probability *= lam[j] if bit else (1-lam[j])
        if bit:
            sR[j] = 0.0
    HR = entropy_strength(at, ct, sR)
    ERH += probability * HR
    E_information += probability * (HR - HL)

J_remove = Ht - ERH
gap_decomposition_residual = Gamma - (J_end + J_remove + E_information)
assert J_end >= -2e-10
assert J_remove >= -2e-10
assert E_information >= -2e-10
assert abs(gap_decomposition_residual) < 2e-10

# Explicit Pinsker lower bound from the report.
pinsker_bound = 0.0
for j, v in enumerate(vs):
    max_v4 = max(abs(entry)**4 for entry in v)
    pinsker_bound += ((8.0 / n**2) * t * (1-t)
                      * abs(z1[j]-z0[j])**2 * bar_s[j] * max_v4)
assert Gamma + 2e-10 >= pinsker_bound

# Random feasible endpoint pairs from this same family.
rng = np.random.default_rng(20260915)
random_pairs_checked = 0
random_min_gap = float("inf")
for _ in range(300):
    sA = rng.uniform(0.0, 0.35, size=2)
    sB = rng.uniform(0.0, 0.35, size=2)
    lowA = np.dot(alphas, sA) + 0.08
    highA = 1 - np.dot(betas, sA) - 0.08
    lowB = np.dot(alphas, sB) + 0.08
    highB = 1 - np.dot(betas, sB) - 0.08
    if lowA >= highA or lowB >= highB:
        continue
    aA, aB = rng.uniform(0.12, 0.88, 2)
    cA = rng.uniform(lowA, highA)
    cB = rng.uniform(lowB, highB)
    phaseA = rng.uniform(0, 2*np.pi, 2)
    phaseB = rng.uniform(0, 2*np.pi, 2)
    zA = np.sqrt(sA) * np.exp(1j*phaseA)
    zB = np.sqrt(sB) * np.exp(1j*phaseB)
    KA = full_kernel(aA, cA, zA)
    KB = full_kernel(aB, cB, zB)
    if feasibility_margin(KA) < -1e-9 or feasibility_margin(KB) < -1e-9:
        raise AssertionError("Schur-domain generator produced invalid endpoint")
    HA, HB = entropy_kernel(KA), entropy_kernel(KB)
    theta = rng.uniform(0.05, 0.95)
    am = (1-theta)*aA + theta*aB
    cm = (1-theta)*cA + theta*cB
    zm = (1-theta)*zA + theta*zB
    HM = entropy_kernel(full_kernel(am, cm, zm))
    gap = HM - ((1-theta)*HA + theta*HB)
    assert gap > -2e-9
    random_min_gap = min(random_min_gap, gap)
    random_pairs_checked += 1

print("PROB20-16 EXCHANGEABLE-CORE SATELLITE CHECK PASSED")
print("alphas =", alphas.tolist())
print("betas =", betas.tolist())
print("minimum spectral feasibility margin =", min_margin)
print("max conditional entropy identity residual =", max_conditional_residual)
print("minimum fixed-chord Jensen gap =", min_jensen_gap)
print("t=0.37 total Jensen gap =", Gamma)
print("  endpoint conditional gap J_end =", J_end)
print("  removal conditional gap J_remove =", J_remove)
print("  expected information term =", E_information)
print("  decomposition residual =", gap_decomposition_residual)
print("  explicit Pinsker lower bound =", pinsker_bound)
print("random feasible endpoint pairs checked =", random_pairs_checked)
print("minimum random Jensen gap =", random_min_gap)
