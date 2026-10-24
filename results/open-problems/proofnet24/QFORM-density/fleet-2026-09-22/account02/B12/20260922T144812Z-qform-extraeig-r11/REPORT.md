# account02/B12 — spectral-tail stability under arbitrary added eigen-directions

**Run:** `20260922T144812Z-qform-extraeig-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_STABILITY_THEOREMS / FULL_TARGET_OPEN`  
**Context:** authenticated private-repository retrieval was used directly in this derivation; no claim is made of native learned-memory ingestion.

## 1. Exact target and live correction discipline

The full target remains open: for arbitrary independent real `X_i` with densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension-free bound on the density of `X^T A X`, or give a valid counterexample.

This report does **not** rotate the random vector and does **not** treat an added quadratic term as an independent convolution. All analytic certificates below are phrased on disjoint sets of the original independent coordinates.

The live correction inbox was re-read before publication. In particular, this argument does not use the refuted fixed-minor, single-Schur-pivot, post-rotation-independence, conditional-cap, or pointwise-Fresnel mechanisms.

The first unpaid implication attacked here is precise: once a source-valid physical smoothing certificate has been found, determine when arbitrary additional eigen-directions — including a few arbitrarily large directions plus an arbitrarily large cloud of smaller directions of either sign — can be added without destroying that certificate.

## 2. Source-pinned inputs actually applied

### 2.1 Reviewed regularized cross-block determinant theorem

From the interactive canonical report

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`,

if `I,J` are disjoint original-coordinate sets and `B=A[I,J]` has five singular values at least `alpha>0`, then for every admissible product source the law of `Q=X^TAX` has a continuous density and

`||p_Q||_infinity <= 5e/(2 alpha)`.                                      (2.1)

No leverage assumption is needed in this five-direction version, and the theorem keeps arbitrary self blocks, outside couplings and signs.

The requested independent review of Sections 3--6 was completed by account02/B02 and passed at

`yspennstate/math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T140817Z-account02-B02-qform-r11/REPORT.md`.

### 2.2 Assigned partner account03/B12

I also apply the completed partner result

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

Its theorem `QFORM-TWO-SAMESIGN-THREEBLOCK-v1` gives, for a physical `3x3` block with two same-sign eigenvalues of magnitude at least `L` and arbitrary third eigenvalue,

`||p_Q||_infinity <= C_*/L`,

where

`C_*=C_3+sqrt(C_3^2+3 pi^2)=24.183038289961516...`,
`C_3=2pi+3sqrt(3)`.                                                       (2.2)

In particular a physical definite triple with gap `L` survives one arbitrary global rank-one quadratic perturbation, of either sign and any magnitude.

## 3. Arbitrary spikes plus an arbitrary small spectral tail

Write `s_k(M)` for the `k`-th singular value in decreasing order.

### Theorem 3.1 — `QFORM-CROSS-SPECTRAL-TAIL-STABILITY-v1`

Let `A_0,E` be real symmetric `n x n` matrices. Let `I,J` be disjoint original-coordinate sets. Fix an integer `r>=0` and numbers `sigma>delta>=0`. Assume

` s_{5+r}( A_0[I,J] ) >= sigma`.                                         (3.1)

Assume `E` admits a decomposition

`E=R+S`,

with

`rank(R)<=r`, `||S||_op<=delta`.                                         (3.2)

Then, for

`A=A_0+E`,

one has

` s_5( A[I,J] ) >= sigma-delta`.                                         (3.3)

Consequently every admissible product source satisfies

`||p_{X^TAX}||_infinity <= 5e/[2(sigma-delta)]`.                         (3.4)

Moreover the density has the continuous representative supplied by the reviewed determinant theorem.

#### Proof

Set

`B_0=A_0[I,J]`, `R_0=R[I,J]`, `S_0=S[I,J]`.

Taking a submatrix cannot increase rank or operator norm, so

`rank(R_0)<=r`, `||S_0||_op<=delta`.                                     (3.5)

The singular-value rank perturbation inequality gives

` s_k(M+N) >= s_{k+r}(M)` whenever `rank(N)<=r`.                          (3.6)

For completeness, (3.6) is the standard singular-value Weyl inequality

` s_{k+r}(M) <= s_k(M+N)+s_{r+1}(-N)`,

and `s_{r+1}(N)=0` under the rank hypothesis. Applying (3.6) with `k=5` gives

` s_5(B_0+R_0) >= s_{5+r}(B_0) >= sigma`.                                (3.7)

The operator-norm Weyl inequality then gives

` s_5(B_0+R_0+S_0) >= s_5(B_0+R_0)-||S_0||_op >= sigma-delta`.            (3.8)

Now apply (2.1) to the **final physical cross block** `A[I,J]`. This proves (3.4). No decomposition of the random output and no independence of the quadratic pieces is used. QED.

### Spectral form of the hypothesis

Because `E` is symmetric, let its eigenvalues be ordered by magnitude,

`|tau_1|>=|tau_2|>=...`.

If `|tau_{r+1}|<=delta`, split `E` spectrally into its first `r` eigen-directions and the remainder. Then (3.2) holds. Hence Theorem 3.1 says:

> a physical cross certificate with `5+r` singular directions of size `sigma` survives **r completely arbitrary added eigen-directions** — any signs and any magnitudes — together with arbitrarily many further added eigen-directions of either sign whose magnitudes are at most `delta<sigma`.

The simple numerical constant in (3.4) is

`5e/2 = 6.7957045711476125...`.                                          (3.9)

Two useful endpoints are worth recording.

* `r=0`: an arbitrary full-rank perturbation with operator norm at most `delta<sigma` preserves the five-cross certificate, with `sigma` replaced by `sigma-delta`.
* `delta=0`: an arbitrary rank-`r` symmetric perturbation of completely unrestricted norm and sign is harmless provided the base cross block has `5+r` redundant singular directions at least `sigma`.

This is absolute certificate stability, not relative stability of output density norms. The latter was refuted in the preceding B12 run.

## 4. Applying the assigned partner: one arbitrary spike plus an arbitrary small tail around a physical definite triple

The partner theorem yields a second stability mechanism which needs no cross-block redundancy.

### Theorem 4.1 — `QFORM-DEFINITE-TRIPLE-SPIKE-TAIL-STABILITY-v1`

Let `T` be three original coordinates and suppose

`A_0[T,T] >= L I_3`                                                        (4.1)

or symmetrically `A_0[T,T] <= -L I_3`, for some `L>0`.

Let

`E=tau vv^T + S`,                                                         (4.2)

where `tau` is arbitrary real, `v` is arbitrary, and

`||S||_op<=delta<L`.                                                       (4.3)

Then for `A=A_0+E`, every admissible product source satisfies

`||p_{X^TAX}||_infinity <= C_*/(L-delta)`,                                (4.4)

with `C_*` from (2.2).

#### Proof

On the physical triple,

`||S[T,T]||_op<=delta`,

so `A_0[T,T]+S[T,T]` remains definite with gap at least `L-delta`. The remaining update on that block is

`tau v_T v_T^T`,

of rank at most one and arbitrary sign/magnitude. Apply the partner's arbitrary-rank-one perturbation corollary at gap `L-delta`, then condition on all outside original coordinates. Outside quadratic terms and cross couplings enter only through the affine tilt already allowed by the partner theorem. QED.

Thus a single arbitrarily large added eigen-direction can coexist with an arbitrarily large number of smaller eigenvalues of either sign, without any post-rotation independence assumption, whenever a physical definite triple is present with a spectral margin.

## 5. Unlimited same-sign additions around a physical definite pair

There is also a zero-cost Loewner-monotone branch.

### Proposition 5.1 — `QFORM-DEFINITE-PAIR-MONOTONE-ADDITION-v1`

If a physical pair `T` satisfies `A_0[T,T]>=L I_2` and `E>=0` is an arbitrary positive-semidefinite global perturbation of any rank and magnitude, then for `A=A_0+E`,

`||p_{X^TAX}||_infinity <= pi/L`.                                        (5.1)

The negative-definite/negative-semidefinite analogue also holds.

Indeed `A[T,T]>=L I_2`. Condition on all other original coordinates. The conditional joint density of the two remaining coordinates is at most one; after completing the square the level annulus of the positive-definite quadratic has area density exactly `pi/sqrt(det A[T,T])<=pi/L`. Mixing the conditional laws preserves the same bound.

This branch permits arbitrarily many added eigenvalues with the favorable Loewner sign.

## 6. Exact obstruction: the `+r` cross-direction redundancy is algebraically necessary

The redundancy count in Theorem 3.1 cannot be reduced if one wants a guarantee based only on the number of strong singular directions in one fixed physical cross block.

Fix `r>=1`, `sigma>0`, and put `m=4+r`. Let `I,J` be disjoint coordinate sets of size `m`. Define

`A_0 = [[0, sigma I_m], [sigma I_m, 0]]`.                                 (6.1)

Thus `A_0[I,J]=sigma I_m` has exactly `4+r` singular values equal to `sigma`.

For `a=1,...,r`, let

`z_a=(e_a^I+e_a^J)/sqrt(2)`,

and add the rank-`r` spectral perturbation

`R=-2 sigma sum_{a=1}^r z_a z_a^T`.                                      (6.2)

The vectors `z_a` are orthonormal, so `R` has rank `r` and consists of `r` added eigen-directions, each of eigenvalue `-2sigma`. Its cross block is

`R[I,J]=-sigma diag(I_r,0_4)`.                                           (6.3)

Therefore the final cross block is

`(A_0+R)[I,J]=sigma diag(0_r,I_4)`,                                      (6.4)

which has only four nonzero singular values. Hence `4+r` initial strong directions do **not** guarantee the five directions needed by the unconditional determinant certificate after an arbitrary rank-`r` spectral addition.

This obstruction lies inside the actual matrix class rather than an arbitrary row model. Each canceled two-coordinate block becomes `-sigma I_2`, while each uncanceled block remains `[[0,sigma],[sigma,0]]`; consequently **every eigenvalue of the final matrix has absolute value `sigma`**. For `sigma>=1` the final matrix is deep inside the full QFORM hypothesis.

This is not a counterexample to QFORM: it only proves that a more optimistic fixed-cross-block stability rule without the `+r` redundancy is false.

## 7. What changed and what remains open

### Target-level status

`OPEN -> OPEN.` No universal density bound was proved from the bare three-large-eigenvalue hypothesis.

### Mechanism-level progress

The additional-eigenvalue question now has three exact source-valid stability interfaces:

1. **arbitrary spikes + small spectral tail:** `5+r` strong physical cross directions at scale `sigma` survive `r` arbitrary-magnitude/sign eigen-directions plus an arbitrary tail of operator norm `delta<sigma`, with density cap `5e/[2(sigma-delta)]`;
2. **one arbitrary spike + small tail:** a physical definite triple of gap `L` survives one arbitrary eigen-direction plus an arbitrary tail of norm `delta<L`, with cap `C_*/(L-delta)` by the completed account03/B12 theorem;
3. **favorable-sign additions:** a physical definite pair survives arbitrary-rank Loewner-monotone additions with cap `pi/L`.

The exact construction in Section 6 shows that arbitrary large extra directions can genuinely cancel a fixed cross certificate, so the rank redundancy is not bookkeeping slack.

### First remaining full-target implication

The bare hypothesis of three global large eigenvalues still does not force either a physical definite triple or a cross block with `5+r` redundant strong directions. Known low-cross-rank star/bank families and the live correction inbox rule out such a naive exhaustive dichotomy. The remaining bridge is an **aggregate product-preserving structural decomposition** which routes the three-large spectral mass into one of the safe certificates above or into the already-proved bank/hyperbolic aggregate mechanisms, before paying inverse local conditioning constants.

That structural bridge, not the handling of extra spectral directions once a certificate exists, is now the explicit unpaid implication.
