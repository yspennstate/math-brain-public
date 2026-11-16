# The length of the network spanning k random points in the Poisson line SIRSN

Place k independent uniform points in a square of area k and join every pair by its route in a scale-invariant random spatial network (SIRSN). Aldous (Electron. J. Probab. 19 (2014); Open Problem 35 in Section 8.4.3 of arXiv:1204.0817v1) asked for a proof that the expected length of the union of these routes is asymptotic to ℓk, where ℓ is the mean length per unit area of the network on a unit-rate Poisson process.

The paper proves this for the network of geodesics of the planar improper Poisson line process, in which the speeds of the lines have a power-law intensity with exponent γ > 2. Kendall constructed this network and Kahn proved that it is a SIRSN. The lower bound holds for every SIRSN. The upper bound rests on a tail bound: the probability that some geodesic between two points of the unit square leaves the disc of radius R about its centre is O(R^(-a)) for every 0 < a < γ − 1. Since γ − 1 > 1, the expected length of the union far from the square is O(√k).

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `SHA256SUMS`: checksums of the files above.
