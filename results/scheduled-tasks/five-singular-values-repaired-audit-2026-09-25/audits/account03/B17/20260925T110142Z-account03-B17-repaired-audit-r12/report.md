# account03/B17 repaired-source audit — 20260925T110142Z-account03-B17-repaired-audit-r12

Objective: `QFORM-FIVE-270-REPAIRED-AUDIT-20260925`.

Exact source: `yspennstate/math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa`,
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/repaired-2026-09-25/paper.tex`,
blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`,
SHA-256 `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`.

Fresh controls were read from current brain main and refreshed immediately before publication. OWNER CONTROL revision remained `2026-09-25.2`. Execution remains `WITHOUT_VERIFIED_BRAIN`: GitHub transport is verified, but no native learned-memory receiver use occurred.

## Coverage

This invocation independently audited repaired `paper.tex` physical lines **1–387**. The preceding B17 repaired-source run covered lines **388–683**, so cumulative B17 physical-source traversal is now **1–683** on the repaired hash.

No new `GAP` or `FALSE` mathematical clause was found in lines 1–387.

### Repaired clauses independently rechecked

- **Line 41 — PASS.** The abstract now qualifies five-to-three random-sign extraction by the no-pivot hypothesis and (m\in\{1,2,3\}).
- **Line 62 — PASS.** The unsupported literature-wide “open” assertion is replaced by the manuscript-local statement that this argument does not settle three or four directions; essential bounds and limited continuity are stated correctly.
- **Line 65 — PASS.** Pivot laws are described by square-root/logarithmic **upper envelopes**, not mandatory singularities.
- **Line 81 — PASS.** The logarithmic and negative-half kernels are total extended-valued Borel functions; capped Borel density versions are legitimate.
- **Lines 106–127 — PASS.** The half-moment representation is correct and the specialization now explicitly assumes (u>0).
- **Lines 143–149 — PASS.** The singular-value variational proof now handles (s_j(T)=0), including padded indices, before invoking right singular vectors.
- **Lines 208–229 — PASS.** Any number of zero-(\beta_i) factors may be dropped because they are fiber-independent and bounded by one; (p(y)=0) is separated before logarithms and finiteness is established in the positive case.
- **Lines 311–322 — PASS.** Finite-partition total-variation domination yields (|\nu_x|\le p_Y). A fixed approximate-identity sequence establishes measurability of (x\mapsto\|\nu_x\|_2^2) before its expectation and before the terminal (\ell'=0) branch.
- **Lines 323–330 — PASS.** The missing Jensen step is now explicit: (|\mathbb EF_t|^2\le\mathbb E|F_t|^2).
- **Lines 331–378 — PASS.** Terminal branch, mollifier dominated convergence, weighted Hölder, one-set projection, determinant weights, and entropy recombination are correct.
- **Lines 380–386 — PASS.** The greedy heavy-row proof closes the decay theorem with the stated constant, including the (m=1) endpoint.

The unchanged dependency chain also passes: Fourier normalization, conditioning domination, Schur spectral count with mixed signs, Gram/Cauchy–Binet identities, heat-flow Brascamp–Lieb with both limiting operations, product-projection density, and integrated Fourier powers. All probabilistic independence is retained in original coordinates; orthogonal maps are deterministic changes of variables only.

## Remaining UNCHECKED evidence

This is **not** yet an every-clause PASS. The remaining unresolved evidence classes are:

1. the external related-work attributions on source line 74;
2. bibliography metadata on source lines 659–679;
3. visual comparison against the repaired 15-page reference PDF.

The package records that PDF as 15 pages with SHA-256 `2a493f2dd3dc4eb126d965cc1d246c554f9a5c61bc9a4a9bd8ca0ab9e439cd09`, but the PDF binary is not present in the repository and was not available as a mountable file in this run. Visual page verification is therefore recorded `UNCHECKED`, not inferred.

No schedule state, notification setting, email, Drive delivery, public release, remote workflow, installation, or other worker artifact was changed.
