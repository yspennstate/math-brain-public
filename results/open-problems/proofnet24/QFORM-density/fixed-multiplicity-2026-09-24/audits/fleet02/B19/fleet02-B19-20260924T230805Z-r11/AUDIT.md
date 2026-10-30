# fleet02/B19 independent fixed-multiplicity audit

Run: fleet02-B19-20260924T230805Z-r11
Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924
Control head refreshed during run: 6d9615ebdbcfc12e32bcf0eff26d779af17c8211
Math master refreshed during run: dd5810509d7becad8c5ad4ab3acc40ab998030e2

## Pinned historical baseline
Source commit: 7c0d6e60946b19423e6400a12d34b473cf0591e2
manuscript.tex blob: 183ccd294763214e6a707e8d4749ff9a8cf7006d
SHA-256: 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69
Bytes/lines: 47883 / 790

Verdict: PASS_AFTER_LOCAL_REPAIR.

* lines 47-434: PASS. The theorem quantifiers/scaling, Fourier and Gaussian identities, Riesz half-potential, nonsymmetric singular-value perturbation, singular Schur count, diagonal dominance, heat-flow geometric Brascamp--Lieb, product projections, scalar Fourier powers, decoupling, regularized determinant, volume envelopes, scalar profile and definite pair were independently reconstructed.
* lines 437-482 (hyperbolic pair): GAP_REPAIRABLE_LOCAL. The positive tail chooses a physical coordinate large for u, but the negative tail needs a possibly different coordinate large for w. Witness: u=(1/sqrt(2),0), w=(0,1/sqrt(2)). Repair: choose i_+ from u and i_- independently from w. Since |u|=|w|, both cutoffs and all constants are unchanged.
* lines 485-780: PASS after that repair. Quarter-power concentration, sampled nonsymmetric interpolation, rank R<=3r, restricted rank R[L,L]<=r, seed-zero D, zero-diagonal E, spectral-to-volume conversion, random cuts, full/truncated half-potentials, case assembly and K^2/s scaling reconstruct. The diagonal-dominance slack is 371/400-23/28=297/2800.
* lines 781-790: UNCHECKED priority/bibliographic attribution only; no proof dependency.
* verify.py/checks.json: PASS as source-bound finite reproducibility support. verify.py hashes manuscript.tex against the pinned SHA before testing. The finite suite reports 534 interpolation seeds, 18 volume cases, 240 Schur threshold cases and 30 graph-weight cases; it is not a universal proof.

Downstream: the historical s_17 theorem remains mathematically valid with the no-cost two-coordinate tail repair. The pinned manuscript itself is preserved unchanged.

## Guarded lower-threshold integration
Current complete paper:
proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/paper.tex
Repair commit: 5ba2a4d6b689721601cce7ec7e22ffea9fa98f90
Current blob: bbebd6f6c5a27e9f639186a305008ab43a481e70
Current MANIFEST SHA-256: 040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3
Current bytes: 65367.

Verdict on the mathematical source: PASS. Sections 2-5 and 7 were reconstructed independently in this run, and the repaired Lemma 5.3 was compared directly with the original blob f3e5fc173cdcee40174c19c955d813d47f32bd91. The master source now chooses separate positive- and negative-tail coordinates. No new gap was found in the grouped Fourier compiler, weighted Holder/entropy argument, projection Jacobian, rough-law limiting steps, pivot estimates, or final case split. Section 6 was also checked algebraically; its attached Lean execution was not rerun in this invocation and is therefore UNCHECKED as an independent execution.

Supported replacement:
s_5(A)>=s>0 => ||p_(X^TAX+b^TX+c)||_infty <= 270 K^2/s.
Auxiliary:
s_3(A)>=s>0 => sup_a E|Q-a|^{-1/2} <= 77 K/sqrt(s).
No bounded-density theorem at multiplicity three is claimed.

Next obligation: multiplicity four. The separate improvement artifact gives a counterexample to an unqualified disjoint-two-star structural dichotomy and a source-compatible exact receiver for the counterexample family.
