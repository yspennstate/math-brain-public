"""Aggregate Ehrhart counts of the Toeplitz moment polytopes.

L_k(N) = sum over all pairings pi of 2k slots of #(N * P_pi  cap  Z^{k+1}).
A lattice point of N*P_pi is (x0, t_1..t_k) with x0 in [0,N], t_j in [-N,N] and every
slot form W_l = x0 + (signed partial sum) in [0,N].  Summing over pi, scan the slots
left to right: a slot either opens a chord with any value t (step +t) or closes one of
the open chords (step -t of that chord).  The state is (current height, multiset of
open chord values); the number of ways to close a chord of value t is its multiplicity.

Then h*(z) of each P_pi is palindromic of degree k (Gorenstein of index two, dimension
k+1), so the aggregate h* is too, and h*_0..h*_{floor(k/2)} from L(0..floor(k/2))
determine it.  m_{2k} = sum h* / (k+1)!.
"""
import sys, time
from fractions import Fraction as F
from math import comb, factorial

def L(k, N):
    V = 2 * N + 1                      # chord values -N..N -> index 0..2N
    cur = {}
    zero = (0,) * V
    for h in range(N + 1):
        cur[(h, zero)] = 1
    n = 2 * k
    for l in range(1, n + 1):
        nxt = {}
        rem = n - l                    # slots after this one
        for (h, cnt), w in cur.items():
            nopen = sum(cnt)
            # open a chord (only if it can still be closed)
            if nopen + 1 <= rem:
                for vi in range(V):
                    t = vi - N
                    h2 = h + t
                    if 0 <= h2 <= N:
                        c2 = list(cnt); c2[vi] += 1; key = (h2, tuple(c2))
                        nxt[key] = nxt.get(key, 0) + w
            # close a chord of value t: step -t, multiplicity cnt[vi]
            if nopen >= 1 and nopen - 1 <= rem:
                for vi in range(V):
                    m = cnt[vi]
                    if m:
                        t = vi - N
                        h2 = h - t
                        if 0 <= h2 <= N:
                            c2 = list(cnt); c2[vi] -= 1; key = (h2, tuple(c2))
                            nxt[key] = nxt.get(key, 0) + w * m
        cur = nxt
    return sum(w for (h, cnt), w in cur.items())

def hstar_from(vals, d):
    # L(n) = sum_i h_i C(n + d - i, d)
    hs = []
    for n, v in enumerate(vals):
        hs.append(v - sum(hs[i] * comb(n + d - i, d) for i in range(len(hs))))
    return hs

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7]
    for k in ks:
        t0 = time.time()
        half = k // 2 + 1                       # h_0..h_{floor(k/2)}
        vals = [L(k, N) for N in range(half)]
        hs = hstar_from(vals, k + 1)
        full = hs + [hs[k - i] for i in range(half, k + 1)]
        m = F(sum(full), factorial(k + 1))
        print(f"k={k}: L(0..{half-1}) = {vals}  h* = {full}  m_{2*k} = {m}  ({time.time()-t0:.0f}s)", flush=True)
