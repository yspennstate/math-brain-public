"""Does the extremal AND/OR slack Gamma survive every three-input gate?

For a k-input gate G on independent inputs of measures p_i, the composition lemma gives
H(g) <= C I(g) - [ sum_i It_i (Gamma(p_i) + h(V_i)) / V_i - Ht_G ], so the induction closes for formulas using G iff

   (A_G)  Gamma(p_out) <= sum_i It_i(G; p) (Gamma(p_i) + h(V_i)) / V_i - Ht_G(p)     for all input measures p.

This script evaluates D_G(p) = RHS - LHS for every nondegenerate 3-input gate on a grid of (p1, p2, p3) using a
batched biased Walsh transform, with Gamma the numerical fixed point (N = 600, C = 6.4548) interpolated linearly.
A negative D_G beyond grid noise (~5e-3) would mean a 3-input gate can push read-once formulas above beta(1/2).
"""
import sys, os, math, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fei_readonce_gamma import h2
import fei_recsys as R
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

def batched_stats3(vals, P):
    """vals: (8,) +-1 truth values (index bit i = input i, 1 = true); P: (B,3) true-probabilities.
    returns p_out (B,), It (B,3), Ht (B,)"""
    B = P.shape[0]
    Ms = []
    for j in range(3):
        p = P[:, j]; eta = 1 - 2 * p; sig = np.sqrt(np.maximum(1e-300, 1 - eta * eta))
        M = np.empty((B, 2, 2))
        M[:, 0, 0] = 1 - p; M[:, 0, 1] = p
        M[:, 1, 0] = (1 - p) * (1 - eta) / sig; M[:, 1, 1] = p * (-1 - eta) / sig
        Ms.append(M)
    a0 = np.asarray(vals, dtype=float).reshape(2, 2, 2)  # axes: input2, input1, input0 (C-order of the flat index)
    # coefficient c[b, s2, s1, s0]
    c = np.einsum('bsx,bty,buz,xyz->bstu', Ms[2], Ms[1], Ms[0], a0)
    c = c.reshape(B, 8)  # flat index bit0 = s0 (input 0), bit1 = s1, bit2 = s2
    pS = c * c
    with np.errstate(divide="ignore", invalid="ignore"):
        Ht = -np.where(pS > 1e-18, pS * np.log2(np.maximum(pS, 1e-300)), 0.0).sum(axis=1)
    p_out = (1 - c[:, 0]) / 2
    It = np.stack([pS[:, [s for s in range(8) if (s >> i) & 1]].sum(axis=1) for i in range(3)], axis=1)
    return p_out, It, Ht

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    Gam = np.load(os.path.join(here, "gamma_N600_C64548_final.npy")); ps = np.arange(1, 600) / 600
    Gi = lambda x: np.interp(x, ps, Gam)
    g = np.linspace(0.02, 0.98, 33)
    P = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T   # (B,3)
    hV = h2(4 * P * (1 - P)); V = 4 * P * (1 - P); GP = Gi(P)
    base = ((GP + hV) / V)   # (B,3) per-input factor multiplying It_i
    worst = []; t0 = time.time(); n = 0
    for tt in range(256):
        vals = R.tt_values(tt, 3)
        if not R.nondegenerate(tt, 3):
            continue
        p_out, It, Ht = batched_stats3(vals, P)
        ok = (p_out > 0.003) & (p_out < 0.997)
        D = (It * base).sum(axis=1) - Ht - Gi(np.clip(p_out, 1e-6, 1 - 1e-6))
        D = np.where(ok, D, np.inf)
        j = int(np.argmin(D)); n += 1
        worst.append((float(D[j]), tt, [round(float(x), 3) for x in P[j]], round(float(p_out[j]), 4)))
    worst.sort()
    print("3-input gates checked: %d nondegenerate; %.0f s" % (n, time.time() - t0))
    print("ten smallest D_G over the grid (D, gate tt, input measures, output measure):")
    for w in worst[:10]:
        print("  %+.5f  tt=%3d  p=%s  p_out=%.4f" % w)
    # sanity: the 3-input gate AND(a, AND(b, c))-like gates must reproduce AND2-type constraints; e.g. tt = AND3 = 128
    json.dump(worst, open(os.path.join(here, "gate3_check.json"), "w"))
