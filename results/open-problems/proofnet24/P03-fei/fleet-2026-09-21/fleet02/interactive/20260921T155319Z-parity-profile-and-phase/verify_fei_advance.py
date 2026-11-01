#!/usr/bin/env python3
"""Self-checks for parity-profile obstruction and quadratic-phase compression.
Exact integer/Fraction checks are separated from floating entropy diagnostics.
This is not a proof or exhaustive test of unrestricted FEI.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product, combinations
import json
import math
from pathlib import Path
import numpy as np


def walsh(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=np.int64).copy()
    N = a.shape[-1]
    if N < 1 or N & (N - 1):
        raise ValueError('last dimension must be a power of two')
    h = 1
    while h < N:
        v = a.reshape(*a.shape[:-1], -1, 2, h)
        u, w = v[..., 0, :].copy(), v[..., 1, :].copy()
        v[..., 0, :], v[..., 1, :] = u + w, u - w
        h *= 2
    return a


def basis(rows: list[int], n: int) -> list[int]:
    pivots: dict[int, int] = {}
    for row in rows:
        v = int(row)
        while v:
            bit = v.bit_length() - 1
            if bit in pivots:
                v ^= pivots[bit]
            else:
                pivots[bit] = v
                break
    return [pivots[i] for i in sorted(pivots, reverse=True)]


def parity_mean_check() -> dict:
    count = 0
    # Exact direct enumeration, including marginals on both sides of 1/2.
    for n in range(1, 5):
        xs = list(product((0, 1), repeat=n))
        for nums in product((1, 2, 3), repeat=n):
            den = 4 ** n
            weights = [math.prod(nums[i] if x[i] else 4 - nums[i]
                                 for i in range(n)) for x in xs]
            mean = F(sum(w * sum(x) for w, x in zip(weights, xs)), den)
            for J in range(1, 1 << n):
                for parity in (0, 1):
                    selected = [(w, x) for w, x in zip(weights, xs)
                                if sum(x[i] for i in range(n) if J >> i & 1) % 2 == parity]
                    total = sum(w for w, _ in selected)
                    conditional = F(sum(w * sum(x) for w, x in selected), total)
                    assert abs(conditional - mean) <= 1 - F(total, den)
                    count += 1
    # The scalar tensor inequality used in the all-dimensional proof.
    tensor_count = 0
    for n in range(1, 7):
        for cs in product((F(0), F(1, 4), F(3, 4), F(1)), repeat=n):
            lhs = sum((1 - c*c) * math.prod(cs[:i] + cs[i+1:])
                      for i, c in enumerate(cs))
            rhs = 1 - math.prod(cs) ** 2
            assert lhs <= rhs
            tensor_count += 1
    return {'exact_conditional_mean_cases': count,
            'exact_scalar_tensor_cases': tensor_count, 'status': 'PASS'}


def product_laplace_check() -> dict:
    # m=2 member has n=16. Permutation symmetry reduces ALL J,T choices
    # to j=|J|, a=|J intersect T|, b=|T minus J|.
    p, n = F(1, 4), 16
    c = 1 - 2*p
    count = 0
    for s in (F(k, 16) for k in range(17)):
        z0, z1 = 1-p+p*s, p+(1-p)*s
        u0, u1 = 1-p-p*s, (1-p)*s-p
        exponent = (1-s)/(1+s)
        for j in range(1, n+1):
            for a in range(j+1):
                for b in range(n-j+1):
                    ordinary = z0 ** (n-a-b) * z1 ** (a+b)
                    signed = z0 ** (n-j-b) * z1 ** b * u0 ** (j-a) * u1 ** a
                    for y in (-1, 1):
                        r = (1+y*c**j)/2
                        L = (ordinary+y*signed)/(1+y*c**j)
                        assert 0 <= L <= 1
                        assert L ** exponent.denominator <= r ** exponent.numerator
                        count += 1
    # Independent direct truth-table check of the symmetry formula.
    formula_count = 0
    for n0 in range(1, 5):
        xs = list(range(1 << n0))
        probs = [p**x.bit_count()*(1-p)**(n0-x.bit_count()) for x in xs]
        for s in (F(0), F(1, 3), F(1)):
            z0, z1 = 1-p+p*s, p+(1-p)*s
            u0, u1 = 1-p-p*s, (1-p)*s-p
            for J in range(1, 1 << n0):
                j = J.bit_count()
                for T in xs:
                    a, b = (T & J).bit_count(), (T & ~J).bit_count()
                    ordinary = z0**(n0-a-b)*z1**(a+b)
                    signed = z0**(n0-j-b)*z1**b*u0**(j-a)*u1**a
                    for y in (-1, 1):
                        direct = sum(probs[x]*s**((x ^ T).bit_count())
                                     for x in xs if (-1)**((x & J).bit_count()) == y)
                        assert direct == (ordinary+y*signed)/2
                        formula_count += 1
    family = []
    for m in (2, 4, 6, 10, 20):
        p0 = 2.0 ** (-m)
        h = m*p0 - (1-p0)*math.log1p(-p0)/math.log(2)
        family.append({'m': m, 'dimension': 2*m*(1 << m),
                       'expected_size_exact': 2*m,
                       'entropy_over_expected_size_float': h/p0,
                       'ratio_lower_bound_exact': m})
    return {'status': 'PASS', 'exact_symmetry_grid_cases': count,
            'exact_direct_formula_comparisons': formula_count,
            'continuum_proof': 'analytic in REPORT.md, not inferred from this grid',
            'large_dimension_values': family}


def phase_check() -> dict:
    summaries = []
    total_compressed = 0
    exact_entropy_patterns = set()
    exact_entropy_instances = 0
    for n in range(0, 5):
        N = 1 << n
        ids = np.arange(1 << N, dtype=np.uint32)
        values = 1 - 2*((ids[:, None] >> np.arange(N, dtype=np.uint32)) & 1).astype(np.int64)
        W = walsh(values)
        assert np.all(np.sum(W*W, axis=1) == N*N)
        bitweights = np.left_shift(np.uint32(1), np.arange(N, dtype=np.uint32))
        support = np.sum((W != 0).astype(np.uint32)*bitweights, axis=1, dtype=np.uint32)
        negative = np.sum((W < 0).astype(np.uint32)*bitweights, axis=1, dtype=np.uint32)
        monomials = [(1 << N)-1]
        monomials += [sum(((s >> i) & 1) << s for s in range(N)) for i in range(n)]
        edges = list(combinations(range(n), 2))
        monomials += [sum((((s >> i) & 1)*((s >> j) & 1)) << s for s in range(N))
                      for i, j in edges]
        qmasks = [0]
        for z in monomials:
            qmasks += [v ^ z for v in qmasks]
        best = np.full(len(ids), 99, dtype=np.int8)
        chosen = np.zeros(len(ids), dtype=np.uint16)
        qrows = []
        for code, mask in enumerate(qmasks):
            rows = [0]*n
            for e, (i, j) in enumerate(edges):
                if code >> (n+1+e) & 1:
                    rows[i] ^= 1 << j
                    rows[j] ^= 1 << i
            rb = basis(rows, n)
            qrows.append(rb)
            rank = len(rb)
            good = (((negative ^ np.uint32(mask)) & support) == 0) & (rank < best)
            best[good], chosen[good] = rank, code
        degree = np.array([s.bit_count() for s in range(N)], dtype=np.int64)
        odd = degree % 2
        I_num = (W*W) @ degree
        p = W.astype(float)**2/(N*N)
        H = -(p*np.log2(np.where(p > 0, p, 1))).sum(axis=1)
        ok = best != 99
        for code in np.unique(chosen[ok]):
            group = np.where(ok & (chosen == code))[0]
            rows = qrows[int(code)]
            r = len(rows)
            labels = [sum(((s & row).bit_count() % 2) << j for j, row in enumerate(rows))
                      for s in range(N)]
            compressed = np.zeros((len(group), 1 << r), dtype=np.int64)
            occupancy = np.zeros_like(compressed)
            for s, label in enumerate(labels):
                compressed[:, label] += W[group, s]
                occupancy[:, label] += W[group, s] != 0
            assert np.all(occupancy <= 1)
            assert np.all(np.sum(occupancy, axis=1) <= 1 << r)
            # Fourier coefficients are W/N. No floating arithmetic enters.
            physical = walsh(compressed)
            assert np.all(np.abs(physical) == N)
            total_compressed += len(group)
            if r == 0:
                assert np.all(np.sum(W[group] != 0, axis=1) == 1)
            if r == 2:
                assert np.all(np.sum(W[group] != 0, axis=1) == 4)
                assert np.all((W[group] == 0) | (np.abs(W[group]) == N//2))
                assert np.all(I_num[group] >= N*N)
        valid_ratio = ok & (I_num > 0)
        ratios = H[valid_ratio]/(I_num[valid_ratio]/(N*N))
        corrected_num = I_num - (W*W) @ odd
        nontrivial = ok & (corrected_num > 0)
        amp = H[nontrivial]/(corrected_num[nontrivial]/(N*N))
        max_amp = float(amp.max()) if len(amp) else 0.0
        assert max_amp <= 4 + 1e-10
        # H <= 4(I-odd_mass) is also checked without evaluating any logarithm.
        # After multiplying by N^2 it is product_s (W_s^2)^(W_s^2)
        # >= 2^(2*n*N^2 - 4*corrected_num). Cache amplitude histograms.
        magnitudes = sorted(set(int(v) for v in np.unique(np.abs(W[ok]))) - {0})
        for j in np.where(ok)[0]:
            histogram = tuple((v, int(np.sum(np.abs(W[j]) == v))) for v in magnitudes)
            exponent = int(2*n*N*N - 4*corrected_num[j])
            pattern = (histogram, exponent)
            if pattern not in exact_entropy_patterns:
                lhs = math.prod((v*v)**(v*v*count) for v, count in histogram)
                assert exponent <= 0 or lhs >= 1 << exponent
                exact_entropy_patterns.add(pattern)
            exact_entropy_instances += 1
        summaries.append({'n': n, 'all_boolean_functions': len(ids),
                          'quadratic_phase_compatible': int(ok.sum()),
                          'minimal_polar_rank_counts': {('not_quadratic' if r == 99 else str(int(r))): int(np.sum(best == r))
                                                       for r in np.unique(best)},
                          'max_H_over_I_float': float(ratios.max()) if len(ratios) else 0.0,
                          'max_H_over_I_minus_odd_mass_float': max_amp})
    return {'status': 'PASS', 'integer_compression_instances': total_compressed,
            'exact_corrected_entropy_instances': exact_entropy_instances,
            'distinct_integer_entropy_comparisons':len(exact_entropy_patterns),
            'summaries': summaries,
            'warning': 'entropy ratio maxima are floating diagnostics; compression and corrected-entropy inequality tests are integer-exact; no higher-dimensional quadratic-phase FEI theorem is claimed'}



def robust_phase_check() -> dict:
    rng = np.random.default_rng(20260921)
    count = 0
    max_entropy_excess = 0.0
    for n in range(1, 7):
        N = 1 << n
        edges = list(combinations(range(n), 2))
        for _ in range(256):
            v = rng.choice(np.array([-1, 1], dtype=np.int64), size=N)
            W = walsh(v)
            linear = int(rng.integers(N))
            edge_code = int(rng.integers(1 << len(edges)))
            rows = [0]*n
            for e, (i, j) in enumerate(edges):
                if edge_code >> e & 1:
                    rows[i] ^= 1 << j
                    rows[j] ^= 1 << i
            rb = basis(rows, n)
            r = len(rb)
            def q(s):
                return ((s & linear).bit_count() +
                        sum(((s >> i) & 1)*((s >> j) & 1)
                            for e, (i, j) in enumerate(edges) if edge_code >> e & 1)) % 2
            labels = [sum(((s & row).bit_count() % 2) << j
                          for j, row in enumerate(rb)) for s in range(N)]
            radical = [s for s in range(N) if labels[s] == 0]
            x0 = next(x for x in range(N)
                      if all(((x & u).bit_count() % 2) == q(u) for u in radical))
            positive = np.zeros(1 << r, dtype=np.int64)
            negative = np.zeros_like(positive)
            quotient_mass_num = np.zeros_like(positive)
            actual = np.zeros_like(positive)
            for s, t in enumerate(labels):
                if W[s] * (-1)**q(s) >= 0:
                    positive[t] += abs(W[s])
                else:
                    negative[t] += abs(W[s])
                quotient_mass_num[t] += W[s]*W[s]
                actual[t] += W[s] * (-1)**((x0 & s).bit_count())
            assert np.all(actual*actual == (positive-negative)**2)
            assert int(np.sum(actual*actual)) == N*N
            assert np.all(np.abs(walsh(actual)) == N)
            absolute = positive + negative
            L1_bad_num = int(negative.sum())
            assert int(np.sum(absolute*absolute)) <= (N+2*L1_bad_num)**2
            p0 = W.astype(float)**2/(N*N)
            p1 = quotient_mass_num.astype(float)/(N*N)
            H0 = -float(np.sum(p0*np.log2(np.where(p0 > 0, p0, 1))))
            H1 = -float(np.sum(p1*np.log2(np.where(p1 > 0, p1, 1))))
            conditional_bound = math.log2(int(np.sum(absolute*absolute))/(N*N))
            assert H0-H1 <= conditional_bound+1e-12
            max_entropy_excess = max(max_entropy_excess, H0-H1-conditional_bound)
            assert H0 <= r+2*math.log2(1+2*L1_bad_num/N)+1e-12
            count += 1
    # Direct 9-bit two-level ternary majority check.
    N = 1 << 9
    vals = []
    for x in range(N):
        bits = [1-2*((x >> i) & 1) for i in range(9)]
        children = [1 if sum(bits[3*j:3*j+3]) > 0 else -1 for j in range(3)]
        vals.append(1 if sum(children) > 0 else -1)
    W = walsh(np.array(vals, dtype=np.int64))
    H_num = I_num = 0
    for s, w in enumerate(W):
        if w:
            assert s.bit_count() % 2 == 1
            assert (w > 0) == (((s.bit_count()*(s.bit_count()-1)//2) % 2) == 0)
            a = abs(int(w))
            assert a & (a-1) == 0
            H_num += int(w*w)*2*(9-(a.bit_length()-1))
            I_num += int(w*w)*s.bit_count()
    assert F(H_num,N*N) == 5
    assert F(I_num,N*N) == F(9,4)
    # Influence is not preserved by entropy-preserving linear restriction.
    # f=x1, Q(s)=s1*s2, L has rows (1,1),(1,0): g=y1*y2.
    assert walsh(np.array([1,-1,1,-1])).tolist() == [0,4,0,0]
    assert walsh(np.array([1,-1,-1,1])).tolist() == [0,0,0,4]
    return {'status':'PASS', 'seed':20260921,
            'integer_robust_phase_cases':count,
            'entropy_diagnostics':'floating, never substituted for analytic proof',
            'max_conditional_entropy_bound_excess_float':max_entropy_excess,
            'recursive_majority_9_exact':{'H':'5','I':'9/4','support':int(np.sum(W != 0))},
            'influence_increase_example_exact':{'original_I':1,'compressed_I':2}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', choices=['mean', 'laplace', 'phase', 'robust', 'all'], default='all')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    funcs = {'mean': parity_mean_check, 'laplace': product_laplace_check, 'phase': phase_check, 'robust': robust_phase_check}
    chosen = funcs if args.part == 'all' else {args.part: funcs[args.part]}
    result = {'schema_version': 1, 'full_FEI': 'OPEN_NOT_PROVED',
              'checks': {name: fun() for name, fun in chosen.items()}}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    print(text)

if __name__ == '__main__':
    main()
