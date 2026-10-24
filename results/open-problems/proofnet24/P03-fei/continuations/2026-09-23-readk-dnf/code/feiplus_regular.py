"""Uniform FEI+ for regular functions: audit of the proof pieces, plus a composition sanity check.
Positions: coordinate 0 is the most desirable (position 1).  Checks
  RR  = sum_{|S|>=2} P(S) sum_{i in S} ln+(pos(i)/|S|) / J     (proof: <= 2 L_1 = 8.302)
  RQ  = sum_{|S|>=2} P(S) log2(1/Q(S)) / J, Q(S)=2^{-(|S|-1)} pi_{|S|}(S), rank reference with a=1.1087 (proof: <= 19.07)
  inf_order: Inf nonincreasing along the order; any Inf > 1/2 occurs at position <= 3
  FEI+ ratio H^{>=1}/(I-Var)."""
import math, itertools, numpy as np
from feicore import spectrum, popcounts, polite
from verify_f5 import ltf, shifted_upset
from readk_nonmono import random_nonmono
polite()
LN2 = math.log(2); L1 = 2 * math.log(3 * math.sqrt(3 / math.pi)) + 2; A_OPT = 1.1087

def feiplus_ratio(P, pc):
    nz = P > 1e-300
    H = float(-(P[nz] * np.log2(P[nz])).sum())
    Hp = H - (P[0] * math.log2(1 / P[0]) if P[0] > 0 else 0.0)
    I = float((P * pc).sum()); Var = 1 - float(P[0])
    return Hp / (I - Var) if I - Var > 1e-12 else float('nan')

def rank_audit(P, n, pc):
    N = P.size; xs = np.arange(N)
    big = pc >= 2
    J = float((P * pc)[big].sum())
    # ln+(pos(i)/|S|) summed over i in S, pos(i) = i+1
    lnsum = np.zeros(N)
    for i in range(n):
        inS = (xs >> i) & 1
        lnsum += inS * np.log(np.maximum(1.0, (i + 1) / np.maximum(pc, 1)))
    RR = float((P[big] * lnsum[big]).sum()) / J
    # rank reference: log2 1/Q = (|S|-1) + log2 Z_k + (a/ln2) sum ln+(pos/k)
    logZ = np.zeros(n + 1)
    for kk in range(1, n + 1):
        th = np.minimum(1.0, (kk / np.arange(1, n + 1)) ** A_OPT)
        e = np.zeros(kk + 1); e[0] = 1.0            # elementary symmetric polynomial of degree kk
        for t in th:
            e[1:] = e[1:] + t * e[:-1]
        logZ[kk] = math.log2(e[kk])
    cost = (pc - 1) + logZ[pc] + (A_OPT / LN2) * lnsum
    sel = big & (P > 1e-300)
    RQ = float((P[sel] * cost[sel]).sum()) / J
    return RR, RQ, J

def infl(P, n):
    xs = np.arange(P.size)
    return np.array([float(P[((xs >> i) & 1) == 1].sum()) for i in range(n)])

rng = np.random.default_rng(41)
worst = dict(RR=0.0, RQ=0.0, fp=0.0); bad_order = 0; cnt = 0
for n in (6, 8, 10, 12):
    pc = popcounts(n)
    for r in range(80):
        if r % 2 == 0:
            w = np.sort(rng.exponential(size=n))[::-1]
            if r % 4 == 0: w = np.sort(rng.integers(1, 6, size=n).astype(float))[::-1]
            theta = float(rng.uniform(-0.8, 0.8) * w.sum())
            tt = ltf(w, theta, n)
        else:
            tt = shifted_upset(n, rng)
        if np.all(tt == tt[0]): continue
        P = spectrum(tt); cnt += 1
        if float((P * pc)[pc >= 2].sum()) < 1e-12:
            nzs = (P > 1e-300) & (pc >= 1)
            assert float(-(P[nzs] * np.log2(P[nzs])).sum()) < 1e-9   # J = 0: a dictator, H^{>=1} = 0
            continue
        RR, RQ, J = rank_audit(P, n, pc)
        Iv = infl(P, n)
        if np.any(np.diff(Iv) > 1e-12) or any(Iv[i] > 0.5 and i + 1 > 3 for i in range(n)): bad_order += 1
        worst['RR'] = max(worst['RR'], RR); worst['RQ'] = max(worst['RQ'], RQ)
        fp = feiplus_ratio(P, pc)
        if fp == fp: worst['fp'] = max(worst['fp'], fp)
print(f"regular/LTF functions checked: {cnt}; order violations: {bad_order}")
print(f"max RR = {worst['RR']:.3f} (proof bound {2*L1:.3f});  max RQ = {worst['RQ']:.3f} (proof bound 19.07);  max FEI+ ratio = {worst['fp']:.3f}")

# composition sanity check: gates AND2, OR2, MAJ3, XOR2 over leaves that are LTFs or read-k DNFs on disjoint variables
def leaf(nv, kind):
    if kind == 'ltf':
        w = rng.exponential(size=nv); theta = float(rng.uniform(-0.6, 0.6) * w.sum())
        return ltf(w, theta, nv)
    xs = np.arange(1 << nv, dtype=np.int64)
    terms = random_nonmono(nv, 2, [2, 3, 3, 2, 4], rng, pneg=0.3)
    sat = np.zeros(1 << nv, dtype=bool)
    for (mm, v) in terms: sat |= (xs & mm) == v
    return np.where(sat, -1, 1).astype(np.int8)

def compose(gate, leaves, sizes):
    n = sum(sizes); N = 1 << n; xs = np.arange(N); vals = []; off = 0
    for tt, s in zip(leaves, sizes):
        vals.append(tt[(xs >> off) & ((1 << s) - 1)]); off += s
    V = np.stack(vals).astype(int)          # -1 = true
    B = (V == -1)
    if gate == 'AND': out = B.all(axis=0)
    elif gate == 'OR': out = B.any(axis=0)
    elif gate == 'MAJ': out = B.sum(axis=0) >= 2
    else: out = (B.sum(axis=0) % 2) == 1
    return np.where(out, -1, 1).astype(np.int8), n

best = {}
for gate, ar in (('AND', 2), ('OR', 2), ('XOR', 2), ('MAJ', 3)):
    for r in range(30):
        sizes = [int(rng.integers(3, 6)) for _ in range(ar)]
        leaves = [leaf(s, rng.choice(['ltf', 'dnf'])) for s in sizes]
        tt, n = compose(gate, leaves, sizes)
        if np.all(tt == tt[0]): continue
        P = spectrum(tt); pc = popcounts(n)
        nz = P > 1e-300; H = float(-(P[nz] * np.log2(P[nz])).sum()); I = float((P * pc).sum())
        fp = feiplus_ratio(P, pc)
        b = best.setdefault(gate, [0.0, 0.0])
        b[0] = max(b[0], H / I); b[1] = max(b[1], fp if fp == fp else 0.0)
for gate, (hi, fp) in best.items():
    print(f"composition {gate}: max H/I = {hi:.3f}, max FEI+ ratio = {fp:.3f}")
