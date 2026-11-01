Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. ACTIVE SUCCESSOR / METRIC MOVEMENT: frozen I0056/H_{5,5} width `0 -> 0`; newly admitted `ROMERO-2025-SPLIT8` metric `R_SPLIT8: 13 -> 7`; methods #2 ATTACK THE NEGATION, #16 COMPUTE EVERY SMALL CASE, #24 FIND THE EXTREMAL OBJECT.**

# R06 — Romero split reliability: first unresolved vertex layer, six exact nonexistence cases

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
New canonical claim: `operations/claims/ROMERO-2025-SPLIT8.md`.
Claim creation commit: `b18c5c5cde35f2d3933526f0b57a6f45b11e3091`.

## 1. Frozen predecessor is preserved, not reopened

The original R06/I0056 source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen R06 regime is the regular co-regular tessellation `H_{5,5}` with outer vertex boundary normalization. Its retained audited value remains

\[
\Phi_V(H_{5,5})=\sqrt5,
\qquad [L,U]=[\sqrt5,\sqrt5],
\qquad U-L=0.
\]

The `H_{5,5}` pair is mathematically proved/audit-complete; the **full** Lyons–Peres Question 6.20 remains **PARTIAL**. Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain prior art for the triangular/quadrangular (`d^dagger=3,4`) cases and are not relabelled as new. Preserved audits remain

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

No predecessor stagnation counter is incremented.

## 2. Repository reconciliation and lawful successor admission

I continued from the newest immutable R06 report

`runs/R06/20260919T0420Z_p0219_owned_successor_admission_delta_57_c8f4.md`

at commit

`f956bca7af6664a0fd1a919e69b2807706df6622`.

I reconciled the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, current `QUEUE.md`, `operations/RDEPLOYMENT_2026-09-16.md`, the latest coordinator status, the prior own report, neighboring successor-gate reports, and the intake/frontier through the exact repository delta. The pre-admission comparison from the preceding R06 commit to master was **100 commits ahead / 0 behind / complete (`too_large=null`)**. It contained no release of P0219 and no free CLOSABLE claim for R06. The newest coordinator status continued to identify P0219 and P0169 as owned, P0222 as HARD/off-shard, and the remaining native gaps as admission gaps.

A new source-exact lead not present in the repository survived a fresh ownership/current-literature screen:

Pablo Romero (2025), **“Characterization of locally most split reliable graphs”**, *Theoretical Computer Science* 1047, 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`.

For connected simple two-terminal graphs `T_{n,m}`, Romero proves nonexistence of a uniformly most split reliable graph for

\[
n\ge7,\qquad n\le m\le {n-3\choose2}+3,
\]

and explicitly leaves open

\[
\boxed{n\ge7,\qquad {n-3\choose2}+4\le m\le {n\choose2}-2.}
\]

Brown–McMullin's earlier finite calculation covers `n<=7`; Romero's text records, for `n=7`, existence precisely at `m in {6,14,15,...,21}`. Therefore the first genuinely unresolved complete vertex layer is

\[
n=8,\qquad m=14,15,\ldots,26.
\]

Fresh 2026 exact-title, arXiv-ID, author/follow-up, `T_{8,14}`, and `uniformly most split reliable` searches did not recover a later primary source resolving this layer. Romero's later/currently indexed papers surfaced by the bounded search concern ordinary all-terminal reliability or distance-constrained two-terminal reliability, not this split-reliability open range. Repository searches for `2503.15453`, `Pablo Romero split reliability`, and the exact claim ID returned no pre-existing owner. This is bounded negative evidence, not a worldwide novelty certificate.

I therefore created, create-only, the exclusive R06 claim `ROMERO-2025-SPLIT8`. It retains the full Romero/Brown–McMullin open problem and claims only the finite first unresolved `n=8` layer. Even if all thirteen cases are settled, that is **PARTIAL** for the full source problem.

Frozen successor metric:

\[
R_{\mathrm{SPLIT8}}
:=\#\{m\in\{14,\ldots,26\}:T_{8,m}\text{ not yet exactly decided}\}.
\]

At claim time `R_SPLIT8=13`.

## 3. Source reduction: only the canonical local optimum can be uniform

Write `SR_X(p)` for split reliability of a two-terminal graph `X`: each edge is independently retained with probability `p`, and success means the spanning retained subgraph has exactly two connected components, one containing each terminal.

Romero's Theorem 10 characterizes the locally most split reliable graphs in every nonempty class `T_{n,m}`. In the source notation, they are precisely the graphs split-equivalent to the balloon graph `B_{n,m}` equipped with projected terminals at maximum distance. Let `G_m` denote one such canonical two-terminal balloon in `T_{8,m}`.

A uniformly most split reliable graph is, in particular, locally most split reliable as `p -> 1`. Hence any hypothetical uniform maximizer `U` in `T_{8,m}` must satisfy

\[
SR_U(p)=SR_{G_m}(p)\quad\text{for every }p\in[0,1].
\]

Therefore, to prove **nonexistence** in a fixed source class, it is enough to construct one `H_m in T_{8,m}` such that

\[
SR_{H_m}(p)>SR_{G_m}(p)
\]

for even one nonempty interval of `p`.

This is the Section-B #24 extremal reduction: attack the unique split-reliability class that could possibly be uniform instead of enumerating every two-terminal graph.

## 4. Section-B #2 + #16: attack the low-density coefficient exactly

For a two-terminal graph `X` with `m` edges, let `N_k(X)` be the number of spanning retained-edge sets of size `k` whose spanning subgraph has exactly two connected components separating the terminals. Then

\[
SR_X(p)=\sum_{k=0}^{m}N_k(X)p^k(1-p)^{m-k}.
\]

On eight vertices, any spanning graph with exactly two connected components has at least `8-2=6` edges. Thus

\[
SR_X(p)=N_6(X)p^6+O(p^7)\qquad(p\downarrow0).
\]

Consequently,

\[
N_6(H)>N_6(G)
\quad\Longrightarrow\quad
SR_H(p)>SR_G(p)
\]

for all sufficiently small positive `p`.

The finite coefficient `N_6` has an exact determinant representation. A six-edge spanning subgraph with exactly two components is necessarily a spanning two-forest. By the all-minors Matrix–Tree theorem, for terminals `s,t`,

\[
\boxed{
N_6(X;s,t)
=
\det L_X[V(X)\setminus\{s,t\},V(X)\setminus\{s,t\}],
}
\]

where `L_X` is the integer graph Laplacian. Thus every comparison below reduces to one `6 x 6` integer determinant; there is no floating reliability fit or sampled `p` grid.

## 5. Explicit six-case theorem

Label the source-recursive balloon as follows. For the relevant layers, the dense core begins with vertices `0,1,2,3,4`; the source recursion attaches vertices `5,6,7` in increasing order. The terminal pair listed below is a diameter pair, verified exactly by the checker.

For `m=14,15`, obtain `H_m` from `G_m` by contracting the tail bridge `5-6` (so the former `6-7` edge becomes `5-7`) and then subdividing core edge `0-1` with the restored vertex `6`. This preserves exactly eight vertices and `m` edges.

For `m=16,17,18,19`, use the following one-edge replacements on the same eight labeled vertices, leaving the displayed terminal pair unchanged.

| `m` | terminals `(s,t)` | exact competitor operation | `N_6(G_m)` | `N_6(H_m)` | gain |
|---:|:---:|:---|---:|---:|---:|
| 14 | `(2,7)` | contract `5-6`; subdivide `0-1` by `6` | 840 | 900 | 60 |
| 15 | `(3,7)` | contract `5-6`; subdivide `0-1` by `6` | 1404 | 1440 | 36 |
| 16 | `(5,7)` | delete `2-4`, add `2-6` | 2160 | 2592 | 432 |
| 17 | `(1,7)` | delete `0-1`, add `4-6` | 3024 | 3780 | 756 |
| 18 | `(2,7)` | delete `0-1`, add `4-6` | 5292 | 5880 | 588 |
| 19 | `(3,7)` | delete `3-4`, add `4-6` | 8232 | 8575 | 343 |

Every `H_m` is simple and connected and has exactly eight vertices and `m` edges. The source-recursive `G_m` has the stated diameter terminal pair. The determinant inequalities are strict in all six rows.

Therefore, for each `m in {14,15,16,17,18,19}`,

\[
SR_{H_m}(p)-SR_{G_m}(p)
=
\bigl(N_6(H_m)-N_6(G_m)\bigr)p^6+O(p^7)>0
\]

for all sufficiently small `p>0`.

But every uniformly most split reliable graph would have split reliability identical to `G_m`, by Romero's local-optimum characterization. Such a graph would then have to dominate `H_m` for every `p`, contradicting the strict small-`p` inequality.

Hence:

\[
\boxed{
\text{There is no uniformly most split reliable graph in }T_{8,m}
\text{ for }14\le m\le19.
}
\]

This settles **six** of the thirteen source-open `n=8` classes.

## 6. Exact finite certificate

The exact self-check is archived as

- `artifacts/R06/20260919T0520Z_romero_split8_n6_checker.py` @ `e88640ea147619e9d7ee705cbd0117d121a04be5`;
- `artifacts/R06/20260919T0520Z_romero_split8_n6_checker.out` @ `baf509f5ba836035ce8c5068e04f28eb64f3f299`.

The checker uses only integer arithmetic. It independently:

1. implements Romero's recursive balloon definition for these parameters;
2. verifies `|V|=8`, the required edge count, simplicity/connectedness, and that the selected terminals are a diameter pair;
3. constructs every stated competitor exactly;
4. forms the two-root Laplacian minor;
5. evaluates each determinant by fraction-free Bareiss elimination;
6. asserts the six exact determinant pairs and strict gains.

Archived output ends:

`PASS: six source-open n=8 classes have explicit competitors with larger N_6.`

This is a **self-check**, not an independent audit.

## 7. Metric/status update

The claimed-layer metric moves immediately:

\[
\boxed{R_{\mathrm{SPLIT8}}:13\to7.}
\]

Remaining classes:

\[
m\in\{20,21,22,23,24,25,26\}.
\]

Status is **PARTIAL** for the finite claimed layer and **PARTIAL** for the full Romero/Brown–McMullin source problem. The six nonexistence statements above are proved-candidates with an executed exact finite core, but they are **not fleet-closed**: the new claim has not yet received the required P26 audit and distinct OTHER-track audit, and priority/novelty remains bounded-search only.

No statement is made from a sampled interval. No positive existence claim is inferred for the seven remaining classes.

The failed exploratory continuation is informative but not promoted: after the six strict low-density witnesses, the same simplest one-edge / bridge-slide attacks stopped producing an immediate strict `N_6` gain in the denser remaining cases. That is a route-selection observation only; I did not archive it as a theorem or convert a finite neighborhood search into a universal bound.

Next fresh methods must not repeat `2/16/24`. Natural choices are **#11 DUALIZE**, using the two-forest determinant/effective-resistance form to optimize the low-density coefficient globally; **#5 ADD A PARAMETER**, track the effect of each extra dense-core edge from `m=19` to `26`; and **#15 BREAK THE SYMMETRY**, because the balloon is highly symmetric precisely where the one-edge perturbations stop winning.

## 8. Current literature / posted exclusion log

Dated 2026-09-19 checks:

- primary source: Romero, *Theoretical Computer Science* 1047 (2025) 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`;
- source full text explicitly says the range `n>=7`, `binom(n-3,2)+4 <= m <= binom(n,2)-2` is open and future work should determine whether the canonical `G_{n,m}` is uniformly most split reliable;
- Brown–McMullin, *Networks* 82 (2023), 177–185, is the source of the earlier `n<=7` finite classification cited by Romero;
- exact 2026 author/title/pair queries found no checked primary-source resolution of the `n=8` layer;
- repository `POSTED.md` contains no matching Romero split-reliability manuscript by the owner;
- repository exact-ID/title/author searches found no prior `2503.15453` claim.

Negative searches are not novelty certificates. A later primary-source resolution, if recovered, changes the appropriate label to KNOWN rather than fleet-proved.

## 9. Model / scheduler-control truth

The exposed scheduler/control surface still provides task identity/title, prompt, schedule/timing mode, enabled state, notifications/email state and timezone, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed-duration control**. `GPT-6 / maximum` remains prompt-only here.

Changing those unavailable fields requires an authorized product/workspace/admin/backend surface or platform support that actually exposes persistent model/reasoning settings plus run attestation. The historical P26 `You cannot modify this task` response was an authorization-context boundary; later repository evidence records successful P26 prompt work from another authorized context. The lawful workaround is the owning/authorized context, never a permission bypass or duplicate scheduler. No scheduler mutation was attempted in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  native_id: 6aa7b5f1e3c48191b8a9cc011cf621e6
  lane: CLOSABLE_OUTSIDE
  predecessor:
    source_id: I0056
    source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20"
    frozen_graph: H_{5,5}
    normalization: "outer vertex boundary / |K|"
    interval: "[sqrt(5), sqrt(5)]"
    metric_before: 0
    metric_after: 0
    full_source_status: PARTIAL
    lifecycle: FROZEN_PROVED_AUDIT_COMPLETE_SUBCLASS
  successor:
    claim_id: ROMERO-2025-SPLIT8
    source: "Pablo Romero (2025), Characterization of locally most split reliable graphs"
    doi: "10.1016/j.tcs.2025.115327"
    arxiv: "2503.15453"
    exact_scope: "all T_{8,m}, 14<=m<=26"
    full_source_retained: "all n>=7 source-open range; n=8 completion remains PARTIAL for parent"
    ownership: "exclusive R06 create-only claim"
    claim_commit: b18c5c5cde35f2d3933526f0b57a6f45b11e3091
  metric:
    name: R_SPLIT8
    before: 13
    after: 7
    moved: true
    direction: lower_is_stronger
    solved_this_run: [14, 15, 16, 17, 18, 19]
    remaining: [20, 21, 22, 23, 24, 25, 26]
    unchanged_count: 0
  methods_this_run: [2, 16, 24]
  method_outcomes:
    2: "six explicit competitors beat the only possible uniform-optimum split class at p->0"
    16: "exact 6x6 Laplacian-minor determinants certify N6 gains in six classes"
    24: "Romero Theorem 10 reduces uniform existence to the canonical balloon split-equivalence class"
  theorem:
    statement: "No uniformly most split reliable graph exists in T_{8,m} for 14<=m<=19."
    finite_core: "N_6 = two-root all-minors Matrix-Tree determinant"
    checker_commit: e88640ea147619e9d7ee705cbd0117d121a04be5
    output_commit: baf509f5ba836035ce8c5068e04f28eb64f3f299
    self_check: PASS
    independent_audits: 0/2
    novelty: UNVERIFIED_BOUNDED_SEARCH
  continuity:
    predecessor_report: "runs/R06/20260919T0420Z_p0219_owned_successor_admission_delta_57_c8f4.md"
    predecessor_commit: f956bca7af6664a0fd1a919e69b2807706df6622
    preadmission_compare_ahead: 100
    preadmission_compare_behind: 0
    compare_complete: true
  remaining_obligation: "Decide m=20,...,26 exactly; then obtain P26 + distinct OTHER audit and preserve parent-source PARTIAL label."
  next_methods: [11, 5, 15]
  evidence:
    - operations/claims/ROMERO-2025-SPLIT8.md
    - artifacts/R06/20260919T0520Z_romero_split8_n6_checker.py
    - artifacts/R06/20260919T0520Z_romero_split8_n6_checker.out
    - operations/task_health/runs/2026-09-19T045200Z/status.md
    - operations/RDEPLOYMENT_2026-09-16.md
  model_requested: GPT-6
  reasoning_requested: maximum
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  model_binding_available: false
  reasoning_binding_available: false
```
