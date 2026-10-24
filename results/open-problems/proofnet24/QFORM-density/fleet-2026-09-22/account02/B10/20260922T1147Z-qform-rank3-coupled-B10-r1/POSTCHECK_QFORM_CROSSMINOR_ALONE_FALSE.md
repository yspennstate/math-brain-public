# Post-publication correction check — `QFORM-CROSSMINOR-ALONE-FALSE`

A source-backed correction entered the shared inbox after the immutable B10 report and initial receipt were created:

- event: `QFORM-CROSSMINOR-ALONE-FALSE`;
- source worker: account02/B09, run `20260922T115241Z-account02-B09-QFORM-r1`;
- canonical report commit: `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`.

The refuted intermediate claim is: a nonsingular `2x2` cross block alone forces bounded density without any pivot-side principal-block condition. The counterexample is `(X1+Y1)^2-(X2+Y2)^2`, which has a nonsingular cross block but only two nonzero eigenvalues and a logarithmic singularity.

This correction does **not** invalidate `QFORM-HYPERBOLIC-SQUARE-v1` or its triangular physical-triple corollary. The B10 theorem assumes an additional nonzero square coefficient `b` and proves the bound by an exact two-stage inverse-square-root integration; it is not a cross-minor-alone argument. In the canonical model `2XY+Z^2`, the third square is exactly what regularizes the rank-two hyperbolic logarithmic singularity.

The B09 safe replacement is complementary: for disjoint equal-size blocks `I,J`, `m>=2`, with `A[I,I]=0` and invertible `A[I,J]`, it gives `||p_Q||_infinity <= m/(m-1)|det A[I,J]|^{-1/m}`. Thus the updated localized closure menu contains both the B09 multipivot bilinear branch and the B10 one-pivot-plus-square branch. The residual heavy/light rank-three problem remains unchanged in substance: close frames for which neither localized certificate is dimension-free and the diffuse leverage theorem does not directly apply.

Status after applying correction: B10 classification remains `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; full conjecture OPEN.
