"""Sensitivity test of verify_rho23: recompute all constants at a different c and check the certificate
FAILS when c is below the relaxation supremum for that rho (rho=3 e odd: relaxation sup 2.914374)."""
import sys
from mpmath import iv, mpf, mp
import verify_rho23 as V
def setc(cval):
    V.C = iv.mpf(cval); V.KAP = V.C/2 - 1; V.DEL = 2 - V.C/2
    V.PSI = V.log2(1 + iv.mpf(2) ** (-V.C))
    V.GA = V.Gpair(2, 1) / V.SA
    V.GB = (V.KAP * (V.L10 - 2) - V.PSI) / (V.L10 - 1)
def best_mu(rho, e_odd):
    # coarse scan of mu with the interval certificate itself (K small)
    best = None
    for k in range(-60, 1):
        mu = str(k / 20)
        tot, _ = V.certificate(rho, e_odd, mu, 400)
        if best is None or tot < best[0]: best = (tot, mu)
    return best
for cval in ("2.90", "2.92"):
    setc(cval)
    tot, mu = best_mu(3, True)
    tot2, M = V.certificate(3, True, mu, 2000)
    print(f"c={cval}: rho=3 e odd best certified bound over mu grid = {float(tot2):+.5f} at mu={mu}",
          "-> FAIL (expected for c < 2.9144)" if tot2 >= 0 else "-> PASS")
