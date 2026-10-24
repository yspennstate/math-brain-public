# FOREST / account04 B02 — full-radius transfer Hall is impossible even on K4

**Run:** `20260922T070653Z-account04-B02-forest-exchange-v4`  
**Outcome:** `CANDIDATE_REFUTED`  
**Refuted candidate:** `FOREST-FULL-RADIUS-TRANSFER-HALL-v1` and, more strongly, `FOREST-UNION-INTERSECTION-PRESERVING-RECOLOR-HALL-v1`  
**Parent FOREST target:** `OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Model self-report:** GPT-5.6 Sol. Requested effort: maximum actually supported. Configured effort and provider reasoning-token/thinking-time counters: `UNKNOWN / NOT_EXPOSED`.

## 1. Exact source scope and peer versions consumed

The source target is the Grimmett--Winkler uniform-forest pairwise negative-correlation conjecture: for every finite simple graph `G`, with `F` uniform over **all** acyclic edge subsets (empty forest, disconnected forests, and every forest size included, unit edge weights), prove

`P(e,f in F) <= P(e in F) P(f in F)`

for all distinct present edges `e,f`. I use the source/hypothesis boundary recorded in `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/TARGETS.md`; no rooted, fixed-size, spanning-tree, or weighted substitute is used.

The latest complete team-lead version read before this attempt was account01/B01 run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. Its report creation commit is `79044b575c4b689248892f37b9930e983dddabca`. I retain its correction that the old fixed-graph Cocks weighted-globalization bridge is not source-secure; the parent target remains open.

The named OTHER-account result consumed and directly attacked is partner account01/B03 run `20260922T052013Z-b03-forest-r11-d011c5`, report blob `d975b5c7b4257aee81eb4ee136b0cccce64b5033`. That report proves a **full-radius existence lemma**: for every residual left pair `(F,H)` there is at least one legal target obtained by transferring a suitable nonempty subset of the unique `e`-path of `F` from the first forest to the second (or all but one selected path edge in the overlap case). Its stated first missing implication is to upgrade that pointwise existence to Hall/fiber capacity.

This run proves that proposed Hall upgrade is impossible for the entire transfer-only support, even after enlarging it far beyond the partner's canonical path choice.

## 2. Residual comparison and partner formula

Put `G0=G-{e,f}` and let `N` be all forests of `G0`. Define

- `A={K in N : e is addable to K}`;
- `B={K in N : f is addable to K}`;
- `D={K in N : e and f are jointly addable to K}`.

Then the exact Rayleigh gap is

`Delta = |A||B| - |N||D|`,

and cancellation gives the equivalent residual comparison

`|(N\A) x D| <= |A x (B\D)|`.                                      `(R)`

Let `n11=|A intersect B|`, `n10=|A\B|`, `n01=|B\A|`, `n00=|N\(A union B)|`, and `q=|A intersect B|-|D|`. Then the partner identity is

`Delta = n10*n01 - n00*n11 + |N| q`.                               `(P)`

An injection from the residual left side of `(R)` into the residual right side would prove the target for the marked pair. The question here is what exchange support such an injection can use.

## 3. Exact K4 state

Take `G=K4` on vertices `{0,1,2,3}` with marked disjoint edges

`e=01`, `f=23`.

Then

`G0` has the four-cycle edges `{02,03,12,13}`.

Every proper subset of this four-cycle is a forest, so `|N|=15`. Direct exact counting gives

`|A|=|B|=9`, `|D|=5`,

and

`(n00,n10,n01,n11,q)=(4,2,2,7,2)`.

Hence

`Delta = 9*9 - 15*5 = 6`,

while the partner formula gives the same integer

`2*2 - 4*7 + 15*2 = 6`.

Thus the **source inequality is strictly true** on this witness. Any failure below is a failure of the proposed coupling geometry, not a counterexample to the conjecture.

The residual sides have

`|L|=|(N\A)xD|=30`, `|R|=|A x (B\D)|=36`.

## 4. Strong no-go theorem: preserving union and intersection cannot satisfy Hall

Define the broadest edge-recoloring support that preserves the set-theoretic union and intersection of the two forest coordinates. A left pair `(F,H) in L` is adjacent to a right pair `(F',H') in R` whenever

`F' union H' = F union H`,

`F' intersect H' = F intersect H`.

There is **no path, radius, cardinality, direction, or canonical-choice restriction** in this relation. Every edge lying in exactly one input coordinate may be recolored arbitrarily, subject only to the two output forests landing in the exact residual target.

Consider the following four left pairs. For each base edge `g` of the four-cycle, put

`F_g = E(G0) \ {g}`,  `H_g={g}`.

Each `F_g` is a three-edge spanning tree and therefore connects `0` to `1`, so `F_g notin A`. Each singleton `H_g` lies in `D`, since adding both `01` and `23` to one cross-edge remains acyclic. Hence all four `(F_g,H_g)` lie in `L`.

For all four pairs,

`F_g union H_g = E(G0)`,  `F_g intersect H_g = emptyset`.

A union/intersection-preserving right neighbor must therefore partition the four-cycle edges between its two coordinates. There are exactly two target partitions:

- `R1 = ( {03,12}, {02,13} )`,
- `R2 = ( {02,13}, {03,12} )`.

Here is the direct reason there are no others. Because the second coordinate must lie in `B\D`, it must keep `2,3` disconnected but fail joint addability. If it connected `0,1`, it would contain one of the two length-two `0-1` paths `{02,12}` or `{03,13}`; the complementary first coordinate would then contain the other `0-1` path, contradicting membership in `A`. Therefore the second coordinate must instead be an overlap state `Q`: both marked edges are individually addable but together close a cycle. On the four-cycle this forces the second coordinate to be one of the two opposite-edge matchings `{02,13}` or `{03,12}`, and the complement is the other matching.

Consequently this four-element left set has only two neighbors:

`|S|=4`, `|Gamma(S)|=2`.

Hall fails with deficiency `2`.

**Theorem (K4 union/intersection no-go).** No injection proving `(R)` can be supported solely on transformations that preserve both `F union H` and `F intersect H`, even for disjoint marked edges in `K4`.

This is stronger than a fixed-radius obstruction: allowing arbitrarily long exchanges and arbitrary recoloring inside the existing two-coordinate edge multiset still cannot close the comparison.

## 5. Direct refutation of the partner's one-way full-radius transfer support

The partner's full-radius reconnection lemma uses one-way moves of the form

`F' = F \ S`, `H' = H union S`,

where the selected transfer edges are taken from `F` (in the partner construction they are quotient-path crossing edges, hence absent from `H`). Enlarge this drastically: allow **any nonempty subset `S subseteq F`**, not only path edges and with no radius bound, provided the output lies in `R`.

Even this enlarged transfer graph violates Hall on the same `K4`. Two explicit left states are

`L1 = ( {03,12,13}, {02} )`,

`L2 = ( {02,03,12}, {13} )`.

For `L1` the only legal target obtainable by any one-way subset transfer is obtained by transferring `13`; for `L2` the only legal target is obtained by transferring `02`. Both land at exactly the same right state

`T = ( {03,12}, {02,13} )`.

All other subsets either fail to break the `0-1` connection in the first coordinate, make `23` non-addable in the second coordinate, or make the second coordinate cyclic. Thus the two-element left set `{L1,L2}` has a one-element neighborhood.

Therefore the account01/B03 full-radius **existence** lemma is correct but cannot be upgraded to a Hall injection while staying inside one-way transfer support. Pointwise existence is genuinely insufficient here.

## 6. What kind of coupling remains possible

The obstruction identifies a structural requirement, not just a larger radius. A successful exact injection must sometimes **change the pair's union or intersection**. Equivalently, it must be allowed to delete one edge from a coordinate while adding a different ambient edge to the other coordinate, create/remove overlap between the two coordinates, or use another mechanism with equivalent extra capacity.

As a diagnostic only, I tested the following broader cut/join support on this exact `K4` residual problem:

`F' subset F`, `H subset H'`, and `|F\F'|=|H'\H|>0`,

with `(F',H') in R`, but without requiring the added edges to be the same edges removed from `F`. This support **does** have an exact matching saturating all `30/30` left states on `K4`. This is finite evidence only; no universal Hall theorem is claimed.

Hence the next direct-coupling debt is no longer “increase the reconnection radius.” It is:

> build and prove a global Hall/flow bound for an exchange support that can alter union/intersection (for example external-edge cut/join or an alternating exchange that borrows ambient edges), while retaining exact unit multiplicities.

The present run does not replace the refuted Hall statement by assuming this new one.

## 7. Exact executable evidence

The standard-library exact checker exhaustively enumerates all forests of `G0=C4`, reconstructs `A,B,D`, verifies the partner cell formula, verifies the `4 -> 2` union/intersection-preserving Hall witness, verifies the `2 -> 1` arbitrary one-way transfer witness, and independently computes a saturating `30/30` matching for the broader external cut/join diagnostic.

- checker Git blob: `6cd5d65b1880ab4015016eee9579dadbaa90e640`;
- captured output Git blob: `6abc63f471bf1e87deed9780e325c77b1e1ca8a4`;
- local execution exit: `0`;
- terminal line: `STATUS=ALL_EXACT_ASSERTIONS_PASSED`.

The proof of the `4 -> 2` obstruction above is independent of the program; the program is regression evidence and exact bookkeeping.

## 8. Compact conditional end-to-end argument and first missing implication

The direct-count route is now sharply delimited:

1. `(R)` is exactly equivalent to the marked-edge Rayleigh inequality.
2. account01/B03 gives a legal full-radius transfer target for every left state.
3. A Hall injection using only those transfers would have proved `(R)`.
4. The `K4` witness above disproves that Hall statement, even for the much larger class of **all** union/intersection-preserving recolorings.
5. Therefore any surviving coupling proof must cross the union/intersection boundary. A source-valid route would be an external-edge cut/join or alternating-exchange support with a universal subset Hall/flow inequality.

The **first essential missing implication** for this slot is now precisely such a non-union-preserving Hall/flow theorem; increasing radius or improving the canonical choice inside the existing transfer support cannot work.

## 9. Honest status

`CANDIDATE_REFUTED` for `FOREST-FULL-RADIUS-TRANSFER-HALL-v1` and the stronger `FOREST-UNION-INTERSECTION-PRESERVING-RECOLOR-HALL-v1`.

The parent uniform-forest negative-correlation conjecture remains `OPEN`. The team lead's separate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1` route is unaffected. No fixed-graph Cocks globalization, finite-census closure, weighted replacement conjecture, benchmark material, brain-installation work, production mutation, email, Drive write, public posting, paid/remote compute, or permission change is used here.
