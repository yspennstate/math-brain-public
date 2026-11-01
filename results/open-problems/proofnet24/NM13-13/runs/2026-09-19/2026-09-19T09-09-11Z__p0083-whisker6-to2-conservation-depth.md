Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `A_whisker_cert: 6 -> 2`; actual Section-B methods tried this run: #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS, #26 HUNT THE SPORADIC CASE.**

# NM13-13 — P0083: whisker threshold 6 -> 2 by high-incidence conservation and a depth obstruction

Date: 2026-09-19 UTC  
Track: `NM13-13`  
Namespace: `proofnet24/NM13-13/`  
Category: HARD OUTSIDE  
Canonical source/claim ID: `P0083`  
Canonical dedup key: `sharp_reinforcement_threshold_for_warm_whiskers`  
Exclusive shard: `12 mod 13`  
Status: **PARTIAL / OPEN**

## 0. Executive result

The frozen metric moves

`A_whisker_cert: 6 -> 2`.

I prove the following source-valid theorem.

### Claim `NM13-13-P0083-WHISKER-2-04`

Let `G=(V,E)` be any finite graph WARM with uniform vertex firing. Let `alpha>2`. Then every equilibrium that is not linearly unstable has every connected component of its positive support equal to a whisker, i.e. a tree of diameter at most `3`.

This lowers the track's certified strict universal sufficient threshold from `alpha>6` to `alpha>2` while preserving the exact source scope and strict-threshold convention.

This is **not closure** of Open Problem 13. The MATRIX source explicitly notes the triangle transition at `4/3` and suggests that `alpha>4/3` may be sharp for both the forest and whisker conclusions. The remaining interval is therefore `(4/3,2]`, and neither P26 nor NM13-01 has independently audited the present claim.

The new idea is genuinely different from the preceding local pair-Hessian route. Once the published `alpha>2` forest theorem is available, every supported tree edge has a `high` endpoint carrying incidence at least `1-1/alpha>1/2`. Counting these high incidences on a tree leaves only two global orientation types. A power-law ratio plus the published least-edge lower bound then proves that a low-parent-incidence edge cannot continue for another generation. The only remaining possible diameter-4 shape is a rooted depth-two tree with two deep branches; an exact one-variable inequality shows each such deep branch would consume more than one half of the root incidence, so two cannot coexist.

---

## 1. Runtime and task-control truth

The requested line `Model: GPT-6. Reasoning: maximum` remains prompt text only. This invocation actually runs as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed here, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed task-control surface still provides task identity/title, prompt, schedule/start fields, timing mode, enablement, and list/update operations. It provides **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-model/applied-effort receipt**. Making GPT-6/maximum binding would require an owner-authorized scheduler/product/API surface that persists explicit model and effort fields into inference routing and returns a trustworthy per-run receipt.

The repository now also preserves the correction to the older P26 modification failure: one authorization context returned `You cannot modify this task`, while a later authorized context successfully applied the P26 update. The lawful workaround for any future denial is the same task's owning/otherwise authorized product/workspace/API/admin context or authorized platform support, not duplication, identity substitution, or permission bypass. This invocation changes no scheduler or permission.

---

## 2. Authoritative continuity, ownership, and repository delta

The controlling predecessor is

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T08-16-30Z__p0083-whisker43over5-to6-linegraph-spectral.md`

at creation commit

`35cf76f4c47d8d37880f9f595a8d70a79cbe5a38`.

Its retained state is:

- canonical claim `P0083` active and exclusively owned by NM13-13;
- metric `A_whisker_cert = 6`;
- source status PARTIAL / OPEN;
- previous methods #3/#15/#18 genuinely attempted;
- unchanged-run count `0`;
- HARD stuck-recovery count `0/2`;
- P26 audit NOT_DONE;
- NM13-01 audit NOT_DONE;
- next planned methods #12/#20/#26.

Before new mathematics I freshly read or recovered the required current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the predecessor report;
- current `operations/claims/P0083.md`;
- the newest recovered neighboring NM13-01 and NM13-12 reports;
- source/attempt continuity already frozen in the canonical claim and predecessor reports; and
- fresh bounded source/current-literature queries described below.

Newest recovered neighbors before this write were:

- `proofnet24/NM13-01/runs/2026-09-19/2026-09-19T08-08-30Z__admission-delta-screen-29-p0336-p0459-owned-offshard-p0220-not-release.md`; and
- `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T07-53-25Z__p0214-softmin-progress-typical-stuck-trigger.md`.

The append-only intake/attempt corpora are too large for an honest claim that every unchanged historical byte was freshly rendered model-visible during one invocation. I make no such claim. Continuity is carried by the canonical P0083 claim plus the complete exact Git delta. Missing display is never treated as permission to reset history or ownership.

Final frozen pre-write `master` observed by this invocation:

`d1050821f8f6cd8c95f2c239f305dce7eff8860c`.

Exact comparison

`35cf76f4c47d8d37880f9f595a8d70a79cbe5a38 .. d1050821f8f6cd8c95f2c239f305dce7eff8860c`

reports:

- status: `ahead`;
- commits ahead: **106**;
- commits behind: **0**;
- total commits: **106**;
- complete changed-file set (`too_large = null`).

That complete interval contains no mutation of root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, screened `probability_1000_intake_*/problems.jsonl`, or `operations/claims/P0083.md`. A fresh exact-commit read of `operations/claims/P0083.md` at the frozen head still records owner NM13-13, category HARD OUTSIDE, canonical key `sharp_reinforcement_threshold_for_warm_whiskers`, SHA-256 `7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`, and residue 12. No ownership release, alias collision, or source retirement occurred.

A fresh repository search for `P0083 audit` recovered the claim and NM13-13 self-reports, plus unrelated ownership mentions, but no independent P26 or NM13-01 PASS. Audit state therefore remains NOT_DONE for both required auditors.

---

## 3. Source and literature status checked 2026-09-19

The exact source is Aletti--Collevecchio--Crimaldi--Deijfen--Dereich--Ghiglietti--van der Hofstad--Holmes--Kious--Kleptsyn--Lodewijks--Mörters--Schapira, *Open problems in stochastic reinforcement models*, MATRIX Annals, Open Problem 13.

The primary source was reopened directly. Its finite-graph paragraph states that a limiting equilibrium cannot be linearly unstable, that for `alpha>2` such an equilibrium is supported on a forest, and that for `alpha>25` with uniform firing each tree is a whisker. Open Problem 13 asks to improve the `25` bound. Immediately afterward the source records the triangle transition at `4/3` and says perhaps `alpha>4/3` is sharp.

The published baseline paper was also rechecked: Mark Holmes and Victor Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, DOI `10.1063/1.4978683`. Its abstract states the two thresholds `2` (forest) and `25` (whisker).

The theorem below uses three published ingredients from that finite-equilibrium analysis, already source-checked in the P0083 continuity record:

1. for `alpha>2`, every support component of a not-linearly-unstable equilibrium is a tree;
2. for every supported edge `e=uv`, at least one endpoint incidence is at least `h:=1-1/alpha`; equivalently every edge has a `high` endpoint; and
3. in a nontrivial support component, after rescaling by the number of vertices, every supported edge weight is strictly greater than `1` (the least-edge/leaf corollary; equality belongs only to the one-edge trivial component).

Fresh queries included exact source title / Open Problem 13, `WARM whisker`, Holmes--Kleptsyn, `alpha>2`, `alpha>25`, and 2025--2026 threshold-improvement terms. They recovered the source, the 2017 baseline, and later adjacent WARM work including the 2023 infinite-graph strong-reinforcement paper, but no checked primary source matching this finite-equilibrium Open Problem 13 scope with a threshold below 25. This is **bounded negative evidence only**, not a proof of worldwide openness, novelty, or priority.

---

## 4. Normalization and published ingredients

Let a connected support component have edge set `E_T`. Uniform firing means every graph vertex fires with the same probability. Write `n=|V(G)|` and use the rescaled edge weights

`w_e := n x_e`.

For an incidence `(e,v)` with `v` an endpoint of `e`, write

`q_{e,v} := x_e^alpha / sum_{f incident to v} x_f^alpha`.

At equilibrium,

`w_e = q_{e,u} + q_{e,v}`                                                   (4.1)

for `e=uv`, and at every support vertex

`sum_{e incident to v} q_{e,v} = 1`.                                         (4.2)

For `alpha>2`, put

`h := 1 - 1/alpha > 1/2`.                                                     (4.3)

The published finite-equilibrium argument gives, for every supported edge,

`max(q_{e,u},q_{e,v}) >= h`.                                                  (4.4)

For completeness, this is also consistent with the exact support-Hessian formulation proved in the preceding NM13-13 report: with `C_{v,e}=q_{e,v}/sqrt(w_e)`, absence of a positive support-Jacobian eigenvalue gives `C^T C >= h I`. Looking at the `e,e` entry gives

`(q_{e,u}^2+q_{e,v}^2)/w_e >= h`.

Since `(a^2+b^2)/(a+b) <= max(a,b)`, (4.4) follows.

If the component consists of one edge, it is already a whisker. Hence below I assume at least two supported edges. The published least-edge corollary then gives

`w_e > 1` for every `e in E_T`.                                                (4.5)

Finally, the published `alpha>2` theorem gives that the component `T` is a tree.

Everything new begins from (4.1)--(4.5).

---

## 5. Method #12 — FIND WHAT IS CONSERVED: count the high incidences

Call an incidence `(e,v)` **high** if

`q_{e,v} >= h`.

By (4.4), every edge has at least one high endpoint. By (4.2) and `h>1/2`, no vertex can support two high incidences.

Let the tree `T` have `m` edges and hence `m+1` vertices. Let `H` be the number of high incidences. Then

`m <= H <= m+1`.                                                              (5.1)

There are therefore only two possibilities.

### Type D: one double-high edge

If `H=m+1`, every vertex has exactly one high incidence, and exactly one edge is high at both endpoints. Call that edge the **central edge**.

Every other edge has exactly one high endpoint. Starting from either endpoint of the central edge, all side edges point away from the central edge toward their unique high endpoints.

### Type R: one high-free root

If `H=m`, every edge has exactly one high endpoint and exactly one vertex has no high incidence. Call that vertex `r`.

Orient every edge toward its high endpoint. Because the underlying graph is a tree, this orientation is exactly the outward orientation of a rooted tree with root `r`: every non-root vertex has one incoming/high parent edge.

This is the run's conservation law. The local incidence threshold plus Euler's identity `|V|=|E|+1` collapses an arbitrary support tree to two global orientation types.

Outcome of Method #12: **SUCCESS.** It replaces the preceding run's pairwise local classification by a global count with only two orientation cases.

---

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS: a low-parent edge cannot continue

The previous `alpha>6` route failed below `6` because it used a local pair-Hessian bound to force a high endpoint to be a leaf. That inequality saturates at a constant near the old threshold. The missing information is not another local Hessian minor: it is the exact WARM power-law ratio between a parent edge and a child edge, together with the published strict lower bound `w_f>1`.

The following lemma is the new mechanism.

### Lemma 6.1 — depth obstruction for every `alpha>2`

Suppose an oriented edge `e=u v` is low at its parent `u` and high at its child `v`, and suppose

`lambda := q_{e,u} <= 1/alpha`.                                                (6.1)

Then `v` has no child edge.

#### Proof

Assume instead that `v` has at least one child. Let

`t := sum_{f child of v} q_{f,v}`.

Because the parent edge is high at `v`,

`q_{e,v}=1-t >= h=1-1/alpha`,

so

`0 < t <= 1/alpha`.                                                           (6.2)

Choose a child edge `f` and write

`d := q_{f,v}`, so `0<d<=t`.

At the common vertex `v`, the definition of the incidences gives the exact ratio

`d/(1-t) = (w_f/w_e)^alpha`.                                                   (6.3)

By (4.5), `w_f>1`. Therefore

`w_e = w_f ((1-t)/d)^(1/alpha)
     > ((1-t)/d)^(1/alpha)
     >= ((1-t)/t)^(1/alpha)`.                                                 (6.4)

On the other hand (4.1) gives

`w_e = lambda + 1 - t`.

Thus

`lambda > B_alpha(t)
          := t - 1 + ((1-t)/t)^(1/alpha)`.                                    (6.5)

I claim

`B_alpha(t) > 1/alpha`                                                        (6.6)

for every `alpha>2` and `0<t<=1/alpha`.

Inequality (6.6) is equivalent to

`((1-t)/t)^(1/alpha) > 1 + 1/alpha - t`.

Both sides are positive, so define

`phi_alpha(t)
 := log((1-t)/t) - alpha log(1+1/alpha-t)`.

It suffices to prove `phi_alpha(t)>0`. Differentiating,

`phi_alpha'(t)
 = -1/[t(1-t)] + alpha/(1+1/alpha-t)`.                                        (6.7)

The sign is negative exactly when

`Q_alpha(t)
 := alpha^2 t^2 - alpha(alpha+1)t + alpha+1 > 0`.                              (6.8)

If `2<alpha<3`, the discriminant of `Q_alpha` is

`alpha^2(alpha+1)(alpha-3)<0`,

so (6.8) holds for all real `t`.

If `alpha>=3`, the smaller root is

`rho_- = [(alpha+1)-sqrt((alpha+1)(alpha-3))]/(2alpha)`.

Moreover

`rho_- > 1/alpha`

because

`(alpha-1)^2 - (alpha+1)(alpha-3) = 4 > 0`.

Hence in all cases `phi_alpha'(t)<0` throughout `(0,1/alpha]`. Therefore

`phi_alpha(t) >= phi_alpha(1/alpha)
              = log(alpha-1) > 0`,

proving (6.6). Combining (6.5), (6.6), and (6.1) gives the contradiction

`lambda > 1/alpha >= lambda`.

So `v` cannot have a child. QED.

### Consequence for Type D

At an endpoint of the central double-high edge, the total incidence available to all side edges is at most

`1-h = 1/alpha`.

Thus every side edge has parent-side incidence at most `1/alpha`, and Lemma 6.1 says its other endpoint is a leaf. The component is a central edge with leaves attached to its two endpoints, hence a whisker of diameter at most `3`.

### Consequence for Type R

At every non-root vertex, the parent edge is high, so the total incidence of all child edges is at most `1/alpha`. Therefore every edge from depth `1` to depth `2` has parent-side incidence at most `1/alpha`, and Lemma 6.1 says every depth-2 vertex is a leaf.

Thus every Type-R component has height at most `2` from its unique high-free root.

Outcome of Method #20: **SUCCESS.** It identifies precisely why the prior `6` barrier was artificial and replaces the saturated local pair-Hessian leaf test by a parent-child power-law depth obstruction valid for every `alpha>2`.

---

## 7. Method #26 — HUNT THE SPORADIC CASE: eliminate two deep root branches for `2<alpha<=6`

After Lemma 6.1, the only Type-R tree that can still have diameter `4` is a height-two rooted tree with **two different depth-1 vertices that each have at least one depth-2 leaf**.

I now rule out exactly that sporadic shape for the interval not covered by the predecessor theorem, namely

`2 < alpha <= 6`.                                                             (7.1)

Fix a depth-1 vertex `v` that has at least one child leaf. Let `e=rv` be its parent edge and write

`lambda := q_{e,r}`

for its incidence at the root. At `v`, let

`t := sum_{f child of v} q_{f,v}`.

The parent edge is high at `v`, so

`0<t<=1/alpha<1/2`,

and

`q_{e,v}=1-t`.

Choose a child leaf edge `f` and write

`d:=q_{f,v}`, so `0<d<=t`.

Because the other endpoint of `f` is a support leaf, its incidence there is exactly `1`. Hence

`w_f=1+d`.                                                                     (7.2)

The power-law ratio at `v` gives

`d/(1-t) = (w_f/w_e)^alpha`.

Using (7.2) and `w_e=lambda+1-t`, this is exactly

`lambda
 = t-1 + (1+d)((1-t)/d)^(1/alpha)`.                                          (7.3)

For fixed `alpha`, the factor

`(1+d)d^(-1/alpha)`

has logarithmic derivative

`1/(1+d) - 1/(alpha d)`,

which is negative whenever `(alpha-1)d<1`. Since

`d<=t<=1/alpha<1/(alpha-1)`,

it is decreasing on the whole admissible interval. Therefore (7.3) implies

`lambda >= A_alpha(t)
 := t-1 + (1+t)((1-t)/t)^(1/alpha)`.                                          (7.4)

For (7.1), `1/alpha>=1/6`, while `(1-t)/t>1`; hence

`A_alpha(t)
 >= t-1 + (1+t)((1-t)/t)^(1/6)`.                                             (7.5)

It remains to show the right-hand side of (7.5) exceeds `1/2` for every `0<t<1/2`. This is equivalent to

`((1-t)/t)^(1/6) > (3/2-t)/(1+t)`,

and, after taking sixth powers, to

`P(t):=(1-t)(1+t)^6 - t(3/2-t)^6 > 0.                                        (7.6)

Set `u=2t`, so `0<u<1`. In the degree-7 Bernstein basis

`B_{j,7}(u)=C(7,j)u^j(1-u)^(7-j)`,

the exact identity is

`P(u/2)=sum_{j=0}^7 b_j B_{j,7}(u)`,

with

`(b_0,...,b_7)
 = (1,
    487/896,
    165/224,
    297/224,
    243/112,
    711/224,
    1899/448,
    665/128)`.                                                               (7.7)

Every coefficient in (7.7) is strictly positive and every Bernstein basis function is nonnegative on `[0,1]`; hence `P(t)>0` on `[0,1/2]`. Therefore every depth-1 vertex that has a child leaf satisfies

`lambda > 1/2`.                                                               (7.8)

At the root, the incidences of all incident edges sum to `1`. Thus **at most one** root child can have descendants.

A rooted tree of height at most `2` with at most one deep branch has diameter at most `3`: paths between two depth-2 leaves in the same branch have length `2`, and a path from a depth-2 leaf to a root leaf has length `3`.

So every Type-R component is also a whisker for `2<alpha<=6`.

Outcome of Method #26: **SUCCESS.** The only residual diameter-4 motif after the depth obstruction is eliminated by an exact one-variable finite certificate.

---

## 8. Main theorem and metric movement

We have proved the whisker conclusion for every `2<alpha<=6`:

- Type D is a whisker by Lemma 6.1;
- Type R has height at most two by Lemma 6.1 and at most one deep branch by (7.8), hence diameter at most three.

The immediately preceding NM13-13 report already proved the same universal source-scope conclusion for every `alpha>6`.

Therefore, combining the two intervals:

> **Theorem (`NM13-13-P0083-WHISKER-2-04`).** For every finite graph WARM with uniform vertex firing and every `alpha>2`, every equilibrium that is not linearly unstable has each positive-support component equal to a whisker, i.e. a tree of diameter at most `3`.

The frozen metric therefore moves

`A_whisker_cert: 6 -> 2`.

This is a source-level quantitative improvement relative to the published `25` threshold, but it remains PARTIAL because the source explicitly suggests the lower `4/3` scale and because the required independent audits have not occurred.

---

## 9. Exact finite-core self-check

The finite algebra in Method #26 was independently executed with exact rational arithmetic only. The checker is

`proofnet24/NM13-13/artifacts/P0083_whisker2_bernstein_exact_check.py`

created at commit

`c84fedaf9e4a0176287698f8a6159f93ae0f19bf`,

and the archived output is

`proofnet24/NM13-13/artifacts/P0083_whisker2_bernstein_exact_check.out`

created at commit

`898389857c966ff14f78fc437af6615dc1ad4d4d`.

The checker was executed before archival and then both files were read back at their creation commits. It returns:

```text
PASS
P_t_power = ['1', '-409/64', '873/16', '-1135/16', '125/2', '-171/4', '4', '-2']
P_u_over_2_bernstein = ['1', '487/896', '165/224', '297/224', '243/112', '711/224', '1899/448', '665/128']
min_bernstein = 487/896
P(0) = 1
P(1/6) = 326101/279936
P(1/2) = 665/128
root_comparison_gap = 4
```

Besides checking the Bernstein coefficients and reconstructing the polynomial exactly from them, the script verifies the identity

`(alpha-1)^2-(alpha+1)(alpha-3)=4`

used in the depth-lemma derivative sign.

This is a **self-check**, not an independent audit.

---

## 10. What did and did not move

Mathematical movement:

- certified strict universal whisker threshold: `6 -> 2`;
- theorem scope remains exactly finite graph / uniform firing / not-linearly-unstable equilibrium / all support components;
- endpoint convention remains strict (`alpha>A_whisker_cert`).

No silent metric change occurred.

What remains open:

- the source-suggested interval `(4/3,2]`;
- below `2`, the published forest theorem is unavailable, so cyclic support must be confronted rather than hidden inside a tree argument;
- source-level sharpness at `4/3` is not proved;
- P26 audit NOT_DONE;
- NM13-01 audit NOT_DONE;
- no paper package is created because closure is not established.

Because the metric moved, the unchanged-run counter remains `0`. No stuck-recovery episode is consumed; HARD recovery count remains `0/2`.

---

## 11. Next route: cross the forest barrier instead of polishing the tree proof

The present argument appears to have extracted the whole easy gain available once the published `alpha>2` forest theorem is granted. Further polishing inside the tree class cannot move `A_whisker_cert` below `2`, because below `2` a source-valid proof must itself control possible cyclic support.

The next invocation therefore rotates mechanisms rather than extending the same inequalities. Planned unused methods are:

- **#1 CHANGE THE CATEGORY:** recast the support-Hessian condition on a cyclic component in cycle-space / signed-incidence language and isolate the exact obstruction carried by a fundamental cycle;
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** re-read the published forest-threshold proof and the triangle `4/3` transition to identify exactly which step breaks at `2` and whether it is a proof artifact or a real stable-cycle mechanism;
- **#25 COUNT THE SAME THING TWICE:** replace the `high>1/2` injection used here by a fractional matching/incidence count that remains meaningful when `h<=1/2`, beginning with exact triangle and square motifs.

The first objective is a source-valid exact statement on the interval `(4/3,2]`: either construct a genuinely not-linearly-unstable non-whisker/cyclic equilibrium (which would give a counterexample to any too-low universal threshold) or prove an exact cycle exclusion on the smallest motifs and identify a transfer mechanism. Numerical candidates alone will not be promoted.

---

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-13
  namespace: proofnet24/NM13-13/
  source_id: P0083
  claim_id: P0083
  theorem_id: NM13-13-P0083-WHISKER-2-04
  category: HARD_OUTSIDE
  status: PARTIAL_OPEN
  canonical_dedup_key: sharp_reinforcement_threshold_for_warm_whiskers
  shard_residue_mod13: 12
  metric_name: A_whisker_cert
  metric_scope: >-
    Smallest certified strict universal sufficient threshold on this track such
    that every finite uniform-firing graph WARM, for alpha above the threshold,
    has every not-linearly-unstable equilibrium supported in components of
    diameter at most 3.
  metric_before: 6
  metric_after: 2
  movement: true
  actual_methods:
    - 12_FIND_WHAT_IS_CONSERVED
    - 20_FIND_WHY_THE_ALGORITHM_FAILS
    - 26_HUNT_THE_SPORADIC_CASE
  method_outcomes:
    12: SUCCESS_high_incidence_count_reduces_tree_to_double_high_or_rooted_type
    20: SUCCESS_power_law_depth_obstruction_valid_for_all_alpha_gt_2
    26: SUCCESS_exact_Bernstein_certificate_eliminates_two_deep_root_branches_for_2_lt_alpha_le_6
  exact_checker: proofnet24/NM13-13/artifacts/P0083_whisker2_bernstein_exact_check.py
  checker_output: proofnet24/NM13-13/artifacts/P0083_whisker2_bernstein_exact_check.out
  checker_status: PASS_SELF_CHECK
  checker_commit: c84fedaf9e4a0176287698f8a6159f93ae0f19bf
  output_commit: 898389857c966ff14f78fc437af6615dc1ad4d4d
  p26_audit: NOT_DONE
  secondary_audit_partner: NM13-01
  nm13_01_audit: NOT_DONE
  unchanged_run_count: 0
  stuck_recovery_count: 0
  stuck_recovery_limit: 2
  source_remaining_target: >-
    Cross below alpha=2 toward the source-suggested 4/3 scale; below 2 cyclic
    support must be controlled because the published forest theorem no longer
    supplies a tree reduction.
  next_methods:
    - 1_CHANGE_THE_CATEGORY
    - 22_READ_THE_FAILURES_NOT_THE_SUCCESSES
    - 25_COUNT_THE_SAME_THING_TWICE
  prewrite_master: d1050821f8f6cd8c95f2c239f305dce7eff8860c
  predecessor_report_commit: 35cf76f4c47d8d37880f9f595a8d70a79cbe5a38
  bounded_literature_check_date: 2026-09-19
  literature_scope: >-
    MATRIX Open Problem 13 primary PDF; Holmes-Kleptsyn 2017 finite WARM
    baseline; exact WARM-whisker/threshold queries; later adjacent WARM work.
  literature_limit: >-
    Bounded indexed-web/source check only; negative search evidence is not a
    proof of worldwide openness, novelty, or priority.
```

---

## 13. Operational safeguards

Exactly one immutable report is written by this invocation in the NM13-13 `runs/` namespace and is to be read back at its creation commit. The two new artifact files are substantive exact checks for a moved mathematical quantity, not receipt-only activity.

No shared root ledger, peer namespace, existing canonical claim, workflow, permission, public surface, email/Gmail resource, Drive resource, paid-compute resource, or schedule was modified. No task was duplicated to bypass authorization. No floating-point result is used as a certificate. No independent audit is claimed.

**End of complete run report.**
