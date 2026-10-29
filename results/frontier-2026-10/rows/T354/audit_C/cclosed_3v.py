"""c(s) of agent_B/NOTE.md "c(n d) in closed form", evaluated by quadrature for any finite b, plus its two limits
(agent C, 20 Oct 2026). Written from the note's formulas, not from c_closed.py / c_closed_sym.py.

    k = 1 - (1 - e^-t)/s, Q = 1/2 - (1 - e^-t)^2/s - e^(-2t) tanh(s/2)/s,
    cb = avg[1 - 2(1 - e^-t)/s - (1 - e^-2t)/(2s) + 2(1 - e^-t)^2/s^2],   avg over t uniform on [0, s)
    c(s) = K - (3/8) r1 avg Q - (3/4) r2 cb/K + (15/8) r1 avg[k Q]/K,   r1 = (B4 - B2^2)/B2^2, r2 = E[b (b^2 - B2)^2]/(B2 B3)
usage: python cclosed_3v.py [B1V B2V BO]   (b on 0.1, 0.1, 0.8; default 6 2 -1; '9 -1 -1' is the two-valued 9/-1 model)
"""
import sys

import numpy as np

bv = np.array([float(v) for v in sys.argv[1:4]]) if len(sys.argv) > 3 else np.array([6.0, 2.0, -1.0])
p = np.array([0.1, 0.1, 0.8])
B = {k: p @ bv ** k for k in (1, 2, 3, 4)}
assert abs(B[1]) < 1e-12
r1 = (B[4] - B[2] ** 2) / B[2] ** 2
r2 = (p @ (bv * (bv ** 2 - B[2]) ** 2)) / (B[2] * B[3])
x, w = np.polynomial.legendre.leggauss(400)


def c(s, r1=r1, r2=r2):
    t = 0.5 * s * (x + 1)
    ww = 0.5 * w  # weights of the average over [0, s)
    em = 1 - np.exp(-t)
    k = 1 - em / s
    Q = 0.5 - em ** 2 / s - np.exp(-2 * t) * np.tanh(s / 2) / s
    cbi = 1 - 2 * em / s - (1 - np.exp(-2 * t)) / (2 * s) + 2 * em ** 2 / s ** 2
    K, aQ, cb, akQ = ww @ k, ww @ Q, ww @ cbi, ww @ (k * Q)
    Kc = 1 - 1 / s + (1 - np.exp(-s)) / s ** 2
    assert abs(K - Kc) < 1e-7, (K, Kc)  # Kc cancels at small s
    return K - 0.375 * r1 * aQ - 0.75 * r2 * cb / K + 1.875 * r1 * akQ / K


print("b %s on %s:"[:0] + "b %s on %s: B2 %g B3 %g B4 %g r1 %.6f r2 %.6f" % (bv.tolist(), p.tolist(), B[2], B[3], B[4], r1, r2))
print("c(0+) claimed 1/2 - r2/4 = %.6f; c(1e-4) = %.6f, c(1e-3) = %.6f" % (0.5 - r2 / 4, c(1e-4), c(1e-3)))
print("c(inf) claimed 1 + (3/4)(r1 - r2) = %.6f; c(1e3) = %.6f, c(1e4) = %.6f" % (1 + 0.75 * (r1 - r2), c(1e3), c(1e4)))
print("(1 - c) s at s 1e4: %.4f, claimed 1 + 3 r1/8 = %.4f (two-valued only: r1 = r2)" % ((1 - c(1e4)) * 1e4, 1 + 0.375 * r1))
for s in (0.2, 0.5, 1, 2, 5, 10, 20, 50):
    print("s %5g  c %+.6f" % (s, c(s)))
print("wrong-formula foils (to show the test can tell): r2 set to r1 / r1 set to r2")
for s in (0.2, 1, 2, 5, 10):
    print("s %5g  c %+.6f  r2->r1 %+.6f  r1->r2 %+.6f" % (s, c(s), c(s, r2=r1), c(s, r1=r2)))
print("the four terms (K, -(3/8) r1 avgQ, -(3/4) r2 cb/K, +(15/8) r1 avg[kQ]/K), the last being the E[b eta^3] step")
for s in (0.2, 1, 2, 5, 10):
    t = 0.5 * s * (x + 1)
    ww = 0.5 * w
    em = 1 - np.exp(-t)
    k = 1 - em / s
    Q = 0.5 - em ** 2 / s - np.exp(-2 * t) * np.tanh(s / 2) / s
    cbi = 1 - 2 * em / s - (1 - np.exp(-2 * t)) / (2 * s) + 2 * em ** 2 / s ** 2
    K = ww @ k
    print("s %5g  %+.4f %+.4f %+.4f %+.4f" % (s, K, -0.375 * r1 * (ww @ Q), -0.75 * r2 * (ww @ cbi) / K, 1.875 * r1 * (ww @ (k * Q)) / K))
