SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T00:12:27Z.
attacking: translation-uniform fractional-trace synthesis in the rough-input no-pivot collar: turn a literal physical pair into a whole-copy collision bound, convert that to a quarter-Riesz residual, and feed the completed pinned hyperbola peel to recover linear one-copy small-ball scale.

# fleet02/B03 — determinant-only collision compiler and hyperbola splice

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Classification:** **NEW SUPPORTING THEOREM / LINEAR SMALL-BALL SPLICE / AGGREGATE-OVER-LOCAL OBSTRUCTION / FULL TARGET OPEN**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. Full-target continuity remains **OPEN**. This report proves a dependence-safe collision theorem from one literal physical pair, derives a critical quarter-Riesz bound, and applies the pinned coordinate-hyperbola theorem to obtain a new one-copy `L^infinity` branch. It also gives an exact target-valid family showing why this local determinant currency cannot be the final structural bridge: on a diffuse rank-three Hadamard frame it deteriorates like `sqrt(n)` while the pinned aggregate Fresnel theorem stays dimension-free.


## 1. First unpaid implication

The analytic debt attacked here is narrower than the full structural problem. Suppose a proof assembly has exposed a literal zero-diagonal physical hyperbolic pair and, after its Schur completion, a residual with some invertible physical two-coordinate block. Can that residual pair be spent without paying a smallest singular value, while preserving all arbitrary same-bank curvature and recovering **linear** one-copy small-ball scale?

The answer is yes. If the hyperbolic coefficient is `mu` and the residual pair determinant is `Delta`, the branch below gives

`||p_Q||_infinity < 2^(9/4) kappa 93^(1/4) |mu|^(-3/4) Delta^(-1/8)`,

where `kappa=sup_{y>0} log(1+y)/sqrt(y)=0.8047...`; numerically the constant is `<11.887`. Equivalently the scale currency is `|mu|^6 Delta`.

What remains unpaid is structural: the three-large-eigenvalue hypothesis has not been shown to force such a currency at universal scale. In fact Section 5 gives a target-valid diffuse family for which every physical pair determinant is `O(n^-2)` while a global frame estimate is uniform. Thus any final proof has to allow an aggregate receiver in addition to the local hyperbola-pair branch.

## 2. New theorem: a physical pair controls the whole-copy collision

Let

`Q=X^T A X+b^T X+c`,

where the scalar coordinates of `X` are independent and have probability densities at most one. Let `Q'` be an independent copy of the **whole scalar output**. Fix two genuine original coordinates `I={i,j}` and put

`B=A[I,I]`,   `Delta=|det B|>0`.                                   (2.1)

### Theorem 2.1 — `QFORM-PHYSICAL-PAIR-COLLISION-DET-v1`

The whole-copy difference has an essentially bounded density satisfying

`boxed:
 ||p_(Q-Q')||_infinity < 93 Delta^(-1/2).
}`                                                                  (2.2)

Consequently, for every `epsilon>0`,

`boxed:
 P(|Q-Q'|<=epsilon) < 186 Delta^(-1/2) epsilon.
}`                                                                  (2.3)

Moreover `Q` has an `L^2` density and

`boxed:
 ||p_Q||_2^2 <= 93 Delta^(-1/2).
}`                                                                  (2.4)

Its critical quarter-potential satisfies

`boxed:
 H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <= 2 sqrt(2) 93^(1/4) Delta^(-1/8)
 = 8.7834620787... Delta^(-1/8).
}`                                                                  (2.5)

Finally, the exact B03 weighted whole-copy integral obeys

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <= 4 sqrt(93 pi) Delta^(-1/4)
 = 68.3717037124... Delta^(-1/4),
}`                                                                  (2.6)

and equivalently

`boxed:
 E|Q-Q'|^(-1/2)
 <= 2 sqrt(186) Delta^(-1/4)
 = 27.2763633940... Delta^(-1/4).
}`                                                                  (2.7)

No smallest singular value of `B` appears.

### Proof of (2.2)-(2.3)

Condition on every coordinate outside `I` in both independent copies `X,X'`. The four remaining scalars

`(X_i,X_j,X_i',X_j')`

are mutually independent and retain their original density caps. Under the conditioning, `Q-Q'` is a quadratic polynomial in those four variables with arbitrary affine terms and quadratic matrix

`M=diag(B,-B)`.                                                     (2.8)

Its determinant satisfies

`|det M|=|det B|^2=Delta^2`.                                      (2.9)

Apply the completed physical-four-coordinate determinant theorem

`QFORM-PHYSICAL-FOUR-DETERMINANT-RECEIVER-v1`,

source `yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`, which gives for four independent cap-one physical coordinates and arbitrary affine terms

`||p||_infinity < 93 |det M|^(-1/4)`.                            (2.10)

Equations (2.9)-(2.10) give the conditional cap `93 Delta^-1/2`, uniformly in every conditioned coordinate. Averaging the conditional densities proves (2.2). Integrating that density over `[-epsilon,epsilon]` gives (2.3).

The proof never conditions on a spectral coordinate and never invokes independence of a sum and its conjugate difference.

### Proof of the `L^2` consequence (2.4)

Write `mu` for the law of `Q`, and let

`g=p_(Q-Q')=d(mu*mu_tilde)/dx`,   `||g||_infinity<=M`,

with `M=93 Delta^-1/2`. Let `gamma_sigma` be a centered Gaussian approximate identity and

`p_sigma=mu*gamma_sigma`.

Then

`||p_sigma||_2^2
 =[(mu*mu_tilde)*(gamma_sigma*gamma_sigma_tilde)](0)
 =(g*gamma_(sqrt(2)sigma))(0)
 <=M`.                                                            (2.11)

Thus `p_sigma` is uniformly bounded in `L^2`. Along a sequence `sigma ->0`, weak compactness in `L^2` gives a weak limit `p`; distributional convergence of the approximate identities identifies `mu=p dx`, and lower semicontinuity gives

`||p||_2^2<=M`.                                                    (2.12)

This proves (2.4) without presupposing an output density.

### Proof of the quarter-Riesz estimate (2.5)

Let `L=||p_Q||_2`. For any center `s` and radius `R>0`, Cauchy-Schwarz on the near region gives

`int_(|x-s|<=R) |x-s|^(-1/4)p_Q(x)dx
 <= L [int_(|u|<=R)|u|^(-1/2)du]^(1/2)
 =2 L R^(1/4).`                                                    (2.13)

The far region is at most `R^-1/4`. Hence

`H_(1/4)(Q) <= 2 L R^(1/4)+R^(-1/4)`.                            (2.14)

Optimizing in `R^(1/4)` gives

`H_(1/4)(Q)<=2 sqrt(2L)`.                                        (2.15)

By (2.4), `L<=sqrt(M)=sqrt(93) Delta^-1/4`, yielding (2.5).

### Proof of the assigned time estimate (2.6)-(2.7)

A probability density bounded by `M` maximizes its `|x|^-1/2` integral by filling a centered interval of length `1/M`; therefore

`int |x|^(-1/2)g(x)dx <=2 sqrt(2M)`.                              (2.16)

Use only the exact whole-copy identity

`|phi_Q(t)|^2=E exp(it(Q-Q'))`.                                  (2.17)

The positive-regularized one-dimensional Riesz identity

`int_R e^(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`                  (2.18)

gives

`int |t|^(-1/2)|phi_Q(t)|^2dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)
 <=sqrt(2pi) 2sqrt(2M)
 =4sqrt(pi M)`.                                                    (2.19)

Substituting `M=93 Delta^-1/2` proves (2.6)-(2.7). At no point is a coordinatewise sum/difference pair separated.

## 3. Pinned result applied: a determinant-only hyperbola receiver

The required pinned package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

especially `FOURIER_ROUTE_REPORT.md`, Lemma 4.3. Its completed coordinate-hyperbola theorem states: if two literal original coordinates satisfy

`A_ii=A_jj=0`,   `A_ij=mu!=0`,                                   (3.1)

then exact product completion gives

`Q=2mu(X_i+beta_j)(X_j+beta_i)+S`,                               (3.2)

where `S` is the physical Schur residual, and

`D(Q):=||p_Q||_infinity
 <=2^(3/4) kappa |mu|^(-3/4) H_(1/4)(S)`,                        (3.3)

with `kappa=sup_(y>0) log(1+y)/sqrt(y)=0.8047...`.

Assume now that the Schur residual `S` has **any** invertible literal physical `2 x 2` principal block `B_S`, and put

`Delta_S=|det B_S|>0`.                                            (3.4)

Apply Theorem 2.1 to `S`; its input coordinates are still the remaining genuine original independent variables. Equation (2.5) gives

`H_(1/4)(S)
 <=2 sqrt(2) 93^(1/4) Delta_S^(-1/8)`.                           (3.5)

Insert (3.5) into the pinned inequality (3.3):

`boxed:
 ||p_Q||_infinity
 <=2^(9/4) kappa 93^(1/4)
   |mu|^(-3/4) Delta_S^(-1/8)
 <11.887 |mu|^(-3/4) Delta_S^(-1/8).
}`                                                                  (3.6)

Therefore every interval `I` satisfies the actual linear one-copy small-ball estimate

`boxed:
 P(Q in I)
 <=11.887 |mu|^(-3/4) Delta_S^(-1/8)|I|.
}`                                                                  (3.7)

Equivalently, a uniform lower bound on the product-preserving matrix currency

`|mu|^6 Delta_S`                                                   (3.8)

pays this branch. There is no `sigma_min(B_S)` loss. Arbitrary same-bank quadratic and affine terms are retained inside `S`; no support, moments, log-concavity or post-rotation independence is used.

This is an actual equation-level application of a completed theorem from the required pinned `e5f71d79...` package.

## 4. Latest designated partner fleet03/B03 applied to a target-valid packet

The newest compatible designated partner report is fleet03/B03 r43,

`yspennstate/math-open-problems@f3198cfe9b2f5f88659958c714b1ea0f7dfa29c9`,

which proves `QFORM-THREE-GROUP-TRIANGLE-PLANCHEREL-v1`. In its notation, for three genuinely independent source groups `Z`, `X_R`, `X_C`, two-dimensional bank projections of density caps `M_R,M_C`, and nonzero triangle coefficients `sigma,alpha,beta`, it gives

`|phi_T(t)|
 <=min{1, K|t|^(-3/2)},
 K=pi^(3/2) M_0(M_RM_C)^(1/2)|sigma alpha beta|^(-1/2)`,          (4.1)

plus

`||p_T||_infinity
 <=3 M_0^(2/3)(M_RM_C)^(1/3)|sigma alpha beta|^(-1/3)`           (4.2)

and

`int |t|^(-1/2)|phi_T(t)|^2dt <=(24/5)K^(1/3)`.                 (4.3)

Apply it to five independent cap-one coordinates

`Z,Y_1,Y_2,W_1,W_2`

with the exact quadratic form

`T=2Y_1W_1+2Z(Y_2+W_2)`.                                        (4.4)

Here the two bank projections are the identity maps, so `M_0=M_R=M_C=1`, and `sigma=alpha=beta=1`. The matrix of (4.4) is the orthogonal direct sum of the edge `Y_1--W_1` and the two-leaf star `Y_2--Z--W_2`, hence its spectrum is

`{+1,-1,+sqrt(2),-sqrt(2),0}`.                                  (4.5)

Thus this is an exact owner-target family with four eigenvalues of modulus at least one. The partner theorem gives the concrete inequalities

`boxed: ||p_T||_infinity <=3,`                                   (4.6)

`boxed:
 int |t|^(-1/2)|phi_T(t)|^2dt
 <=(24/5)sqrt(pi)
 =8.5077784843...,
}`                                                                  (4.7)

and, for an independent whole copy `T'`,

`boxed:
 E|T-T'|^(-1/2)
 <=24/(5sqrt(2))
 =3.3941125497....
}`                                                                  (4.8)

This application keeps the three original source groups independent and uses the whole-copy identity only after the partner's triangle estimate. It is a direct use of the newest fleet03/B03 result, not a citation-only mention.

## 5. A target-valid obstruction to local pair determinant closure

Theorem 2.1 is useful analytically but cannot be the exhaustive structural bridge. The following exact rank-three family quantifies the obstruction.

Let `n=4m>=8`. Define an `n x 3` matrix `R_n` by repeating each of the four row patterns

`(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)`                      (5.1)

exactly `m` times, with every row divided by `sqrt(n)`. The three columns are orthonormal. Put

`A_n=R_n diag(1,1,-1) R_n^T`.                                   (5.2)

Then

`spec(A_n)={1,1,-1,0,...,0}`,                                   (5.3)

so every `A_n` lies exactly in the owner target.

For every physical coordinate,

`(A_n)_(ii)=1/n`.                                                 (5.4)

For two row patterns `s_i,s_j`, direct multiplication by `diag(1,1,-1)` gives only the values `1` and `-3`; hence

`(A_n)_(ij) in {1/n,-3/n}`.                                     (5.5)

Therefore every physical `2 x 2` principal determinant is either

`0` or `-8/n^2`,                                                  (5.6)

so the best local determinant magnitude is

`Delta_max=8/n^2`.                                                (5.7)

If one insists on Theorem 2.1 alone, its weighted-time bound is at best

`int |t|^(-1/2)|phi_(Q_n)(t)|^2dt
 <=4sqrt(93pi)(8/n^2)^(-1/4)
 =40.65405826... sqrt(n),`                                      (5.8)

which diverges.

Now apply a second completed result from the required pinned package: Theorem F in `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`. For (5.2), the spectral frame has

`G=sum_i rho_i rho_i^T=I_3`,   `rho_i^T G^-1 rho_i=3/n<=1/2`,    (5.9)

and `|lambda_1lambda_2lambda_3|=1`. Hence

`|phi_(Q_n)(t)|
 <=min{1,(4pi)^(3/2)|t|^(-3/2)}`                                (5.10)

and

`boxed: ||p_(Q_n)||_infinity <=12.`                              (5.11)

Squaring (5.10) and integrating exactly at the crossover `4pi` gives

`boxed:
 int_R |t|^(-1/2)|phi_(Q_n)(t)|^2dt
 <=(48/5)sqrt(pi)
 =17.0155569687...,
}`                                                                  (5.12)

uniformly in `n`. Therefore

`boxed:
 E|Q_n-Q_n'|^(-1/2)
 <=48/(5sqrt(2))
 =6.7882250994....
}`                                                                  (5.13)

This family is not a counterexample to QFORM. It is a quantitative obstruction to treating a single literal physical pair determinant, even through the stronger collision compiler, as an exhaustive consequence of the three-large-eigenvalue hypothesis. Aggregate frame information can remain order one while every physical pair determinant tends to zero.

## 6. Consequences and next structural debt

The new collision theorem contributes three distinct currencies from one physical pair determinant:

1. **linear whole-copy collision scale** `186 Delta^-1/2 epsilon`;
2. **critical one-copy quarter-potential** `8.784 Delta^-1/8`;
3. **B03 whole-copy half-Riesz time integral** `68.372 Delta^-1/4`.

The second currency is what makes the pinned coordinate-hyperbola peel close at linear one-copy scale without a residual `sigma_min` penalty.

The first unpaid implication is therefore now explicitly structural. For every remaining rough no-pivot/hub survivor under `s_3(A)>=1`, one needs a product-preserving alternative that yields, at universal scale, either

- a literal zero-diagonal hyperbolic pair whose Schur residual contains a physical pair with `|mu|^6 Delta_S >= c>0`, so (3.6) applies;
- an exact/near triangle packet of the type paid by the newest fleet03/B03 theorem;
- or one of the already-paid aggregate receivers (Fresnel frame, grouped hub, projected crossing/volume, three-hub, low-rank carrier, or other current source-valid branch).

The Hadamard family (5.2) proves that `Delta_S` or any single physical pair determinant cannot be demanded in isolation. The live correction forbidding a universal rank-three physical cross cut remains binding as well. The near-rank-one/genuine-rank-two anchored-star collar identified by fleet03/B03 r43 therefore remains a plausible common frontier: a successful interpolation must retain the additional small crossing direction exactly rather than regard it as a small random quadratic perturbation.

No claim is made that the new hyperbola-pair currency is automatically extractable from every target matrix. No continuity claim is made for Theorems 2.1 or 3.6; continuity is obtained only on branches with an actual `L^1` characteristic-function envelope such as (4.1) or (5.10).

## 7. Source status

Required pinned package consumed at exact commit:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Literal four-coordinate determinant receiver consumed from:

`yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`.

Newest compatible designated partner fleet03/B03 consumed from:

`yspennstate/math-open-problems@f3198cfe9b2f5f88659958c714b1ea0f7dfa29c9`.

The unrestricted conjecture remains **OPEN**. This report is a supporting theorem plus a source-valid obstruction to an overly local structural bridge.