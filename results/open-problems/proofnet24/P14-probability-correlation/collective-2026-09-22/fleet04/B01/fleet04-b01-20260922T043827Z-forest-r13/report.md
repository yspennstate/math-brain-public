# FOREST / fleet04 B01 — local Cocks gluing and a unit-weight 3-connected minimal-counterexample theorem

**Run:** `fleet04-b01-20260922T043827Z-forest-r13`  
**Candidate version:** `FOREST-UNIT-MINIMAL-3CONN-v2`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent team state:** the lead currently records `FOREST-KN-COCKS-RECONCILED-v3` as an internal `FULL_PROOF_CANDIDATE`; this report does not independently promote it to an established theorem.

## 1. Why this run is materially different

The preceding fleet04/B01 gluing run `FOREST-WEIGHTED-3CONN-EQUIVALENCE-v1` avoided the then-disputed fixed-graph Cocks theorem and proved only that a failure of the global unit conjecture can be compiled into a **positive-weight** 3-connected failure. The current lead has since repaired the source chronology, and two other workers have reviewed that chain.

This run therefore changes mechanism: it uses the fixed-graph Cocks implication **locally on each smaller augmented separator bridge**. That pays the virtual separator fugacity exactly and proves the stronger structural statement that an edge-minimal **unit-weight counterexample itself** must be 3-vertex-connected. No theta compilation, global weighted-equivalence theorem, contraction, or parallel-edge simplification is used.

## 2. Exact current inputs consumed

Latest complete lead: fleet01/B01, run `20260922T030948Z-b01-forest-auto11`, candidate `FOREST-KN-COCKS-RECONCILED-v3`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`. It gives the complete-graph Hermite proof and the source-reconciled Cocks/minor chain.

Assigned partner: fleet01/B02, run `20260922T032220Z-fleet01-B02-forest11`, report blob `404c46990062a1d16228a6ce4c3d28eedb1da06e`. Its direct deletion-only transfer is important here because contraction-created parallel classes are not needed.

Named OTHER-account result actually applied: fleet03/B02, `FOREST-KN-COCKS-REDUCTION-v2`, shared handoff blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`. It independently rederived the complete-graph calculation and checked the final Semple--Welsh source wording of the Cocks fixed-graph implication.

Primary-source check in this run: Semple--Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), Proposition 3.5 states that independence-correlated matroids are minor-closed. More importantly for this run, the final Section 5 Note states that Cocks proved: **if Conjecture 1.1 holds for a graph G, then M(G) is independence correlated**. Cocks's published paper is *Correlated Matroids*, CPC 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`. The Cocks full proof body was not independently available here; the exact fixed-graph statement is source-bound through the final published Semple--Welsh Note.

## 3. Notation

For a finite simple graph `G` with positive weights `y`, write

`Z_G(y)=sum_{F forest} product_{h in F} y_h`.

For distinct edges `e,f`, use the derivative Rayleigh difference

`R_G(e,f;y) = (partial_e Z_G)(partial_f Z_G) - Z_G partial_ef Z_G`.

At unit weights this is exactly

`Z_e Z_f - Z Z_ef`.

For positive weights its sign is the same as the probability-covariance form, because multiplying by `y_e y_f>0` converts derivative sums to weighted containing-edge sums.

## 4. Exact all-parameter two-cut algebra

Let `G` be 2-connected and let `{u,v}` be a genuine 2-vertex cut. For each component of `G-{u,v}`, form the corresponding non-singleton `uv`-bridge `B_i`, **excluding** an original edge `uv` if one exists. If `uv` is an edge of `G`, treat it as one additional singleton bridge.

For each bridge define

- `D_i`: weighted forest sum in `B_i` with `u,v` disconnected;
- `C_i`: weighted forest sum in `B_i` with `u,v` connected.

For the singleton original separator edge `h=uv`, `D_h=1` and `C_h=y_h`.

Because two distinct bridges connecting `u` to `v` would create a cycle, a global forest connects the terminals through at most one bridge. Conversely, local forests with at most one connecting bridge glue acyclically. Hence

`Z_G = product_i D_i + sum_i C_i product_{j!=i} D_j`.

All `D_i>0`. Every non-singleton bridge of a 2-connected graph contains a `u-v` path, so its `C_i>0`.

### 4.1 Two marked edges in the same non-singleton bridge

Let `e,f in E(B_i)`, put

`A_i = product_{j!=i} D_j`,

`lambda_i = sum_{j!=i} C_j/D_j`.

Since a genuine 2-cut supplies at least two non-singleton bridges, `lambda_i>0`.

Add one new edge `g_i=uv` to `B_i` with weight `lambda_i`; call the resulting graph `H_i`. Since the original `uv` edge, if present, was separated as its own singleton bridge, `H_i` is simple. Its forest polynomial is

`Z_Hi = C_i + (1+lambda_i)D_i`,

and the global polynomial is exactly

`Z_G = A_i Z_Hi`.

The outside quantities are independent of `e,f`, therefore

`R_G(e,f;1) = A_i^2 R_Hi(e,f; y_g=lambda_i, other weights=1)`.

Thus the same-bridge unit sign follows from **weighted** independence correlation of the smaller augmented bridge.

### 4.2 Marked edges in different bridges

Let `e in B_i`, `f in B_j`, `i!=j`, and set

`A_ij=product_{k notin {i,j}}D_k`,

`Q_i(e)=D_i partial_e C_i-C_i partial_e D_i`,

`Q_j(f)=D_j partial_f C_j-C_j partial_f D_j`.

Expanding the four derivatives of the global bridge formula gives the exact cancellation

`R_G(e,f)=A_ij^2 Q_i(e)Q_j(f)`.

Every bridge outside `i,j` cancels; there is no residual separator parameter.

For a non-singleton bridge, add a virtual edge `g_i=uv` with any positive weight `t`. Then directly

`R_{B_i+g_i}(e,g_i)=Q_i(e)`.

So weighted independence correlation of the augmented bridge implies `Q_i(e)>=0`.

For the singleton original separator edge `h=uv`,

`D_h=1`, `C_h=y_h`, `partial_h D_h=0`, `partial_h C_h=1`,

hence `Q_h(h)=1`. Therefore cross-bridge pairs involving the original separator edge are covered explicitly; no parallel virtual edge is ever created.

## 5. Local unit-to-weight closure via Cocks

The exact new closure statement is:

> **Two-cut unit closure lemma.** Suppose every non-singleton augmented bridge `H_i=B_i+g_i` satisfies the unit uniform-forest inequality for every distinct edge pair. Then the original simple graph `G` satisfies the unit inequality for every distinct pair.

Proof: by the Cocks fixed-graph theorem recorded in the final Semple--Welsh Note, unit Conjecture 1.1 on each fixed `H_i` implies that `M(H_i)` is independence correlated, i.e. all positive weights satisfy the Rayleigh inequalities. Apply this at `y_g=lambda_i` in the same-bridge formula. For different bridges, apply it to `(e,g_i)` and `(f,g_j)` to make both response factors nonnegative. The singleton `uv` response is exactly `1`. These cases exhaust all distinct marked pairs. QED.

This is stronger for the assigned purpose than the previous weighted-counterexample reduction: the only weighted objects are local smaller augmented bridges, and their all-parameter validity is paid by a published fixed-graph theorem from their unit validity.

## 6. Edge-minimal unit counterexamples are 3-connected

Assume the source conjecture is false and choose a finite simple unit-weight counterexample `G` with the minimum number of edges.

1. `G` is connected. For a disconnected graph, `Z_G` factors over components. A pair in different components has Rayleigh difference zero; a pair in one component has the component difference times the square of a positive outside factor.
2. `G` has no cut vertex. The same factorization holds over the edge-disjoint pieces attached through one cut vertex, because a cycle cannot traverse two such pieces.
3. `G` has at least four vertices. Forests with no cycle have product polynomial and zero gap, while `K_3` has `(Z,Z_e,Z_ef)=(7,3,1)` and gap `9-7=2`.
4. Suppose now that the 2-connected graph `G` has a 2-cut `{u,v}`. There are at least two non-singleton component bridges. In a 2-connected graph each component of `G-{u,v}` has neighbours to both `u` and `v`, so every non-singleton bridge contains at least two edges. For any such `B_i`, the simple augmentation `H_i=B_i+g_i` therefore satisfies

   `|E(H_i)|=|E(B_i)|+1 < |E(G)|`,

   because at least one other non-singleton bridge contributes at least two edges.

By edge-minimality, every `H_i` satisfies the **unit** conjecture. The two-cut unit closure lemma then implies that `G` satisfies the unit conjecture, contradiction.

Therefore an edge-minimal simple unit-weight counterexample is 3-vertex-connected.

This conclusion was *not* justified by the preceding fleet04 run, which only reduced a global unit failure to a weighted 3-connected failure after network compilation. The local Cocks mechanism closes that distinction.

## 7. Relation to the current lead full candidate

The campaign lead currently has a shorter global route: unit `K_n` by the exact Hermite argument, fixed-graph Cocks upgrade on each `K_n`, then deletion of nonedges. The theorem above is not needed to make that route shorter; it is an independent structural cross-check that fully discharges the assignment's separator/three-connected obligation, including the original separator-edge case and arbitrary induced virtual fugacity.

The named fleet03/B02 review is applied precisely at the only non-elementary input of the new unit-minimality theorem: the fixed-graph Cocks implication. Fleet01/B02's deletion/contraction warning is also respected: the proof uses no contraction and never collapses a parallel class.

## 8. Computation and failures

No computation is used as a proof step in this run. The separator identities are exact polynomial identities derived above. The prior exact weighted-gluing checker is preserved unchanged; it is not rerun or counted as new progress.

Source limitation preserved: the full body of Cocks's paper was not directly inspected in this run. The exact fixed-graph statement is nevertheless explicit in the final published Semple--Welsh Note and is independently recorded in the named fleet03/B02 review. Any future contradiction from the Cocks primary proof body would reopen §5 immediately.

## 9. Status

**`ESSENTIAL_STEP_APPLIED`.** The assigned all-parameter gluing/three-connected step is now closed in the stronger unit-minimal-counterexample form, conditional only on the source-explicit Cocks fixed-graph theorem that the current team candidate already uses. This report is not a third independent end-to-end review of the entire lead proof and does not make a public novelty or solved-problem claim.
