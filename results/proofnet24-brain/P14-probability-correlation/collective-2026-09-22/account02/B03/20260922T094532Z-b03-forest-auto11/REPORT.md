# B03 FOREST research report — local STAR-2 unitizer lower bound and exact single-doubling criterion

**Run:** `20260922T094532Z-b03-forest-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target status:** FOREST remains `OPEN`; no full-proof claim.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## Controls and sources

Fresh entry controls were resolved at main `049dcedb88d73825394b0f0bb99f10d3761555a9`. Before external writes main was re-resolved at `3e39467dd208c10f30603e5113e80310f0995ad6`; OWNER CONTROL remained `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, and no later applicable stop/pause was present. Current README Git blob: `3d4a9372c87802ab734141a3374d04c8823372e3`. Native-byte SHA-256 of the whole README/OWNER MESSAGE was not separately exposed by the connector, so no stale SHA-256 was reused.

Latest complete campaign-lead version actually read: account01/B01 blob `4cee205cb7d254caf785692838111988a0b8a155`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, canonical report revision `79044b575c4b689248892f37b9930e983dddabca`. Its first missing comparison is the source-generated `{1,2}` STAR-2 contraction created when a triangle edge is conditioned present.

Named OTHER-account result actually consumed and applied: account03/B01 handoff blob `3c14c9b8968ec37d1a2df3506dac3d294a395e65`, source-bound commit `5e01cba072fe4bc74cf421eab22967d3fac8c6fa`, result `EXACT_STAR2_UNITIZATION_AND_SCOPE_CORRECTION`. It proves that the simple two-terminal gadget consisting of a direct terminal edge plus three internally-disjoint length-2 paths has `(D,C)=(27,54)` and response `C/D=2`, and that replacing `d` STAR-2 edges gives `Delta_unit=27^(2d) Delta_STAR2`. The peer correctly leaves **size-controlled** STAR-2 as the missing minimality-compatible step.

## Conditional end-to-end route and first debt

The current direct route can be stated compactly.

1. Assume an edge-minimal simple unit counterexample `G` with violating marked pair `(e,f)`.
2. The lead's rank/Simpson argument controls every third edge `g` that lies in no triangle because both conditional minors remain smaller simple graphs.
3. If `g=uv` lies in a triangle, conditioning `g=1` and contracting it produces a smaller simple quotient with fugacity `2` exactly on the star edges corresponding to common neighbors of `u,v`.
4. A minimality-compatible theorem proving the Rayleigh gap nonnegative for those **source-generated** STAR-2 quotients would close the triangle branch and hence the lead's direct minimal-counterexample mechanism.

The first debt is therefore not universal weighted Rayleigh closure. It is a size-controlled/direct comparison for the source-generated STAR-2 quotient.

## 1. Exact lower bound: the peer response-2 gadget is locally size-optimal

For a finite simple unit two-terminal network `N` with terminals `s,t`, let

- `D_N` = number of forests in which `s,t` are disconnected;
- `C_N` = number of forests in which `s,t` are connected;
- `r_N=C_N/D_N`.

A local exact replacement for one fugacity-2 edge must have `r_N=2`, because two-terminal substitution multiplies all four marked counts by the same factor `D_N` while replacing the edge weight by `C_N/D_N`.

### Theorem 1

Every finite simple unit two-terminal network with response `r_N=2` has at least **7 edges** and at least **5 vertices**. Both minima are attained simultaneously. With fixed terminals on five labelled vertices, the unique response-2 graph is

`01,02,03,04,12,13,14`,

i.e. a direct terminal edge `01` plus three internally-disjoint length-2 paths. It has `(D,C)=(27,54)`.

### Exact finite proof

The attached checker enumerates every simple graph with fixed terminals on `n=2,3,4,5` vertices. The numbers with `C=2D` are exactly

`0,0,0,1`.

For the edge lower bound, suppose a response-2 graph had at most six edges. Delete every component not containing the terminals; this multiplies `D,C` by the same positive factor and leaves the response unchanged. The remaining terminal component is connected and therefore has at most `m+1<=7` vertices. Relabel it into seven vertices and add isolates. Hence it appears among the labelled subgraphs of `K_7` with at most six edges. The checker exhausts all

`sum_{j=0}^6 binom(21,j) = 82,160`

such graphs and finds no instance with `C=2D`.

Thus account03/B01's seven-edge gadget is not merely a convenient construction: **no smaller local two-terminal unitizer exists in edge count**, and no response-2 simple network exists on fewer than five vertices.

## 2. Consequence: independent local unitization cannot close edge-minimality

Let the parent simple graph `G` have `m` edges, let `g=uv` be the contracted triangle edge, and let `d>=1` be the number of common neighbors of `u,v`. After contracting `g` and collapsing each parallel pair to one representative fugacity-2 edge, the simple quotient `J` has

`|E(J)| = m - 1 - d`.

Now replace each of the `d` fugacity-2 edges independently by any exact simple unit two-terminal network. Theorem 1 says each replacement network has at least seven edges, so replacing one representative edge adds at least six edges. Therefore the resulting unit-simple graph `S` satisfies

`|E(S)| >= (m-1-d)+6d = m-1+5d > m`.

So **no independent local exact response-2 unitizer can turn a source-generated STAR-2 contraction into a strictly smaller graph for an edge-minimal-counterexample induction**. For `d=1` the best possible local exact replacement has at least four more edges than the original parent.

This refutes the candidate mechanism

`CANDIDATE_REFUTED: LOCAL_TWO_TERMINAL_STAR2_UNITIZER_AS_MINIMALITY_STEP`.

Any successful size-controlled unitization must be genuinely joint/global (sharing structure across doubled edges or exploiting parent fibers), or one must bypass unitization and prove the contraction comparison directly.

## 3. Corrected exact sufficient statement for one doubled edge

Let `J` be a simple unit graph with distinct marked edges `e,f` and an unmarked edge `h`. Give only `h` weight `t` and write

`q(t)=Delta_J(e,f;t)=D0 + M t + D1 t^2`.

Here

`q(0)=D0=Delta_{J\h}(e,f)`

and `D1` is the Rayleigh count-gap in the contraction coefficient (equivalently `Delta_{J/h}` with contraction-created parallel copies retained distinctly). Direct algebra gives

`q(2) = 2 q(1) - q(0) + 2 D1`.

Hence a single source-generated doubling is safe **if and only if**

`q(0) <= 2 q(1) + 2 D1`.                                           (★)

When `h` lies in no triangle of `J`, `J/h` is again simple, so all three terms in (★) are genuine unit-simple minor gaps. This is a source-valid exact comparison; it does not assume arbitrary weighted Rayleigh closure. It identifies the quantitative minor-gap inequality that a direct minimality proof would have to derive.

For several doubled edges the same identity can be applied sequentially, but after the first doubling the intermediate graph is already weighted. Therefore a multi-edge proof still needs genuinely new structure; iterating (★) does not silently solve STAR-2.

## 4. Source-simple irreducible adversary to doubling monotonicity

A tempting strengthening of (★) is monotonicity `q(2)>=q(1)`. It is false even in the exact source-generated, common-block setting.

Take the five-vertex core

`J = K_5 - {34}`

with variable edge `h=01` and marks `e=03`, `f=14`. Exact forest counts give

`(A,B,a0,a1,b0,b1,c0,c1)=(134,64,52,18,52,18,19,5)`

and therefore

`q(t)=158 - 14 t + 4 t^2`.

Thus

`q(1)=148`,  `q(2)=146`.

The doubled edge and both marks lie in one 2-connected block, yet doubling **decreases** the gap.

This is genuinely source-generated by a simple triangle contraction. Split endpoint `0` into `0,5`, add the triangle edges `05,01,51`, keep `02,03,04,12,13,14,23,24`, and mark `e=03,f=14`, `g=05`. The parent is simple and 2-connected; `g` has exactly one common neighbor. Contracting `g` produces the core above with `01` doubled. Exact coefficients with respect to `g` have conditional-present gap `146`, while the parent unit gap is `1318`.

Therefore neither source generation nor irreducible block geometry implies `Delta(weight 2)>=Delta(weight 1)`. A valid direct proof must use an inequality of the exact type (★), or a stronger parent-fiber mechanism, rather than monotonicity in the doubled activity.

## 5. What this changes

The named partner's exact unitizer remains correct and valuable for parent-equivalence, but Theorem 1 shows that **optimizing the local gadget cannot repair its minimality mismatch**: seven edges is already optimal. This eliminates one natural implementation of the partner's `SIZE_CONTROLLED_STAR2` debt.

The next mathematically honest attack is therefore one of:

- prove (★) from the parent triangle geometry in the single-double case and then seek a joint multi-double analogue; or
- construct a genuinely joint cross-fiber transformation that preserves the marked Rayleigh gap and uses fewer than the parent's `1+2d` local triangle/spoke edges; or
- derive the triangle conditional comparison directly from the lead's rank/Simpson budget without unitizing.

The K4 union/intersection-preserving Hall obstruction cited by the named partner means the second option must allow genuine cross-fiber cut/join moves.

## Exact computation

`forest_star2_unitizer_checker.py` is a complete exact integer checker. It verifies:

- response-2 census `n=2..5`;
- the `82,160`-graph `m<=6` edge lower-bound certificate;
- the unique `(D,C)=(27,54)` seven-edge gadget;
- the overlapping-cycle coefficients `q(t)=158-14t+4t^2`;
- the exact identity `q(2)=2q(1)-q(0)+2D1`;
- the simple triangle lift's conditional-present gap `146` and parent gap `1318`.

The saved stdout ends `STATUS=PASS`. The Python process exited successfully. An unrelated environment spreadsheet-runtime warmup warning was emitted after the mathematical stdout; it was not used by the checker and is not copied into the operational artifact because it contains machine-local implementation details prohibited by this task.

## Status

`ESSENTIAL_STEP_APPLIED`.

Parent FOREST remains `OPEN`. No novelty claim is made. No benchmark material, private transcript, credential, production state, or unrelated private data was accessed or written. Brain installation/benchmark work remained stopped.
