"""Independent attempt to break BT-9: sup over weighted thresholds and product laws of H+/Delta = 2 + 4/ln 2.

All distinct threshold functions with every coordinate relevant, n = 2..5 (integer weights 1..7, every
threshold), exact rational spectra (biases rational), random log-odds starts in [-16, 16] plus a greedy
coordinate hill-climb on log-odds.  Evidence only.
"""
import itertools
import math
import random
import sys
import time
from fractions import Fraction as Fr
from bfcore import *
import mpmath
mpmath.mp.dps = 40

TARGET = 2 + 4 / math.log(2)


def ratio(T, xs):
    qs = []
    for x in xs:
        q = 1 / (1 + math.exp(-x))
        qq = Fr(round(q * 10 ** 12), 10 ** 12)
        qq = min(max(qq, Fr(1, 10 ** 12)), 1 - Fr(1, 10 ** 12))
        qs.append(qq)
    P = spectrum([2 * t - 1 for t in T], qs)
    D = sum((popcount(S) - 1) * P[S] for S in range(len(P)) if popcount(S) >= 2)
    if D == 0:
        return 0.0
    # NOTE: float64 logs are NOT accurate here (log of 1 + 6e-12 loses 5 digits; a first run
    # reported 7.770826 > 2+4/ln2 on OR2, which is false at 50 digits).  Use mpmath logs.
    E = corrected_entropy(P, qs)
    return float(E / mpmath.log(2) / mpq(D))


def relevant_all(T, n):
    for i in range(n):
        if all(T[y] == T[y ^ (1 << i)] for y in range(1 << n)):
            return False
    return True


if __name__ == "__main__":
    random.seed(9)
    t0 = time.time()
    funcs = {}
    for n in range(2, 6):
        wmax = 7 if n <= 4 else 5
        for w in itertools.product(range(1, wmax + 1), repeat=n):
            if list(w) != sorted(w, reverse=True):
                continue
            for th in range(1, sum(w) + 1):
                T = tuple(threshold_table(list(w), th))
                if 0 < sum(T) < len(T) and relevant_all(T, n):
                    funcs.setdefault((n, T), (w, th))
    print("distinct threshold functions (all coordinates relevant), n=2..5:", len(funcs))
    best = (0, None)
    budget = 540
    keys = list(funcs.keys())
    it = 0
    while time.time() - t0 < budget:
        n, T = random.choice(keys)
        xs = [random.uniform(-16, 16) for _ in range(n)]
        v = ratio(T, xs)
        it += 1
        if v > best[0] - 0.3:
            step = 2.0
            while step > 0.05:
                improved = False
                for i in range(n):
                    for sgn in (1, -1):
                        ys = list(xs)
                        ys[i] = max(-27, min(27, ys[i] + sgn * step))
                        vv = ratio(T, ys)
                        if vv > v:
                            v, xs, improved = vv, ys, True
                if not improved:
                    step /= 2
        if v > best[0]:
            best = (v, (funcs[(n, T)], [round(x, 3) for x in xs]))
            print("  new best %.6f  (target %.6f)  %s  t=%.0fs" % (v, TARGET, best[1], time.time() - t0))
            sys.stdout.flush()
    print("random starts:", it, " best H+/Delta found:", best[0], " exceeds 2+4/ln2?", best[0] > TARGET + 1e-9)
