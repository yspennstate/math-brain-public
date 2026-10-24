"""Brute-force cross-checks of ltf_ref.py on small n (definitions, not FWHT)."""
import itertools, math, random, sys
import numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import ltf_ref as L

L.be_polite()
random.seed(1)
fails = 0


def xs_of(n):
    # index convention: bit j = 1 <-> x_j = -1
    return [[1 - 2 * ((b >> j) & 1) for j in range(n)] for b in range(1 << n)]


for trial in range(60):
    n = random.randint(2, 7)
    w = [random.randint(-4, 4) for _ in range(n)]
    theta = random.randint(-6, 6)
    tab = L.ltf_table(w, theta)
    xs = xs_of(n)
    # truth table by definition
    for b, x in enumerate(xs):
        t = sum(wi * xi for wi, xi in zip(w, x)) - theta
        v = 1 if t > 0 else -1
        if tab[b] != v:
            fails += 1
    # Fourier by definition
    sp = L.Spec(tab)
    for S in range(1 << n):
        fh = sum(tab[b] * (-1) ** bin(b & S).count("1") for b in range(1 << n)) / 2 ** n
        if abs(fh ** 2 - sp.p[S]) > 1e-12:
            fails += 1
    # influences by definition
    inf = sp.influences()
    for i in range(n):
        d = sum(1 for b in range(1 << n) if tab[b] != tab[b ^ (1 << i)]) / 2 ** n
        if abs(d - inf[i]) > 1e-12:
            fails += 1
    # pointwise Pr[g(y) != 0 | x] by exact enumeration of flips on U_i
    absw = [abs(t) for t in w]
    r, U, N = L.ranks_and_U(absw)
    for i in range(n):
        if inf[i] == 0 or N[i] < 2:
            continue
        c = random.uniform(0.3, N[i])
        q = c / (2 * N[i])  # flip probability
        Ubits = [j for j in range(n) if (U[i] >> j) & 1]
        res = L.lemma2_pointwise(tab, absw, i, U[i], N[i], [c])
        maxP_fwht = res[0][1]
        maxP = 0.0
        for b in range(1 << n):
            P = 0.0
            for flips in itertools.product([0, 1], repeat=len(Ubits)):
                pr = 1.0
                bb = b
                for j, fl in zip(Ubits, flips):
                    pr *= q if fl else (1 - q)
                    if fl:
                        bb ^= (1 << j)
                if tab[bb | 0] != tab[bb ^ (1 << i)]:
                    P += pr
            maxP = max(maxP, P)
        if abs(maxP - maxP_fwht) > 1e-9:
            fails += 1
            print("pointwise mismatch", n, w, theta, i, maxP, maxP_fwht)

print("selftest failures:", fails)
