#!/usr/bin/env python3
"""
Finite/exact support checks for B12's FEI random-prefix-loss / Palm-row report.

These checks support only the finite statements explicitly printed below.
They are not a proof of full FEI or of the analytic hypercontractive theorem.
"""
from fractions import Fraction
from math import comb, log2
import hashlib, json


def walsh_int(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def entropy(ps):
    return -sum(float(p)*log2(float(p)) for p in ps if p)


def spectral_data(vals, n):
    N = 1 << n
    W = walsh_int(vals)
    p = [Fraction(c*c, N*N) for c in W]
    return W, p


def shadow(p, n):
    N = 1 << n
    v = [Fraction(0,1) for _ in range(N)]
    for A in range(N):
        a = A.bit_count()
        for B in range(N):
            if p[B] and (B & A) == A:
                v[A] += p[B] / comb(B.bit_count(), a)
    return v


def log2_fact(k):
    out = 0.0
    for j in range(2, k+1):
        out += log2(j)
    return out


def loss_identity(vals, n):
    N = 1 << n
    _, p = spectral_data(vals, n)
    lam = sum(p[s]*s.bit_count() for s in range(N))
    if not lam:
        return None
    infl = [sum(p[s] for s in range(N) if (s>>i)&1) for i in range(n)]
    pi = [x/lam for x in infl]
    v = shadow(p, n)

    hxb = sum(float(p[s]*s.bit_count()/lam)*log2(s.bit_count())
              for s in range(1, N) if p[s])
    hxa = 0.0
    for A in range(N):
        mass = (v[A]-p[A])/lam
        if not mass:
            continue
        den = (A.bit_count()+1)*(v[A]-p[A])
        row = [v[A|(1<<i)]/den for i in range(n) if not ((A>>i)&1)]
        hxa += float(mass)*entropy(row)

    L = hxa-hxb
    G = sum(float(p[s]/lam)*(s.bit_count()*log2(s.bit_count())-
              log2_fact(s.bit_count())) for s in range(1, N) if p[s])
    Hpi = entropy(pi)
    Ixa = Hpi-hxa
    selector_over_I = Hpi-Ixa-sum(
        float(p[s]/lam)*log2_fact(s.bit_count()) for s in range(1, N) if p[s]
    )
    return L, G, selector_over_I, p


def exact_hypercontractive_half(p, n, i):
    """Check E[2^{-Z}|X=i]^3 <= Inf_i exactly (rho^2=1/2)."""
    N = 1 << n
    ji = sum(p[s] for s in range(N) if (s>>i)&1)
    if ji == 0:
        return True
    m = sum(p[s]*Fraction(1, 1 << (s.bit_count()-1))
            for s in range(N) if (s>>i)&1) / ji
    return m*m*m <= ji


def mean_prefix(p, n, i):
    N = 1 << n
    ji = sum(p[s] for s in range(N) if (s>>i)&1)
    if ji == 0:
        return None
    d = sum(p[s]*(s.bit_count()-1) for s in range(N) if (s>>i)&1)
    return d/(2*ji), ji


summary = {
    "schema_version": 1,
    "exhaustive_boolean_dimensions": [1,2,3,4],
    "functions_checked": 0,
    "coordinate_rows_checked": 0,
    "hypercontractive_exact_rows_checked": 0,
    "loss_identity_rows_checked": 0,
    "min_prefix_ratio_by_n": {},
    "max_terminal_prefix_loss_by_n": {},
    "one_point_exact_equalities": 0,
    "assertions": "PASS"
}

for n in range(1,5):
    N = 1 << n
    min_ratio = None
    max_L = None
    for mask in range(1 << N):
        vals = [1 if (mask>>x)&1 else -1 for x in range(N)]
        summary["functions_checked"] += 1
        dat = loss_identity(vals, n)
        if dat is None:
            continue
        L, G, sel, p = dat
        assert abs(sel-(L+G)) < 2e-11
        summary["loss_identity_rows_checked"] += 1
        max_L = L if max_L is None or L > max_L else max_L
        for i in range(n):
            mp = mean_prefix(p, n, i)
            if mp is None:
                continue
            meanA, ji = mp
            summary["coordinate_rows_checked"] += 1
            assert exact_hypercontractive_half(p, n, i)
            summary["hypercontractive_exact_rows_checked"] += 1
            jf = float(ji)
            if jf <= 0.5:
                rhs = 0.25*log2(1.0/jf)
                assert float(meanA)+1e-12 >= rhs
                if rhs > 0:
                    ratio = float(meanA)/log2(1.0/jf)
                    min_ratio = ratio if min_ratio is None or ratio < min_ratio else min_ratio
    summary["min_prefix_ratio_by_n"][str(n)] = None if min_ratio is None else round(min_ratio,15)
    summary["max_terminal_prefix_loss_by_n"][str(n)] = None if max_L is None else round(max_L,15)

# One-point Boolean function: +1 at one vertex, -1 elsewhere.
# For every coordinate: Inf_i=2^{1-n}, E(|A||X=i)=(n-1)/4 exactly.
for n in range(2,13):
    N = 1 << n
    vals = [1]+[-1]*(N-1)
    _, p = spectral_data(vals, n)
    for i in range(n):
        meanA, ji = mean_prefix(p, n, i)
        assert ji == Fraction(1, 1 << (n-1))
        assert meanA == Fraction(n-1, 4)
        summary["one_point_exact_equalities"] += 1

summary["loss_constant_lower_bound_from_current_FEI_ratio"] = round(
    6.521845710923046575-log2(2.71828182845904523536), 15
)
summary["addressing_asymptotic_loss_calibration"] = round(
    4-log2(2.71828182845904523536), 15
)
raw = json.dumps(summary, sort_keys=True, separators=(",", ":")).encode()
summary["result_digest_sha256"] = hashlib.sha256(raw).hexdigest()
print(json.dumps(summary, indent=2, sort_keys=True))
