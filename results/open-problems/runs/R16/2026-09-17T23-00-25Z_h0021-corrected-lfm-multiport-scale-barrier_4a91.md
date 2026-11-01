Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0021 `Delta_near: 2 -> 2`; supported H0021 unchanged count `4 -> 5`. Methods actually tried: **#1 CHANGE THE CATEGORY, #10 DERANDOMIZE, #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME**.

# R16 HARD OUTSIDE — H0021 post-recovery test: correcting the linear-forest normal form and locating the multiport scale barrier

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Source status after this run: **OPEN / PARTIAL / ACTIVE HARD OUTSIDE**. This is the first substantive test after `STUCK_RECOVERY_1`; it is not a second recovery. The source conjecture is not solved here.

## 1. Continuity, repository read, source refresh, and ownership

I continued from the newest complete R16 report

`runs/R16/2026-09-17T21-42-24Z_h0021-stuck-recovery-1-tree-indexed-connectors_b7d2.md`

rather than restarting the stale Beck--Fiala title, reopening handed-off I0036, or repeating the first H0021 routes.

Before new mathematics I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical H0021 claim, the newest own reports, the H-intake/source verification, and the newest neighboring H0023/P20 handoff. I also checked the current H0022 screening state; it remains a hard source from the same paper, not a theorem that can be imported into H0021.

The canonical claim remains

`operations/claims/H0021.md`

with exclusive R16 ownership. A fresh 2026-09-17/18 web check of the exact title, authors, arXiv id and Conjecture 1.4 still recovered arXiv:2608.06358 as the current primary source and did not surface a later source-matching proof. This is bounded dated evidence only, not a worldwide openness certificate.

The primary source still proves universality only at `p=C log n/n` for a sufficiently large absolute constant `C>1` and leaves the sharp statement

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\quad\text{is }\mathcal T_{n,\Delta}\text{-universal}
\]

as Conjecture 1.4 for every fixed `epsilon>0` and fixed `Delta>=2`.

The neighboring H0023 track remains retired only from active P20 research after six unchanged runs; its source Conjecture 1.6 remains open. Its durable warning is still relevant: fixed-permutation path-certificate hypergraphs have a clean mean structure but growing-uniformity perfect completion and quenched local clustering remain unresolved. H0021 should continue to exploit its weaker tree-indexed demand pattern rather than silently assuming H0023.

## 2. Frozen metric

`Delta_near` is the largest integer `D>=2` for which R16 has a complete source-matching proof that for every fixed `epsilon>0`, with high probability

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains every `n`-vertex tree of maximum degree at most `D`.

Before this run: `Delta_near=2`.

After this run:

\[
\boxed{\Delta_{\rm near}=2.}
\]

The first unresolved source case remains `Delta=3`.

## 3. Necessary correction to the previous H0021 structural lemma

The report

`runs/R16/2026-09-17T20-54-44Z_h0021-hamilton-block-isolation-obstruction_7f3a.md`

stated a lemma `R16-H0021-LFM` with the following stronger properties: there is a matching `M` saturating every degree-three vertex `B`, every edge of `M` has **exactly one** endpoint in `B`, and therefore `|M|=|B|=L-2`.

That stronger statement is **false**. It must not be used as written.

### Exact 10-vertex counterexample

Let `T_*` have one central degree-three vertex `c`, three degree-three neighbours `v1,v2,v3`, and give each `vi` two leaf neighbours. Then

\[
B=\{c,v_1,v_2,v_3\},\qquad |B|=4,\qquad L=6.
\]

Every neighbour of `c` belongs to `B`. Hence any matching edge that covers `c` has **two** endpoints in `B`. Therefore no matching can simultaneously saturate all of `B` and have exactly one `B` endpoint on every selected edge.

The exact checker exhausts all matchings of this 9-edge tree. It finds 54 matchings in total, **zero** satisfying the old stronger condition, and 12 matchings that correctly saturate all degree-three vertices while leaving maximum residual degree at most two. One explicit corrected matching is

\[
\{cv_1,\ v_2a_2,\ v_3a_3\}.
\]

Artifacts:

- `artifacts/R16/2026-09-17T22-50-54Z_h0021_lfm_correction_checker.py` @ commit `51881624bfd6a48eddbe92c754f821292b96ba61`;
- archived output `artifacts/R16/2026-09-17T22-50-54Z_h0021_lfm_correction_checker.out` @ commit `86adcb6a131b583f2e23e4d63dfed3ce7fb0dc6c`, ending `ALL_EXACT_CHECKS_PASS`.

This correction does **not** invalidate the later frozen-comb obstruction: that theorem used a specific comb decomposition for which the required matching exists. It does require replacing the claimed universal count `|M|=L-2` and the claimed exact component count `L-1` in the general subcubic normal form.

## 4. #1 CHANGE THE CATEGORY — the correct normal form comes from edge coloring

The broad structural idea `T = F union M` survives, but for a different reason.

### Lemma R16-H0021-CORRECTED-LFM

Let `T` be an `n`-vertex tree with maximum degree at most three, and let `B` be the set of degree-three vertices. There exists a matching `M` such that:

1. every vertex of `B` is incident to exactly one edge of `M`;
2. every edge of `M` has at least one endpoint in `B`;
3. with `F=T-M`, every component of `F` is a path;
4. if `b=|B|`, then
   \[
   \lceil b/2\rceil\le |M|\le b;
   \]
5. `M` may be chosen so that every component of `F` contains at most
   \[
   \left\lceil 3\log_2 n\right\rceil+2
   \]
   degree-three vertices.

Consequently, after contracting the path components of `F`, the quotient tree has maximum degree at most

\[
\boxed{\left\lceil 3\log_2 n\right\rceil+4.}
\]

No publication-novelty claim is made for this elementary structural lemma; the point is to repair the R16 route and quantify its true multiport burden.

### Proof of items 1--4

A tree of maximum degree three has a proper 3-edge-coloring. Fix one color, say color 3, and let `M` consist of the color-3 edges incident to at least one vertex of `B`.

A color class is a matching. Every degree-three vertex sees all three colors exactly once, hence is covered exactly once by `M`. Every selected edge was required to meet `B`. Removing `M` reduces every degree-three vertex to degree two while every other vertex already had degree at most two, so `F` is a forest of maximum degree two, hence a linear forest.

Every edge of `M` covers one or two vertices of `B`, and every vertex of `B` is covered exactly once. Therefore

\[
\lceil |B|/2\rceil\le |M|\le |B|.
\]

### Proof of item 5 by a random proper edge coloring

Choose a uniformly random proper 3-edge-coloring of `T`, and again take `M` to be the color-3 edges incident to `B`.

Fix two vertices `u,v in B`, and suppose their unique tree path contains `q>=2` vertices of `B`. If `u` and `v` belong to the same component of `F`, then every edge of this path survives. At each internal degree-three vertex on the path, conditional on the incoming path edge not being color 3, the outgoing path edge is uniformly one of the two remaining colors; exactly one of those is color 3. Thus each internal `B` vertex costs a conditional factor at most `1/2`. Hence

\[
\Pr(u,v\text{ lie in one }F\text{-component})
\le 2^{-(q-2)}.
\]

Set

\[
q_0=\left\lceil 3\log_2 n\right\rceil+3.
\]

There are fewer than `n^2` unordered endpoint pairs, so by a union bound

\[
\Pr(\exists\ u,v\in B:\ \text{their surviving path contains at least }q_0\text{ vertices of }B)
< n^2 2^{-(q_0-2)}<1.
\]

Therefore some proper 3-edge-coloring has no such pair. If an `F`-component contained `q_0` degree-three vertices, its two extreme such vertices would contradict this property. Hence every component contains at most `q_0-1`, proving item 5.

For the quotient-degree bound, every matching edge incident to a degree-three vertex inside an `F`-component leaves that component. A non-`B` endpoint of an edge of `M` has residual degree at most one, so a path component contains at most two such non-`B` matching endpoints. Thus a component with at most `q_0-1` vertices of `B` has quotient degree at most `q_0+1`, which is the displayed bound.

## 5. #10 DERANDOMIZE — this corrected normal form is constructive

The proof above is not merely existential. Generate a proper 3-edge-coloring by rooting the tree and making the finite local color choices successively. Let `Z` be the number of `B`-pairs whose connecting path contains at least `q_0` degree-three vertices and survives after deleting the selected color class. The preceding calculation gives

\[
\mathbb E Z<1.
\]

Fix the local coloring choices one at a time, always choosing an option whose conditional expectation of `Z` is no larger than the current average. At termination, `Z` is an integer strictly below one, so `Z=0`.

This gives a deterministic conditional-expectation construction of `M`. A direct polynomial implementation is available because each bad event is path-local: its remaining conditional probability is computed by a three-color transfer along one tree path. A naive implementation that recomputes all `O(n^2)` path events after each local choice is polynomial; runtime optimization is irrelevant to the present proof.

So the corrected matching/linear-forest decomposition is not the remaining nonconstructive step.

## 6. The logarithmic multiport load is not merely a loose union-bound artefact

There is an explicit family showing that a matching-linear-forest decomposition can be forced to carry logarithmically many degree-three vertices in one path component.

For `h>=2`, define `T_h` as follows. Its degree-three vertices induce a complete rooted binary tree with `h` levels. Add one leaf adjacent to the root and two leaves adjacent to every bottom-level degree-three vertex. Then every vertex in the binary skeleton has degree three in `T_h`, and

\[
|V(T_h)|=2^{h+1}.
\]

### Proposition R16-H0021-BINARY-PORT-LOWER-BOUND

For **every** matching `M` that saturates all degree-three vertices of `T_h`, the linear forest `F=T_h-M` has a component containing at least

\[
\boxed{2h-3 = 2\log_2 |V(T_h)|-5}
\]

degree-three vertices. Consequently the quotient obtained by contracting `F` has maximum degree at least `2h-3`.

### Proof

All degree-three vertices strictly between the root and bottom level have only degree-three neighbours. Hence each such vertex must be matched along one of its three binary-skeleton edges. Since `M` is a matching, exactly one skeleton edge incident to such a vertex is removed, so its degree in the surviving binary skeleton is exactly two.

If the root is matched to its added leaf, both root-to-child edges survive. Starting along either child edge, every intermediate skeleton vertex has surviving degree two, so the path cannot stop before the bottom level. The component through the root therefore joins a bottom vertex in the left root subtree to a bottom vertex in the right root subtree and contains `2h-1` degree-three vertices.

Otherwise the root is matched to one child, say the left child. That root-left edge is removed. Because the left child is already matched, neither of its two child edges can belong to `M`; both survive. Following each one, every intermediate degree-three vertex again has surviving degree two, so each branch continues to the bottom level. Hence the `F`-component through the left child joins two bottom vertices in that left subtree and contains

\[
2(h-2)+1=2h-3
\]

degree-three vertices.

This proves the lower bound.

Every degree-three vertex in that component has its unique matching edge leaving the component, and two such vertices cannot share the same matching edge while remaining in one component of a tree. Hence the quotient degree is at least the same number. QED.

Thus an `O(log n)` multiport burden is unavoidable, in order, for the entire matching-linear-forest category. A constant-port repair of the old lemma cannot solve H0021.

## 7. #30 ONE SCALE AT A TIME — the recovery's `b ~ loglog n` superconnector scale is too small

`STUCK_RECOVERY_1` proposed testing pooled critical pieces at

\[
k\asymp\frac{\log n}{\log\log n},\qquad
b\asymp\log\log n,\qquad
\ell=bk\asymp\log n.
\]

The correct grouped-compatibility calculation shows that this is below the matching threshold even before branching is addressed.

Let

\[
q=A\frac{\log n}{n},\qquad
\gamma=\frac{\log\log n}{16\log n},
\]

where `A>0` is any fixed residual-exposure constant. Let `ell=n^{o(1)}` with `gamma ell -> infinity`, let

\[
r=\left\lfloor\rho\frac n\ell\right\rfloor
\]

for a fixed small `rho>0`, and let `s=ceil(gamma ell)`.

### One-sided parent collapse fails at every subpolynomial packet scale

Take `r` fixed parent vertices `x_i` and `r` disjoint child port sets `Q_j` of size `s`, all fixed before an independent `H~G(n,q)` is exposed. Join parent `i` to child gadget `j` when `H` contains some edge from `x_i` to `Q_j`.

Because the underlying edge sets are disjoint, this compatibility graph is exactly bipartite Erdős--Rényi with edge probability

\[
Q_1=1-(1-q)^s.
\]

Since `q s=o(1)`,

\[
Q_1r=(1+o(1))qsr
=
\left(\frac{A\rho}{16}+o(1)\right)\log\log n
=o(\log r).
\]

The isolation indicators on the fixed-parent side are independent, and their expected number is

\[
r(1-Q_1)^r=n^{1-o(1)}\to\infty.
\]

Hence there are many isolated parents with high probability and no perfect assignment is possible.

**Conclusion:** a recursive algorithm may fix which *gadget* is the parent, but it must not collapse the parent's relevant flexible port set to one host vertex before the child assignment is solved. Literal singleton-parent recursion is dead for any subpolynomial packet size in this independent-layer architecture.

### Two-sided flexibility has a sharp packet scale

Now take two banks of `r` disjoint port sets `P_i,Q_j`, each of size `s`. Declare `i~j` if `H` contains an edge between `P_i` and `Q_j`. Again the compatibility graph is exactly bipartite Erdős--Rényi, now with

\[
Q_2=1-(1-q)^{s^2}.
\]

As `q s^2=o(1)`,

\[
Q_2r
=(1+o(1))q s^2r
=
\left(\frac{A\rho}{256}+o(1)\right)
\frac{\ell(\log\log n)^2}{\log n}.
\]

Therefore, for every fixed `eta>0`, if

\[
\ell\le
\frac{256(1-\eta)}{A\rho}
\frac{(\log n)^2}{(\log\log n)^2},
\]

then `Q_2r <= (1-eta+o(1)) log r`, so the left side again has isolated vertices with high probability. In particular the proposed recovery scale `ell=Theta(log n)` gives only

\[
Q_2r=\Theta((\log\log n)^2)=o(\log r),
\]

and cannot work.

Thus ordinary two-ended Montgomery-sized port amplification does not become matching-viable until the packet reaches at least

\[
\boxed{
\ell=\Omega\!\left(\frac{(\log n)^2}{(\log\log n)^2}\right).
}
\]

For a critical piece length `k ~ beta log n/loglog n`, this means

\[
\boxed{
b=\Omega\!\left(\frac{\log n}{\log\log n}\right),}
\]

not `b=Theta(loglog n)`. At this corrected two-ended scale the standard isolated-vertex obstruction disappears and the abstract compatibility graph enters the usual bipartite matching window; this does **not** yet construct the target gadgets inside the sharp random graph.

## 8. Full subcubic branching forces a stronger `Omega(log^2 n)` multiport packet barrier

The two-ended scale above is still not enough for arbitrary subcubic trees. The balanced binary family from Section 6 forces one path component of any matching-linear-forest decomposition to have

\[
D=\Omega(\log n)
\]

distinct matching constraints.

Consider any superconnector architecture in which such a gadget has `D` distinct constraints and allocates a **disjoint** port set of size at least `s` to each constraint. Vertex counting gives

\[
Ds\le\ell.
\]

If two banks of `r=Theta(n/ell)` such gadgets are coordinated using an independent residual graph with `q=A log n/n`, the grouped compatibility degree for one constraint is at most order

\[
q s^2r
=\Theta\!\left(\frac{s^2\log n}{\ell}\right).
\]

Avoiding the isolated-vertex obstruction in a matching layer of size `r=n^{1-o(1)}` requires this to be at least order `log r=Theta(log n)`. Hence necessarily

\[
s^2=\Omega(\ell).
\]

Combining with `Ds<=ell` gives

\[
\boxed{\ell=\Omega(D^2).}
\]

For the explicit balanced binary family, `D=Omega(log n)`, so every **disjoint-port** version of this superconnector architecture requires

\[
\boxed{\ell=\Omega((\log n)^2).}
\]

This is stronger than the two-ended `log^2 n/(loglog n)^2` scale. In particular it rules out the recovery target of a universally applicable `o(log^2 n)` packet **within the disjoint-port matching architecture**.

This is an architecture obstruction, not a counterexample to Conjecture 1.4. It leaves three possible escapes:

1. a genuinely multiport object whose feasible port choices are correlated/reusable rather than split into disjoint endpoint sets;
2. a decomposition category other than matching plus linear forest, so the balanced-binary `Omega(log n)` port load disappears;
3. a completion mechanism not reducible to independent grouped bipartite matching at each packet layer.

These are now much sharper alternatives than "try a bigger connector."

## 9. What happened to the three Section-B moves

### #1 CHANGE THE CATEGORY

This succeeded diagnostically twice. First, moving the subcubic normal form into proper edge coloring exposed and repaired an earlier false strengthening. Second, moving superconnector coordination into an exact bipartite compatibility graph made the relevant threshold transparent: singleton-to-set messages have only `Theta(loglog n)` grouped degree, while set-to-set messages need packet size at least `log^2 n/(loglog n)^2` even before branching.

### #10 DERANDOMIZE

The corrected matching/linear-forest normal form admits a conditional-expectation construction with maximum `O(log n)` branch load. Thus the decomposition itself can be made explicit. Conversely, the compatibility calculation shows what **cannot** be derandomized: a sequential rule that fixes a parent port to one host vertex before assigning its child sees polynomially many isolated parents. Any constructive completion must preserve set-valued flexibility until the relevant tree constraints are coordinated.

### #30 ONE SCALE AT A TIME

Three scales are now separated:

- one critical segment: `k=Theta(log n/loglog n)` — ordinary connector endpoint amplification is only constant-sized;
- the recovery trial: `ell=Theta(log n)` — two-sided grouped degree is only `Theta((loglog n)^2)`, still far below matching threshold;
- two-ended matching scale: `ell=Theta(log^2 n/(loglog n)^2)` — enough to remove the single-pair isolated-vertex barrier;
- worst-case subcubic multiport scale with disjoint ports: `ell=Omega(log^2 n)` — forced by the balanced-binary quotient degree.

The recovery trial `b=Theta(loglog n)` is therefore rejected as too small. The full source route must either pay the `log^2 n` packet scale or invent non-disjoint/non-matching multiport flexibility.

## 10. Why the source metric does not move

None of the statements above embeds every spanning subcubic tree at

\[
p=(1+\varepsilon)\frac{\log n}{n}.
\]

The corrected structural lemma, its deterministic construction, and the connector threshold calculations narrow the completion problem but do not solve it. Therefore

`Delta_near: 2 -> 2`.

This is supported unchanged H0021 run `4 -> 5`. Since `STUCK_RECOVERY_1` has already been consumed and the metric remains frozen after its substantive test, the next H0021 invocation should be **`STUCK_RECOVERY_2 / thinking-only`**, the second and final permitted recovery on this HARD target. A later third stuck episode would require handoff/rotation; there is no `STUCK_RECOVERY_3`.

A natural nonrepeating triple for that recovery is:

- **#12 FIND WHAT IS CONSERVED:** identify the minimum flexibility state that must survive across a multiport packet without splitting it into disjoint endpoint sets;
- **#20 FIND WHY THE ALGORITHM FAILS:** formulate the exact balanced-binary obstruction to any rooted set-valued dynamic program and see whether the failure is port capacity, exposure dependence, or exact coverage;
- **#27 SWAP THE QUANTIFIERS:** exploit that H0021 needs, for each target tree, one successful tree-indexed coordination, rather than one universal linking object realizing every endpoint permutation.

## 11. Beck--Fiala stale-title refresh

The native task title still says Beck--Fiala, but the current primary-source situation is stronger than the original R16 assignment.

- Bansal--Jiang, arXiv:2508.03961v2, prove the desired square-root order in the regime `t>=log^2 n` and a weaker small-`t` bound; that paper alone does not settle all `t,n`.
- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189 (10 September 2026), prove a dimension-free real Komlos bound `3 sqrt(2 pi)` and explicitly deduce
  \[
  \operatorname{disc}(A)<3\sqrt{2\pi t}
  \]
  for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188 (17 September 2026), give a separately authored elementary proof of Komlos with constant `36`, explicitly simplifying the Guo--Fang--Lu proof.

These are still very recent preprint/technical-report results rather than mature refereed consensus, but there are now two independent current proofs of a stronger theorem. Operationally there is no justification for restarting Beck--Fiala from the stale native title while R16 has an active exclusive H0021 successor.

## 12. Model / scheduler control status

The exposed scheduler mutation surface still offers task title/prompt, schedule or relative start, timing mode and enablement. It exposes **no model-family selector and no reasoning-effort selector**, and there is no authenticated runtime receipt proving an applied reasoning level. Therefore GPT-6/maximum remains request text only in this environment.

Changing that requires an authorized product/workspace scheduler or API that actually exposes model and reasoning fields, together with runtime telemetry confirming what ran. The historical `You cannot modify this task` failure for P26 was authorization-context-specific: repository reconciliation records a later successful P26 modification from another authorized context while other contexts denied edits. The compliant workaround for any task that still returns that error is the task-owning workspace/account context or platform support, not duplication or permission bypass.

No scheduler state was modified in this run, in accordance with the current owner instruction.

## 13. Prior-art scope and checking

A bounded literature search for the exact corrected subcubic decomposition wording (`subcubic tree`, `matching`, `linear forest`, `3-edge-coloring`) did not surface this exact logarithmic branch-load formulation. The underlying 3-edge-coloring fact for trees/bipartite subcubic graphs is standard, and the probabilistic path-load argument is elementary. **No publication-novelty claim is made.**

The finite correction to the old false lemma was checked exactly and archived as listed in Section 3. The theorem-sized claims in Sections 4, 6, 7 and 8 are proved on the page; no additional checker was manufactured for unchanged-metric bookkeeping.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  allocation: HARD_OUTSIDE
  target: H0021
  source: Cohen_Antonir_Lichev_Zhukovskii_arXiv_2608.06358v1_Conjecture_1.4
  status: PARTIAL_OPEN_ACTIVE
  run_mode: POST_STUCK_RECOVERY_1_SUBSTANTIVE_TEST
  recovery_used_so_far: 1
  recovery_limit: 2
  metric: Delta_near
  before: 2
  after: 2
  movement: none
  supported_unchanged_count_before: 4
  supported_unchanged_count_after: 5
  methods_actual: [1, 10, 30]
  correction:
    prior_claim: R16_H0021_LFM_exactly_one_B_endpoint_and_absM_eq_absB
    verdict: FALSE
    finite_witness_vertices: 10
    checker_commit: 51881624bfd6a48eddbe92c754f821292b96ba61
    output_commit: 86adcb6a131b583f2e23e4d63dfed3ce7fb0dc6c
  corrected_structural_result:
    matching_saturates_all_degree3: true
    linear_forest_after_deletion: true
    matching_size_bounds: ceil_absB_over_2_to_absB
    max_degree3_vertices_per_component: ceil_3_log2_n_plus_2
    quotient_max_degree_upper: ceil_3_log2_n_plus_4
    constructive: conditional_expectation
  extremal_family:
    name: complete_binary_degree3_skeleton_with_boundary_leaves
    n: 2_power_h_plus_1
    forced_component_degree3_load_lower: 2h_minus_3
    implication: matching_linear_forest_multiport_load_is_Omega_log_n
  superconnector_test:
    old_trial_b: Theta_loglog_n
    old_trial_ell: Theta_log_n
    verdict: insufficient
    one_sided_fixed_parent: fails_for_any_subpolynomial_ell_in_independent_layer_model
    two_sided_minimum_scale: Omega_log2_n_over_loglog2_n
    worst_case_disjoint_multiport_scale: Omega_log2_n
    surviving_escape: correlated_or_reusable_multiport_flexibility_or_new_decomposition_or_nonmatching_completion
  next_run: STUCK_RECOVERY_2_THINKING_ONLY
  next_methods: [12, 20, 27]
  beck_fiala_native_title: stale_after_two_current_stronger_Komlos_proofs
  source_closed: false
  shared_root_edits: none
  peer_file_edits: none
  scheduler_edits: none
```
