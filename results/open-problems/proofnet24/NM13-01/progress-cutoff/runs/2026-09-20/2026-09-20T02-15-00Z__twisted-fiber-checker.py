import itertools
import math
import numpy as np
from scipy.linalg import expm

# Sanity instance for the theorem in the accompanying T08 report.
# Base: Cay(Z/7Z,{+-1,+-2}).
# Fixed fiber: Cay(S_3,{(12),(23)}).
# Cross moves carry noncommuting S_3 twists; vertical and cross kernels
# therefore do not admit the commuting semigroup factorization used for
# lexicographic blow-ups.

perms = list(itertools.permutations(range(3)))
pi_idx = {p: i for i, p in enumerate(perms)}


def comp(p, q):
    # p*q = first q, then p
    return tuple(p[q[i]] for i in range(3))


def inv(p):
    out = [0] * 3
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


e = (0, 1, 2)
t12 = (1, 0, 2)
t23 = (0, 2, 1)
cyc = (1, 2, 0)
cyc_inv = inv(cyc)
T = [t12, t23]

nG = 7
S = [1, -1, 2, -2]
phi = {1: cyc, -1: cyc_inv, 2: t12, -2: t12}

d = len(S)
s = len(T)
K = len(perms)
D = d + s
a = d / D
b = s / D

P = np.zeros((nG, nG))
for g in range(nG):
    for x in S:
        P[g, (g + x) % nG] += 1 / d

W = np.zeros((K, K))
for k, p in enumerate(perms):
    for t in T:
        W[k, pi_idx[comp(p, t)]] += 1 / s

N = nG * K


def idx(g, k):
    return g * K + k


Q = np.zeros((N, N))
Qc = np.zeros_like(Q)
Qv = np.zeros_like(Q)
for g in range(nG):
    for k, p in enumerate(perms):
        for x in S:
            j = idx((g + x) % nG, pi_idx[comp(p, phi[x])])
            Q[idx(g, k), j] += 1 / D
            Qc[idx(g, k), j] += 1 / d
        for t in T:
            j = idx(g, pi_idx[comp(p, t)])
            Q[idx(g, k), j] += 1 / D
            Qv[idx(g, k), j] += 1 / s

# Projection to the base coordinate.  The claimed generator identity is
# Q C = C(aP+bI), hence (Q-I)C = a C(P-I).
C = np.zeros((N, nG))
for g in range(nG):
    C[g * K:(g + 1) * K, g] = 1
projection_error = np.max(np.abs(Q @ C - C @ (a * P + b * np.eye(nG))))

# The cross and vertical kernels are genuinely noncommuting in this example.
commutator = np.max(np.abs(Qc @ Qv - Qv @ Qc))


def gap(M):
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    ev = np.sort(ev)[::-1]
    return 1 - ev[1]


gap_base = gap(P)
gap_fiber = gap(W)
gap_output = gap(Q)
gap_lower = min(a * gap_base, b * gap_fiber)

uniformG = np.ones(nG) / nG
uniformH = np.ones(N) / N
startG = np.zeros(nG)
startG[0] = 1
startH = np.zeros(N)
startH[idx(0, pi_idx[e])] = 1
C_K = 0.5 * math.sqrt(K - 1)

print("twisted_fiber_checker")
print(f"d={d} s={s} D={D} a={a:.12f} b={b:.12f} |K|={K}")
print(f"projection_error={float(projection_error):.16g}")
print(f"cross_vertical_commutator_max={float(commutator):.16g}")
print(f"gap_base={float(gap_base):.15f}")
print(f"gap_fiber={float(gap_fiber):.15f}")
print(f"gap_output={float(gap_output):.15f}")
print(f"gap_lower_bound={float(gap_lower):.15f}")
print(f"gap_bound_pass={bool(gap_output + 1e-12 >= gap_lower)}")

all_ok = projection_error < 1e-12 and commutator > 1e-6 and gap_output + 1e-12 >= gap_lower
for t in [0.5, 1, 2, 4, 8, 16]:
    HG = expm(a * t * (P - np.eye(nG)))
    HH = expm(t * (Q - np.eye(N)))
    lawG = startG @ HG
    lawH = startH @ HH
    dG = 0.5 * np.abs(lawG - uniformG).sum()
    dH = 0.5 * np.abs(lawH - uniformH).sum()
    upper = dG + C_K * math.exp(-b * gap_fiber * t)
    lower_pass = bool(dH + 1e-12 >= dG)
    upper_pass = bool(dH <= upper + 1e-12)
    all_ok = all_ok and lower_pass and upper_pass
    print(
        f"t={t:g} base_at={float(dG):.15f} output={float(dH):.15f} "
        f"upper={float(upper):.15f} lower_pass={lower_pass} upper_pass={upper_pass}"
    )

branching_ratio = (d - 1) / (D - 1)
beta = 0.5 * (1 - math.log(d - 1) / math.log(D - 1))
print(f"branching_ratio={branching_ratio:.12f}")
print(f"lre_polynomial_exponent_beta={beta:.12f}")

assert all_ok
print("ALL_CHECKS_PASS")
