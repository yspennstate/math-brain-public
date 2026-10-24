# account02/B19 — exact one-effective aggregate core and contamination residual

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T151209Z-account02-B19-qform-r15`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The target remains: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of `Q=X^TAX`, or give a target-valid counterexample. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption is added.

Fresh control was read from `yspennstate/math-research-brain@46b75c39fb2d557c6550afd43d7bfdc26772177a`. The live correction inbox through that commit was consumed. In particular this report does not use law-uniform pointwise Fresnel decay, conditional-cap-as-independence, a universal good physical triple, a rank-three cross-cut dichotomy, or an absolute phase-Wiener norm.

The designated partner result actually applied is account03/B19, canonical `yspennstate/math-open-problems@143e97c42cdbccb14fe847efb6abd3f6c3d349dc`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T143049Z-account03-B19-QFORM-r11b/REPORT.md`. Its one-effective residual writes

`A = D + lambda v v^T + R`, `||R||op<=1/8`,

with opposite heavy physical diagonals `a,b>=7/8`, every tail diagonal `<1/7`, `|lambda|>=41/56`, tail mass `r^2>=27/41`, and a normalized tail aggregate `w` on a coordinate bank disjoint from the two heavy coordinates. Its exact main three-variable core is

`M0 = diag(a,-b,0) + lambda (x,y,r)^T(x,y,r)`.

The partner proved that the actual compressed matrix remains nondegenerate after contamination, but left the product-preserving use of the aggregate unpaid.

Two completed compatible results are also used with exact scope:

1. account02/B11, canonical `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, proves that every normalized linear form in independent cap-one coordinates has density at most `sqrt(e)`.
2. account03/B11, available in the completed zero-pivot/local-three-variable synthesis report on the current science branch, proves for an invertible indefinite physical three-variable block with a nonzero scalar pivot `c` the uniform bound `||p||inf <= 8 |c det B|^(-1/4)` in the indefinite-Schur branch, while the complementary definite-Schur branch has the smaller constant `2 sqrt(pi)` on the same scale. The proof is uniform in affine terms.

## 2. New theorem: the exact one-effective aggregate core is already paid

### Theorem — `QFORM-EXACT-ONE-EFFECTIVE-AGGREGATE-v1`

Let `p,q` be two original coordinates and let `T` be a disjoint coordinate bank. Let `X_i` be independent with one-dimensional densities at most one. Let `w in R^T` satisfy `||w||_2=1`, and put

`Z = sum_{k in T} w_k X_k`.

Assume

`a,b >= 7/8`, `|lambda| >= 41/56`, `r^2 >= 27/41`,

and consider the exact aggregate quadratic

`Q0 = [X_p,X_q,Z] M0 [X_p,X_q,Z]^T + affine terms`,

where

`M0 = diag(a,-b,0) + lambda (x,y,r)^T(x,y,r)`.

Then `Q0` has a density and

`||p_{Q0}||_infinity <= 64 sqrt(e)/(3 sqrt(3)) < 20.307`.

The bound is independent of the dimension of `T`, of the coefficients `x,y`, and of all input laws subject to the cap-one hypotheses.

### Proof

Because `T` is disjoint from `{p,q}`, the scalar variables `X_p`, `X_q`, and `Z` are genuinely independent. This is not post-rotation independence: `Z` is a measurable function of an original coordinate bank disjoint from the two heavy coordinates.

By the completed one-dimensional projection lemma from account02/B11,

`||p_Z||_infinity <= K := sqrt(e)`.

The determinant of the rank-one update has an exact closed form. Since `diag(a,-b,0)` has adjugate supported only in the third diagonal entry,

`det M0 = -a b lambda r^2`.

The third physical diagonal pivot of `M0` is

`c = lambda r^2`.

The matrix is invertible and indefinite: the unperturbed diagonal matrix has one positive, one negative, and one zero direction, and a rank-one update can remove the zero but cannot remove both opposite signs. Thus one of the completed account03/B11 nonzero-pivot branches applies.

Rescale only the aggregate scalar by `Z_tilde=K Z`. Its density is at most one. The corresponding matrix is

`M_tilde = S^{-1} M0 S^{-1}`, `S=diag(1,1,K)`.

Hence

`c_tilde = c/K^2`, `det M_tilde = det M0/K^2`,

so

`|c_tilde det M_tilde| = |c det M0|/K^4`.

Using the worse of the two local constants gives

`||p_{Q0}||_infinity <= 8 K |c det M0|^(-1/4)`.

Now

`|c det M0| = a b (|lambda| r^2)^2`.

The partner normal-form bounds imply

`|lambda| r^2 >= (41/56)(27/41)=27/56`,

and therefore

`|c det M0| >= (7/8)^2 (27/56)^2 = 729/4096`.

Consequently

`||p_{Q0}||_infinity <= 8 sqrt(e) (4096/729)^(1/4)`
`= 64 sqrt(e)/(3 sqrt(3)) < 20.307`.

This proves the theorem. QED.

### Stronger constant if the sharp one-dimensional projection cap is imported

The partner report records the sharper standard cap `||p_Z||inf<=sqrt(2)`. If that exact projection theorem is used with its own proof source, the same argument gives `64 sqrt(6)/9 < 17.419`. The canonical theorem above deliberately uses the fully source-pinned `sqrt(e)` bound reproved by account02/B11.

## 3. Exact relevance to the designated partner

The partner's one-effective branch is not blocked by the aggregate itself. If its contamination vanished, namely

`R=0` and `D_T=0`,

then the full quadratic form would depend on the entire tail bank only through the single normalized aggregate `Z=w^T X_T`, and the theorem above would close that branch with a universal constant.

Thus the first unpaid implication is strictly narrower than the partner's earlier `mixed aggregate compression splice`: the pure rank-one aggregate core is paid. What remains is the effect of same-bank contamination, where the same original tail variables simultaneously generate the good aggregate and the perturbing quadratic/cross terms.

## 4. Quantitative adversary against bounded-cardinality physical extraction

The paid exact core itself shows why one cannot replace aggregation by a bounded number of original coordinates.

For `m>=8`, let `w=m^(-1/2)(1,...,1)` on a tail bank of size `m` and set

`A_m = diag(1,-1,0_m) + w w^T`.

Then the nonzero spectrum is exactly `{1,-1,1}`, so this is an exact target-rank-three family. Relative to the physical diagonal of `A_m`, the off-diagonal part on the tail is

`H_m = J_m/m - I_m/m`,

whose eigenvalues are `1-1/m` and `-1/m` with multiplicity `m-1`. Hence for `m>=8`,

`||H_m||op>7/16`, `s_2(H_m)=1/m<=1/8`,

and every tail diagonal of `A_m` is `1/m<1/7`. The partner's one-effective regime is therefore realized exactly, with aggregate compression `diag(1,-1,1)`.

Yet for any physical principal subset `S` containing at most `K` coordinates, the third singular value obeys

`s_3(A_m[S,S]) <= K/m`.

Indeed, if `S` contains both heavy coordinates and `r` tail coordinates, the tail block is `J_r/m`, whose only nonzero eigenvalue is `r/m`; all other cases have no larger third singular value. Therefore any fixed-cardinality physical extraction loses the third curvature as `m->infinity`. To retain third singular value at least `delta`, one needs at least `delta m` tail coordinates.

The family is not a QFORM counterexample. In fact `Z=w^T X_T` is independent of the two heavy coordinates and has density at most `sqrt(e)`, so the theorem above already gives a universal bound. A direct same-sign-square convolution also bounds this special family. The point is structural: the correct interface must genuinely compile a growing coordinate bank.

This strengthens, rather than contradicts, the live local-extraction corrections: in the exact one-effective chamber, the aggregate is both mathematically sufficient and quantitatively unavoidable for this family.

## 5. Conditional full-proof architecture after this run

Combining completed source-valid branches gives the following conditional architecture.

- Near-diagonal matrices and definite physical two-plane branches are paid.
- High off-diagonal stable-rank/diffuse branches and full-range diffuse regularized-determinant branches are paid in their stated scopes.
- Physical invertible three-variable branches, including zero-pivot and both nonzero-pivot Schur signatures, are paid.
- Rank-two mixed packets with scalar curvature, including two-sided scalar coupling after Schur correction, are paid when a product-compatible packet is actually extracted.
- The designated partner reduces the low-offdiagonal-rank branch to either `s_2(H)>1/8` (still requiring product-preserving two-resource extraction) or the one-effective normal form above.
- This run pays the **uncontaminated** one-effective normal form by compiling the whole tail into one genuine independent scalar aggregate.

The full theorem would follow if the two remaining structural transfers were proved: the `s_2(H)>1/8` bank extraction, and the contaminated one-effective aggregate transfer below, together with the already-recorded handling of arbitrary extra spectrum in every branch where it is genuinely source-valid.

## 6. First unpaid implication with exact quantifiers

### `QFORM-SAME-BANK-CONTAMINATION-SPLICE-v1` — OPEN

There should exist a universal finite constant `C` such that the following holds.

Let independent cap-one coordinates be split into two heavy coordinates `{p,q}` and a disjoint tail bank `T`. Suppose

`A = diag(a,-b,D_T) + lambda v v^T + R`,

where `v=(x,y,v_T)`, `r=||v_T||_2`, `w=v_T/r`, and

`a,b>=7/8`,
`|lambda|>=41/56`,
`r^2>=27/41`,
`max_k |(D_T)_{kk}|<1/7`,
`||R||op<=1/8`,
`x^2,y^2<=7/41`.

Prove

`||p_{X^T A X}||_infinity <= C`

uniformly in dimension, all coefficients satisfying those inequalities, and all admissible input laws.

The theorem in Section 2 proves this when `D_T=0` and `R=0`. What remains is precisely that the perturbation is generated by the **same tail variables** as the good aggregate `w^T X_T`; it cannot be replaced by independent convolution noise, nor may one rotate the tail and condition on an orthogonal complement while retaining a false conditional density cap.

A quantitatively useful replacement would be any dimension-free theorem that pays this branch under a source-valid additional condition on `(D_T,R)` and whose failure forces the complementary `s_2(H)>1/8` or diffuse/cross-block branch.

## 7. Status

**New proved implication:** `QFORM-EXACT-ONE-EFFECTIVE-AGGREGATE-v1`, universal bound `<20.307` in the exact partner core.

**New exact stress family:** `A_m=diag(1,-1,0_m)+J_m/m`, showing that bounded-cardinality physical extraction cannot replace the aggregate; third curvature `>=delta` requires at least `delta m` tail coordinates.

**Not proved:** same-bank contamination splice, the general `s_2(H)>1/8` extraction, arbitrary unresolved extra-spectrum cases, or the full conjecture. No full-proof claim is made.
