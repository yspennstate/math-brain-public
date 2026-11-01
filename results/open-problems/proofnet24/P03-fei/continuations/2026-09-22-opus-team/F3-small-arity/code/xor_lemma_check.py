"""Exact check of the hypothesis of the XOR lemma for a stored potential: the node values G_j (Gamma(p)/p at x_j = log2(1/p))
are strictly increasing in j (compared as exact binary rationals), the nodes x_j increase from 1, and the tail slope
(G_J - b*)/K is positive (b* = 8 - 4/ln 2, enclosed with exact_gate.LN2).  Also a floating-point spot check of the
inequality Gamma(p) + Gamma(q) >= Gamma(p + q - 2pq) on a grid, which the lemma proves.
usage: xor_lemma_check.py <npz> [c]"""
import sys, os
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import exact_gate as X
import fgate as F

npz = sys.argv[1]; c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
d = np.load(npz)
xs = [Fr(float(v)) for v in d["xs"]]; G = [Fr(float(v)) for v in d["G"]]
inc_x = all(xs[j + 1] > xs[j] for j in range(len(xs) - 1))
inc_G = all(G[j + 1] > G[j] for j in range(len(G) - 1))
mininc = min(G[j + 1] - G[j] for j in range(len(G) - 1))
K = xs[-1]
bstar_hi = 8 - 4 / X.LN2[1]            # b* = 8 - 4/ln2 is increasing in ln2, so the upper end of ln2 gives the upper b*
tail_lo = (G[-1] - bstar_hi) / K
print("%s: %d nodes, x_0 = %s, K = %s" % (os.path.basename(npz), len(xs), xs[0], K))
print("  nodes strictly increasing: %s ; G strictly increasing: %s (min increment %.3e) ; G_0 = %.10f > 0: %s"
      % (inc_x, inc_G, float(mininc), float(G[0]), G[0] > 0))
print("  tail slope (G_J - b*)/K > %.6f > 0: %s" % (float(tail_lo), tail_lo > 0))
pot = F.Pot(npz, c)
u = np.linspace(-40, 40, 1601)
UU = np.array(np.meshgrid(u, u, indexing="ij")).reshape(2, -1).T
P = 1 / (1 + 2.0 ** (-UU)); p, q = P[:, 0], P[:, 1]
lhs = pot(p) + pot(q) - pot(p + q - 2 * p * q)
print("  float spot check: min Gamma(p)+Gamma(q)-Gamma(p*q) over a 1601^2 logit grid = %.4e (c = %g)" % (lhs.min(), c))
