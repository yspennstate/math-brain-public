# P0309: source audit and conditional proof route

## Scope recovered

The September ranking names P0309 but its only matching raw rank-sheet row is truncated. There is no exact quantified 3D finite-temperature theorem in the recovered intake record. Lewin's 2022 review, *Coulomb and Riesz gases: The known and the unknown* (arXiv:2202.09240, Sections I, IV.B and VI), defines the Riesz parameter s and describes crystallization/phase transition, but Conjectures 35 and 38 concern zero temperature. Blanc–Lewin's 2015 review (Section 3.1, equations (47)-(50)) gives a finite-temperature correlation-function formulation. Neither has been verified as the specific P0309 source. Current open status is UNKNOWN. No parent proof or novelty claim follows.

## Hardest missing input for a defensible route

Fix d=3, a specific s>3 first, density rho>0 and a continuum canonical or DLR Gibbs specification for V_s(x)=|x|^{-s}. For 1<=s<3, the neutralized long-range Hamiltonian and its thermodynamic-limit prescription must also be fixed. Select two distinct lattice phases a,b and a bounded continuous *local* phase observable f with values in [0,1]. The hard input is a uniform-in-volume, phase-fitted low-temperature estimate that bounds the partition-function weight of every contour where the local configuration leaves phase a (and analogously b), including phonons, dislocations, grain boundaries, alternative lattices, and the continuum entropy. It must be measured after optimizing over the permitted global translation/rotation or with an explicit pinned boundary. Its constants must hold for the unrestrained Gibbs measure, not only configurations near an assumed crystal. This input includes a robust ground-state stability statement and is not proved here.

The common shortcut E(Y)-E(X)>=c times the number of sites displaced from one fixed absolute lattice X fails: w529 C1 gives the exact torus translation counterexample, independently reproduced in REVIEW.md. A harmonic phonon calculation restricted to an assumed crystal also does not give the required partition-function bound; the rank-sheet itself names defects and alternative configurations as missing.

## Proved conditional reduction (elementary, not P0309)

Suppose, for each volume L and phases a,b, finite-volume Gibbs measures mu_L^a and mu_L^b have locally convergent subsequences whose limits satisfy the chosen DLR equation. Suppose a bounded continuous local f:[configuration]->[0,1] obeys E_{mu_L^a} f >= 1-q and E_{mu_L^b} f <= q uniformly in L, with q<1/2. Then the two infinite-volume DLR limits are distinct: local weak convergence preserves the two expectations and their gap is at least 1-2q>0. This is a rigorous reduction, conditional on both the DLR limit and the uniform order bound.

One sufficient (still unproved) way to obtain the order bound is: every failure of the selected local phase has a contour of size m>=m0; at most A^m such contours occur at the origin; and, for each contour, its probability under the pinned Gibbs measure is at most exp[-(kappa/T-sigma)m] with A,kappa>0 independent of volume. The union bound then gives q <= r^{m0}/(1-r), r=A exp(sigma-kappa/T), provided r<1. Distinctness follows if this value is <1/2 and the local observable separates a from b. The counting, contour-cost estimate, existence of DLR limits, and an actual separating f are the unproved load-bearing work for a continuum Riesz gas.

## What was attempted and rejected

An absolute-reference site-defect energy penalty was independently falsified by a common half-lattice translation on a torus. The repaired route must fit phase or pin it and pay for *all* competing configurations. There is no evidence here that the corrected contour-cost estimate holds. In particular, this conditional reduction does not bypass the open 3D zero-temperature crystallization problem described in Lewin's Conjectures 35 and 38.

NEXT: obtain an exact source formulation for a fixed exponent/ensemble and ask independent referee w533 to audit any new contour or DLR lemma before upgrading its status.
