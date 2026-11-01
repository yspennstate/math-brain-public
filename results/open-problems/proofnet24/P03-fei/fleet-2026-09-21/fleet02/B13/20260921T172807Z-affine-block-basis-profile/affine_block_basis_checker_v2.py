#!/usr/bin/env python3
"""Exact self-checks for B13 affine block-basis FEI reduction.

Standard library only. Exhausts Boolean functions modulo global output sign for n<=4.
All structural checks use fractions/integers; floating point is used only for printed
diagnostics of the bent family and the current C0 threshold.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

def rank(vectors, n):
    piv = [0] * n
    r = 0
    for x in vectors:
        y = x
        while y:
            j = y.bit_length() - 1
            if piv[j]:
                y ^= piv[j]
            else:
                piv[j] = y
                r += 1
                break
    return r

def greedy(cost, n):
    basis = []
    picked = []
    for u, w in sorted(cost.items(), key=lambda kv: (kv[1], kv[0])):
        if rank(basis + [u], n) > len(basis):
            basis.append(u)
            picked.append((u, w))
            if len(basis) == n:
                break
    return sum((w for _, w in picked), Fraction(0)), picked

def rank_integral(cost, n):
    levels = sorted(set([Fraction(0), Fraction(1,2)] + list(cost.values())))
    total = Fraction(0)
    for a, b in zip(levels, levels[1:]):
        r = rank([u for u, w in cost.items() if w <= a], n)
        total += (b - a) * (n - r)
    return total

def fwht_int(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

counts = {
    "functions": 0,
    "affine_correlation_formula": 0,
    "rank_integral_formula": 0,
    "basis_exchange_inequalities": 0,
    "collision_lower_bound": 0,
}

for n in range(1, 5):
    N = 1 << n
    # Fix f(0)=+1 to quotient the irrelevant global output sign.
    for mask in range(1 << (N-1)):
        f = [1] + [1 if (mask >> (x-1)) & 1 else -1 for x in range(1, N)]

        cost = {}
        corr_abs = {}
        for u in range(1, N):
            disagreements = sum(f[x] != f[x ^ u] for x in range(N))
            q = Fraction(disagreements, N)
            cost[u] = min(q, 1-q)
            corr_abs[u] = abs(Fraction(N - 2*disagreements, N))

        I_aff, picked = greedy(cost, n)
        counts["functions"] += 1

        # I_aff = 1/2 (n - max_basis sum |c_u|).
        corr_formula = Fraction(n, 2) - sum(
            (corr_abs[u] for u, _ in picked), Fraction(0)
        ) / 2
        assert I_aff == corr_formula
        counts["affine_correlation_formula"] += 1

        # I_aff = integral_0^{1/2} (n-rank{u:q_tilde(u)<=t}) dt.
        assert I_aff == rank_integral(cost, n)
        counts["rank_integral_formula"] += 1

        # Every chosen basis element is cheapest in its fundamental coset.
        us = [u for u, _ in picked]
        for i, u in enumerate(us):
            others = us[:i] + us[i+1:]
            span = {0}
            for v in others:
                span |= {x ^ v for x in tuple(span)}
            for v in span:
                assert cost[u ^ v] >= cost[u]
                counts["basis_exchange_inequalities"] += 1

        # Quotient-sharp Parseval/collision bound.  Zero-cost translations
        # are exact spectral periods; contract their span before applying
        # Cauchy-Schwarz.  If d is the essential affine spectral dimension,
        # D_d = 2^d sum mu^2 - 1 and
        # I_aff >= (d - sqrt(d D_d))/2.
        wh = fwht_int(f)
        mu = [Fraction(w*w, N*N) for w in wh]
        collision = sum((p*p for p in mu), Fraction(0))
        zero_rank = rank([u for u, w in cost.items() if w == 0], n)
        d = n - zero_rank
        D_d = (1 << d) * collision - 1
        assert D_d >= 0
        if 2*I_aff <= d:
            # Exact squared form; both sides are nonnegative.
            assert (Fraction(d) - 2*I_aff) ** 2 <= Fraction(d) * D_d
        counts["collision_lower_bound"] += 1

print("EXACT PASS")
for k, v in counts.items():
    print(f"{k}={v}")
print("total_exact_checks=" + str(sum(counts.values())))

# Current unrestricted lower-bound scale from TASKS_2026-09-21.md.
getcontext().prec = 50
C0 = Decimal("6.521845710923046575")
alpha = Decimal(1) - Decimal(2) / C0
threshold = alpha * alpha
print("C0=" + str(C0))
print("alpha_C0=1-2/C0=" + str(alpha))
print("collision_excess_threshold_per_dimension=" + str(threshold))

# Quadratic bent family on even n:
# f(x)=(-1)^{x1 x2 + x3 x4 + ...}. Its spectral law is uniform.
for n in (2, 4, 6, 8, 10, 20):
    r_shell = Decimal(2) ** Decimal(1-n)
    print(
        f"bent_n={n} H={n} I_aff={Decimal(n)/2} "
        f"H_over_I_aff=2 first_shell_ratio={r_shell}"
    )
