"""Independent one-dimensional quadrature for the alpha=1 orientation example.

The law is proved by the conditional Gaussian mixture in i01_entrance.md.
This numerical check only reports the two illustrative probabilities there.
"""

from math import asin, pi, sqrt, tan
from scipy.integrate import quad


def averaged_asin(correlation):
    return (2 / pi) * quad(
        lambda theta: asin(max(-1.0, min(1.0, correlation(tan(theta))))),
        0,
        pi / 2,
        epsabs=1e-12,
        epsrel=1e-12,
    )[0]


axis = averaged_asin(lambda t: 1 / sqrt(1 + 3 * t * t))
symmetric = averaged_asin(lambda t: (3 - t * t) / (3 + t * t))
print(f"X_A selected mark probability: {0.75 - axis / (2 * pi):.10f}")
print(f"X_B selected mark probability: {0.75 - symmetric / (2 * pi):.10f}")
print(f"fixed-Gram Gaussian-angle shortcut: {0.75 - asin(0.5) / (2 * pi):.10f}")
