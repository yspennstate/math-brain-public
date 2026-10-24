"""Hard families: tilt fluxes, terminal entropy, KKL split, per-coordinate shares, pointwise tests.

Columns (entropies in nats; H/I also in bits):
  HI_bits   H/I in bits
  K/I, R/I  KKL split H = K + R, K = sum_S (w/|S|) sum_{i in S} log(1/Inf_i) <= 2 I (proved)
  Hinf/I    terminal entropy H(q_infty) of the normalized tilt over I
  supE      sup over the t-grid of (-dH(q_t)/dt) / E_t|S|
  supV      sup over the t-grid of (-dH(q_t)/dt) / Var_t|S|
  supP      sup over the t-grid of G(t) / (M(t) + Kr(t) + N(t))  (unnormalized, KKL-augmented test)
  Amax      max_i A_i / Inf_i, A_i = sum_{S ni i} w(S) log(1/w(S)) / |S| (per-coordinate share)
"""
import math, sys
import numpy as np
from fei_core import *

lowprio()
TGRID = np.concatenate([np.linspace(0, 2, 41), np.linspace(2.25, 30, 112)])


def analyse(f, name, P, tgrid=TGRID):
    sp = Spec.from_table(f)
    n = sp.n
    if n >= 17:
        tgrid = np.concatenate([np.linspace(0, 2, 17), np.linspace(2.5, 16, 28)])
    H, I = sp.H(), sp.I()
    K, R, inf = sp.kkl_split()
    W, h = sp.levels()
    kmin = int(sp.ks.min())
    Hinf = h[kmin] if kmin > 0 else 0.0
    # per-set sum of log(1/Inf_i)
    li = np.where(inf > 0, -np.log(np.maximum(inf, 1e-300)), 0.0)
    s = np.zeros(sp.ws.size)
    for i in range(n):
        s += li[i] * ((sp.idx >> i) & 1)
    supE = supV = supP = 0.0
    argE = argP = None
    for t in tgrid:
        d = sp.tilt(t)
        if d['Ek'] > 1e-12 and d['mdHdt'] / d['Ek'] > supE:
            supE = d['mdHdt'] / d['Ek']; argE = t
        if d['Vk'] > 1e-12:
            supV = max(supV, d['mdHdt'] / d['Vk'])
        u = sp.ws * np.exp(-2 * t * sp.ks)
        G = float((u * sp.ks * sp.L).sum()); M = float((u * sp.ks ** 2).sum())
        Nn = float((u * sp.ks).sum()); Kr = float((u * s).sum())
        den = M + Kr + Nn
        if den > 1e-300 and G / den > supP:
            supP = G / den; argP = t
    # per-coordinate share
    Amax = 0.0
    nz = sp.ks > 0
    for i in range(n):
        sel = (((sp.idx >> i) & 1) == 1) & nz
        if inf[i] > 0:
            Ai = float((sp.ws[sel] * sp.L[sel] / sp.ks[sel]).sum())
            Amax = max(Amax, Ai / inf[i])
    P("%-26s n=%2d I=%9.5f HI_bits=%8.5f K/I=%7.4f R/I=%7.4f Hinf/I=%8.4f supE=%9.3f(t=%s) supV=%8.3f supP=%7.4f(t=%s) Amax=%8.4f"
      % (name, n, I, H / I / LN2, K / I, R / I, Hinf / I, supE, argE, supV, supP, argP, Amax))
    return dict(H=H, I=I, K=K, R=R)


def main():
    lines = []
    def P(*a):
        s = ' '.join(str(x) for x in a); lines.append(s); print(s, flush=True)
    P("# entropies in nats unless marked; t-grid up to 30")
    # 1. two-point flips of x0 x1 (balanced): edge version (a, a xor e_0) and a spread version
    for n in [6, 8, 10, 12, 14, 16]:
        base = parity(n, [0, 1])
        P_edge = flip(base, [0, 1])                          # x=0 and x=e_0
        b = sum(1 << i for i in [0] + list(range(2, n)))     # flip coords 0,2..n-1
        P_spread = flip(base, [0, b])
        analyse(P_edge, "x0x1 edge 2-flip", P)
        analyse(P_spread, "x0x1 spread 2-flip", P)
    # 2. one-point flips
    for n in [6, 10, 14]:
        analyse(flip(np.ones(1 << n, dtype=np.int8), [0]), "const 1-flip", P)
        analyse(flip(dictator(n, 0), [0]), "dictator 1-flip", P)
    for n in [7, 11, 15]:
        analyse(flip(majority(n), [0]), "maj 1-flip", P)
    # 3. bent and bent+flip
    for m in [2, 3, 4, 5, 6, 7]:
        analyse(inner_product(m), "bent IP", P)
        analyse(flip(inner_product(m), [0]), "bent+1flip", P)
    # 4. tribes
    for (w, c) in [(2, 3), (2, 5), (3, 3), (3, 5), (4, 4), (4, 5), (5, 4)]:
        analyse(tribes(w, c), "tribes %dx%d" % (w, c), P)
    # 5. x0 * Maj(rest)
    for n in [8, 12, 16, 20]:
        idx = np.arange(1 << n, dtype=np.int64)
        mj = majority(n - 1)
        f = np.where((idx & 1) == 1, -1, 1).astype(np.int8) * mj[idx >> 1]
        analyse(f.astype(np.int8), "x0*Maj%d" % (n - 1), P)
    # 6. majority
    for n in [9, 13, 17, 21]:
        analyse(majority(n), "maj", P)
    # 7. addressing
    for a in [2, 3, 4]:
        analyse(addressing(a), "addressing a=%d" % a, P)
    # 8. recursive majority 3x3
    idx = np.arange(1 << 9, dtype=np.int64)
    def maj3bits(b0, b1, b2):
        return ((b0 + b1 + b2) >= 2).astype(np.int64)
    blocks = [maj3bits((idx >> (3 * j)) & 1, (idx >> (3 * j + 1)) & 1, (idx >> (3 * j + 2)) & 1) for j in range(3)]
    rm = maj3bits(*blocks)
    analyse(np.where(rm == 1, -1, 1).astype(np.int8), "recmaj3^2", P)
    # 9. Numaro's g
    analyse(load_numaro(), "Numaro g (18)", P)
    with open('../logs/families.log', 'w') as fh:
        fh.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
