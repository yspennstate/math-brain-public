Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `m_cert = UNMEASURED -> 5`. Section-B methods actually tried: #2 ATTACK THE NEGATION FIRST, #8 GO THE OTHER WAY AND DISCRETIZE, #11 DUALIZE. Status: PARTIAL.**

# NM13-05 / C0146 — fixed-size layer transport and the exact five-edge theorem

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Source: Gábor Pete, *Probability and Geometry on Groups*, Question 13.2 (printed p. 185; current PDF extraction p. 184)  
Canonical problem / claim: **C0146**  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`  
Selection residue: `4` modulo 13  
Frozen metric: `m_cert` as defined in `operations/claims/C0146.md`  
Metric before / after: **UNMEASURED -> 5**  
Unchanged-run counter after this invocation: **0**  
Stuck recoveries: **0**  
Required eventual auditors for a completed source claim: **P26 and NM13-06; neither is presumed to pass**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still has prompt/title, timing/schedule and enabled-state controls but **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore GPT-6/maximum remains prompt text only. Enforcing it would require an owner-authorized product/workspace/API/admin surface that exposes those controls and authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` event is an authorization-context boundary; current `RESULTS.md` records that P26 was later modified successfully from another authorized context. The lawful workaround for a future refusal is the owning/authorized context or platform/admin support, never cloning the task or bypassing access control.

## 2. Continuity and required repository read

This run continued from the newest NM13-05 report available at start:

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T07-32-00Z__successor-admission-screen-2-e-series.md`.

That report preserved the mandatory six-unchanged-run handoff of old target D0004, so D0004 was not reopened and its old metric was not inherited.

Before admission I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report above;
- newest visible neighboring NM13-04 state (`2026-09-18T07-25-00Z__p0457-disconnected-shell-correction.md`);
- newest visible neighboring NM13-06 state (`2026-09-18T07-30-30Z__p0195-stuck-recovery-1.md`);
- the C-intake source row, raw Pete source transcription, `C0146-A001`, canonical aliases/dedup index, current claims, historical campaign references, and exact-key searches.

Large aggregate files are connector-bounded when rendered wholesale, so exact source IDs/keys, immutable reports and targeted claim/history searches are the continuity anchors. Truncated aggregate output was not treated as evidence of absence.

## 3. Admission: why C0146 passes now

The unresolved custom-dedup C backlog left by the preceding run contains a genuinely focus-fit residue-4 source:

- intake ID: `C0146`;
- canonical key: `fk_q_less_than_1_monotone_coupling`;
- SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`;
- residue: `4`;
- exact source question: **“Is there a monotone coupling `(omega_p)_{p in [0,1]}` of the `FK(p,q)` measures for any `q in [0,1)`?”**

I re-read the public source PDF around the question. The immediately following Exercise 13.8 asks for an explicit monotone coupling between UST and UST+1 on the six-vertex, seven-edge digital-figure-8 graph. This confirms that finite exact transport is source-native, not an invented proxy.

The only prior repository attempt recovered is `C0146-A001`; it observed that stochastic monotonicity in `p` is necessary, noted that FKG/Holley no longer supplies it for `q<1`, and explicitly left a **small-graph symbolic test** as the next step. It did not solve or claim the source.

Current claim/history searches found no C0146 owner, no handoff, no POSTED/campaign closure and no retired-source instruction. `operations/claims/C0146.md` was absent immediately before the create-only write. The canonical claim was therefore created with create-only semantics at commit

`d63e2c8dc30d0db5fdea54568a2d045890382bf3`

and read back at that exact commit before mathematical work continued.

A bounded current-literature check dated 2026-09-18 used the exact source wording plus searches for `q<1` random-cluster stochastic monotonicity in `p`. It recovered, among other nearby work, Heehyun Park's August 2026 preprint on the `q<1` random-cluster model on wired regular trees, which proves uniqueness and branch negative-dependence results, not the source's general monotone-in-`p` coupling. I found no source-matching general resolution. This is bounded negative evidence only; **publication novelty is UNVERIFIED**.

## 4. Frozen quantity

The source question is not replaced. For measurable progress I froze the following finite source-relevant quantity in the canonical claim:

`m_cert` = the largest integer `m` for which NM13-05 has a rigorous certificate that for **every finite simple graph with at most `m` edges**, every `q in (0,1)`, and all `0 <= p1 <= p2 <= 1`,

`FK_G(p1,q) <=_st FK_G(p2,q)`

under edge inclusion.

At admission the baseline was **UNMEASURED**, not zero. This run proves `m_cert >= 5`; under the frozen convention I record the achieved certified cutoff as **5**. This remains a restricted theorem relative to Pete's full question, in particular because the source includes the `q=0` endpoint/convention and has no five-edge restriction.

## 5. Method #2 — attack the negation first

I first searched for a source-valid finite obstruction rather than trying to prove monotonicity. The relevant finite dual test is: for `p1<p2`, a monotone coupling can exist only if every increasing up-set `U` of edge configurations satisfies

`phi_{p1,q}(U) <= phi_{p2,q}(U)`.

An exploratory maximum-weight-upset/min-cut search over the small nonisomorphic simple-graph atlas through seven edges, across a grid of `q` and `p`, produced **no violating up-set**. This search used floating arithmetic and is **not a certificate** and proves nothing by itself. Its value was diagnostic: the first obstruction did not appear at tiny size, and the extremal transport structure suggested conditioning on the number of open edges.

No approximate or simulated output is used below.

## 6. Method #8 — discretize by fixed edge count

Let `G=(V,E)` be a finite graph with `m=|E|`, fix `q>0`, and write configurations as subsets `A subseteq E`. Put

`w_q(A)=q^{k(A)}`,

where `k(A)` is the number of connected components of `(V,A)`. For `0<p<1`, set `t=p/(1-p)`. Then

`phi_{p,q}(A) = w_q(A) t^{|A|} / Z(t)`.

For each `r`, let

`W_r = sum_{|A|=r} w_q(A)`

and let `nu_r` be the `p`-independent fixed-size law

`nu_r(A)=w_q(A)/W_r`,  `|A|=r`.

Thus FK is the exact mixture

`phi_{p,q} = sum_{r=0}^m alpha_p(r) nu_r`,

where

`alpha_p(r) = W_r t^r / sum_s W_s t^s`.

If `p1<p2`, then

`alpha_{p2}(r)/alpha_{p1}(r) = C (t2/t1)^r`,

which is increasing in `r`. Therefore the size law `alpha_p` is stochastically increasing in `p`; on the total order `{0,...,m}` it has the usual monotone quantile grand coupling `R_p`.

Consequently, it is enough to build nested adjacent fixed-size couplings

`X_0 subseteq X_1 subseteq ... subseteq X_m`,  `X_r ~ nu_r`.

Indeed, choose such a chain independently of the monotone size process and set

`omega_p := X_{R_p}`.

Then `omega_p` is monotone in `p`, and conditioning on `R_p=r` gives exactly `nu_r`, hence its marginal is exactly `FK_G(p,q)`.

This reduction is exact and will be the main route for later runs.

## 7. A complete infinite special class: every finite cactus graph

A connected cactus graph is an iterated one-vertex sum of bridge blocks and simple-cycle blocks. Random-cluster weights factor across one-vertex sums: if `G=G1 vee G2` shares exactly one articulation vertex and `A=A1 union A2`, then

`k_G(A)=k_{G1}(A1)+k_{G2}(A2)-1`.

Hence `q^{k_G(A)}` differs from the product `q^{k_{G1}(A1)}q^{k_{G2}(A2)}` only by the constant `q^{-1}`, and the FK law is a product of its block laws. Disconnected components factor similarly. It is therefore enough to grand-couple each block.

For a bridge block, the edge is open with probability

`p_hat = p/(p+q(1-p))`,

which is increasing in `p`, so a single uniform label gives a monotone grand coupling.

For a cycle `C_l`, conditional on having exactly `r` open edges the configuration is uniform among the `r`-subsets of the cycle (including `r=l`; the exceptional cycle-rank factor changes only the weight assigned to that size). The size distribution again has monotone likelihood ratio in `r` as `p` increases. Couple all uniform `r`-subsets by taking the first `r` edges of one uniformly random permutation of the cycle, and combine this with the monotone size coupling.

Taking independent block couplings proves:

**Theorem A (cactus class).** For every finite cactus graph `G` and every `q>0`, the family `{FK_G(p,q): 0<=p<=1}` admits a monotone grand coupling in `p`.

This is a complete restricted-class theorem, not a claim that the unrestricted source is solved.

## 8. Method #11 — Strassen transport on the unique five-edge non-cactus block

To move the universal simple-graph cutoff past four edges, the only new 2-connected block is the **diamond** `K4-e`. Label its five edges by bit positions `0,...,4`, with edge 0 shared by the two triangles `{0,1,2}` and `{0,3,4}`.

For a fixed size `r`, the component counts are:

- `r=0`: one state with `k=4`;
- `r=1`: five states, all `k=3`;
- `r=2`: ten states, all `k=2`;
- `r=3`: eight spanning trees with `k=1`, and two triangles-plus-isolated-vertex states with `k=2`;
- `r=4`: five states, all `k=1`;
- `r=5`: one state with `k=1`.

Thus `nu_1`, `nu_2`, and `nu_4` are uniform. The only nonuniform fixed-size layer is `nu_3`, with

`nu_3(B)=1/[2(4+q)]` for each of the 8 spanning trees,

`nu_3(B)=q/[2(4+q)]` for each of the 2 triangle states.

The transitions `0->1`, `1->2`, `4->5` have the standard nested uniform-subset coupling. It remains to couple `nu_2 -> nu_3` and `nu_3 -> nu_4`.

I formulated each as the finite Strassen transport LP on the incidence bipartite graph `A subset B`. Its dual obstruction is exactly an up-set/Hall inequality. Instead of filing a numerical LP solution, I found exact integer endpoint flows and interpolate them convexly in `q`.

### 8.1 Exact `2 -> 3` flow

Let `F23(q)=(1-q)F23_0 + q F23_1`. Nonzero entries of `F23_0` are

`3->11:18, 3->19:6, 5->13:18, 5->21:6, 6->14:18, 6->22:6,`

`9->11:12, 9->13:12, 10->14:12, 10->26:12, 12->28:24,`

`17->19:24, 18->22:24, 20->21:24, 24->26:18, 24->28:6`.

Nonzero entries of `F23_1` are

`3->7:30, 5->13:30, 6->14:30, 9->11:30, 10->26:30,`

`12->28:30, 17->19:30, 18->22:30, 20->21:30, 24->25:30`.

Every displayed arrow is inclusion of a 2-edge mask in a 3-edge mask. Since this is convex interpolation of nonnegative endpoint flows, every entry is nonnegative for `0<=q<=1`.

The exact row sums are `24+6q` for each of the ten 2-subsets. The exact column sums are `30` for each spanning-tree 3-subset and `30q` for each triangle 3-subset. The total flow is `60(4+q)`. After normalization, each source row has mass

`(24+6q)/(60(4+q)) = 1/10`,

while target columns have masses exactly `1/[2(4+q)]` or `q/[2(4+q)]`. Hence this is an exact monotone coupling `nu_2 <=_st nu_3`.

### 8.2 Exact `3 -> 4` flow

Let `F34(q)=(1-q)F34_0 + q F34_1`. Nonzero entries of `F34_0` are

`11->15:8, 11->27:2, 13->15:8, 13->29:2, 14->30:10,`

`19->23:6, 19->27:4, 21->23:6, 21->29:4, 22->23:4,`

`22->30:6, 26->27:10, 28->29:10`.

Nonzero entries of `F34_1` are

`7->15:10, 11->15:10, 13->29:10, 14->30:10, 19->23:10,`

`21->23:10, 22->30:10, 25->27:10, 26->27:10, 28->29:10`.

Again every arrow is inclusion. Exact row sums are `10` on each spanning-tree 3-state and `10q` on each triangle 3-state. Every 4-state column sum is `16+4q`. The total flow is `20(4+q)`. Normalizing therefore gives exactly the `nu_3` source masses and the uniform `1/5` target masses. Hence `nu_3 <=_st nu_4`.

Together with the trivial/uniform adjacent layers, these flows produce a nested chain `X_0 subset ... subset X_5` with `X_r~nu_r`; Section 6 then gives a monotone grand coupling in `p` for the diamond for every `0<q<1` (indeed the displayed transport is valid through `q=1`).

## 9. Why this certifies every simple graph with at most five edges

Let `H` be a 2-connected simple graph with at most five edges. A 2-connected graph has minimum degree at least two, so `|V(H)| <= |E(H)|`.

- If `|E(H)|=|V(H)|`, the sum of degrees is exactly `2|V(H)|`; minimum degree at least two therefore forces every degree to be two, so `H` is a cycle.
- If `|E(H)|>|V(H)|` and `|E(H)|<=5`, then `|V(H)|<=4`. A simple graph on three vertices has at most three edges, so the only non-cycle possibility is `|V|=4, |E|=5`, namely `K4-e`, the diamond.

Every finite graph decomposes into bridge and 2-connected blocks. Therefore a finite simple graph with at most five edges either has only bridge/cycle blocks (the cactus theorem) or its five edges form the diamond block. Both cases have now been proved monotone.

**Theorem B (five-edge source class).** For every finite simple graph `G` with at most five edges, every `q in (0,1)`, and all `0<=p1<=p2<=1`, there is a coupling with

`omega_{p1} subseteq omega_{p2}` almost surely,

and in fact the full one-parameter family admits a monotone grand coupling.

This proves the frozen movement `m_cert = UNMEASURED -> 5`.

## 10. Exact finite certificate

The finite core was checked independently of the exploratory search with integer arithmetic only:

- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m5_exact_checker.py`
- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m5_exact_checker.out`

The checker exhaustively enumerates the 2-connected labeled simple graphs with at most five edges and confirms that every one is a cycle or diamond; verifies the diamond fixed-size component-count profile; verifies every support inclusion and every constant/linear coefficient in both affine transport tables. Its archived output is:

`two_connected_simple_graphs_checked 22`

`diamond_layer_counts [1, 5, 10, 10, 5, 1]`

`F23_endpoint_support_sizes 16 10`

`F34_endpoint_support_sizes 13 10`

`ALL_EXACT_CHECKS_PASS`

The checker was executed locally before archiving. This is a **self-check**, not an independent audit.

## 11. Section-B accounting and outcomes

**#2 ATTACK THE NEGATION FIRST.** Searched directly for a small increasing-event violation / finite no-coupling witness. No candidate emerged in the exploratory small-graph scan. The failure was informative: tiny graphs appear to support, not obstruct, the conjecture.

**#8 GO THE OTHER WAY AND DISCRETIZE.** Conditioned exactly on the number of open edges, turning the continuous `p`-family into finitely many `p`-independent layers `nu_r`. This produced the core exact reduction and the cactus theorem.

**#11 DUALIZE.** Recast adjacent-layer monotonicity as Strassen transport feasibility, with increasing-event/Hall inequalities as the dual obstruction. On the diamond, exact primal transport tables at the two endpoint structures and convex interpolation in `q` close the only nontrivial five-edge cases.

All three methods were genuinely attempted in this run and are now spent for C0146. No method is credited merely for screening.

## 12. Literature status and scope discipline

Dated bounded searches on 2026-09-18 included:

- exact Pete Question 13.2 wording plus `FK(p,q)` / `q<1` / monotone coupling;
- `random-cluster q<1 stochastic monotonicity in p`;
- recent 2025-2026 `q<1` random-cluster work and citing/nearby papers.

The public Pete PDF still states Question 13.2 as open and immediately gives the finite UST/UST+1 coupling exercise. Park's August 2026 `q<1` wired-tree paper addresses uniqueness and negative dependence on a special infinite tree class, not this general monotone-in-`p` coupling. I found no source-matching later theorem resolving the universal question. **A bounded search is not proof of worldwide openness, and novelty of Theorems A/B is UNVERIFIED.**

The source itself remains **OPEN** in this report. Theorems A/B are **PARTIAL**: no counterexample was found, no unrestricted proof was produced, and no claim is made for the source's `q=0` endpoint convention beyond the exact transport limiting structures used internally.

## 13. Audits, counters, and next route

No outside audit is counted:

- P26: **NOT PASSED / not requested as a result of this run**;
- NM13-06: **NOT PASSED / not requested as a result of this run**.

Because the frozen metric moved on the first admitted C0146 invocation:

- `unchanged_runs = 0`;
- `stuck_recoveries = 0`.

The next high-value mathematical step is **not** another blind grid search. The six-edge frontier contains the first additional 2-connected blocks beyond cycles/diamond. The fixed-size reduction turns each into a finite parametric transport problem. A genuinely new next route is to seek a polynomial/Bernstein-basis transport whose coefficient flows are exact and nonnegative on `q in [0,1]`; if that succeeds uniformly across the six-edge block types, the same block argument moves `m_cert` to 6. If this stops moving the cutoff, return to the method menu rather than manufacturing more certificates at `m_cert=5`.

## 14. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE OUTSIDE
  status: PARTIAL
  source_id: C0146
  claim_id: C0146
  source_locator: "Gabor Pete, Probability and Geometry on Groups, Question 13.2, printed p.185"
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  canonical_sha256: dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6
  selection_residue: 4
  claim_commit: d63e2c8dc30d0db5fdea54568a2d045890382bf3
  metric_name: m_cert
  metric_definition: "largest edge cutoff rigorously certified for all finite simple graphs, all q in (0,1), and all p1<=p2"
  metric_before: UNMEASURED
  metric_after: 5
  mathematical_movement: true
  source_scope_status: OPEN
  proved_scope:
    - "all finite cactus graphs, every q>0"
    - "all finite simple graphs with at most 5 edges, every q in (0,1)"
  methods:
    - number: 2
      name: ATTACK_THE_NEGATION_FIRST
      outcome: "no small finite obstruction found; route redirected to structural positive theorem"
    - number: 8
      name: DISCRETIZE
      outcome: "exact fixed-edge-count layer reduction; cactus grand coupling"
    - number: 11
      name: DUALIZE
      outcome: "Strassen transport/Hall dual; exact affine diamond flows"
  exact_checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m5_exact_checker.py
  exact_output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m5_exact_checker.out
  exact_output_commit: 2b2cad74b1f94eff267e52da1d2c71724aab7a68
  checker_result: ALL_EXACT_CHECKS_PASS
  unchanged_runs: 0
  stuck_recoveries: 0
  audits:
    P26: NOT_PASSED
    NM13-06: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_status: "bounded search found no source-matching general resolution; novelty UNVERIFIED"
  next_step: "six-edge 2-connected blocks via exact parametric/Bernstein transport; move m_cert or abandon route"
```

No shared root, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation. The only writes were the canonical create-only claim, substantive exact checker/output in NM13-05, and this single immutable run report.
