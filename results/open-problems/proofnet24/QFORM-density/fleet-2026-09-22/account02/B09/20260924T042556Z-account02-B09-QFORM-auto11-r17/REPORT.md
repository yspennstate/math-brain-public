SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T04:25:56Z.
attacking: the partner's near-Schur-null heavy physical-pair collar by proving a scalar-curvature-uniform rough-star square-root small-ball estimate, then feeding it to pair-log before any worst half-Riesz slice.

# account02/B09 — rough-star uniform collar through an invertible indefinite physical pair

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING THEOREM / PARTNER DEBT CLOSED IN THE NONZERO-STAR BRANCH / FULL QFORM OPEN**.

All variables below are literal original-coordinate variables. Inputs are independent with densities bounded by one. No moment, support, log-concavity, Gaussianity, iid hypothesis, post-rotation independence, or deletion of a small coefficient is used. Continuity is not claimed from the pair-log step.

## 1. First unpaid implication

The latest completed designated partner account03/B09 r43 leaves

`QFORM-RANK2-HEAVY-PAIR-NEAR-SCHURNULL-INTERPOLATION-v1`:

a literal invertible indefinite physical pair `B` is completed, and the exact Schur remainder has the form

`R=s X^2+2X<m,Z>+beta X+G(Z)+c`,

where `s=det(P)/det(B)` may tend to zero, `m` is the entire original-coordinate Schur-star row, and `G` is arbitrary same-bank quadratic-affine curvature. The partner pays `s=0` but explicitly forbids deleting a small nonzero `sX^2` or taking a worst conditional-density/half-Riesz slice first.

The theorem below removes this `s -> 0` obstruction whenever `m != 0`.

## 2. Theorem `QFORM-ROUGH-STAR-UNIFORM-SQRT-SMALLBALL-v1`

Let `X` be one literal original coordinate and `Z` a disjoint bank of original independent coordinates, all with densities <=1. Let `m != 0`, let `G(Z)` be an arbitrary real measurable phase, and put

`R=sX^2+2X<m,Z>+bX+G(Z)+c`.

Then for every `t != 0`,

`|phi_R(t)| <= 2^(1/4) sqrt(pi) ||m||_2^(-1/2) |t|^(-1/2)`.          (2.1)

Consequently, for every `rho>0`,

`sup_u P{|R-u|<=rho}`
` <= exp(1/2) Gamma(1/4) ||m||_2^(-1/2) sqrt(rho)`.                  (2.2)

Both estimates are uniform in the scalar curvature `s` and in the full same-bank phase `G`.

### Proof

Let `L=<m,Z>`. The reviewed one-dimensional product-projection estimate gives

`||p_L||_infinity <= sqrt(2)/||m||_2`.                              (2.3)

For fixed `t`, push the complex measure `exp(itG(Z)) dP_Z` forward by `Z -> L`. It has a complex density `b_t` with `|b_t(l)|<=p_L(l)` almost everywhere, hence

`||b_t||_2^2 <= ||p_L||_infinity <= sqrt(2)/||m||_2`.               (2.4)

Put `g_t(x)=f_X(x) exp(it(sx^2+bx))`. Since `f_X<=1`,

`||g_t||_2^2 = int f_X^2 <=1`.                                     (2.5)

With angular Fourier transform `hat g(xi)=int g(x)e^{i xi x}dx`,

`phi_R(t)=unit_phase * int b_t(l) hat g_t(2tl) dl`.                 (2.6)

Cauchy-Schwarz and Plancherel therefore give

`|phi_R(t)| <= ||b_t||_2 [(1/(2|t|)) int |hat g_t(xi)|^2 dxi]^(1/2)`
` <= 2^(1/4) sqrt(pi) ||m||_2^(-1/2)|t|^(-1/2)`,

which is (2.1). The chirp `exp(itsx^2)` is retained exactly and costs nothing in the L2 norm.

For `|y|<=rho`,

`1 <= exp(1/2) exp(-y^2/(2rho^2))`.

Fourier inversion of the Gaussian and (2.1) yield

`P{|R-u|<=rho}`
` <= e^(1/2) rho/sqrt(2pi) int exp(-rho^2t^2/2)|phi_R(t)|dt`.

Using

`int_0^infinity t^(-1/2)e^{-rho^2t^2/2}dt = rho^(-1/2)2^(-3/4)Gamma(1/4)`,

all powers of `2` and `pi` cancel and (2.2) follows. `square`

## 3. Splice into the latest designated partner: the near-Schur-null collar is paid

Use account03/B09 r43's exact pair completion and the completed pair-log theorem. For an invertible indefinite literal physical pair `B`, write

`D=|det B|`, `kappa=sigma_min(B)`.

The pair-log theorem says that if its Schur remainder satisfies

`sup_u P{|R-u|<=rho} <= H0 sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H0) (D kappa)^(-1/4)`.                 (3.1)

By (2.2),

`H0=e^(1/2)Gamma(1/4)||m||_2^(-1/2)`.

Hence, for **every real scalar Schur coefficient `s`**, including `s=0` and arbitrarily small nonzero `s`,

`boxed:`
`||p_Q||_infinity`
` <= 4 sqrt(2)e^(1/4)Gamma(1/4)^(1/2)`
`    [D kappa ||m||_2]^(-1/4)`
` < 13.831 [D kappa ||m||_2]^(-1/4).`                               (3.2)

This is already the required linear interval estimate

`P{Q in I} <= 13.831 [D kappa ||m||_2]^(-1/4)|I|`.                 (3.3)

Thus the partner's exact-Schur-null face extends to a full scalar-curvature collar on every branch with nonzero aggregate Schur star. No square-root decoupling loss survives: the square-root profile occurs only in the remainder and is consumed by the logarithmic physical-pair kernel before the final estimate.

## 4. Actual target-valid dense-curvature family

Let `U,V,X,Z_1,...,Z_m` be independent cap-one inputs. Choose orthonormal vectors `m,w in R^m` with `||m||=||w||=1`, and take `w` flat so `ww^T` is dense in source coordinates. For arbitrary real `s`, set

`Q_s=2UV+sX^2+2X<m,Z>+<w,Z>^2`.                                   (4.1)

The physical pair `(U,V)` has

`B=[[0,1],[1,0]]`, so `D=kappa=1`.

Its Schur remainder is exactly of the form in Theorem 2 with `||m||=1` and arbitrary dense same-bank phase `G(Z)=<w,Z>^2`. Therefore

`boxed: ||p_{Q_s}||_infinity < 13.831`                             (4.2)

uniformly for every `s in R`, with `P{Q_s in I}<13.831|I|`.

This family is inside the owner target for every `s`: the `(U,V)` block contributes eigenvalues `{1,-1}`, the `w` direction contributes eigenvalue `1`, and the `(X,m)` block has eigenvalues `(s +/- sqrt(s^2+4))/2`. In particular at least three eigenvalues have modulus >=1 for all `s`. The dense physical same-side coupling `ww^T` is retained, and (4.2) remains uniform through the exact `s=0` Schur-null face.

## 5. Required pinned `e5f71d79...` mixed-hub application

The pinned completed Theorem H is applied to a different genuine source-coordinate star, retaining dense same-side curvature. Let `c,v_1,v_2` be flat orthonormal Walsh vectors on an `m>=8` leaf bank and put

`F=2H<c,Y>+<v_1,Y>^2+<v_2,Y>^2`.                                  (5.1)

The leaf operator `v_1v_1^T+v_2v_2^T` is dense in physical coordinates. The mixed rows `(v_1(i),v_2(i),c(i))` have Gram `I_3` and leverage `3/m<=1/2`. Theorem H therefore gives

`|phi_F(t)| <= 8 pi^2 |t|^(-2)`.                                  (5.2)

Exact integration of `min(1,8pi^2/t^2)` gives

`boxed: ||p_F||_infinity <=4sqrt(2)<5.657`,                        (5.3)

hence `P{F in I}<=4sqrt(2)|I|`. The active spectrum is `{-1,1,1,1}`, so this is target-valid. There is no post-rotation independence and no probability squaring.

## 6. What remains

The scalar-curvature near-Schur-null interpolation is no longer the first B09 obstruction when the aggregate Schur star is nonzero. The sharpened unpaid implication is

`QFORM-HEAVY-PAIR-ZEROSTAR-OR-PAIR-RANK-COLLAR-v1`:

route the partner's branches where the relevant aggregate Schur star `m` vanishes (including its `n_k=0` complement endpoint), or where the selected physical pair itself approaches rank one so `D kappa ->0`, without dividing by a disappearing pair determinant. The exact rank-one pair endpoint is paid by the preceding account02/B09 arbitrary-cross theorem, but the near-rank-one collar still requires joint spending of the third resource.

The pinned counterexample search reports no valid full-target counterexample, and none is produced here. Full unrestricted QFORM remains OPEN. Full-target continuity remains OPEN.
