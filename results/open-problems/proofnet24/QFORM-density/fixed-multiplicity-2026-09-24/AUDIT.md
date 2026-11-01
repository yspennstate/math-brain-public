# Self-audit and independent-review brief

Candidate: QFORM-FIXED-MULTIPLICITY-17-20260924.

Source commit: 7c0d6e60946b19423e6400a12d34b473cf0591e2.
Source SHA-256: 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.
Git source blob: 183ccd294763214e6a707e8d4749ff9a8cf7006d (read back and matched to the local source).
Compiled 16-page PDF SHA-256: 6a0a4e11512ea93457a15abededae8a42a233f055e162143fd42b1ed68ce4c67.

## Verdict and limits

Completed authoring-agent self-audit: no fatal gap identified in the complete written 17-eigenvalue argument. Independent end-to-end review remains pending. This is NOT peer review, Lean verification, or a universal computation certificate. No optimality, exhaustive novelty, or full three-eigenvalue-conjecture claim is made.

The precise candidate is: independent arbitrary real coordinate densities <=K; arbitrary real symmetric A; s_17(A)>=s>0; arbitrary affine b,c; density of X^T A X+b^T X+c <=10000 K^2/s. The 33-eigenvalue statement is a corollary.

## Completed passes

1. Dependency closure: all specialized ingredients are proved in manuscript.tex. No citation to or dependency on the longer source manuscript remains. The classical sources are attribution only; geometric Brascamp-Lieb, projection densities, Gaussian Fourier identities, and all subsequent inequalities are proved at the constants used.
2. Algebra: checked singular Schur-complement approximation, nonsymmetric singular-value perturbation, ordered disjoint minors, the inequality (not equality) when a deleted seed is singular, support of R-P in rows T or columns S, rank(R)<=3r, rank(R[L,L])<=r, zero diagonal E, and D=0 on the seed.
3. Fourier analysis: re-derived decoupling powers two and four, the graph Jacobian, weights and trace identity, the regularizer alpha=(2*pi*e)^2, and determinant exponent -1/8. The order-five exponent 5/4>1 gives density; order-three exponent 3/4>1/2 is used with the weight |t|^(-1/2), not for direct density inversion.
4. Measure theory and kernels: checked square inverse branches, the hyperbolic Jacobian and both tails, logarithmic-kernel integration, Gaussian negative-half-moment normalization, and conditional Tonelli arguments. Bounds are measure domination statements for rough laws. No independence of rotated coordinates or conditional cap from an unconditional marginal is assumed.
5. Constants and finite diagnostics: all listed checks in verify.py passed. Exact rational diagonal-dominance slack is 297/2800. The largest final branch bound is 6010<10000.
6. Presentation: three-pass LaTeX compilation with resolved references and no overfull/underfull warnings; all 16 manuscript pages and 3 separate audit-report pages rendered and visually inspected. Source length: 790 lines. See proof_map.csv for labels/ranges.

## Finite-check coverage

- 504 exact rational interpolation seeds, all with nonsymmetric interpolants, including restricted/global rank, support, zero diagonal, and bordered-minor identities.
- 10 exact volume-sampling aggregate comparisons.
- 192 exact random-cut/order cases (64 cuts at orders 1,2,3).
- 800 numerical Schur spectral-count threshold cases.
- 1040 numerical nonsymmetric rank-perturbation inequalities.
- 160 numerical regularized graph-weight cases.
- High-precision constants: J near-region 7.196771497<8; quarter-power coefficient 3.995259362<16; hyperbolic branch 5.198603854<6; no-pivot half potential 176.959336188<200; no-pivot density 2174.625462768<2400.

These finite tests do not replace the symbolic proofs or establish correctness in every dimension.

## What changed relative to the earlier 33-eigenvalue note

A nonsymmetric auxiliary interpolation avoids symmetrization loss. Its full corrected rank is <=3r, while its seed-complement block has rank <=r. Forced large diagonal entries lie in that complement, so 4r+1 directions suffice. Orders three and five give thresholds nine and seventeen. The original hard two-eigenvalue no-pivot input is replaced by a self-contained nine-eigenvalue half-potential argument. Larger convenient Fourier constants remove the need for unproved sharp Hausdorff-Young or Gaussian-extremizer inputs. The pivot threshold becomes 1/100 instead of 10^-15.

## Independent review instructions

Pin the exact source commit/hash. Audit every definition, quantifier, equation, line, and proof, not just the assigned starting section. Report PASS/GAP/FALSE/UNCHECKED with source ranges and explicit reasoning. Publish fatal defects immediately. The most sensitive new points are lem:sampling, lem:completion, prop:volume, thm:determinant, and the chain ending at prop:nine. Recheck all rough-law limiting arguments and the distinction between full and truncated half potentials.

After establishing a sound baseline, lower the multiplicity as far as possible while preserving all hypotheses. Gaussian-only, diagonal-only, exact-rank, bounded-support, or leverage-restricted results are not lower-threshold versions of this theorem. Require a complete replacement proof and two genuinely separate end-to-end reviews before marking any candidate independently validated. Do not overwrite this pinned baseline; use immutable review/improvement folders.

## Remaining limitations

Independent complete reviews had not been received at preparation. The literature lookup verified classical attribution but was not a comprehensive priority review. GitHub delivery, compilation, scheduler configuration and numerical checks are not mathematical proof certificates.
