---
name: p0167_slab_beats_ball_every_rho_paper_posted_referee_fixes_2026_11_14
description: "[VERIFIED] P0167 symmetric Gaussian noise stability: is the ball optimal? No, the slab wins near measure 1 for every rho; posted 48342665 after referee repairs"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T21:58:53+02:00
  status: provisional
  evidence: ""
---

P0167 (O'Donnell/Heilman: which symmetric set of given Gaussian measure maximizes noise stability) is posted as
github.com/yspennstate/symmetric-gaussian-noise-stability-slabs, v1.0 = main = 48342665cd44f443896b6de4675c0bb889111eb0
(14 Nov 2026). Ledger row open-problems-repo 88ac3f0b; math-brain-public table 0140707.

Result: for n >= 2 and every 0 < rho < 1, at measure close to 1 the slab {|x_1| <= t} beats every C_k (k >= 2) and every
cylinder complement; at measure close to 0 the slab complement wins. So the ball conjecture fails at every correlation,
not only near rho = 0 (Heilman's second-order counterexample).

What the independent Codex referee (gpt-6.1-sol, high) found, all fixed before posting:
- The step "t <= r <= 2t" was not justified. The proof needs only r >= t: the exponent of r,
  k-3-2(k-2)/(1+rho) = -2rho/(1+rho) - (k-1)(1-rho)/(1+rho), is negative.
- (X,Y) must be stated jointly Gaussian; marginal Gaussianity plus cross-covariance is not enough.
- The planar search is a [0,1]-valued relaxation, and the 300-iteration cap was hit in 28 of 55 cases. So the outputs are
  "best returned sets", not local maxima, and optimality is only among the candidates compared.
- The literature had more than we cited: Barchiesi-Julin (PTRF 2020: the slab is the symmetric Gaussian-perimeter
  minimizer near measure 1), Milman (arXiv 2611.12456: the planar symmetric minimizers) and Baker (Queen's MSc 2018,
  Sec. 3.4: the same four planar cylinders at rho = 0.9). Baker means the planar table is an extension, not a first.

Scar: a numerical "search over sets" in a paper must say what it is (a relaxation, an iteration cap, how often the cap was
hit) before it is used as evidence. Calling a capped Frank-Wolfe output a "local maximum" overstates it.

What would change this: a referee finding a gap in Lemma 3.2's three-part ball bound, or a prior paper that already states
the slab-beats-ball result at every rho.


Related: [[p0167_symmetric_gaussian_strip_beats_ball_all_rho_2026_11_14]] (the proof itself), [[p0413_hyperbolic_voronoi_variance_paper_posted_referee_fixes_2026_11_14]] (same posting flow), [[p0452_p0243_independent_referee_passes_what_they_found_2026_11_12]].
