#!/usr/bin/env python3
"""Finite sanity checks for B15 balanced stop/KL fusion.

This is not used to prove the universal FKN/isoperimetric lemmas.  It checks the
exact harmonic identities numerically on every balanced Boolean function through
n=4 and checks the closed formulas for the balanced one-point suspension family.
"""
import itertools
import math


def entropy(ps):
    return -sum(p * math.log2(p) for p in ps if p > 0.0)


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def kl(p, q):
    ans = 0.0
    for x, y in zip(p, q):
        if x > 0.0:
            ans += x * math.log2(x / y)
    return ans


def walsh(vals):
    a = [float(x) for x in vals]
    n = len(a)
    step = 1
    while step < n:
        for base in range(0, n, 2 * step):
            for j in range(base, base + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return [x / n for x in a]


def balanced_stats(vals):
    N = len(vals)
    n = N.bit_length() - 1
    coeff = walsh(vals)
    p = [x * x for x in coeff]
    assert p[0] < 1e-24
    H = entropy(p)
    inf = [sum(p[s] for s in range(N) if (s >> i) & 1) for i in range(n)]
    I = sum(inf)
    beta = I - 1.0
    q = [x / I for x in inf]

    # Uniform-prefix shadows v_A.
    v = {}
    for A in range(1, N):
        a = A.bit_count()
        total = 0.0
        for S in range(N):
            if S & A == A:
                total += p[S] / math.comb(S.bit_count(), a)
        v[A] = total

    alpha = [v[1 << i] for i in range(n)]
    T_stop = 0.0
    for A, va in v.items():
        if va > 1e-30:
            x = p[A] / va
            T_stop += va * h2(x)

    W = [0.0] * (n + 1)
    factorial_credit = 0.0
    for S, ps in enumerate(p):
        k = S.bit_count()
        W[k] += ps
        if ps > 0.0:
            factorial_credit += ps * math.lgamma(k + 1) / math.log(2.0)
    H_K = entropy(W)

    if beta < 1e-12:
        return H, I, beta, T_stop, H_K, 0.0, 0.0, 0.0, 0.0

    beta_i = [inf[i] - alpha[i] for i in range(n)]
    rho = [x / beta for x in beta_i]

    K_rho = 0.0
    deletion_entropy = 0.0
    for A, va in v.items():
        a = A.bit_count()
        ta = va - p[A]
        if ta <= 1e-13:
            continue
        pairs = []
        for i in range(n):
            if not ((A >> i) & 1):
                pi = v.get(A | (1 << i), 0.0) / ((a + 1) * ta)
                if pi > 1e-13:
                    pairs.append((i, pi))
        assert abs(sum(pi for _, pi in pairs) - 1.0) < 2e-10
        deletion_entropy += ta * entropy([pi for _, pi in pairs])
        K_rho += ta * sum(pi * math.log2(pi / rho[i]) for i, pi in pairs)

    D_del = deletion_entropy - factorial_credit
    mix_KL = kl(alpha, q) + beta * kl(rho, q)
    fused = I * entropy(q) + T_stop - factorial_credit - K_rho - mix_KL
    root_del = entropy(alpha) + T_stop + D_del
    resid = max(abs(H - fused), abs(H - root_del))
    J = sum(min(x, 1.0 - x) for x in inf)
    return H, I, beta, T_stop, H_K, resid, J, mix_KL, D_del


def suspension_formula(m):
    eps = 2.0 ** (1 - m)
    beta = m * eps
    I = 1.0 + beta
    u = eps * (2 * m - 2 + eps) / (m + 1)
    mix = (
        math.log2(I)
        + beta * (m - 1 - math.log2(m))
        - h2(u)
        - beta * h2(u / beta)
    )
    p0 = (1.0 - eps) ** 2
    H = -p0 * math.log2(p0) + (2**m - 1) * eps * eps * (2 * (m - 1))
    return beta, u, mix, H


def main():
    total = 0
    max_resid = 0.0
    max_stop_over_level = 0.0
    max_level_over_beta = 0.0
    max_J_over_beta = 0.0

    for n in range(1, 5):
        N = 1 << n
        for plus in itertools.combinations(range(N), N // 2):
            vals = [-1] * N
            for x in plus:
                vals[x] = 1
            H, I, beta, T, HK, resid, J, mix, Ddel = balanced_stats(vals)
            total += 1
            max_resid = max(max_resid, resid)
            if HK > 1e-13:
                max_stop_over_level = max(max_stop_over_level, T / HK)
            if beta > 1e-13:
                max_level_over_beta = max(max_level_over_beta, HK / beta)
                max_J_over_beta = max(max_J_over_beta, J / beta)

    print("balanced_functions_checked", total)
    print("max_fusion_residual_bits", repr(max_resid))
    print("max_Tstop_over_HK", repr(max_stop_over_level))
    print("max_HK_over_beta", repr(max_level_over_beta))
    print("max_J_over_beta", repr(max_J_over_beta))

    print("suspension_family")
    for m in (4, 8, 16, 32):
        beta, u, mix, H = suspension_formula(m)
        print(m, "mix_over_beta", repr(mix / beta), "H_over_beta", repr(H / beta),
              "u_over_beta", repr(u / beta))

    assert total == 12948
    assert max_resid < 3e-12
    assert max_stop_over_level <= 1.0 + 1e-12
    assert suspension_formula(32)[2] / suspension_formula(32)[0] > 25.0
    print("PASS")


if __name__ == "__main__":
    main()
