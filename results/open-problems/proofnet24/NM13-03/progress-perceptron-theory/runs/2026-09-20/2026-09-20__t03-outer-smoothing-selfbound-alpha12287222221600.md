Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-03 / T03 — Gaussian smoothing curvature, score self-bound, and supported alpha=12.287222221600

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW EXACT GAUSSIAN COMPARISON-FEASIBILITY LEMMA / STRICT SUPPORTED-CONDITIONAL THRESHOLD IMPROVEMENT / THIRD-FULL DIRECTED CERTIFICATE STILL OPEN**

## 0. Compact handoff and source freeze

The source problem remains exactly

- `M=floor(alpha N)`;
- rows `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- constraints `<g_a,sigma> >= -sqrt(N)` for every `a<=M` (`kappa=-1`);
- fixed `alpha`, `N->infinity`.

No ball relaxation, smaller sphere, radial normalization, Ising restriction, algorithmic-class threshold, or replica-only number is used as a source implication.

The latest companion report on `master`,

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-semiconcave-cell-compiler-alpha1231963444619075.md`,

has now exhausted the complete-second transport chart at the review-pending directed endpoint

`alpha_U = 12.31963444619075`,

and proved the sharp inner hinge semiconcavity

`-ell <= U'' <= 0`, `ell=beta/(1+beta)`,

plus closed Gaussian conditional cell masses. Its named remaining obstruction is **uniform outward evaluation of the nested third-full branch parameter tube**, especially the outer `V` layer feeding the KL-free final Schur row. The immediately preceding NM13-03 report had already eliminated `D_H` exactly from that final row, leaving `Q=E_V q(V)` and `S1=E_V g(V)^2` as central quantities.

This run attacks that exact outer layer. It does not return to complete-second decimal mining.

A repository search for the formula below (`q''`, `m ell/(1+m ell d^2)`, and the resulting `S1` versus `Q` self-bound) found no prior project instance. Thus the lemma is **unposted in this repository**. Publication novelty is not claimed.

## 1. Primary-source status, refreshed 20 September 2026

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their model is exactly the iid-Gaussian spherical perceptron on the sphere of radius `sqrt(N)`, with `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, however, the algorithm in the abstract outputs on radius `sqrt(qbar N)` with `qbar in (0,1)` and only expects `qbar -> 1` near capacity. This is not the exact full-radius threshold theorem required here.
2. **Stojnic, arXiv:2312.16531.** This fits the negative spherical perceptron into stationarized fully lifted RDT and states a capacity characterization; the abstract explicitly notes that making the framework practically operational requires substantial numerical work and reports rapid convergence by the third stationarized level. The repository continues to require a directed stationary-root/inclusion layer before promoting finite-lift numerical values.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** They prove rigorous upper and lower bounds on the interpolation threshold and characterize the linear-programming threshold, not the exact `kappa=-1` SAT/UNSAT threshold. The repository retains `alpha_L=6.30297437506` from this rigorous layer.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717**, compute the transition using a full-RSB ansatz. **Winer--Herderschee, arXiv:2503.11761**, give a jammed Parisi ansatz and threshold/SAT-probability calculations. Both are structural guidance, not the missing directed exact-radius proof.
5. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** They exactly characterize a dimension-free-Lipschitz algorithmic projection-pursuit class and explicitly state that characterization of unrestricted feasible projections remains a major outstanding challenge.

A bounded fresh search on 20 September 2026 did not surface a later rigorous theorem plainly closing the unrestricted exact-radius `kappa=-1` target. This is dated negative search evidence, not a novelty or priority certificate. `POSTED.md` zero-margin/Ising exclusions remain different source problems.

## 2. Original problem before / after

There are two tiers and they must not be conflated.

### 2.1 Review-pending directed tier

The companion has essentially exhausted the complete-second linear transport certificate. This run makes **no directed-tier change**:

`before = after = [6.30297437506, 12.31963444619075]`,

width

`6.01666007113075`.

I do not claim a new directed third-full root.

### 2.2 Stronger supported-CONDITIONAL third-full tier

The preceding supported conditional endpoint was

`12.287222221605`.

The executed checker solves the complete-third fixed-density stationary equations at

`boxed: alpha = 12.287222221600`.

Thus the supported conditional bracket moves strictly from

`[6.30297437506, 12.287222221605]`

to

`boxed: [6.30297437506, 12.287222221600]`,

with exact width

`boxed: 5.984247846540`.

The supported upper-endpoint gain is exactly

`boxed: 5e-12`.

This is a source-level threshold candidate improvement, not merely an auxiliary constant, but it remains **SUPPORTED CONDITIONAL / NUMERICAL_ONLY**, not directed interval arithmetic.

## 3. New exact theorem — Gaussian smoothing sharpens semiconcavity and self-bounds the score

Let `U:R->R` be `C^2` with

`U <= 0`, `U' <= 0`, and `-ell <= U'' <= 0`

for some `ell>=0`. Fix `m>0`, `d>0`, and define

`Z(a)=E_G exp[m U(a+dG)]`,

`q(a)=log Z(a)`.

Let `nu_a` be the tilted law of

`T=a+dG`

with density proportional to

`exp[mU(t)] exp[-(t-a)^2/(2d^2)] dt`.

Put

`L := m ell/(1+m ell d^2)`.

### Theorem NM03-T03-OUTER-SMOOTHING-SELFBOUND

Under the hypotheses above:

1. **Derivative and variance identities**

   `q'(a)=m E_{nu_a} U'(T)`,

   `q''(a)=-1/d^2 + Var_{nu_a}(T)/d^4`.

2. **Sharp inherited semiconcavity**

   `boxed: -L <= q''(a) <= 0` for every `a`.

   The constant is exact for the fully quadratic extremizer `U(t)=-ell t^2/2`.

3. **Self-bounding score inequality**

   `boxed: q'(a)^2 <= 2 L [-q(a)]`.

   Writing

   `g(a)=E_{nu_a}U'(T)=q'(a)/m`,

   this is

   `boxed: g(a)^2 <= [2 ell/(m(1+m ell d^2))] [-q(a)]`.      (3.1)

4. If `A` is any random outer mean independent of the inner Gaussian, then

   `boxed: E g(A)^2 <= [2 ell/(m(1+m ell d^2))] E[-q(A)]`.   (3.2)

5. For an affine outer coordinate `a(v)=a0+s v`, put `r(v)=q(a(v))`. Then

   `-Ls^2 <= r''(v) <= 0`.

   On a cell `[v0-h/2,v0+h/2]`, the midpoint tangent

   `T0(v)=r(v0)+r'(v0)(v-v0)`

   obeys

   `boxed: T0(v)-(Ls^2/2)(v-v0)^2 <= r(v) <= T0(v)`.        (3.3)

   Consequently the Gaussian-weighted upper/lower cell integrals differ by at most

   `boxed: (Ls^2 h^2/8) * P(G in cell)`,                    (3.4)

   and the total central error over equal-width cells is at most `Ls^2 h^2/8` before endpoint-evaluation uncertainty and tails.

### Proof

Differentiate the Gaussian mean parameter. Since

`log dnu_a/dt = const + mU(t) -(t-a)^2/(2d^2)`,

the score identity gives

`E_{nu_a}[(T-a)/d^2]=m E_{nu_a}U'(T)`.

The left-hand side is exactly `q'(a)`, proving the first derivative formula. A second derivative in the Gaussian mean parameter gives

`q''(a)=-1/d^2+Var_{nu_a}(T)/d^4`.                           (3.5)

Write the tilted potential

`W_a(t)=(t-a)^2/(2d^2)-mU(t)`.

The curvature assumptions on `U` give

`lambda:=1/d^2 <= W_a''(t) <= Lambda:=1/d^2+m ell`.         (3.6)

For the upper variance bound, one-dimensional Brascamp--Lieb gives

`Var_{nu_a}(T) <= d^2`.                                     (3.7)

For the lower variance bound, integration by parts gives

`E[(T-ET)W_a'(T)] = 1`.                                     (3.8)

Also `E W_a'(T)=0`. Because `W_a'` is globally `Lambda`-Lipschitz, an independent-copy argument gives

`Var(W_a'(T))`
` = (1/2)E[W_a'(T)-W_a'(T')]^2`
` <= Lambda^2 Var(T)`.                                      (3.9)

Cauchy--Schwarz in (3.8), followed by (3.9), yields

`1 <= sqrt(Var(T) Var(W_a'(T))) <= Lambda Var(T)`,

hence

`Var(T) >= 1/Lambda = d^2/(1+m ell d^2)`.                   (3.10)

Substituting (3.7)--(3.10) into (3.5) gives

`-m ell/(1+m ell d^2) <= q'' <= 0`,

proving item 2.

For item 3, set `f=-q`. Because `U<=0`, `Z(a)<=1`, so `f>=0`. Item 2 says `f` is convex with `0<=f''<=L`; in particular it is `L`-smooth. The elementary descent inequality is

`f(y) <= f(a)+f'(a)(y-a)+(L/2)(y-a)^2`.

For `L>0`, choose `y=a-f'(a)/L`. Since `f(y)>=0`,

`0 <= f(a)-f'(a)^2/(2L)`,

which is exactly `q'(a)^2<=2L[-q(a)]`. The `L=0` case follows by continuity (and in the present hinge application `L>0`). Dividing by `m^2` proves (3.1), and averaging proves (3.2).

Finally, composition with `a(v)=a0+sv` gives the stated curvature interval for `r`. The tangent upper bound follows from concavity, and the quadratic lower bound follows by integrating `r''>=-Ls^2`. On a midpoint cell, `|v-v0|<=h/2`, so the pointwise gap is at most `Ls^2 h^2/8`; multiplying by the Gaussian density and integrating proves (3.4). QED.

### Tail closure for the perceptron hinge

For the dimensionless hinge kernel

`U_beta(t)=log E_H exp[-beta(t+H)_+^2/2]`,

Jensen gives

`0 <= -U_beta(t) <= (beta/2) E(t+H)_+^2`.

Applying Jensen again to `q` gives

`0 <= -q(a)`
` <= (m beta/2) E(a+sqrt(1+d^2)G)_+^2`.                    (3.11)

Combining (3.11) with the self-bound also gives an explicit tail cage for `|q'|` and hence for `|g|`. Thus the second-order outer cell compiler closes with elementary Gaussian tails; it does not introduce a new quadrature dimension.

## 4. Application to NM13-07's named third-full obstruction

The latest companion positive-gap compiler uses

`d^2=w1/w0`,

`a(v)=sqrt(w2/w0) v - 1/sqrt(w0)`,

`m=c3/c2`,

and, by its exact hinge theorem,

`ell=beta/(1+beta)`.

Its KL-free final row is of the form

`Rhat_H = A_alg Q + B_alg S1`,

where

`Q=E_V q(a(V))`,

`S1=E_V g(a(V))^2`,

and `A_alg,B_alg` are algebraic functions of `(w0,w1,m,x)`.

The theorem gives two new pieces of proof infrastructure that were absent from the preceding compiler.

### 4.1 Second-order outer `Q` enclosure

The conditional log-partition itself satisfies

`-L <= q'' <= 0`, `L=m ell/(1+m ell d^2)`.

Therefore the **outer** `V` map has curvature

`-L_V <= d^2/dv^2 q(a(v)) <=0`,

`L_V=L*w2/w0`.

The preceding outer evaluator used monotone endpoint cells, whose deterministic width is first order in the outer cell width. Equation (3.3) upgrades the `Q` layer to midpoint tangent/quadratic cells with deterministic `O(h^2)` width. The inner midpoint values `q,q'` can be supplied by NM13-07's already-proved closed Gaussian conditional cells. No empirical two-dimensional quadrature remainder is needed.

### 4.2 `S1` feasibility cage from `Q`

Equation (3.2) becomes

`boxed: S1 <= C_Q (-Q)`,

`C_Q = 2 ell/[m(1+m ell d^2)]`.                              (4.1)

Thus every branch subbox gets an algebraic/`Q`-based upper feasibility test for the score moment. In particular an upper `S1` cage no longer requires a separate nested score-square numerator evaluation if (4.1) is already stronger on that subbox. The same self-bound converts the explicit `Q` tail estimate into a score tail estimate.

This does **not** eliminate the need for a lower `S1` enclosure in the final crossing; see the failed-route note below. It is a pruning and one-sided enclosure mechanism, not a complete stationary-root proof by itself.

## 5. Demonstrated mechanism gain at the `delta=10^-3` waypoint

At the archived waypoint

`w0=0.0321710159451139`,
`w1=0.370106966023378`,
`x=3.54218891058057`,
`m=0.226621581517544`,

with `delta=10^-3`, the checker obtains

`ell = 0.7164129802019763`,

`d^2 = 11.504360529204533`,

`w2/w0 = 18.579519498273399`,

`L = 0.056613228195001718`,

`L_V = 1.0518465771092358`.

A GH240 scan over outer means corresponding to `V in [-6,6]` gives

`q'' in [-0.056561837286757094, 5.6e-17]`,

inside the exact theorem interval `[-L,0]`. The pointwise self-bound utilization reaches about

`0.94586373`,

so the inequality is not merely asymptotic decoration on the relevant right tail.

For the outer averages,

`Q = -0.097295052595172918`,

`S1 = 0.094258682163430474`,

while (4.1) gives

`S1 <= 0.21450436822048513`.

This integrated bound is useful for pruning but is not by itself sharp enough to certify the delicate final sign.

The major numerical gain is the outer `Q` cell order. On the central `V in [-8,8]` range, ordinary monotone endpoint widths (computed numerically using GH midpoint data) versus the exact curvature-only cap are:

- 100 cells: `0.02463686` versus `0.00336591` (factor `7.32`);
- 200 cells: `0.01229169` versus `0.000841477` (factor `14.61`);
- 400 cells: `0.00614250` versus `0.000210369` (factor `29.20`);
- 800 cells: `0.00307083` versus `5.25923e-5` (factor `58.39`);
- 1600 cells: `0.00153536` versus `1.31481e-5` (factor `116.77`).

The monotone widths in that comparison are NUMERICAL_ONLY; the `L_V h^2/8` curvature cap is the proved formula. The scaling difference, first order versus second order, is exact.

This directly attacks the companion's named remaining bottleneck: the outer layer of the nested Gaussian evaluator on the positive-gap branch tube.

## 6. Supported third-full threshold calculation at alpha=12.287222221600

The checker independently solves the complete-third fixed-density stationarity system at

`alpha=12.287222221600`.

The comparison remains positive at every tested Gauss--Hermite order:

- GH160: `Psi3 = 2.1443957720634899e-13`;
- GH200: `Psi3 = 2.5046631435543532e-13`;
- GH240: `Psi3 = 2.5013324744804777e-13`;
- GH280: `Psi3 = 2.5035529205297280e-13`;
- GH320: `Psi3 = 2.5024426975051028e-13`.

The corresponding full-gradient infinity norms are between `1.69e-15` and `1.69e-14`. At GH320 the reconstructed stationary parameters are

`p3=0.59916661554407757`,
`p2=0.96911591246567508`,
`q3=0.22869805152002043`,
`q2=0.63843683126931883`,
`c3=2.8674017463469124`,
`c2=13.103474334644494`,
`gamma_sq=0.076564602119094452`,
`gamma_p=3.2652164718563506`.

An independently coded adaptive two-dimensional evaluation gives

`Q=-0.098053731889718859`,

reported scalar quadrature error `6.499e-14`, and reconstructed

`Psi3=1.8496315590255108e-13>0`.

The adaptive error report is a numerical integrator estimate, **not a directed proof bound**. These computations therefore support the stricter conditional endpoint but do not promote it to the directed tier.

## 7. Failed / insufficient routes preserved

1. **Self-bound alone does not certify the final Schur sign.** At the positive-gap center, (4.1) gives `S1<=0.2145` while the numerical value is about `0.09426`; the integrated utilization is only `0.439`. The final KL-free row is cancellation-sensitive, so direct lower/upper `S1` cells are still required. The new result is a pruning/upper-cage tool and a second-order `Q` compiler, not a magic scalar closure.
2. **Outer semiconcavity does not by itself certify the parameter tube.** The midpoint quantities `q,q'` still need outward inner-cell values uniformly over `(w0,w1,m,x)`, and the nested Schur branch faces still need a genuine inclusion/sign proof.
3. **Further complete-second decimal mining is exhausted.** The companion's `12.31963444619075` endpoint is essentially at the inherited linear transport zero. This run does not count another complete-second decimal as progress.
4. **Direct 4D Krawczyk remains inferior to the nested Schur geometry.** The weak direction is still best isolated in the last scalar crossing.
5. **Modulo-`m` and replica-only shortcuts remain rejected** for the reasons already recorded: the source implication direction/stationarity hypotheses do not permit replacing the missing full stationary certificate by an arbitrary positive trial or an ansatz value.

## 8. Residual obstruction and next attack

The third-full directed proof is still missing the uniform outward nested branch inclusion. The new theorem changes the best next implementation:

1. keep NM13-07's inner semiconcave closed-cell evaluator for `q,q'`;
2. use the present inherited curvature `L=m ell/(1+m ell d^2)` to compile the **outer `Q` layer at second order** rather than monotone first order;
3. use `S1<=C_Q(-Q)` and the self-bound score tail before evaluating separate score-square numerators;
4. retain direct endpoint score cells only where a lower `S1` bound is needed;
5. certify the nested scalar stages `(Rscale,RU,Rratio)` and then the two KL-free `Rhat_H` endpoint signs on `x0+-0.2`;
6. directly enclose reconstructed `alpha<12.31950` on the certified branch tube.

A successful implementation at the existing `delta=10^-3` waypoint would move the review-pending directed endpoint by more than `1.34e-4`, to below `12.31950`; the numerical root remains near `12.31643335693`. Those values remain **CONDITIONAL / NOT PROMOTED** here.

## 9. Durable artifacts

Essential checker:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_outer_smoothing_selfbound_alpha12287222221600.py`

creation commit:

`c6132f06e3b931144c97fb34f05215894eb2efef`.

Actual archived stdout:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_outer_smoothing_selfbound_alpha12287222221600.out`

creation commit:

`67c63bc5bbf4e92344061f8fb4477bd0f0af2386`.

The checker explicitly distinguishes exact bookkeeping/theorem-derived formulas from NUMERICAL_ONLY GH/adaptive support.

## 10. ledger_delta

```yaml
ledger_delta:
  parent: T03_negative_spherical_perceptron
  source_model:
    kappa: -1
    disorder: iid_standard_Gaussian_rows
    radius: exact_sqrtN_sphere
  original_problem:
    review_pending_directed_before: [6.30297437506, 12.31963444619075]
    review_pending_directed_after: [6.30297437506, 12.31963444619075]
    directed_changed: false
    directed_width: 6.01666007113075
    supported_conditional_before: [6.30297437506, 12.287222221605]
    supported_conditional_after: [6.30297437506, 12.287222221600]
    supported_width_after: 5.984247846540
    supported_upper_gain: 5.0e-12
    supported_status: CONDITIONAL_NUMERICAL_ONLY
  mechanism_gain:
    theorem: NM03-T03-OUTER-SMOOTHING-SELFBOUND
    inherited_curvature: "-ell <= U'' <= 0"
    smoothed_curvature: "-m*ell/(1+m*ell*d^2) <= q'' <= 0"
    score_self_bound: "q'^2 <= 2 L (-q); S1 <= 2 ell/[m(1+m ell d^2)] (-Q)"
    outer_cell_order: O(h^2)
    prior_outer_monotone_order: O(h)
    waypoint_L: 0.056613228195001718
    waypoint_LV: 1.0518465771092358
    outer_1600cell_gain_factor_numerical: 116.77475811831283
  named_obstruction:
    worker: NM13-07
    obstruction: uniform_outward_nested_Gaussian_evaluator_over_positive_gap_Schur_branch_tube
    application: second_order_outer_Q_cells_plus_Q_based_S1_upper_and_score_tail
  conditional_third_full:
    alpha: 12.287222221600
    GH160_Psi3: 2.1443957720634899e-13
    GH320_Psi3: 2.5024426975051028e-13
    adaptive_Psi3: 1.8496315590255108e-13
    status: SUPPORTED_CONDITIONAL_NOT_DIRECTED
  artifacts:
    code: proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_outer_smoothing_selfbound_alpha12287222221600.py
    code_commit: c6132f06e3b931144c97fb34f05215894eb2efef
    output: proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_outer_smoothing_selfbound_alpha12287222221600.out
    output_commit: 67c63bc5bbf4e92344061f8fb4477bd0f0af2386
  failed_routes_preserved:
    - selfbound_too_loose_to_settle_final_Rhat_sign_alone
    - outer_semiconcavity_does_not_replace_uniform_parameter_tube_inclusion
    - complete_second_decimal_mining_exhausted
    - direct_4d_krawczyk_wrapping
    - modulo_m_wrong_implication_direction
  next_attack: outward_inner_midpoints_plus_second_order_outer_Q_cells_plus_nested_Schur_faces_then_alpha_lt_12_31950
  historical_or_peer_overwrite: false
  public_posting: false
  email_or_drive: false
  paid_compute: false
  schedule_or_access_change: false
```

No historical or peer file was overwritten. No email, Drive, public posting, paid compute, permission, workflow, or schedule change was performed.