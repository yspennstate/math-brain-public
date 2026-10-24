# B10 findings — account02-B10-20260924T234822Z-r11

Source pin: paper content commit 5ba2a4d6b689721601cce7ec7e22ffea9fa98f90; blob bbebd6f6c5a27e9f639186a305008ab43a481e70; SHA-256 040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3; 715 lines.

Independent Sections 2–5 and 7 review:
- 103–199 PASS: Fourier/Gaussian/half-moment normalization; conditioning; approximation-number/Weyl/compression; singular Schur count; Gram identities.
- 200–267 PASS: heat-flow geometric BL including limiting steps; product projection; Fourier powers. Original-coordinate product provenance is preserved.
- 268–294 PASS: crossing-volume and entropy identities.
- 296–395 PASS: grouped hub compiler, complex-measure L2 domination, mollification, Holder exponents, determinant projection and entropy closure.
- 397–416 PASS: stopping rule and C3/C2 corollaries.
- 418–438 PASS: scalar square and definite pair.
- 440–467 PASS in current blob: separate coordinates i and i' are now chosen for the two hyperbolic tails, repairing the old draft gap with no constant change.
- 469–535 PASS: concentration/log moment, kernel identities, pair half-potential.
- 607–621 PASS: no-pivot bounds <167 and <26.
- 623–641 PASS: s3 half-potential <=77.
- 643–664 PASS: main branches <167, 266.735825, 50.265483, 266.951347; K^2/s scaling correct.
- 666–671 PASS: K/sqrt(s) half-moment scaling.
- FALSE: none.
- GAP in current paper: none.
- UNCHECKED: fresh local Lean recompilation and exhaustive bibliographic priority only. Supplied Section-6 Lean log was inspected and ends rc=0; Section 6 spectral facts were not re-proposed.

The current theorem is therefore PASS in this B10 reconstruction: s5 density <=270 K^2/s and s3 half-moment <=77 K/sqrt(s).

New four-eigenvalue stress result is in FOUR_EIG_STRESS.md.
