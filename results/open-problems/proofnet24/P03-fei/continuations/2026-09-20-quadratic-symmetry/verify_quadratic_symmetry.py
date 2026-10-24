#!/usr/bin/env python3
"""Exact finite checks for quadratic twists of block-symmetric Boolean functions.

Python standard library only. The infinite-dimensional proofs are in REPORT.md;
these checks are not substitutes for the proof or independent review.
All Walsh transforms, influence comparisons, Parseval identities, and structural
checks are integer/rational. Logarithms use rigorously enclosed atanh series,
then are rounded outwards to a dyadic grid. No floating-point test decides PASS.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import random

SCALE = 1 << 80
BASE = F(301, 25)  # Published OWZ symmetric constant, 12.04.
SEED = 20260920
EXTRA_CHECKS = Counter()


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def walsh(values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    a = list(values)
    require(len(a) > 0 and len(a) & (len(a) - 1) == 0, 'Power-of-two table required')
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return tuple(a)


def ln_unit_interval(x: F, terms: int = 40) -> tuple[F, F]:
    """Enclose ln(x), for 1 <= x <= 2, by the positive atanh series."""
    require(F(1) <= x <= F(2), 'Log range reduction failed')
    z = (x-1)/(x+1)
    zz, power, total = z*z, z, F(0)
    for k in range(terms):
        total += power/(2*k+1)
        power *= zz
    lo = 2*total
    tail = 2*power/((2*terms+1)*(1-zz))
    return lo, lo+tail


LN2 = ln_unit_interval(F(2))


@lru_cache(maxsize=None)
def log2_integer(k: int) -> tuple[int, int]:
    """Dyadic lower/upper integer numerators, denominator SCALE."""
    require(k >= 1, 'Positive logarithm argument required')
    e = k.bit_length()-1
    if k == 1 << e:
        return e*SCALE, e*SCALE
    lo, hi = ln_unit_interval(F(k, 1 << e))
    lo, hi = F(e)+lo/LN2[1], F(e)+hi/LN2[0]
    a, b = lo*SCALE, hi*SCALE
    return a.numerator//a.denominator, -((-b.numerator)//b.denominator)


@lru_cache(maxsize=None)
def entropy_histogram(n: int, hist: tuple[tuple[int, int], ...]) -> tuple[F, F]:
    """H = 2n - (2/4^n) sum |Walsh(f)|^2 log2 |Walsh(f)|."""
    lo_sum = hi_sum = 0
    for a, multiplicity in hist:
        if a:
            lo, hi = log2_integer(a)
            lo_sum += multiplicity*a*a*lo
            hi_sum += multiplicity*a*a*hi
    denom = (1 << (2*n))*SCALE
    return F(2*n)-F(2*hi_sum, denom), F(2*n)-F(2*lo_sum, denom)


def entropy_bounds(a: tuple[int, ...]) -> tuple[F, F]:
    n = len(a).bit_length()-1
    return entropy_histogram(n, tuple(sorted(Counter(abs(v) for v in a).items())))


def entropy_signature(a):
    """Exact rational linear form in logarithms of odd primes; key 1 is constant."""
    n, N = len(a).bit_length()-1, len(a)
    coeff = {1: F(2*n)}
    for value, multiplicity in Counter(abs(v) for v in a).items():
        if value == 0:
            continue
        weight = F(-2*value*value*multiplicity, N*N)
        k, prime = value, 2
        while prime*prime <= k:
            exponent = 0
            while k % prime == 0:
                exponent += 1
                k //= prime
            if exponent:
                key = 1 if prime == 2 else prime
                coeff[key] = coeff.get(key, F(0)) + weight*exponent
            prime += 1
        if k > 1:
            key = 1 if k == 2 else k
            coeff[key] = coeff.get(key, F(0)) + weight
    return {p: v for p, v in coeff.items() if v}


def certify_entropy_deletion(full, leaf_tables, k):
    """Cancel common logarithms before enclosing an exact equality."""
    coeff = entropy_signature(full)
    for a in leaf_tables:
        for p, v in entropy_signature(a).items():
            coeff[p] = coeff.get(p, F(0)) - v/(1 << k)
    coeff[1] = coeff.get(1, F(0)) - 2*k
    upper = coeff.get(1, F(0))
    for p, v in coeff.items():
        if p == 1 or not v:
            continue
        lo, hi = log2_integer(p)
        upper += v*F(hi if v > 0 else lo, SCALE)
    require(upper <= 0, 'Symbolically cancelled entropy deletion was not certified')
    EXTRA_CHECKS['symbolic_entropy_cancellation_certificates'] += 1



def measure(f: tuple[int, ...]) -> dict:
    n, N = len(f).bit_length()-1, len(f)
    require(all(v in (-1, 1) for v in f), 'Boolean table required')
    a = walsh(f)
    require(sum(v*v for v in a) == N*N, 'Parseval failure')
    counts = tuple(sum(f[x] != f[x ^ (1 << i)] for x in range(N)) for i in range(n))
    for i in range(n):
        require(sum(v*v for s, v in enumerate(a) if s >> i & 1) == N*counts[i],
                'Fourier versus physical influence mismatch')
    folded = tuple(min(c, N-c) for c in counts)
    return {'a': a, 'counts': counts, 'folded': folded, 'J': F(sum(folded), N),
            'I': F(sum(counts), N), 'H': entropy_bounds(a)}


def partitions(n: int):
    """Each set partition once; blocks and their elements have canonical order."""
    def visit(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from visit(i+1, blocks)
            blocks[j].pop()
        blocks.append([i])
        yield from visit(i+1, blocks)
        blocks.pop()
    yield from visit(0, [])


def masks_of(parts):
    return tuple(sum(1 << i for i in block) for block in parts)


def graph_rows(n: int, graph: int):
    rows = [0]*n
    for b, (i, j) in enumerate(combinations(range(n), 2)):
        if graph >> b & 1:
            rows[i] |= 1 << j
            rows[j] |= 1 << i
    return tuple(rows)


def phase_table(n: int, rows, linear: int = 0):
    vals = []
    for x in range(1 << n):
        q = (x & linear).bit_count() & 1
        for i in range(n):
            if x >> i & 1:
                q ^= (x & rows[i] & ~((1 << (i+1))-1)).bit_count() & 1
        vals.append(1-2*q)
    return tuple(vals)


def group_masks(parts, groups):
    pm = masks_of(parts)
    return tuple(sum(pm[r] for r in group) for group in groups)


def classify(n: int, rows, parts, groups):
    """Disjoint sets: cross-factor endpoints, then within-factor mixed rows."""
    gm = group_masks(parts, groups)
    pm = masks_of(parts)
    cross, mixed = [], []
    for i in range(n):
        gi = next(t for t, mask in enumerate(gm) if mask >> i & 1)
        if rows[i] & ~gm[gi]:
            cross.append(i)
            continue
        for r in groups[gi]:
            mask = pm[r] & ~(1 << i)
            if (rows[i] & mask) not in (0, mask):
                mixed.append(i)
                break
    return tuple(cross), tuple(mixed)


def core_features(n: int, parts, groups):
    """Mixed-radix block-weight indices for every independent factor."""
    pm = masks_of(parts)
    features, dimensions = [], []
    for group in groups:
        dim = 1
        for r in group:
            dim *= len(parts[r])+1
        dimensions.append(dim)
        vals = []
        for x in range(1 << n):
            idx, mult = 0, 1
            for r in group:
                idx += (x & pm[r]).bit_count()*mult
                mult *= len(parts[r])+1
            vals.append(idx)
        features.append(tuple(vals))
    return tuple(features), tuple(dimensions)


def seed_table(features, codes):
    N = len(features[0])
    return tuple(1-2*(sum((code >> feat[x]) & 1 for code, feat in zip(codes, features)) & 1)
                 for x in range(N))


def embed(x: int, indices):
    return sum(((x >> b) & 1) << i for b, i in enumerate(indices))


def structural_graph_check(n: int, rows, parts, groups):
    cross, mixed = classify(n, rows, parts, groups)
    removed = set(cross+mixed)
    residual_parts = [tuple(i for i in p if i not in removed) for p in parts]
    gm = group_masks(parts, groups)
    for i in range(n):
        if i in removed:
            continue
        own = next(mask for mask in gm if mask >> i & 1)
        require(not (rows[i] & ~own), 'Residual cross-factor edge')
    for r, a in enumerate(residual_parts):
        vals = {bool(rows[i] >> j & 1) for i, j in combinations(a, 2)}
        require(len(vals) <= 1, 'Nonconstant residual within-part graph')
        for b in residual_parts[r+1:]:
            vals = {bool(rows[i] >> j & 1) for i in a for j in b}
            require(len(vals) <= 1, 'Nonconstant residual between-part graph')
    return cross, mixed


def verify_case(n: int, rows, parts, groups, f: tuple[int, ...], linear: int = 0,
                leaves: bool = False):
    cross, mixed = structural_graph_check(n, rows, parts, groups)
    m, N = measure(f), 1 << n
    for i in cross:
        require(2*m['folded'][i] == N, 'Cross-factor coordinate not exactly half-influential')
    for i in mixed:
        require(4*m['folded'][i] >= N, 'Mixed coordinate violates quarter-influence payment')
    d = max(map(len, groups))
    c_lo = BASE + F(log2_integer(d)[0], SCALE)
    paid = F(len(cross), 2)+F(len(mixed), 4)
    require(m['J'] >= paid, 'Negative unpaid influence')
    rhs_lo = c_lo*(m['J']-paid)+2*(len(cross)+len(mixed))
    require(m['H'][1] <= rhs_lo, 'Certified entropy bound failed')
    leaf_count = 0
    if leaves:
        E = tuple(sorted(cross+mixed))
        R = tuple(i for i in range(n) if i not in E)
        k, r = len(E), len(R)
        index = {i: j for j, i in enumerate(R)}
        sum_squares = [0]*(1 << r)
        sum_folded = F(0)
        leaf_H_lo = F(0)
        leaf_tables = []
        for z in range(1 << k):
            fixed = embed(z, E)
            leaf = tuple(f[fixed | embed(y, R)] for y in range(1 << r))
            lm = measure(leaf)
            leaf_tables.append(lm['a'])
            leaf_count += 1
            sum_folded += lm['J']
            leaf_H_lo += lm['H'][0]
            for s, a in enumerate(lm['a']):
                sum_squares[s] += a*a
            newlin = sum((((linear >> i) & 1) ^ ((rows[i] & fixed).bit_count() & 1)) << index[i]
                         for i in R)
            unlinear = tuple(v*(1-2*((y & newlin).bit_count() & 1)) for y, v in enumerate(leaf))
            for part in parts:
                pr = tuple(index[i] for i in part if i in index)
                for a, b in combinations(pr, 2):
                    for y in range(1 << r):
                        if ((y >> a) ^ (y >> b)) & 1:
                            require(unlinear[y] == unlinear[y ^ (1 << a) ^ (1 << b)],
                                    'Restricted core lost part symmetry')
            gmr = tuple(sum(1 << index[i] for i in R if mask >> i & 1)
                        for mask in group_masks(parts, groups))
            for y in range(1 << r):
                prod = 1
                for mask in gmr:
                    prod *= unlinear[y & mask]
                require(prod == unlinear[y]*unlinear[0]**(len(groups)-1),
                        'Restricted core lost factorization')
        marginal = [0]*(1 << r)
        for s, a in enumerate(m['a']):
            label = sum(((s >> i) & 1) << index[i] for i in R)
            marginal[label] += a*a
        require(all(v == (1 << k)*w for v, w in zip(marginal, sum_squares)),
                'Partial Parseval mixture identity failed')
        remain_J = F(sum(m['folded'][i] for i in R), N)
        require(sum_folded/(1 << k) <= remain_J, 'Folded influence concavity failed')
        if k and m['H'][1] > leaf_H_lo/(1 << k)+2*k:
            certify_entropy_deletion(m['a'], leaf_tables, k)
    return leaf_count


def summary_number(q: F):
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def data_summary(f):
    m = measure(f)
    return {'dimension': len(f).bit_length()-1, 'H_interval': list(map(summary_number, m['H'])),
            'I': summary_number(m['I']), 'J': summary_number(m['J']),
            'influences': [summary_number(F(c, len(f))) for c in m['counts']]}


def run():
    counts = Counter()
    for n in range(1, 6):
        for parts in partitions(n):
            for graph in range(1 << (n*(n-1)//2)):
                rows = graph_rows(n, graph)
                for groups in ((tuple(range(len(parts))),), tuple((i,) for i in range(len(parts)))):
                    structural_graph_check(n, rows, parts, groups)
                    counts['graph_partition_factorization_checks'] += 1
    for n in range(1, 6):
        parts, groups = (tuple(range(n)),), ((0,),)
        feat, dims = core_features(n, parts, groups)
        for graph in range(1 << (n*(n-1)//2)):
            rows = graph_rows(n, graph)
            phase = phase_table(n, rows)
            for code in range(1 << dims[0]):
                h = seed_table(feat, (code,))
                f = tuple(a*b for a, b in zip(h, phase))
                counts['leaf_tables_checked'] += verify_case(n, rows, parts, groups, f, leaves=(n <= 3))
                counts['exhaustive_symmetric_core_graph_cases'] += 1
    for n in range(1, 4):
        for parts in partitions(n):
            groups = (tuple(range(len(parts))),)
            feat, dims = core_features(n, parts, groups)
            for graph in range(1 << (n*(n-1)//2)):
                rows = graph_rows(n, graph)
                for linear in range(1 << n):
                    phase = phase_table(n, rows, linear)
                    for code in range(1 << dims[0]):
                        f = tuple(a*b for a, b in zip(seed_table(feat, (code,)), phase))
                        counts['leaf_tables_checked'] += verify_case(n, rows, parts, groups, f, linear, True)
                        counts['exhaustive_partition_core_graph_linear_cases'] += 1
    rng = random.Random(SEED)
    for n in range(4, 11):
        for trial in range(120):
            d = rng.randint(1, min(n, 5))
            labels = list(range(d))+[rng.randrange(d) for _ in range(n-d)]
            rng.shuffle(labels)
            parts = tuple(tuple(i for i in range(n) if labels[i] == a) for a in range(d))
            groups = rng.choice(tuple(partitions(d)))
            feat, dims = core_features(n, parts, groups)
            codes = tuple(rng.getrandbits(dim) for dim in dims)
            if trial % 2:
                graph = rng.getrandbits(n*(n-1)//2)
            else:
                graph = sum((rng.randrange(8) == 0) << b for b in range(n*(n-1)//2))
            rows = graph_rows(n, graph)
            linear = rng.getrandbits(n)
            f = tuple(a*b for a, b in zip(seed_table(feat, codes), phase_table(n, rows, linear)))
            counts['leaf_tables_checked'] += verify_case(n, rows, parts, groups, f, linear, True)
            counts['random_product_part_symmetric_cases'] += 1
    # Universal pair budget, with no symmetry hypothesis on the base.
    for n in range(1, 4):
        N = 1 << n
        for table in range(1 << N):
            h = tuple(1-2*((table >> x) & 1) for x in range(N))
            hm = measure(h)
            for graph in range(1 << (n*(n-1)//2)):
                rows = graph_rows(n, graph)
                # Linear output factors preserve all folded influences.
                f = tuple(a*b for a, b in zip(h, phase_table(n, rows)))
                fm = measure(f)
                for i in range(n):
                    if rows[i]:
                        require(2*(hm['folded'][i]+fm['folded'][i]) >= N,
                                'Universal quadratic pair budget failed')
                        counts['universal_pair_budget_coordinate_checks'] += 1
                counts['universal_pair_budget_function_graph_cases'] += 1
    original = (1, -1, -1, 1, -1, 1, -1, 1)
    compressed = (-1, 1, -1, 1, -1, 1, -1, 1)
    require(measure(original)['H'] == (F(2), F(2)), 'Compression input entropy')
    require(measure(compressed)['H'] == (F(0), F(0)), 'Compression output entropy')
    require(measure(original)['I'] == 2 and measure(compressed)['I'] == 1, 'Compression influences')
    rare = []
    for degree in range(4, 11):
        n = degree+1
        f = tuple(1-2*((x & ((1 << degree)-1)) == (1 << degree)-1) for x in range(1 << n))
        m = measure(f)
        require(all(F(c, 1 << n) == F(1, 1 << (degree-1)) for c in m['folded'][:degree]),
                'Rare monomial influence formula')
        require(m['folded'][degree] == 0, 'Unused coordinate must be irrelevant')
        require(f[(1 << degree)-1] != f[((1 << degree)-1) ^ 1 ^ (1 << degree)],
                'Rare example accidentally fully symmetric')
        rare.append({'degree': degree, 'dimension': n, 'nonzero_folded_influence': summary_number(F(1, 1 << (degree-1)))})
    counts.update(EXTRA_CHECKS)
    return {'status': 'PASS', 'seed': SEED, 'counts': dict(counts),
            'arithmetic': 'Integer Walsh transforms and influence counts; Fraction atanh-series logarithm enclosures, outward rounded at 2^-80.',
            'tested_constant': '301/25 + log2(maximum number of symmetric parts in any independent factor)',
            'stronger_defect_payment_tested': 'H <= C*(J - |E_cross|/2 - |E_mixed|/4) + 2*(|E_cross|+|E_mixed|)',
            'compression_shortcut_counterexample': {'original': list(original), 'compressed': list(compressed),
                                                    'original_metrics': data_summary(original), 'compressed_metrics': data_summary(compressed)},
            'higher_degree_counting_obstruction': rare,
            'scope': 'Finite exact checks of the stated class and proof ingredients. Not a proof of full FEI, a priority clearance, independent review, or formal verification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('verification.json'))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
