#!/usr/bin/env python3
"""Exact finite checks for the proposed GP determinant/LN arithmetic circuit.

This verifies rational identities on finite examples, not architecture expressivity
or a general theorem. Square roots are handled through their exact squared norms.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import random

def det(a):
    if not a:
        return F(1)
    a = [row[:] for row in a]
    result = F(1)
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[j], a[k] = a[k], a[j]
            result = -result
        q = a[j][j]
        result *= q
        for k in range(j + 1, len(a)):
            ratio = a[k][j] / q
            a[k] = [x - ratio*y for x, y in zip(a[k], a[j])]
    return result

def inverse(a):
    n = len(a)
    b = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j])
        b[j], b[k] = b[k], b[j]
        q = b[j][j]
        b[j] = [x/q for x in b[j]]
        for k in range(n):
            if k != j:
                q = b[k][j]
                b[k] = [x-q*y for x, y in zip(b[k], b[j])]
    return [row[n:] for row in b]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def mv(a, b):
    return [dot(row, b) for row in a]

def check(condition, label):
    if not condition:
        raise RuntimeError(label)

def main():
    rng = random.Random(228336)
    count = 0
    examples = []
    for n in range(1, 5):
        for r in range(1, 5):
            for repeat in range(8):
                s = F(1 + repeat % 3, 2)
                eps = F(repeat, 100)
                phi = [[F(rng.randrange(-3, 4), 2) for _ in range(r)] for _ in range(n)]
                query = [F(rng.randrange(-3, 4), 2) for _ in range(r)]
                y = [F(rng.randrange(-9, 10))*10**repeat for _ in range(n)]
                h = [[s*F(i == j) + sum(phi[k][i]*phi[k][j] for k in range(n)) for j in range(r)] for i in range(r)]
                d = det(h)
                sos = F(0)
                terms = 1
                for k in range(1, min(n, r) + 1):
                    for rows in combinations(range(n), k):
                        for cols in combinations(range(r), k):
                            minor = det([[phi[i][j] for j in cols] for i in rows])
                            sos += s**(r-k)*minor**2
                            terms += 1
                check(terms == comb(n+r, r), 'Vandermonde term count')
                check(d == s**r+sos, 'Cauchy-Binet determinant SOS')
                lam2 = (1+terms*eps)/s**r
                ln_denominator_squared = (lam2*sos+1)/terms+eps
                reciprocal = (lam2/terms)/ln_denominator_squared
                check(reciprocal == 1/d, 'Exact normalized-constant reciprocal')
                inv_h = inverse(h)
                h_y = [sum(phi[k][j]*y[k] for k in range(n)) for j in range(r)]
                mean = dot(query, mv(inv_h, h_y))
                variance = s+s*dot(query, mv(inv_h, query))
                k_noise = [[dot(phi[i], phi[j])+s*F(i == j) for j in range(n)] for i in range(n)]
                inv_k = inverse(k_noise)
                cross = [dot(row, query) for row in phi]
                check(mean == dot(cross, mv(inv_k, y)), 'Feature and kernel posterior means')
                check(variance == s+dot(query, query)-dot(cross, mv(inv_k, cross)), 'Feature and kernel posterior variances')
                check(variance >= s, 'Positive noisy variance')
                count += 1
                if repeat == 7:
                    examples.append({'n': n, 'rank': r, 'signed_LN_width': 2*terms, 'determinant': str(d), 'mean': str(mean), 'variance': str(variance)})
    result = {'status': 'PASS', 'cases': count, 'checks_per_case': 6, 'exact_checks': count*6,
              'scope': 'Finite rational identity checks, not a general proof or transformer compiler verification.',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'examples': examples}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'cases', 'exact_checks', 'scope']}))

if __name__ == '__main__':
    main()
