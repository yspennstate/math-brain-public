#!/usr/bin/env python3
"""Exact checker for B16 paired-Shapley double-resolvent transport.

This is a finite falsification checker for the algebraic transport theorem in the
companion report. It does NOT test FEI and it does not treat finite verification
as a universal proof.

Checks:
1. Direct fine/coarse Shapley values for deterministic rational games on
   2, 3 and 4 clone pairs equal the divergence of the proposed signed flow.
2. The genuine pair-thinning law reproduces the claimed third-difference
   generating polynomial at exact rational (x,y) points.
3. Every single-dividend type through s=50 obeys the exact energy identity and
   the sharp 1/(8 s^2) current-energy bound.
4. Records the s=30,r=10 obstruction showing that omitting the pair-support
   resolvent overpays current energy by s^2=900.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def touched_info(mask, m):
    s = r = 0
    for j in range(m):
        cnt = ((mask >> (2*j)) & 1) + ((mask >> (2*j+1)) & 1)
        if cnt:
            s += 1
            if cnt == 2:
                r += 1
    return s, r


def deterministic_dividends(m):
    d = {}
    for T in range(1, 1 << (2*m)):
        z = ((T*37 + T.bit_count()*11 + 5) % 19) - 9
        if z:
            d[T] = Fraction(z, 7)
    return d


def game_values_from_dividends(d, n):
    V = [Fraction(0) for _ in range(1 << n)]
    for S in range(1 << n):
        total = Fraction(0)
        T = S
        while True:
            total += d.get(T, Fraction(0))
            if T == 0:
                break
            T = (T - 1) & S
        V[S] = total
    return V


def shapley_values(V, n):
    fact = [factorial(i) for i in range(n+1)]
    out = []
    for i in range(n):
        bit = 1 << i
        val = Fraction(0)
        for S in range(1 << n):
            if S & bit:
                continue
            k = S.bit_count()
            wt = Fraction(fact[k] * fact[n-k-1], fact[n])
            val += wt * (V[S | bit] - V[S])
        out.append(val)
    return out


def coarse_game(V, m):
    W = []
    for B in range(1 << m):
        S = 0
        for j in range(m):
            if (B >> j) & 1:
                S |= (1 << (2*j)) | (1 << (2*j+1))
        W.append(V[S])
    return W


def flow_from_dividends(d, m):
    F = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for T, value in d.items():
        s, _ = touched_info(T, m)
        k = T.bit_count()
        doubled, single = [], []
        for j in range(m):
            cnt = ((T >> (2*j)) & 1) + ((T >> (2*j+1)) & 1)
            if cnt == 2:
                doubled.append(j)
            elif cnt == 1:
                single.append(j)
        if not doubled or not single:
            continue
        amount = value / (s * k)
        for a in doubled:
            for b in single:
                F[a][b] += amount
                F[b][a] -= amount
    div = [sum(F[a][b] for b in range(m)) for a in range(m)]
    return F, div


def finite_difference(V, R, base_bits):
    base = 0
    for b in base_bits:
        base |= 1 << b
    k = len(base_bits)
    total = Fraction(0)
    A = base
    while True:
        sign = -1 if ((k - A.bit_count()) & 1) else 1
        total += sign * V[R | A]
        if A == 0:
            break
        A = (A - 1) & base
    return total


def q_direct(V, m, a, b, x, y):
    # Pair law: 11=xy^2, 10=01=xy(1-y), 00=1-2xy+xy^2.
    local = [
        (0, Fraction(1) - 2*x*y + x*y*y),
        (1, x*y*(1-y)),
        (2, x*y*(1-y)),
        (3, x*y*y),
    ]
    others = [j for j in range(m) if j not in (a, b)]
    exp_sum = Fraction(0)
    for states in product(local, repeat=len(others)):
        prob = Fraction(1)
        R = 0
        for j, (state, p) in zip(others, states):
            prob *= p
            if state & 1:
                R |= 1 << (2*j)
            if state & 2:
                R |= 1 << (2*j+1)
        if not prob:
            continue
        for eps in (0, 1):
            base = [2*a, 2*a+1, 2*b+eps]
            exp_sum += prob * finite_difference(V, R, base)
    return x*y*y*exp_sum


def q_coeff(d, m, a, b, x, y):
    total = Fraction(0)
    for T, value in d.items():
        ca = ((T >> (2*a)) & 1) + ((T >> (2*a+1)) & 1)
        cb = ((T >> (2*b)) & 1) + ((T >> (2*b+1)) & 1)
        if ca == 2 and cb == 1:
            s, _ = touched_info(T, m)
            k = T.bit_count()
            total += value * x**(s-1) * y**(k-1)
    return total


def main():
    direct_cases = 0
    thinning_checks = 0
    sample_points = [
        (Fraction(1, 3), Fraction(2, 5)),
        (Fraction(3, 4), Fraction(1, 2)),
        (Fraction(1, 1), Fraction(2, 3)),
    ]

    for m in (2, 3, 4):
        d = deterministic_dividends(m)
        V = game_values_from_dividends(d, 2*m)

        fine = shapley_values(V, 2*m)
        fine_pair = [fine[2*j] + fine[2*j+1] for j in range(m)]
        coarse = shapley_values(coarse_game(V, m), m)
        defect = [fine_pair[j] - coarse[j] for j in range(m)]
        _, div = flow_from_dividends(d, m)
        assert defect == div
        assert sum(defect) == 0
        direct_cases += 1

        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                for x, y in sample_points:
                    assert q_direct(V, m, a, b, x, y) == q_coeff(
                        d, m, a, b, x, y
                    )
                    thinning_checks += 1

    energy_cases = 0
    sharp_pairs = []
    for s in range(2, 51):
        for r in range(1, s):
            k = s + r
            w_d = Fraction(s-r, s*k)
            w_s = Fraction(-r, s*k)
            defect_energy = r*w_d*w_d + (s-r)*w_s*w_s
            flow_energy = Fraction(r*(s-r), s*s*k*k)
            assert defect_energy == s*flow_energy
            assert flow_energy <= Fraction(1, 8*s*s)
            if flow_energy == Fraction(1, 8*s*s):
                sharp_pairs.append((s, r))
            energy_cases += 1

    s, r = 30, 10
    k = s + r
    exact_edge = Fraction(1, s*k)
    single_resolvent_edge = Fraction(1, k)
    exact_energy = Fraction(r*(s-r), s*s*k*k)
    single_resolvent_energy = Fraction(r*(s-r), k*k)
    assert single_resolvent_energy / exact_energy == s*s

    print(f"direct_fine_coarse_shapley_games={direct_cases} all_passed=true")
    print(f"exact_pair_thinning_generating_checks={thinning_checks} all_passed=true")
    print(f"single_dividend_energy_types={energy_cases} all_passed=true")
    print("sharp_scaled_current_energy=1/8")
    print(f"sharp_types_through_s50={len(sharp_pairs)} first={sharp_pairs[0]} last={sharp_pairs[-1]}")
    print("dead_single_resolvent_example_s=30_r=10")
    print(f"  exact_edge_current={exact_edge}")
    print(f"  single_resolvent_edge_current={single_resolvent_edge}")
    print(f"  exact_total_current_energy={exact_energy}")
    print(f"  single_resolvent_total_current_energy={single_resolvent_energy}")
    print(f"  energy_overpay_factor={single_resolvent_energy/exact_energy}")
    print("FULL_FEI_STATUS=OPEN_NOT_PROVED")


if __name__ == "__main__":
    main()
