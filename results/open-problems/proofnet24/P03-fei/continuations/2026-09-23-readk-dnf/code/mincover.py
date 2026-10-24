"""Minimal-cover cost of the spectral sample of read-k DNF formulas.
For each nonempty A: c(A) = min |V(U)| over sets U of terms whose variable sets cover A
(V(U) = union).  Reports E_P[c(S)]/E_P|S| over nonempty S, next to the all-dense-terms cost
E_P[sum_{t dense} |V_t|]/E|S| (beta = 3) used in the proof, as k grows."""
import numpy as np, numba as nb
from feicore import spectrum, popcounts, polite
polite()

@nb.njit(cache=True)
def unions_closure(masks, n):
    N = 1 << n
    reach = np.zeros(N, dtype=np.bool_)
    reach[0] = True
    stack = np.zeros(N, dtype=np.int64); sp = 0
    stack[sp] = 0; sp += 1
    while sp > 0:
        sp -= 1; B = stack[sp]
        for m in masks:
            C = B | m
            if not reach[C]:
                reach[C] = True; stack[sp] = C; sp += 1
    return reach

@nb.njit(cache=True)
def min_superset(best, n):
    a = best.copy()
    for i in range(n):
        bit = 1 << i
        for A in range(1 << n):
            if (A & bit) == 0:
                if a[A | bit] < a[A]:
                    a[A] = a[A | bit]
    return a

def random_readk(n, k, rng, wmin=2, wmax=5):
    load = np.zeros(n, dtype=int); terms = []
    for _ in range(40 * n):
        w = int(rng.integers(wmin, wmax + 1))
        cand = np.where(load < k)[0]
        if len(cand) < w: break
        p = (k - load[cand]).astype(float); p /= p.sum()
        V = rng.choice(cand, size=w, replace=False, p=p)
        load[V] += 1
        signs = rng.integers(0, 2, size=w)
        terms.append((V, signs))
    return terms

def tt_dnf(n, terms):
    xs = np.arange(1 << n); val = np.zeros(1 << n, dtype=bool)
    for V, s in terms:
        ok = np.ones(1 << n, dtype=bool)
        for v, b in zip(V, s):
            ok &= ((xs >> int(v)) & 1) == int(b)
        val |= ok
    return np.where(val, -1, 1).astype(np.int8)

rng = np.random.default_rng(11)
pc_cache = {}
for n in (14, 16):
    pc = popcounts(n)
    for k in (1, 2, 3, 4, 6, 8):
        for rep in range(3):
            terms = random_readk(n, k, rng)
            if not terms: continue
            masks = np.array([sum(1 << int(v) for v in V) for V, _ in terms], dtype=np.int64)
            tt = tt_dnf(n, terms)
            P = spectrum(tt)
            reach = unions_closure(masks, n)
            best = np.where(reach, pc.astype(np.float64), np.inf)
            ms = min_superset(best, n)
            nz = np.arange(1, 1 << n)
            Pn = P[nz]; I = float((Pn * pc[nz]).sum())
            cmin = float((Pn * ms[nz]).sum())
            # all-dense cost, beta=3
            sizes = np.array([len(V) for V, _ in terms])
            inter = np.zeros((len(nz),), dtype=np.float64)
            dense_cost = np.zeros(1 << n)
            for m, w in zip(masks, sizes):
                cnt = popcounts(n)[np.arange(1 << n) & m] if False else None
            A = np.arange(1 << n)
            dc = np.zeros(1 << n)
            for m, w in zip(masks, sizes):
                ai = pc[A & m]
                dc += np.where(3 * ai >= w, w, 0)
            dcost = float((P[nz] * dc[nz]).sum())
            maxload = max(np.bincount(np.concatenate([V for V, _ in terms]), minlength=n))
            print(f"n={n} k={k} (max load {maxload}) terms={len(terms):3d}  E[mincover]/I={cmin/I:6.3f}  E[alldense]/I={dcost/I:6.3f}  I={I:.3f}", flush=True)
