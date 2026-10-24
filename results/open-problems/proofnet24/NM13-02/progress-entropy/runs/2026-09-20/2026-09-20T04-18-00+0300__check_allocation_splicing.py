#!/usr/bin/env python3
from fractions import Fraction
import itertools, json, math, random

def fwht(values):
    a = [float(x) for x in values]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def phase_from_weight_profile(n, vals):
    return [vals[x.bit_count()] for x in range(1 << n)]

def spectral_entropy(f):
    return sum(-p*math.log2(p) for p in (x*x for x in fwht(f)) if p > 1e-15)

def influence(f, n, i):
    return Fraction(sum(f[x] != f[x ^ (1 << i)] for x in range(1 << n)), 1 << n)

def B_coord(f, n, i):
    p = [x*x for x in fwht(f)]
    bit = 1 << i
    out = 0.0
    for T in range(1 << n):
        if T & bit:
            continue
        a, b = p[T], p[T | bit]
        s = a+b
        if a > 1e-15 and b > 1e-15:
            q = b/s
            out += s * (-q*math.log2(q) - (1-q)*math.log2(1-q))
    return out

# Exhaust every symmetric Boolean function through n=8.
sym_summary = {}
global_sym = (0.0, None)
han_slack_min = float("inf")
for n in range(1, 9):
    count = 0
    max_ratio = 0.0
    for mask in range(1 << (n+1)):
        vals = [1 if ((mask >> k) & 1) == 0 else -1 for k in range(n+1)]
        f = phase_from_weight_profile(n, vals)
        p = float(influence(f, n, 0))
        if p == 0.0:
            continue
        H = spectral_entropy(f)
        B = B_coord(f, n, 0)
        slack = H - n*B
        if slack < -1e-9:
            raise AssertionError(("Han inequality numeric failure", n, mask, slack))
        if B > 12.04*p + 1e-9:
            raise AssertionError(("12.04 local certificate failure", n, mask, B/p))
        han_slack_min = min(han_slack_min, slack)
        ratio = B/p
        max_ratio = max(max_ratio, ratio)
        if ratio > global_sym[0]:
            global_sym = (ratio, [n, mask, H, B, p])
        count += 1
    sym_summary[n] = {"nonconstant_profiles": count, "max_B_over_Inf": max_ratio}

# Exhaust unweighted thresholds through n=12; this is only stress data.
thr_summary = {}
thr_global = (0.0, None)
for n in range(2, 13):
    max_ratio = 0.0
    arg = None
    for theta in range(-n+1, n, 2):
        if theta % 2 == n % 2:
            continue
        vals = [1 if 2*k-n > theta else -1 for k in range(n+1)]
        f = phase_from_weight_profile(n, vals)
        p = float(influence(f, n, 0))
        if p == 0.0:
            continue
        B = B_coord(f, n, 0)
        ratio = B/p
        if ratio > max_ratio:
            max_ratio, arg = ratio, [theta, p, B]
        if ratio > thr_global[0]:
            thr_global = (ratio, [n, theta, p, B])
    thr_summary[n] = {"max_B_over_Inf": max_ratio, "arg": arg}

# Exact algebraic degree of the phase bit for shifted threshold f_m.
# If g(w)=1_{w<=t}, then for d>t its symmetric ANF coefficient is
# sum_{j<=t} C(d,j) = C(d-1,t) mod 2.
def shifted_anf_degree(m):
    n = m*m + 1
    t = (n + m - 1)//2
    degree = 0
    for d in range(n+1):
        if d == 0:
            a = 1
        elif d <= t:
            a = 0
        else:
            a = math.comb(d-1, t) & 1
        if a:
            degree = d
    return n, t, degree

anf = {}
for m in [2, 4, 8, 16]:
    n, t, d = shifted_anf_degree(m)
    if d != m*m or d != n-1:
        raise AssertionError(("shifted degree failure", m, n, t, d))
    anf[m] = {"n": n, "t": t, "degree": d}

# Exact partial influence budget Q_T + sum_l w_l I(f_l)=I(f).
def inf_under_restriction(f, n, i, assign):
    assert i not in assign
    free = [j for j in range(n) if j not in assign and j != i]
    good = total = 0
    for vals in itertools.product([0,1], repeat=len(free)):
        x = 0
        for j,b in assign.items():
            if b:
                x |= 1 << j
        for j,b in zip(free, vals):
            if b:
                x |= 1 << j
        x0 = x & ~(1 << i)
        x1 = x0 | (1 << i)
        total += 1
        good += (f[x0] != f[x1])
    return Fraction(good, total)

def total_inf_restriction(f, n, assign):
    return sum((inf_under_restriction(f, n, i, assign)
                for i in range(n) if i not in assign), Fraction())

def random_partial_tree(n, assign):
    free = [i for i in range(n) if i not in assign]
    if not free or random.random() < 0.35:
        return ("L",)
    i = random.choice(free)
    a0, a1 = dict(assign), dict(assign)
    a0[i], a1[i] = 0, 1
    return ("q", i, random_partial_tree(n, a0), random_partial_tree(n, a1))

def budget(f, n, tree, assign=None, weight=Fraction(1)):
    if assign is None:
        assign = {}
    if tree[0] == "L":
        return Fraction(), weight * total_inf_restriction(f, n, assign)
    _, i, left, right = tree
    q = weight * inf_under_restriction(f, n, i, assign)
    a0, a1 = dict(assign), dict(assign)
    a0[i], a1[i] = 0, 1
    q0, l0 = budget(f, n, left, a0, weight/2)
    q1, l1 = budget(f, n, right, a1, weight/2)
    return q+q0+q1, l0+l1

random.seed(20260920)
budget_cases = 0
for n in range(1, 6):
    for _ in range(200):
        f = [random.choice([-1,1]) for _ in range(1 << n)]
        tree = random_partial_tree(n, {})
        q, leaves = budget(f, n, tree)
        I = total_inf_restriction(f, n, {})
        if q + leaves != I:
            raise AssertionError(("budget failure", n, q, leaves, I))
        budget_cases += 1

h01 = -0.1*math.log2(0.1) - 0.9*math.log2(0.9)
out = {
    "status": "PASS",
    "symmetric_exhaustion": sym_summary,
    "global_symmetric_max_B_over_Inf_small_n": global_sym,
    "minimum_numeric_H_minus_sum_B": han_slack_min,
    "threshold_small_n": thr_summary,
    "threshold_global_max_B_over_Inf_small_n": thr_global,
    "candidate_threshold_constant_CONJECTURAL": 1.5 + 2.5*h01,
    "shifted_threshold_anf_power2_m": anf,
    "exact_partial_influence_budget_random_cases": budget_cases,
}
print(json.dumps(out, indent=2, sort_keys=True))
