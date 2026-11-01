# fleet01/B07 — localized spectral direction forces either a paid pivot or a strong physical bilinear bank

**Run:** `a01-b07-20260922T143228Z-qform-r12b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection  
**Status:** `ESSENTIAL_SUPPORTING_STEP / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope

The full target is: for independent real coordinates `X_i` with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a dimension-free density bound for `X^T A X`, or give a valid counterexample. The additional desired continuity conclusion is tracked separately.

This report proves a new exact-rank-three structural reduction. It does **not** prove the arbitrary-rank target. The result preserves original-coordinate independence throughout and does not rotate the random vector.

Current corrections are respected: no law-uniform pointwise Fresnel decay is used; no post-rotation independence is asserted; no fiber-supremum estimate is used; no single cross minor is assumed large; and a bounded marginal for a projected variable is not promoted to a bounded conditional density.

## 2. Inputs actually used

### 2.1 Assigned partner fleet02/B07

I use the completed determinant-weighted disjoint-basis theorem

`QFORM-PLUCKER-ENTROPY-BL-v1 / disjoint-basis dichotomy`,

canonical source

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

For an exact-rank-three matrix

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_r|>=1`,

write `w_I=det(U_I)^2` over coordinate triples and

`delta=sum_{I cap J=empty} w_I w_J`.

The partner proves:

1. if `delta>=1/8`, then the exact-rank-three quadratic form has a dimension-free density bound `||p_Q||_infinity <=6e`;
2. if `delta<1/8`, there are a coordinate triple `I` and a unit spectral vector `v in R^3` such that

`sum_{j notin I} <u_j,v>^2 <= delta^(1/3)<1/2`,

hence

`sum_{j in I}<u_j,v>^2>1/2`.

### 2.2 Completed fleet03/B10 nonisotropic-pivot theorem

I also use

`QFORM-RANK3-NONISOTROPIC-PIVOT-v1`,

canonical source

`yspennstate/math-open-problems@5ce98ee83b2fef75136f10cdd0e89741f017d3e0`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/fleet03-B10-20260922T141643Z-r11/REPORT.md`.

If row `u_i` has leverage `ell_i=||u_i||^2` and diagonal pivot

`d_i=u_i^T Lambda u_i !=0`, then

`||p_Q||_infinity <97 [|d_i| ell_i |det Lambda|]^(-1/4)`.

The same report supplies the one-dimensional Ball--Rogozin marginal fact used below: for a unit coefficient vector `b`, a linear combination `sum b_j X_j` of independent cap-one coordinates has density at most `sqrt(2)`.

## 3. New theorem: localized-isotropic-bank dichotomy

### Theorem 3.1 (`QFORM-LOCALIZED-ISOTROPIC-BANK-DICHOTOMY-v1`)

Let

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_1|,|lambda_2|,|lambda_3|>=1`,

so `A` has exact rank three. Define the Pluecker disjointness mass `delta` as above. Then one of the following holds.

**Diffuse determinant branch.**

`delta>=1/8`, and therefore

`||p_Q||_infinity <=6e`.

**Paid physical-pivot branch.**

There is an original coordinate `i` with

`ell_i>1/6`, `|d_i|>=ell_i/2`,

and hence

`||p_Q||_infinity <97*72^(1/4) <283`.

**Strong physical bilinear-bank branch.**

There is an original coordinate `i` with `ell_i>1/6` and

`|d_i|<ell_i/2`,

for which the off-diagonal row energy

`beta_i^2 := sum_{j!=i} A_{ij}^2`

satisfies

`beta_i^2>1/8`.

Moreover, there is a random variable

`Y_i=(sqrt(2)/beta_i) sum_{j!=i} A_{ij}X_j`

such that:

* `Y_i` is independent of `X_i`;
* `Y_i` has a probability density bounded by one;
* with `R_i=X_{-i}^T A_{-i,-i}X_{-i}`, one has the exact original-coordinate representation

`Q=d_i X_i^2 + c_i X_i Y_i + R_i`,

where

`c_i=sqrt(2) beta_i>1/2`;

* `Y_i` is not asserted independent of `R_i`; its stronger provenance is that it is a normalized linear combination of the original independent cap-one coordinates `X_j`, `j!=i`.

Thus every exact-rank-three instance is either already uniformly paid by a completed determinant/pivot theorem or is reduced to a quantitatively nondegenerate hyperbolic bank with coefficient exceeding `1/2` and exact product-linear provenance.

### Proof

If `delta>=1/8`, the first branch is precisely the assigned partner theorem.

Assume `delta<1/8`. By the partner localization result there exist a coordinate triple `I` and a unit spectral vector `v` for which

`sum_{j in I}<u_j,v>^2>1/2`.

Since `I` has three elements, some `i in I` satisfies

`<u_i,v>^2>1/6`.

Therefore

`ell_i=||u_i||^2 >= <u_i,v>^2>1/6`.                                      (3.1)

Put `ell=ell_i`, `d=d_i`, and normalize the nonzero row by

`r=u_i/sqrt(ell)`, `||r||=1`.

Let

`alpha=r^T Lambda r=d/ell`.                                                (3.2)

#### Case 1: `|alpha|>=1/2`

Then

`|d| ell = ell^2 |alpha| > (1/6)^2 (1/2)=1/72`.                           (3.3)

Also `|det Lambda|>=1`. Applying the completed fleet03/B10 theorem gives

`||p_Q||_infinity <97 [|d|ell|det Lambda|]^(-1/4)
                    <97*72^(1/4)
                    =282.5563...<283`.                                    (3.4)

This is the paid physical-pivot branch.

#### Case 2: `|alpha|<1/2`

Use Parseval for the rows of `U`:

`sum_j u_j u_j^T=I_3`.

The squared Euclidean norm of physical row `i` of `A` is therefore

`sum_j A_{ij}^2
 =sum_j (u_i^T Lambda u_j)^2
 =u_i^T Lambda (sum_j u_j u_j^T) Lambda u_i
 =u_i^T Lambda^2 u_i`.                                                     (3.5)

Since every eigenvalue of `Lambda` has modulus at least one,

`Lambda^2 >= I_3`, so

`sum_j A_{ij}^2 >= ell`.                                                    (3.6)

Subtract the diagonal contribution `d^2=ell^2 alpha^2`:

`beta_i^2=sum_{j!=i}A_{ij}^2
          >= ell-ell^2 alpha^2
          >= ell(1-alpha^2)
          > (1/6)(1-1/4)=1/8`.                                             (3.7)

Here we used `ell<=1`, which follows because `U U^T` is an orthogonal projection.

Now put

`Z_i=(1/beta_i)sum_{j!=i}A_{ij}X_j`.                                      (3.8)

The coefficient vector in (3.8) has Euclidean norm one. Hence the Ball--Rogozin marginal theorem gives

`||p_{Z_i}||_infinity <= sqrt(2)`.                                         (3.9)

Set

`Y_i=sqrt(2) Z_i`.                                                         (3.10)

Then scaling gives `||p_{Y_i}||_infinity<=1`. Since `Y_i` uses only coordinates `X_j`, `j!=i`, it is independent of `X_i`. Expanding the quadratic form in the physical coordinate `i`,

`Q=d_i X_i^2 +2X_i sum_{j!=i}A_{ij}X_j+R_i
  =d_i X_i^2 +sqrt(2)beta_i X_iY_i+R_i`.                                 (3.11)

Thus `c_i=sqrt(2)beta_i>1/2` by (3.7). This proves the third branch. QED.

## 4. Spectral hyperbolic normal form behind the bank branch

The preceding physical-row identity has a useful exact spectral interpretation. In the bank branch, extend `r=u_i/sqrt(ell)` to an orthonormal spectral basis `(r,e_2,e_3)`. In that basis write

`Lambda=[[alpha,b^T],[b,C]]`.

Then

`||b||^2=r^T Lambda^2 r-alpha^2 >=1-alpha^2>3/4`.                         (4.1)

Rotate only the deterministic two-dimensional spectral complement so `b=(rho,0)`, `rho=||b||`; this is an algebraic change of basis, not a claim of independence of spectral coordinates. Because `u_i` is parallel to `r`, the two complementary spectral linear forms use only `X_{-i}`. The first spectral form is

`Z_1=sqrt(ell)X_i+L_1(X_{-i})`.

Consequently the `X_i`-dependent hyperbolic coefficient before cap-one normalization is exactly

`2 sqrt(ell) rho`,                                                        (4.2)

and after scaling the complementary linear form by `sqrt(2)` to cap its density by one it is

`sqrt(2 ell) rho >1/2`.                                                    (4.3)

This is the same lower bound as (3.11), because

`beta_i^2=u_i^T Lambda^2u_i-d_i^2
          =ell(r^TLambda^2r)-ell^2 alpha^2`,

while the spectral decomposition separates the Euclidean complement more finely. The key point is structural: near-isotropy of a heavy diagonal pivot does not make the row harmless; it forces a quantitatively large hyperbolic coupling into an original-coordinate linear bank.

## 5. Why this does not yet close the density theorem

A tempting but invalid next step would be to forget the provenance of `Y_i` and retain only `||p_{Y_i}||_infinity<=1`. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` shows that bounded marginal/conditional caps can coexist with a logarithmically unbounded hyperbolic output when the relevant receiver variables are correlated. Here `Y_i` and `R_i` are generally dependent.

What survives beyond that correction is stronger and source-valid: `Y_i` is **exactly a normalized linear image of the original independent coordinates**, with a coefficient vector of norm one, and `X_i` remains independent of the whole source bank. Any closure theorem must exploit that product-linear provenance before, or jointly with, the curved/hyperbolic trace.

## 6. Conditional end-to-end implication

For exact rank three, a complete proof would now follow from the single product-preserving statement below.

`QFORM-STRONG-BANK-HYPERBOLIC-PAYMENT-v1`:

> There exists a universal constant `C_bank` such that whenever `X` is an independent cap-one scalar, `Z=(Z_j)` is a vector of independent cap-one coordinates independent of `X`, `Y=sum a_j Z_j` with `||a||_2=1` (or, after normalization, density cap one), `|c|>=1/2`, and `R(Z)` is the quadratic residual forced by an exact-rank-three symmetric form, the law of
> 
> `d X^2+cXY+R(Z)`
> 
> has a universal bounded density, uniformly for `|d|` in the near-isotropic range produced above.

The theorem in this report proves that this bank statement is not an optional corner case: after the determinant-weighted disjoint-basis and nonisotropic-pivot branches, it is the quantitatively isolated exact-rank-three obstruction.

For the **full arbitrary-rank conjecture**, one must additionally preserve this reduction in the presence of arbitrary nonseparable small-eigenvalue residual coupling. The regularized-determinant theorem supplies a complete diffuse-range branch but does not yet remove that heavy-coordinate/nonseparable debt.

## 7. Continuity status

* Diffuse determinant branch (`delta>=1/8`): the partner's integrable Fourier argument yields a continuous density.
* Paid physical-pivot branch: the imported fleet03/B10 theorem establishes an essentially bounded density; continuity is not claimed there.
* Strong bilinear-bank branch: no density bound is proved here, so continuity is open as well.

## 8. Outcome

`ESSENTIAL_SUPPORTING_STEP / FULL_TARGET_OPEN`.

The new content is the quantitative conversion

`small disjoint-basis mass -> heavy physical row -> either |d|ell is uniformly paid, or beta_offdiag^2>1/8`,

followed by the exact cap-one hyperbolic-bank normalization with coefficient `>1/2`. This converts the previously qualitative localized branch into a concrete original-coordinate inequality and isolates the next product-preserving payment problem.
