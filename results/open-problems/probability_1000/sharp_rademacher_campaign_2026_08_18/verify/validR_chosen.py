"""The honest version of the d_cb bound: the pair must be CHOSEN, not fixed to the shared one.

Correction to my earlier framing. `pairsum_space` always took each triangle's SHARED pair. On one
system in 240 that specific choice was inadmissible under the campaign's valid_R - but of the 729
possible pair-choices for that system, 725 were admissible and the minimum admissible dimension was
5, the same dimension the shared-pair choice had. So the family is fine; my selection rule was not.

This measures the real quantity the RC chain needs:

    d_cb  <=  min { dim span(chosen pair-sums) : the span is admissible under valid_R }

For each random linear system it enumerates pair-choices (3^k, capped), finds the minimum admissible
dimension, and compares against:
    - the shared-pair choice's dimension and admissibility (was my rule adequate?)
    - what RC needs, k - c/beta, computed from the exact fibre

Reports any system where NO choice is admissible (that would break the family), and any system where
RC is at risk.
"""
import itertools
import math
import random
import sys

SRC = "/srv/aiwork/rc_deep_box.py"
src = open(SRC, encoding="utf-8").read()
cut = src.index('print("dmax = %d"')
ns = {"__name__": "rc_lib", "sys": sys}
exec(compile(src[:cut], SRC, "exec"), ns)
full_dual = ns["full_dual"]
valid_R = ns["valid_R"]
rank_of = ns["rank_of"]
fib = ns["fib"]

BETA = math.log2(4.0 / 3.0)
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 60


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


def shared_choice(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    out = []
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) >= 2:
            pair = tuple(sorted(s[:2]))
        else:
            pair = (t[0], t[1])
        opts = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])]
        out.append(opts.index(pair) if pair in opts else 0)
    return tuple(out)


none_admissible = []
rc_risk = []
shared_bad = 0
tested = 0
worst_gap = None
for _ in range(TRIALS):
    r = rng.choice([8, 9, 10, 11])
    kmax = rng.choice([3, 4, 5])
    T = random_system(r, kmax)
    used = sorted({x for t in T for x in t})
    if len(used) < 5 or len(T) < 2:
        continue
    lab = {x: i for i, x in enumerate(used)}
    T = [tuple(lab[x] for x in t) for t in T]
    rr, k = len(used), len(T)
    if rr > 13 or 3 ** k > 300:
        continue
    A = fib(rr, T)
    if not A:
        continue
    tested += 1
    D = full_dual(A, rr)
    n = len(A)
    ell = rr - math.log2(n)
    c = k * BETA - ell
    need = k - c / BETA

    best = None
    for choice in itertools.product(range(3), repeat=k):
        vs = []
        for t, ci in zip(T, choice):
            pair = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])][ci]
            v = [0] * rr
            v[pair[0]] += 1
            v[pair[1]] += 1
            vs.append(v)
        d = rank_of(vs, rr)
        if best is not None and d >= best:
            continue
        if valid_R(D, vs, rr):
            best = d
    sc = shared_choice(T)
    vs = []
    for t, ci in zip(T, sc):
        pair = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])][ci]
        v = [0] * rr
        v[pair[0]] += 1
        v[pair[1]] += 1
        vs.append(v)
    if not valid_R(D, vs, rr):
        shared_bad += 1

    if best is None:
        none_admissible.append((rr, k, tuple(T)))
    else:
        gap = need - best
        if worst_gap is None or gap < worst_gap[0]:
            worst_gap = (gap, rr, k, tuple(T), best, need)
        if best > need:
            rc_risk.append((rr, k, tuple(T), best, need))

print("systems tested                              : %d" % tested)
print("systems where NO pair-choice is admissible  : %d" % len(none_admissible))
for x in none_admissible[:5]:
    print("    r=%d k=%d %s" % x)
print("systems where the SHARED-pair rule failed   : %d" % shared_bad)
print("systems where RC is at risk (min dim > need): %d" % len(rc_risk))
for x in rc_risk[:5]:
    print("    r=%d k=%d %s  min dim %d > need %.3f" % x)
print()
if worst_gap:
    g, rr, k, T, b, nd = worst_gap
    print("tightest system: min admissible dim %d against RC's allowance %.4f  (slack %.4f)" % (b, nd, g))
    print("   r=%d k=%d  %s" % (rr, k, T))
