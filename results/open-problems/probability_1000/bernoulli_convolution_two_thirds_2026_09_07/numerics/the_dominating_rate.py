"""Where does the octave integral's mass actually sit? The large-deviation profile, measured.

With s(theta) = (1/K) sum_(m<=K) log(1 + cos 2 pi theta (3/2)^m), the octave integral is
int_(1/3)^(2/3) e^(K s) d theta. A TYPICAL theta has s -> -log 2 = -0.6931 (checked), so the typical
integrand is 2^-K while the integral is ~0.016: the mass is carried by rare theta with s well above
typical. This finds the DOMINATING RATE s* - the s maximising the contribution e^(K s) P(s) - and the
measure of the carrying set. If s* is stable in K and the carrying measure shrinks like e^(-K I(s*))
with s* = I(s*), the flatness is a large-deviation balance and explaining the gap constant needs exactly
that rate function. Sampling only; nothing iterated, nothing large.
"""
import numpy as np

NS = 2_000_000
rng = np.random.default_rng(20260908)
print(f"{'K':>4} {'typical s':>11} {'s* (dominating)':>16} {'carrying meas':>14} {'I(s*)':>9} {'check s*-I':>11}")
for K in (10, 14, 18, 22, 26):
    th = 1/3 + rng.random(NS) / 3.0
    s = np.zeros(NS)
    for m in range(K + 1):
        s += np.log(np.maximum(1.0 + np.cos(2*np.pi*np.mod(th * 1.5**m, 1.0)), 1e-300))
    s /= (K + 1)
    lo, hi = s.min(), s.max()
    nb = 400
    h, edges = np.histogram(s, bins=nb, range=(lo, hi))
    mid = 0.5*(edges[:-1] + edges[1:])
    P = h / NS                                  # empirical probability per bin
    contrib = P * np.exp((K + 1) * mid)         # contribution of each rate band
    j = int(contrib.argmax())
    sstar = mid[j]
    meas = P[j]
    # rate function I(s*) = -(1/K) log P(s*)  (per-sample band probability)
    I = -np.log(max(P[j], 1e-300)) / (K + 1)
    print(f"{K:>4} {s.mean():>11.4f} {sstar:>16.4f} {meas:>14.3e} {I:>9.4f} {sstar - I:>11.4f}")
print()
print("typical s should sit near -log 2 = -0.6931; if s* - I(s*) is near 0 and stable, the octave")
print("integral is a large-deviation balance and the gap constant is that balance, not a simpler object.")
