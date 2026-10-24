"""Per-move second-order change of the effective cost W = V + h(V) near 1/2, with flat inputs (V = C at the inputs):
Delta(eps) = s_flat + h(V_out) - C - sum_i (It_i/V_i) h(V_i),   s_flat = sum_i (It_i/V_i)(C + h(V_i)) - Htilde,
so W_out - C = sum_i (It_i/V_i)(W_i - C) + Delta.  Delta < 0 means the move lowers the effective cost below the linear
image of its inputs.  Moves: A (all core at bias eps), B (core 0), Ba (aux 9), A+ (all 18 at eps).
Fit Delta = -Z eps^2 log2(1/eps^2) + K eps^2."""
import math
import numpy as np
import fast_gate as FG

C = 6.521845710923046575


def h2(v):
    return 0.0 if v <= 0 or v >= 1 else -v * math.log2(v) - (1 - v) * math.log2(1 - v)


def delta(mask, eps):
    mu = np.zeros(18); mu[mask] = eps
    p = (1 - mu) / 2
    Ht, It, po, c = FG.evaluate(p)
    V = 1 - mu * mu
    lin = sum(It[i] / V[i] * h2(V[i]) for i in range(18))
    sflat = sum(It[i] / V[i] * (C + h2(V[i])) for i in range(18)) - Ht
    Vout = 1 - c[0] ** 2
    return sflat + h2(Vout) - C - lin, sflat - C, (1 - c[0]) / 2


moves = {"A": list(range(9)), "B": [0], "Ba": [9], "A+": list(range(18))}
for nm, mask in moves.items():
    print("move %s:" % nm)
    rows = []
    for eps in (3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5):
        d, sf, po = delta(mask, eps)
        L = math.log2(1 / eps ** 2)
        rows.append((eps, d, L))
        print("   eps=%.0e  Delta=%+.4e  Delta/eps^2=%+.5f  L=%.2f  (s_flat-C=%+.3e, p_out-1/2=%+.3e)" % (eps, d, d / eps ** 2, L, sf, po - 0.5))
    # least-squares fit Delta/eps^2 = -Z L + K on the three smallest eps
    X = np.array([[-r[2], 1.0] for r in rows[-4:]]); y = np.array([r[1] / r[0] ** 2 for r in rows[-4:]])
    Z, K = np.linalg.lstsq(X, y, rcond=None)[0]
    print("   fit Delta ~ -%.5f eps^2 log2(1/eps^2) + %.5f eps^2  -> Delta < 0 for eps < %.2e" % (Z, K, 2 ** (-K / (2 * Z)) if Z > 0 and K > 0 else float('nan')))

# exactly balanced pairs: core 0 at +eps, core 1 solved (E F = 0); aux 9 at +eps, aux 10 at -eps
print("balanced pairs (Delta = s_flat - C - sum (It/V) h(V_i), output balanced so h(V_out) = 0):")
W0 = FG.evaluate(np.full(18, 0.5))[3]
g01 = W0[(1 << 0) | (1 << 1)]; c0 = W0[1]
for eps in (3e-2, 1e-2, 3e-3, 1e-3, 3e-4):
    mu1 = -c0 * eps / (c0 + g01 * eps)
    for lab, mask_mu in (("cc+ (0,1)", {0: eps, 1: mu1}), ("aa (9,10)", {9: eps, 10: -eps})):
        mu = np.zeros(18)
        for k, v in mask_mu.items():
            mu[k] = v
        p = (1 - mu) / 2
        Ht, It, po, c = FG.evaluate(p)
        V = 1 - mu * mu
        lin = sum(It[i] / V[i] * h2(V[i]) for i in range(18))
        sflat = sum(It[i] / V[i] * (C + h2(V[i])) for i in range(18)) - Ht
        print("   %s eps=%.0e: |E F|=%.1e  s_flat-C=%+.4e  Delta=%+.4e  Delta/eps^2=%+.4f" % (lab, eps, abs(c[0]), sflat - C, sflat - C - lin, (sflat - C - lin) / eps ** 2))
