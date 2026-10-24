"""Conjecture 13 of the Randomstrasse 2024 list at k = 15, the Patterson-Wiedemann setting.

disc(H_k) = min over f of max |W_f|, f a Boolean function on k variables, so the conjecture
disc(H_k) = sqrt(2)*sqrt(2^k) for odd k says the maximum nonlinearity on k variables is exactly the
bent-concatenation value 2^(k-1) - 2^((k-1)/2).  At k = 15 that is 16256, i.e. max|W| = 256.

Patterson and Wiedemann (1983) beat it inside the class of functions on GF(2^15) invariant under
multiplication by GF(2^5)* (order 31) and under the Frobenius map x -> x^2 (order 15), a group of order
465 whose orbits on the 32767 nonzero elements number a few dozen.  This builds that class and searches
it: any function with max|W| <= 254 refutes the conjecture at k = 15.

Nonlinearity is invariant under a linear change of basis, so identifying GF(2^15) with F_2^15 through
the polynomial basis of x^15 + x + 1 (primitive) is harmless.
"""
import numpy as np, sys, time

K = 15; N = 1 << K; POLY = (1 << 15) | (1 << 1) | 1

def tables():
    log = np.zeros(N, dtype=np.int32); alog = np.zeros(N - 1, dtype=np.int32)
    x = 1
    for i in range(N - 1):
        alog[i] = x; log[x] = i
        x <<= 1
        if x & (1 << K): x ^= POLY
    return log, alog

LOG, ALOG = tables()

def orbits():
    """orbits of <multiplication by GF(2^5)*, Frobenius> on GF(2^15)* """
    step = (N - 1) // 31                      # GF(2^5)* = { g^(1057 k) }
    sub = [ALOG[(step * k) % (N - 1)] for k in range(31)]
    rep = -np.ones(N, dtype=np.int32); reps = []
    for u in range(1, N):
        if rep[u] >= 0: continue
        idx = len(reps); reps.append(u)
        frontier = {u}
        seen = set()
        while frontier:
            v = frontier.pop()
            if v in seen: continue
            seen.add(v); rep[v] = idx
            frontier.add(ALOG[(2 * LOG[v]) % (N - 1)])                      # Frobenius
            for c in sub: frontier.add(ALOG[(LOG[v] + LOG[c]) % (N - 1)])   # GF(2^5)* multiples
    rep[0] = len(reps); reps.append(0)          # the zero element is its own class
    return rep, reps

REP, REPS = orbits()
NORB = len(REPS)

def wht(x):
    a = x.astype(np.int64).copy(); h = 1
    while h < N:
        a = a.reshape(-1, 2, h)
        u, v = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = u + v; a[:, 1, :] = u - v
        a = a.reshape(-1); h <<= 1
    return a

def spectrum(signs):
    return wht(signs[REP])

if __name__ == '__main__':
    print(f"GF(2^15) under the group of order 465: {NORB} classes (including the zero element)")
    sizes = np.bincount(REP, minlength=NORB)
    print(f"class sizes: {sorted(set(sizes.tolist()))}, total {sizes.sum()}")
    rng = np.random.default_rng(0)
    s = 1 - 2 * rng.integers(0, 2, NORB)
    w = spectrum(s)
    print(f"sanity, a random member of the class: max|W| = {abs(w).max()} "
          f"(nonlinearity {N//2 - abs(w).max()//2}); the bound to beat is max|W| = 256, nonlinearity 16256")
