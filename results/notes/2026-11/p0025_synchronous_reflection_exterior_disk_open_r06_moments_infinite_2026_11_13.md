---
name: p0025_synchronous_reflection_exterior_disk_open_r06_moments_infinite_2026_11_13
description: "P0025 (Burdzy, My favorite open problems, Problem 5(ii): synchronous reflected Brownian motions in the complement of a closed disc - is limsup |X_t - Y_t| > 0 with positive probability?) is open on 13 Nov 2026: Burdzy's page still lists it, and arXiv has nothing new on synchronous coupling in an exterior domain. Known: Cranston-Le Jan 1989 (no coalescence in finite time); Burdzy-Chen-Jones 2006 (bounded smooth domains). Our R06 run (18 Sep, six reports, retired PARTIAL) found why the bounded-domain proof does not transfer: its dyadic excursion sums stop at diam(D), and in the exterior disc the matching Euclidean excursion moments are infinite (its Prop 2.1)"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T17:19:22.741Z
---

P0025, rank 47 on the 200 list. Source: Krzysztof Burdzy, "My favorite open problems", Problem 5 "Convergence of
synchronous couplings", part (ii), https://sites.math.washington.edu/~burdzy/open_mathjax.php . X and Y are reflected
Brownian motions in a smooth planar domain D, driven by the same planar Brownian motion B and reflected along the inward
normal. For D the complement of a non-degenerate closed disc: is limsup_{t->infinity} |X_t - Y_t| > 0 with positive
probability?

Status 13 Nov 2026: open.
- Burdzy's page, fetched 13 Nov, still lists 5(ii) as open. It notes that a bounded domain answering part (i) must have
  at least two holes (Burdzy-Chen-Jones, "Synchronous couplings of reflected Brownian motions in smooth domains",
  Illinois J. Math. 2006, math/0501486), and points to Burdzy-Chen 2002 for background.
- Known for the exterior disc: Cranston and Le Jan (1989) show the two processes do not meet in finite time. The
  long-time limsup is the open part.
- Our earlier work:
  - The 6 Sep first pass P0025-A001 (codex_20h): a reflection can move the separation either way. At x = (R,0) on the
    circle, with inward normal (1,0), <x - y, n> is negative for y = (r,0) and positive for y = (-r,0). So no monotone
    distance argument is available.
  - Run R06 in open-problems-repo (18 Sep, six reports, runs/R06/20260918T0222Z..0721Z_p0025_*; claim
    operations/claims/P0025.md) tried the reduced reflected diffusion, winding and local-time invariants, a Mellin/Lamperti
    reduction, and stuck-regeneration and corner-layer estimates. Its metric stayed 0 and it was retired PARTIAL. The
    lasting finding is report 36's Proposition 2.1: the Burdzy-Chen-Jones lemmas sum dyadic excursion displacements up
    to diam(D), and in the exterior disc the corresponding positive Euclidean excursion moments are infinite, not just
    unproved. So the bounded-domain proof cannot be carried over by removing the cutoff. Unrefereed.
- My arXiv check on 13 Nov: synchronous coupling(s) with reflect*, reflected Brownian motion with coupling and
  exterior, and Burdzy as author with coupling. Nothing addresses the exterior disc. The hits are Wasserstein-contraction
  papers that use "synchronous coupling" for diffusions with drift, plus two older works nearby:
  - Burdzy, "Simultaneous boundary hitting by coupled reflected Brownian motions", arXiv 1812.08355: local-time
    measures of two synchronous RBMs are mutually singular until the normals at the reflection points agree.
  - Banerjee and Brown, arXiv 2009.12937: synchronous coupling of RBMs in the orthant, a different setting.
- There is no Codex report for P0025 in referee_reports/2026-11-13. The D0025A, D0025AR and D0025PR folders there are a
  different problem (the TASEP item).
- Where an attempt could start: the problem has a scale structure. Brownian motion in the plane is neighbourhood-
  recurrent, so the pair keeps returning to the disc, and each visit changes the separation by a random factor. A
  candidate is a multiplicative random walk for log |X - Y| sampled at the returns, with the heavy excursion tails that
  R06 found. Whether its drift is zero or negative is the whole question.

Related: [[p0188_joint_strong_convergence_permutations_deterministic_open_alev_rao_weak_2026_11_13]] (previous item in
this loop).
