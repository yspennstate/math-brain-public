Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `n_edge^* >= 6 -> n_edge^* >= 6`. Section-B methods actually tried and credited: #3, #25, #4.**

# NM13-06 research invocation — P0195 bridge theorem and connected-source reduction

Run date: 2026-09-18 UTC  
Track / namespace: `proofnet24/NM13-06`  
Category: CLOSABLE OUTSIDE  
Canonical source / claim: `P0195`, `operations/claims/P0195.md`  
Parent source status after this run: **OPEN**  
NM13-06 status after this run: **PARTIAL**  
Frozen metric before / after: **`n_edge^* >= 6 -> n_edge^* >= 6`**  
Consecutive unchanged runs since the last metric movement: **1 -> 2**  
Stuck recoveries used: **0 -> 0**  
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime and task-control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control schema continues to provide task title/prompt, schedule or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only here. Making it binding would require an owner-authorized product/workspace/API/admin surface that actually exposes those controls and authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary. Current repository policy records that a later P26 update succeeded from another authorized context; the legitimate workaround is therefore the owning/authorized surface or platform support, never task cloning or access-control bypass. No schedule or permission was changed in this invocation.

## 2. Continuity, ownership, and required repository read

This invocation continues the already admitted **P0195 — Monotonicity of the ferromagnetic Ising spectral gap** target. It does not reopen intake, create a second claim, alter the source clause, change normalization, or reset the frozen metric.

Before new mathematics I reread or targeted-recovered the current controlling and continuity state required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0195.md`;
- current exact-ID, title, canonical-key, claim, handoff, attempt, POSTED, campaign, and audit searches for P0195;
- the complete current NM13-06 report chain through the newest report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T04-45-45Z__p0195-n6-dense-class.md`;
- newest recovered neighboring reports from NM13-05 and NM13-07, namely `2026-09-18T04-23-00Z__d0004-fully-symmetric-envelope.md` and `2026-09-18T04-57-09Z__e0095-c20-girth6-exact.md`.

Canonical identity remains:

- source ID `P0195`;
- dedup key `monotonicity_of_the_ferromagnetic_ising_spectral_gap`;
- SHA256 `102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`;
- residue `5 mod 13`, matching NM13-06's exclusive shard;
- exclusive owner `proofnet24/NM13-06`.

The immutable claim is still present under that owner. I recovered no release, handoff, retirement, alternate-ID owner, source-level POSTED closure, campaign settlement, or passed P0195 audit. The only historical pre-NM13 work remains the limited two-spin calculation recorded by the claim/current reports. Large root and JSONL surfaces can be connector-truncated, so current root views plus exact source/key/path searches and the immutable claim are used as continuity anchors; I do not infer that inaccessible or deleted history is empty.

The preceding metric-moving run proved all edge additions through five vertices, moving `n_edge^* >= 5` to `n_edge^* >= 6`. The immediately preceding run then proved the complete six-vertex dense source stratum `|E(G)|>=13` but correctly left the frozen metric at `n_edge^*>=6`; its unchanged-run count was 1. That is the state continued here.

## 3. Exact source and fresh bounded literature/status check — 2026-09-18

I rechecked the original Levin--Peres--Wilmer PDF itself. In the freely available edition, Chapter 23 opens by saying to assume Glauber dynamics unless specified otherwise, and Question 2 asks whether the Ising spectral gap is monotone increasing in temperature and monotone decreasing under addition of edges. The source then asks the stronger inhomogeneous-interaction version and records Nacu's proof for a cycle.

Source PDF checked directly:

`https://www.stat.berkeley.edu/~aldous/260-FMIE/Levin-Peres-Wilmer.pdf`

This worker continues only the literal **edge-addition clause** in the frozen zero-field, common-`beta`, random-scan one-site heat-bath setting. It does not claim the separate temperature clause or the full inhomogeneous-coupling strengthening.

Fresh bounded public-web searches on 2026-09-18 used combinations of:

- the exact LPW edge-addition wording;
- `Ising Glauber spectral gap adding bridge edge disconnected components monotonicity heat-bath`;
- `Glauber dynamics spectral gap disjoint union bridge edge Ising`;
- `Ising spectral gap addition of edges Glauber 2026`;
- `Monotonicity Glauber dynamics finite graphs coupling constants spectral gap Shirai Nacu`.

The search recovered Shirai's 2010 paper *A remark on monotonicity for the Glauber dynamics on finite graphs*, whose counterexample concerns monotonicity of a fixed-time single-spin expectation from the all-up state, not spectral-gap monotonicity. It also recovered current spectral-gap/mixing work on other regimes, such as rapid mixing under spectral-independence/uniqueness hypotheses, not a theorem settling LPW Question 2. I did not recover a source-matching resolution or a published statement of the bridge-addition theorem below. This is **bounded negative evidence only**, not proof of worldwide openness and not a publication-novelty certificate. Publication novelty remains **UNVERIFIED**.

## 4. Frozen model and metric

For a finite simple graph `G=(V,E)`, let

`mu_G,beta(sigma) proportional exp(beta * sum_{uv in E} sigma_u sigma_v)`

on `{−1,+1}^V`, and let `P_G(beta)` be the random-scan one-site heat-bath chain, choosing one vertex uniformly at each discrete step. For an absent edge `e`, compare `G` and `G+e` at the same finite `beta>=0` and the same one-update-per-step normalization.

The frozen metric is

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if no counterexample exists.

Before this run: `n_edge^* >= 6`.  
After this run: **`n_edge^* >= 6`**.

The theorems below remove every disconnected six-vertex source and, more generally, prove a source-wide connected-source reduction, but they do not yet certify every connected six-vertex marked edge addition. Therefore the frozen metric does not move and is not replaced by the smaller unresolved-case count.

## 5. New idea before code

The preceding exact dense-class computation showed that brute-force symbolic comparison across all 572 six-vertex marked edge-addition types is the wrong immediate scaling direction: asymmetric connected graphs can have much larger odd quotients than the five-vertex problem.

A different question is structural:

> Can a **minimal counterexample** ever come from a disconnected source graph?

For an edge added *inside* one disconnected component, a minimal-counterexample argument already suggests reduction to a smaller graph. The nontrivial case is an edge joining two components. The key zero-field observation is that adding a single bridge coupling between two components does **not change either component marginal**: after summing over the other component, global spin-flip symmetry makes the bridge partition function independent of the boundary spin. Once this is noticed, the heat-bath Dirichlet form and the law of total variance compare in exactly the conjectured direction.

That gives a theorem in every order before any finite enumeration. Only then is a finite exact count useful: it measures precisely how much of the six-vertex frontier the theorem removes.

## 6. Method #3 — PROVE SOMETHING STRONGER: a universal bridge-addition theorem

### Theorem `NM13-06-P0195-BRIDGE-07`

Let `G` be any finite simple graph, let `A` and `B` be two distinct connected components of `G`, let `u in A`, `v in B`, and let

`H = G + {u,v}`.

For zero-field ferromagnetic Ising at any common finite `beta>=0`, under random-scan one-site heat-bath dynamics with one update per step,

`gap_beta(H) <= gap_beta(G)`.

Equivalently, **adding an edge between two previously disconnected components can never be a counterexample to the LPW edge-addition monotonicity clause.**

### Proof

Write the connected components of `G` as `G_1,...,G_r`, with vertex counts `m_i`, and let `n=sum_i m_i`. Let `P_i` denote the random-scan heat-bath chain on component `G_i`, normalized to choose one of its `m_i` vertices uniformly.

Because the source Gibbs measure is the product of the component Gibbs measures and a global random-scan step chooses a vertex uniformly from all `n` vertices,

`P_G = sum_i (m_i/n) (P_i tensor I_{-i})`.

The summands commute and are self-adjoint. Hence the product eigenbasis gives

`gap_beta(G) = min_i (m_i/n) gap_beta(G_i)`.          (6.1)

The same identity also follows from the heat-bath Dirichlet form, but the tensor decomposition makes the exact normalization transparent.

Now suppose the new edge joins components `A` and `B` at `u` and `v`. First observe that the marginal Gibbs law on `A` is **unchanged** by the bridge. Before normalization, the target marginal weight of an `A`-configuration `sigma` is

`exp(beta H_A(sigma)) * sum_tau exp(beta H_B(tau) + beta sigma_u tau_v)`.

Call the second factor `Z_B(sigma_u)`. The change of variables `tau -> -tau` preserves `H_B(tau)` and changes `tau_v` to `-tau_v`; therefore

`Z_B(+1)=Z_B(-1)`.

Thus the second factor is independent of `sigma_u`, and the target marginal on `A` is exactly the original zero-field Ising law `mu_A`. By the same argument, the target marginal on `B` is exactly `mu_B`. Every untouched component also retains its source marginal.

For any finite Gibbs heat-bath chain on `n` sites, its Dirichlet form is

`E(f,f) = (1/n) sum_w E[ Var(f | sigma_{V\{w}}) ]`.          (6.2)

Fix a function `f` depending only on spins in `A`. All update terms outside `A` vanish. For `w in A\{u}`, the bridge interaction does not involve `w`, so after conditioning on all other spins the target one-site conditional law at `w` is the same as in the isolated component `A`; averaging uses the unchanged `A` marginal.

At the bridge endpoint `u`, the target conditions on the extra information carried by component `B`. The law of total variance gives

`E_H[ Var_H(f | A\{u}, B) ] <= E_H[ Var_H(f | A\{u}) ]`.

Because the target marginal on `A` is exactly `mu_A`, the right-hand side is exactly

`E_A[ Var_A(f | A\{u}) ]`.

Combining these facts with (6.2),

`E_H(f,f) <= (m_A/n) E_A(f,f)`,          (6.3)

where `E_A` is the component heat-bath Dirichlet form under its own `1/m_A` update normalization. Also

`Var_H(f)=Var_A(f)`

because the marginal on `A` is unchanged. Taking `f` to be a component Poincare minimizer gives

`gap_beta(H) <= (m_A/n) gap_beta(A)`.

The same argument applies to `B`. For any untouched component `C`, a test function depending only on `C` gives the exact analogous upper bound

`gap_beta(H) <= (m_C/n) gap_beta(C)`.

Therefore

`gap_beta(H) <= min_i (m_i/n) gap_beta(G_i)`.

Using (6.1), the right side is `gap_beta(G)`, proving

`gap_beta(H) <= gap_beta(G)`.

QED.

### Corollary — any minimal counterexample source is connected

Assume `n_edge^*` is finite and choose a counterexample of minimal vertex order. Its source graph cannot be disconnected.

If the added edge joins two source components, the bridge theorem rules out a gap increase. If the added edge lies inside one component `C`, write the source gap using (6.1). If the global target gap were larger than the global source gap, no unchanged component could have supplied the source minimum, since that same scaled gap remains available after the addition. Hence the changed component must itself satisfy

`gap_beta(C+e) > gap_beta(C)`,

which is a counterexample on strictly fewer vertices, contradicting minimality.

Thus every finite minimal witness for the frozen metric has a **connected source graph**.

### Outcome of #3

**Success.** Instead of proving only another finite six-vertex stratum, this route proves the conjectured direction for every cross-component edge addition in every finite order and reduces the global minimal-counterexample search to connected source graphs.

## 7. Method #25 — COUNT THE SAME THING TWICE: exact six-vertex orbit census

Only after the analytic theorem was proved did I build a finite checker to quantify the six-vertex consequence.

A marked edge-addition type is a pair `(G,e)` with `G` a simple six-vertex graph and `e` an absent edge, modulo simultaneous relabeling by `S_6`.

The checker counts these orbits in two independent exact ways.

### Count A — graph classes, then automorphism orbits of missing edges

1. Enumerate all `2^15` labelled six-vertex simple graphs.
2. Quotient by `S_6`, obtaining exactly **156** unlabeled graph classes.
3. For each canonical source graph, compute its exact automorphism group.
4. Quotient its absent edges under that automorphism group.

This gives exactly **572** marked edge-addition orbits, stratified as

- **402** with connected source;
- **112** with disconnected source and the marked edge joining two components;
- **58** with disconnected source and the marked edge lying within one component.

### Count B — Burnside directly on marked pairs

Independently apply Burnside's lemma to the `S_6` action on labelled marked pairs.

For a vertex permutation `p`, inspect its induced permutation of the 15 possible graph edges. A marked pair `(G,e)` can be fixed only when the marked absent edge `e` is a one-cycle of this induced edge action, while the source edge set is a union of the induced edge cycles that excludes `e`. The checker enumerates these invariant edge-cycle selections exactly, classifies source connectivity exactly, sums the fixed marked pairs over all 720 vertex permutations, and divides by 720.

The independent Burnside totals are again exactly

`connected_source = 402`,
`cross_components = 112`,
`within_component = 58`.

Thus the two exact orbit counts agree in every source-connectivity stratum.

For the connected-source frontier, the exact source-edge distribution is

`5:27, 6:64, 7:90, 8:89, 9:65, 10:39, 11:18, 12:7, 13:2, 14:1`.

The preceding dense theorem already covers the last `2+1=3` connected marked types with 13 or 14 source edges.

### Outcome of #25

**Success.** Two independent integer orbit counts agree exactly and show that the structural theorem removes 112 cross-component six-vertex types before any spectral calculation. Together with the already-proved five-vertex theorem, all 170 disconnected six-vertex marked types are certified. The current connected remainder after also removing the three dense types is exactly **399** marked types. This case count is route information only and is **not** substituted for the frozen metric.

## 8. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: all disconnected six-vertex sources

### Theorem `NM13-06-P0195-N6-DISCONNECTED-08`

Let `G` be any disconnected simple graph on six vertices, let `e` be any absent edge, and let `beta>=0` be finite. Then

`gap_beta(G+e) <= gap_beta(G)`.

### Proof

There are two cases.

**Case 1: `e` joins two distinct components of `G`.** This is exactly Theorem `NM13-06-P0195-BRIDGE-07`.

**Case 2: both endpoints of `e` lie in one component `C`.** Since `G` is disconnected and has six vertices, `|V(C)|<=5`. The previous complete five-vertex theorem proved edge-addition monotonicity for every graph on at most five vertices and every finite common `beta>=0`, so

`gap_beta(C+e) <= gap_beta(C)`.

For a disconnected product source, (6.1) gives the full gap as the minimum of the component gaps multiplied by their component-size fractions. Replacing one component gap by a weakly smaller value cannot increase that minimum. Hence

`gap_beta(G+e) <= gap_beta(G)`.

This covers every disconnected six-vertex source. QED.

The exact orbit checker independently confirms that this theorem covers **170** of the 572 six-vertex marked isomorphism types: 112 by the universal bridge theorem and 58 by the within-component reduction to the already certified `n<=5` theorem.

### Outcome of #4

**Success.** A complete source-faithful six-vertex class is closed without a large spectral certificate. It does not move `n_edge^*`, because 399 connected marked types remain after also accounting for the previous dense theorem.

## 9. Exact finite self-check and archived output

Exact finite coverage checker:

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_disconnected_orbits_exact.py`

Creation commit:

`8d88bfaeaf6c145e6fbfd279f0529002afa47031`

Read-back blob:

`2a6b0fe90309636ccaafa1722eacacb636176b3e`

Archived executed output:

`proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_disconnected_orbits_exact.out`

Creation commit:

`ee3cdea8f0a3228ce9da877e9c26cb2f07fb5147`

Read-back blob:

`3f92cfe4e1cd07ee4e1b27364bf37388ded69bca`

The checker was inspected and executed locally with ordinary Python. It uses only exact integer graph masks, vertex permutations, connected-component searches, automorphism orbits, and Burnside sums. Its archived output is:

`unlabeled_graphs 156`

`marked_edge_addition_orbits 572`

`method_A_counts {'connected_source': 402, 'cross_components': 112, 'within_component': 58}`

`method_B_burnside_counts {'connected_source': 402, 'cross_components': 112, 'within_component': 58}`

`disconnected_marked_types_covered 170`

`connected_dense_marked_types_already_covered 3`

`connected_marked_types_remaining_after_dense 399`

and ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit. The universal bridge theorem is proved on the page; the checker certifies only the finite six-vertex orbit accounting and coverage bookkeeping.

## 10. Interpretation, failed routes avoided, and remaining obligation

The frozen metric does not move:

`n_edge^* >= 6 -> n_edge^* >= 6`.

However, the shape of any future witness is now strictly narrower for a theorem-level reason rather than a numerical pattern:

1. a finite minimal counterexample must have a **connected source graph**;
2. at order six, all **170 disconnected** marked types are impossible;
3. the previous dense theorem removes the **3** connected marked types with 13 or 14 source edges;
4. exactly **399 connected marked types with at most 12 source edges** remain at order six.

The key route lesson is that disconnectedness should never again consume exact spectral algebra on this target. The bridge theorem removes it in all orders.

I deliberately did not scale the previous resultant/Sturm engine blindly to all 399 remaining connected types. For asymmetric six-vertex graphs the odd quotient can be much larger than in the five-vertex atlas, and producing hundreds of high-degree certificates without a new structural idea would violate the owner's new-method-first rule.

The next substantive run should therefore attack the **connected** six-vertex frontier with three still-untried methods on P0195: **#7 TAKE THE LIMIT**, **#13 FIND WHAT ONLY INCREASES**, and **#26 HUNT THE SPORADIC CASE**. Concretely: derive the first nonzero low-temperature separation for connected marked types, look for a monotone quantity controlling that sign away from the boundary, and isolate any exceptional connected types where the asymptotic coefficient vanishes or reverses. If that run also leaves the frozen metric unchanged, the unchanged-run counter becomes 3 and the following invocation must use the owner-prescribed Section-I stuck-recovery protocol rather than continuing routine lemmas.

No paper folder is created: the parent source remains OPEN, the track remains PARTIAL, and neither required outside audit has passed.

## 11. Operational boundaries

No shared root, peer namespace, canonical claim file, schedule, workflow, permission, public surface, email/Drive item, or paid-compute resource was modified. The only writes were the two warranted own-namespace artifacts above and this one immutable own-namespace run report. No external script was executed.

## 12. Structured `ledger_delta` for P26

```json
{
  "track": "NM13-06",
  "category": "CLOSABLE OUTSIDE",
  "source_id": "P0195",
  "claim_id": "P0195",
  "canonical_dedup_key": "monotonicity_of_the_ferromagnetic_ising_spectral_gap",
  "shard_mod_13": 5,
  "source_status": "OPEN",
  "track_status": "PARTIAL",
  "metric": {
    "name": "n_edge^*",
    "before": ">= 6",
    "after": ">= 6",
    "movement": false
  },
  "new_claims": [
    "NM13-06-P0195-BRIDGE-07: adding one edge between two disconnected source components cannot increase the zero-field ferromagnetic random-scan heat-bath spectral gap, at every finite common beta>=0",
    "connected-source reduction: any finite minimal counterexample to the frozen edge-addition clause has connected source graph",
    "NM13-06-P0195-N6-DISCONNECTED-08: every disconnected six-vertex source and every absent edge obeys the conjectured spectral-gap direction"
  ],
  "methods": [
    {"number": 3, "name": "PROVE SOMETHING STRONGER", "outcome": "universal bridge-addition theorem and connected-source reduction"},
    {"number": 25, "name": "COUNT THE SAME THING TWICE", "outcome": "Aut-orbit and independent Burnside counts both give 402 connected, 112 cross-component, 58 within-component marked n=6 types"},
    {"number": 4, "name": "PROVE SOMETHING WEAKER, COMPLETELY", "outcome": "all 170 disconnected six-vertex marked types certified using bridge theorem plus complete n<=5 theorem"}
  ],
  "unchanged_runs": {"before": 1, "after": 2},
  "stuck_recoveries": {"before": 0, "after": 0},
  "finite_frontier": {
    "n6_marked_types_total": 572,
    "n6_disconnected_covered": 170,
    "n6_connected_total": 402,
    "n6_connected_dense_already_covered": 3,
    "n6_connected_remaining_after_dense": 399
  },
  "checker": {
    "path": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_disconnected_orbits_exact.py",
    "commit": "8d88bfaeaf6c145e6fbfd279f0529002afa47031",
    "blob": "2a6b0fe90309636ccaafa1722eacacb636176b3e"
  },
  "output": {
    "path": "proofnet24/NM13-06/artifacts/2026-09-18/p0195_n6_disconnected_orbits_exact.out",
    "commit": "ee3cdea8f0a3228ce9da877e9c26cb2f07fb5147",
    "blob": "3f92cfe4e1cd07ee4e1b27364bf37388ded69bca",
    "result": "ALL_EXACT_CHECKS_PASS"
  },
  "audits": {
    "P26": "NOT PASSED / not presumed",
    "NM13-07": "NOT PASSED / not presumed"
  },
  "literature_check": {
    "date": "2026-09-18",
    "scope": "original LPW source PDF; exact edge-addition wording; bridge/disconnected-component Glauber spectral-gap queries; Shirai/Nacu monotonicity neighborhood; recent spectral-gap/mixing queries",
    "outcome": "no source-matching resolution or published bridge theorem recovered in bounded search",
    "qualification": "negative evidence only; worldwide openness and publication novelty unverified"
  },
  "next_step": "connected n=6 only; try fresh methods #7, #13, #26; derive low-temperature separation, seek monotone control, isolate sporadic vanishing cases",
  "next_if_unchanged": "if the next substantive run is again unchanged, unchanged_runs becomes 3 and the following invocation must be the Section-I stuck-recovery report"
}
```
