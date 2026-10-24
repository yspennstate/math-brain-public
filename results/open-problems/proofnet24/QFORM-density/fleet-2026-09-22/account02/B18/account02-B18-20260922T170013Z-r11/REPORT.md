# account02/B18 — zero-pivot product-projection compression and source audit

**Run:** `account02-B18-20260922T170013Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The target remains the full arbitrary-product statement: independent real coordinates with densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. The desired conclusion is one finite dimension-independent bound for the density of `X^T A X`. No moment, support, centering, log-concavity, smoothness, or independence-after-rotation hypothesis is introduced here.

This run isolates a sharper exact-rank-three zero-pivot problem.

**First unpaid implication `QFORM-PROJECTION-PROVENANCE-TRACE-v1`.** Let `X` be a scalar cap-one variable independent of a product vector `Z`; let `Y=R^T Z`, where `R` has orthonormal columns and `dim(Y)=2` or `3`. For the canonical forms

`T = Y^T B Y + 2 X ell^T Y`,

prove a universal density bound in the three rank cases forced by `rank([[0,ell^T],[ell,B]])=3`:

1. `dim Y=2`, `rank B=1`, `ell notin Ran(B)`;
2. `dim Y=2`, `B` invertible and `ell^T B^{-1} ell != 0`;
3. `dim Y=3`, `B` invertible and `ell^T B^{-1} ell = 0`.

The effective symmetric matrix is also required to satisfy the target spectral normalization (three nonzero eigenvalues of modulus at least one, or equivalently the normalized `s_3=1` form after target scaling).

The point is that `Y` is not an arbitrary bounded-density vector: it is an orthogonal projection of an original-coordinate product law. The Livshyts--Paouris--Pivovarov theorem gives a sharp dimension-free joint density cap for `Y`, but the current correction set shows that a bare joint/conditional cap is not enough to justify the needed curved trace. A proof must retain this product-projection provenance.

## 2. Current controls and completed partner actually applied

The fresh brain control read for this run was on the QFORM programme; later control revision `2026-09-22.8` kept the same mathematical target and added no stop for this slot. Relevant live corrections include the failure of pointwise law-uniform quadratic oscillatory decay, unrestricted fiber suprema, conditional-cap-for-independence substitutions, one-good-minor extraction, and single-Schur-rank-two extraction.

The designated completed partner result actually used is account03/B18 run `B18-20260922T155856Z-r13`, canonical mathematics

`yspennstate/math-open-problems@fb0c75e8f951da2564fe595f09f7e484c37dfd40`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/B18-20260922T155856Z-r13/REPORT.md`.

That report source-checks Livshyts--Paouris--Pivovarov (LPP) and proves `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1`. I use its LPP transfer quantitatively below; I do **not** extend the one-sided cross theorem across an uncontrolled self-quadratic block.

## 3. Primary source transfer: sharp product marginals

Primary source:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949.

Their theorem applies exactly to the present source class: if

`f(z)=prod_j f_j(z_j)`, `||f_j||_infinity <= 1`,

and `E` is a `k`-dimensional subspace, then the density of the orthogonal marginal onto `E` is bounded by

`2^(k/2)`.

No moments, bounded support, log-concavity, identical distributions, or smoothness are assumed.

A useful immediate corollary, retaining exact constants, is the following. Let `L:R^m -> R^k` have full row rank. Write

`S=(L L^T)^(-1/2) L`,

so `S S^T=I_k` and `LZ=(L L^T)^(1/2) S Z`. Therefore

`||p_(LZ)||_infinity <= 2^(k/2) / sqrt(det(L L^T)).`     (3.1)

If `k=m`, orthogonal change of variables preserves the full product density cap `<=1`, which is stronger than the displayed bound.

This is a genuine source-matching theorem. It controls a **joint projection density**, not independence of its projected coordinates.

## 4. New exact algebra: bordered-rank trichotomy at a zero physical pivot

### Theorem 4.1 — `QFORM-ZEROPIVOT-RANK-TRICHOTOMY-v1`

Let `A` be a real symmetric matrix of exact rank three and choose a physical coordinate `i` with `A_ii=0`. Write, after moving `i` first,

`A = [[0,b^T],[b,C]]`.

Then `r=rank(C)` belongs to `{1,2,3}`. Let `R=Ran(C)`, `N=Ker(C)`, decompose `b=b_R+b_N`, and when `b_R in R` put

`alpha = b_R^T (C|_R)^(-1) b_R = b^T C^+ b`

when `b_N=0`. Exactly one of the following holds:

- **rank-one deletion:** `r=1` and `b_N != 0`;
- **rank-two deletion:** `r=2`, `b_N=0`, and `alpha != 0`;
- **rank-three isotropic deletion:** `r=3`, `b_N=0`, and `alpha=0`.

#### Proof

Choose an orthonormal basis of the residual space adapted to `R direct_sum N`; in it

`C = diag(C_R,0)`

with `C_R` invertible. If `b_N !=0`, rotate inside `N` so its first vector is `b_N/||b_N||`. A congruence eliminating `b_R` through `C_R^{-1}` reduces the nonzero part of the border to

`diag(C_R, [[-alpha, ||b_N||],[||b_N||,0]])`.

The last `2x2` block has determinant `-||b_N||^2`, hence rank two. Therefore

`rank(A)=r+2` when `b_N !=0`.

If `b_N=0`, the same Schur-completion congruence yields

`diag(C_R,-alpha,0_N)`,

so

`rank(A)=r+1_{alpha !=0}`.

Imposing `rank(A)=3` gives precisely the three cases above. Also `r=0` is impossible because a pure zero-diagonal border has rank at most two. QED.

The third case is exactly a Schur-isotropic obstruction: the residual `C` is rank three and the border vector lies on the null cone of `C^{-1}`. This is the algebraic zero-pivot form of the live near-isotropic difficulty; it is not an artifact of a chosen eigenbasis.

## 5. New product-preserving compression

### Theorem 5.1 — `QFORM-ZEROPIVOT-LPP-COMPRESSION-v1`

Under Theorem 4.1 let

`E = Ran(C) + span{b}`

inside the residual physical coordinate space. Then

- in the rank-one deletion case, `dim(E)=2`;
- in the rank-two deletion case, `dim(E)=2`;
- in the rank-three isotropic deletion case, `dim(E)=3`.

Let `R_E` have orthonormal columns spanning `E`, put `Y=R_E^T X_{-i}`, and write

`C=R_E B R_E^T`, `b=R_E ell`.

Then the exact quadratic form is

`X^T A X = Y^T B Y + 2 X_i ell^T Y`,      (5.1)

and `X_i` is genuinely independent of `Y` because `Y` uses only the other original physical coordinates. Moreover LPP gives

`||p_Y||_infinity <= 2` in both two-dimensional cases,

`||p_Y||_infinity <= 2^(3/2)=2 sqrt(2)` in the three-dimensional isotropic case.      (5.2)

No independence of the coordinates of `Y` is asserted or needed for (5.2).

#### Proof

The dimension statements follow immediately from the three cases of Theorem 4.1. Since both the range of `C` and `b` lie in `E`, the quadratic expression depends on the residual physical vector only through its orthogonal projection onto `E`, giving (5.1). Independence of `X_i` from the entire residual vector is part of the original product law and survives applying a deterministic function to the residual vector. Finally (5.2) is exactly the LPP orthogonal-marginal theorem. QED.

This is a strict reduction in **output dimension**, but not a reduction to independent eigen/projection coordinates. It converts every exact-rank-three zero physical pivot into a scalar independent coordinate plus a two- or three-dimensional product projection with an explicit joint density cap.

## 6. Target-valid dependence test: why projected coordinates may not be declared independent

Consider the effective matrix

`M = [[0,1,1,0],
      [1,1,0,0],
      [1,0,-1,0],
      [0,0,0,1]].`

Its spectrum is exactly

`{-sqrt(3), 0, 1, sqrt(3)}`,

so it is a target-valid exact-rank-three matrix and its first physical pivot is zero. Here `C=diag(1,-1,1)`, `b=(1,1,0)`, and

`b^T C^{-1} b = 1-1=0`,

so this is the rank-three isotropic case of Theorem 4.1.

Now take the explicit non-permutation orthogonal matrix whose columns are

`u1=(1,1,0)/sqrt(2)`,

`u2=(1,-1,2)/sqrt(6)`,

`u3=(1,-1,-1)/sqrt(3)`.

Replacing the residual coordinates by this physical rotation preserves the spectrum and the zero first pivot. If the original residual physical inputs are iid `Uniform[-1/2,1/2]`, the projected vector `Y=O^T Z` is uniform on a rotated cube. Its coordinates are not independent: the support is not a Cartesian product of one-dimensional supports because `O` is not a signed permutation.

Thus the exact target already contains zero-pivot instances in which the low-dimensional `Y` in Theorem 5.1 is genuinely dependent. Applying an independent-three-variable density theorem after this projection would reintroduce precisely the forbidden rotation-independence assumption.

## 7. Literature audit: oscillatory Loomis--Whitney does not source-match a quadratic phase

Primary source audited:

Maxim Gilula, Kevin O'Neill, Lechao Xiao, *Oscillatory Loomis-Whitney and Projections of Sublevel Sets*, arXiv:1903.12300; J. Anal. Math. 145 (2021).

Their Theorem 1.1 assumes a real-analytic phase satisfying their Newton-polyhedron **nondegeneracy** condition. In their Section 2.1 the phase is first decomposed as

`S(x)= sum_{alpha in (N\{0})^d} c_alpha x^alpha + tilde S(x)`,

where `tilde S` is a sum of functions each omitting one coordinate, and that `tilde S` is absorbed into the Loomis--Whitney factors. Their nondegeneracy requires, on every compact Newton face,

`D_d S_F = partial_1 ... partial_d S_F != 0`

off the coordinate hyperplanes.

For **every quadratic polynomial** in dimension `d>=3`, every monomial has total degree at most two, hence omits at least one of the `d` variables. Consequently the entire quadratic polynomial belongs to the absorbable `tilde S` class and the fully mixed Newton part is identically zero. Equivalently,

`partial_1 ... partial_d S == 0` for every quadratic `S` and every `d>=3`.

Therefore their nondegeneracy hypothesis fails universally on the QFORM phase. Their Oscillatory Loomis--Whitney theorem and its stated sublevel corollary cannot be transferred to prove the desired quadratic density estimate.

This remains true after any linear orthogonal change of phase variables: a quadratic polynomial is still quadratic and still has no monomial involving all `d>=3` variables. More importantly for the present problem, a generic orthogonal change would also destroy the original product structure of the amplitude. Hence there is no source-valid escape through rotation.

### Claim status

`QFORM-OLW-QUADRATIC-DEGENERACY-v1`: **PROVED SOURCE-HYPOTHESIS OBSTRUCTION**. It is a no-go for this literature transfer, not a counterexample to the QFORM conjecture.

The result does not rule out scalar resolution-of-singularities arguments designed specifically for quadratic phases; it only prevents citing this multilinear Loomis--Whitney theorem as though its hypotheses matched the target.

## 8. Exact use and exact limit of the designated partner theorem

Account03/B18's `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1` proves a bounded continuous density for

`G(U)+2 U^T B V + beta^T V`

when `U,V` are independent original-coordinate families and `rank(B)>=2`; it deliberately allows a same-side term only on the `U` side. The canonical zero-pivot forms (5.1) generally contain the self-quadratic term `Y^T B Y` on the same projected side that supplies the cross linear form. Therefore that theorem cannot simply be applied to (5.1).

What **does** transfer exactly is its LPP input: (5.2) supplies a universal cap for the complete low-dimensional projection. The remaining gap is therefore not projection-density blowup itself. It is a curved quadratic trace of a dependent projection law, with its product-projection provenance needing to be used more strongly than a bare `L^infinity` cap.

This distinction also respects the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: a bounded pair density plus a bounded conditional scalar density is not a substitute for genuine independence in a hyperbolic-square reduction.

## 9. Relation to the full target

**What changed.** The zero-pivot exact-rank-three branch is no longer an unspecified high-dimensional algebra problem: it has the exact three-way classification in Theorem 4.1 and the product-preserving low-dimensional compression in Theorem 5.1. The designated partner's sharp marginal theorem gives explicit caps `2` or `2 sqrt(2)` on the projected law. In parallel, the most tempting multilinear Newton-polyhedron literature transfer is proved inapplicable to quadratic phases at its source hypothesis.

**What did not change.** The full theorem is still open. A bounded joint density for `Y` alone does not authorize a universal curved-trace bound, and the correction archive already contains examples showing that naive fiberwise trace or conditional-density replacements can diverge. The arbitrary-extra-spectrum case also remains beyond this exact-rank-three reduction.

The next mathematically honest attack is `QFORM-PROJECTION-PROVENANCE-TRACE-v1`: prove the density estimate for the three canonical projected-product forms above, preferably by a weighted physical-space Brascamp--Lieb/coarea argument that acts before the orthogonal projection has forgotten product structure. A successful bound stable under a small nonzero pivot would directly feed the owner-prioritized near-isotropic branch. A failure must be a counterexample realized by an actual orthogonal projection of a cap-one product law, not by an arbitrary bounded joint density.

## 10. Source pins

- Fresh brain main at substantive publication check: `be314b24f4b6d59aa6754dd17e79f6dcb8a19730`; owner-control revision `2026-09-22.8`; mathematical programme revision remains `2026-09-22.5`.
- LPP: arXiv:1507.07949, *On sharp bounds for marginal densities of product measures*.
- Gilula--O'Neill--Xiao: arXiv:1903.12300, *Oscillatory Loomis-Whitney and Projections of Sublevel Sets*.
- Designated partner account03/B18: `math-open-problems@fb0c75e8f951da2564fe595f09f7e484c37dfd40`, report path pinned in Section 2.
- Corrections used from live brain: pointwise-decay false; fiber-sup dimension loss; no independence after rotation; conditional-cap-not-independence; single-Schur-rank2-extraction false; local-cross-rank3 dichotomy false; fiberwise-trace-mass bound false.

No claim in this report is a full solution or an independent review of a peer proof.
