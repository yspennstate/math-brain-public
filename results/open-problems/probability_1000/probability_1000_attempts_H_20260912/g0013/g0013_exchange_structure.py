"""G0013 exchange-structure test (2026-09-12, claude-q2-attack-0912).
For every permutation sigma of n points, compare T(sigma) with T(sigma o tau) over all transpositions tau
(swapping two positions) and over adjacent transpositions only.  Questions:
 Q1  does every non-extremal sigma have a strictly improving transposition (no other local maxima)?
 Q2  ... an improving ADJACENT transposition?
 Q3  if inv(sigma) < n(n-1)/4 (nearer the identity), is there an improving UNCROSSING (an inversion-reducing
     transposition)?  Symmetrically, nearer the reversal, an improving crossing?
 Q4  is the 'sort the first misplaced position' move always improving on the identity side?
"""
import itertools, sys, time
import numpy as np
from g0013_exact_assignment import T_of

def inv(s): return sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if s[i] > s[j])

def main(n):
    t0 = time.time()
    perms = list(itertools.permutations(range(n)))
    T = {s: T_of(n, s) for s in perms}
    ident = tuple(range(n)); rev = tuple(range(n-1, -1, -1))
    half = n*(n-1)/4
    q1 = q2 = q3 = q4 = 0; bad1 = []; bad2 = []; bad3 = []; bad4 = []
    for s in perms:
        if s in (ident, rev): continue
        v = T[s]; best_any = -1; best_adj = -1; best_toward = -1
        moves = []
        for i in range(n):
            for j in range(i+1, n):
                t = list(s); t[i], t[j] = t[j], t[i]; t = tuple(t)
                tv = T[t]; moves.append((i, j, tv, inv(t)))
                best_any = max(best_any, tv)
                if j == i+1: best_adj = max(best_adj, tv)
        k = inv(s)
        if k < half:      toward = [m for m in moves if m[3] < k]
        elif k > half:    toward = [m for m in moves if m[3] > k]
        else:             toward = moves
        best_toward = max(m[2] for m in toward)
        if best_any > v: q1 += 1
        else: bad1.append((s, v))
        if best_adj > v: q2 += 1
        else: bad2.append((s, v, best_adj))
        if best_toward > v: q3 += 1
        else: bad3.append((s, v, k))
        # Q4: first misplaced position i, swap position i with the position holding value i (identity side)
        if k < half:
            i = next(p for p in range(n) if s[p] != p); j = s.index(i)
            t = list(s); t[i], t[j] = t[j], t[i]; t = tuple(t)
            if T[t] > v: q4 += 1
            else: bad4.append((s, v, t, T[t]))
        elif k > half:
            i = next(p for p in range(n) if s[p] != n-1-p); j = s.index(n-1-i)
            t = list(s); t[i], t[j] = t[j], t[i]; t = tuple(t)
            if T[t] > v: q4 += 1
            else: bad4.append((s, v, t, T[t]))
    tot = len(perms) - 2
    print(f"n={n}: {tot} non-extremal perms ({time.time()-t0:.0f}s)")
    print(f"  Q1 improving transposition exists: {q1}/{tot}; failures: {bad1[:5]}")
    print(f"  Q2 improving ADJACENT transposition exists: {q2}/{tot}; failures: {bad2[:5]}")
    print(f"  Q3 improving move TOWARD the nearer extremal exists: {q3}/{tot}; failures: {bad3[:8]}")
    print(f"  Q4 'fix first misplaced position' toward nearer extremal improves: {q4}/{tot - sum(1 for s in perms if inv(s)==half and s not in (ident,rev))}; failures: {bad4[:8]}")
    # level structure: T as a function of inversion count
    byinv = {}
    for s in perms: byinv.setdefault(inv(s), []).append(T[s])
    print("  inv -> (min, max) T:", {k: (min(v), max(v)) for k, v in sorted(byinv.items())})

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    for n in [int(a) for a in sys.argv[1:]] or [5, 6, 7]:
        main(n)
