Runtime model: **GPT-5.6 Sol**. Requested GPT-6/maximum is not an authenticated configurable native setting here; reasoning-effort telemetry is **UNVERIFIED**.

# PROB10-03 — R14 bounded substantive iteration: parameter-face calculus, overlap obstruction, and nonconvex dual

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status: **OPEN / PARTIAL / SOURCE BRACKET UNCHANGED BY R14 THIS RUN / NEW EXACT PARAMETER-FACE COMPILER**.

## 1. Contract, continuity, current ownership, and consumed updates

This run first consumed the controlling `operations/PROB10_2026-09-20.md`, root `POSTED.md`, the current R14 history, the immutable Campbell--O'Rourke Q1.8 handoff, the newest own PROB10-03 report, and the newest materially relevant companion reports visible on current `master`.

Continuity preserved:

- controlling contract: `operations/PROB10_2026-09-20.md`;
- exclusion registry: root `POSTED.md`; the owner's posted zero-margin/Ising perceptron work is distinct and does not close this target;
- immutable intervening-successor handoff: `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, blob `edaa787e384c28a4b5a658dbba80f664cde75882`, preserving Campbell--O'Rourke Q1.8, metric `S=5`, and navigation commit `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding own report: `runs/prob10_2026-09-20/PROB10-03/20260920T1310Z_r14_dimensionless_positivepath_capnet_d31f.md`, blob `81cc1fd4adc0d5ce72e1601385cf575317ea8842`;
- newest companion source move: `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-posgap-dimensionless-allmoment-alpha12319634446195.md` and its exact output `artifacts/t03_posgap_dimensionless_allmoment.out`.

The fresh pre-report branch state observed during this run was `b41f5d0cd8452beb8dde62b00ff4f1c7d99a73f7`; concurrent workers were active, so all writes here are create-only and no shared claim/index is overwritten.

### Concurrent-collision handling

The idea note for this run was written before code, as required. Its first attack derived monotonicity of the three score/energy outer integrands. Before claiming that result as new, I re-read current `master` and found that the intervening NM13-07 report had independently already proved the stronger **all-five-moment outer monotonicity theorem** and a positive-gap four-overlap compiler. I therefore do **not** count that overlapping theorem as R14 progress or overwrite the companion's ownership. The present run pivots to the complementary parameter-face sensitivity calculus below, which is not the same theorem.

No scheduler, cadence, enabled state, workflow, permission, canonical claim, email, Drive object, or public posting was changed. No force push was used.

## 2. Exact source target, probability convention, and bounded source-status refresh

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)`,

and require

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

A rigorous lower endpoint means the SAT probability tends to one as `N->infinity` at each fixed `alpha` below that endpoint. A rigorous upper endpoint means the SAT probability tends to zero at each fixed `alpha` above that endpoint. Boundary equality is not silently assigned a convention. A smaller-radius construction, a ball relaxation, an Ising restriction, a finite-lift floating root, or an ansatz value is not a source endpoint.

The primary-source scope remains consistent with **OPEN / PARTIAL**:

1. El Alaoui--Sellke, `https://arxiv.org/abs/2010.15811`, work in the exact radius-`sqrt(N)` spherical model, but for negative margin their algorithm uses the conjectural FRSB/Parisi structure and outputs radius `sqrt(qbar N)` with `qbar<1`; this is not the full-radius capacity theorem.
2. Stojnic, `https://arxiv.org/abs/1306.3980`, gives rigorous random-duality bounds/mechanisms for the negative spherical perceptron, not an already certified exact `kappa=-1` equality.
3. Stojnic, `https://arxiv.org/abs/2312.16531`, fits the problem into fully lifted RDT and states a capacity characterization, while explicitly noting that substantial numerical work is needed to make it practically operational. The repository therefore keeps the comparison theorem separate from a floating finite-level stationary computation and requires directed inclusion before promotion.
4. The current follow-ups retained by the companion tracks (full-RSB/jammed-Parisi calculations and the 29 August 2026 algorithmic projection-pursuit characterization) do not replace unrestricted exact-radius source closure.

This is a dated bounded status check, not a worldwide priority certificate.

## 3. Entering source metric

A concurrent NM13-07 update, consumed rather than credited here, moved the review-pending complete-second upper endpoint by `5e-12`:

`alpha_L = 6.30297437506`,

`alpha_U = 12.319634446195`,

`W = 6.016660071135`.

The complete-third values near `12.3164` at prescribed positive objective gap and near `12.28722` at the numerical capacity zero remain **conditional / numerical until an outward four-dimensional root inclusion and the full source-matched comparison hypotheses are certified**.

## 4. Attack A — exact parameter-face covariance calculus for the dimensionless third-full compiler

This is the main new mathematical contribution of this run.

Use the dimensionless inner kernel

`F_lambda(t)=E_H exp[-lambda (t+H)_+^2/2]`,

`u_lambda(t)=log F_lambda(t)`, with `lambda>0`.

For fixed outer mean `a`, variance `d^2>0`, and `m in (0,1)`, define

`nu(dt)=Z^{-1} exp[m u_lambda(t)] phi_d(t-a) dt`.              (4.1)

For the projective complete-third chart,

`d^2=w1/w0`,

`a(v)=sqrt(w2/w0) v-1/sqrt(w0)`,

and at capacity `lambda=x-1`; at prescribed positive gap the same formulas hold with the effective dimensionless hinge stiffness used by the companion positive-gap compiler.

Let `Y=t+H` under the inner tilted law

`rho_t(dH) proportional exp[-lambda (t+H)_+^2/2] d gamma(H)`,

and put

`h(t)=E_{rho_t} Y_+^2`,

`K(t)=KL(rho_t || gamma_H)`.

Define outer quantities

`g=E_nu u_t`,

`A1=g^2`, `A2=E_nu u_t^2`, `AH=E_nu h`,

`D_U=KL(nu || N(a,d^2))=m E_nu u-log Z`,

`D_H=m E_nu K`.

### Theorem R14-T03-PARAMETER-FACE-CALCULUS

For any integrable `G=G(t;a,m,lambda,s)` under (4.1), where `s=d^2`,

`partial_a E_nu G = E_nu G_a + Cov_nu(G,T)/s`,               (4.2)

`partial_m E_nu G = E_nu G_m + Cov_nu(G,u)`,                 (4.3)

`partial_lambda E_nu G = E_nu G_lambda + m Cov_nu(G,u_lambda)`, (4.4)

`partial_s E_nu G = E_nu G_s + Cov_nu(G,(T-a)^2)/(2s^2)`.   (4.5)

The inner derivatives satisfy

`u_lambda = -h/2`,                                           (4.6)

`h_lambda = -(1/2) Var_{rho_t}(Y_+^2) <= 0`,                (4.7)

`h_t >= 0`, `u_t <= 0`, `u_tt <= 0`.                         (4.8)

Consequently, at fixed `s`:

`partial_a A1 >= 0`, `partial_m A1 <= 0`,                    (4.9)

`partial_a A2 >= 0`, `partial_m A2 <= 0`,                    (4.10)

`partial_a AH >= 0`, `partial_m AH <= 0`, `partial_lambda AH <= 0`, (4.11)

`partial_a D_U >= 0`, `partial_m D_U >= 0`, `partial_lambda D_U >= 0`, (4.12)

and

`partial_a D_H >= 0`.                                       (4.13)

Moreover the strongest new signed identity is

`boxed: partial_lambda AH`
` = -(1/2) E_nu Var_{rho_T}(Y_+^2) -(m/2) Var_nu(h(T)) <= 0`. (4.14)

The `m`-derivative of `D_H` has the exact form

`partial_m D_H=E_nu K+m Cov_nu(K,u)`                         (4.15)

and has **no universal sign**; a numerical falsification below finds stable strict examples of both signs. Thus a future interval compiler may use corner monotonicity for (4.9)--(4.13), but must not invent an `m`-corner rule for `D_H`.

### Proof

For (4.2)--(4.5), differentiate the normalized density (4.1). The derivative of a normalized expectation is the expectation of the explicit derivative plus covariance with the derivative of the unnormalized log density. The four log-density derivatives are, modulo constants killed by covariance,

`(T-a)/s`, `u`, `m u_lambda`, `(T-a)^2/(2s^2)`,

which proves (4.2)--(4.5).

Differentiating the inner log partition in `lambda` gives (4.6). Differentiating `h=E_{rho_t}Y_+^2` in `lambda` gives (4.7). The function `exp[-lambda y_+^2/2]` is decreasing and log-concave; Gaussian convolution preserves log-concavity, so `u_t<=0` and `u_tt<=0`. Rewriting the inner law in the `y=t+H` coordinate gives

`rho_t(dy) proportional exp[t y] exp[-y^2/2-lambda y_+^2/2] dy`.

It is therefore a monotone-likelihood-ratio family in `t`, and the increasing statistic `y_+^2` has nondecreasing expectation, proving `h_t>=0`.

For `A1`, `g=E u_t<=0`. From (4.2),

`g_a=Cov(u_t,T)/s<=0`

because `u_t` is nonincreasing, while from (4.3),

`g_m=Cov(u_t,u)>=0`

because `u_t` and `u` are both nonincreasing. Hence `2g g_a>=0` and `2g g_m<=0`, proving (4.9).

Since `u_t<=0` and is nonincreasing, `u_t^2` is nondecreasing. Equations (4.2)--(4.3) therefore give

`partial_a A2=Cov(u_t^2,T)/s>=0`,

`partial_m A2=Cov(u_t^2,u)<=0`,

proving (4.10).

Because `h` is nondecreasing and `u` is nonincreasing,

`partial_a AH=Cov(h,T)/s>=0`,

`partial_m AH=Cov(h,u)<=0`.

Using (4.4), (4.6), and (4.7),

`partial_lambda AH=E h_lambda+m Cov(h,-h/2)`

`=-(1/2)E Var_{rho_T}(Y_+^2)-(m/2)Var(h)`,

which proves (4.11) and (4.14).

For `D_U=m E u-log Z`, direct differentiation in `m` gives

`partial_m D_U=m Var(u)>=0`.                                  (4.16)

For `lambda`, (4.4) and `partial_lambda log Z=m E u_lambda` give

`partial_lambda D_U=m^2 Cov(u,u_lambda)`.

Now `u` is nonincreasing and `u_lambda=-h/2` is also nonincreasing, hence this covariance is nonnegative. For `a`, integration by parts under (4.1) gives

`Cov(u,T)/s=E u_t+m Cov(u,u_t)`

and `partial_a log Z=m E u_t`; therefore

`partial_a D_U=m^2 Cov(u,u_t)>=0`,                            (4.17)

because both `u` and `u_t` are nonincreasing. This proves (4.12).

Finally

`K(t)=-(lambda/2)h(t)-u(t)`.

A direct exponential-family differentiation gives

`K_t=(lambda^2/2) Cov_{rho_t}(Y_+^2,Y_+) >=0`.                (4.18)

Thus (4.2) gives

`partial_a D_H=(m/s)Cov(K,T)>=0`,

proving (4.13). Equation (4.15) follows directly from (4.3). No sign is asserted for (4.15). QED.

### Why this matters for the lost uniform-control step

The complete-third directed inclusion must control `S1,S2,H1,D_U,D_H` over a parameter box, not merely at its center. The companion all-moment theorem removed the **outer `V` derivative** problem at each fixed parameter tuple. The theorem above removes additional parameter-face dependence:

- `A1,A2` have rigorous `a` and `m` corner directions;
- `AH` has rigorous `a,m,lambda` corner directions;
- `D_U` has rigorous `a,m,lambda` corner directions;
- only `D_H` lacks a universal `m` rule, and (4.15) identifies exactly what must be enclosed there;
- (4.5) gives an exact variance-coordinate derivative for the remaining `d^2` face rather than requiring differentiation of nested quadrature code.

This does not yet produce the Krawczyk inclusion, but it materially narrows the uniform enclosure that remains.

## 5. Attack B — exact negation of the unweighted overlap second moment

This is a materially different SAT-side overlap attack.

Let `Z_N` be the normalized spherical surface measure of feasible unit directions `u` satisfying `g_a dot u >= -1` for all `a`. For a fixed direction,

`E Z_N=Phi(1)^M`.

For two directions with overlap `rho`, let

`p(rho)=P(X>=-1,Y>=-1)`

for a centered bivariate normal pair of correlation `rho`. The exponential rate entering the unweighted second-moment ratio is

`F_alpha(rho)=(1/2)log(1-rho^2)+alpha log[p(rho)/Phi(1)^2]`. (5.1)

At `rho=0`, `F_alpha(0)=0`. Plackett differentiation of the bivariate Gaussian probability gives

`p'(0)=phi(1)^2`.

Therefore

`boxed: F_alpha'(0)=alpha phi(1)^2/Phi(1)^2 >0`               (5.2)

for every `alpha>0`. Hence for every positive density there is a sufficiently small positive overlap with `F_alpha(rho)>0`.

### Consequence

The **unweighted** spherical second-moment route is exponentially unstable immediately away from zero overlap and cannot certify the desired SAT lower endpoint. This is an exact obstruction, not a finite simulation. It also explains why a useful lower-bound attack must compensate the linear overlap drift by conditioning/weighting or a genuinely different planted measure. The previous R14 analysis already found that the particular existing one-body weighted second-moment formula checked there cannot beat the current lower endpoint `6.30297437506`; this run therefore does not recycle it as a source move.

## 6. Attack C — dual inradius minmax and the convexification obstruction

The exact geometric dual remains useful. With `K=conv(0,-g_1,...,-g_M)`, exact-sphere UNSAT is equivalent to `K` containing the Euclidean unit ball. Equivalently define

`R_N=min_{||u||_2=1} max_{a<=M} (-g_a dot u)`;               (6.1)

then the radius-one covering/inradius question is controlled by whether `R_N` lies above or below `1` (with boundary events treated separately rather than silently assigned).

This suggests a Gaussian minmax/CGMT route. The direct convexification, however, is invalid for the source problem: replacing the sphere in (6.1) by the unit ball admits `u=0`, for which the inner maximum is `0`. The radius-one information is destroyed before any comparison theorem is applied. The same issue appears in primal form: replacing `||sigma||=sqrt(N)` by `||sigma||<=sqrt(N)` makes `sigma=0` feasible for every realization because `0>=-sqrt(N)`.

Thus a viable minmax dual attack must retain norm equality by a proved penalty/Lagrange mechanism and prove that the optimizer stays on the boundary. A standard ball relaxation or radius-blind origin-in-hull statement cannot become a source endpoint. I did not find such a boundary-preserving comparison in this bounded iteration, so no dual number is promoted.

## 7. Comparison of the three attacks

1. **Parameter-face fully lifted calculus (Attack A): strongest current route.** It directly addresses the remaining uniform-control step for the four-dimensional complete-third inclusion, with exact signed faces and one explicit nonsigned obstruction.
2. **Unweighted overlap second moment (Attack B): now rigorously exhausted.** Equation (5.2) proves an immediate positive-overlap instability for every `alpha>0`; a future SAT-side improvement must use a different weighted/conditioned measure, not the raw overlap functional.
3. **Dual inradius Gaussian minmax (Attack C): structurally promising but still open.** Its exact obstacle is preservation of the sphere boundary. Convexifying to the ball trivializes the radius information. A nonconvex or exact-penalty comparison is required.

This comparison changes method within the same PROB10-03 problem and does not rotate to an unrelated target.

## 8. Idea-before-code, executed tests, and collision-safe artifacts

The mathematical idea was persisted before code:

- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1358Z_r14_monotone_score_energy_idea_4c2a.md`, creation commit `d6268ff53ca8408ac3ff65368eccd25ec4358b09`.

After discovering the concurrent NM13-07 all-moment theorem, that overlapping portion was not claimed as new. Its checker/output remain an honest record of the attempted route:

- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1406Z_r14_monotone_score_energy_checker_4c2a.py`, commit `651100ee073c2d092432c6f7f63587dbb1f6a251`;
- matching `.out`, commit `57b09ca23687343ad72428f1640759c69cb8d1ef`, ending `ALL_SELF_CHECKS_PASS`.

The genuinely complementary parameter-face theorem was then checked separately:

- `artifacts/prob10_2026-09-20/PROB10-03/20260920T1421Z_r14_parameter_face_sensitivity_checker_4c2a.py`, commit `fbdbddbc0fe8d41a37298c6950d680b0b59f850f`;
- matching `.out`, commit `ca5fe2c78d049d764528cee90e8990be6ec0bd68`, ending `ALL_PARAMETER_FACE_SELF_CHECKS_PASS`.

The numerical falsification checks are deliberately not promoted to theorem endpoints. They verify the signed derivative predictions at the inherited third-full numerical point and test (4.14) by finite differences. Most importantly, they falsify the tempting stronger statement that `D_H` is monotone in `m`: two stable test tuples give `partial_m D_H approximately +3.955643465` and `approximately -0.1950824765` consistently at GH orders 100, 140, 180, and 220. That is numerical evidence of the obstruction; the report relies only on the exact unsigned formula (4.15), not on treating those floating values as a theorem.

All checks here are self-checks, not independent audits.

## 9. Source metric before/after and auxiliary movement

### Source metric

After consuming the newer companion update, before this R14 mathematical iteration:

`[6.30297437506, 12.319634446195]`, width `6.016660071135`.

After this R14 iteration:

`[6.30297437506, 12.319634446195]`, width `6.016660071135`.

**R14 source-level movement this run: none.**

The `5e-12` move from `12.3196344462` to `12.319634446195` belongs to NM13-07 and is only consumed here. No `12.316...` or `12.287...` complete-third numerical value is promoted.

### Auxiliary / mechanism movement

1. Proved the exact normalized-expectation sensitivity formulas (4.2)--(4.5) for the complete-third outer tilt.
2. Proved a signed parameter-face table for `A1,A2,AH,D_U,D_H` in `a,m,lambda`, including the two-level variance identity (4.14).
3. Isolated the one dangerous c-sector face: `D_H` has exact derivative (4.15) but no safe universal `m` sign; the checker explicitly tested the negation rather than assuming monotonicity.
4. Proved the unweighted overlap second moment has positive first derivative at zero overlap for every `alpha>0`, rigorously retiring that raw SAT-side route.
5. Re-expressed the dual as a radius-one nonconvex minmax and isolated why direct ball/CGMT convexification loses the source constraint.
6. Preserved the companion's concurrent all-moment theorem as companion work rather than duplicating or overwriting ownership.

## 10. Remaining full-scope gap

The exact `kappa=-1` capacity problem remains **OPEN / PARTIAL** under the repository closure standard.

The strongest next source-moving route is now more specific:

1. work at a prescribed positive complete-third objective gap (rather than the zero-objective capacity point) so positivity is exact by construction;
2. choose a small strict-domain box in the companion's dimensionless `(w0,w1,x,m)` chart;
3. use companion outer-`V` monotonicity together with this report's parameter-face signs to replace as much nested interval differentiation as possible by corner evaluations;
4. treat the remaining `D_H`-in-`m`, `d^2`, and residual cross-dependence with explicit covariance/interval bounds rather than an invented monotonicity;
5. obtain a weighted Krawczyk/contraction inclusion for all four residuals and reconstruct a density strictly below `12.319634446195` with a certified positive comparison value;
6. recheck every source-matched fully lifted comparison hypothesis and obtain the required independent validations before any closure claim.

A floating quadrature root, ansatz transition, smaller-radius algorithm, ball relaxation, or self-check is not an endpoint.

## 11. Structured ledger delta

```yaml
ledger_delta:
  task: PROB10-03
  worker_route: R14 owner-refocused complementary route
  status: OPEN/PARTIAL
  model_runtime: GPT-5.6 Sol
  reasoning_effort: UNVERIFIED
  entering_companion_update:
    alpha_U_previous: "12.3196344462"
    alpha_U_current: "12.319634446195"
    credited_worker: NM13-07
    source_gain: "5e-12"
  source_metric_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.319634446195"
    width: "6.016660071135"
  source_metric_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.319634446195"
    width: "6.016660071135"
  source_movement_this_run: none
  new_exact_auxiliary_results:
    - "outer normalized-expectation sensitivity identities in a,m,lambda,d^2"
    - "signed parameter-face table for score/energy moments and D_U"
    - "two-level negative lambda derivative identity for AH"
    - "positive a derivative for D_H with m derivative left unsigned"
    - "unweighted overlap second-moment positive-slope obstruction at rho=0"
    - "radius-one dual minmax / convexification obstruction"
  concurrent_collision:
    companion_all_moment_theorem: "NM13-07; consumed, not claimed as R14 novelty"
  campbell_handoff_preserved:
    path: "artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md"
    navigation: "3846db33296cfb6eea59ff7c488929087c7b62a2"
    metric: "S=5 preserved"
  scheduler_changed: false
  cadence_or_enabled_state_changed: false
  email_or_drive: false
  public_posting: false
  canonical_claim_changed: false
  force_push: false
```
