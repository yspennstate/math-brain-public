# account02/B08 — perturbatively stable diffuse block certificate

**Run:** `B08-20260922T153820Z-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**

## 0. Exact target and live corrections

For every dimension `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, the owner asks for one universal finite bound on the density of `X^TAX`, or a valid counterexample. No moments, support connectedness, centering, identical laws, sign assumption, or independence after spectral rotation is available.

This run consumed the current correction inbox at brain main `a024fc6d01d9af0a0503bd76732e41014c3166a4`, inbox blob `2ee621225465e603dfd118f6bd86b1ddc853f40e`. In particular it does not use law-uniform pointwise oscillatory decay, unrestricted fiber suprema, conditional-density caps after non-product changes of variables, or a bare local cross-rank-three dichotomy.

The named partner result actually used is account03/B08 `QFORM-DIFFUSE-BLOCK-REMAINDER-v1`, canonical source

`yspennstate/math-open-problems@55d185b63ba44f172d9342b5d89e0875e850e17a`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T122924Z-account03-B08-qform-diffuse-v2/REPORT.md`.

Its exact block-coloring step is applied below, not merely cited as background. The perturbative closure uses the completed one-scale ridge theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

at

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

The latest partner full-range theorem at `f6bc73f719d1e9dbcaeb06df49913bb84dd274b6` is also used to certify that the explicit family in Section 4 lies genuinely outside that theorem's hypothesis.

## 1. First unpaid implication attacked

The preceding B08 run proved an exact separator theorem: after conditioning a physical coordinate set `H`, if the spectral remainder compression becomes block diagonal with sufficiently small selected-frame mass in each block, then the density is uniformly bounded. Its first unpaid implication was to extract such a separator from arbitrary dense remainder structure, or replace exact separation by an aggregate cross-block certificate.

The new observation is that exact separation is unnecessary. A block-diagonal remainder may be accompanied by a **dense full-rank operator-norm perturbation**. The partner's block coloring supplies a strong selected-spectrum cross block, while the new ridge theorem quantitatively absorbs the dense perturbation. This gives an explicit robust interface between localized conditioning and diffuse smoothing.

## 2. General theorem — `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`

Let

`A = R Lambda R^T + C`,

where `R` is `n x 3` with orthonormal columns and `Lambda` is real symmetric with

`s_min(Lambda) >= 1`.

For the target application, the columns of `R` are any three eigenvectors whose eigenvalues have modulus at least one and `C` is the remaining spectral part, so `CR=0`; the proof below only needs the displayed decomposition.

Condition on an arbitrary set `H` of original physical coordinates and put `T=H^c`. Define

`M = R_T^T R_T = I - R_H^T R_H`,

`eta = ||R_H^T R_H||_op`,

and assume `eta<1`. Whiten the surviving selected frame by

`W = R_T M^(-1/2)`,

so `W^T W=I_3`.

Assume that on the surviving coordinates the remainder can be decomposed as

`C[T,T] = C_0 + E`,

where `C_0` is block diagonal over a partition `G_1,...,G_m` of `T`. Put

`mu = max_k ||W_{G_k}^T W_{G_k}||_op`,
`tau = ||E||_op`,

and suppose `mu<1/3`. Set

`alpha = (1-sqrt(3 mu))/2`,
`sigma = alpha (1-eta)`,
`rho = sigma - tau`.

If

`rho>0`

and

`( sqrt(mu/alpha) + sqrt(6) tau/rho )^2 <= 1/2`,

then for every admissible independent cap-one product law, `Q=X^TAX` has a bounded continuous density, vanishing at infinity, with

`||p_Q||_infinity <= 9 sqrt(3e)/(2 rho).`

No moments, support assumptions, sign restrictions, or independence after rotation are used. The perturbation `E` may be dense, full rank, indefinite, and nonseparable.

### Proof

Condition on `X_H`. Independence and the density caps on the unconditioned original coordinates are unchanged. All interactions with `H` become fixed affine terms, so it is enough to obtain a characteristic-function bound uniform in the conditioned value.

Rewrite the selected part on `T` as

`R_T Lambda R_T^T = W Lambda_T W^T`,

where

`Lambda_T = M^(1/2) Lambda M^(1/2)`.

Since `M >= (1-eta) I` and `s_min(Lambda)>=1`,

`s_min(Lambda_T) >= 1-eta`.

Now apply the exact block-coloring construction proved in the named partner result `QFORM-DIFFUSE-BLOCK-REMAINDER-v1` to the Parseval frame `W` and the blocks `G_k`. There is a union of whole blocks `I` and its complement `J=T\I` such that

`Sigma_I = W_I^T W_I >= alpha I_3`,
`Sigma_J = W_J^T W_J >= alpha I_3`,

with `alpha=(1-sqrt(3mu))/2`. Because the cut is a union of whole `C_0`-blocks,

`C_0[I,J]=0`.

The selected cross block is therefore

`B_0 = W_I Lambda_T W_J^T`.

Its three nonzero singular values are those of

`Sigma_I^(1/2) Lambda_T Sigma_J^(1/2)`,

hence

`s_3(B_0) >= alpha (1-eta) = sigma`.

Moreover `range(B_0)=range(W_I)`. If `P_S` denotes the orthogonal projection onto this range, then for `i in I`,

`(P_S)_{ii} = w_i^T Sigma_I^(-1) w_i <= ||w_i||^2/alpha <= mu/alpha`,

because the singleton row outer product is dominated by its block Gram matrix.

The actual cross block of the full conditional quadratic form is

`B = A[I,J] = B_0 + F`,

where `F=E[I,J]` and `||F||<=tau`. Weyl's inequality gives

`s_3(B) >= sigma-tau = rho`.

Choose

`gamma = rho/sqrt(6)`.

Then the ridge effective dimension from the completed ridge theorem satisfies

`theta_gamma >= 3 rho^2/(gamma^2+rho^2) = 18/7 > 2`.

The same theorem's perturbation lemma gives for every coordinate on the `I` side

`(K_gamma)_{ii}
 <= ( sqrt((P_S)_{ii}) + tau/gamma )^2
 <= ( sqrt(mu/alpha) + sqrt(6) tau/rho )^2
 <= 1/2`.

Thus its `q=1` criterion applies. The three-singular-value corollary gives

`||p_Q||_infinity <= 9 sqrt(3e)/(2 rho)`.

The ridge proof supplies one integrable characteristic-function envelope independent of the values conditioned on in `H`; averaging therefore preserves the same envelope and yields a continuous `C_0` density for the unconditional quadratic form. QED.

## 3. Clean numerical corollary

A particularly simple source-valid regime is

`eta <= 1/4`,
`mu <= 1/48`,
`tau <= 1/40`.

Then

`alpha >= 3/8`,
`sigma >= 9/32`,
`rho >= 9/32-1/40 = 41/160`,
`mu/alpha <= 1/18`.

For the ridge-leverage condition,

`(sqrt(mu/alpha)+sqrt(6)tau/rho)^2
 <= (1/sqrt(18)+4sqrt(6)/41)^2`.

A crude exact bound already suffices:

`1/sqrt(18) < 1/4`, `4sqrt(6)/41 < 10/41`,

so the preceding square is less than

`(1/4+10/41)^2 = (81/164)^2 < 1/2`.

Therefore

`||p_Q||_infinity
 <= (720/41) sqrt(3e)
 = 50.1483338055... < 51.`

This is a robust conditioned theorem: the physical remainder need only be **approximately** block diagonal, with a dense operator-norm error of size `1/40` allowed.

## 4. Exact dense full-rank family outside the preceding diffuse theorems

Let `H_256` be the Sylvester Hadamard matrix and let `R` be its first three columns divided by `16`. Then `R^TR=I_3` and every selected row has squared norm

`3/256`.

Take

`Lambda = diag(1,1,-1)`,
`C = (1/40)(I-RR^T)`,
`A = R Lambda R^T + C`.

This is an exact target matrix. Since `CR=0`, its eigenvalues are

`1, 1, -1, 1/40, ..., 1/40`,

so `A` is full rank and has the required three large eigenvalues.

Use `H=empty`, singleton blocks, `C_0=0`, and `E=C`. Then

`mu=3/256`,
`alpha=(1-sqrt(9/256))/2=13/32`,
`rho=13/32-1/40=61/160`,
`mu/alpha=3/104`.

The exact checker gives

`(sqrt(3/104)+4sqrt(6)/61)^2
 = 0.1092063451437711... <1/2`,

and hence

`||p_Q||_infinity
 <= (720/61)sqrt(3e)
 = 33.70625714799906... <34.`

This family is deliberately outside three earlier supporting branches.

1. `C` is genuinely nonseparable: if `S` denotes the first three unnormalized Hadamard columns, every off-diagonal entry of `SS^T` is one of `-1,1,3`, never zero. Thus every off-diagonal entry of `C` is nonzero. The partner's exact block-diagonal-remainder theorem cannot be applied to the actual remainder by any nontrivial block partition.
2. `A` is invertible, so its entire-range projection is `I_256`; the partner's latest full-range diffuse theorem has leverage one and does not apply.
3. Since `1/40>1/64`, the spectral projection onto all eigenspaces with `|lambda|>=1/64` is also `I_256`. Hence the new `1/64` spectral-window theorem's `max P_ii<=1/32` hypothesis fails maximally.

The present perturbatively stable certificate nevertheless gives the explicit `<34` bound for **all** independent input densities bounded by one.

## 5. Exact computation record

Checker source was committed first at

`yspennstate/math-open-problems@f19e67dfda23900a1e0f47320fcd7aaaafed0f77`

in this run directory. Its archived output was committed at

`yspennstate/math-open-problems@391c94fdca1f2972938a94ccc573514306b143ed`.

The checker verifies the exact Hadamard orthogonality, exact annihilation `(256I-SS^T)S=0`, nonzero off-diagonal remainder entries, all rational constants above, and records the two ridge bounds and density constants. Terminator:

`QFORM_B08_STABLE_BLOCK_CHECK_PASS`.

The floating evaluations are used only to display constants; the theorem inequalities are proved symbolically above.

## 6. What this closes and what remains

This run strictly weakens the preceding B08 exact-separator hypothesis: after localized physical-coordinate conditioning, the residual spectral remainder need only be block diagonal **up to a dense operator-norm perturbation**. The new result also treats full-rank matrices with a genuinely dense nonseparable tail that are excluded by both the partner's full-range theorem and the current `1/64` spectral-window theorem.

The full conjecture is still open. The first remaining structural implication is now:

### `QFORM-DIFFUSE-APPROX-BLOCK-EXTRACTION-v1`

Given only a delocalized selected three-large-eigenvector frame `R` and an arbitrary spectral remainder `C` with `CR=0`, prove that after conditioning a set carrying uniformly bounded selected mass one can either

1. decompose the surviving remainder as `C_0+E` with small whitened block mass and operator error satisfying the theorem above, or
2. use failure of every such approximate block decomposition to force a direct aggregate ridge/cross-block smoothing certificate.

This is sharper than the previous exact-separator debt: a dense remainder of norm up to a fixed positive constant is now already paid. The unsolved obstruction is therefore a remainder that is simultaneously nonseparable **and** not small in the relevant operator scale, while evading all source-valid aggregate cross-block certificates.

## 7. Status

**Proved in this run:** `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`, its clean `<51` conditional corollary, and the exact full-rank dense-tail Hadamard family with bound `<34`.

**Named partner result applied:** account03/B08 `QFORM-DIFFUSE-BLOCK-REMAINDER-v1` supplies the quantitative whole-block coloring used in the proof.

**Additional completed source applied:** one-scale ridge leverage theorem at commit `9c1167db05c7b0f520f060796fde921ed769a4e7` supplies perturbative ridge control and the final Fourier inversion.

**Not proved:** the approximate-block extraction dichotomy for arbitrary spectral remainders, or the unrestricted QFORM conjecture.
