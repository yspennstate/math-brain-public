Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED — not GPT-6 maximum**. **MOVEMENT: `S_exact = 2 -> 3`; methods #18, #24, #30 genuinely attempted.**

# NM13-04 / P0457 — exact preference-profile support, sharp extremal diameter, and the co-degree-three classifier

Status: **OPEN / PARTIAL** relative to the source near-logarithmic random-diameter problem.

Exclusive claim remains `operations/claims/P0457.md` (owner NM13-04, namespace `proofnet24/NM13-04/`). No conflicting claim, handoff, release, retirement, or source-level closure was recovered this run.

Source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (2026), 552–579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025.

Frozen source model: iid continuous edge weights on `K_n`; `LK(n,k)` retains `{u,v}` iff that edge is among the `k` smallest-weight incident edges at both endpoints.

Frozen metric, unchanged from admission:

`S_exact = largest co-degree s >= 0 for which this track has a complete deterministic diameter classification for LK(n,n-1-s), valid for every n in the stated range.`

Before this run: `S_exact = 2`.
After this run: `S_exact = 3`.

The movement is the complete `s=3` theorem in Section 6. The stronger all-`s` extremal theorem in Section 5 is additional progress, but I do not silently replace the frozen metric by that extremal quantity.

---

## 1. Continuity, ownership, source, and control surfaces

This is the third NM13-04 research run on the already admitted P0457 target; intake was **not** reopened.

I reread the controlling policy surfaces `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, and the later owner-authorized NM13 deployment record `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; canonical claim `operations/claims/P0457.md`; the two preceding NM13-04 reports; the newest neighboring NM13-03 and NM13-05 reports recovered by repository search; and the P0457 intake/ranking/attempt surfaces.

Canonical identity remains:

- ID `P0457`;
- dedup key `diameter_near_the_newly_established_bilateral_connectivity_threshold`;
- SHA256 `839d9617dd11661f03c25aa6c4d2e47c012b337f35570dde06ca7695f66ff561`;
- residue `3 mod 13`, the NM13-04 selection shard.

The intake ledger still records P0457 as `unsolved`; the older campaign attempt supplied only a Moore/maximum-degree lower bound and explicitly left the upper-diameter behavior unresolved. The admitted claim remains the sole recovered ownership record for this exact source identity.

Large root files and campaign catalogs are connector-truncated surfaces rather than guaranteed byte-for-byte dumps. Exact target, claim, own reports, and exact-ID/dedup history were read directly or recovered by exact repository search. I do not interpret truncated or inaccessible history as permission to reset a baseline.

The exposed task/scheduler control surface still has fields for task title/prompt, schedule or offset, timing mode, and enabled state, but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only in this environment. Changing that would require an authorized product/scheduler surface that actually exposes model and reasoning controls. Repository history records that a prior P26 edit returned `You cannot modify this task`, while a later update succeeded in a different authorized context; therefore such a refusal is context/authorization-specific. The legitimate remedy is the owning account/workspace or an authorized product/admin/support surface, not a duplicate task or access-control bypass.

---

## 2. Fresh source and literature check — 2026-09-17 UTC

The Cambridge article page was checked again. The published source still says that the La–Kabkab connectivity methodology also determined diameter in its earlier range and then explicitly poses as future work the problem of characterizing the diameter in the **additional range of `k(n)` covered by Dabirian–Subramanian Theorem 6**. The same page states the source model using iid continuous edge weights and bilateral top-`k` preference.

Fresh bounded searches included:

- exact paper title plus `diameter`;
- both authors plus `bilateral preference diameter`;
- `LK(n,k) diameter bilateral`;
- later-2026 author/title queries;
- `bilateral preference acyclic asymmetry digraph top-k realization`;
- `mutual top-k graph realization acyclic preference digraph`.

They recovered the published Cambridge paper / its arXiv predecessor and unrelated preference-graph material, but no later source-matching resolution of the diameter question and no located source-specific statement matching the exact support theorem below.

This is a bounded dated search, not proof of worldwide openness and not a novelty certificate. In particular, the support theorem in Section 4 is elementary once one introduces vertex cutoffs, so I make no claim that its mechanism is new in a broader preference-realization literature.

---

## 3. Recovered structural baseline

Write

`k = n-1-s`,

so every vertex rejects exactly its `s` largest incident weights. Let

`G_s = LK(n,n-1-s)`,
`H_s = complement(G_s)`.

The preceding run proved, for every distinct-weight realization and every `s>=1`:

1. `H_s` is `s`-degenerate;
2. if `G_s` is connected, then

   `diam(G_s) <= s+2`.

The proof used the cutoff `tau_v` equal to the `s`-th largest incident edge weight and the vertex minimizing `tau_v` in each induced subgraph. I use those theorems as recovered continuity; I do not count them again as new movement.

The new questions for this run were exactly the previous report's proposed ones:

- can the source realizability condition be stated in a cleaner language than an edge-comparison DAG? (#18)
- is the upper bound `s+2` actually the exact extremal diameter, or does the common-weight realization condition improve it? (#24)
- can `s=3` be classified completely without pretending that a finite high-degree theorem solves the near-logarithmic random problem? (#30)

---

## 4. Method #18 — say the source realization problem in another language

The previous finite check decided whether a collection of local rejected sets could arise from one global edge ordering by building a comparison DAG whose vertices were **edges of `K_n`**. There is a much smaller exact description on the original vertices.

Fix `1 <= k <= n-2`. A **local `k`-selection profile** is a family

`K_v subset V\{v}`,  `|K_v|=k`,

where `u in K_v` means that vertex `v` proposes/selects edge `uv`.

Define the **asymmetry digraph** `D_K` on the vertex set `V` by

`u -> v  iff  v in K_u  and  u notin K_v`.

Thus an arc points from the endpoint that selects an edge to the endpoint that rejects the same edge.

### Theorem P0457-SUPPORT — exact support characterization

A local `k`-selection profile `K=(K_v)` is realized by some assignment of distinct real edge weights to `K_n` under the exact source rule if and only if `D_K` is acyclic.

Equivalently: the only global consistency obstruction to prescribed top-`k` sets is a directed cycle of one-sided selections.

### Proof — necessity

Assume distinct edge weights realize the profile. For every vertex `v`, choose a cutoff `c_v` strictly between its `k`-th and `(k+1)`-st smallest incident edge weights. Then

`u in K_v  iff  W_uv < c_v`.

If `u -> v` in `D_K`, then `u` selects `uv` while `v` rejects it, so

`W_uv < c_u`

and

`W_uv > c_v`.

Hence `c_u > c_v` along every directed arc. A directed cycle would imply a strict cyclic chain

`c_{v_1} > c_{v_2} > ... > c_{v_r} > c_{v_1}`,

which is impossible. Therefore `D_K` is acyclic. QED.

### Proof — sufficiency

Assume `D_K` is acyclic. Choose pairwise distinct cutoffs `c_v` in `(1/3,2/3)` in a topological order so that

`u -> v  =>  c_u > c_v`.

For each unordered edge `uv`, choose its weight independently inside the following nonempty open interval:

- if `u in K_v` and `v in K_u` (mutual selection), choose
  `W_uv in (0, min(c_u,c_v))`;
- if neither endpoint selects the other, choose
  `W_uv in (max(c_u,c_v),1)`;
- if `u` selects `v` but `v` rejects `u`, then `u -> v`, so `c_u>c_v`; choose
  `W_uv in (c_v,c_u)`;
- symmetrically for `v -> u`.

Every required interval is open and nonempty. There are finitely many edges, so the choices can be made pairwise distinct.

At each vertex `v`, exactly the `k` incident edges indexed by `K_v` lie below `c_v`, and every other incident edge lies above `c_v`. Therefore those `k` edges are exactly the `k` smallest incident edges, and the source rule realizes precisely the prescribed profile. QED.

### Consequence

The edge-comparison DAG from the preceding finite enumerator is unnecessary for mathematical characterization. Source realizability can be checked on an `n`-vertex digraph. More importantly, this lets one design exact source examples at the level of local preference sets and prove realizability by one acyclicity check.

This theorem is an exact structural reformulation, not a claim that arbitrary independent local preference sets occur with equal probability under iid global edge weights. They do not.

---

## 5. Method #24 — find the extremal object

The recovered deterministic theorem gave

`diam(G_s) <= s+2`

whenever `G_s` is connected. It was not clear whether the global common-weight constraint forces a better bound than generic `s`-degeneracy. P0457-SUPPORT decides this exactly.

### Theorem P0457-EXTREMAL-DIAM — the deterministic bound is sharp for every feasible co-degree

Let `n>=4` and `2 <= k <= n-2`, and put

`s = n-1-k`.

Then among all distinct-weight source realizations for which `LK(n,k)` is connected,

`max diam(LK(n,k)) = s+2 = n-k+1`.

Equivalently, for every `s>=1` and every `n>=s+3`, there is an exact source realization of `LK(n,n-1-s)` with diameter exactly `s+2`.

At the endpoints: `k=n-1` gives `K_n` and diameter 1; for `k=1` and `n>=3`, every vertex proposes one edge, so the mutual graph has maximum degree at most one and no connected realization exists.

### Proof

The upper bound is the recovered P0457-DIAM-BOUND theorem. It remains to construct a matching source realization.

Fix `s>=1` and `n>=s+3`. Put

`q = n-s-3`,  so  `k=q+2`.

Take base vertices

`x_0,x_1,...,x_{s+2}`

and an additional set `Q` of `q` vertices.

Define a local `k`-selection profile as follows.

For each `y in Q`, let

`K_y = (Q\{y}) union {x_0,x_1,x_2}`.

For the base vertices set

`K_{x_0} = Q union {x_1,x_2}`,

`K_{x_i} = Q union {x_{i-1},x_{i+1}}`  for `1 <= i <= s+1`,

and

`K_{x_{s+2}} = Q union {x_s,x_{s+1}}`.

Every set has cardinality `q+2=k`.

The only one-sided selections are:

- `x_0 -> x_2`;
- `x_{s+2} -> x_s`;
- `x_i -> y` for every `i>=3` and every `y in Q`.

There is no directed cycle: the `Q` vertices have no outgoing asymmetry arc, and the two remaining arcs do not feed back. Hence P0457-SUPPORT gives distinct global edge weights realizing this exact local profile.

Now inspect the mutual graph. The base vertices induce exactly the path

`x_0-x_1-...-x_{s+2}`.

The set `Q` is a clique, and every `y in Q` is adjacent exactly to `x_0,x_1,x_2` among the base vertices. There are no other mutual edges.

Therefore the graph is connected. The path gives

`d(x_0,x_{s+2}) <= s+2`.

Any path from `x_0` that enters `Q` can leave `Q` toward the base only at one of `x_0,x_1,x_2`. The best possible shortcut is

`x_0 - y - x_2 - x_3 - ... - x_{s+2}`,

which still has length

`2+s = s+2`.

So `d(x_0,x_{s+2})=s+2`. The recovered universal upper bound gives equality for the graph diameter. QED.

### Source-level meaning

This closes an important deterministic question about the previous theorem: **the common iid-weight support imposes no better worst-case diameter bound than `s+2`.** In fact the bound is sharp for every feasible `(n,s)`.

It also says exactly why this deterministic high-degree route cannot simply be pushed into the source's near-logarithmic regime. There `s=n-1-k` is of order `n`, so the sharp deterministic bound `s+2=n-k+1` is linear and therefore carries essentially no typical-random diameter information. Any real attack on the source window must now use probability, not a stronger universal deterministic inequality of this form.

That negative route diagnosis is substantive: it prevents spending further runs looking for a nonexistent deterministic improvement to `s+2`.

---

## 6. Method #30 — one scale at a time: complete `s=3` classification

Now freeze

`s=3`,  `k=n-4`,  `G=LK(n,n-4)`,  `H=bar G`,

with `n>=5`.

The recovered theorem gives `H` 3-degenerate and, when `G` is connected,

`diam(G)<=5`.

The extra shell below gives a complete exact classifier, advancing the frozen metric.

For a missing pair `uv in H`, define

`A_uv = N_G(u)`,  `B_uv = N_G(v)`.

Define three source-visible bridge tests:

`C_0(uv): A_uv intersect B_uv != empty`;

`C_1(uv): there is a G-edge joining A_uv to B_uv`;

`C_2(uv): there exists z having at least one G-neighbor in A_uv and at least one G-neighbor in B_uv`.

### Theorem P0457-S3-CLASS — complete co-degree-three deterministic classification

For every distinct-weight realization of `LK(n,n-4)`:

1. `H` is 3-degenerate.
2. If `G` is disconnected, its largest connected component has size at least `n-3`. Hence, apart from small-`n` coincidences, the only possible component-size patterns are
   - `(n-1,1)`,
   - `(n-2,2)`,
   - `(n-2,1,1)`,
   - `(n-3,3)`,
   - `(n-3,2,1)`,
   - `(n-3,1,1,1)`.
3. If `G` is connected, every missing pair `uv` has exact distance
   - 2 if `C_0(uv)` holds;
   - 3 if `C_0(uv)` fails but `C_1(uv)` holds;
   - 4 if `C_0(uv),C_1(uv)` fail but `C_2(uv)` holds;
   - 5 if all three tests fail.
4. Consequently the connected graph diameter is exactly one of `2,3,4,5`, and is obtained by taking the maximum of these exact missing-pair distances. Equivalently:
   - diameter 2 iff every missing pair satisfies `C_0`;
   - diameter 5 iff some missing pair fails `C_0,C_1,C_2`;
   - diameter 4 iff no pair has distance 5 and some pair fails `C_0,C_1` but satisfies `C_2`;
   - otherwise the connected diameter is 3.

### Proof

Part 1 is P0457-DEGEN at `s=3`.

For Part 2, let the connected components of `G` have sizes `n_1,...,n_r`, and let `M=max_i n_i`. Every cross-component pair is an edge of `H`, so `H` contains the complete multipartite graph whose parts are the `G`-components. In that subgraph every vertex in a largest part has degree at least `n-M`. If `n-M>=4`, this subgraph has minimum degree at least four, contradicting 3-degeneracy. Therefore `M>=n-3`. The displayed list is exactly the set of integer partitions having at most three vertices outside a largest component, modulo low-order coincidences.

Assume now that `G` is connected and fix a missing pair `uv`.

A length-two `u-v` path exists iff some vertex lies in both `A_uv` and `B_uv`; this is exactly `C_0`.

If `C_0` fails, a length-three path exists iff there are `a in A_uv` and `b in B_uv` with `ab in G`; this is exactly `C_1`.

If both earlier tests fail, a length-four path exists iff there are `a in A_uv`, `b in B_uv`, and a vertex `z` with `az,zb in G`; this is exactly `C_2`.

If all three tests fail, there is no path of length at most four from `u` to `v`. But the recovered universal bound gives `diam(G)<=5`, so `d_G(u,v)=5`.

Thus the four tests give the exact distance of every missing pair. Adjacent pairs have distance one, and `H` is nonempty for `s=3`; taking the maximum proves Part 4. QED.

This is the same standard of complete deterministic local classification used for `s=2`, now one full shell farther. Therefore the frozen metric moves

`S_exact = 2 -> 3`.

The classification is exact for every `n>=5`; the connected branch is vacuous at orders where no connected source realization exists.

---

## 7. Exact finite self-checks and witness

The mathematics above was developed before the checker. The checker is a **self-check**, not an independent audit.

Checker:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T23-19-15Z__p0457_s3_support_check.py`

creation commit `d831b23b25a06354a8479a593b93e371a4f68f34`, read back at that commit, blob `e0efb6fb1cd82b992baf99542d6b574eb864e6b9`.

Archived output:
`proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T23-19-15Z__p0457_s3_support_check.out`

creation commit `33ab116b66200a1e44410c872c3b6451ac7c4c64`, read back at that commit, blob `31fbf457333d0703d65eed542e464f11c8b15fb9`.

The checker performs four separate exact checks.

### 7.1 Realizability theorem against the old edge-comparison criterion

It exhausts all local selection profiles in the following cases:

- `n=4,k=1`: 81 profiles;
- `n=4,k=2`: 81 profiles;
- `n=5,k=2`: 7776 profiles;
- `n=5,k=3`: 1024 profiles.

For every one of these 8962 profiles, acyclicity of the new vertex asymmetry digraph agrees exactly with acyclicity of the full edge-comparison constraint digraph. There were zero disagreements.

This finite test does not replace the proof of P0457-SUPPORT; it checks the reformulation against the previous exact realizability mechanism.

### 7.2 Explicit integer-weight diameter-five source witness

For `n=6,k=2` (`s=3`), the exact weights include

`W_01=4, W_12=3, W_23=1, W_34=2, W_45=5, W_02=55, W_35=65`,

with the eight remaining edge weights assigned the distinct integers `101,...,108`.

The source rule then gives exactly the path

`0-1-2-3-4-5`,

so the diameter is 5. This is a literal exact source realization, not a graph supplied independently of bilateral preferences.

### 7.3 Full `n=6,k=2` local-profile census

There are `10^6` possible local two-selection profiles. Using the proved exact support criterion, the checker finds:

- realizable profiles: `272860`;
- connected realizable profiles: `5460`;
- connected diameter 3: `60`;
- connected diameter 5: `5400`;
- shell-classifier/BFS mismatches: `0`.

These are counts of local selection profiles, **not probabilities** under iid edge weights; profiles are not equiprobable under a random global edge ordering.

### 7.4 General sharpness construction

The checker verifies the Section 5 profile combinatorially for every

`s=1,...,12`, `q=0,...,6`,

84 exact cases in total: selection-set sizes are correct, the asymmetry digraph is acyclic, and the mutual graph has diameter exactly `s+2`.

The archived output terminates

`ALL_EXACT_CHECKS_PASS`.

---

## 8. Method ledger and what actually happened

### #18 — SAY IT IN ANOTHER LANGUAGE

**Succeeded.** Replaced the edge-level comparison feasibility problem by the vertex-level asymmetry digraph `D_K`. Proved exact realizability iff `D_K` is acyclic. This is a genuine structural simplification and a construction tool, not merely a restatement of degeneracy.

### #24 — FIND THE EXTREMAL OBJECT

**Succeeded.** Constructed, for every feasible `1<=s<=n-3`, a source-valid connected realization achieving the universal upper bound `diam=s+2`. Therefore the deterministic bound is exactly sharp, uniformly in `n`, and deterministic strengthening cannot bridge to the random near-logarithmic source window.

### #30 — ONE SCALE / ONE DIRECTION AT A TIME

**Succeeded for the frozen next scale.** Solved `s=3` completely in the same deterministic sense as the prior `s=1,2` reports: exact component-size restriction, exact connected diameter range, and an explicit finite local test distinguishing diameters 2,3,4,5. This moves `S_exact` from 2 to 3.

All three methods are new on this target and differ from the preceding triples `#2/#14/#19` and `#5/#20/#25`.

---

## 9. What this does and does not settle

### Now proved on this track

- exact support characterization of local bilateral `k`-selection profiles by an acyclic vertex asymmetry digraph;
- sharp deterministic connected-diameter extremum

  `max diam(LK(n,k)) = n-k+1`

  for every `2<=k<=n-2`;
- complete deterministic `s=3` / `k=n-4` classifier;
- exact source witness achieving diameter five at `n=6,k=2`.

### Still open

The source asks for diameter behavior in the random near-logarithmic connectivity range, roughly the additional `k(n)` regime around and above `log n` covered by Theorem 6. Nothing here supplies the needed high-probability upper bound, limiting law, or sharp typical asymptotic there.

Indeed Section 5 shows a precise obstruction to the current deterministic route: the exact worst-case diameter is linear in that regime. The next progress must exploit how **unlikely** the extremal preference profiles are under iid global edge weights rather than try to outlaw them deterministically.

Status therefore remains **OPEN / PARTIAL**, not PROVED or REFUTED.

No P26 or NM13-05 independent audit is counted. No paper folder is created because the source problem is not closed.

---

## 10. Counters

- metric before: `S_exact=2`;
- metric after: `S_exact=3`;
- movement: **yes**;
- unchanged-run counter: `0`;
- stuck-recovery episodes used: `0`;
- closure audits: `0/2` for any source-level closure claim;
- self-checks: present and explicitly not audits.

---

## 11. Next mathematical attack

Do not repeat `#18/#24/#30` next run.

The deterministic extremal theorem has now done its job and also proved its own limitation. The next run should cross from universal structure to the actual iid source law.

Suggested next unused Section-B triple:

- **#9 RANDOMIZE:** for a fixed candidate long geodesic or layer profile, compute/upper-bound the probability that the required local proposal/rejection pattern occurs under one random global edge ordering, rather than treating all realizable profiles equally;
- **#11 DUALIZE:** express failure of radius-`r` expansion from a vertex as a family of cutoff/order-statistic inequalities and look for a counting/LP-style dual certificate that avoids summing over all local profiles;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** target a genuine high-probability diameter upper bound in an overlapping growing-`k` regime, even if still above the source threshold, with explicit quantifiers and no simulation-to-theorem leap.

A useful concrete target is to show that the exact extremal path-profile family from Section 5 has exponentially or superpolynomially small source probability at a growing `k`, then identify which more numerous near-extremal profiles dominate. If this does not yield a source-relevant growing-`k` bound, record the fixed-co-degree theorem as complete restricted progress and change route rather than extending `s=4,5,...` mechanically.

---

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  target: P0457
  canonical_claim: operations/claims/P0457.md
  source: Dabirian-Subramanian bilateral preference diameter open problem
  status: PARTIAL
  source_status: OPEN
  frozen_metric: S_exact
  metric_definition: largest co-degree s with a complete deterministic diameter classification for LK(n,n-1-s)
  metric_before: 2
  metric_after: 3
  movement: true
  methods_actual: [18, 24, 30]
  method_outcomes:
    18: exact local-profile realizability iff vertex asymmetry digraph is acyclic
    24: proved max connected diameter is s+2=n-k+1 for every feasible fixed n,k
    30: complete s=3 deterministic classifier; S_exact moved to 3
  substantive_claims:
    - P0457-SUPPORT
    - P0457-EXTREMAL-DIAM
    - P0457-S3-CLASS
  exact_checker: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T23-19-15Z__p0457_s3_support_check.py
  exact_checker_commit: d831b23b25a06354a8479a593b93e371a4f68f34
  exact_output: proofnet24/NM13-04/artifacts/2026-09-17/2026-09-17T23-19-15Z__p0457_s3_support_check.out
  exact_output_commit: 33ab116b66200a1e44410c872c3b6451ac7c4c64
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  exact_finite_notes:
    - 8962 small profiles compare new support criterion with edge-comparison feasibility
    - n=6,k=2 census has 272860 realizable profiles, 5460 connected, 0 classifier mismatches
    - explicit integer-weight LK(6,2)=P6 witness has diameter 5
    - 84 sampled all-s extremal construction cases pass exactly
  unchanged_runs: 0
  stuck_recoveries_used: 0
  p26_audit: NOT_REQUESTED_NOT_PASSED
  secondary_audit_partner: NM13-05
  secondary_audit: NOT_REQUESTED_NOT_PASSED
  literature_check_date_utc: 2026-09-17
  literature_scope: original Cambridge source; exact-title/author/diameter queries; later-2026 searches; preference-realization terminology
  literature_result: no later source-matching diameter resolution recovered in bounded search; novelty not certified
  next_methods: [9, 11, 28]
  next_step: move from worst-case realizable profiles to high-probability iid-weight estimates for long geodesic/poor-expansion profiles in a growing-k regime
```

END OF IMMUTABLE REPORT
