#!/usr/bin/env python3
"""Exact certificates for C047's inertia-sensitive Fisher budget.

Python standard library only.  All matrices, atom derivatives, Fisher terms,
and logarithm enclosures are rational.  The finite examples verify the full
entropy identity and retained positive frozen curvature, not the universal
analytic theorem (which is proved in agents/C047.md).
"""
from fractions import Fraction as F
from math import exp, sqrt
from pathlib import Path
import json


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(ar, bc)), F(0)) for bc in bt]
            for ar in a]


def diag(xs):
    return [[x if i == j else F(0) for j in range(len(xs))]
            for i, x in enumerate(xs)]


def outer(v):
    return [[x * y for y in v] for x in v]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def det(a):
    a = [row[:] for row in a]
    n = len(a)
    ans = F(1)
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        v = a[j][j]
        ans *= v
        for k in range(j + 1, n):
            if a[k][j]:
                c = a[k][j] / v
                for l in range(j + 1, n):
                    a[k][l] -= c * a[j][l]
    return ans


def inverse(a):
    n = len(a)
    a = [row[:] + erow for row, erow in zip(a, eye(n))]
    for j in range(n):
        pivot = next(k for k in range(j, n) if a[k][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
        v = a[j][j]
        a[j] = [x / v for x in a[j]]
        for k in range(n):
            if k != j and a[k][j]:
                c = a[k][j]
                a[k] = [x - c * y for x, y in zip(a[k], a[j])]
    return [row[n:] for row in a]


def ldlt_inertia(a):
    """Exact symmetric elimination; chosen examples have nonzero pivots."""
    a = [row[:] for row in a]
    signs = []
    for j in range(len(a)):
        v = a[j][j]
        assert v
        signs.append(1 if v > 0 else -1)
        for k in range(j + 1, len(a)):
            for l in range(k, len(a)):
                a[k][l] -= a[k][j] * a[l][j] / v
                a[l][k] = a[k][l]
    return [signs.count(1), signs.count(-1), 0]


LOG_GRID = 10**35


def log_series_unit(x, terms=50):
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    term = z
    total = F(0)
    for j in range(terms):
        total += 2 * term / (2*j + 1)
        term *= z*z
    tail = 2 * term / ((2*terms + 1) * (1 - z*z))
    return total, total + tail


LOG2 = log_series_unit(F(2))


def log_bounds(x):
    assert x > 0
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = log_series_unit(x)
    if k >= 0:
        lo += k * LOG2[0]
        hi += k * LOG2[1]
    else:
        lo += k * LOG2[1]
        hi += k * LOG2[0]
    # Outward rounding makes later sums inexpensive while keeping exact bounds.
    lo = F((lo * LOG_GRID).__floor__(), LOG_GRID)
    hi = F((hi * LOG_GRID).__ceil__(), LOG_GRID)
    return lo, hi


def int_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def int_scale(c, a):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, (tuple, list)):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def interval_json(x):
    return {"lower": str(x[0]), "upper": str(x[1]),
            "decimal_midpoint": float((x[0] + x[1])/2)}


def dense_congruence_direction(n, eigen_signature):
    v = eye(n)
    for i in range(1, n):
        v[i][i-1] = F(1, 20)
    a = mul(mul(v, diag(eigen_signature)), transpose(v))
    return a, v


def example(name, weights, sign, a, inertia, construction):
    n = len(weights)
    total = sum(weights, F(0))
    assert sign == 1 or total < 1
    l = add(diag([1/w for w in weights]), scale(F(sign), outer([F(1)]*n)))
    normalization = det(add(eye(n), l))
    k = add(eye(n), scale(F(-1), inverse(add(eye(n), l))))
    kappa = 1 + total if sign == 1 else 1/(1-total)
    budget_argument = (kappa + 1)**2/(4*kappa)
    budget = log_bounds(budget_argument)
    m = max(inertia[:2])
    gamma = F(m-1, m)
    c = int_add((F(1), F(1)), int_scale(-gamma, budget))
    assert c[0] > 0
    atoms = []
    fisher = F(0)
    frozen = (F(0), F(0))
    sums = [F(0), F(0), F(0)]
    for mask in range(1 << n):
        subset = [i for i in range(n) if mask >> i & 1]
        ls = [[l[i][j] for j in subset] for i in subset]
        p = det(ls)/normalization
        # Matrix determinant lemma gives an independent exact atom formula.
        factor = F(1)
        for i in subset:
            factor /= weights[i]
        factor *= 1 + sign * sum((weights[i] for i in subset), F(0))
        assert p == factor/normalization and p > 0
        qmat = [row[:] for row in k]
        for i in range(n):
            if not mask >> i & 1:
                qmat[i][i] -= 1
        assert ((-1)**(n-len(subset))) * det(qmat) == p
        rmat = mul(inverse(qmat), a)
        d1 = p * trace(rmat)
        d2 = p * (trace(rmat)**2 - trace(mul(rmat, rmat)))
        fisher += d1*d1/p
        frozen = int_add(frozen, int_scale(-d2, log_bounds(p)))
        sums[0] += p
        sums[1] += d1
        sums[2] += d2
        atoms.append({"subset": subset, "p": p, "p_prime": d1, "p_second": d2})
    assert sums == [F(1), F(0), F(0)]
    hessian = int_add(frozen, (-fisher, -fisher))
    margin = int_add(int_scale(gamma*fisher, budget), int_scale(F(-1), frozen))
    assert frozen[0] > 0, (name, "no positive frozen curvature", frozen)
    assert hessian[1] < 0 and margin[0] > 0
    return {
        "name": name, "n": n, "sign": sign, "weights": weights,
        "L": l, "K": k, "direction": a, "inertia": inertia,
        "inertia_construction": construction, "kappa": kappa,
        "budget_log_argument": budget_argument,
        "budget": interval_json(budget),
        "fisher_coefficient": interval_json(c),
        "FI": fisher, "FI_decimal": float(fisher),
        "positive_frozen_curvature": interval_json(frozen),
        "negative_entropy_curvature": interval_json(hessian),
        "proved_bound_margin": interval_json(margin),
        "atom_sum_checks": sums, "atoms": atoms,
    }


def convex_segment():
    u = list(map(F, [1, 2, 1, 1, 2, 1]))
    n = len(u)
    delta = F(1, 4)
    norm2 = sum((v*v for v in u), F(0))
    cap = 7*delta/(9*norm2)
    c0 = [F(1,4), F(1,3), F(2,5), F(3,5), F(2,3), F(3,4)]
    c1 = list(reversed(c0))
    k0 = add(diag(c0), scale(cap, outer(u)))
    k1 = add(diag(c1), scale(-cap, outer(u)))
    direction = add(k1, scale(F(-1), k0))
    dinv_moment = sum((u[i]*u[i]/(c1[i]-c0[i]) for i in range(n)), F(0))
    assert dinv_moment == 0
    assert ldlt_inertia(direction) == [3, 3, 0]
    samples = []
    for t in [F(0), F(1,4), F(1,2), F(3,4), F(1)]:
        c = [(1-t)*x+t*y for x,y in zip(c0,c1)]
        tau = cap*(1-2*t)
        r = sum((u[i]**2/c[i] for i in range(n)), F(0))
        s = sum((u[i]**2/(1-c[i]) for i in range(n)), F(0))
        assert 1+tau*r > 0 and 1-tau*s > 0
        ratio = (1+tau*r)/(1-tau*s)
        kappa = max(ratio, 1/ratio)
        assert kappa <= 8
        kmat = add(diag(c), scale(tau, outer(u)))
        odds = add(inverse(add(eye(n), scale(F(-1), kmat))), scale(F(-1), eye(n)))
        b = [u[i]/(1-c[i]) for i in range(n)]
        expected_odds = add(diag([x/(1-x) for x in c]), scale(tau/(1-tau*s), outer(b)))
        assert odds == expected_odds
        samples.append({"t": t, "tau": tau, "kappa": kappa})
    return {"u": u, "delta": delta, "tau_cap": cap, "c0": c0, "c1": c1,
            "K0": k0, "K1": k1, "direction": direction,
            "direction_inertia": [3,3,0], "inverse_diagonal_moment": dinv_moment,
            "exact_odds_formula_samples": samples}


def main():
    w = [F(2),F(1),F(3,2),F(1,2),F(3,4),F(5,4)]
    afull, v = dense_congruence_direction(6, [F(1)]*3+[F(-1,100)]*3)
    assert ldlt_inertia(afull) == [3,3,0]
    apsd, vp = dense_congruence_direction(6, [F(1)]*6)
    assert ldlt_inertia(apsd) == [6,0,0]
    u = [[F(1),F(0),F(0)], [F(0),F(1),F(0)], [F(0),F(0),F(1)],
         [F(1,10),F(1,20),F(1,30)],
         [F(1,20),F(-1,10),F(1,40)],
         [F(1,30),F(1,50),F(-1,20)]]
    rank3 = mul(mul(u,diag([F(1),F(1),F(-1,1000)])),transpose(u))
    examples = [
        example("positive_odds_full_rank_indefinite_kappa8", w, 1, afull, [3,3,0],
                {"V": v, "diagonal": [F(1)]*3+[F(-1,100)]*3}),
        example("positive_odds_full_rank_positive_kappa8", w, 1, apsd, [6,0,0],
                {"V": vp, "diagonal": [F(1)]*6}),
        example("negative_odds_full_rank_indefinite_kappa8", [x/8 for x in w], -1,
                afull, [3,3,0], {"V": v, "diagonal": [F(1)]*3+[F(-1,100)]*3}),
        example("positive_odds_rank3_indefinite_kappa25", list(map(F,[3,4,2,5,6,4])), 1,
                rank3, [2,1,3], {"U":u, "diagonal":[F(1),F(1),F(-1,1000)]}),
    ]
    # The exact general variance-range identity at assorted rational endpoints.
    variance_checks = 0
    for values, probabilities in [([F(1),F(2),F(4)], [F(1,5),F(1,2),F(3,10)]),
                                 ([F(1,4),F(1,2),F(1)], [F(1,3)]*3)]:
        mean = sum((x*p for x,p in zip(values, probabilities)), F(0))
        second = sum((x*x*p for x,p in zip(values, probabilities)), F(0))
        lo, hi = min(values), max(values)
        root = F(2) if lo == 1 else F(1,2)
        assert root*root == lo*hi
        gap = lo+hi-2*root - (second-mean*mean)/mean
        exact_squares = (sum(((x-lo)*(hi-x)*p for x,p in zip(values,probabilities)), F(0))
                         +(mean-root)**2)/mean
        assert gap == exact_squares and gap >= 0
        variance_checks += 1
    certificate = {"status":"PASS", "examples":examples,
                   "convex_segment":convex_segment(), "variance_identity_checks":variance_checks,
                   "note":"Universal theorem is analytic; these are exact corroborating certificates."}
    out = Path(__file__).with_name("certificate.json")
    out.write_text(json.dumps(encode(certificate), indent=2)+"\n")
    summary = {
        "status":"PASS: 256 exact atoms with first/second derivatives; 4 positive frozen curvatures compensated by Fisher; 5 exact odds-transform checks; convex rank-six indefinite segment",
        "examples":[{k:e[k] for k in ["name","inertia","kappa","FI_decimal",
                    "positive_frozen_curvature","negative_entropy_curvature","proved_bound_margin"]}
                    for e in examples],
        "thresholds_approximate_only":{
            str(m):(sqrt(exp(m/(m-1)))+sqrt(exp(m/(m-1))-1))**2
            for m in [2,3,6,20]},
        "dimension_uniform_threshold_approximate_only":(sqrt(exp(1))+sqrt(exp(1)-1))**2,
    }
    Path(__file__).with_name("verified_output.json").write_text(json.dumps(encode(summary),indent=2)+"\n")
    print(json.dumps(encode(summary),indent=2))


if __name__ == "__main__":
    main()
