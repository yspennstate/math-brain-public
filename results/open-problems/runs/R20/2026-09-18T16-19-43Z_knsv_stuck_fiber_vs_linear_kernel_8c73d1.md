Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `N_sep > 11 -> N_sep > 11`; methods #4 PROVE SOMETHING WEAKER COMPLETELY, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS.**

# R20 — KNSV Conjecture 8.2: stuck analysis, the fiber-vs-linear-kernel obstruction

## 0. Continuity, ownership, and why this is a thinking-only run

R20 does **not** reopen the retired Paley one-localization predecessor I0100. Its historical frozen metric remains `p_max=1213`. The current exclusive R20 target remains the create-only reservation

`operations/claims/KNSV-2026-LOOPY-U.md`,

owned by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

Current source:

- Anatol Kirillov, Gleb Nenashev, Boris Shapiro, Arkady Vaintrob, *The Loopy Polynomial: from Tutte's Universal V-Function to Bizonotopal Geometry*, arXiv:2609.07728v1, Conjecture 8.2.
- Exact scope: for **simple** graphs, ordinary loopy `L`, ordinary `U`, the polychromate and the Tutte symmetric function are conjectured to have the same distinguishing power.
- Fixed R20 metric: `N_sep`, the minimum order of a rigorously certified simple pair separating `U` and `L` in either direction.
- Source baseline: Proposition 8.6 verifies the equivalence exactly through 11 vertices, so `N_sep>11`.

Fresh source/status check, 18 September 2026: I queried the exact title, exact arXiv id `2609.07728`, `Conjecture 8.2`, and simple-graph proof/counterexample variants. The current arXiv record remains v1, submitted 7 September 2026. The author-hosted current PDF still calls Conjecture 8.2 / Problem 11.1 the central problem, records exact verification through eleven vertices, and states that the simple-graph version remains open. I found no later source-matching proof or counterexample in the accessible bounded search. This is negative search evidence only, not a claim about inaccessible literature.

Current source URLs checked:

- https://arxiv.org/abs/2609.07728
- https://staff.math.su.se/shapiro/Articles/LoopyFinal.pdf

Repository continuity checked before research: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the KNSV ownership claim, the latest R20 report, and current R20 KNSV artifacts. No shared root or peer track is edited in this run.

Three consecutive directly observed KNSV reports leave the source metric unchanged:

1. `runs/R20/2026-09-18T12-59-00Z_knsv_rooted_subdivision_no_go_a4e8c2.md`;
2. `runs/R20/2026-09-18T14-13-09Z_knsv_graphical_block_rigidity_two_terminal_0c51e7.md`;
3. `runs/R20/2026-09-18T14-49-45Z_knsv_dual_local_obstruction_refined_join_no_go_7d4c2a.md`.

Each preserved `unchanged_count=UNKNOWN`, so I do **not** manufacture a numeric streak in the ledger. But the direct three-report sequence triggers Section I's stuck protocol. Accordingly this is a **thinking-only stuck run**: no new theorem-sized claim, no new finite certificate, and no checker manufactured merely to demonstrate activity.

## 1. (a) Exact blocking statement

The previous two reports reduced the first nonautomatic block profile to `(4,3)` and the hidden vector

\[
h(G)=(h_1(G),h_2(G),h_3(G)),
\]

where, for a four-set `B` and disjoint three-set `C`, the entries measure the correlation between the activity coefficients of the connected-block polynomial on `B` and the event that `C` is a triangle.

For an actual ordinary-`U` collision, a discrepancy of this hidden vector already separates the transformed `(4,3,1^{n-7})` loopy layer. The simplest unresolved fiber question at the first open order is therefore

\[
\boxed{
U_G=U_H\quad\stackrel{?}{\Longrightarrow}\quad
(h_1,h_2,h_3)(G)=(h_1,h_2,h_3)(H)
}
\tag{1.1}
\]

for connected simple graphs `G,H` on twelve vertices.

A counterexample to (1.1) would be a source-valid `U_G=U_H` but `L_G\ne L_H` counterexample to Conjecture 8.2. A proof of (1.1) would only eliminate the **first** hidden block obstruction at `n=12`; it would not by itself prove the full conjecture because higher block profiles could still separate.

This is the exact blocker for the present route: reach an **actual pairwise U-fiber**, not merely a formal linear relation among graph invariants.

## 2. (b) Routes tried and the precise reason each failed

### Route R1 — one-root gadget simulation from the ten-vertex source collision

The source's ten-vertex collision pair `I?bB@_wYO`, `I?bB@_wk_` was rooted at every vertex and compared by exact rooted ordinary-`U` transfer state. The only cross-root state matches were the two diagonal pairs `(2,2)` and `(9,9)`, and the pointed-loopy states match there as well. Exhausting every labeled simple rooted gadget on the root plus three new vertices therefore produced no separator.

**Failure mechanism:** the exact rooted state needed to make the one-sum preserve `U` already retains enough pointed loopy information on the available congruent roots. A larger gadget does not repair the absence of a promising root-state mismatch in this seed architecture.

### Route R2 — simpleification of the five-vertex loopless multigraph counterexample by subdivisions

The source's five-vertex multigraph witness has four excess parallel-edge copies beyond its six-edge simple support. Replacing those copies by internally disjoint paths and distributing seven internal vertices is the minimal path-only route to order twelve. All `20 x 20 = 400` exact cross choices were checked.

**Failure mechanism:** none of the 400 pairs even preserved ordinary `U`; the obstruction appears before the loopy comparison. Independent subdivisions do not reproduce the multiedge witness's delicate redistribution of cyclomatic mass among forest components.

### Route R3 — two-terminal extensions of the ten-vertex simple collision

The next run left the one-root category. For each seed, every choice of two old terminals and every simple graph on those terminals plus two new vertices was enumerated, giving 2,432 extensions per seed. Exact transfer arithmetic found 5,778 cross pairs with equal ordinary `U` and zero with different `L(1,x)`.

**Failure mechanism:** support on at most two old vertices is still too local. It creates many honest U-collisions, but every one lies inside an L-fiber. Any first separator in this neighborhood has to mix at least three old locations or use a qualitatively different primitive collision source.

### Route R4 — low-block rigidity and the first hidden `(4,3)` profile

Block-transform analysis shows that all profiles with parts at most three, and the previously proved family `(s,2^a,1^c)`, are automatic. The first place where ordinary block products can lose transformed information is `(4,3)`, represented by `(h1,h2,h3)`.

**Failure mechanism:** isolating missing coordinates does not show that those coordinates vary on an actual U-collision fiber. It converts the global conjecture into a smaller target but does not populate that target with a pair.

### Route R5 — dual linear obstruction

The previous report gave an exact signed relation among twelve seven-vertex graph types with weighted ordinary-`U` sum zero but weighted `h1` sum nonzero.

**Failure mechanism:** this proves only that `h1` is not a universal **linear functional** of the ordinary-U coefficient vector. It does **not** imply that two individual graphs share the same U-value and have different `h1`. This distinction is now the central conceptual obstruction; Section 3 spells it out.

### Route R6 — join/complement lifting of known collisions

The previous report showed that equality of the refined/extended invariant survives a fixed join. Since every simple ordinary-U collision through eleven vertices is already an extended-U collision by Proposition 8.6, joining a fixed graph to any known <=11 seed cannot create a U/L separator.

**Failure mechanism:** the operation preserves too much. It transports known collisions but cannot turn a refined collision into an ordinary-only collision.

## 3. (c) What a proof or counterexample must contain that no tried route contains

Let `Phi(G)` denote the full ordinary-U coefficient vector and let `h1(G)` denote the first hidden `(4,3)` statistic. The exact dual certificate from the previous run has the form

\[
\sum_i a_i\,\Phi(G_i)=0,
\qquad
\sum_i a_i\,h_1(G_i)\ne0.
\tag{3.1}
\]

Therefore no linear functional `ell` on the ambient coefficient space satisfies `h1(G)=ell(Phi(G))` for every seven-vertex graph.

But (3.1) does **not** supply

\[
\Phi(G)=\Phi(H),\qquad h_1(G)\ne h_1(H).
\tag{3.2}
\]

A nonlinear function on the finite realized image `Phi(Graphs)` can exist even when no ambient linear functional represents it. Put differently: the signed kernel of the linearized graph-measure map can be strictly larger than the difference set of two points in a single U-fiber.

This is why the last route stalled. A successful argument now needs one of two ingredients not present so far:

1. **fiber access:** a construction or source-scale computation producing a genuinely primitive simple U-collision, preferably at `n=12`, on which `(h1,h2,h3)` can be tested; or
2. **graphical nonlinear rigidity:** a theorem using simplicity/positivity/realizability of connected-block polynomials to show that the hidden transformed data are constant on every actual U-fiber even though they are not ambient-linear functions of U.

The paper itself identifies exactly this type of gap in Problem 9.5: arbitrary polynomial-valued block data need not survive the transform, so any proof must use the fact that the block polynomials come from **simple graphs**. The current routes have exploited symmetry, transfer states and linear identities, but not yet a nonlinear characterization of the realizable block-polynomial cone.

## 4. (d) Simplest special case still unproved

The smallest source-relevant special case is:

> Among connected simple graphs on exactly twelve vertices, does there exist an exact ordinary-U collision `G,H` for which the `(4,3,1^5)` hidden vector `(h1,h2,h3)` differs?

This is weaker than Conjecture 8.2 in both directions: it fixes the first possible order and only tests the first nonautomatic block profile. It is nevertheless decisive if the answer is YES, because such a pair is already a source-valid counterexample.

The two-terminal experiment does not settle this case: it covers only extensions of one ten-vertex seed whose two new vertices collectively meet at most two old vertices. The source's complete `n<=11` census likewise says nothing about primitive `n=12` collision classes.

## 5. (e) Nearest solved problem and the ingredient it has that the simple case lacks

The nearest solved problem is in the same source: Theorem 8.10 / Example 8.11 gives a five-vertex **loopless multigraph** pair with equal ordinary `U` but distinct `L`. Both graphs have the same six-edge simple support, a 5-cycle with one chord, but distribute edge multiplicities differently. Their loopy difference is already visible in two-component spanning forests. The source explains the mechanism: ordinary `U` remembers the **total** cyclomatic number across components, while the loopy specialization retains one activity/size index per component.

What that proof/construction has and the simple case lacks is the ability to move cyclomatic mass locally by changing **parallel-edge multiplicities without changing the vertex support**. In a simple graph there is no parallel-edge knob. Replacing a parallel copy by a path introduces vertices and changes component-size data, which is exactly why the path-only simpleification search lost U-equality.

This comparison suggests that a useful simple-graph counterexample should imitate the multigraph witness at the level of a **two-terminal transfer state**, not by literal independent subdivisions.

## 6. Section-B moves used in this thinking run

### #4 PROVE SOMETHING WEAKER, COMPLETELY

I did not attempt the full conjecture. I isolated the first finite source-relevant fiber problem, equation (1.1), as the next meaningful target. Outcome: a precise weaker problem, **not solved in this run**.

### #20 FIND WHY THE ALGORITHM FAILS

The exact failure is the distinction between a signed linear dependency (3.1) and a pairwise fiber collision (3.2). The previous dual certificate kills linear recovery but gives no mechanism for extracting two graphs from the signed relation. Outcome: the next method must operate on actual U-fibers or on the nonlinear realizable cone, not on the ambient linear span.

### #27 SWAP THE QUANTIFIERS

Instead of asking for every simple U-collision to preserve L, fix the known multigraph counterexample and ask whether there exists a **simple replacement operator** on its parallel-edge bundles that preserves the pair's ordinary-U equality while retaining the refined two-component discrepancy. The path-only replacement is one failed member of this larger operator family. Outcome: this gives a concrete porting problem with a fixed finite support rather than an unrestricted search over all 12-vertex graphs.

## 7. Exactly one stuck-protocol action chosen

**Chosen action: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

Next route, and only this route, is to port Theorem 8.10 through a two-terminal transfer formalism:

1. keep the five-vertex simple support of the source multigraph pair fixed;
2. replace each multiplicity-bearing support edge by an internally vertex-disjoint **simple two-terminal network**, allowing networks more general than paths;
3. quotient candidate networks by their exact two-terminal ordinary-U transfer state before gluing;
4. use the total budget of seven internal vertices first, because this is the minimal order `n=12` not excluded by Proposition 8.6;
5. search for a pair whose whole-graph ordinary-U transfer sums agree exactly, then test `(h1,h2,h3)` before computing full `L`.

This is genuinely different from the exhausted subdivision route: a path is only one two-terminal transfer type. The point is to reproduce the **componentwise cycle-rank redistribution** of the multigraph witness with a simple network whose internal branching/cycles create compensating transfer states.

No code is written in this stuck run. The next run should first derive the finite transfer-state equations for candidate two-terminal networks and only then build a checker if the equations expose a nontrivial feasible family.

## 8. Current source check and access limits

The current source still states Conjecture 8.2 and Problem 11.1 as open, and Proposition 8.6 still gives exact verification only through 11 vertices. The author-hosted PDF explicitly says the simple-graph version of the Merino-Noble problem remains open and that the multigraph obstruction does not settle the simple case. Its Appendix A reports an `O(3^n)` connected-block computation, finite-field fingerprints followed by exact integer recomputation of collision classes, and approximately 7.5 hours for the full `n=11` search on an M2 machine.

The source's code/data DOI is `10.5281/zenodo.21929427`. Direct Zenodo contents were not available through the web surface used in the preceding R20 source checks, so this run does not claim to have inspected the authors' raw collision database or code. No claim about `n=12` census data is made.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "KNSV arXiv:2609.07728v1, Conjecture 8.2"
  ownership: "operations/claims/KNSV-2026-LOOPY-U.md; exclusive R20"
  metric: "N_sep = minimum simple-graph U/L separator order"
  before: ">11"
  after: ">11"
  metric_movement: "none"
  status: "PARTIAL / CLAIMED / OPEN-looking / STUCK-THINKING-RUN"
  unchanged_count_before: UNKNOWN
  unchanged_count_after: UNKNOWN
  stuck_trigger_evidence:
    - "runs/R20/2026-09-18T12-59-00Z_knsv_rooted_subdivision_no_go_a4e8c2.md"
    - "runs/R20/2026-09-18T14-13-09Z_knsv_graphical_block_rigidity_two_terminal_0c51e7.md"
    - "runs/R20/2026-09-18T14-49-45Z_knsv_dual_local_obstruction_refined_join_no_go_7d4c2a.md"
  tried_moves: [4, 20, 27]
  chosen_stuck_action: "port the technique from the nearest solved problem"
  remaining_obligation: "Construct an actual simple U-collision with differing transformed block data, or prove nonlinear graphical rigidity on every actual U-fiber."
  next_route: "two-terminal simple-network transfer port of the five-vertex multigraph witness"
  evidence:
    - "operations/claims/KNSV-2026-LOOPY-U.md"
    - "runs/R20/2026-09-18T14-49-45Z_knsv_dual_local_obstruction_refined_join_no_go_7d4c2a.md"
    - "artifacts/R20/knsv_two_terminal_n12_check.out"
    - "artifacts/R20/knsv_seven_vertex_dual_check.out"
    - "https://arxiv.org/abs/2609.07728"
    - "https://staff.math.su.se/shapiro/Articles/LoopyFinal.pdf"
  audit_ids: []
```

## 10. Model / scheduler-control status

The operative repository implementation record remains unchanged: the exposed scheduler surface has prompt/title/schedule/timing/enabled controls but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed hour-long execution control. Thus `GPT-6 / maximum` cannot be enforced or attested from this worker surface; the actual report line above remains `GPT-5.6 Sol / UNVERIFIED`.

The historical P26 response `You cannot modify this task` was authorization-context-specific; the repository records a later successful P26 edit from an authorized context. The lawful remedy is an owner/admin-authorized product/backend surface or platform support, not duplication or permission bypass. No scheduler change is attempted here.

**NO I0100 REOPENING. NO KNSV CLOSURE OR REFUTATION CLAIM. NO NEW THEOREM CLAIM THIS THINKING RUN. CURRENT R20 STATUS: PARTIAL / CLAIMED / OPEN-looking.**