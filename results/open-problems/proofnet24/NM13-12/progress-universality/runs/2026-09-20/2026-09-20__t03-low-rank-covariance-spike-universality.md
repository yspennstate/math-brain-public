Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this run exposes no authenticated applied-model / reasoning-effort receipt, so I do not claim otherwise.

# NM13-12 progress-universality — low-rank covariance-spike universality for the negative spherical perceptron

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-12`  
Progress root: `proofnet24/NM13-12/progress-universality/`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Parent: T03 negative spherical perceptron at `kappa=-1`  
Status: **PARTIAL / NEW THEOREM PROVED / STRICT DISTRIBUTIONAL-CLASS AND DIMENSION-REGIME GAIN / ORIGINAL T03 BRACKET UNCHANGED**

## 1. Compact handoff and latest P12 state

The latest retained P12 report remains

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T07-17-16Z__run-report.md`.

Its frozen theorem is exactly this. For `F in {R,C}`, with `d_R=1` and `d_C=2`, let `A_m` have iid centered variance-one entries with density `f_m`. Assume one fixed integer `q>=1` and one fixed `M<infinity` such that

`sup_m ||f_m^{*q}||_infinity <= M`,

`N_m/m -> gamma>1`,

`k_m=r_m+1`,

`k_m log m=o(m)`.

Then

`(k_m/m) log M^F_{m,r_m}(A_m) ->_P -h(gamma)/d_F`.

There is **no fourth-moment assumption** and no positive-moment assumption beyond variance normalization. The unresolved mathematical successor named by the frozen P12 state is triangular smooth / bounded-fourth-moment universality **without** a uniform microscopic finite-convolution smoothing hypothesis. P12's remaining own-track obligations are protocol/final-package gates, not a missing author-side theorem.

`POSTED.md` excludes rediscovery of the two row-submatrix papers, kernels, ReLU results and zero-margin / Ising perceptron work. This run does not touch any of those claims.

The two preceding NM13-12 progress-universality runs proved row-radial comparison theorems for negative-margin feasibility: first an all-row radial sandwich, then a quantile/trimmed radial theorem allowing a small fraction of order-one lower-radius defects. Their common structural hypothesis is that rows have **uniform spherical directions** and are changed only by positive row scales.

This run intentionally switches method after those two radial attacks. It changes the **column covariance geometry**, not the row radii. The resulting row directions are anisotropic angular-Gaussian directions and their radii are direction-dependent, so the previous radial theorems do not apply.

## 2. Exact T03 baseline and coordination with NM13-03 / NM13-07

Freeze T03 exactly:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- seek `sigma` with `||sigma||_2=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x in S^{N-1}` satisfying `Gx>=-1`.

The fully certified repository bracket entering and leaving this run is

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`width = 6.48139658710`.

NM13-07 has proved an exact two-scalar reduction of the complete second-full stationarity system and numerically locates an `alpha=12.75` point with positive comparison value. NM13-03 has removed the nested Gaussian/automatic-differentiation layer by a closed one-dimensional kernel and exhibits a robust Poincare--Miranda rectangle. Both correctly keep `12.75` as **CANDIDATE_FULL / review-pending**, because directed continuum enclosure of the face signs and positive objective is still missing.

I do not duplicate their second-full stationarity equations or interval-certification problem. The theorem below is a distributional transfer statement. If `12.75` is later certified for isotropic T03, its upper endpoint will transfer automatically to the covariance-spike class proved here, with no new lifted-RDT calculation.

## 3. New route: deterministic covariance geometry

For an `M x N` matrix `A` and `kappa<0`, write

`SAT(A,kappa) := { exists x in S^{N-1} : Ax >= kappa * 1_M }`.

Let `G` be an arbitrary real `M x N` matrix and let `Sigma` be positive definite. Put

`A = G Sigma^{1/2}`.

This is a **column deformation**. For Gaussian `G`, the rows of `A` are iid `N(0,Sigma)`.

### Theorem NM12-COV-1 (general covariance margin sandwich)

Let

`a = sqrt(lambda_min(Sigma))`,
`b = sqrt(lambda_max(Sigma))`.

For every `kappa<0`, pathwise in `G`,

`SAT(G, kappa/b) subset SAT(G Sigma^{1/2}, kappa) subset SAT(G, kappa/a)`.

#### Proof

For the left inclusion, let `z in S^{N-1}` satisfy `Gz >= kappa/b`. Define

`x = Sigma^{-1/2} z / ||Sigma^{-1/2}z||`.

Then `x in S^{N-1}` and

`Sigma^{1/2}x = r z`,
`r = 1/||Sigma^{-1/2}z||`.

The spectral bounds give `a<=r<=b`. For a row value `t=(Gz)_j`, if `t>=0` then `rt>=0>kappa`. If `t<0`, then `r<=b` implies `rt>=bt`, and `t>=kappa/b` gives `bt>=kappa`. Hence every row of `G Sigma^{1/2}x` is at least `kappa`.

For the right inclusion, let `x in S^{N-1}` satisfy `G Sigma^{1/2}x >= kappa`. Set

`y=Sigma^{1/2}x`,
`r=||y||`,
`z=y/r`.

Then `a<=r<=b` and

`Gz = (Gy)/r >= kappa/r`.

Because `kappa<0` and `r>=a`, one has `kappa/r >= kappa/a`. Hence `Gz>=kappa/a`, proving the inclusion. QED.

This already gives quantitative covariance robustness, but it pays for the largest eigenvalue. The next theorem removes that dependence completely for low-rank positive semidefinite spikes.

## 4. Main theorem: exact finite-N rank-defect sandwich with arbitrary spike magnitude

Let

`Sigma = I_N + B`,

where `B` is positive semidefinite of rank `r<N`. No upper bound on `||B||_op` is assumed.

Let

`p_iso(M,n,kappa) = P{ SAT(G_{M x n},kappa) }`

for an iid standard Gaussian matrix of the displayed size, and

`p_spike(M,N,B,kappa) = P{ SAT(G_{M x N}(I+B)^{1/2},kappa) }`.

### Theorem NM12-COV-2 (low-rank PSD-spike universality sandwich)

For every finite `M,N`, every `kappa<0`, and every deterministic `B>=0` of rank `r<N`,

`p_iso(M,N-r,kappa) <= p_spike(M,N,B,kappa) <= p_iso(M,N,kappa)`.

The same statement holds conditional on any random `B` independent of `G`; hence it also holds after averaging over such a random spike.

#### Proof: upper comparison

Since `B>=0`, `Sigma=I+B>=I`, so `lambda_min(Sigma)>=1`. The right inclusion in NM12-COV-1 with `a>=1` gives

`SAT(G Sigma^{1/2},kappa) subset SAT(G,kappa/a)`.

Because `kappa<0` and `a>=1`, `kappa/a>=kappa`; satisfying the harder margin `kappa/a` implies satisfying margin `kappa`. Therefore pathwise

`SAT(G Sigma^{1/2},kappa) subset SAT(G,kappa)`,

and thus

`p_spike(M,N,B,kappa) <= p_iso(M,N,kappa)`.

No bound on `lambda_max(Sigma)` appears.

#### Proof: lower comparison

Let `Q` be an `N x (N-r)` matrix whose columns form an orthonormal basis of `ker(B)`. On this subspace,

`Sigma Q = Q`

and therefore, by functional calculus for the positive semidefinite matrix `Sigma`,

`Sigma^{1/2} Q = Q`.

If `z in S^{N-r-1}` satisfies

`(GQ)z >= kappa`,

then `x=Qz in S^{N-1}` and

`G Sigma^{1/2}x = G Sigma^{1/2}Qz = GQz >= kappa`.

Thus

`SAT(GQ,kappa) subset SAT(G Sigma^{1/2},kappa)`.

For deterministic `Q`, rotational invariance of the standard Gaussian law implies that `GQ` is an iid standard Gaussian `M x (N-r)` matrix. Hence

`p_iso(M,N-r,kappa) <= p_spike(M,N,B,kappa)`.

If `B` is random but independent of `G`, condition on `B` and its kernel basis `Q`; the same argument applies conditionally, then average. QED.

### What is new relative to the radial theorems

This theorem is not a row-scaling reformulation.

For a nonscalar `Sigma`, a row `g Sigma^{1/2}` has an angular Gaussian / projected-normal direction rather than a uniform spherical direction; its radius and direction are dependent. In particular, for a rank-one spike

`Sigma_N = I_N + theta_N v_N v_N^T`

with `theta_N -> infinity`, the condition number diverges and the angular law becomes increasingly anisotropic. Neither the predecessor all-row condition `max_a |S_a-1|->0` nor the quantile radial model `S_a * sqrt(N) theta_a` with `theta_a` uniform independent of `S_a` describes this distribution.

NM12-COV-2 nonetheless has **no dependence at all on `theta_N`**. It pays only the lost dimension `r`.

## 5. Asymptotic dimension-regime corollary

Suppose `r_N/N -> rho in [0,1)` and `B_N>=0` has rank `r_N`. Let `M_N=floor(alpha N)`.

Assume an isotropic Gaussian SAT lower threshold `L(kappa)` is rigorously known in the standard sense:

for every `beta<L(kappa)`,
`p_iso(floor(beta n),n,kappa)->1`.

Assume an isotropic Gaussian UNSAT upper threshold `U(kappa)` is rigorously known:

for every `beta>U(kappa)`,
`p_iso(floor(beta n),n,kappa)->0`.

Then NM12-COV-2 gives

- SAT whp in the spiked model whenever
  `alpha < (1-rho)L(kappa)`;
- UNSAT whp in the spiked model whenever
  `alpha > U(kappa)`.

#### Proof

Let `d_N=N-r_N`, so `d_N/N->1-rho`.

If `alpha<(1-rho)L(kappa)`, choose `beta` with

`alpha/(1-rho) < beta < L(kappa)`.

For all large `N`,

`M_N/d_N < beta`.

By monotonicity in the number of constraints and the isotropic lower theorem,

`p_iso(M_N,d_N,kappa)->1`.

The lower comparison in NM12-COV-2 then gives spiked SAT probability tending to one.

If `alpha>U(kappa)`, the isotropic `N`-dimensional SAT probability tends to zero, and the upper comparison in NM12-COV-2 forces the spiked SAT probability to zero. QED.

### Sublinear-rank universality

If

`r_N=o(N)`,

then `rho=0`, and **every currently rigorous isotropic threshold bracket transfers with no asymptotic loss**:

`L(kappa) <= alpha_c^spike(kappa) <= U(kappa)`

in the same lower/upper threshold sense, regardless of how large the nonzero eigenvalues of `B_N` are.

Moreover, if the isotropic model has an actual sharp limiting threshold `alpha_c(kappa)`, then the same finite-N sandwich proves that every deterministic or independent-random PSD spike of rank `o(N)` has the same limiting threshold.

This is the strict dimension-regime gain: the theorem tolerates an unbounded anisotropic perturbation on `o(N)` directions.

## 6. Concrete unresolved probability application: diverging-spike T03

Fix any deterministic orthogonal projection `P_N` of rank

`r_N=floor(N^(2/3))`

and any nonnegative spike amplitude `theta_N`; to make the separation from previous near-isotropy results explicit one may take, for example,

`theta_N = exp(N^(1/4))`.

Define iid Gaussian constraints

`h_a ~ N(0, Sigma_N)`,
`Sigma_N = I_N + theta_N P_N`,

and ask whether there exists `x in S^{N-1}` such that

`<h_a,x> >= -1`,
`1<=a<=floor(alpha N)`.

The exact threshold of this anisotropic negative spherical perceptron is unresolved.

Here

`rank(Sigma_N-I_N)=floor(N^(2/3))=o(N)`

while

`||Sigma_N-I_N||_op = theta_N -> infinity`.

Thus this model lies far outside operator-norm perturbative covariance universality and outside both predecessor radial theorems.

Applying NM12-COV-2 and the current rigorous T03 endpoints gives:

### Theorem NM12-T03-SPIKE

For the model above, for every choice of nonnegative `theta_N` (including the displayed diverging choice),

- if `alpha < 6.30297437506`, SAT probability tends to one;
- if `alpha > 12.78437096216`, SAT probability tends to zero.

Therefore the anisotropic diverging-spike model inherits the current rigorous bracket

`[6.30297437506, 12.78437096216]`

**with no loss whatsoever**, despite an arbitrarily large covariance spike.

#### Verification of transferred hypotheses

- Rows are independent Gaussian `N(0,Sigma_N)` because they are `g_a Sigma_N^{1/2}` with independent `g_a~N(0,I)`.
- The feasible vector remains on the exact unit sphere (equivalently radius `sqrt(N)` in the source normalization).
- The margin remains exactly `kappa=-1`.
- The spike is PSD, so the upper comparison applies.
- Its rank is `o(N)`, so the complement dimension is `N-o(N)` and the lower isotropic density is asymptotically unchanged.
- No row-radius independence, bounded condition number, bounded fourth moment beyond Gaussianity, or microscopic smoothing hypothesis is used.

This is a concrete new probability theorem, not a framework proposal.

### Positive-density rank tradeoff

The same proof gives an explicit bracket when `r_N/N->rho>0`:

`[(1-rho)*6.30297437506, 12.78437096216]`.

Examples:

- `rho=0.01`: lower `6.23994463131`;
- `rho=0.05`: lower `5.98782565631`;
- `rho=0.10`: lower `5.67267693755`;
- `rho=0.20`: lower `5.04237950005`.

The upper endpoint is unchanged for every PSD spike, even at positive rank density and with unbounded spike magnitude.

## 7. Parent T03 before/after versus demonstrated theory gain

### Applied parent claim: exact isotropic T03

Certified before:

`[6.30297437506, 12.78437096216]`,
width `6.48139658710`.

Certified after:

`[6.30297437506, 12.78437096216]`,
width `6.48139658710`.

**No movement on the original isotropic T03 bracket is claimed.**

NM13-03/NM13-07's `12.75` endpoint remains review-pending; I do not count it as certified.

### Demonstrated theory gain

Before this run, NM13-12 could transfer T03 bounds only through row-radial models with uniform spherical directions, first under all-row radius control and then under a quantile/defect condition.

After this run, T03 bounds transfer to the genuinely anisotropic Gaussian class

`N(0, I_N+B_N)`

for arbitrary PSD `B_N` of sublinear rank, with **no restriction on `||B_N||_op`** and no change in the asymptotic bracket. At positive rank density `rho`, the exact finite-N theorem yields the explicit lower-density factor `1-rho` while preserving the isotropic upper endpoint.

This is a strict distributional-class and dimension-regime extension.

### Coordination payoff

If NM13-03 and NM13-07 later complete the rigorous `alpha_U=12.75` certificate, NM12-COV-2 immediately upgrades every PSD-spiked model here from

`alpha_U=12.78437096216`

to

`alpha_U=12.75`

without any additional anisotropic calculation. Their stationarity work therefore remains complementary rather than duplicated.

## 8. Fresh bounded literature check

A targeted 20 September 2026 search for combinations of

- `"negative spherical perceptron" anisotropic covariance`,
- `"spherical perceptron" spiked covariance`,
- `perceptron covariance Gaussian ellipsoid`

recovered the standard isotropic negative-spherical-perceptron literature (including El Alaoui--Sellke and Stojnic) and solution-geometry work, but did not surface a primary theorem matching the finite-N low-rank PSD covariance sandwich above. This is bounded negative evidence only, not a priority or worldwide novelty certificate.

The source-exact public T03 papers continue to use iid standard Gaussian constraints. Stojnic's fully lifted RDT paper continues to describe substantial numerical work as necessary for concrete negative-capacity values; El Alaoui--Sellke's algorithmic-pure-state paper remains on the exact Gaussian source model but does not settle the full-radius negative threshold.

## 9. Essential executed sanity checker

Executed source:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_spike_universality_check.py`

Archived output:

`proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_spike_universality_check.out`

The checker is only a sanity layer; the theorem proof above is analytic. It numerically verifies on random finite matrices:

1. the explicit witness transformation in both directions of NM12-COV-1;
2. the identity `Sigma^{1/2}Q=Q` on the low-rank spike kernel and `G Sigma^{1/2}Qz=(GQ)z`;
3. the T03 rank-fraction bracket arithmetic.

The archived output ends `ALL_CHECKS_PASS`.

## 10. Failure accounting and next attack

This run is not another unchanged radial attempt; it executes a materially different column-covariance method and proves a new theorem.

The original isotropic T03 metric remains unchanged because a universality transfer theorem cannot by itself sharpen the isotropic Gaussian endpoint. The nearest source-moving opportunity is still NM13-03/NM13-07's directed interval enclosure for `12.75`, which this worker does not duplicate.

The next nonduplicating universality problem exposed by NM12-COV-2 is **signed low-rank covariance deformation**: allow `Sigma-I` to have both positive and negative eigenvalues while keeping `lambda_min(Sigma)` bounded away from zero and rank `o(N)`. The complement argument still gives the full lower transfer, but the exact same-margin upper inclusion fails when eigenvalues below one are present. Any successful next route must control whether an anisotropic feasible witness can concentrate in that exceptional `o(N)` subspace; a sphere-net or Gaussian-width argument would have to beat `M=Theta(N)` constraints without smuggling in a radius change.

No historical file, peer file, root ledger, schedule, permission, workflow, public surface, email, Drive object, or paid-compute resource was modified.

```yaml
ledger_delta:
  worker: NM13-12
  parent: T03
  target: "quantitative universality / covariance deformation for negative spherical perceptron"
  status: "PARTIAL / NEW THEOREM PROVED / PARENT T03 OPEN"
  p12_state:
    latest_report: "proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T07-17-16Z__run-report.md"
    frozen_hypotheses: "iid centered variance-one density; fixed q,M with sup ||f_m^{*q}||_inf<=M; N_m/m->gamma>1; k_m log m=o(m)"
    unresolved_successor: "triangular smooth/B4 laws without uniform microscopic finite-convolution smoothing"
  parent_metric:
    quantity: "certified isotropic T03 threshold bracket"
    before: "[6.30297437506, 12.78437096216]"
    after: "[6.30297437506, 12.78437096216]"
    width_before: "6.48139658710"
    width_after: "6.48139658710"
    movement: "NONE"
  theory_gain:
    theorem_1: "NM12-COV-1 general covariance margin sandwich"
    theorem_2: "NM12-COV-2 exact finite-N low-rank PSD-spike probability sandwich"
    exact_finite_N: "p_iso(M,N-r,kappa) <= p_spike(M,N,B,kappa) <= p_iso(M,N,kappa)"
    assumptions: "kappa<0; B>=0; rank(B)=r<N; no upper bound on ||B||op"
    sublinear_rank_gain: "r_N=o(N) transfers the full isotropic threshold bracket with zero asymptotic loss"
    positive_density_gain: "r_N/N->rho transfers lower endpoint multiplied by 1-rho and preserves upper endpoint"
  concrete_application:
    model: "h_a iid N(0,I+theta_N P_N), rank(P_N)=floor(N^(2/3)), theta_N arbitrary nonnegative and may diverge"
    proved_bracket: "[6.30297437506, 12.78437096216]"
    distinction: "anisotropic angular Gaussian directions; radius-direction dependence; unbounded covariance condition number allowed"
  coordination:
    NM13-03: "closed 1D kernel + Miranda rectangle at alpha=12.75 remains review-pending continuum enclosure"
    NM13-07: "exact two-scalar second-full reduction; alpha=12.75 remains conditional"
    transfer_if_12p75_certified: "same 12.75 upper endpoint automatically for every PSD-spiked class covered here"
  artifacts:
    checker: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_spike_universality_check.py"
    output: "proofnet24/NM13-12/progress-universality/runs/2026-09-20/artifacts/t03_lowrank_spike_universality_check.out"
    output_status: "ALL_CHECKS_PASS"
  residual_obstruction: "original isotropic Gaussian upper endpoint unchanged; signed low-rank covariance needs a new upper-transfer mechanism"
  next_attack: "signed rank-o(N) covariance perturbations with lambda_min bounded away from zero; control exceptional-subspace witness concentration"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
