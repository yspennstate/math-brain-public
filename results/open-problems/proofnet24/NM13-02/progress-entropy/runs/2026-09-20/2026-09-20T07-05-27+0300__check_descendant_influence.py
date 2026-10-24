#!/usr/bin/env python3
import json, math
from fractions import Fraction
from functools import lru_cache

A = 1.0 / math.log(2.0)
TOL = 5e-11

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1.0-p)*math.log2(1.0-p)

def fwht(vals):
    a = [float(x) for x in vals]
    N = len(a)
    h = 1
    while h < N:
        for i in range(0, N, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    inv = 1.0/N
    return tuple(x*inv for x in a)

@lru_cache(None)
def metrics(vals):
    p = tuple(x*x for x in fwht(vals))
    n = len(vals).bit_length()-1
    infl = tuple(
        sum(q for s, q in enumerate(p) if (s >> i) & 1)
        for i in range(n)
    )
    return p, infl, sum(infl)

@lru_cache(None)
def restrict(vals, i, bit):
    n = len(vals).bit_length()-1
    out = []
    for m in range(1 << (n-1)):
        low = m & ((1 << i)-1)
        high = m >> i
        full = low | (bit << i) | (high << (i+1))
        out.append(vals[full])
    return tuple(out)

def B_i(vals, i):
    p = metrics(vals)[0]
    out = 0.0
    for s in range(len(p)):
        if ((s >> i) & 1) == 0:
            x, y = p[s], p[s | (1 << i)]
            q = x+y
            if q:
                out += q*h2(y/q)
    return out

def derivative_from_children(g, h):
    return tuple(a*b for a, b in zip(g, h))

stats = {
    "status": "PASS",
    "constant_1_over_ln2": A,
    "exhaustive_coordinate_cases": 0,
    "by_dimension": {},
    "max_child_budget_violation": -1e100,
    "max_derivative_triangle_violation": -1e100,
    "max_curvature_step_violation": -1e100,
}

# Exhaust every Boolean truth table through n=4.
for n in range(1, 5):
    N = 1 << n
    cases = 0
    for mask in range(1 << N):
        vals = tuple(-1 if (mask >> x) & 1 else 1 for x in range(N))
        p, infs, Itot = metrics(vals)
        for i in range(n):
            g, h = restrict(vals, i, 0), restrict(vals, i, 1)
            Ig, Ih = metrics(g)[2], metrics(h)[2]
            D = derivative_from_children(g, h)
            ID = metrics(D)[2] if len(D) > 1 else 0.0
            inf = infs[i]
            j = min(inf, 1.0-inf)
            B = B_i(vals, i)

            stats["max_derivative_triangle_violation"] = max(
                stats["max_derivative_triangle_violation"],
                ID - (Ig + Ih),
            )
            stats["max_curvature_step_violation"] = max(
                stats["max_curvature_step_violation"],
                B - (0.5*ID + A*j),
            )
            stats["max_child_budget_violation"] = max(
                stats["max_child_budget_violation"],
                B - (0.5*(Ig+Ih) + A*j),
            )
            cases += 1
    stats["by_dimension"][str(n)] = cases
    stats["exhaustive_coordinate_cases"] += cases

# Analytic stress family:
# F_r(x0,y)=(-1)^{x0 * sum_{s=1}^r y_{2s-1} y_{2s}}.
# Query x0. The minus child is constant and the plus child is a
# quadratic phase of polar rank 2r and total influence r.
star = []
for r in range(1, 17):
    alpha = Fraction((1 << r)-1, 1 << (r+1))  # (1-2^{-r})/2
    Iq = Fraction(r, 1)
    Iroot = Fraction(r, 2) + alpha
    ratio = Iq / alpha
    upper = A*float(alpha) + float(r)  # local child budget plus weighted quadratic leaf allocation
    slack = 2.0*float(Iroot) - upper
    star.append({
        "r": r,
        "query_influence_exact": f"{alpha.numerator}/{alpha.denominator}",
        "quadratic_child_influence_exact": str(r),
        "root_influence_exact": f"{Iroot.numerator}/{Iroot.denominator}",
        "curvature_over_query_charge_exact": f"{ratio.numerator}/{ratio.denominator}",
        "curvature_over_query_charge_float": float(ratio),
        "hereditary_upper_from_child_budget_float": upper,
        "hereditary_upper_over_root_influence_float": upper/float(Iroot),
        "two_I_slack_float": slack,
    })
    if slack < -TOL:
        stats["status"] = "FAIL"

stats["star_cubic_analytic"] = star

for key in (
    "max_child_budget_violation",
    "max_derivative_triangle_violation",
    "max_curvature_step_violation",
):
    if stats[key] > TOL:
        stats["status"] = "FAIL"

print(json.dumps(stats, indent=2, sort_keys=True))
