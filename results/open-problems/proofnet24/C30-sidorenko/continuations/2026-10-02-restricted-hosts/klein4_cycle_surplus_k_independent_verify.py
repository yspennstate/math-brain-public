"""Independent exact cycle-surplus verifier: fundamental cycles + multinomials.

The source graph is C10 plus its five diameter chords. A spanning-tree
fundamental-cycle basis, rather than all-mask incidence filtering, produces
the flow polynomial. Closed multinomial formulas, rather than repeated
linear-form multiplication, produce all ordered coefficients. No float is
used. The author proof, script, and certificates are read but never edited.
"""
from collections import Counter
from fractions import Fraction
from math import factorial, prod
from pathlib import Path
import json


ROOT = Path(__file__).parent


def weak_compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for rest in weak_compositions(n - first, k - 1):
                yield (first,) + rest


def linear_power(coefficients, degree):
    support = [i for i, c in enumerate(coefficients) if c]
    polynomial = {}
    for exponents in weak_compositions(degree, len(support)):
        monomial = [0] * 4
        for i, exponent in zip(support, exponents):
            monomial[i] = exponent
        coefficient = factorial(degree) // prod(factorial(e) for e in exponents)
        coefficient *= prod(coefficients[i] ** e for i, e in zip(support, exponents))
        polynomial[tuple(monomial)] = coefficient
    return polynomial


def multiply(left, right):
    polynomial = Counter()
    for m, c in left.items():
        for n, d in right.items():
            polynomial[tuple(x + y for x, y in zip(m, n))] += c * d
    return {m: c for m, c in polynomial.items() if c}


def encoded(polynomial):
    return {','.join(map(str, m)): c for m, c in polynomial.items() if c}


def main():
    certificate = json.loads((ROOT / 'continuation_20261002_klein4_cycle_surplus.json').read_text())
    original = json.loads((ROOT / 'continuation_20261002_klein4_schur.json').read_text())

    # Tree edges are consecutive edges 0--1 through 8--9. The remaining
    # edges are 9--0 and the five diameter chords i--(i+5).
    edges = [(i, (i + 1) % 10) for i in range(10)] + [(i, i + 5) for i in range(5)]
    basis = [(1 << 10) - 1]
    basis += [sum(1 << k for k in range(i, i + 5)) | (1 << (10 + i)) for i in range(5)]
    cycles = []
    for subset in range(64):
        vector = 0
        for i, b in enumerate(basis):
            if subset >> i & 1:
                vector ^= b
        cycles.append(vector)
    assert len(set(cycles)) == 64
    for vector in cycles:
        vertex_parities = [0] * 10
        for i, (u, v) in enumerate(edges):
            if vector >> i & 1:
                vertex_parities[u] ^= 1
                vertex_parities[v] ^= 1
        assert not any(vertex_parities)

    fourier = Counter()
    for x in cycles:
        for y in cycles:
            monomial = [0] * 4
            for i in range(15):
                monomial[((x >> i) & 1) + 2 * ((y >> i) & 1)] += 1
            fourier[tuple(monomial)] += 1
    assert encoded(fourier) == certificate['Fourier_polynomial']

    # Independently expand by n!/(a!b!c!d!), using the ordered linear forms
    # s=4A+3B+2C+D, r1=B+2C+D, r2=B+D, r3=D-B.
    forms = [(4, 3, 2, 1), (0, 1, 2, 1), (0, 1, 0, 1), (0, -1, 0, 1)]
    powers = {(i, n): linear_power(form, n) for i, form in enumerate(forms) for n in range(16)}
    density = Counter()
    for monomial, coefficient in fourier.items():
        term = {(0, 0, 0, 0): coefficient}
        for i, n in enumerate(monomial):
            term = multiply(term, powers[i, n])
        density.update(term)

    fourth_modes = Counter()
    sixth_modes = Counter()
    for i in range(1, 4):
        fourth_modes.update(powers[i, 4])
        sixth_modes.update(powers[i, 6])
    fourth = multiply(powers[0, 11], fourth_modes)
    sixth = multiply(powers[0, 9], sixth_modes)
    gap_four = Counter(density)
    gap_four.subtract(powers[0, 15])
    gap_four.subtract({m: 5 * c for m, c in fourth.items()})
    assert all(c >= 0 for c in gap_four.values())
    assert all(c >= 0 for c in sixth.values())
    gap = Counter(gap_four)
    gap.subtract({m: 14 * c for m, c in sixth.items()})
    assert encoded(gap) == certificate['ordered_surplus_coefficients']
    assert len(encoded(gap)) == 760
    assert all(c >= 0 for c in gap.values())
    ratios = [(Fraction(gap_four.get(m, 0), c), m) for m, c in sixth.items() if c > 0]
    ratio, monomial = min(ratios)
    assert (ratio, monomial) == (Fraction(8165, 567), (6, 8, 0, 1))
    stronger_gap = Counter({m: 567 * c for m, c in gap_four.items()})
    stronger_gap.subtract({m: 8165 * c for m, c in sixth.items()})
    assert all(c >= 0 for c in stronger_gap.values())

    # Check all 23 orbit-table rows without assuming the printed table.
    orbit_coefficients = {}
    for (n0, n1, n2, n3), coefficient in fourier.items():
        key = (n0, tuple(sorted((n1, n2, n3), reverse=True)))
        if key in orbit_coefficients:
            assert orbit_coefficients[key] == coefficient
        orbit_coefficients[key] = coefficient
    assert len(orbit_coefficients) == 23

    # The witness is evaluated using the previous vertex polynomial,
    # not the Fourier polynomial used to generate the new certificate.
    p = [Fraction(97, 400)] + [Fraction(101, 400)] * 3
    value = sum(c * prod(p[i] ** n for i, n in enumerate(map(int, k.split(','))))
                for k, c in original['density_polynomial'].items())
    r = Fraction(-1, 100)
    threshold = 1 + 15 * r ** 4 + 45 * r ** 6
    assert str(value) == certificate['coefficient15_failure']['density']
    assert str(value - threshold) == certificate['coefficient15_failure']['difference_from_coefficient15_threshold']
    assert value - threshold < 0

    result = {
        'status': 'independent fundamental-cycle and multinomial certificate PASS',
        'source_graph': 'C10 plus five diameter chords',
        'binary_cycles': len(cycles),
        'complete_73_Fourier_coefficients_match': True,
        'complete_760_ordered_surplus_coefficients_match': True,
        'stronger_constant': str(ratio),
        'limiting_monomial_A_B_C_D': monomial,
        'stronger_gap_all_coefficients_nonnegative': True,
        'orbit_table': {str(k): c for k, c in sorted(orbit_coefficients.items(), reverse=True)},
        'independent_vertex_polynomial_witness_density': str(value),
        'independent_vertex_polynomial_difference15': str(value - threshold),
    }
    (ROOT / 'klein4_cycle_surplus_k_independent_verify.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
