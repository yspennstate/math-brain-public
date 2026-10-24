Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT / STUCK_RECOVERY_1 / THINKING-ONLY:** H0021 `Delta_near: 2 -> 2`; supported H0021 unchanged count `3 -> 4`. Methods actually tried: **#6 DEFORM TO A POINT YOU CAN SOLVE, #18 SAY IT IN ANOTHER LANGUAGE, #22 READ THE FAILURES, NOT THE SUCCESSES**.

# R16 HARD OUTSIDE — H0021 STUCK_RECOVERY_1: from two-ended connectors to tree-indexed flexible embeddings

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Source status after this run: **OPEN / PARTIAL / ACTIVE HARD OUTSIDE**. This is the first of at most two allowed HARD stuck recoveries on H0021. By protocol this is a thinking-only recovery: it makes **no new theorem claim**, creates **no checker**, and chooses exactly one recovery action at the end.

## 1. Continuity, repository surfaces, ownership, and current-source check

I continued from the newest complete R16 report

`runs/R16/2026-09-17T20-54-44Z_h0021-hamilton-block-isolation-obstruction_7f3a.md`

rather than restarting the stale Beck--Fiala title, returning to handed-off I0036, or re-deriving the first three H0021 runs.

Before the recovery analysis I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, canonical `operations/claims/H0021.md`, the newest R16 reports, the neighboring H0023/P20 final handoff, and the H-intake/source verification surfaces. H0021 remains the exclusive R16 HARD claim.

Fresh web/source queries on 2026-09-17 recovered arXiv:2608.06358v1 as the current primary H0021 source and found no later source-matching proof of Conjecture 1.4 in the bounded search. The source still proves only the `C log n/n` theorem for a sufficiently large absolute `C` and leaves

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\quad\text{is }\mathcal T_{n,\Delta}\text{-universal}
\]

as Conjecture 1.4 for every fixed `epsilon>0` and fixed `Delta>=2`. This is bounded negative evidence only, not a worldwide openness certificate.

The neighboring H0023 track has now retired after six unchanged runs. Its most useful durable diagnosis is that the source's sharper all-permutation linking-system problem at depth

\[
k\asymp \frac{\log n}{\log\log n}
\]

has a clean fixed-permutation path-hypergraph formulation, but a growing-uniformity perfect-completion problem and quenched local clustering remain. H0021 should not silently inherit H0023's stronger all-permutation obligation.

## 2. Frozen metric

`Delta_near` is the largest integer `D>=2` for which R16 has a complete source-matching proof that for every fixed `epsilon>0`, with high probability

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains **every** `n`-vertex tree of maximum degree at most `D`.

Before this recovery: `Delta_near=2`.

After this recovery:

\[
\boxed{\Delta_{\rm near}=2.}
\]

No narrower theorem, reformulation, or route diagnosis is counted as movement.

## 3. The required five-part stuck diagnosis

### (a) Exact statement that blocks

The first unresolved source case is `Delta=3`. The previous R16 structural reduction writes every subcubic tree as

\[
T=F\cup M,
\]

where `F` is a spanning linear forest and `M` is a matching saturating every degree-three vertex. Let the path components of `F` be `C_1,...,C_s`. Every edge of `M` joins a marked vertex (a **port**) of one path component to a port of another path component; contracting every `C_i` gives a tree of matching constraints.

The exact blocker is no longer ordinary small-set expansion and no longer the almost-spanning phase. It is the following completion problem at the connectivity-threshold density:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
For every such tree-indexed family of path components and ports, construct disjoint spanning embeddings of the paths whose port images retain enough flexibility that all matching edges in `M` can be realized simultaneously, while using all `n` host vertices and only the single sharp-density graph `G(n,(1+epsilon)log n/n)`.
\end{minipage}
}
\]

A useful formal language is to assign to each path component `C_i`, with port set `P_i`, a family `E_i` of spanning path embeddings into a reserved host vertex set `W_i`. What is missing is a **joint spread** estimate on the port-image projections strong enough for the tree-indexed edge constraints. Schematically, for small `J subset P_i`, one would want a distribution `mu_i` on `E_i` satisfying a bound of the shape

\[
\Pr_{\phi\sim\mu_i}\bigl[\phi(u)=x_u\ \forall u\in J\bigr]
\le \left(\frac{K}{|W_i|}\right)^{|J|}
\]

with `K` controlled strongly enough to survive simultaneous Hall-type matching across the quotient tree. This display is a **target condition**, not a proved lemma.

### (b) Routes tried and precise reason each failed or stopped

1. **Counterexample / negation search on the source.** No source counterexample emerged. Uniformly subdivided cubic cores instead showed that the difficult family naturally lives at the same `n loglog n/log n` branch/leaf scale as the source's hard decomposition. This made them stress tests, not refutations.

2. **Bare-path packing from the suppressed subcubic core.** The first H0021 run obtained explicit bare-path mass unless the number of leaves lies in the hard window. The route stops exactly when a uniformly subdivided cubic core has about `n loglog n/log n` branch vertices and no bare path at the chosen critical length. Thus a bare-path-only dichotomy does not cover the first unresolved source case.

3. **Homeomorphism-type entropy reduction.** In the low-leaf window the number of subcubic homeomorphism types is only `exp(o(n))`. This would make a union bound plausible **if** one had a sufficiently strong conditional failure tail for each fixed tree on a common host-good event. No such tail was proved, and ordinary unconditional host failures are too correlated/common to support the required direct union bound.

4. **Sharp almost-spanning rollback.** Using the source's constant-degree extendability lemma, R16 proved universality down to an uncovered window of order

\[
O\!\left(\frac{n\log\log n}{\log n}\right).
\]

This is real partial progress, but it stops at the exact scale of the difficult branch structure. The missing step is a spanning absorber/completion mechanism, not another improvement to the initial expansion estimate.

5. **Large-`d` rollback / constant optimization.** Combining the source's `t`-joined certification with its large-`d` rollback reserve exposes a reserve of order at least `20n/c` inside that architecture. Hence merely optimizing constants in that exact proof template cannot reach `c=1+epsilon`.

6. **Independent constant-fraction exposure layers.** A layer with edge density `theta(1+epsilon) log n/n` and `theta(1+epsilon)<1` retains polynomially many isolated vertices, so it cannot carry the global singleton extendability required by the rollback argument. A sharp proof cannot permanently dilute the connectivity-threshold mass into several independent subcritical layers.

7. **Linear-forest-plus-matching followed by a frozen Hamilton cycle.** The structural normal form is valid, but the rigid implementation fails even on a comb that is known to be embeddable at the sharp threshold. With each tooth slot exposing only two possible attachment vertices, a backbone vertex sees only `Theta(loglog n)` effective choices in the hard regime, and whp many backbone vertices are isolated from all possible slot roots. The failure persists even if the independent chord graph is given `A log n/n` for any fixed `A`.

8. **Adjacent block swaps / local monovariant on the frozen cycle.** The same isolated-parent set is invariant under all block permutations and orientations, creating terminal local minima. Local rearrangement cannot repair the absence of edges to the entire allowed root pool.

9. **Two-ended Montgomery connectors as a literal drop-in replacement.** This is the key scale failure isolated in this recovery. Montgomery's `(l,gamma)` connectors have

\[
\gamma=\frac{\log\log n}{16\log n}
\]

in the classical construction, with endpoint sets of size about `gamma l`. At the critical subdivision length

\[
l\asymp \frac{\log n}{\log\log n},
\]

this gives

\[
\gamma l=\Theta(1),
\]

so a single critical-length segment has **no growing endpoint amplification at all**. The uniformly subdivided cubic-core stress family has precisely this segment length on every core edge. Therefore the classical two-ended connector lemma cannot simply be inserted edge-by-edge to solve H0021.

10. **Use the sibling H0023 all-permutation linking system as a black box.** That would solve a stronger problem, but H0023 itself is open and its P20 route stopped at a growing-uniformity perfect-completion problem. H0021 needs a weaker tree-indexed mechanism, not an appeal to the unresolved stronger conjecture.

### (c) What a proof must contain that no route so far contains

A successful `Delta=3` proof must contain **all three** of the following ingredients in one exposure-compatible mechanism:

1. **Critical-scale flexibility.** It must manufacture more than `O(1)` effective choices from structures whose natural segment length is only `Theta(log n/loglog n)`. Classical two-ended connectors do not do this at that scale.

2. **Tree-indexed rather than arbitrary-permutation coordination.** It must exploit the fact that the matching constraints form a tree. H0021 does not need every endpoint permutation. A proof that ignores this acyclicity is paying for H0023 unnecessarily.

3. **Exact spanning completion with one near-threshold exposure.** It must consume the final `Theta(n loglog n/log n)`-scale window without reserving a positive fraction of the graph and without relying on a subcritical independent layer for singleton expansion.

A plausible mathematical object would be a **tree-shaped superconnector** or a spread family of embeddings of a small connected cluster of several adjacent path pieces. The point of clustering would be to accumulate enough total size before asking for port flexibility. This is a proposed research object, not a theorem.

### (d) Simplest special case still unproved on this route

The simplest source-relevant class I can isolate after the three failed substantive runs is:

> subcubic trees admitting the matching-linear-forest decomposition `T=F union M` for which every path component of `F` contains at most two `M`-ports.

Contracting the path components then gives a path-shaped constraint tree, so there is no branching in the quotient coordination problem. The remaining difficulty is already nontrivial because the two ports of one component may be interior marked vertices rather than endpoints, and the path segment lengths may still be only `Theta(log n/loglog n)`.

I do **not** claim this class is new in the literature or unresolved as a fixed-tree embedding problem. The source-level question here is simultaneous sharp-density universality for the whole class. The bounded literature search did not locate a source-matching universality theorem that closes this exact class, but that negative search is not a novelty certificate.

### (e) Nearest solved problem and the ingredient it has that H0021 lacks

The nearest solved mechanism remains Montgomery's *Sharp threshold for embedding combs and other spanning trees in random graphs* (arXiv:1405.6560). Its connectors have two large endpoint sets `H+` and `H-` such that every chosen pair supports a Hamilton path through the connector. The proof then passes to grouped graphs and uses Hall matching. In the sharp comb argument it also deliberately chooses **good** path endpoints rather than accepting a frozen path geometry.

That proof has something the failed R16 Hamilton-block route lacked: **the host path geometry itself remains flexible until the matching problem is solved**.

But it also reveals the precise gap: with its classical value `gamma=loglog n/(16 log n)`, a connector of critical length `Theta(log n/loglog n)` has only constant-sized flexible endpoint sets. Montgomery can use larger connector scales in the regimes his argument treats; the uniformly subdivided cubic-core H0021 stress family offers only critical-length pieces edge-by-edge.

The other nearest comparison is the source's own linking-system framework: it creates exactly the kind of short prescribed-endpoint paths needed at this scale, but the source proves them only with a larger constant and leaves the sharp `(1+epsilon)` depth/density as Conjecture 1.6. The neighboring P20/H0023 work further shows that an all-permutation formulation pays for a difficult perfect-completion problem. H0021 should try to use the **tree constraint** to avoid that full price.

## 4. The three Section-B recovery moves and what happened

### #6 DEFORM TO A POINT YOU CAN SOLVE

I deformed the desired arbitrary multi-port completion toward Montgomery's solved two-ended connector regime. This did not close a new case, but it isolated the exact scale at which the literal deformation stops being useful:

\[
\gamma l
\asymp
\frac{\log\log n}{\log n}
\cdot
\frac{\log n}{\log\log n}
=\Theta(1).
\]

So the next route cannot be "replace every critical segment by an ordinary Montgomery connector." To recover growing flexibility one must **pool several critical pieces before applying a connector-like idea**, or invent a genuinely stronger optimal-depth connector.

### #18 SAY IT IN ANOTHER LANGUAGE

I rewrote the final spanning problem as a **tree-indexed constraint-satisfaction / spread-embedding problem**. Each linear-forest component supplies a family of path embeddings; the variables are the images of its marked ports; the constraints are the random host edges corresponding to the matching `M`. The quotient constraint graph is a tree.

This language matters because an all-permutation linking system treats the demand pattern as adversarially arbitrary, whereas H0021 only needs one acyclic demand graph per target tree. A rooted dynamic-programming or message-passing proof could in principle condition on one parent port at a time and preserve large feasible sets for child ports. No route so far has exploited this acyclicity quantitatively.

### #22 READ THE FAILURES, NOT THE SUCCESSES

Three failures line up:

- Montgomery's frozen-slot sketch explicitly notes that at `p=C log n/n`, ordinary endpoint pools leave vertices with no available neighbor, and his fix is to build connectors and choose good endpoints adaptively.
- Cohen Antonir--Lichev--Zhukovskii explain that older deterministic/AKS-style linking constructions cannot reach the conjectured `Theta(log n/loglog n)` depth just above connectivity; their new framework reaches optimal depth only up to constants.
- The neighboring H0023 path-hypergraph route finds that even after a very regular mean incidence structure, quenched clustering and exact perfect completion remain at growing path length.

Together these failures say that H0021 needs **adaptive flexibility at the critical depth without demanding arbitrary-permutation universality**. That is a narrower target than H0023 and a more realistic target than an edge-by-edge classical connector transplant.

## 5. Exactly one recovery choice

**Chosen recovery: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The technique to port is not the literal `(l,gamma)` connector lemma at one core edge. It is Montgomery's broader principle:

> delay the path geometry, manufacture many admissible attachment locations, pass to a grouped compatibility graph, and solve the remaining constraints by Hall-type matching.

For H0021 the next substantive test will port that principle to a **tree-indexed superconnector** made from a small connected packet of critical path pieces, with the explicit goal of obtaining a growing feasible port set after conditioning on the parent attachment. The quotient is a tree, so the proposed ported mechanism should be tested recursively rather than against all endpoint permutations.

This is recovery 1 of at most 2 for H0021. It does not authorize a third recovery if the hard-task limit is later reached.

## 6. Next substantive target and next Section-B moves

The next run should not optimize the almost-spanning constant and should not build a checker unless a finite claim emerges. Its concrete target is to decide whether **pooling `b=b(n)->infinity` consecutive/adjacent critical pieces before exposing the parent port** can create a recursively usable superconnector while keeping cluster size `o(log^2 n)` and preserving exact vertex coverage.

The first scale to test is

\[
b\asymp \log\log n,
\qquad
k\asymp \frac{\log n}{\log\log n},
\qquad
bk\asymp\log n,
\]

because the classical connector endpoint factor would then become of order `loglog n` rather than order one. This is a scale-selection heuristic, not a proved construction.

The next nonrepeating Section-B triple will be:

- **#1 CHANGE THE CATEGORY:** formulate the pooled object as a rooted tree-CSP / spread-measure problem rather than a path-linking system;
- **#10 DERANDOMIZE:** if a random choice of flexible embeddings appears to satisfy the tree-indexed constraints with positive probability, extract an explicit sequential selector/message rule;
- **#30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME:** freeze the critical scale `k~log n/loglog n`, first treat the path-shaped quotient special case, and identify exactly what extra branching breaks.

If the metric remains unchanged through the recovery test and later reaches another three-run stuck episode, H0021 gets at most `STUCK_RECOVERY_2`; a third stuck episode requires handoff/rotation.

## 7. Beck--Fiala stale-title refresh

The native title still names Beck--Fiala, but the current literature situation is now stronger than in the early R16 reports.

- Bansal--Jiang, arXiv:2508.03961v2, prove the square-root order for `t>=log^2 n` and a weaker small-`t` bound; that paper alone does not settle all `t,n`.
- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1 (submitted 10 September 2026), claim the full real Komlos theorem with constant `3 sqrt(2 pi)`, and explicitly deduce

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no restriction on `n`.
- On 17 September 2026, Karingula--Lovett, ECCC TR26-188, posted an independent elementary proof of the Komlos conjecture, explicitly described as simplifying the Guo--Fang--Lu proof, with constant `36`.

Thus Beck--Fiala is no longer merely supported by one very recent preprint claim: there is now a second, independently authored proof of the stronger Komlos conjecture in another current preprint venue. Neither is being relabelled here as refereed publication, but operationally this is stronger reason not to restart Beck--Fiala research from the stale scheduler title.

## 8. Model / scheduler control status

The exposed automation control surface still has no model-family selector and no reasoning-effort selector. GPT-6/maximum can therefore be requested in prompt text only; actual execution must be reported from available runtime metadata or as UNVERIFIED. This run actually identifies as GPT-5.6 Sol with reasoning telemetry UNVERIFIED.

The historical `You cannot modify this task` failure is authorization-context-specific. Repository reconciliation records successful P26 modification from another authorized context while other contexts denied edits. The compliant workaround is to use the owning workspace/account context or platform support. Do not duplicate the task and do not bypass permissions.

No scheduler state, shared root ledger, peer file, email, Drive content, public post, purchase, permission, or workflow was changed in this run.

## 9. Artifacts / checking

This is the mandated thinking-only stuck recovery. It makes no new finite claim, so no exact checker or artifact was appropriate. The research value of the run is the route diagnosis and the selected recovery, not a certificate manufactured for an unchanged metric.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  allocation: HARD_OUTSIDE
  target: H0021
  source: Cohen_Antonir_Lichev_Zhukovskii_arXiv_2608.06358v1_Conjecture_1.4
  status: PARTIAL_OPEN_ACTIVE
  run_mode: STUCK_RECOVERY_1_THINKING_ONLY
  recovery_number: 1
  recovery_limit: 2
  metric: Delta_near
  before: 2
  after: 2
  movement: none
  supported_unchanged_count_before: 3
  supported_unchanged_count_after: 4
  methods_actual: [6, 18, 22]
  recovery_choice: port_nearest_solved_technique
  recovery_technique: Montgomery_connector_grouped_Hall_principle
  exact_blocker: tree_indexed_multiport_spanning_completion_at_sharp_density
  simplest_special_case: path_shaped_quotient_of_matching_linear_forest
  key_scale_obstruction: classical_connector_gamma_times_critical_length_is_Theta_1
  next_methods: [1, 10, 30]
  next_target: pooled_tree_indexed_superconnector_at_b_Theta_loglogn_k_Theta_logn_over_loglogn
  beck_fiala_native_title: stale_resolved_by_stronger_current_preprint_results
  checker: none_thinking_only
  shared_root_edits: none
  peer_file_edits: none
```
