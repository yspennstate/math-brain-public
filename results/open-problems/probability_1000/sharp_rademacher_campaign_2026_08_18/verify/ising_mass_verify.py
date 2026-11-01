"""Mass machine-check of the Ising law. Trust replaced by machinery, not by care.

CLAIM: for every linear NAE triangle system,
    |A| / (2^r (3/4)^k) = Z = SUM over even edge-selections of (-1/3)^{|S|},
each triangle contributing at most one edge: its unique shared pair (2 shared coords) or any one of
its three pairs (3 shared coords); triangles with <=1 shared coordinate contribute no edge.

The proof rests on a case analysis over how many of a triangle's coordinates are shared. The step
that "feels free" is that EVERY case factors as 2^{#private}(3/4) times a residual term - i.e. that
the normalisation 2^r(3/4)^k is exactly right in all four cases. This checks the whole claim,
end to end, on a large random population that hits all four cases, with |A| by exact enumeration.

Reports a per-case breakdown so a failure localises to a triangle type rather than just failing.
Exact rational comparison, no float tolerance.
"""
import itertools
import random
import sys
from fractions import Fraction

SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 400
rng = random.Random(SEED)


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        ok = True
        for (a, b, c) in T:
            if s[a] == s[b] == s[c]:
                ok = False
                break
        if ok:
            n += 1
    return n


def is_linear(T):
    return all(len(set(x) & set(y)) < 2 for x, y in itertools.combinations(T, 2))


def Z_exact(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    opts = []
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) <= 1:
            opts.append([None])
        elif len(s) == 2:
            opts.append([None, tuple(sorted(s))])
        else:
            opts.append([None] + [tuple(sorted(p)) for p in itertools.combinations(s, 2)])
    verts = sorted(sh)
    idx = {v: i for i, v in enumerate(verts)}
    tot = Fraction(0)
    for choice in itertools.product(*opts):
        deg = [0] * len(verts)
        ne = 0
        for e in choice:
            if e is None:
                continue
            deg[idx[e[0]]] += 1
            deg[idx[e[1]]] += 1
            ne += 1
        if all(d % 2 == 0 for d in deg):
            tot += Fraction(-1, 3) ** ne
    return tot


def random_system(r, kmax):
    allt = list(itertools.combinations(range(r), 3))
    rng.shuffle(allt)
    T = []
    for t in allt:
        if all(len(set(t) & set(u)) < 2 for u in T):
            T.append(t)
        if len(T) >= kmax:
            break
    return T


ok = bad = skipped = 0
case_counts = {0: 0, 1: 0, 2: 0, 3: 0}
failures = []
for trial in range(TRIALS):
    r = rng.choice([7, 8, 9, 10, 11, 12])
    kmax = rng.choice([3, 4, 5, 6, 7])
    T = random_system(r, kmax)
    used = sorted({x for t in T for x in t})
    if len(used) < 4 or len(T) < 2:
        skipped += 1
        continue
    lab = {x: i for i, x in enumerate(used)}
    T = [tuple(lab[x] for x in t) for t in T]
    rr = len(used)
    if rr > 20 or not is_linear(T):
        skipped += 1
        continue
    k = len(T)
    if len(T) > 13:
        skipped += 1
        continue
    # per-triangle case census
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    for t in T:
        case_counts[sum(1 for x in t if cnt[x] >= 2)] += 1

    n = fibre_size(rr, T)
    lhs = Fraction(n) * Fraction(4, 3) ** k / Fraction(2) ** rr
    rhs = Z_exact(T)
    if lhs == rhs:
        ok += 1
    else:
        bad += 1
        if len(failures) < 5:
            failures.append((T, rr, k, n, lhs, rhs))

print("trials attempted : %d" % TRIALS)
print("checked exactly  : %d" % (ok + bad))
print("skipped (size)   : %d" % skipped)
print()
print("EXACT MATCHES    : %d" % ok)
print("MISMATCHES       : %d" % bad)
print()
print("triangle-type coverage (shared-coordinate count per triangle):")
for c in sorted(case_counts):
    print("   %d shared : %6d triangles" % (c, case_counts[c]))
if failures:
    print()
    print("first failures:")
    for T, rr, k, n, lhs, rhs in failures:
        print("   T=%s r=%d k=%d |A|=%d  lhs=%s  rhs=%s" % (T, rr, k, n, lhs, rhs))
