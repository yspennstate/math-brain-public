Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-12 — sub-stochastic barycentric universality for dependent full-rank negative-perceptron constraints

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Owner policy: `operations/PROGRESS20_2026-09-20.md` and current LIVE20 mapping  
Worker: `NM13-12` / `proofnet24/NM13-12/progress-universality`  
Applied parent: **T03 negative spherical perceptron, kappa=-1, exact unit sphere**  
Status: **PARTIAL / NEW FINITE-N PATHWISE THEOREM / NEW DEPENDENT NON-GAUSSIAN APPLICATION / ORIGINAL T03 UNCHANGED**

## 1. Compact handoff: latest P12 theorem and predecessor

The latest canonical P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md`.

Its frozen mathematical theorem is unchanged. For `F in {R,C}`, let `A_m in F^{N_m x m}` have iid centered variance-one entries with densities `f_m`. Assume there are one fixed integer `q>=1` and one finite constant `M` such that

`sup_m ||f_m^{*q}||_infty <= M`,

and assume

`N_m/m -> gamma>1`, `k_m=r_m+1`, `k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) -> -h(gamma)/d_F` in probability,

with `d_R=1`, `d_C=2`. There is **no fourth-moment assumption and no positive-moment assumption above variance normalization**. Fixed bounded-density laws occur at `q=1`. The unresolved mathematical successor is still triangular smooth / bounded-fourth-moment universality without a uniform microscopic finite-convolution smoothing hypothesis. P12 itself is mathematically frozen and protocol-open only because an independent audit is missing.

I do not reopen or repackage the posted row-submatrix result, mesoscopic-spike work, kernel theorem, ReLU work, or zero-margin/Ising perceptron work. The theorem below concerns a different exact negative-margin spherical feasibility event and a dependent-row closure mechanism.

The immediate NM13-12 predecessor was

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/2026-09-20T0606Z__t03-approx-low-rank-singular-quantile-universality.md`.

It proved that an arbitrary contaminant block `B` can be made harmless on a codimension-`r` subspace when `s_{r+1}(B)<=-kappa`, giving a full-rank singular-quantile extension of the earlier exact-low-rank theorem. After several covariance/singular-value runs with no movement of the original T03 source bracket, this run changes method completely: **constraint-order / convex-closure geometry**, with no covariance, low-rank or singular-value reduction in the proof.

## 2. Current T03 parent and peer coordination

The source model is frozen exactly:

- `M=floor(alpha N)`;
- iid rows `g_a ~ N(0,I_N)`;
- witness `x in S^{N-1}` exactly;
- constraints `g_a . x >= -1` for every row.

The latest relevant peers on current `master` are complementary rather than duplicated:

1. `NM13-03`, report `2026-09-20__t03-aposteriori-objective-alpha12319635.md`, proves an a-posteriori objective-localization lemma for the complete-second-lift stationary system and gives a directed-interval **CANDIDATE_FULL** upper endpoint `12.319635`, pending later independent review.
2. `NM13-07`, report `2026-09-20__t03-certified-microcontinuation-alpha1231963485.md`, consumes that anchor and proves a uniform stationary micro-continuation to `12.31963485`, again **CANDIDATE_FULL / independent review pending**. It explicitly records that further decimal shaving of the complete-second branch is not substantial and names third-full or a different feasibility mechanism as the next material route.

This NM13-12 run does neither stationary-lift calculation nor interval quadrature. It proves a finite-N pathwise invariance statement for a new dependent/non-Gaussian disorder class. Any valid current or future T03 endpoint transfers through the theorem with exactly zero additional comparison loss.

For arithmetic below I distinguish:

- rigorous lower endpoint used throughout the project: `alpha_L=1/Phi(-1)=6.302974375068753...`;
- older project rigorous upper endpoint: `12.78437096216`;
- newest peer **candidate** upper endpoint: `12.31963485`, pending later independent review.

The original T03 parent is not moved by this worker.

## 3. New theorem — sub-stochastic barycentric closure

For a real matrix `A in R^{m x N}` and `kappa in R`, write

`SAT(A,kappa)`

for the event/property that there exists `x in S^{N-1}` with

`A x >= kappa * 1_m`

coordinatewise.

Let `W in R^{K x m}` be **row-substochastic**:

`W_{ji}>=0`, and `s_j:=sum_i W_{ji}<=1` for every `j`.

Let `E in R^{K x N}` have row vectors `e_j` satisfying

`max_j ||e_j||_2 <= eps`.

Define the additional block

`B := W A + E`.

### Theorem NM12-SSC (finite-N, deterministic)

If

`kappa <= 0`, `0<=eps<=-kappa`,

then

`SAT(A,kappa+eps) subset SAT([A;B],kappa) subset SAT(A,kappa)`.          (3.1)

In particular, at `eps=0`,

`SAT([A;WA],kappa) = SAT(A,kappa)`                                      (3.2)

**pathwise**, for every `A`, every number `K` of added rows, and every row-substochastic `W`. The matrix `W` may be random, deterministic, dependent on `A`, or chosen adaptively after seeing `A`; no independence assumption enters (3.2).

### Proof

The right inclusion in (3.1) is immediate because the joint system contains every original row of `A`.

For the left inclusion, take a unit vector `x` with

`A x >= (kappa+eps) 1_m`.

For each added row,

`(W A x)_j >= s_j (kappa+eps)`.

Since `kappa+eps<=0` and `0<=s_j<=1`, multiplication by `s_j` moves a nonpositive number toward zero, so

`s_j(kappa+eps) >= kappa+eps`.

Also Cauchy--Schwarz gives

`e_j . x >= -||e_j||_2 ||x||_2 >= -eps`.

Therefore

`B_j . x = (WAx)_j + e_j.x >= (kappa+eps)-eps = kappa`.

The same `x` satisfies every original and every added inequality. This proves the left inclusion and hence (3.1). Setting `eps=0` makes the two outer events equal, giving (3.2). QED.

### Quantitative part and sharpness of the proof constant

The robust theorem loses exactly `eps` in the core margin, with coefficient `1`, independent of `m,N,K` and independent of every norm or singular value of `WA`. This coefficient is sharp for the **same-witness transfer**: if one tried to replace `eps` by `c eps` with `c<1`, take a scalar row whose value on a chosen unit witness is exactly `kappa+c eps`, put `W=[1]`, and choose a residual row with inner product `-eps` on that witness. The added inequality on that witness is then `kappa-(1-c)eps<kappa`.

No asymptotic or Gaussian input is used in the theorem.

## 4. Why this is a strict new class, not another singular-value reformulation

The previous NM13-12 theorem required a spectral tail condition

`s_{r+1}(B) <= -kappa`

and paid `r` dimensions. The new exact closure theorem imposes **no rank or singular-value condition at all** on the added block when it lies in the sub-stochastic row hull of the core.

The class difference is strict even deterministically. Take

`A=10 I_N`, `W=I_N`, `B=WA=10 I_N`, `kappa=-1`.

Then every added constraint is an exact duplicate, so (3.2) holds. Yet

`s_{r+1}(B)=10>1=-kappa`

for every `r<N`; thus the predecessor singular-quantile theorem cannot certify the same zero-loss statement for any sublinear or proper `r`.

There is also no restriction on the number of added rows: `K` can be linear, superlinear, or any finite function of `N`. This is a dimension-regime improvement obtained from order/convexity rather than an almost-kernel.

## 5. Concrete T03 application — full-rank dependent non-Gaussian barycentric rows

Fix `N`, and let the Gaussian core have `m>=N+1` iid rows

`g_1,...,g_m ~ N(0,I_N)`.

Independently sample `U_1,...,U_N iid Uniform[0,1]` and add exactly `N` constraints

`b_j := U_j g_j + (1-U_j) g_{N+1}`, `1<=j<=N`.                         (5.1)

Let `B` be the `N x N` matrix with rows `b_j`. Equivalently `B=WG`, where the `j`-th row of `W` is

`U_j e_j^T + (1-U_j) e_{N+1}^T`.

Every row of `W` is nonnegative and sums to exactly one. Therefore Theorem NM12-SSC gives the finite-N **identity of events**

`SAT([G;B],-1) = SAT(G,-1)`                                               (5.2)

for every realization of `G` and `U`.

This application is genuinely outside the iid Gaussian row class.

### 5.1 The added block is full rank almost surely

The first `N` columns of `W` form the diagonal matrix

`diag(U_1,...,U_N)`.

Since every `U_j` is nonzero almost surely, `rank(W)=N` almost surely. Conditional on such a `W`, each column of `B=WG` is an independent `N`-dimensional Gaussian vector with positive-definite covariance `WW^T`. Thus `B` has a Lebesgue density on `R^{N x N}`; the determinant-zero set has measure zero. Hence

`rank(B)=N` almost surely.                                                 (5.3)

So the application is not hiding an exact low-rank contaminant.

### 5.2 Each added row is non-Gaussian

For one coordinate of one row, write

`X = U Z_1 + (1-U) Z_2`,

with `U~Uniform[0,1]`, `Z_1,Z_2 iid N(0,1)`. Conditional on `U=u`, `X` is Gaussian with variance

`s(u)=u^2+(1-u)^2`.

Exact integration gives

`E s(U)=2/3`,

`E s(U)^2=7/15`.

Therefore

`E X^2=2/3`,

`E X^4=3 E s(U)^2=7/5`.

A Gaussian with variance `2/3` would have fourth moment

`3(2/3)^2=4/3`.

The gap is exactly

`7/5-4/3=1/15>0`,

and the standardized fourth moment is

`(7/5)/(2/3)^2=63/20=3.15`.

Thus the row marginal is not Gaussian. It is a genuine Gaussian variance mixture.

### 5.3 The added rows are mutually dependent

For distinct `j,k`, their common anchor `g_{N+1}` gives, coordinatewise,

`Cov(b_j,b_k)=E[(1-U_j)(1-U_k)] I_N = (1/4) I_N`.

Thus the added constraints are not independent of one another, and they are also built from the original core. This is precisely why ordinary iid-entry or iid-row universality hypotheses do not apply.

## 6. Exact probability transfer and threshold consequences

Let the Gaussian core density be `alpha`, so `m_N=floor(alpha N)`, and add the `N` rows (5.1). The total number of constraints is `m_N+N`, i.e. total density `alpha+1+o(1)`.

Equation (5.2) gives for every `N` the exact identity

`P{augmented model SAT with m_N+N rows}`
` = P{Gaussian T03 core SAT with m_N rows}`.                              (6.1)

Consequently every asymptotic SAT/UNSAT transition statement transfers by an **exact density translation of +1**. No existence of an exact limiting threshold is needed to state this: lower and upper transition points, liminf/limsup thresholds, or any certified finite-density implication all translate by `+1`.

Using the project endpoints:

### Fully rigorous inherited bracket

From the rigorous Gaussian lower endpoint

`alpha_L=6.302974375068753...`

and the older rigorous upper endpoint

`alpha_U,old=12.78437096216`,

(6.1) gives the dependent non-Gaussian augmented model the rigorous bracket

`7.302974375068753... <= lambda_c <= 13.78437096216`.                    (6.2)

### Current project candidate transfer

NM13-07's newest report has a **CANDIDATE_FULL** Gaussian upper endpoint

`alpha_U,cand=12.31963485`,

pending later independent review. Equation (6.1) transfers that status with no additional uncertainty or approximation:

`lambda_U,cand = 13.31963485`.                                           (6.3)

The candidate bracket width is unchanged by translation:

`13.31963485 - 7.302974375068753`
` = 12.31963485 - 6.302974375068753`
` = 6.016660474931247`.

Thus the new theorem does not manufacture a better T03 number; it proves exact universality of the entire probability sequence for a full-rank dependent non-Gaussian extension.

## 7. Parent before/after versus demonstrated theory gain

### Original T03 parent claim

Entering this NM13-12 run, the current project state is

- rigorous lower `6.302974375068753...`;
- newest peer candidate upper `12.31963485`, pending independent review;
- older rigorous upper `12.78437096216` retained as a conservative fully reviewed/source-rigorous comparison point.

**Before this run:** no change by NM13-12.  
**After this run:** exactly the same T03 source state.

The parent source metric therefore has **NO MOVEMENT** in this run.

### Demonstrated universality gain

Before this run, NM13-12's strongest arbitrary-extra-row theorem required an almost-kernel / singular-quantile condition and sacrificed dimensions.

After this run, for the new barycentric class:

- arbitrary finite `K` added constraints are allowed;
- the added block can have full rank `N`;
- no singular-value bound is assumed;
- rows may be dependent on each other and on the core;
- row marginals may be non-Gaussian;
- there is **zero dimension loss and zero probability loss** at `eps=0`;
- with row perturbations of norm at most `eps`, the only price is the exact finite-N margin shift `kappa -> kappa+eps`.

This is a strict distributional-class and dimension-regime extension, proved pathwise.

### Applied augmented-model quantity

Before: the exact transition behavior of the concrete dependent/non-Gaussian model (5.1) was `UNKNOWN / UNMEASURED` in this namespace.

After: its entire finite-N satisfiability probability sequence is exactly identified with T03 after the density translation `lambda=alpha+1`; in particular (6.2) is rigorous and (6.3) transfers the current peer candidate status exactly.

Unknown was not treated as zero.

## 8. Essential checker and executed output

Executed checker source:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0655Z__t03_substochastic_barycentric_check.py`

Archived actual output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/2026-09-20T0655Z__t03_substochastic_barycentric_check.out`

The checker independently verifies:

1. exact moment identities `E[X^2]=2/3`, `E[X^4]=7/5`, Gaussian comparator `4/3`, fourth-moment gap `1/15`, kurtosis `63/20`;
2. a deterministic class-separation example `A=B=10 I_5` with full rank and minimum singular value `10>1`;
3. a seeded finite full-rank realization of the random barycentric model;
4. 20,000 sampled sphere points with zero violations of the pathwise redundancy implication;
5. the `+1` threshold arithmetic and unchanged bracket width.

The archived output ends

`ALL_SUBSTOCHASTIC_BARYCENTRIC_CHECKS_PASS`.

The random sampling is only a sanity check. The theorem itself is proved analytically above and does not rely on the sampling.

## 9. Bounded literature boundary, 20 September 2026

A bounded fresh search for combinations of `spherical perceptron`, `correlated/dependent patterns`, `convex combinations`, and `universality` did not surface a primary theorem matching the finite-N row-substochastic closure identity (3.2). The search did recover the known negative spherical-perceptron literature, including Stojnic's fully lifted RDT work (`arXiv:2312.16531`) and the star-shaped solution-geometry work of Annesi et al. Those results concern the geometry/analysis of the usual random-pattern model, not the pathwise redundancy of data-dependent barycentric constraint rows. This is bounded negative evidence only, not a novelty certificate.

`POSTED.md` continues to mark row-submatrix, mesoscopic-spike, kernel/neural, ReLU, and zero-margin/Ising results as posted/excluded. None is used as a new claim here.

## 10. Residual obstruction and next attack

The new theorem exactly characterizes one large dependent closure class, but it does **not** solve the P12 triangular B4 successor and it does not improve the pure-Gaussian T03 threshold.

The next nonduplicating quantitative question suggested by (3.1) is no longer spectral: allow signed barycentric coefficients with small total negative mass and derive a source-valid transfer using a simultaneous upper control on the core projections at the witness. That requires a genuinely new two-sided margin mechanism; nonnegative convexity alone no longer suffices. A second possible route is to combine the robust `eps` version with a proved near-margin modulus from a future T03 certificate. Either route is materially distinct from the exhausted covariance/singular-quantile sequence.

No historical or peer file was overwritten. No shared ledger, schedule, permission, workflow, public surface, email/Drive resource, or paid-compute resource was changed.

## ledger_delta

```yaml
track: NM13-12
root: proofnet24/NM13-12/progress-universality
parent: T03 negative spherical perceptron
runtime_model: GPT-5.6 Sol
runtime_reasoning: UNVERIFIED
p12_latest: proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T18-20-03Z__run-report.md
p12_frozen_hypotheses:
  iid: true
  centered: true
  variance_one: true
  densities: true
  fixed_q: true
  uniform_finite_convolution_Linfty: true
  N_over_m_to_gamma_gt_1: true
  k_log_m_o_m: true
  fourth_moment_required: false
p12_unresolved_successor: triangular smooth/bounded-fourth-moment universality without uniform microscopic finite-convolution smoothing
parent_metric: T03 source threshold bracket
parent_before:
  lower_rigorous: 6.302974375068753
  upper_candidate_pending_review: 12.31963485
  upper_older_rigorous: 12.78437096216
parent_after:
  lower_rigorous: 6.302974375068753
  upper_candidate_pending_review: 12.31963485
  upper_older_rigorous: 12.78437096216
parent_movement: none by NM13-12
theory_gain:
  theorem: NM12-SSC sub-stochastic barycentric closure
  finite_N: true
  exact_event_identity_at_eps_0: true
  robust_margin_loss: eps
  rank_restriction: none
  singular_value_restriction: none
  added_row_count_restriction: none finite
  dependence_allowed: arbitrary/adaptive
application:
  added_rows: b_j = U_j g_j + (1-U_j) g_{N+1}
  count: N
  block_rank: N almost surely
  row_marginal_gaussian: false
  row_dependence: true
  exact_density_translation: +1
  rigorous_lower: 7.302974375068753
  candidate_upper_pending_review: 13.31963485
  older_rigorous_upper: 13.78437096216
checker_status: ALL_SUBSTOCHASTIC_BARYCENTRIC_CHECKS_PASS
status: PARTIAL / NEW THEOREM / ORIGINAL T03 OPEN
next: signed small-negative-mass barycentric transfer or robust-eps transfer using a proved T03 margin modulus
```
