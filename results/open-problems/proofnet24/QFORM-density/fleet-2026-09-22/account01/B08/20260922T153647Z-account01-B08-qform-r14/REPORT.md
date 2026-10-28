# account01/B08 — robust separator/ridge theorem for diffuse selected eigenvectors

**Run:** `20260922T153647Z-account01-B08-qform-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and source dependencies

The full target remains open: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of magnitude at least one, prove one universal density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, sign, finite-rank, or post-rotation independence hypothesis is added here.

This run consumes the live corrections: law-uniform pointwise quadratic-phase decay is false; unrestricted fiber suprema lose dimension; a single cross minor / single Schur pivot / fixed local cut is not forced by the spectral hypothesis; transformed conditional density caps do not preserve the needed product structure. None of those claims is used below.

The named assignment partner result actually used is **account02/B08** `QFORM-DIFFUSE-SEPARATOR-CONDITIONING-v1`, canonical source

`yspennstate/math-open-problems@537a79d82a9af69b8fd35a1086538db339cc74eb`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/account02-B08-20260922T143724Z-r12/REPORT.md`.

For a selected orthonormal frame `R`, conditioning a physical separator `H` gives the exact surviving Gram

`M=R_T^T R_T=I-R_H^T R_H`, `T=H^c`,

and whitening `W=R_T M^{-1/2}`. If the exact residual on `T` is block diagonal and the original block selected masses are bounded by `mu`, the partner proof gives whitened block mass at most `mu/(1-eta)`, where `eta=||R_H^T R_H||op`, and its whole-block coloring produces a physical cut with both selected Gram matrices bounded below by

`alpha I`, `alpha=(1-sqrt(r mu/(1-eta)))/2`.

That exact quantitative cut is the partner inequality applied below.

The analytic endpoint is the complete `QFORM-RIDGE-DENSITY-v1` proof at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

path

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.


## 2. New theorem: approximate block remainder survives

### Theorem — `QFORM-ROBUST-SEPARATOR-RIDGE-v1`

Let

`A=R Lambda R^T+C`,

where `R` is an `n x 3` real matrix with orthonormal columns and `Lambda` is real symmetric with all three singular values at least one. In the target application these are any three genuine eigenvectors with `|lambda_j|>=1`, and `C=A-R Lambda R^T`.

Condition an arbitrary set `H` of **original physical coordinates**, put `T=H^c`, and define

`eta=||R_H^T R_H||op`, `beta=1-eta`.

Assume `eta<1`. Suppose on `T` the residual admits

`C[T,T]=D+E`,

where `D` is block diagonal over a partition `T=G_1 union ... union G_m`, while `E` is an arbitrary real symmetric matrix. Put

`mu=max_k ||R_Gk^T R_Gk||op`, `mu_bar=mu/beta`,

and assume `3 mu_bar<1`. Define

`alpha=(1-sqrt(3 mu_bar))/2`,

`sigma_0=alpha beta`.

Let `epsilon=||E||op`. Assume `epsilon<sigma_0`, set

`sigma=sigma_0-epsilon`,

and choose any `tau in (0,1/sqrt(2))`. If

`[ sqrt(mu_bar/alpha) + epsilon/(tau sigma) ]^2 <= 1/2`,                (2.1)

then for every admissible independent cap-one product law the full quadratic form `Q=X^T A X` has a bounded **continuous `C_0` density** satisfying

`||p_Q||infinity
 <= [sqrt(e)/(sqrt(2) tau sigma)]
    * theta_0/(theta_0-2),`                                           (2.2)

where

`theta_0=3/(1+tau^2)>2`.

All entries and signs inside each block of `D` are arbitrary. The perturbation `E` can be globally dense and nonseparable. All couplings to the conditioned set `H` are arbitrary.

### Proof

Condition on `X_H=x_H`. Because the conditioning uses original independent coordinates, `X_T` remains a product law with the original one-dimensional density caps. All `H-T` couplings become affine terms in `X_T`; the ridge theorem permits such terms.

The partner result gives

`M=R_T^T R_T >= beta I_3`,

`W=R_T M^{-1/2}`, `W^T W=I_3`,

and the selected matrix on `T` is

`R_T Lambda R_T^T = W Lambda_T W^T`,

`Lambda_T=M^{1/2} Lambda M^{1/2}`.

For every residual block,

`||W_Gk^T W_Gk||op <= mu_bar`.

Apply the whole-block coloring step from the partner proof to the block family of `D`. There is a union-of-blocks cut `I|J` of `T` such that, with

`Sigma_I=W_I^T W_I`, `Sigma_J=W_J^T W_J`,

one has

`Sigma_I,Sigma_J >= alpha I_3`.                                      (2.3)

Since `D` is block diagonal and whole blocks are colored, `D[I,J]=0`. Thus the conditional physical cross block is

`B = B_0+F`,

`B_0=W_I Lambda_T W_J^T`, `F=E[I,J]`, `||F||op<=epsilon`.            (2.4)

The nonzero singular values of `B_0` are those of

`Sigma_I^{1/2} Lambda_T Sigma_J^{1/2}`.

For every vector `x`, because `M>=beta I` and `s_min(Lambda)>=1`,

`||Lambda_T x||
 =||M^{1/2} Lambda M^{1/2}x||
 >= beta ||x||`.

Together with (2.3),

`s_3(B_0)>=alpha beta=sigma_0`.

Weyl's singular-value perturbation inequality applied to (2.4) yields

`s_3(B)>=sigma_0-epsilon=sigma>0`.                                 (2.5)

Next control the ridge leverage on the `I` side. Since `Sigma_J` and `Lambda_T` are invertible,

`range(B_0)=range(W_I)`.

For a row `w_i` of `W_I`,

`(P_range(B0))_ii = w_i^T Sigma_I^{-1} w_i
 <= ||w_i||^2/alpha`.

The coordinate `i` belongs to some block `G_k`, and

`w_i w_i^T <= W_Gk^T W_Gk`,

hence `||w_i||^2<=mu_bar`. Therefore

`ell:=max_i(P_range(B0))_ii <= mu_bar/alpha`.                      (2.6)

Set `gamma=tau sigma` and form the ridge operator

`K_gamma(B)=BB^T(gamma^2 I+BB^T)^{-1}`.

The ridge-stability lemma in `QFORM-RIDGE-DENSITY-v1`, applied to `B=B_0+F`, gives

`max_i (K_gamma(B))_ii
 <= [sqrt(ell)+epsilon/gamma]^2
 <= [sqrt(mu_bar/alpha)+epsilon/(tau sigma)]^2
 <=1/2`                                                            (2.7)

by (2.1).

By (2.5), at least three singular values of `B` are at least `sigma`. Consequently its ridge effective dimension satisfies

`theta_gamma=tr K_gamma(B)
 >= 3 sigma^2/(gamma^2+sigma^2)
 =3/(1+tau^2)=theta_0>2`.                                          (2.8)

Apply `QFORM-RIDGE-DENSITY-v1` with `q=1`. Its coarse determinant-free form is

`||p||infinity
 <= [sqrt(e)/(sqrt(2) gamma)] theta_gamma/(theta_gamma-2)`.

The function `x/(x-2)` decreases on `(2,infinity)`, so (2.8) and `gamma=tau sigma` give (2.2), uniformly in the conditioned value `x_H`.

The ridge proof supplies a uniform integrable characteristic-function envelope, also independent of `x_H`. Averaging the conditional characteristic functions preserves that envelope. Fourier inversion therefore gives the asserted bounded continuous `C_0` unconditional density. QED.

## 3. Explicit robust diffuse corollary

Take no separator (`H` empty), so `beta=1`. Suppose the selected three-large-eigenvector frame has a physical block partition for which

`mu=max_k ||R_Gk^T R_Gk||op <=1/48`,

and decompose the true spectral remainder as

`C=D+E`,

with `D` block diagonal on those blocks and

`||E||op<=1/16`.

Then

`alpha=(1-sqrt(3/48))/2=3/8`,

`mu/alpha=1/18`,

`sigma_0=3/8`, `sigma>=5/16`.

Choose `tau=1/2`, hence `gamma>=5/32` and

`theta_0=3/(1+1/4)=12/5`.

The ridge-leverage condition follows exactly from

`sqrt(1/18)+(1/16)/[(1/2)(5/16)]
 =1/(3sqrt(2))+2/5
 <1/sqrt(2)`,

because `2/5 < sqrt(2)/3` (equivalently `36<50`). Thus (2.1) holds. Formula (2.2) gives the explicit universal bound on this robust branch

`||p_Q||infinity
 <= 96 sqrt(2e)/5
 =44.7675644466...`.                                                (3.1)

The density is continuous and vanishes at infinity.

This is a strict structural extension of the exact block-remainder branch: a globally dense, arbitrarily signed and nonseparable residual defect of operator norm `1/16` is permitted. No smallness of the entries or rank of `E` is required.

## 4. What this pays and what remains

The preceding B08 debt was `QFORM-SELECTED-DIFFUSE-ARBITRARY-REMAINDER-v1`: selected three-large-eigenvector diffuseness alone does not control an arbitrary high-rank spectral remainder. This run pays a genuine open neighborhood of the exact-block/separator branch. It also shows that exact component structure is not necessary: one may first isolate a block-structured part and spend a quantitative operator-norm defect through ridge leverage.

It does **not** prove the unrestricted conjecture. The remaining first implication is now sharper:

**`QFORM-DIFFUSE-LARGE-DEFECT-AGGREGATION-v1` (OPEN).** Given a sufficiently diffuse selected three-dimensional large-eigenspace, if every useful physical block/separator approximation leaves residual operator defect larger than the ridge budget above, extract from that large defect either (i) enough ridge effective dimension of the *actual* cross block directly, or (ii) a product-preserving bank/star smoothing certificate. The live singleton-plus-two-banks obstruction shows this cannot be phrased as a universal rank-three cross-cut theorem.

A natural quantitative split is frequency dependent: at a chosen physical cut, a large residual defect can hurt the selected-space ridge leverage only if it contributes appreciable singular mass; one should charge that same mass to `theta_gamma` rather than bounding it purely as an adversarial perturbation. That is the next mechanism for B08.

## 5. Verification scope

The companion checker verifies the exact constants in Section 3 and the algebraic admissibility inequalities. It does not replace the analytic proof. No Monte Carlo or distributional regularity assumption is used.
