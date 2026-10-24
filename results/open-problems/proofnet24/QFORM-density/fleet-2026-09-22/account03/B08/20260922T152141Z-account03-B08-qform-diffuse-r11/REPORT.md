# account03/B08 — codimension-one diffuse/Schur bridge

**Run:** `20260922T152141Z-account03-B08-qform-diffuse-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `TARGET_SUPPORTING_THEOREM / CODIMENSION_ONE_BRIDGE`; full conjecture **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and route discipline

The target is unchanged: for every dimension, every family of independent real random variables with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a universally bounded density, or give a target-valid counterexample. No moment, compact-support, log-concavity, connected-support, Gaussian, diagonal-basis, or post-rotation independence hypothesis is used below.

The live corrections are respected. In particular, this run does not use a law-uniform pointwise one-dimensional quadratic-phase decay estimate, an unrestricted spectral-fiber supremum, or independence of spectral coordinates.

This is a deliberate mechanism change from the preceding B08 run. The preceding run optimized an MSS/full-range-diffuseness threshold. The present run instead eliminates one localized spectral direction by an exact **physical-coordinate Schur complement**, identifies the exact residual range projection, and computes its pseudo-determinant.

The designated assignment partner `account04/B08` had no completed current-QFORM handoff at both fresh checks made in this run, so no theorem is attributed to that slot. A compatible completed account04 theorem is nevertheless applied mathematically below: account04/B18's `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source report

`yspennstate/math-open-problems@6676b37d6b7c0557bd618f0273f0b58abbec0ca0:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

The other completed B08 input used is the earlier rank-three diffuse theorem `QFORM-DIFFUSE-RANK3-BL-v1`, whose relevant consequence is: if `W` has three orthonormal columns, every row leverage is at most `1/2`, and `B` is an invertible real symmetric `3 x 3` coefficient matrix, then for arbitrary independent input coordinates with densities bounded by one,

`R=(W^T X)^T B(W^T X)`

has a bounded continuous density satisfying

`||p_R||_infinity <= 3e |det B|^(-1/3)`.

The optimized full-range theorem from the immediately preceding B08 run is also used in the diffuse-fourth-direction branch.

## 2. Setup: three diffuse large eigenvectors plus one arbitrary spectral direction

Let `A` have rank exactly four and write its spectral decomposition as

`A = F Theta F^T`,

where

`F=[U,w]`, `F^T F=I_4`,

`Theta=diag(lambda_1,lambda_2,lambda_3,mu)`,

`|lambda_j|>=1` for `j=1,2,3`, and `mu!=0` is arbitrary in sign and magnitude. Thus the fourth spectral direction may be tiny, huge, positive, or negative.

Write the `i`th row of `F` as

`f_i=(u_i,w_i) in R^3 x R`,

where `u_i` is the `i`th row of `U`. Assume only that the three-large-eigenvalue subspace is strongly diffuse:

`max_i ||u_i||^2 <= epsilon_0 := 1/1024`.                         (2.1)

There is **no** diffuseness assumption on `w`.

The theorem below gives a complete quantitative dichotomy between a diffuse fourth direction and a localized fourth direction with a nonzero physical pivot.

## 3. Diffuse fourth direction: the old full-range theorem now applies

Assume first

`max_i w_i^2 <= 1/17`.                                           (3.1)

Then every row leverage of the entire four-dimensional range obeys

`||f_i||^2 <= epsilon_hat := 1/1024 + 1/17 = 1041/17408 < 3/50`.  (3.2)

For the previous full-range theorem define

`delta(epsilon)=1/2-epsilon-sqrt(2 epsilon)`.

Since `delta` is decreasing and `epsilon_hat<3/50`,

`delta(epsilon_hat) > delta(3/50)
 = 11/25 - sqrt(3)/5
 = (11-5sqrt(3))/25`.                                            (3.3)

Moreover

`2 epsilon_hat/delta(epsilon_hat)
 < 3/(11-5sqrt(3)) < 7/5 < 3/2`.                                (3.4)

The middle inequality is exact: it is equivalent to `35sqrt(3)<62`, and squaring gives `3675<3844`.

Therefore the preceding B08 full-range theorem applies with `q=7/5`, despite the arbitrary fourth eigenvalue `mu`. It yields a bounded **continuous** density, vanishing at infinity, with

`||p_Q||_infinity
 <= 3e/[sqrt(14/5) delta(epsilon_hat) (1/5)]`

and hence the explicit universal estimate

`boxed(
 ||p_Q||_infinity
 <= C_diff
 := 375e/[sqrt(14/5)(11-5sqrt(3))]
 < 261.
)`                                                                 (3.5)

This branch uses only diffuseness of the chosen three-large-eigenvalue subspace plus diffuseness of the one remaining range direction; it allows every sign pattern.

## 4. Localized fourth direction: exact Schur-range identity

Suppose now that (3.1) fails. Choose an original coordinate `h` such that

`s:=w_h^2 > 1/17`.                                                (4.1)

Put `L={1,...,n}\{h}` and partition

`A = [[a,b^T],[b,C]]`,

where `a=A_hh`. For the moment assume `a!=0`, and define the physical Schur complement

`S=C-bb^T/a`.                                                     (4.2)

Let `f=f_h=(u_h,w_h)`. Since

`a=f^T Theta f`,
`b=F_L Theta f`,
`C=F_L Theta F_L^T`,

we have the exact factorization

`S=F_L T F_L^T`,

where

`T=Theta-Theta f f^T Theta/a`.                                   (4.3)

### Lemma 4.1 — exact residual range

`T f=0`, `ker T=span{f}`, and `range T=f^perp`. Moreover `F_L` is an isometry on `f^perp`.

**Proof.** The first assertion follows from `f^TTheta f=a`. If `Tx=0`, invertibility of `Theta` gives

`x=f (f^TTheta x)/a`,

so the kernel is exactly `span{f}`. Symmetry gives `range T=f^perp`. Finally

`F_L^T F_L=I_4-ff^T`.

Hence for `x perpendicular f`,

`||F_Lx||^2=x^T(I-ff^T)x=||x||^2`. QED.

Choose an orthonormal `4 x 3` matrix `V` spanning `f^perp` and put

`W=F_L V`.

Then `W^TW=I_3`. Since scalar Schur elimination preserves rank and `rank A=4`, `rank S=3`; hence

`range S=F_L(f^perp)=range W`.                                   (4.4)

For every `i in L`, the physical row leverage of this residual range is therefore exactly

`ell_i = ||V^T f_i||^2
       = dist(f_i,span{f})^2`.                                   (4.5)

This identity is the main structural step of the run.

### Lemma 4.2 — localization of `w` forces diffuseness of the Schur residual

Under (2.1) and (4.1),

`max_{i in L} ell_i <= 25/1024 < 1/32`.                           (4.6)

**Proof.** For `i!=h`, choose the particular scalar `alpha=w_i/w_h`. Then the fourth coordinate cancels:

`f_i-alpha f=(u_i-alpha u_h,0)`.

By (4.5),

`ell_i <= ||u_i-(w_i/w_h)u_h||^2`

`      <= epsilon_0 (1+|w_i|/|w_h|)^2`.

Because `sum_{i!=h}w_i^2=1-s`,

`|w_i|/|w_h| <= sqrt((1-s)/s) < 4`

from `s>1/17`. Thus `ell_i<=25 epsilon_0=25/1024<1/32`. QED.

The important point is that this conclusion is completely independent of `mu`, of all eigenvalue signs, and of the size of the scalar pivot `a`.

## 5. Exact pseudo-determinant of the Schur residual

The residual determinant has an equally clean formula.

### Lemma 5.1 — codimension-one Schur pseudo-determinant

With the notation above,

`boxed(
 |pdet S| = |det Theta| ||f||^2 / |a|.
)`                                                                 (5.1)

**Proof.** Since `T` has rank three and kernel `span f`, its signed pseudo-determinant is the derivative at zero of `det(T+tI)`. The matrix determinant lemma gives

`det(T+tI)
 = det(Theta+tI)
   [1-(1/a) f^T Theta(Theta+tI)^(-1)Theta f]`.

The bracket vanishes at `t=0`. Differentiating it at zero gives

`(1/a)||f||^2`,

because

`d/dt [f^T Theta(Theta+tI)^(-1)Theta f]_{t=0}
 = -||f||^2`.

Hence

`pdet T=det Theta ||f||^2/a`.                                    (5.2)

By Lemma 4.1, writing `T=V T_0 V^T` gives

`S=(F_LV)T_0(F_LV)^T=WT_0W^T`

with `W^TW=I_3`. Therefore `S` and `T_0` have the same three nonzero eigenvalues, so `pdet S=pdet T`. Taking absolute values proves (5.1). QED.

## 6. A new explicit density estimate for the heavy-fourth-direction branch

Let

`R=X_L^T S X_L`.

By Lemma 4.2, the rank-three range frame of `S` has maximum physical leverage `<1/32`, hence in particular `<1/2`. Applying the completed rank-three diffuse theorem and then Lemma 5.1 gives

`||p_R||_infinity
 <= 3e |pdet S|^(-1/3)`

` = 3e ( |a|/(|det Theta| ||f||^2) )^(1/3).`                    (6.1)

This density is continuous.

Now complete the square in the **original independent coordinate** `X_h`:

`Q
 = a (X_h + b^T X_L/a)^2 + R`.                                 (6.2)

Conditionally on `R=r`, the variable

`V_r=X_h+b^T X_L/a`

has a density bounded by one: it is a mixture, over the conditional law of `X_L`, of translations of the original density of `X_h`. No independence after a rotation is asserted.

Apply account04/B18's completed `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` to (6.2). It gives the actual inequality

`||p_Q||_infinity <= 2 sqrt( ||p_R||_infinity/|a| )`.

Using (6.1),

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(3e)
    ( |a|^2 |det Theta| ||f||^2 )^(-1/6).
)`                                                                 (6.3)

This is the main analytic estimate of the run. It is valid for **all sign patterns** and for arbitrary nonzero `mu`; it uses only original-coordinate independence and the selected-three-eigenvector diffuseness (2.1), together with the heavy-fourth-coordinate and nonzero-pivot conditions.

Since

`|det Theta|=|lambda_1lambda_2lambda_3mu|>=|mu|`

and `||f||^2>=w_h^2>1/17`, (6.3) yields the simpler target-relevant form

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(3e)
    (17/(|a|^2 |mu|))^(1/6).
)`                                                                 (6.4)

In particular, the branch

`|a|^2 |mu| >= 1/64`                                               (6.5)

has the universal bound

`||p_Q||_infinity
 <=2sqrt(3e) 1088^(1/6)
 <18.32.`                                                          (6.6)

Only an essentially bounded density is claimed in (6.3)--(6.6). The account04 square-smoothing theorem proves absolute continuity and the `L^infinity` bound, but not continuity for arbitrary rough input densities.

## 7. Why this is a genuine extension of the previous B08 theorem

The previous theorem required the **entire range projection** to be diffuse. The heavy branch above can have full-range leverage bounded away from zero, even near one. The Schur identity removes the localized fourth range direction in one physical-coordinate elimination and shows that the remaining three-dimensional range is diffuse automatically.

For example, take a rank-four indefinite matrix with eigenvalues `(1,1,-1,1)`, choose `w` with `w_h^2=1/4`, choose the three large-eigenvector rows so that `u_h=0` and `max_i||u_i||^2<=1/1024`, and arrange the remaining three columns orthogonally in the complement of `w` (a sufficiently large Hadamard-type tail supplies such frames). Then the entire-range leverage at `h` is `1/4`, far outside the prior full-range threshold. Here

`a=1/4`, `||b||=sqrt(3)/4`,

and (6.3) gives a dimension-free bound (well below the coarse universal subbranch constant). The matrix is rotated and indefinite; no eigen-coordinate independence is used.

## 8. Combined rank-four dichotomy and exact residual

For rank-four target matrices satisfying the selected-large-subspace diffuseness (2.1), this run proves:

1. If the fourth spectral vector satisfies `max_i w_i^2<=1/17`, then `Q` has a bounded continuous density with universal constant `<261`.
2. If some `w_h^2>1/17` and `a=A_hh!=0`, then the exact density estimate (6.3) holds; in particular `|a|^2|mu|>=1/64` gives the universal bound `<18.32`.

Thus a still-unpaid rank-four configuration in this diffuse-large-eigenspace regime must have a localized fourth eigenvector and, at every useful heavy coordinate, either a zero scalar pivot or very small product `|A_hh|^2 |mu|`.

This is substantially narrower than the preceding unpaid implication “selected-large-eigenspace diffuseness versus an arbitrary localized spectral remainder.” It resolves that implication completely for one extra spectral atom except for the explicit small-pivot/small-fourth-eigenvalue corner.

For rank exactly three, the earlier diffuse theorem already gives the universal continuous bound `3e` under (2.1), so the new issue begins only at codimension one.

## 9. Next mechanism

The next B08 step should attack the explicit residual

`QFORM-CODIM1-SMALL-PIVOT-v1`:

> `rank A=4`, the three `|lambda|>=1` eigenvectors satisfy maximum row leverage `<=1/1024`, the fourth vector is localized, but every heavy fourth-vector coordinate has `A_hh=0` or `|A_hh|^2|mu|` very small.

The natural product-preserving alternatives are a two-coordinate hyperbolic pivot or account04/B20's disjoint-aggregate hyperbolic-square channel; a new proof must avoid replacing conditional density caps by independence.

## 10. Status

**Proved in this run:**

- exact Schur-residual range identity (4.4)--(4.5);
- explicit leverage transfer `max ell_i<=25/1024` from a localized fourth eigenvector;
- exact pseudo-determinant formula (5.1);
- the heavy-fourth-direction density estimate (6.3), using the completed account04/B18 square-smoothing theorem;
- universal corollary `<18.32` under (6.5);
- diffuse-fourth-direction continuous-density branch `<261`.

**Not proved:** the unrestricted quadratic-form conjecture; the codimension-one zero/small-pivot residual above; continuity in the heavy branch. The full target remains **OPEN**.
