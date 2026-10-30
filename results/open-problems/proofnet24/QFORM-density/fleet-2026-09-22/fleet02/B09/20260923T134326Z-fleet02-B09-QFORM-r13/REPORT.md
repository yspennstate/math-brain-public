SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T13:43:26Z.
attacking: the very-high-hub-leverage survivor by spending one compulsory physical hub row separately inside the partner's selected three-volume compiler, while retaining arbitrary same-side curvature.

# fleet02/B09 r13 — one-anchor three-volume hybrid crosses the 3/4 hub-leverage barrier

## Status

**ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN.**

This run proves `QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1`, a source-coordinate cross-block theorem that permits one selected-minor row marginal to equal one. It combines a three-volume determinant estimate with a derived two-volume determinant estimate *before* taking the quadratic-decoupling square root. The resulting characteristic-function power is `|t|^{-5/4}`, hence integrable. The conclusion is a continuous density and a direct linear interval bound; there is no square-root small-ball loss.

Applied to the designated fleet03/B09 aggregate compiler, the theorem pays a family with physical hub leverage exactly one, completely beyond the preceding `<3/4` q-Jensen gate, while retaining high-rank dense same-side leaf curvature. The remaining high-hub debt is narrowed to concentration of the two-dimensional hub Pluecker mass on one partner row (or another already-paid exit).

No moments, bounded support, centering, identical laws, log-concavity, connected support, diagonal-basis assumption, or post-rotation independence is used. Full-target continuity remains open; continuity is proved only in the stated branches. Execution status remains `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The immediately preceding fleet02/B09 result `QFORM-FRACTIONAL-SUBVOLUME-BL-q-v1` proves the selected three-volume estimate for row marginals `alpha_i<=q/2`, `1<=q<3/2`. Plugged into the latest fleet03/B09 compiler, it pays every physical hub leverage `eta<3/4`. At `eta=3/4`, the absolute Jensen route reaches only `|t|^{-1}` and is not Fourier-integrable.

The first unpaid implication attacked here is therefore

`QFORM-VERY-HIGH-HUB-ONE-ANCHOR-OR-CONCENTRATED-PAIR-v1`:

> In the partner's actual selected physical-minor family, if one physical hub row is compulsory or nearly compulsory, spend that row by a separate L2/Plancherel step and retain enough of the other two determinant directions to recover an integrable Fourier power. If this works, isolate the genuinely remaining case where the hub Pluecker mass itself is concentrated on a single partner row.

The theorem below pays the exact compulsory-row branch, including leverage one.

## 2. Sources actually consumed and applied

### 2.1 Required `e5f71d79...` Claude package

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The proof below uses its completed cap-one characteristic-function lemma

`integral |psi|^p <= 4 pi / sqrt(p), p>=2`,

and its original-coordinate decoupling/Brascamp--Lieb determinant mechanism. The counterexample search still reports no valid counterexample to the full QFORM target.

I also apply its completed mixed-hub Theorem H to a concrete target-valid star in Section 6, deriving `||p||_inf<=4sqrt(2)`.

### 2.2 Designated partner fleet03/B09 r32

The latest completed partner result is

`QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`,

`yspennstate/math-open-problems@56d0211f2f04d74152032fd1914196673eb5c3e6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T124906Z-fleet03-B09-QFORM-r32/REPORT.md`.

For a physical rank-two hub/star

`A[H,I]=P C^T, P^T P=I_2`,

with arbitrary `D=A[I,I]`, it defines singleton third-volume quantities `Gamma_k` and

`G_*=sum_k Gamma_k^2`.

Its Bernoulli compiler produces an actual source-coordinate cut and a selected family of physical `3x3` minors with total squared determinant mass

`W >= (27/256) G_*`.

In the diffuse-singleton branch, every moved-leaf row marginal is `<1/2`. The selected hub-pair weight is exactly `det(P[{a,b},:])^2`, so a hub row `h` has marginal `(PP^T)_{hh}`.

This exact factorization is used in Section 5, not merely cited.

## 3. New theorem — one compulsory physical row

Let `I,J` be disjoint sets of ORIGINAL coordinates and put `M=A[I,J]`. Condition on all remaining original coordinates. The same-side quadratic blocks `A[I,I]`, `A[J,J]` and all induced affine terms may be arbitrary.

Fix a distinguished physical row `h in I`, and write

`a=M[h,:]`.

Let `Omega` be any nonempty selected family of actual physical `3x3` minors `(R,C)` of `M` such that

`h in R` for every `(R,C) in Omega`.

Put

`Z=sum_(R,C in Omega) det(M[R,C])^2>0`,

and normalize by these squared determinants. For `i!=h`, let

`alpha_i=P(i in R)`.

### Theorem `QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1`

If

`max_(i!=h) alpha_i <=1/2`,

then the full quadratic-plus-affine output has a continuous density and

`boxed:
 ||p_Q||_inf
 <= 5*2^(4/5)*sqrt(e) * ||a||_2^(1/5) * Z^(-1/5)
 < 14.353 ||a||_2^(1/5) Z^(-1/5).`

Consequently every interval `L` obeys

`boxed:
 P{Q in L}
 <=14.353 ||a||_2^(1/5) Z^(-1/5)|L|.`

The scaling is correct: replacing `M` by `sM` sends `||a||^(1/5) Z^(-1/5)` to `s^{-1}` times itself.

### Proof

Use the source-coordinate quadratic decoupling on the `I` bank. For `W=X_J-X'_J`, whose coordinates are independent with densities `g_j=f_j*tilde(f_j)<=1`, let

`h_i(s)=|psi_i(2ts)|`.

Then

`|phi_Q(t)|^2 <= F(t)`

with

`F(t)=integral prod_(i in I) h_i(<M[i,:],w>) prod_(j in J) g_j(w_j) dw.`

All same-side curvature is retained until legitimate Weyl differencing; no rotated random coordinates are declared independent.

Set

`H(w)=h_h(<a,w>)`,
`R(w)=prod_(i!=h) h_i(<M[i,:],w>)`.

Cauchy--Schwarz under the probability measure `prod_j g_j(w_j)dw` gives

`F(t)^2 <= F_2(t) F_0(t)`,

where

`F_2=integral H^2 R prod_j g_j`,
`F_0=integral R prod_j g_j`.

#### 3.1 Three-volume estimate for `F_2`

Use the selected family `Omega` in the Gaussian Brascamp--Lieb determinant expansion. The distinguished row exponent is one; all other row exponents are `alpha_i<=1/2`. Let `beta_j` be the selected column marginals.

For the distinguished row, Plancherel gives

`integral h_h(s)^2 ds <= pi/|t|`.

For every other active row, the required `e5f71d79...` Lp lemma with `p=1/alpha_i>=2` gives

`(integral h_i(s)^(1/alpha_i) ds)^(alpha_i)
 <=[2pi sqrt(alpha_i)/|t|]^(alpha_i).`

The `alpha_i` factors cancel the row-entropy part of the BL constant. Since `sum_(i!=h)alpha_i=2` and the column entropy factor is at most `e^(3/2)`, the selected determinant lower bound yields

`F_2(t)
 <=4 pi^3 e^(3/2) Z^(-1/2)|t|^(-3).`                 (3.1)

#### 3.2 Derive a genuine two-volume measure for `F_0`

For a low row pair `R0={i,k}`, define

`z_R0=sum_(C:({h} union R0,C) in Omega) det M[{h} union R0,C]^2`.

Then `sum_R0 z_R0=Z`. Put `pi_R0=z_R0/Z`; its row marginals are precisely the low-row `alpha_i`.

Let

`Z2_R0=sum_(|C|=2) det M[R0,C]^2
       =||M[i,:] wedge M[k,:]||_2^2.`

The full exterior-volume identity gives

`z_R0
 <=||a wedge M[i,:] wedge M[k,:]||_2^2
 <=||a||_2^2 Z2_R0.`

Hence

`Z2_R0/pi_R0 >= Z/||a||_2^2.`                         (3.2)

For each row pair distribute probability `pi_R0` among its actual physical `2x2` minors in proportion to their squared determinants. This yields a bona fide determinant weight `w` on physical `2x2` minors, with the same low-row marginals `alpha_i`. If `gamma_j` are its column marginals, its weighted geometric determinant mass is

`Z_eff
 =exp(E_w log(det^2/w))
 =exp(sum_R0 pi_R0 log(Z2_R0/pi_R0))
 >=Z/||a||_2^2.`                                      (3.3)

Run the two-volume BL estimate for `F_0`. The same `e5f71d79...` Lp lemma applies because `alpha_i<=1/2`, `sum alpha_i=2`; the column entropy is at most `e`. Thus

`F_0(t)
 <=4 pi^2 e Z_eff^(-1/2)|t|^(-2)
 <=4 pi^2 e ||a||_2 Z^(-1/2)|t|^(-2).`                (3.4)

#### 3.3 Assemble before the decoupling square root

From (3.1) and (3.4),

`F(t)
 <=4 pi^(5/2)e^(5/4)||a||_2^(1/2)Z^(-1/2)|t|^(-5/2).`

Therefore

`|phi_Q(t)|
 <=2 pi^(5/4)e^(5/8)||a||_2^(1/4)Z^(-1/4)|t|^(-5/4).`

The power `5/4` is strictly integrable. Combining with `|phi_Q|<=1`, exact integration of `min(1,K|t|^{-5/4})` gives

`||p_Q||_inf
 <=(5/pi)K^(4/5)
 =5*2^(4/5)*sqrt(e)||a||_2^(1/5)Z^(-1/5).`

Fourier inversion gives continuity, and the density bound directly gives the stated `O(|L|)` interval estimate. There is no probability squaring after the density estimate and no square-root small-ball loss. QED.

## 4. Consequence for high hub leverage

In the partner rank-two hub/star compiler, selected determinant weights factor into a hub-pair term and an independent moved-leaf term. For a hub row `h`, write

`eta_h=(PP^T)_{hh}
      =sum_(b!=h) det(P[{h,b},:])^2.`

Conditioned on the selected minor containing `h`, the other hub row has distribution

`delta_b=det(P[{h,b},:])^2/eta_h.`

The moved-leaf marginal is unchanged by this conditioning. Therefore, in the partner's diffuse-singleton branch, the new theorem pays any `eta_h`, including `eta_h=1`, whenever

`max_b delta_b<=1/2`.

This is qualitatively different from the preceding q-Jensen result: one row may now have selected marginal exactly one.

A source-valid regression shows the new spread condition is not automatic from Parseval geometry alone. Taking `P=I_2` gives hub leverage one and conditional partner mass one. Thus a universal proof cannot simply assert that every high-leverage hub has a diffuse Pluecker partner. This is a structural obstruction only, not a QFORM counterexample.

## 5. Actual target-valid family at hub leverage exactly one

Let the hub bank have `r+1` physical coordinates, `r>=2`. Define a Parseval two-frame by

`p_0=(1,0)`,
`p_b=(0,1/sqrt(r)), 1<=b<=r`.

Then `P^TP=I_2`, the physical hub leverage at row zero is exactly

`eta_0=1`,

and every nonzero hub-pair determinant has

`det(P[{0,b},:])^2=1/r`.

So the conditional partner distribution is completely diffuse: `delta_b=1/r<=1/2`.

Let `n>=32` be a Walsh dimension. Choose flat orthonormal Walsh vectors

`c_1,c_2,v_3,...,v_n`

on the leaf bank. Choose equal numbers of signs `sigma_l=+1` and `-1` for `l=3,...,n`, and set

`C=[c_1,c_2]`,
`D=sum_(l=3)^n sigma_l v_l v_l^T`,

`A=[[0,PC^T],[CP^T,D]].`

Because the Walsh vectors are flat and the signs balance, `D` has zero physical diagonal, `D c_1=D c_2=0`, and

`D^2=I-c_1c_1^T-c_2c_2^T`.

The two coupled hub/leaf directions give two copies of the matrix `[[0,1],[1,0]]`, hence eigenvalues `+1,-1,+1,-1`. On the leaf complement, `D` has eigenvalues `sigma_3,...,sigma_n`, all of modulus one. The remaining `r-1` hub directions are null. Thus **every nonzero eigenvalue of A has modulus one**; this is a genuine owner-target family.

For every leaf index `k`, the partner singleton third-volume identity gives

`Gamma_k^2=(1-2/n)^2.`

Indeed the truncated `c_1,c_2` Gram determinant is `1-2/n`, the row `D[k,:]` is orthogonal to both and has squared norm `1-2/n`, and `D_kk=0`. Hence

`G_*=n(1-2/n)^2.`

Also

`Gamma_k^2/G_*=1/n<27/512`,

so the partner's concentrated-singleton exit does **not** apply. The old partner diffuse theorem fails because the hub leverage is `1>1/2`; the preceding fleet02 q-extension fails because `1>=3/4`.

Now apply the partner's actual Bernoulli compiler. It produces a source-coordinate cut and selected three-minor family with

`Z=W >= (27/256)G_*.`

Every positive selected hub pair is `{0,b}`, so row zero belongs to every positive selected minor. The other hub-row marginal is `1/r<=1/2`, and the moved-leaf row marginal is `<1/2` in this diffuse-singleton branch. The distinguished physical row of the cross cut is a restriction of `c_1`, hence has norm at most one.

`QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1` therefore gives the actual inequality

`boxed:
 ||p_(X^T A X)||_inf
 <= 5*2^(4/5)*sqrt(e)*(256/27)^(1/5)
    [n(1-2/n)^2]^(-1/5)
 <22.507 [n(1-2/n)^2]^(-1/5).`

For `n>=32`, the right side is `<11.548`. For every interval `L`, the same coefficient multiplies `|L|`.

This is a target-valid high-rank same-side-curvature family at **physical hub leverage exactly one**, paid by an aggregate source-coordinate mechanism with no large physical minor requirement.

## 6. Required `e5f71d79...` result applied to a real target inequality

Take one physical hub coordinate `X_0` and a disjoint leaf bank `Y`. Choose three orthonormal flat leaf vectors `c,v_1,v_2`, with leaf dimension at least six, and form

`F=2X_0<c,Y>+<v_1,Y>^2+<v_2,Y>^2.`

Its active coefficient matrix on `span{e_0,c,v_1,v_2}` has spectrum

`{-1,1,1,1}`,

so it is target-valid. In the required `e5f71d79...` Theorem H, use one physical hub and rank-two same-side leaf curvature. The mixed frame `[v_1,v_2,c]` has Gram `I_3`, and every physical mixed leverage is `3/n<=1/2`. The theorem gives

`|phi_F(t)|<=8 pi^2 |t|^(-2).`

Exact integration of `min(1,8pi^2|t|^-2)` yields

`boxed: ||p_F||_inf <=4sqrt(2)<5.657,`

and therefore

`boxed: P{F in L}<=4sqrt(2)|L|.`

This is an actual source-coordinate mixed-hub inequality, not a theorem citation. It complements Section 5: Theorem H pays low-rank same-side curvature directly, while the new one-anchor theorem retains the arbitrary/high-rank same-side curvature compiled by the designated partner.

## 7. Remaining implication

The first unpaid B09 implication is now

`QFORM-HIGH-HUB-CONCENTRATED-PLUCKER-PAIR-OR-PAID-EXIT-v1`:

> Starting from the bare three-large-eigenvalue hypothesis in the rank-two hub/star survivor, if a hub row has very high leverage and more than half of its conditional two-dimensional Pluecker mass lies on one physical partner row, force either an already-paid physical-pair/zero-hub/ridge/grouped-cross/definite exit, or a new two-hub-plus-general-leaf-curvature smoothing theorem that preserves the external third source direction.

The simple frame `P=I_2` shows that the concentrated-pair alternative itself is geometrically possible, so the next step must use the quadratic-form coefficients and the third spectral resource, not Parseval geometry alone.

Nothing here proves the unrestricted QFORM conjecture and no valid counterexample to it was found.
