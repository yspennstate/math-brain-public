# B14 repair note and rigorous threshold conclusion

Pinned manuscript: blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## 1. Minimal repairs required in the baseline manuscript

### Replace the statement of `lem:quarter` (lines 485--494) by

> **Lemma (Quarter-power concentration).** Let `X=(X_1,...,X_m)` have independent real coordinates with probability densities bounded by one. Let `S=S^T != 0`, let `R=X^T S X+b^T X+c`, and put `L=||S||>0`. Then for all `a in R`, `rho>0`,
> `P{|R-a|<rho} <= min{1,16(rho/L)^(1/4)}`.
> In particular `R` has no atoms. If `L>=1`, then
> `sup_a E log_+(1/|R-a|) <= 4+4 log 16`.

No proof change is needed. The written proof already uses exactly these hypotheses.

### Replace the statement of `prop:pivot-H` (lines 676--681) by

> **Proposition (A pivot controls truncated half potentials).** Let `X` have independent real coordinates with probability densities bounded by one, let `A=A^T` have at least two eigenvalues of modulus at least one and an `eta`-pivot, and put `Q=X^TAX+b^TX+c`. Then for all affine terms,
> `H(Q)<=600`.

Again no proof change is needed. This removes the only input-law ambiguity in the finishing section.

These repairs are logically local. They do not change any constant, equation, later branch, or the main theorem, because the main theorem is normalized to precisely these cap-one product laws before either result is invoked.

## 2. Why the uncorrected quarter lemma is literally false

Take one coordinate, deterministic `X=0`, `S=[1]`, `b=c=0`. Then `R=0` has an atom. For `a=0` and any `rho<16^{-4}`,

`P{|R|<rho}=1 > 16 rho^(1/4)`.

Thus the missing law hypothesis is not cosmetic; it is necessary to the standalone lemma statement.

## 3. Rough-law closure needed by the multiplicity-nine replacement

For completeness, the new grouped compiler can be justified without any smoothness assumption as follows.

Let `nu=T_#(q mu)` be a finite complex pushforward with `|q|<=1`, and let `eta=T_#mu`. Then `|nu|<=eta` as measures: for every Borel partition `B=disjoint_union B_j`,

`sum_j |nu(B_j)| <= sum_j mu(T^{-1}B_j)=eta(B)`.

Hence if `eta=h dx`, then `nu=g dx` with `|g|<=h` a.e. This proves the hub-side `L2` domination used by the grouped compiler for arbitrary rough laws.

On the light side, if `nu*rho_eps` has a uniform `L2` bound `C`, weak compactness in `L2` supplies a subsequence converging weakly to `g` with `||g||_2<=C`. For every `psi in C_c^infinity`,

`int psi (nu*rho_eps) dx = int (psi*tilde rho_eps) dnu -> int psi dnu`

by uniform convergence of the test-function convolution and finiteness of `|nu|`. Weak `L2` convergence gives the same limit as `int psi g dx`, so `nu=g dx`. Thus the compiler's mollified estimate passes to the unmollified complex pushforward with exactly the same constant. No moment, bounded support, translation bound, smoothness, or pointwise conditional-density version is used.

## 4. Lowest theorem supported by the complete-proof/review gate

The complete replacement proof

`improvements/account02/B09/20260924T144107Z-account02-B09-fixedmult-auto11/NINE_EIGENVALUE_REPLACEMENT.md`

proves, after restoring the product-law hypothesis in the baseline quarter lemma,

`boxed: s_9(A)>=s >0  ==>  ||p_{X^TAX+b^TX+c}||_infinity <= 6010 K^2/s.`

A sharper independently reconstructed constant `<5338 K^2/s` is recorded in the full reviews. The proof keeps all hubs/promotions as literal original coordinates and uses coefficient-space orthogonalization only deterministically, so no hidden rotated-independence assumption occurs.

At least two genuinely separate complete reviews are present and PASS: account01/B07 and account02/B05; account01/B16 supplies a third complete PASS reconstruction. Hence multiplicity **9** meets the requested replacement-proof-plus-two-reviews gate.

Multiplicity **8** does not. Current eight-direction work produces a structural overlap/collar (and a bilateral-shear normal form) but no dependence-safe, arbitrary-curvature receiver yielding a linear interval bound. Full negative-half-potential control alone is insufficient to imply an `L^infinity` density bound. Therefore the rigorous threshold conclusion of this B14 audit is **9, not 8**.
