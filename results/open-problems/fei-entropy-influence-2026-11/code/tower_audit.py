"""Independent check of the tower values reported by worker FEIB26 (FLOW 12(y) item 4).

Composition f = F(psi, ..., psi), F on k variables, the same psi on m variables in every block, coordinate i in
block 1. With c = psihat(empty), t = 1 - c^2, a = psihat({i})^2 and
    K_A(c) = sum_{B >= A} Fhat(B) c^{|B - A|},
the spectrum of f is  mu_f(S) = K_A(c)^2 prod_{j in A} mu_psi(S_j)  (A = blocks met by S), and so
    E_i(f)   = sum_{A' <= {2..k}} t^{|A'|} [ Phi(K_{A'}^2, K_{A'+1}^2 a) + K_{A'+1}^2 (E_i(psi) - Phi(c^2, a)) ],
    Inf_i(f) = Inf_i(psi) sum_{A'} t^{|A'|} K_{A'+1}^2,
    fhat(empty) = K_empty(c),   fhat({i})^2 = K_{1}(c)^2 a.
This file (1) checks these four formulas against a direct transform on random small F and psi, and (2) iterates
them for the tower of the 9-variable function "the chosen edges of K_{3,3} contain a perfect matching".

Nothing here is taken from the worker's code. Usage: python tower_audit.py [depth]
"""
import sys
import itertools
import numpy as np
from rand_restrict_identity import wht


def phi(p, q):
    s = p + q
    out = 0.0
    for x in (p, q):
        if x > 0:
            out -= x * np.log2(x / s)
    return out


def erasure(mu, n, i):
    idx = np.arange(1 << n)
    lo = idx[(idx >> i) & 1 == 0]
    p, q = mu[lo], mu[lo | (1 << i)]
    s = p + q
    e = 0.0
    for x in (p, q):
        m = x > 0
        e -= float((x[m] * np.log2(x[m] / s[m])).sum())
    return e, float(q.sum())


def kcoef(Fh, k, c):
    """K_A(c) for every A, as an array indexed by the mask of A."""
    K = np.zeros(1 << k)
    for A in range(1 << k):
        rest = ((1 << k) - 1) & ~A
        B = rest
        while True:
            K[A] += Fh[A | B] * c ** bin(B).count("1")
            if B == 0:
                break
            B = (B - 1) & rest
    return K


def step(Fh, k, c, a, E, d):
    """One level: (c, a, E, d) of psi at coordinate i -> the same four numbers for F(psi, ..., psi)."""
    K = kcoef(Fh, k, c)
    t = 1.0 - c * c
    base = phi(c * c, a)
    En, infF = 0.0, 0.0
    for Ap in range(0, 1 << k, 2):          # subsets of blocks 2..k: bit 0 (block 1) clear
        w = t ** bin(Ap).count("1")
        k0, k1 = K[Ap] ** 2, K[Ap | 1] ** 2
        En += w * (phi(k0, k1 * a) + k1 * (E - base))
        infF += w * k1
    return K[0], K[1] ** 2 * a, En, infF * d


def compose(F, k, psi, m):
    n = k * m
    idx = np.arange(1 << n)
    inner = np.zeros(idx.size, dtype=np.int64)
    for j in range(k):
        blk = (idx >> (j * m)) & ((1 << m) - 1)
        bit = (psi[blk] < 0).astype(np.int64)
        inner |= bit << j
    return F[inner], n


def selfcheck(rng):
    worst = 0.0
    for trial in range(6):
        k, m = (3, 3) if trial < 3 else (4, 3)
        F = rng.choice([-1.0, 1.0], size=1 << k)
        psi = rng.choice([-1.0, 1.0], size=1 << m)
        ph = wht(psi)
        Fh = wht(F)
        E0, d0 = erasure(ph ** 2, m, 0)
        if d0 < 1e-12:
            continue
        c, a, E, d = step(Fh, k, ph[0], ph[1] ** 2, E0, d0)
        f, n = compose(F, k, psi, m)
        fh = wht(f)
        Eb, db = erasure(fh ** 2, n, 0)
        err = max(abs(E - Eb), abs(d - db), abs(c - fh[0]), abs(a - fh[1] ** 2))
        worst = max(worst, err)
        print("selfcheck k=%d m=%d  E %.12f / %.12f  Inf %.12f / %.12f  err %.2e" % (k, m, E, Eb, d, db, err))
    return worst


def pm_k33():
    """+1 if the edge set (bit 3u+v = edge u-v present) contains no perfect matching, -1 if it does."""
    perms = list(itertools.permutations(range(3)))
    f = np.ones(512)
    for x in range(512):
        for p in perms:
            if all((x >> (3 * u + p[u])) & 1 for u in range(3)):
                f[x] = -1.0
                break
    return f


def main():
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    rng = np.random.default_rng(7)
    print("worst selfcheck error %.2e" % selfcheck(rng))
    F = pm_k33()
    Fh = wht(F)
    mu = Fh ** 2
    es = [erasure(mu, 9, i) for i in range(9)]
    print("PM(K33): mean %.10f  Inf_i %s  E_i/Inf_i %s" % (
        Fh[0], sorted({round(e[1], 10) for e in es}), sorted({round(e[0] / e[1], 10) for e in es})))
    c, a, (E, d) = Fh[0], mu[1], es[0]
    print("depth 1  n=%-8d c=% .12f  Inf=%.6e  G=%.15f" % (9, c, d, E / d))
    for r in range(2, depth + 1):
        c, a, E, d = step(Fh, 9, c, a, E, d)
        print("depth %d  n=%-8d c=% .12f  Inf=%.6e  G=%.15f" % (r, 9 ** r, c, d, E / d))


if __name__ == "__main__":
    main()
