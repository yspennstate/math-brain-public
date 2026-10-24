"""Independent slow re-implementation (pure Python, exact Fractions for p and pi, mpmath logs at 50 digits)
of H, I, U and Delta_i U, to audit the numpy code (feilib/upward)."""
import json, itertools
from fractions import Fraction
import mpmath as mp
mp.mp.dps = 50

def walsh_exact(table):
    n = len(table).bit_length() - 1; N = len(table); out = []
    for S in range(N):
        s = 0
        for x in range(N):
            s += table[x] * (-1 if bin(S & x).count('1') % 2 else 1)
        out.append(Fraction(s, N))
    return n, out

def spectral(table):
    n, a = walsh_exact(table); p = [c * c for c in a]
    N = len(p)
    pi = [sum(p[T] for T in range(N) if (T & S) == S) for S in range(N)]
    return n, p, pi

def HIU(table):
    n, p, pi = spectral(table)
    H = sum((-pp * mp.log(pp, 2) for pp in p if pp > 0), mp.mpf(0))
    I = sum(bin(S).count('1') * p[S] for S in range(len(p)))
    U = sum((pp * mp.log(pi[S] / pp, 2) for S, pp in enumerate(p) if pp > 0), mp.mpf(0))
    return n, H, I, U

def restrict(table, n, i, b):
    return [table[x] for x in range(len(table)) if ((x >> i) & 1) == b]

def deltaU(table, i):
    n, H, I, U = HIU(table)
    _, _, _, U0 = HIU(restrict(table, n, i, 0)); _, _, _, U1 = HIU(restrict(table, n, i, 1))
    return U - (U0 + U1) / 2

if __name__ == "__main__":
    import numpy as np
    from feilib import spectrum, influences
    from upward import Uprime
    g5 = json.load(open("../data/anneal_G.json"))["5"]["table"]
    n, H, I, U = HIU(g5)
    print('g5 slow: H=', mp.nstr(H, 12), 'I=', I, 'U=', mp.nstr(U, 12))
    p = spectrum(np.array(g5)); print('g5 fast: U=', float(Uprime(p, 5)))
    G = sum(deltaU(g5, i) for i in range(5)); print('g5 slow G/I =', mp.nstr(G / I, 12))
    # X003 k=4 r=4 selector coordinate
    from x003_scan import x003_table
    t, nn = x003_table(4, 4); t = [int(v) for v in t]
    d = deltaU(t, 0); n2, p2, pi2 = spectral(t); Inf0 = sum(p2[S] for S in range(len(p2)) if S & 1)
    print('x003 k4r4 slow Delta_y U / Inf_y =', mp.nstr(d / Inf0, 12), ' Inf_y =', Inf0)
