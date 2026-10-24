"""Can the remaining gap be closed for free? Test: |D| > r+k  =>  c <= 0.

Where the chain stands:
  |D| = r+k  : RC proved (Ising closed form + the cut inequality + the step-3 transversal argument).
  |D| > r+k  : the step-3 argument does not apply, because a class can consist of extra dual forms
               with no coordinate form to pick.

But RC does not need step 3 when c <= 0. RC is  c <= beta(k - d_cb), and the campaign has PROVED
d_cb <= k, so any system with c <= 0 satisfies RC outright.

And there is a reason to expect c <= 0 exactly outside the regime: |D| counts linear forms that are
+-1-valued on the fibre A, so extra forms appear when A is SMALL - and a small fibre means large
ell = r - log2|A|, hence very negative c = k*beta - ell. The one system where the pair-sum
construction failed had c/beta = -1.45 with an allowance of 7.45 against k = 6, i.e. RC held
trivially by d_cb <= k.

If  |D| > r+k  =>  c <= 0  holds, then RC is proved for ALL linear NAE triangle systems:
    |D| = r+k  by the chain, |D| > r+k  by c <= 0 and d_cb <= k.

This measures c against |D| - (r+k) on random systems and reports any system with |D| > r+k AND
c > 0 - which is the only thing that would keep the gap open.
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
fib = ns["fib"]

BETA = math.log2(4.0 / 3.0)
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 41)
TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 200


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


inside_pos = inside_nonpos = 0
outside_pos = outside_nonpos = 0
bad = []
worst_outside_c = None
tested = 0
for _ in range(TRIALS):
    r = rng.choice([7, 8, 9, 10, 11, 12])
    kmax = rng.choice([3, 4, 5, 6, 7])
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
    extra = len(D) - (rr + k)
    ell = rr - math.log2(len(A))
    c = k * BETA - ell
    if extra == 0:
        if c > 1e-12:
            inside_pos += 1
        else:
            inside_nonpos += 1
    else:
        if c > 1e-12:
            outside_pos += 1
            bad.append((rr, k, len(A), len(D), extra, c / BETA, tuple(T)))
        else:
            outside_nonpos += 1
        if worst_outside_c is None or c > worst_outside_c[0]:
            worst_outside_c = (c, rr, k, len(A), len(D), tuple(T))

print("systems tested: %d" % tested)
print()
print("  |D| = r+k  (inside the proved regime):  c > 0 : %d    c <= 0 : %d" % (inside_pos, inside_nonpos))
print("  |D| > r+k  (outside):                   c > 0 : %d    c <= 0 : %d" % (outside_pos, outside_nonpos))
print()
if bad:
    print("*** systems OUTSIDE the regime with c > 0 - these keep the gap open:")
    for rr, k, na, nd, ex, cb, T in bad[:8]:
        print("    r=%d k=%d |A|=%d |D|=%d (extra %d) c/beta=%+.4f  %s" % (rr, k, na, nd, ex, cb, T))
else:
    print("NO system outside the regime had c > 0.")
    print("If that holds in general, RC follows there from the campaign's proved d_cb <= k,")
    print("and the chain covers ALL linear NAE triangle systems.")
if worst_outside_c:
    c, rr, k, na, nd, T = worst_outside_c
    print()
    print("largest c seen outside the regime: c/beta = %+.4f  (r=%d k=%d |A|=%d |D|=%d)"
          % (c / BETA, rr, k, na, nd))
