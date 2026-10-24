# Gaussian benchmark chapter: source map and verification

Author/reviewer of this chapter: `/root/claude_core/adapted_attack`.
Date: 23 September 2026.

## Source map

- Diffuse Lindeberg global Gaussian ceiling:
  `source_snapshot/fleet/account02/B17/account02-B17-20260923T1142Z-r11/REPORT.md`.
- One-heavy Gaussianized cone-tip optimizer and uniform gap:
  `source_snapshot/fleet/account01/B17/20260923T154011Z-account01-B17-QFORM-auto11b/REPORT.md`
  and
  `source_snapshot/fleet/account03/B17/20260923T163000Z-account03-B17-QFORM-auto11/REPORT.md`.
- Exact Householder cube tip:
  `source_snapshot/fleet/account04/B17/20260923T081528Z-account04-B17-QFORM-r4/REPORT.md`.
- The sharp Gaussian ceiling is reproduced directly, including arbitrary
  affine terms, from the classical Gaussian quadratic-form framework. Root
  supplied the useful explicit gamma convolution reduction, which is fully
  proved in the chapter. Existing literature references GNSU2019, BNU2020,
  and CK2026 provide context; no priority claim is made.

## Mathematical verification and strengthened exposition

1. Independently computed both compound-Poisson Laplace transforms. The
   central intensity measure is nonnegative with total mass `(log lambda)/2`.
   The noncentral intensity is `m^2/2`, with `lambda*chi_2^2` jumps.
2. Verified the covariance congruence singular-value bound and the treatment
   of affine terms in the kernel. The three extracted standard squares have
   maximum density `1/(2*sqrt(2))` for mixed signature; the same-sign gamma
   maximum is smaller. This proves the sharp Gaussian ceiling globally.
3. Included the variance floor `1/12` and a characteristic-function proof
   of the needed triangular-array central limit theorem. The upgrade to
   uniform output-density convergence uses `four:diffuse` and an explicit
   common integrable majorant; weak convergence is never used as a local
   density theorem.
4. Independently derived the one-heavy conditional elliptical kernel, proved
   continuity at zero for arbitrary heavy densities, and proved the unique
   centered-unit-interval optimizer directly. Recomputed the perfect-square
   identity, Gaussian angular normalization, weighted half-mass inequality,
   and monotonic Laplace ratio. Both source arguments give the same ceiling.
5. Added an exact rational certificate for `<4.111374`: truncate the
   alternating exponential integral at order 12 and use the rational upper
   bound `14142135623731/10^13` for sqrt(2). The resulting rational value is
   less than 4.111374 by
   `217418556395186901/266521615360000000000000`.
6. Proved the fixed-angle finite-product tip limit directly from L1 convergence
   of normalized-uniform-bank characteristic functions. This avoids reliance
   on an unproved Edgeworth remainder and does not claim a uniform rate as the
   angle parameter tends to zero.
7. Reconstructed the corrupted Householder TeX and independently evaluated
   the angular integral. The proof of continuity uses an explicit positive-
   plane polar density formula and dominated convergence; it does not rely
   on the source's terse statement about the contribution near the cone
   vertex.

## Scope and peripheral source corrections

The one-heavy and Householder assertions are cone-tip statements. No claim
is made about their global maxima. The Lindeberg statement is global under
its explicit finite-variance, mean/covariance convergence, and Lindeberg
hypotheses. Its affine extension requires convergence of the three spectral
linear coefficients and the scalar constant.

The account02 source's peripheral rare-fragment discussion is not reproduced.
Its displayed first-variation liminf alone does not imply convergence of
the tip, although the main uniform-density theorem and the identified
Gaussian limit do supply that conclusion. Its cap-one remote-interval
formula also requires the remote and main intervals to be disjoint (as holds
eventually for a fixed nonzero displacement). These issues do not affect the
main Lindeberg theorem proved here.

## Compilation

Standalone compilation with the actual master preamble succeeded. The
chapter occupies six text pages; the standalone file has seven pages when
its three-entry bibliography is included. BibTeX and repeated pdflatex
resolved every internal label and citation. Only the intentionally absent
cross-chapter references `sec:literature` and `four:diffuse` remain undefined
in that isolated compilation. There were no overfull or underfull boxes.

Root was asked to obtain an independent mathematical review of the finished
chapter before release. This record is the author's full verification, not
that separate review.
