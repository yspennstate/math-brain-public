"""Aggregate Ehrhart counts of the Hankel moment polytopes.

A lattice point of N*P_H(pi) is (x0, s_1..s_k): x0 in [0,N], each chord carries a
sum s, and the walk x_l = s(chord at slot l) - x_{l-1} stays in [0,N].  The walk
returns to x0 automatically exactly when every chord joins slots of opposite
parity (parity-mixing pairings); other pairings have volume zero.  Scan slots left
to right with state (x, multiset of open (s, parity of opening slot)).

Mode "full k": print L(0..k) and the h* vector, to test palindromicity.
Mode "half k...": h* from L(0..floor(k/2)) assuming palindromic degree k.
"""
import sys, time
from fractions import Fraction as F
from math import comb, factorial

def L(k, N):
    S = 2 * N + 1                       # sums 0..2N
    V = 2 * S                           # (s, parity) -> index s*2 + p
    zero = (0,) * V
    cur = {(x, zero): 1 for x in range(N + 1)}
    n = 2 * k
    for l in range(1, n + 1):
        par = l % 2
        rem = n - l
        nxt = {}
        for (x, cnt), w in cur.items():
            nopen = sum(cnt)
            if nopen + 1 <= rem:
                for s in range(S):
                    x2 = s - x
                    if 0 <= x2 <= N:
                        c2 = list(cnt); c2[s * 2 + par] += 1
                        key = (x2, tuple(c2))
                        nxt[key] = nxt.get(key, 0) + w
            if nopen >= 1:
                for s in range(S):
                    m = cnt[s * 2 + (1 - par)]
                    if m:
                        x2 = s - x
                        if 0 <= x2 <= N:
                            c2 = list(cnt); c2[s * 2 + (1 - par)] -= 1
                            key = (x2, tuple(c2))
                            nxt[key] = nxt.get(key, 0) + w * m
        cur = nxt
    return sum(cur.values())

def hstar_from(vals, d):
    hs = []
    for n, v in enumerate(vals):
        hs.append(v - sum(hs[i] * comb(n + d - i, d) for i in range(len(hs))))
    return hs

if __name__ == "__main__":
    mode = sys.argv[1]
    ks = [int(a) for a in sys.argv[2:]]
    for k in ks:
        t0 = time.time()
        if mode == "full":
            vals = [L(k, N) for N in range(k + 2)]
            hs = hstar_from(vals, k + 1)
            print(f"k={k}: h* = {hs}  m = {F(sum(hs), factorial(k + 1))}", flush=True)
        else:
            half = k // 2 + 1
            vals = [L(k, N) for N in range(half)]
            hs = hstar_from(vals, k + 1)
            full = hs + [hs[k - i] for i in range(half, k + 1)]
            print(f"k={k}: L = {vals}  h* = {full}  m_{2*k} = {F(sum(full), factorial(k + 1))}  ({time.time()-t0:.0f}s)", flush=True)
