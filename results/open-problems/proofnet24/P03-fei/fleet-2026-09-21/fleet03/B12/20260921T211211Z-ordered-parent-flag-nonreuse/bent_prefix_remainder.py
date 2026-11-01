#!/usr/bin/env python3
"""Check the prefix-total-correlation obstruction and stop-conditioned repair.

For even n, q_n(x)=(-1)^{x1 x2 + x3 x4 + ...} is bent, so its squared
Fourier coefficients are exactly uniform on 2^[n]. This script computes the
uniform-prefix edge-law quantities used in the FEI sequential code.

No external packages are required.
"""
from math import comb, log2, lgamma, log

LN2 = log(2.0)

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*log2(p) - (1.0-p)*log2(1.0-p)

def bent_prefix(n):
    assert n >= 2 and n % 2 == 0
    pk = [comb(n,k) / (2.0**n) for k in range(n+1)]
    I = n / 2.0
    # Under the size-biased terminal-set / uniform insertion-edge law:
    # P(T=t)=Pr(K>t)/I, 0<=t<=n-1.
    pt = [sum(pk[k] for k in range(t+1,n+1)) / I for t in range(n)]
    assert abs(sum(pt)-1.0) < 1e-12
    ET = sum(t*pt[t] for t in range(n))
    beta = ET/n
    HT = -sum(p*log2(p) for p in pt if p > 0.0)
    ElogC = sum(pt[t]*log2(comb(n,t)) for t in range(n))
    HP = HT + ElogC
    TC = n*h2(beta) - HP

    # Conditional total correlation E_T TC(P|T=t).
    TC_T = sum(
        pt[t]*(n*h2(t/n) - log2(comb(n,t)))
        for t in range(n)
    )

    ElogFact = sum(pk[k] * (lgamma(k+1)/LN2) for k in range(n+1))
    R_uncond = I*TC - ElogFact
    R_cond = I*TC_T - ElogFact
    return {
        "n": n,
        "I": I,
        "beta": beta,
        "TC": TC,
        "TC_given_T": TC_T,
        "E_log2_K_factorial": ElogFact,
        "R_uncond_over_I": R_uncond/I,
        "R_cond_over_I": R_cond/I,
    }

if __name__ == "__main__":
    for n in (20, 58, 100, 200, 500, 1000):
        r=bent_prefix(n)
        print(
            f"n={n:4d} beta={r['beta']:.12f} "
            f"TC={r['TC']:.12f} TC|T={r['TC_given_T']:.12f} "
            f"R/I={r['R_uncond_over_I']:.12f} "
            f"R_T/I={r['R_cond_over_I']:.12f}"
        )
    c0 = h2(0.25) - 1.0/(2.0*LN2)
    print(f"asymptotic_TC_per_n={c0:.15f}")
    print(f"asymptotic_R_uncond_per_n2={0.5*c0:.15f}")
