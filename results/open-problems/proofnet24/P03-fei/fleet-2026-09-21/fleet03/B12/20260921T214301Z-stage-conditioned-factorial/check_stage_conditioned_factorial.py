#!/usr/bin/env python3
"""Diagnostics for B12 stage-conditioned Palm-prefix coding.

Standard library only.  This script checks:
  (i) exact-subcube rows U_F for 1 <= |F| <= 511 at Decimal precision 70;
  (ii) the two-cluster arbitrary-row obstruction;
  (iii) all nonzero ternary rows g:{0,1}^m->{-1,0,1}, m<=3, for the
        candidate C(nu_g) <= A(nu_g) + E_phys(g).

The Decimal run is high-precision numerical evidence, not interval arithmetic.
"""
from decimal import Decimal, getcontext
from math import comb, log2, lgamma, log
from itertools import product
from collections import Counter, defaultdict
import json

getcontext().prec = 70
LN2 = Decimal(2).ln()
LNFAC = [Decimal(0)]
for n in range(1, 514):
    LNFAC.append(LNFAC[-1] + Decimal(n).ln())


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def dh2(t, m):
    if t == 0 or t == m:
        return Decimal(0)
    td, md = Decimal(t), Decimal(m)
    u = md - td
    return (md.ln() - td / md * td.ln() - u / md * u.ln()) / LN2


def subcube_C(m):
    # For nu=U_[m], P|T=t is uniform on t-subsets and the tail weights
    # pair to 2/(m+1), yielding C_m=(m+1)^-1 sum_t TC(U_{m,t}).
    s = Decimal(0)
    for t in range(1, m):
        c = Decimal(m) * dh2(t, m) - (LNFAC[m] - LNFAC[t] - LNFAC[m-t]) / LN2
        s += c
    return s / Decimal(m + 1)


def subcube_A(m):
    # A_m=E_{R~Bin(m,1/2)} log2((R+1)!)/(R+1).
    den = Decimal(2) ** m
    s = Decimal(0)
    for r in range(m + 1):
        g = LNFAC[r + 1] / (Decimal(r + 1) * LN2)
        s += Decimal(comb(m, r)) / den * g
    return s


def two_cluster(k):
    # B is either of two disjoint k-sets, each with probability 1/2.
    C = 0.0
    for t in range(1, k + 1):
        tc = 2 * k * h2(t / (2 * k)) - 1.0 - log2(comb(k, t))
        C += tc / (k + 1)
    A = lgamma(k + 2) / log(2.0) / (k + 1)
    return C, A


def walsh(vals, m):
    N = 1 << m
    out = []
    for A in range(N):
        s = 0
        for x, v in enumerate(vals):
            s += v * (-1 if ((A & x).bit_count() & 1) else 1)
        out.append(s / N)
    return out


def palm(vals, m):
    j = sum(v * v for v in vals) / (1 << m)
    if j == 0:
        return None, 0.0
    h = walsh(vals, m)
    return [a * a / j for a in h], j


def prefix_tc(nu, m):
    # B~nu; conditionally choose T uniformly from 0..|B| and P uniformly
    # among the T-subsets of B.  Return TC(P|T).
    joint = [defaultdict(float) for _ in range(m + 1)]
    qt = [0.0] * (m + 1)
    for B, pb in enumerate(nu):
        if pb == 0.0:
            continue
        r = B.bit_count()
        for t in range(r + 1):
            wT = pb / (r + 1)
            subs = []
            sub = B
            while True:
                if sub.bit_count() == t:
                    subs.append(sub)
                if sub == 0:
                    break
                sub = (sub - 1) & B
            w = wT / len(subs)
            qt[t] += wT
            for P in subs:
                joint[t][P] += w
    ans = 0.0
    for t, q in enumerate(qt):
        if q <= 1e-15:
            continue
        probs = {P: w / q for P, w in joint[t].items()}
        H = -sum(p * log2(p) for p in probs.values() if p > 0.0)
        sum_marginal_H = 0.0
        for k in range(m):
            pk = sum(p for P, p in probs.items() if (P >> k) & 1)
            sum_marginal_H += h2(pk)
        ans += q * (sum_marginal_H - H)
    return ans


def factorial_share(nu):
    s = 0.0
    for B, p in enumerate(nu):
        r = B.bit_count()
        s += p * lgamma(r + 2) / log(2.0) / (r + 1)
    return s


def ephys(vals, m):
    support = [x for x, v in enumerate(vals) if v]
    N = len(support)
    if N == 0:
        return 0.0
    counts = Counter(vals[x] for x in support)
    Hsig = -sum((c / N) * log2(c / N) for c in counts.values())
    HXgiven = sum((c / N) * log2(c) for c in counts.values())
    cond = 0.0
    for r in range(m):
        groups = defaultdict(list)
        for x in support:
            groups[(x & ~(1 << r), vals[x])].append(x)
        for xs in groups.values():
            if len(xs) == 2:
                cond += len(xs) / N
    return Hsig + HXgiven - cond


def main():
    min_gap = Decimal(999)
    min_m = None
    selected = {}
    for m in range(1, 512):
        C, A = subcube_C(m), subcube_A(m)
        gap = A - C
        if gap < min_gap:
            min_gap, min_m = gap, m
        if m in {1,2,3,4,5,6,16,64,128,256,511}:
            selected[str(m)] = {"C": str(C), "A": str(A), "gap": str(gap)}

    clusters = {}
    for k in (8,16,32,64,128,256):
        C, A = two_cluster(k)
        clusters[str(k)] = {"C": C, "A": A, "excess": C-A}

    total = fail_CA = fail_CAE = 0
    max_excess = (-1.0, None)
    max_ratio = (-1.0, None)
    for m in range(1, 4):
        for vals in product((-1,0,1), repeat=1 << m):
            if all(v == 0 for v in vals):
                continue
            nu, j = palm(vals, m)
            C, A, E = prefix_tc(nu, m), factorial_share(nu), ephys(vals, m)
            total += 1
            excess = C-A
            if excess > 1e-10:
                fail_CA += 1
            if C > A+E+1e-9:
                fail_CAE += 1
            if excess > max_excess[0]:
                max_excess = (excess, [m, list(vals), C, A, E, j])
            if E > 1e-12 and excess/E > max_ratio[0]:
                max_ratio = (excess/E, [m, list(vals), C, A, E, j])

    print(json.dumps({
        "exact_subcube_decimal_precision": 70,
        "exact_subcube_checked_m": [1,511],
        "exact_subcube_min_gap_A_minus_C": str(min_gap),
        "exact_subcube_min_gap_m": min_m,
        "selected_exact_subcube": selected,
        "two_cluster_obstruction": clusters,
        "ternary_rows_checked": total,
        "ternary_C_gt_A": fail_CA,
        "ternary_C_gt_A_plus_Ephys": fail_CAE,
        "max_ternary_C_minus_A": max_excess,
        "max_ternary_ratio_excess_over_Ephys": max_ratio,
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
