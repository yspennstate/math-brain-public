# Subcube edits of a seed gate, no symmetry kept in the result: fix d of the inputs to given values and, on that subcube
# only, replace the gate by its negation, by a constant, or by a free input or its negation.  One subcube from each orbit
# of the structure's group is tried (the seed is invariant, so the score is the same along an orbit).  Each edited gate
# is scored from its full transform; the best few are scored again by sym_search.explicit from a rebuilt truth table.
#   usage: python3 cube1.py CODEDIR WTABLE STRUCT SEEDNAME D OUT [--check]
# --check also runs every subcube (no orbit reduction) and compares the sets of scores (all edits for D = 1, negation
# only for larger D).
import heapq
import itertools
import sys
import time
import numpy as np
sys.path.insert(0, sys.argv[1])
import sym_search as S

tab = np.loadtxt(sys.argv[2]); wt, ww = tab[:, 0], tab[:, -1]


def wfun(p):
    p = min(max(p, 1e-15), 1 - 1e-15)
    return float(np.interp(np.log2(p / (1 - p)), wt, ww))


c = wfun(0.5)
name, seedname, D, out = sys.argv[3], sys.argv[4], int(sys.argv[5]), sys.argv[6]
check = "--check" in sys.argv
B = 24
fo = open(out, "a")


def say(s):
    print(s, flush=True); fo.write(s + "\n"); fo.flush()


t0 = time.time()
m, gens, edges = S.struct(name)
N = 1 << m
f = dict(S.graph_seeds(m, edges, N))[seedname].copy()
G0, J0, pp0, sl0 = S.explicit(f, wfun, c)
idx = np.arange(N, dtype=np.int64)
for g in gens:                                   # the seed is invariant under every generator
    y = np.zeros(N, dtype=np.int64)
    for i in range(m):
        y |= ((idx >> i) & 1) << g[i]
    assert np.array_equal(f[y], f), "seed not invariant"
idt = tuple(range(m)); seen = {idt}; stack = [idt]
while stack:
    a = stack.pop()
    for g in gens:
        b = tuple(g[a[i]] for i in range(m))
        if b not in seen:
            seen.add(b); stack.append(b)
grp = sorted(seen)
say("# cube edits of %s seed %s m=%d d=%d group order %d c=%.12f; seed value %+.12f G %.9f J %.9f" % (name, seedname, m, D, len(grp), c, sl0, G0, J0))


def img(g, x):
    r = 0; i = 0
    while x:
        if x & 1:
            r |= 1 << g[i]
        x >>= 1; i += 1
    return r


def cubes(reduce):
    for comb in itertools.combinations(range(m), D):
        mask = sum(1 << i for i in comb)
        if reduce:
            if any(img(g, mask) < mask for g in grp):
                continue
            stab = [g for g in grp if img(g, mask) == mask]
        for bits in range(1 << D):
            val = sum(1 << comb[i] for i in range(D) if bits >> i & 1)
            if reduce and any(img(g, val) < val for g in stab):
                continue
            yield mask, val


pcf = S.popcounts(N).astype(np.float64)
lits = [1.0 - 2.0 * ((idx >> j) & 1) for j in range(m)]
buf = np.empty((B, N)); tags = []


def edits(mask, val, only_neg):
    sel = (idx & mask) == val
    fs = f[sel]
    yield "neg", sel, -fs
    if only_neg:
        return
    for nm, v in (("+1", 1.0), ("-1", -1.0)):
        new = np.full(fs.shape, v)
        if not np.array_equal(new, fs):
            yield nm, sel, new
    for j in range(m):
        if mask >> j & 1:
            continue
        for sg, nm in ((1.0, "x%d" % j), (-1.0, "-x%d" % j)):
            new = sg * lits[j][sel]
            if not np.array_equal(new, fs):
                yield nm, sel, new


def build(tag):
    mask, val, nm = tag
    for n2, sel, new in edits(mask, val, False):
        if n2 == nm:
            g = f.copy(); g[sel] = new
            return g
    raise ValueError(tag)


def flush(sink):
    k = len(tags)
    if not k:
        return
    a = buf[:k]
    S.fwht_rows(a)
    a /= N
    mean = a[:, 0].copy()
    np.multiply(a, a, out=a); a[:, 0] = 0.0
    V = a.sum(axis=1); Jn = a @ pcf
    for r in range(k):
        if V[r] < 1e-12:
            continue
        pi = a[r] / V[r]; pi = pi[pi > 0]
        G = float(-(pi * np.log2(pi)).sum()); J = float(Jn[r] / V[r]); pp = 0.5 * (1 - mean[r])
        sink(G - c * J + wfun(pp), G, J, pp, tags[r])
    tags.clear()


def scan(reduce, only_neg, sink):
    ncube = 0
    for mask, val in cubes(reduce):
        ncube += 1
        for nm, sel, new in edits(mask, val, only_neg):
            row = buf[len(tags)]
            row[:] = f; row[sel] = new
            tags.append((mask, val, nm))
            if len(tags) == B:
                flush(sink)
        if ncube % 200 == 0:
            print("progress cubes", ncube, "%.0f s" % (time.time() - t0), flush=True)
    flush(sink)
    return ncube


def show(mask, val, nm):
    E = m // 2
    pat = "".join("*" if not mask >> i & 1 else str(val >> i & 1) for i in range(m))
    return "cells %s coins %s -> %s" % (pat[:E], pat[E:], nm)


stat = {"n": 0, "ties": 0, "pos": 0, "best": -1e9}
top = []
allv = set()


def sink(sl, G, J, pp, tag):
    stat["n"] += 1
    allv.add((round(sl, 7), tag[2] == "neg"))
    if abs(sl) < 1e-9 and abs(J - J0) < 1e-9:
        stat["ties"] += 1                       # the seed again (an input renamed or negated)
        return
    stat["best"] = max(stat["best"], sl)
    if sl > 1e-7 and J > 1 + 1e-9:
        stat["pos"] += 1
        say("!!! POSITIVE SLACK %+.9f G %.9f J %.9f p' %.9f %s: check before a word is said" % (sl, G, J, pp, show(*tag)))
    item = (sl, stat["n"], G, J, pp, tag)
    if len(top) < 8:
        heapq.heappush(top, item)
    elif sl > top[0][0]:
        heapq.heapreplace(top, item)


ncube = scan(True, False, sink)
for sl, _, G, J, pp, tag in sorted(top, reverse=True):
    G2, J2, pp2, sl2 = S.explicit(build(tag), wfun, c)
    say("top slack %+.9f G %.9f J %.9f p' %.9f | explicit: slack %+.9f | %s" % (sl, G, J, pp, sl2, show(*tag)))
total = sum(1 for _ in itertools.combinations(range(m), D)) << D
say("summary d=%d subcubes %d, one per orbit %d, gates scored %d, the seed again %d, above 0: %d, best below the seed slack %+.9f; %.0f s"
    % (D, total, ncube, stat["n"], stat["ties"], stat["pos"], stat["best"], time.time() - t0))
if check:
    red = set(allv) if D == 1 else {v for v in allv if v[1]}
    full = set()
    scan(False, D != 1, lambda sl, G, J, pp, tag: full.add((round(sl, 7), tag[2] == "neg")))
    say("reduction check d=%d (%s): distinct scores one-per-orbit %d, every subcube %d, same set %s"
        % (D, "all edits" if D == 1 else "negation only", len(red), len(full), red == full))
