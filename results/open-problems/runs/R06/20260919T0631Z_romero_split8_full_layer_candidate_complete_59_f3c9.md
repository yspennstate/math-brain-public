Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. ACTIVE SUCCESSOR / METRIC MOVEMENT: frozen I0056/H_{5,5} width `0 -> 0`; `ROMERO-2025-SPLIT8` metric `R_SPLIT8: 7 -> 0`; methods #11 DUALIZE, #5 ADD A PARAMETER, #15 BREAK THE SYMMETRY.**

# R06 — Romero split reliability: exact completion of the first unresolved n=8 layer, audit gate pending

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Lane: **CLOSABLE OUTSIDE**.
Active canonical claim: `operations/claims/ROMERO-2025-SPLIT8.md`.

## 1. Frozen predecessor remains frozen

The original R06/I0056 source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen regular co-regular regime is `H_{5,5}` with outer-vertex-boundary normalization, and its retained audited value is still

\[
\Phi_V(H_{5,5})=\sqrt5,
\qquad [L,U]=[\sqrt5,\sqrt5],
\qquad U-L=0.
\]

The `H_{5,5}` subclass is proved/audit-complete; the full Lyons–Peres Question 6.20 remains **PARTIAL**. Haslegrave–Panagiotis, DOI `10.1002/rsa.20946`, remain prior art for the triangular/quadrangular cases and are not relabelled as new. Root `POSTED.md` now also records the corresponding owner paper *Outer Vertex-Isoperimetry of Regular Plane Tessellations* in the latest ResearchGate snapshot, so this predecessor stays excluded from duplicate research.

Preserved predecessor audits:

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

## 2. Required repository/current-source continuation

I continued from the newest own immutable report

`runs/R06/20260919T0520Z_romero_split8_six_nonexistence_58_f2a9.md`

at creation commit

`f0c9720a7b4b8beca686e4c55dadc7ad7c2485b3`.

Before new mathematics I reread/reconciled the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, the current follow-up implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the active canonical claim, the newest own report, current coordinator/task-health state and neighboring claim/admission reports. Exact repository/source searches for `2503.15453` recover only the R06 claim/report plus downstream ownership acknowledgements, not a conflicting earlier owner. The very large intake corpora cannot be rendered byte-for-byte through this connector in one call; exact source-ID/title/ownership search was used rather than pretending to have visually reread every unrelated JSONL byte.

The exact repository comparison from the preceding R06 creation commit to the then-current `master` was **99 commits ahead / 0 behind / complete (`too_large=null`)**. No deletion or release of this claim appeared; coordinator/task-health records continue to identify `ROMERO-2025-SPLIT8` as exclusively owned by R06.

Fresh dated literature checks on **2026-09-19** again recovered Pablo Romero, *Characterization of locally most split reliable graphs*, *Theoretical Computer Science* 1047 (2025), 115327, DOI `10.1016/j.tcs.2025.115327`, arXiv:`2503.15453`. The current arXiv record still says the remaining existence/nonexistence cases are an open problem, proves the local characterization by the diameter-terminal balloon split-equivalence class, and proves nonexistence only through `m <= binom(n-3,2)+3` for `n>=7`. Exact-title, arXiv-ID, `uniformly most split reliable`, author/follow-up and 2026 searches did not recover a later source settling the `n=8` layer. Current indexed later Romero work surfaced ordinary/distance-constrained two-terminal reliability, not the split-reliability question. One bibliographic index presently reports zero citations to the exact 2025 paper. These are bounded negative searches, **not** a novelty certificate.

## 3. Entering state

The claim freezes the first unresolved complete vertex layer

\[
n=8,\qquad m=14,15,\ldots,26,
\]

with metric

\[
R_{\mathrm{SPLIT8}}
:=\#\{m\in\{14,\ldots,26\}:T_{8,m}\text{ not yet exactly decided}\}.
\]

The preceding run proved exact **nonexistence** of a uniformly most split reliable graph for

\[
m=14,15,16,17,18,19
\]

by explicit competitors with strictly larger lowest split coefficient `N_6`; the integer Laplacian-minor certificate is archived in `artifacts/R06/20260919T0520Z_romero_split8_n6_checker.py/.out`. Thus this run enters with

\[
R_{\mathrm{SPLIT8}}=7,
\]

and only `m=20,...,26` unresolved.

## 4. New idea before code: replace one coefficient by the entire positive coefficient cone

The preceding low-density perturbation route stopped producing an immediate strict `N_6` gain in the dense range. Rather than search for a different isolated coefficient, I used the selected fresh moves as follows.

**#11 DUALIZE.** View the reliability comparison through its nonnegative Bernstein basis. For a fixed two-terminal graph `G` with `m` edges define

\[
N_j(G)=\#\{F\subseteq E(G): |F|=j,\ (V,F)\text{ has exactly two connected components separating }s,t\}.
\]

Then

\[
SR_G(p)=\sum_{j=0}^{m}N_j(G)p^j(1-p)^{m-j}.
\]

Therefore the coefficientwise cone condition

\[
N_j(B)\ge N_j(H)\qquad\forall j
\]

is a certificate that `SR_B(p)>=SR_H(p)` for **every** `p in [0,1]`. This replaces sampled-`p` optimization by an exact finite dominance problem.

**#5 ADD A PARAMETER.** Parameterize the dense range by the number of missing edges

\[
k=28-m\in\{2,3,4,5,6,7,8\}.
\]

This makes the seven remaining classes one finite deformation family rather than seven unrelated searches.

**#15 BREAK THE SYMMETRY.** Do not assume an extremal competitor inherits balloon symmetry. Fix the two terminals as labels `0,1` and quotient **all** missing-edge sets only by the full `S_6` action on the other six vertices. This is finer than allowing terminal interchange, so it cannot omit a two-terminal isomorphism class.

All three moves succeeded together.

## 5. Exact connected-subgraph recurrence for the full split coefficient vector

For a vertex subset `S`, let

\[
C_S(z)=\sum_{q\ge0}c_{S,q}z^q
\]

be the generating polynomial of connected spanning subgraphs of the induced graph `G[S]`. Choose one root `r in S`. Every selected-edge subgraph of `G[S]` has a unique root component `T` containing `r`; edges crossing from `T` to `S\setminus T` are absent and the graph on `S\setminus T` is arbitrary. Hence

\[
(1+z)^{e(S)}
=
\sum_{\substack{T\subseteq S\\ r\in T}}
C_T(z)(1+z)^{e(S\setminus T)},
\]

so recursively

\[
\boxed{
C_S(z)
=(1+z)^{e(S)}-
\sum_{\substack{T\subsetneq S\\r\in T}}
C_T(z)(1+z)^{e(S\setminus T)}.
}
\]

This is an exact integer recurrence over the `2^8` vertex subsets.

A split-success subgraph has a unique component `S` containing terminal `s` and not terminal `t`. Therefore its full coefficient polynomial is

\[
\boxed{
F_G(z)
=
\sum_{\substack{S\subseteq V\\s\in S,\ t\notin S}}
C_S(z)C_{V\setminus S}(z)
=
\sum_j N_j(G)z^j.
}
\]

Thus the checker computes **every** `N_j` exactly, without floating-point reliability evaluation and without iterating over all `2^m` edge subsets.

## 6. Exhaustive two-terminal orbit theorem for m=20,...,26

There are 28 possible edges on eight vertices. A graph with `m` edges is encoded by its `k=28-m` missing edges. The exact checker fixes terminals `0,1`, acts by all `6!=720` permutations of vertices `2,...,7`, and constructs complement orbits inductively: from every canonical `(k-1)`-set it adds each possible new missing edge and canonicalizes under `S_6`.

Completeness is both structural and checked numerically. Structurally, for any missing-edge `k`-set `X`, removing one edge gives a `(k-1)`-set; carrying that set to its canonical representative carries `X` to one of the generated children, which canonicalizes back to the orbit of `X`. Independently, for every canonical representative the checker computes its stabilizer among all 720 permutations and uses orbit–stabilizer. The exact orbit sizes sum to `binom(28,k)` for every `k=2,...,8`.

The complete orbit counts are

\[
13,43,137,419,1189,3021,6860
\]

for `k=2,...,8`, respectively. After filtering to connected graphs, the dense classes have:

| `m` | missing `k` | connected two-terminal `S_6` orbits | coefficient vectors tied with balloon | coefficientwise violations |
|---:|---:|---:|---:|---:|
| 20 | 8 | 6852 | 4 | **0** |
| 21 | 7 | 3018 | 2 | **0** |
| 22 | 6 | 1189 | 2 | **0** |
| 23 | 5 | 419 | 2 | **0** |
| 24 | 4 | 137 | 2 | **0** |
| 25 | 3 | 43 | 2 | **0** |
| 26 | 2 | 13 | 2 | **0** |

For each `m`, the source-recursive balloon is built exactly, a diameter terminal pair is found, and that pair is relabelled to `0,1`. For **every connected orbit representative** `H`, the exact integer coefficient vectors satisfy

\[
N_j(B_{8,m})\ge N_j(H)\qquad\forall j.
\]

Since every basis function `p^j(1-p)^{m-j}` is nonnegative on `[0,1]`, it follows immediately that

\[
SR_{B_{8,m}}(p)\ge SR_H(p)
\qquad\forall H\in T_{8,m},\quad\forall p\in[0,1].
\]

Hence:

\[
\boxed{
B_{8,m}\text{ with diameter terminals is uniformly most split reliable for every }20\le m\le26.
}
\]

This is a full finite proof, not a smaller sampled interval and not a heuristic enumeration of a neighborhood.

## 7. Exact certificate and arithmetic scope

New exact artifacts:

- `artifacts/R06/20260919T0631Z_romero_split8_full_layer_checker.c` — creation commit `2187a9257b9f64f0ea0f3b6a5d1210fa5567a1cd`;
- `artifacts/R06/20260919T0631Z_romero_split8_full_layer_checker.out` — creation commit `42ebfa9af7e4509b4f4a32538f1f5c9b1043bfa2`.

The checker was compiled with

`gcc -O3 -std=c11 -Wall -Wextra`

and ran to completion with no compiler warnings in the final archived source. Its recorded run was `elapsed=0:01.64`, `maxrss=1408KB`.

It checks, in one executable:

1. all `720` terminal-preserving internal-vertex permutations;
2. constructive completeness of missing-edge orbits through `k=8`;
3. canonicality, cardinality and orbit–stabilizer totals `sum |Orb| = binom(28,k)`;
4. graph connectivity;
5. the source-recursive balloon and a diameter terminal pair;
6. the exact connected-spanning-subgraph recurrence over all vertex subsets;
7. the exact split coefficient vector for every connected orbit representative;
8. zero coefficientwise violations in every remaining class.

All counted quantities fit far below signed 64-bit range: a connected-subgraph coefficient is at most the number of subgraphs of `K_7`, `2^21`, and a split coefficient on an eight-vertex graph with at most 26 present edges is at most `2^26`. The program also asserts nonnegativity and conservative integer bounds at each recurrence stage. No floating arithmetic is used.

Archived output ends:

`PASS: coefficientwise domination for every connected two-terminal orbit, m=20,...,26.`

This is a **self-check**, not an independent audit.

## 8. Combined n=8 classification and metric movement

Combining the preceding exact nonexistence proof for `m=14,...,19` with the new coefficientwise-uniform-optimality proof for `m=20,...,26` gives the complete first unresolved vertex layer:

\[
\boxed{
\begin{array}{ll}
14\le m\le19:&\text{no uniformly most split reliable graph exists in }T_{8,m};\\[2mm]
20\le m\le26:&\text{a diameter-terminal balloon is uniformly most split reliable in }T_{8,m}.
\end{array}}
\]

Therefore the frozen claim metric moves

\[
\boxed{R_{\mathrm{SPLIT8}}:7\to0.}
\]

This is **candidate-complete for the claimed finite n=8 layer**. It is **not yet fleet-closed** and I do not label the full source PROVED, because the closure protocol still requires two independent OTHER-task audits and the prior-art/priority check remains bounded rather than exhaustive. Current repository search finds **0/2** independent audits for `ROMERO-2025-SPLIT8`.

The unrestricted Romero/Brown–McMullin existence problem over all larger `n` remains **PARTIAL / OPEN**. Completing `n=8` does not answer all source cases.

No paper folder is created yet because the fleet closure gate is not satisfied. If both independent audits pass and current-literature review still finds no prior resolution, the next lifecycle step is the required self-contained paper folder for this finite-layer theorem; until then the correct state is `CANDIDATE_COMPLETE / AUDITS_PENDING`.

## 9. What changed conceptually

The decisive improvement was not another local perturbation. The low-density `N_6` certificate was ideal for disproving uniformity in `m=14,...,19`, but became uninformative in the dense range. The full Bernstein coefficient cone reverses the task: instead of finding one coefficient on which the balloon loses, it certifies that the balloon wins **simultaneously on every split coefficient** against the entire two-terminal graph class.

The complement parameter `k=28-m` and the terminal-preserving `S_6` action make the otherwise huge finite universe small enough for a complete exact orbit proof. This is precisely why methods #11, #5 and #15 moved the metric rather than producing another unchanged certificate.

## 10. Model / scheduler-control truth

The exposed task/control surface still has no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt and no guaranteed-duration control. The requested `GPT-6 / maximum` therefore remains prompt-only here. This report truthfully records the actual harness model as GPT-5.6 Sol and reasoning metadata as UNVERIFIED.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary in the implementation record. Repository history also records later successful P26 prompt work from another authorized context. The lawful workaround is the owning/authorized product/workspace/admin/backend context that exposes the necessary permission; there is no worker-side permission bypass, and no scheduler change was attempted here.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  model_actual: GPT-5.6-Sol
  reasoning_actual: UNVERIFIED
  predecessor:
    source_id: I0056
    source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20"
    frozen_graph: H_{5,5}
    normalization: "outer vertex boundary / |K|"
    metric_name: "certified interval width U-L"
    metric_before: 0
    metric_after: 0
    subclass_status: PROVED_AUDIT_COMPLETE_FROZEN
    full_source_status: PARTIAL
  successor:
    claim_id: ROMERO-2025-SPLIT8
    source: "Pablo Romero (2025), Characterization of locally most split reliable graphs"
    source_locator: "TCS 1047, 115327; DOI 10.1016/j.tcs.2025.115327; arXiv:2503.15453"
    claimed_scope: "all T_{8,m}, 14 <= m <= 26"
    metric_name: R_SPLIT8
    metric_before: 7
    metric_after: 0
    unchanged_count: 0
    tried_moves: [11, 5, 15]
    new_result:
      m_14_19: "NO uniformly most split reliable graph (preserved prior exact result)"
      m_20_26: "YES; diameter-terminal balloon coefficientwise dominates every connected two-terminal orbit"
      claimed_layer: CANDIDATE_COMPLETE
      full_source: PARTIAL_OPEN
    remaining_obligation: "two independent OTHER-task audits plus completed prior-art/priority review before fleet closure; unrestricted n remains outside claimed layer"
    evidence:
      prior_low_density_checker: "artifacts/R06/20260919T0520Z_romero_split8_n6_checker.py"
      prior_low_density_output: "artifacts/R06/20260919T0520Z_romero_split8_n6_checker.out"
      full_layer_checker: "artifacts/R06/20260919T0631Z_romero_split8_full_layer_checker.c"
      full_layer_checker_commit: 2187a9257b9f64f0ea0f3b6a5d1210fa5567a1cd
      full_layer_output: "artifacts/R06/20260919T0631Z_romero_split8_full_layer_checker.out"
      full_layer_output_commit: 42ebfa9af7e4509b4f4a32538f1f5c9b1043bfa2
      self_check: PASS
    audit_ids: []
    independent_audits: "0/2"
    novelty_status: "BOUNDED_SEARCH_ONLY / UNVERIFIED"
```
