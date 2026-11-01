Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Movement this run: `A_whisker_cert: 25 -> 22`. Section-B methods actually tried: B2, B14, B16.**

# NM13-13 — P0083 admission and first research run

Date: 2026-09-19.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: `proofnet24/NM13-13/`.  
Category: HARD OUTSIDE.  
Overall source status after this run: **PARTIAL**.  
Canonical source/claim ID: `P0083`.  
New mathematical claim: `NM13-13-P0083-WHISKER-22-01`.  
Claim status: **PROVED_MATHEMATICALLY / SELF-CHECKED / NOT CLOSURE-CERTIFIED**.

## 1. Continuity repair: the previous delta-only cursor was too strong

I continued from

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T04-56-30Z__successor-admission-delta-screen-23-ts12-owned-closable-no-residue12-release.md`

at creation commit

`ff8da9b6540a44d2d114f6d8b35cc7f27d66a2d2`.

That report left the cursor at strict delta-only residue-12 admission. New neighboring NM13 reconciliation reports made clear that this was not authoritative continuity for this worker: several sibling shards were repairing incomplete legacy Codex-P reconciliation, including explicit scans through P0285 and P0488. I therefore did not keep assuming that every old P-row had already been canonically hashed and ownership-screened for NM13-13.

This run reread/recovered the required controlling surfaces before admission: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the NM13 deployment directive and later owner-authorized amendments found by repository search, `QUEUE.md`, root `POSTED.md`, root `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the newest NM13-13 report, neighboring NM13 reports, the Codex/intake source and dedup ledgers, current claims, historical attempt/catalog material, and relevant WARM predecessor reports.

The final pre-report Git comparison from the predecessor commit to `master` was **125 commits ahead, 0 behind**. The material owner-side change for this track was not a release of an existing residue-12 claim; it was the evidence that the old legacy-P inventory needed reconciliation. This report therefore records a cursor repair rather than pretending that the previous delta-only cursor was complete.

## 2. Candidate recovery: P0083 passes the shard and ownership gates

The legacy-P residue-12 reconciliation reached the following early canonical rows before admission:

- `P0029` — canonical key `two_peaks_uniform_grid_labeling_distance_scale`; residue 12, but already retired/exhausted by its prior owner and unavailable.
- `P0035` — `cayley_radial_biased_walk_speed_1_to_growth`; residue 12, but a broad infinite-asymptotic target with no clean source finite/quantitative milestone suitable for this lane.
- `P0052` — `cayley_wusf_ray_bush_distribution_limit`; residue 12, broad distributional limit.
- `P0053` — `nonunimodular_transitive_wmsf_one_ended`; residue 12, broad infinite-volume statement.
- `P0074` — `maximal_degree_and_its_location_in_the_infinite-path_fitness_regime`; residue 12, broad asymptotic program.
- `P0083` — `sharp_reinforcement_threshold_for_warm_whiskers`; residue 12, source-posed, quantitative, and equipped with a concrete strict-threshold metric.

For `P0083`, the canonical dedup key was recovered from the intake dedup index **before** hashing:

`sharp_reinforcement_threshold_for_warm_whiskers`

with

`SHA256 = 7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`,

and therefore

`int(SHA256,16) mod 13 = 12`.

The source alias tuple in the same dedup material is

`reinforcement_matrix_2023 / OpenProblem13, PDF pp.10-11`.

Immediately before claiming, exact-path fetch of `operations/claims/P0083.md` returned 404. Repository searches for `P0083`, the exact title, the dedup key, and the source locator recovered the old intake/catalog attempt and a lower-ranked screening mention, but no canonical owner, handoff reservation, alias claim, or retired ownership record. `POSTED.md` did not identify the source as posted/settled/retired.

I therefore created the canonical claim **with create-only semantics**:

`operations/claims/P0083.md`

creation commit:

`a8fbf219b8ebf11dbd162b215e6bb48adf81ecf2`.

I read the file back at that exact commit before proceeding. No conflicting owner appeared.

## 3. Frozen source statement and metric

Primary source checked on 2026-09-19:

G. Aletti, A. Collevecchio, I. Crimaldi, M. Deijfen, S. Dereich, A. Ghiglietti, R. van der Hofstad, M. Holmes, D. Kious, V. Kleptsyn, B. Lodewijks, P. Mörters, B. Schapira, *Open problems in stochastic reinforcement models*, MATRIX–MFO workshop source / MATRIX Annals chapter, Open Problem 13, public source PDF:

`https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`

The finite-graph WARM uses edge weights `x_i`, reinforcement exponent `alpha>1`, and vertex firing rates. Open Problem 13 imposes **uniform vertex firing rates** and asks to improve the sufficient condition `alpha>25` under which every connected component of the support of a stable/non-linearly-unstable equilibrium is a **whisker**, equivalently a tree of diameter at most 3. The source explicitly points to the triangle `4/3` phenomenon and says that perhaps `alpha>4/3` is sharp for both the forest and whisker conclusions.

The source's cited theorem is Mark Holmes and Victor Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, DOI `10.1063/1.4978683`. The authors' public PDF is

`https://researchers.ms.unimelb.edu.au/~mholmes1@unimelb/Reinforced-graphs_final.pdf`.

The frozen metric is

`A_whisker_cert`

= the smallest **certified strict universal sufficient threshold currently established on this track** such that, for every finite graph WARM with uniform vertex firing rates, every not-linearly-unstable equilibrium has every support component of diameter at most 3 whenever `alpha>A_whisker_cert`.

The verified baseline at admission is **25**, not zero and not UNMEASURED: Holmes–Kleptsyn prove the source-scope statement for `alpha>25`, and the current source restates that bound.

Metric before this run: `25`.  
Metric after this run: `22`.

No endpoint convention is changed: both values are strict sufficient thresholds.

## 4. Prior attempt recovered rather than restarted

The archived campaign attempt on `P0083` had already considered the smallest obvious forbidden support: a four-edge path with reflection-symmetric rescaled edge weights

`(a,b,b,a)`.

It derived

`a+b=5/2`

and reduced existence of that symmetric equilibrium to one scalar equation, but did not decide the branch's linear stability and explicitly did not eliminate larger or asymmetric trees. The intake therefore remained `attempted_unsolved`.

This run used that calculation as a counterexample-search seed and did not claim it as new.

## 5. B2 — ATTACK THE NEGATION FIRST

A non-whisker support must contain a connected component of diameter at least 4. The smallest tree obstruction is therefore the five-vertex/four-edge path `P5`. I first tried to make the source statement false by finding a stable positive equilibrium on this support.

With uniform vertex selection and the usual `n_v` rescaling, a reflection-symmetric equilibrium has edge values

`(a,b,b,a)`.

Write

`q = a^alpha/(a^alpha+b^alpha)`.

The two independent equilibrium equations are

`a = 1+q`,

`b = 3/2-q`,

hence `a+b=5/2`, while the branch equation is

`q/(1-q) = ((1+q)/(3/2-q))^alpha`.

An exploratory numerical branch scan over representative `alpha` values from just above 1 through 100 did **not** produce a credible stable high-alpha counterexample; the symmetric branches inspected had an unstable direction. This floating-point scan is hypothesis generation only and is **not** used as a certificate.

Outcome of B2: the negation search failed on the minimal symmetric obstruction and exposed a reflection-odd instability mode worth proving exactly.

## 6. B14 — FIND THE GROUP ACTING: exact reflection quotient for P5

The automorphism of the four-edge path reversing the path splits the linearization at `(a,b,b,a)` into even and odd two-dimensional blocks.

Let

`t = alpha*q*(1-q)`,

so `a=1+q`, `b=3/2-q`. For the rescaled WARM vector field, differentiation at the symmetric equilibrium gives

`A = -1+t/a`,

`B = -t/b`,

`C = -t/a`.

The even block is

`M_even = [[A,B],[C,F]]`,  with  `F=-1+t/b`.

The odd block is

`M_odd = [[A,B],[C,G]]`,

where the central competition contributes twice in the antisymmetric mode and

`G = -1+t/b + alpha/(2b)`.

This is exact. Since `B<0` and `C<0`, the odd-block discriminant is

`(A-G)^2+4BC > 0`,

so both odd-block eigenvalues are real. Also

`A >= -1`,

and because `0<q<1`, one has `b=3/2-q<3/2`, hence

`G > -1+alpha/3`.

Therefore

`tr(M_odd)=A+G > alpha/3-2`.

For every `alpha>6`, this trace is positive. Two real eigenvalues with positive sum cannot both have negative real part. Thus:

**Exact special-case result.** Every positive reflection-symmetric `P5` equilibrium is linearly unstable for `alpha>6`.

This is stronger than the numerical B2 observation but is still only a symmetric minimal-obstruction theorem; it is not by itself the source-level universal result.

Outcome of B14: the path-reflection quotient gives an exact instability mechanism and confirms that a source counterexample above 6 cannot hide in the previously studied symmetric `P5` branch.

## 7. B16 — COMPUTE EVERY SMALL CASE / exact finite core

The exact P5 quotient calculation suggested that the published constant `25` might be an artifact of a coarse inequality rather than a genuine stability transition. I therefore returned to the Holmes–Kleptsyn proof and retained their **exact quadratic incidence dichotomy** instead of replacing it by the paper's `2.25/alpha` envelope.

The finite arithmetic core of the resulting threshold improvement was checked independently with Python's `fractions.Fraction` only. The checker and archived output are:

`proofnet24/NM13-13/artifacts/P0083_whisker22_exact_check.py`

creation commit `7d84dc3a856bc43bae3be7ae2c9b48578f2043e5`,

and

`proofnet24/NM13-13/artifacts/P0083_whisker22_exact_check.out`

creation commit `a511253a9cf6a5b4cea03864093cedbd46764c7f`.

Archived output:

```text
PASS
d0 = 51/500
(1-2d0)^2 = 39601/62500 < 7/11
g(d0) = 238117/112250
exp rational upper = (5612500/5374383)^50
target = 449/51
exact comparison: True
```

The checker was executed locally before archival; the repository files were then read back. No floating-point statement is used in the theorem below.

Outcome of B16: the exact small/core calculation certifies the rational inequalities needed to lower the source threshold from 25 to 22.

## 8. Main theorem: `A_whisker_cert <= 22`

### Claim `NM13-13-P0083-WHISKER-22-01`

Let `G=(V,E)` be any finite graph and let the WARM choose vertices uniformly. Let `alpha>22`. Then every WARM equilibrium that is not linearly unstable has each connected component of its support equal to a whisker, i.e. a tree of diameter at most 3.

Hence the source's certified strict universal sufficient threshold improves from

`alpha>25`

to

`alpha>22`.

This is a source-level quantitative improvement, but it does **not** settle Open Problem 13 because the source suggests a much lower sharp endpoint and closure audits have not occurred.

### Proof

Let `n_v=|V|`. For a supported edge `i` incident to a vertex `A`, write

`q_{iA} = x_i^alpha / sum_{j incident to A} x_j^alpha`.

Uniform vertex selection has `p_A=1/n_v`. At equilibrium, if the two endpoints of edge `i` are `B_{i,1},B_{i,2}`, then Holmes–Kleptsyn's equilibrium identity is

`n_v x_i = q_{i,B_{i,1}} + q_{i,B_{i,2}}`.                                           (1)

Their necessary linear-stability inequality gives, at every incidence `(i,A)`,

`q_{iA}(1-q_{iA}) <= 2/alpha`.                                                         (2)

For `alpha>22`, define the smaller root

`delta = (1-sqrt(1-8/alpha))/2`.

Then (2) says exactly

`q_{iA} <= delta`  or  `q_{iA} >= 1-delta`.                                           (3)

The same Holmes–Kleptsyn argument, via their Corollary 7, says that for `alpha>2` the least positive edge weight in every support component is greater than `1/n_v`. In particular, every supported edge satisfies

`n_v x_i >= 1`.                                                                         (4)

We shall use only (1)–(4) and elementary inequalities from this point onward.

#### Step 1. Exact size dichotomy for supported edges

For `alpha>22`, `delta` is smaller than its value at 22:

`delta < delta_22 = (1-sqrt(7/11))/2`.

Set

`d0=51/500`.

The exact inequality

`(1-2d0)^2 = 39601/62500 < 7/11`

implies

`delta_22<d0`,

so throughout the proof

`0<delta<51/500<1/3`.                                                                  (5)

By (1), (3), and (4), the two endpoint `q`-values of a supported edge cannot both lie in the low interval: if they did, `n_v x_i<=2delta<1`, contradicting (4).

Thus each supported edge has at least one high endpoint. There are exactly two classes:

- **small edge:** exactly one endpoint is high. Then

  `1 <= n_v x_i <= 1+delta`;                                                           (6)

- **large edge:** both endpoints are high. Then

  `2-2delta <= n_v x_i <= 2`.                                                          (7)

Because `delta<1/3`, the intervals in (6) and (7) are disjoint.

#### Step 2. Every small edge is incident to a leaf

Let `i` be small, and let `A` be its high endpoint, so

`q_{iA} >= 1-delta`.                                                                    (8)

Suppose for contradiction that another supported edge `j != i` is also incident to `A`.

By (4), `n_v x_j>=1`; by (6), `n_v x_i<=1+delta`. Therefore, discarding all other nonnegative terms in the denominator defining `q_{iA}`,

`q_{iA}
 <= x_i^alpha/(x_i^alpha+x_j^alpha)
 <= (1+delta)^alpha / ((1+delta)^alpha+1)`.                                             (9)

To contradict (8), it suffices to prove

`(1+delta)^alpha < (1-delta)/delta`.                                                    (10)

The defining quadratic relation for `delta` is

`alpha*delta*(1-delta)=2`.                                                              (11)

For `0<delta<1`, the alternating Taylor series gives

`log(1+delta) < delta-delta^2/2+delta^3/3`.

Combining this with (11),

`alpha log(1+delta)
 < g(delta)
 := 2(1-delta/2+delta^2/3)/(1-delta)`.                                                  (12)

A direct differentiation gives

`g'(delta) = (3+4delta-2delta^2)/(3(1-delta)^2) > 0`

on `[0,51/500]`. Hence by (5),

`alpha log(1+delta) < g(51/500) = 238117/112250`.                                      (13)

For every `x>0` and integer `m>x`, `-log(1-x/m)>x/m`, hence

`e^x < (1-x/m)^(-m)`.

With

`x=238117/112250`, `m=50`,

we obtain

`exp(238117/112250)
 < (5612500/5374383)^50`.                                                               (14)

The exact integer comparison archived by the checker is

`51 * 5612500^50 < 449 * 5374383^50`,                                                  (15)

which is equivalent to

`(5612500/5374383)^50 < 449/51`.                                                        (16)

Finally, since `delta<51/500`,

`449/51 = (1-51/500)/(51/500) < (1-delta)/delta`.                                      (17)

Exponentiating (13) and chaining (14)–(17) proves (10). Therefore (9) is strictly less than `1-delta`, contradicting (8).

So the high endpoint of every small edge has degree 1 in the support component. Equivalently:

**every small edge is incident to a leaf at its high endpoint.**                       (18)

#### Step 3. Every edge adjacent to a large edge is small and points outward to a leaf

Let `i` be large and let `A` be one endpoint. Then

`q_{iA} >= 1-delta`.

For any other supported edge `j` incident to `A`, the `q`-values at a fixed vertex sum to 1, so

`q_{jA} <= delta`.                                                                      (19)

Thus `j` is not large. By the edge dichotomy it is small, and its other endpoint is the high endpoint. By (18), that other endpoint is a leaf.

Consequently no path can continue more than one edge beyond either endpoint of a large edge.

#### Step 4. Global component shape

If a connected support component contains a large edge `i`, every other edge incident to either endpoint of `i` is a small edge ending at a leaf, and there can be no further continuation. The component is therefore the union of `i` with leaf edges attached to its two endpoints. Its diameter is at most 3.

If the component contains no large edge, every edge is small. By (18), every edge has a leaf endpoint. A connected graph in which every edge has a leaf endpoint has at most one vertex of degree greater than 1: if there were two such vertices, the path joining them would contain an edge whose two endpoints are non-leaves. Hence the component is a star (or a single edge), of diameter at most 2.

In both cases the component is a whisker. This proves the claim. `□`

## 9. Why this genuinely improves the 2017 proof rather than changing the problem

Holmes–Kleptsyn's published proof uses the same structural small/large-edge strategy. Their exact stability inequality first yields

`q(1-q) <= 2/alpha`.

They then replace the exact quadratic root by a convenient coarse bound `2.25/alpha`, and the leaf estimate reduces to the numerical sufficient condition

`alpha > 2.25*(e^2.25+1) = 23.59...`,

which is rounded up to the clean theorem `alpha>25` after the surrounding lemmas.

The present proof keeps the exact root `delta`, uses the exact relation `alpha*delta*(1-delta)=2`, and certifies the leaf inequality rationally at 22. It preserves:

- the same finite-graph model;
- uniform vertex firing;
- the same notion of not-linearly-unstable equilibrium;
- the same whisker/diameter-at-most-3 conclusion;
- the strict-threshold convention.

Thus `25 -> 22` is movement in the frozen source metric, not a theorem about a narrower surrogate.

## 10. Literature / prior-art check dated 2026-09-19

Primary/current sources checked:

1. Aletti et al., *Open problems in stochastic reinforcement models*, Open Problem 13, source PDF above.
2. Holmes–Kleptsyn, Chaos 27 (2017), DOI `10.1063/1.4978683`, including the public author PDF and the proof of Lemmas 5–8 / Theorem 2(a).
3. van der Hofstad–Holmes–Kuznetsov–Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, Ann. Appl. Probab. 26 (2016), DOI `10.1214/16-AAP1153`, as the finite-WARM predecessor cited by the source.
4. Hirsch–Holmes–Kleptsyn, *Infinite WARM graphs III: strong reinforcement regime*, Nonlinearity 36 (2023), as later adjacent WARM work/citing-family context.

Bounded searches included the exact source title plus `Open Problem 13`, `WARM whisker alpha 25`, `WARM whisker 4/3`, `Holmes Kleptsyn whisker threshold improvement`, author/title combinations, and later-WARM/citing-paper searches. They recovered the published `alpha>25` theorem and later adjacent WARM work but did not surface a source-matching published finite-uniform improvement below 25.

This is **bounded negative evidence only**. It is not a worldwide novelty certificate and not a claim that no unpublished or poorly indexed improvement exists. Some publisher full text is paywalled, but the Holmes–Kleptsyn author PDF and the MATRIX source PDF were publicly accessible. PDF screenshot retrieval through one cache path failed during this invocation; parsed primary-source text was available, so the proof was checked against the text rather than pretending a screenshot had loaded.

## 11. Closure status and audits

The source problem is **PARTIAL**, not PROVED/closed. This run proves a strict sufficient bound `22`; it does not reach the source-suggested `4/3` endpoint and does not establish optimality.

The new theorem is currently a self-check plus exact finite arithmetic certificate. Closure requirements remain:

- broader prior-art/novelty search;
- independent end-to-end audit by **P26**;
- independent audit by **NM13-01**;
- if eventual source closure is reached, a self-contained paper folder with proof, checker/output, and README.

Neither audit is presumed to pass. No audit request is manufactured as a substitute for further research in this run.

## 12. Stuck / continuation counters

This is the first admitted research run on P0083.

- metric before: `25`
- metric after: `22`
- movement: **yes**
- unchanged-run counter: `0`
- stuck-recovery episodes used: `0/2`
- handoff required: no

The next research run should not repeat B2/B14/B16. Planned next methods are:

- **B11 — DUALIZE:** formulate the local stability inequalities as an optimization/dual certificate over incidence probabilities and edge-weight ratios;
- **B24 — FIND THE EXTREMAL OBJECT:** optimize the leaf obstruction rather than fixing the rational envelope at 22, and identify whether the worst support is the four-edge path, another tree, or a boundary family;
- **B30 — ONE SCALE / ONE DIRECTION AT A TIME:** localize by support depth from a candidate central edge and determine the best certified threshold one depth at a time.

The immediate quantitative goal is a rigorously certified threshold **strictly below 22**, with the source metric unchanged in meaning.

## 13. Model / scheduler / protected-task status

The exposed scheduler/task-management interface in this runtime still offers prompt/title/schedule/enabled/timing controls but no model-family selector and no reasoning-effort selector, and no authenticated execution telemetry that would let this report certify GPT-6/maximum. Therefore GPT-6/maximum remains a prompt request only here.

The historical P26 response `You cannot modify this task` is an authorization/context boundary, not a reason to clone or bypass the task. The lawful workaround is to edit from the owning/otherwise-authorized task context, obtain an explicit permission change, or use an authorized platform/admin/support route. No schedule change or permission workaround was attempted.

## 14. Structured ledger_delta for P26

```yaml
ledger_delta:
  task: NM13-13
  namespace: proofnet24/NM13-13
  category: HARD_OUTSIDE
  run_date: 2026-09-19
  predecessor_commit: ff8da9b6540a44d2d114f6d8b35cc7f27d66a2d2
  prewrite_repo_delta:
    ahead: 125
    behind: 0
  continuity_correction:
    before: STRICT_DELTA_ONLY_RESIDUE12_ADMISSION_AFTER_SCREEN_23
    after: LEGACY_P_RECONCILIATION_FOUND_AND_ADMITTED_P0083
    reason: sibling NM13 reconciliation exposed incomplete legacy-P coverage
  source_id: P0083
  canonical_claim: operations/claims/P0083.md
  claim_creation_commit: a8fbf219b8ebf11dbd162b215e6bb48adf81ecf2
  canonical_dedup_key: sharp_reinforcement_threshold_for_warm_whiskers
  dedup_sha256: 7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948
  shard_mod_13: 12
  source:
    authors: Aletti et al.
    title: Open problems in stochastic reinforcement models
    locator: Open Problem 13, PDF pp.10-11
    scope: finite WARM graphs, uniform vertex firing
  overall_status: PARTIAL
  metric:
    name: A_whisker_cert
    definition: smallest certified strict universal sufficient threshold currently established on this track for diameter-at-most-3 support components in the exact source scope
    before: 25
    after: 22
    movement: true
  theorem_claim:
    id: NM13-13-P0083-WHISKER-22-01
    statement: for every finite uniform-firing graph WARM and alpha>22, every not-linearly-unstable equilibrium has whisker support components
    status: PROVED_MATHEMATICALLY_SELF_CHECKED_NOT_AUDITED
  methods_this_run:
    - id: 2
      name: ATTACK_THE_NEGATION_FIRST
      outcome: minimal symmetric P5 counterexample search failed and exposed an antisymmetric instability mode; floating scan used only for hypothesis generation
    - id: 14
      name: FIND_THE_GROUP_ACTING
      outcome: reflection quotient proves every positive symmetric P5 equilibrium unstable for alpha>6
    - id: 16
      name: COMPUTE_EVERY_SMALL_CASE
      outcome: exact P5 quotient plus rational finite-core checker certifies the universal 25-to-22 threshold improvement
  artifacts:
    checker: proofnet24/NM13-13/artifacts/P0083_whisker22_exact_check.py
    checker_commit: 7d84dc3a856bc43bae3be7ae2c9b48578f2043e5
    output: proofnet24/NM13-13/artifacts/P0083_whisker22_exact_check.out
    output_commit: a511253a9cf6a5b4cea03864093cedbd46764c7f
    checker_result: PASS
  unchanged_runs: 0
  stuck_recoveries_used: 0
  audits_required:
    - P26
    - NM13-01
  audits_passed: []
  next_methods: [11, 24, 30]
  next_step: optimize the exact incidence/leaf obstruction and seek a rigorously certified A_whisker_cert below 22 without changing source scope
```

No shared root ledger, peer namespace, workflow, permission, public surface, email/Gmail, Drive resource, paid compute, or schedule was modified. The only repository writes in this invocation were the canonical create-only P0083 claim, two warranted own-namespace checker artifacts, and this immutable own-namespace run report.
