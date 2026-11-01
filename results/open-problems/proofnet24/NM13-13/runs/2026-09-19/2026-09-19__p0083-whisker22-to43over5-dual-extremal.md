Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `A_whisker_cert: 22 -> 43/5`; actual Section-B methods tried: #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# NM13-13 — P0083 second substantive run: self-consistent leaf obstruction lowers the whisker threshold to 43/5

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-13` / `proofnet24/NM13-13/`  
Category: **HARD OUTSIDE**  
Canonical source / claim: `P0083` / `operations/claims/P0083.md`  
Source status: **OPEN**  
Track status after this invocation: **PARTIAL / CLAIM RETAINED**

## 1. Runtime and scheduler-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`. This invocation actually identifies as **GPT-5.6 Sol**. The exposed runtime provides no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The exposed task-control surface still provides title/prompt, schedule or relative-start fields, timing mode, enabled state, and list/update controls. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort receipt**. Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy runtime attestation.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary. Current repository continuity records a later successful P26 update from an authorized context. The lawful workaround for any future denial is the same task's owning or otherwise authorized account/workspace/API/admin context, or authorized platform support; it is not task duplication, identity substitution, or a permission bypass. This invocation changes no scheduler or permission.

## 2. Authoritative continuity recovered before research

The controlling predecessor is

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19__p0083-admission-whisker25-to22.md`

created at commit

`5d2e9f0b2e27a1c7fe620f301fcc7da03f59a5ba`.

Its durable state is preserved:

- `P0083` is already admitted and exclusively owned by NM13-13;
- canonical dedup key `sharp_reinforcement_threshold_for_warm_whiskers`, SHA-256 `7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`, residue `12 mod 13`;
- source statement is Aletti et al. Open Problem 13: improve the finite uniform-firing WARM whisker sufficient threshold `alpha>25`;
- frozen metric `A_whisker_cert` is the smallest certified **strict universal sufficient threshold currently established on this track** for the source-scope conclusion that every not-linearly-unstable equilibrium has support components of diameter at most 3;
- admission baseline was `25`, and the first substantive run proved `25 -> 22`;
- status remained PARTIAL rather than closed because the source suggests the much lower `4/3` scale and no two-auditor closure exists;
- methods #2/#14/#16 were genuinely used in the preceding run and are not repeated here;
- planned methods for the continuation were #11/#24/#30;
- unchanged-run counter after the movement run was `0`; HARD stuck-recovery count `0/2`.

Before new mathematics I freshly read or recovered the required current surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the predecessor report; `operations/claims/P0083.md`; P0083 intake/dedup/attempt material; the newest visible NM13-12 and NM13-01 reports; and the adjacent P13 WARM-forest history. The P0083 intake/campaign record remains `attempted_unsolved`, and the canonical key remains present in the F-intake dedup index.

No relevant private-repository history was inaccessible. The append-only intake corpus is too large to claim every unchanged historical byte was freshly rendered model-visible, and I make no such claim; P0083-specific source, dedup, attempt, claim, and continuity evidence was reopened directly.

## 3. Exact predecessor-to-prewrite repository delta

Frozen final prewrite `master` snapshot:

`fc1c8b6d584866cc4b15b43dd2db5f3de064d01e`.

Exact comparison:

`5d2e9f0b2e27a1c7fe620f301fcc7da03f59a5ba .. fc1c8b6d584866cc4b15b43dd2db5f3de064d01e`

reported:

- status `ahead`;
- commits ahead **90**;
- commits behind **0**;
- total commits **90**;
- `too_large = null`, so the returned changed-file set is complete for this interval.

Admission/continuity consequences relevant to P0083:

- `operations/claims/P0083.md` was not modified or released;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, intake `problems.jsonl`, probability attempt ledgers, and controlling owner/NM13 policy files did not change;
- new claims elsewhere, including `P0411` and `P0458`, do not collide with P0083;
- the newest NM13-12 report explicitly recognizes P0083 as NM13-13's admitted source with prior movement `25 -> 22`;
- the newest NM13-01 report likewise records P0083 as owned by NM13-13, HARD OUTSIDE, canonical residue 12.

This run therefore continues the admitted P0083 target; it does not reopen admission or create a duplicate claim.

## 4. Fresh source and literature check — 2026-09-19 UTC

Primary source checked directly:

1. G. Aletti et al., *Open problems in stochastic reinforcement models*, MATRIX Annals, DOI `10.1007/978-3-031-76738-8_29`, public PDF `https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`. The source states that for finite graphs, equilibria reached by the stochastic process cannot be linearly unstable, that the known uniform-firing whisker result is `alpha>25`, and **Open Problem 13** asks to improve that lower bound; immediately afterward it notes the triangle transition at `4/3` and says perhaps `alpha>4/3` is sharp.
2. M. Holmes and V. Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, DOI `10.1063/1.4978683`, public author PDF `https://researchers.ms.unimelb.edu.au/~mholmes1@unimelb/Reinforced-graphs_final.pdf`. I checked the proof pages containing the incidence dichotomy, equilibrium identity, least-positive-edge input, leaf lemma, and adjacent-large-edge lemma.
3. Adjacent/later WARM literature checked included the van der Hofstad--Holmes--Kuznetsov--Ruszel finite-WARM predecessor and Hirsch--Holmes--Kleptsyn's infinite-WARM work. These concern the same model family but did not supply a source-matching finite uniform-firing whisker threshold below the published 25 in the bounded search.

Dated bounded searches included exact source-title + `Open Problem 13`, `WARM whisker alpha 25 2026`, `Proof of the WARM whisker conjecture threshold improvement`, `WARM whisker 4/3`, and author/title/citation-family combinations. They recovered the 2017 `alpha>25` theorem, the 2025 open-problems source, and later infinite-WARM work, but no checked primary source claiming the finite-uniform source result below 25.

This is **bounded negative evidence only**, not proof of worldwide openness, priority, or novelty. The source and author PDFs were directly accessible and visually inspected at the relevant pages during this invocation; some publisher pages expose only metadata/abstracts.

## 5. Frozen metric and movement

The metric is unchanged in definition:

`A_whisker_cert`

= the smallest **certified strict universal sufficient threshold currently established on this track** such that, for every finite-graph WARM with uniform vertex firing rates, every equilibrium that is not linearly unstable has every support component of diameter at most 3 whenever `alpha>A_whisker_cert`.

Before this invocation: **22**.  
After this invocation: **43/5 = 8.6**.

The strict-threshold convention and source scope are unchanged. No invented zero or surrogate metric is introduced.

## 6. Research idea written before checker code

The `22` proof still inherited one coarse step from the old leaf argument: after an edge `i` was classified as small, it bounded its rescaled weight by `n_v x_i <= 1+delta`, forgetting that the high-end incidence probability `r=q_{iA}` itself appears in the equilibrium identity. The new route keeps that self-consistency.

For a small edge with high endpoint `A`, write

`r := q_{iA}`.

At its other endpoint the incidence probability is at most `delta`, so the exact equilibrium relation gives

`n_v x_i <= r+delta`,

not merely `1+delta`.

If `A` had a second supported edge `j`, the least-positive-weight theorem gives `n_v x_j>1`. Therefore the very definition of `r` forces

`r < (r+delta)^alpha / ((r+delta)^alpha+1)`,

or equivalently

`(r+delta)^alpha > r/(1-r)`.                                      (6.1)

The research problem has become one-dimensional: prove that (6.1) is impossible throughout the high-incidence interval. This is the new route. Only after deriving a rational exact envelope for that one-dimensional obstruction did I write a checker.

## 7. Section-B #11 — DUALIZE: turn the leaf question into a scalar fixed-point obstruction

The old proof treated the high-incidence condition `r>=1-delta` and the competitor condition independently. The dual viewpoint is to make them fight each other through the same scalar `r`.

The necessary non-leaf condition derived above is

`(r+delta)^alpha > r/(1-r)`,                                      (7.1)

while stability requires

`r >= 1-delta`.                                                    (7.2)

Thus the high endpoint can fail to be a leaf only if the reinforcement amplification map beats the odds map on the entire admissible interval. The dualized obstruction is the ratio

`R_alpha(r) := ((1-r)/r) (r+delta(alpha))^alpha`.

A non-leaf high endpoint requires `R_alpha(r)>1`; proving `R_alpha(r)<1` uniformly certifies the leaf.

**B11 outcome: worked.** It removes the main loss in the `22` proof by replacing the worst-case weight `1+delta` with the self-consistent weight `r+delta`.

## 8. Section-B #24 — FIND THE EXTREMAL OBJECT: exact worst local non-leaf configuration

Let

`delta(alpha) = (1-sqrt(1-8/alpha))/2`,

so

`alpha delta(1-delta)=2`.                                         (8.1)

Take the rational anchor

`a0=43/5`, `d0=46/125`.

At `a0`,

`delta(a0)=(1-sqrt(3/43))/2 < 46/125=d0`,                         (8.2)

because (8.2) is equivalent to `sqrt(3/43)>33/125`, and after squaring

`3*125^2 - 43*33^2 = 48 > 0`.

### 8.1 Monotonic transfer from every `alpha>=a0` to the rational anchor

Fix `alpha>=a0` and a possible high incidence `r>=1-delta(alpha)` with `r<1`. For `beta in [a0,alpha]` define

`H(beta)=beta log(r+delta(beta))`.

From (8.1),

`delta'(beta) = -delta(1-delta)/(beta(1-2delta))`.

Putting `z=r+delta(beta)`,

`H'(beta)=log z - delta(1-delta)/((1-2delta)z)`.                   (8.3)

Because `delta(beta)>=delta(alpha)`, one has `r>=1-delta(beta)`, so `z>=1`; and because `r<1`, `z<1+delta`. Hence

`log z < z-1 < delta`,

while

`delta(1-delta)/((1-2delta)z)
 > delta(1-delta)/((1-2delta)(1+delta))
 > delta`,                                                        (8.4)

since

`1-delta > (1-2delta)(1+delta)=1-delta-2delta^2`.

Thus `H'(beta)<0`. Therefore

`(r+delta(alpha))^alpha
 <= (r+delta(a0))^a0
 < (r+d0)^a0`.                                                     (8.5)

So it suffices to solve one fixed rational-envelope extremal problem.

### 8.2 Exact extremal point at the anchor

Put `s=1-r`. Since `r>=1-delta(alpha)` and `delta(alpha)<d0`,

`0<s<d0`.

The desired contradiction to (7.1) follows if

`R(s):= [s/(1-s)] (1+d0-s)^(43/5) < 1`                           (8.6)

for all `0<s<=d0`.

Its logarithmic derivative has the sign of

`43 s^2 - 48 s + 171/25`.                                       (8.7)

The two roots are

`s_-=(120-9 sqrt(87))/215`,

`s_+=(120+9 sqrt(87))/215`.

The second lies above `d0`; the first lies inside `(0,d0)`. Hence `R` rises to `s_-` and then falls on the relevant interval. The unique interior extremal obstruction is therefore `s_-`.

Two exact rational brackets suffice:

`1/6 < s_- < 21/125`.                                            (8.8)

The lower inequality follows by squaring `505>54 sqrt(87)`; its exact square gap is

`505^2-54^2*87 = 1333 >0`.

The upper inequality follows by squaring `10485<1125 sqrt(87)`; its exact square gap is

`1125^2*87-10485^2 = 174150 >0`.

Consequently

`s_-/(1-s_-) < 21/104`,

and

`1+d0-s_- < 171/125-1/6 = 901/750`.

Therefore

`R(s_-) < (21/104) (901/750)^(43/5)`.                            (8.9)

Raise (8.9) to the fifth power. The exact integer inequality

`21^5 * 901^43 < 104^5 * 750^43`                                 (8.10)

shows that the right side of (8.9) is strictly below 1. At the interval endpoint,

`R(d0)=d0/(1-d0)=46/79<1`,

and `R(s)->0` as `s->0`. Thus (8.6) holds everywhere.

**B24 outcome: worked.** The extremal local non-leaf configuration is a one-dimensional algebraic critical point, and a short rational enclosure certifies it away from 1 at `alpha=43/5`.

Exploratory floating-point work, used only for route selection and not as evidence, suggests this particular self-consistent leaf inequality becomes tight around `alpha≈8.543`. Thus the present local architecture has nearly exhausted its own leverage; getting anywhere near `4/3` will require a qualitatively different instability/global argument rather than repeated polishing of this scalar envelope.

## 9. Section-B #30 — ONE SCALE / ONE DIRECTION AT A TIME: depth-one leaf obstruction to the global whisker shape

The source conclusion is global, but after the incidence dichotomy the only source-relevant local obstruction is depth one: can a small edge's high endpoint have another supported edge?

The calculation above answers **no** for `alpha>43/5`. Once that one direction is closed, no second large-scale enumeration is needed:

1. every small edge has a leaf at its high endpoint;
2. any edge adjacent to a large edge is small, because the large edge already consumes at least `1-delta` of the incidence probability at their common vertex;
3. that adjacent small edge therefore points outward to a leaf;
4. if there is no large edge, every edge has a leaf endpoint, forcing a connected component to be a star.

**B30 outcome: worked.** Localizing to the single depth-one obstruction turns the global diameter statement into a deterministic graph-shape consequence with no further threshold loss.

## 10. Main theorem — `A_whisker_cert <= 43/5`

### Claim `NM13-13-P0083-WHISKER-43OVER5-02`

Let `G=(V,E)` be any finite graph. Consider the graph WARM with uniform vertex firing rates and reinforcement exponent

`alpha > 43/5`.

Then every equilibrium that is not linearly unstable has every connected component of its support equal to a whisker, i.e. a tree of diameter at most 3.

Hence the source-valid strict sufficient threshold improves in this track from

`alpha>22`

to

`alpha>43/5`.

This is a genuine source-level quantitative improvement, but **not** closure of Open Problem 13.

### Proof

Let `n_v=|V|`. For a supported edge `i` incident to vertex `A`, define

`q_{iA}=x_i^alpha / sum_{j incident to A} x_j^alpha`.

For uniform firing the Holmes--Kleptsyn equilibrium identity is

`n_v x_i = q_{iB_1}+q_{iB_2}`                                   (10.1)

for the two endpoints `B_1,B_2` of `i`.

Their necessary not-linearly-unstable condition yields at each incidence

`q_{iA}(1-q_{iA}) <= 2/alpha`.                                   (10.2)

Their Corollary-7 input gives, for `alpha>2`, that every supported edge has

`n_v x_i > 1`.                                                    (10.3)

For `alpha>43/5>8`, set

`delta=(1-sqrt(1-8/alpha))/2`.

The two roots of `q(1-q)=2/alpha` are `delta` and `1-delta`; hence (10.2) gives

`q_{iA}<=delta` or `q_{iA}>=1-delta`.                            (10.4)

Because `delta<1/2`, the two endpoint incidences of a supported edge cannot both be low: otherwise (10.1) would give `n_v x_i<=2delta<1`, contradicting (10.3).

Call an edge **small** when exactly one endpoint incidence is high, and **large** when both are high.

#### Lemma 10.1. Every small edge has a leaf as its high endpoint.

Let `i` be small and let `A` be its high endpoint. Put

`r=q_{iA}>=1-delta`.

Let `t` be the incidence at the other endpoint. Since `i` is small, `t<=delta`; by (10.1),

`n_v x_i=r+t<=r+delta`.                                          (10.5)

Suppose `A` is not a leaf of the support. Then some other supported edge `j` is incident to `A`. By (10.3),

`n_v x_j>1`.                                                      (10.6)

The quantities `q` are unchanged by the common rescaling `x -> n_v x`, so (10.5), (10.6), and the denominator defining `q_{iA}` imply, strictly,

`r=q_{iA}
 < (r+delta)^alpha / ((r+delta)^alpha+1)`.                        (10.7)

Rearranging (10.7),

`(r+delta)^alpha > r/(1-r)`.                                     (10.8)

We prove the reverse inequality.

Let `a0=43/5`, `d0=46/125`. As shown in (8.2), `delta(a0)<d0`. For fixed `r` and `beta in [a0,alpha]`, define `H(beta)=beta log(r+delta(beta))`. Equations (8.3)--(8.4) prove `H'(beta)<0`, so

`(r+delta)^alpha < (r+d0)^(43/5)`.                               (10.9)

Set `s=1-r`. Then `0<s<d0`. Section 8.2 proves exactly that

`[s/(1-s)] (1+d0-s)^(43/5)<1`,                                  (10.10)

which is equivalent to

`(r+d0)^(43/5)<r/(1-r)`.                                         (10.11)

Combining (10.9) and (10.11) contradicts (10.8). Therefore `A` is a leaf. `□`

#### Lemma 10.2. Every edge adjacent to a large edge is small and points outward to a leaf.

Let large edge `i` and another supported edge `j` meet at `A`. Since

`q_{iA}>=1-delta`

and the incidence probabilities at `A` sum to 1,

`q_{jA}<=delta`.

Therefore `j` cannot be large. It is small, its high endpoint is its other endpoint, and Lemma 10.1 makes that endpoint a leaf. `□`

#### Global shape

If a connected support component contains a large edge `i`, every other edge incident to either endpoint of `i` is, by Lemma 10.2, a small edge whose opposite endpoint is a leaf. Such an edge cannot continue farther. Hence the entire component is the union of `i` and leaf edges attached to the endpoints of `i`; its diameter is at most 3.

If a connected support component contains no large edge, every edge is small. Lemma 10.1 says every edge has a leaf endpoint. A connected graph with that property has at most one vertex of degree greater than 1: if two such vertices existed, a path joining them would contain an edge whose two endpoints were non-leaves. Thus the component is a star (or a single edge), of diameter at most 2.

Every support component is therefore a whisker. This proves the theorem. `□`

## 11. Exact finite core and independent self-check

The theorem-sized argument is written in full above. The finite arithmetic core was independently executed with Python standard-library exact rational/integer arithmetic only, after the idea and analytic reduction were written down.

Checker:

`proofnet24/NM13-13/artifacts/P0083_whisker43over5_exact_check.py`

creation commit:

`0550fe165bd703b064b2ba23b62ec7f67c2d8dbd`.

Archived output:

`proofnet24/NM13-13/artifacts/P0083_whisker43over5_exact_check.out`

creation commit:

`0010ea58d5f17398401a2aed48594fc983d0d1eb`.

The archived output is:

```text
PASS
alpha0 = 43/5
d0 = 46/125
delta0<d0 square-gap = 48
s*>1/6 square-gap = 1333
s*<21/125 square-gap = 174150
critical-envelope fifth-power integer comparison = True
critical-envelope integer gap = 5458334334256733985481842865188939633817139673043126332428646825702001303300976545206492026689344476883042029624540259162055457777199
endpoint R(d0) = 46/79
```

Both artifact files were read back at their creation commits. This is a **self-check**, not an independent audit.

## 12. Why this is not just another checker run

The movement comes from a new mathematical route, not from replacing one numerical bound with a larger certificate:

- #11 exposed the missing self-consistency variable `r` and converted the leaf problem to a scalar fixed-point obstruction;
- #24 identified and solved the exact worst local obstruction at a rational anchor;
- #30 showed that this single local obstruction controls the whole support-component diameter without further search.

Only after those three ideas gave the candidate `43/5` theorem was the finite algebra checked. The checker contains no search over graphs, no floating-point acceptance criterion, and no hidden heuristic step.

## 13. Status, audits, counters, and next route

The source remains **OPEN / track PARTIAL**. This run does not claim the source-suggested `4/3` endpoint, optimality, worldwide novelty, or closure.

Independent audit status:

- P26: **NOT AUDITED / no PASS presumed**;
- designated secondary auditor NM13-01: **NOT AUDITED / no PASS presumed**.

Because the metric moved, the admitted-source unchanged-run counter is reset/remains

`0`.

HARD stuck-recovery episodes remain

`0/2`.

The scalar leaf route is now close to its own apparent numerical barrier near `8.543` and is not a plausible road to `4/3`. The next run should therefore change mechanism rather than squeeze this envelope again. Planned unused Section-B moves are:

- **#3 PROVE SOMETHING STRONGER:** seek a direct positive-eigenvalue certificate for every non-whisker support rather than a leaf-weight contradiction;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** study asymmetric minimal diameter-4 trees beyond the reflection quotient already used in the first run;
- **#18 SAY IT IN ANOTHER LANGUAGE:** rewrite the linearized WARM stability condition as a weighted incidence/Laplacian or matrix comparison problem and look for a support-diameter spectral obstruction.

No audit request or paper package is warranted yet; research continues on the same admitted source.

## 14. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-13
  namespace: proofnet24/NM13-13
  category: HARD_OUTSIDE
  source_id: P0083
  claim_id: P0083
  claim_status: ACTIVE
  source_status: OPEN
  track_status_before: PARTIAL
  track_status_after: PARTIAL
  metric_name: A_whisker_cert
  metric_definition: smallest certified strict universal sufficient threshold currently established on this track for uniform-firing finite-WARM whisker support of every not-linearly-unstable equilibrium
  metric_before: "22"
  metric_after: "43/5"
  mathematical_movement: true
  theorem_claim: NM13-13-P0083-WHISKER-43OVER5-02
  methods_actual:
    - 11
    - 24
    - 30
  methods_outcome:
    11: "worked: self-consistent high-incidence scalar obstruction"
    24: "worked: exact algebraic extremum plus rational envelope"
    30: "worked: depth-one leaf obstruction implies global whisker shape"
  exact_checker: proofnet24/NM13-13/artifacts/P0083_whisker43over5_exact_check.py
  checker_output: proofnet24/NM13-13/artifacts/P0083_whisker43over5_exact_check.out
  checker_status: PASS_SELF_CHECK
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  hard_recovery_episodes_before: 0
  hard_recovery_episodes_after: 0
  hard_recovery_limit: 2
  audit_P26: NOT_DONE
  audit_NM13_01: NOT_DONE
  closure: false
  next_methods:
    - 3
    - 15
    - 18
  next_step: "leave the near-saturated scalar leaf envelope; seek a direct spectral instability theorem for non-whisker supports, beginning with asymmetric diameter-4 trees and a weighted-incidence reformulation"
  literature_check_date: 2026-09-19
  literature_scope: "source PDF; Holmes-Kleptsyn 2017 author PDF; finite-WARM predecessor; later adjacent WARM papers; bounded current title/author/Open-Problem-13 searches"
  literature_caveat: "bounded negative evidence only; no worldwide novelty claim"
```

No shared root, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation.
