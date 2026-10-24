"""Confirm the MECHANISM of the step-3 sketch, not just its conclusion.

243/243 systems with |D| = r+k had an admissible pair-sum space. That is the conclusion. The sketch
says WHY:

  (M1) with R = span of chosen pair-sums, every f_t reduces mod R to +- its third coordinate,
       so every leftover form lands in the class of a COORDINATE form;
  (M2) hence every class contains at least one coordinate form;
  (M3) so one can pick a coordinate form per class - distinct coordinate forms, automatically
       independent - and #classes <= r.

If the conclusion held for a different reason, M2 would fail somewhere while valid_R still passed.
This checks M1-M3 directly on each system, separately for |D| = r+k and |D| > r+k, so the regime
boundary is visible rather than assumed.
"""
import itertools
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
rref = ns["rref"]
reduce_mod = ns["reduce_mod"]
fib = ns["fib"]

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 31)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 120


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


def shared_pairsum(T, r):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    vs = []
    for t in T:
        s = [x for x in t if x in sh]
        pick = (s[0], s[1]) if len(s) >= 2 else (t[0], t[1])
        v = [0] * r
        v[pick[0]] += 1
        v[pick[1]] += 1
        vs.append(v)
    return vs


def coord_forms(r):
    out = []
    for i in range(r):
        v = [0] * r
        v[i] = 1
        out.append(tuple(v))
    return set(out)


stats = {}
for _ in range(TRIALS):
    r = rng.choice([7, 8, 9, 10, 11])
    kmax = rng.choice([3, 4, 5, 6])
    T = random_system(r, kmax)
    used = sorted({x for t in T for x in t})
    if len(used) < 5 or len(T) < 2:
        continue
    lab = {x: i for i, x in enumerate(used)}
    T = [tuple(lab[x] for x in t) for t in T]
    rr, k = len(used), len(T)
    if rr > 12:
        continue
    A = fib(rr, T)
    if not A:
        continue
    D = full_dual(A, rr)
    regime = "|D| = r+k" if len(D) == rr + k else "|D| > r+k"
    vs = shared_pairsum(T, rr)
    basis, piv = rref(vs, rr)
    cls = {}
    for f in D:
        cls.setdefault(reduce_mod(f, basis, piv), []).append(tuple(f))
    coords = coord_forms(rr)
    # M2: does every class contain a coordinate form (up to sign)?
    def has_coord(group):
        for g in group:
            if g in coords or tuple(-x for x in g) in coords:
                return True
        return False
    m2 = all(has_coord(g) for g in cls.values())
    m3 = len(cls) <= rr
    ok = valid_R(D, vs, rr)
    key = (regime, m2, m3, ok)
    stats[key] = stats.get(key, 0) + 1

print("regime      M2 every class has a coordinate form")
print("            M3 #classes <= r")
print("            OK valid_R")
print()
print("  regime      M2     M3     valid_R   count")
for key in sorted(stats, key=lambda z: (z[0], not z[1], not z[3])):
    reg, m2, m3, ok = key
    print("  %-11s %-6s %-6s %-9s %d" % (reg, m2, m3, ok, stats[key]))
print()
print("The sketch predicts: in the |D| = r+k regime, M2 and M3 both TRUE and valid_R TRUE,")
print("with no other combination appearing.")
