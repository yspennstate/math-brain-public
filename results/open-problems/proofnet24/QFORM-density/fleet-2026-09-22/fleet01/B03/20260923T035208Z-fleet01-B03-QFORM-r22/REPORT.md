SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T03:52:08Z.
attacking: close the h=1 decoupled one-volume endpoint by a random-slope sublevel estimate that keeps the hub diagonal arbitrary, then splice it into fleet02/B03's indefinite-pair logarithmic transducer.

# fleet01/B03 r22 — random-slope endpoint closes the one-volume hub marginal gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T035208Z-fleet01-B03-QFORM-r22`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary-dimensional QFORM conjecture remains OPEN. This run proves a new dependence-safe endpoint lemma and uses it to remove the `h<1` row-marginal restriction from the **quarter-Riesz / one-volume analytic branch** behind fleet02/B03's latest indefinite-pair theorem. The argument also permits an arbitrary quadratic coefficient on the heavy coordinate, so the exact-zero-hub restriction from an earlier B03 route is removed. It does not assert that the bare spectral hypothesis forces a quantitatively good physical pair or residual cross Frobenius mass.

## 1. Fresh source boundary and completed inputs


Current mathematical state/corrections retain:

- no law-uniform pointwise quadratic-phase decay;
- no independence after spectral rotation;
- no density cap for one member of a conjugate sum/difference pair after conditioning the other;
- no arbitrary-joint rank-three coarea inequality;
- no dimension-free worst fiber-supremum route;
- no universal single-good-minor or local cross-rank-three reduction.

The live event `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` is especially relevant: `U^2+X^2+2UX=(U+X)^2` can have an unbounded density, so one heavy row plus one square does **not** by itself imply a bounded density. The present result is consistent with that correction: it proves only a square-root small-ball / fractional-potential estimate for the heavy-row residual, then uses a genuinely separate indefinite physical pair as the final logarithmic smoother.

Required newest Claude package actually used for the product-projection input and correction boundary:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The normalized one-dimensional product projection bound used below is the standard Rogozin/Ball consequence in the current source package:

`||p_{u^T Y}||_infinity <= sqrt(2)` for `||u||_2=1` and independent cap-one coordinates `Y_j`.

The designated partner actually applied is the latest completed fleet02/B03 result:

`yspennstate/math-open-problems@fab77e73a6163b18eea08d2807aa1a38166279ff`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T021907Z-fleet02-B03-QFORM-auto11/REPORT.md`.

Its exact transducer used below is: after completing an invertible **indefinite** ORIGINAL-coordinate physical pair `B`, with

`D=|det B|`, `kappa=sigma_min(B)`,

if the Schur residual `R` obeys

`sup_t P(|R-t|<rho) <= H rho^(1/4)`,

then

`||p_Q||_infinity <= 3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6)`.   (1.1)

The same report gives, for a half-power small-ball residual,

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                (1.2)

The source allows the pair shift to depend arbitrarily on the residual variables.

The diffuse one-volume input used on the complementary branch is fleet03/B03's completed `QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1`:

`yspennstate/math-open-problems@406753a39f5fbaf78396b31075f36ae5682ef3ad`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T235821Z-fleet03-B03-QFORM-r22/REPORT.md`.

For `k=1`, `Z_1=||M||_F^2`, and maximum row-energy fraction `h<=1/2`, it gives

`H_(1/4)(R):=sup_z E|R-z|^(-1/4)
 <= C_diff Z_1^(-1/8)`,                                           (1.3)

with

`C_diff=8(2pi)^(1/4)e^(1/8)/(Gamma(1/4)cos(pi/8))
 =4.284748578336202...`.                                          (1.4)

This input comes from the independent-copy decoupling estimate without separating dependent conjugate sums and differences.

## 2. New random-slope sublevel lemma

### Lemma 2.1 — `QFORM-RANDOM-SLOPE-SQRT-SMALLBALL-v1`

Let `X` be a real random variable with density at most one. Let `(L,R)` be an arbitrary real random pair independent of `X`; **L and R need not be independent of each other**. Assume only that `L` has a density satisfying

`||p_L||_infinity <= M < infinity`.

For arbitrary `a in R`, define

`T = a X^2 + 2 L X + R`.                                          (2.1)

Then for every `z in R`, `epsilon>0`, and `r>0`,

`P(|T-z|<=epsilon) <= 2 M r + 2 epsilon/r`.                       (2.2)

Consequently

`boxed: sup_z P(|T-z|<=epsilon) <= min(1,4 sqrt(M epsilon)).`      (2.3)

The constant and exponent are uniform in the quadratic coefficient `a`, including `a=0` and arbitrarily small nonzero `a`, and uniform in the complete dependence between `L` and `R`.

#### Proof

Split according to the random derivative scale

`E_r={|aX+L|<=r}`.

Because `X` is independent of `L`, conditioning on `X=x` gives

`P(E_r | X=x)
 =P(L in [-ax-r,-ax+r]) <=2Mr`.

Hence

`P(E_r)<=2Mr`.                                                     (2.4)

On the complement, condition on `(L,R)=(l,s)`. The active one-variable polynomial is

`q(x)=a x^2+2 l x+s-z`,

with

`q'(x)=2(ax+l)`.                                                   (2.5)

On `{x:|ax+l|>r}`, the set has at most two intervals and `q` is monotone on each, with `|q'|>2r`. Therefore on each component the preimage of `[-epsilon,epsilon]` has Lebesgue length at most

`2epsilon/(2r)=epsilon/r`.

There are at most two components, so the total active `x`-length is at most `2epsilon/r`. Since `f_X<=1`,

`P(|q(X)|<=epsilon, |aX+l|>r | L=l,R=s)
 <=2epsilon/r`.                                                    (2.6)

Averaging (2.6) and combining with (2.4) proves (2.2). Choosing

`r=sqrt(epsilon/M)`

gives (2.3). For `a=0` there is in fact only one monotone component whenever `|l|>r`, so the same stated bound remains valid. QED.

### Why this does not contradict the heavy-row/same-square correction

For the correction example `T=(U+X)^2`, (2.3) only asserts an `O(sqrt(epsilon))` small-ball bound; that is compatible with the `t^(-1/2)` output-density singularity. The new lemma is therefore **not** a hidden bounded-density claim. Its purpose is to supply a fractional smoother to a separate pair-level logarithmic kernel.

## 3. Fractional potential and the exact independent-copy time integral

Suppose a random variable `T` satisfies

`sup_z P(|T-z|<rho) <= min(1,H rho^(1/2))`.                        (3.1)

For every `0<gamma<1/2`, layer cake gives

`sup_z E|T-z|^(-gamma)
 <= H^(2gamma)/(1-2gamma)`.                                       (3.2)

Indeed the crossover is `rho_0=H^(-2)`, and

`gamma int_0^rho0 rho^(-gamma-1) H rho^(1/2) d rho
 + gamma int_rho0^infinity rho^(-gamma-1)d rho
 =H^(2gamma)/(1-2gamma)`.

Applying this to Lemma 2.1 with `H=4sqrt(M)` gives

`boxed:
 sup_z E|T-z|^(-gamma)
 <= (4sqrt(M))^(2gamma)/(1-2gamma), 0<gamma<1/2.
`                                                                      (3.3)

At the B03 quarter endpoint,

`boxed: H_(1/4)(T) <=4 M^(1/4).`                                  (3.4)

Now let `T'` be an independent copy. The exact independent-copy identity

`|phi_T(t)|^2 = phi_(T-T')(t)`                                    (3.5)

is used **as a whole**. Conditioning on `T'` in (3.3),

`E|T-T'|^(-gamma)
 <=(4sqrt(M))^(2gamma)/(1-2gamma)`.                               (3.6)

The positive one-dimensional Riesz-energy identity (or a Gaussian positive regularization followed by monotone/Fatou passage) yields

`int_R |t|^(gamma-1)|phi_T(t)|^2 dt
 =2 Gamma(gamma) cos(pi gamma/2) E|T-T'|^(-gamma)`.                (3.7)

Hence

`boxed:
 int_R |t|^(gamma-1)|phi_T(t)|^2 dt
 <= [2 Gamma(gamma) cos(pi gamma/2)/(1-2gamma)]
    (4sqrt(M))^(2gamma).
`                                                                      (3.8)

At `gamma=1/4`,

`boxed:
 int_R |t|^(-3/4)|phi_T(t)|^2 dt
 <=8 Gamma(1/4)cos(pi/8) M^(1/4).
`                                                                      (3.9)

No coordinate-pair sum is conditioned against its dependent difference anywhere in this derivation.

## 4. Closing the one-volume hub endpoint `h=1`

Let `I,J` be disjoint ORIGINAL-coordinate banks in an arbitrary conditioned quadratic-plus-linear residual, and let

`M=A[I,J]`, `Z_1=||M||_F^2>0`.

Define the row-energy fractions

`alpha_i=||M_{i,*}||_2^2/Z_1`,

and

`h=max_i alpha_i in (0,1]`.                                       (4.1)

The preceding fleet02/B03 theorem stops at `h<1`, because its volume-sampling exponent has `q=max(1,2h)<2`. The heavy endpoint can instead be paid directly without losing the within-bank curvature.

Choose a row `i` attaining `h`, write

`m=M_{i,*}`,

so

`||m||_2^2=h Z_1`.                                                (4.2)

Condition on all original coordinates in `I\{i}` and on every coordinate outside `{i} union J`. The residual polynomial becomes exactly

`T=a X_i^2+2 X_i(m^T X_J+beta)+R_0(X_J)`,                         (4.3)

where `a` is arbitrary and `R_0` contains **all** remaining quadratic and affine curvature on the `J` bank. The original coordinate `X_i` is independent of the pair

`L=m^T X_J+beta`, `R=R_0(X_J)`,

although `L` and `R` may be maximally dependent.

By the source product-projection theorem,

`||p_L||_infinity <= sqrt(2)/||m||_2`.                            (4.4)

Applying Lemma 2.1 gives the uniform conditional small-ball estimate

`sup_z P(|T-z|<=rho)
 <=4*2^(1/4) ||m||_2^(-1/2) rho^(1/2)`

`=4*2^(1/4) h^(-1/4) Z_1^(-1/4) rho^(1/2)`.                      (4.5)

Since the right side does not depend on the conditioned values, averaging preserves it for the original residual.

Likewise (3.4) gives

`boxed:
 H_(1/4)(T)
 <=4*2^(1/8) h^(-1/8) Z_1^(-1/8).
`                                                                      (4.6)

Thus for every `h>1/2`,

`H_(1/4)(T)
 <=4*2^(1/4) Z_1^(-1/8)`.                                        (4.7)

For `h<=1/2`, the completed fleet03/B03 decoupled one-volume theorem (1.3) gives the stronger

`H_(1/4)(T)<=4.284748578336202... Z_1^(-1/8)`.

Combining the two regimes proves:

### Theorem 4.1 — `QFORM-ONEVOLUME-QUARTER-RIESZ-NO-MARGINAL-GATE-v1`

For every nonzero original-coordinate cross block `M` in a conditioned quadratic-plus-linear residual,

`boxed:
 sup_z E|R-z|^(-1/4)
 <= C_* ||M||_F^(-1/4),
 C_*=4*2^(1/4)=4.756828460010884... .
`                                                                      (4.8)

There is **no row-marginal assumption**. All self blocks and affine terms are arbitrary.

Equivalently, the dependence-safe independent-copy time integral satisfies

`boxed:
 int_R |t|^(-3/4)|phi_R(t)|^2 dt
 <=8*2^(1/4) Gamma(1/4)cos(pi/8) ||M||_F^(-1/4)
 =31.867200062359164... ||M||_F^(-1/4).
`                                                                      (4.9)

The diffuse half of this theorem uses the completed independent-copy / Brascamp--Lieb volume theorem; the hub half uses the new random-slope estimate. Neither half conditions a sum on its dependent difference.

## 5. Actual application of fleet02/B03: linear small-ball after an indefinite pair

Now suppose two disjoint ORIGINAL coordinates form an invertible indefinite physical pair `B`. Complete that pair, with

`D=|det B|`, `kappa=sigma_min(B)>0`,

and suppose the Schur residual has any nonzero original-coordinate cross block `M` between disjoint banks. Let

`Z_1=||M||_F^2`.

By Theorem 4.1 and Markov,

`sup_t P(|R-t|<rho)
 <= C_* Z_1^(-1/8) rho^(1/4)`.                                    (5.1)

Substitute the actual value

`H=C_* Z_1^(-1/8)`

into the designated partner's inequality (1.1). This gives the **marginal-free pair + one-volume theorem**

`boxed:
 ||p_Q||_infinity
 <=3*2^(17/6)
    D^(-1/3) kappa^(-1/6) Z_1^(-1/12)
 <21.382 D^(-1/3) kappa^(-1/6) Z_1^(-1/12).
`                                                                      (5.2)

Therefore every interval `J0` satisfies the genuine linear small-ball bound

`P(Q in J0)
 <=3*2^(17/6) D^(-1/3) kappa^(-1/6) Z_1^(-1/12) |J0|`.           (5.3)

This is the requested end-to-end recovery of **linear** small-ball scaling from the decoupled/fractional time mechanism.

There is a stronger heavy-row formula when `h>1/2`. Use the half-power estimate (4.5) directly in the partner's half-power transducer (1.2). With

`H=4*2^(1/4) h^(-1/4)Z_1^(-1/4)`,

one obtains

`boxed:
 ||p_Q||_infinity
 <=2^(29/8) h^(-1/8)
   (D kappa)^(-1/4) Z_1^(-1/8).
`                                                                      (5.4)

At the exact hub endpoint `h=1`, the scalar constant is

`2^(29/8)=12.337686603263526...`.                                 (5.5)

Uniformly over the whole heavy regime `h>1/2`, it is at most

`2^(15/4)=13.454342644059432...`.                                 (5.6)

This closes the analytic `h=1` hole in the partner theorem. It does **not** prove a universal lower bound on `D`, `kappa`, or `Z_1` from the bare three-large-eigenvalue hypothesis.

## 6. Genuine target-family application with arbitrary/near-zero hub diagonal

Let

`B_0=[[0,1],[1,0]]`                                                (6.1)

on two original coordinates. On a disjoint hub-plus-`m`-leaf bank, let

`S_(m,a)=[[a,v^T],[v,0_m]]`,                                      (6.2)

where `a in R` is arbitrary and `||v||_2=1`. Put

`A_(m,a)=B_0 direct_sum S_(m,a)`.                                  (6.3)

The physical pair `B_0` has

`D=kappa=1`.                                                       (6.4)

The nonzero eigenvalues of `S_(m,a)` are the two roots

`lambda_pm=(a +/- sqrt(a^2+4))/2`,                                (6.5)

whose product is `-1`. Therefore at least one of them has modulus at least one for every real `a`. Together with the eigenvalues `+1,-1` of `B_0`, the full matrix `A_(m,a)` has **at least three eigenvalues of modulus at least one for every `m`, every real `a`, and every unit vector `v`**.

For the star residual, take the hub as `I` and all leaves as `J`. Then

`Z_1=||v||_2^2=1`, `h=1`.                                         (6.6)

The heavy formula (5.4) gives, for every admissible family of independent cap-one input laws,

`boxed:
 ||p_(X^T A_(m,a) X)||_infinity
 <=2^(29/8)
 =12.337686603263526... .
`                                                                      (6.7)

The bound is uniform in the bank dimension `m`, the arbitrary hub diagonal `a` (including zero, near zero, or very large magnitude), and the orientation `v` inside the original leaf bank.

This family is a direct target-level demonstration of what changed: earlier exact-zero-hub arguments required `a=0`; the random-slope lemma pays every `a` while preserving arbitrary same-bank quadratic curvature in the abstract theorem.

## 7. What remains unpaid

The new analytic branch is complete only under the following structural certificate:

1. an invertible indefinite ORIGINAL-coordinate physical pair with quantitative `D=|det B|` and `kappa=sigma_min(B)`, and
2. after its Schur completion, at least one nonzero original-coordinate cross block with quantitative Frobenius mass `Z_1`.

The bare hypothesis `s_3(A)>=1` has not been shown to force those quantities at universal scale. Existing correction families forbid replacing that missing step by a universally good single physical minor, a universally rank-three coordinate cut, or a worst-fiber density supremum. The next B03-compatible structural/analytic target is therefore to aggregate pair quality and one-volume mass **before reciprocal inversion**, or to splice this endpoint into the current N3 exhaustive proof graph alongside the diffuse-volume, mixed-hub, exact-null-coloop, ridge-window, and physical-core exits.

Full QFORM status: **OPEN**.  
Essential boundedness/absolute continuity: proved in the branch (5.2), including the target family (6.3).  
Continuous density: **not proved by this argument**.  
Independent end-to-end reviews of this new theorem: none in this run.

## 8. Constant checks

`C_*=4*2^(1/4)=4.756828460010884...`.

`2 Gamma(1/4)cos(pi/8) C_*
 =31.867200062359164...`.

`3*2^(4/3) C_*^(2/3)
 =3*2^(17/6)
 =21.38156923536814...`.

`4 sqrt(2*(4*2^(1/4)))
 =2^(29/8)
 =12.337686603263526...`.

`2^(29/8)*(1/2)^(-1/8)
 =2^(15/4)
 =13.454342644059432...`.
