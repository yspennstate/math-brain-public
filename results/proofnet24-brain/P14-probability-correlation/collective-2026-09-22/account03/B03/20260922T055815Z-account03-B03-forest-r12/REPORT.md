# FOREST cubic-vertex terminal-partition theorem

Run: `20260922T055815Z-account03-B03-forest-r12`  
Account/slot: `account03/B03`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Context: `WITHOUT_VERIFIED_BRAIN`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent FOREST conjecture remains **OPEN**; no public solved-problem or novelty claim is made.

## Exact assignment and peer consumed

The exact B03 assignment is to compute exact forest-pair counts for structured adversaries to the shared candidate and use failures to derive a missing structural constraint, rather than report a census. Assigned partner: `account04/B01`.

I consumed the completed `account04/B01` report at commit `3b53272eba18cdec04e029651173b1410e3b8b12`. Its exact two-vertex-separator identities imply, together with the fixed-graph Cocks positive-weight upgrade, that an edge-minimal simple counterexample to the unit uniform-forest conjecture must be 3-vertex-connected. I use that conclusion below; I do not substitute the peer's PASS for the new argument.

The current lead candidate `FOREST-KN-HERMITE-REDUCTION-v1` was also read from blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`. It supplies an internal all-`K_n` proof candidate plus the Cocks/minor globalization route. That candidate is not promoted here; its complete-graph derivation still has the team's independent-review gate.

## New mechanism: eliminate a cubic vertex exactly

Let `G` be any finite graph with a vertex `v` of degree exactly three and distinct neighbors `u1,u2,u3`. Write the incident edges

`e1=vu1`, `e2=vu2`, `e3=vu3`,

and let `H=G-v`. Give the edges of `H` arbitrary positive weights. The three incident edges are kept at unit weight, matching the source target.

Partition the weighted forests of `H` according to the connectivity partition induced on `u1,u2,u3`:

- `A`: `1|2|3` (all three terminals in different components);
- `B12`: `12|3`;
- `B13`: `13|2`;
- `B23`: `23|1`;
- `C`: `123`.

The letters denote the total weighted masses of those classes. They are nonnegative and

`T=A+B12+B13+B23+C`

is the full weighted forest partition function of `H`.

For a fixed forest of `H`, a chosen subset of `{e1,e2,e3}` remains acyclic iff it contains at most one star edge whose other endpoint lies in any one component of the `H`-forest. Hence, with formal incident-edge weights `x,y,z`, the exact local extension polynomial is

`Phi(x,y,z) = A(1+x)(1+y)(1+z)`

` + B12(1+x+y)(1+z)`

` + B13(1+x+z)(1+y)`

` + B23(1+y+z)(1+x)`

` + C(1+x+y+z)`.

This identity includes the empty forest, disconnected forests, and every forest size. It does not root the forest or condition on a component count.

## Exact unit Rayleigh factorization

For the marked pair `e1,e2`, set `x=y=z=1`. Direct differentiation gives

`Z = 8A + 6(B12+B13+B23) + 4C`,

`Z_1 = 4A + 2B12 + 2B13 + 3B23 + C`,

`Z_2 = 4A + 2B12 + 3B13 + 2B23 + C`,

`Z_12 = 2A + B13 + B23`.

The exact Rayleigh difference factors as

`Delta_G(e1,e2) = Z_1 Z_2 - Z Z_12`

`= 4 B12 T + (B13+C)(B23+C) >= 0`.

Therefore:

> **Cubic-vertex theorem.** In the uniform law on all unrooted forests, every pair of edges incident to a degree-three vertex is negatively correlated. More strongly, this remains true when every edge outside that three-edge star has an arbitrary positive weight, while the three star edges themselves have unit weight.

The same formula holds for the other two incident pairs by permuting terminal labels.

This is an exact theorem, not finite evidence. It follows solely from the five terminal-partition masses being nonnegative.

## Strict form inside the partner's 3-connected reduction

Now assume `G` is 3-vertex-connected and `v` is cubic. Then `H=G-v` is 2-connected. For any two neighbors, say `u1,u2`, there is a `u1-u2` path in `H` avoiding `u3`; taking exactly that path as the selected forest gives a forest counted by `B12`. Thus `B12>=1` in the unweighted source model.

Consequently

`Delta_G(e1,e2) >= 4 T = 4 F(H) > 0`.

So any violating edge pair in a 3-connected graph with a cubic vertex must avoid being a pair of edges incident to that cubic vertex. In particular, in a cubic 3-connected counterexample candidate, every violating pair must be vertex-disjoint.

Combined with the assigned partner's exact result, any edge-minimal counterexample must therefore satisfy BOTH:

1. the graph is 3-vertex-connected; and
2. no violating pair is an adjacent pair at a cubic vertex.

This is the requested new structural constraint, not a graph census.

## Weighted third-edge diagnostic and recursive coefficient

To expose where the unit proof stops, keep `e1,e2` at unit weight but assign the third star edge weight `g>0`. The same terminal-partition identity gives

`Delta_12(g) = L g^2 + 2 B12 T g + (B12+C)T`,

where

`L = A B12 - A C + B12^2 + B12 B13 + B12 B23 + B13 B23`.

At `g=1`, this polynomial is exactly the manifestly nonnegative factorization above. The coefficient `L` is itself the unit Rayleigh difference for the two edges `u3u1` and `u3u2` added to `H` (interpreted as distinct added edges):

`Z_K=4A+3B12+2B13+2B23+C`,

`Z_{u3u1}=2A+B12+B23`,

`Z_{u3u2}=2A+B12+B13`,

`Z_{both}=A`,

so `Delta_K=L`.

This identity explains a real boundary of the local mechanism. Unit cubic-star negativity is automatic, but arbitrary positive weight on the third star edge exposes another graph's Rayleigh gap in the leading coefficient. If an added edge duplicates an existing simple edge, the augmentation is a multigraph object and cannot be fed into simple-graph minimality without a separate parallel-edge/weight argument. I therefore do not use this diagnostic to claim a degree-three vertex can be eliminated from all counterexamples.

## Exact regression

A deterministic standard-library checker independently enumerated every forest for all 64 simple graphs `H` on four labelled vertices with terminals `0,1,2`, verified the unit formulas exactly, and also verified the polynomial `Delta_12(g)` at `g=2,3,5`. Four additional positive-integer-weight stress instances on `H` were checked exactly.

Result: `PASS`.

- checker SHA-256: `2bfd54ddf871ef6c6e56ba1795a758c63214ffd59ce1c7cbef015d0cc707603a`
- output SHA-256: `23d7c30ca04e6612dd16f994be7813ab0c85e43d88b0a6f4c0b103fa6395e1b1`

The computation is regression for the algebra; the theorem is the exact symbolic factorization above.

## Source/globalization note

The fixed-host weighted step used by the partner is consistent with the final Semple--Welsh paper's added note recording Cocks's theorem: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Semple--Welsh define independence correlation for all positive real edge weights and prove minor closure. This source step is not reproved by the cubic argument and is not needed for the local factorization itself.

Primary references retained from the team state:

- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423--435.
- C. C. Cocks, *Correlated Matroids*, Combinatorics, Probability and Computing 17 (2008), 511--518.

## Remaining obligation

The parent all-graphs FOREST conjecture is not closed by this lemma. The currently shortest team-level route is still: independently validate the complete-graph/Hermite theorem for every `n`, then apply the already source-checked Cocks/minor globalization. If that internal `K_n` theorem fails review, the cubic-vertex theorem remains a valid structural reduction for any renewed minimal-counterexample route.
