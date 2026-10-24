"""Cross-checks of fgate.py against numbers published elsewhere in the repository.
1. AND gate: c_AND(p,q) against the certificate's own -Phi/((1-p)(1-q)) (fei_cert_vi.E_fun), Pr = probability of true.
2. G10 (account03/B12 restriction of Numaro's g) at uniform bias: c = 4(H/(I-1) - C0) > 0.0182891265514229.
3. Numaro's g at p1 = 3/8 under Gamma_dagger = Gamma_0 + 0.268204856 p(1-p): D = -0.01761141995580175...
4. Numaro's g at p1 = 223/456 under the same potential: -0.038023735 < D < -0.038023734.
"""
import sys, os, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "2026-09-21-readonce-certificate", "code"))
import fgate as F
fgate_lp = F.lowprio()
import fei_cert_vi as V

INP = os.path.join(HERE, "..", "..", "inputs")
pot = F.Pot(os.path.join(INP, "cert_vi_h96k40.npz"), 0.0)

# 1. AND
AND = np.array([1.0, 1.0, 1.0, -1.0])
rng = np.random.default_rng(1)
P = np.column_stack([2.0 ** -rng.uniform(0.01, 12, 2000), 2.0 ** -rng.uniform(0.01, 12, 2000)])
P = np.where(rng.random(P.shape) < 0.3, 1 - P, P)
c1, D1, W1 = F.cG(AND, P, pot)
p, q = P[:, 0], P[:, 1]
E = V.E_fun(p, q, np.log2(1 / p), np.log2(1 / q))
need = -(pot(p) / p + pot(q) / q - pot(p * q) / (p * q) - E) / ((1 - p) * (1 - q))
ok = np.isfinite(need) & (W1 > 1e-9)
print("1. AND: max |c_gate - c_cert| = %.3e over %d points (relative %.3e)" %
      (np.max(np.abs(c1[ok] - need[ok])), ok.sum(), np.max(np.abs(c1[ok] - need[ok]) / (1e-3 + np.abs(need[ok])))))

# 2. G10
g = np.load(os.path.join(INP, "numaro18_pm1_table.npy")).astype(float)
fix = {9: 0, 10: 0, 11: 0, 12: 1, 13: 1, 14: 0, 15: 1, 16: 1}
free = [0, 1, 2, 3, 4, 5, 6, 7, 8, 17]
idx = np.zeros(1 << 10, dtype=np.int64)
for y in range(1 << 10):
    x = 0
    for j, v in fix.items():
        x |= v << j
    for l, j in enumerate(free):
        x |= ((y >> l) & 1) << j
    idx[y] = x
G10 = g[idx]
c, D, W = F.cG(G10, np.full((1, 10), 0.5), pot)
print("2. G10 balanced: sum = %d; c at uniform = %.15f (fleet: > 0.0182891265514229)" % (int(G10.sum()), c[0]))

# 3, 4. Numaro's g at one biased core input
potd = F.Pot(os.path.join(INP, "cert_vi_h96k40.npz"), 0.268204856)
for p1, ref in ((3 / 8, "-0.01761141995580175378949"), (223 / 456, "(-0.038023735, -0.038023734)")):
    Pb = np.full((1, 18), 0.5); Pb[0, 0] = p1
    D, W, po, It = F.stats(g, Pb, potd)
    D0, W0, _, _ = F.stats(g, Pb, pot)
    print("   g at p1=%.6f: p_out = %.10f (x2048 = %.4f), D_dagger = %.17f  [fleet %s];  c_G (base) = %.10f  W = %.10f"
          % (p1, po[0], po[0] * 2048, D[0], ref, -D0[0] / W0[0], W0[0]))
