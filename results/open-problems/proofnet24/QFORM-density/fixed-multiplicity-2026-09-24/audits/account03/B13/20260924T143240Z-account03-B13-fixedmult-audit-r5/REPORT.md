# account03/B13 r5 — full fixed-multiplicity audit refresh

Run: `20260924T143240Z-account03-B13-fixedmult-audit-r5`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS** for the written seventeen-direction theorem in this fresh B13 end-to-end read. No fatal mathematical defect was found. The current repository contains a stronger source-backed nine-direction theorem, so the seventeen-direction manuscript is no longer the best threshold, but its proof remains mathematically consistent.

The unrestricted three-eigenvalue conjecture is not solved by this audit. Multiplicity eight remains open.

## End-to-end ledger

- **Lines 1–120, statement/scaling/Fourier setup — PASS.** Quantifiers match arbitrary independent coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary signs and remaining spectrum. The normalization and final scaling have the correct `K^2/s` factor. Gaussian regularization and inversion constants are consistent.
- **Lines 121–240, Riesz/spectral/BL setup — PASS.** The negative-half-moment Fourier weight is used only with sufficient decay. Singular-value perturbation is valid for nonsymmetric auxiliaries. The Schur count is a principal-compression argument and its singular-matrix limiting step is legitimate.
- **Lines 241–310, geometric BL/product projections/scalar Fourier powers — PASS with harmless wording clarification.** After dropping rows with `b_i=0`, the proof only needs `sum_{b_i>0}(1-b_i)<=d`; equivalently one can keep the displayed equality `sum_i(1-b_i)=d` before omitting those rows. No constant changes. Orthogonal changes occur only in deterministic integrals; no rotated-coordinate independence is asserted.
- **Lines 311–429, two-copy decoupling and regularized crossing determinant — PASS.** The two copies are independent original-coordinate copies. The difference coordinates retain independent cap-one densities. The BL weights close exactly, and the fourth root yields determinant exponent `-1/8`. Cauchy–Binet and the crossing-volume expansion are correctly normalized.
- **Lines 430–540, square/definite/hyperbolic pair and quarter-power concentration — PASS.** The definite-pair bound uses only a two-dimensional joint density cap. The indefinite pair keeps the original two independent coordinates and controls both hyperbolic tails without rotating the random law. The Jacobian is `1/(2 sqrt(|det B|))`. Exceptional critical levels are handled through nonnegative test functions/Tonelli. The quarter-power lemma uses the integrated crossing determinant, not the refuted law-uniform pointwise quadratic-phase claim.
- **Lines 541–660, sampled interpolation and spectral-to-volume conversion — PASS.** The bordered determinant is exact. Singular seeds only turn the count into an inequality. `P` may be nonsymmetric; this is allowed. The decomposition has `rank R<=3r` globally, `rank R[L,L]<=r`, `D=0` on the seed, and `E` zero on the diagonal. The diagonal-dominance contradiction uses the restricted rank, not the global rank. The numerical margin `371/400>23/28` is positive.
- **Lines 661–790, pivot potentials/final proof/limitations — PASS.** Truncated and full half-potentials are kept distinct. Scalar, definite-pair and hyperbolic-pair branches retain the correct Schur spectral counts. The final normalized constants are below `10^4`; scaling back is correct. The manuscript accurately limits its own continuity claim to the Fourier-integrable no-pivot branch.

## B13-specific pair audit

For an indefinite principal pair `B`, the hyperbolic parametrization is correct and the density envelope

`p(z) <= |det B|^{-1/2} [6+log_+(16 sqrt(|det B|)/|z-v|)]`

is valid for arbitrary fragmented/unbounded cap-one independent input coordinates. The proof's tail argument uses one original coordinate at a time and never treats the orthogonal eigenbasis coordinates as independent. The determinant singularity is genuine; current multiplicity-eight work therefore cannot simply invoke this lemma when the terminal pair determinant tends to zero.

The recent account03/B15 strong-cross reduction is compatible with this diagnosis: it replaces the aggregate collar by a physical pair with a strong outside cross map but a potentially arbitrarily small nonzero self determinant. The improvement artifact from this run gives an explicit counterexample showing that local strong-cross/weak-self information alone does not remove the hyperbolic singularity; the six Schur directions forced by `s_8(A)>=1` are a genuinely necessary extra resource.

## Review status

This is a worker audit, not a formal verification certificate. It agrees with the existing independent PASS reports for the pinned baseline. The stronger nine-direction theorem has separate source-backed reviews and a same-height `C_0` closure; this report does not self-award global release status.
