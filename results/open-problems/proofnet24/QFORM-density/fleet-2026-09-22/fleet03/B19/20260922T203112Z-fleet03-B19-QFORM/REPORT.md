SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-22T20:31:12Z.
attacking: the zero/near-zero O0 branch by extracting two independent transverse product banks in the exact-null diffuse state and a quantitative star/residual certificate for the near-null full-matrix state.

# fleet03/B19 — diffuse null-row two-bank partition and near-null star certificate

**Run:** `20260922T203112Z-fleet03-B19-QFORM`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Fresh owner revision:** `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREMS PROVED / FULL TARGET OPEN`.

## 1. Exact target and correction boundary

The target remains: for arbitrary finite `n`, independent real coordinates with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` satisfying `s_3(A)>=1`, prove one universal finite essential bound for the density of `Q=X^TAX`, or construct a target-valid counterexample. Continuity is tracked separately.

This report does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, the false arbitrary-joint rank-three coarea inequality, positive conditional projection-density moments, a fixed good physical minor, or the refuted rule that a merely near-zero pivot may be replaced by an exact-zero half-Riesz endpoint.

The previous B19 run closed the inherited **nonzero** O0 transverse branch by a mixed-exponent product-bank Brascamp--Lieb estimate. Its first unpaid state was the zero/near-zero pivot branch. Fresh completed fleet work further isolates the exact-null exact-rank-three endpoint: fleet02/B10 proves that a heavy null row plus any complementary row of residual leverage `>1/2` is already paid. Therefore the exact-null survivor is the residual-diffuse chamber in which every transverse physical row has squared leverage at most `1/2`.

The present run changes mechanism. It does not perturb an exact null pivot. Instead it proves a quantitative **two independent bank decomposition** of every such diffuse transverse Parseval frame. Separately, for the genuinely near-null full-matrix state it proves a spectral-leverage star certificate that is stable under arbitrary extra spectrum.

## 2. Completed inputs actually used

1. **Residual-diffuse null-row reduction.** fleet02/B10, `QFORM-NULL-ROW-NESTED-HEAVY-CLOSURE-v1`, current source path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T193653Z-fleet02-B10-QFORM-r15/REPORT.md`.

Inside exact rank three, after a heavy exact-null row is fixed, it closes every branch containing a complementary row with residual two-plane leverage `>1/2`. Thus the unpaid exact-null state satisfies `||v_j||^2<=1/2` for every residual transverse row `v_j` and `sum_j v_j v_j^T=I_2`.

2. **Weighted product projection.** fleet02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an orthonormal `k`-dimensional original-coordinate projection, the projected density is at most `exp(k/2)`.

3. **Full-matrix indefinite physical pair theorem.** canonical source

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If `s_3(A)>=sigma`, an original-coordinate principal pair `B` is invertible indefinite, `D=|det B|`, and `kappa=sigma_min(B)`, then

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa sigma)^(-1/6)`.

4. **Designated partner fleet04/B19.** `QFORM-FINITE-UNION-CORE-v1`, canonical source

`yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`.

For every measurable output map and interval, the supremum over arbitrary independent cap-one input densities equals the supremum over product indicator laws on bounded finite unions of intervals of measure one. This will be applied to the actual pair inequality in Section 5.

## 3. A two-bank partition theorem for a diffuse two-dimensional Parseval frame

### Theorem 3.1 — `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`

Let `v_1,...,v_m in R^2` satisfy

`sum_i v_i v_i^T = I_2`,

and assume

`h_i:=||v_i||^2 <=1/2` for every `i`.

Then the indices admit a partition `J disjoint K={1,...,m}` such that, with

`S_J=sum_(i in J) v_i v_i^T`,
`S_K=sum_(i in K) v_i v_i^T=I_2-S_J`,

one has

`boxed( det S_J * det S_K >=1/640 )`,                         (3.1)

and consequently

`boxed( det S_J>=1/640, det S_K>=1/640,`
`       lambda_min(S_J)>=1/640, lambda_min(S_K)>=1/640. )`    (3.2)

The partition is on **original coordinate indices**. Hence random vectors built from the two banks are genuinely independent.

#### Proof

For `i<j` define the Pluecker weight

`w_ij := det(v_i,v_j)^2 >=0`.                                  (3.3)

Cauchy--Binet gives

`sum_(i<j) w_ij = det(sum_i v_i v_i^T)=1`.                    (3.4)

There is also an exact degree identity. Let `J_0` be the ninety-degree rotation on `R^2`. Then

`sum_(j!=i) w_ij`
`= (J_0 v_i)^T [sum_(j!=i)v_jv_j^T](J_0v_i)`
`= (J_0v_i)^T(I_2-v_iv_i^T)(J_0v_i)`
`=||v_i||^2=h_i`,                                              (3.5)

because `J_0v_i` is perpendicular to `v_i`. In particular

`sum_i h_i=2`.                                                  (3.6)

Choose a random partition by independent fair Bernoulli variables `xi_i`, with `i in J` iff `xi_i=1`. Two-dimensional Cauchy--Binet gives

`det S_J=sum_(i<j) xi_i xi_j w_ij`,
`det S_K=sum_(k<l)(1-xi_k)(1-xi_l)w_kl`.                       (3.7)

Only disjoint edge pairs survive in the product. Put

`D:=sum_(e,f: e cap f=empty) w_e w_f`,                         (3.8)

where the sum is over ordered edge pairs. Then

`E[det S_J det S_K]=D/16`.                                    (3.9)

It remains to bound `D` below. Put

`S=sum_i h_i^2`, `W=sum_e w_e^2`.

The total weight of ordered edge pairs is one. The weight of ordered pairs sharing at least one endpoint is `S-W`: `S` counts a repeated edge twice, once at each endpoint, so one copy `W` must be subtracted. Therefore

`D=1-S+W`.                                                     (3.10)

If `1-S>=1/16`, then `D>=1/16` and we are done. Assume instead

`1-S<1/16`.                                                     (3.11)

Using (3.6),

`1-S=sum_i h_i(1/2-h_i)`.                                     (3.12)

Let

`H={i:h_i>3/8}`.

For `i notin H`, `1/2-h_i>=1/8`, so (3.11)-(3.12) imply

`sum_(i notin H)h_i <1/2`.                                    (3.13)

Also `|H|<=5`, since every member has degree greater than `3/8` while the total degree is two. The total edge weight touching `H^c` is at most the degree mass in (3.13). Thus the total weight of edges entirely inside `H` is greater than `1/2`. There are at most `binom(5,2)=10` such edges, and Cauchy--Schwarz gives

`W >= sum_(e subset H) w_e^2`
`  > (1/2)^2/10 =1/40`.                                       (3.14)

Equations (3.10)-(3.14) yield `D>1/40`. Hence in every case

`D>=1/40`.                                                      (3.15)

By (3.9), `E[det S_J det S_K]>=1/640`, so some partition satisfies (3.1). Since `0<=S_J,S_K<=I_2`, both determinants are at most one; therefore each is at least `1/640`. For a positive semidefinite `2x2` contraction, `lambda_min=det/lambda_max>=det`, proving (3.2). QED.

### Corollary 3.2 — two independent transverse density packets

Let the original coordinates in the two banks be independent cap-one variables and define

`Y_J=sum_(i in J) v_i X_i`,
`Y_K=sum_(i in K) v_i X_i`.

Then `Y_J` and `Y_K` are independent `R^2`-valued random vectors and each has a joint density satisfying

`boxed( ||p_(Y_J)||_infinity, ||p_(Y_K)||_infinity <= e sqrt(640) <68.768. )` (3.16)

Proof. For `G=J` or `K`, let `V_G` be the matrix with rows `v_i`, so `V_G^T V_G=S_G`. Put `R_G=V_G S_G^(-1/2)`. Then `R_G^T R_G=I_2`, hence the weighted affine-fiber theorem gives the density of `S_G^(-1/2)Y_G=R_G^T X_G` the cap `e`. Scaling back multiplies the cap by `det(S_G)^(-1/2)<=sqrt(640)`. Independence follows because `J,K` are disjoint original-coordinate sets. QED.

This is stronger than saying that the two-dimensional residual projection is globally diffuse: it manufactures **two separate, genuinely independent, quantitatively nondegenerate physical-coordinate packets**.

## 4. Application to the exact-null residual-diffuse endpoint

Use the exact-rank-three heavy-null basis from the completed B10/B01 work. A heavy physical row is `sqrt(c) r`, and after writing the other spectral rows as

`u_j=alpha_j r + beta_j e + gamma_j w`,

Parseval gives

`sum_j (beta_j,gamma_j)(beta_j,gamma_j)^T=I_2`.                 (4.1)

The B10 nested-heavy theorem has already paid every branch in which

`beta_j^2+gamma_j^2>1/2`                                      (4.2)

for some complementary physical row. Therefore every surviving exact-null residual-diffuse state satisfies the hypotheses of Theorem 3.1 with

`v_j=(beta_j,gamma_j)`.                                        (4.3)

Consequently there is an original-coordinate partition `J,K` for which both transverse frame matrices dominate `(1/640)I_2`, and the two projected packets `(L_J,Z_J)` and `(L_K,Z_K)` are independent with joint density caps below `68.768`.

This removes a genuine global ambiguity from `QFORM-NULLROW-RESIDUAL-DIFFUSE-OVERLAP-v1`: the unpaid state can no longer hide all two-dimensional transverse curvature in one inseparable product bank. It always contains **two independent transverse banks**. What remains is exactly the leakage splice: the longitudinal coefficients `alpha_j` live inside the same two banks and enter the null form through the term `2s A L`. A valid next proof must use the two independent vector packets while retaining those `alpha`-leakage variables, rather than conditioning on them and inserting a false conditional projection-density cap.

The new first exact-null implication is therefore

`QFORM-NULLROW-TWO-BANK-LEAKAGE-PAYMENT-v1`:

> Starting from two disjoint original-coordinate banks whose transverse `2x2` frame matrices each dominate `(1/640)I_2`, prove a universal density bound for the heavy-null quadratic form while retaining the longitudinal leakage coordinates exactly.

The exact-null issue is thus no longer a bank-extraction problem; it is a two-bank analytic splice problem.

## 5. Full-matrix near-null star/residual certificate

The genuinely near-zero but nonzero pivot cannot be obtained by perturbing the exact-zero theorem. The following full-matrix lemma gives the stable resource that survives instead.

### Theorem 5.1 — `QFORM-HIGH-LEVERAGE-NEARNULL-STAR-v1`

Let `A` be any real symmetric matrix with `s_3(A)>=1`. Choose any three orthonormal eigenvectors whose eigenvalues have modulus at least one, and let `P` be their spectral projector. For a physical coordinate `i`, put

`c=P_ii`, `a=A_ii`, `b=A_(i,-i)`, `C=A_(-i,-i)`.

Then

`boxed( ||b||_2^2 >= c-a^2, )`                                (5.1)

and

`boxed( ||C||_op >=1. )`                                      (5.2)

In particular, if

`c>=7/9`, `|a|<=1/4`,                                          (5.3)

then

`boxed( ||b||_2 >= sqrt(103)/12 =0.8457409637... )`.           (5.4)

#### Proof

For the standard basis vector `e_i`, spectral decomposition gives

`||A e_i||_2^2=sum_k lambda_k^2 |<e_i,u_k>|^2 >=c`,            (5.5)

using only the selected three eigenvalues. Since `Ae_i=(a,b)^T`, (5.1) follows.

Embed `C` as `C_0=diag(0,C)`. Then

`A-C_0=[[a,b^T],[b,0]]`                                       (5.6)

has rank at most two. By the Eckart--Young characterization of the third singular value,

`1<=s_3(A)<=||A-(A-C_0)||_op=||C_0||_op=||C||_op`,             (5.7)

proving (5.2). Finally

`c-a^2 >=7/9-1/16=103/144`,                                   (5.8)

which gives (5.4). QED.

Thus a high-leverage near-null pivot always carries **two simultaneous full-target resources**: an original-coordinate star of norm at least `0.8457` and a complementary principal residual with operator norm at least one. No exact-rank-three assumption is used, and arbitrary extra spectrum is allowed.

### Paid local atom subbranch

Under (5.3), suppose there is a physical `j!=i` with

`|A_ij|>=1/2`, `|A_jj|<=1/4`.                                  (5.9)

The physical principal pair

`B=[[A_ii,A_ij],[A_ij,A_jj]]`

is indefinite because

`det B <= |A_ii A_jj|-A_ij^2 <=1/16-1/4=-3/16`.               (5.10)

Hence

`D=|det B|>=3/16`.                                             (5.11)

Relative to `[[0,A_ij],[A_ij,0]]`, the diagonal perturbation has operator norm at most `1/4`; therefore Weyl's singular-value inequality gives

`kappa=sigma_min(B)>=1/2-1/4=1/4`.                             (5.12)

The completed full-matrix pair theorem, with `s_3(A)>=1`, yields

`boxed( ||p_Q||_infinity`
` <=3*400^(1/3)[(3/16)^2(1/4)]^(-1/6)`
` =48.6576159645... <49. )`                                   (5.13)

This branch allows arbitrary dimension, arbitrary signs outside the pair, arbitrary extra spectrum, and arbitrary cap-one product laws.

Therefore an unpaid high-leverage near-null state must satisfy at least one of the following: the star is genuinely diffuse at the `1/2` atom scale, or every star atom of magnitude at least `1/2` sits on a physical diagonal of magnitude greater than `1/4`. Together with (5.2), this is a sharper scale bridge than merely saying that the pivot is small.

## 6. Designated partner fleet04/B19 applied to an actual inequality

The partner theorem `QFORM-FINITE-UNION-CORE-v1` applies to the measurable map `Phi(x)=x^TAx` and every interval `I`. On the paid local-atom branch (5.9), the finite-union product core satisfies the actual interval inequality corresponding to (5.13),

`P{Q in I} <=48.658 |I|`.                                     (6.1)

The fleet04/B19 theorem transfers this exact inequality, with no constant loss and no fragment-count/support-radius parameter, to the full class of arbitrary independent cap-one marginal densities. Thus the arbitrary-law version of (5.13) is also obtained through the designated partner's extremal-law reduction.

The pair theorem itself already has arbitrary-law scope; the point of this application is that the designated partner supplies an independent exact closure of the law class for this concrete target inequality, not a merely verbal citation.

## 7. Compact conditional end-to-end position

The currently assembled proof architecture can be stated compactly.

* The inherited **nonzero-pivot O0 transverse branch** is paid by B19 r18 / B08, with explicit dimension-free density bounds.
* In the **exact-null exact-rank-three heavy-row branch**, B10 pays every residual-heavy row. Theorem 3.1 of this report now forces the remaining residual-diffuse state to contain two disjoint independent transverse banks, each uniformly nondegenerate and each having a two-dimensional density cap below `68.768`.
* In the **genuinely near-null full-matrix branch**, Theorem 5.1 forces a star norm at least `sqrt(c-a^2)` and a complementary operator-norm resource at least one. A large star atom paired with a small second diagonal is paid by (5.13).

The full conjecture is **not** proved. The first essential analytic implication exposed by the exact-null assembly is now `QFORM-NULLROW-TWO-BANK-LEAKAGE-PAYMENT-v1`. The separate near-zero implication is to combine the star resource (5.1) and residual resource (5.2) without invoking the refuted near-zero-half-Riesz shortcut; the remaining difficult subcase is a diffuse star or large-diagonal support on all large star atoms.

The continuous-density conclusion is **not** proved for the unrestricted target or for the new structural branches. It remains available only in previously proved subbranches whose source theorem states continuity.

## 8. Exact arithmetic / identity check

The sibling `verify.py` checks:

* `7/9-1/16=103/144`;
* the pair constant in (5.13) is below `49`;
* the partition constants `1/40` and `1/640`;
* the two-dimensional packet cap `e sqrt(640)<68.768`;
* deterministic random Parseval-frame samples satisfy the Pluecker degree identity `sum_(j!=i) det(v_i,v_j)^2=||v_i||^2` and the random-partition expectation identity used in (3.9).

The checker is arithmetic/regression only; the proof is the exact derivation above.