SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-23T11:39:53Z.
attacking: projection-product interaction at the remaining shared-bank/null-Rayleigh transition; first isolate how far the completed fresh-bank transducer survives arbitrary higher-rank cross coupling without reintroducing conditional projection caps.

# fleet01/B16 — cross-coupled full-ambient lift of the aggregated fresh-bank receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** projection-product interaction  
**Run:** `20260923T113953Z-fleet01-B16-QFORM-r12`  
**Status:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Regularity:** absolute continuity and an essential `L^infinity` bound are proved in the stated classes; continuity is not proved here.

## 1. Inputs actually used

The analytic source is the completed rank-two affine half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

together with the already checked source-preserving translated-square consequence from fleet01/B16

`yspennstate/math-open-problems@ab9eee0f982c189620b67212476538c53db2ea60`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T094106Z-fleet01-B16-QFORM-projprod/REPORT.md`.

For disjoint original source banks `I,J`, `Y=M X_I in R^2`, `Z=n^T X_J`, an invertible symmetric `2 x 2` matrix `B`, `gamma!=0`, an arbitrary affine vector `d` on the entire `I` bank, and an arbitrary same-bank measurable shift `h(X_I)`, that theorem gives

`||p_[Y^T B Y+d^T X_I+c+gamma(Z+h)^2]||_infinity
 <= 128 sqrt(2)/(||n|| sqrt(|gamma|))
    [det(MM^T)|det B|]^(-1/4)`.                              (1.1)

If `d` lies in the row span of `M`, the constant `128 sqrt(2)` in (1.1) is replaced by `16 sqrt(60)` after the same normalization. This uses the genuine one- and two-dimensional bounded-density projection theorems before the nonlinear square integration. The two coordinates of `M X_I` are never declared independent.

The designated partner actually consumed in this run is fleet02/B16

`yspennstate/math-open-problems@ade5cfe51d454341667779f7d9da714e4de99ed9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T103259Z-fleet02-B16-078f791ea823/REPORT.md`.

It proves `QFORM-BANK-AGGREGATED-FRESH-SQUARE-N3-v1`, including the target-valid family and the sharp supplied inequality `||p_Q||_infinity<=4` described below. Its pinned receiver is fleet03/B16 `QFORM-DEPENDENT-PAIR-FRESH-SQUARE-SIGNFREE-v1` at `math-open-problems@4388eeb12a94dd167f305554419fd4c986eda04a`; that theorem explicitly permits arbitrary deterministic affine terms in its three aggregate variables.

## 2. A full-ambient conditional-affine closure

### Theorem `QFORM-FRESH-BANK-FULL-AMBIENT-CROSS-LIFT-v1`

Let `I,J,K` be disjoint sets of original coordinates. Let

`P=M X_I in R^2`, `V=n^T X_J`,

where `rank M=2` and `n!=0`. Let `B` be invertible symmetric `2 x 2`, `gamma!=0`, let `R` be an arbitrary `|I| x |K|` matrix, let `a in R^|I|`, `r in R^|K|`, and let `C` be arbitrary symmetric on the outside bank. Define

`Q = P^T B P
     + 2 X_I^T R X_K
     + gamma [V+a^T X_I+r^T X_K]^2
     + X_K^T C X_K`.                                        (2.1)

Then

`boxed:
 ||p_Q||_infinity
 <= 128 sqrt(2)/(||n|| sqrt(|gamma|))
    [det(MM^T)|det B|]^(-1/4).`                              (2.2)

If every column of `R` lies in the row span of `M` (equivalently `R=M^T S` for some `S`), then

`boxed:
 ||p_Q||_infinity
 <= 16 sqrt(60)/(||n|| sqrt(|gamma|))
    [det(MM^T)|det B|]^(-1/4).`                              (2.3)

### Proof

Condition only on the genuine outside original-coordinate bank `X_K=z`. The remaining `I` and `J` banks stay independent product sources. The conditional form is

`P^T B P + d_z^T X_I+c_z
 + gamma[V+h_z(X_I)]^2`,

with

`d_z=2Rz`, `h_z(X_I)=a^T X_I+r^T z`.

Equation (1.1) applies uniformly in `z`. The arbitrary shared-source shift `h_z` is removed only after conditioning on the genuinely disjoint `J` bank; no conditional density of `P`, no normalized conditional projection height, and no post-rotation independence are introduced. Averaging the conditional laws proves (2.2). If `R=M^T S`, then `d_z` belongs to the row span of `M` for every `z`, so the sharper row-span half-Riesz constant gives (2.3). QED.

The point is structural: arbitrary outside quadratic terms and arbitrary outside couplings into every coordinate of the dependent two-dimensional receiver bank are free once one exact disjoint scalar bank remains reserved for the square. The fresh scalar may also carry an arbitrary same-receiver-bank linear shift `a^T X_I` inside its square.

## 3. Apply the designated fleet02/B16 result to a genuinely cross-coupled target family

Use the partner's balanced construction. Let `m` be divisible by four and let

`L=m^(-1/2) sum X_j`,
`U=m^(-1/2) sum eps_j X_j`,
`T=m^(-1/2) sum tau_j X_j`,
`V=m^(-1/2) sum Z_j`,
`H=eta(L+rho T)`, `Y=X_0+H`,

with `eta^2(1+rho^2)<1/63`, `0<delta<=1/16`. Put

`s^2=1+eta^2(1+rho^2)`.

The coefficient vectors of `Y/s`, `U`, `V` are orthonormal original-coordinate vectors, but their projected coordinates are not asserted independent. Fleet02/B16 proves for

`Q_0=4 delta Y^2+8YU+4V^2`                                  (3.1)

that

`||p_(Q_0)||_infinity<=4`.                                   (3.2)

Now add a completely new disjoint outside product bank `Z_out in R^q`. Write `S=(Y,U,V)`. For arbitrary real `3 x q` matrix `G` and arbitrary symmetric `C`, define the non-block-diagonal quadratic form

`Q_cross = S^T B_delta S + 2 S^T G Z_out + Z_out^T C Z_out`,  (3.3)

where

`B_delta=4[[delta,1,0],[1,0,0],[0,0,1]]`.

Conditioning on `Z_out=z` adds only the deterministic affine term `2(Gz)^T S`. The sign-free receiver used by fleet02/B16 explicitly allows arbitrary deterministic affine terms in `(Y,U,V)`, with the same source caps

`L_X=1`, `L_U<=sqrt(2)`, `L_V<=sqrt(2)`.

Its quantitative bound is

`2^(13/4) L_V sqrt(L_X L_U) (|b det B_delta|)^(-1/4)`.

Here `b=4`, `det B_delta=-64`, so `|b det B_delta|=256`; hence for every outside realization

`||p_(Q_cross | Z_out=z)||_infinity <=4`.

Averaging gives the actual inequality

`boxed: ||p_(Q_cross)||_infinity <=4`.                        (3.4)

This is not a convolution-only extension: `G` is arbitrary, so the extra coordinates may couple bilinearly to all three active aggregate directions.

### Target verification survives arbitrary `G,C`

Let `y,u,v` be the physical coefficient vectors of `Y,U,V`. On the orthonormal three-dimensional subspace

`E=span{y/s,u,v}`

the compression of the full coefficient matrix of (3.3) is exactly

`Gamma=4[[delta s^2,s,0],[s,0,0],[0,0,1]]`.                  (3.5)

The outside cross terms vanish under compression to `E`. The partner calculation gives one eigenvalue `4`, a positive eigenvalue at least `4s>=4`, and a negative eigenvalue whose modulus is at least

`4s/(1+delta s)>1`.                                           (3.6)

By the min-max/Poincare separation principle, the full symmetric matrix therefore has at least two eigenvalues `>=1` and at least one eigenvalue `<=-1`, regardless of `q,G,C`. Hence every form in (3.3) is genuinely inside the owner's three-large-eigenvalue target class.

Thus the completed fleet02/B16 result lifts to arbitrary ambient dimension and arbitrary nonseparable outside coupling along the whole active three-dimensional aggregate space, with the same density bound `4`.

## 4. Allow arbitrary outside coupling into every shared/hub source coordinate

There is a larger family for which the sharp `4` receiver no longer directly applies but (2.2) does. Let `X_I=(X_0,X_1,...,X_m)`, let the fresh bank still enter through its normalized aggregate `V`, and take arbitrary

`R in R^{(m+1) x q}`, `r in R^q`, `C=C^T`.

Define

`Q_wide = Q_0 + 2 X_I^T R Z_out + 2V r^T Z_out + Z_out^T C Z_out`. (4.1)

Conditioning on `Z_out=z` makes `2X_I^TRz` an arbitrary affine term across the entire shared/hub bank. Complete the fresh term:

`4V^2+2V r^Tz = 4[V+(r^Tz)/4]^2-(r^Tz)^2/4`.                (4.2)

Use

`P=(Y/s,U)`,
`M M^T=I_2`,
`B=4[[delta s^2,s],[s,0]]`,
`|det B|=16s^2`,
`gamma=4`, `||n||=1`.

The general affine estimate (2.2) gives, uniformly in `z`,

`||p_(Q_wide | Z_out=z)||_infinity
 <= 128sqrt(2)/2 * (16s^2)^(-1/4)
 = 32sqrt(2)/sqrt(s)`.                                        (4.3)

Therefore

`boxed:
 ||p_(Q_wide)||_infinity
 <= 32sqrt(2)/sqrt(s)
 <= 32sqrt(2)
 =45.2548339959... .`                                         (4.4)

The same compression argument as in Section 3 shows that every matrix in (4.1) remains in the three-large-eigenvalue target class. Thus the fresh-bank certificate tolerates **arbitrary cross coupling from every original coordinate in the dependent shared/hub bank to an arbitrary-dimensional outside block**, at a still-universal cost below `46`.

If the columns of `R` happen to lie in the aggregate row span of `(Y/s,U)`, (2.3) instead gives

`||p_(Q_wide)||_infinity <=4sqrt(60)/sqrt(s)<=30.98386677...`,

although the affine-uniform sign-free receiver in Section 3 is sharper (`4`) when the coupling factors entirely through `(Y,U,V)`.

## 5. What this resolves and what it does not

The new result removes one part of the arbitrary-higher-rank interface. An exact disjoint normalized fresh bank does not have to sit in a block-diagonal component: arbitrary outside quadratic structure is allowed, arbitrary outside coupling to the whole dependent shared/hub bank is allowed, and arbitrary outside coupling to the fresh bank **through its aggregate scalar direction** is allowed. Product aggregation occurs before the inverse-square-root singularity is paid.

The next unpaid B16 implication is more precise:

`QFORM-FRESH-BANK-TRANSVERSE-AFFINE-OR-SHARED-NULL-v1`.

The theorem above does not yet permit the outside block to couple to directions of the fresh source bank orthogonal to the reserved aggregate scalar `V`; after conditioning outside, that would create an arbitrary affine term throughout the same bank carrying the rank-one square. Nor does it create an exact disjoint fresh bank in the genuinely shared/null-Rayleigh near-coloop geometry. Those are now the two analytic/structural boundaries. A bare joint projection-density cap is still insufficient, so neither boundary can be crossed by arbitrary-joint coarea or normalized conditional projection heights.

Global QFORM remains open. Continuity for (3.3) and (4.1) is not proved by this argument; the conclusion here is absolute continuity with the displayed essential bounds.
