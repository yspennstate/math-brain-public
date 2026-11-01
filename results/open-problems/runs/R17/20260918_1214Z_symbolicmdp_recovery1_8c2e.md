Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but this runtime and the exposed scheduler surface still provide no enforceable model-family selector, reasoning-effort selector, or authenticated applied-effort receipt, so I do not claim otherwise. **NO MOVEMENT: certified deterministic interval width `0.033609950762282626 -> 0.033609950762282626`. Methods tried: #10 DERANDOMIZE, #7 TAKE THE LIMIT, #21 ASK WHO ELSE HAS THIS SHAPE. STUCK RECOVERY 1/2.**

# R17 C048 — stuck recovery 1: exact symbolic Bellman certificates instead of another transfer-matrix refinement

Run ID: `20260918_1214Z_symbolicmdp_recovery1_8c2e`.

The source target remains the binary Chvátal--Sankoff constant
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,\operatorname{LCS}(X_1^n,Y_1^n)}{n}
\]
for two independent iid uniform binary strings. The alphabet, fair product distribution, normalization, and true dependent match array are unchanged. Independent Bernoulli matching is not substituted. Simulation confidence intervals remain excluded from deterministic endpoints.

Because C046 and C047 both left the fixed interval unchanged after C045's movement, this is the third consecutive no-movement run. Under the controlling hard-task rule, this run is therefore a **thinking/stuck run**: I do not manufacture another same-machine lemma or certificate merely to show activity. I identify the blocking statement, audit the failed routes, isolate the simplest unresolved special case, compare to the nearest solved construction, and select exactly one recovery route.

## 1. Baseline and repository continuity

I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the newest R17 report C047, and the newest repository search hits for this target before doing new work. The compact root R17 row remains stale by its own warning and is not used to reset the metric. No posted exclusion or competing ownership for this exact binary-LCS target surfaced.

The deterministic retained interval is still
\[
\boxed{0.792665992\le\gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]
The lower endpoint is the deterministic Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer bound. The upper endpoint is R17 C045's internally exact, gauge-correct all-row cone certificate. C033--C035 remain withdrawn because of the complement-gauge bug repaired at C036.

## 2. (a) Exact blocking statement

The operative blocker is not another local LCS lemma. It is the absence of a compact **exact asymptotic certificate** that crosses either current endpoint:
\[
\boxed{
\text{construct }L_\star>0.792665992\text{ with }L_\star\le\gamma_2,
\quad\text{or construct }U_\star<0.826275942762282626\text{ with }\gamma_2\le U_\star.
}
\]

For the recovery route selected below, this becomes a concrete Bellman-certificate problem. Let `S` be the exact finite lookahead state space, `A(s)` its admissible alignment actions, `r(s,a)` the matched-symbol reward, and `c(s,a)` the consumed-length normalization used by the binary feasible-triplet recurrence. It is enough to exhibit an exactly represented rational potential `h` and a rational
\[
\beta>0.792665992
\]
for which the appropriate average-reward Bellman subsolution inequality holds at **every** state, schematically
\[
\boxed{
\forall s\in S:\quad
\max_{a\in A(s)}
\left[r(s,a)-\beta c(s,a)+\sum_{s'}P(s,a,s')h(s')-h(s)\right]\ge0.
}
\]
A full exact statement must use the precise Kiwi--Soto/Heineman state convention and normalization; the schematic formula here records the object that is missing, not a new theorem. An exact rational Bellman witness above the current lower endpoint would immediately move the fixed metric after applying the already-established finite-to-infinite transfer.

## 3. (b) Routes tried and the precise failure of each

### Upper-bound local-deficiency route, C039--C045

The gauge-correct finite-state covering operator produced genuine repeated movement and culminated in C045, which exhausts the complete minimal local-deficiency language through six factors for the existing `h=8` process. C046 then proved the sharper cap-`r` tail theorem, so seven-factor deficiency is in principle exact on the current hook alphabet. What is missing is not validity of seven-factor deficiency; it is a compact enough representation of the seven-factor obstruction language/product to make a new rigorous operator certificate practical without simply paying for another enormous dictionary/product. The natural universal synchronizer shortcut failed exactly in C047.

### Universal synchronization shortcut, C047

The hoped-for quantifier
\[
\exists w\ \forall s:T_w(s)=s_*
\]
was attacked directly. The natural eight-zero-hook synchronizer has an exact counterexample: two reachable orientations retain distinct derivative masks after the same control word. Therefore a one-word reset cannot be assumed, and the controller must retain more boundary information or use state-dependent completions.

### Monte-Carlo beam lower bound

The public width-100 beam computation gives a strong empirical mean and a Hoeffding confidence statement, but it does not deterministically evaluate the finite expectation. Under the fixed R17 rules, a `1-10^{-12}` confidence conclusion is still not a deterministic endpoint. Hashing the trials does not change that logical status.

### #10 DERANDOMIZE: exact beam expectation

The natural derandomization is to count all input prefixes through the beam policy with exact integer multiplicities. The obstruction is that the beam state's frontier coordinates alone are not a finite Markov state for the random-input law after adaptive `next-0` / `next-1` scans: different frontier states reveal overlapping, variable-length pieces of the two strings, and future transition probabilities depend on which bits have already been exposed. A valid finite abstraction therefore needs either a proved regeneration rule, an exact finite revealed-context quotient, or a pessimistic truncation whose lost mass/reward is rigorously controlled. I did not obtain such a closed exact abstraction this run.

### #7 TAKE THE LIMIT: finite-lookahead MDP

A separate public `markov_decision_subadditivity` implementation initially looked like an independent route. Reading its recurrence and output shows that its lookahead-8, 9, and 10 values reproduce the published Kiwi--Soto/Heineman finite-lookahead lower-bound values to the displayed precision. Thus it is not a new mechanism. Heineman et al. already execute the exact feasible-triplet recurrence through lookahead `ell=21`, producing the retained `0.792665992` lower bound. Their state vector has size `2^(2 ell)`, so the naive next case `ell=22` has `2^44` state entries before exploiting structure. Continuing with an explicit dense state table is therefore the wrong category of computation.

### Particle/TASEP analogy

Tiskin's particle-process approximation is useful conceptual evidence but not an exact replacement for binary LCS. The revised arXiv version explicitly removes earlier incorrect claims and treats the particle model as an approximation/local fit; no stochastic domination or exact coupling presently transfers its asymptotic speed into a deterministic endpoint for the true dependent binary match array. This route cannot be used as a bound without a new comparison theorem.

## 4. (c) What a proof must contain that no tried route currently contains

A successful lower-bound recovery needs **all three** of the following at once:

1. an exact finite or finitely represented state object for the true iid binary-input process, not an independent-match surrogate and not a sampled approximation;
2. an exact rational Bellman / potential / occupancy certificate whose validity can be checked statewise or symbolically with no floating-point inequality in the theorem step; and
3. a finite-to-infinite argument preserving the exact normalization and producing a number strictly greater than `0.792665992`.

The upper-bound side analogously needs a new exact compression of seven-factor state-dependent obstruction information, not merely another enumeration of already-known six-factor patterns.

The recurring missing ingredient on both sides is **exact structured state compression**: the existing proofs know what inequality to check, but not how to represent the next-scale state space compactly enough while preserving every inequality.

## 5. (d) Simplest special case still unproved

The cleanest next special case is:

> **Binary lookahead `ell=22`: produce one exact rational Bellman/feasible-triplet certificate, represented symbolically rather than as a full `2^44` dense table, that certifies a lower bound strictly greater than `0.792665992`.**

This is deliberately narrower than “derandomize the width-100 beam” and narrower than determining `gamma_2`. It has the correct model, a known exact recurrence, a known finite-to-infinite transfer, a single quantitative pass/fail criterion, and a finite certificate target. A certificate below or equal to the present lower endpoint would be mathematically valid but would not move R17's fixed metric.

## 6. (e) Nearest solved problem and what it has that we lack

The nearest solved construction is exactly the Kiwi--Soto / Heineman feasible-triplet lower-bound computation through `ell=21`. Heineman et al. publish the increasing exact lower-bound sequence through lookahead 21 and obtain `0.792665992`. Their method has two features the current recovery lacks:

- an exact finite state table on which every recurrence step is explicit; and
- a directly checkable finite calculation whose output has a proved transfer to `gamma_2`.

What fails at the next scale is representation size, not the underlying recurrence. This makes symbolic probabilistic model checking / factored-MDP dynamic programming the closest useful external technique: BDD/MTBDD and algebraic-decision-diagram methods were designed precisely to carry exact transition and value-function operations over very large structured finite-state systems without enumerating every state explicitly. That literature does **not** solve the LCS problem for us; it supplies a representation technology that the nearest solved LCS method currently lacks.

## 7. Method #21 — external technique worth porting

I checked symbolic-MDP/model-checking work rather than another LCS transfer matrix. PRISM's symbolic engines use decision diagrams for structured probabilistic transition systems, and exact/factored MDP work with algebraic decision diagrams shows that Bellman-style dynamic programming can sometimes be performed on state spaces far larger than an explicit table. The relevant lesson is not a claimed complexity bound for this LCS recurrence. It is that the `ell=22` feasible-triplet map should first be expressed as Boolean-variable transition/reward formulas and tested for exact ADD/MTBDD closure before abandoning the finite-lookahead line as computationally impossible.

The promising representation is a reduced decision diagram for the **Bellman residual/potential**, not a diagram for a floating approximate policy. Exact terminal values should be rationals/integers after clearing denominators. Verification should recursively prove the Bellman inequality on whole Boolean subcubes represented by shared nodes. A final certificate can be a compact node table plus a small exact checker that evaluates every reduced node relation symbolically.

## 8. The one recovery action selected

Per the stuck protocol I choose exactly one action:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED CASE.}}
\]

Specifically: keep the exact `ell=22` Kiwi--Soto/Heineman feasible-triplet recurrence, but port symbolic BDD/MTBDD/ADD representation from exact probabilistic model checking / factored MDPs. The next run should not build another six-factor transfer checker, should not use Monte Carlo as an endpoint, and should not treat the TASEP approximation as the binary model.

The first success criterion is brutally simple: an exact symbolic rational certificate for some `beta > 0.792665992`. If symbolic reduction does not compress the relevant Bellman residual enough to verify, record the obstruction and use the second allowed hard recovery rather than reverting to checker churn.

## 9. Current literature / prior-art search

Fresh dated searches in this run included variants of:

- `Chvatal Sankoff gamma_2 2026 new bound`;
- `0.792665992 longest common subsequence 2026`;
- `Heineman Soiffer binary LCS constant 2026`;
- `Tiskin arXiv:2212.01582 revised binary coefficient unresolved`;
- `symbolic MDP MTBDD Bellman algebraic decision diagram exact dynamic programming`.

The exact binary constant remains open in the current sources checked. Tiskin's revised paper still describes the coefficient as unresolved and explicitly retracts incorrect claims from v1. Heineman et al. remain the source of the deterministic `0.792665992` lower bound and explicitly describe exact Chvátal--Sankoff constants as open. Li--Ren--Wen, published online 2 March 2026, still summarize the public rigorous binary interval at approximately `0.792665 <= gamma <= 0.826280`. I found no later deterministic public endpoint that supersedes the retained lower bound. A negative search is not a priority certificate for R17's candidate upper endpoint.

I also checked the public 2026 Archivara repository rather than treating its headline number as a theorem. Its width-100 beam computation is Monte Carlo, while its separate finite-lookahead MDP code produces the already-known lookahead values at 8, 9, and 10. Thus neither supplies a new deterministic endpoint here.

## 10. Status, recovery count, and next methods

No deterministic endpoint moved:
\[
\boxed{0.792665992\le\gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]
Status: **PARTIAL**. Source status: **OPEN**.

The consecutive no-movement count advances `2 -> 3`, triggering this first hard recovery. Hard-recovery count is now **1/2** on this source. This is not a rotation run. If the selected symbolic-certificate route fails to move the metric through the second allowed recovery, the following stuck event must leave a handoff and rotate to a newly eligible outside target after current source/status/ownership admission; `PENDING` is not `READY`.

The next Section-B triple is deliberately different from `[10,7,21]` and `[19,25,27]`:

- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the `ell=22` feasible-triplet recurrence as a Boolean factored average-reward MDP suitable for exact decision diagrams;
- **#11 DUALIZE:** formulate the lower certificate equivalently as an exact Bellman potential / occupancy-measure dual so either side can yield a compact witness;
- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** certify one rational `beta > 0.792665992`, not the optimal `ell=22` value, if that permits a much smaller symbolic witness.

No new finite checker is archived in this thinking-only recovery, intentionally: no finite numerical claim from the exploratory routes is promoted to a theorem or endpoint.

## 11. Model/scheduler control and the historical P26 denial

The control limitation is still true. The exposed scheduling interface provides title, prompt, schedule/relative-start, timing mode, and enablement controls, but no bindable model-family field, reasoning-effort field, or authenticated runtime-effort telemetry. Therefore `GPT-6 / maximum` remains prompt text only in this context. Enforcing it would require an authorized product/workspace/API surface that exposes those controls, plus runtime metadata sufficient to verify what actually ran, or a platform-side change.

The historical P26 `You cannot modify this task` failure was context/ownership-specific. Root `RESULTS.md` records that a later P26 update succeeded from an authorized P/C context. For any task still refusing modification, the legitimate workaround is the task's owning authorized context or platform support, not a permission bypass and not a duplicate schedule. No scheduler modification is attempted here.

No email, Drive operation, public posting, purchase, permission change, workflow execution, shared-root edit, or peer-file edit was performed.

```yaml
ledger_delta:
  track: R17
  lane: HARD_OUTSIDE
  source: "Chvatal and Sankoff (1975), binary longest-common-subsequence constant"
  target: "determine gamma_2 for two independent iid uniform binary strings"
  metric: "width U-L of deterministically rigorously certified interval for gamma_2"
  lower_before: 0.792665992
  lower_after: 0.792665992
  upper_before: 0.826275942762282626
  upper_after: 0.826275942762282626
  width_before: 0.033609950762282626
  width_after: 0.033609950762282626
  movement: "none"
  status: PARTIAL
  source_status: OPEN
  no_movement_before: 2
  no_movement_after: 3
  stuck: true
  hard_recovery_before: 0
  hard_recovery_after: 1
  methods: [10, 7, 21]
  selected_recovery_action: "port the nearest-solved finite-lookahead technique into an exact symbolic BDD/MTBDD/ADD Bellman certificate at ell=22"
  simplest_unproved_special_case: "exact symbolic ell=22 certificate for a rational beta > 0.792665992"
  next_methods: [18, 11, 4]
```
