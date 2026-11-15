"""Check of the composition formula for the erasure entropy (FLOW section 12(g)).

f(x_B, z) = F(g(x_B), z) = F_0(z) + g(x_B) F_1(z),  F_0 = (F(+1, .) + F(-1, .))/2,  F_1 = (F(+1, .) - F(-1, .))/2.
For i in B:
    Inf_i(f) = Inf_i(g) ||F_1||^2,
    E_i(f)   = ||F_1||^2 [ E_i(g) - Phi(ghat(0)^2, ghat(i)^2) ]
               + sum_{T2} Phi( (F_0hat + ghat(0) F_1hat)(T2)^2 , ghat(i)^2 F_1hat(T2)^2 ).
Random Boolean g on r variables and F on 1 + m variables; prints the largest difference between the two sides.

usage: python comp_check.py trials seed
"""
import sys
import numpy as np
from local_cs import wht, phi


def erasure(mu, n, i):
    idx = np.arange(1 << n)
    lo = idx[(idx >> i) & 1 == 0]
    return float(phi(mu[lo], mu[lo | (1 << i)]).sum()), float(mu[lo | (1 << i)].sum())


def main():
    trials, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    worst = 0.0
    for t in range(trials):
        r = int(rng.integers(2, 5))
        m = int(rng.integers(1, 5))
        dens = rng.choice([0.5, 0.25, 0.1])
        g = np.where(rng.random(1 << r) < dens, -1.0, 1.0)
        Fp = np.where(rng.random(1 << m) < 0.5, -1.0, 1.0)      # F(+1, z)
        Fm = np.where(rng.random(1 << m) < 0.5, -1.0, 1.0)      # F(-1, z)
        F0, F1 = (Fp + Fm) / 2, (Fp - Fm) / 2
        if not F1.any():
            continue
        # f on r + m variables: the low r bits are x_B, the high m bits are z
        f = (F0[:, None] + F1[:, None] * g[None, :]).reshape(-1)
        n = r + m
        mu = wht(f, n) ** 2
        gh = wht(g, r)
        F0h, F1h = wht(F0, m), wht(F1, m)
        n1 = float((F1h ** 2).sum())
        for i in range(r):
            E, inf = erasure(mu, n, i)
            Eg, infg = erasure(gh ** 2, r, i)
            c, b = gh[0], gh[1 << i]
            rhs = n1 * (Eg - float(phi(c * c, b * b))) + float(phi((F0h + c * F1h) ** 2, b * b * F1h ** 2).sum())
            worst = max(worst, abs(E - rhs), abs(inf - infg * n1))
    print("trials %d  largest difference between the two sides %.3e" % (trials, worst))


if __name__ == "__main__":
    main()
