"""Exact route checks; not a proof of the actual three-crossing trace bound.

Checks a genuine two-crossing common-score slab with a NON-CROSSING trace
threshold; its trace ratio diverges. Also checks the four-flux reduction
and a failure of total positivity for the score-ordered cube semigroup.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import numpy as np


def truth_check(k, N):
    assert k >= 2 and N >= 3 and N % 2
    A = 2 * N + 1
    n = k + N
    size = 1 << n
    indices = np.arange(size, dtype=np.int64)
    coarse = np.zeros(size, dtype=np.int64)
    fine = np.zeros(size, dtype=np.int64)
    for j in range(k):
        coarse += (1 << j) * (2 * ((indices >> j) & 1) - 1)
    for j in range(k, n):
        fine += 2 * ((indices >> j) & 1) - 1
    scores = A * coarse + fine
    f = np.where(coarse == 1, -1, 1)
    assert np.array_equal(f, np.where((scores > 0) & (scores < 2*A), -1, 1))
    assert not np.any(scores == A)
    H = np.where(scores > A, 1, -1)
    gamma = np.zeros(size, dtype=np.int64)
    f_flips = 0
    for j in range(n):
        partner = indices ^ (1 << j)
        gamma += H != H[partner]
        f_flips += int(np.sum(f != f[partner]))
    K = F(int(gamma.sum()), size)
    M = F(int((gamma * f).sum()), size)
    influence = F(f_flips, size)
    p = F(1, 1 << k)
    majority = F(N * comb(N-1, (N-1)//2), 1 << (N-1))
    assert K == 1 + (k-2)*p + p*majority
    assert M == 1 - 2*p - p*majority
    assert influence == 2*k*p
    trace = K - M*M/K
    return {'k': k, 'fine_bits': N, 'K': str(K), 'K_times_nu_mean': str(M),
            'I_f': str(influence), 'trace_value': str(trace), 'trace_ratio': str(trace/influence)}


def symbolic_check(k):
    N = (1 << (2*k)) + 1
    p = F(1, 1 << k)
    majority = F(N * comb(N-1, (N-1)//2), 1 << (N-1))
    K = 1 + (k-2)*p + p*majority
    M = 1 - 2*p - p*majority
    influence = 2*k*p
    trace = K - M*M/K
    assert trace >= F(2, 3)
    assert trace/influence >= F(1, 3*k*p)
    return {'k': k, 'N': N, 'I_f': str(influence),
            'trace_at_least_two_thirds': True,
            'ratio_lower_bound': str(F(1, 3*k*p)),
            'trace_ratio_approx': float(trace/influence)}


def four_flux_check():
    weights = [2, 2, 2, 2, 3]
    n, size = len(weights), 1 << len(weights)
    scores = [sum(w * (1 if x >> j & 1 else -1) for j, w in enumerate(weights))
              for x in range(size)]
    cuts = [-2, 0, 2]
    region = [sum(s > c for c in cuts) for s in scores]
    counts = {(i, j): 0 for i in range(4) for j in range(i+1, 4)}
    for u in range(size):
        for j in range(n):
            if not u >> j & 1:
                v = u | (1 << j)
                a, b = region[u], region[v]
                if a != b:
                    assert a < b
                    counts[a, b] += 1
    flux = {ij: F(2*c, size) for ij, c in counts.items()}
    x, y = flux[0, 2], flux[1, 3]
    o, t = flux[0, 3]+flux[1, 2], flux[0, 1]+flux[2, 3]
    K, influence = x+y+o, o+t
    trace = K - (x-y)**2/K
    assert trace/influence == F(15, 11)
    assert (influence+2*min(x,y))/influence == F(23, 11)
    assert (trace <= 2*influence) == (4*x*y <= o*o+2*t*K)
    return {'weights': weights, 'cuts': cuts,
            'flux': {str(ij): str(v) for ij, v in flux.items()},
            'trace_ratio': str(trace/influence),
            'min_component_ratio': str((influence+2*min(x,y))/influence),
            'four_flux_equivalence': True}


def main():
    truth = [truth_check(k, N) for k, N in
             [(2, 3), (2, 5), (2, 9), (2, 17), (3, 3), (3, 5), (3, 9), (4, 3), (4, 5)]]
    symbolic = [symbolic_check(k) for k in range(2, 7)]
    # For rho=1/2, each bit stays with probability p=3/4 and flips with
    # probability q=1/4. In the score order -3,-1,1,3, use rows0,1 cols1,2.
    p, q = F(3, 4), F(1, 4)
    minor = (p*q)*(q*q) - (p*q)*(p*p)
    assert minor == -F(3, 32)
    out = {'status': 'exact route obstructions PASS; actual three-crossing conjecture unproved',
           'scope': 'trace threshold lies strictly INSIDE the negative slab, not at a crossing',
           'truth_checks': truth, 'symbolic_checks': symbolic,
           'four_flux_check': four_flux_check(),
           'score_semigroup_TP2_minor': str(minor)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
