# account01/B01 — principal rank-two Schur patch closure with compound-minor aggregation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T171330Z-b01-qform-auto11`  
Outcome: **ESSENTIAL_STEP_APPLIED / full target OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport was used, not native learned-memory ingestion.

## 1. Exact target and first unpaid implication attacked

The full target remains: for independent real inputs with densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `Q=X^T A X`, or give a valid counterexample. No rotated-coordinate independence is assumed.


B01's first missing implication was the higher-rank Schur obstruction left by the completed orientation-free rank-two half-Riesz theorem: can an exact rank-two residual be used inside an arbitrary ambient quadratic form without conditioning away the product structure? The result below answers this for an arbitrary **original-coordinate principal rank-two Schur patch**, with completely arbitrary outside quadratic terms and cross couplings.

## 2. Source theorem actually used

The source-complete supporting theorem is `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, canonical report

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

It proves: if `U^T U=I_2`, `Lambda` is invertible symmetric `2x2`, `b` is arbitrary in physical coordinates, and the inputs are independent with densities at most one, then

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2) <= 128 |det Lambda|^(-1/4)`.

If the affine term lies in `range(U)`, including zero affine term, the constant improves to `16 sqrt(30)`.

This supporting theorem is not itself the full QFORM theorem; its report records independent review as pending. The present result is a direct conditional consequence of that precise source theorem.

## 3. New theorem: arbitrary ambient form from a rank-two Schur patch

### Theorem — `QFORM-PRINCIPAL-RANK2-SCHUR-PATCH-v1`

Let `A` be any real symmetric `n x n` matrix. Fix a physical coordinate `i` with

`a=A_ii != 0`.

Write `K=[n]\{i}`, `r=A[K,i]`, and let

`S=A[K,K]-a^(-1) r r^T`

be the physical Schur complement of the scalar pivot. Let `J subset K` be any set of original coordinates. Assume only that the principal patch

`H=S[J,J]`

has rank exactly two, with nonzero eigenvalues `mu_1,mu_2`. Then for every product input law with independent marginal densities bounded by one, `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 128 |a|^(-1/2) |mu_1 mu_2|^(-1/4).`    (3.1)

There are **no assumptions** on `S[J,K\J]` or `S[K\J,K\J]`; in particular all outside quadratic coefficients and all cross couplings are arbitrary.

If, in addition,

`range(S[J,K\J]) subset range(H)`,

then the affine term created after conditioning the outside variables lies in `range(H)`, and the improved source constant gives

`||p_Q||_infinity <= 16 sqrt(30) |a|^(-1/2) |mu_1 mu_2|^(-1/4).`    (3.2)

### Proof

Split `X_K=(Z,W)` with `Z=X_J` and `W=X_{K\J}`. Completing the square in the original physical coordinate `X_i` gives the exact identity

`Q = a ( X_i + a^(-1) r^T X_K )^2 + X_K^T S X_K.`

For fixed `(Z,W)`, translation of `X_i` does not affect its density cap. The conditional law of

`a (X_i+m)^2 + R`

therefore has density bounded pointwise by

`|a|^(-1/2) |t-R|^(-1/2)`

(the sign of `a` only reflects the support). Consequently, after conditioning only on `W`,

`p_{Q|W}(t)`
` <= |a|^(-1/2) E_Z | t - [ Z^T H Z + 2 Z^T S[J,K\J] W + c(W) ] |^(-1/2).`    (3.3)

Because `H` has rank exactly two, write `H=U Lambda U^T` with `U^T U=I_2` and `det Lambda=mu_1 mu_2`. For fixed `W`, the term

`2 S[J,K\J] W`

is an arbitrary original-coordinate affine vector in the independent product variables `Z`. The source rank-two affine half-Riesz theorem therefore applies **uniformly in W** to (3.3), giving

`p_{Q|W}(t) <= 128 |a|^(-1/2) |mu_1 mu_2|^(-1/4)`.

Average over `W`. This proves existence of an essentially bounded density and (3.1). If `range(S[J,K\J]) subset range(H)`, the induced affine vector lies in `range(U)` for every `W`, so the sharper `16 sqrt(30)` source constant proves (3.2). No rotation of the physical input coordinates was made, and independence is used only between original coordinate blocks. QED.

## 4. Exact compound-minor aggregation

A rank-two patch can be strong even when every individual physical `2x2` certificate is tiny. If `H` has nonzero eigenvalues `mu_1,mu_2`, then its second compound matrix has rank one and singular value `|mu_1 mu_2|`. Therefore

`|mu_1 mu_2|^2`
` = sum_{|R|=|C|=2, R,C subset J} det(H[R,C])^2.`    (4.1)

Hence (3.1) can be rewritten as

`||p_Q||_infinity`
` <=128 |a|^(-1/2)`
`   [ sum_{|R|=|C|=2} det(H[R,C])^2 ]^(-1/8),`    (4.2)

provided `rank(H)=2`.

The key point is that all physical pair minors are aggregated **before** paying the reciprocal cost. This is compatible with the live corrections refuting one-good-minor and one-good-pair reductions.

## 5. Named partner result actually applied

The designated partner `account02/B01` completed r24, canonical report

`yspennstate/math-open-problems@007d06d8118bc87becd247676c7a63ae336755c9`


Its theorem treats a rank-two residual

`H=S_frame Gamma S_frame^T`, `S_frame^T S_frame=I_2`,

a scalar independent square coefficient `d`, and one conditioned heavy residual row of leverage `c`, under a whitened-tail diffuse condition. It proves

`||p_Q||_infinity <= C0 |d|^(-1/2) [(1-c)|det Gamma|]^(-1/4),`

where

`C0=2*3^(1/4)*sqrt(pi e)=7.691879759019983...`.

In the **pure quadratic rank-two residual scope** (`V_j=0` in the partner notation), the new theorem applies with `J` equal to the whole residual coordinate bank and gives instead

`||p_Q||_infinity <= 16 sqrt(30) |d|^(-1/2)|det Gamma|^(-1/4)`    (5.1)

because there is no outside affine term. Combining the two valid estimates where the partner's whitened-tail hypothesis also holds gives the actual inequality

`||p_Q||_infinity`
` <= |d|^(-1/2)|det Gamma|^(-1/4)`
`    * min(16 sqrt(30), C0 (1-c)^(-1/4)).`    (5.2)

Thus the partner theorem is stronger away from the endpoint, while the new rank-two-patch theorem removes the blow-up as `c -> 1` in the pure quadratic residual branch.

For the partner's exact stress family

`A_{m,epsilon}=[1] direct_sum S_frame diag(1,-1) S_frame^T`

with one row leverage `c=1-epsilon`, every fixed physical pair certificate tends to zero as `m -> infinity`, but the full residual patch has nonzero eigenvalues exactly `+1,-1`. Therefore (5.1) gives the dimension- and epsilon-uniform bound

`||p_Q||_infinity <= 16 sqrt(30)=87.63560920082658...`.

The partner bound is `7.6918797590... epsilon^(-1/4)`; the new bound becomes the smaller of the two once

`epsilon < (7.6918797590.../(16 sqrt(30)))^4`
`        = 5.934819384269377e-05.`

This does not refute or replace the partner theorem, whose scope with arbitrary one-coordinate potentials is broader. It supplies a complementary endpoint closure for exact rank-two quadratic residuals.

## 6. Diagnostic computation

`check_compound.py` tests (4.1) on 150 random rank-two symmetric matrices and evaluates the constants in (5.2). The captured output is `CHECK_OUTPUT.txt` and ends

`STATUS=PASS`.

The largest numerical compound-identity discrepancy was `1.208e-13`; this is only a floating-point diagnostic, not part of the proof.

Checker source commit: `37b8db7cdfdeba9c95a378c54b2dbff237b3990b`.  
Captured-output commit: `7dbd2e4164369b931d75dce3920789d6e34aa804`.

## 7. What remains unpaid

This result closes a genuine grouped low-rank branch, but it does **not** prove that every matrix with three eigenvalues of modulus at least one possesses a dimension-free rank-two principal Schur patch. In particular, a general Schur complement may have rank greater than two on every useful large physical block. The next B01 implication is therefore:

**Higher-rank patch replacement.** Replace the exact `rank(H)=2` hypothesis by a condition that is forced by the bare three-large-eigenvalue assumption and remains stable under arbitrary additional Schur curvature, without reverting to a single shrinking physical minor or assuming independence after spectral rotation.

A plausible next mechanism is to combine the source rank-two half-Riesz theorem with the existing ridge/diffuse branch on the orthogonal residual curvature, but an actual inequality that keeps their dependence has not yet been proved.

## 8. Status

Classification: **ESSENTIAL_STEP_APPLIED**.  
Full QFORM conjecture: **OPEN**.  
Continuous density: **not proved** by this theorem; the conclusion is an essentially bounded density.  
No source-valid counterexample to the full conjecture was found in this run.
