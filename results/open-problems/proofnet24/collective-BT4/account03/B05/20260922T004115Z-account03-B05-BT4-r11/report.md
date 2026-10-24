# BT4 account03/B05 — segment-bypass exchange and block-collar amplification

Run: `account03-B05-20260922T0041Z-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Candidate: `BT4-TCEX-v2-segment`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Authority and exact target

Fresh owner control revision `2026-09-22.2` supersedes the old B05 brain-installation/cognitive-firing assignment. The live account03/B05 assignment is now collective BT4 research: prove the disjointness-preserving exchange promised by the current two-partition/linkage candidate, without replacing minimum-outdegree hypotheses by averages.

The source-exact target is the `k=4` Bermond-Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a digon counts as a directed cycle. The current source record cites Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the exact directed statement remains unresolved for `k>=4`; their same-threshold result allows a one-arc reversal and is not substituted here.

## Exact peer mathematics consumed

The named other-account partner was consumed directly:

- `account04/B06`, report `proofnet24/collective-BT4/account04/B06/20260922T001024Z-b06-bt4-r43/report.md`, blob `08cf8f4283de825d533677d6edf5707523744a22`, candidate `BT4-MCR-v2`. Its missing-arc saturation lemma produces a fan-avoiding return path plus a disjoint replacement three-packing, and its boundary-blocking lemma converts an occupied predecessor at the final old-packing gateway into a forced exit arc used by a replacement cycle.

I also use the compatible exact current exchange state:

- `account01/B05`, report `proofnet24/collective-BT4/account01/B05/20260922T002817Z-account01-B05-BT4-r11/report.md`, blob `f61ce94c50464f2d59491377df32f7e549db7242`, candidate `BT4-TCEX-v1`. It proves the support-correct one-vertex two-cycle bypass inequality `m<=ell` and the neutral equality exchange.
- `account02/B04`, correction `proofnet24/collective-BT4/account02/B04/20260922T001806Z-b04-bt4-a1ceeb3c/correction.md`, blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`. In the exact-seven normal form, a cycle-supported five-fan witness has one unique `R`-exit and a six-fan witness has no `R`-exit; witness support on the complementary packed cycle cannot be treated as if it lay in `R`.
- `account03/B06`, commit `4e204703776c90319afc67c4a03d56d474272d9c`, candidate `BT4-RSC-v2-tight-port`. Its equality exchange forces acyclicity of the exchanged remainder and hence an inversion prohibition on freed consecutive vertices.

No peer PASS label is used as a theorem. Only the stated proved reductions above enter the derivation.

## Shared conditional route and first unpaid implication

Assume BT4 false. Work in the exact-outdegree-seven, oriented minimum counterexample with a globally minimum-total three-cycle packing `(A,B,C)` and acyclic remainder `R`, as supplied by the current lead state.

The repaired pair-deletion branch gives either witnesses in `R`, where the one-vertex path-fan machinery applies, or witnesses on the complementary packed cycle. In the latter case a five-witness has exactly one `R`-exit while a six-witness has none. `BT4-TCEX-v1` handles a single cycle-supported witness when an `R`-internal predecessor-to-successor bypass is available. The surviving obstruction is that several five-witnesses can interact through a longer portion of their own packed cycle, and applying single-witness inequalities separately does not account for the vertices simultaneously displaced.

The next lemma is the exact multi-vertex disjointness-preserving exchange. It strictly contains the `BT4-TCEX-v1` inequality as the case of a one-vertex segment.

## Lemma 1 — segment-bypass exchange inequality

Let `A,B,C` be a globally minimum-total three-cycle packing in a digraph with no four vertex-disjoint directed cycles, and let `R` be the uncovered vertex set. Let

`S=B[u,v]`

be the forward directed segment of `B` from `u` through `v`, inclusive, with

`1 <= s:=|S| <= |B|-2`.

Write `u^-` for the predecessor of `u` and `v^+` for the successor of `v` on `B`. Assume:

1. `b in V(A)` and `b->u` is an arc;
2. there is a directed path

   `Q: u^-=q_0 -> q_1 -> ... -> q_ell=v^+`

   whose internal vertices `q_1,...,q_(ell-1)` lie in `R`.

Then for every `a in N^+(u) intersect V(A)`, if `t=d_A(b,a)` is the forward distance from `b` to `a` on `A`,

`                         t <= ell+1-s.                 (1)`

Consequently, with `m=|N^+(u) intersect V(A)|`,

`                         m <= ell+1-s,                 (2)`

or equivalently

`                         ell >= m+s-1.                 (3)`

### Proof

Because the minimum counterexample is oriented, `a!=b`: otherwise `b->u` and `u->b` would be a digon.

For a fixed such `a`, form

`A_a = b -> u -> a -> A[a,b]`,

where `A[a,b]` is the forward directed segment of `A` from `a` back to `b`. If `r_A=|A|`, then

`|A_a| = r_A+2-t`.                                      (4)

Now bypass the entire segment `S` in `B`. Let

`B_Q = Q + B[v^+,u^-]`,

where `B[v^+,u^-]` is the forward complementary segment of `B`. Since `S` has `s` vertices, its complement has `|B|-s` vertices; the path `Q` has `ell+1` vertices and shares its two endpoints with that complementary segment. Hence

`|B_Q| = |B|-s+ell-1.                                  (5)`

The cycles `A_a` and `B_Q` are vertex-disjoint: `A_a` uses vertices of `A` together with the single vertex `u` of `B`; `B_Q` uses `B-S` together with internal vertices of `R`. Both are disjoint from the untouched packed cycle `C`.

Thus `(A_a,B_Q,C)` is another legitimate three-cycle packing. Relative to `(A,B,C)`, its total covered size changes by

`(2-t)+(ell-s-1)=ell+1-s-t`.                            (6)

Global minimality forbids a negative change, proving (1).

The distinct outneighbors of `u` on `A` give distinct positive forward distances from `b`. If `ell+1-s<|A|`, all such distances lie in `{1,...,ell+1-s}` by (1); if the upper bound is at least `|A|-1`, the trivial bound `m<=|A|-1` is already no larger. Therefore (2), hence (3), follows. QED.

### Why this is a genuine strengthening

For `s=1`, the segment is just `{u}` and (3) becomes `ell>=m`, exactly the single-witness two-cycle bypass inequality of `BT4-TCEX-v1`. For `s>1`, every additional packed-cycle vertex bypassed costs one additional unit of path length. This cost comes from exact vertex accounting, not an average-degree estimate.

## Lemma 2 — equality normal form and exchanged remainder

Under Lemma 1, assume equality in (2):

`                         m=ell+1-s.                    (7)`

Then the fan of `u` on `A` is forced to be consecutive:

`N^+(u) intersect A={b^+,b^(+2),...,b^(+m)}.            (8)`

Choosing `a=b^(+m)` in the construction gives a new globally minimum three-cycle packing `(A*,B*,C)` with

`A*=b -> u -> b^(+m) -> A[b^(+m),b]`,

`B*=Q+B[v^+,u^-]`.

Let

`F_A={b^+,...,b^(+(m-1))}`,  `Q^o={q_1,...,q_(ell-1)}`.

The new remainder is exactly

`R*=(R\Q^o) union F_A union (S\{u}).                   (9)`

Moreover `D[R*]` is acyclic. Hence:

- there is no directed path in `R*` from a later vertex of `F_A` back to an earlier one;
- there is no directed path in `R*` from a later vertex of the freed directed segment `S\{u}` back to an earlier one.

### Proof

Equation (1) places the `m` distinct positive fan distances in `{1,...,m}`, proving (8). With `t=m`, (6) is zero by (7), so the exchange is size-neutral.

The internal bypass vertices consumed from `R` number

`|Q^o|=ell-1=m+s-2`.

The vertices freed from `A` number `m-1`, and the vertices freed from `B` are precisely `S\{u}`, numbering `s-1`. The counts agree, giving (9).

If `R*` contained a directed cycle, that cycle together with `A*,B*,C` would be four vertex-disjoint directed cycles in the original digraph, contradiction. The two inversion prohibitions follow by adjoining any hypothetical backward path to the surviving forward old-cycle segment between its endpoints. QED.

This is the first neutral exchange in the current candidate that can free a nontrivial block of the complementary packed cycle at the same time as a consecutive fan block on the target cycle.

## Corollary 3 — block-collar amplification for consecutive five-witnesses

Work in the exact-seven normal form. Suppose

`z_0,z_1,...,z_k`

are consecutive vertices of the packed cycle `B`, with `k>=1`, and `z_0` is a cycle-supported five-fan witness for a deleted pair. Let `r` be its unique `R`-outneighbor. Suppose `z_1` is heavy on a packed cycle `A`, with

`m=|N^+(z_1) intersect A|>=3`,

and some `b in A` satisfies `b->z_1`.

If `q in R` satisfies `q->z_k^+` and there is a directed `R`-path from `r` to `q`, then

`                  dist_R(r,q) >= m+k-3.               (10)`

### Proof

Use the segment

`S=B[z_1,z_k]`,

which has `s=k` vertices. The path

`z_0 -> r -> ... -> q -> z_k^+`

is an `R`-internal bypass from `z_1^-=z_0` to `z_k^+` of length

`ell=dist_R(r,q)+2`.

Lemma 1 gives `ell>=m+s-1=m+k-1`, which is exactly (10). QED.

For `k=1`, (10) recovers the single-witness collar `dist_R(r,q)>=m-2`. For two vertices in the bypassed segment (`k=2`), it strengthens that to

`dist_R(r,q)>=m-1`.

Since every directed path in the acyclic remainder has length at most `|R|-1`, (10) also gives the immediate avoidance criterion

`m+k>|R|+2  =>  no arc A->z_1`

whenever the stated entry path to `z_k^+` exists. This is a minimum-packing obstruction, not a degree-average surrogate.

At equality in (10), Lemma 2 applies: the exchange frees both the consecutive `m-1` block on `A` and the `k-1` vertices `z_2,...,z_k` on `B`, while consuming the exact same number of remainder vertices. The no-four-pack hypothesis then forces acyclicity and both inversion prohibitions in the new remainder.

## What changed in the live candidate

Before this run, the cycle-supported branch had a sharp single-witness alternative: either a short predecessor-to-successor bypass gives reverse avoidance, or the bypass is long; equality gives one neutral exchange. That leaves the three-five-witness branch difficult because separate one-vertex estimates do not account for overlapping use of the same packed cycle.

`BT4-TCEX-v2-segment` supplies the missing multi-vertex accounting. A bypass around `s` consecutive packed-cycle vertices has the sharp lower bound `ell>=m+s-1`; at equality it gives a single disjointness-preserving two-cycle exchange with an exactly described remainder. In particular, a consecutive block of five-witnesses creates an accumulating collar in `R`, not merely several independent copies of the old `m-2` bound.

This does not yet prove that the three five-witnesses supplied by pair deletion contain a long enough consecutive block, nor that the necessary entry into `z_k^+` is always reachable from the predecessor witness's unique `R`-exit. Those are the remaining structural obligations; I do not hide them inside the exchange lemma.

## First remaining universal implication

The next exact step is:

> In the third-cycle five-witness saturation branch, use the three witnesses together with the missing-arc saturation/forced-exit certificates to produce either (i) an `R`-internal segment bypass violating `ell>=m+s-1`, or (ii) an equality segment exchange whose two freed blocks force a directed cycle in the exchanged remainder, or (iii) a source-valid structural separation showing all such bypasses are long and then exploit that separation to obtain a strict packing reduction.

The six-witness branch remains separate because a cycle-supported six-witness has no `R`-exit; importing the five-witness collar there would be invalid.

## Adversarial checks and scope

- All replacement cycles are vertex-disjoint; no edge-disjoint surrogate is used.
- Every internal vertex of `Q` is required to lie in the actual old remainder `R`.
- The segment size restriction `s<=|B|-2` keeps `u^-` and `v^+` as distinct vertices on the complementary directed segment; degenerate whole-cycle bypasses are not silently included.
- The arc `b->u` is an explicit hypothesis. No blanket `heavy => return` or `heavy => no return` claim is made.
- Global minimum is minimum over all three-cycle packings, exactly the hypothesis needed for (6).
- Equality yields another minimum packing, not an immediate contradiction.
- Acyclicity of `R*` uses the actual no-four-vertex-disjoint-cycle assumption and is where target-level global information enters.
- This report does not claim BT4 solved or claim novelty in the literature.

## Outcome and recipients

`ESSENTIAL_STEP_APPLIED`.

The requested disjointness-preserving exchange is now proved for an entire packed-cycle segment, with sharp vertex accounting, equality normal form, exact exchanged remainder, and a block-collar consequence that strengthens the current three-five-witness route. Full BT4 remains open.

Next recipients: `account04/B06` (assigned partner, to combine the segment exchange with its missing-arc saturation and forced-exit certificates), `account02/B04` (campaign lead), and `account01/B05` (to replace the single-witness exchange by the segment form when witness blocks occur).
