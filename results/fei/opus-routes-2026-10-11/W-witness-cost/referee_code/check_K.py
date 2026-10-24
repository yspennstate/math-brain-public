"""Referee check of W-P41 (Prop 4.1), W-C71 (Cor 7.1) and W-T51 (Theorem 5.1) on random instances of K.

Everything spectral is exact (integer Walsh transform, Fractions). Code lengths use floats (evidence), with the
single-root witness-sum lower bound Q_lb(A) of Lemma 3.2 (exact elementary symmetric normalizers), which is <= Q(A).
Usage: python check_K.py SEED COUNT MODE   (MODE = ro | em | both)
"""
import sys, math, random, time
from fractions import Fraction
import numpy as np
from rc_common import coords, spectrum, popcount, bits_of, elem_sym, theta, h2, LOG2E, A_EXP
from rc_trees import (eval_tree, leaves_with_paths, internal_nodes, leaf_table, mean_of,
                      rand_readonce_tree, rand_general_tree_equal_means, tree_n)

a = A_EXP
L_STAR = 1 + math.log(2)
CREG = math.log2(4 + math.e) + 2 * math.log2(math.e * math.pi)


def analyse(tree, read_once, negative=None):
    n = tree_n(tree)
    X = coords(n)
    f = eval_tree(tree, X)
    nn, spec = spectrum(f)
    assert nn == n
    N = 1 << n
    leaves = leaves_with_paths(tree)
    info = []
    data_owner = {}
    for li, (leaf, path) in enumerate(leaves):
        P, rel, order, lspec, k = leaf_table(leaf)
        mu = 2 * P - 1
        pathvars = [v for v, _ in path]
        assert len(set(pathvars)) == len(pathvars)
        sign = {v: s for v, s in path}
        c = len(path)
        # local leaf spectrum in global coordinates
        gl = {}
        if leaf['kind'] == 'ltf':
            kk = len(leaf['vars'])
            for Sl, cl in lspec.items():
                Sg = 0
                for i in range(kk):
                    if (Sl >> i) & 1:
                        Sg |= 1 << leaf['vars'][i]
                gl[Sg] = Fraction(cl, 1 << kk)
        else:
            gl[0] = Fraction(leaf['val'])
        for v in rel:
            assert v not in data_owner, "data var reused: DS violated"
            data_owner[v] = li
        var_g = 1 - mu * mu
        Ig = sum(popcount(S) * m * m for S, m in gl.items())
        Hplus = sum(-float(m * m) * math.log2(float(m * m)) for S, m in gl.items() if S != 0)
        info.append(dict(leaf=leaf, path=path, pathvars=pathvars, sign=sign, c=c, P=P, mu=mu, rel=rel,
                         order=order, gl=gl, var=var_g, I=Ig, Hplus=Hplus, p=Fraction(1, 1 << c)))
    nodes = internal_nodes(tree)
    ninfo = {}
    for (var, anc, tp, tm) in nodes:
        mp, mm = mean_of(tp), mean_of(tm)
        d = len(anc) + 1
        ninfo[var] = dict(anc=anc, d=d, mp=mp, mm=mm, Delta=abs(mp - mm) / 2,
                          reach=Fraction(1, 1 << (d - 1)))
    ctrl = set(v for (var, anc, tp, tm) in nodes for v in [var])
    # ---------------- Prop 4.1 (i)-(iii): every nonzero coefficient ----------------
    fails = []
    blk_mass = [Fraction(0)] * len(info)
    phi_mass = {}
    kind_of = {}
    for S, cS in spec.items():
        if S == 0:
            continue
        fh = Fraction(cS, N)
        vs = bits_of(S)
        T = [v for v in vs if v in ctrl]
        B = [v for v in vs if v not in ctrl]
        if B:
            owners = set(data_owner.get(v, -1) for v in B)
            if len(owners) != 1 or -1 in owners:
                fails.append(('block-owner', S)); continue
            li = owners.pop()
            d = info[li]
            if not set(T) <= set(d['pathvars']):
                fails.append(('block-T-not-in-path', S)); continue
            Bmask = 0
            for v in B:
                Bmask |= 1 << v
            sgn = 1
            for v in T:
                sgn *= d['sign'][v]
            pred = Fraction(sgn, 1 << d['c']) * d['gl'].get(Bmask, Fraction(0))
            if negative == 'drop_sign':
                pred = Fraction(1, 1 << d['c']) * d['gl'].get(Bmask, Fraction(0))
            if pred != fh:
                fails.append(('block-value', S)); continue
            blk_mass[li] += fh * fh
            kind_of[S] = ('blk', li, T, B)
        else:
            if not read_once:
                fails.append(('phi-set-in-EM', S)); continue
            # deepest node of T
            depth = {v: ninfo[v]['d'] for v in T}
            vdeep = max(T, key=lambda v: depth[v])
            ni = ninfo[vdeep]
            ancvars = [u for u, _ in ni['anc']]
            if not set(T) - {vdeep} <= set(ancvars):
                fails.append(('phi-not-chain', S)); continue
            sgn = 1
            for u, s in ni['anc']:
                if u in T:
                    sgn *= s
            pred = Fraction(sgn, 1 << ni['d']) * (ni['mp'] - ni['mm'])
            if negative == 'plus_means':
                pred = Fraction(sgn, 1 << ni['d']) * (ni['mp'] + ni['mm'])
            if pred != fh:
                fails.append(('phi-value', S)); continue
            phi_mass[vdeep] = phi_mass.get(vdeep, Fraction(0)) + fh * fh
            kind_of[S] = ('phi', vdeep, T)
    # completeness of masses (so no predicted set is missing)
    for li, d in enumerate(info):
        if blk_mass[li] != d['p'] * d['var']:
            fails.append(('block-total-mass', li))
    for v, ni in ninfo.items():
        w_v = ni['reach'] * ni['Delta'] ** 2
        if read_once and phi_mass.get(v, Fraction(0)) != w_v:
            fails.append(('phi-total-mass', v))
    # ---------------- (iv) influence of control vars, (v) decomposition ----------------
    idx = np.arange(N, dtype=np.int64)
    if read_once:
        for v, ni in ninfo.items():
            inf = Fraction(int(np.count_nonzero(f[idx ^ (1 << v)] != f)), N)
            pred = ni['reach'] * (1 - ni['mp'] * ni['mm']) / 2
            if negative == 'plus_inf':
                pred = ni['reach'] * (1 + ni['mp'] * ni['mm']) / 2
            if inf != pred:
                fails.append(('inf-formula', v))
            if inf < ni['reach'] * ni['Delta']:
                fails.append(('inf-lower', v))
    den = Fraction(1, N * N)
    v_f = sum((c * c * den for S, c in spec.items() if S != 0), Fraction(0))
    I_f = sum((popcount(S) * c * c * den for S, c in spec.items() if S != 0), Fraction(0))
    IXblk = sum((d['p'] * d['var'] * Fraction(d['c'], 2) for d in info), Fraction(0))
    IY = sum((d['p'] * d['I'] for d in info), Fraction(0))
    Iphi = Fraction(0)
    if read_once:
        Iphi = sum((ni['reach'] * ni['Delta'] ** 2 * Fraction(ni['d'] + 1, 2) for ni in ninfo.values()), Fraction(0))
    if I_f != IXblk + IY + Iphi:
        fails.append(('I-decomp',))
    IX_f = sum((sum(1 for u in bits_of(S) if u in ctrl) * c * c * den for S, c in spec.items()), Fraction(0))
    if IX_f != IXblk + Iphi:
        fails.append(('IX-decomp',))
    # ---------------- Cor 7.1 exact entropy identity ----------------
    H = 0.0
    for S, c in spec.items():
        m = float(c * c * den)
        H -= m * math.log2(m)
    Hpred = 0.0
    vf = float(v_f)
    if vf < 1:
        Hpred += -(1 - vf) * math.log2(1 - vf)
    for d in info:
        Hpred += float(d['p']) * (2 * d['c'] * float(d['var']) + d['Hplus'])
    if read_once:
        for ni in ninfo.values():
            w_v = float(ni['reach'] * ni['Delta'] ** 2)
            if w_v > 0:
                Hpred += w_v * (2 * (ni['d'] - 1) + 2 * math.log2(1 / float(ni['Delta'])))
    cor71_ok = abs(H - Hpred) < 1e-9 * max(1, H)
    if not cor71_ok:
        fails.append(('cor71-identity', H, Hpred))
    if H > (CREG + LOG2E) * float(I_f) + 1e-12:
        fails.append(('cor71-bound',))
    return dict(n=n, spec=spec, f=f, info=info, ninfo=ninfo, ctrl=ctrl, kind_of=kind_of, fails=fails,
                v=v_f, I=I_f, IXblk=IXblk, IY=IY, Iphi=Iphi, H=H, read_once=read_once)


def code_lengths(R):
    """Theorem 5.1's law: gates i in G (leaf not identically -1), inner functions kappa_i (path order) and g_i
    (desirability order). Returns per-set costs and totals."""
    info, n = R['info'], R['n']
    N = 1 << n
    den = Fraction(1, N * N)
    gates = []
    for li, d in enumerate(info):
        if d['P'] == 0:
            continue
        rank = {}
        for pos, (v, s) in enumerate(d['path']):
            rank[v] = pos + 1
        for pos, v in enumerate(d['order']):
            rank[v] = pos + 1
        pi = min(float(d['p'] * d['P']), 0.5)
        gates.append(dict(li=li, rank=rank, R=set(rank.keys()), pi=pi))
    Lam = sum(math.log2(1 + g['pi']) for g in gates)
    zcache = {}

    def Zs(gi, s):
        key = (gi, s)
        if key not in zcache:
            g = gates[gi]
            zcache[key] = elem_sym([theta(s, r) for r in g['rank'].values()], s)
        return zcache[key]

    tot_lb = 0.0
    tot_min = 0.0
    parts = dict(root_blk=0.0, root_phi=0.0, size=0.0, norm=0.0, rank=0.0)
    worst_step = []
    for S, c in R['spec'].items():
        if S == 0:
            continue
        p = float(c * c * den)
        A = bits_of(S)
        s = len(A)
        owners = [gi for gi, g in enumerate(gates) if set(A) <= g['R']]
        assert owners, "set with no owner gate"
        terms = []
        for gi in owners:
            g = gates[gi]
            lt = 1.0
            for j in A:
                lt *= theta(s, g['rank'][j])
            terms.append(g['pi'] * lt / Zs(gi, s) / (s * (s + 1)) / 2)
        Qlb = 2.0 ** (-Lam) * sum(terms)
        cost = -math.log2(Qlb)
        tot_lb += p * cost
        tot_min += p * (Lam - math.log2(max(terms)))
        # step-by-step quantities in the proof's split (using the proof's bounds where the proof does)
        kind = R['kind_of'][S]
        if kind[0] == 'blk':
            g = [gg for gg in gates if gg['li'] == kind[1]][0]
            parts['root_blk'] += p * math.log2(1 / g['pi'])
            parts['rank'] += p * a * sum(max(0.0, math.log2(g['rank'][j] / s)) for j in A)
            parts['norm'] += p * math.log2(Zs(gates.index(g), s))
        else:
            pis = sum(gates[gi]['pi'] for gi in owners)
            parts['root_phi'] += p * math.log2(1 / pis)
            g0 = gates[owners[0]]
            parts['rank'] += p * a * sum(max(0.0, math.log2(g0['rank'][j] / s)) for j in A)
            parts['norm'] += p * max(math.log2(Zs(gi, s)) for gi in owners)
        parts['size'] += p * (math.log2(s * (s + 1)) + 1)
    v = float(R['v'])
    I = float(R['I'])
    code_lb = h2(v) + tot_lb
    code_min = h2(v) + tot_min
    return dict(Lam=Lam, code_lb=code_lb, code_min=code_min, parts=parts, v=v, I=I)


def step_bounds(R, C):
    """Compare each averaged part with the bound the proof of Theorem 5.1 states for it."""
    I = float(R['I']); v = float(R['v'])
    IXblk = float(R['IXblk']); IY = float(R['IY']); Iphi = float(R['Iphi'])
    IX = IXblk + Iphi
    v_blk = sum(float(d['p'] * d['var']) for d in R['info'])
    v_phi = v - v_blk
    P = C['parts']
    out = {}
    out['a_root_blk'] = (P['root_blk'], v_blk + 2 * IXblk + 2 * IY)
    out['b_root_phi'] = (P['root_phi'], 2 * Iphi - v_phi + (LOG2E / math.e) * IX)
    out['c_size_norm'] = (P['size'] + P['norm'], v + math.log2(6 * math.e * a / (a - 1)) * I)
    out['d_rank'] = (P['rank'], a * IX + a * (L_STAR / math.log(2)) * IY)
    return out


def main():
    seed = int(sys.argv[1]); count = int(sys.argv[2]); mode = sys.argv[3]
    rng = random.Random(seed)
    t0 = time.time()
    worst = dict(code_lb=0, code_min=0, literal=0, H=0)
    nfail = 0
    step_viol = {}
    step_ratio = {}
    ninst = 0
    nphi = 0
    while ninst < count and time.time() - t0 < 480:
        ro = (mode == 'ro') or (mode == 'both' and rng.random() < 0.6)
        if ro:
            tree, nv = rand_readonce_tree(rng, rng.randint(1, 5), 9, rng.randint(1, 4), 0, p_stop=rng.choice([0.1, 0.3, 0.5]))
            # data vars must come after control vars in the generator: they are interleaved but fresh; fine
        else:
            tree, nv = rand_general_tree_equal_means(rng, rng.randint(1, 5), rng.randint(1, 5), rng.choice(['dict', 'and2', 'mix']))
        n = tree_n(tree)
        if n > 17 or n < 1:
            continue
        R = analyse(tree, ro)
        ninst += 1
        if R['I'] == 0:
            continue
        if R['fails']:
            nfail += 1
            print('FAIL', seed, ninst, R['fails'][:3])
            continue
        if ro and R['Iphi'] > 0:
            nphi += 1
        C = code_lengths(R)
        I = C['I']
        Hn = R['H'] / I
        if R['H'] > C['code_lb'] + 1e-9:
            print('GIBBS VIOLATION', seed, ninst, R['H'], C['code_lb'])
        worst['H'] = max(worst['H'], Hn)
        worst['code_lb'] = max(worst['code_lb'], C['code_lb'] / I)
        worst['code_min'] = max(worst['code_min'], C['code_min'] / I)
        worst['literal'] = max(worst['literal'], (C['code_lb'] + C['v'] * C['Lam']) / I)
        for k, (val, bd) in step_bounds(R, C).items():
            if val > bd + 1e-9:
                step_viol[k] = step_viol.get(k, 0) + 1
            if bd > 1e-12:
                step_ratio[k] = max(step_ratio.get(k, 0.0), val / bd)
    print(f'mode={mode} seed={seed} instances={ninst} with_phi={nphi} spectral_failures={nfail} '
          f'time={time.time()-t0:.1f}s')
    print('max H/I = %.4f   max code_lb/I = %.4f   max code_min/I = %.4f   max (code_lb + v*Lam)/I = %.4f'
          % (worst['H'], worst['code_lb'], worst['code_min'], worst['literal']))
    print('step-bound violations:', step_viol if step_viol else 'none')
    print('max part/bound ratios:', {k: round(v, 4) for k, v in step_ratio.items()})


if __name__ == '__main__':
    main()
