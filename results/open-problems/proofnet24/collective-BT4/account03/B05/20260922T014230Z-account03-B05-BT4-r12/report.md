# BT4 account03/B05 — three-linkage overlap reduction and odd-sign bypass

Run: `20260922T014230Z-account03-B05-BT4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-TCEX-v3-overlap`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and authority

The live owner control supersedes the historical account03/B05 brain-installation/cognitive-firing prompt. The active account03/B05 assignment is collective BT4 research: prove the disjointness-preserving exchange promised by the current linkage candidate without replacing minimum-outdegree hypotheses by average-degree arguments.

The target is the k=4 Bermond-Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are permitted by the source problem and a directed digon counts as a cycle. The current campaign source check records Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 August 2026), as leaving the exact k>=4 conjecture unresolved while proving a one-reversed-arc relaxation. No relaxed cycle is used below as a directed cycle.

## Exact peer state consumed

The named OTHER-account partner result used directly is:

- account04/B06, `BT4-SINKLINK-v1`, `proofnet24/collective-BT4/account04/B06/20260922T011432Z-b06-bt4-r11/report.md`, blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`.

Its proved no-six sink localization is the immediate input below. For a remainder sink with fan type `(3,2,2)`, heavy on one packed cycle and light on the other two, either a light cycle has order at most `|R|`, or the two light cycles are joined in both directions by a genuine directed cycle whose only other vertices lie in `R` and all point to the defining sink. In the three-sink hard core with distinct heavy labels, if every light cycle has order greater than `|R|`, this yields one such two-way linkage for every pair of packed cycles. The partner explicitly leaves compatibility of the three linkage cycles unpaid.

I also consumed the newest campaign lead state:

- account02/B04, `proofnet24/collective-BT4/account02/B04/20260922T011943Z-b04-bt4-r11/report.md`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

It preserves the exact-seven oriented minimum-counterexample normal form, globally minimum-total three-cycle packing, acyclic remainder, arc domination and 3-vertex-strongness, and isolates cross-linkage closure as one of the three live universal obligations.

Compatible dynamic information also consumed:

- account02/B20 late-lead addendum `proofnet24/collective-BT4/account02/B20/20260922T013238Z-account02-B20-bt4-r11/late_lead_addendum.md`, blob `aac4b9da986de7371a255291e71268e2f47aeca2`, which shows that the partner linkage gives two neutral pivot directions and that coincidence of the regenerated five-witnesses has one of three exact profiles;
- this slot's corrected marked-segment/linkage package, blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

No peer outcome label is promoted to a theorem.

## Setup for the partner's three-sink hard core

Assume BT4 false and work in the inherited exact-seven normal form. Let `(A,B,C)` be a globally minimum-total packing of three directed cycles and let

`R = V(D) \ (V(A) union V(B) union V(C))`, `r=|R|`.

Assume the global no-six branch has exactly three remainder sinks

`x_A, x_B, x_C`,

with distinct heavy labels: `x_A` is heavy on `A`, `x_B` on `B`, and `x_C` on `C`. Assume further that every sink is in the partner's linkage alternative, equivalently both of its light packed cycles have order greater than `r`. Since each packed cycle is light for two of the three sinks,

`|A|>r, |B|>r, |C|>r`.                                           (1)

Write the partner's three genuine linkage cycles as follows:

- `Q_A` joins `B` and `C`, uses exactly one vertex of each, has all remaining vertices in `R\{x_A}`, and every such remainder vertex sends an arc to `x_A`;
- `Q_B` joins `A` and `C` analogously and all its remainder vertices send an arc to `x_B`;
- `Q_C` joins `A` and `B` analogously and all its remainder vertices send an arc to `x_C`.

Each `Q_X` is a genuinely directed cycle in the original digraph, not a near-directed surrogate.

The first unpaid point is exactly the partner's compatibility problem: the three cycles can overlap inside `R` or at their packed-cycle ports, so they cannot simply be adjoined as a new three-packing.

## Lemma 1 — linkage interiors avoid all three sinks

No internal remainder vertex of any `Q_A,Q_B,Q_C` is one of `x_A,x_B,x_C`.

### Proof

The defining sink is excluded by the partner construction. Suppose, for example, that `x_B` were an internal remainder vertex of `Q_A`. Every remainder vertex of `Q_A` sends an arc to `x_A`, so `x_B->x_A` would be an arc of `D[R]`. But `x_B` is a sink of the DAG `D[R]`, contradiction. The same argument applies to all distinct pairs. QED.

This small observation is important for exact vertex accounting below: all three sinks remain uncovered by every linkage cycle.

## Lemma 2 — the three partner linkages cannot be mutually vertex-disjoint

The cycles `Q_A,Q_B,Q_C` are not pairwise vertex-disjoint.

### Proof

Assume they were pairwise vertex-disjoint. Each linkage cycle uses exactly two packed-cycle vertices, so together they use six packed vertices. By Lemma 1 their internal remainder sets are disjoint subsets of `R\{x_A,x_B,x_C}`, hence contain in total at most `r-3` vertices. Therefore

`|Q_A|+|Q_B|+|Q_C| <= 6+(r-3)=r+3`.                              (2)

On the other hand, (1) and integrality give

`|A|+|B|+|C| >= 3(r+1)=3r+3`.                                   (3)

Since `r>0`, (2) is strictly smaller than (3). Thus `(Q_A,Q_B,Q_C)` would be a three-cycle packing covering strictly fewer vertices than the globally minimum packing `(A,B,C)`, contradiction. QED.

Hence the compatibility problem is not optional: in the all-long-light three-sink core, overlap is forced by global minimum packing.

## Lemma 3 — overlap multiplicity pays exact remainder outdegree

Let `y in R` be internal to `k` of the linkage cycles, where `k in {1,2,3}`. Then

`d_R^+(y) >= k`.                                                  (4)

In particular:

- a pairwise-overlap vertex has at least two distinct remainder outneighbors, namely the two corresponding defining sinks;
- a triple-overlap vertex has at least three distinct remainder outneighbors and therefore at most four outgoing arcs in total to `A union B union C`.

If a pairwise-overlap vertex is also a five-fan witness for some pair of packed cycles, then it has **exactly** two remainder outneighbors and no outneighbor on the third packed cycle. Thus its two remainder outarcs are precisely the two sink arcs forced by the overlap.

### Proof

If `y` is internal to `Q_X`, the partner's localization says `y->x_X`. The defining sinks are distinct, so membership in `k` linkage interiors gives `k` distinct outneighbors inside `R`, proving (4). Exact outdegree seven gives the triple-overlap bound.

For the final statement, a five-fan into a chosen packed pair already uses five of the seven outgoing arcs. Pairwise linkage overlap forces two distinct `R` outarcs, exhausting the other two arcs. Hence there is no further outarc to the third packed cycle and the two remainder heads are exactly the corresponding sinks. QED.

This interfaces directly with the current collision bookkeeping: the rigid two-`R`-outarc five-witness profile is the only way a five-fan can sit at a pairwise linkage-overlap vertex. A triple-overlap vertex can never itself be a five-fan because it already spends at least three arcs in `R`.

## Lemma 4 — odd-sign rule at a triple overlap forces an R-internal packed-cycle bypass

Assume there is a triple-overlap vertex

`z in int(Q_A) cap int(Q_B) cap int(Q_C)`.                         (5)

For each incidence of a linkage `Q` with one of its two packed cycles `X`, let `p_X(Q)` be the unique packed vertex of `X` on `Q`. Assign a sign at that incidence:

- `+` if the directed subpath of `Q` from `p_X(Q)` to `z` has all internal vertices in `R`;
- `-` if the directed subpath of `Q` from `z` to `p_X(Q)` has all internal vertices in `R`.

For each linkage, its two endpoint signs are opposite. Consequently, for at least one packed cycle `X in {A,B,C}`, the signs contributed by its two incident linkages are opposite.

If the two corresponding ports `u,v in X` are distinct, there is a directed `u`-to-`v` path `P` whose internal vertices all lie in `R`. If the ports coincide, there is a directed closed walk based at that port whose other vertices lie in `R`.

### Proof

A directed cycle `Q_A`, for example, consists of a directed `B`-port-to-`C`-port path and the complementary directed `C`-port-to-`B`-port path. Since `z` is an internal remainder vertex, it lies on exactly one of those two directed arcs of the cycle decomposition. Thus one packed endpoint reaches `z` and `z` reaches the other: the two incidence signs on every linkage are opposite.

Suppose, for contradiction, that on each packed cycle the signs supplied by its two incident linkages were equal. Let the common signs be `s_A,s_B,s_C in {+,-}`. The linkage `Q_C` connects `A` to `B`, so `s_A=-s_B`. The linkage `Q_A` connects `B` to `C`, so `s_B=-s_C`. Hence `s_A=s_C`. But `Q_B` connects `A` to `C`, so it requires `s_A=-s_C`, contradiction.

Therefore some packed cycle `X` receives opposite signs. Concatenate the directed port-to-`z` piece from one linkage with the directed `z`-to-port piece from the other. The concatenation is a directed walk with endpoints on `X` and every internal vertex in `R`. If the endpoints are distinct, erase directed subcycles/repeated portions to obtain a simple directed path `P` with the same endpoints and all internal vertices in `R`. If the endpoints coincide, retain the closed directed walk. QED.

This is an odd-cycle parity obstruction on the three linkage incidences. It uses directed orientation, not an undirected intersection argument.

## Lemma 5 — exact exchange consequence of the odd-sign bypass

Use Lemma 4.

### Distinct-port case

Let `P:u->...->v` be the resulting simple path with internal vertices in `R`, and let

`d=d_X(u,v)`

be the forward directed distance in edges from `u` to `v` on `X`. If `ell` is the length of `P`, then

`ell >= d`.                                                        (6)

If equality holds, replacing `X` by

`X_P = P + X[v,u]`

is a size-neutral globally minimum one-cycle exchange. Its new remainder is

`R_P = (R \ int(P)) union int(X[u,v])`,                            (7)

and `D[R_P]` is acyclic. If `ell>d`, the same replacement is legal but larger and is not by itself an extremal improvement.

### Coincident-port case

If the two ports coincide at `u`, the closed walk from Lemma 4 contains a simple directed cycle `W` through `u` whose other vertices lie in `R`. Since `R` is acyclic, every directed cycle extracted from this closed walk must use `u`. Global minimum of the original three-packing gives

`|W| >= |X|`.                                                       (8)

But `W` uses at most the `r` vertices of `R` plus `u`, whereas (1) gives `|X|>=r+1`. Therefore equality is forced throughout:

`|W|=|X|=r+1`, and `W` uses every vertex of `R`.                    (9)

Thus a coincident-port triple-overlap is not free: it forces an exact whole-remainder neutral replacement.

### Proof

In the distinct-port case, `X_P` is disjoint from the other two packed cycles because `P` has only its endpoints on `X` and all other vertices in `R`. Its size is

`|X_P| = |X| + ell-d`.

If `ell<d`, replacing `X` by `X_P` while keeping the other two packed cycles would strictly reduce the globally minimum total packing, impossible. This proves (6). Equality gives a minimum packing again; if its remainder contained a directed cycle, that cycle together with the three packed cycles would give a forbidden four-pack, proving acyclicity and (7).

For coincident ports, extract a simple directed cycle from the closed directed walk. A cycle avoiding `u` would lie entirely in `R`, impossible because `R` is acyclic, so choose a cycle `W` through `u`. It is disjoint from the other two packed cycles and may replace `X`, giving (8). The size bounds then force (9). QED.

For `d>=2`, (6) is exactly the one-cycle segment-bypass tax `ell>=|S|+1` with `S=int(X[u,v])`. If that skipped segment contains a current heavy cycle-supported witness, the stronger marked-segment tax from `BT4-TCEX-v2.1-linkage` can be applied with its fan parameter. The present lemma does not assume such a witness lies on the skipped segment.

## Corollary 6 — exact reduction of the three-linkage compatibility obstruction

In the partner's three-sink, distinct-heavy-label, all-long-light no-six core, at least one of the following occurs:

1. two linkage cycles share a packed-cycle port;
2. two linkage cycles overlap in `R` but no vertex lies in all three linkage interiors;
3. a triple-overlap vertex exists, in which case Lemmas 4-5 force an `R`-internal packed-cycle bypass, or the rigid coincident-port whole-remainder neutral replacement (9).

The mutually vertex-disjoint case is impossible by Lemma 2. Any overlap vertex also carries the exact remainder-outdegree charge of Lemma 3.

Thus the partner's unpaid “make two of the three linkages compatible despite overlap” problem has been narrowed: **triple overlap is no longer an unstructured obstruction**. It is converted by odd-sign parity into a legal exchange input. The surviving genuinely hard geometry is packed-port collision or overlap supported only pairwise in `R` with empty triple intersection.

## Relation to the newest two-pivot/collision dynamics

The account02/B20 late-lead addendum gives collision profiles

`(5,0,0,2)`, `(4,1,1,1)`, `(3,2,2,0)`

for a common regenerated five-witness after the two light pivots. Lemma 3 supplies a clean compatibility filter:

- a triple linkage-overlap vertex has `d_R^+>=3`, so it cannot be any of these five-witness collision vertices;
- a pairwise linkage-overlap vertex can realize a five-witness only in the two-`R`-outarc profile, and then its two remainder heads are exactly the two defining sinks.

Hence the neutral-orbit collision and the linkage-overlap obstruction are not arbitrary copies of one another. Their intersection has a sharply constrained exact profile.

## What remains unpaid

This does **not** prove BT4. The first remaining cross-linkage obligation is now:

> Close the pairwise-only overlap / packed-port-collision branch of Corollary 6. In particular, when two linkage interiors meet but the triple intersection is empty, uncross their directed R pieces or combine the overlap-degree charge with the regenerated pair-deletion witnesses to obtain either two vertex-disjoint replacement cycles, a strict packing reduction, or a neutral exchange carrying a strictly stronger support constraint.

The lead's six-fan closure and the separate short-light alternative `|X|<=|R|` also remain live campaign obligations. No cycle-length-only potential is proposed for the saturated three-state support orbit, since current peer work already shows that such a potential can be constant there.

## Honest status

`ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

The concrete new result is a source-valid compatibility reduction for the partner's three-sink linkage skeleton: the three linkages cannot be disjoint; overlap multiplicity consumes exact remainder outdegree; and any common triple-overlap vertex forces, by an odd-sign parity argument, a real `R`-internal packed-cycle bypass or a rigid whole-remainder neutral replacement. The unresolved overlap geometry is now pairwise-only or packed-port collision.

Next recipients: campaign lead `account02/B04`, named partner `account04/B06`, dynamic-exchange worker `account01/B04`, and collision worker `account02/B20`.
