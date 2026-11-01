SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B13, 2026-09-23T03:28:48Z.
attacking: the exact-null/near-null scalar gap by replacing one scalar Schur peel with an invertible indefinite physical pair, then gluing the pair singularity to the product-preserving cross-three-volume L3 theorem.

# fleet01/B13 auto14 — pair-anchored five-volume gluing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Status: **PROVED SUPPORTING TARGET-LEVEL CERTIFICATE / FULL QFORM OPEN / CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid inputs

The target remains the full arbitrary-dimensional statement for independent original-coordinate laws with densities `0<=f_i<=1` and a real symmetric matrix with at least three eigenvalues of absolute value at least one. No moment, compact-support, connected-support, iid, centering, log-concavity, or diagonal-basis assumption is made.

This proof uses three completed inputs at their exact scopes.

1. `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1`, canonical source
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   For two original independent cap-one coordinates with an invertible indefinite coefficient matrix `B`, writing
   `D=|det B|`, `kappa=sigma_min(B)`, and `t0` for the completed-pair critical value, for every `r>0`

   `p_pair(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2r^2/(kappa |t-t0|))`.

   The shifts of the two physical coordinates may depend arbitrarily on the remaining original variables when the estimate is applied conditionally.

2. `QFORM-CROSS-3VOLUME-L3-v1`, fleet03/B13, canonical source
   `yspennstate/math-open-problems@3345697a0e1ea6c84ef3128a22917d49f0b0a826`,
   path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T013555Z-fleet03-B13-qform-r21/REPORT.md`.
   If a quadratic polynomial in independent cap-one original coordinates has a disjoint physical cross block `M` with

   `Z=e_3(M^T M)>0`,

   then its output has an `L^3` density satisfying

   `||p||_3 < 6.787 Z^(-1/9)`.

   Arbitrary same-side quadratic terms and affine terms are allowed.

3. The designated partner fleet02/B13 result `QFORM-L3-RIESZ-INTERPOLATION-v1`, canonical source
   `yspennstate/math-open-problems@f3a7dec6b3f56132ba769d3e0e205596114f22c2`,
   path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T025607Z-fleet02-B13-extreme-cf3f0909/REPORT.md`.
   If a probability density `p` satisfies `||p||_3<=M`, then

   `sup_s int |x-s|^(-1/2) p(x) dx <= 4(4/3)^(3/4) M^(3/4)`.

   I apply this partner result below to an actual pair-Schur inequality. The same partner line also rests on the exact product-indicator purification; no single interval or centered uniform law is assumed.

The live corrections are respected: there is no law-uniform pointwise quadratic oscillatory decay, no independence after rotating the source, no arbitrary-joint three-dimensional coarea lemma, no positive worst conditional projection-density moment, and no bounded-diameter/fixed-fragment extremality step.

## 2. A sharper consequence of the physical-pair logarithmic envelope

The logarithmic pair envelope contains a useful pointwise half-Riesz majorant that was not used in the earlier pair-log gluing.

### Lemma 2.1 — `QFORM-INDEFINITE-PAIR-HALF-RIESZ-KERNEL-v1`

Let `U,V` be independent cap-one real variables and let

`F=(U,V) B (U,V)^T + 2 ell.(U,V)+c`,

where `B` is symmetric invertible indefinite and `kappa=sigma_min(B)`. Let

`t0=c-ell^T B^(-1) ell`.

Then `F` has a density satisfying, for almost every `t!=t0`,

`p_F(t) <= 4 kappa^(-1/2) |t-t0|^(-1/2)`.                 (2.1)

This is translation-uniform in `ell`.

### Proof

Use the completed pair envelope from input 1. For a fixed `t!=t0`, choose

`r^2 = kappa |t-t0|/2`.

Then

`2r^2/(kappa |t-t0|)=1`,

so its logarithmic term vanishes exactly. The remaining term is

`2 sqrt(2)/r = 4/[sqrt(kappa) sqrt(|t-t0|)]`.

That proves (2.1). The exceptional critical value is irrelevant for essential bounds and subsequent integration. No diagonalization of the random source is used. QED.

A key point is that this estimate depends on the least singular value `kappa`, not on either scalar diagonal entry. Thus it survives the exact zero-diagonal pair

`B=[[0,b],[b,0]]`,

where `kappa=|b|`.

## 3. Pair-Schur gluing to a cross-three-volume remainder

Let

`Q(x)=x^T A x + beta^T x + gamma`

in independent cap-one original coordinates. Choose two original coordinates `K={i,j}` and write, after reordering,

`A=[[B,C],[C^T,E]]`,

where `B=A[K,K]` is invertible indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`,
`S=E-C^T B^(-1) C`.

Completing the pair square gives

`Q = (X_K + m(X_R))^T B (X_K+m(X_R)) + R(X_R)`,            (3.1)

where `R` is a quadratic polynomial in the remaining ORIGINAL coordinates and `m(X_R)` is an arbitrary affine function of them. Conditional on `X_R`, the two pair variables remain the original independent variables, merely shifted by constants.

By Lemma 2.1, for almost every output value `t`,

`p_Q(t) <= 4 kappa^(-1/2) E |t-R|^(-1/2).`                 (3.2)

Now let `I,J` be disjoint original-coordinate sets contained in the complement of `K` and set

`M=S[I,J]`, `Z=e_3(M^T M)`.

If `Z>0`, input 2 gives

`||p_R||_3 < 6.787 Z^(-1/9)`.

Apply the designated partner fleet02/B13 half-Riesz interpolation to this ACTUAL remainder density. It yields

`sup_t E|t-R|^(-1/2)`
` < 4(4/3)^(3/4) 6.787^(3/4) Z^(-1/12)`
` < 20.870 Z^(-1/12).`                                      (3.3)

Substituting (3.3) into (3.2) proves:

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-CROSS3-LINF-v1`

Under the hypotheses above,

`boxed: ||p_Q||_infinity < 83.480 kappa^(-1/2) Z^(-1/12).`  (3.4)

All remaining spectrum, same-side curvature, signs, outside couplings and affine terms are arbitrary. The proof conditions only on original coordinates and does not infer independence after a spectral rotation.

The homogeneity is exact: scaling all quadratic coefficients by `s` sends `kappa` to `s kappa` and `Z` to `s^6 Z`, so the right side scales by `s^(-1)`.

## 4. Original-matrix pair-anchored five-volume identity

The Schur inverse in Theorem 3.1 can be eliminated from the exterior-volume part exactly.

For fixed disjoint `I,J` in the complement of `K`, define

`W_K(I,J)`
` = sum_{U subset I, |U|=3} sum_{V subset J, |V|=3}`
`     det A[K union U, K union V]^2.                         (4.1)`

For every `U,V`, block determinant gives

`det A[K union U, K union V]`
` = det(B) det( A[U,V]-A[U,K]B^(-1)A[K,V] )`
` = det(B) det S[U,V].`                                      (4.2)

Therefore

`boxed: W_K(I,J)=D^2 e_3(S[I,J]^T S[I,J])=D^2 Z.`           (4.3)

Combining (3.4) and (4.3) gives the fully original-matrix certificate

`boxed: ||p_Q||_infinity`
` < 83.480 kappa^(-1/2) D^(1/6) W_K(I,J)^(-1/12).`          (4.4)

This is `QFORM-PAIR-ANCHORED5VOLUME-v1`.

The certificate is genuinely complementary to a scalar anchored-four-volume certificate: it remains meaningful when `A_ii=A_jj=0` but `A_ij!=0`, because then `B` is invertible indefinite.

## 5. Aggregate-before-inversion version

Define the global pair-anchored disjoint five-volume

`Omega_K(A)`
` = sum det A[K union U, K union V]^2,`                      (5.1)

where the sum is over ordered pairs of disjoint triples `U,V` in `[n]\K`.

Randomly color every coordinate outside `K` red or blue, independently with probability `1/2`. Each ordered disjoint pair `(U,V)` is captured with `U` red and `V` blue with probability `2^(-6)=1/64`. Therefore some disjoint physical cut `I,J` in the complement of `K` satisfies

`W_K(I,J) >= Omega_K(A)/64.`                                 (5.2)

Since `64^(1/12)=sqrt(2)`, (4.4) yields:

### Theorem 5.1 — `QFORM-PAIR-ANCHORED-DISJOINT-5VOLUME-v1`

If `B=A[K,K]` is invertible indefinite, then whenever `Omega_K(A)>0`,

`boxed: ||p_Q||_infinity`
` < 118.059 kappa^(-1/2) D^(1/6) Omega_K(A)^(-1/12).`        (5.3)

No individual five-by-five minor is selected or inverted. The entire squared exterior-volume channel is aggregated first.

For a definite pair `B`, the already-completed ellipse estimate gives the simpler bound `pi/sqrt(D)`; thus Theorem 5.1 is targeted precisely at the indefinite/null-diagonal side.

## 6. A simple singular-value corollary

Suppose `K` is disjoint from another physical cross cut `I,J`, and let `M0=A[I,J]`. Since

`S[I,J]=M0-A[I,K]B^(-1)A[K,J]`

is a rank-at-most-two perturbation of `M0`, singular-value interlacing under rank-two perturbation gives

`s_3(S[I,J]) >= s_5(M0)`.

Hence

`Z=e_3(S[I,J]^T S[I,J]) >= s_3(S[I,J])^6 >= s_5(M0)^6`.

Theorem 3.1 therefore implies the clean local branch

`boxed: ||p_Q||_infinity < 83.480 [kappa s_5(M0)]^(-1/2).`   (6.1)

Thus one uniformly invertible indefinite physical pair plus five robust cross singular directions elsewhere is paid, with arbitrary same-side curvature retained.

## 7. Actual application to the designated partner's finite-grid bad-witness normal form

The designated fleet02/B13 r15 normal form, canonical report
`yspennstate/math-open-problems@d59fc91cdb6c772a0b3c73ba5b90fb62e10e3bf5`,
produces, under a hypothetical failure of full QFORM, for every `m` a rational finite-grid product-indicator witness with slab ratio

`R_m > C3 m`, `C3=9 sqrt(3e)=25.701021...`,

while all physical scalar/pair pivots are small and every disjoint physical cross block has `s_5<1/m`.

Apply Theorem 5.1 to ANY invertible indefinite physical pair `K` of such a witness. Since interval probability divided by interval length cannot exceed the density cap in (5.3), the strict bad-witness ratio forces

`kappa^6 D^(-2) Omega_K(A_m)`
` < (118.059/(C3 m))^12`
` < 8.83*10^7 m^(-12).`                                    (7.1)

This is a new simultaneous obstruction: every invertible indefinite physical pair of a hypothetical finite-grid counterexample must have its entire anchored disjoint five-volume collapse at the quantitative rate (7.1), after the natural pair conditioning factor is removed.

At the exact zero-diagonal endpoint

`B=[[0,b],[b,0]]`,

we have `D=b^2` and `kappa=|b|`, so (7.1) simplifies to

`boxed: |b|^2 Omega_K(A_m) < 8.83*10^7 m^(-12).`             (7.2)

This is the pair analogue of the earlier scalar anchored-four-volume collapse, and unlike that scalar certificate it remains active when every physical diagonal is exactly zero.

## 8. Product-set geometric form

The fleet02/B13 exact bang-bang theorem (`QFORM-PRODUCT-BANGBANG-REDUCTION-v1`, canonical commit `604a08009638981da254a72f09a24dd50e3a3c94`) identifies every fixed quadratic-slab supremum over cap-one product densities with the supremum over arbitrary unit-measure product indicators. Therefore Theorem 5.1 gives the actual requested geometric inequality: for every measurable `E_l subset R` with `|E_l|=1` and every interval `J0`, throughout the pair-anchored branch,

`|{x in product_l E_l : x^T A x in J0}|`
` < 118.059 kappa^(-1/2) D^(1/6) Omega_K(A)^(-1/12) |J0|.`  (8.1)

The sets may be disconnected, arbitrarily translated and have arbitrarily many components. The theorem does not assume a single interval or a centered uniform law. The same partner theorem says bounded finite unions suffice in the supremum, but there is no uniform fragment-count bound.

## 9. What remains

This run closes a concrete part of the zero-scalar-pivot gap: an invertible indefinite physical PAIR plus any residual cross-three-volume upgrades the product-preserving `L^3` theorem to an `L^infinity` bound; the certificate can be written as one aggregate original-matrix five-volume. It particularly covers exact zero diagonals whenever an off-diagonal edge has a sufficiently noncollapsed anchored five-volume.

It does NOT prove that the three-large-eigenvalue hypothesis forces the quantity in (5.3) to be uniformly favorable for some pair. The sharpened first unpaid implication is

`QFORM-NULLPIVOT-PAIR5VOLUME-OR-THREEBANK-v1`:

in the no-pivot finite-grid normal form, combine simultaneous scalar anchored-four-volume collapse with the new simultaneous pair anchored-five-volume collapse. Prove that what remains must enter a paid grouped three-bank / bi-hub / low-cross-rank skeleton branch, or construct a genuine product-indicator counterexample. In the exact zero-diagonal case, every nonzero physical edge now either pays by (5.3) or carries vanishing anchored five-volume in the precise sense (7.2).

Full QFORM remains OPEN / NOT PROVED. Continuity remains separately OPEN.

## 10. Deterministic checks

A local deterministic check on 100 random symmetric 10-by-10 matrices with an invertible indefinite physical pair verified

`W_K(I,J)=det(B)^2 e_3(S[I,J]^T S[I,J])`

with maximum absolute floating error `9.095e-13`. The same check gives

`4(4/3)^(3/4)=4.963225915211198`,
`C_local=83.47999646552641`,
`C_aggregate=118.05854318840548`,
`C3=25.70102107534928`,
`(C_aggregate/C3)^12=8.826011826395169e7`.

These numerical checks corroborate constants and the block identity only; the proof above is analytic.
