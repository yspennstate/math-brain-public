# account01/B13 — two-bank Fresnel aggregation and disjoint exterior-mass payment

**Run:** `20260922T135910Z-account01-B13-qform-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED RANK-THREE STRUCTURAL THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains **OPEN / NOT PROVED**. The theorem below is for rank-exactly-three forms. It does not remove arbitrary additional spectral directions.

## 1. Source state and corrections consumed

Fresh control was read at `yspennstate/math-research-brain@ee4045cd9a6f3e3fcb0b3d4aa31bc18dcf0c8104` and refreshed before publication at `725d4c34bff9dfe74c2a494655fc432b3499b50d`. The live owner programme remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.

Corrections explicitly respected: law-uniform pointwise quadratic oscillatory decay is false; rotation does not preserve independence; fiber-supremum/X-ray-only arguments are insufficient; a single cross minor or Schur pivot need not close the rank-three problem; conditional cap does not replace independence; absolute phase-Wiener payment is not universal. The present argument keeps the original-coordinate product structure and performs aggregation before absolute Fourier payment.

## 2. Completed partner result actually applied

The assigned partner `account02/B13` completed the finite-direction aggregation theorem at

`yspennstate/math-open-problems@9bf04fb890e99db8ddd4e9bfd176f654bc5a82cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T125435Z-account02-B13-80c2a32d/REPORT.md`.

For rank exactly three, if the nonzero spectral-frame rows lie in at most `m` projective directions, it proves

`||p_Q||_infinity <= 2(2 pi+3 sqrt(3)) binom(m,3)`.

Its key product-preserving normalization is also used below: for any physical coordinate bank `G`, if

`S_G = sum_{i in G} r_i r_i^T`

is positive definite, then the normalized aggregate

`Z_G = S_G^{-1/2} sum_{i in G} r_i X_i`

is a genuine three-dimensional orthogonal marginal of the original product law. By the Livshyts--Paouris--Pivovarov projection theorem used in the partner report,

`||p_{Z_G}||_infinity <= 2^(3/2)`.

Hence the unnormalized bank aggregate `Y_G=sum_{i in G} r_i X_i` has density cap

`M_G <= 2^(3/2) / sqrt(det S_G)`.  (2.1)

This exact bank normalization is the partner ingredient applied in the theorem below.

## 3. Main theorem: two disjoint full-rank physical banks

Let `A=R Lambda R^T` have rank exactly three, where `R` is `n x 3`, `R^T R=I_3`, and `Lambda` is real symmetric invertible. Write `r_i in R^3` for the rows of `R`. Assume the three nonzero eigenvalues of `A` satisfy `|lambda_j|>=1`, so `|det Lambda|>=1`.

Let `G,H` be **disjoint** subsets of physical coordinates, not necessarily covering all coordinates, and set

`S_G=sum_{i in G} r_i r_i^T`,  `S_H=sum_{i in H} r_i r_i^T`.

Assume both are positive definite.

### Theorem `QFORM-RANK3-TWO-BANK-FRESNEL-v1`

For arbitrary independent real `X_i` with densities bounded by one, `Q=X^T A X` has a bounded continuous density and

`||p_Q||_infinity <= 6 |det Lambda|^(-1/3) (det S_G det S_H)^(-1/6)`.  (3.1)

In particular, under the target normalization `|lambda_j|>=1`,

`||p_Q||_infinity <= 6 (det S_G det S_H)^(-1/6)`.  (3.2)

If in addition `S_G >= alpha I_3` and `S_H >= alpha I_3`, then

`||p_Q||_infinity <= 6/alpha`.  (3.3)

### Proof

Define the independent three-dimensional bank aggregates

`Y_G=sum_{i in G} r_i X_i`,  `Y_H=sum_{i in H} r_i X_i`.

By the partner normalization (2.1), their densities `g,h` satisfy

`||g||_infinity <= M_G := 2^(3/2)/sqrt(det S_G)`,

`||h||_infinity <= M_H := 2^(3/2)/sqrt(det S_H)`.  (3.4)

Let `K` denote all remaining coordinates. Conditional on `X_K`, the residual spectral vector

`w=sum_{i in K} r_i X_i`

is fixed, and

`Q=(Y_G+Y_H+w)^T Lambda (Y_G+Y_H+w)`.

Thus it is enough to bound, uniformly in fixed `w`, the density of

`T_w=(Z+w)^T Lambda (Z+w)`,  `Z=Y_G+Y_H`.

The density of `Z` is `k=g*h`, and

`hat k(xi)=hat g(xi) hat h(xi)`.

With Fourier convention `hat g(xi)=int exp(i xi dot x)g(x)dx`, Cauchy--Schwarz and Plancherel give

`||hat k||_1 <= ||hat g||_2 ||hat h||_2`

`= (2 pi)^3 ||g||_2 ||h||_2`

`<= (2 pi)^3 sqrt(M_G M_H)`,  (3.5)

because each of `g,h` has mass one and therefore `||g||_2^2<=||g||_infinity`, `||h||_2^2<=||h||_infinity`.

For `t!=0`, the three-dimensional Fresnel transform of the nondegenerate quadratic phase has modulus

`| Fourier_y[ exp(i t (y+w)^T Lambda (y+w)) ](xi) |`

`= pi^(3/2) |t|^(-3/2) |det Lambda|^(-1/2)`.  (3.6)

The affine shift `w` changes only the phase, not this modulus. Fourier inversion in `y`, followed by (3.5), yields the conditional characteristic-function estimate

`|phi_w(t)| <= K0 |t|^(-3/2)`,

where

`K0 = pi^(3/2) |det Lambda|^(-1/2) sqrt(M_G M_H)`.  (3.7)

Of course `|phi_w(t)|<=1`, so

`|phi_w(t)| <= min(1, K0 |t|^(-3/2))`.  (3.8)

The right-hand side is integrable. Its exact integral is

`int_R min(1,K0 |t|^(-3/2)) dt = 6 K0^(2/3)`,  (3.9)

because the crossover is `|t|=K0^(2/3)`. Therefore Fourier inversion for the one-dimensional output gives a bounded continuous conditional density with

`||p_{T_w}||_infinity <= (1/(2 pi)) 6 K0^(2/3)`

`= 3 |det Lambda|^(-1/3) (M_G M_H)^(1/3)`.  (3.10)

Substituting (3.4),

`(M_G M_H)^(1/3) <= 2 (det S_G det S_H)^(-1/6)`,

which proves (3.1). The estimate is uniform in `w`, so mixing over the conditioned coordinates `X_K` preserves the same bound. QED.

## 4. Exterior-power aggregation: pay the whole disjoint channel, not one minor

For every triple `I={i,j,k}` write

`w_I = det(R_I)^2`,

where `R_I` is the `3 x 3` row submatrix. Cauchy--Binet gives

`sum_{|I|=3} w_I = det(R^T R)=1`.  (4.1)

Define the **disjoint Plucker mass**

`D_0 = sum_{|I|=|J|=3, I intersect J = empty} w_I w_J`.  (4.2)

Equivalently, if `I,J` are independent random bases sampled from the projection-DPP law `P(I)=w_I`, then

`D_0=P(I intersect J = empty)`.  (4.3)

Now color every physical coordinate independently red/blue with probability `1/2`, and let `G` and `H` be the two color classes. By Cauchy--Binet,

`det S_G = sum_I w_I 1_{I subset G}`,

`det S_H = sum_J w_J 1_{J subset H}`.

Taking expectation over the coloring,

`E[det S_G det S_H]`

`= 2^(-6) sum_{I intersect J=empty} w_I w_J`

`= D_0/64`.  (4.4)

Hence some deterministic partition satisfies

`det S_G det S_H >= D_0/64`.  (4.5)

Applying Theorem (3.1) gives:

### Corollary `QFORM-RANK3-DISJOINT-EXTERIOR-MASS-v1`

If `D_0>0`, then

`||p_Q||_infinity <= 12 |det Lambda|^(-1/3) D_0^(-1/6)`.  (4.6)

Since, for rank three,

`det A[I,J] = det(R_I) det(Lambda) det(R_J)`,

we have the exact physical-coordinate identity

`M_0 := sum_{I intersect J=empty, |I|=|J|=3} det(A[I,J])^2`

`= |det Lambda|^2 D_0`.  (4.7)

Therefore the determinant of `Lambda` cancels completely in (4.6):

`boxed( ||p_Q||_infinity <= 12 M_0^(-1/6) )`.  (4.8)

This is the key structural gain. The theorem pays the **aggregate disjoint exterior-power channel** before selecting any inverse-conditioned local minor. It is therefore not contradicted by the existing correction that one cross minor alone may be arbitrarily small.

In particular, if a fixed fraction `eta>0` of the total rank-three exterior mass lies in disjoint cross minors, i.e.

`M_0 >= eta |det Lambda|^2`,

then under `|lambda_j|>=1`,

`||p_Q||_infinity <= 12 eta^(-1/6)`.  (4.9)

Thus any rank-three sequence capable of defeating every universal bound through this channel must force `D_0 -> 0`, equivalently force two independent spectral bases to intersect with probability tending to one.

## 5. Explicit growing family beyond the max-row-leverage diffuse regime

The theorem is not merely a reformulation of the existing `max row leverage <=1/2` diffuse theorem.

Fix `N>=5`. Choose angles `theta_k` in the `e_2,e_3` plane so that the projective directions are distinct and

`sum_{k=1}^N u_k u_k^T = (N/2)(e_2 e_2^T + e_3 e_3^T)`,

where `u_k=(0,cos theta_k,sin theta_k)`; equally spaced angles with a generic phase shift do this.

Take the following spectral-frame rows:

**Bank G**

`r_0 = sqrt(7/10) e_1`,

`r_k = N^(-1/2) u_k`, `1<=k<=N`.

Then

`S_G = diag(7/10,1/2,1/2)`.  (5.1)

**Bank H**

`s_1=sqrt(3/10)e_1`, `s_2=2^(-1/2)e_2`, `s_3=2^(-1/2)e_3`,

so

`S_H = diag(3/10,1/2,1/2)`.  (5.2)

Hence `S_G+S_H=I_3`, so these rows form a valid rank-three Parseval spectral frame. The maximum physical-row leverage is `7/10>1/2`, outside the existing diffuse theorem. The number of projective row directions grows linearly with `N`, so the assigned partner's finite-direction bound grows like `binom(m,3)` on this family.

By the new theorem, however,

`det S_G det S_H = (7/40)(3/40)=21/1600`,

and therefore for every `N` and every rank-three `Lambda` with `sigma_min(Lambda)>=1`,

`||p_Q||_infinity <= 6 (1600/21)^(1/6)`

`= 12.3538227259...`.  (5.3)

Thus the new aggregation theorem gives a uniform constant on an explicit growing-direction family that lies outside the max-leverage-`1/2` branch and for which the partner's general finite-direction estimate diverges polynomially with the number of directions.

This is a direct quantitative application and strengthening of the completed `account02/B13` bank framework.

## 6. Relation to the fresh exterior-power programme

A fresh account03/B12 handoff proposes decomposing the rank-three exterior identity by overlap size `|I intersect J|=0,1,2,3`. The present result exactly closes the `|I intersect J|=0` channel whenever it carries a fixed positive amount of mass:

`M_0=sum_{I intersect J=empty} det(A[I,J])^2`  large  `=>`  density bounded by `12 M_0^(-1/6)`.

Hence the remaining rank-three structural difficulty is now concentrated in overlap-heavy frames, where the disjoint channel is small and the exterior mass lives mainly in `|I intersect J|=1,2,3`.

## 7. Exact remaining implication

The first unpaid rank-three implication is now:

> **`QFORM-RANK3-OVERLAP-HEAVY-CLOSURE-v1` (OPEN):** prove that a rank-three Parseval frame with very small disjoint Plucker mass `D_0` either falls into a product-preserving finite-bank/saturated-direction geometry already controlled by completed aggregation theorems, or admits a different original-coordinate smoothing mechanism that pays the `|I intersect J|=1,2,3` exterior channels with a universal constant.

This is strictly sharper than selecting one principal/cross minor. The disjoint aggregate has been paid exactly. The unresolved object is the overlap-heavy geometry.

After rank three is closed, arbitrary additional spectral directions remain a separate full-target issue except in already proved diffuse/regularized-determinant and principal-block scopes.

## 8. Status and integrity

- Full QFORM: **OPEN / NOT PROVED**.
- New theorem: analytic, arbitrary-sign, rank exactly three, arbitrary independent input densities `<=1`.
- It proves a bounded **continuous** density in its scope because the conditional output characteristic function is uniformly `L^1`.
- No single-interval/centered-uniform extremality is assumed.
- No pointwise law-uniform one-dimensional oscillatory decay is used.
- No rotation of the input random vector is used.
- No local inverse-minor selection is used in the aggregate corollary.
- Assigned partner `account02/B13` was consumed and applied quantitatively in Sections 2 and 5.
- Fresh account03/B12 exterior-power direction was also checked for compatibility; the present theorem pays precisely its disjoint-overlap channel.
