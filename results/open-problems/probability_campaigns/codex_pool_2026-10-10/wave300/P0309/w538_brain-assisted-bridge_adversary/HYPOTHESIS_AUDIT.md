P0309 hypothesis and quantifier audit

The exact intake entry is quoted in p0309_exact_intake.json. The dated source asks for a crystalline low-positive-temperature Gibbs phase of a 3D Coulomb or Riesz gas, with regimes delegated to Lewin's review. It does not supply a fully quantified theorem statement. Definition 15 is a short-range (s>3 in dimension three) grand-canonical DLR specification; long-range s<3 needs a separately specified neutral/renormalized specification. Conjecture 35 is an energy assertion at zero temperature and Conjecture 38 concerns configurations; neither supplies a positive-temperature phase theorem. Current openness is UNKNOWN after a bounded inconclusive current-literature check.

Returned mathematical card (full body in math_brain_probe.json): "if there is a matrix Gamma > 0 such that Hessian V(z) >= Gamma uniformly, then Cov(nu) <= Gamma^{-1}." This is the substance of Theorem 3.13 in Liu, Mohanty, Rajaraman and Wu, https://arxiv.org/html/2405.06616v2 . Its complete source display was checked at the Theorem 3.13 heading; the Ising setting of the enclosing paper is not itself a hypothesis of this standalone continuous covariance statement. Carlen, Cordero-Erausquin and Lieb, https://arxiv.org/pdf/1106.0709 , Introduction and (1.3), specify a C^2 potential with everywhere positive Hessian and integrable exp(-V).

| Required premise | B1 surrogate | Actual P0309 gas |
| --- | --- | --- |
| Probability density exp(-V) on a specified Euclidean space | V=beta H_D+log Z on R^{3|D|} | A variable-number, unlabeled continuum law; a displacement chart is not automatic |
| C^2 potential and integrability | Assumed C^2; finite-D positive Hessian gives Gaussian domination | Pair collisions are singular; restricting to one crystal chart changes the law |
| Full uniform Hessian comparison | Assumed Hessian H_D >= kappa L_D tensor I_3 for every u, same kappa for all D | Unproved. O1 shows individual transverse pair curvatures are negative |
| Correct temperature scaling | Gamma=beta kappa L_D tensor I_3 | beta must multiply the full Hessian; it cannot be omitted |
| Positive definite boundary operator | Dirichlet L_D is invertible for finite D | A periodic operator has a translation zero mode; pin or quotient it first |
| Uniform diagonal inverse bound | 3D killed-walk Green bound C_3 | Does not follow from a scalar minimum eigenvalue bound |
| Coherent reciprocal Fourier phase | Reference x in Z^3, G in 2pi Z^3, E u_x=0 from evenness | Not guaranteed by a covariance theorem; O2 refutes dropping this premise |
| Defects, alternative configurations, DLR limit | Not supplied by B1 | The main unclosed bridge; do not identify a constrained chart with the full Gibbs measure |

Measured loss from discarding the matrix: for the 63^3 Dirichlet box, inverse minimum Laplacian eigenvalue=138.364970524398 whereas the exact spectral sum for the center diagonal is 0.25055763977551726, a factor 552.2281046722968. These are floating-point checks of a surrogate, not measured Riesz stability. The uniform analytic bound is C_3<=sqrt(3)pi/8. It is the matrix-shaped Hessian comparison that permits a volume-independent result.

Adversarial decision: reject a direct scalar-convexity transfer (O1), reject a covariance-only fixed-mode-order transfer without coherent phase (O2), retain B1 only as a conditional proof sketch pending independent w539 review. The hardest missing piece is uniform stiffness and defect control for the full continuum Gibbs law. A finite harmonic integral cannot replace it.

Peer coverage: At initial post-independence inspection w537's folder contained no files. No paired proof was available to audit; the existing author attempt in the brain explicitly disclaims proving a Gibbs phase. Do not report a completed adversarial audit of w537. Narrow review questions are in REVIEW_PACKET.md.

Final paired-audit update: C1-C5 are now covered in PAIRED_AUDIT.md. C5 is valid under its full-law hypothesis, which B1 does not supply. O3 strengthens the pair warning: whole-space finite Riesz convexity fails near an isolated collision. O4 keeps exact circular symmetry yet a conditional positive Bragg moment has exponentially small full-law weight and no pressure cusp. The remaining route must control a crystalline region and its unrestricted mass.
