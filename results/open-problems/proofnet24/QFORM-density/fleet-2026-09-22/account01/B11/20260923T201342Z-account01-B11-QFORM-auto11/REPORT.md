SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T20:13:42Z.
attacking: the same-bank residual shear in the punctured indefinite double-graph collar; isolate the right-bank self-curvature obstruction, prove two product-safe analytic receivers that remain uniform in the residual shear, and apply the designated account02/B11 result to an actual target family.

# account01/B11 auto11 — rough-hub discriminant generalization and linear-right-bank collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Control revision: `2026-09-22.15`  
Status: **NEW SUPPORTING ANALYTIC THEOREMS / DESIGNATED PARTNER RESULT APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new theorems establish essential boundedness only; continuity is not claimed.

The unrestricted owner target remains OPEN. No Gaussianity, log-concavity, moment, compact-support, connected-support, post-rotation independence, law-uniform pointwise van-der-Corput estimate, arbitrary-joint coarea bound, or conditional projection-cap estimate is used.

## 1. Fresh source state and exact obstruction

The fresh designated-partner report is account02/B11,

`yspennstate/math-open-problems@a79f3268361c2368db54125eeaa3c77f9beb1871`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/account02-B11-20260923T184947Z-auto11/REPORT.md`.

It proves, among other things:

1. `QFORM-INDEFINITE-SQUARE-INDEPENDENT-SHEAR-v1`: for independent cap-one `X1,X2,Z,W`,

   `Q=2 a X1 X2+b Z^2+2 kappa ZW`, `|a|,|b|>=1`,

   satisfies

   `||p_Q||_infinity <=8*2^(1/4)|a|^(-3/4)|b|^(-1/4)`,

   uniformly in `kappa`.

2. `QFORM-R39-INDEPENDENT-RESIDUAL-SHEAR-v1`: the r39 rank-two crossing + internal-bilinear theorem is unchanged by `2 kappa zW` when `W` is genuinely source-disjoint from both active banks.

The freshest adjacent B11 source is account03/B11 r40,

`yspennstate/math-open-problems@2db0a7f81437b6e67efe800f129abebae0e10b4c`.

It proves two facts that are important here:

- throughout the true-near-coloop punctured collar the two largest crossing singular values satisfy

  `sigma1*sigma2 > kappa_* s^2`,

  where

  `kappa_*=(34/111)(17/288)^2=0.0010672564926...`;

- the naive same-bank mixed slice bridge `L^1_W(L^2_v)` is false, even for an orthogonal transform of three independent cap-one coordinates.

Thus the remaining instability is not loss of the top two crossing directions. It is the right-bank self-curvature coupled to the same product bank that generates the residual scalar.

The completed source theorem used analytically below is `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`.

For an orthonormal two-frame `P`, invertible symmetric `Lambda`, arbitrary original-coordinate affine term, and independent cap-one inputs,

`sup_t E |(P^T Z)^T Lambda(P^T Z)+b^T Z-t|^(-1/2)
 <=128 |det Lambda|^(-1/4)`.

When the affine term lies in `range(P)`, the constant improves to `16 sqrt(30)`.

A second source used below is the product-projection bound already used in account03/B11 r39: every normalized scalar projection of a cap-one product source has density cap at most `sqrt(2)`, every orthonormal two-dimensional projection has joint density cap at most `2`.

## 2. New theorem I: arbitrary 3x3 rough-hub discriminant

The account03/B06 theorem `QFORM-SAMEBANK-TRANSLATED-SQUARE-DISCRIMINANT-v1` treats a special five-parameter translated-square core. The next statement removes that parametrization completely: the three-dimensional quadratic core may be any invertible symmetric matrix with nonzero hub pivot.

### Theorem `QFORM-ROUGH-HUB-FULL3-DISCRIMINANT-v1`

Let `X` be a scalar random variable with probability density bounded by `L_X`. Let

`Z=(Z_1,...,Z_m)`

have independent coordinates, each with density at most one. Let `W` be an auxiliary source independent of `(X,Z)`. Let `u,v in R^m` be linearly independent and put

`U=u.Z`, `V=v.Z`,

`G=det Gram(u,v)>0`.

Let

`Y=gamma X+H(Z,W)`, `gamma!=0`,

where `H` is completely arbitrary measurable. Let

`M=[[a,c^T],[c,B]]`

be a real symmetric `3x3` matrix in the coordinates `(Y,U,V)`, with

`a!=0`, `det M!=0`.

Let `eta(W)` be any real measurable function, `ell(W) in R^m` any measurable vector, and `R(W)` any measurable real function. Define

`Q=(Y,U,V)^T M (Y,U,V)+2 eta(W)Y+ell(W).Z+R(W)`.

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=128 (L_X/|gamma|)
       [ |a det M| G ]^(-1/4).`                                    (2.1)

If almost surely `ell(W) in span{u,v}`, then

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(30) (L_X/|gamma|)
       [ |a det M| G ]^(-1/4).`                                    (2.2)

No bound depends on `H`, `eta`, `R`, or the support/fragmentation of the input laws.

### Proof

Fix `(Z,W)=(z,w)` and a target `t`. The conditional variable

`Y=gamma X+H(z,w)`

has density bounded by

`L_Y=L_X/|gamma|`.

Write `r=(U,V)^T`. The equation `Q=t` is

`aY^2+2(c^T r+eta)Y+r^TBr+ell.Z+R=t`.

Its discriminant divided by four is

`Dscr=(c^T r+eta)^2+a[t-r^TBr-ell.Z-R]`.                           (2.3)

At every simple root the derivative magnitude is `2 sqrt(Dscr)`. Summing the two root contributions gives

`p_(Q|Z,W)(t|z,w)
 <=L_Y 1_{Dscr>0} Dscr^(-1/2)
 <=L_Y |Dscr|^(-1/2).`                                             (2.4)

The quadratic part of `Dscr` in `r` is

`N=cc^T-aB`.                                                        (2.5)

The key exact identity is

`boxed: det N = a det M.`                                          (2.6)

Indeed,

`N=-a(B-cc^T/a)`,

and because the transverse dimension is two,

`det N=a^2 det(B-cc^T/a)=a det M`.

Choose an orthonormal physical frame `P` spanning `span{u,v}`. If `T` is the `2x2` coefficient matrix satisfying

`(U,V)^T=T P^T Z`,

then

`det(T)^2=G`.

Therefore the determinant of the rank-two quadratic part of `Dscr` in the orthonormal coordinates `P^T Z` is exactly

`boxed: det Lambda = a det M G.`                                   (2.7)

All remaining terms in (2.3) are affine in the original coordinates `Z`, plus a scalar shift depending on `(t,w)`. Apply `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` to (2.4), uniformly in `w` and `t`, and then average in `W`. This gives (2.1). If `ell(W)` lies in `span{u,v}`, every affine term in the discriminant lies in the rank-two projection range and the improved `16 sqrt(30)` half-Riesz constant gives (2.2). QED.

### Exact relation to the earlier translated-square theorem

For

`delta0 Y^2+2k UY+beta(V+theta Y+zeta U)^2`,

one has

`a=Delta=delta0+beta theta^2`,

and a direct determinant calculation gives

`det M=-beta k^2`.

Thus (2.1) becomes exactly

`128 (L_X/|gamma|)[k^2 |beta Delta| G]^(-1/4)`,

recovering account03/B06's special theorem. The new content is that no translated-square normal form is needed: only the invariant pair `a` and `det M` survive the scalar root calculation.

### Why the theorem stops exactly at the hard null pivot

If `a=0`, the scalar equation is linear in `Y` and the Jacobian becomes proportional to

`1/|c^T r+eta|`.

That singularity lives on a line in the two-dimensional `r` plane and is logarithmically nonintegrable under a mere density cap. This is the same endpoint seen in the rank-two opposite-sign benchmark. The theorem therefore does not hide the null-pivot problem; it identifies it algebraically.

## 3. New theorem II: rank-two crossing with a same-bank residual shear and no right self-curvature

The next theorem is simpler but directly isolates what the account02/account03 collar results leave unpaid.

### Theorem `QFORM-RANK2-CROSS-LINEAR-RIGHTBANK-v1`

Let `Xsrc` and `Ysrc` be independent source objects. Assume `Ysrc` is a product of independent scalar variables with densities at most one. Let

`u in R^2`

be any two-dimensional statistic of `Xsrc` having density cap `M_2`. Let `z=z(Xsrc)` be arbitrary. Let `(v,W)` be a three-dimensional orthonormal projection of `Ysrc`, with `v in R^2`, `W in R`. Let `S` be an invertible real `2x2` matrix. Let `kappa` be arbitrary, let `H_X(Xsrc)` be arbitrary measurable, and let `h.Ysrc+c` be an arbitrary affine function of the right source. Put

`Q=H_X(Xsrc)+2 u^T S v+2 kappa z W+h.Ysrc+c`.                      (3.1)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=2 sqrt( pi M_2 / |det S| ).`                                    (3.2)

The bound is completely uniform in `kappa`, in `z`, in `H_X`, and in the affine right-bank term.

### Proof

Condition on the entire left source `Xsrc`. The right-bank random part is one scalar linear form in the original independent coordinates `Ysrc`. Let `V_3` denote the orthonormal coefficient frame generating `(v,W)`. The coefficient vector of that scalar linear form is

`2 V_3 (Su,kappa z)+h`.

Decompose `h=V_3(a,b)+h_perp`, with `a in R^2`, `b in R`, and `h_perp perpendicular to range(V_3)`. Hence its Euclidean norm is at least

`|2Su+a|`.

The one-dimensional product-projection theorem gives density cap at most

`sqrt(2)/|2 V_3(Su,kappa z)+h|
 <=(1/sqrt(2)) |Su+a/2|^(-1).`                                    (3.3)

Thus

`||p_Q||_infinity
 <=(1/sqrt(2)) E |Su+a/2|^(-1).`                                  (3.4)

The random vector `Y=Su+a/2` has a two-dimensional density bounded by

`K=M_2/|det S|`.

For every probability density `p<=K` on `R^2` and every center `y0`,

`int p(y)/|y-y0| dy
 <=2 pi K R +1/R`

for every `R>0`: use the density cap on the disk and total mass outside. Optimizing at

`R=(2 pi K)^(-1/2)`

gives

`int p(y)/|y-y0| dy <=2 sqrt(2 pi K)`.                              (3.5)

Combining (3.4)-(3.5) proves (3.2). QED.

### Geometric interpretation: why two crossing directions beat the logarithm

For a single crossing coordinate, conditioning produces `1/|x|` and averaging against a one-dimensional density gives the familiar logarithmic divergence. Here the coefficient lives in the two-dimensional plane `Su`; the singular kernel is `1/|Su|`, and

`int_{|u|<epsilon} |u|^(-1) du ~ epsilon`

is locally integrable. The extra direction is exactly the codimension gain that removes the rank-two logarithm in this branch.

This argument never conditions on `W`, never invokes a conditional density of `v`, and is therefore untouched by the account03/B11 r40 `L^1_W(L^2_v)` counterexample.

## 4. Designated account02/B11 result applied at actual inequalities

### 4.1 Independent-square collar

Apply account02/B11 `QFORM-INDEFINITE-SQUARE-INDEPENDENT-SHEAR-v1` with `a=b=1`. For every four independent cap-one inputs and every real `kappa`,

`boxed:
 ||p_(2X1X2+Z^2+2 kappa ZW)||_infinity
 <=8*2^(1/4)
 =9.513656920... .`                                                (4.1)

This family is target-valid for every `kappa`; at `kappa=0` its nonzero signature is `(+,+,-)`.

### 4.2 Sharpening the partner's rank-two-crossing collar family

The same partner report proves that

`Q_kappa=2ZX1+2X1Y1+2X2Y2+2 kappa ZW`                              (4.2)

is target-valid for every `kappa` and obtains a continuous-density bound `<13` by the r39 dyadic theorem.

Apply Theorem 3.1 instead. Here

`u=(X1,X2)`, `S=I_2`, `z=Z`, `(v,W)=(Y1,Y2,W)`,

and because `X1,X2` are themselves independent cap-one original coordinates,

`M_2<=1`.

Therefore

`boxed:
 ||p_(Q_kappa)||_infinity
 <=2 sqrt(pi)
 =3.544907701811... ,`                                             (4.3)

uniformly in `kappa`.

This is a strict height improvement over the partner's `<13` estimate for this actual target-valid same-bank-shear family. I do **not** infer continuity from (4.3); the partner's Fourier proof supplies continuity for (4.2), while the new conditional-linear proof only gives essential boundedness.

## 5. Why Theorem 3.1 does not falsely close the punctured exact-rank-three collar

For an exact-rank-three form, compress a partition `(H,T)` to its three-dimensional spectral images. Write the compressed matrix as

`A_comp=[[C,B],[B^T,D]]`.

If the punctured collar has `rank(B)=3`, then both side spectral maps have full rank and `C` is invertible. Since the full compressed matrix still has rank three, its Schur complement is exactly zero:

`boxed: D=B^T C^(-1) B.`                                          (5.1)

Consequently `D` cannot vanish when `B` is invertible. Thus the hypothesis of Theorem 3.1 — no right-bank quadratic self-curvature beyond affine terms — is not the generic punctured exact-rank-three survivor. This is a structural reason, not merely a proof-technical caution.

Equation (5.1) also identifies the correct remaining analytic problem: the right self-curvature is not arbitrary, but it is tied quadratically to the same small third crossing direction. A proof uniform as the third singular value tends to zero must exploit this Schur compatibility, rather than delete the self-curvature or condition on the same-bank residual scalar.

## 6. Quantitative use of the r40 top-two crossing currency

Although Theorem 3.1 does not by itself close the exact-rank-three collar, it pays any branch in which the right-bank self-action has been removed legitimately by an original-source decomposition. Indeed, account03/B11 r40 gives

`sigma1*sigma2>kappa_* s^2`,

and the product-projection theorem gives `M_2<=2`. Hence, whenever the right-bank contribution is genuinely affine after an allowed source-disjoint conditioning,

`||p_Q||_infinity
 <=2 sqrt(2 pi/kappa_*) / s
 <153.457/s.`                                                       (6.1)

No reciprocal third singular value appears.

This is a useful endpoint certificate, but (5.1) shows exactly why an additional argument is needed before applying it to the full punctured exact-rank-three collar.

## 7. Rank-two logarithmic control retained

For centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`.

Thus two opposite-sign directions alone remain unbounded. The new mechanisms remove that singularity in two distinct ways:

- Theorem 2.1: a nonzero hub pivot converts the scalar-root discriminant into an invertible rank-two half-Riesz receiver with determinant `a det(M) G`.
- Theorem 3.1: two genuine crossing directions produce an integrable `1/|u|` kernel in a two-dimensional coefficient plane, uniformly in the residual shear.

Neither mechanism asserts independence after rotation.

## 8. Precise remaining B11 implication

The first unpaid implication is now

`QFORM-SCHUR-COMPATIBLE-SAMEBANK-COLLAR-v1`:

> In the punctured exact-rank-three normal form with `sigma1*sigma2` uniformly bounded below and `D=B^T C^(-1)B`, prove a universal bound uniform as `sigma3(B)->0`, retaining the product provenance of both source banks; or reduce by an original-coordinate cut to the affine-right-bank branch (3.1) or another already-paid receiver.

The remaining singular endpoint must allow a zero or arbitrarily small hub pivot, arbitrary fragmented/unbounded cap-one laws, and the same-bank residual scalar. The r40 mixed-slice counterexample rules out naive `W`-conditioning, while (5.1) rules out simply dropping the right self-curvature. Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner target.

## 9. Constants checked

With

`kappa_*=(34/111)(17/288)^2`,

`2 sqrt(2 pi/kappa_*)=153.4565842398...`.

For the partner family (4.2), Theorem 3.1 gives

`2 sqrt(pi)=3.544907701811...`.

The accompanying verifier records these constants and checks the determinant identities used above.

Full QFORM status: **OPEN**. Continuity for the new theorems: **not proved**.
