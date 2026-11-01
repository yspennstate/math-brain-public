"""Referee check of Corollary 11.2 (equal-mean term-test decision trees), exact small instances.

Tree: internal node = (block id, true subtree, false subtree); blocks are fixed variable sets with literal signs; along a
path blocks are distinct, a block may recur on different paths. Leaves: regular, one common mean, fresh data blocks.
Gates: unfolded paths (false node u -> first failing position t_u), AND [leaf = 1]. Order: full true blocks in path order,
then false prefixes by increasing deficit, ties to earlier nodes. Checks: product formula for every coefficient (exact),
I split, witness-sum code (exact Z) <= 26.71 I, Gibbs, per-part bounds as in Theorem 11.1's proof.
Usage: python check_TTT.py SEED COUNT BUDGET
"""
import sys, math, random, itertools, time
from fractions import Fraction
import numpy as np
from rc_common import coords, fwht_int, popcount, bits_of, elem_sym, theta, h2, LOG2E
from rc_trees import leaf_table
from check_TDL import equal_mean_leaves, eval_ltf, e_w

a = 1.2
L_STAR = 1 + math.log(2)
LOG3 = math.log2(3)


def rand_tree(rng, nblocks, depth):
    def build(avail, d):
        if d == 0 or not avail or rng.random() < 0.3:
            return ('leaf',)
        b = rng.choice(sorted(avail))
        rest = avail - {b}
        return ('node', b, build(rest, d - 1), build(rest, d - 1))
    return build(set(range(nblocks)), depth)


def leaves_of(t, path=()):
    if t[0] == 'leaf':
        return [path]
    _, b, tt, tf = t
    return leaves_of(tt, path + ((b, True),)) + leaves_of(tf, path + ((b, False),))


def check(rng):
    nblocks = rng.randint(1, 4)
    widths = [rng.randint(1, 3) for _ in range(nblocks)]
    tree = rand_tree(rng, nblocks, rng.randint(1, 3))
    if tree[0] == 'leaf':
        return None
    paths = leaves_of(tree)
    kind = rng.choice(['dict', 'and2', 'or2', 'mix'])
    est = sum(widths) + len(paths) * {'dict': 1, 'and2': 2, 'or2': 2, 'mix': 4}[kind]
    if est > 16:
        return None
    blocks = []
    nv = 0
    for w in widths:
        blocks.append(dict(vars=list(range(nv, nv + w)), sig=[rng.choice([1, -1]) for _ in range(w)], w=w, q=Fraction(1, 1 << w)))
        nv += w
    leaves, nv = equal_mean_leaves(rng, len(paths), nv, kind)
    n = nv
    X = coords(n)
    N = 1 << n
    tau = []
    for bl in blocks:
        tk = np.ones(N, dtype=bool)
        for v, s in zip(bl['vars'], bl['sig']):
            tk &= X[v] == s
        tau.append(tk)
    f = np.zeros(N, dtype=np.int8)
    for li, path in enumerate(paths):
        ev = np.ones(N, dtype=bool)
        for b, out in path:
            ev &= tau[b] if out else ~tau[b]
        f = np.where(ev, eval_ltf(leaves[li], X), f).astype(np.int8)
    F = fwht_int(f)
    L = []
    for lf in leaves:
        P, rel, order, lspec, kk = leaf_table(lf)
        gl = {}
        for Sl, cl in lspec.items():
            Sg = sum(1 << lf['vars'][i] for i in range(kk) if (Sl >> i) & 1)
            gl[Sg] = Fraction(cl, 1 << kk)
        mu = 2 * P - 1
        L.append(dict(P=P, var=1 - mu * mu, rel=rel, order=order, gl=gl, mask=sum(1 << v for v in lf['vars']),
                      I=sum(popcount(S) * c * c for S, c in gl.items())))
    PE = []
    for path in paths:
        p = Fraction(1)
        for b, out in path:
            p *= blocks[b]['q'] if out else 1 - blocks[b]['q']
        PE.append(p)
    I_true = sum((PE[i] * L[i]['var'] * Fraction(sum(blocks[b]['w'] for b, o in paths[i] if o), 2) for i in range(len(paths))), Fraction(0))
    I_rare = sum((PE[i] * L[i]['var'] * sum((blocks[b]['q'] * e_w(blocks[b]['w']) for b, o in paths[i] if not o), Fraction(0))
                  for i in range(len(paths))), Fraction(0))
    I_Y = sum((PE[i] * L[i]['I'] for i in range(len(paths))), Fraction(0))
    gates = {}
    for li, path in enumerate(paths):
        falses = [b for b, o in path if not o]
        trues = [b for b, o in path if o]
        for t in itertools.product(*[range(1, blocks[b]['w'] + 1) for b in falses]):
            p = Fraction(1)
            for b in trues:
                p *= blocks[b]['q']
            for b, tb in zip(falses, t):
                p *= Fraction(1, 1 << tb)
            pi = min(float(p * L[li]['P']), 0.5)
            rank = {}; pos = 1
            for b in trues:
                for v in blocks[b]['vars']:
                    rank[v] = pos; pos += 1
            pidx = {b: i for i, (b, o) in enumerate(path)}
            segs = sorted(range(len(falses)), key=lambda i: (blocks[falses[i]]['w'] - t[i], pidx[falses[i]]))
            for i in segs:
                for v in blocks[falses[i]]['vars'][:t[i]]:
                    rank[v] = pos; pos += 1
            for i, v in enumerate(L[li]['order']):
                rank[v] = i + 1
            gates[(li, t)] = dict(pi=pi, rank=rank, R=set(rank), falses=falses, t=t)
    Lam = sum(math.log2(1 + g['pi']) for g in gates.values())
    zc = {}

    def Z(key, s):
        if (key, s) not in zc:
            zc[(key, s)] = elem_sym([theta(s, r) for r in gates[key]['rank'].values()], s)
        return zc[(key, s)]

    ctrl_mask = (1 << sum(widths)) - 1
    fails = []; H = 0.0; code = 0.0; root = 0.0
    v = Fraction(0); I = Fraction(0)
    for S in np.nonzero(F)[0]:
        S = int(S); fh = Fraction(int(F[S]), N); mass = fh * fh; mf = float(mass)
        H -= mf * math.log2(mf)
        if S == 0:
            continue
        v += mass; s = popcount(S); I += s * mass
        B = S & ~ctrl_mask; T = S & ctrl_mask
        lis = [i for i in range(len(paths)) if B != 0 and (B & ~L[i]['mask']) == 0]
        if len(lis) != 1:
            fails.append(('owner', S)); continue
        li = lis[0]; path = paths[li]
        onpath = {b for b, o in path}
        pred = L[li]['gl'].get(B, Fraction(0))
        for b in range(len(blocks)):
            Sb = [i for i, vv in enumerate(blocks[b]['vars']) if (T >> vv) & 1]
            sg = 1
            for i in Sb:
                sg *= blocks[b]['sig'][i]
            if b not in onpath:
                if Sb:
                    pred = Fraction(0)
                continue
            out = dict(path)[b]
            if out:
                pred *= blocks[b]['q'] * sg
            else:
                pred *= (1 - blocks[b]['q']) if not Sb else -blocks[b]['q'] * sg
        if pred != fh:
            fails.append(('product', S)); continue
        A = bits_of(S)
        owners = [k for k, g in gates.items() if k[0] == li and set(A) <= g['R']]
        terms = []
        for k in owners:
            g = gates[k]; lt = 1.0
            for x in A:
                lt *= theta(s, g['rank'][x])
            terms.append(g['pi'] * lt / Z(k, s))
        code += mf * (Lam - math.log2(sum(terms) / (s * (s + 1)) / 2))
        root += mf * math.log2(1 / sum(gates[k]['pi'] for k in owners))
    if I != I_true + I_rare + I_Y:
        fails.append(('I-split',))
    vf = float(v); If = float(I)
    tot = h2(vf) + code
    return dict(fails=fails, H=H, I=If, code=tot, lit=tot + vf * Lam,
                root_ratio=root / (2 * float(I_true) + 2 * float(I_Y) + (LOG2E + 2) * float(I_rare)),
                recur=len(set(node_blocks(tree))) < len(node_blocks(tree)))


def node_blocks(t):
    """Block ids of all internal NODES (a block tested at two different nodes appears twice)."""
    if t[0] == 'leaf':
        return []
    return [t[1]] + node_blocks(t[2]) + node_blocks(t[3])


if __name__ == '__main__':
    seed, count, budget = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    rng = random.Random(seed); t0 = time.time()
    k = 0; nfail = 0; gib = 0; mx = 0.0; mxl = 0.0; mr = 0.0; nrec = 0
    while k < count and time.time() - t0 < budget:
        r = check(rng)
        if r is None:
            continue
        k += 1
        if r['fails']:
            nfail += 1; print('FAIL', r['fails'][:2]); continue
        if r['H'] > r['code'] + 1e-9:
            gib += 1
        nrec += r['recur']
        mx = max(mx, r['code'] / r['I']); mxl = max(mxl, r['lit'] / r['I']); mr = max(mr, r['root_ratio'])
    print(f'term-test trees: {k} instances ({nrec} with a block on two paths), spectral failures {nfail}, Gibbs failures {gib}; '
          f'max code/I = {mx:.4f}, max (code + v Lam)/I = {mxl:.4f}, max root/bound = {mr:.4f}, time {time.time()-t0:.0f}s')
