"""Validation of vicore against the groups' code: gate spectra (F3 fgate), the AND operator (general spectrum vs the
E-form), the read-once iteration (F1 ro_gamma values at C_rec), the G7 witness D with the stored potential (F3)."""
import os, sys, math, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio()
TEAM = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(TEAM, "F3-small-arity", "code"))
import fgate as F

rng = np.random.default_rng(1)
# 1. spectra vs fgate
worst = 0.0
for k in (2, 3, 4, 5, 7):
    for _ in range(20):
        tab = 1.0 - 2.0 * rng.integers(0, 2, 1 << k)
        p = rng.uniform(0.01, 0.99, k)
        buf = np.empty(1 << k); It = np.empty(k)
        mean, Ht = V.gstats(tab, k, p, buf, It)
        Cf = F.spectrum(tab, p[None, :])[0]
        pS = Cf * Cf
        Ht2 = -np.sum(np.where(pS > 0, pS * np.log2(np.where(pS > 0, pS, 1.0)), 0.0))
        It2 = pS @ F.sel(k)
        worst = max(worst, abs(Ht - Ht2), np.abs(It - It2).max(), abs(mean - Cf[0]))
print("1. gstats vs fgate.spectrum: max abs difference %.2e" % worst)

# 2. AND operator: E-form vs general spectrum
AND = np.array([1.0, 1.0, 1.0, -1.0])      # true iff both inputs true
g = V.Grid()
Gro = np.load(os.path.join(TEAM, "F1-biased-record", "logs", "ro_gamma_Crec.npz"))["G"]
sig = g.sig(Gro)
worst = 0.0
for _ in range(2000):
    p, q = rng.uniform(1e-3, 1 - 1e-3, 2)
    S, po = V.S_batch(AND, 2, np.array([[p, q]]), g.xs, Gro, g.K, sig)
    Lp, Lq = -math.log2(p), -math.log2(q)
    E = 8 * p * (1 - q) * Lp + 8 * q * (1 - p) * Lq + 8 * (1 - p) * (1 - q) + V.psi_s(p * q) - V.psi_s(p) - V.psi_s(q)
    v = q * V.vat(g.xs, Gro, g.K, sig, p) + p * V.vat(g.xs, Gro, g.K, sig, q) - p * q * E
    worst = max(worst, abs(v - S[0]), abs(po[0] - p * q))
print("2. AND move, E-form vs general spectrum: max abs difference %.2e" % worst)

# 3. read-once iteration at C_rec reproduces F1's values
Crec = 6.521845710923046575
t0 = time.time()
res = V.iterate(g, Crec, use_xor=False, verbose=False)
G = res["G"]
ref = {0.5: 6.5218457109, 0.4995: 6.5375636025, 0.49: 6.6164863244, 0.45: 6.4702005347, 0.25: 4.5218457109,
       0.125: 2.6744670965, 0.01: 0.3646248393, 0.001: 0.0527428157}
d = max(abs(float(g.V(G, p)[0]) - v) for p, v in ref.items())
print("3. read-once iteration at C_rec: %s after %d sweeps (%.0f s); max |V - F1| at 8 points = %.2e"
      % (res["reason"], res["it"], time.time() - t0, d))
print("   max |G - G_F1| over nodes = %.2e" % np.abs(G - Gro).max())
res2 = V.iterate(g, Crec, use_xor=True, verbose=False, G0=G)
print("   with XOR added: %s, max change of G %.2e" % (res2["reason"], np.abs(res2["G"] - G).max()))

# 4. G7 witness against the stored potential
MINTERMS = [(1, 3), (0, 4), (2, 3, 4), (0, 1, 5), (1, 4, 6), (2, 4, 6), (1, 5, 6)]
tab7 = np.array([-1.0 if any(all((x >> i) & 1 for i in m) for m in MINTERMS) else 1.0 for x in range(128)])
st = np.load(os.path.join(TEAM, "inputs", "cert_vi_h96k40.npz"))
xs_s, G_s, K_s = st["xs"], st["G"], float(st["xs"][-1])
p = np.array([[0.5, 0.5, 7 / 24, 0.5, 0.5, 2 / 7, 5 / 17]])
D, Wd, po = V.D_batch(tab7, 7, p, xs_s, G_s, K_s, 0.0)
print("4. G7 witness with cert_vi_h96k40: D = %.12e (F3 exact: -6.784395770752e-03), W = %.9f (87741665/522031104 = %.9f),"
      " p_out = %.9f (11483/22848 = %.9f)" % (D[0], Wd[0], 87741665 / 522031104, po[0], 11483 / 22848))
