---
name: c0090_scale_free_percolation_continuity_alpha_below_2d_exponents_open_2026_11_13
description: "[PROVISIONAL] C0090 scale-free percolation: continuity at lambda_c known for alpha in (d,2d) (Deprez-Hazra-Wuthrich 2015); exponents and upper critical dimension in (alpha,tau) open"
metadata:
  type: project
status: provisional
---

C0090 on the 200 list (Heydenreich-van der Hofstad survey): for scale-free percolation (long-range exponent alpha,
weight tail tau) decide when lambda -> theta(lambda) is continuous, find the critical exponents, and the upper critical
dimension as a function of (alpha, tau).

Literature read 13 Nov 2026 (arXiv abstracts plus search snippets; theorem statements not read in full):
- Deijfen-van der Hofstad-Hooghiemstra, "Scale-free percolation", arXiv 1103.0208: lambda_c = 0 when the degree tail
  exponent gamma = alpha(tau-1)/d < 2 (infinite variance); 0 < lambda_c < infinity for gamma > 2, alpha > d, d >= 2.
- Deprez-Hazra-Wuthrich, arXiv 1401.0409 (Risks 2015): continuity of theta at lambda_c on Z^d. From the snippets, for
  alpha in (d, 2d) and gamma > 2, by Berger's long-range argument.
- Deprez-Wuthrich, arXiv 1312.1948: the continuum version; no infinite cluster at criticality for alpha in (d,2d),
  tau > 2; they say alpha > 2d with tau > 2 is open except d = 1.
- Dickson-Heydenreich, arXiv 2210.07727 (rev. Mar 2025): infrared bound, hence the triangle condition and mean-field
  behaviour, for marked random connection models in high d under conditions on the edge function. Caicedo-Dickson,
  arXiv 2305.07398: mean-field gamma, beta and cluster-tail exponents for marked RCMs given a triangle condition.
  Whether their conditions cover the heavy-tailed scale-free weights was NOT checked.
- Dhara-van der Hofstad-van Leeuwaarden, arXiv 1909.05590: the non-spatial analogue (configuration model, tau in (2,3))
  has a new universality class. That hints the spatial exponents depend on (alpha, tau).

Status: PARTIAL. Continuity is known for alpha in (d,2d). For alpha > 2d it contains the short-range continuity
question in d = 3..6, so it is hopeless in general. Exponents and the (alpha, tau) upper critical dimension: no
general result found. A predicted d_c (heuristic min over the long-range and weight effects) is the natural paper
target, but needs the lace expansion with unbounded marks.

Would change this: a paper proving the triangle condition for scale-free percolation with gamma > 2 in high d.
