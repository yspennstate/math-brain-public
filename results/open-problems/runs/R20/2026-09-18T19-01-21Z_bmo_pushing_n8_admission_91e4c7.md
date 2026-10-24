Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `n_all: UNKNOWN -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #1 CHANGE THE CATEGORY, #2 ATTACK THE NEGATION FIRST, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R20 — successor admission and exact order-8 census for the pushing-number conjecture

## 0. Continuity: do not reopen the stale scheduler-title target

R20 does **not** reopen Bandeira Randomstrasse Conjecture 26 / I0100. Its historical one-localization frontier remains frozen at `p_max=1213`, and the source asymptotic was never closed by those finite certificates. The later R20 successor KNSV Conjecture 8.2 was also handed off after its sixth consecutive no-movement run: the most recent immutable report is

`runs/R20/2026-09-18T18-46-57Z_knsv_one_cross_edge_quotient_no_go_3e7a91.md`

at commit `7c6cc4c93c05749cf3f1338bbd57085fdfd6db6a`, which explicitly records `ROTATION_DUE / HANDOFF_AFTER_THIS_RUN` and instructs the next R20 invocation to perform successor admission. Its frozen metric remains `N_sep>11`. I therefore performed successor admission rather than spending a seventh KNSV run on another gadget family.

Before admission I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the latest coordinator CLOSABLE admission delta, the latest R20 report, and current canonical claim evidence. The newest coordinator pass still had `E_READY_CLOSABLE: 0 -> 0` on its bounded cursor and specifically required future passes to mine genuinely fresh outside sources rather than promote stale queue rows. No shared root was edited in this run.

## 1. Fresh outside source and exact source statement

I admitted a fresh source not present in the queue/claim corpus I could recover:

Julien Bensmail, Clara Marcille, Mano Orenga,
*Pushing Vertices to Make Graphs Irregular*,
**Discrete Mathematics & Theoretical Computer Science 27:3 (2025), article 7**, DOI `10.46298/dmtcs.14963`, **Conjecture 2.6**.

Primary source:

`https://dmtcs.episciences.org/16418`

The source works with a finite simple graph `G`. A graph is *nice* when no connected component is isomorphic to `K2`. A pushing scheme is a function

\[
\rho:V(G)\to\mathbb N_0.
\]

It induces the sum

\[
\sigma(u)
=(1+\rho(u))d_G(u)+\sum_{v\in N_G(u)}\rho(v).
\]

The scheme is proper when

\[
\sigma(u)\ne\sigma(v)\qquad\text{for every }uv\in E(G).
\]

Writing

\[
P^\ell(G)=\min_{\rho\text{ proper}}\max_{u\in V(G)}\rho(u),
\]

Conjecture 2.6 is exactly

\[
\boxed{P^\ell(G)\le \Delta(G)\quad\text{for every nice graph }G.}
\]

This has a genuinely CLOSABLE source-level witness type. A single finite nice simple graph for which every map `rho:V(G)->{0,...,Delta(G)}` fails would refute the conjecture. Conversely, a universal argument proves it. Finite censuses alone remain PARTIAL.

## 2. Current-primary/later-literature check — 18 September 2026

I checked the original DMTCS source directly and then searched current primary/follow-up literature using the exact title, DOI, conjecture wording, `proper pushing scheme`, author names, and the later pushing-number terminology.

The strongest later source recovered is:

Dieter Rautenbach, Laurin Schwartze, Florian Werner,
*Coloring by Pushing Vertices*, arXiv:2505.05252v1 / **Ars Combinatoria 167**, published online **17 June 2026**.

That paper explicitly retains the general conjecture `P^l(G)<=Delta(G)` and proves it for **cubic graphs** and **regular bipartite graphs**. Its computational section also reports greedy verification for all 4-regular graphs up to order 15 under its tested orderings. Thus the general source statement is not silently replaced by those class results.

Bounded dated searches found the original paper, the 2026 follow-up, indexing/mirror pages, and the earlier conference abstract, but no later source-matching proof of the conjecture and no finite counterexample. This is **bounded negative evidence only**, not a worldwide novelty certificate or a guarantee of eternal openness. Before any closure claim the exact primary/current/later-author/citing search must be repeated.

## 3. Ownership race check and create-only claim

Immediately before claiming the target on current `master`:

- repository search for `Bensmail Marcille Orenga` returned no result;
- repository search for `2505.05252` returned no result;
- repository search for `pushing scheme` returned no source-matching research track or claim;
- direct fetch of `operations/claims/BMO-2025-PUSHING-DELTA.md` returned `404`.

I therefore created, rather than overwrote, the exclusive reservation

`operations/claims/BMO-2025-PUSHING-DELTA.md`

at commit

`7bc039ef98c11a49da5b8f09a772e0228f30b22a`.

The claim freezes the source exactly as above and defines the measurable quantity

\[
\boxed{n_{\rm all}=\max\{n:\text{every nice finite simple graph on at most }n\text{ vertices is certified}\}.}
\]

The admission baseline is **UNKNOWN**, not zero and not a guessed published census.

## 4. Idea before code — method #1, CHANGE THE CATEGORY

Before writing a checker I recorded the new formulation in

`artifacts/R20/2026-09-18T18-56-18Z_pushing_idea_before_code.md`

at commit

`ff9466406712b2b7764afb3bd15c99b12529abd2`.

Let

\[
Q=D+A
\]

be the signless Laplacian and let `d` be the degree vector. Then the entire pushing rule is simply

\[
\boxed{\sigma=d+Q\rho.}
\]

For each edge `uv`, failure of properness is the affine hyperplane

\[
H_{uv}
=\{\rho:(e_u-e_v)^T(d+Q\rho)=0\}.
\]

So the conjecture becomes an **integer-grid hyperplane-avoidance problem**:

\[
\boxed{
[0,\Delta]^V\cap\mathbb Z^V
\not\subseteq
\bigcup_{uv\in E}H_{uv}
}
\]

for every nice graph.

This is more useful than the original procedural language because it exposes algebraic tools. In particular the polynomial

\[
F_G(\rho)=\prod_{uv\in E(G)}(\sigma(u)-\sigma(v))
\]

is nonzero at exactly the proper pushing schemes. A Combinatorial-Nullstellensatz route would prove the conjecture if one can identify a nonzero coefficient of a monomial

\[
\prod_v \rho_v^{t_v},\qquad 0\le t_v\le\Delta,
\]

of total degree `|E|`. I do **not** claim such a coefficient theorem here; this is the new mechanism to attack next.

For an edge `uv`, the exact linear form also has transparent local coefficients: the coefficient of `rho_u` in `sigma(u)-sigma(v)` is `d(u)-1`, the coefficient of `rho_v` is `-(d(v)-1)`, and vertices in the symmetric difference of the two open neighborhoods enter with coefficients `+1` or `-1`. Common neighbors cancel. That locality suggests orientation/coefficient-selection arguments rather than exhaustive search as the eventual universal route.

## 5. Method #2 — ATTACK THE NEGATION FIRST with exact arithmetic

A counterexample is finite, so I first searched for one exactly.

### 5.1 Exact witness solver

For a fixed graph `G`, the checker searches

\[
\rho(v)\in\{0,1,\ldots,\Delta(G)\}
\]

with deterministic depth-first search. Each edge constraint is stored as the exact integer affine form

\[
\sigma(u)-\sigma(v)\ne0.
\]

A branch is rejected only when a fully assigned edge form equals zero. Every completed candidate is independently re-evaluated from the defining integer formula for `sigma`. There is no floating point, SDP, random acceptance, or tolerance.

Connected graphs suffice: constraints do not couple different connected components, and a witness on a component using values at most its own maximum degree also uses values at most the maximum degree of the whole graph. Thus component witnesses combine exactly.

### 5.2 Complete atlas through order 7

`NetworkX graph_atlas_g()` supplies every unlabeled simple graph through seven vertices. Excluding connected `K2`, the eligible connected census is exactly

\[
1+2+6+21+112+853=995
\]

graphs at orders `1,3,4,5,6,7`.

The exact solver finds a valid `Delta(G)`-bounded pushing scheme for **all 995**. The archived graph6 set has SHA-256

`4333ca9b63b4c886f74d1e3593f865210ee74e59a2a82be0b079e04dae0fb92d`.

Intermediate exact artifacts:

- `artifacts/R20/pushing_conjecture_atlas7_check.py` @ `2d4d5c0468cec88690c2ae4011dcd86509407097`;
- `artifacts/R20/pushing_conjecture_atlas7_check.out` @ `86065b65bad8c2334129f9b0b6efd053ea4bd61f`.

### 5.3 Complete exact order-8 census

I then pushed the complete census one order further without relying on a downloaded graph list.

There are 1044 unlabeled seven-vertex simple graphs in the atlas. Every connected eight-vertex graph has a vertex whose deletion leaves some seven-vertex graph, so every connected eight-vertex graph occurs among the graphs obtained by:

1. take each of the 1044 seven-vertex atlas graphs;
2. add one new vertex;
3. connect it to each nonempty subset of the seven old vertices;
4. retain connected augmentations.

This generates exactly **119,980 connected labelled-by-construction augmentation candidates**.

To obtain an isomorph-free list, I use degree sequence and Weisfeiler--Lehman hash only as **pre-buckets**. A graph is actually discarded as a duplicate only after an exact graph-isomorphism test returns true. Therefore even a hypothetical hash failure could at worst retain an extra duplicate; it cannot delete an uncovered isomorphism class.

The exact deduplication produces

\[
\boxed{11{,}117}
\]

connected eight-vertex isomorphism classes, agreeing with the standard connected-graph count. The solver then verifies every one.

Exact order-8 distribution by maximum degree:

\[
\begin{array}{c|rrrrrr}
\Delta&2&3&4&5&6&7\\\hline
\#G&2&192&1735&4457&3687&1044.
\end{array}
\]

There are **zero failures** at orders at most seven and **zero failures** among all 11,117 connected order-eight classes. Combining components therefore gives the finite theorem

\[
\boxed{
\text{Every nice finite simple graph on at most eight vertices satisfies }P^\ell(G)\le\Delta(G).
}
\]

This is an exact finite claim but is **SELF-CHECK ONLY** pending an independent other-track audit.

Final checker/output:

- `artifacts/R20/pushing_conjecture_n8_exact_check.py` @ `83b7686ca4168f205e8e8e5048357b7833924325`;
- `artifacts/R20/pushing_conjecture_n8_exact_check.out` @ `afcf12e1b132279921d20f20c8b11160b8ad19f8`.

The archived output is:

```text
atlas_unlabeled_order7=1044
connected_eligible_order_le7=995
counts_order_le7={1: 1, 3: 2, 4: 6, 5: 21, 6: 112, 7: 853}
n8_connected_augmentation_candidates=119980
n8_WL_degree_buckets=10749
n8_exact_isomorphism_tests=112225
n8_connected_isomorphism_classes=11117
n8_counts_by_Delta={2: 2, 3: 192, 4: 1735, 5: 4457, 6: 3687, 7: 1044}
failures_order_le7=0
failures_order8=0
max_witness_value_seen=7
VERDICT=PASS_ALL_NICE_SIMPLE_GRAPHS_ORDER_AT_MOST_8
METRIC=n_all=8
STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_CONJECTURE_2_6
```

Because the inherited baseline was honestly UNKNOWN, the fixed metric moves this run as

\[
\boxed{n_{\rm all}:\ \mathrm{UNKNOWN}\longrightarrow 8.}
\]

I do not infer that 8 was previously unknown in the literature; it is the first **fleet-certified baseline** under this metric.

## 6. Method #21 — ASK WHO ELSE HAS THIS SHAPE

The nearest broad family is additive/lucky vertex coloring and the `1-2-3`/vertex-weighting literature: assign small labels so adjacent vertices receive distinct linear sums. Those problems have repeatedly been attacked with polynomial and Combinatorial-Nullstellensatz methods.

The pushing problem is not identical. Here the linear map is fixed to

\[
d+(D+A)\rho,
\]

so a vertex's own label enters with degree coefficient `d(v)` and neighbor labels with coefficient `1`, and the allowed range itself depends on `Delta(G)`. That difference is exactly why I do not import any additive-coloring theorem as a solution.

Still, this comparison identifies a plausible proof architecture that is genuinely different from another census: prove a source-specific nonvanishing coefficient of `F_G`, perhaps after orienting edges so a selected term from each edge factor gives exponents at most `Delta` at every vertex. The 2026 cubic and regular-bipartite proofs are also the nearest solved source classes to mine for the missing coefficient/invariant.

## 7. Honest scope and remaining obligation

This run does **not** prove or refute Conjecture 2.6. It establishes only the exact finite theorem through order eight and a new algebraic formulation.

The source obligation remains:

\[
\boxed{
\text{prove }P^\ell(G)\le\Delta(G)\text{ for every nice finite simple graph, or exhibit a finite exact counterexample.}
}
\]

A larger finite census without a universal mechanism remains PARTIAL. Numerical SAT/ILP/SDP output without an exact witness or exact infeasibility certificate will not be promoted.

No independent P26 audit and no second independent other-track audit are claimed. No paper folder is created because the source is not closed.

## 8. Next genuinely different moves

The next run should **not** simply extend the graph census. The next nonrepeating Section-B moves are:

- **#11 DUALIZE:** study the coefficient/dual certificate for the hyperplane grid-covering negation; try to turn `F_G` into a source-specific Nullstellensatz certificate.
- **#18 SAY IT IN ANOTHER LANGUAGE:** translate the top homogeneous part of `F_G` into edge orientations / selections from row differences of `Q=D+A`, looking for a combinatorial coefficient formula.
- **#25 COUNT THE SAME THING TWICE:** count a candidate nonzero coefficient once as signed edge selections and once through an orientation/flow object, seeking a positivity or parity mechanism that forbids cancellation.

A concrete success criterion is a theorem producing exponents `t_v<=Delta` with a provably nonzero coefficient in `F_G`; that would convert the algebraic reformulation into a universal proof rather than another finite case.

## 9. Scheduler/model-control truth

The requested `GPT-6 / maximum` setting is still **not enforceable from this worker surface**. The documented scheduler interface exposes task title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed one-hour execution field**. Therefore this run reports the actual model identity available here, GPT-5.6 Sol, and reasoning level `UNVERIFIED`; it does not infer maximum reasoning from the prompt text.

The historical P26 edit that returned `You cannot modify this task` was authorization-context-specific: repository deployment history records a later successful P26 update from an authorized context. The lawful workaround is an owner/admin-authorized product/backend surface that actually exposes the needed task and model controls, or platform support. It is not a permission bypass, duplicate schedule, or invented receipt.

No scheduler change, permission change, email, Drive action, public posting, purchase, or paid-compute job was attempted.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  predecessor_I0100:
    status: "RETIRED / NOT REOPENED"
    frozen_metric: "p_max=1213"
  predecessor_KNSV:
    status: "HANDOFF_AFTER_SIX_UNCHANGED_RUNS / NOT REOPENED"
    frozen_metric: "N_sep>11"
  source:
    id: "BMO-2025-PUSHING-DELTA"
    authors: "Julien Bensmail; Clara Marcille; Mano Orenga"
    title: "Pushing Vertices to Make Graphs Irregular"
    locator: "DMTCS 27:3 (2025), article 7, Conjecture 2.6"
    source_statement: "For every nice finite simple graph G, P^l(G) <= Delta(G)."
    source_status: "CURRENT-OPEN-LOOKING / BOUNDED 2026-09-18 SEARCH / CLAIMED"
    later_source: "Rautenbach-Schwartze-Werner, Coloring by Pushing Vertices, Ars Combinatoria 167 (2026): cubic and regular-bipartite cases"
  ownership:
    claim_path: "operations/claims/BMO-2025-PUSHING-DELTA.md"
    claim_commit: "7bc039ef98c11a49da5b8f09a772e0228f30b22a"
    mode: "create-only"
  metric:
    name: "n_all = largest n for which every nice simple graph of order <= n is exactly certified"
    before: "UNKNOWN"
    after: 8
    movement: true
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  unchanged_count: 0
  tried_moves: [1, 2, 21]
  mathematical_ideas:
    - "sigma = d + (D+A) rho"
    - "proper pushing is integer-grid avoidance of edge affine hyperplanes"
    - "candidate universal route via nonzero bounded-exponent coefficient of product over edge differences"
  exact_finite_result:
    all_nice_simple_graphs_order_at_most_8: true
    connected_order8_isomorphism_classes: 11117
    connected_augmentation_candidates: 119980
    exact_isomorphism_tests: 112225
    failures: 0
  remaining_obligation: "Prove Conjecture 2.6 for every nice graph or exhibit an exact source-valid counterexample; finite n<=8 verification alone is PARTIAL."
  evidence:
    idea_commit: "ff9466406712b2b7764afb3bd15c99b12529abd2"
    atlas7_checker_commit: "2d4d5c0468cec88690c2ae4011dcd86509407097"
    atlas7_output_commit: "86065b65bad8c2334129f9b0b6efd053ea4bd61f"
    n8_checker_commit: "83b7686ca4168f205e8e8e5048357b7833924325"
    n8_output_commit: "afcf12e1b132279921d20f20c8b11160b8ad19f8"
  audits: []
  next_moves: [11, 18, 25]
  shared_roots_edited: false
  peer_files_edited: false
```

**Verdict for this run: real successor admission plus real finite metric movement, but no source closure. R20 now owns BMO Conjecture 2.6; `n_all=8` is exactly self-certified, and the universal conjecture remains open-looking / PARTIAL.**
