# Full re-audit — five-singular-value quadratic-form density theorem

Date: 2026-09-24

## Verdict

**PASS as a written mathematical proof, subject to the ordinary distinction between a proof audit and formal verification/peer review.**

The re-audited theorem is:

> If (X_1,ldots,X_n) are independent real random variables with densities bounded by (K), (A=A^T), and (s_5(A)ge s>0), then (Q=X^TAX+b^TX+c) has an essentially bounded density with
> [
> |p_Q|_infty<2400 K^2/s.
> ]

The audit did not identify a fatal gap. It does not claim the four- or three-singular-value bounded-density theorem.

## Fresh audit coverage

The final manuscript has 1,093 source lines and 21 explicit proof environments. The audit was repeated from the hypotheses through the scaling conclusion rather than merely comparing the final text with an earlier review.

### 1. Analytic foundations — PASS

Rechecked Fourier inversion/regularization, the negative-half-moment Fourier representation, product projection density bounds, integrated scalar Fourier powers, and all uses of Tonelli/dominated/monotone convergence. No hidden moment, support, smoothness, iid, or post-rotation-independence assumption was found.

### 2. Grouped product-Fourier receiver — PASS

Rechecked the conditional (L^2) step, mollification, Plancherel scaling, determinant-weighted Hölder step, entropy inequality for determinant weights, and the heavy-row promotion mechanism. Promoted coordinates are literal original coordinates; deterministic orthogonal projection is used only in row-space algebra. The resulting order-three density receiver and order-two full half-potential receiver preserve the original product-law hypotheses.

### 3. Schur-complement spectral bookkeeping — PASS

Rechecked the signed spectral-count statement for principal Schur complements, including indefinite matrices and singular limiting cases. Scalar pivots lose at most one large spectral direction and two-coordinate pivots lose at most two.

### 4. Five-direction structural extraction — PASS

Rechecked the disjoint-minor interpolation, restricted/global rank distinction, aligned rank-three approximation, residual Gram identity, and the maximal physical-pair argument. The key rank saving uses an actual physical row aligned with the rank-two complement block; no generic rank-one approximation is substituted. The proof obtains a quantitative physical two-anchor cross Gram lower bound and then forces anchored third-minor mass unless the ordinary third crossing volume is already sufficient.

### 5. Maximal-pair completion — PASS

Rechecked the leverage split, inverse-Gram/coefficient identities, the at-most-one exceptional high-leverage coordinate conclusion, the diagonal-correction estimate obtained from maximality of the physical pair, and the rank-four approximation in the exceptional-coordinate branch. The numerical inequalities retain positive slack at the constants used.

### 6. Pivot branches — PASS

Rechecked:
- scalar-square conditional density domination;
- the full negative-half-moment estimate needed after a scalar pivot;
- definite two-coordinate density;
- indefinite two-coordinate logarithmic envelope and averaging over the random critical value.

The branch bounds are all below the stated normalized constant 2400.

### 7. Three-direction half-potential appendix — PASS

Rechecked the one-anchor no-pivot extraction, maximal-row completion, second-minor receiver, and pivot alternatives. The appendix proves a full negative-half-moment theorem under three large singular values. This is a supporting theorem only and is not promoted to a three-value bounded-density theorem.

### 8. Scaling and quantifiers — PASS

For (Y=KX) and normalization by (s), coordinate densities become cap one and (s_5(A/s)ge1). Density scaling gives exactly the (K^2/s) factor. Arbitrary affine terms survive all reductions.

### 9. Lower-threshold boundary — PASS

Rechecked the two-weighted-star obstruction: four nonzero unit-modulus eigenvalues can coexist with no pivot and vanishing disjoint third-order crossing volume. This invalidates a naive extension of the current third-volume extraction to four singular values, but it is not a counterexample to the four-value density conjecture.

## Finite checks

The accompanying verification script/check output tests the new rank, leverage, Gram, and completion identities on finite exact examples. These checks passed in the reviewed package. They supplement but do not replace the analytic proof.

## Remaining limitations

1. This is not Lean kernel verification.
2. It is not journal peer review.
3. The bounded-density theorem is not proved here at multiplicity four or three.
4. The numerical constant 2400 is not claimed optimal.
5. The five-value theorem is the strongest complete bounded-density statement in this audited package; the three-value result concerns only the full negative-half moment.

## Re-audit conclusion

No fatal defect was found in the final five-singular-value proof after a second complete pass. The theorem may be treated as the current internally verified mathematical result for this project, while preserving the distinction between repeated proof audit and external/formal verification.
