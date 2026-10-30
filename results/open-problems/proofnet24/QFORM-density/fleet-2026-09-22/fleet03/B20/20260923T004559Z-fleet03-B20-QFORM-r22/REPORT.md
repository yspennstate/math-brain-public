SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B20, 2026-09-23T00:45:59Z.
attacking: the fresh B19 robust 2+1 grouped O3 survivor by conditioning the unused rank-one companion, applying fleet04/B20's conditioned-whitened diffuse theorem, and converting failure of whitened diffuseness into a quantitative original-coordinate cross star.

# fleet03/B20 r22 — robust 2+1 grouped block: diffuse payment or a physical cross star

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`  
Classification: `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING REDUCTION / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Scope and source boundary

The unrestricted target remains open: for every dimension, every independent real input with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `Q=X^TAX`, or give a valid counterexample. Full-target continuity is separately open.

This run uses the fresh fleet03/B19 r20 exact-rank-three O3 reduction. In its remaining exactly-one-internal-rank-two chamber there are disjoint original-coordinate banks `H_1,H_2,G`, with `H_1,H_2` spectrally rank one and `G` spectrally rank two. Write the exact selected rank-three form as

`A = R M R^T`, `R^T R = I_3`, `s_min(M)>=1`, hence `|det M|>=1`.

For `a=1,2`, rows in `H_a` are collinear with a unit vector `v_a`, and their squared coefficient mass is `lambda_a`. The internal bank has frame

`S_G = I - lambda_1 v_1v_1^T - lambda_2 v_2v_2^T`.

The fresh B19 theorem proves, in the unpaid rank-two-internal branch, that `rank(S_G)=2`; its nonzero eigenvalues are `1,tau`, with `tau>1/3`; and for

`L_a = [sqrt(lambda_a)v_a, W]`, `W W^T=S_G`,

`det(L_a)^2 = 1-lambda_b` for `{a,b}={1,2}`. Since `(1-lambda_1)+(1-lambda_2)=tau>1/3`, one may choose `a` so that

`delta := 1-lambda_b = det(L_a)^2 > 1/6`.                         (1.1)

The preceding B19 near-null reduction also gives, for both rank-one companions,

`theta_a=lambda_a |a_a| |det M| < 1/4096`,
`a_a=lambda_a v_a^T M v_a`.                                     (1.2)

Sources consumed:

- fleet03/B19 r19 rank-one-bank pivot theorem, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T223200Z-fleet03-B19-QFORM-r19/REPORT.md`, with the proved bound
  `||p_Q||_inf <=16 sqrt(60) [lambda |a| |det M|]^(-1/4)` for a nonzero rank-one-bank scalar pivot.
- designated partner fleet04/B20 r2, `QFORM-CONDITIONED-WHITENED-DIFFUSE-v1`, canonical `yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f`. If original-coordinate conditioning leaves frame Gram `S` with `delta=lambda_min(S)>0` and every residual whitened row leverage at most `1/32`, then the full conditional/unconditional form has a continuous density with
  `||p_Q||_inf <= 96e/(7 sqrt(2) delta) < 27/delta`.

No post-rotation independence, arbitrary-joint coarea, conditional-density-cap substitute, pointwise van-der-Corput decay, fixed-good-minor extraction, or fiber supremum is used.

## 2. Exact residual frame after conditioning the unused companion

Choose the companion `H_a` satisfying (1.1), and condition only the original coordinates in the other companion bank `H_b`. Put

`R_0 = H_a union G`.

The residual selected-frame Gram is exactly

`S := R_{R_0}^T R_{R_0}`
`   = I - lambda_b v_bv_b^T`.                                    (2.1)

Thus `S` has eigenvalues `1,1,delta`, with `delta>1/6`. In particular it is positive definite. Define the whitened residual frame and the compressed spectral coefficient matrix by

`V = R_{R_0} S^(-1/2)`,
`N = S^(1/2) M S^(1/2)`.                                        (2.2)

Then

`V^T V=I_3`,
`A[R_0,R_0] = V N V^T`,
`s_min(N) >= s_min(S^(1/2))^2 s_min(M) >= delta`.                (2.3)

For each `i in R_0`, write its original selected spectral row as `u_i` and its whitened row as

`w_i=S^(-1/2)u_i`,
`h_i=||w_i||^2=u_i^T S^(-1)u_i`.                                (2.4)

## 3. Main theorem: diffuse payment or a quantitative physical row

### Theorem `QFORM-O3-ROBUST-2PLUS1-DIFFUSE-OR-PHYSICAL-STAR-v1`

In the inherited O3 chamber above, one of the following holds.

**(D) Conditioned-whitened diffuse branch.**

`max_(i in R_0) h_i <=1/32`.

Then `Q` has a continuous density and

`||p_Q||_inf <= 96e/(7 sqrt(2) delta) < 162`.                    (3.1)

**(P) Paid physical scalar pivot.** There is an original coordinate `i in R_0` with

`h_i>1/32`, `||u_i||^2>1/192`, `|A_ii|>=1/48`,                  (3.2)

and therefore

`||p_Q||_inf <1215`.                                             (3.3)

**(S) Localized cross-star survivor.** There is an original coordinate `i in R_0` with

`h_i>1/32`, `||u_i||^2>1/192`, `|A_ii|<1/48`,
`||A[i,R_0\{i}]||_2 >1/48`.                                    (3.4)

Consequently every still-unpaid member of this fresh O3 chamber lies in (S).

#### Proof

If `max h_i<=1/32`, apply the designated partner fleet04/B20 conditioned-whitened theorem to the genuine original-coordinate conditioning set `H_b`. Since `lambda_min(S)=delta>1/6`,

`||p_Q||_inf <=96e/(7sqrt(2)delta) < 6*96e/(7sqrt(2))`
`=158.162649...<162`,                                             (3.5)

and that theorem also supplies continuity. This proves (D).

Assume instead that some `i` has `h_i>1/32`. Since `S>=delta I`,

`h_i=u_i^T S^(-1)u_i <= delta^(-1)||u_i||^2`,

hence

`||u_i||^2 >= delta h_i > (1/6)(1/32)=1/192`.                   (3.6)

Now use (2.3). Because `V^T V=I`, the squared Euclidean norm of row `i` of the residual physical matrix is

`sum_(j in R_0) A_ij^2`
` = e_i^T (VNV^T)^2 e_i`
` = w_i^T N^2 w_i`
` >= delta^2 ||w_i||^2`
` > (1/6)^2(1/32)=1/1152`.                                      (3.7)

If `|A_ii|>=1/48`, regard the singleton `{i}` as a rank-one bank in the B19 r19 pivot theorem. Its bank mass is exactly `lambda=||u_i||^2`; using (3.6), `|det M|>=1`, and `|A_ii|>=1/48`,

`lambda |A_ii| |det M| > 1/(192*48)=1/9216`.                    (3.8)

Therefore

`||p_Q||_inf`
` <=16sqrt(60) * 9216^(1/4)`
` =16sqrt(60)sqrt(96)`
` =384sqrt(10)`
` =1214.314... <1215`.                                           (3.9)

This is (P).

Otherwise `|A_ii|<1/48`. Subtracting the diagonal square from (3.7),

`||A[i,R_0\{i}]||_2^2`
` =sum_(j in R_0)A_ij^2-A_ii^2`
` >1/1152-1/2304`
` =1/2304`,                                                       (3.10)

so the active physical cross star has norm `>1/48`. This is (S). QED.

## 4. Sharpening the star by the inherited near-null companion information

The survivor (S) can be localized further without any rotation of the product law.

### Proposition 4.1 — companion-heavy rows point into the internal bank

If the heavy coordinate `i` in (S) belongs to the chosen rank-one companion bank `H_a`, then

`||A[i,G]||_2 >1/49`.                                            (4.1)

#### Proof

First, (1.1) and Hadamard's determinant inequality imply `lambda_a>1/6`. Indeed `det(L_a)^2<=lambda_a det(W^T W)=lambda_a tau<=lambda_a`.

From (1.2) and `|det M|>=1`,

`lambda_a |a_a| <1/4096`,

hence, since `lambda_a>1/6`,

`|a_a|<6/4096=3/2048`.                                          (4.2)

For rows `i,j in H_a`, write `u_i=c_i v_a`, `u_j=c_j v_a`. Then

`A_ij=c_i c_j t_a`, `t_a=v_a^T M v_a`,

and therefore

`||A[i,H_a\{i}]||_2`
` <= |c_i||t_a| sqrt(lambda_a)`
` <= lambda_a |t_a|`
` = |a_a|`
` <3/2048`.                                                       (4.3)

The supports `H_a\{i}` and `G` are disjoint, so by (3.10)

`||A[i,G]||_2^2`
` >1/48^2-(3/2048)^2`
` >1/49^2`,                                                       (4.4)

where the final difference is exactly

`1/48^2-(3/2048)^2-1/49^2`
`=1394767/90634715136 >0`.                                       (4.5)

This proves (4.1). QED.

### Proposition 4.2 — internal-heavy rows give a two-channel physical star

If the heavy coordinate `i` in (S) belongs to `G`, then, because the active star splits over the disjoint banks `H_a` and `G\{i}`,

`max{ ||A[i,H_a]||_2, ||A[i,G\{i}]||_2 } > 1/(48sqrt(2)).`       (4.6)

This is immediate from (3.10): if both terms were at most `1/(48sqrt(2))`, their squared sum would be at most `1/2304`.

Thus the fresh B19 robust 2+1 grouped branch has been reduced to a product-preserving **physical-star** obstruction with fixed strength. It is no longer necessary to solve the fully diffuse grouped projection case: fleet04/B20 r2 pays that case directly.

## 5. Designated-partner application at an actual inequality

The assigned partner is fleet04/B20. Its completed r2 theorem is used at equation (3.5), not cited abstractly. The inherited frame identity (2.1) gives the theorem's exact conditioning parameter

`delta=lambda_min(S)=1-lambda_b>1/6`,

while its hypothesis is precisely the current residual whitened leverage test

`max_i u_i^T S^(-1)u_i<=1/32`.

Substitution yields the explicit continuous-density estimate `<162`. Failure of that partner hypothesis is then converted by (3.6)--(3.10) into the physical-star survivor; no partner hypothesis is extended outside its proved scope.

## 6. What is now unpaid

The first unpaid implication in this chamber is

`QFORM-O3-ROBUST-PHYSICAL-STAR-PAYMENT-v1`:

pay, with one universal constant and without post-projection independence, an exact-rank-three O3 state having the selected residual Gram floor `delta>1/6` and an original coordinate satisfying either

1. companion-to-internal star: `i in H_a` and `||A[i,G]||_2>1/49`; or
2. internal two-channel star: `i in G` and
   `max{||A[i,H_a]||_2,||A[i,G\{i}]||_2}>1/(48sqrt(2))`,

while the diagonal at that physical row is `<1/48`.

The natural next mechanism is aggregate hyperbolic-square / pair-log smoothing on the whole star before any reciprocal coefficient is selected. This is compatible with fleet04/B20 r1, but this report does not claim the required disjoint-square extraction.

## 7. Status and nonclaims

Proved here: `QFORM-O3-ROBUST-2PLUS1-DIFFUSE-OR-PHYSICAL-STAR-v1`, Proposition 4.1, and Proposition 4.2.

Applied designated partner: fleet04/B20 r2 at the exact residual conditioning inequality.

Not proved: the physical-star payment in Section 6, the other O0/O3 packets, the unrestricted QFORM conjecture, or full-target continuity.

The new diffuse subbranch has a continuous density. The scalar-pivot subbranch has the essential bound inherited from B19 r19; no new continuity claim is added there.
