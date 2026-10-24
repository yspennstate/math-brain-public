Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: `A_whisker_cert: 2 -> 2`; Section-B methods actually tried: #1 CHANGE THE CATEGORY, #22 READ THE FAILURES, #25 COUNT THE SAME THING TWICE.**

# NM13-13 — P0083 fifth substantive run: full-rank incidence topology, no even unicycles, and an exact path Rayleigh reduction

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-13` / `proofnet24/NM13-13/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: `P0083`  
Canonical dedup key: `sharp_reinforcement_threshold_for_warm_whiskers`  
Selection shard: **12 mod 13**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED**

## 1. Frozen target, metric, and honest outcome

The source and metric are unchanged.  The source is Aletti et al., *Open problems in stochastic reinforcement models*, Open Problem 13: for a finite graph WARM with uniform vertex firing, improve the sufficient reinforcement threshold `alpha>25` under which every connected component of the support of a not-linearly-unstable equilibrium is a whisker (a tree of diameter at most three).  The source records the triangle transition at `4/3` and says that perhaps `alpha>4/3` is sharp for both the forest and whisker conclusions.

The frozen metric remains

`A_whisker_cert`

= the smallest strict universal sufficient threshold proved on this track in the exact source scope.

The preceding run proved the source-valid universal whisker theorem for every `alpha>2`.  This invocation does **not** lower that strict threshold:

- metric before: `2`;
- metric after: `2`;
- movement: **none**.

There is nevertheless substantive structural progress below: the stability matrix forces **every** support component for every `alpha>1` to be a pseudoforest; its unique cycle, when present, must be odd; and every non-whisker tree has an exact one-dimensional alternating-path Rayleigh obstruction.  These statements materially shrink the remaining `(4/3,2]` problem but do not certify a smaller universal whisker threshold.

Counters after this report:

- unchanged substantive runs after the last metric movement: **0 -> 1**;
- HARD stuck-recovery episodes consumed: **0 / 2**;
- stuck protocol: **not triggered**;
- P26 independent audit: **NOT_DONE**;
- NM13-01 independent audit: **NOT_DONE**.

No checker artifact is manufactured for an unchanged metric.  The new claims are symbolic theorem-sized deductions with complete arguments on this page; there is no bounded exhaustive/UNSAT claim or finite numerical core to certify in this run.

## 2. Runtime and task-control truth

The task prompt requests GPT-6 with maximum reasoning.  This invocation actually runs as **GPT-5.6 Sol**.  The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**.  I do not claim GPT-6, maximum reasoning, a guaranteed hour-long execution, or a support escalation.

The task-control surface exposed to this worker still offers title/prompt, schedule or relative-start fields, timing mode, enabled state, list, and update operations.  It exposes **no binding model-family selector and no binding reasoning-effort selector**.  Therefore GPT-6/maximum remains prompt text only.  Making that requirement enforceable would require an owner-authorized product/workspace/API/admin scheduling object with persistent model-family and reasoning-effort fields, backend routing that honors them, and trustworthy per-run attestation of the applied route.

The historical P26 response `You cannot modify this task` is an authorization-context boundary, not a mathematical or ownership release.  Repository task-health history records later successful in-place scheduler updates from an authorized context.  The lawful remedy to any recurrence is the owning/otherwise authorized product, workspace, API/admin context, or authorized platform support for the same task; it is not task duplication, identity substitution, or a permission bypass.  This invocation changes no schedule or permission.

## 3. Authoritative continuity, ownership, and repository reads

The controlling predecessor is

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T09-09-11Z__p0083-whisker6-to2-conservation-depth.md`

created at commit

`8e64ba51256913510005be842b23ead7d31d2350`.

Its durable state is preserved:

- `P0083` is admitted and exclusively owned by NM13-13;
- exact source scope and strict-threshold metric are frozen;
- metric history is `25 -> 22 -> 43/5 -> 6 -> 2`;
- methods genuinely used on P0083 before this invocation are `#2/#14/#16`, then `#11/#24/#30`, then `#3/#15/#18`, then `#12/#20/#26`;
- no HARD stuck-recovery episode has been consumed;
- required independent auditors remain P26 and NM13-01, with neither audit presumed or found complete.

Before doing new mathematics I freshly read or recovered the required control surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest own report; the newest visible neighboring NM13-12 and NM13-01 reports; current `operations/claims/P0083.md`; and P0083's archived source/attempt material.

The candidate-specific prior-attempt record still carries `attempted_unsolved`; the archived attempt studied a reflection-symmetric four-edge path and did not settle general asymmetric supports.  A fresh repository search for `P0083 attempted_unsolved` recovered the same history, not a later release or competing claim.

A fresh exact read of `operations/claims/P0083.md` at prewrite master `4c68a3a703f5b050b6362d12766c0eda285a1b35` still records:

- owner `NM13-13`;
- namespace `proofnet24/NM13-13/`;
- category `HARD OUTSIDE`;
- status `ACTIVE`;
- canonical SHA-256 `7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`;
- residue `12 mod 13`.

No release, retirement, alias collision, or duplicate owner was recovered.

The exact predecessor-to-prewrite comparison

`8e64ba51256913510005be842b23ead7d31d2350 .. 4c68a3a703f5b050b6362d12766c0eda285a1b35`

reports `ahead`, **131 commits ahead and 0 behind**.  A direct search of that compare response finds no mutation of `operations/claims/P0083.md`; the current claim read above is authoritative for this continuation.  Concurrent fleet activity in the interval includes unrelated claims/reports and does not release or supersede P0083.

No private-repository history necessary for this continuation was known to be inaccessible.  The append-only intake/attempt corpora are too large to honestly claim that every unchanged byte was rendered model-visible in this single invocation; P0083's canonical identity, current claim, prior attempt, source, and newest continuity were directly recovered.

## 4. Fresh source and bounded literature check — 2026-09-19

This is a bounded current-status check, not a proof of worldwide openness, novelty, or priority.

### 4.1 Current primary source

The current MATRIX/MFO open-problem source was inspected directly, including the PDF page containing Open Problems 12 and 13.  It still states:

- for `alpha>2`, every connected support component of a non-linearly-unstable equilibrium is a tree;
- for `alpha>25` and uniform firing, each such tree is a whisker;
- Open Problem 13 asks to improve `25`;
- the triangle has an edge die out for `alpha>4/3`, but not for `alpha<4/3`;
- perhaps `4/3` is sharp for both forest and whisker statements.

### 4.2 Published baseline

Holmes--Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, still gives the published source-scope baseline: forest support for `alpha>2` and whisker support for `alpha>25`.

### 4.3 Read the failure, not only the success

The earlier van der Hofstad--Holmes--Kuznetsov--Ruszel paper, *Strongly reinforced Pólya urns with graph-based competition*, Ann. Appl. Probab. 26 (2016), is unusually informative for the present barrier.  It proves the triangle phase transition at `4/3`, but explicitly says that for the line graph on four edges the authors **believe** the analogous vanishing statement and had not proved it there.  In other words, the smallest non-whisker path was already recognized as the next obstruction after the triangle.

That is exactly where the present track now lands from the opposite direction.  The preceding `alpha>2` proof used the fact that the Holmes--Kleptsyn champion incidence is `>1/2`, which orients every tree edge uniquely and converts the tree to a one-root/double-root problem.  As soon as `alpha<=2`, that unique-majority orientation is no longer available.  Repeating the same leaf argument would therefore be polishing a mechanism at its natural barrier rather than finding a way through it.

Focused searches on 2025--2026 WARM whisker thresholds, Open Problem 13, and the citation neighborhood of Holmes--Kleptsyn recovered later adjacent WARM work (including infinite/weak-reinforcement regimes) but no checked source-matching finite-equilibrium threshold improvement beyond the published literature.  That is negative bounded evidence only.

The 2016 and 2017 PDFs were inspected through indexed text; screenshot calls were also attempted as required for PDF analysis.  The current MATRIX source page rendered successfully.  The 2016 and 2017 screenshot fetches returned cache errors, so no visual-only detail from those failed screenshots is used as evidence.

## 5. Recalled exact stability language

Let a connected positive-support component have support vertices `V_H` and support edges `E_H`.  For a supported edge `e=uv`, write

`q_{e,v} = x_e^alpha / sum_{f incident to v} x_f^alpha`

and normalize edge weights by

`w_e = n_v x_e`.

At equilibrium under uniform firing,

`w_e = q_{e,u}+q_{e,v}`.                                    (5.1)

The preceding incidence-Gram run derived, in the Holmes--Kleptsyn `y_e=2 sqrt(x_e)` coordinates, the symmetric support Jacobian

`J = (alpha-1) I - alpha C^T C`,                            (5.2)

where

`C_{v,e} = q_{e,v}/sqrt(w_e)`

when `v` is incident to `e`, and is zero otherwise.

Holmes--Kleptsyn's octant/simplex stability lemma removes a possible hidden tangent-space issue.  Thus if the equilibrium is **not linearly unstable**, `J` has no positive eigenvalue and therefore

`C^T C >= h I`,   where   `h=(alpha-1)/alpha>0`.             (5.3)

Everything new below starts from (5.1)--(5.3).

## 6. Method #1 — CHANGE THE CATEGORY

### 6.1 Stability becomes graph topology: every support component is a pseudoforest for every `alpha>1`

Equation (5.3) is positive definite because `h>0`.  Consequently `C` has full column rank.

Restrict to one connected support component `H`.  If it has `m=|E_H|` supported edges and `n=|V_H|` support vertices, its block `C_H` is an `n x m` matrix.  Full column rank gives

`m <= n`.                                                     (6.1)

For a finite connected graph, the cyclomatic number is

`beta(H) = m-n+1`.

By (6.1), `beta(H)<=1`; connectedness gives `beta(H)>=0`.  Hence:

**Theorem `NM13-13-P0083-PSEUDOFOREST-05`.**  For every finite uniform-firing graph WARM, every `alpha>1`, and every equilibrium that is not linearly unstable, each connected component of its positive support is either a tree or a unicyclic graph.

This is stronger than a small-case calculation: stability itself, before any `alpha>2` incidence dichotomy, forbids two independent cycles.

It does **not** yet imply Open Problem 12's desired forest statement below `2`, because one cycle can remain.

### 6.2 Algebraic potential parametrization

The same category change produces a clean exact parametrization.  Put

`p = 1/(alpha-1) > 0`

and define, at each support vertex,

`A_v = 1 / sum_{e incident to v} w_e^alpha`.

Then

`q_{e,v}=A_v w_e^alpha`.                                    (6.2)

For `e=uv`, equilibrium (5.1) becomes

`w_e = (A_u+A_v) w_e^alpha`,

so

`w_e = (A_u+A_v)^(-p)`.                                     (6.3)

Therefore

`q_{e,v} = A_v (A_u+A_v)^(-(p+1))`,                         (6.4)

and vertex normalization is exactly

`A_v sum_{u~v} (A_u+A_v)^(-(p+1)) = 1`.                     (6.5)

The normalized incidence entries are

`C_{v,e}=A_v (A_u+A_v)^(-(p/2+1))`.                         (6.6)

For arbitrary edge variables `t_e`, set

`z_e=(A_u+A_v)^(p/2+1) t_e`.

Then (6.6) gives the exact cancellation

`(Cz)_v = A_v sum_{e incident to v} t_e`.                   (6.7)

Since `h=1/(p+1)`, stability (5.3) is therefore equivalent to the weighted unsigned-incidence inequality

`sum_v A_v^2 (sum_{e incident to v} t_e)^2
 >= (1/(p+1)) sum_{e=uv} (A_u+A_v)^(p+2) t_e^2`             (6.8)

for every real edge vector `t`.

This puts the remaining problem into a different category: a generalized eigenvalue problem for a **weighted signless incidence form**.  The conjectured source scale `alpha>4/3` is `p<3`, and its stability threshold is `h>1/4`.

Outcome of #1: **success as a structural route**, but no improvement of `A_whisker_cert` yet.

## 7. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

The historical failure is now mathematically precise.

The 2016 paper already separated the triangle (`alpha=4/3` transition proved) from the four-edge line (analogous support loss believed but unproved).  The 2017 proof later established a universal tree theorem only at `alpha>2`, then the whisker theorem at `alpha>25`.

The preceding NM13-13 run lowered the whisker theorem to `alpha>2` by exploiting the `>1/2` incidence majority available exactly above that forest threshold.  Below `2`, an edge may have no uniquely determined high endpoint.  Thus the old orientation/leaf mechanism no longer contains the ingredient required to continue.

The correct question for the interval `(4/3,2]` is therefore not “how do we sharpen the same leaf constant?” but rather:

1. can (5.3) alone eliminate the remaining unicyclic topology? and
2. if the component is a tree, can a global spectral test eliminate diameter at least four without assigning every edge a unique majority endpoint?

Sections 8 and 9 answer those questions partially and exactly.

Outcome of #22: **successful diagnosis**.  It identifies the lost ingredient at `2` and prevents a fifth version of the same scalar leaf proof.

## 8. Method #25 — COUNT THE SAME THING TWICE: every surviving cycle must be odd

Assume a support component is unicyclic, and let its unique cycle be

`v_1 --e_1-- v_2 --e_2-- ... --e_k-- v_1`,

with indices modulo `k`, where `e_i=v_i v_{i+1}`.

At cycle vertex `v_i`, define

`a_i = q_{e_i,v_i}`,

`b_i = q_{e_{i-1},v_i}`.

Because all incidences at the same vertex have the same denominator,

`a_i/b_i = (w_i/w_{i-1})^alpha`.                            (8.1)

Multiplying (8.1) around the cycle telescopes the weights:

`prod_i a_i = prod_i b_i`.                                  (8.2)

Now look at the `k x k` submatrix of `C` with rows `v_1,...,v_k` and columns `e_1,...,e_k`.  Cycle edge `e_i` is incident only to `v_i,v_{i+1}`, so these `k` rows contain **all** nonzero entries of the selected cycle-edge columns.  Factoring the positive column factors `1/sqrt(w_i)`, the numerator matrix has in row `i` precisely

- `b_i` in column `i-1`, and
- `a_i` in column `i`.

Its determinant has exactly two permutation terms:

`det = prod_i a_i + (-1)^(k-1) prod_i b_i`.                 (8.3)

If `k` is even, (8.2)--(8.3) give `det=0`.  Hence the cycle-edge columns of the **full** matrix `C` are linearly dependent, because those columns have no support outside the cycle rows.  This contradicts full column rank from (5.3).

Therefore:

**Theorem `NM13-13-P0083-NO-EVEN-CYCLE-06`.**  For every `alpha>1`, a not-linearly-unstable finite uniform-firing WARM equilibrium cannot have an even unicyclic positive-support component.  Combining with Theorem 05, every support component is either a tree or is unicyclic with an **odd** unique cycle.

For odd `k`, (8.2)--(8.3) instead give

`det = 2 prod_i a_i > 0`,

so this determinant mechanism stops honestly at odd cycles.  This is not a proof that odd cycles are stable; it is the exact point where this route ceases to contradict stability.  The source's triangle example shows that the odd-cycle distinction is not cosmetic.

Outcome of the cycle half of #25: **success**, eliminating all even cycles but not moving the whisker metric because odd unicycles remain possible below `2`.

## 9. Method #25 again — an alternating-path spectral certificate for every non-whisker tree

The potential form (6.8) also makes the smallest tree obstruction exact without assuming reflection symmetry or majority orientations.

Let

`v_0 -e_1- v_1 - ... -e_L- v_L`

be any simple support path.  Put

`t_{e_i}=(-1)^(i-1)`

on its path edges and `t_e=0` off the path.

At each internal path vertex `v_i`, the two path signs cancel:

`sum_{e incident to v_i} t_e = 0`,

including in the presence of side branches because those branch coordinates were set to zero.

If the endpoints are support leaves, only `v_0` and `v_L` contribute on the left side of (6.8).  Therefore stability forces

`A_{v_0}^2 + A_{v_L}^2
 >= (1/(p+1)) sum_{i=1}^L (A_{v_{i-1}}+A_{v_i})^(p+2)`.       (9.1)

Equivalently define the exact path Rayleigh quotient

`R_path = (A_{v_0}^2+A_{v_L}^2)
          / sum_{i=1}^L (A_{v_{i-1}}+A_{v_i})^(p+2)`.        (9.2)

Every stable/non-linearly-unstable equilibrium must satisfy

`R_path >= 1/(p+1)`.                                        (9.3)

Every tree of diameter at least four has a diameter path with `L>=4` and leaf endpoints, so (9.1)--(9.3) give an exact global obstruction for every non-whisker tree.  No symmetry assumption is present.

Using (6.3), the same quotient can be written purely in normalized edge weights along the path:

`R_path
 = (w_1^(-2 alpha)+w_L^(-2 alpha))
   / sum_{i=1}^L w_i^(1-2 alpha)`.                           (9.4)

Thus one concrete remaining obligation is now finite-dimensional in shape:

> prove, from the equilibrium vertex equations (6.5), that every diameter-at-least-four tree equilibrium with `p<3` has some leaf-to-leaf diameter path for which `R_path < 1/(p+1)`.

That statement would rule out the tree part throughout the source-suggested `alpha>4/3` interval.  It is **not proved in this invocation**, so no threshold movement is claimed.

Outcome of the path half of #25: **successful exact reduction**, but not a source-level threshold improvement.

## 10. What remains, exactly

The previous `alpha>2` theorem already settles the track metric at `2`.  To move below `2`, this run reduces the topology to two sharply defined classes:

1. **odd unicyclic components** — all multi-cycle and even-cycle components are now excluded for every `alpha>1`; and
2. **trees of diameter at least four** — every such tree must satisfy the exact alternating-path stability inequality (9.1).

The cycle determinant cannot itself eliminate odd cycles: its determinant is positive there.  The tree inequality is necessary but has not yet been shown universally impossible for all `p<3`.

So the exact blocker after this invocation is:

`(B_odd/tree)`  For `1<=p<3` (`alpha>4/3`), prove that every source-valid equilibrium on either

- an odd unicyclic support, or
- a tree with diameter at least four

has a test vector violating the generalized incidence bound (6.8).

The simplest unproved special cases are the triangle-with-an-attached-nontrivial-branch family on the odd-cycle side and the four-edge path `P5` on the tree side.  The latter is precisely the shape that the 2016 source paper said it believed should lose full support but did not prove.

This is the **first** unchanged run after four consecutive metric improvements, so Section I does not trigger a stuck-recovery episode.

## 11. Next mechanism rotation

The next invocation should not repeat `#1/#22/#25`.  The planned unused triple is:

- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** use `p=1/(alpha-1)` and study monotonicity/extrema of the forbidden-support generalized Rayleigh quotient on `1<=p<3` rather than treating `alpha` as a fixed opaque exponent;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** compare (6.8) with weighted signless-Laplacian / fastest-mixing-chain extremal eigenvalue inequalities and look specifically for the sharp `1/4` barrier;
- **#29 ADD THE POINTS AT INFINITY:** compactify vertex-potential ratios so an extremizer can be forced either to a boundary degeneration (shorter support) or to an interior critical configuration, avoiding an unproved assumption that the symmetric path is worst.

No SAT/SMT search is justified yet: the new reduction is analytic and continuous.  If it later reduces to finitely many polynomial sign conditions, an exact certificate will be required before any threshold claim.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-13
  namespace: proofnet24/NM13-13/
  source_id: P0083
  claim_file: operations/claims/P0083.md
  canonical_dedup_key: sharp_reinforcement_threshold_for_warm_whiskers
  shard_mod13: 12
  category: HARD_OUTSIDE
  source_status: OPEN
  track_status: PARTIAL
  metric_name: A_whisker_cert
  metric_before: 2
  metric_after: 2
  movement: false
  unchanged_runs_after_last_movement: 1
  hard_recovery_episodes: 0/2
  methods_attempted:
    - 1_CHANGE_THE_CATEGORY
    - 22_READ_THE_FAILURES
    - 25_COUNT_THE_SAME_THING_TWICE
  method_outcomes:
    B1: "proved full-rank incidence => every support component pseudoforest for all alpha>1; derived exact vertex-potential/signless-incidence formulation"
    B22: "identified the alpha=2 barrier as loss of unique >1/2 edge orientation; recovered 2016 four-edge-path failure point"
    B25: "proved no even unicyclic support via telescoping product plus cycle determinant; derived exact alternating-path Rayleigh obstruction for every non-whisker tree"
  new_claims:
    - NM13-13-P0083-PSEUDOFOREST-05
    - NM13-13-P0083-NO-EVEN-CYCLE-06
  finite_checker: NOT_APPLICABLE_THIS_RUN_NO_FINITE_ENUMERATION_OR_NUMERICAL_CLAIM
  audit_P26: NOT_DONE
  audit_NM13_01: NOT_DONE
  closure: false
  next_methods: [5, 17, 29]
  next_step: "attack odd-unicycle and P5 generalized incidence eigenvalue obstruction throughout p<3 (alpha>4/3)"
```

## 13. Delivery boundary

This invocation creates exactly one immutable report in `proofnet24/NM13-13/runs/` and no other file.  It does not edit the canonical claim, shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign ledgers, peer namespaces, email/Gmail, Drive, public surfaces, paid compute, credentials/access controls, workflows, permissions, or schedules.  No audit is requested or presumed.  Readback of this report at its creation commit is required before the invocation is complete.
