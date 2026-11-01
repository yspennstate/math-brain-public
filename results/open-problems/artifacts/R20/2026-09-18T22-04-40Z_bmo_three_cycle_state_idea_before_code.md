# R20 idea before code — finite interface algebra for three-cycle triangular cacti

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Current owner/target: continue the exclusive R20 claim `operations/claims/BMO-2025-PUSHING-DELTA.md`, not retired I0100 and not handed-off KNSV. Fixed all-graphs metric remains `n_all=8`.

This run uses new Section-B moves #13 FIND WHAT ONLY INCREASES, #19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT.

## Idea

Work modulo 3 on the cycle-core of a cactus and encode a rooted subtree by a relation

`R subset F_3^3`, with `(r,s,t) in R` meaning: the root push is `r`, the desired final root sum modulo 3 is `s`, and the rooted subtree contributes `t` modulo 3 at the root, while every internal core edge is distinguished modulo 3. Ordinary tree appendages remain handled by the already-written tree-transparency lemma, where pendant edges need only integer properness.

For an empty rooted child collection,

`U = {(r,s,0): r,s in F_3}`.

A leaf triangle gives the exact syndrome relation

`F = {(r,r-1,t): r,t in F_3}`.

There are three exact composition operations on relations:

1. `B(R)`: insert one bridge between the current root and a child with state `R`;
2. `M(R,S)`: identify the roots of two child collections and add their contributions;
3. `T(R,S)`: make a triangle whose two nonroot vertices carry child states `R,S`.

The research question is whether this state algebra collapses to a small readable family before the first possible obstruction. In particular, for a leaf triangle moved `k` bridges away from the current root, calculate `B^k(F)` symbolically. The preliminary algebra suggests the sharp stabilization

- `k=0`: `s=r-1`, contribution arbitrary;
- `k=1`: every contribution except `t=s+r-1`;
- `k=2`: every contribution except `t=1-r`;
- `k>=3`: all 27 triples are attainable.

This is far stronger than another graph-by-graph census: after three bridge steps a triangle branch is completely transparent to the parent state.

The next target is to classify all rooted triangular cactus cores with at most three cycle blocks under `B,M,T`, prove that every whole-graph state relation contains a diagonal state `s=t`, and identify the shape attaining the smallest diagonal set. A diagonal state is exactly what closes the root when there is no parent contribution.

A second goal is to ask where this strong modulo-3 mechanism first fails. If a four-cycle triangular cactus has no diagonal state (or even empty rooted relation), that is a genuine obstruction to the present proof architecture rather than a counterexample to `P^l<=2`: search for an exact integer `{0,1,2}` pushing witness on that same graph. Such a pair — no all-edges-mod-3 certificate but a valid integer certificate — would explain precisely why the source authors' modulo approach becomes complicated after a few cycle blocks.

No checker has been written for this run before this note. Any finite claim below will be validated exactly after the state formulas and proof are written down.
