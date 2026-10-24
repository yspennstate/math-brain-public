"""Exact Klein-four Fourier-flow and cycle-surplus certificate.

The cycle-space generator is independent of both vertex enumeration and
the transfer matrix. Every arithmetic operation is an ordinary integer or
Fraction operation. Numerical optimization is not part of the certificate.
"""
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


def multiply(P, Q):
    R = Counter()
    for a, u in P.items():
        for b, v in Q.items():
            R[tuple(a[i] + b[i] for i in range(4))] += u * v
    return {a: u for a, u in R.items() if u}


def power(P, n):
    R = {(0, 0, 0, 0): 1}
    for _ in range(n):
        R = multiply(R, P)
    return R


def linear(values):
    return {tuple(int(i == j) for i in range(4)): v
            for j, v in enumerate(values) if v}


def encode(P):
    return {','.join(map(str, a)): v for a, v in sorted(P.items()) if v}


def main():
    edges = [(i, 5 + j) for i in range(5) for j in range(5)
             if (j - i) % 5 in (0, 1, 4)]
    cycles = []
    for mask in range(1 << 15):
        degree = [0] * 10
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                degree[u] ^= 1
                degree[v] ^= 1
        if not any(degree):
            cycles.append(mask)
    assert len(cycles) == 64
    Fourier = Counter()
    for x in cycles:
        for y in cycles:
            counts = [0] * 4
            for i in range(15):
                counts[((x >> i) & 1) + 2 * ((y >> i) & 1)] += 1
            Fourier[tuple(counts)] += 1
    assert sum(Fourier.values()) == 4096
    assert len(Fourier) == 73
    assert all((a - b) % 2 == 0 and (b - c) % 2 == 0
               for _, a, b, c in Fourier)

    # p0=A+B+C+D, p1=A+B+C, p2=A+B, p3=A.
    # s and the three Fourier modes, in an immaterial permutation.
    forms = [linear([4, 3, 2, 1]), linear([0, 1, 2, 1]),
             linear([0, 1, 0, 1]), linear([0, -1, 0, 1])]
    powers = {(j, n): power(P, n) for j, P in enumerate(forms)
              for n in range(16)}
    ordered = Counter()
    for counts, coefficient in Fourier.items():
        T = {(0, 0, 0, 0): coefficient}
        for j, n in enumerate(counts):
            T = multiply(T, powers[j, n])
        ordered.update(T)

    # Independently substitute the existing vertex-enumeration polynomial.
    original = json.loads(Path(__file__).with_name(
        'continuation_20261002_klein4_schur.json').read_text())
    host_powers = {(j, n): power(linear([int(k <= 3-j)
                                       for k in range(4)]), n)
                   for j in range(4) for n in range(16)}
    host_ordered = Counter()
    for key, coefficient in original['density_polynomial'].items():
        counts = tuple(map(int, key.split(',')))
        T = {(0, 0, 0, 0): coefficient}
        for j, n in enumerate(counts):
            T = multiply(T, host_powers[j, n])
        host_ordered.update(T)
    assert {a: v for a, v in ordered.items() if v} == {
        a: v for a, v in host_ordered.items() if v}

    C4 = Counter()
    C6 = Counter()
    for j in range(1, 4):
        C4.update(powers[j, 4])
        C6.update(powers[j, 6])
    fourth = multiply(powers[0, 11], C4)
    sixth = multiply(powers[0, 9], C6)
    gap_four = Counter(ordered)
    gap_four.subtract(powers[0, 15])
    gap_four.subtract({a: 5 * v for a, v in fourth.items()})
    assert all(v >= 0 for v in gap_four.values())
    gap = Counter(gap_four)
    gap.subtract({a: 14 * v for a, v in sixth.items()})
    assert all(v >= 0 for v in gap.values())
    assert all(v >= 0 for v in sixth.values())
    best_ratio = min((Fraction(gap_four.get(a, 0), v), a)
                     for a, v in sixth.items() if v > 0)
    assert best_ratio[0] == Fraction(8165, 567)

    # Exact three-negative-mode obstruction to replacing 14 by 15.
    s = Fraction(1)
    r = -Fraction(1, 100)
    value = sum(c * s ** a * r ** (b+c1+d)
                for (a, b, c1, d), c in Fourier.items())
    threshold15 = 1 + 15 * r**4 + 45 * r**6
    difference15 = value - threshold15
    assert difference15 < 0
    value14 = 1 + 15 * r**4 + 42 * r**6
    assert value > value14
    out = {
        'status': 'exact Fourier-flow and ordered cycle-surplus certificate PASS',
        'edges': edges,
        'binary_cycle_count': len(cycles),
        'Fourier_polynomial': encode(Fourier),
        'Fourier_to_vertex_polynomial_match': True,
        'ordered_surplus_coefficients': encode(gap),
        'ordered_surplus_nonzero_terms': sum(bool(v) for v in gap.values()),
        'ordered_surplus_negative_terms': sum(v < 0 for v in gap.values()),
        'largest_coefficientwise_sixth_cycle_constant': str(best_ratio[0]),
        'limiting_coefficient_monomial': best_ratio[1],
        'coefficient15_failure': {
            's': '1',
            'r1': '-1/100', 'r2': '-1/100', 'r3': '-1/100',
            'p': ['97/400', '101/400', '101/400', '101/400'],
            'density': str(value),
            'difference_from_coefficient15_threshold': str(difference15),
            'difference_from_coefficient14_threshold': str(value-value14),
        },
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2))
    print(json.dumps({k: v for k, v in out.items()
                      if not k.endswith('coefficients') and k not in
                      ['edges', 'Fourier_polynomial']}, indent=2))


if __name__ == '__main__':
    main()
