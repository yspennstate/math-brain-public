"""Independent check of the 'Every T' reduction (agent B, REFUTATION_T2.md), by agent A.
Built from the mechanism at general T in sign-normalised coordinates (conjectured answers give means 2 | 1 in the batch holding the
record): the last-step inner difference I_SAME - I_ANTI at a T = 4 or T = 5 prefix, computed directly, against beta * Delta(A, G)
where Delta is read off the T = 3 mechanism at a T = 3 prefix (h1, h2) with the same (A, G) (solved for). If the reduction holds
the two agree to quadrature error."""
import numpy as np
from scipy.optimize import brentq
E = np.exp(0.5)
phi = lambda x: np.exp(-x * x / 2) / np.sqrt(2 * np.pi)
z = np.linspace(-12, 12, 120001); hz = z[1] - z[0]; wz = np.full(z.size, hz); wz[0] = wz[-1] = hz / 2


def inner(gpre, same):
    """I(g) = int (p - e q)_+ dg_T at prefix gpre, T = len(gpre) + 1, directly from the mixture over the batch holding i."""
    T = len(gpre) + 1; P0 = np.prod(phi(np.asarray(gpre)))
    a = sum(phi(gpre[t] - 2) / phi(gpre[t]) for t in range(T - 1)) * P0 / T
    c = sum(phi(gpre[t] - 1) / phi(gpre[t]) for t in range(T - 1)) * P0 / T
    b = P0 / T
    mx, mxp = (0.0, -1.0) if same else (2.0, 1.0)
    p = a * phi(z) + b * phi(z - mx); q = c * phi(z) + b * phi(z - mxp)
    return (np.maximum(p - E * q, 0) * wz).sum(), b


def AG(g):
    x = np.exp(np.asarray(g) - 0.5); return (x ** 2).sum() / np.e, x.sum()


for g in ((0.3, 1.6, -0.4), (-0.5, 2.1, 0.0, 0.4), (0.4, 2.5, 2.0), (-0.2, 2.3, 1.9, 2.4)):
    s1, b = inner(list(g), True); s0, _ = inner(list(g), False); direct = s1 - s0
    A, G = AG(g)
    # T = 3 prefix (h1, h2) with x1 + x2 = G, x1^2 + x2^2 = e A: x1, x2 roots of t^2 - G t + (G^2 - e A)/2
    disc = 2 * np.e * A - G ** 2
    x1, x2 = (G - np.sqrt(disc)) / 2, (G + np.sqrt(disc)) / 2
    h = [np.log(x1) + 0.5, np.log(x2) + 0.5]
    t1, b3 = inner(h, True); t0, _ = inner(h, False)
    red = b * (t1 - t0) / b3
    print(f"T={len(g)+1} prefix {g}: eA/G^2 {np.e*A/G**2:.4f}  direct {direct:+.10e}  via T=3 {red:+.10e}  rel {abs(direct-red)/abs(direct):.1e}")

print("-- prefixes with eA/G^2 < 1/2 (no T = 3 twin): compare with a DIFFERENT prefix of the same length and the same (A, G)")
for g in ((1.0, 0.2, 0.9), (2.0, -1.0, 0.5, 1.5)):
    s1, b = inner(list(g), True); s0, _ = inner(list(g), False); direct = s1 - s0
    A, G = AG(g); x = np.exp(np.asarray(g) - 0.5)
    for f in (0.9, 0.8, 1.1, 0.7, 1.2):
        rest = x[2:] * f; S1 = G - rest.sum(); S2 = np.e * A - (rest ** 2).sum(); disc = 2 * S2 - S1 ** 2
        if disc > 0 and S1 > np.sqrt(disc):
            y = np.concatenate([[(S1 - np.sqrt(disc)) / 2, (S1 + np.sqrt(disc)) / 2], rest]); break
    h = list(np.log(y) + 0.5); t1, b2 = inner(h, True); t0, _ = inner(h, False); red = b * (t1 - t0) / b2
    print(f"T={len(g)+1} prefix {g} vs {tuple(round(v,4) for v in h)}: direct {direct:+.10e}  twin {red:+.10e}  rel {abs(direct-red)/abs(direct):.1e}")
r = np.exp(np.array([2.1, 2.6])); print("B ratio range eA/G^2 =", (1 + r ** 2) / (1 + r) ** 2, " (1/m <= 1/2 for every m >= 2)")
