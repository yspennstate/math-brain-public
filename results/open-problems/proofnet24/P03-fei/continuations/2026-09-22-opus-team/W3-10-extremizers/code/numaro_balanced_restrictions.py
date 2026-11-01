"""Exhaustive over ALL restrictions of Numaro's g with k free coordinates (every free set, every assignment of the
rest): among the balanced ones, maximum of J = H/(I-1), with primality and the free set of the maximiser.
Usage: python numaro_balanced_restrictions.py k1 k2 ..."""
import sys, time, itertools, json
import numpy as np
import numba as nb
sys.path.insert(0, '.')
from core import polite, walsh_int, popc, phi, is_prime, relevant, stats
polite()

@nb.njit(cache=True)
def JI(tt):
    W = walsh_int(tt)
    N = tt.shape[0]
    H = 0.0
    I = 0.0
    for S in range(N):
        p = (W[S] / N) ** 2
        H += phi(p)
        I += popc(S) * p
    return H, I

g = np.load('../../inputs/numaro18_pm1_table.npy').astype(np.int8)
arr = g.reshape([2] * 18).transpose(list(range(17, -1, -1)))   # arr[b0,...,b17]
res = {}
out = open('../logs/numaro_balanced_restrictions.log', 'a')
for k in [int(a) for a in sys.argv[1:]]:
    t0 = time.time()
    best = []
    nbal = 0
    for F in itertools.combinations(range(18), k):
        F = list(F)
        R = [i for i in range(18) if i not in F]
        rows = np.ascontiguousarray(arr.transpose(R + F[::-1]).reshape(1 << len(R), 1 << k))
        sums = rows.astype(np.int64).sum(axis=1)
        for r in np.nonzero(sums == 0)[0]:
            H, I = JI(rows[r])
            if I <= 1 + 1e-9:
                continue
            nbal += 1
            J = H / (I - 1)
            best.append((J, tuple(F), int(r)))
        if len(best) > 2000:
            best.sort(key=lambda z: -z[0]); best = best[:200]
    best.sort(key=lambda z: -z[0])
    # report distinct values with primality/full support
    shown = 0
    line = 'k=%d: %d balanced restrictions with I>1 (%.0fs)' % (k, nbal, time.time() - t0)
    print(line); out.write(line + '\n')
    lastJ = None
    for J, F, r in best:
        if lastJ is not None and abs(J - lastJ) < 1e-12:
            continue
        R = [i for i in range(18) if i not in F]
        rows = arr.transpose(R + list(F)[::-1]).reshape(1 << len(R), 1 << k)
        t = np.ascontiguousarray(rows[r])
        full = len(relevant(t)) == k
        pr = is_prime(t) if full else None
        fixed = {R[j]: int((r >> (len(R) - 1 - j)) & 1) for j in range(len(R))}
        s = stats(t)
        line = '   J=%.12f full_support=%s prime=%s free=%s fixed(bit=1 means coordinate true)=%s H=%.12f I=%.9f rho0=%.4f' % (
            J, full, pr, list(F), fixed, s['H'], s['I'], s['rho0'])
        print(line); out.write(line + '\n'); out.flush()
        res.setdefault(str(k), []).append(dict(J=J, free=list(F), fixed=fixed, prime=pr, full=full,
                                               table=''.join('1' if v == -1 else '0' for v in t)))
        lastJ = J
        shown += 1
        if shown >= 4:
            break
    json.dump(res, open('../logs/numaro_balanced_restrictions_%s.json' % '_'.join(sys.argv[1:]), 'w'))
