Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — METRIC MOVEMENT on active R09 successor G0013: `U_* = 1/6 -> 1/9`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported unchanged count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B21 ASK WHO ELSE HAS THIS SHAPE, B15 BREAK THE SYMMETRY ON PURPOSE, B3 PROVE SOMETHING STRONGER.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013 second active run: Chatterjee-xi representation and a full-class `1/9` bound

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Tang Question 4.11. Its periodic-tree clause remains retired in R09 with frozen metric `UNBOUNDED_ABOVE` and supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which R09 handed off at `Delta_8=UNMEASURED`.

The controlling current claim is `operations/claims/G0013.md`: R09 exclusively owns the Catalano--Lavenant uniform-copula Wasserstein problem. With `lambda=Unif[0,1]`, `nu=lambda tensor lambda`,

`M = sup_{pi in Pi(lambda,lambda)} W_2^2(pi,nu)`.

The source conjecture is `M=1/10`, attained by the diagonal and antidiagonal copulas. The frozen metric is

`U_* = the smallest rigorous source-valid global upper bound on M established by R09`.

The preceding R09 report proved `U_*=1/6` by one-coordinate resampling and exactly evaluated the diagonal at `1/10`. Thus the pre-run rigorous bracket was

`1/10 <= M <= 1/6`.

I continued from that state rather than restarting the finite permutation searches.

### Required repository continuity reads

Before new work I reread/recovered the current campaign/control state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the active G0013 claim, the newest complete R09 G0013 report, and the newest available neighboring R08 material. Repository-wide searches were also used for ownership and prior G0013 attempts. Large intake JSONL files exceed a single connector rendering, so exact-ID/current-claim/attempt retrieval was used for the active target; I do not falsely claim a byte-for-byte visual reread of all roughly 780 intake rows.

## 2. Fresh source/current-literature/ownership check

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3. It poses the Euclidean quadratic-Wasserstein supremum over bivariate uniform copulas and conjectures the monotone and antimonotone couplings.

Fresh later source: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 2026-09-09. Its abstract still states the Catalano--Lavenant uniform result as a conjecture and proves instead the Gaussian analogue.

Fresh bounded searches on 2026-09-17 included the exact source title/authors, exact later title, `uniform copula Wasserstein 1/9`, `Catalano Lavenant 1/9`, `Chatterjee xi Brenier Wasserstein copula`, and the relevant Wright--Fisher/Jacobi weighted Poincare terminology. I found no later source-matching resolution and no source explicitly advertising the `1/9` bound below. This is only bounded negative evidence: **publication novelty is UNVERIFIED**.

Current ownership is unambiguous: `operations/claims/G0013.md` names R09. Another current research-track report explicitly excludes G0013 because of that R09 claim. I create no new claim and do not edit shared roots.

## 3. B21 — the weighted Brenier functional is exactly a sum of two directed Chatterjee-xi coefficients

This is the main category connection of the run.

Let `Q=(0,1)^2`, let `(X,Y)` be uniform on `Q`, and let

`T=grad phi=(u,v)`

be the Brenier map from the independent uniform square `nu` to an arbitrary copula `pi`. Because `pi` has uniform one-dimensional marginals, both random variables `u(X,Y)` and `v(X,Y)` are uniform on `[0,1]`.

Write

`w(s)=s(1-s)`

and, initially in the smooth strictly convex case,

`a=phi_xx`, `b=phi_xy`, `c=phi_yy`.

The previous run established

`W_2^2(pi,nu)=1/3-J_1-J_2`,

where

`J_1 = int_Q w(x) a(x,y) dxdy`,
`J_2 = int_Q w(y) c(x,y) dxdy`.

I now rewrite each `J_i` as a conditional-variance deficit.

For `t in [0,1]`, define the horizontal sublevel length

`q_t(y) = Leb{x in [0,1] : u(x,y) <= t}`.

Convexity makes `x -> u(x,y)` nondecreasing, so this is a single threshold (with the usual clipping at `0` and `1`). Since `u(X,Y)` is uniform,

`int_0^1 q_t(y) dy = P(u<=t)=t`.                                  (3.1)

For fixed `y`, changing variables `t=u(x,y)` on the non-clipped portion gives

`int_0^1 w(x) u_x(x,y) dx = int_0^1 w(q_t(y)) dt`.

The clipped portions cause no term because `w(0)=w(1)=0`. Integrating in `y` and using (3.1),

`J_1`
` = int_0^1 int_0^1 [q_t(y)-q_t(y)^2] dy dt`
` = int_0^1 [t(1-t)-Var_y(q_t(Y))] dt`
` = 1/6 - I_1`,                                                 (3.2)

where

`I_1 := int_0^1 Var_y(q_t(Y)) dt`.

Likewise, with

`r_s(x)=Leb{y in [0,1]: v(x,y)<=s}`

and

`I_2 := int_0^1 Var_x(r_s(X)) ds`,

we have

`J_2 = 1/6-I_2`.                                                (3.3)

Substitution into the Brenier identity yields the exact formula

`W_2^2(pi,nu) = I_1+I_2`.                                      (3.4)

Now compare (3.4) with the population definition of Chatterjee's directed rank correlation. For a continuous uniform response `U`,

`xi(Z,U)=6 int_0^1 Var(P(U<=t | Z)) dt`

(the use of `<=` versus `>=` does not change the variance). Therefore

`xi(Y,u)=6 I_1`,
`xi(X,v)=6 I_2`,

and hence

> **Exact directed-dependence identity**
>
> `W_2^2(pi,lambda^2) = [ xi(Y,u) + xi(X,v) ] / 6`,             (3.5)
>
> where `(u,v)=grad phi(X,Y)` is the Brenier image of the independent square.

There is a second exact identity. Spearman's rho for two uniforms is `rho_S(A,B)=12 Cov(A,B)`. The one-dimensional integration-by-parts identity from the previous report gives

`rho_S(X,u)=6J_1=1-xi(Y,u)`,
`rho_S(Y,v)=6J_2=1-xi(X,v)`.                                  (3.6)

Thus the source conjecture `M<=1/10` is equivalently the statement that the two **cross-directed** Chatterjee coefficients of every square Brenier map satisfy

`xi(Y,u)+xi(X,v) <= 3/5`.                                     (3.7)

This appears to be a substantially cleaner dependence-theoretic target than the original Wasserstein maximization.

### Literature shape check

Ansari--Rockel, *The exact region and an inequality between Chatterjee's and Spearman's rank correlations* (arXiv:2506.15897; Journal of Multivariate Analysis 2026), gives the population conditional-variance formulation of `xi`, determines the exact `xi-rho` region, and proves `xi<=|rho|` for stochastically increasing/decreasing copulas. Their reported maximal `rho-xi` is `0.4`.

For the diagonal extremizer here, symmetry and the already proved value `W_2^2=1/10` give

`xi(X,u)=xi(Y,u)=3/10`,
`rho_S(X,u)=7/10`,

so the diagonal Brenier coordinate pair lands exactly at difference `0.4`. This does **not** prove the source conjecture, but it is a nonaccidental match to a current sharp dependence inequality and identifies a concrete outside toolkit for the remaining `3/5` bound.

I found no source in the bounded search stating identity (3.5). I do **not** claim novelty from that absence.

## 4. B15 — keep the two directions asymmetric and use the PSD Hessian instead of symmetrizing the copula

The next step deliberately avoids assuming that an optimizer is symmetric. The two directed slice families `q_t` and `r_s` are treated separately.

The needed one-dimensional inequality is the sharp Jacobi/Wright--Fisher Poincare inequality for uniform measure on `[0,1]`:

> **Lemma (sharp weighted Poincare).** For every absolutely continuous `f` with finite weighted energy,
>
> `Var(f) <= (1/2) int_0^1 y(1-y) f'(y)^2 dy`.                 (4.1)

A short proof is included because the constant matters. Expand the mean-zero part of `f` in the shifted Legendre basis. The Sturm--Liouville operator

`L g = - d/dy [ y(1-y) g'(y) ]`

has shifted Legendre eigenfunctions of degree `n` with eigenvalues `n(n+1)`. Constants are the `n=0` mode and the first nonconstant eigenvalue is `2`, attained by the affine mode. Parseval therefore gives

`int y(1-y) f'^2 >= 2 int (f-Ef)^2`,

which is exactly (4.1); density extends it from polynomials/smooth functions to the weighted Sobolev domain.

Apply (4.1) to `q_t`. Wherever `0<q_t(y)<1`, the identity

`u(q_t(y),y)=t`

gives by implicit differentiation

`q_t'(y) = - b/a`

at the point `(q_t(y),y)`; on clipped portions `q_t` is locally constant a.e. Therefore

`I_1`
` <= (1/2) int_0^1 int_0^1 w(y) q_t'(y)^2 dy dt`
` =  (1/2) int_Q w(y) b(x,y)^2/a(x,y) dxdy`.                  (4.2)

The last equality is again `dt=a dx` on each horizontal slice. Since `D^2 phi` is positive semidefinite,

`b^2 <= ac`,

so

`I_1 <= (1/2) int_Q w(y)c = J_2/2`.                           (4.3)

The completely asymmetric twin argument gives

`I_2 <= J_1/2`.                                                (4.4)

No exchangeability of `pi`, no sign assumption on `b`, and no diagonal/antidiagonal ansatz was used.

In Chatterjee language (4.3)--(4.4) become the pair of directed inequalities

`xi(Y,u) <= [1-xi(X,v)]/2`,
`xi(X,v) <= [1-xi(Y,u)]/2`.                                  (4.5)

Adding them gives

`xi(Y,u)+xi(X,v) <= 2/3`.                                    (4.6)

This already improves the Wasserstein metric globally.

### A distinct deterministic-density correction to the old extreme-point obstruction

The prior G0013 attempt correctly warned that nonatomic extreme copulas need not all be deterministic maps. That blocks an **extreme-point classification**, but it does not block a deterministic approximation strategy. The classical shuffles-of-Min theorem says shuffles of Min are dense in the copula class in the uniform topology; later multivariate shuffle work records the same density mechanism. On compact `[0,1]^2`, uniform convergence of copula distribution functions implies weak convergence of the induced probability measures, and compactness upgrades this to `W_2` convergence. Consequently

`M = sup{ W_2^2(pi,nu) : pi is a shuffle of Min }`.           (4.7)

This is not used to justify the full-class bound below, but it is strategically important: a future proof or counterexample search may restrict to arbitrarily asymmetric deterministic shuffles **by density**, without making the false claim that all extreme copulas are deterministic. Because Chatterjee's `xi` itself has delicate continuity properties, (4.7) should be applied to the original `W_2` functional, not naively to the `xi` terms separately.

## 5. B3 — stronger full-class theorem: `M <= 1/9`

We can now prove a full continuous theorem, not a grid or deterministic-map restriction.

> **Theorem.** For every bivariate copula `pi` with uniform marginals on `[0,1]`,
>
> `W_2^2(pi, lambda tensor lambda) <= 1/9`.                    (5.1)
>
> Hence the active R09 metric improves from `U_*=1/6` to
>
> `U_*=1/9`.

### Proof for smooth positive copulas

With the notation above, combine (3.2)--(3.4) and (4.3)--(4.4):

`I_1 <= J_2/2 = (1/6-I_2)/2`,
`I_2 <= J_1/2 = (1/6-I_1)/2`.

Adding,

`I_1+I_2 <= 1/6 - (I_1+I_2)/2`.

Therefore

`(3/2)(I_1+I_2) <= 1/6`,

so

`I_1+I_2 <= 1/9`.

By (3.4), this is exactly (5.1).

For completeness about regularity: for a smooth target copula density bounded above and below away from zero, the Brenier potential from the uniform square is an Alexandrov solution with positive definite Hessian a.e. and has the standard interior Monge--Ampere regularity. The preceding slice identities are applied where the threshold lies in the interior; clipped pieces are constant and contribute zero, and the square boundary is null. Equivalently one may work on compact interior subrectangles and pass to the boundary. The change-of-variables relation `dt=a dx` and `b^2<=ac` hold a.e., which is all the proof uses.

### Passage to an arbitrary copula

Let `K_epsilon` be a positive smooth approximate identity on the circle. If `(U,V)~pi`, add independent circular noises `Z_1^epsilon,Z_2^epsilon` with density `K_epsilon` and set

`U_epsilon=(U+Z_1^epsilon) mod 1`,
`V_epsilon=(V+Z_2^epsilon) mod 1`.

The law `pi_epsilon` is a positive `C^infinity` copula density: convolution preserves each uniform marginal exactly. Also `pi_epsilon -> pi` in Euclidean `W_2`. One direct coupling is the construction just given; away from a boundary strip its Euclidean displacement is the small circular noise, while the bad wrap event has probability tending to zero because each marginal is uniform. Bounded support then gives convergence of the second moment cost.

Apply the smooth result to every `pi_epsilon`:

`W_2^2(pi_epsilon,nu) <= 1/9`.

Because `W_2(pi_epsilon,pi)->0`, the triangle inequality implies

`W_2(pi_epsilon,nu)->W_2(pi,nu)`.

Passing to the limit proves (5.1) for every copula. QED.

### Metric consequence

The source lower endpoint remains the exact diagonal value `1/10`, so the source-valid global bracket is now

`1/10 <= M <= 1/9`.                                            (5.2)

The absolute upper-gap shrinks from

`1/6-1/10 = 1/15`

to

`1/9-1/10 = 1/90`.

This is **PARTIAL**, not closure.

## 6. The exact remaining inequality is now a positive-deficit problem of size `1/60`

The proof above also identifies the missing sharp ingredient.

Define the two weighted Poincare deficits

`D_q = (1/2) int_0^1 int_0^1 w(y) q_t'(y)^2 dy dt - I_1 >= 0`,

`D_r = (1/2) int_0^1 int_0^1 w(x) r_s'(x)^2 dx ds - I_2 >= 0`,

and the two PSD/determinant slacks

`S_q = (1/2) int_Q w(y) [ c - b^2/a ] dxdy >= 0`,

`S_r = (1/2) int_Q w(x) [ a - b^2/c ] dxdy >= 0`,

with the natural limiting interpretation where a diagonal Hessian entry vanishes.

Then (4.2)--(4.4) give the exact identity

`D_q + D_r + S_q + S_r`
` = (J_1+J_2)/2 - (I_1+I_2)`
` = 1/6 - (3/2) W_2^2(pi,nu)`.                                (6.1)

Nonnegativity of the left side is exactly the new `1/9` theorem. The Catalano--Lavenant upper bound `W_2^2<=1/10` is therefore equivalent, in this regularized Brenier formulation, to the stronger uniform deficit estimate

> `D_q + D_r + S_q + S_r >= 1/60`.                            (6.2)

For the diagonal Brenier map, the Hessian has rank one, so the determinant slacks vanish, and the total Jacobi Poincare deficit is exactly `1/60`. Thus the conjectured extremizer has exactly the amount of non-affineness needed to bridge `1/9` to `1/10`.

This is the cleanest remaining obligation I know: prove that a Brenier map with two uniform output coordinates cannot make **both** the Jacobi spectral deficit and the Monge--Ampere determinant slack simultaneously smaller than the diagonal's `1/60`.

## 7. What the three methods actually did

- **B21 ASK WHO ELSE HAS THIS SHAPE — succeeded.** The weighted section-variance terms are exactly directed Chatterjee-xi coefficients, and the sharp one-dimensional operator is the Jacobi/Wright--Fisher spectral-gap operator. Current Ansari--Rockel `xi-rho` theory hits the diagonal at its sharp `rho-xi=0.4` gap.
- **B15 BREAK THE SYMMETRY ON PURPOSE — succeeded.** The proof keeps the two directions separate and uses only `b^2<=ac`; it assumes neither exchangeability nor a sign of the mixed derivative. Separately, shuffles of Min give a dense, highly asymmetric deterministic class for future source-level searches without relying on a false extreme-point classification.
- **B3 PROVE SOMETHING STRONGER — succeeded but did not close the source.** Instead of another finite-grid theorem, the run proves the full continuous source-class bound `M<=1/9`, moving the frozen metric. The remaining gap is `1/90` in squared Wasserstein distance, equivalently the deficit lower bound (6.2).

No exact-arithmetic checker was created: the new claim is analytic and its full proof is on this page. A checker would not strengthen the theorem-sized argument.

## 8. Prior-art status and next routes

Searches performed this run were intentionally mechanism-specific as well as source-specific. They included the exact Catalano--Lavenant and Schrott titles/authors, `1/9` with the uniform-copula Wasserstein problem, Chatterjee-xi + Brenier/optimal transport, Jacobi/Wright--Fisher Poincare, and shuffles-of-Min density. The searches recovered the current source/later Gaussian paper, current exact `xi-rho` work, classical shuffle-density results, and standard Jacobi machinery; they did not surface the theorem (5.1) or identity (3.5). **This is not a novelty certificate.** The mechanisms individually are classical/current; the source-specific combination requires a proper citation search before publication.

Next genuinely different triple, if the metric does not move again, should be:

- **B5 ADD A PARAMETER AND DIFFERENTIATE:** interpolate between determinant-dominated full-rank maps and rank-one shuffle/diagonal maps and differentiate the exact deficit in (6.1).
- **B24 FIND THE EXTREMAL OBJECT:** minimize `D_q+D_r+S_q+S_r` directly; the conjecture predicts the minimum `1/60` and equality only at diagonal/antidiagonal Brenier maps.
- **B13 FIND WHAT ONLY INCREASES:** test whether the combined deficit has a monotonicity under a marginal-preserving Wright--Fisher/heat regularization of the target copula, which would reduce the sharp inequality to the rank-one boundary.

## 9. Model/scheduler control status

The control limitation is still the one recorded by the current owner policy and `RESULTS.md`: the exposed task-management interface offers title, prompt, schedule, enablement, and timing-mode controls, but **no model-family selector, no reasoning-effort selector, and no authenticated applied-run model telemetry**. GPT-6/maximum is therefore request text only here.

To make it enforceable, the product/API would need explicit model and reasoning fields plus authenticated runtime telemetry, or the task would need to be managed from an authorized owning surface that exposes those controls. The historical `You cannot modify this task` response for P26 was authorization-context dependent: current `RESULTS.md` records a later successful P26 update from a different authorized context while another context denied edits. The lawful workaround is the owning authorized context, an ownership/admin transfer, or platform support; not duplication or permission bypass. No scheduler modification was attempted in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  allocation: CLOSABLE_OUTSIDE
  active_target: G0013
  source: Catalano-Lavenant arXiv:2510.06034 Remark 3
  status_before: CLAIMED_ACTIVE / PARTIAL / OPEN_CURRENT
  status_after: CLAIMED_ACTIVE / PARTIAL / OPEN_CURRENT
  metric_name: U_*
  metric_definition: smallest rigorous source-valid global upper bound on M
  metric_before: 1/6
  metric_after: 1/9
  movement: true
  active_stagnation_count_after: 0
  rigorous_bracket_after: 1/10 <= M <= 1/9
  new_full_class_theorem: W_2^2(pi,lambda^2) <= 1/9 for every bivariate uniform copula pi
  new_exact_identity: W_2^2 = [xi(Y,u)+xi(X,v)]/6 for the Brenier map (u,v)=grad(phi)
  remaining_sharp_gap: 1/90
  remaining_equivalent_deficit: D_q + D_r + S_q + S_r >= 1/60
  source_closed: false
  novelty_certified: false
  methods_used: [21, 15, 3]
  next_methods: [5, 24, 13]
  predecessor_Tang:
    state: RETIRED_FROZEN
    metric: UNBOUNDED_ABOVE
    supported_unchanged_count: 6
  predecessor_G0002:
    state: HANDOFF_FROM_R09
    metric: UNMEASURED
  shared_roots_edited: false
  checker_created: false
  scheduler_modified: false
```
