#!/usr/bin/env python
"""B07 lead checks (exact). Usage: python -X utf8 b07_lead_checks.py OUTDIR [parts]

P1  A032 ten-atom coupled-phase obstruction, re-derived independently.
P2  Uniform-on-support Boolean spectra for n<=4: support affine of even dimension, every such subspace realized.
P3  Generic min-entropy inequality on n-bit point defects (closed forms, mpmath 60 digits) and A031's anchor (float).
P4  Exhaustive census of two-address conditional-product Boolean functions, N=n+2 with n=2,3; 40/17 witness at n=4.
"""
import sys, os, json, time, math, itertools
from fractions import Fraction
import numpy as np

OUT = sys.argv[1]
PARTS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['P1', 'P2', 'P3', 'P4']
os.makedirs(OUT, exist_ok=True)
T0 = time.time()


def save(name, obj):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1, default=str)


def popc(v):
    return bin(v).count('1')


def hmat(n):
    P = 1 << n
    return np.array([[1 - 2 * (popc(x & T) & 1) for T in range(P)] for x in range(P)], dtype=np.int64)


def all_boolean(n):
    P = 1 << n
    k = np.arange(1 << P, dtype=np.int64)
    bits = (k[:, None] >> np.arange(P, dtype=np.int64)) & 1
    return 1 - 2 * bits  # rows are truth tables f[x]


# ---------------------------------------------------------------- P1
def part1():
    m = [8, 8, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0]
    N = 16
    res = {'magnitudes': m, 'sum_squares': sum(v * v for v in m)}
    assert res['sum_squares'] == 256
    supp = [s for s in range(N) if m[s]]
    indep = {}
    for U in range(1, N):
        prods = [m[S] * m[S ^ U] for S in range(N) if S < (S ^ U) and m[S] and m[S ^ U]]
        tot = sum(prods)
        ok = (tot == 0)
        if tot % 2 == 0 and not ok:
            reach = {0}
            for p in prods:
                reach |= {r + p for r in reach}
            ok = (tot // 2) in reach
        indep[U] = {'pair_products': prods, 'independent_sign_partition_to_zero': ok}
    zero_per_U = {U: 0 for U in range(1, N)}
    all_zero = 0
    for bits in range(1 << len(supp)):
        a = [0] * N
        for k, s in enumerate(supp):
            a[s] = -m[s] if (bits >> k) & 1 else m[s]
        allz = True
        for U in range(1, N):
            c = sum(a[S] * a[S ^ U] for S in range(N))
            if c == 0:
                zero_per_U[U] += 1
            else:
                allz = False
        if allz:
            all_zero += 1
    res['independent_pair_partitions_all_pass'] = all(v['independent_sign_partition_to_zero'] for v in indep.values())
    res['per_U_common_sign_vectors_with_zero_convolution'] = zero_per_U
    res['sign_vectors_tested'] = 1 << len(supp)
    res['sign_vectors_with_all_15_convolutions_zero'] = all_zero
    # direct: no Boolean 4-bit function has |W| = m; pattern count
    F = all_boolean(4)
    W = F @ hmat(4)
    A = np.abs(W)
    res['boolean_truth_tables'] = int(len(F))
    res['boolean_with_abs_walsh_equal_m'] = int(np.all(A == np.array(m), axis=1).sum())
    laws = {tuple(r) for r in A.tolist()}
    res['distinct_boolean_spectral_laws_n4'] = len(laws)
    pat = sorted(m, reverse=True)
    real_pat = [l for l in laws if sorted(l, reverse=True) == pat]
    res['pattern_8_8_4x8_0x6_realizable_labelled_laws'] = len(real_pat)
    res['pattern_8_8_4x8_0x6_arithmetic_placements'] = math.factorial(16) // (math.factorial(2) * math.factorial(8) * math.factorial(6))
    res['independent_pair_partitions'] = {str(k): v for k, v in indep.items()}
    save('P1_ten_atom.json', res)
    return res


# ---------------------------------------------------------------- P2
def gauss_binom(n, r):
    num = den = 1
    for i in range(r):
        num *= (1 << n) - (1 << i)
        den *= (1 << r) - (1 << i)
    return num // den


def is_affine(sup):
    s = set(sup)
    if len(s) & (len(s) - 1):
        return False
    a0 = sup[0]
    lin = {a ^ a0 for a in s}
    return all((u ^ v) in lin for u in lin for v in lin)


def part2():
    out = {}
    for n in range(1, 5):
        F = all_boolean(n)
        W = F @ hmat(n)
        A = np.abs(W)
        uniform_supports = {}
        small_support_laws = {}
        for row in {tuple(r) for r in A.tolist()}:
            sup = [T for T, v in enumerate(row) if v]
            vals = {row[T] for T in sup}
            if len(sup) <= 4:
                small_support_laws.setdefault(len(sup), set()).add((tuple(sup), tuple(row[T] for T in sup)))
            if len(vals) == 1:
                uniform_supports.setdefault(tuple(sup), 0)
        by_dim = {}
        bad = []
        for sup in uniform_supports:
            if not is_affine(list(sup)):
                bad.append(sup)
                continue
            r = int(round(math.log2(len(sup))))
            by_dim[r] = by_dim.get(r, 0) + 1
        total_affine = {r: gauss_binom(n, r) * (1 << (n - r)) for r in range(n + 1)}
        small = {}
        for size, laws in small_support_laws.items():
            small[size] = {'count': len(laws),
                           'all_uniform_affine': all(len(set(v)) == 1 and is_affine(list(s)) for s, v in laws)}
        out[n] = {'uniform_support_laws_nonaffine': len(bad),
                  'realized_uniform_affine_by_dim': by_dim,
                  'all_affine_subspaces_by_dim': total_affine,
                  'even_dims_fully_realized': all(by_dim.get(r, 0) == total_affine[r] for r in range(0, n + 1, 2)),
                  'odd_dims_realized': sum(by_dim.get(r, 0) for r in range(1, n + 1, 2)),
                  'support_le_4_laws': small}
    save('P2_affine_even.json', out)
    return out


# ---------------------------------------------------------------- P3
def part3():
    import mpmath as mp
    mp.mp.dps = 60
    rows = []
    for n in range(3, 41):
        q = mp.mpf(2) ** (1 - n)
        p0 = (1 - q) ** 2
        p1 = q * q            # each nonzero S
        cnt = 2 ** n - 1
        l0 = -mp.log(p0, 2)
        l1 = -mp.log(p1, 2)
        H = p0 * l0 + cnt * p1 * l1
        I = mp.mpf(n) * 2 ** (n - 1) * p1
        var = p0 * (l0 - H) ** 2 + cnt * p1 * (l1 - H) ** 2
        gap = H - l0
        bound = mp.sqrt((1 - p0) * var / p0)
        rows.append({'n': n, 'H_over_I': mp.nstr(H / I, 12), 'gap_over_I': mp.nstr(gap / I, 12),
                     'generic_bound_over_I': mp.nstr(bound / I, 12),
                     'bound_minus_gap_over_I': mp.nstr((bound - gap) / I, 6)})
    a031 = []
    for n in range(3, 15):
        P = 1 << n
        f = np.ones(P)
        f[0] = -1.0
        Hm = hmat(n).astype(float)
        a = (f @ Hm) / P
        p = a * a
        ell = np.where(p > 0, -np.log2(np.where(p > 0, p, 1)), 0.0)
        H = float((p * ell).sum())
        pc = np.array([popc(T) for T in range(P)], dtype=float)
        I = float((pc * p).sum())
        v = a * ell
        # c_U = sum_S a_S a_{S^U} ell_S = (1/P) WHT( WHT(a) * WHT(v) ) up to normalisation
        c = ((a @ Hm) * (v @ Hm)) @ Hm / P
        Elog = float((pc[1:] * c[1:] ** 2).sum())
        R = int(np.argmax(p))
        J = sum(p[R ^ U] / pc[U] for U in range(1, P))
        a031.append({'n': n, 'H_over_I': H / I, 'Elog_over_I': Elog / I,
                     'A031_anchor_gap_bound_over_I': math.sqrt(J * Elog / p[R]) / I,
                     'true_gap_over_I': (H + math.log2(p[R])) / I})
    save('P3_generic_minentropy.json', {'point_defect_generic': rows, 'point_defect_A031_float_illustration': a031})
    return rows[-1], a031[-1]


# ---------------------------------------------------------------- P4
def product_ok(C, Z, n):
    """C: (M,P) int64 squared integer amplitudes; Z: row sums. Exact product-law test."""
    P = 1 << n
    ok = np.ones(C.shape[0], dtype=bool)
    Mi = [C[:, [T for T in range(P) if (T >> i) & 1]].sum(1) for i in range(n)]
    for T in range(P):
        lhs = C[:, T] * Z ** (n - 1)
        rhs = np.ones(C.shape[0], dtype=np.int64)
        for i in range(n):
            rhs = rhs * (Mi[i] if (T >> i) & 1 else Z - Mi[i])
        ok &= (lhs == rhs)
    return ok


def subsets(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            return
        sub = (sub - 1) & mask


def leq_exact(atoms, n, a, b):
    """atoms: list of (C, size) with C=W^2 integers summing to Ztot=4^(n+1). Decide H <= (a/b) I exactly."""
    Ztot = 4 ** (n + 1)
    assert sum(c for c, _ in atoms) == Ztot
    E = (2 * n + 2) * b * Ztot - a * sum(c * s for c, s in atoms)
    if E <= 0:
        return True
    rhs = 1
    for c, _ in atoms:
        rhs *= c ** (b * c)
    return (1 << E) <= rhs


def census(n, want_exact_all=True, internal=False):
    P = 1 << n
    full = (1 << P) - 1          # bit mask over the P points x
    Hm = hmat(n)
    vals = np.array([-2, -1, 0, 1, 2], dtype=np.int64)
    idx = np.indices((5,) * P, dtype=np.int64).reshape(P, -1).T
    G = vals[idx]
    del idx
    W = G @ Hm
    C = W * W
    Z = C.sum(1)
    keep = np.nonzero(product_ok(C, Z, n))[0]
    Gk, Wk, Ck, Zk = G[keep], W[keep], C[keep], Z[keep]
    del G, W, C, Z
    Ztot = 4 ** (n + 1)
    pc = np.array([popc(T) for T in range(P)], dtype=np.int64)
    logC = np.where(Ck > 0, np.log2(np.where(Ck > 0, Ck, 1)), 0.0)
    S1 = (Ck * (math.log2(Ztot) - logC)).sum(1)          # sum_T C log2(Ztot/C)
    S2 = (Ck * pc).sum(1)
    half = np.zeros(len(Gk), dtype=np.int64); one = np.zeros_like(half); hs = np.zeros_like(half)
    for x in range(P):
        half |= (np.abs(Gk[:, x]) == 1).astype(np.int64) << x
        one |= (np.abs(Gk[:, x]) == 2).astype(np.int64) << x
        hs |= (Gk[:, x] == -1).astype(np.int64) << x
    half = half.tolist(); one = one.tolist(); hs = hs.tolist()
    byHO, byHOS = {}, {}
    for i in range(len(Gk)):
        byHO.setdefault((half[i], one[i]), []).append(i)
        byHOS.setdefault((half[i], one[i], hs[i]), []).append(i)
    S1l, S2l, Zl = S1.tolist(), S2.tolist(), Zk.tolist()
    combos = []
    for i0 in range(len(Gk)):
        H0, O0 = half[i0], one[i0]
        Z0 = full & ~(H0 | O0)
        s0 = hs[i0]
        for sub1 in subsets(Z0):
            for i1 in byHO.get((H0, sub1), ()):
                s1 = hs[i1]
                rem1 = Z0 & ~sub1
                for sub2 in subsets(rem1):
                    for i2 in byHO.get((H0, sub2), ()):
                        s12 = H0 & ~(s0 ^ s1 ^ hs[i2])
                        for i12 in byHOS.get((H0, rem1 & ~sub2, s12), ()):
                            combos.append((i0, i1, i2, i12))
    res = {'n_physical': n, 'N_total': n + 2, 'product_slice_functions_including_zero': int(len(Gk)),
           'valid_two_address_conditional_product_boolean_functions': len(combos)}
    # Booleanity re-check and Parseval on every combo
    chi = [(1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1)]  # rows y; cols J=(0,{1},{2},{12})
    weightsJ = [0, 1, 1, 2]
    best = -1.0
    ratios = []
    wdist = {}
    for (i0, i1, i2, i12) in combos:
        js = (i0, i1, i2, i12)
        if sum(Zl[j] for j in js) != Ztot:
            raise AssertionError('Parseval fails: %r %r %r' % (js, [Zl[j] for j in js], [Gk[j].tolist() for j in js]))
        Hn = sum(S1l[j] for j in js)
        In = sum(weightsJ[k] * Zl[j] + S2l[j] for k, j in enumerate(js))
        r = Hn / In if In > 0 else float('nan')
        ratios.append(r)
        key = tuple(Fraction(Zl[j], Ztot) for j in js)
        wdist[key] = wdist.get(key, 0) + 1
    # explicit Booleanity re-verification of every combo (independent of the pointwise pattern logic)
    gk = Gk.tolist()
    for (i0, i1, i2, i12) in combos:
        for y in range(4):
            for x in range(P):
                v = chi[y][0] * gk[i0][x] + chi[y][1] * gk[i1][x] + chi[y][2] * gk[i2][x] + chi[y][3] * gk[i12][x]
                assert v in (2, -2), 'non-Boolean combo'
    finite = [r for r in ratios if r == r]
    rmax = max(finite)
    arg = [k for k, r in enumerate(ratios) if r == r and r >= rmax - 1e-9]

    def atoms_of(k):
        js = combos[k]
        at = []
        for J, j in enumerate(js):
            for T in range(P):
                c = int(Ck[j, T])
                if c:
                    at.append((c, weightsJ[J] + popc(T)))
        return at
    # exact certification: every combo satisfies H <= 2 I ?  and bracket of the maximum
    exact_le2 = None
    if want_exact_all:
        exact_le2 = all(leq_exact(atoms_of(k), n, 2, 1) for k in range(len(combos)) if ratios[k] == ratios[k])
    top = []
    for k in arg[:20]:
        js = combos[k]
        top.append({'slices_G_times2': [gk[j] for j in js], 'weights': [str(Fraction(Zl[j], Ztot)) for j in js],
                    'ratio_float': ratios[k]})
    res.update({'ratio_max_float': rmax, 'argmax_count': len(arg), 'every_combo_H_le_2I_exact': exact_le2,
                'count_ratio_eq_2_float': sum(1 for r in finite if abs(r - 2) < 1e-12),
                'weight_vectors': {','.join(str(f) for f in k): v for k, v in sorted(wdist.items(), key=lambda kv: -kv[1])},
                'top_examples': top})
    if internal:
        return res, {'combos': combos, 'Ck': Ck, 'Zl': Zl, 'S1l': S1l, 'S2l': S2l, 'gk': gk, 'ratios': ratios}
    return res


def witness_40_17():
    n = 4
    P = 16
    g = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]
    h = []
    for low in (3, 5, 6):
        h.append([1 if (x & 7) == low else 0 for x in range(P)])
    slices = [g] + h
    Hm = hmat(n)
    G2 = np.array([[2 * v for v in s] for s in slices], dtype=np.int64)
    W = G2 @ Hm
    C = W * W
    Z = C.sum(1)
    prod = product_ok(C, Z, n).tolist()
    chi = [(1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1)]
    boolean = all(sum(chi[y][J] * slices[J][x] for J in range(4)) in (1, -1) for y in range(4) for x in range(P))
    atoms = []
    wJ = [0, 1, 1, 2]
    for J in range(4):
        for T in range(P):
            if C[J, T]:
                atoms.append((int(C[J, T]), wJ[J] + popc(T)))
    Ztot = 4 ** (n + 1)
    Hf = sum(Fraction(c, Ztot) * Fraction(int(round(math.log2(Ztot / c)))) for c, _ in atoms)
    assert all(Ztot % c == 0 and (Ztot // c) & (Ztot // c - 1) == 0 for c, _ in atoms)
    If = sum(Fraction(c * s, Ztot) for c, s in atoms)
    return {'boolean': boolean, 'slices_product': prod, 'slice_masses': [str(Fraction(int(z), Ztot)) for z in Z],
            'H_exact': str(Hf), 'I_exact': str(If), 'H_over_I': str(Hf / If),
            'H_le_40_17_I_exact': leq_exact(atoms, n, 40, 17), 'H_le_2I_exact': leq_exact(atoms, n, 2, 1)}


def part4():
    out = {'witness_N6': witness_40_17()}
    save('P4_census.json', out)
    for n in (2, 3):
        t = time.time()
        out['census_n%d' % n] = census(n)
        out['census_n%d' % n]['seconds'] = round(time.time() - t, 2)
        save('P4_census.json', out)
    return out


if __name__ == '__main__':
    summary = {}
    if 'P1' in PARTS:
        r = part1()
        summary['P1'] = {k: r[k] for k in ('independent_pair_partitions_all_pass', 'sign_vectors_tested',
                                           'sign_vectors_with_all_15_convolutions_zero', 'boolean_with_abs_walsh_equal_m',
                                           'distinct_boolean_spectral_laws_n4', 'pattern_8_8_4x8_0x6_realizable_labelled_laws',
                                           'pattern_8_8_4x8_0x6_arithmetic_placements')}
        summary['P1']['min_common_zero_per_U'] = min(r['per_U_common_sign_vectors_with_zero_convolution'].values())
        print('P1', summary['P1'], round(time.time() - T0, 1), flush=True)
    if 'P2' in PARTS:
        r = part2()
        summary['P2'] = {n: {k: v[k] for k in ('uniform_support_laws_nonaffine', 'even_dims_fully_realized', 'odd_dims_realized',
                                               'realized_uniform_affine_by_dim')} for n, v in r.items()}
        print('P2', summary['P2'], round(time.time() - T0, 1), flush=True)
    if 'P3' in PARTS:
        a, b = part3()
        summary['P3'] = {'generic_n40': a, 'A031_n14': b}
        print('P3', summary['P3'], round(time.time() - T0, 1), flush=True)
    if 'P4' in PARTS:
        r = part4()
        summary['P4'] = {'witness': r['witness_N6']}
        for n in (2, 3):
            c = r['census_n%d' % n]
            summary['P4']['n%d' % n] = {k: c[k] for k in c if k not in ('top_examples', 'weight_vectors')}
            summary['P4']['n%d' % n]['weight_vectors_top'] = dict(list(c['weight_vectors'].items())[:12])
        print('P4', json.dumps(summary['P4'], default=str)[:3000], round(time.time() - T0, 1), flush=True)
    summary['seconds'] = round(time.time() - T0, 1)
    save('SUMMARY_%s.json' % '_'.join(PARTS), summary)
