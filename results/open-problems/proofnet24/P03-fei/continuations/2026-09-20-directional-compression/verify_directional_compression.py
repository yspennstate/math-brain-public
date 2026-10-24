#!/usr/bin/env python3
"""Reproducible finite checks for directional FEI compression.

Only integer/Fraction arithmetic is used for assertions. Entropy logarithms
are enclosed by rational atanh-series intervals. Finite checks supplement,
and do not replace, the all-dimensional proofs in REPORT.md.
Requires Python >=3.10 and NumPy. Run: python verify_directional_compression.py
"""
from __future__ import annotations
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import numpy as np

SEED = 20260920


def dimension(length: int) -> int:
    if length < 1 or length & (length - 1):
        raise ValueError('Truth-table length must be a positive power of two.')
    return length.bit_length() - 1


def anf_degrees(tables: np.ndarray) -> np.ndarray:
    a = np.asarray(tables, dtype=np.uint8).copy()
    if a.ndim == 1:
        a = a[None, :]
    n = dimension(a.shape[1])
    for i in range(n):
        r = a.reshape(a.shape[0], -1, 2 << i)
        r[:, :, 1 << i:] ^= r[:, :, :1 << i]
    weights = np.array([x.bit_count() for x in range(1 << n)])
    return np.max(np.where(a != 0, weights[None, :], -1), axis=1)


def all_truth_tables(n: int) -> np.ndarray:
    return ((np.arange(1 << (1 << n), dtype=np.uint64)[:, None]
             >> np.arange(1 << n, dtype=np.uint64)[None, :]) & 1).astype(np.uint8)


def folded_counts(table: np.ndarray) -> np.ndarray:
    n = dimension(len(table)); x = np.arange(len(table))
    counts = np.array([np.count_nonzero(table ^ table[x ^ (1 << i)]) for i in range(n)])
    return np.minimum(counts, len(table) - counts)


def eligible_directions(table: np.ndarray, d: int = 2) -> np.ndarray:
    x = np.arange(len(table))
    ds = table[None, :] ^ table[x[None, :] ^ x[:, None]]
    return np.flatnonzero(anf_degrees(ds) <= d)


def compress_code(tables: np.ndarray) -> np.ndarray:
    return tables.astype(np.uint64) @ (np.uint64(1) << np.arange(tables.shape[1], dtype=np.uint64))


def exact_small_checks() -> dict:
    counts = dict(functions=0, nonzero_direction_pairs=0,
                  nonconstant_low_degree_coordinate_certificates=0,
                  subspace_closure_implications=0, restriction_inclusions=0)
    eligible_by_n: dict[int, np.ndarray] = {}
    for n in range(1, 5):
        tables = all_truth_tables(n); N = 1 << n; x = np.arange(N)
        eligible = np.ones((len(tables), N), dtype=bool)
        folds = np.stack([np.minimum(np.sum(tables ^ tables[:, x ^ (1 << j)], axis=1),
                                    N - np.sum(tables ^ tables[:, x ^ (1 << j)], axis=1))
                          for j in range(n)], axis=1)
        for v in range(1, N):
            deriv = tables ^ tables[:, x ^ v]
            degrees = anf_degrees(deriv)
            eligible[:, v] = degrees <= 2
            counts['nonzero_direction_pairs'] += len(tables)
            for d in (1, 2):
                for j in range(n):
                    varies = np.any(deriv ^ deriv[:, x ^ (1 << j)], axis=1)
                    mask = (degrees <= d) & (degrees >= 1) & varies
                    assert np.all((1 << d) * folds[mask, j] >= N)
                    counts['nonconstant_low_degree_coordinate_certificates'] += int(mask.sum())
        for v in range(N):
            for w in range(N):
                mask = eligible[:, v] & eligible[:, w]
                assert np.all(eligible[mask, v ^ w])
                counts['subspace_closure_implications'] += int(mask.sum())
        sizes = eligible.sum(axis=1)
        assert np.all((sizes & (sizes - 1)) == 0)
        if n > 1:
            child_eligible = eligible_by_n[n - 1]
            for j in range(n):
                for b in (0, 1):
                    ids = x[((x >> j) & 1) == b]
                    codes = compress_code(tables[:, ids]).astype(np.int64)
                    for v in range(N):
                        if v & (1 << j):
                            continue
                        residual = (v & ((1 << j) - 1)) | ((v >> (j + 1)) << j)
                        mask = eligible[:, v]
                        assert np.all(child_eligible[codes[mask], residual])
                        counts['restriction_inclusions'] += int(mask.sum())
        counts['functions'] += len(tables)
        eligible_by_n[n] = eligible
    counts['scope'] = 'Every Boolean function in dimensions 1 through 4; all nonzero directions; d=1 and d=2.'
    return counts


def robust_small_checks() -> dict:
    pairs = positive = certificates = 0
    for n in range(1, 4):
        tables = all_truth_tables(n); N = 1 << n; x = np.arange(N)
        qs = tables[anf_degrees(tables) <= 2]
        qdeg = anf_degrees(qs)
        qvar = np.stack([np.any(qs ^ qs[:, x ^ (1 << j)], axis=1) for j in range(n)], axis=1)
        # For each proposed quadratic q, require epsilon < 1/4.
        for table in tables:
            folds = folded_counts(table)
            for v in range(1, N):
                dv = table ^ table[x ^ v]
                errs = np.sum(qs ^ dv[None, :], axis=1)
                pairs += len(qs)
                good = (qdeg >= 1) & (4 * errs < N)
                positive += int(good.sum())
                for j in range(n):
                    use = good & qvar[:, j]
                    assert np.all(4 * folds[j] >= N - 4 * errs[use])
                    certificates += int(use.sum())
    return dict(candidate_triples=pairs, nonconstant_positive_certificates=positive,
                coordinate_assertions=certificates,
                scope='Every f, nonzero v, and degree-at-most-two q in dimensions 1 through 3; exact Hamming errors.')


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return len(pivots)


def exact_tree_checks() -> dict:
    rng = np.random.default_rng(SEED)
    stats = dict(roots=0, nodes=0, paid_nodes=0, zero_cost_nodes=0, leaves=0, normal_form_assertions=0)
    def check_normal_form(table: np.ndarray) -> None:
        n = dimension(len(table)); dirs = eligible_directions(table)
        basis: list[int] = []
        for v in dirs:
            v = int(v)
            if gf2_rank(basis + [v]) > len(basis):
                basis.append(v)
        r = len(basis)
        assert len(dirs) == (1 << r)
        for j in range(n):
            if gf2_rank(basis + [1 << j]) > len(basis):
                basis.append(1 << j)
        assert len(basis) == n
        mapped = []
        for y in range(len(table)):
            x = 0
            for i,b in enumerate(basis):
                if y & (1 << i): x ^= b
            mapped.append(x)
        coeff = table[np.array(mapped)].copy()
        for j in range(n):
            a = coeff.reshape(-1,2 << j)
            a[:,1 << j:] ^= a[:,:1 << j]
        for monomial in np.flatnonzero(coeff):
            if int(monomial) & ((1 << r)-1):
                assert int(monomial).bit_count() <= 3
        stats['normal_form_assertions'] += 1
    def visit(table: np.ndarray, depth: int) -> None:
        n = dimension(len(table)); N = len(table); x = np.arange(N)
        dirs = eligible_directions(table)
        assert len(dirs) >= (1 << depth)
        if depth == 0:
            stats['leaves'] += 1
            return
        v = int(dirs[1]); dv = table ^ table[x ^ v]
        constant = bool(np.all(dv == dv[0]))
        if constant:
            j = (v & -v).bit_length() - 1
            stats['zero_cost_nodes'] += 1
        else:
            j = next(j for j in range(n) if np.any(dv ^ dv[x ^ (1 << j)]))
            assert 4 * int(folded_counts(table)[j]) >= N
            stats['paid_nodes'] += 1
        stats['nodes'] += 1
        parent_fold_sum = int(folded_counts(table).sum())
        child_fold_sum = 0
        for b in (0, 1):
            child = table[((x >> j) & 1) == b]
            child_fold_sum += int(folded_counts(child).sum())
            visit(child, depth - 1)
        assert child_fold_sum <= parent_fold_sum - int(folded_counts(table)[j])
    # Affinely scrambled high-degree cores, with arbitrary random cubic additions.
    # Constant directional derivatives are included separately through affine functions.
    for n in range(5, 9):
        N = 1 << n; x = np.arange(N)
        for repeat in range(8):
            k = min(5, n - 1)
            rows: list[int] = []
            while len(rows) < k:
                row = int(rng.integers(1, N))
                if gf2_rank(rows + [row]) > len(rows):
                    rows.append(row)
            y = np.zeros(N, dtype=np.int64)
            for i, row in enumerate(rows):
                y |= np.array([(int(z) & row).bit_count() & 1 for z in x]) << i
            core = rng.integers(0, 2, size=1 << k, dtype=np.uint8)
            table = core[y].copy()
            for monomial in range(N):
                if monomial.bit_count() <= 3 and rng.integers(0, 2):
                    table ^= ((x & monomial) == monomial).astype(np.uint8)
            assert len(eligible_directions(table)) >= 1 << (n - k)
            check_normal_form(table)
            visit(table, n - k); stats['roots'] += 1
        affine = np.array([int(z).bit_count() & 1 for z in x], dtype=np.uint8)
        check_normal_form(affine)
        visit(affine, n); stats['roots'] += 1
    stats['scope'] = '32 seeded affine-scrambled high-degree cores plus cubic phases, and 4 affine roots, in dimensions 5 through 8.'
    return stats


def fwht_int(signs: np.ndarray) -> np.ndarray:
    a = np.asarray(signs, dtype=np.int64).copy(); n = dimension(len(a))
    for i in range(n):
        r = a.reshape(-1, 2 << i)
        l, h = r[:, :1 << i].copy(), r[:, 1 << i:].copy()
        r[:, :1 << i], r[:, 1 << i:] = l + h, l - h
    return a


def add(a: tuple[F,F], b: tuple[F,F]) -> tuple[F,F]:
    return a[0] + b[0], a[1] + b[1]


def scale(c: F, a: tuple[F,F]) -> tuple[F,F]:
    return (c*a[0], c*a[1]) if c >= 0 else (c*a[1], c*a[0])


def log_atanh_interval(t: F, terms: int = 48) -> tuple[F,F]:
    if not F(1) <= t <= F(2):
        raise ValueError('Range reduction must produce 1 <= t <= 2.')
    z = (t - 1)/(t + 1); z2 = z*z; power = z; total = F(0)
    for j in range(terms):
        total += 2 * power/(2*j+1)
        power *= z2
    tail = 2*power/((2*terms+1)*(1-z2))
    return total, total+tail


@lru_cache(maxsize=None)
def log2_interval(x: F) -> tuple[F,F]:
    if x <= 0:
        raise ValueError('Logarithm argument must be positive.')
    k = x.numerator.bit_length() - x.denominator.bit_length()
    t = x / (F(2)**k)
    if t < 1: k -= 1; t *= 2
    if t >= 2: k += 1; t /= 2
    lo, hi = log_atanh_interval(t)
    l2, u2 = log_atanh_interval(F(2))
    return F(k) + lo/u2, F(k) + hi/l2


def entropy_interval(signs: np.ndarray) -> tuple[F,F]:
    N = len(signs); w = fwht_int(signs); sq = w*w
    assert int(sq.sum()) == N*N
    out = F(0),F(0)
    for numerator, count in Counter(int(z) for z in sq).items():
        if numerator:
            p = F(numerator, N*N)
            out = add(out, scale(count*p, log2_interval(1/p)))
    return out


def binentropy_interval(p: F) -> tuple[F,F]:
    out = F(0),F(0)
    for t in (p,1-p):
        if t:
            out = add(out,scale(t,log2_interval(1/t)))
    return out


def character_child_cost(d: F) -> tuple[F,F]:
    w = 4*d*(1-d); q = 1-w/2
    out = 2*d*(1-d), 2*d*(1-d)
    out = add(out,scale(q,binentropy_interval(d*d/q)))
    out = add(out,binentropy_interval(w/2))
    return add(out,scale(F(-1,2),binentropy_interval(w)))


def as_decimal(x: F, places: int = 36) -> str:
    with localcontext() as ctx:
        ctx.prec = places
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def witness_checks() -> dict:
    k = 5; d = F(1,1 << k)
    small_x = np.arange(1 << (k+1)); small_bits = ((small_x & 1) == 1) & ((small_x >> 1) == 0)
    small = 1 - 2*small_bits.astype(np.int64)
    big_x = np.arange(1 << (2*k+1)); y=(big_x >> 1)&((1 << k)-1); z=big_x >> (k+1)
    big_bits = ((big_x & 1) == 1) & ((y == 0) ^ (z == 0))
    big = 1 - 2*big_bits.astype(np.int64)
    direct = add(entropy_interval(big),scale(F(-2),entropy_interval(small)))
    formula = add(character_child_cost(2*d*(1-d)),scale(F(-2),character_child_cost(d)))
    assert direct[0] > 0 and formula[0] > 0
    assert max(direct[0],formula[0]) <= min(direct[1],formula[1])
    # A transparent, exact rational enclosure wider than the computational one.
    display_lo = F(239650700679,10**14)
    display_hi = F(239650700680,10**14)
    assert display_lo < direct[0] <= direct[1] < display_hi
    return dict(k=k, individual_parent_dimension=k+1, shared_control_parent_dimension=2*k+1,
                inequality_refuted='Delta(shared product) <= Delta(first factor) + Delta(second factor)',
                certified_gap_lower=str(display_lo), certified_gap_upper=str(display_hi),
                certified_decimal_enclosure=['0.00239650700679','0.00239650700680'],
                higher_precision_midpoint=as_decimal((direct[0]+direct[1])/2),
                interval_width_upper=as_decimal(direct[1]-direct[0]),
                exact_walsh_and_scalar_formula_agree=True,
                interpretation='Counterexample to the proposed gluing inequality, NOT to FEI.')


def constant_approx_checks() -> dict:
    triples = pivots = 0
    for n in range(1,4):
        N = 1 << n; x = np.arange(N)
        for table in all_truth_tables(n):
            for v in range(1,N):
                dv = table ^ table[x ^ v]
                for q in (0,1):
                    err = int(np.count_nonzero(dv != q))
                    if 2*err > N:
                        continue
                    triples += 1
                    for i in range(n):
                        if not v & (1 << i):
                            continue
                        ids = x[((x >> i)&1)==0]
                        a = fwht_int(1-2*table[ids].astype(np.int64))
                        b = fwht_int(1-2*table[ids^(1 << i)].astype(np.int64))
                        childN = N//2
                        affinity_numer = int(np.abs(a*b).sum())
                        # M=(1-A)/2 <= epsilon, after clearing denominators.
                        assert N*(childN*childN-affinity_numer) <= 2*err*childN*childN
                        pivots += 1
    return dict(approximate_signed_symmetry_triples=triples,pivot_affinity_assertions=pivots,
                scope='Every f, direction, constant phase, and supported pivot in dimensions 1 through 3, with error <=1/2.')


def scalar_constant_check() -> dict:
    l2,u2=log_atanh_interval(F(2))
    value=add(scale(F(4),binentropy_interval(F(1,4))),(2/u2,2/l2))
    lo,hi=F(61305025796144,10**13),F(61305025796145,10**13)
    assert lo < value[0] <= value[1] < hi
    return {'formula':'4*h_2(1/4)+2/ln(2) = 8-3*log_2(3)+2/ln(2)',
            'certified_decimal_enclosure':['6.1305025796144','6.1305025796145'],
            'interpretation':'Existing local entropy-payment bound used in the new directional compression theorem; not a new universal FEI constant.'}


def main() -> None:
    result = {'status':'PASS', 'date':'2026-09-20', 'seed':SEED,
              'full_FEI_proved':False, 'formal_proof_assistant_used':False,
              'exact_small':exact_small_checks(), 'robust_small':robust_small_checks(),
              'tree_checks':exact_tree_checks(), 'approximate_symmetry':constant_approx_checks(),
              'gluing_counterexample':witness_checks(), 'compression_constant':scalar_constant_check()}
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = Path(__file__).with_name('verification.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
