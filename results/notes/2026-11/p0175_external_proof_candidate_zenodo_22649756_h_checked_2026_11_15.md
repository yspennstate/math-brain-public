---
name: p0175_external_proof_candidate_zenodo_22649756_h_checked_2026_11_15
description: "P0175 free convolution of symmetric unimodal laws: an external unrefereed proof candidate exists (Zenodo 22649756, 7 Sep 2026); its key inequality (H) holds on 300 laws at 50 digits and its subordination step checks; Sections 4-5 unaudited"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T21:52:24+02:00
  status: provisional
  evidence: ""
---

P0175 (Hasebe-Ueda Conjecture 3.5: mu, nu symmetric unimodal => mu boxplus nu unimodal) has an external, unrefereed
proof candidate, found 15 Nov by a web search: "Symmetric unimodality under free additive convolution", Anonymous,
7 Sep 2026, Zenodo 22649756, github.com/ipitchford/symmetric-unimodality-free-convolution (AI-assisted, Codex
workflow; maintainer Ian Pitchford). Not ours. Before spending more effort on P0175, read it.

Its route: prove (H) Im(1/G'(z)) + 2y Re(1/G(z)) <= 0 on the quadrant x, y > 0 for every symmetric unimodal law
(single uniforms; atom plus uniform; a moment-extremum reduction to two radii; R -> infinity), then subordination.

Checked here, 15 Nov:
- Section 6 (subordination) by hand: g'(1/a1 + 1/a2 + 1/g^2) = 1 and (H) at w1, w2 give Im D <= -2y Re F < 0, so
  Im g' > 0 = unimodality of every Cauchy smoothing. Correct.
- (H) numerically on 300 random atom-plus-uniform laws, widths over six decades: every law's worst grid point is
  negative at 50 digits (largest -1.39e-14); Bernoulli negative control gives +1.0 (h_check.py, h_mp.py).
  Scar: writing G with log((z+a)/(z-a)) gave 257 false violations near the imaginary axis at |z| ~ 1e5 a; use
  arctanh(a/z)/a.

Audited 15 Nov later the same day: Section 4 (attainment, dual condition), Lemma 2 (cubic in a^2, Rolle count) and the R -> infinity limit read line by line, no gap; Lemma 1 coefficients extracted from M directly (audit_lemma1.py): c1, c2 > 0, matching the paper to 5e-10.
Next useful step: none on P0175 beyond an outside referee; no more proof or counterexample search here.

Status: no refereed proof; candidate holds under our audit of Sections 2-6 and all numerics. What would change this: a gap in Sections
4-5, or a law violating (H) at 50 digits. Files: 12_cognitive_architecture/math/trio_1011/op/P0175/NOTE.md
(section "15 Nov: an external proof candidate").

