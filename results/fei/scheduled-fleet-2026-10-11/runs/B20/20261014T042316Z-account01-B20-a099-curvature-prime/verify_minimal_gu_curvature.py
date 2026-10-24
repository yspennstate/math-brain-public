#!/usr/bin/env python3
"""High-precision finite audit of the tensor-prime GU curvature reduction."""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80
LN2 = Decimal(2).ln()


def restrict_table(table, n, i, bit):
    out = 0
    for y in range(1 << (n - 1)):
        lo = y & ((1 << i) - 1)
        hi = y >> i
        x = lo | (bit << i) | (hi << (i + 1))
        if (table >> x) & 1:
            out |= 1 << y
    return out


def walsh_numerators(table, n):
    N = 1 << n
    values = [1 if (table >> x) & 1 else -1 for x in range(N)]
    return [sum(v * (-1 if ((s & x).bit_count() & 1) else 1)
                for x, v in enumerate(values))
            for s in range(N)]


LOG2_INT = {k: Decimal(k).ln() / LN2 for k in range(1, 257)}


def log2_int(k):
    if k not in LOG2_INT:
        LOG2_INT[k] = Decimal(k).ln() / LN2
    return LOG2_INT[k]


def invariants(table, n):
    N = 1 << n
    den = N * N
    nums = walsh_numerators(table, n)
    sq = [x * x for x in nums]
    upper = sq[:]
    for i in range(n):
        for s in range(N):
            if not ((s >> i) & 1):
                upper[s] += upper[s | (1 << i)]
    u = Decimal(0)
    for x, y in zip(sq, upper):
        if x:
            u += (Decimal(x) / Decimal(den)) * (log2_int(y) - log2_int(x))
    inf = []
    for i in range(n):
        inf.append(Fraction(sum(sq[s] for s in range(N) if (s >> i) & 1), den))
    influence = sum((Fraction(s.bit_count() * sq[s], den) for s in range(N)), Fraction())
    return u, influence, inf, sq


def tensor_table(t1, n1, t2, n2):
    out = 0
    for x in range(1 << n1):
        a = 1 if (t1 >> x) & 1 else -1
        for y in range(1 << n2):
            b = 1 if (t2 >> y) & 1 else -1
            z = x | (y << n1)
            if a * b == 1:
                out |= 1 << z
    return out


def direct_G(table, n):
    u = invariants(table, n)[0]
    if n == 0:
        return Decimal(0)
    ans = Decimal(0)
    for i in range(n):
        ans += u - (invariants(restrict_table(table, n, i, 0), n - 1)[0]
                    + invariants(restrict_table(table, n, i, 1), n - 1)[0]) / 2
    return ans


def main():
    U = [[Decimal(0), Decimal(0)]]
    influences = [[[], []]]
    sqs = [[[], []]]
    for n in range(1, 5):
        count = 1 << (1 << n)
        un, pn, sn = [], [], []
        for table in range(count):
            u, _, p, sq = invariants(table, n)
            un.append(u)
            pn.append(p)
            sn.append(sq)
        U.append(un)
        influences.append(pn)
        sqs.append(sn)

    G = [[Decimal(0), Decimal(0)]]
    for n in range(1, 5):
        gn = []
        for table, u in enumerate(U[n]):
            total = Decimal(0)
            for i in range(n):
                c0 = restrict_table(table, n, i, 0)
                c1 = restrict_table(table, n, i, 1)
                total += u - (U[n - 1][c0] + U[n - 1][c1]) / 2
            gn.append(total)
        G.append(gn)

    cases = 0
    coordinate_tests = 0
    worst = Decimal('-Infinity')
    worst_data = None
    min_certified_margin = Decimal('Infinity')
    for n in range(1, 5):
        for table in range(1 << (1 << n)):
            ratios = []
            diffs = []
            for i, p in enumerate(influences[n][table]):
                if p == 0:
                    continue
                c0 = restrict_table(table, n, i, 0)
                c1 = restrict_table(table, n, i, 1)
                dG = G[n][table] - (G[n - 1][c0] + G[n - 1][c1]) / 2
                pd = Decimal(p.numerator) / Decimal(p.denominator)
                ratios.append(dG / pd)
                diffs.append(Decimal(14) * pd - dG)
                coordinate_tests += 1
            if ratios:
                best = min(ratios)
                margin = max(diffs)
                assert margin > Decimal('1e-20')
                if margin < min_certified_margin:
                    min_certified_margin = margin
                if best > worst:
                    worst = best
                    worst_data = (n, table)
            cases += 1

    gate = 6014
    ug, ig, pg, sq = invariants(gate, 4)
    gg = G[4][gate]
    assert sq == [16] * 16
    assert abs(ug - Decimal(2)) < Decimal('1e-70')
    assert ig == 2
    assert abs(gg - Decimal(11) / 2) < Decimal('1e-70')
    assert worst_data == (4, gate)
    assert abs(worst - Decimal(53) / 4) < Decimal('1e-70')

    for i in range(4):
        c0 = restrict_table(gate, 4, i, 0)
        c1 = restrict_table(gate, 4, i, 1)
        dU = U[4][gate] - (U[3][c0] + U[3][c1]) / 2
        dG = G[4][gate] - (G[3][c0] + G[3][c1]) / 2
        assert abs(dU - Decimal(11) / 8) < Decimal('1e-70')
        assert abs(dG - Decimal(53) / 8) < Decimal('1e-70')

    gate2 = tensor_table(gate, 4, gate, 4)
    u2, i2, _, _ = invariants(gate2, 8)
    g2 = direct_G(gate2, 8)
    assert abs(u2 - 4) < Decimal('1e-65')
    assert i2 == 4
    assert abs(g2 - 11) < Decimal('1e-65')

    print('MINIMAL_GU_CURVATURE_PASS')
    print('boolean_truth_tables', cases)
    print('relevant_coordinate_tests', coordinate_tests)
    print('worst_good_coordinate_ratio', worst)
    print('worst_gate_n_table', worst_data[0], worst_data[1])
    print('minimum_a14_margin', min_certified_margin)
    print('gate_U_I_G', ug, ig, gg)
    print('gate_tensor_square_U_I_G', u2, i2, g2)
    print('status PASS')


if __name__ == '__main__':
    main()
