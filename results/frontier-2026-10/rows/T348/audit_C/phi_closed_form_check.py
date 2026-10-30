# Independent check (agent C, 20 Oct): the closed forms in DOSSIER.md 19 Oct against a brute-force sup on a grid.
import numpy as np
I = lambda t: -0.5 * np.log1p(-t * t)
def phi_brute(a, lam):
    t = np.linspace(-1 + 1e-12, 1 - 1e-12, 2_000_001)
    ok = I(t) <= a
    return np.max(t[ok] + (a - I(t[ok])) / lam)
def phi_closed(a, lam):
    s = np.sqrt(1 + 4 * lam * lam)
    lstar = np.exp(2 * a) * np.sqrt(1 - np.exp(-2 * a))
    if lam <= lstar:
        return a / lam + (s - 1 - np.log((1 + s) / 2)) / (2 * lam), "uncond"
    return np.sqrt(1 - np.exp(-2 * a)), "cond"
def alpha1(lam):
    s = np.sqrt(1 + 4 * lam * lam)
    return lam - (s - 1 - np.log((1 + s) / 2)) / 2
worst = 0
for lam in (0.2, 0.5, 1, 2, 3, 5, 10):
    for a in (0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 1.5):
        pb = phi_brute(a, lam); pc, ph = phi_closed(a, lam)
        worst = max(worst, abs(pb - pc))
        print("lam %5.2f a %4.2f brute %.6f closed %.6f %s" % (lam, a, pb, pc, ph))
    a1 = alpha1(lam); p1, ph = phi_closed(a1, lam)
    print("  alpha_1(%g) = %.6f, phi there %.6f (%s), tau_2 there %.6f" % (lam, a1, p1, ph, np.sqrt(1 - np.exp(-4 * a1))))
print("max |brute - closed| = %.2e" % worst)
