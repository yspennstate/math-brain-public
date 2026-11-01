SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T23:15:06Z.
attacking: the r43 same-hub curvature collar by moving the physical hub to the opposite source bank and absorbing every residual cross column before invoking the completed fleet02/B11 three-dimensional crossing theorem.

# fleet01/B11 — hub transfer and exact cross-column absorption


Status: **NEW SOURCE-PRESERVING STRUCTURAL COROLLARY / PARTNER RESULT APPLIED / UNIFORM RESIDUAL-SHEAR BRANCH / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Regularity: the new branch below has a continuous `C_0` density; full-target continuity remains open.

No Gaussianity, log-concavity, moment, compact-support, connected-support, conditional density cap, post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea theorem, or perturbative deletion of a small random term is used.

## 1. Source boundary and newest partner correction

The newest fleet02/B11 run is

`yspennstate/math-open-problems@cc0c9a6b7a942713317894ada2a2003e8fca11c5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T220048Z-fleet02-B11-qform-auto11/REPORT.md`.

It proves that merely splitting the leaves of one hub into two disjoint source banks does **not** create a third quadratic direction: the same-hub star remains rank two and can retain the logarithmic singularity. It also shows that a genuinely source-disjoint square removes that logarithm by the completed rank-two half-Riesz theorem. I retain this correction exactly; the argument below does not count two leaf banks as two hub directions.

The completed fleet02/B11 theorem actually applied below is `QFORM-3D-PROJECTION-CROSS-L2-v1`, source

`yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T201026Z-fleet02-B11-QFORM-auto11/REPORT.md`.

It states: for two disjoint original-coordinate product banks, three-dimensional orthogonal projections `U,V`, arbitrary within-bank phases, and an invertible `3 x 3` crossing matrix `C`,

`||p_Q||_infinity <= 6 |det C|^(-1/3)`,                            (1.1)

with a continuous density. The constant uses the dimension-three product-projection density cap `2^(3/2)` on each side.

The live finite-heavy reduction used for interpretation is fleet03/B11 r43,

`yspennstate/math-open-problems@d75835c958b5dcdd28649eb79af0faf3103b5d89`.

It reduces the unpaid exact-rank-three indefinite chamber to one heavy original hub with a robust but diffuse physical self-star, after scalar-pivot, strong-edge, and two-heavy-row exits have fired.

## 2. Main structural corollary: transfer the hub and absorb all remaining cross columns

### Corollary `QFORM-HUB-TRANSFER-COLUMN-ABSORPTION-v1`

Let three mutually source-disjoint collections consist of

- one product bank `Z`;
- one original scalar `X`;
- one product bank `Y`.

Let `T in R^3` be a three-dimensional orthogonal projection of `Z`. Let

`(V_1,V_2,W_1,...,W_m)`

be an orthogonal `(m+2)`-dimensional projection of `Y`; put `V=(V_1,V_2)` and `W=(W_1,...,W_m)`. Let

`B in R^(3 x 2)`, `a in R^3`, `D in R^(3 x m)`,

and suppose

`C_0 := [ B  a ] in R^(3 x 3)`

is invertible. For arbitrary measurable within-bank phases `F(Z)` and `G(X,Y)`, consider

`Q = F(Z)+G(X,Y)
     +2 T^T B V +2 X a^T T +2 T^T D W`.                            (2.1)

Then `Q` has a bounded continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity
 <= 6 { |det C_0| sqrt(det(I+K K^T)) }^(-1/3)
 <= 6 |det C_0|^(-1/3),`                                           (2.2)

where

`K=C_0^(-1)D`.                                                       (2.3)

Thus **arbitrarily many residual cross columns, of arbitrary size, cost nothing in the upper bound** once two crossing columns together with the physical hub-star column already span the three-dimensional leaf projection.

### Proof

Put

`R=(V_1,V_2,X)^T`.

Because `X` is an original coordinate disjoint from `Y`, the vector

`(R,W)=(V_1,V_2,X,W_1,...,W_m)`

is itself an orthogonal `(m+3)`-dimensional projection of the combined original product bank `(X,Y)`.

By (2.3), `D=C_0 K`, so the entire cross interaction in (2.1) is exactly

`2 T^T C_0 R +2 T^T D W
 =2 T^T C_0 (R+K W)`.                                                (2.4)

Define

`R_*:=R+K W`.                                                        (2.5)

Relative to the orthonormal source coordinates `(R,W)`, the three coefficient rows generating `R_*` form the matrix

`L=[ I_3  K ]`,

hence their Gram matrix is

`L L^T=I_3+K K^T=:H^2`.                                             (2.6)

Take the positive definite square root `H`. Then

`U:=H^(-1)R_*`                                                       (2.7)

has orthonormal coefficient rows in the **original** combined `(X,Y)` coordinate space, because

`H^(-1)L L^T H^(-1)=I_3`.                                           (2.8)

Therefore `U` is a genuine three-dimensional orthogonal projection of an independent cap-one product source, not a declaration that its coordinates are independent. Equation (2.4) becomes

`2 T^T (C_0 H) U`.                                                  (2.9)

All terms involving only `(X,Y)`, including arbitrary hub-to-right couplings, hub self-action, right-bank self-action, and interactions among `V,W,X`, remain inside the arbitrary phase `G(X,Y)`. All terms involving only `Z` remain in `F(Z)`.

Now apply the completed fleet02/B11 theorem (1.1) to the source-disjoint banks `Z` and `(X,Y)`. Since

`|det(C_0 H)|
 =|det C_0| sqrt(det(I_3+K K^T)),`                                  (2.10)

we obtain (2.2), as well as continuity and vanishing at infinity. QED.

### Important scope point

This is not a small-perturbation statement. The columns in `D` may be arbitrarily large. They are absorbed by an exact linear identity and an exact Gram normalization. The density cap of the new right projection does not increase; the expansion factor `H` instead appears beneficially in the determinant in (2.10).

## 3. Exact incidence identity and quantitative branch

If the two columns of `B` have singular values `sigma_1>=sigma_2>0` and `n` is a unit normal to `range(B)`, then

`boxed: |det C_0|=sigma_1 sigma_2 |a dot n|.`                       (3.1)

This is simply base-times-height for the three-volume `[B,a]`.

Consequently, at spectral scale `s`, if

`sigma_1 sigma_2 >= kappa s^2`,
`||a|| >= eta s`,
`|a dot n| >= tau ||a||`,                                           (3.2)

then every residual cross column is paid uniformly and

`boxed: ||p_Q||_infinity
 <= 6 (kappa eta tau)^(-1/3) / s.`                                 (3.3)

For the live r43 star scale

`eta_0=(sqrt(191)/16)(289/15984)=0.01561741219248...`,

and the inherited two-cross scale

`kappa_*=(34/111)(17/288)^2=0.001067256492604...`,

if an actual source-disjoint leaf/right two-plane satisfies

`sigma_1 sigma_2 >= kappa_* s^2`

and the robust star has incidence angle at least `tau=1/8`, then

`|det C_0| >= (kappa_* eta_0/8) s^3`

and (3.3) gives

`boxed: ||p_Q||_infinity < 469.774/s`,                              (3.4)

continuously. I do **not** assert that r43 automatically supplies this leaf-side area inequality after the heavy hub is removed; (3.4) is the exact quantitative branch once that source-valid area is present. This distinction avoids transferring a full-bank singular-value bound to a different leaf-only map without proof.

The structural gain is nevertheless decisive for the punctured-collar logic: once `[B,a]` is nondegenerate, the small third cross singular value does not need to be divided by at all. It is one of the columns in `D` and is absorbed by (2.4)-(2.10).

## 4. Genuinely rotated exact-rank-three indefinite family, uniform under arbitrary shear

The preceding corollary is not merely a high-rank crossing statement. It applies to a clean exact-rank-three family of both requested signatures.

Let `M=diag(1,1,-1)` (or its negative), let `T,R in R^3` be the coordinate vectors of two disjoint triples of independent cap-one inputs, and let `W in R^m` be further independent originals. For an arbitrary real `3 x m` matrix `K`, put

`Y=T+R+K W`,
`Q=Y^T M Y`.                                                        (4.1)

This is a genuinely rotated form in the original coordinates. Its coefficient factor is

`G=[ I_3  I_3  K ]`,

so

`G G^T=2I_3+K K^T >=2I_3`.                                         (4.2)

The three nonzero eigenvalues of the original-coordinate quadratic matrix have the same inertia as `M`; moreover their absolute values are at least `2`. Thus (4.1) is an exact-rank-three target family of signature `(2,1)` (or `(1,2)`) for every `m` and every `K`.

Split the source as left bank `T` and right bank `(R,W)`. Then

`Q=T^T M T +(R+KW)^T M(R+KW)
  +2 T^T M R +2 T^T M K W`.                                        (4.3)

Take `C_0=M`, `D=MK`. Corollary 2 gives

`||p_Q||_infinity
 <=6 det(I+K K^T)^(-1/6)
 <=boxed: 6`,                                                       (4.4)

with a continuous `C_0` density, uniformly over dimension, all cap-one input laws, and **arbitrarily large** shear `K`.

This family demonstrates the exact mechanism in the requested indefinite signatures without ever rotating the input law and pretending that eigen-coordinates are independent.

## 5. Relation to the rank-two logarithmic obstruction

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2`,                             (5.1)

so the opposite-sign rank-two saddle genuinely has unbounded density.

The completed fleet02/B11 three-dimensional crossing theorem supplies a Fourier envelope of order `|t|^(-3/2)` when there are three source-valid crossing directions. Corollary 2 identifies a new way that the **third direction can be the original physical hub-star itself**: group the hub with the opposite source bank, and the three-volume `[B,a]` becomes the third crossing determinant. Any residual shear is then absorbed before absolute values are taken. Thus the mechanism is not “a small third perturbation smooths the logarithm”; it is an exact product-provenance reorganization that preserves a genuine three-dimensional crossing.

When `det[B,a]=0`, this mechanism correctly degenerates. That is consistent with the rank-two logarithmic endpoint and with the newest fleet02/B11 warning that splitting one star into two leaf banks is not by itself a third direction.

## 6. What remains unpaid

The unrestricted conjecture remains OPEN.

For the r43 unique-heavy survivor, this run removes the residual-shear obstruction whenever a source-valid leaf-to-right rank-two plane and the hub-star column have nontrivial three-volume. The next B11 implication is therefore sharper:

`QFORM-R43-STAR-CROSS-COPLANAR-COMPILER-v1`:

> In the unique-heavy-row r43 survivor, handle the branch in which every usable leaf-to-right rank-two crossing plane has small three-volume with the hub-star coefficient vector (or the leaf crossing itself has small rank-two area). Use the exact rank-three Schur/internal-curvature structure and the two disjoint diffuse star banks to force either an overlap-safe half-Riesz square, a paid physical pair/volume exit, or another source-preserving three-direction receiver. Do not count a partition of one hub-star as two directions, condition on a dependent projection with an assumed cap, or discard a small nonzero shear.

The previously completed fleet01/B11 exact aligned endpoint remains useful when the hub direction is an exact crossing null direction; the new result attacks the complementary transverse-incidence geometry and is uniform in every additional right cross column. Arbitrary additional nonseparable spectrum beyond the exact-rank-three compression remains a separate full-target bridge.

Full QFORM: OPEN. Full continuity: OPEN. New corollary and family (4.1): continuous `C_0` density proved.
