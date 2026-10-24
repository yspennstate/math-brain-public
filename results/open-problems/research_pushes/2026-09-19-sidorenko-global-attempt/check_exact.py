"""Exact obstructions for two proposed global Sidorenko proof steps.
Run with Python 3, standard library only. These are NOT Sidorenko counterexamples.
All acceptance comparisons use fractions; no floating-point sign tests occur.
"""
from fractions import Fraction as F
from itertools import product, permutations, combinations
from pathlib import Path
import json

Q = [[547845, 22, 30967151, 932390],
     [22, 27, 5, 2177],
     [30967151, 5, 870744517, 32344047],
     [932390, 2177, 32344047, 216028]]

def kernel_from_flow(q):
    n = len(q)
    assert all(len(row) == n for row in q)
    assert all(q[i][j] == q[j][i] and q[i][j] >= 0
               for i in range(n) for j in range(n))
    rows = list(map(sum, q)); total = sum(rows)
    assert min(rows) > 0
    p = [F(r, total) for r in rows]
    w = [[F(total*q[i][j], rows[i]*rows[j]) for j in range(n)]
         for i in range(n)]
    assert sum(p) == 1
    assert all(sum(w[i][j]*p[j] for j in range(n)) == 1 for i in range(n))
    return p, w

def mm(a, b, p):
    n = len(p)
    return [[sum((a[i][k]*p[k]*b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]

def inner(a, b, p, weight=None):
    n = len(p)
    return sum((p[i]*p[j]*a[i][j]*b[i][j]
                *(1 if weight is None else weight[i][j])
                for i in range(n) for j in range(n)), F(0))

def densities(w, p):
    n = len(p)
    c = [[[sum((p[u]*w[u][i]*w[u][j]*w[u][k] for u in range(n)), F(0))
           for k in range(n)] for j in range(n)] for i in range(n)]
    h = F(0)
    for x in product(range(n), repeat=5):
        term = F(1)
        for i in range(5):
            term *= p[x[i]]*c[x[i]][x[(i+1)%5]][x[(i+2)%5]]
        h += term
    k33 = sum((p[i]*p[j]*p[k]*c[i][j][k]**3
               for i,j,k in product(range(n), repeat=3)), F(0))
    return h, k33

def main():
    p, w = kernel_from_flow(Q)
    assert min(v for row in w for v in row) > 0
    u = [[v-1 for v in row] for row in w]
    u2 = mm(u,u,p); u3 = mm(u2,u,p); u5 = mm(u3,u2,p)
    g33 = inner(u3,u3,p,w); g35 = inner(u3,u5,p,w)
    g55 = inner(u5,u5,p,w); s8 = inner(u3,u5,p)
    assert s8 > 0 and g35 < 0
    assert F(-33,20) < g35/s8 < F(-8,5)
    assert g33 >= 0 and g55 >= 0 and g33*g55-g35*g35 >= 0
    h, _ = densities(w,p)
    assert F(33,25) < h < F(133,100)
    p2 = [F(1,2)]*2
    w2 = [[F(5,4),F(3,4)], [F(3,4),F(5,4)]]
    h2, k2 = densities(w2,p2)
    assert h2 == F(1073389,1048576)
    assert k2 == F(2123,2048)
    assert 1 < h2 < k2
    triples = list(combinations(range(5),3))
    counts = {t:0 for t in triples}
    for perm in permutations(range(5)):
        for i in range(5):
            counts[tuple(sorted(perm[(i+j)%5] for j in range(3)))] += 1
    assert set(counts.values()) == {60}
    output = {
        'status':'ALL_EXACT_CHECKS_PASS',
        'scope':'Two proof-mechanism counterexamples, not Sidorenko counterexamples',
        'integer_flow':Q, 'strictly_positive_regular_kernel':True,
        'gram_g35_negative':True, 'gram_g35_over_s8_interval':['-33/20','-8/5'],
        'gram_g35':str(g35), 's8':str(s8),
        'weighted_gram_determinant_nonnegative':True,
        'four_block_H_density_interval':['33/25','133/100'],
        'transfer_H':str(h2), 'transfer_K33':str(k2),
        'transfer_difference':str(h2-k2),
        'holder_permutations':120, 'holder_occurrences_each_triple':60,
        'half_exponent_lower_bound_proved':False,
        'full_Sidorenko_proof':False,
        'independent_audit':False
    }
    Path(__file__).with_name('exact_checks.json').write_text(json.dumps(output,indent=2)+'\n')
    print('ALL_EXACT_CHECKS_PASS')
    print('Four-block W is strictly positive, symmetric, and exactly 1-regular.')
    print('-33/20 < integral(W U3 U5)/Tr(U^8) < -8/5 < 0.')
    print('33/25 < t_H(W) < 133/100; this is not a Sidorenko counterexample.')
    print('Two-block t_H = 1073389/1048576 < t_K33 = 2123/2048.')
    print('Hölder symmetrization: each triple occurs 60 times in 120 permutations.')
    print('Full Sidorenko proof: NOT OBTAINED.')

if __name__ == '__main__':
    main()
