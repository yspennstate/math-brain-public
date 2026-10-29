"""Independent check of REFUTATION_T2.md (agent A, 19 Oct). Model, written from the ABLQ_S definition and not from the
candidate's scripts: T = 2, one record differs (x holds u, x' holds bottom with psi(bottom) = 0), every other record holds w, the shuffle
puts the record in batch 1 or 2 with probability 1/2, outputs shifted by the known b psi_t(w). Step 1 uses psi_1(u) = p1u, psi_1(w) = p1w.
Step 2 may depend on g1: when the record is in batch 2 the g2 means are a = psi2(u) - psi2(w) (x) and c = -psi2(w) (x'); in batch 1 they
are 0 for both. Hockey stick D = int (p - e^eps q)_+ ."""
import numpy as np, sys
from scipy.stats import norm
from scipy.integrate import quad
s, eps = 1.0, 0.5; E = np.exp(eps)
def I(g1, a, c, m, mp):
    """inner integral over g2 at fixed g1; m, mp = step-1 means of the batch-1 case under x, x'"""
    A1 = 0.5 * norm.pdf(g1, m, s); A0 = 0.5 * norm.pdf(g1, 0, s); B1 = 0.5 * norm.pdf(g1, mp, s)
    f = lambda g2: max(A1 * norm.pdf(g2, 0, s) + A0 * norm.pdf(g2, a, s) - E * (B1 * norm.pdf(g2, 0, s) + A0 * norm.pdf(g2, c, s)), 0.0)
    return quad(f, -12, 14, limit=200, points=[0, a, c])[0]
m, mp = -2.0, -1.0
# 1. the conjectured pair by an independent 2-D integral of P_S, Q_S as defined in the conjecture (means 2e_t vs e_t)
P = lambda x, y: 0.5 * (norm.pdf(x, 2, s) * norm.pdf(y, 0, s) + norm.pdf(x, 0, s) * norm.pdf(y, 2, s))
Q = lambda x, y: 0.5 * (norm.pdf(x, 1, s) * norm.pdf(y, 0, s) + norm.pdf(x, 0, s) * norm.pdf(y, 1, s))
from scipy.integrate import dblquad
DPQ = dblquad(lambda y, x: max(P(x, y) - E * Q(x, y), 0), -10, 12, -10, 12, epsabs=1e-10)[0]
DQP = dblquad(lambda y, x: max(Q(x, y) - E * P(x, y), 0), -10, 12, -10, 12, epsabs=1e-10)[0]
print(f"D(P_S||Q_S) = {DPQ:.6f}   D(Q_S||P_S) = {DQP:.6f}")
# 2. pointwise: ANTI (a,c) = (2,1) vs SAME (0,-1) and the best (a, c) on a grid of the full allowed set
grid = [(pu - pw, -pw) for pu in np.linspace(-1, 1, 9) for pw in np.linspace(-1, 1, 9)]
for g1 in (-3.5, -3.0, -2.5, -2.0, -1.5, -1.0, 0.0, 1.0):
    ia, isame = I(g1, 2, 1, m, mp), I(g1, 0, -1, m, mp)
    best = max(grid, key=lambda ac: I(g1, ac[0], ac[1], m, mp)); ib = I(g1, *best, m, mp)
    print(f"g1={g1:+.1f}  I_ANTI={ia:.10f}  I_SAME={isame:.10f}  diff={isame-ia:+.3e}  best (a,c)={best} I={ib:.10f}")
# 3. totals: ANTI everywhere, and pointwise max(ANTI, SAME)
gs = np.linspace(-9, 7, 1601); w = np.full(len(gs), gs[1] - gs[0]); w[[0, -1]] /= 2
ia = np.array([I(g, 2, 1, m, mp) for g in gs]); isa = np.array([I(g, 0, -1, m, mp) for g in gs])
print(f"total ANTI = {(w*ia).sum():.6f}   total max(ANTI,SAME) = {(w*np.maximum(ia,isa)).sum():.6f}   SAME wins on g1 in "
      f"[{gs[isa>ia].min() if (isa>ia).any() else float('nan'):.2f}, {gs[isa>ia].max() if (isa>ia).any() else float('nan'):.2f}] ({(isa>ia).sum()} pts)")
