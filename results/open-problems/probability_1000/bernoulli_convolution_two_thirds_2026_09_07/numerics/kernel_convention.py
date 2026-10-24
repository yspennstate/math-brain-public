"""Are the two window kernels the same function in different variables?

The window is an OCTAVE band.  The kernel is the inverse Fourier transform of the band
indicator, normalised to 1 at the origin.  For a band [a,b] (and its mirror [-b,-a]):

    k_[a,b](u) = (1/(b-a)) * int_a^b cos(2 pi t u) dt
               = (1/(b-a)) * (sin(2 pi b u) - sin(2 pi a u)) / (2 pi u)
               = (1/(b-a)) * cos(pi (a+b) u) sin(pi (b-a) u) / (pi u).

Band [1,2]      ->  cos(3 pi u) sin(pi u) / (pi u)                 (the subagent's h)
Band [1/3,2/3]  ->  (3/(pi u)) cos(pi u) sin(pi u / 3)             (my g)

Claim to test: g(u) = h(u/3) identically, i.e. they are ONE kernel and the disagreement was a
choice of frequency variable (m/2^K versus m/3^K), not a wrong formula.
Both have zero integral, since the band omits the origin: int k = khat(0) = 0.
"""
import numpy as np

h = lambda u: np.cos(3*np.pi*u) * np.sin(np.pi*u) / (np.pi*u)
g = lambda u: (3.0/(np.pi*u)) * np.cos(np.pi*u) * np.sin(np.pi*u/3.0)

u = np.linspace(0.017, 40.0, 200001)
d = np.abs(g(u) - h(u/3.0))
print(f"max |g(u) - h(u/3)| over u in [0.017, 40], 200k points: {d.max():.3e}")
print(f"g(1) = {g(1.0):.12f}   h(1/3) = {h(1/3):.12f}")
print(f"h(1) = {h(1.0):.12f}   g(3)   = {g(3.0):.12f}")
print(f"limits at 0: g -> {g(1e-9):.12f}, h -> {h(1e-9):.12f}  (both 1)")

# zero integral: int_{-inf}^{inf} k = khat(0) = 0 because the band omits the origin.
# check by direct quadrature on a long symmetric window with a mild taper
for name, k, scale in (("h (band [1,2])", h, 1.0), ("g (band [1/3,2/3])", g, 3.0)):
    U = 4000.0 * scale
    uu = np.linspace(1e-7, U, 8_000_001)
    taper = 0.5 * (1 + np.cos(np.pi * uu / U))          # Hann, kills the truncation ringing
    I = 2.0 * np.trapezoid(k(uu) * taper, uu)           # symmetric, so twice the half line
    print(f"{name}: tapered int k du = {I:+.6f}   (exact value 0)")
