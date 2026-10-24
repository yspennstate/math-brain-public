# account01/B16 — projection-product interaction by half-order residual smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T123944Z-B16-qform`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED RANK-THREE HYBRID BRANCH`; full conjecture **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Live target and source pins

The live target is: for independent real `X_i` with probability densities `0<=f_i<=1` and every real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove one universal bound on the density of `X^T A X`, or give a genuine counterexample.

Fresh owner control was read from `yspennstate/math-research-brain` main commit `baf7d58a1430202ba8b114f63b1c159e4cc3a718`, then revalidated after concurrent updates at main commit `92c96e3fcdebda3f7c5ded323c48e43b034964d6`. The correction inbox at revalidation contained `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. None of the refuted implications is used below.

The named partner result is account02/B16 run `20260922T115600Z-account02-B16-qform-projprod`, canonical report `yspennstate/math-open-problems@0605c987ff531ccc2fd5554c48df29e65b3eaaa8:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T115600Z-account02-B16-qform-projprod/REPORT.md`, blob `aa77eea73a99b6a58329ece190589b110716b485`. Its exact averaged weighted-Wiener criterion is applied in Section 2.

A second dependency is the account02/B08 diffuse-frame calculation, canonical report `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a:proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T113624Z-qform11/REPORT.md`, blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0a`. I reuse its geometric Brascamp--Lieb plus sharp Hausdorff--Young argument, but in dimension two and with a different terminal functional.

The previous account01/B16 X-ray theorem is `yspennstate/math-open-problems@8004481452c19f103fd5dd24c2cb4d787860b56a:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/qform-20260922T114042Z-account01-B16-r11/REPORT.md`, blob `26aafd1b006c5977ed9bad0095e8f4d8af155054`. The current correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` shows why a generic X-ray norm cannot close the minority-sign two-sheet side. The new argument below instead keeps the original-coordinate product structure through a rank-two Fourier estimate and a physical-coordinate square kernel.

## 2. Actual application of the named partner theorem

Account02/B16 proves: if three selected eigenvectors form `R`, `A=R^T Lambda R+B`,

`Psi_t(xi)=E exp(i<xi,RX>+it X^T B X)`, `W(t)=int |Psi_t(xi)| dxi`,

and

`int_{|t|>=1}|t|^(-3/2) W(t) dt <= K`,

then

`||p_Q||_infinity <= 1/pi + K/(16 pi^(5/2))`.

For the rank-exactly-three diffuse branch `B=0`, account02/B08 gives

`W(t)=||hat g||_1 <= (2pi)^3 e^(3/2)`.

Therefore the partner criterion applies with

`K <= 4(2pi)^3 e^(3/2)=32 pi^3 e^(3/2)`,

and yields the fully explicit, although non-sharp, bound

`||p_Q||_infinity <= 1/pi + 2 sqrt(pi) e^(3/2)`.

This is a literal application of the partner theorem. More importantly for the new branch, it identifies the correct analytic principle: after some curvature is paid in physical space, it is enough to control a **weighted time integral** of the residual characteristic function. The next lemma executes exactly that principle with the half-order weight forced by one square variable.

## 3. Rank-two diffuse half-order potential

### Lemma 3.1 — `QFORM-RANK2-DIFFUSE-RIESZ-HALF-v1`

Let `V in R^{m x 2}` satisfy `V^T V=I_2`, with rows `v_k`, and assume

`d_k=||v_k||^2 <= 1/2` for every `k`.

Let `X_k` be independent with densities `0<=f_k<=1`, put `W=V^T X`, and let `S` be any real symmetric invertible `2 x 2` matrix. Then

`R=W^T S W`

satisfies

`ess sup_t E |t-R|^(-1/2) <= 4 sqrt(2e) |det S|^(-1/4)`.              (3.1)

This is deliberately weaker than asking the indefinite rank-two quadratic itself to have a bounded density. The latter is false in general at the logarithmic threshold; the half-order Riesz potential is the amount of smoothing needed after one additional square.

### Proof

Ignore zero rows. Write `v_k=sqrt(d_k) omega_k`, with `omega_k` unit. Since `V^T V=I_2`,

`sum_k d_k omega_k omega_k^T=I_2`, `sum_k d_k=2`.

The characteristic function of `W` is

`hat h(xi)=prod_k hat f_k(<v_k,xi>)`.

Exactly as in the account02/B08 calculation, geometric rank-one Brascamp--Lieb with

`q_k=1/d_k >=2`, `p_k=1/(1-d_k)<=2`

and sharp Hausdorff--Young gives

`||hat h||_1 <= (2pi)^2 prod_k (1-d_k)^(-(1-d_k)/2)`.

Because `-(1-d)log(1-d)<=d` and `sum d_k=2`,

`boxed{ ||hat h||_1 <= (2pi)^2 e. }`                                  (3.2)

In particular `W` has a bounded continuous density.

Let

`phi_R(tau)=E exp(i tau W^T S W)`.

Gaussian-regularized Fourier inversion, now in dimension two, gives the standard Fresnel estimate

`|phi_R(tau)| <= (2pi)^(-2) ||hat h||_1 pi |tau|^(-1) |det S|^(-1/2)`

for `tau!=0`. Using (3.2),

`|phi_R(tau)| <= pi e |det S|^(-1/2) |tau|^(-1)`.                       (3.3)

Together with `|phi_R|<=1`, set

`A=pi e |det S|^(-1/2)`

and obtain

`|phi_R(tau)| <= min(1,A/|tau|)`.                                      (3.4)

For the Fourier convention `hat f(tau)=int e^(-i tau x) f(x) dx`,

`widehat{|x|^(-1/2)}(tau)=sqrt(2pi)|tau|^(-1/2)`

as a tempered distribution. The product

`|tau|^(-1/2) phi_R(tau)`

is absolutely integrable by (3.4). Hence the convolution `E|t-R|^(-1/2)` has an essentially bounded representative and

`ess sup_t E|t-R|^(-1/2)`

`<= 1/sqrt(2pi) int_R |tau|^(-1/2)|phi_R(tau)| dtau`

`<= 1/sqrt(2pi) * 8 sqrt(A)`

`=4 sqrt(2e) |det S|^(-1/4)`.

The integral identity used here is

`int_R |tau|^(-1/2) min(1,A/|tau|) dtau=8 sqrt(A)`.

This proves (3.1). `QED`

## 4. Heavy-coordinate / diffuse-transverse hybrid theorem

### Theorem 4.1 — `QFORM-RANK3-HEAVY-RAYLEIGH-HALF-v1`

Let `U in R^{n x 3}` have orthonormal columns and let `Lambda` be a real symmetric invertible `3 x 3` matrix. Write `u_k` for the rows of `U`. Let `X_k` be independent with densities bounded by one, and set

`Q=(U^T X)^T Lambda (U^T X)`.

Suppose there is an index `i` with

`c=||u_i||^2>0`.

Put

`e=u_i/sqrt(c)`, `P=I-ee^T`, `a=e^T Lambda e`.

Assume

1. `a!=0`, and
2. every transverse residual row satisfies

   `||P u_k||^2 <=1/2` for `k!=i`.

Then `Q` has an essentially bounded density and

`boxed{
||p_Q||_infinity
<=4 sqrt(2e) c^(-1/2)|a|^(-1/4)|det Lambda|^(-1/4).
}`                                                                   (4.1)

In particular, if the three nonzero eigenvalues of `Lambda` all have absolute value at least one, `c>1/2`, and `|a|>=eta>0`, then

`||p_Q||_infinity <=8 sqrt(e) eta^(-1/4)`.                             (4.2)

For `eta=1/4`, this is

`||p_Q||_infinity <=8 sqrt(2e) <18.654`.                              (4.3)

If row `i` is the unique row of `U` with leverage greater than `1/2`, hypothesis 2 is automatic because `||Pu_k||<=||u_k||`.

### Proof

Decompose the spectral projection as

`Y=U^T X=sqrt(c) e X_i+Z`,

where

`Z=sum_{k!=i}u_k X_k`

is independent of `X_i`. Put

`W=PZ`.

The transverse rows are `w_k=Pu_k`. Since

`sum_k u_k u_k^T=I_3`

and `Pu_i=0`,

`sum_{k!=i} w_k w_k^T=P`.

Thus, after identifying `e^perp` with `R^2`, the rows `w_k` form a Parseval frame and hypothesis 2 puts it exactly in Lemma 3.1.

Write `Lambda` in the orthogonal decomposition `span(e) direct-sum e^perp` as

`Lambda=[[a,b^T],[b,C]]`.

If

`s=e^T Y=sqrt(c)X_i+e^T Z`,

then

`Q=a s^2+2s b^T W+W^T C W`.

Completing the square gives

`Q=a [s+a^(-1)b^T W]^2+W^T S W`,

where

`S=C-bb^T/a`.

Equivalently,

`Q=ac [X_i+theta(Z)]^2+R`,

with

`R=W^T S W`.

The shift `theta(Z)` may depend arbitrarily on the other coordinates, but conditional on them it only translates the density of `X_i`; its height remains at most one.

The block determinant identity is

`det Lambda=a det S`.                                                  (4.4)

Since `Lambda` is invertible and `a!=0`, `S` is invertible.

For fixed values of all coordinates except `X_i`, the square variable

`ac [X_i+theta]^2`

has a density bounded by

`1/(sqrt(|ac|) sqrt(|v|))`

on its supporting half-line. Therefore, after averaging the conditional density and dropping only the half-line indicator,

`p_Q(t) <= |ac|^(-1/2) E |t-R|^(-1/2)`                               (4.5)

for almost every `t`.

Apply Lemma 3.1 to the transverse Parseval frame and `S`:

`ess sup_t p_Q(t)`

`<=4sqrt(2e)|ac|^(-1/2)|det S|^(-1/4)`

`=4sqrt(2e)c^(-1/2)|a|^(-1/4)|det Lambda|^(-1/4)`,

where (4.4) was used in the last step. This is (4.1).

If all three eigenvalues have modulus at least one, then `|det Lambda|>=1`. If `c>1/2`, then `c^(-1/2)<sqrt(2)`, giving (4.2) and (4.3). `QED`

## 5. What this resolves and why it survives the two-sheet correction

The previous B16 argument bounded only the ruled one-sheet side from the generic X-ray norm. `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correctly kills any claim that the same X-ray data alone control the two-sheet side.

Theorem 4.1 is different. It yields a **two-sided** `L^infinity` density bound. The extra information is exactly the original-coordinate product provenance:

- one original coordinate supplies a genuine square-density kernel;
- the other original coordinates remain independent long enough to yield the rank-two Brascamp--Lieb/Hausdorff--Young estimate;
- the logarithmically singular rank-two indefinite residual is not asked to have a bounded density; only its half-order Riesz potential is paid.

Thus the theorem addresses a real part of the projection-product interaction rather than contradicting the curved-shell correction.

A useful corollary is that, for rank exactly three, every **definite** form in this branch automatically has `|a|>=1`: if all eigenvalues are >=1 or all <=-1, every unit Rayleigh quotient has magnitude at least one. Hence a unique leverage-heavy row plus diffuse transverse remainder is already a completely closed definite rank-three case.

## 6. Sharp unresolved interface

The theorem does **not** prove the full conjecture. The first remaining rank-three interface is now:

`QFORM-HEAVY-ISOTROPIC-OR-MULTIHEAVY-v1`.

One must handle either

1. a leverage-heavy physical row whose Rayleigh quotient `a=e^T Lambda e` is small or zero (possible only in the indefinite case), where the heavy coordinate enters mainly through a bilinear saddle rather than a square; or
2. several transverse residual rows with leverage above `1/2`, where the two-dimensional Fourier `L^1` argument is unavailable.

These are precisely the cases in which the reciprocal `|a|^(-1/4)` or diffuse-frame hypothesis in (4.1) becomes ineffective. Existing hyperbolic-square physical-coordinate theorems show that some such cases are still bounded, but a dimension-free aggregation that covers all frames is not yet proved.

After rank-three closure, arbitrary additional nonzero spectral components remain a separate issue. The account02/B16 weighted-Wiener interface is a valid route for those correlated extra components, but no universal estimate of its phase-weighted Wiener integral is currently available in the full leverage-heavy regime.

No full-solution promotion is made.

## 7. Integrity notes

This report uses no law-uniform pointwise stationary-phase estimate, no independence after spectral rotation, no unrestricted fiber-supremum reduction, no fixed physical minor assumption, and no generic X-ray-only closure. No numerical sweep is used as proof. The constants above come from exact analytic inequalities.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort/provider reasoning counters: `UNKNOWN / NOT_EXPOSED`. Repository synchronization occurred; native learned-memory ingestion did not, so execution remains `WITHOUT_VERIFIED_BRAIN`.
