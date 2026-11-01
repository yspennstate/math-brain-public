Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED-METRIC MOVEMENT: `ROMERO-2025-SPLIT8` has `R_SPLIT8: 0 -> 0`; closure audit gate `0/2 -> 1/2`; frozen I0056/H_{5,5} width `0 -> 0`; methods #1 CHANGE THE CATEGORY, #3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R06 — Romero split reliability: an analytic max-density-minus-two theorem while the n=8 audit gate advances

Run date: 2026-09-19.
Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Continuity and the frozen metric

I continued from the newest own immutable report

`runs/R06/20260919T0631Z_romero_split8_full_layer_candidate_complete_59_f3c9.md`

at creation commit

`26c39052586e085df399b4c21ecbc465c655e03a`.

That report completed the exact claimed finite layer

`n=8, m=14,...,26`

and moved the fixed metric

`R_SPLIT8: 7 -> 0`.

The layer is therefore **candidate-complete mathematically**, but the fleet closure gate was `0/2` independent OTHER-task audits at that report. This run does not redefine the metric merely because a stronger source-level observation became available.

The original R06/I0056 predecessor remains frozen:

`Phi_V(H_{5,5}) = sqrt(5)`, with certified interval `[sqrt(5),sqrt(5)]` and width `0`, under the outer-vertex-boundary normalization. The full Lyons--Peres Question 6.20 remains PARTIAL. Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art for triangular/quadrangular cases and are not relabelled as new.

## 2. Required repository continuation and audit delta

Before new mathematics I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the active claim `operations/claims/ROMERO-2025-SPLIT8.md`;
- the newest own R06 report;
- current neighboring/support evidence involving this exact claim.

The exact repository comparison from the preceding R06 creation commit `26c39052586e085df399b4c21ecbc465c655e03a` to observed head `6674040af9f268a9ac214bb7352243629068a0de` was **113 commits ahead / 0 behind / complete (`too_large=null`)**.

The mathematically relevant change is the first genuinely independent audit:

`P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED_N8 / EXACT_FINITE_CORE_PASS / SOURCE_PARTIAL_OPEN / PRIOR_ART_BOUNDED_NEGATIVE / PENDING_SECOND_DISTINCT_AUDIT`.

P26 independently checked the six `m=14,...,19` determinant inequalities, the connected-subgraph recurrence, the orbit completeness using an orthogonal Burnside calculation, and direct labeled coefficientwise domination for all `m=25,26` graphs. It correctly records that this supplies only **one** independent auditor.

Repository-wide searches for `ROMERO-SPLIT8 second audit` and the exact claim ID still find no distinct second OTHER-task full-proof audit. Thus the closure gate moves

`0/2 -> 1/2`,

while the fixed mathematical metric remains

`R_SPLIT8: 0 -> 0`.

I do **not** count this R06 run, another R06 proof, or repeated P26 work as the missing second auditor.

## 3. Fresh source and prior-art check

Primary source rechecked on **2026-09-19**:

Pablo Romero, *Characterization of locally most split reliable graphs*, Theoretical Computer Science 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv `2503.15453`.

Its current abstract still states that Brown--McMullin left the simple-graph existence/nonexistence problem open outside their finite/special cases; Romero characterizes local optima and proves nonexistence only through

`n >= 7, n <= m <= binom(n-3,2)+3`.

Hence the source-unresolved upper band includes

`m = binom(n,2)-2`.

I also re-read Brown--McMullin, *On the split reliability of graphs*, Networks 82 (2023), 177--185, DOI `10.1002/net.22166`. Its global nonexistence theorem concerns the broader graph/multigraph setting, but Section 3 explicitly separates **simple graphs**, records the small-order computations, notes the obvious simple cases `m=n-1`, `m=binom(n,2)`, and `m=binom(n,2)-1`, and leaves the other simple-graph cases open. This distinction prevents the misleading conclusion that the 2023 multigraph theorem already settles Romero's simple class.

Fresh bounded queries included:

- `"uniformly most split reliable" "binom(n,2)-2"`;
- `"split reliability" "Kelmans" graph`;
- exact Romero title / arXiv ID / 2026 follow-up searches;
- `"all-terminal reliability" Kelmans transformation compression Satyanarayana Suffel`;
- `"split reliability" complete graph two edges`.

They recovered Romero 2025, Brown--McMullin 2023, later reliability-root work using split reliability in a different role, and classical all-terminal reliability transformations, but no later primary source stating the theorem proved below. One current bibliographic index reports zero citations to Romero's exact 2025 article. These are **bounded negative searches only**. Priority/novelty for the theorem below remains **UNVERIFIED**.

The crucial old theorem recovered by method #21 is:

A. Satyanarayana, L. Schoppmann, C. L. Suffel, *A reliability-improving graph transformation with applications to network reliability*, Networks 22 (1992), 209--216, DOI `10.1002/net.3230220206`.

Their published abstract states: if `H` is obtained by deleting `r` independent edges from a complete graph, then for every other graph `G` with the same numbers of vertices and edges,

`Rel(H,p) > Rel(G,p)` for every `0<p<1`,

where `Rel` is all-terminal reliability. I use only the `r=2` instance.

## 4. Negation-first structural screen

Before trying to prove a general statement, I classified what a counterexample to the densest still-open diagonal could look like.

Fix terminals `s,t` and let

`M = binom(n,2)`, `m=M-2`.

Every candidate is `K_n` with two missing edges, but the terminal edge `st` need not itself be missing. There are therefore two logical fronts:

1. `st` is present;
2. `st` is missing, in which case the one other missing edge is either incident with a terminal or joins two nonterminals.

The first front can be reduced monotonically to the second by an exact coupling lemma below. The second front has only two terminal-isomorphism types. Thus there is no hidden large finite universe at this density: the full source class reduces exactly to two canonical types plus a monotone edge swap.

This counterexample screen is structural, not sampled numerics.

## 5. Method #1 — CHANGE THE CATEGORY: a bridge from split reliability to all-terminal reliability

Write `Rel_X(p)` for all-terminal reliability of a graph `X`, and `SR_X^{s,t}(p)` for split reliability with terminals `s,t`.

### Lemma 1 (terminal-edge bridge)

If `st` is not an edge of `X`, then

`Rel_{X+st}(p) = Rel_X(p) + p SR_X^{s,t}(p)`.

### Proof

Expose the random operational subgraph of `X` first.

- If it is connected, `X+st` is connected regardless of the state of the new edge.
- If it has exactly two components, one containing `s` and the other `t`, then the new graph is connected exactly when `st` is operational, which has probability `p`.
- In every other disconnected state, adding the single edge `st` cannot produce a connected spanning graph.

The three cases are disjoint and exhaustive, proving the identity. `square`

This converts a split-reliability comparison into a difference of two classical all-terminal reliabilities.

## 6. A terminal-edge deletion swap that never hurts split reliability

### Lemma 2 (force the terminal edge to be absent)

Let `G` be a simple two-terminal graph with `st in E(G)`, and let `e` be any missing edge. Put

`G' = G - st + e`.

Then

`SR_{G'}^{s,t}(p) >= SR_G^{s,t}(p)` for every `p in [0,1]`.

### Proof

Let

`H = G-st = G'-e`,

and couple all random edge states in `H` identically.

Condition on one fixed operational state `F` of `H`. In `G`, a split-success state is possible only if `st` fails. Moreover, when `st` fails, success occurs exactly when `F` already has exactly two components separating `s` and `t`. Thus the conditional success probability for `G` is

`(1-p) * 1_{F is an (s,t)-split}`.

Now consider `G'`. If `F` is such a split, then:

- when the endpoints of `e` lie in the same split component, either state of `e` preserves the split, so the conditional success probability is `1`;
- when `e` crosses the two split components, success occurs exactly when `e` fails, so the conditional success probability is `1-p`.

In either case the conditional success probability of `G'` is at least that of `G`. If `F` is not already such a split, `G` contributes zero while `G'` contributes a nonnegative amount. Averaging over `F` proves the inequality. `square`

For `m=M-2`, choosing either missing edge as `e` converts any candidate with `st` present into a candidate with `st` missing without decreasing split reliability.

## 7. Method #3 + #21 — PROVE SOMETHING STRONGER by importing the exact old all-terminal extremal theorem

After Lemma 2, assume `st` is missing. Since there is exactly one other missing edge, up to relabeling nonterminals and interchanging the terminals there are only two cases:

`A_n = K_n - {st, su}`,

where `u` is a nonterminal, and

`B_n = K_n - {st, uv}`,

where `u,v` are distinct nonterminals.

The graph `A_n` is precisely the diameter-terminal balloon in this dense class: the two missing edges share the terminal `s`, so `d(s,t)=2`.

Adding `st` gives

`A_n + st = K_n - su`,

`B_n + st = K_n - uv`.

These two graphs are isomorphic. Hence by Lemma 1,

`Rel(A_n,p) + p SR_{A_n}(p) = Rel(B_n,p) + p SR_{B_n}(p)`,

so for `p>0`,

`p [SR_{A_n}(p)-SR_{B_n}(p)] = Rel(B_n,p)-Rel(A_n,p)`.     (1)

Now `B_n` is obtained from `K_n` by deleting the two **independent** edges `st` and `uv`, whereas `A_n` deletes two adjacent edges. The `r=2` case of Satyanarayana--Schoppmann--Suffel therefore gives

`Rel(B_n,p) > Rel(A_n,p)` for every `0<p<1`.

Substitution in (1) yields

`SR_{A_n}(p) > SR_{B_n}(p)` for every `0<p<1`.

At `p=0` and `p=1` both split reliabilities are zero for connected graphs of order at least three, so the weak inequality holds on the closed interval.

Combining this strict two-type comparison with Lemma 2 proves the following theorem.

### Theorem (dense max-minus-two diagonal)

For every `n>=4`, let `M=binom(n,2)`. In the class of connected simple two-terminal graphs `T_{n,M-2}`, the graph

`A_n = K_n - {st,su}`

with terminals `s,t` is uniformly most split reliable:

`SR_{A_n}(p) >= SR_G(p)`

for every `G in T_{n,M-2}` and every `p in [0,1]`.

Moreover `A_n` strictly beats the other terminal-missing type `B_n=K_n-{st,uv}` for every `0<p<1`.

### Source-scope consequence

Brown--McMullin already cover the small orders through `n<=7`. The source-level new content, if the bounded priority search is complete, starts at **every `n>=8`** and decides the entire upper diagonal

`m = binom(n,2)-2`

inside Romero's explicitly unresolved simple-graph range.

This is an **auxiliary source extension** discovered while strengthening the already solved `n=8,m=26` case. I do not silently enlarge the canonical `ROMERO-2025-SPLIT8` claim, and I do not change its fixed metric. The theorem itself is currently a self-proof with priority unverified and no independent audit directed specifically at the all-`n` extension.

## 8. Relation to the existing exact n=8 certificate

The previous exact finite checker proved coefficientwise domination of the balloon for every `m=20,...,26` in the `n=8` layer. In particular it covered `m=26=M-2` by exhaustive terminal-preserving orbit enumeration.

The theorem above gives a completely different analytic proof of that `m=26` case and explains its mechanism:

- first force `st` into the complement by a monotone split-reliability swap;
- then use the terminal-edge bridge to turn the only nontrivial comparison into an all-terminal reliability comparison;
- finally use the classical theorem that deleting two independent edges from `K_n` maximizes all-terminal reliability.

This is a self-rederivation by the owner track, **not** a second independent audit of the finite package.

The analytic proof also shows why this route is potentially useful beyond `n=8`: it never enumerates an `n`-vertex graph class.

## 9. Why I stop the claim short of closure

The fixed finite claim has mathematical metric `R_SPLIT8=0`, but fleet closure still requires two independent OTHER-task audits. The current exact state is:

- owner exact finite certificate: PASS;
- P26 independent full-proof audit: PASS;
- second genuinely distinct OTHER-task full-proof audit: **MISSING**;
- current prior-art search: bounded negative, not a novelty certificate.

Therefore the correct lifecycle label remains

`CANDIDATE_COMPLETE / SOURCE_PARTIAL_OPEN / AUDIT_GATE_1_OF_2`.

I do not create the required paper folder yet, because Section G requires the second audit before closure packaging. I also do not call the unrestricted Romero/Brown--McMullin simple-graph problem solved: the theorem above settles one infinite dense diagonal, while many other `(n,m)` classes remain open.

## 10. Method outcomes

**#1 CHANGE THE CATEGORY — SUCCESS.** The identity `Rel(X+st)=Rel(X)+p SR_X` turns the split comparison into classical all-terminal reliability.

**#3 PROVE SOMETHING STRONGER — SUCCESS.** The finite `n=8,m=26` case extends by the same argument to every `n>=4`, with genuinely unresolved source content from `n>=8` onward.

**#21 ASK WHO ELSE HAS THIS SHAPE — SUCCESS.** The 1992 Satyanarayana--Schoppmann--Suffel theorem on deleting independent edges from a complete graph supplies exactly the all-terminal ordering needed after the bridge. This is explicitly credited as prior machinery, not relabelled as a new theorem.

If the audit gate remains pending next run, the next nonrepeating attack triple reserved is **#6 DEFORM TO A POINT YOU CAN SOLVE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE**, aimed at determining whether the max-minus-three diagonal admits a similarly clean bridge without turning exploratory evidence into a claim.

## 11. Model / scheduler-control truth

The operative implementation manifest still records that the exposed native scheduler surface has **no model selector, no reasoning selector, no authenticated applied-runtime model/reasoning receipt, and no guaranteed hour-long execution control**. The requested `GPT-6 / maximum` is therefore prompt text only here.

The same manifest records the historical P26 response `You cannot modify this task` in one authorization context. Later repository records show that a different authorized context successfully updated P26's prompt. The lawful remedy for a future denial is an owning/authorized workspace/API/admin context, ownership repair/transfer, or platform support for the same task — not a permission bypass or unauthorized clone.

No scheduler mutation was attempted in this worker run, consistent with the current operational restriction.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  active_claim: ROMERO-2025-SPLIT8
  source: Pablo Romero, TCS 1047 (2025) 115327, arXiv:2503.15453
  fixed_metric: R_SPLIT8
  before: 0
  after: 0
  movement: NO_FIXED_METRIC_MOVEMENT
  unchanged_count_before: 0
  unchanged_count_after: 1
  claimed_layer_status: CANDIDATE_COMPLETE
  unrestricted_source_status: PARTIAL_OPEN
  audit_gate_before: 0/2
  audit_gate_after: 1/2
  audit_ids:
    - P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64_PASS_FULL_MATHEMATICAL_PROOF
    - SECOND_DISTINCT_AUDIT_MISSING
  new_source_extension:
    statement: "For every n>=4, a diameter-terminal K_n minus two adjacent edges is uniformly most split reliable in T_{n,binom(n,2)-2}."
    source_new_content_begins: n>=8
    proof_status: SELF_PROOF_COMPLETE_ON_PAGE
    priority_status: UNVERIFIED_BOUNDED_NEGATIVE_SEARCH
    independent_audits: 0/2_for_extension
    changes_active_claim_scope: false
  methods: [1, 3, 21]
  remaining_obligation: "Obtain a second genuinely distinct OTHER-task full-proof audit for the exact n=8 package before fleet closure; keep broader Romero problem PARTIAL."
  frozen_predecessor:
    source: Lyons-Peres Question 6.20 / I0056
    regime: H_5_5 outer-vertex normalization
    interval: "[sqrt(5),sqrt(5)]"
    width_before: 0
    width_after: 0
    full_source_status: PARTIAL
  repository_delta_from_prior_r06:
    base: 26c39052586e085df399b4c21ecbc465c655e03a
    observed_head: 6674040af9f268a9ac214bb7352243629068a0de
    ahead_by: 113
    behind_by: 0
    complete: true
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
```

End of R06 immutable run report.
