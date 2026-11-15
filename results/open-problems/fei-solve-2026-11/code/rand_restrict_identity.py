"""Check of the random-restriction identity (FLOW 12(v), item 3) and of two constants.

Identity: for every Boolean f on n variables

    H(f) = sum_{m=1..n} (1/m) E_{rho with m free variables} [ EE(f_rho) + JJ(f_rho) ]
         = integral_0^1 E_{rho ~ p-random} [ EE(f_rho) + JJ(f_rho) ] dp / p,

EE(g) = sum_i E_i(g) (edge entropy), JJ(g) = sum_i J_i(g), J_i = Jensen-Shannon divergence of the spectra of the two
restrictions of g at x_i. rho fixes a uniformly random set of n - m variables to uniformly random values.
Everything is computed from the definitions (E_i and J_i from spectra, no use of the tree identity).

Also prints: max over delta of delta * log2(1 + delta^-2) (the constant for the empty-set term), and for each f
the largest ratio  fhat(S)^2 / (4^(|S|-1) M(S)^2),  M(S) = sum of fhat(S')^2 over S' containing S  (must be <= 1).

Usage: python rand_restrict_identity.py [n] [number of random functions]
"""
import sys
import itertools
import numpy as np


def wht(v):
    a = np.array(v, dtype=np.float64)
    n = a.size.bit_length() - 1
    h = 1
    while h < a.size:
        a = a.reshape(-1, 2, h)
        a = np.concatenate((a[:, 0, :] + a[:, 1, :], a[:, 0, :] - a[:, 1, :]), axis=1).reshape(-1)
        h *= 2
    return a / (1 << n)


def ent(p):
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())


def edge_and_js(f, m):
    """sum_i E_i and sum_i J_i for f on m variables (truth table of +-1, bit j of the index is x_j)."""
    if m == 0:
        return 0.0, 0.0
    mu = wht(f) ** 2
    idx = np.arange(1 << m)
    ee = jj = 0.0
    for i in range(m):
        lo = idx[(idx >> i) & 1 == 0]
        p, q = mu[lo], mu[lo | (1 << i)]
        nu = p + q
        ee += ent(np.concatenate((p, q))) - ent(nu)          # H(U) - H(U - i) = H(1[i in U] | U - i)
        f0, f1 = f[lo], f[lo | (1 << i)]
        jj += ent(nu) - 0.5 * ent(wht(f0) ** 2) - 0.5 * ent(wht(f1) ** 2)
    return ee, jj


def restrict(f, n, free, vals):
    """f with the variables outside `free` set to `vals`; result indexed by the free variables in order."""
    fixed = [j for j in range(n) if j not in free]
    base = sum(v << j for j, v in zip(fixed, vals))
    out = np.empty(1 << len(free))
    for t in range(1 << len(free)):
        x = base
        for pos, j in enumerate(free):
            x |= ((t >> pos) & 1) << j
        out[t] = f[x]
    return out


def rhs(f, n):
    tot = 0.0
    for m in range(1, n + 1):
        acc, cnt = 0.0, 0
        for free in itertools.combinations(range(n), m):
            for vals in itertools.product((0, 1), repeat=n - m):
                ee, jj = edge_and_js(restrict(f, n, free, vals), m)
                acc += ee + jj
                cnt += 1
        tot += acc / cnt / m
    return tot


def gran(f, n):
    mu = wht(f) ** 2
    up = mu.copy()                       # upward zeta transform: M(S) = sum over supersets
    for j in range(n):
        for s in range(1 << n):
            if not (s >> j) & 1:
                up[s] += up[s | (1 << j)]
    worst = 0.0
    for s in range(1, 1 << n):
        if mu[s] > 0:
            worst = max(worst, mu[s] / (4.0 ** (bin(s).count("1") - 1) * up[s] ** 2))
    return worst


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    d = np.linspace(1e-4, 1.0, 200001)
    print(f"max delta*log2(1+delta^-2) = {(d * np.log2(1 + d ** -2)).max():.6f}")
    rng = np.random.default_rng(20261110)
    worst_gap = worst_gran = 0.0
    for r in range(reps):
        f = rng.choice([-1.0, 1.0], size=1 << n)
        h = ent(wht(f) ** 2)
        s = rhs(f, n)
        g = gran(f, n)
        worst_gap = max(worst_gap, abs(h - s))
        worst_gran = max(worst_gran, g)
        print(f"n={n} random {r}: H={h:.12f}  restriction sum={s:.12f}  diff={h - s:+.2e}  granularity ratio max={g:.4f}",
              flush=True)
    print(f"largest |H - sum| = {worst_gap:.2e}; largest granularity ratio = {worst_gran:.4f} (bound 1)")


if __name__ == "__main__":
    main()
