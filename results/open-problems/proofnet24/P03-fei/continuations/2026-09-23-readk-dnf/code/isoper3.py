# Fast exact biased Fourier transform (mpmath, per-coordinate butterfly) and the two isoperimetric ratios.
import mpmath as mp, math, random, sys, itertools
mp.mp.dps = 50

def biased_P(fvals, q):
    n = len(q); N = 1 << n
    c = [mp.mpf(1 - 2 * v) for v in fvals]
    for i in range(n):
        qi = mp.mpf(q[i]); s = mp.sqrt(qi * (1 - qi)); bit = 1 << i
        for x in range(N):
            if not x & bit:
                a, b = c[x], c[x | bit]
                c[x] = (1 - qi) * a + qi * b
                c[x | bit] = s * (b - a)
    return [v * v for v in c]          # P(A), A as bitmask

def ratios(fvals, q, cc=1):
    n = len(q); P = biased_P(fvals, q)
    sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    Var = mp.fsum(P[1:]); W = mp.fsum(P[A] for A in range(1, 1 << n) if bin(A).count('1') >= 2)
    I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << n))
    J = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << n) if bin(A).count('1') >= 2)
    Inf = [mp.fsum(P[A] for A in range(1 << n) if A >> i & 1) for i in range(n)]
    Ji = [Inf[i] - P[1 << i] for i in range(n)]
    out = {}
    cred1 = mp.fsum(Inf[i] * max(0, mp.log(cc * Inf[i] / sig2[i] / Var)) for i in range(n) if Inf[i] > 0)
    out['r1'] = float((Var * mp.log(1 / Var) - cred1) / I)
    if W > 0:
        cred2 = mp.fsum(Ji[i] * max(0, mp.log(cc * Ji[i] / sig2[i] / W)) for i in range(n) if Ji[i] > 0)
        out['r2'] = float((W * mp.log(1 / W) - cred2) / J)
    lhs = mp.fsum(P[A] * mp.log(mp.fprod(sig2[i] for i in range(n) if A >> i & 1) / P[A]) for A in range(1, 1 << n) if P[A] > 0)
    out['feiplus'] = float(lhs / J) if J > 0 else None
    return out

if __name__ == '__main__':
    print('tribes (OR of N pairs), q = 1/N:')
    for N in [2, 3, 4, 5, 6]:
        n = 2 * N
        f = [1 if any((x >> (2 * j)) & 1 and (x >> (2 * j + 1)) & 1 for j in range(N)) else 0 for x in range(1 << n)]
        print(N, ratios(f, [1.0 / N] * n), flush=True)
    print('tribes (OR of N pairs), q = 1/N^2:')
    for N in [2, 3, 4, 5, 6]:
        n = 2 * N
        f = [1 if any((x >> (2 * j)) & 1 and (x >> (2 * j + 1)) & 1 for j in range(N)) else 0 for x in range(1 << n)]
        print(N, ratios(f, [1.0 / N ** 2] * n), flush=True)
