Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `m_cert = 8 -> 9`. Section-B methods actually tried: #1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #19 MAKE IT AN ALGORITHM. Status: PARTIAL.**

# NM13-05 / C0146 — graphic-matroid obstruction and exact nine-edge theorem

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: **C0146**, `operations/claims/C0146.md`  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`  
Selection residue: `4 mod 13`  
Frozen metric: `m_cert`  
Metric before / after: **8 -> 9**  
Unchanged-run counter after this invocation: **0**  
Stuck recoveries: **0**  
Required eventual auditors for a completed source claim: **P26 and NM13-06; neither is presumed to pass**

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides prompt/title, schedule/start, timing mode, enabled-state, and identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/reasoning controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; repository state records a later successful P26 update from another authorized context. The lawful workaround is the owning/authorized context or platform/admin support, never duplication or bypass. No schedule was modified here.

## 2. Authoritative continuity and ownership

This is **not a new admission**. I continued the already admitted exclusive C0146 claim and did not create or modify another claim.

Before new mathematics I reread or targeted-recovered the current state required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- the C0146 intake row, canonical dedup alias/index, and historical attempt `C0146-A001`;
- newest own report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T09-23-00Z__c0146-m8-bernstein-transport.md`;
- newest recovered neighboring NM13-04 state at commit `6c9c8dbae62f2b07fad2d3a7a59a0a3af6ec9a3f` (P0457, first external audit PASS, still waiting for its distinct NM13-05 audit);
- newest recovered neighboring NM13-06 state at commit `0c54ebb085f3cf740e5771f357ea8fdd432faa92` (P0195 six-run handoff/rotation);
- exact-ID, canonical-key, ownership, audit, POSTED, and campaign searches for C0146.

No competing owner, owner-authorized release, retirement, source settlement, P26 C0146 PASS, or NM13-06 C0146 PASS was recovered. A disabled or rotated neighboring task does not release this ownership or create an audit. C0146 remains the lawful current target.

The previous C0146 report moved the frozen metric `5 -> 8` using methods #14/#16/#25 and explicitly set the next step to seek a **structural graphic-matroid explanation of the Bernstein coefficient transports or a first exact coefficient Hall obstruction before extending the edge census**. This run follows that instruction rather than blindly extending the same enumeration route.

## 3. Exact source and bounded literature check — 2026-09-18

The current primary source remains Gábor Pete, *Probability and Geometry on Groups*, current PDF dated April 3, 2024. The parsed primary PDF still prints on PDF page 184:

`Question 13.2. Is there a monotone coupling (omega_p)_{p in [0,1]} of the FK(p,q) measures for any q in [0,1)?`

and immediately follows it with Exercise 13.8 asking for an explicit UST-to-UST+1 monotone coupling on the six-vertex seven-edge digital-figure-8 graph. The PDF text was accessible; the page-image screenshot endpoint returned a cache miss, so no visual-page claim is made beyond the parsed primary text.

Fresh bounded searches on 2026-09-18 included the exact source question/title, `q<1 random-cluster monotone coupling`, `stochastic covering random cluster q<1`, current q<1 negative-dependence papers, `Lorentzian multivariate Tutte q<=1`, and `strongly log-concave stochastic covering property`.

The current nearest literature recovered was:

- Heehyun Park, *The q<1 Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence*, arXiv:2608.08565 (2026-08-09): wired regular trees and branch negative dependence, not arbitrary finite-graph monotone coupling in `p`;
- Pengfei Tang and Zibo Zhang, *Negative correlation for the random-cluster model below one on high-degree regular graphs*, arXiv:2609.11578 (2026-09-10): high-degree regular classes; its abstract still says even pairwise negative correlation is open on general finite graphs;
- Brändén–Huh, *Lorentzian polynomials*, Annals of Mathematics 192 (2020): the homogenized multivariate Tutte polynomial of a matroid is Lorentzian for `0<q<=1`, yielding negative-dependence consequences;
- the modified-log-Sobolev / strongly-log-concave literature explicitly notes that SLC does **not** imply the stochastic covering property (SCP), since some matroid-base measures are SLC while failing the relevant negative-dependence consequence of SCP.

Thus the Lorentzian theorem is relevant structure but is not a black-box stochastic-covering theorem. None of the bounded searches produced a source-matching general resolution of Pete Question 13.2 or a published theorem matching the nine-edge finite result below. This is **bounded negative evidence only**; worldwide openness and publication novelty remain **UNVERIFIED**.

## 4. Frozen metric and recalled reduction

The source question is unchanged. The frozen progress metric remains

`m_cert` = largest integer `m` for which NM13-05 has a rigorous source-valid certificate that for **every finite simple graph with at most `m` edges**, every `q in (0,1)`, and all `0<=p1<=p2<=1`,

`FK_G(p1,q) <=_st FK_G(p2,q)`

under edge inclusion.

The preceding certified value was `8`. This invocation proves `m_cert >= 9`, so the frozen after-value is **9**. I do not extend the metric to the source's `q=0` endpoint; the present fixed-size normalization is proved for `q>0`. The parent source therefore remains OPEN and this report is PARTIAL.

For a graph `H=(V,E)`, `m=|E|`, and a fixed size `|A|=r`, write

`c(A)=|A|-|V|+k(A)`

for cycle nullity. Conditioning the FK measure on `|A|=r` gives

`nu_r(A)=q^{c(A)}/W_r(q)`,

where `W_r(q)=sum_{|C|=r} q^{c(C)}`. If every adjacent pair `nu_r,nu_{r+1}` has an inclusion coupling, composing the kernels gives a nested chain. The FK size law has monotone likelihood ratio in `r` as `p` increases, so an independent common-quantile size process turns the nested fixed-size chain into a monotone grand coupling with exact FK marginals.

As proved in the preceding reports, random-cluster weights factor over graph blocks under one-vertex sums. Therefore it suffices to treat 2-connected blocks (and the one-edge bridge block, whose open probability is increasing in `p`).

## 5. Method #1 — CHANGE THE CATEGORY: from random cluster to matroid/Lorentzian structure

The fixed-size weights `q^{c(A)}` are graphic-matroid weights. This makes Brändén–Huh's Lorentzian theorem the natural structural candidate: the homogeneous multivariate Tutte polynomial is Lorentzian for `0<q<=1`, and its fixed-degree pieces inherit strong log-concavity-type information.

If Lorentzian/SLC automatically implied the exact stochastic covering relation needed between adjacent cardinality layers, this would provide the missing all-graph theorem in one step. But the implication is false in general. The strongly-log-concave sampling literature explicitly records that **SLC does not imply SCP**: uniform measures on some matroid bases are SLC while failing a negative-dependence property forced by SCP.

So the category change was informative but did **not** close C0146. It isolates the missing ingredient sharply: any all-graph proof must use more than Lorentzianity alone—either graphic-specific structure or a transport identity stronger than generic SLC.

Outcome of #1: **generic Lorentzian/SLC machinery is insufficient as a black box; a graphic-specific covering mechanism is still needed**.

## 6. Method #20 — FIND WHY THE ALGORITHM FAILS: the obvious bridge/nonbridge deletion kernel

I next tried to turn the graphic structure into a direct Markov deletion rule, rather than another LP certificate.

Fix an `r`-edge set `A`, and let `t(A)` be the number of absent graph edges whose endpoints lie in different connected components of `A`. Adding one of those edges leaves cycle nullity unchanged; adding any of the other `m-r-t(A)` absent edges raises nullity by one.

Consider the simplest possible reverse kernel from an `(r+1)`-edge set `B`: assign unnormalized deletion weight `alpha` to a bridge of `B` and `beta` to a nonbridge. The total incoming unnormalized mass at `A`, starting from target weights `q^{c(B)}`, is

`q^{c(A)} [ alpha t(A) + beta q (m-r-t(A)) ].`                 (6.1)

For this to be proportional to the desired source weight `q^{c(A)}` independently of `A`, the coefficient of `t(A)` must vanish, forcing

`alpha = beta q`.                                                (6.2)

This looks promising until the required row normalization is imposed. If `b(B)` is the number of bridges of `B`, then the total deletion weight out of `B` is

`alpha b(B) + beta((r+1)-b(B))
 = beta[ q b(B) + (r+1)-b(B) ].`                                (6.3)

At a fixed size `r+1`, the bridge count `b(B)` is not constant. Normalizing (6.3) therefore introduces a `B`-dependent denominator and destroys the cancellation in (6.1). In particular, no deletion algorithm depending **only** on whether the deleted edge is a bridge or nonbridge can produce the desired adjacent-layer coupling on general graphs.

This is the precise obstruction to the most obvious graphic-specific constructive kernel. It explains why the exact coefficient flows found previously contain genuinely finer state information than bridge status alone.

Outcome of #20: **two-state bridge/nonbridge deletion is structurally too coarse; the obstruction is the varying bridge count at fixed layer**.

## 7. Method #19 — MAKE IT AN ALGORITHM: exact nine-edge obstruction search

Having first eliminated the two most plausible black-box/closed-form routes, I used the previous Bernstein transport as an exact decision algorithm specifically to hunt for the first coefficient Hall obstruction at the nine-edge frontier.

For adjacent layers `r,r+1`, use unnormalized desired margins

`row_A(q)=q^{c(A)} W_{r+1}(q)`,
`col_B(q)=q^{c(B)} W_r(q)`.

Expand each polynomial in the degree-`N` Bernstein basis

`B_{j,N}(q)=binom(N,j) q^j(1-q)^{N-j}`

using

`q^k = sum_{j=k}^N [binom(j,k)/binom(N,k)] B_{j,N}(q)`.

All coefficients are nonnegative. For each coefficient index `j`, solve the finite inclusion bipartite flow problem with those exact rational row/column margins. If every coefficient flow exists, their Bernstein-weighted sum is a nonnegative inclusion transport for every `q in [0,1]` simultaneously.

The new issue is exact completeness of the nine-edge 2-connected block list. A 2-connected simple graph with nine edges has at most nine vertices because minimum degree is at least two.

### 7.1 Exact classification at nine edges

For `n=5,6,7`, I exhaustively enumerated every labeled nine-edge simple graph, tested 2-connectivity, and quotiented by an exact degree-preserving canonical code. The checker finds respectively

- labeled 2-connected counts `10, 3535, 46830`;
- unlabeled counts `1, 14, 20`.

For `n=8`, the degree sum is 18, so the total degree surplus above two is exactly two. There are only two possible degree patterns:

1. one vertex of degree four and all other vertices of degree two; or
2. two vertices of degree three and all other vertices of degree two.

The first pattern is impossible in a 2-connected graph: after deleting the unique degree-four vertex, its four neighbors have degree one and every remaining vertex has degree at most two. A connected graph of maximum degree two has at most two degree-one vertices, so the deletion is disconnected, contradicting 2-connectivity.

Hence there are exactly two degree-three vertices and all other vertices have degree two. Suppressing the degree-two vertices gives three internally vertex-disjoint paths between the two degree-three vertices: a theta graph. Their positive integer path lengths sum to nine. Simplicity permits at most one path of length one. The sorted possibilities are exactly

`(1,2,6), (1,3,5), (1,4,4), (2,2,5), (2,3,4), (3,3,3)`,

so there are exactly six `n=8` types.

For `n=9`, minimum degree two and average degree two force every degree to equal two; connectedness gives the unique cycle `C9`.

Therefore the exact number of nine-edge 2-connected simple-graph types is

`1+14+20+6+1 = 42`.                                               (7.1)

### 7.2 Exact coefficient transports

Degree `N=9` suffices for every margin polynomial on all 42 representatives. There are

- `42 * 9 = 378` adjacent-layer transport pairs;
- `10` Bernstein coefficient indices (`j=0,...,9`);
- hence `3780` exact coefficient max-flow instances.

Every instance is feasible. The checker uses only exact integers and `Fraction` rational arithmetic. After each max-flow it independently re-sums the realized inclusion-edge flows and asserts every row and every column margin. No floating point, interpolation grid, random search, or external package is used.

Outcome of #19: **no nine-edge coefficient Hall obstruction exists; the exact algorithm certifies every nine-edge 2-connected block**.

## 8. The nine-edge theorem

**Theorem (source-valid restricted result).** Let `G` be any finite simple graph with at most nine edges and let `q in (0,1)`. Then the family `{FK_G(p,q): 0<=p<=1}` admits a monotone grand coupling in `p`. In particular,

`FK_G(p1,q) <=_st FK_G(p2,q)` whenever `p1<=p2`.

### Proof

The preceding C0146 report proved the theorem for all finite simple graphs with at most eight edges, so only graphs containing a nine-edge 2-connected block are new.

Let `H` be a 2-connected simple graph with exactly nine edges. By Section 7.1, `H` is isomorphic to one of the 42 exactly classified representatives. For every adjacent fixed-size pair of layers of that representative, Section 7.2 and the exact coefficient flows give a nonnegative inclusion coupling `nu_r <=_st nu_{r+1}` for every `q in (0,1)`. Compose those adjacent kernels to obtain a nested fixed-size chain. Couple the stochastically increasing FK size distributions by a common quantile variable; the reduction in Section 4 then gives a monotone grand coupling with exact `FK_H(p,q)` marginals.

For a general graph `G` with at most nine edges, decompose into blocks. Every 2-connected block has at most nine edges and is covered either by the preceding `<=8` theorem or the new exactly-nine-edge argument. One-edge bridge blocks are monotone directly. Random-cluster weights factor across one-vertex block sums and disconnected components up to configuration-independent factors, so take the block grand couplings independently and unite their open-edge sets. The resulting coupling is monotone in `p` and has the exact FK law on `G` at each `p`.

This proves the theorem. `QED`

The theorem moves the frozen finite cutoff but does **not** solve Pete's unrestricted all-finite-graphs question and does not certify the `q=0` endpoint.

## 9. Exact self-check and archived evidence

The mathematical routes in Sections 5–7 were developed before the new checker was treated as evidence. The finite core was then executed exactly. This is a **self-check, not an independent audit**.

Artifacts:

- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m9_bernstein_checker.py`
  - creation commit `cb0482356f2b82bbfb708704e521435763b44545`;
- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m9_bernstein_checker.out`
  - creation commit `b7814bc46d6349875aab2679d4fd70c1a99d998f`;
  - read-back blob `757de79304b5a4291164a1793955ba5d507a8f4b`.

Archived output:

```text
labeled_biconnected_n5_n6_n7 [10, 3535, 46830]
unlabeled_counts_by_n {5: 1, 6: 14, 7: 20, 8: 6, 9: 1}
theta_path_partitions_n8 [(1, 2, 6), (1, 3, 5), (1, 4, 4), (2, 2, 5), (2, 3, 4), (3, 3, 3)]
m9_representatives_total 42
adjacent_layer_transport_pairs 378
bernstein_degree 9
coefficient_flow_instances 3780
ALL_EXACT_CHECKS_PASS
```

## 10. Honest status, counters, and next route

The frozen metric genuinely moves

`m_cert: 8 -> 9`.

Therefore the unchanged-run counter remains **0** and stuck recoveries remain **0**. The source status is **OPEN** and this result is **PARTIAL**. Required source-closure audits remain **P26 = NOT PASSED** and **NM13-06 = NOT PASSED** for C0146; neither neighboring work nor this self-check counts as an independent audit.

The nine-edge result also says what **not** to do next. Repeating a blind `m=10` census would ignore the structural lesson of this run. The next high-value route is to use the exact flows to infer a graphic-specific transport invariant finer than bridge/nonbridge status, preferably via ear decomposition or cyclomatic-number localization. A natural target is a theorem for an infinite structural class (for example theta/series-parallel blocks) that explains coefficient-flow feasibility, with an exact Hall obstruction search only as a falsification tool.

Reserved fresh methods for the next invocation: **#3 PROVE SOMETHING STRONGER, #10 DERANDOMIZE, #30 DO ONE PRIME/ONE SCALE/ONE DIRECTION AT A TIME**. They are not credited as tried in this report.

```yaml
ledger_delta:
  track: NM13-05
  source_id: C0146
  claim_id: C0146
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  source_status: OPEN
  status: PARTIAL
  metric_name: m_cert
  metric_definition: "largest m rigorously certified for all finite simple graphs with <=m edges, q in (0,1), and all p1<=p2, under FK stochastic order"
  before: 8
  after: 9
  movement: true
  methods_actual: [1, 20, 19]
  method_outcomes:
    1: "Lorentzian/graphic-matroid category identified, but generic SLC does not imply stochastic covering; no black-box source proof"
    20: "bridge/nonbridge-only deletion kernel fails because row normalization depends on the variable bridge count"
    19: "exact nine-edge classification plus Bernstein coefficient max-flow succeeds for all 42 2-connected types"
  exact_checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m9_bernstein_checker.py
  exact_checker_commit: cb0482356f2b82bbfb708704e521435763b44545
  exact_output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m9_bernstein_checker.out
  exact_output_commit: b7814bc46d6349875aab2679d4fd70c1a99d998f
  exact_output_blob: 757de79304b5a4291164a1793955ba5d507a8f4b
  finite_counts:
    labeled_biconnected_n5_n6_n7: [10, 3535, 46830]
    unlabeled_n5_to_n9: [1, 14, 20, 6, 1]
    nine_edge_types_total: 42
    adjacent_layer_pairs: 378
    bernstein_degree: 9
    coefficient_flow_instances: 3780
  unchanged_runs: 0
  stuck_recoveries: 0
  audits:
    P26: NOT_PASSED
    NM13-06: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_status: "Pete Q13.2 still printed in current source PDF; Park 2608.08565 and Tang-Zhang 2609.11578 do not settle arbitrary finite-graph monotone coupling; Lorentzianity alone does not imply stochastic covering; bounded search only; novelty UNVERIFIED"
  next_step: "seek a graphic-specific transport invariant/ear-decomposition theorem explaining Bernstein feasibility, using exact Hall obstruction search only as falsification"
  next_methods_reserved: [3, 10, 30]
```

No shared root, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified. The only writes in this invocation were the warranted exact C0146 checker/output and this single immutable NM13-05 report.
