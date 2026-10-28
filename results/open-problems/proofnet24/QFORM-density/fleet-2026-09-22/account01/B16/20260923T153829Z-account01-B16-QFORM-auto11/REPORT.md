SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T15:38:29Z.
attacking: remove the partner rank-two diagonal-side leverage gate by a capacitated Brascamp-Lieb reweighting of the actual dependent product projection, then apply the newest account02/B16 null-side theorem to a genuinely cross-coupled full-target family.

# account01/B16 — capacitated projection-product compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / NEW TARGET FAMILY / PARTNER RESULT APPLIED / FULL QFORM OPEN`  
**Regularity:** the new theorem below gives a continuous density. The partner null-side application gives essential boundedness; continuity is not claimed there.

## 1. Fresh control and pinned mathematical sources


The actual bounded-density projection and Fourier inputs used below are source-pinned at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

The two facts used are exactly:

1. every two-dimensional orthonormal projection `Z=U^T X` of independent cap-one coordinates has joint density `||p_Z||_infinity <= 2`; this does **not** assert independence of the two coordinates of `Z`;
2. for `|g|<=f<=1`, `integral |g_hat|^p <= 4 pi / sqrt(p)` for every `p>=2`, and geometric Brascamp-Lieb may be applied to translated one-dimensional arguments.

The newest completed designated-partner result consumed is

`yspennstate/math-open-problems@b84dffeb117523831ee7871e8ebee3630c14f372`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T142923Z-auto11/REPORT.md`.

Its Theorem A treats a rank-two cross block with an original-coordinate diagonal side when the canonical right singular-frame leverages are all at most `1/2`; its Theorem B treats a null side with no leverage gate and gives `2 sqrt(pi) (s_1 s_2)^(-1/2)`.

## 2. New theorem: replace canonical leverage by a capped isotropic reweighting

### `QFORM-CAPACITATED-BL-RANK2-DIAGONAL-SIDE-v1`

Partition the original coordinates into disjoint sets `I union J union K`. Condition on `X_K`. Assume

* `A_JJ=diag(d_j : j in J)` is diagonal in the ORIGINAL `J` coordinates;
* the physical cross block `M=A_IJ` has exact rank two, with thin SVD

`M = U Sigma V^T`, `Sigma=diag(s_1,s_2)`, `s_1>=s_2>0`,

where `U^T U=V^T V=I_2`;
* for each row `v_j=V_{j,*}` with `c_j=||v_j||_2^2>0`, set `e_j=v_j/sqrt(c_j) in S^1`;
* there is a subset `S subseteq {j:c_j>0}` and weights `omega_j` satisfying

`0 < omega_j <= 1/2`,

`sum_(j in S) omega_j e_j e_j^T = I_2`.                              (2.1)

No restriction is placed on `A_II`, on any block involving `K`, or on affine terms. Define

`R_omega = product_(j in S) (omega_j/c_j)^(omega_j/4)`.               (2.2)

Then the full quadratic polynomial has a continuous density and

`boxed: ||p_Q||_infinity <= 4 sqrt(2) R_omega (s_1 s_2)^(-1/2).`      (2.3)

The two coordinates of `U^T X_I` may be arbitrarily dependent.

### Proof

After conditioning `X_K=x_K`, absorb every term not involving `X_J` into an arbitrary real function `R(X_I)` and the conditioned `J`-linear term into `b`. Thus

`Q = R(X_I) + sum_(j in J) d_j X_j^2 + 2 X_I^T M X_J + b^T X_J`.     (2.4)

Put `Z=U^T X_I`. The actual product-projection theorem gives

`p_Z(z) <= 2` a.e.                                                   (2.5)

but no independence is asserted inside `Z`. Disintegrating the `I` bank over `Z`, the conditional phase contributed by `R(X_I)` has modulus at most one. Hence, for `t!=0`,

`|phi_Q(t)| <= 2 integral_(R^2) product_(j in J)
  |g_hat_j(2t <v_j,Sigma z> + t b_j)| dz`,                           (2.6)

where

`g_j(x)=exp(i t d_j x^2) f_j(x)`, `|g_j|<=f_j<=1`.                   (2.7)

Set `y=2tz` and then `x=Sigma y`. Since `det Sigma=s_1s_2`,

`|phi_Q(t)| <= [2/(4 t^2 s_1 s_2)]
 integral_(R^2) product_(j in J)
 |g_hat_j(<v_j,x>+t b_j)| dx`.                                      (2.8)

Every omitted factor is at most one because `||g_j||_1=1`, so the product may be restricted to `S`. Since `v_j=sqrt(c_j)e_j`, apply geometric Brascamp-Lieb to the unit directions `e_j` with the **new weights** `omega_j` from (2.1). For

`h_j(u)=|g_hat_j(sqrt(c_j)u+t b_j)|^(1/omega_j)`,

(2.1) gives

`integral product_(j in S) h_j(<e_j,x>)^(omega_j) dx
 <= product_(j in S) (integral h_j)^(omega_j)`.                      (2.9)

Now `1/omega_j>=2`, so the pinned Fourier lemma applies:

`integral h_j
 = c_j^(-1/2) integral |g_hat_j(v)|^(1/omega_j) dv
 <= c_j^(-1/2) 4 pi sqrt(omega_j)`.                                  (2.10)

Taking traces in (2.1) gives `sum omega_j=2`. Combining (2.9)-(2.10),

`integral_(R^2) product_(j in J)|g_hat_j(<v_j,x>+t b_j)| dx
 <= (4 pi)^2 product_(j in S)(omega_j/c_j)^(omega_j/2).`             (2.11)

Therefore

`|phi_Q(t)| <= [8 pi^2/(s_1s_2)]
 product_(j in S)(omega_j/c_j)^(omega_j/2) |t|^(-2).`                (2.12)

Let

`B = [8 pi^2/(s_1s_2)] product_(j in S)(omega_j/c_j)^(omega_j/2)`.

Together with `|phi_Q(t)|<=1`,

`integral_R |phi_Q(t)| dt <= integral_R min(1,B/t^2)dt = 4 sqrt(B)`. (2.13)

Fourier inversion yields

`||p_Q||_infinity <= (2pi)^(-1) 4 sqrt(B)
 = 4 sqrt(2) (s_1s_2)^(-1/2)
   product_(j in S)(omega_j/c_j)^(omega_j/4)`,                       (2.14)

which is (2.3). The same integrable majorant survives averaging over `X_K`, so the unconditional characteristic function lies in `L^1`; hence the full law has a continuous density. QED.

### Relation to account02/B16 Theorem A

The partner theorem is recovered by the canonical choice

`omega_j=c_j` for all `j`,

because `sum_j c_j e_j e_j^T=sum_j v_jv_j^T=I_2`. The partner gate `c_j<=1/2` is sufficient because it makes every canonical Fourier exponent `1/c_j>=2`.

The new theorem is strictly broader: the canonical weights need not be used. A row can have `c_j>1/2` provided the **directions** admit another isotropic decomposition with every selected weight at most `1/2`.

In angle coordinates `e_j=(cos theta_j,sin theta_j)`, condition (2.1) is exactly

`sum omega_j = 2`,

`sum omega_j exp(2 i theta_j)=0`,

`0<omega_j<=1/2`.                                                     (2.15)

So the remaining obstruction is a concrete capped zero-barycentre problem on the doubled-angle circle, not the canonical leverage numbers themselves.

## 3. A target-valid family outside the partner Theorem A gate

Take `I={1,2}`, `J={3,4,5,6}`, and

`V = [[sqrt(3/5),0],
      [sqrt(2/5),0],
      [0,1/sqrt(2)],
      [0,1/sqrt(2)]]`,

so `V^T V=I_2`. Let

`M=2 V^T`,

so `s_1(M)=s_2(M)=2`, and let

`D=(1/4) diag(1,-1,1,-1)`.

The canonical right-frame leverages are

`(c_1,c_2,c_3,c_4)=(3/5,2/5,1/2,1/2)`,                              (3.1)

so account02/B16 Theorem A does **not** apply because `c_1=3/5>1/2`. Theorem B does not apply either because `D!=0`.

However choose

`omega_1=omega_2=omega_3=omega_4=1/2`.                               (3.2)

The first two rows point along the first coordinate axis and the last two along the second, hence

`sum_j omega_j e_j e_j^T=I_2`.                                      (3.3)

For the six-dimensional core

`A_* = [[0_2,M],[M^T,D]]`,                                          (3.4)

Theorem (2.3) gives, for every choice of six independent cap-one input densities,

`||p_(X^T A_* X)||_infinity
 <= 2 sqrt(2) (25/24)^(1/8)
 = 2.8428967653... < 2.843`.                                        (3.5)

Indeed the reweighting factor is

`product_j (omega_j/c_j)^(omega_j/4)
 = [(5/6)(5/4)]^(1/8)=(25/24)^(1/8)`.                               (3.6)

This is a genuine member of the full target. If `D` is temporarily replaced by zero, the core has spectrum

`{2,2,0,0,-2,-2}`.

Restoring `D` is an operator-norm perturbation of size `1/4`; by Weyl, the perturbed core has two eigenvalues at least `7/4` and two at most `-7/4`. Thus it has four eigenvalues of modulus at least one.

Moreover (3.5) survives an arbitrary-dimensional outside block and arbitrary cross couplings to that outside block, because Theorem (2.3) allows arbitrary conditioned `K` blocks. The six-dimensional core remains a principal submatrix, so Cauchy interlacing preserves at least those four large eigenvalues in the full matrix.

This proves that canonical row leverage `>1/2` is not itself a real obstruction to the diagonal-side projection-product route.

## 4. Actual application of the completed account02/B16 partner result

Now apply the partner's completed null-side Theorem B to a full target family with arbitrary outside cross-coupling, not merely a direct sum.

Let `m>=4` be even. Choose balanced signs `eps_i,tau_j in {+1,-1}` and define `m x 2` matrices

`C_i=(1,eps_i)/sqrt(m)`,

`E_j=(1,tau_j)/sqrt(m)`.

Then

`C^T C=E^T E=I_2`,

and

`M_m=C E^T`

has exactly two nonzero singular values, both equal to one.

For any outside dimension `r`, arbitrary matrices `G,H in R^(m x r)`, and arbitrary symmetric `S in R^(r x r)`, define

`A_ext = [[0,   M_m, G],
          [M_m^T, 0,   H],
          [G^T, H^T,   S]]`.                                        (4.1)

For independent cap-one vectors `X in R^m`, `Y in R^m`, `Z in R^r`,

`Q_ext = 2 X^T M_m Y + 2 X^T G Z + 2 Y^T H Z + Z^T S Z`.            (4.2)

Take the partner theorem's sets `I=X`, `J=Y`, `K=Z`. The `J`-side quadratic block is exactly zero and `A_IJ=M_m` has `s_1=s_2=1`; all the `G,H,S` terms are expressly allowed after conditioning on `Z`. Therefore account02/B16 Theorem B gives the actual inequality

`boxed: ||p_(Q_ext)||_infinity <= 2 sqrt(pi)=3.5449077018...`.       (4.3)

This entire family lies inside the user's target for **every** choice of `G,H,S`. The `X,Y` principal submatrix

`[[0,M_m],[M_m^T,0]]`

has nonzero spectrum exactly

`{1,1,-1,-1}`.                                                       (4.4)

By Cauchy interlacing, the full matrix `A_ext` has at least two eigenvalues `>=1` and at least two eigenvalues `<=-1`, regardless of the outside couplings. Hence it has at least four eigenvalues of modulus at least one.

This is a direct application of a completed partner theorem to an arbitrary-higher-dimensional, genuinely cross-coupled target inequality. Continuity is not inferred because the partner's Theorem B asserted essential boundedness only.

## 5. What this changes in the proof map

The partner r29/r30 obstruction was phrased using canonical right-side leverages. The new theorem shows that the correct analytic object is instead a **capped isotropic decomposition of the whitened cross directions**. Canonical leverage failure can be harmless when directional mass is duplicated or can be reallocated.

The next unpaid B16 implication can therefore be sharpened to

`QFORM-SUPERDIFFUSE-CAPPED-ISOTROPIC-OR-CURVATURE-CLUSTER-v1`:

starting from a surviving superdiffuse/near-coloop bank cut, prove either

1. a useful rank-two diagonal-side cut has a capped isotropic decomposition (2.1) with controlled reweighting factor `R_omega`, so Theorem (2.3) pays it; or
2. failure of every such capped decomposition forces a bounded collection of heavy doubled-angle directions, and the same-side non-diagonal curvature concentrated on those source clusters supplies a source-preserving Fresnel/pair-log exit.

The second bullet is not proved here. The unrestricted QFORM conjecture therefore remains `OPEN / NOT PROVED / NOT DISPROVED`.

## 6. Integrity notes

No bounded joint projection density was inserted directly into an indefinite coarea integral. The joint projection cap `p_Z<=2` is used only before the diagonal original-source bank is integrated by Fourier/BL, where the nonlinear quadratic twists remain attached to their original independent coordinates. No post-rotation independence, no conditional projected-density cap, and no arbitrary-joint coarea lemma is used.

Continuity is tracked separately: it follows for Theorem (2.3) from the `L^1` characteristic-function majorant; it is not claimed for the partner null-side inequality (4.3).
