"""The one system where my pair-sum choice was inadmissible. Does ANOTHER choice work?

Failure found by validR_mass.py seed 5 (1 of 240):
    r=8, k=6, T = ((0,1,6),(0,2,4),(0,3,7),(1,2,7),(5,6,7),(1,3,4)), dim R = 5

My `pairsum_space` always takes each triangle's SHARED pair. But a triangle offers THREE pairs, so
the construction has 3^k choices and I used exactly one. This enumerates all of them for this
system, and reports:
   - how many choices give an admissible R (valid_R True)
   - the minimum dim R over admissible choices  -> an upper bound on d_cb
   - what the RC chain needs for this system

If some admissible choice has dim R small enough, the RC conclusion survives for this system and the
lesson is that the residual family must be CHOSEN, not taken as the shared pair. If no choice works,
the d_cb bound genuinely fails here and the RC chain needs repair.
"""
import itertools
import math
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
T = [(0, 1, 6), (0, 2, 4), (0, 3, 7), (1, 2, 7), (5, 6, 7), (1, 3, 4)]
r = 8
k = len(T)

print("system: %s" % (T,))
print("linear: %s" % all(len(set(x) & set(y)) < 2 for x, y in itertools.combinations(T, 2)))
A = fib(r, T)
n = len(A)
ell = r - math.log2(n)
c = k * BETA - ell
print("r=%d k=%d |A|=%d  ell=%.6f  c=%+.6f  c/beta=%+.6f" % (r, k, n, ell, c, c / BETA))
print("independence prediction 2^r (3/4)^k = %.4f;  Z = %.6f" % (2.0 ** r * 0.75 ** k, n / (2.0 ** r * 0.75 ** k)))
D = full_dual(A, r)
print("|D| = %d   (r + k = %d)" % (len(D), r + k))
print()

best = None
adm = 0
tot = 0
by_dim = {}
for choice in itertools.product(range(3), repeat=k):
    vs = []
    for t, ci in zip(T, choice):
        pair = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])][ci]
        v = [0] * r
        v[pair[0]] += 1
        v[pair[1]] += 1
        vs.append(v)
    d = rank_of(vs, r)
    tot += 1
    if valid_R(D, vs, r):
        adm += 1
        by_dim[d] = by_dim.get(d, 0) + 1
        if best is None or d < best[0]:
            best = (d, choice)

print("pair-choices enumerated : %d" % tot)
print("admissible (valid_R)    : %d" % adm)
print("admissible dims         : %s" % dict(sorted(by_dim.items())))
if best:
    print()
    print("MINIMUM admissible dim R = %d  (choice %s)" % (best[0], best[1]))
    print("so d_cb <= %d for this system" % best[0])
    need = k - c / BETA
    print("RC needs d_cb <= k - c/beta = %.4f  ->  %d" % (need, math.floor(need)))
    print("RC on this system: %s" % ("HOLDS" if best[0] <= need else "*** AT RISK"))
else:
    print()
    print("NO admissible pair-sum choice at all - the pair-sum family fails on this system")
