#!/usr/bin/env python3
from itertools import product
from functools import lru_cache


def count_word(word, intervals):
    ranges = [range(intervals[c][0], intervals[c][1] + 1) for c in word]
    out = 0
    for g in product(*ranges):
        if all(g[i] <= g[i + 1] for i in range(len(g) - 1)):
            out += 1
    return out


# Exact deletion-fiber identity for p<u<v with q incomparable to p,u,v.
interval_cases = 0
for l0 in range(3):
    for l1 in range(l0, 4):
        for u0 in range(l0, 5):
            for u1 in range(max(u0, l1), 5):
                for v0 in range(u0, 6):
                    for v1 in range(max(v0, u1), 6):
                        I = (l0, l1)
                        J = (u0, u1)
                        K = (v0, v1)
                        ints = {'p': I, 'q': I, 'u': J, 'v': K}
                        words = [
                            ('q', 'p', 'u', 'v'),
                            ('p', 'q', 'u', 'v'),
                            ('p', 'u', 'q', 'v'),
                            ('p', 'u', 'v', 'q'),
                        ]
                        n = [count_word(w, ints) for w in words]
                        assert n[0] == n[1]
                        assert n[0] + n[1] == 2 * n[0]
                        interval_cases += 1


def closures(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen = set()
    for mask in range(1 << len(pairs)):
        rows = [0] * n
        for k, (i, j) in enumerate(pairs):
            if (mask >> k) & 1:
                rows[i] |= 1 << j
        for k in range(n):
            for i in range(n):
                if (rows[i] >> k) & 1:
                    rows[i] |= rows[k]
        t = tuple(rows)
        if t not in seen:
            seen.add(t)
            yield t


def rel(rows, a, b):
    if (rows[a] >> b) & 1:
        return -1
    if (rows[b] >> a) & 1:
        return 1
    return 0


def disting(rows, p, q):
    return [z for z in range(len(rows)) if z not in (p, q) and rel(rows, z, p) != rel(rows, z, q)]


def positive_upper(rows, p, q, z):
    return rel(rows, p, z) == -1 and rel(rows, z, q) == 0


def linear_extensions(rows):
    n = len(rows)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (rows[j] >> i) & 1:
                pred[i] |= 1 << j

    @lru_cache(None)
    def rec(mask):
        if mask == (1 << n) - 1:
            return ((),)
        ans = []
        for i in range(n):
            if not ((mask >> i) & 1) and (pred[i] & ~mask) == 0:
                for tail in rec(mask | (1 << i)):
                    ans.append((i,) + tail)
        return tuple(ans)

    return rec(0)


posets = 0
ordered_chain_cases = 0
for n in range(2, 7):
    for rows in closures(n):
        posets += 1
        exts = None
        for p in range(n):
            for q in range(n):
                if p == q or rel(rows, p, q) != 0:
                    continue
                ds = disting(rows, p, q)
                if len(ds) != 2 or not all(positive_upper(rows, p, q, z) for z in ds):
                    continue
                u, v = ds
                if rel(rows, u, v) == -1:
                    lo = u
                elif rel(rows, v, u) == -1:
                    lo = v
                else:
                    continue
                if exts is None:
                    exts = linear_extensions(rows)
                n_qp = sum(L.index(q) < L.index(p) for L in exts)
                n_qu = sum(L.index(q) < L.index(lo) for L in exts)
                assert n_qu == 2 * n_qp
                ordered_chain_cases += 1


# Six-point calibration: a comparable shared support can exist locally, so the
# proof must use the live adjacent strong-majority hypotheses rather than claim
# that shared support alone is impossible.
names = ['l', 'a', 'r', 'x', 'y', 'z']
idv = {v: i for i, v in enumerate(names)}
gens = [('l','a'), ('a','z'), ('z','r'), ('x','y'), ('l','y'), ('x','r')]
rows = [0] * len(names)
for u, v in gens:
    rows[idv[u]] |= 1 << idv[v]
for k in range(len(names)):
    for i in range(len(names)):
        if (rows[i] >> k) & 1:
            rows[i] |= rows[k]
exts = linear_extensions(tuple(rows))

def cnt_before(u, v):
    iu, iv = idv[u], idv[v]
    return sum(L.index(iu) < L.index(iv) for L in exts)

E = len(exts)
assert E == 13
assert cnt_before('l','x') == 9
assert cnt_before('x','a') == 8
assert cnt_before('a','y') == 11
assert cnt_before('y','r') == 9

print('interval_chain_cases', interval_cases)
print('naturally_labelled_posets', posets)
print('ordered_two_upper_chain_cases', ordered_chain_cases)
print('shared_comparable_calibration', E, cnt_before('l','x'), cnt_before('x','a'), cnt_before('a','y'), cnt_before('y','r'))
print('POS3_SHARED_SUPPORT_CHAIN_CHECK_PASS')
