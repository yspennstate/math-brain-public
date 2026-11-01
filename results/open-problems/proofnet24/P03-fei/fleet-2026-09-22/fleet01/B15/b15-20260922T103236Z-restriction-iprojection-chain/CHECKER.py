#!/usr/bin/env python3
"""Deterministic checker for the four-bit restriction witness in REPORT.md.

The theorem in REPORT.md is analytic. This script checks only the explicit
Boolean witness and the numerical decomposition quoted in Section 6.
No external packages are required.
"""

from math import log, log2

TOL = 5e-12


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    return a


def KL(p, q):
    out = 0.0
    for x, y in zip(p, q):
        if x > 0.0:
            assert y > 0.0
            out += x * log2(x / y)
    return out


def occurrence(w, d):
    return [sum(w[S] for S in range(1 << d) if (S >> i) & 1)
            for i in range(d)]


def conditional_product_iproj(r):
    """Q_r on nonempty subsets and its conditioning mass c."""
    d = len(r)
    mu = sum(r)
    assert mu >= 1.0 - 1e-13
    if abs(mu - 1.0) < 1e-13:
        q = [0.0] * (1 << d)
        for i, ri in enumerate(r):
            q[1 << i] = ri
        return q, 1.0

    def f(c):
        prod = 1.0
        for ri in r:
            prod *= 1.0 - c * ri
        return 1.0 - c - prod

    lo, hi = 1e-14, 1.0
    assert f(lo) > 0.0
    assert f(hi) <= 0.0
    for _ in range(240):
        mid = (lo + hi) / 2.0
        if f(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    c = (lo + hi) / 2.0
    t = [c * ri for ri in r]
    q = [0.0] * (1 << d)
    for S in range(1, 1 << d):
        z = 1.0
        for i, ti in enumerate(t):
            z *= ti if ((S >> i) & 1) else (1.0 - ti)
        q[S] = z / c
    assert abs(sum(q) - 1.0) < 2e-12
    return q, c


def full_iproj(w):
    d = (len(w) - 1).bit_length()
    assert 1 << d == len(w)
    v = 1.0 - w[0]
    rho = occurrence(w, d)
    if v < 1e-15:
        R = [0.0] * len(w)
        R[0] = 1.0
        return R, v, [0.0] * d, 1.0
    r = [x / v for x in rho]
    q, c = conditional_product_iproj(r)
    R = [0.0] * len(w)
    R[0] = 1.0 - v
    for S in range(1, len(w)):
        R[S] = v * q[S]
    assert abs(sum(R) - 1.0) < 2e-12
    return R, v, r, c


def squared_spectrum(truth):
    raw = fwht(truth)
    N = len(truth)
    return raw, [(x / N) ** 2 for x in raw]


def erase_parent(w, j, d):
    out = [0.0] * (1 << (d - 1))
    for S, mass in enumerate(w):
        lower = S & ((1 << j) - 1)
        upper = S >> (j + 1)
        T = lower | (upper << j)
        out[T] += mass
    return out


def reference_pair_credit(w, R, j, d):
    E = erase_parent(w, j, d)
    Rm = erase_parent(R, j, d)
    credit = 0.0
    for T in range(1 << (d - 1)):
        # lift erased T into the parent coordinates, once without j and once with j
        lower = T & ((1 << j) - 1)
        upper = T >> j
        S0 = lower | (upper << (j + 1))
        S1 = S0 | (1 << j)
        if E[T] > 0.0:
            q = w[S1] / E[T]
            theta = R[S1] / Rm[T]
            if q > 0.0:
                credit += E[T] * q * log2(q / theta)
            if q < 1.0:
                credit += E[T] * (1.0 - q) * log2((1.0 - q) / (1.0 - theta))
    return credit


# Little-endian truth-table order, values in {+1,-1}.
truth = [1, 1, 1, -1, 1, 1, 1, -1,
         1, -1, -1, -1, -1, 1, 1, 1]
raw, W = squared_spectrum(truth)
assert raw == [4, 4, 4, -4, -4, 4, 4, 4,
               4, 4, 4, -4, 4, -4, -4, -4]
assert all(abs(x - 1.0 / 16.0) < TOL for x in W)

# Restrict bit j=0.  The remaining bit order is inherited little-endian.
truth0 = [truth[x] for x in range(16) if (x & 1) == 0]
truth1 = [truth[x] for x in range(16) if (x & 1) == 1]
raw0, U = squared_spectrum(truth0)
raw1, V = squared_spectrum(truth1)
assert raw0 == [4, 0, 0, 4, 4, 0, 0, -4]
assert raw1 == [0, 4, -4, 0, 0, 4, 4, 0]

RW, vp, rp, cp = full_iproj(W)
RU, v0, r0, c0 = full_iproj(U)
RV, v1, r1, c1 = full_iproj(V)
assert KL(W, RW) < TOL

s = 0.5
E = [(1.0 - s) * u + s * v for u, v in zip(U, V)]
RE, vbar, rbar, cbar = full_iproj(E)
assert all(abs(x - 1.0 / 8.0) < TOL for x in E)
assert KL(E, RE) < TOL

# Parent-reference erasure equals the erased source because the parent is uniform.
Rminus = erase_parent(RW, 0, 4)
C_erase = KL(RE, Rminus)
C_pair = reference_pair_credit(W, RW, 0, 4)

K_parent = KL(W, RW)
K0_weighted = KL(U, RU)
K1_weighted = KL(V, RV)
child_avg = 0.5 * (K0_weighted + K1_weighted)
JS = 0.5 * KL(U, E) + 0.5 * KL(V, E)
C_marg = 0.5 * KL(RU, RE) + 0.5 * KL(RV, RE)
rhs = child_avg + C_marg + C_erase + C_pair - JS

assert K0_weighted > 0.8
assert K1_weighted > 0.7
assert abs(JS - 1.0) < TOL
assert abs(C_marg - 0.21688984173957326) < 2e-12
assert C_erase < TOL
assert C_pair < TOL
assert abs(K_parent - rhs) < 2e-11

# Convert weighted KL to child conditional K_occ for the printed diagnostics.
K0_occ = K0_weighted / v0
K1_occ = K1_weighted / v1

# Physical influence of bit 0 is the parent spectral occurrence probability.
It_j = sum(W[S] for S in range(16) if S & 1)
kappa_half = 2.0 / log(2.0)

print("PASS")
print("parent_raw_walsh=", raw)
print("child0_raw_walsh=", raw0)
print("child1_raw_walsh=", raw1)
print(f"parent_weighted_K={K_parent:.15f}")
print(f"child_average_weighted_K={child_avg:.15f}")
print(f"JS={JS:.15f}")
print(f"C_marg={C_marg:.15f}")
print(f"C_erase={C_erase:.15f}")
print(f"C_pair={C_pair:.15f}")
print(f"chain_rhs={rhs:.15f}")
print(f"It_j={It_j:.15f}")
print(f"kappa_half_It_j={kappa_half * It_j:.15f}")
print(f"child0_v={v0:.15f}, child0_Kocc={K0_occ:.15f}")
print(f"child1_v={v1:.15f}, child1_Kocc={K1_occ:.15f}")
