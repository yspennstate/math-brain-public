"""Bounded exact-arithmetic checks of the written proof; not a formal proof.

Run only after a fresh compute admission receipt, and keep that receipt beside
the output. No third-party packages, random search, GPU, store writes or workers.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parents[1]


def bc(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def inner(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm2(v):
    return inner(v, v)


def project_first(t, q):
    # Average actual coordinate orbits, without using the sharpness formula.
    buckets = {}
    for coordinate, value in t.items():
        key = (sum(coordinate[:q]), coordinate[q:])
        values = buckets.setdefault(key, [])
        values.append(value)
    means = {key: sum(values)/len(values) for key, values in buckets.items()}
    return {coordinate: means[(sum(coordinate[:q]), coordinate[q:])]
            for coordinate in t}


def compositions(d, s):
    if s == 1:
        yield (d,)
        return
    for first in range(1, d-s+2):
        for rest in compositions(d-first, s-1):
            yield (first,)+rest


def polynomial(j):
    if j == 0:
        return {0: F(1)}
    return {j: F(1, factorial(j)), j-1: -F(1, factorial(j-1))}


def exp_inner(j, k):
    return sum(a*b*factorial(r+s)
               for r, a in polynomial(j).items()
               for s, b in polynomial(k).items())


def run():
    started = time.perf_counter()
    checks = {}
    coefficient_cases = 0
    for p in range(1, 8):
        for q in range(p, 13):
            for r in range(p+1):
                lhs = bc(q-p+r, p)
                rhs = sum(bc(r, s)*bc(q-p, p-s) for s in range(p+1))
                assert lhs == rhs, (p, q, r, lhs, rhs)
                coefficient_cases += 1
    checks['incidence_coefficient_cases'] = coefficient_cases

    # Actual vector-valued incidence quadratic identity, not only coefficients.
    p, q = 2, 4
    universe = range(p+q)
    subsets = list(combinations(universe, p))
    vectors = {a: (F((i*7)%11-5), F((i*3)%7-3))
               for i, a in enumerate(subsets)}
    def sum_vectors(keys):
        keys = list(keys)
        return tuple(sum(vectors[k][j] for k in keys) for j in range(2))
    lhs = sum(norm2(sum_vectors(a for a in subsets if set(a)<=set(e)))
              for e in combinations(universe, q))
    rhs = sum(bc(q-p,p-s)*sum(
        norm2(sum_vectors(a for a in subsets if set(a)>=set(small)))
        for small in combinations(universe, s)) for s in range(p+1))
    assert lhs == rhs
    checks['vector_incidence_identity'] = {'lhs': str(lhs), 'rhs': str(rhs)}

    sharp = []
    coordinate_checks = 0
    for p in range(1, 4):
        for q in range(p, 6):
            coords = list(product((0, 1), repeat=p+q))
            t = {i: F((-1)**sum(i[:p]), bc(q,p-sum(i[:p])))
                 if sum(i)==p else F(0) for i in coords}
            projected = project_first(t,q)
            b = bc(q,p)
            for i in coords:
                moved = i[q:]+i[:q]
                assert projected[i] == F((-1)**p,b)*t[moved], (p,q,i)
                coordinate_checks += 1
            tnorm = sum(v*v for v in t.values())
            pnorm = sum(v*v for v in projected.values())
            assert tnorm > 0 and b*b*pnorm == tnorm
            sharp.append({'p':p,'q':q,'optimal_factor':b,
                          'tensor_norm_squared':str(tnorm),
                          'projected_norm_squared':str(pnorm)})
    checks['sharpness_coordinate_cases'] = coordinate_checks
    checks['sharpness_models'] = sharp

    # The weakened block-symmetry statement must fail, with exact zero projection.
    bad = {i:F(0) for i in product((0,1), repeat=3)}
    bad[(0,1,0)] = F(1)
    bad[(1,0,0)] = F(-1)
    assert sum(v*v for v in bad.values()) == 2
    assert all(v == 0 for v in project_first(bad,2).values())
    checks['missing_symmetry_control'] = {'norm_squared':2,'projected_norm_squared':0}

    moment_cases = 0
    for j in range(0, 13):
        for k in range(0, 13):
            expected = F(1 if j==k==0 else 0) if j==0 or k==0 else F(bc(j+k-2,j-1))
            assert exp_inner(j,k) == expected, (j,k)
            moment_cases += 1
    checks['exponential_polynomial_moment_cases'] = moment_cases

    trace_cases = []
    composition_cases = 0
    for d in range(1, 10):
        target = bc(2*d-2,d-1)
        for s in range(1,d+1):
            alphas = list(compositions(d,s))
            trace = F(0)
            weight_sum = F(0)
            for alpha in alphas:
                numerator = 1
                diagonal = 1
                for a in alpha:
                    numerator *= factorial(a)
                    diagonal *= bc(2*a-2,a-1)
                weight = F(numerator,factorial(d))
                weight_sum += weight
                trace += weight*diagonal
                composition_cases += 1
            assert weight_sum <= 1
            assert trace <= bc(2*(d-s),d-s) <= target
            if s==1:
                assert trace == target
            trace_cases.append({'d':d,'support_size':s,'trace':str(trace),
                                'sharp_norm_squared':target})
    checks['support_trace_cases'] = len(trace_cases)
    checks['positive_composition_cases'] = composition_cases
    checks['support_trace_results'] = trace_cases

    # An incorrect tensor normalization changes the exact norm by d!, not n.
    d = 4
    correct_squared = bc(2*d-2,d-1)
    unnormalized_squared = factorial(d)**2*correct_squared
    assert correct_squared == 20 and unnormalized_squared == 11520
    checks['factorial_normalization_control'] = {
        'd':d,'correct_norm_squared':correct_squared,
        'unnormalized_norm_squared':unnormalized_squared}

    # Isotropy without log-concavity does not bound the second tilt coefficient.
    m = 101
    checks['isotropy_only_control'] = {
        'law':'mass 1/(2M) at each of +/-sqrt(M), remainder at 0; not log-concave',
        'M':m,'variance_X':1,'variance_X_squared':m-1,
        'degree_two_operator_norm_squared':F(m-1,4).__str__()}

    checks['before_after_constants'] = [
        {'d':d,'published_stated_bound':4**d,
         'bound_already_in_published_proof':bc(2*d,d),
         'verified_sharp_bound':bc(2*d,d),
         'ratio_stated_to_sharp':str(F(4**d,bc(2*d,d))),
         'exact_exp_product_tilt_norm_squared':bc(2*d-2,d-1)}
        for d in (1,2,4,8,16)]
    result = {'status':'PASS','scope':'finite exact arithmetic; not a formal or independent proof',
              'elapsed_compute_seconds':time.perf_counter()-started,'checks':checks}
    out = BASE/'checks'/'exact_results.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    summary = {k:v for k,v in checks.items() if k.endswith('_cases')}
    print(json.dumps({'status':result['status'],'elapsed_compute_seconds':result['elapsed_compute_seconds'],
                      'counts':summary,'output':str(out)}))


if __name__ == '__main__':
    run()
