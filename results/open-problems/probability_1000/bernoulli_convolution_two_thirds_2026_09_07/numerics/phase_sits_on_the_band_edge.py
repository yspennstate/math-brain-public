"""The octave position puts the phase frequency exactly on the edge of the band.

At the octave, k0 nu / P -> nu / (3 * 2^K) exactly (ratio 1.00024 by K = 14, and replacing the true
phase by this idealised one reproduces Err/L to five digits).  In the rescaled variable u = nu / 2^K the
phase is therefore e(u/3): a pure frequency 1/3.

The kernel g is the normalised transform of the octave band, which in this variable is [1/3, 2/3]:
    g(u) = (3/(pi u)) cos(pi u) sin(pi u / 3),   ghat(t) = 3 * 1_{[1/3, 2/3]}(|t|).
So the leading term of Err/L is (smooth weight) x ghat(1/3) - the band indicator evaluated AT ITS OWN
LEFT ENDPOINT.  A knife edge: the octave position places the phase frequency exactly on the boundary,
where the indicator is neither 0 nor 1 but half.  That is the structural reason the answer is a bounded
O(1) number rather than either vanishing or growing geometrically, and it is specific to k0 = R.

Test: evaluate ghat at 1/3 (the octave), and at frequencies inside and outside the band, by tapered
quadrature; compare with the indicator's values 3 (inside), 0 (outside) and 3/2 (edge).
"""
import numpy as np

g = lambda u: np.where(np.abs(u) < 1e-12, 1.0,
                       (3.0 / (np.pi * np.where(np.abs(u) < 1e-12, 1.0, u)))
                       * np.cos(np.pi * u) * np.sin(np.pi * u / 3.0))

U = 6000.0
uu = np.linspace(-U, U, 12_000_001)
taper = 0.5 * (1 + np.cos(np.pi * uu / U))          # Hann, kills truncation ringing
gv = g(uu) * taper

def ghat(t):
    return float(np.trapezoid(gv * np.cos(2 * np.pi * t * uu), uu))

print("ghat(t) = int g(u) e(-t u) du ; the band indicator is 3 inside [1/3,2/3], 0 outside, 3/2 at an edge")
print(f"{'t':>10} {'ghat(t)':>12}   position")
for t, lab in ((0.20, "outside, below the band"),
               (0.30, "outside, just below"),
               (1/3,  "THE OCTAVE PHASE - left edge"),
               (0.40, "inside the band"),
               (0.50, "inside, mid-band"),
               (2/3,  "right edge"),
               (0.80, "outside, above")):
    print(f"{t:>10.5f} {ghat(t):>12.5f}   {lab}")
print()
print("If the octave value sits at half the interior value, the knife-edge reading is right.")
