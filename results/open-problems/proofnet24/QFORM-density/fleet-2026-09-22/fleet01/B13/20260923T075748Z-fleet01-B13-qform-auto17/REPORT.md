SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T07:57:48Z.
attacking: the two-hub/transverse-star survivor by a positive-kernel half-Riesz endpoint and an exact rank-one-tube compression of the designated partner's Schur exterior identity.

# fleet01/B13 auto17 — null-Schur mixed-edge payment and transverse-star rank-one compression

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws  
Status: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL THEOREMS / FULL_QFORM_OPEN / CONTINUITY_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact target remains unrestricted: independent original-coordinate real variables with densities at most one; arbitrary dimension; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moments, centering, support diameter, interval structure, log-concavity, post-rotation independence, or continuity assumption is introduced.

The live corrections are respected: there is no law-uniform pointwise quadratic Fresnel decay; rotations are not used to preserve independence; projection-density bounds are not substituted for an indefinite quadratic pushforward; arbitrary-joint coarea and positive conditional-projection-moment shortcuts are not used; small matrix coefficients are not deleted perturbatively on translated/fragmented supports.

Completed source actually applied below: designated partner `fleet02/B13` r23, canonical mathematics `yspennstate/math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T040105Z-fleet02-B13-extremal-r23/REPORT.md`. Its exact rank-one Schur `E_2`-loss identity is used in Section 5 at an actual inequality. The previous fleet01/B13 auto16 source is `yspennstate/math-open-problems@8b002eaeebab0b09362bc2f258e2f5dfd62e15ce`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T063002Z-fleet01-B13-qform-auto16/REPORT.md`.

## 1. Extremal product front end retained exactly

For every bounded nonnegative measurable kernel `K` on `R^n`, the coordinatewise bathtub principle gives

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_1|=...=|E_n|=1} int_{prod_i E_i} K(x) dx`.            (1.1)

This is equality of suprema over arbitrary measurable unit-measure sets. It does not select one interval, a centered uniform law, bounded diameter, or a fixed number of fragments. The proof was written in full in auto16; it is retained here because every new density estimate below therefore has an exact geometric product-set form for slab kernels.

## 2. A sharp one-dimensional half-Riesz cap

### Lemma 2.1 — `QFORM-CAP-HALFRIESZ-ONE-D-v1`

If a real random variable `Y` has density bounded by `L`, then

`sup_t E |Y-t|^{-1/2} <= 2 sqrt(2L)`.                              (2.1)

Proof. For fixed `t`, the kernel `|y-t|^{-1/2}` is symmetric decreasing away from `t`. Among probability densities bounded by `L`, the bathtub principle maximizes its integral by density `L` on the centered interval of length `1/L`. Thus

`E|Y-t|^{-1/2}
 <= L int_{-1/(2L)}^{1/(2L)} |u|^{-1/2}du
 =2 sqrt(2L)`.                                                     (2.2)

No support or moment assumption is used. QED.

## 3. Affine bilinear variables have a uniform half-Riesz potential

### Theorem 3.1 — `QFORM-AFFINE-BILINEAR-HALFRIESZ-v1`

Let `U,V` be independent real random variables with density caps `M_U,M_V`. For `c!=0` and arbitrary real `alpha,beta,gamma`, put

`Z=2cUV+alpha U+beta V+gamma`.                                    (3.1)

Then

`boxed:
 sup_t E|Z-t|^{-1/2}
 <=4 sqrt(2) (M_U M_V)^{1/2}|c|^{-1/2}.
`                                                                     (3.2)

Proof. Condition on `U=u`. Except at the single value where `2cu+beta=0`, which is null because `U` is absolutely continuous, the conditional variable is an affine image of `V` with density cap

`M_V/|2cu+beta|`.

Lemma 2.1 therefore gives

`E[|Z-t|^{-1/2}|U=u]
 <=2 sqrt(2M_V) |2cu+beta|^{-1/2}`.                               (3.3)

The variable `2cU+beta` has density cap `M_U/(2|c|)`. Apply Lemma 2.1 again:

`E|2cU+beta|^{-1/2}
 <=2 sqrt(M_U/|c|)`.                                               (3.4)

Multiplying (3.3)-(3.4) proves (3.2), uniformly in `t,alpha,beta,gamma`. QED.

This is deliberately a positive-kernel argument. It does not claim that the affine bilinear density itself is bounded; the familiar logarithmic singularity remains possible. What is uniformly bounded is exactly the half-Riesz potential needed by one additional genuine square innovation.

## 4. New target-level endpoint: one physical square plus an exact null-Schur mixed edge

Fix three distinct original coordinates `k,i,j` and let

`d=A_kk !=0`.

Write the scalar Schur complement after pivoting only the original coordinate `k` as

`S=A[-k,-k]-A[-k,k]A[k,-k]/d`.                                  (4.1)

Assume

`S_ii=S_jj=0`, `c:=S_ij!=0`.                                    (4.2)

### Theorem 4.1 — `QFORM-OUTER-SQUARE-ZERODIAG-EDGE-v1`

For arbitrary independent cap-one inputs and arbitrary remaining coefficients of `A`,

`boxed:
 ||p_{X^TAX}||_infinity <=4 sqrt(2)|dc|^{-1/2}.
`                                                                     (4.3)

Proof. Complete the square in the original coordinate `X_k`:

`Q=d (X_k+d^{-1}A[k,-k]X_-k)^2 + R`,
`R=X_-k^T S X_-k`.                                                  (4.4)

Conditional on all `X_-k`, the translated scalar in parentheses has density cap one, hence the conditional density of its `d`-weighted square is bounded by

`|d|^{-1/2}|u|^{-1/2}`                                            (4.5)

on the appropriate sign half-line. Mixture therefore gives, for every `t`,

`p_Q(t)<=|d|^{-1/2} E|t-R|^{-1/2}`.                              (4.6)

Now condition on every original coordinate other than `i,j` inside the remainder. Because of (4.2), the active two-variable remainder is exactly

`R_W=2cX_iX_j+alpha_W X_i+beta_W X_j+gamma_W`,                   (4.7)

where the coefficients may depend arbitrarily on the conditioned coordinates. The two active variables remain independent with density caps one. Theorem 3.1, uniformly in all affine coefficients, gives

`sup_t E[|t-R_W|^{-1/2}|W] <=4sqrt(2)|c|^{-1/2}`.                (4.8)

Average over `W` and substitute into (4.6). QED.

The theorem has a clean original-matrix formulation. Define the anchored mixed `2x2` determinant

`Delta_{k;i,j}:=det A[{k,i},{k,j}]
               =d A_ij-A_ik A_kj
               =d S_ij`.                                         (4.9)

The null-Schur conditions are exactly

`det A[{k,i},{k,i}]=0`, `det A[{k,j},{k,j}]=0`.                  (4.10)

Hence, if the two anchored principal minors in (4.10) vanish while `Delta_{k;i,j}!=0`, then

`boxed:
 ||p_Q||_infinity <=4sqrt(2)|Delta_{k;i,j}|^{-1/2}.
`                                                                     (4.11)

No dependence on dimension, on the other coefficients, or on the support geometry of the marginal laws occurs.

By (1.1), the exact geometric slab version is: for arbitrary measurable `|E_l|=1` and every interval `J`,

`boxed:
 |{x in prod_l E_l : x^T A x in J}|
 <=4sqrt(2)|Delta_{k;i,j}|^{-1/2}|J|.
`                                                                     (4.12)

Thus an exact-null scalar-Schur chamber is not automatically hard: two null rays with a nonzero mixed anchored determinant are completely paid. A genuinely unpaid exact-null survivor must have the corresponding anchored mixed determinants vanish along every candidate null pair.

## 5. Designated-partner application: a destroyed Schur `E_2` bank is quantitatively a transverse rank-one tube

The auto16 obstruction still had an apparently arbitrary `transverse-star` alternative. The partner's exact exterior identity lets us sharpen it.

Let a physical cross block before scalar Schur descent be

`N=S+xy^T`,                                                        (5.1)

and put

`E_0=e_2(N^T N)=||wedge^2 N||_F^2`,
`E=e_2(S^T S)=||wedge^2 S||_F^2`.                                (5.2)

For nonzero `x,y`, set

`T=P_{x^perp} S P_{y^perp}`,
`L=||x||^2||y||^2`,
`F^2=||T||_F^2`.                                                   (5.3)

The designated partner `fleet02/B13` proves the exact identity

`D_*^2:=||wedge^2 N-wedge^2 S||_F^2
       =L F^2`.                                                     (5.4)

It also gives

`sqrt(E_0)<=sqrt(E)+D_*`.                                         (5.5)

Hence in the Schur-destruction branch

`E<E_0/4`,                                                         (5.6)

we have

`D_*^2>E_0/4`, and therefore

`F^2>E_0/(4L)`.                                                    (5.7)

The following elementary singular-value inequality is the new step. For every matrix `T`, if

`tau_1(T):=inf_{rank R<=1} ||T-R||_F^2`,                          (5.8)

then

`boxed:
 tau_1(T) <= 2 e_2(T^T T)/||T||_F^2.
`                                                                     (5.9)

Indeed, with `lambda_1>=lambda_2>=...` the squared singular values, `F^2=sum lambda_i` and `tau_1=sum_{i>=2}lambda_i`. Since

`2e_2=F^4-sum_i lambda_i^2`,

`2e_2-tau_1 F^2
 =lambda_1 F^2-sum_i lambda_i^2
 =sum_i lambda_i(lambda_1-lambda_i)>=0`.                           (5.10)

Orthogonal projections are contractions on the second exterior power, so

`e_2(T^T T)=||wedge^2(P_{x^perp}SP_{y^perp})||_F^2<=E`.           (5.11)

Combine (5.4), (5.9), and (5.11):

`tau_1(T)
 <=2E/F^2
 =2EL/D_*^2`.                                                      (5.12)

Under the actual partner destruction inequality (5.7), this becomes

`boxed:
 tau_1(T)<8 E L/E_0.
`                                                                     (5.13)

This is `QFORM-TRANSVERSE-STAR-RANKONE-TUBE-v1`. It is an equation-level application of the designated partner result: the old qualitative `star currency` has been converted into a quantitative best-rank-one tube in the first genuinely hard regime.

A convenient scale-free form follows by dividing by `F^2` and using (5.7):

`boxed:
 tau_1(T)/||T||_F^2
 <32 E L^2/E_0^2.
`                                                                     (5.14)

Thus, for any `0<eta<1`, if

`E L^2/E_0^2 <= eta/32`,                                          (5.15)

then more than a fraction `1-eta` of the transverse-star Frobenius energy lies in one singular direction:

`tau_1(T)<eta ||T||_F^2`,
`sigma_1(T)^2>(1-eta)E_0/(4L)`.                                  (5.16)

The star alternative is therefore not an arbitrary high-rank object once its surviving `E_2` currency is genuinely small: it is a quantitatively strong rank-one grouped bank plus a controlled Frobenius tail.

## 6. Refined survive / two-hub / rank-one-tube trichotomy

Combine Section 5 with auto16's `h<1` entropic `E_2` theorem for the actual scalar-Schur block `S`. In the destruction branch (5.6), take `eta=1/2`.

If

`E L^2/E_0^2 >=1/64`,                                             (6.1)

then either the entropy branch already pays, or the actual Schur `E_2` mass is concentrated on at most two physical row hubs and at most two physical column hubs. In the paid subcase, auto16's constant gives

`||p_Q||_infinity
 <=17.086318 |d|^{-1/2}E^{-1/8}
 <=17.086318*64^{1/8}|d|^{-1/2}L^{1/4}E_0^{-1/4}`

and therefore

`boxed:
 ||p_Q||_infinity
 <=28.735648 |d|^{-1/2}L^{1/4}E_0^{-1/4}.
`                                                                     (6.2)

If instead

`E L^2/E_0^2 <1/64`,                                               (6.3)

then (5.14)-(5.16) give

`boxed:
 tau_1(T)<(1/2)||T||_F^2,
 sigma_1(T)^2>E_0/(8L).
`                                                                     (6.4)

So the prior three-way obstruction has been sharpened. After the diffuse density exits, every remaining scalar-Schur `E_2` failure is now localized to either a finite two-by-two physical hub packet or a quantitatively strong transverse rank-one tube. The exact-null physical mixed-edge endpoint of Section 4 is separately paid whenever it occurs.

This is structural progress, not a full proof: neither a small Frobenius tail nor a finite hub packet may simply be deleted under arbitrary translated/fragmented product laws. The remaining grouped rank-one core can resonate with same-bank quadratic curvature, so it still needs a product-preserving third-direction mechanism.

## 7. First unpaid implication after this run

`QFORM-TWOHUB-RANKONE-TUBE-CLOSURE-v1`:

Starting from the finite two-row/two-column hub packet or the quantitative transverse rank-one tube (5.16), use the third large spectral direction to force one already-paid physical-square, indefinite-pair, grouped-rank-two, ridge-window, or exact-null mixed-edge certificate, while retaining the Frobenius tail inside the estimate rather than dropping it perturbatively. A valid counterexample would instead have to survive the exact product-indicator reduction (1.1), the null-Schur determinant gate (4.11), and the partner-compressed rank-one-tube alternative simultaneously.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. The separate continuous-density conclusion remains OPEN.