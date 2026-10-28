SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T20:37:38Z.
attacking: the high-leverage S0 matching-bank transducer — calibrate an effective-rank-two ridge scale, pay the moderate branch, and force two-sided near-coloops into one anchored determinant packet.

# account03/B07 — effective-rank-two ridge collar and two-sided anchored second-compound packet

**Run:** `20260922T203738Z-account03-B07-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS / FULL TARGET OPEN`.

## 1. Target, incoming state, and correction discipline

The exact target remains unrestricted: for every finite `n`, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. Continuity is a separate stronger requested conclusion.

This run uses no Gaussian, moment, compact-support, log-concavity, post-rotation independence, arbitrary-joint rank-three coarea bound, positive conditional projection-density moment, worst conditional scalar-core density, law-uniform pointwise quadratic-phase decay, or one-good-local-minor assumption. All conditioning discussed below is on original coordinates or is purely an algebraic determinantal identity. The live correction that a single tiny physical minor is insufficient is respected throughout.

The designated partner `account04/B07` still had no completed current-QFORM canonical directory or current-QFORM handoff at the fresh source check. I therefore do not invent a partner result. The compatible completed other-account theorem actually applied below is account02/B19 r17:

`yspennstate/math-open-problems@fc8343c379bbddf14be670349f664f7fcb39994a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T192830Z-account02-B19-qform-r17/REPORT.md`.

After a genuine physical scalar Schur pivot of a target matrix, that report proves `s_2(S)>=1` for the exact residual and, in its disjoint-overlap alternative S0, produces an original-coordinate cross block `B` with

`E_2(B):=e_2(BB^T)=sum_{|I|=|J|=2} det B[I,J]^2 >= 1/48`.       (1.1)

Its determinant-bank half-Riesz theorem already pays a range-diffuse S0 subbranch. The remaining S0 problem is a high-leverage aggregate branch. The present run replaces the ordinary-range leverage split by a scale-calibrated ridge split and then proves an exact two-sided localization theorem in the surviving near-coloop branch.

The second completed input actually used is the ridge characteristic-function estimate

`QFORM-RIDGE-DENSITY-v1`, canonical source

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B`, a scale `gamma>0`, and `q in [1,2]`, put

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta=tr K_gamma`,
`D=det(I+BB^T/gamma^2)`,
`L_q=pi e sqrt(2/q)`.

If `max_i(K_gamma)_ii<=q/2`, its proved graph estimate gives, while retaining arbitrary self quadratic terms, affine terms, outside couplings, and extra spectrum,

`|phi_R(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`.    (1.2)

The source used (1.2) with `theta>2q` for a density estimate. The first theorem below integrates the same proved envelope against the half-Riesz Fourier weight and therefore only needs `theta>q`.

## 2. Ridge half-Riesz lemma at arbitrary effective rank

For a real random variable `R`, write

`H_(1/2)(R)=sup_y E |R-y|^(-1/2)`.

Whenever the weighted Fourier integral is finite, the standard Abel-regularized Riesz representation gives

`H_(1/2)(R) <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)| dt`.       (2.1)

### Theorem 2.1 — `QFORM-RIDGE-HALFRIESZ-v1`

Under the hypotheses of (1.2), if in addition `theta>q`, then

`boxed(
H_(1/2)(R)
 <= 2 sqrt(e) (2/q)^(1/4) gamma^(-1/2)
    [theta/(theta-q)] D^(-1/(4theta)).
)`                                                                 (2.2)

All scopes of the source ridge estimate are retained: this is an original-coordinate product-law statement and arbitrary self blocks/outside couplings are allowed.

### Proof

Set

`beta=theta/(2q)>1/2`,
`t_0=[L_q/(2gamma)] D^(-1/(2theta)).`                            (2.3)

Then (1.2), together with `|phi_R(t)|<=1`, is exactly

`|phi_R(t)|<=min(1,(t_0/|t|)^beta)`.                            (2.4)

A direct calculation gives

`int_R |t|^(-1/2) min(1,(t_0/|t|)^beta) dt`
` =4 sqrt(t_0) theta/(theta-q)`.                                 (2.5)

Indeed on the positive half-line the two integrals are

`int_0^t0 t^(-1/2)dt=2sqrt(t0)`,

`t0^beta int_t0^infinity t^(-beta-1/2)dt
 =sqrt(t0)/(beta-1/2)`,

and then one doubles for negative frequencies. Substituting (2.3) into (2.1)-(2.5) and using `L_q=pi e sqrt(2/q)` yields exactly (2.2). QED.

This is a fractional-potential theorem, not by itself a density theorem. It is precisely the endpoint required after an outer physical square pivot.

## 3. Effective-rank-two calibration spends the whole second compound

Let `B` have rank at least three and `E_2(B)>0`. Write its nonzero singular values as `s_r`. Since

`theta_gamma=sum_r s_r^2/(gamma^2+s_r^2)`                       (3.1)

is continuous and strictly decreasing from `rank(B)>2` to zero, there is a unique `gamma_*>0` satisfying

`theta_(gamma_*)=2`.                                             (3.2)

Put `K=K_(gamma_*)` and `D=D_(gamma_*)`.

### Theorem 3.1 — `QFORM-E2-RIDGE-HALFRIESZ-COLLAR-v1`

If on at least one side of `B` the calibrated ridge leverage satisfies

`max_i K_ii <= 23/24`,                                          (3.3)

then

`boxed(
H_(1/2)(R)
 <= C_* E_2(B)^(-1/8),
C_* = 48 sqrt(e) (24/23)^(1/4)
     =79.98514376669046... .
)`                                                               (3.4)

If `rank(B)=2`, no leverage condition is needed and the sharper completed two-cross Fourier estimate gives

`boxed(H_(1/2)(R)<=8 E_2(B)^(-1/8).)`                            (3.5)

Thus for the partner S0 resource (1.1), every rank-two state is paid by

`H_(1/2)(R)<12.980`,                                             (3.6)

and every rank-at-least-three state satisfying (3.3) is paid by

`H_(1/2)(R)<129.768`.                                            (3.7)

### Proof of (3.4)

Use Theorem 2.1 with

`q=23/12`, so `q/2=23/24` and `theta=2>q`.                       (3.8)

At `theta=2`, (2.2) becomes

`H_(1/2)(R)
 <= [4 sqrt(e)(2/q)^(1/4)/(2-q)]
    gamma_*^(-1/2) D^(-1/8).`                                  (3.9)

The determinant expansion is

`D=det(I+BB^T/gamma_*^2)
  =1+gamma_*^(-2)E_1(B)+gamma_*^(-4)E_2(B)+...`,                (3.10)

so

`D>=gamma_*^(-4)E_2(B)`.                                        (3.11)

Consequently

`gamma_*^(-1/2)D^(-1/8)<=E_2(B)^(-1/8)`.                        (3.12)

Since `2-q=1/12`, the coefficient in (3.9) is the stated `C_*`.

For rank two, if the two singular values are `s_1,s_2`, then `E_2=s_1^2s_2^2`. The completed original-coordinate two-cross Fourier theorem gives `H_(1/2)<=8(s_1s_2)^(-1/4)=8E_2^(-1/8)`, proving (3.5). QED.

### Why the calibration matters

No lower bound on one singular value, one matrix entry, or one `2x2` minor was used. The potentially bad scale `gamma_*^(-1/2)` cancels against the **entire** determinant through the exact `E_2` term in (3.10). The only surviving obstruction is a genuinely physical ridge near-coloop on both sides.

## 4. The near-coloop branch carries a single anchored determinant packet

Assume now `rank(B)>=3`, `theta_(gamma_*)=2`, and the collar (3.3) fails on **both** sides. Thus there exist an original row `i` and original column `j` with

`K^L_ii>23/24`,
`K^R_jj>23/24`,                                                  (4.1)

where

`K^L=BB^T(gamma_*^2I+BB^T)^(-1)`,
`K^R=B^TB(gamma_*^2I+B^TB)^(-1)`.                               (4.2)

The nonzero eigenvalues of both ridge kernels are

`k_r=s_r^2/(gamma_*^2+s_r^2) in (0,1)`,
`sum_r k_r=2`.                                                   (4.3)

Let `N=sum_r Bernoulli(k_r)` with independent Bernoulli variables. The determinantal `L`-ensemble with `L=BB^T/gamma_*^2` has subset-size law `N`, and the column-side ensemble has the same size law.

### Lemma 4.1 — a uniform size-two mass bound

`boxed(P(N=2)>=1/6.)`                                            (4.4)

Proof. The classical Darroch mode theorem for a Poisson-binomial sum says that every mode `m` satisfies `|m-EN|<1`; because `EN=2` is an integer, `2` is a mode. (J. N. Darroch, “On the Distribution of the Number of Successes in Independent Trials”, Ann. Math. Statist. 35 (1964), DOI 10.1214/AOMS/1177703287.) Also

`Var(N)=sum_r k_r(1-k_r)<=sum_r k_r=2`.                          (4.5)

Chebyshev therefore gives

`P(N in {1,2,3})=P(|N-2|<2)>=1-Var(N)/4>=1/2`.                  (4.6)

Since `2` is a mode, each of the three probabilities in (4.6) is at most `P(N=2)`. Hence `3P(N=2)>=1/2`, proving (4.4). QED.

The same probability has the exact exterior form

`P(N=2)=gamma_*^(-4)E_2(B)/D`.                                  (4.7)

### Theorem 4.2 — `QFORM-TWOSIDED-RIDGE-COLOOP-ANCHOR-v1`

Under (4.1), more than one half of the **whole second-compound mass** is carried by minors containing row `i` and column `j` simultaneously:

`boxed(
M_ij:=sum_{k!=i,l!=j} det B[{i,k},{j,l}]^2 > E_2(B)/2.
)`                                                               (4.8)

### Proof

Consider the joint fixed-size-two minor law

`mu(I,J)=det B[I,J]^2/E_2(B),    |I|=|J|=2`.                    (4.9)

By Cauchy-Binet its row marginal is the row `L`-ensemble conditioned on `N=2`; its column marginal is the analogous conditioned column ensemble.

For the row ensemble, `P(i in S)=K^L_ii`. Therefore, using (4.4),

`mu(i notin I)
 =P(i notin S | N=2)
 <=P(i notin S)/P(N=2)
 <(1/24)/(1/6)=1/4`.                                           (4.10)

Likewise

`mu(j notin J)<1/4`.                                            (4.11)

The union bound now gives

`mu(i in I and j in J)>1-1/4-1/4=1/2`.                         (4.12)

Multiplying (4.12) by `E_2(B)` is exactly (4.8). QED.

This is substantially stronger than selecting one tiny minor. The row and column are physical, but the second coordinate on each side is still summed over the entire original-coordinate bank.

## 5. Exact edge-versus-two-star factorization

Write `b=B_ij`, let

`r=(B_i,l)_(l!=j)`,
`c=(B_k,j)_(k!=i)`,
`C=(B_k,l)_(k!=i,l!=j)`.                                       (5.1)

Then every anchored `2x2` minor in (4.8) equals

`b C_kl-c_k r_l`.                                               (5.2)

Hence there is the exact identity

`boxed(M_ij=||bC-c r^T||_F^2.)`                                 (5.3)

Using `||X-Y||_F^2<=2||X||_F^2+2||Y||_F^2`,

`M_ij<=2 b^2||C||_F^2+2||c||_2^2||r||_2^2`.                    (5.4)

Combining with (4.8) gives the following completely physical dichotomy.

### Corollary 5.1 — `QFORM-ANCHORED-E2-EDGE-OR-TWOSTAR-v1`

At least one of

`boxed(b^2 ||C||_F^2 > E_2(B)/8)`                              (5.5)

or

`boxed(||r||_2^2 ||c||_2^2 > E_2(B)/8)`                        (5.6)

holds. In the partner S0 branch `E_2(B)>=1/48`, the surviving two-sided ridge-coloop geometry therefore carries the explicit source-valid reserve

`boxed(b^2 ||C||_F^2 >1/384)`                                  (5.7)

or

`boxed(||r||_2^2 ||c||_2^2 >1/384).`                           (5.8)

The second alternative is a pair of disjoint physical stars: `{i}` to the original column bank excluding `j`, and the original row bank excluding `i` to `{j}`. The first is one physical edge times a disjoint residual cross-energy bank. No orthogonal complement of an input bank is conditioned on or treated as independent.

If `b!=0`, (5.3) also has the exact rectangular Schur form

`M_ij=b^2 ||C-c r^T/b||_F^2`,                                  (5.9)

but (5.9) is recorded only as algebra; it is **not** treated as a product-preserving probabilistic Schur complement.

## 6. Actual application of the completed account02/B19 result

The other-account S0 inequality (1.1) is now consumed quantitatively rather than merely cited.

For its exact Schur residual cross block `B`:

1. If `rank(B)=2`, (3.5) and `E_2>=1/48` give

   `H_(1/2)(R) <=8*48^(1/8)=12.97911682888782...`.              (6.1)

2. If `rank(B)>=3`, calibrate `gamma_*` by `tr K=2`.
   If either side has maximum calibrated ridge leverage at most `23/24`, (3.4) gives

   `H_(1/2)(R)
    <=48 sqrt(e)(24/23)^(1/4) 48^(1/8)
    =129.76706569040797...`.                                    (6.2)

3. The only S0 state not covered by (6.1)-(6.2) has a physical row and column satisfying (4.1), and then necessarily satisfies one of the explicit reserves (5.7)-(5.8).

If this residual arose after a physical scalar square pivot `a`, the standard completed square transducer multiplies (6.1) or (6.2) by `|a|^(-1/2)` to obtain a density bound at exactly that pivot scope. No lower bound on `|a|` is silently assumed here.

Thus the prior phrase “high-leverage S0” can be replaced by a strictly narrower and quantitative state: **two-sided `23/24` ridge near-coloops at the unique effective-rank-two scale, carrying at least half of all second-minor mass through one physical row-column anchor, hence an edge-times-bank or two-star reserve of at least `1/384`.**

## 7. Smallest conditional end-to-end deduction and first unpaid implication

The correction-safe scalar-Schur route is now:

1. A genuine nonzero physical scalar pivot of a full target leaves an exact residual with `s_2>=1` (completed account02/B19 theorem).
2. Its second compound enters S0/S1/S2. Diffuse/previously paid branches stay paid at their proved scopes.
3. In S0, the present Theorem 3.1 pays every rank-two state and every rank-at-least-three state outside the two-sided `23/24` ridge-near-coloop branch, without selecting a local minor.
4. In the remaining S0 branch, Theorem 4.2 forces one row-column anchor to carry more than half of the entire second-compound mass, and Corollary 5.1 yields either the physical edge-times-bank reserve (5.7) or the disjoint two-star reserve (5.8).

The first unpaid implication is therefore sharpened to

`QFORM-S0-ANCHORED-EDGE-OR-TWOSTAR-PAYMENT-v1` (OPEN):

> Starting from an exact scalar-Schur residual `S` with `s_2(S)>=1` and an S0 cross block satisfying either (5.7) or (5.8), prove a universal translation-uniform half-Riesz bound while retaining arbitrary same-bank curvature; or force an already-paid physical pair, second pivot, two-cross, ridge, zero-internal, grouped-square, or affine-hyperbolic branch.

The analytic theorem must use the global second spectral resource; the existing rank-one-square counterexamples show that a single strong star plus arbitrary same-bank curvature is insufficient. The new point is that the truly unpaid state has **two-sided anchored currency**, not merely one strong cross direction and not merely a cloud of tiny minors.

S1, genuinely coupled S2, and no-usable-scalar-pivot parent branches remain separate synthesis debts. Full QFORM is still **OPEN / NOT PROVED / NOT DISPROVED**. The present half-Riesz theorem does not establish the full continuity conclusion.

## 8. Verification and provenance

The finite constants are deterministic consequences of the displayed formulas:

`C_*=48 sqrt(e)(24/23)^(1/4)=79.98514376669046...`,

`C_* 48^(1/8)=129.76706569040797...`,

`8*48^(1/8)=12.97911682888782...`.

A companion checker verifies these constants, the exact `theta=2` determinant cancellation, the joint-minor marginal identity on deterministic test matrices, and the anchored Frobenius identity (5.3). Those computations are regression checks, not substitutes for the analytic proof.

**Native brain ingestion:** not verified. Repository retrieval/write is not authenticated learned-memory receiver use, so this run remains `WITHOUT_VERIFIED_BRAIN`.
