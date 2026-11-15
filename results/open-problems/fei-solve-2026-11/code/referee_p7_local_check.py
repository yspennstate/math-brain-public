"""Referee check for P7: Phi(a,b) <= 2 sqrt(ab) (Lemma rel) and the constants of Theorem local."""
import math
import numpy as np

lg = math.log2
e = math.e


def eta(x):
    return -x * lg(x) if x > 0 else 0.0


def Phi(a, b):
    return eta(a) + eta(b) - eta(a + b)


xs = np.logspace(-6, 6, 20001)
print("max over x of Phi(x^2,1) - 2x:", max(Phi(x * x, 1.0) - 2 * x for x in xs))

worst = (0, None)
for L in range(3, 81):
    a = 2.0 ** -L
    u = 1 / (64 * L * L)
    th = 1 - L * u * a
    eps = (math.sqrt(a) + math.sqrt(u)) ** 2 / th
    kap = L * u / (4 * th * (1 - u * a / 2))
    b0 = (1 + u) * a
    t2 = 8 / math.log(2) * math.sqrt(kap)
    t3 = eps * lg(e * (3 + 8 / (eps * a * th)))
    t4 = b0 * lg(e * (1 + b0 ** -2))
    B = 2 + t2 + t3 + t4
    if B > worst[0]:
        worst = (B, L)
    if L <= 5:
        print(f"L={L} eps0={eps:.5f} L*eps0={L*eps:.5f} kappa0={kap:.6f} terms {t2:.4f} {t3:.4f} {t4:.4f} bound={B:.4f}")
print(f"largest bound over L=3..80: {worst[0]:.4f} at L={worst[1]}")
