#!/usr/bin/env python3
"""Exhaustive diagnostic for B11-A052-U-PERSISTENCE-v1 through n=4.

The analytic theorem is proved in RANDOM_RESTRICTION_U_PERSISTENCE.tex.
This script independently checks the full retained-terminal inequality for
every one-coordinate restriction of every descendant-critical Boolean table
through n=4, and the binomial random-restriction corollary for every maximizer
of H/I at t in {1/4,1/2,3/4,1}.
"""
from itertools import product
from math import log2, log

TOL = 2e-10


def walsh(vals):
    a = [float(x) for x in vals]
    n = (len(a)).bit_length() - 1
    for j in range(n):
        step = 1 << j
        for base in range(0, len(a), 2 * step):
            for k in range(step):
                x, y = a[base + k], a[base + k + step]
                a[base + k], a[base + k + step] = x + y, x - y
    scale = 1.0 / len(a)
    return [x * scale for x in a]


def stats(vals):
    n = len(vals).bit_length() - 1
    p = [x*x for x in walsh(vals)]
    h = sum(-x*log2(x) for x in p if x > 0)
    influence = sum(mask.bit_count()*p[mask] for mask in range(len(p)))
    pi = p[:]
    for j in range(n):
        for mask in range(len(p)):
            if not (mask >> j) & 1:
                pi[mask] += pi[mask | (1 << j)]
    u = sum(p[m]*log2(pi[m]/p[m]) for m in range(len(p)) if p[m] > 0)
    var = 1.0 - p[0]
    bias_mass = 1.0 - var
    b = bias_mass*log2(1.0/bias_mass) if 0.0 < bias_mass < 1.0 else 0.0
    return h, influence, u, var, b


def restrict(vals, live_mask, assignment):
    n = len(vals).bit_length() - 1
    live = [j for j in range(n) if (live_mask >> j) & 1]
    dead = [j for j in range(n) if not ((live_mask >> j) & 1)]
    out = []
    for y in range(1 << len(live)):
        x = 0
        for k, j in enumerate(live):
            x |= ((y >> k) & 1) << j
        for k, j in enumerate(dead):
            x |= ((assignment >> k) & 1) << j
        out.append(vals[x])
    return out


def all_restriction_ratios(vals):
    n = len(vals).bit_length() - 1
    ratios = []
    for live in range(1 << n):
        dead_count = n - live.bit_count()
        for z in range(1 << dead_count):
            h, i, *_ = stats(restrict(vals, live, z))
            if i > TOL:
                ratios.append(h/i)
    return ratios


def check():
    local_checks = 0
    critical_tables = 0
    maxima = {}
    maximizers = {}
    for n in range(1, 5):
        best = -1.0
        best_tables = []
        for code in range(1 << (1 << n)):
            vals = [1 if (code >> x) & 1 else -1 for x in range(1 << n)]
            h, i, u, var, b = stats(vals)
            if i <= TOL:
                continue
            r = h/i
            if r > best + TOL:
                best, best_tables = r, [vals]
            elif abs(r-best) <= TOL:
                best_tables.append(vals)

            ratios = all_restriction_ratios(vals)
            if max(ratios, default=0.0) > r + TOL:
                continue
            critical_tables += 1
            for j in range(n):
                live = ((1 << n)-1) ^ (1 << j)
                child_stats = [stats(restrict(vals, live, z)) for z in range(2)]
                ih = sum(s[0] for s in child_stats)/2
                ii = sum(s[1] for s in child_stats)/2
                iu = sum(s[2] for s in child_stats)/2
                iv = sum(s[3] for s in child_stats)/2
                ib = sum(s[4] for s in child_stats)/2
                delta = r*ii - ih
                rhs = (r-2)*ii/2 - delta/2 + iv + ib/2
                assert iu + TOL >= rhs, (n, code, j, iu, rhs)
                local_checks += 1
        maxima[n] = best
        maximizers[n] = best_tables

    random_checks = 0
    ts = (0.25, 0.5, 0.75, 1.0)
    for n, tables in maximizers.items():
        c = maxima[n]
        for vals in tables:
            _, root_i, *_ = stats(vals)
            for t in ts:
                eu = ed = ev = eb = ei = 0.0
                for live in range(1 << n):
                    k = live.bit_count()
                    prob_live = (t**k)*((1-t)**(n-k))
                    if prob_live == 0:
                        continue
                    dead_count = n-k
                    for z in range(1 << dead_count):
                        w = prob_live/(1 << dead_count)
                        h, i, u, var, b = stats(restrict(vals, live, z))
                        eu += w*u
                        ed += w*(c*i-h)
                        ev += w*var
                        eb += w*b
                        ei += w*i
                rhs_exact = (c-2)*ei/2 - ed/2 + ev + eb/2
                rhs_closed = ((c-2)*t/2-(1-t)/log(2))*root_i + ev + eb/2
                assert abs(ei-t*root_i) <= TOL
                assert eu + TOL >= rhs_exact
                assert eu + TOL >= rhs_closed
                random_checks += 1
    print(f"critical_tables={critical_tables}")
    print(f"local_full_terminal_checks={local_checks}")
    print(f"random_restriction_checks={random_checks}")
    print("max_ratios=" + ",".join(f"n{n}:{maxima[n]:.12f}" for n in maxima))
    print("status=PASS")


if __name__ == "__main__":
    check()

