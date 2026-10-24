#!/usr/bin/env python3
import math, random

SEED = 20260920
TOL = 1e-10

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def entropy_and_l1(vals):
    w = fwht(vals)
    H = 0.0
    L = 0.0
    for a in w:
        p = a*a
        L += abs(a)
        if p > 0.0:
            H -= p*math.log2(p)
    return H, L

def influence(vals, n):
    N = 1 << n
    total = 0.0
    for i in range(n):
        bit = 1 << i
        disagree = 0
        for x in range(N):
            if (x & bit) == 0 and vals[x] != vals[x | bit]:
                disagree += 1
        total += disagree / (N/2)
    return total

def restrict(vals, n, i, b):
    out = []
    for y in range(1 << (n-1)):
        lo = y & ((1 << i)-1)
        hi = y >> i
        x = lo | (b << i) | (hi << (i+1))
        out.append(vals[x])
    return out

_quad_cache = {}
def quadratic_phases(n):
    if n in _quad_cache:
        return _quad_cache[n]
    mons = [("lin", i) for i in range(n)]
    mons += [("quad", i, j) for i in range(n) for j in range(i+1, n)]
    phases = []
    for mask in range(1 << len(mons)):
        vals = []
        for x in range(1 << n):
            bit = 0
            for k, mon in enumerate(mons):
                if (mask >> k) & 1:
                    if mon[0] == "lin":
                        bit ^= (x >> mon[1]) & 1
                    else:
                        bit ^= ((x >> mon[1]) & 1) & ((x >> mon[2]) & 1)
            vals.append(-1 if bit else 1)
        phases.append(vals)
    _quad_cache[n] = phases
    return phases

def lambda2(vals, n):
    if n == 0:
        return 1.0
    best = float("inf")
    for q in quadratic_phases(n):
        u = [a*b for a, b in zip(vals, q)]
        _, L = entropy_and_l1(u)
        best = min(best, L)
    return best

def Cqw(L):
    return max(15.0, 2.0*math.log2(math.e) + 12.0*math.log2(max(1.0, L)))

def check_state(vals, n):
    H, _ = entropy_and_l1(vals)
    I = influence(vals, n)
    L2 = lambda2(vals, n)
    theorem_slack = Cqw(L2)*I - H
    mono_slack = float("inf")
    if n:
        for i in range(n):
            for b in (0, 1):
                child = restrict(vals, n, i, b)
                Lc = lambda2(child, n-1)
                mono_slack = min(mono_slack, L2-Lc)
    return theorem_slack, mono_slack, H/I if I > 0 else 0.0, L2

def main():
    exact_states = 0
    min_theorem_slack = float("inf")
    min_mono_slack = float("inf")
    max_ratio = 0.0
    max_L2 = 1.0

    for n in range(1, 4):
        N = 1 << n
        for mask in range(1 << N):
            vals = [-1 if ((mask >> x) & 1) else 1 for x in range(N)]
            ts, ms, ratio, L2 = check_state(vals, n)
            exact_states += 1
            min_theorem_slack = min(min_theorem_slack, ts)
            min_mono_slack = min(min_mono_slack, ms)
            max_ratio = max(max_ratio, ratio)
            max_L2 = max(max_L2, L2)

    rng = random.Random(SEED)
    random_states = 120
    n = 4
    random_min_theorem = float("inf")
    random_min_mono = float("inf")
    random_max_ratio = 0.0
    random_max_L2 = 1.0
    for _ in range(random_states):
        vals = [rng.choice((-1, 1)) for _ in range(1 << n)]
        ts, ms, ratio, L2 = check_state(vals, n)
        random_min_theorem = min(random_min_theorem, ts)
        random_min_mono = min(random_min_mono, ms)
        random_max_ratio = max(random_max_ratio, ratio)
        random_max_L2 = max(random_max_L2, L2)

    h01 = -(0.1*math.log2(0.1) + 0.9*math.log2(0.9))
    integer_margin = 32*(9**9) - 10**10

    print("quadratic-normalized Wiener sanity checker")
    print("seed =", SEED)
    print("h2(1/10) =", repr(h01))
    print("exact integer witness 32*9^9 - 10^10 =", integer_margin)
    print("C_QW(3) =", repr(Cqw(3.0)))
    print("C_QW(9) =", repr(Cqw(9.0)))
    print("exhaustive states n<=3 =", exact_states)
    print("exhaustive min theorem slack =", repr(min_theorem_slack))
    print("exhaustive min Lambda2 monotonicity slack =", repr(min_mono_slack))
    print("exhaustive max H/I =", repr(max_ratio))
    print("exhaustive max Lambda2 =", repr(max_L2))
    print("random n=4 states =", random_states)
    print("random min theorem slack =", repr(random_min_theorem))
    print("random min Lambda2 monotonicity slack =", repr(random_min_mono))
    print("random max H/I =", repr(random_max_ratio))
    print("random max Lambda2 =", repr(random_max_L2))

    assert h01 < 0.5
    assert integer_margin > 0
    assert min_theorem_slack >= -TOL
    assert min_mono_slack >= -TOL
    assert random_min_theorem >= -TOL
    assert random_min_mono >= -TOL
    print("PASS")

if __name__ == "__main__":
    main()
