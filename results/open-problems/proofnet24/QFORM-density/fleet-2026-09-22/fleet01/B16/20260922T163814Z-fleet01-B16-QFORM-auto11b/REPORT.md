# fleet01/B16 — conditional-projection shortcut refuted; product-preserving two-isotropic-row trace

**Run:** `20260922T163814Z-fleet01-B16-QFORM-auto11b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control used:** revision `2026-09-22.8`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / REFUTED INTERMEDIATE ROUTE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and live correction discipline

The full target remains OPEN: for arbitrary independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension-independent finite bound on the density of `Q=X^T A X`. Continuity is separate.

The revision-8 owner message proposes a rank-three coarea/conditional-projection route. Two distinct implications in that shortcut are false under the exact target hypotheses:

1. an arbitrary bounded three-dimensional density does **not** have a universally bounded indefinite rank-three quadratic pushforward merely from its `L^infinity` norm;
2. even for an actual orthogonal projection of a cap-one product density, the conditional three-dimensional projection density given the orthogonal complement has no universal essential-supremum cap.

These failures are consistent with the already-live corrections `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`. They do not refute the QFORM conjecture. The replacement mechanism below keeps original product provenance through the nonlinear integration.

The designated completed partner used substantively is **fleet02/B16**, run `20260922T153609Z-fleet02-B16-QFORM-auto11`, canonical report

`yspennstate/math-open-problems@85c527c3172670ca9e6200138e1364be554413ac`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T153609Z-fleet02-B16-QFORM-auto11/REPORT.md`.

Its determinant-scaled binary Frostman theorem and inverse-square-root potential bound are used in Section 4. Its earlier product-log envelope from the zero-diagonal triple run, canonical report

`yspennstate/math-open-problems@f1de723dfb00adf76b4a6e73f2336c47676cb6bc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T142906Z-fleet02-B16-QFORM-auto12/REPORT.md`,

is used in Section 5.

## 2. First falsifier: bounded 3D density does not imply bounded indefinite rank-three trace

Let

`q(y)=y_1^2+y_2^2-y_3^2`.

Fix `0<delta<=1/2` and put

`L_delta=(2 pi delta)^(-1)`.

In cylindrical coordinates `(r,theta,z)` define

`E_delta={ y : -1-delta <= q(y) <= -1+delta,  2<=z<=2+L_delta }`.

For every point in these coordinate ranges,

`r^2=z^2+q >=4-(1+delta)>0`,

so the change of variables

`s=q=r^2-z^2`, `theta=theta`, `z=z`

is valid throughout. Since `ds=2r dr`, Euclidean volume is

`dy=r dr dtheta dz=(1/2) ds dtheta dz`.

Hence

`|E_delta|=(1/2)(2delta)(2pi)L_delta=1`.

Therefore

`rho_delta=1_{E_delta}`

is a probability density with

`||rho_delta||_infinity=1`.

But the pushforward density of `q` is exactly

`p_delta(s)=pi L_delta=1/(2delta)`

for every `s in[-1-delta,-1+delta]` and zero outside that band. Thus

`||p_delta||_infinity=1/(2delta) -> infinity`.

### Consequence

There is no universal constant `C_0` such that

`||p_{q(Y)}||_infinity <= C_0 ||rho_Y||_infinity`

for arbitrary probability densities `rho_Y` on `R^3`, even for the normalized signature `(2,1)` form. The noncompact hyperboloid direction defeats the naive coarea estimate. A proof for QFORM must use more than a bounded 3D marginal density; it must retain product-projection provenance or an equivalent stronger trace statistic.

This is an information-loss counterexample only. `rho_delta` is not claimed to be an orthogonal marginal of a cap-one product law.

## 3. Second falsifier: the conditional 3D projection cap is false for an actual product law

Let `X_1,X_2,X_3,X_4` be iid `Uniform[0,1]`, each with density cap one. Define the orthogonal coordinates

`Y_1=(X_1+X_2)/sqrt(2)`,
`Z=(X_1-X_2)/sqrt(2)`,
`Y_2=X_3`,
`Y_3=X_4`.

The joint density of `(Y_1,Z)` is the indicator of the rotated unit square. For

`|z|<1/sqrt(2)`,

the section in `Y_1` is

`|z| <= Y_1 <= sqrt(2)-|z|`,

of length

`ell(z)=sqrt(2)-2|z|`.

Therefore

`p_Z(z)=ell(z)`

and, for almost every such `z`,

`p_{Y_1|Z=z}(y)=1/ell(z)`

on that interval. Since `Y_2,Y_3` are independent uniforms independent of `(Y_1,Z)`,

`||p_{(Y_1,Y_2,Y_3)|Z=z}||_infinity=1/ell(z)`.

As `|z| -> 1/sqrt(2)`, this tends to infinity. For every finite `M`, the set of `z` with `1/ell(z)>M` has positive `Z`-probability. Hence the essential supremum of the conditional three-dimensional density cap is infinite.

Now take the exact target matrix whose spectral coordinates are `(Y_1,Y_2,Y_3,Z)` and whose eigenvalues are

`(1,1,-1,0)`.

Then

`Q=Y_1^2+Y_2^2-Y_3^2`

has exactly three eigenvalues of modulus one. Thus the failure above occurs inside the exact target geometry. It refutes the proposed universal conditional-projection cap, not QFORM itself.

## 4. Apply the designated partner: the same target example is uniformly paid without conditional projection

The preceding target example is harmless when the original product aggregation is preserved.

The scalar aggregate `Y_1=(X_1+X_2)/sqrt(2)` is independent of `Y_3=X_4`, and the sharp one-dimensional product-marginal theorem gives

`||p_{Y_1}||_infinity <= sqrt(2)`.

Put

`R=Y_1^2-Y_3^2`.

Apply fleet02/B16's completed `QFORM-INDEFINITE-BINARY-FROSTMAN-v1` after the standard density-cap scaling. Its inverse-square-root consequence says that for independent input caps `K_1,K_2` and binary determinant `D<0`,

`sup_t E |t-R|^(-1/2)
 <= C_ind sqrt(K_1 K_2) |D|^(-1/4)`,

where

`C_ind=8*3^(3/4)*5^(1/4)/sqrt(e)
      =16.53964516612327...`.

Here `K_1=sqrt(2)`, `K_2=1`, and `D=-1`, so

`sup_t E |t-R|^(-1/2) <= 2^(1/4) C_ind`.

Since `Y_2=X_3` is independent of `R` and has density cap one, the usual square pushforward bound gives, for almost every `t`,

`p_Q(t)
 <= E |t-R|^(-1/2)`.

Consequently

`boxed( ||p_Q||_infinity <= 2^(1/4) C_ind < 19.670 ).`

This is an actual use of the designated partner theorem on the same product-law target example that destroys the conditional-projection shortcut. The difference is exactly provenance: aggregate first in original independent variables, then apply the nonlinear square kernel.

## 5. New replacement theorem: two physical isotropic rows plus the genuine projection cap

The preceding falsifiers show that one cannot discard product structure and keep only a projected density cap. The next theorem gives a source-preserving rank-three trace in a nontrivial overlapping geometry.

### Theorem `QFORM-RANK3-TWO-ISOTROPIC-ROWS-PRODUCT-TRACE-v1`

Let

`A=U Lambda U^T`, `U^T U=I_3`,

have exact rank three, with `Lambda` real symmetric and invertible. Let `u,v` be two distinct physical rows of `U` such that

`u^T Lambda u=0`,
`v^T Lambda v=0`,

and assume they are linearly independent. Put

`Delta=||u wedge v||_2`.

For independent original coordinates with densities bounded by one,

`boxed(
 ||p_{X^T A X}||_infinity
 <= 12 e^(-1/3)
    ( |det Lambda| Delta^2 )^(-1/3).
 )`

In particular, under the exact-rank-three target normalization `|lambda_j|>=1`,

`||p_Q||_infinity <= 12 e^(-1/3) Delta^(-2/3)`.

No independence is asserted after spectral rotation, and no conditional projected-density cap is used.

### Proof

Let the physical coordinates corresponding to `u,v` be `X_i,X_j`; write the remaining spectral aggregate as

`Z_0=sum_{k notin{i,j}} u_k X_k in R^3`.

Choose a unit Euclidean vector `n` normal to `span{u,v}`. Since the rows of `U` are a Parseval frame,

`sum_k u_k u_k^T=I_3`.

Thus

`L=n^T Z_0=sum_{k notin{i,j}} (n^T u_k) X_k`

has coefficient-vector norm exactly one:

`sum_{k notin{i,j}} (n^T u_k)^2=1`.

By the sharp one-dimensional product-marginal theorem (Livshyts--Paouris--Pivovarov, as already source-transferred in the QFORM archive),

`||p_L||_infinity <= K:=sqrt(2)`.                                      (5.1)

Every `Z_0` decomposes uniquely as

`Z_0=s_1 u+s_2 v+Ln`,

where `s_1,s_2` are measurable linear functions of the remaining original coordinates. Put

`C=[u v n]` and `M=C^T Lambda C`.

Because the first two rows are isotropic,

`M_[1:2,1:2]=[[0,b],[b,0]]`,

where `b=u^T Lambda v`. Since a nondegenerate real three-dimensional form has Witt index one, two linearly independent isotropic vectors cannot be mutually orthogonal for the bilinear form; hence `b!=0`.

Write

`M=[[B,m],[m^T,d_0]]`,
`B=[[0,b],[b,0]]`.

Complete the square only in the first two coordinates. Conditional on all original coordinates except `X_i,X_j`, this merely translates `X_i,X_j`; their conditional laws remain independent and density-capped by one. We obtain the exact identity

`Q=2b U_* V_* + kappa L^2`,                                         (5.2)

where `U_*,V_*` are translates of the original independent variables `X_i,X_j` by functions of the remaining coordinates and

`kappa=d_0-m^T B^(-1)m`.

The determinant identity gives

`|b|^2 |kappa|
 =|det M|
 =|det C|^2 |det Lambda|
 =Delta^2 |det Lambda|=:D_3`.                                      (5.3)

Now use fleet02/B16's source-exact product envelope. For any two independent cap-one variables (and hence for arbitrary deterministic translates of them),

`p_{2bUV}(s)
 <= (2/|b|)
    log(1+sqrt(|b|/(2|s|)))`.                                      (5.4)

Conditioning on the remaining original coordinates and then averaging therefore yields

`p_Q(t)
 <= (2/|b|)
 E log(1+A/sqrt(|t-kappa L^2|)),`                                  (5.5)

with

`A=sqrt(|b|/2)`.

It remains to integrate this curved logarithm against the genuine product projection `L`; this is where the actual projection theorem is used.

For `y>0`,

`log(1+A/sqrt(|t-kappa L^2|))>y`

implies

`|t-kappa L^2|
 < |b|/[2(e^y-1)^2]`.

For every interval `J` of length `H`,

`|{l:kappa l^2 in J}|
 <=2 sqrt(H/|kappa|)`.

Together with (5.1), this gives

`P( log(1+A/sqrt(|t-kappa L^2|))>y )
 <= min(1, x/(e^y-1))`,                                            (5.6)

where

`x=2K sqrt(|b|/|kappa|)`.

Layer cake gives the exact elementary function

`E log(1+A/sqrt(|t-kappa L^2|))
 <= F(x)`,

`F(x)=log(1+x)+x log(1+1/x)`.                                      (5.7)

For every `x>0`,

`F(x) <= 3 e^(-1/3) x^(2/3)`.                                     (5.8)

Indeed, for `0<x<=1`,

`F(x)=(1+x)log(1+x)-x log x
 <=x(2+log(1/x))`,

and `x^(1/3)(2+log(1/x))<=3e^(-1/3)`. For `x>=1`, use the identity `F(x)=xF(1/x)` and the same estimate; the resulting ratio is at most `2`, hence also at most `3e^(-1/3)`.

Combining (5.5)--(5.8), and using

`x=2K |b|^(3/2) D_3^(-1/2)`,

we obtain

`p_Q(t)
 <=2^(5/3) 3e^(-1/3) K^(2/3) D_3^(-1/3)`.

With `K<=sqrt(2)`, the powers of two collapse to `4`, giving

`p_Q(t)
 <=12e^(-1/3) D_3^(-1/3)`.

Using (5.3) proves the theorem. QED.

## 6. Actual application to the live exact-rank-three isotropic collar

The completed fleet01/B13 exact-rank-three reduction identifies a terminal collar with two heavy physical rows

`u=sqrt(c)e_1`,
`v=rho e_1+sqrt(h)e_2`,

where `c>1/2`, `h>1/2`, and a putative bad sequence forces their physical quadratic pivots toward zero. The exact boundary subcase

`u^T Lambda u=v^T Lambda v=0`

is now completely paid.

Indeed

`Delta^2=||u wedge v||^2=c h>1/4`,

and under `|lambda_j|>=1`, `|det Lambda|>=1`. Therefore Theorem 5 gives

`boxed(
 ||p_Q||_infinity
 <12 e^(-1/3) 4^(1/3)
 =13.649071... .
 )`

Thus an exact pair of separated heavy isotropic physical rows cannot be the terminal obstruction. The genuinely unpaid collar is **near-isotropic but not exactly isotropic**; coefficient-smallness cannot be treated perturbatively without support or moment assumptions, because cap-one input laws may move to arbitrarily large scales.

## 7. Exact status and next implication

What changed in this run:

1. `QFORM-RANK3-COAREA-FROM-LINF-v1`: **REFUTED** as an information-loss statement by the explicit unit-density hyperboloid shell.
2. `QFORM-CONDITIONAL-3D-PROJECTION-CAP-v1`: **REFUTED** inside an exact product-law rank-three target by the rotated-square conditional section calculation.
3. The designated fleet02/B16 binary Frostman theorem was applied to the same exact target example, giving `||p_Q||_infinity<19.670` without conditional projection.
4. `QFORM-RANK3-TWO-ISOTROPIC-ROWS-PRODUCT-TRACE-v1`: **PROVED**, with explicit constant `12e^(-1/3)` and determinant/wedge scaling.
5. The exact two-heavy-isotropic boundary of the current B13 rank-three collar is closed with density `<13.650`.

The full QFORM conjecture remains OPEN. The first remaining implication in this branch is a product-preserving treatment of **near-isotropic** separated physical rows, or an exhaustive reduction showing that if the pivots are nonzero then an already-proved Schur/half-Riesz branch pays them uniformly. Arbitrary additional spectral directions remain a separate interaction debt.

No continuity claim is made. No finite computation is used as proof. No native learned-memory receiver was used.
