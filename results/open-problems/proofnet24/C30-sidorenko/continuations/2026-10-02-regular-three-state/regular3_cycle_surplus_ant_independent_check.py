#!/usr/bin/env python3
"""Independent left-vertex integration of the regular-three-state ML10 claim.

No author modules imported. Polynomial keys encode exponents in base 16;
every multiplication here has total degree at most 15, hence no carries.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ONE = {0: 1}
V = [{16**i: 1} for i in range(4)]

def add(*ps):
    q = Counter()
    for p in ps:
        q.update(p)
    return {k: v for k, v in q.items() if v}

def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}

def mul(p, q):
    out = Counter()
    for i, x in p.items():
        for j, y in q.items():
            out[i+j] += x*y
    return {k: v for k, v in out.items() if v}

def power(p, n):
    out = ONE
    for _ in range(n):
        out = mul(out, p)
    return out

def decode(k):
    return tuple((k // 16**i) % 16 for i in range(4))

def serial(p):
    return {','.join(map(str, decode(k))): v for k, v in sorted(p.items())}

def evaluate(p, x):
    return sum(Fraction(v) * product_numeric(xi**ei for xi, ei in zip(x, decode(k)))
               for k, v in p.items())

def product_numeric(xs):
    p = Fraction(1)
    for x in xs:
        p *= x
    return p

def matmul(p, q):
    n = len(p)
    return [[add(*(mul(p[i][k], q[k][j]) for k in range(n)))
             for j in range(n)] for i in range(n)]

def trace_power(p, n):
    r = p
    for _ in range(n-1):
        r = matmul(r, p)
    return add(*(r[i][i] for i in range(len(p))))

def make_cone(name):
    A, BB, C, D = V
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    complete = [[int(i != j) for j in range(3)] for i in range(3)]
    transpositions = []
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        permutation = list(range(3))
        permutation[i], permutation[j] = permutation[j], permutation[i]
        transpositions.append([[int(col == permutation[row]) for col in range(3)]
                               for row in range(3)])
    factor = 1 if name == 'I' else 2
    weights = [scale(add(A, BB, C), factor), scale(add(A, BB), factor), scale(A, factor)]
    base = identity if name == 'I' else complete
    return [[add(scale(D, base[i][j]),
                 *(scale(w, T[i][j]) for w, T in zip(weights, transpositions)))
             for j in range(3)] for i in range(3)]

def density_from_left(P):
    triples = list(combinations_with_replacement(range(3), 3))
    cubic = {t: add(*(mul(mul(P[t[0]][j], P[t[1]][j]), P[t[2]][j])
                     for j in range(3))) for t in triples}
    profiles = Counter()
    for left in product(range(3), repeat=5):
        profile = tuple(sorted(tuple(sorted((left[(j-1) % 5], left[j], left[(j+1) % 5])))
                               for j in range(5)))
        profiles[profile] += 1
    total = {}
    for profile, count in profiles.items():
        term = ONE
        for t in profile:
            term = mul(term, cubic[t])
        total = add(total, scale(term, count))
    return scale(total, 3**5), len(profiles), sum(profiles.values())

def cycle_count(k):
    # Literal ladder graph; count every directed start/orientation, divide by 2k.
    adjacency = {i: set() for i in range(10)}
    for i in range(5):
        for j in range(5):
            if (j-i) % 5 in (0, 1, 4):
                adjacency[i].add(5+j)
                adjacency[5+j].add(i)
    count = 0
    def visit(start, path):
        nonlocal count
        if len(path) == k:
            count += start in adjacency[path[-1]]
            return
        for nxt in adjacency[path[-1]]:
            if nxt not in path:
                visit(start, path+[nxt])
    for start in range(10):
        visit(start, [start])
    assert count % (2*k) == 0
    return count // (2*k)

def main():
    author_full = json.loads((HERE/'continuation_20261002_regular3_full_enumeration.json').read_text())
    author_cycles = json.loads((HERE/'continuation_20261002_regular3_cycle_surplus.json').read_text())
    report = {'route': 'integrate right vertices after all 243 left assignments; base16 polynomials',
              'cycles4': cycle_count(4), 'cycles6': cycle_count(6), 'cones': {}}
    saved = {}
    for name in ('I', 'T'):
        P = make_cone(name)
        s = add(*P[0])
        assert all(add(*row) == s for row in P)
        F, profile_count, assignments = density_from_left(P)
        assert assignments == 243
        assert serial(F) == author_full['results'][name]['density']
        E4 = add(trace_power(P, 4), scale(power(s, 4), -1))
        E6 = add(trace_power(P, 6), scale(power(s, 6), -1))
        R = add(power(V[1], 2), mul(V[1], V[2]), power(V[2], 2))
        q = scale(R, 1 if name == 'I' else 4)
        e4_formula = add(scale(power(V[3], 4), 2), scale(mul(power(V[3], 2), q), 12), scale(power(q, 2), 2))
        e6_formula = add(scale(power(V[3], 6), 2), scale(mul(power(V[3], 4), q), 30),
                         scale(mul(power(V[3], 2), power(q, 2)), 30), scale(power(q, 3), 2))
        assert E4 == e4_formula and E6 == e6_formula
        author = author_cycles['results'][name]
        assert serial(E4) == author['C4_excess']
        assert serial(E6) == author['C6_excess']
        gap = add(F, scale(power(s, 15), -1))
        assert serial(gap) == author_full['results'][name]['gap']
        remainder = add(gap, scale(mul(power(s, 11), E4), -5))
        denominator = mul(power(s, 9), E6)
        L = add(scale(remainder, 18), scale(denominator, -265))
        assert serial(L) == author['integer_scaled_surplus_coefficients']
        assert all(c > 0 for c in L.values())
        assert all(c >= 0 for c in remainder.values())
        minimum = min(Fraction(remainder.get(k, 0), v) for k, v in denominator.items())
        assert minimum == Fraction(265, 18)
        limiting = sorted(decode(k) for k, v in denominator.items()
                          if Fraction(remainder.get(k, 0), v) == minimum)
        assert tuple(author['limiting_monomial']) in limiting
        assert all(v >= 0 for k, v in remainder.items() if k not in denominator)
        report['cones'][name] = {'left_assignments': assignments, 'left_profiles': profile_count,
            'density_coefficients': len(F), 'all_author_density_coefficients_match': True,
            'direct_matrix_cycle_formulas_match': True, 'all_author_surplus_coefficients_match': True,
            'positive_surplus_coefficients': len(L), 'minimum_surplus_coefficient': min(L.values()),
            'coefficientwise_sixth_constant': str(minimum), 'limiting_monomials': limiting}
        saved[name] = (F, s, E4, E6)
    F, s, E4, E6 = saved['T']
    witness = (Fraction(49,300), Fraction(0), Fraction(0), Fraction(1,100))
    fval = evaluate(F, witness)
    sval = evaluate(s, witness)
    e4val, e6val = evaluate(E4, witness), evaluate(E6, witness)
    bad_gap = fval - sval**15 - 5*sval**11*e4val - 15*sval**9*e6val
    good_gap = fval - sval**15 - 5*sval**11*e4val - Fraction(265,18)*sval**9*e6val
    assert bad_gap < 0 < good_gap
    assert str(fval) == author_cycles['coefficient15_failure']['density']
    assert str(bad_gap) == author_cycles['coefficient15_failure']['difference_from_coefficient15_threshold']
    report['sixth15_witness'] = {'density': str(fval), 'coefficient15_gap': str(bad_gap),
                                'proven_bound_gap': str(good_gap)}
    # A third exact route also verifies the perturbation expansion and leading sharpness.
    F = saved['I'][0]
    univariate = Counter()
    for k, value in F.items():
        a, b, c, d = decode(k)
        if b or c:
            continue
        for j in range(a+1):
            univariate[d+j] += Fraction(value * comb(a,j) * (-1)**j, 3**a)
    coeff = {str(i): str(univariate[i]) for i in range(16)}
    assert [univariate[i] for i in range(7)] == [1,0,0,0,10,0,30]
    report['identity_perturbation_coefficients'] = coeff
    report['status'] = 'PASS: all exact assertions succeeded'
    out = HERE/'regular3_cycle_surplus_ant_independent_checks.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
