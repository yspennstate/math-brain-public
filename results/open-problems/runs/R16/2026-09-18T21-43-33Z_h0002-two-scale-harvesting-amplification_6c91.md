Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the canonical frozen H0002 class, the concrete certified giant fraction moves from `rho*(q_out-q0/64)` to `rho*(1-q0/32)`, and in fact every fixed coefficient strictly below `rho*(1-q0/64)` is proved. Section-B methods actually used: **#19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE, #30 DO ONE SCALE AT A TIME**. All 30 catalogued moves had already been used on H0002, so this is a nonconsecutive reuse of a different triple, not invented unused history.

# R16 — H0002: two-scale harvesting amplifies Poisson-survival trials to almost the full deletion budget

## 1. Continuity, ownership, required reads, and current source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural conditions under which, at `p >= (1+epsilon)/lambda(G)`, bond percolation has a component of order `Omega(|G|)` with constant probability.

Before doing mathematics I reread/reconciled the required repository surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the newest own R16 report `runs/R16/2026-09-18T20-44-14Z_h0002-poisson-survival-root-correction_c2f7.md`, and the newest recoverable neighboring same-source records. G0010 / Question 5.2 is already at terminal HARD handoff, and the old G0011 long-cycle lane is also handed off; neither changes H0002 ownership. I found no H0002 release or handoff.

Fresh primary-source checks on 18 Sep 2026 / 19 Sep local time still recover CMW only as arXiv:2608.19145v1 from 19 Aug 2026; a bounded title/question/author search found no later source-matching resolution. This is negative bounded-search evidence, not a worldwide novelty certificate.

Primary/current URLs checked:

- `https://arxiv.org/abs/2608.19145`
- `https://arxiv.org/abs/2508.03961`
- `https://arxiv.org/abs/2609.11189`
- `https://eccc.weizmann.ac.il/report/2026/188/`

The native Beck--Fiala scheduler title is stale as an active mathematical target. Bansal--Jiang, arXiv:2508.03961v2, reach `O(sqrt(t))` for `t >= log^2 n` and weaker polylogarithmic bounds below that range. Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`, all `n`. Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with constant `36`. These are extremely recent primary-source baselines, not R16 discoveries. On their stated theorems the original Beck--Fiala square-root target is currently KNOWN, so R16 correctly continues the admitted H0002 successor instead of reopening the obsolete `t>=log^2 n` gap.

## 2. Frozen H0002 class and incoming metric

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Let `n=|G|`, `lambda=lambda(G)`, and set

`a0 := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`beta0 := q0/64`,

`alpha0 := rho*beta0`.

The frozen graph class is unchanged:

1. **H1 (spectral deletion resilience):** `lambda(G-S) >= a0 lambda` whenever `|S|<=rho n`;
2. **H2 (macroscopic pair expansion):** `e_G(A,B) >= kappa lambda n` for all disjoint `A,B` with `|A|,|B|>=alpha0 n`;
3. **H3:** `lambda -> infinity` along the graph sequence.

The tracked quantity is the largest explicit uniform giant fraction `g_twoaxis(epsilon,rho,kappa)` proved on this frozen class.

The incoming report proved a local Poisson-survival law. Define

`u_inf := a0*(1+epsilon)-1 = epsilon*(7-epsilon)/8`,

`b_inf := 1+u_inf = a0*(1+epsilon)`,

and let `q_BP` be the positive solution of

`q_BP = 1-exp(-b_inf*q_BP)`.

It proved every fixed coefficient below `rho*(q_BP-beta0)` and used the concrete receipt

`q_out := (q_KL+q_BP)/2`,

`g_in := rho*(q_out-beta0)`.

The present run does **not** improve the one-trial survival probability. It changes how trial **sizes** are accumulated. That distinction is the entire gain.

## 3. Dependency reproduced: the root-corrected local survival lemma

I restate the exact local fact needed below so the new amplification is checkable without guessing what the prior report used.

Let `H` be a current connected residual host with spectral radius `Lambda`. Normalize a positive Perron vector `w` so that a maximum-weight root `v` has `w(v)=1`. Explore its Bernoulli-`p1` component by adaptive edge queries. If query `i` points to a vertex of weight `x_i in [0,1]` and has Bernoulli result `xi_i`, put

`S=sum_i xi_i x_i`, `Q=sum_i x_i`, `W=w(C_v)`.

Every discovered nonroot vertex is first reached by exactly one successful query, hence the exact identity

`S=W-1`.

On `|C_v|<=gamma Lambda`, the Perron boundary accounting gives

`Q >= (1-gamma)Lambda W`.

For any `a>=0`,

`M_t = exp{-a S_t + p1(1-exp(-a))Q_t}`

is a nonnegative supermartingale, because for each predictable `x in [0,1]`,

`1-p1+p1 exp(-a x) <= exp{-p1 x(1-exp(-a))}`.

If

`b := p1 Lambda (1-gamma)>1`,

let `r(b)>0` be the positive solution

`r=b(1-exp(-r))`.

At `a=r(b)`, on the small-component event,

`log M_T >= r + [b(1-exp(-r))-r]W = r`.

Optional stopping and Markov imply

`P(|C_v|<=gamma Lambda) <= exp(-r(b))`.

Thus

`P(|C_v|>gamma Lambda) >= q(b)`,

where `q(b)=1-exp(-r(b))` is the positive solution of

`q=1-exp(-bq)`.

Only this already-proved local lemma is used below.

## 4. Methods #19 and #30 — make the proof an algorithm, at two genuinely different scales

As before put

`tau := lambda^(-1/3)`,

`p1 := (1+epsilon-epsilon*tau)/lambda`,

and expose an independent second round with probability `p2` chosen so that

`1-p=(1-p1)(1-p2)`, `p=(1+epsilon)/lambda`.

Then

`p2 >= epsilon*tau/lambda = epsilon*lambda^(-4/3)`.

The **small scale**, used only to classify a trial as seed/nonseed, is

`s := a0*tau*lambda = a0*lambda^(2/3)`.

Now introduce a separate **jackpot scale** of order `lambda`. Set

`gamma_J := u_inf/(4*b_inf) > 0`,

`L_J := a0*gamma_J*lambda`.

Since `tau->0`, eventually `s<L_J`.

Consider any adaptive residual graph `H=G-S_old` at a moment when fewer than `rho n` vertices have been deleted. H1 gives

`Lambda_H >= a0 lambda`.

For the jackpot threshold choose

`gamma_H := L_J/Lambda_H <= gamma_J`.

Also

`p1 Lambda_H >= a0*(1+epsilon-epsilon*tau) = b_inf-a0*epsilon*tau`.

Hence the branching parameter in the local lemma satisfies

`b_H := p1 Lambda_H (1-gamma_H)`

`>= (b_inf-a0*epsilon*tau)(1-gamma_J)`.

By the definition of `gamma_J`, the right-hand side tends to

`b_inf(1-gamma_J)=b_inf-u_inf/4=1+3u_inf/4`.

Therefore, for all sufficiently large `lambda`,

`b_H >= b_J := 1+u_inf/2 > 1`.

Let `q_J=q(b_J)>0` be the positive solution

`q_J=1-exp(-b_J q_J)`.

The local survival lemma now gives the uniform adaptive statement

`P( |C_v|>L_J | entire past ) >= q_J`.

So every trial, no matter what happened on earlier trials as long as fewer than `rho n` vertices have been deleted, has a fixed positive conditional probability of producing a component of order `lambda`.

### The harvesting algorithm

Let `R:=rho n`. Repeatedly:

1. in the current residual graph, choose a component attaining the residual spectral radius and a maximum-Perron-weight root;
2. expose the entire round-one `p1` component of that root;
3. delete that whole revealed component;
4. call it a **seed** if its vertex size is `>s`;
5. call it a **jackpot** if its vertex size is `>L_J` (hence every jackpot is a seed).

Stop when either

- seed vertex mass `W` reaches a prescribed target, or
- total deleted vertex mass `D` reaches `R`.

H1 is valid at the start of every trial, since all trials begin with `D<R`.

This is the algorithmic change: the preceding proof treated every successful seed as one Bernoulli success. Here seed **mass** is harvested, and the `s` versus `L_J` scale gap is exploited.

## 5. Method #25 — count the failure mass twice

First prove a concrete fixed movement. Set the target

`W_target := (1-beta0)R`.

Suppose the harvesting algorithm fails, meaning that it hits `D>=R` while still

`W < (1-beta0)R`.

Every deleted component that is not a seed has size at most `s`. Since deleted components partition the deleted vertex set,

`nonseed mass = D-W > beta0 R`.

Therefore the number of nonseed trials is strictly larger than

`beta0 R/s`.

In particular, on failure the first

`N0 := ceil(beta0 R/(2s))`

trials certainly exist.

For `1<=j<=N0`, let `X_j` be the jackpot indicator. From the preceding section,

`P(X_j=1 | F_{j-1}) >= q_J`.

The adaptive indicators therefore satisfy the same lower-tail Chernoff estimate as iid Bernoulli(`q_J`) variables. For completeness, for `theta>0`,

`E[exp(-theta X_j)|F_{j-1}] <= 1-q_J+q_J exp(-theta)`,

so iteration plus the usual exponential Markov optimization gives

`P(sum_{j<=N0} X_j < q_J N0/2) <= exp(-q_J N0/8)`.

If instead

`sum_{j<=N0} X_j >= q_J N0/2`,

then jackpot components alone contribute seed mass greater than

`(q_J/2) N0 L_J`

`>= (q_J beta0/4)(L_J/s) R`

`= (q_J beta0 gamma_J/(4 tau)) R`.

Because `tau=lambda^(-1/3)->0`, this last coefficient tends to infinity. Hence for all sufficiently large `lambda` it exceeds `1-beta0`, contradicting the assumed failure `W<(1-beta0)R`.

Consequently

`P( W<(1-beta0)R before D reaches R )`

`<= exp(-q_J N0/8)=o(1)`.

The `o(1)` is uniform along the graph sequence: since `lambda<=n-1`,

`N0 >= c(epsilon,rho) n/lambda^(2/3) >= c'(epsilon,rho)n^(1/3)`

for all large `n`.

This is the key amplification. A fixed positive **trial** probability `q_J` no longer caps the fraction of **vertex mass** that can become seed mass, because a positive fraction of trials contribute `Theta(lambda)` vertices while failures contribute at most `O(lambda^(2/3))` each.

## 6. Sprinkling gives the new concrete giant fraction

Condition on the high-probability event

`W >= (1-beta0)R`.

Every seed is a genuine connected round-one component of size `>s`, so the true seed-component quotient has at most

`m <= n/s = n/(a0 lambda^(2/3))`

vertices.

For large `lambda`, `W>=3 alpha0 n` because `alpha0=beta0 rho` and `beta0<1/64`.

If no round-two component captures at least `W-alpha0 n` seed vertices, the same deterministic balanced-cut extraction used in the repaired preceding R16 proof gives a quotient cut whose two original vertex sides each have size at least `alpha0 n`. H2 supplies at least

`kappa lambda n`

host edges across this cut.

For any fixed quotient cut, the probability that round two opens none of those edges is at most

`exp(-p2*kappa lambda n) <= exp(-kappa*epsilon*n/lambda^(1/3))`.

There are at most `2^m` quotient cuts. Therefore

`P(sprinkling fails | seed family)`

`<= exp{ [ (log 2)/(a0 lambda^(2/3)) - kappa*epsilon/lambda^(1/3) ] n }`

`=o(1)`

by H3.

Thus with probability `1-o(1)` after the successful harvest,

`L1(G_p) >= W-alpha0 n`

`>= (1-beta0)rho n - beta0 rho n`

`= rho(1-2 beta0)n`.

Since `2 beta0=q0/32`, the new explicit concrete metric is

`g_new := rho*(1-q0/32)`

`= rho*[1-(1-exp(-epsilon^2/288))/32]`.

This is a strict improvement over the incoming

`g_in=rho*(q_out-beta0)`.

Indeed `q_out<q_BP<1`, while `1-beta0>q_BP`: from the fixed-point equation,

`1-q_BP=exp(-b_inf q_BP)>exp(-b_inf)>=exp(-7/4)>1/64>beta0`.

Hence

`1-2beta0 > q_out-beta0`.

So the fixed metric genuinely moves on exactly the same frozen H1--H2--H3 class.

## 7. Stronger theorem: the harvesting envelope is `rho*(1-beta0)`

The preceding fixed choice `beta0` is not intrinsic to the harvest. Let

`delta_lambda := lambda^(-1/6)`

and instead stop successfully at

`W >= (1-delta_lambda)R`.

If this target fails before `D>=R`, then the nonseed mass exceeds `delta_lambda R`, hence failure forces at least order

`delta_lambda R/s`

`= Theta( n/lambda^(5/6) )`

trials. This tends to infinity uniformly because `lambda<=n`.

Take the first half that many trials. Their jackpot count is at least a positive constant fraction with probability `1-o(1)`. The corresponding jackpot mass divided by `R` is bounded below by a positive constant times

`delta_lambda*(L_J/s)`

`= Theta(lambda^(-1/6)*lambda^(1/3))`

`= Theta(lambda^(1/6)) -> infinity`,

which contradicts failure for large `lambda`.

Therefore

`P( W >= (1-lambda^(-1/6)) rho n ) = 1-o(1)`.

Applying the same sprinkling step gives

`P( L1(G_p)/n >= rho*(1-beta0-lambda^(-1/6)) ) = 1-o(1)`.

Consequently **every fixed coefficient strictly below**

`g_harvest_sup := rho*(1-beta0)`

`= rho*[1-(1-exp(-epsilon^2/288))/64]`

is certified on the unchanged frozen H1--H2--H3 class.

I am **not** claiming attainment of the endpoint `g_harvest_sup`; the proved finite-`lambda` statement has the displayed `lambda^(-1/6)` loss. The immutable single-number receipt for this run is the simpler exact constant `rho*(1-q0/32)` from Section 6.

## 8. What this changes conceptually, and the next obstruction

The preceding report's `q_BP` was a true one-trial local survival probability, but it was **not** a global ceiling on harvestable vertex mass. That apparent ceiling came from treating all successful/failed trials as if they had comparable sizes.

The new invariant is a two-scale size bias:

- failures/nonseeds cost at most `s=Theta(lambda^(2/3))` vertices;
- every trial has fixed positive conditional probability `q_J` to return a jackpot of size `Theta(lambda)`;
- H1 makes this repeatable until a linear deletion budget `rho n` is consumed.

That is enough to make the seed mass occupy `rho n-o(n)` vertices with high probability.

There is now a clean structural barrier in the **frozen assumptions**, not merely in the proof constants. H1 guarantees repeatability only while fewer than `rho n` vertices have been deleted. H2 only guarantees an edge across cuts when both sides have at least

`alpha0 n = beta0 rho n`

vertices. Therefore this harvest-plus-all-cut-sprinkling architecture naturally tops out at

`rho n-alpha0 n = rho(1-beta0)n`

up to `o(n)`. To beat that envelope, a future route must contain information absent from the current black boxes: deletion resilience beyond `rho n`, expansion below the `alpha0 n` scale, or a mechanism that attaches the final sub-`alpha0 n` remainder without asking H2 to control it. This is a barrier of the frozen H1/H2 proof interface, **not** an upper bound on the source problem.

## 9. Prior-art scope

I searched combinations of finite-graph percolation, spectral radius/Perron exploration, repeated component harvesting, large-set expansion, sprinkling, and giant components. The search recovered established expander/pseudorandom-graph percolation literature, including Alon--Benjamini--Stacey on finite expanders and Diskin--Krivelevich on pseudorandom graphs. Those works are baseline evidence that local branching plus large-set connectivity is a standard shape of argument. I did not find this exact adaptive H1 repeated-harvest / two-threshold `lambda^(2/3)` versus `lambda` amplification theorem in the bounded search. That negative result is **not** a novelty certificate.

The source question remains open-ended rather than closed: H0002 is only a sufficient-condition theorem on a frozen graph class. No claim is made that this class is necessary or that Question 5.1 is classified.

## 10. Status, metric, stuck counter, and next methods

Status remains **PARTIAL / SOURCE OPEN / ACTIVE**.

Metric before:

`g_before = rho*(q_out-q0/64)`

from the Poisson-survival report.

Metric after (single concrete receipt):

`g_after = rho*(1-q0/32)`.

Stronger asymptotic statement:

`L1(G_p)/n >= rho*(1-q0/64-lambda^(-1/6))`

with probability `1-o(1)`, hence every fixed coefficient below `rho*(1-q0/64)` is certified.

Because the fixed metric moved, the supported unchanged count resets to `0`; no stuck recovery is active.

All thirty Section-B methods have already appeared in the H0002 history. The next run should therefore reuse a nonconsecutive triple only if it attacks the **new** structural obligation above. A sensible next triple is **#6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #27 SWAP THE QUANTIFIERS**: deform H2 below `alpha0`, express attachment of the leftover as a cut/flow dual question, and ask whether one can find a random/selected remainder-attaching structure instead of demanding H2 for every small remainder.

No exact-arithmetic checker was created: the new claim is analytic and has no finite computational core. The proof is on the page. Independent OTHER-track audits required for closure have not been requested or claimed here.

## 11. Model/scheduler and permission status

The model-control limitation is still unchanged. The exposed automation interface has fields for title, prompt, schedule/start offset, timing mode, enablement and task identity, but no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model receipt. Therefore GPT-6/maximum remains a prompt request only here. Enforcing it would require the scheduler/API to expose model and reasoning fields and to provide per-run runtime attestation.

The historical `You cannot modify this task` error for P26 was authorization-context-specific: the current root ledger records a later successful P26 update from an authorized context, while other contexts still recorded denials. The compliant workaround for any task that still refuses modification is to use its owning authorized workspace/account context or platform support. Do not duplicate the task or bypass permissions. No scheduler changes were attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  canonical_target: H0002
  source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  status_before: PARTIAL / SOURCE OPEN / ACTIVE
  status_after: PARTIAL / SOURCE OPEN / ACTIVE
  metric: g_twoaxis(epsilon,rho,kappa), frozen H1-H2-H3 class
  value_before: rho*(q_out-q0/64), q_out=(q_KL+q_BP)/2
  value_after: rho*(1-q0/32)
  stronger_certified_envelope: every fixed g < rho*(1-q0/64)
  quantitative_rate: L1/n >= rho*(1-q0/64-lambda^(-1/6)) with probability 1-o(1)
  movement: strict
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_this_run: [19,25,30]
  new_mechanism: two-scale adaptive harvesting; nonseeds O(lambda^(2/3)), jackpots Omega(lambda)
  source_closed: false
  independent_audits_this_run: 0
  checker_required: false
  artifacts_created: none
```
