# fleet01/B08 — finite-rank floating paving for diffuse quadratic forms

**Run:** `20260922T144029Z-fleet01-B08-qform-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-FINITE-RANK-FLOATING-PAVING-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Scope, corrections, and source dependencies

The target remains the full arbitrary-product-law statement: independent real `X_i` with densities `0<=f_i<=1`, real symmetric `A`, and at least three eigenvalues of `A` of modulus at least one. No moments, support regularity, sign restriction, or post-rotation independence is assumed.

Fresh control was read from `yspennstate/math-research-brain` main, initially at `bb31f4fe59319fd29922dbd4ae21528c5bf91bbc`; the prepublication head observed was `8af8b62de2a0d44f7ba57c9f737a5bf787c94ed1`, with unchanged owner revision `2026-09-22.5` and no later stop. Live corrections consumed include the failure of law-uniform pointwise quadratic-phase decay, fiber-supremum dimension loss, loss of independence after rotation, the false one-cross-minor/local-cut dichotomies, and the conditional-density-cap counterexamples. None is used as a premise.

The named completed partner result actually applied is **fleet02/B08** `QFORM-DIFFUSE-RANGE-FRACTIONAL-MSS-v1`, canonical report

`yspennstate/math-open-problems@4fe4c12495d52c47fa86a2e389ba571e85277e22:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260922T133725Z-fleet02-B08-QFORM-r12/REPORT.md`.

Its analytic endpoint is the source-dependent regularized-determinant cross-block estimate: if an original-coordinate cross block has three singular values at least `sigma`, and the coordinate leverage of its range on one physical side is at most `q/2` for `1<=q<3/2`, then

`||p_Q||_infinity <= 3e/[sqrt(2q) sigma (3-2q)]`,

with continuity of the density. The partner obtained the needed cut from two-part MSS. The present run replaces that partition step by a different finite-dimensional floating/rounding mechanism; the analytic endpoint is then applied verbatim to the resulting quantitative cut.

The regularized-determinant source used by the partner is

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

## 2. New deterministic-probabilistic paving lemma

### Lemma 2.1 — floating half-paving

Let `U in R^{n x m}` have orthonormal columns, with rows `u_i^T`, and put

`c_i=||u_i||^2`, `delta=max_i c_i`, `d=m(m+1)/2`, `kappa_m=sqrt(d)/2=sqrt(m(m+1)/8)`.

Then there is a subset `I` of the original coordinates, with complement `J`, such that

`|| U_I^T U_I - (1/2)I_m ||_op <= kappa_m delta`,

and hence the same bound holds for `U_J^T U_J-(1/2)I_m`.

#### Proof

Set `A_i=u_i u_i^T in Sym_m`; then `sum_i A_i=I_m` and `||A_i||_op=c_i<=delta`. Start with fractional coefficients `x_i=1/2`, so

`sum_i x_i A_i=(1/2)I_m`.

While more than `d=dim Sym_m` coefficients lie strictly between zero and one, the corresponding matrices are linearly dependent. Choose a nonzero vector `h` supported on the fractional coordinates with `sum_i h_i A_i=0`, and move `x` in one of the two directions `x +/- t h` until at least one fractional coefficient reaches `0` or `1`. This preserves the matrix sum and all coefficients remain in `[0,1]`. Iteration leaves at most `d` fractional coefficients.

Independently round each remaining fractional `x_i` to a Bernoulli variable `Y_i in {0,1}` with mean `x_i`; leave integral coordinates fixed. Let

`E=sum_i (Y_i-x_i)A_i`.

Then `E E=0`, and independence gives

`E ||E||_F^2 = sum_i Var(Y_i) ||A_i||_F^2`.

For rank-one `A_i`, `||A_i||_F=c_i`; there are at most `d` random terms and `Var(Y_i)<=1/4`. Therefore

`E ||E||_F^2 <= d delta^2/4 = kappa_m^2 delta^2`.

Some rounding outcome satisfies `||E||_op<=||E||_F<=kappa_m delta`. Taking `I={i:Y_i=1}` proves the claim. `QED`.

This is a genuinely different mechanism from the preceding fractional-frame-weight route and from the partner's MSS partition. Its gain is strongest when the spectral range rank `m` is moderate.

## 3. Main theorem: finite-rank diffuse full-spectrum branch

### Theorem 3.1 — `QFORM-FINITE-RANK-FLOATING-PAVING-v1`

Let `U in R^{n x m}` have orthonormal columns and `Lambda` be a real symmetric invertible `m x m` matrix with at least three eigenvalues of absolute value at least one. Put

`delta=max_i ||u_i||^2`,
`kappa_m=sqrt(m(m+1)/8)`,
`alpha=1/2-kappa_m delta`.

Assume `alpha>0` and choose `q` with

`1<=q<3/2`,
`2 delta/alpha <= q`.

For independent real `X_i` with densities `0<=f_i<=1`, and even after adding arbitrary measurable coordinate-separable real terms `sum_i V_i(X_i)`, the random variable

`T=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`

has a bounded continuous density and

`||p_T||_infinity <= 3e/[sqrt(2q) alpha (3-2q)]`.                 (3.1)

In particular, this applies to every rank-`m` symmetric matrix `A=U Lambda U^T` in the stated diffuse regime, uniformly over arbitrarily small additional nonzero eigenvalues among the remaining `m-3` spectral directions.

#### Proof

Apply Lemma 2.1 and write

`M_I=U_I^T U_I`, `M_J=U_J^T U_J`.

Then

`alpha I_m <= M_I,M_J <= (1-alpha)I_m`.

In particular both restricted frames have full column rank. Across this original-coordinate cut, the nonseparable quadratic component has cross block

`B=U_I Lambda U_J^T`.

Writing `U_I=P M_I^(1/2)` and `U_J=R M_J^(1/2)` with `P,R` column isometries shows that the nonzero singular values of `B` equal those of

`M_I^(1/2) Lambda M_J^(1/2)`.

Hence, for every singular-value index,

`s_k(B) >= alpha s_k(Lambda)`.

Because the third singular value of `Lambda` is at least one, `B` has three singular values at least `alpha`.

Moreover `Lambda` and `U_J^T` have full row rank, so

`range(B)=range(U_I)`.

The coordinate leverage on the `I` side is therefore

`(P_range(B))_ii = u_i^T M_I^(-1)u_i <= ||u_i||^2/alpha <= delta/alpha <= q/2`.

Now apply the completed fleet02/B08 fractional cross-block inequality with `sigma=alpha`, exactly three retained singular directions, and the chosen `q`. The regularized-determinant proof permits arbitrary within-`I` and within-`J` self phases, so the coordinate-separable terms `V_i` are harmless. Formula (3.1) follows, and the same `L^1` characteristic-function envelope yields a continuous density. `QED`.

## 4. Thresholds and combination with the partner's MSS branch

A suitable `q in [1,3/2)` exists precisely under the strict sufficient condition

`delta < delta_m^* := 3/[2(4+3 kappa_m)]`.                     (4.1)

Indeed `2delta/alpha<3/2` is equivalent to `(4+3kappa_m)delta<3/2`.

The particularly clean choice `q=1` is valid whenever

`delta <= delta_m^(1) := 1/[2(2+kappa_m)]`.                   (4.2)

The new floating partition can also be combined with the partner's MSS partition rather than replacing it. MSS gives half-partition error `delta+sqrt(2delta)`, while Lemma 2.1 gives `kappa_m delta`. Thus one may use

`eta_m(delta)=min{kappa_m delta, delta+sqrt(2delta)}`,
`alpha_best=1/2-eta_m(delta)`,

and then the same condition `2delta/alpha_best<=q<3/2`. This never weakens the partner branch and strictly improves it in the finite-rank regimes where `kappa_m delta < delta+sqrt(2delta)`.

For reference, the floating thresholds `delta_m^*` exceed `1/16` through rank `m=18`; hence the low/moderate-rank full-range branch is strictly enlarged beyond the partner's clean all-rank `1/16` certificate.

## 5. Strict witness: rank four with an arbitrarily tiny fourth eigenvalue

Take a normalized real `32 x 32` Sylvester Hadamard matrix and let `U` be any four of its columns. Then

`U^T U=I_4`, `||u_i||^2=4/32=1/8` for every row.

Let

`Lambda_epsilon=diag(1,1,-1,epsilon)`, `0<|epsilon|<1`.

This is an exact target-signature family with three eigenvalues of modulus one and an arbitrarily small fourth nonzero eigenvalue. For `m=4`,

`kappa_4=sqrt(5/2)=sqrt(10)/2`,
`alpha=1/2-kappa_4/8=(8-sqrt(10))/16`,
`delta/alpha=2/(8-sqrt(10))<1/2`.

Thus `q=1` is valid and Theorem 3.1 gives the epsilon-independent bound

`||p_T||_infinity <= 48e/[sqrt(2)(8-sqrt(10))] < 19.072`.       (5.1)

This family lies outside the partner's all-rank `delta<=1/16` certificate because `1/8>1/16`. It also shows why retaining only the previous direct full-determinant Brascamp--Lieb estimate is insufficient here: that estimate pays `|det Lambda_epsilon|^{-1/4}=|epsilon|^{-1/4}`, whereas (5.1) is uniform as `epsilon->0`. The regularized cross-block route correctly discards the tiny fourth singular value after the new partition creates three paid cross directions.

The companion checker records the exact threshold formulas and the rank-four constant.

## 6. What this changes and what remains open

This run does **not** prove the unrestricted conjecture. It gives a new source-dependent but complete supporting theorem for finite/moderate-rank diffuse spectral ranges and improves the usable leverage region of the partner's regularized-determinant branch without paying arbitrary small eigenvalues.

The first essential unpaid implication remains the genuinely hard one:

**`QFORM-SELECTED-DIFFUSE-ARBITRARY-REMAINDER-v1`.** When only the three large spectral directions are diffuse but the rest of the spectral range is arbitrarily high-rank/localized, convert that selected-space diffuseness into either (i) a true original-coordinate cross block whose regularized range leverage remains controlled despite the remainder, or (ii) a product-preserving localized smoothing payment for the high-leverage remainder. The live corrections rule out replacing this by a single good principal minor/cut or by post-rotation conditional density caps.

The floating lemma suggests a possible next move: perform the half-paving only on the selected large spectral subspace, then quantify how much the remainder can enlarge the **regularized** (frequency-dependent) cross-block leverage before its own determinant mass becomes large enough to pay the tail. That is a different, frequency-dependent bridge and does not require a false uniform full-range leverage statement.

## 7. Verification

`check.py` and `check_output.txt` in this immutable run folder verify the threshold algebra. In particular:

- rank 4: `delta_4^*=0.171557651596...`;
- rank 4 with `delta=1/8`: `alpha=0.302357646239...`, `delta/alpha=0.413417691117...`, and the `q=1` constant is `19.071277389398...`;
- at `delta=1/16`, `q=1` is valid through rank 16, while the general `q<3/2` floating regime still covers rank 18.

The script checks constants only; the analytic proof is the argument above.
