Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 6 -> n_edge^* >= 6`. Section-B methods actually tried: #8 GO THE OTHER WAY AND DISCRETIZE, #27 SWAP THE QUANTIFIERS, #28 REPLACE "FOR ALL" WITH "FOR TYPICAL".**

# NM13-06 research invocation — P0195 exact low-temperature theorem for the split-graph blocker

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Canonical source / claim: `P0195`, `operations/claims/P0195.md`  
Canonical dedup key: `monotonicity_of_the_ferromagnetic_ising_spectral_gap`  
Shard: `5 mod 13`  
Parent source status after this run: **OPEN (bounded current-status check only)**  
NM13-06 status after this run: **PARTIAL**  
Frozen metric before / after: **`n_edge^* >= 6 -> n_edge^* >= 6`**  
Consecutive unchanged runs since last frozen-metric movement: **4 -> 5**  
Stuck-recovery episodes used: **1 -> 1**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime and task-control disclosure

The scheduler prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still offers prompt/title, scheduling or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and reasoning controls and ideally authenticated per-run attestation.

The historical P26 `You cannot modify this task` event was an authorization-context boundary, not a release of mathematical ownership. Current repository policy records that a later P26 update succeeded from another authorized context. The lawful workaround is the owning/otherwise-authorized context or an authorized product/admin/API/support path, never cloning the task or bypassing access controls. No task, schedule, workflow, permission, or support request was changed in this invocation.

## 2. Authoritative continuity and repository read

This is **not a new admission**. It continues the already admitted P0195 assignment under the immutable claim `operations/claims/P0195.md`. The claim still records owner `proofnet24/NM13-06`, CLOSABLE OUTSIDE status, exact LPW source, dedup key, SHA256 `102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`, and residue `5 mod 13`.

Before substantive work I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0195.md`;
- exact-ID/title/dedup-key claim, attempt, handoff, POSTED, campaign, and audit searches for P0195;
- the full current NM13-06 report chain through the immediately preceding stuck report `2026-09-18T07-30-30Z__p0195-stuck-recovery-1.md`;
- newest recovered neighboring NM13-05 and NM13-07 states.

The current claim remains exclusive to NM13-06. I recovered no owner-authorized release, competing owner under an alias, retirement, source-level POSTED closure, campaign settlement, or passed P0195 audit. The historical campaign work remains a limited two-spin attempt rather than a source resolution. Large root/JSONL surfaces can be connector-bounded, so exact identity/claim/history searches, not truncation, are the continuity anchors.

The immediately preceding run was mandatory Section-I stuck-recovery episode 1. It isolated the unique densest unresolved six-vertex cutwidth tie as the simplest special case still unproved:

- source `G = K_3 \vee 3K_1`, canonical mask `4095`, 12 edges;
- target `H = G + {b_1b_2}`, canonical mask `8191`, 13 edges;
- cutwidth transition `7 -> 7`.

It also identified the missing ingredient: an all-temperature comparison of the actual second eigenvalue, not another graph-theoretic barrier estimate. This run executes that recovery route on an explicit low-temperature tail rather than restarting the intake or repeating the previous lemma chain.

## 3. Exact source and bounded current literature check — 2026-09-18

The exact source remains Levin--Peres--Wilmer, *Markov Chains and Mixing Times*, second-edition open-problem chapter, Question 2 (same wording in the older public edition under Chapter 23). Under the chapter's Glauber-dynamics convention it asks whether the ferromagnetic Ising spectral gap is monotone increasing in temperature and monotone decreasing when edges are added, with a stronger individual-coupling formulation nearby.

This worker continues only the literal **edge-addition clause** in the frozen zero-field, common-`beta`, random-scan one-site heat-bath model. It does not replace the source by temperature monotonicity, continuous-time normalization, a different dynamics, or a stronger fixed-time expectation statement.

Fresh bounded public-web checks on 2026-09-18 used combinations of:

- `ferromagnetic Ising spectral gap edge addition monotonicity Glauber dynamics 2026`;
- `monotonicity Ising spectral gap adding edges Glauber`;
- `Glauber Dynamics On The Cycle Is Monotone Nacu`;
- `A remark on monotonicity for the Glauber dynamics on finite graphs Shirai`;
- exact-source wording around Peres / LPW monotonicity.

The check recovered Serban Nacu's 2003 cycle theorem: for heat-bath Glauber dynamics on a finite cycle, relaxation time is increasing in each coupling. It also recovered Tomoyuki Shirai's 2010 paper, which explicitly describes the general spectral-gap coupling monotonicity question as open there while disproving the stronger fixed-time single-spin expectation monotonicity statement. Searches also surfaced recent Ising/Glauber papers on different questions, but no theorem or counterexample settling the exact LPW edge-addition clause or this six-vertex split-graph comparison. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

## 4. Frozen model and metric

For a finite simple graph `G=(V,E)`, let the zero-field ferromagnetic Ising measure at common inverse temperature `beta>=0` be proportional to

`exp(beta * sum_{uv in E} sigma_u sigma_v)`.

Let `P_G(beta)` be random-scan one-site heat-bath dynamics, one uniformly selected site per discrete step. For an absent edge `e`, compare `G` and `G+e` at the same `beta` and same update normalization.

The frozen metric remains

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

Before this run: `n_edge^* >= 6`.  
After this run: **`n_edge^* >= 6`**.

The theorem below proves a new source-valid temperature interval for one important six-vertex marked type, but it does not eliminate all remaining six-vertex marked types. Therefore it is **not** frozen-metric movement. The unchanged counter honestly advances `4 -> 5`; stuck recoveries remain `1 -> 1`.

## 5. Method #8 — GO THE OTHER WAY AND DISCRETIZE

### 5.1 Idea, written before code

The blocker's full-temperature cross-resultant is large and was the wrong first object after the stuck report. I instead compactified the low-temperature endpoint by

`x = tanh(beta)`, `t = 1-x`,

and asked for a finite sign certificate on the rational interval `0 <= t <= 1/10`.

The idea note was written before the checker at

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_idea.md`

creation commit `2d5fc717eb282bf3e4171e2845de2a8b6db809a7`, blob `5f05ac6b5a05dda5a89eaf92340734c084d9d2e6`.

The note proposed the rational barrier

`q(t) = 1 - t^7/32`

and a Bernstein-basis certificate rather than a whole-interval bivariate resultant.

### 5.2 Previously established spectral reduction used here

For zero-field ferromagnetic heat-bath dynamics, the prior P0195 proof established that a second-eigenvalue eigenfunction can be chosen increasing and odd under global spin flip. Averaging it over graph automorphisms remains an increasing odd `lambda_2` eigenfunction and cannot vanish because the all-plus configuration is fixed by every automorphism and an increasing odd nonzero eigenfunction has positive all-plus value.

Hence for each endpoint graph the true `lambda_2` occurs in the subspace that is odd under spin flip and invariant under that endpoint's automorphism group. For the present pair, the exact quotient dimensions are

- `dim Q_G = 8`;
- `dim Q_H = 12`.

Because the full heat-bath chain is reversible, these quotient eigenvalues are real.

Let `f_G(x,L)` and `f_H(x,L)` be the cleared monic-in-`L` characteristic polynomials of these odd automorphism quotients.

## 6. New theorem: exact low-temperature ordering for the unique densest cutwidth-tie blocker

### Theorem `NM13-06-P0195-SPLIT-LOWTEMP-08`

Let

`G = K_3 \vee 3K_1`

and let `H` be obtained from `G` by adding one edge between two of the three independent vertices. For zero-field ferromagnetic Ising random-scan one-site heat-bath dynamics with common inverse temperature `beta`,

`gap_beta(H) < gap_beta(G)`

for every finite

`beta >= (1/2) log 19`.

Equivalently, the desired LPW edge-monotonicity inequality is strict on this marked transition whenever

`tanh(beta) >= 9/10`.

Numerically, `(1/2) log 19 = 1.4722194895832201...`.

### Proof

Set `x=tanh(beta)` and `t=1-x`. The theorem's range is exactly `0 < t <= 1/10`; finite beta gives `t>0`.

At the compactified endpoint `x=1`, the exact odd-quotient characteristic polynomials factor as

`f_G(1,L) = 9674588160000 * L*(L-1)*(3L-2)^2*(6L-5)^2*(6L-1)^2`,

and

`f_H(1,L) = 178322008965120000 * L*(L-1)*(3L-2)^3*(6L-5)^3*(72L^2-66L+13)*(72L^2-30L+1)`.

Every root other than `L=1` is strictly below `9/10`. Thus each endpoint has exactly one odd-quotient eigenvalue above `9/10` at `t=0`.

Now specialize at `L=9/10`. The exact checker expands

`f_G(1-t,9/10)` and `f_H(1-t,9/10)`

as rational univariate polynomials in `t`, rescales `[0,1/10]` to `[0,1]`, and converts each polynomial exactly to the Bernstein basis. Every Bernstein coefficient is **strictly negative** for both polynomials. Therefore neither characteristic polynomial vanishes at `L=9/10` anywhere on `0<=t<=1/10`.

Since the quotient spectra are real and vary continuously with `t`, an eigenvalue can enter or leave `(9/10,infinity)` only by crossing `9/10`. No such crossing occurs. Therefore for every `0<=t<=1/10`, each quotient still has **exactly one** eigenvalue above `9/10`; by the established odd-quotient reduction, it is the true second eigenvalue of the corresponding heat-bath chain.

Next use the rational barrier

`q(t)=1-t^7/32`.

On `0<=t<=1/10`, `q(t)>9/10`. Exact substitution shows that both

`f_G(1-t,q(t))` and `f_H(1-t,q(t))`

vanish to order exactly seven at `t=0`. After dividing by `t^7`, the checker again converts the resulting rational polynomials exactly to the Bernstein basis on `[0,1/10]`. It certifies

`f_G(1-t,q(t))/t^7 > 0`

and

`f_H(1-t,q(t))/t^7 < 0`

throughout the closed interval, because every Bernstein coefficient in the first polynomial is strictly positive and every Bernstein coefficient in the second is strictly negative.

Fix `0<t<=1/10`. Because each monic characteristic polynomial has exactly one real root above `9/10`, and because `q(t)>9/10`, the sign of the characteristic polynomial at `q(t)` determines on which side of that unique top root the barrier lies. The positive `G` sign gives

`lambda_2(G) < q(t)`,

while the negative `H` sign gives

`q(t) < lambda_2(H)`.

Hence

`lambda_2(G) < q(t) < lambda_2(H)`.

With discrete-time gap `gap=1-lambda_2`, this is exactly

`gap_beta(H) < gap_beta(G)`.

Finally `t<=1/10` is equivalent to `tanh(beta)>=9/10`, which is equivalent to

`beta >= atanh(9/10) = (1/2) log 19`.

This proves the theorem. `square`

### Low-temperature asymptotic mechanism

The same exact symbolic calculation gives the simple-root expansions at `t=0`:

`gap_G = (9/160) t^7 + O(t^8)`,

`gap_H = (9/608) t^7 + O(t^8)`.

Thus the cutwidth tie `7 -> 7` is broken at the next level by the prefactor: the source gap has the larger leading coefficient, by

`9/160 - 9/608 = 63/1520 > 0`.

The barrier coefficient satisfies

`9/608 < 1/32 < 9/160`,

which explains why `q(t)=1-t^7/32` separates the two slow branches near the zero-temperature endpoint.

## 7. Exact certificate and independent same-run reexecution

The exact checker is

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_exact.py`

creation commit `6d03b0da6a4edc8ceff093a4abb461333ad02f85`, blob `a63767826eb1779bfaab0511bbc22c5437950aa3`.

The archived output is

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_exact.out`

creation commit `15cd3bbb3a7d5256a21c699815ced0b7ccf1b94e`, blob `14646a47bfcede0cde942e3394e0af1c54244014`.

The checker was executed and ends `ALL_EXACT_CHECKS_PASS`. After archival I reexecuted the same local checker from scratch and byte-diffed its stdout against the archived output; the diff was empty. This is a **self-check**, not an independent outside audit.

The finite exact core verifies, among other things:

- masks `4095 -> 8191` and edge counts `12 -> 13`;
- odd quotient dimensions `8` and `12`;
- the endpoint factorizations above;
- strict Bernstein negativity at `L=9/10`;
- strict Bernstein positivity/negativity at the barrier after removing the exact `t^7` factor;
- gap leading coefficients `9/160` and `9/608`;
- final theorem range `beta >= (1/2)log(19)`.

No floating-point datum is used in the theorem proof.

## 8. Method #27 — SWAP THE QUANTIFIERS

The stuck report's blocker was not “prove another generic six-vertex lemma”; it was the all-temperature comparison for one uniquely dense and highly symmetric unresolved transition. Instead of quantifying over all 399 remaining marked types and all beta at once, I fixed that one source-valid transition and sought a complete theorem uniform on an explicit beta interval.

Outcome: **success as a restricted theorem**. The whole low-temperature tail `beta >= (1/2)log 19` is now rigorously settled for the blocker. This is mathematically substantive but remains PARTIAL relative to the source and does not move `n_edge^*`.

## 9. Method #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”

This method was used only for route selection, not as a claim. At the generic intermediate temperature `x=tanh(beta)=1/2`, I numerically diagonalized the reversible `64 x 64` heat-bath matrices for all **402** connected six-vertex marked edge-addition isomorphism types from the already-certified census.

Every sampled target-minus-source `lambda_2` difference was positive. The overall smallest numerical increment was about

`2.128723542829114e-4`,

on a 14-edge source already covered by the exact dense theorem. Among the 399 types outside that dense class, the smallest numerical increment was about

`5.321457613796099e-4`,

at source mask `5887` (11 source edges), adding edge `(1,5)`.

This is **floating-point diagnostic evidence only**. It is not an exact finite certificate, does not establish even the single temperature rigorously, does not prove a beta interval, and is not metric movement. Its value is strategic: the typical middle-temperature scan did not reveal a counterexample and points to mask `5887` as a plausible near-extremal target if another six-vertex attack is permitted.

## 10. What moved mathematically and what did not

The new theorem is a genuine all-beta-tail result for the exact special case selected by the mandatory stuck recovery. It also identifies a quantitative low-temperature mechanism invisible to cutwidth alone: both endpoint gaps scale like `(1-tanh beta)^7`, but the exact prefactors differ by `63/1520`.

However, the frozen metric is a **minimum counterexample order**, not a count of restricted theorems or temperatures covered. Because many connected six-vertex marked types and intermediate temperatures remain unresolved, the metric stays

`n_edge^* >= 6`.

I therefore do not relabel the new interval theorem as `n_edge^* >= 7`, do not call the source PROVED, and do not reset the unchanged counter.

All thirty Section-B methods have now been genuinely used at least once on P0195. There are no untried menu entries left to name honestly on this problem. Any future invocation must therefore say transparently that it is **reusing** a method rather than falsely labeling it new.

## 11. Audit and closure status

This source remains **PARTIAL / OPEN**. The new theorem has an executed exact self-check, but source closure would still require a full source-matching argument or counterexample, a complete prior-art record, and two independent outside audits. Exact P0195/P26/NM13-07 searches in current master did not recover a passed audit for P0195. Therefore:

- P26 audit: **NOT PASSED / not presumed**;
- NM13-07 audit: **NOT PASSED / not presumed**.

No audit request was manufactured merely to satisfy bookkeeping while the frozen metric is unchanged.

## 12. Next step and rotation threshold

This is the fifth consecutive invocation without frozen-metric movement since the `n<=5` completion moved the bound to `n_edge^*>=6`. Under the CLOSABLE rotation rule, one more unchanged run reaches the six-run rotation threshold.

Therefore the next invocation, if P0195 is still owned and no source-status correction intervenes, must prioritize a **metric-moving** attempt rather than another narrow interval certificate. The two honest possibilities are:

1. attack the negation again on the remaining six-vertex frontier, using the `x=1/2` near-extremizer and a temperature sweep only to locate a candidate, then exactify any candidate; or
2. attempt a genuine all-temperature exact classification route capable of eliminating every remaining six-vertex marked type and moving the bound to `n_edge^*>=7`.

Because all 30 menu methods have now been used, such a run must transparently reuse appropriate methods rather than pretend they are untried. If the frozen metric is still unchanged at the end of the next invocation, the six-unchanged-run CLOSABLE rule requires a preserved handoff and rotation to a new eligible source; P0195 must not receive filler certificates beyond that threshold.

## 13. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-06
  category: CLOSABLE_OUTSIDE
  source_id: P0195
  claim_id: P0195
  canonical_dedup_key: monotonicity_of_the_ferromagnetic_ising_spectral_gap
  shard_mod_13: 5
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: n_edge_star
  metric_definition: "minimum number of vertices in a source-valid edge-addition spectral-gap counterexample; +infinity if none"
  metric_before: ">=6"
  metric_after: ">=6"
  movement: false
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  stuck_recoveries_before: 1
  stuck_recoveries_after: 1
  methods_actual:
    - 8
    - 27
    - 28
  theorem_id: NM13-06-P0195-SPLIT-LOWTEMP-08
  theorem_scope: "G=K3 join 3K1; H=G plus one independent-part edge; gap_beta(H)<gap_beta(G) for every finite beta >= (1/2)log 19"
  new_exact_constants:
    beta_tail: "(1/2)log 19"
    source_gap_leading_coefficient_in_t7: "9/160"
    target_gap_leading_coefficient_in_t7: "9/608"
    coefficient_difference: "63/1520"
    t: "1-tanh(beta)"
  idea_artifact:
    path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_idea.md
    commit: 2d5fc717eb282bf3e4171e2845de2a8b6db809a7
    blob: 5f05ac6b5a05dda5a89eaf92340734c084d9d2e6
  checker:
    path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_exact.py
    commit: 6d03b0da6a4edc8ceff093a4abb461333ad02f85
    blob: a63767826eb1779bfaab0511bbc22c5437950aa3
  checker_output:
    path: proofnet24/NM13-06/artifacts/2026-09-18/p0195_split_tail_exact.out
    commit: 15cd3bbb3a7d5256a21c699815ced0b7ccf1b94e
    blob: 14646a47bfcede0cde942e3394e0af1c54244014
    result: ALL_EXACT_CHECKS_PASS
    same_run_reexecution_diff: empty
  typical_temperature_diagnostic:
    exact_claim: false
    x: "1/2"
    connected_marked_types_scanned: 402
    min_unresolved_numeric_increment: 0.0005321457613796099
    near_extremal_source_mask: 5887
    near_extremal_added_edge: "(1,5)"
  audits:
    P26: NOT_PASSED
    NM13-07: NOT_PASSED
  all_section_B_methods_now_used: true
  next_step: "metric-moving n=6 counterexample search or all-temperature n=6 classification; if next run is unchanged, preserve handoff and rotate under six-run CLOSABLE rule"
```

## 14. Operational safeguards

This invocation wrote only substantive P0195 artifacts and this one immutable NM13-06 report. It did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign roots, claims, peer namespaces, schedules, workflows, permissions, or public surfaces. It used no email/Gmail, Drive, paid compute, public posting, or unreviewed external scripts.
