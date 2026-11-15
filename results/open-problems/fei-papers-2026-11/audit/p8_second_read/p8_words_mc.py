"""Spot checks of paper 8 Theorem 1.1 (i)-(iii) by Monte Carlo of Toeplitz word volumes."""
import numpy as np
from p8_moment_mc import vol

def pairs_of(word):
    pos = {}
    for i, c in enumerate(word, 1):
        pos.setdefault(c, []).append(i)
    return [tuple(v) for v in pos.values()], len(word)

rng = np.random.default_rng(7)
N = 4_000_000
def pT(word):
    pr, n = pairs_of(word)
    return vol(pr, n, "T", N, rng)

for r in (2, 3, 4, 5):
    w = list(range(r)) * 2
    p, se = pT(w)
    print(f"(ii) w_{r}: {p:.4f} +- {se:.4f}  target 2/(r+1) = {2/(r+1):.4f}")
p, se = pT("a1212a".replace("1", "b").replace("2", "c"))
print(f"(i) a w a, w=1212: {p:.4f} +- {se:.4f}  target p_T(1212) = 0.6667")
p, se = pT("abab" + "cdcd")
print(f"(i)/(iii) 1212.3434: {p:.4f} +- {se:.4f}  >= 4/9 = 0.4444; profile product integral = int f2^2")
# f_{w_2}(x) = (1-x^2)/2 + (1-(1-x)^2)/2 ; int f^2 exactly
xs = np.linspace(0, 1, 200001)
f2 = (1 - xs**2) / 2 + (1 - (1 - xs)**2) / 2
print("   int f_{w2}^2 =", np.trapezoid(f2**2, xs))
p, se = pT("ab" + "cc" + "ab")
print(f"(i) ear inserted into 1212 gap: {p:.4f} +- {se:.4f}  target 0.6667")
