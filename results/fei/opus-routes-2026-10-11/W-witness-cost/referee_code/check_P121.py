"""Referee check of W-L120 (Lemma 12.0), W-P121 (Prop 12.1) and W-P123 (mixture of orders).

For every tested f: decision trees (several variable-choice rules), both level sets b = +1, -1, three orders per cell
(path, reversed path, random). Exact: spectrum, Lemma 12.0 (Fractions). Floats: Q_lb (Lemma 3.2 witness sum, exact
elementary symmetric Z with M = 1), Gibbs, the per-set intermediate inequality of the proof, the final inequality
H <= 23.55 I + 2.4 R, and for P123 (two copies: path / reversed, gamma = 1/2) the per-set and final inequalities.
Usage: python check_P121.py exhaustive N   |   python check_P121.py families
"""
import sys, math, random, itertools, time
from fractions import Fraction
import numpy as np
from rc_common import fwht_int, popcount, bits_of, elem_sym, theta, h2, LOG2E, coords

a = 1.2
C121 = 8 + 3 * LOG2E + 2 * math.log2(3 * math.e * a / (a - 1))


def build_tree(f, n, rule, rng):
    """Leaves as (fixed dict var->sign, value). rule: 'first' (lowest relevant var), 'last', 'rand', 'greedy'."""
    N = 1 << n
    idx = np.arange(N)
    leaves = []

    def rec(fixed):
        mask = np.ones(N, dtype=bool)
        for v, s in fixed.items():
            bit = 0 if s == 1 else 1
            mask &= ((idx >> v) & 1) == bit
        vals = f[mask]
        if np.all(vals == vals[0]):
            leaves.append((dict(fixed), int(vals[0])))
            return
        free = [v for v in range(n) if v not in fixed]
        rel = []
        for v in free:
            sub = idx[mask]
            if np.any(f[sub] != f[sub ^ (1 << v)]):
                rel.append(v)
        if rule == 'first':
            v = rel[0]
        elif rule == 'last':
            v = rel[-1]
        elif rule == 'rand':
            v = rng.choice(rel)
        else:  # greedy: max influence inside the subcube
            best = None
            for u in rel:
                sub = idx[mask]
                infl = np.count_nonzero(f[sub] != f[sub ^ (1 << u)])
                if best is None or infl > best[0]:
                    best = (infl, u)
            v = best[1]
        for s in (1, -1):
            fx = dict(fixed); fx[v] = s
            rec(fx)
    rec({})
    return leaves


def analyse(f, n, leaves, b, orders_kind, rng):
    """Returns dict of checks for one (tree, level, order choice)."""
    F = fwht_int(f)
    N = 1 << n
    cells = []
    for fixed, val in leaves:
        if val != b:
            continue
        path = list(fixed.keys())          # insertion order = root first
        Vmask = 0
        for v in path:
            Vmask |= 1 << v
        ords = {}
        ords['path'] = {v: i + 1 for i, v in enumerate(path)}
        ords['rev'] = {v: len(path) - i for i, v in enumerate(path)}
        rp = path[:]; rng.shuffle(rp)
        ords['rand'] = {v: i + 1 for i, v in enumerate(rp)}
        cells.append(dict(V=Vmask, p=Fraction(1, 1 << len(path)), ords=ords, k=len(path)))
    assert all(c['k'] >= 1 for c in cells)
    Lam = sum(math.log2(1 + float(c['p'])) for c in cells)
    Lam_mix = sum(2 * math.log2(1 + float(c['p']) / 2) for c in cells)
    zc = {}

    def Z(k, s):
        if (k, s) not in zc:
            zc[(k, s)] = elem_sym([theta(s, r) for r in range(1, k + 1)], s)
        return zc[(k, s)]

    den = Fraction(1, N * N)
    v = Fraction(0); I = Fraction(0); H = 0.0; Hplus = 0.0
    code = 0.0; code_mix = 0.0; Rsum = 0.0; Rmix = 0.0
    lem_fail = 0; inter_fail = 0; inter_mix_fail = 0; worst_inter = -1e9
    for S in np.nonzero(F)[0]:
        S = int(S)
        m = Fraction(int(F[S]) ** 2) * den
        mf = float(m)
        H -= mf * math.log2(mf)
        if S == 0:
            continue
        v += m; s = popcount(S); I += s * m
        Hplus -= mf * math.log2(mf)
        A = bits_of(S)
        own = [c for c in cells if (S & ~c['V']) == 0]
        # Lemma 12.0 (exact)
        if Fraction(abs(int(F[S])), N) > 2 * sum((c['p'] for c in own), Fraction(0)):
            lem_fail += 1
        assert own, 'no owner cell'
        sp = sum(float(c['p']) for c in own)
        o = orders_kind
        terms = []; terms_mix = []
        Ew_rank = 0.0; Ew_rank_mix = 0.0
        for c in own:
            pc = float(c['p'])
            lt = 1.0
            for j in A:
                lt *= theta(s, c['ords'][o][j])
            terms.append(pc * lt / Z(c['k'], s))
            rk = sum(max(0.0, math.log2(c['ords'][o][j] / s)) for j in A)
            Ew_rank += pc / sp * rk
            # mixture: copies path / rev with gamma 1/2
            best = float('inf'); tm = 0.0
            for oo in ('path', 'rev'):
                lt2 = 1.0
                for j in A:
                    lt2 *= theta(s, c['ords'][oo][j])
                tm += pc * 0.5 * lt2 / Z(c['k'], s)
                rk2 = sum(max(0.0, math.log2(c['ords'][oo][j] / s)) for j in A)
                best = min(best, (1 / a) * 1.0 + rk2)
            terms_mix.append(tm)
            Ew_rank_mix += pc / sp * best
        Qlb = 2.0 ** (-Lam) * sum(terms) / (s * (s + 1)) / 2
        Qlb_mix = 2.0 ** (-Lam_mix) * sum(terms_mix) / (s * (s + 1)) / 2
        cost = -math.log2(Qlb); cost_mix = -math.log2(Qlb_mix)
        code += mf * cost; code_mix += mf * cost_mix
        Rsum += mf * Ew_rank; Rmix += mf * Ew_rank_mix
        rhs = Lam + 1 + 0.5 * math.log2(1 / mf) + math.log2(s * (s + 1)) + 1 + s * math.log2(math.e * a / (a - 1)) + a * Ew_rank
        rhs_mix = Lam_mix + 1 + 0.5 * math.log2(1 / mf) + math.log2(s * (s + 1)) + 1 + s * math.log2(math.e * a / (a - 1)) + a * Ew_rank_mix
        if cost > rhs + 1e-9:
            inter_fail += 1
        if cost_mix > rhs_mix + 1e-9:
            inter_mix_fail += 1
        worst_inter = max(worst_inter, cost - rhs)
    vf = float(v); If = float(I)
    code_tot = h2(vf) + code
    code_mix_tot = h2(vf) + code_mix
    return dict(H=H, I=If, v=vf, R=Rsum, Rmix=Rmix, code=code_tot, code_mix=code_mix_tot,
                lem_fail=lem_fail, inter_fail=inter_fail, inter_mix_fail=inter_mix_fail,
                worst_inter=worst_inter,
                gibbs_ok=H <= code_tot + 1e-9 and H <= code_mix_tot + 1e-9,
                final_ok=H <= C121 * If + 2 * a * Rsum + 1e-9,
                final_mix_ok=H <= C121 * If + 2 * a * Rmix + 1e-9,
                hplus_chain=Hplus <= 2 * h2(vf) + 2 * vf * (LOG2E + 2) + 2 * math.log2(3 * math.e * a / (a - 1)) * If + 2 * a * Rsum + 1e-9)


def run_function(f, n, rng, agg, rules=('first', 'last', 'rand', 'greedy')):
    if np.all(f == f[0]):
        return
    for rule in rules:
        leaves = build_tree(f, n, rule, rng)
        for b in (1, -1):
            if not any(val == b for _, val in leaves):
                continue
            for o in ('path', 'rev', 'rand'):
                r = analyse(f, n, leaves, b, o, rng)
                agg['runs'] += 1
                for k in ('lem_fail', 'inter_fail', 'inter_mix_fail'):
                    agg[k] += r[k]
                for k in ('gibbs_ok', 'final_ok', 'final_mix_ok', 'hplus_chain'):
                    if not r[k]:
                        agg['bad_' + k] += 1
                agg['max_code_over_I'] = max(agg['max_code_over_I'], r['code'] / r['I'])
                agg['max_cost_minus_perset_bound'] = max(agg['max_cost_minus_perset_bound'], r['worst_inter'])
                agg['max_R_over_I'] = max(agg['max_R_over_I'], r['R'] / r['I'])
                agg['max_H_over_I'] = max(agg['max_H_over_I'], r['H'] / r['I'])


def new_agg():
    return dict(runs=0, lem_fail=0, inter_fail=0, inter_mix_fail=0, bad_gibbs_ok=0, bad_final_ok=0,
                bad_final_mix_ok=0, bad_hplus_chain=0, max_cost_minus_perset_bound=-1e9, max_code_over_I=0.0, max_R_over_I=0.0, max_H_over_I=0.0)


def families():
    """Witness families from COUNTEREXAMPLES.md (small parameters), all exact Boolean tables."""
    rng = random.Random(3)
    out = []
    # X001 parity lift of random g on 4 bits: f(x,z) = g(x1 z, ..., x4 z)
    for t in range(6):
        n0 = 4; N0 = 1 << n0
        g = np.array([rng.choice([1, -1]) for _ in range(N0)], dtype=np.int8)
        n = n0 + 1
        X = coords(n)
        z = X[n0]
        idx = np.zeros(1 << n, dtype=np.int64)
        for i in range(n0):
            bit = ((X[i] * z) == -1).astype(np.int64)
            idx |= bit << i
        out.append(('X001 parity lift', n, g[idx]))
    # X002 splice for m = 3, 5: b(t) = (-1)^(t1 t2 + ... ) on m-1 bits (0/1), g0(y) = b(y1+ym, ...), g1 = (-1)^ym g0
    for m in (3, 5):
        n = m + 1
        f = np.zeros(1 << n, dtype=np.int8)
        for xi in range(1 << n):
            y = [(xi >> i) & 1 for i in range(m)]
            sel = (xi >> m) & 1
            tt = [(y[i] + y[m - 1]) % 2 for i in range(m - 1)]
            e = sum(tt[2 * k] * tt[2 * k + 1] for k in range((m - 1) // 2))
            val = (-1) ** e
            if sel == 1:
                val *= (-1) ** y[m - 1]
            f[xi] = val
        out.append((f'X002 splice m={m}', n, f))
    # X003 sparse activation, k = 4 (b on 4 bits), r = 2k = 8 activation bits, selector y: n = 13 (too slow), use r = 4
    k = 4; r = 4
    n = k + r + 1
    f = np.zeros(1 << n, dtype=np.int8)
    for xi in range(1 << n):
        xb = [(xi >> i) & 1 for i in range(k)]
        zb = [(xi >> (k + i)) & 1 for i in range(r)]
        ysel = (xi >> (k + r)) & 1
        bval = (-1) ** (xb[0] * xb[1] + xb[2] * xb[3])
        bp = bval - (2 if all(v == 0 for v in xb) else 0)
        Aact = 1 if all(v == 0 for v in zb) else 0
        G = 1 + Aact * (bval - 1)
        Hh = 1 + Aact * (bp - 1)
        f[xi] = G if ysel == 0 else Hh
    assert set(np.unique(f)) <= {1, -1}
    out.append(('X003 activation k=4 r=4', n, f))
    # X004 zy
    out.append(('X004 zy', 2, np.array([1, -1, -1, 1], dtype=np.int8)))
    # X005 shared leaves g(z) y with random g on 3 bits
    for t in range(3):
        g = np.array([rng.choice([1, -1]) for _ in range(8)], dtype=np.int8)
        n = 4
        f = np.zeros(16, dtype=np.int8)
        for xi in range(16):
            zz = xi & 7; yy = 1 - 2 * ((xi >> 3) & 1)
            f[xi] = g[zz] * yy
        out.append(('X005 g(z)y', n, f))
    # X009: splice bent b with b - 2*1_{y=0} on m = 4 bits with a physical bit t
    m = 4; n = m + 1
    f = np.zeros(1 << n, dtype=np.int8)
    for xi in range(1 << n):
        yb = [(xi >> i) & 1 for i in range(m)]
        t = (xi >> m) & 1
        bval = (-1) ** (yb[0] * yb[1] + yb[2] * yb[3])
        if t == 1 and all(v == 0 for v in yb):
            bval = bval - 2
        f[xi] = bval
    out.append(('X009 bent splice m=4', n, f))
    # majority 5, 7; tribes 2x3; address a=2 (n=6)
    for nm in (5, 7):
        X = coords(nm)
        f = np.where(sum(x.astype(int) for x in X) > 0, 1, -1).astype(np.int8)
        out.append((f'MAJ{nm}', nm, f))
    X = coords(6)
    t1 = (X[0] == 1) & (X[1] == 1) & (X[2] == 1); t2 = (X[3] == 1) & (X[4] == 1) & (X[5] == 1)
    out.append(('tribes 2x3', 6, np.where(t1 | t2, 1, -1).astype(np.int8)))
    X = coords(6)
    addr = ((X[0] == -1).astype(int) + 2 * (X[1] == -1).astype(int))
    f = np.choose(addr, [X[2], X[3], X[4], X[5]]).astype(np.int8)
    out.append(('address a=2', 6, f))
    return out


if __name__ == '__main__':
    t0 = time.time()
    mode = sys.argv[1]
    rng = random.Random(5)
    if mode == 'exhaustive':
        n = int(sys.argv[2])
        agg = new_agg()
        N = 1 << n
        rules = ('first', 'last', 'greedy') if n <= 3 else ('first', 'greedy')
        for code in range(1 << N):
            f = np.array([1 if (code >> x) & 1 else -1 for x in range(N)], dtype=np.int8)
            run_function(f, n, rng, agg, rules)
        print(f'exhaustive n={n}:', agg, f'time={time.time()-t0:.1f}s')
    elif mode == 'sample':
        n = int(sys.argv[2]); cnt = int(sys.argv[3]); budget = float(sys.argv[4])
        agg = new_agg()
        N = 1 << n
        k = 0
        while k < cnt and time.time() - t0 < budget:
            # mix of uniform random functions and sparse/biased ones (rare level sets)
            pr = rng.choice([0.5, 0.25, 0.1, 0.03])
            f = np.array([1 if rng.random() < pr else -1 for _ in range(N)], dtype=np.int8)
            run_function(f, n, rng, agg, ('first', 'greedy'))
            k += 1
        print(f'sample n={n} functions={k}:', agg, f'time={time.time()-t0:.1f}s')
    else:
        for name, n, f in families():
            agg = new_agg()
            run_function(f, n, rng, agg)
            print(f'{name:28s} n={n:2d}', {k: (round(v, 3) if isinstance(v, float) else v) for k, v in agg.items()})
        print(f'time={time.time()-t0:.1f}s')
