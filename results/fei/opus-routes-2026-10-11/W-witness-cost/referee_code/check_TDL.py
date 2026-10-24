"""Referee check of W-T111 (Theorem 11.1, equal-mean term decision lists) and Cor 11.2 (term-test trees).

Exact: truth table, integer Walsh transform, product formula for every nonzero coefficient (Fractions), influence
split I = I_true + I_rare + I_Y.  Floats: the witness sum over ALL owner gates (exact Z), the Jensen form used by the
proof, each averaged part against the proof's bound, and the per-set rare-rank inequality of step (5).
Usage: python check_TDL.py SEED COUNT BUDGET_SECONDS
"""
import sys, math, random, itertools, time
from fractions import Fraction
import numpy as np
from rc_common import coords, fwht_int, popcount, bits_of, elem_sym, theta, h2, LOG2E
from rc_trees import leaf_table

a = 1.2
L_STAR = 1 + math.log(2)
LOG3 = math.log2(3)


def e_w(w):
    return Fraction(w * (1 << w), 2 * ((1 << w) - 1))


def equal_mean_leaves(rng, count, start, kind):
    leaves = []
    nv = start
    for _ in range(count):
        k2 = kind if kind != 'mix' else rng.choice(['and2', 'ltf4'])
        if kind == 'dict':
            leaves.append({'kind': 'ltf', 'vars': [nv], 'w': [1], 'sig': [rng.choice([1, -1])], 'th': 0}); nv += 1
        elif k2 == 'and2':
            leaves.append({'kind': 'ltf', 'vars': [nv, nv + 1], 'w': [1, 1], 'sig': [rng.choice([1, -1]) for _ in range(2)], 'th': 2}); nv += 2
        elif k2 == 'ltf4':
            leaves.append({'kind': 'ltf', 'vars': [nv, nv + 1, nv + 2, nv + 3], 'w': [2, 1, 1, 1],
                           'sig': [rng.choice([1, -1]) for _ in range(4)], 'th': 3}); nv += 4
        elif kind == 'or2':
            leaves.append({'kind': 'ltf', 'vars': [nv, nv + 1], 'w': [1, 1], 'sig': [rng.choice([1, -1]) for _ in range(2)], 'th': 0}); nv += 2
    return leaves, nv


def eval_ltf(leaf, X):
    tot = np.zeros(X[0].shape, dtype=np.int64)
    for v, w, s in zip(leaf['vars'], leaf['w'], leaf['sig']):
        tot += w * s * X[v].astype(np.int64)
    return np.where(tot >= leaf['th'], 1, -1).astype(np.int8)


def check_instance(widths, kind, rng, rare_check=True):
    m = len(widths)
    blocks = []
    nv = 0
    for w in widths:
        blocks.append(dict(vars=list(range(nv, nv + w)), sig=[rng.choice([1, -1]) for _ in range(w)], w=w,
                           q=Fraction(1, 1 << w)))
        nv += w
    leaves, nv = equal_mean_leaves(rng, m + 1, nv, kind)
    n = nv
    X = coords(n)
    N = 1 << n
    # evaluate f
    f = eval_ltf(leaves[m], X)
    for k in range(m - 1, -1, -1):
        tk = np.ones(N, dtype=bool)
        for v, s in zip(blocks[k]['vars'], blocks[k]['sig']):
            tk &= X[v] == s
        f = np.where(tk, eval_ltf(leaves[k], X), f).astype(np.int8)
    F = fwht_int(f)
    den = Fraction(1, N * N)
    # leaf data
    L = []
    for j, lf in enumerate(leaves):
        P, rel, order, lspec, kk = leaf_table(lf)
        gl = {}
        for Sl, cl in lspec.items():
            Sg = 0
            for i in range(kk):
                if (Sl >> i) & 1:
                    Sg |= 1 << lf['vars'][i]
            gl[Sg] = Fraction(cl, 1 << kk)
        mu = 2 * P - 1
        L.append(dict(P=P, mu=mu, var=1 - mu * mu, rel=rel, order=order, gl=gl,
                      I=sum(popcount(S) * c * c for S, c in gl.items()), mask=sum(1 << v for v in lf['vars'])))
    mus = set(d['mu'] for d in L)
    assert len(mus) == 1
    reach = [Fraction(1)]
    for k in range(m):
        reach.append(reach[-1] * (1 - blocks[k]['q']))
    PE = [reach[j] * (blocks[j]['q'] if j < m else 1) for j in range(m + 1)]
    I_true = sum((PE[j] * L[j]['var'] * Fraction(blocks[j]['w'], 2) for j in range(m)), Fraction(0))
    I_rare = sum((PE[j] * L[j]['var'] * sum((blocks[k]['q'] * e_w(blocks[k]['w']) for k in range(j)), Fraction(0))
                  for j in range(m + 1)), Fraction(0))
    I_Y = sum((PE[j] * L[j]['I'] for j in range(m + 1)), Fraction(0))
    # ---------- gates ----------
    gates = {}
    for j in range(m + 1):
        ranges = [range(1, blocks[k]['w'] + 1) for k in range(j)]
        for t in itertools.product(*ranges):
            p = (blocks[j]['q'] if j < m else Fraction(1))
            for k in range(j):
                p *= Fraction(1, 1 << t[k])
            pi = min(float(p * L[j]['P']), 0.5)
            # deficit order on the conjunction
            rank = {}
            pos = 1
            if j < m:
                for v in blocks[j]['vars']:
                    rank[v] = pos; pos += 1
            segs = sorted(range(j), key=lambda k: (blocks[k]['w'] - t[k], k))
            for k in segs:
                for v in blocks[k]['vars'][:t[k]]:
                    rank[v] = pos; pos += 1
            for i, v in enumerate(L[j]['order']):
                rank[v] = i + 1   # separate inner function g_j (its own ranks)
            gates[(j, t)] = dict(pi=pi, rank=rank, R=set(rank.keys()))
    Lam = sum(math.log2(1 + g['pi']) for g in gates.values())
    zc = {}

    def Z(key, s):
        if (key, s) not in zc:
            g = gates[key]
            zc[(key, s)] = elem_sym([theta(s, r) for r in g['rank'].values()], s)
        return zc[(key, s)]

    fails = []
    tot = dict(code=0.0, root=0.0, rank=0.0, normsize=0.0, H=0.0, rank_true=0.0, rank_data=0.0, rank_rare=0.0)
    v = Fraction(0); I = Fraction(0)
    perset_viol = 0; perset_worst = -1e9; elem_viol = 0
    ctrl_mask = (1 << sum(widths)) - 1
    for S in np.nonzero(F)[0]:
        S = int(S)
        fh = Fraction(int(F[S]), N)
        mass = fh * fh
        mf = float(mass)
        tot['H'] -= mf * math.log2(mf)
        if S == 0:
            continue
        v += mass; s = popcount(S); I += s * mass
        B = S & ~ctrl_mask
        T = S & ctrl_mask
        js = [j for j in range(m + 1) if (B & ~L[j]['mask']) == 0 and B != 0]
        if len(js) != 1:
            fails.append(('no-unique-output', S)); continue
        j = js[0]
        # product formula
        pred = L[j]['gl'].get(B, Fraction(0))
        for k in range(m):
            Sk = [i for i, vv in enumerate(blocks[k]['vars']) if (T >> vv) & 1]
            sg = 1
            for i in Sk:
                sg *= blocks[k]['sig'][i]
            if k < j:
                pred *= (1 - blocks[k]['q']) if not Sk else -blocks[k]['q'] * sg
            elif k == j:
                pred *= blocks[k]['q'] * sg
            else:
                if Sk:
                    pred = Fraction(0)
        if pred != fh:
            fails.append(('product-formula', S)); continue
        # owners
        Mk = []
        for k in range(j):
            Sk = [i + 1 for i, vv in enumerate(blocks[k]['vars']) if (T >> vv) & 1]
            Mk.append(max(Sk) if Sk else 0)
        owners = [key for key in gates if key[0] == j and all(key[1][k] >= max(Mk[k], 1) for k in range(j))]
        A = bits_of(S)
        terms = []; ranks = []; logZ = []
        for key in owners:
            g = gates[key]
            lt = 1.0
            for x in A:
                lt *= theta(s, g['rank'][x])
            terms.append(g['pi'] * lt / Z(key, s))
            ranks.append(a * sum(max(0.0, math.log2(g['rank'][x] / s)) for x in A))
            logZ.append(math.log2(Z(key, s)))
        Qlb = 2.0 ** (-Lam) * sum(terms) / (s * (s + 1)) / 2
        tot['code'] += mf * (-math.log2(Qlb))
        pis = [gates[k2]['pi'] for k2 in owners]
        sp = sum(pis)
        wts = [p_ / sp for p_ in pis]
        tot['root'] += mf * math.log2(1 / sp)
        tot['rank'] += mf * sum(w_ * r_ for w_, r_ in zip(wts, ranks))
        tot['normsize'] += mf * (sum(w_ * z_ for w_, z_ in zip(wts, logZ)) + math.log2(s * (s + 1)) + 1)
        # split of the rank term: true block / data / rare elements
        trueset = set(blocks[j]['vars']) if j < m else set()
        dataset = set(L[j]['rel'])
        for w_, key in zip(wts, owners):
            g = gates[key]
            for x in A:
                c_ = a * max(0.0, math.log2(g['rank'][x] / s))
                if x in trueset:
                    tot['rank_true'] += mf * w_ * c_
                elif x in dataset:
                    tot['rank_data'] += mf * w_ * c_
                else:
                    tot['rank_rare'] += mf * w_ * c_
        # per-set rare-rank inequality of step (5) and the per-element mean-rank bound
        if rare_check and j > 0:
            Rset = [k for k in range(j) if Mk[k] > 0]
            if Rset:
                W_R = (blocks[j]['w'] if j < m else 0) + sum(blocks[k]['w'] for k in Rset)
                Lam_j = sum(float(blocks[k]['q']) * blocks[k]['w'] for k in range(j))
                lhs = 0.0
                rhs = 0.0
                for k in Rset:
                    Sk = [vv for vv in blocks[k]['vars'] if (T >> vv) & 1]
                    for x in Sk:
                        Er = sum(w_ * gates[key]['rank'][x] for w_, key in zip(wts, owners))
                        if Er > W_R + 2 ** (blocks[k]['w'] - Mk[k] + 3) * Lam_j + 1e-9:
                            elem_viol += 1
                        lhs += sum(w_ * max(0.0, math.log2(gates[key]['rank'][x] / s)) for w_, key in zip(wts, owners))
                    rhs += len(Sk) * (math.log2(1 + W_R / s) + (blocks[k]['w'] - Mk[k] + 3) + math.log2(1 + Lam_j / s))
                if lhs > rhs + 1e-9:
                    perset_viol += 1
                perset_worst = max(perset_worst, lhs - rhs)
    vf = float(v); If = float(I)
    if I != I_true + I_rare + I_Y:
        fails.append(('I-split',))
    code = h2(vf) + tot['code']
    It, Ir, Iy = float(I_true), float(I_rare), float(I_Y)
    bounds = dict(
        root=(tot['root'], 2 * It + 2 * Iy + (LOG2E + 2) * Ir),
        rank=(tot['rank'], a * (1 + LOG3) * It + a * (2 * LOG3 + 7) * Ir + a * (L_STAR / math.log(2)) * Iy),
        rank_true=(tot['rank_true'], a * It),
        rank_data=(tot['rank_data'], a * (L_STAR / math.log(2)) * Iy),
        rank_rare=(tot['rank_rare'], a * (LOG3 * (It + Ir) + 7 * Ir + LOG3 * Ir)),
        normsize=(tot['normsize'], vf + math.log2(6 * math.e * a / (a - 1)) * If),
        total=(code, 26.71 * If),
    )
    return dict(n=n, fails=fails, H=tot['H'], I=If, v=vf, Lam=Lam, code=code, bounds=bounds,
                perset_viol=perset_viol, perset_worst=perset_worst, elem_viol=elem_viol, gates=len(gates))


if __name__ == '__main__':
    seed = int(sys.argv[1]); count = int(sys.argv[2]); budget = float(sys.argv[3])
    MAXM = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    MAXW = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    MAXN = int(sys.argv[6]) if len(sys.argv) > 6 else 16
    rng = random.Random(seed)
    t0 = time.time()
    agg = dict(inst=0, spectral_fail=0, gibbs_fail=0, perset_viol=0, elem_viol=0)
    worst = {}
    maxcode = 0.0; maxH = 0.0; maxlit = 0.0; maxworst = -1e9
    while agg['inst'] < count and time.time() - t0 < budget:
        m = rng.randint(1, MAXM)
        widths = [rng.randint(1, MAXW) for _ in range(m)]
        kind = rng.choice(['dict', 'and2', 'mix', 'or2'])
        est = sum(widths) + (m + 1) * {'dict': 1, 'and2': 2, 'or2': 2, 'mix': 4}[kind]
        if est > MAXN:
            continue
        r = check_instance(widths, kind, rng)
        agg['inst'] += 1
        if r['fails']:
            agg['spectral_fail'] += 1; print('FAIL', widths, kind, r['fails'][:2]); continue
        if r['H'] > r['code'] + 1e-9:
            agg['gibbs_fail'] += 1
        agg['perset_viol'] += r['perset_viol']; agg['elem_viol'] += r['elem_viol']
        maxworst = max(maxworst, r['perset_worst'])
        maxcode = max(maxcode, r['code'] / r['I']); maxH = max(maxH, r['H'] / r['I'])
        maxlit = max(maxlit, (r['code'] + r['v'] * r['Lam']) / r['I'])
        for k, (val, bd) in r['bounds'].items():
            ratio = val / bd if bd > 0 else (0.0 if val <= 1e-12 else float('inf'))
            worst[k] = max(worst.get(k, 0.0), ratio)
    print(f'seed={seed}', agg, f'time={time.time()-t0:.1f}s')
    print(f'max H/I={maxH:.4f} max code/I={maxcode:.4f} max (code+v*Lam)/I={maxlit:.4f}  max per-set rare-rank (lhs-rhs)={maxworst:.4f}')
    print('max part/bound ratios (must be <= 1):', {k: round(v_, 4) for k, v_ in worst.items()})
