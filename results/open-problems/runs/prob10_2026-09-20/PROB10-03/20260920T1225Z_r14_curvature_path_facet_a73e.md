Runtime model: **GPT-5.6 Sol**. Requested GPT-6/maximum is not an authenticated configurable native setting here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 — R14 bounded substantive iteration: curvature variability, positive KL paths, and a facet-dual obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status: **OPEN / PARTIAL / SOURCE BRACKET UNCHANGED / NEW EXACT CERTIFICATION LEMMAS AND ONE EXACT DUAL OBSTRUCTION**.

## 1. Contract, continuity, ownership, and consumed state

The run first consumed the controlling `operations/PROB10_2026-09-20.md`, root `POSTED.md`, current claims, the actual intervening R14 successor handoff, the newest own PROB10-03 report, and the newest relevant complementary perceptron reports available on `master`.

Preserved continuity:

- `operations/PROB10_2026-09-20.md`, blob recorded by the preceding immutable chain as `6f0fcee836d93371d43b84af1a55150fedc80779`;
- root `POSTED.md`, whose current 20 September owner-supplied update explicitly says zero-margin/restricted perceptron work does not close negative-margin counterparts; the preceding immutable chain records blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- historical R14 negative-margin claim/handoff `operations/claims/I0089.md`, blob `0df4adc0fd8ee99edeb4890de3d5e9e076a1edd0`; it is not reset or overwritten;
- current Campbell--O'Rourke Q1.8 claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`; it still records R14 and remains untouched;
- immutable actual-successor handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, blob `edaa787e384c28a4b5a658dbba80f664cde75882`, preserving owner navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2` and Campbell metric `S=5`;
- newest preceding own report `runs/prob10_2026-09-20/PROB10-03/20260920T1052Z_r14_curvature_deficit_stationary_filter_6f2a.md`, blob `fc5d28ecf5fbdf77bf3df6a8c471b1cac6e2f219`;
- newest materially relevant complementary source movement: `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-matched-gaussian-recenter-alpha1231963446.md`, observed on current-master history, which moves the review-pending directed complete-second exact-sphere endpoint to `12.31963446`;
- newest complementary third-full theory: NM13-03 `2026-09-20__t03-variance-deficit-cage-alpha122872222217.md`, plus the NM13-07 third-full score/overlap reduction.

Concurrent repository activity was present during the run. All writes below are create-only. One create attempt encountered a real GitHub `409` head race; it was retried after refreshing `master`, with no force push and no overwrite.

No scheduler, cadence, enabled state, workflow, permission, canonical claim, peer report, email, Drive object, or public posting was changed.

## 2. Exact source target, probability convention, and source status

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly,

and require

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

A lower endpoint means SAT probability tends to one as `N->infinity` at fixed `alpha`; an upper endpoint means SAT probability tends to zero. Smaller-radius constructions, Ising restrictions, finite-lift floating-point stationary points, restricted ansatzes, and algorithmic thresholds are not source endpoints.

Fresh source reading remains consistent with OPEN/PARTIAL status:

1. El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`, formulate the exact radius-`sqrt(N)` Gaussian spherical model. For negative margin their algorithm uses the conjectured FRSB/Parisi structure and outputs on radius `sqrt(qbar N)` with `qbar<1`; this is not the exact-radius capacity theorem.
2. Stojnic, `https://arxiv.org/abs/1306.3980`, gives rigorous negative-margin random-duality mechanisms and capacity bounds, not the requested exact numerical `kappa=-1` threshold.
3. Stojnic, `https://arxiv.org/abs/2312.16531`, states that fl-RDT characterizes the negative spherical capacity, but also states that making it practically operational requires substantial numerical work; the displayed finite-level values are therefore kept distinct from a directed, source-matched numerical proof layer.
4. Montanari--Zhong--Zhou, `https://arxiv.org/abs/2110.15824`, prove rigorous interpolation bounds and characterize an LP threshold, not the exact unrestricted `kappa=-1` SAT threshold.
5. Annesi--Malatesta--Zamponi, `https://arxiv.org/abs/2410.06717`, compute the transition under a full-RSB ansatz; this is structural guidance rather than the missing rigorous exact-radius endpoint.
6. Huang--Sellke--Sun, `https://arxiv.org/abs/2608.29416`, submitted 29 August 2026, exactly characterize a dimension-free Lipschitz algorithmic projection-pursuit class and explicitly distinguish the non-algorithmic feasible-projection problem as a major outstanding challenge.

This is a bounded dated source-status check, not a worldwide novelty certificate.

## 3. Entering source metric

After consuming the newer NM13-07 recentered certificate, the entering repository-supported/review-pending bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963446`,

`W = 6.01666008494`.

The complete-third numerical capacity zero near `12.28722222159` remains conditional/numerical because there is still no outward four-overlap root certificate.

## 4. Attack A — a curvature-variability upper information cage

The preceding R14 run proved a sharpness obstruction for generic lower bounds using only mean, score variance and a uniform curvature cap. The new route keeps the **distribution of the curvature** and gives a complementary upper cage whose non-Gaussian correction vanishes at the quadratic equality case.

### Theorem R14-T03-CURVATURE-VARIABILITY

Let `gamma=N(0,1)` and

`d nu/d gamma = exp(phi)/Z`,

where `phi` is `C^2`, concave, and has enough integrability/decay to justify the integrations by parts below. Put

`r=phi'`, `tau=-phi''>=0`,

`mu=E_nu X`, `v=Var_nu(X)>0`, `a=E_nu tau`,

and let `G=N(mu,v)`. Define

`eta_tau = (1/(1+a)) E_nu[(tau-a)^2/(1+tau)]`.

Then

`boxed: 1 <= v(1+a) <= 1+eta_tau`,                            (4.1)

and

`boxed: D(nu||gamma)`

` <= D(G||gamma) + (1/2)log(1+eta_tau)`,                     (4.2)

where

`D(G||gamma)=(mu^2+v-1-log v)/2`.

#### Proof

The Lebesgue density is proportional to `exp(phi(x)-x^2/2)`. If `ell` is its log density, then

`ell''=-(1+tau)`.

Hence the ordinary Fisher information is

`J(nu)=E[(ell')^2]=-E ell''=1+a`.                            (4.3)

The Cramer--Rao inequality gives

`v(1+a)=vJ(nu)>=1`.                                         (4.4)

Brascamp--Lieb for the potential `x^2/2-phi(x)`, whose second derivative is `1+tau`, gives

`v <= E[1/(1+tau)]`.                                        (4.5)

The exact algebraic identity is

`(tau-a)^2/(1+tau)`

` = (tau-a) - (1+a)(tau-a)/(1+tau)`.

Taking expectations and using `E(tau-a)=0` gives

`E[(tau-a)^2/(1+tau)]`

` = (1+a)[(1+a)E(1/(1+tau))-1]`.                            (4.6)

Therefore (4.5)--(4.6) imply the upper side of (4.1).

Because `G` matches the first two moments of `nu`,

`D(nu||gamma)=D(G||gamma)+D(nu||G)`.                        (4.7)

Stam's entropy--Fisher inequality gives

`D(nu||G)=h(G)-h(nu) <= (1/2)log(vJ(nu))`.                  (4.8)

Combining (4.1), (4.3), and (4.8) proves (4.2). QED.

This theorem is exact. It is not asserted as a new literature theorem; its value here is the complete-third perceptron compilation below.

### Exact inner hinge specialization

For

`d rho_x/d gamma_H proportional exp[-B(x+sH)_+^2]`,

put

`A=2Bs^2`, `pi_x=P_{rho_x}(x+sH>0)`.

Then, a.e.,

`tau(H)=A 1_{x+sH>0}`,

so direct two-point algebra yields

`boxed: eta_tau=A^2 pi_x(1-pi_x)/(1+A)`.                    (4.9)

The exact Gaussian identities are

`mu=s u_x(x)`, `v=1+s^2u_xx(x)`.

Consequently

`KL(rho_x||gamma_H)`

` <= (1/2){s^2u_x^2+s^2u_xx-log(1+s^2u_xx)}`

`    +(1/2)log(1+A^2 pi_x(1-pi_x)/(1+A))`.                 (4.10)

Unlike a uniform-curvature correction, the last term tends to zero in both outer tails, where `pi_x` tends to `0` or `1`.

### Exact outer tilted-U specialization

For fixed `V=v`, let

`X=dU+sqrt(p3)v-1`,

`d nu_v/d gamma_U proportional exp[m u(X)]`.

Then

`tau_v(U)=m d^2[-u_xx(X)]`.

Theorem (4.2) therefore yields an outer KL upper cage using only

`a_v=<tau_v>_v`,

`eta_v=(1/(1+a_v))< (tau_v-a_v)^2/(1+tau_v) >_v`,

plus the matching mean/variance. This is a complementary interval cage; I do **not** claim it is pointwise tighter than the existing matched-Gaussian Fisher upper cage.

### Negation/falsification check for Attack A

The quadratic case has constant `tau`, hence `eta_tau=0`, and the matching Gaussian is exact. Thus the new correction correctly vanishes at the previous sharpness obstruction rather than pretending to improve it.

The numerical-only hinge tests at `x=-1,0,1` all satisfy

`D(G||gamma) <= D(rho_x||gamma) <=` the new curvature-variability upper bound.

These are sanity checks only; the theorem is proved analytically above.

## 5. Attack B — exact positive thermodynamic-path representation of the c-sector KL

This attack targets the step still lost in the third-full interval proof: cancellation in nested KL/log-partition evaluation.

### Theorem R14-T03-POSITIVE-KL-PATH

Let `mu_0` be a probability measure and `Y` have finite exponential moments for `0<=t<=T`. Define

`F(t)=log E_{mu_0} exp(tY)`,

`d mu_t/d mu_0=exp(tY-F(t))`.

Then

`D(mu_t||mu_0)=tF'(t)-F(t)`,

hence

`d/dt D(mu_t||mu_0)=tF''(t)=t Var_{mu_t}(Y)`.               (5.1)

Since `D(mu_0||mu_0)=0`,

`boxed: D(mu_T||mu_0)=int_0^T t Var_{mu_t}(Y) dt`.          (5.2)

For a partition `0=t_0<...<t_n=T`, if

`L_i <= Var_{mu_t}(Y) <= U_i` throughout `[t_i,t_{i+1}]`,

then

`sum_i (t_{i+1}^2-t_i^2)L_i/2`

` <= D(mu_T||mu_0)`

` <= sum_i (t_{i+1}^2-t_i^2)U_i/2`.                        (5.3)

#### Proof

Differentiate the log partition: `F'=E_tY`, `F''=Var_t(Y)`. The KL identity follows directly from the Radon--Nikodym derivative. Differentiation gives (5.1), integration gives (5.2), and multiplying interval variance enclosures by the nonnegative weight `t` and integrating gives (5.3). QED.

### Exact third-full compilation

For the outer c-sector at fixed `V=v`, take

`Y=u(X)`, `T=m`, `mu_0=gamma_U`.

Then the conditional outer entropy is

`boxed: D_U(v)=int_0^m t Var_{nu_{v,t}}(u(X)) dt`.           (5.4)

Averaging in `V` yields the full outer c-sector KL term.

For the inner hinge at fixed `x`, take

`Y=-(x+sH)_+^2`, `T=B`, `mu_0=gamma_H`.

Then

`boxed: KL(rho_x||gamma_H)`

` = int_0^B b Var_{rho_{x,b}}((x+sH)_+^2) db`.              (5.5)

Every integrand is nonnegative. Therefore a future directed proof can replace cancellation-prone expressions such as energy-minus-log-partition by cellwise variance bounds. The H expectation remains analytically closed at each path parameter; only a one-dimensional positive path integral is added.

For interval transport between path mesh points,

`d/dt Var_{mu_t}(Y)=E_t[(Y-E_tY)^3]`.                       (5.6)

Thus existing fourth-moment/tail envelopes can bound the variance slope rigorously.

### Negation test: the tempting monotonicity shortcut is false

Let `H` be Bernoulli(`p`) with `p=3/4` and tilt by `exp(-bH)`. At `b=0`,

`kappa_3(H)=p(1-p)(1-2p)=-3/32`,

so

`d/db Var_b(H)|_{0}=+3/32>0`.                               (5.7)

Thus variance under a negative-energy tilt need not decrease. The path proof must use true interval enclosures on each path cell; a monotonicity assumption would be invalid.

The numerical-only outer-U check at the archived third-full parameter set and `V=0` gives

`direct KL = 0.0041249618466979478`,

`positive-path integral = 0.004124961846697783`,

absolute difference `1.648e-16`.

This is only a falsification check of the implementation; (5.2) is already exact.

## 6. Attack C — exact Gaussian-polytope facet first moment and an obstruction to the naive dual route

This is materially different from the entropy/stationarity route.

Set

`K_N=conv(-g_1,...,-g_M)`.

Writing `sigma=sqrt(N)u`, the constraints are equivalent to

`h_{K_N}(u)<=1`, `||u||=1`.

For fixed `alpha>2`, Wendel's theorem gives `0 in int(K_N)` with probability tending to one. On that event the centered inradius is

`r(K_N)=min_{||u||=1}h_{K_N}(u)`,

so

`SAT <=> r(K_N)<=1`, `UNSAT <=> r(K_N)>1`.                  (6.1)

Gaussian general position makes every facet simplicial with `N` vertices.

Fix an N-subset and let `G` be the square matrix with these vertices as rows. The affine hyperplane through them has distance

`R^2=1/[1^T(GG^T)^(-1)1]`.                                  (6.2)

For square standard Gaussian `G`, the Schur-complement/inverse-Wishart identity gives

`boxed: N R^2 ~ chi-square_1`.                              (6.3)

Hence

`f_R(r)=sqrt(2N/pi) exp(-Nr^2/2)`, `r>=0`.

Orient the selected hyperplane so that the origin is on its interior side. Conditional on that hyperplane, each remaining independent Gaussian vertex lies on that side with probability `Phi(r)`. Therefore the expected number `Z_{<=1}` of facets at support distance at most one is exactly

`E Z_{<=1}`

` = C(M,N) sqrt(2N/pi) int_0^1 exp(-Nr^2/2) Phi(r)^(M-N) dr`. (6.4)

For `M/N->alpha`, its Laplace exponent is

`F_alpha(r)=alpha log alpha-(alpha-1)log(alpha-1)`

`            -r^2/2+(alpha-1)log Phi(r)`.                   (6.5)

For `alpha>=6`,

`F_alpha'(r)=-r+(alpha-1)phi(r)/Phi(r)>0` on `[0,1]`: indeed `phi(r)>=phi(1)` and `Phi(r)<=1`, while `5 phi(1)>1`. Thus the one-facet first moment is governed by `r=1`.

The current endpoint lies in `(12,13)`. The Markov criterion is rigorously on the wrong side there. One elementary bound is enough:

- concavity of the Gaussian density on `[0,1]` plus crude `phi(0)>0.39`, `phi(1)>0.234` gives `Phi(1)>0.81`;
- `log(0.81)>-0.22` because `e^0.22>1+0.22+0.22^2/2>100/81`;
- `log(alpha)>2.3` for `alpha>12` (for example `e<2.72` and `e^0.3<1/(1-0.3)` give `e^2.3<12`);
- `(alpha-1)log(alpha/(alpha-1))>1-1/alpha>11/12`;
- `alpha-1<12`.

Therefore at `alpha=12.31963446`,

`F_alpha(1)`

` > 23/10 + 11/12 - 1/2 - 12*(22/100)`

` = 23/300 > 0`.                                            (6.6)

So **the naive one-facet Markov/union-bound dual cannot certify UNSAT at the current source endpoint**. A successful polar route must use correlated many-facet structure, a covering argument, or a higher-order dual certificate.

The numerical-only zero of `F_alpha(1)` is

`alpha ~= 21.523774715989354`,

which quantifies how far this simple route is from the current `12.31963446` frontier. It is not a source endpoint.

## 7. Executed checks and artifacts

The mathematical idea was persisted before code:

- preliminary idea/proof artifact `artifacts/prob10_2026-09-20/PROB10-03/20260920T1210Z_r14_curvature_path_facet_idea_a73e.md`, creation commit `777403814e9bcfac5eee4f6029c92a9294e9a838`;
- its theorem was correct, but one explanatory pointwise decomposition in that preliminary note was algebraically misstated; preserving immutability, a create-only correction was added at `artifacts/prob10_2026-09-20/PROB10-03/20260920T1218Z_r14_curvature_path_facet_correction_a73e.md`, creation commit `2ebbb0d84ff40ecf00e11789e6e93c9a47ffb9ea`. The final proof in Section 4 above is the corrected proof.

Only after the idea artifact, the checker was added:

- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1212Z_r14_curvature_path_facet_checker_a73e.py`, creation commit `a20f7b2bbcded4b6b9557562fd2ca524aa129e1e`;
- executed output `artifacts/prob10_2026-09-20/PROB10-03/20260920T1212Z_r14_curvature_path_facet_checker_a73e.out`, creation commit `641424994c09261323c1b85be9b90ad94e2879dd`.

The output records

`EXACT_FISHER_REWRITE_PASS`,

`EXACT_BERNOULLI_CURVATURE_VARIABILITY_PASS`,

`EXACT_THERMODYNAMIC_DERIVATIVE_PASS`,

`EXACT_VARIANCE_MONOTONICITY_NEGATION_PASS 3/32`,

and ends

`ALL_EXACT_SELF_CHECKS_PASS`

`NUMERICAL_SCOUT_COMPLETE`.

The numerical hinge cages, positive-path comparison, and facet root are explicitly labeled `NUMERICAL_ONLY`. These are self-checks, not independent audits.

## 8. Before/after source metric and auxiliary movement

### Source metric

Before:

`[6.30297437506, 12.31963446]`, width `6.01666008494`.

After:

`[6.30297437506, 12.31963446]`, width `6.01666008494`.

**Source-level movement: none.**

No `12.287...`, path quadrature, hinge test, or facet first-moment number is promoted to an endpoint.

### Auxiliary/mechanism movement

1. Proved the curvature-variability matched-Gaussian upper cage (4.1)--(4.2), with a fully explicit Bernoulli-curvature correction (4.9) for the hinge kernel.
2. Proved the exact positive thermodynamic representation (5.2), compiling both complete-third c-sector KL terms into nonnegative variance integrals suitable for outward interval subdivision.
3. Falsified the tempting variance-monotonicity shortcut exactly by the Bernoulli `p=3/4` example.
4. Derived the exact Gaussian-polytope one-facet count (6.4) and proved that its first-moment Markov criterion is already exponentially on the wrong side at the current `12.31963446` endpoint; this retires that naive dual attack unless it is upgraded to correlated/many-facet structure.

## 9. Remaining full-scope gap and next source-moving obligation

The exact `kappa=-1` capacity problem remains **OPEN / PARTIAL** under the repository closure standard.

The strongest source-moving route is still the complete-third four-overlap inclusion near the strict positive-gap branch. This run changes the recommended numerical proof architecture:

1. keep the exact algebraic q-sector/projective reconstruction and score-overlap residuals already proved in the repository;
2. use the existing lower entropy cages and the new curvature-variability **upper** cage as cheap box rejection/enclosure tests;
3. for surviving boxes, evaluate `D_U,D_H` through the positive path formulas (5.4)--(5.5), subdividing the path parameter and enclosing the variance with third/fourth-moment bounds rather than subtracting nested log partitions;
4. combine those outward c-sector intervals with a weighted Krawczyk/contraction inclusion for the four overlap residuals;
5. only after a genuine outward stationary/root certificate, verify every source-matched fl-RDT comparison hypothesis and obtain the required independent validation before moving the source endpoint.

A smaller-radius algorithm, an FRSB/replica ansatz, a floating-point finite-lift root, or the numerical `21.52` facet diagnostic is not closure.

## 10. Structured ledger delta

```yaml
ledger_delta:
  task: PROB10-03
  worker_route: R14 owner-refocused complementary route
  status: OPEN/PARTIAL
  model_runtime: GPT-5.6 Sol
  reasoning_effort: UNVERIFIED
  source_metric_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963446"
    width: "6.01666008494"
  source_metric_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963446"
    width: "6.01666008494"
  source_movement: none
  exact_auxiliary_results:
    - "curvature-variability matched-Gaussian upper KL cage"
    - "inner hinge eta=A^2*pi*(1-pi)/(1+A) specialization"
    - "positive thermodynamic KL path D=int t Var_t dt"
    - "exact Bernoulli p=3/4 counterexample to variance monotonicity shortcut"
    - "Gaussian-polytope one-facet first-moment formula and current-endpoint obstruction"
  numerical_only:
    third_full_capacity_scout: "~12.28722222159 inherited, not promoted"
    facet_first_moment_zero: "~21.523774715989354"
  campbell_handoff_preserved:
    path: "artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md"
    navigation: "3846db33296cfb6eea59ff7c488929087c7b62a2"
    metric: "S=5 preserved"
  scheduler_changed: false
  email_or_drive: false
  public_posting: false
  force_push: false
```
