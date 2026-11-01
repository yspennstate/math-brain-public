Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0034: `N_rep: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. SECTION-I STUCK-RECOVERY-2/2. Methods actually used: #4 PROVE SOMETHING WEAKER COMPLETELY, #13 FIND WHAT ONLY INCREASES, #30 DO ONE SCALE, ONE DIRECTION AT A TIME.

# R14 HARD OUTSIDE — D0034 Bradley Question 6 — stuck recovery 2/2

## 1. Continuity, source, ownership, exclusions

I continued the newest repository state rather than the stale task title. The original negative-margin spherical-perceptron target, H0017, D0036, and D0039 were already terminally handed off by prior R14 reports. The current exclusive R14 HARD OUTSIDE claim is `operations/claims/D0034.md`: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions* (Probability Surveys 2, 2005), Question 6, asking whether there exists a strictly stationary psi-mixing — perhaps even 1-dependent — sequence that is not an instantaneous function of any strictly stationary Harris recurrent Markov chain.

The fixed source-closing candidate remains the stationary 1-dependent proper 4-coloring `X_HL` of Holroyd--Liggett, *Finitely dependent coloring*, Forum Math. Pi 4 (2016), arXiv:1403.2448. Holroyd--Liggett prove that no stationary finitely dependent proper coloring is a function of a **finite-state** Markov chain and explicitly state that the countable-state case remains open. Holroyd--Hutchcroft--Levy, *Mallows Permutations and Finite Dependence*, Ann. Probab. 48 (2020), arXiv:1706.09526, later construct other finitely dependent colorings that **are** functions of countable-state Markov chains, so a cardinality-free extension of the finite-state argument cannot hold for finitely dependent colorings in general.

The frozen metric is

`N_rep = number of hidden-state cardinality regimes still requiring exclusion for X_HL after the known finite-state impossibility`.

The two surviving regimes remain:

1. irreducible positive recurrent countable-state stationary Markov representations;
2. genuinely general stationary Harris recurrent representations.

Therefore the certified metric is still `N_rep=2`.

I reread `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical D0034 claim, the newest R14 D0034 report, and neighboring D0034/finite-dependence reports. No posted exclusion or ownership conflict supersedes the R14 claim.

### Fresh literature check, 2026-09-18 UTC

Queries included:

- `Bradley Question 6 psi-mixing Harris recurrent Markov chain instantaneous function 1-dependent`;
- `Holroyd Liggett finitely dependent coloring countable state Markov chain remains open 1-dependent 4-coloring`;
- `Holroyd Hutchcroft Levy countable state Markov chain finitely dependent coloring`.

Primary/currently relevant hits inspected:

- Bradley 2005 survey, Question 6;
- Holroyd--Liggett, arXiv:1403.2448 / Forum Math. Pi 4 (2016), especially Proposition 3, Theorem 4, and Open Problem (ii);
- Holroyd--Hutchcroft--Levy, arXiv:1706.09526 / Ann. Probab. 48 (2020).

The bounded search did not surface a later paper deciding whether the Holroyd--Liggett 4-coloring is a countable-state Markov factor or closing Bradley Question 6. This is bounded negative search evidence, **not** a worldwide novelty certificate.

## 2. What recovery 1 left to do

The previous report selected exactly one Section-I action: prove the simplest unproved special case `FINITE-PAIR-HL`.

For an unordered color pair `{a,b}`, let

`S_ab = {s : f(s) in {a,b}}`

inside a hypothetical countable hidden chain `Y` with output `X_n=f(Y_n)`. The selected special case was:

> Exclude a positive recurrent countable hidden representation in which, for at least one color pair, only finitely many hidden states can participate in positive-probability paths whose outputs stay in that pair.

This run closes that special case, and in fact proves a stronger structural statement. It does **not** eliminate the entire countable-state regime, so the fixed metric does not move.

## 3. Method #4 — complete theorem: every hidden two-color graph is a DAG

### Theorem 1 (pair-DAG obstruction)

Let `X=X_HL` be the Holroyd--Liggett stationary 1-dependent proper 4-coloring. Suppose

`X_n = f(Y_n)`

in law for a stationary irreducible positive recurrent countable-state Markov chain `Y` with transition matrix `P` and stationary distribution `pi`. Fix any unordered color pair `{a,b}`. Form the directed graph on

`S_ab = f^{-1}({a,b})`

with an edge `s -> t` exactly when `P(s,t)>0`. Then this directed graph contains **no directed cycle**.

Consequently:

1. every positive-probability hidden path whose outputs remain in `{a,b}` is self-avoiding;
2. `S_ab` is infinite for every color pair;
3. `FINITE-PAIR-HL` is impossible, so the special case chosen in recovery 1 is fully closed.

### Proof

Because `Y` is irreducible and positive recurrent on a countable state space, every state has `pi(s)>0`.

Since `X` is a proper coloring, adjacent outputs are unequal almost surely. Hence if `P(s,t)>0`, then necessarily

`f(s) != f(t)`.

Indeed, otherwise the stationary event `(Y_0,Y_1)=(s,t)` has probability `pi(s)P(s,t)>0` and would produce `X_0=X_1` with positive probability.

Assume for contradiction that the induced graph on `S_ab` has a directed cycle

`s_0 -> s_1 -> ... -> s_{ell-1} -> s_0`

with all transition probabilities positive. Because every transition changes the output color and only `a,b` occur on the cycle, the colors along the cycle alternate and `ell` is even. Put

`r = product_{j=0}^{ell-1} P(s_j,s_{j+1}) > 0`,

where `s_ell=s_0`.

For every integer `k>=1`, the stationary hidden path that starts at `s_0` and follows this cycle exactly `k` times has probability

`pi(s_0) r^k`.

Its observed word has length `k ell + 1` and is one fixed alternating word on the two colors `{a,b}`.

Holroyd--Liggett's exact cylinder law is

`P(X_1...X_n=x) = B(x)/((n+1)! 2^n)`

for proper 4-color words `x`, where `B(x)` is the number of proper buildings. For an alternating two-color word, the building recursion gives `B(x)=2^{n-1}`. Equivalently, Theorem 4(iii) identifies membership in any fixed two-color set with the descent process `1[U_i>U_{i+1}]`, so a pair-run of length `n` has probability `1/(n+1)!`, split equally between the two possible alternating starting colors. Therefore each fixed alternating two-color word of length `n` has probability

`1/(2(n+1)!)`.

Taking `n=k ell+1`, the hidden cycle event is a subset of that observed cylinder, hence

`pi(s_0) r^k <= 1/(2(k ell+2)!)`.

But for every fixed `r>0` and `ell>=2`,

`(k ell+2)! r^k -> infinity`.

Thus the displayed inequality fails for all sufficiently large `k`, a contradiction. No directed two-color cycle exists.

If a positive-probability pair-only hidden path revisited a state, the segment between two visits would be a directed cycle in `S_ab`; hence every pair-only path is self-avoiding.

Finally, every alternating two-color observed word has strictly positive Holroyd--Liggett probability for every length. Therefore for each length `n` there is at least one positive-probability hidden pair-only path of `n-1` transitions. A finite directed acyclic graph has bounded path length, so `S_ab` must be infinite. This excludes the `FINITE-PAIR-HL` special case. QED.

### Status / novelty discipline

The proof is new within this track. I did not find this exact pair-DAG formulation in the bounded search. That is **not** a novelty certificate; it may be folklore or implicit in existing hidden-Markov discussions.

## 4. Method #13 — the monovariant exists, but it does not yield recurrence contradiction

The theorem supplies the natural monovariant that recovery 1 was seeking: along a hidden path that stays in one fixed output pair, the number of distinct pair states visited increases by one at every step. Equivalently, the path escapes every fixed finite subset of `S_ab`.

The tempting next inference was:

> factorial pair-cylinder decay + pair-state escape + positive recurrence should contradict stationary tightness.

That inference is **false for one pair**. The reason is that conditioning on a rare long pair-run can move the hidden state through a sequence of smaller and smaller stationary-mass states while the unconditioned chain remains positive recurrent.

The following explicit model certifies the obstruction.

### Proposition 2 (positive recurrence can coexist with factorial pair escape)

There is an irreducible positive recurrent countable-state Markov chain with a proper finite-color output such that, for the output pair `{0,1}`:

- the induced hidden pair graph is a one-way DAG;
- arbitrarily long `{0,1}`-only alternating output runs occur;
- the stationary probability of a fixed alternating pair word decays on the factorial scale `Theta(1/(n+1)!)`.

### Construction and proof

Take states

`C, D, U_1, U_2, ...`.

Transitions are

- `C -> D` with probability `1/2`;
- `C -> U_1` with probability `1/2`;
- `D -> C` with probability `1`;
- for `k>=1`, `U_k -> U_{k+1}` with probability `1/(k+2)`;
- for `k>=1`, `U_k -> C` with probability `(k+1)/(k+2)`.

Give the states colors

- `f(C)=2`;
- `f(D)=3`;
- `f(U_k)=0` for odd `k`, and `f(U_k)=1` for even `k`.

Every permitted transition changes color, so the output is proper. The chain is irreducible: every `U_k` can return to `C` with positive probability; from `C`, one can reach `D` and every `U_k`.

Conditional on entering `U_1`, the probability of reaching `U_k` is

`product_{j=1}^{k-1} 1/(j+2) = 2/(k+1)!`.

Hence the expected number of ladder states visited in one ladder excursion is

`sum_{k>=1} 2/(k+1)! = 2(e-2) < infinity`.

Return time to `C` therefore has finite mean, so irreducibility implies positive recurrence.

The stationary equations give

`pi(D)=pi(C)/2`,

`pi(U_k)=pi(C)/(k+1)!`,

and normalization gives

`pi(C)=1/(e-1/2)=2/(2e-1)`.

The pair `{0,1}` lives only on the one-way ladder `U_1 -> U_2 -> ...`, so its induced hidden graph is acyclic.

For a fixed alternating pair word of length `n` starting with color 0, the possible hidden starting states are odd `U_k`. Starting from `U_k`, remaining in the pair for `n` sites has probability

`product_{j=k}^{k+n-2} 1/(j+2) = (k+1)!/(k+n)!`.

Multiplying by `pi(U_k)` and summing over odd `k=2j+1` yields

`P(f(Y_1)...f(Y_n)=0101...)=pi(C) sum_{j>=0} 1/(n+1+2j)!`.

Thus

`pi(C)/(n+1)! <= P(0101...) <= C_0/(n+1)!`

for a finite constant `C_0`, proving factorial decay while the chain remains positive recurrent. QED.

This model is **not** claimed to reproduce `X_HL` or to be 1-dependent. Its role is narrower and rigorous: it disproves the one-pair argument that positive recurrence/tightness alone forbids factorial escape down a countable DAG.

Therefore any successful continuation must use additional structure absent from the toy model — at least the simultaneous six-pair constraints, the exact 1-dependence identities, or the full Holroyd--Liggett building law.

## 5. Method #30 — one pair is now understood; gluing is the actual obstruction

Localizing to one unordered pair produces a complete picture:

1. exact Holroyd--Liggett pair cylinders are factorial;
2. every hypothetical countable hidden pair graph must be a DAG;
3. pair-conditioned paths must escape every finite hidden set;
4. none of (1)--(3), even together with positive recurrence, is enough for a contradiction.

So the failure-to-glue is now the mathematical obstruction, not an unspecified need for “more tightness.” A source-closing countable-state proof must exploit compatibility of **all six** pair-DAGs with one common stationary transition matrix and the exact lag-two independence of the four-color output.

The exact countable-state source obligation remains

`COUNTABLE-HL: X_HL is not an instantaneous factor of any stationary irreducible positive recurrent countable-state Markov chain.`

The general Harris regime remains separate.

## 6. A sharper handoff criterion for the countable regime

The strongest next route I can isolate without pretending it is proved for `X_HL` is a two-sided product-minorant criterion.

Let

`L=(X_i)_{i<=-1}`, `R=(X_i)_{i>=1}`.

Because `X_HL` is 1-dependent, `L` and `R` are independent. Let their laws be `mu_-` and `mu_+`. For a color `a`, define the subprobability measure

`nu_a(dL,dR)=P(L in dL, X_0=a, R in dR)`

and the conditional center kernel

`K_a = d nu_a / d(mu_- x mu_+)`,

which satisfies `0<=K_a<=1`.

### Lemma 3 (countable hidden state forces a positive product rectangle)

If `X_HL` has a stationary countable-state Markov representation, then for every color that occurs with positive probability there exist measurable `A,B` of positive `mu_-`, `mu_+` measure and `epsilon>0` such that

`K_a(L,R) >= epsilon`

for `(mu_- x mu_+)`-almost every `(L,R) in A x B`.

#### Proof

Write the hidden state space as `S` and choose any `s` with `f(s)=a` and stationary mass `pi_s>0`. By the Markov property, the observed past and future are conditionally independent given `Y_0=s`; write their conditional laws as `alpha_s` and `beta_s`. Therefore

`nu_a = sum_{t:f(t)=a} pi_t alpha_t x beta_t`

as measures on the product half-line space. In particular,

`pi_s alpha_s x beta_s <= nu_a <= mu_- x mu_+`.

Hence `alpha_s << mu_-` and `beta_s << mu_+`; let their Radon--Nikodym densities be `u_s` and `v_s`. Then

`K_a >= pi_s u_s v_s`

almost everywhere. Since both densities integrate to one, there are positive constants `delta_-,delta_+` for which

`A={u_s>=delta_-}`, `B={v_s>=delta_+}`

have positive marginal measure. On `A x B`,

`K_a >= pi_s delta_- delta_+ >0`.

QED.

Thus the countable-state regime would be eliminated by the following purely observable theorem:

`NO-RECTANGLE-HL: for every color a, every positive-measure A,B and every epsilon>0, K_a<epsilon on a positive-measure subset of A x B.`

This is a **handoff target**, not a proved property of `X_HL`.

For finite side words `x` of length `m`, `y` of length `n`, the exact finite conditional kernel is available from the building formula:

`K_a^{m,n}(x,y)
 = ((m+1)!(n+1)!)/(2(m+n+2)!) * B(x a y)/(B(x)B(y))`,

whenever `B(x)B(y)>0`. The kernels form the natural finite-window martingale converging to `K_a`. A future attack should try to prove `NO-RECTANGLE-HL` directly from these exact ratios, rather than seek another pair-cycle lemma.

## 7. What was tried and why the routes now stand where they do

The current D0034 route map is:

- **finite-state trace/Hilbert argument:** solved in Holroyd--Liggett, but finite dimensionality is essential;
- **Harris -> countable collapse by Nummelin splitting:** retracted; `m`-step splitting can leave adjacent regenerative blocks 1-dependent;
- **observable one-color renewal as hidden regeneration:** false; neighboring side colors retain dependence;
- **finite-window / product-minorant obstruction:** local radius-one nonnegative rank is too small to obstruct; infinite-scale version remains plausible;
- **Berbee complete-connections port:** structural zero transitions block direct use of the standard positivity hypothesis;
- **reversible hidden chain:** excluded by the exact skew/orthogonality bound, but hidden irreversibility can survive reversible output;
- **critical limit of HHL's countable-state construction:** its positive-density bubble mechanism degenerates at `q=4`, but this only kills that construction;
- **pair cycle / tightness route:** this run proves the pair-DAG theorem, then the factorial-ladder example certifies that one-pair escape plus positive recurrence is insufficient.

A proof that moves `N_rep` must now contain a genuinely global four-color ingredient. The cleanest current candidate is `NO-RECTANGLE-HL` or another theorem that couples all six pair-DAGs through the exact 1-dependence identities.

## 8. Section-I decision

This is **stuck recovery 2/2** on D0034. The selected recovery choice from the prior report — prove the simplest unproved special case — succeeded at the special-case level (`FINITE-PAIR-HL` is closed and strengthened to pair-DAG), but it did not move the fixed source metric `N_rep`.

Under the owner's hard-task rule, R14 has no third D0034 recovery available. If no independent external development moves `N_rep` before the next invocation, the next R14 run must:

1. write a terminal D0034 handoff preserving `PAIR-DAG-HL`, the factorial-ladder obstruction, and `NO-RECTANGLE-HL` as the sharp countable-state frontier;
2. rotate to an ownership-clear eligible HARD OUTSIDE target;
3. not manufacture another D0034 auxiliary lemma.

## 9. Model / scheduler capability check

The exposed scheduler state was checked in this run. It still exposes task prompt/title/schedule/timing/enabled/notification metadata but no binding model-family selector, no reasoning-effort selector, no guaranteed execution-duration control, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains a request in prompt text only; the actual model for this report is GPT-5.6 Sol and reasoning is reported as UNVERIFIED.

The repository policy still records native modification probes for P26/P01/P03 returning `You cannot modify this task`. The legitimate remedy is to use the authorized owning/admin account or workspace context, or platform support. A repository edit, duplicate task, or permission bypass is not a scheduler repair. No scheduler state was changed in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD OUTSIDE
  active_target:
    id: D0034
    source: "Bradley 2005, Basic Properties of Strong Mixing Conditions, Question 6"
    candidate: "Holroyd--Liggett stationary 1-dependent 4-coloring"
    status: "PARTIAL / OPEN"
  metric:
    name: N_rep
    definition: "hidden-state cardinality regimes still requiring exclusion after known finite-state impossibility"
    before: 2
    after: 2
    movement: "NO FIXED-METRIC MOVEMENT"
  authoritative_shared_stagnation_count: UNKNOWN
  section_I:
    recovery: "2/2"
    selected_action: "prove the simplest unproved special case"
    special_case: FINITE-PAIR-HL
    special_case_status: PROVED
    source_metric_status: OPEN
    next_if_no_external_movement: "TERMINAL HANDOFF AND ROTATION"
  methods:
    - 4
    - 13
    - 30
  proved_this_run:
    - "PAIR-DAG-HL: every two-color induced positive-transition graph in a countable positive recurrent hidden representation is acyclic"
    - "every pair-only hidden path is self-avoiding and every color-pair hidden fiber is infinite"
    - "FINITE-PAIR-HL is impossible"
    - "explicit positive recurrent factorial-ladder countermodel showing one-pair factorial escape does not contradict positive recurrence"
    - "countable hidden representation implies a positive product rectangle for the two-sided conditional center kernel"
  not_proved:
    - COUNTABLE-HL
    - HARRIS-HL
    - NO-RECTANGLE-HL
    - "Bradley Question 6"
  metric_regimes_remaining:
    - "countably infinite-state positive recurrent Markov"
    - "general Harris recurrent"
  handoff_frontier:
    primary: NO-RECTANGLE-HL
    structural_input: "simultaneous six pair-DAGs + exact 1-dependence/building law"
    warning: "one-pair escape/tightness alone is certified insufficient"
  literature_check:
    date_utc: "2026-09-18"
    scope: "bounded web + primary-source check"
    novelty_certificate: false
  artifacts_created: []
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
```
