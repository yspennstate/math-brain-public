#!/usr/bin/env python3
"""B13 FEI random-chain/profile stress calculations.

Exploratory finite calculations only. Analytic statements are proved in REPORT.md.
Uses exact integers for majority Fourier level masses; final logs are floating.
"""
from math import comb, log2, lgamma, log


def majority_weights(n):
    assert n % 2 == 1
    m = (n - 1) // 2
    den = 2 ** (n - 1)
    cnum = comb(n - 1, m)
    vals = []
    for k in range(1, n + 1, 2):
        # coefficient = C(n-1,m)/2^(n-1) * C(m,(k-1)/2)/C(n-1,k-1)
        num = cnum * comb(m, (k - 1) // 2)
        den_k = den * comb(n - 1, k - 1)
        vals.append((k, comb(n, k) * num * num, den_k * den_k))
    wf = [(k, num / denom) for k, num, denom in vals]
    z = sum(w for _, w in wf)
    return [(k, w / z) for k, w in wf]


def majority_chain(n):
    wf = majority_weights(n)
    I = sum(k * w for k, w in wf)
    HK = -sum(w * log2(w) for _, w in wf if w)
    C1 = sum(
        w * (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) / log(2)
        for k, w in wf
    )
    H = HK + C1

    # For a level-symmetric law, v_A=tau_a/C(n,a).
    W = [0.0] * (n + 1)
    for k, w in wf:
        W[k] = w
    tau = [0.0] * (n + 2)
    for a in range(n, -1, -1):
        tau[a] = tau[a + 1] + W[a]
    Bsh = sum(W[a] * log2(tau[a] / W[a]) for a in range(n + 1) if W[a])
    C0 = sum(
        tau[a + 1] * log2(tau[a] / tau[a + 1])
        for a in range(n + 1)
        if tau[a + 1] and tau[a]
    )
    return I, H, Bsh, C0, C1


print("majority: n I H/I Bsh/I C0/I C1/I")
for n in (13, 151, 251):
    I, H, B, C0, C1 = majority_chain(n)
    print(n, *(f"{x:.12f}" for x in (I, H / I, B / I, C0 / I, C1 / I)))

print("\nproduct q=1/n: H/I and max normalized unordered U-pair weight")
for n in (3, 10, 100):
    q = 1 / n
    vals = []
    for k in range(1, min(n, 5) + 1):
        mx = (2 ** (-(k - 1))) * ((1 - q) ** (n - k))
        vals.append((k, mx))
    ratio = n * (-q * log2(q) - (1 - q) * log2(1 - q))
    print(n, "H/I=", ratio, "pairmax", vals)

print("\none-point defect: root continuation / I")
for n in (4, 8, 16, 32, 64):
    theta = 2 ** (-n)
    V = 4 * theta * (1 - theta)
    I = 2 * n * theta
    root = V * log2(1 / V)
    print(n, f"{root / I:.12f}")
