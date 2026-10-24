"""Structured evaluation of the obstruction family N1 (NOTES section 6) for large D.

F_{D,w}: root x_0; plus side = complete read-once depth-D control tree with OR_w leaves on fresh blocks,
minus side = same with AND_w leaves. delta = 2^{-w}.
Spectrum: {x_0}: (1-2 delta)^2; block sets T u B (T subset of the D+1 path vars, B nonempty subset of the
leaf block): 4^{-(D+1)} * 4 delta^2 each; nothing else.
Costs use the paper's queue law with a = 6/5 (EVIDENCE: floating point).
"""
import math
import sys
from math import comb, log2

A = 6.0 / 5.0


def theta(s, r):
    return min(1.0, (s / r) ** A)


def elem_sym(vals, smax):
    e = [0.0] * (smax + 1)
    e[0] = 1.0
    for x in vals:
        for s in range(smax, 0, -1):
            e[s] += e[s - 1] * x
    return e


_CACHE = {}

def evaluate(D, w, lam):
    delta = 2.0 ** (-w)
    c = D + 1
    m0 = (1 - 2 * delta) ** 2
    mblk = 4.0 ** (-c) * 4 * delta * delta  # mass of each block set
    nleaves = 2 ** (D + 1)
    pi_plus = 2.0 ** (-c) * (1 - delta)
    pi_minus = 2.0 ** (-c) * delta
    Lam = (nleaves // 2) * (math.log1p(lam * pi_plus) + math.log1p(lam * pi_minus)) / math.log(2)
    v = 1.0  # E F = 0
    H = 0.0
    I = 0.0
    # Z_s for a gate: ranks 1..c (path) and 1..w (block)
    smax = c + w
    key = (D, w)
    if key not in _CACHE:
        Zs = [None] * (smax + 1)
        for s in range(1, smax + 1):
            vals = [theta(s, r) for r in range(1, c + 1)] + [theta(s, r) for r in range(1, w + 1)]
            Zs[s] = elem_sym(vals, s)[s]
        _CACHE[key] = {'Zs': Zs}
    Zs = _CACHE[key]['Zs']
    # {x_0}
    H += m0 * log2(1 / m0)
    I += m0
    inner0 = log2(2) + 1 + log2(Zs[1]) - 0.0  # log(s(s+1)) + 1 + log Z_1 - log theta_1(rank1)=0
    cmin0 = -log2(lam * pi_plus) + inner0
    csum0 = -log2(lam * (nleaves // 2) * (pi_plus + pi_minus)) + inner0
    minW = m0 * cmin0
    sumW = m0 * csum0
    # block sets: per leaf, sum over T subset path, B nonempty subset block of mass*cost
    # cost = -log(lam pi) + log(s(s+1)) + 1 + log Z_s - sum_{j in A} log theta_s(r_j)
    # aggregate via counts: for fixed (t, b) with t=|T|, b=|B|, s=t+b: number = C(c,t) C(w,b);
    # sum over sets of sum_{j in T} log theta_s(rank j) = C(c-1,t-1) * sum_{r=1..c} log theta_s(r); same for B.
    if 'leaf' in _CACHE[key]:
        per_leaf_cost_wo_root, per_leaf_mass, per_leaf_I, per_leaf_H = _CACHE[key]['leaf']
        trange = range(0)
    else:
        per_leaf_cost_wo_root = 0.0
        per_leaf_mass = 0.0
        per_leaf_I = 0.0
        per_leaf_H = 0.0
        trange = range(0, c + 1)
    for t in trange:
        for b in range(1, w + 1):
            s = t + b
            cnt = comb(c, t) * comb(w, b)
            base = log2(s * (s + 1)) + 1 + log2(Zs[s])
            lt = sum(log2(theta(s, r)) for r in range(1, c + 1)) * (comb(c - 1, t - 1) if t >= 1 else 0) * comb(w, b)
            lb = sum(log2(theta(s, r)) for r in range(1, w + 1)) * comb(w - 1, b - 1) * comb(c, t)
            tot = cnt * base - lt - lb
            per_leaf_cost_wo_root += mblk * tot
            per_leaf_mass += mblk * cnt
            per_leaf_I += mblk * cnt * s
            per_leaf_H += mblk * cnt * log2(1 / mblk)
    _CACHE[key]['leaf'] = (per_leaf_cost_wo_root, per_leaf_mass, per_leaf_I, per_leaf_H)
    half = nleaves // 2
    for pi in (pi_plus, pi_minus):
        minW += half * (per_leaf_mass * (-log2(lam * pi)) + per_leaf_cost_wo_root)
        sumW += half * (per_leaf_mass * (-log2(lam * pi)) + per_leaf_cost_wo_root)
    I += nleaves * per_leaf_I
    H += nleaves * per_leaf_H
    hv = 0.0  # v = 1
    minW += hv + v * Lam
    sumW += hv + v * Lam
    return dict(H=H, I=I, minW=minW, sumW=sumW, Lam=Lam, m0=m0)


def best_lambda(D, w):
    best = None
    for e2 in range(-8, 2 * (D + 6)):
        lam = 2.0 ** (e2 / 2)
        r = evaluate(D, w, lam)
        if best is None or r['minW'] < best[0]:
            best = (r['minW'], lam, r)
    return best


if __name__ == '__main__':
    for D in [int(x) for x in sys.argv[1:]]:
        w = max(1, math.ceil(math.log2(max(D, 2))))
        r1 = evaluate(D, w, 1.0)
        bm, bl, rb = best_lambda(D, w)
        I_exact = (1 - 2 * 2.0 ** -w) ** 2 + 2 * 2.0 ** -w * (1 - 2.0 ** -w) * (D + 1) + 2 * w * 2.0 ** -w
        print(f"D={D:3d} w={w} I={r1['I']:.5f} (formula {I_exact:.5f}) H/I={r1['H']/r1['I']:.3f} "
              f"minW/I(lam=1)={r1['minW']/r1['I']:.3f} min_lam minW/I={bm/r1['I']:.3f} (lam=2^{math.log2(bl):.1f}) "
              f"sumW/I(lam=1)={r1['sumW']/r1['I']:.3f}", flush=True)
