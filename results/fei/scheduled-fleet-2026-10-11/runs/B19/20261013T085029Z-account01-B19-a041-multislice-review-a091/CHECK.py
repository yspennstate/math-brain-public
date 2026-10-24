#!/usr/bin/env python3
"""Independent exact-algebra audit of A041's two-weight slice ledgers.

No A041 implementation is imported.  Fourier coefficient squares and all
deficit/covariance identities use Fraction arithmetic.  Decimal logarithms
are used only to corroborate the analytically proved entropy bound.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
import json

getcontext().prec = 80


def assignments(n):
    return range(1 << n)


def bit(x, i):
    return (x >> i) & 1


def prob_out(x, biases, S):
    out = Fraction(1)
    for i, p in enumerate(biases):
        if i in S:
            continue
        out *= p if bit(x, i) else 1 - p
    return out


def amp_r_q(table, biases, S):
    """Return r,q with fhat(S)=sqrt(r)*q and r,q rational."""
    S = frozenset(S)
    r = Fraction(1)
    for i in S:
        r *= biases[i] * (1 - biases[i])
    q = Fraction(0)
    for x in assignments(len(biases)):
        sign = 1
        for i in S:
            sign *= 1 if bit(x, i) else -1
        q += table[x] * prob_out(x, biases, S) * sign
    return r, q


def spectrum(table, biases):
    n = len(biases)
    out = {}
    for mask in assignments(n):
        S = frozenset(i for i in range(n) if bit(mask, i))
        r, q = amp_r_q(table, biases, S)
        out[S] = r * q * q
    assert sum(out.values(), Fraction(0)) == 1
    return out


def vS(biases, S):
    z = Fraction(1)
    for i in S:
        z *= 4 * biases[i] * (1 - biases[i])
    return z


def metrics(table, biases):
    P = spectrum(table, biases)
    empty = P[frozenset()]
    var = 1 - empty
    infl = sum(Fraction(len(S)) * m for S, m in P.items())
    delta = infl - var
    e2 = Decimal(0)
    for S, m in P.items():
        if len(S) < 2 or not m:
            continue
        cap = vS(biases, S)
        assert m <= cap
        ratio = Decimal(cap.numerator) * Decimal(m.denominator) / (
            Decimal(cap.denominator) * Decimal(m.numerator)
        )
        dm = Decimal(m.numerator) / Decimal(m.denominator)
        e2 += dm * ratio.ln()
    return P, var, infl, delta, e2


def threshold_table(weights, threshold):
    n = len(weights)
    return [
        1 if sum(weights[i] * bit(x, i) for i in range(n)) >= threshold else -1
        for x in assignments(n)
    ]


def restrict_first(table, xval):
    n = (len(table)).bit_length() - 1
    return [table[(y << 1) | xval] for y in assignments(n - 1)]


def inner(table0, table1, biases, weight):
    total = Fraction(0)
    n = len(biases)
    for mask in assignments(n):
        S = frozenset(i for i in range(n) if bit(mask, i))
        if not S:
            continue
        r, q0 = amp_r_q(table0, biases, S)
        _, q1 = amp_r_q(table1, biases, S)
        total += weight(len(S)) * r * q0 * q1
    return total


def mean(table, biases):
    return amp_r_q(table, biases, frozenset())[1]


def distinct_slices(weights_A, biases_A, nB, threshold):
    cells = {}
    for a in assignments(len(weights_A)):
        score = sum(weights_A[i] * bit(a, i) for i in range(len(weights_A)))
        f = tuple(threshold_table([Fraction(1)] * nB, threshold - score))
        pa = Fraction(1)
        for i, p in enumerate(biases_A):
            pa *= p if bit(a, i) else 1 - p
        cells[f] = cells.get(f, Fraction(0)) + pa
    return [(list(f), pi) for f, pi in cells.items()]


def check_one_exceptional():
    cases = 0
    max_ratio = Decimal(0)
    max_fixture = None
    ln2 = Decimal(2).ln()
    ee = Decimal(1).exp()
    c = Decimal(460) + Decimal(80) * ln2
    K = Decimal(4) * c + Decimal(12) + Decimal(4) / ee
    profiles = [
        [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(3, 5)],
        [Fraction(1, 5), Fraction(1, 4), Fraction(2, 3), Fraction(4, 5)],
    ]
    for nB in [1, 2, 3]:
        for w in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5, 2)]:
            scores = sorted({w * x + sum(y) for x in [0, 1] for y in product([0, 1], repeat=nB)})
            thresholds = [scores[0] - 1] + scores + [scores[-1] + 1]
            for prof in profiles:
                for p in [Fraction(1, 7), Fraction(1, 2), Fraction(4, 5)]:
                    biases = [p] + prof[:nB]
                    for t in thresholds:
                        F = threshold_table([w] + [Fraction(1)] * nB, t)
                        f0, f1 = restrict_first(F, 0), restrict_first(F, 1)
                        bB = biases[1:]
                        P, _, _, DF, E2 = metrics(F, biases)
                        _, _, _, D0, _ = metrics(f0, bB)
                        _, _, _, D1, _ = metrics(f1, bB)
                        d = [(b - a) // 2 for a, b in zip(f0, f1)]
                        rho = (mean(d, bB) + 0)  # d is 0/1, so this is E d.
                        v = 4 * p * (1 - p)
                        ledger = (1 - p) * D0 + p * D1 + v * rho * (1 - rho)
                        assert DF == ledger

                        # Reconstruct the two coefficient identities without square roots.
                        for mask in assignments(nB):
                            B = frozenset(i for i in range(nB) if bit(mask, i))
                            _, q0 = amp_r_q(f0, bB, B)
                            _, q1 = amp_r_q(f1, bB, B)
                            _, qd = amp_r_q(d, bB, B)
                            _, q_no_x = amp_r_q(F, biases, frozenset(i + 1 for i in B))
                            _, q_with_x = amp_r_q(F, biases, frozenset({0} | {i + 1 for i in B}))
                            assert q_no_x == (1 - p) * q0 + p * q1
                            assert q_with_x == 2 * qd

                        if DF:
                            ratio = E2 / (Decimal(DF.numerator) / Decimal(DF.denominator))
                            assert ratio <= K
                            if ratio > max_ratio:
                                max_ratio = ratio
                                max_fixture = dict(nB=nB, w=str(w), p=str(p), t=str(t))
                        cases += 1
    return cases, max_ratio, max_fixture


def check_multislice():
    cases = 0
    max_slices = 0
    for nA, nB in [(2, 2), (2, 3), (3, 3)]:
        for w in [Fraction(1, 2), Fraction(2), Fraction(3)]:
            weights_A = [w] * nA
            bA = [Fraction(1, 3), Fraction(2, 5), Fraction(3, 4)][:nA]
            bB = [Fraction(1, 4), Fraction(1, 2), Fraction(2, 3)][:nB]
            scores = sorted({w * sum(a) + sum(b) for a in product([0, 1], repeat=nA) for b in product([0, 1], repeat=nB)})
            for t in scores:
                F = threshold_table(weights_A + [Fraction(1)] * nB, t)
                biases = bA + bB
                PF, _, _, DF, _ = metrics(F, biases)
                slices = distinct_slices(weights_A, bA, nB, t)
                max_slices = max(max_slices, len(slices))

                # Pairwise cross Dirichlet vanishes; Gram entries equal -Cov.
                for (fs, _), (fu, _) in combinations(slices, 2):
                    cross_dir = inner(fs, fu, bB, lambda k: Fraction(k))
                    cov = inner(fs, fu, bB, lambda k: Fraction(1))
                    gram = inner(fs, fu, bB, lambda k: Fraction(k - 1))
                    assert cross_dir == 0
                    assert gram == -cov

                slice_delta = Fraction(0)
                rhs_mixed = Fraction(0)
                for fs, pi in slices:
                    _, _, Ifs, Dfs, _ = metrics(fs, bB)
                    slice_delta += pi * Dfs
                    rhs_mixed += pi * (1 - pi) * Ifs

                mixed = sum(
                    Fraction(len(S & frozenset(range(nA, nA + nB)))) * mass
                    for S, mass in PF.items()
                    if S & frozenset(range(nA)) and S & frozenset(range(nA, nA + nB))
                )
                assert mixed == rhs_mixed
                assert mixed <= DF

                IA = sum(Fraction(len(S & frozenset(range(nA)))) * mass for S, mass in PF.items())
                # Spectrum of E_B F on A is exactly the pure-A parent spectrum.
                var_A_mean = sum(mass for S, mass in PF.items() if S and S <= frozenset(range(nA)))
                delta_A = IA - var_A_mean
                assert delta_A >= 0
                assert DF == slice_delta + delta_A

                # The two ledger pieces spend every root deficit coefficient once.
                ledger_by_sets = sum(
                    (Fraction(len(S & frozenset(range(nA, nA + nB))) - 1) if S & frozenset(range(nA, nA + nB)) else Fraction(0)) * mass
                    for S, mass in PF.items()
                ) + delta_A
                assert ledger_by_sets == DF
                cases += 1
    return cases, max_slices


def cofactor_rows(table, n, block):
    block = tuple(block)
    rest = tuple(i for i in range(n) if i not in block)
    rows = set()
    for u in assignments(len(block)):
        row = []
        for v in assignments(len(rest)):
            x = 0
            for j, i in enumerate(block):
                x |= bit(u, j) << i
            for j, i in enumerate(rest):
                x |= bit(v, j) << i
            row.append(table[x])
        rows.add(tuple(row))
    return rows


def check_prime_family():
    checked = 0
    for nlight in range(3, 9):
        n = nlight + 1
        F = threshold_table([Fraction(2)] + [Fraction(1)] * nlight, Fraction(3))
        for mask in range(1, (1 << n) - 1):
            block = [i for i in range(n) if bit(mask, i)]
            if len(block) < 2:
                continue
            assert len(cofactor_rows(F, n, block)) >= 3
            checked += 1
    return checked


def main():
    one_cases, max_ratio, max_fixture = check_one_exceptional()
    multi_cases, max_slices = check_multislice()
    prime_blocks = check_prime_family()
    out = {
        "status": "PASS",
        "randomness": "NONE",
        "arithmetic": "Fraction for algebra; Decimal(80 digits) only for entropy corroboration",
        "one_exceptional_cases": one_cases,
        "multislice_cases": multi_cases,
        "max_distinct_slices": max_slices,
        "prime_family_proper_blocks_checked_nlight_3_to_8": prime_blocks,
        "max_observed_Ege2_over_Delta": str(max_ratio),
        "max_ratio_fixture": max_fixture,
        "scope": "finite independent corroboration; analytic review supplies all-dimensional proof",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
