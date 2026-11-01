"""Does |D| = r + k predict admissibility of the pair-sum space? And does P6 always hold?

PROOF SKETCH for the last link in the RC chain. Let R = span of one chosen pair-sum per triangle.
  - f_t = e_a + e_b + e_c  and  v_t = e_a + e_b in R,  so  f_t == e_c  mod R.
    Every leftover form therefore joins the CLASS OF A COORDINATE FORM.
  - Coordinate forms merge along the chosen-pair graph H: e_a == -e_b for each chosen pair. A
    bipartite component of H gives one class; a NON-bipartite component forces e == -e, i.e. e in R,
    so all its coordinates fall into the ZERO class.
  - Hence every class contains at least one coordinate form, and #classes <= r.
  - Pick one COORDINATE form per class: they are distinct coordinate forms, hence automatically
    linearly independent. valid_R's transversal exists.  QED

**The argument needs D = {coordinate forms} u {f_t}, i.e. |D| = r + k.** If D carries extra forms,
a class could consist only of those, with no coordinate form to pick, and the argument fails. The
campaign's P6 asserts |D| = r + k. The one system where my construction failed had |D| = 30 against
r + k = 14 - which fits exactly.

So two things to measure, on random linear systems:
  (A) how often is |D| = r + k?   (P6 as stated)
  (B) is valid_R(pair-sum) TRUE exactly when |D| = r + k?

A clean correspondence would prove the last link on the P6 regime AND flag a limit on P6 itself.
A valid_R failure WITH |D| = r+k would refute my sketch outright - that is the outcome to watch for.
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
fib = ns["fib"]

rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 21)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 150


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


tab = {}          # (|D| == r+k, valid_R) -> count
examples = {}
p6_ok = p6_bad = 0
tested = 0
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
    if rr > 13:
        continue
    A = fib(rr, T)
    if not A:
        continue
    tested += 1
    D = full_dual(A, rr)
    p6 = (len(D) == rr + k)
    if p6:
        p6_ok += 1
    else:
        p6_bad += 1
    vs = shared_pairsum(T, rr)
    ok = valid_R(D, vs, rr)
    key = (p6, ok)
    tab[key] = tab.get(key, 0) + 1
    if key not in examples:
        examples[key] = (rr, k, len(A), len(D), tuple(T))

print("systems tested: %d" % tested)
print()
print("P6 as stated (|D| = r + k):  holds %d,  FAILS %d" % (p6_ok, p6_bad))
print()
print("cross-tabulation:")
print("   |D|=r+k   valid_R    count")
for key in sorted(tab, key=lambda z: (not z[0], not z[1])):
    print("   %-9s %-10s %d" % (key[0], key[1], tab[key]))
print()
print("one example of each cell (r, k, |A|, |D|, system):")
for key in sorted(examples, key=lambda z: (not z[0], not z[1])):
    print("   |D|=r+k %-6s valid_R %-6s : %s" % (key[0], key[1], examples[key]))
print()
print("The cell to watch is (|D|=r+k TRUE, valid_R FALSE): that would refute the sketch.")
