Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 8 -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / STUCK_RECOVERY_1`; methods #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY.**

# R20 — stuck review: the missing coordinate is exact integer height, not another mod-3 state

## 0. Continuity, ownership, and why this is a thinking-only run

I did **not** reopen the stale scheduler-title target Bandeira / Randomstrasse 2025 Conjecture 26 / intake I0100. Repository history shows that R20 already exhausted that closable track under the controlling rotation rule; its historical exact localized-Paley frontier remains frozen at `p_max=1213`, and finite prime certificates never proved the source asymptotic. R20 subsequently handed off the KNSV loopy-polynomial target after its own six-unchanged-run rotation.

The current canonical R20 claim remains

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned exclusively by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`. The source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, Conjecture 2.6:

\[
P^\ell(G)\le \Delta(G)
\]

for every nice finite simple graph. The frozen all-graphs metric is

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ is exactly certified}\},
\]

with supported value `n_all=8`.

The three preceding BMO reports after the admission run all left this fixed metric unchanged. Under Section I of the owner directive, this invocation is therefore intentionally a **thinking-only stuck run with no new theorem claim and no new checker**. After this report the supported unchanged count is `4` (admission moved the metric; then unicyclic, bicyclic, triangular-three-cycle, and this stuck review leave it at 8).

At run start I reread the campaign INDEX and RANKING, root POSTED and RESULTS, QUEUE, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the owner directive, the canonical BMO claim, the latest R20 report, and repository search results for the BMO source/ownership. The claim remains exclusive to R20; no competing source-matching fleet closure was recovered. No shared root and no other track's file is edited here.

## 1. Current source and later-literature check

Checked 18 September 2026 UTC / 19 September locally.

Primary source:

- Julien Bensmail, Clara Marcille, Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, current source page `https://dmtcs.episciences.org/16418`.
- The current paper still states Conjecture 2.6 in the general form `P^l(G)<=Delta(G)`.
- Its conclusion explicitly singles out cacti, says the authors tried modulo methods toward the optimal cactus bound `P^l(G)<=2`, believed they obtained a functional proof, but did not present it because it depended too heavily on exhaustive computer checks; they ask for a readable direct proof.

Current follow-up:

- Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167 (2026), 147--157, DOI `10.61091/ars167-10`, published online 17 June 2026, current page `https://combinatorialpress.com/ars-articles/volume-167/coloring-by-pushing-vertices/`.
- Its abstract still treats the Bensmail--Marcille--Orenga `Delta` bound as conjectural and proves it for cubic graphs and regular bipartite graphs.
- The proof of the regular-bipartite case is especially relevant below: it distinguishes some edge classes by congruence modulo `Delta`, but other edge classes by **strict numerical ranges** for the actual integer sums `sigma`. The cubic proof likewise partitions vertices into exact integer value ranges and resolves the remaining collision value structurally. Thus the nearest later solved cases do not insist that every edge be separated by one modulus.

Fresh bounded searches for the exact source title/DOI, `Conjecture 2.6`, `pushing scheme cactus`, the original authors, and the 2026 follow-up found the source, that follow-up, mirrors/indexes and unrelated graph-labelling material, but no later source-matching proof of the general conjecture and no published readable proof of the optimal cactus bound. This is dated bounded negative evidence only, not a novelty certificate.

## 2. Section-I stuck protocol

### (a) Exact blocking statement

For the cactus subproblem the target is to construct, for every nice cactus `G`, a push assignment `rho:V(G)->{0,1,2}` such that

\[
\boxed{
\forall uv\in E(G),\qquad
\sigma_\rho(u)\equiv\sigma_\rho(v)\pmod 3
\Longrightarrow
\sigma_\rho(u)-\sigma_\rho(v)\in 3\mathbb Z\setminus\{0\}.
}
\]

The current finite-state machinery only knows how to guarantee the stronger condition

\[
\sigma_\rho(u)\not\equiv\sigma_\rho(v)\pmod3
\]

on every core edge. The preceding report exhibited an explicit four-triangle cactus for which that stronger condition has an empty mod-3 interface state even though an exact integer two-push witness exists. Therefore the remaining obligation is not another missing mod-3 transition: it is a mechanism that preserves enough **integer height information inside one residue class** to certify nonzero multiples of 3.

### (b) Routes already tried, and the precise failure of each

1. **Complete exact finite counterexample search through order 8.** This moved the frozen metric from UNKNOWN to `n_all=8`, with exact witnesses for every nice simple graph through eight vertices. It is useful evidence but gives no induction and says nothing about arbitrary cacti or the full conjecture.

2. **Signless-Laplacian / hyperplane formulation.** Writing `sigma=d+Q rho` turns every bad edge into an affine hyperplane and suggests a polynomial/Combinatorial-Nullstellensatz certificate. The missing step is a source-useful noncancellation theorem for a coefficient whose variable exponents stay inside the permitted push box. No such coefficient mechanism was obtained; the formulation reorganizes the problem but has not yet closed a family.

3. **Pure modulo-3 lifting for unicyclic graphs.** This succeeds: odd cycles reduce to invertibility of the signless Laplacian modulo 3, and even cycles can be handled by a small cokernel/recoloring argument. The route stops being sufficient once several cycle blocks interact at articulation vertices, because modulo 3 forgets whether two equal residues differ by `0`, `+3`, `-3`, or a larger multiple.

4. **Block transparency for one and two cycles.** Exact leaf-cycle analysis gives a readable proof for unicyclic and bicyclic cacti, and cycles of length at least four behave much more flexibly than triangles. This does not by itself recurse through an arbitrary block tree: attaching a solved child block changes the articulation's **integer** sum and can create a new conflict on the parent side.

5. **Finite mod-3 interface algebra for triangular cacti.** The three-coordinate state `(root push, desired root residue, internal root contribution mod 3)` is compositional and completely solves all triangular cacti with at most three cycle blocks. It also identifies a genuine four-cycle obstruction to the *stronger all-edges-proper-mod-3 architecture*. The obstruction is semantic, not computational: the state projection identifies all integers with the same residue and therefore can declare an interface impossible even when an exact integer witness separates the relevant edges by `3` or `6`.

6. **More finite mod-3 states would attack the wrong failure.** The four-cycle witness from the previous report already demonstrates that the lost datum is not another local residue choice. Enlarging the `F_3` state table without restoring an integer-height coordinate can only repackage the same information loss.

### (c) What a proof must contain that no route so far contains

A viable proof now needs all four of the following features simultaneously:

- **Mixed certification:** each edge may be certified either by a residue difference or by a strict integer inequality within one residue class.
- **Block compositionality:** the certificate must survive gluing rooted cactus blocks at articulation vertices.
- **Finite description:** it cannot record every possible exact root sum one by one, because root sums are unbounded as the cactus grows.
- **A saturation/monotonicity argument:** after enough child structure is attached, the exact-sum information must simplify (for example to intervals, semilinear sets, or one-sided bounds) rather than proliferate.

The 2026 regular-bipartite proof has precisely the missing first ingredient: it mixes congruence separation with interval separation. The present R20 interface algebra has the second ingredient but not the first, third and fourth in a compatible form.

### (d) Simplest structural special case still unproved on the page

The cleanest infinite test family is:

> a central cycle `C_m` with `m>=4`, with two leaf triangles attached at two articulation vertices of that central cycle, and arbitrary tree branches suppressed by the already understood tree transparency.

This is the first natural three-cycle cactus family outside both previously proved structural regimes: it is not bicyclic, and it is not all-triangular. Small members are of course already covered by the `n_all=8` census where their order fits, but there is no written argument uniform in `m` and the attachment positions. Any proposed exact-sum interface should be tested here before being promoted to a general cactus induction.

### (e) Nearest solved problems and the ingredient they have that this route lacks

There are two particularly close precedents.

1. **Trees in the original source (Theorem 3.6).** A BFS order lets one later child repair the parent's parity without creating a second cycle constraint, and leaves are automatically safe against their unique neighbor. What a cactus lacks is the unique-parent local geometry: a cycle block couples two directions at once.

2. **Regular bipartite graphs in Rautenbach--Schwartze--Werner (2026).** Their distance-mod-3 push pattern uses congruences on two classes of edges but an honest numerical interval gap on the third. Their cubic proof similarly works with exact sets/ranges of `sigma` values and handles the exceptional common value by local structure. This is the closest published template for escaping the failed 'every edge must already be proper modulo 3' requirement.

## 3. #15 BREAK THE SYMMETRY ON PURPOSE

The symmetry to break is **residue symmetry**. The previous route treated all three residue classes uniformly and demanded that adjacent vertices occupy different classes. The four-cycle obstruction says that is too rigid.

The replacement viewpoint for the next attack is:

- first choose a small set of edges allowed to have equal `sigma mod 3`;
- orient each such dangerous edge and require a strict integer gap in the oriented direction;
- keep residue separation on every other edge.

This is exactly the sort of mixed certificate used implicitly in the 2026 regular-bipartite proof. On a cactus, the block graph is a tree, so one can hope to orient the exceptional equal-residue obligations toward the root without cyclic inequality requirements. This is a route proposal only; no theorem is claimed in this run.

## 4. #20 FIND WHY THE ALGORITHM FAILS

The current state algebra projects the actual integer root sum to one residue `s in F_3`. The four-cycle witness proves that this projection is too coarse.

A useful way to expose the missing coordinate is to write, whenever two endpoint sums have the same residue,

\[
\sigma(u)=a+3h_u,\qquad \sigma(v)=a+3h_v.
\]

The old state remembers `a` and discards `h_u-h_v`. Properness on such an edge is exactly the condition `h_u != h_v`.

A second, more compositional formulation appears if a rooted descendant subcactus `H` meets the rest of the graph only in its root `a`. Once the pushes inside `H` and `rho(a)` are fixed, two pieces of information matter to the parent:

- the **internal contribution** `c_H` added to the final integer sum at `a` by edges of `H` incident with `a`;
- the finite set `B_H` of exact integer sums attained by the neighbors of `a` that lie in `H`.

After the parent contributes an external amount `e`, the root sum is `e+c_H`, and the root-to-child edges are safe exactly when

`e+c_H notin B_H`.

For several descendant pieces sharing the same articulation, the internal contributions add while the bad neighbor-sum sets union. This is the exact information the mod-3 state was quotienting away. I am **not** promoting this observation to a new theorem or claiming that the resulting interface stays finite under cycle composition; the unresolved issue is precisely how to compress `(c_H,B_H)` uniformly as the cactus grows.

For a leaf triangle this viewpoint also explains why residue states are unnecessarily rigid. If the root push is `r` and the two new vertex pushes are distinct values `x,y in {0,1,2}`, the two triangle edges incident with the root contribute

`c = 2 + 2r + x + y`,

while an external contribution `e` creates root/leaf conflicts only at the exact equalities `e+r=x` or `e+r=y`. Thus the local obstruction is a pair of **exact forbidden values**, not an entire forbidden residue class. This calculation is only route diagnosis in this stuck report; no family result is claimed from it.

## 5. #29 ADD THE POINTS AT INFINITY

Recording arbitrary exact sets `B_H` would merely replace a 27-state table by an unbounded one. The compactification to try next is therefore not 'track all exact sums'; it is to track the eventual **shape** of attainable/root-forbidden sets.

Three candidates emerged in this run:

1. residue `mod 3` plus the minimum and maximum attainable quotient `h=(sigma-a)/3`;
2. finite unions of arithmetic intervals (semilinear sets), closed under the Minkowski sums produced by articulation gluing;
3. one-sided states `LOW`, `FINITE`, `HIGH`, where a rooted piece is certified safe once the parent root sum lies strictly below or above every child-neighbor sum.

The third is the literal 'point at infinity' version. It has a plausible structural reason to help: adding many independent child blocks increases the articulation's total contribution, while the exact sum at a fixed neighbor inside one child does not receive contributions from the other children. If this can be turned into a quantitative saturation lemma, high branching becomes easier and the genuine extremal cases reduce toward block paths. At present this is a strategy, not a proved reduction.

## 6. Exactly one Section-I recovery action chosen

**Chosen action: port the technique from the nearest solved problem.**

The next R20 research run should port the Rautenbach--Schwartze--Werner mixed congruence/range method to the simplest unresolved cactus family in Section 2(d), rather than creating another mod-3 table or an order-nine census.

Concrete next-run target:

1. root the central `C_m` between the two leaf triangles;
2. keep the successful modulo-3 assignment on edges that can be separated by residue;
3. allow one controlled chain of equal-residue edges;
4. prove those exceptional edges safe using explicit upper/lower ranges for the **integer** sums, analogous to the `sigma`-range separations in the regular-bipartite proof;
5. abstract whatever survives into a lifted rooted interface only after the direct three-cycle family is understood.

The next nonrepeating Section-B moves are **#3 PROVE SOMETHING STRONGER, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES NOT THE SUCCESSES**. Here 'stronger' should mean a rooted extension lemma with a prescribed one-sided integer gap, not the already-refuted stronger condition of modulo-3 properness on every edge.

## 7. No checker and no new mathematical status claim

This run intentionally creates **no new artifact/checker** beyond this immutable report. Section I required a thinking-only stuck run, and the research outcome is a sharper diagnosis plus a concrete port route, not a finite claim needing validation.

No new theorem, counterexample, closure, refutation, audit, or source-resolution claim is made here. All preceding self-check theorems retain exactly their prior status. The fixed all-graphs metric remains `n_all=8`.

## 8. Scheduler/model-control status

The operative repository implementation manifest still records that the exposed scheduler can modify prompt/title/schedule/timing/enabled state but has **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control**. Therefore GPT-6/maximum remains a prompt request only; this run truthfully reports GPT-5.6 Sol with reasoning `UNVERIFIED`.

The same manifest records the historical P26 update failure `You cannot modify this task`. That is an authorization boundary, not something a worker should bypass. The recorded workaround is an owner/admin-authorized product/backend context that exposes the task and, separately, would need to expose model/reasoning controls if GPT-6/maximum is to be enforced rather than requested in text. No scheduler or permission changes were attempted in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  source: "Julien Bensmail, Clara Marcille, Mano Orenga, Pushing Vertices to Make Graphs Irregular, DMTCS 27:3 (2025), Conjecture 2.6"
  canonical_claim: "operations/claims/BMO-2025-PUSHING-DELTA.md"
  source_scope: "every nice finite simple graph; P^l(G) <= Delta(G)"
  fixed_metric: "n_all = largest n such that every nice simple graph of order <= n has an exact witness with max rho <= Delta"
  metric_before: 8
  metric_after: 8
  movement: false
  unchanged_count_after: 4
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / STUCK_RECOVERY_1"
  tried_moves: [15, 20, 29]
  move_outcomes:
    15: "abandon all-edges-proper-mod-3 symmetry; allow controlled equal-residue edges with directed integer gaps"
    20: "identified exact failure: residue projection discards the quotient/height needed to distinguish nonzero multiples of 3"
    29: "proposed compactifying exact-sum interfaces by semilinear/range/one-sided states rather than enumerating all integer sums"
  section_I_action: "port the mixed congruence-plus-range technique from the 2026 cubic/regular-bipartite follow-up"
  simplest_unproved_structural_case: "central cycle C_m (m>=4) with two leaf triangles at articulation vertices"
  remaining_obligation: "construct a compositional finite exact-sum/range interface that allows sigma(u)=sigma(v) mod 3 while forcing sigma(u)!=sigma(v) over the integers, then extend from the test family to all cacti and ultimately the source conjecture"
  evidence:
    - "runs/R20/2026-09-18T22-10-49Z_bmo_three_cycle_state_and_four_cycle_obstruction_304617.md"
    - "operations/claims/BMO-2025-PUSHING-DELTA.md"
    - "DMTCS source DOI 10.46298/dmtcs.14963"
    - "Rautenbach-Schwartze-Werner, Ars Combinatoria 167 (2026), DOI 10.61091/ars167-10"
  audits: []
  new_checker: null
  new_theorem_claim: false
```

## 10. Handoff to the next invocation

Do not return to I0100, KNSV, another finite `n=9` census, or another pure `F_3` transition table. Start from the mixed integer-height obstruction above. The first concrete task is the uniform central-cycle-plus-two-triangles family, and the standard for progress is either a genuine rooted exact-range lemma or a counterexample to that proposed port route.
