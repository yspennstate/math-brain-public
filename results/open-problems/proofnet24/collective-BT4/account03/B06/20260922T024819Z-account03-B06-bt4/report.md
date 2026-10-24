# BT4 account03/B06 — G1 port-spacing / one-sided fan corridor

Run: `20260922T024819Z-account03-B06-bt4`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Candidate: `BT4-G1-PORT-SPACING-v1`
Outcome: `ESSENTIAL_STEP_APPLIED` with a local `CANDIDATE_REFUTED`
Brain status: `WITHOUT_VERIFIED_BRAIN`
Parent target: `OPEN_NOT_PROVED`

## Exact target and source boundary

The target is the exact k=4 Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a digon counts as a directed cycle.

The current source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 Aug 2026): it leaves the exact k>=4 conjecture open and proves only the one-reversed-arc relaxation.

## Exact team input consumed

Assigned OTHER-account partner: `account04/B04`, `BT4-G1-WITNESS-INVARIANT-v1`, shared blob `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`, canonical science blob `df42a0c3455fe3fb14f71351067f41fac75afb27`.

That result gives, in the exact-outdegree-seven globally minimum three-cycle normal form and persistent NO-SIX, the G1 neutral pivot and the exact G1-S branch: the unchanged opposite-pair degree-two set `W` is wholly on the short light support `B*`, `|W|>=3`, every `w in W` has exactly one exit to the new acyclic remainder, and two witnesses share a heavy target.

I also use the controlling lead correction `account02/B04`, shared blob `efc49c4d0177e30caf791b471ff9a9becb2c060b`: in a no-cross state every cycle-supported heavy witness has an inport from its heavy target cycle. The correction also identifies the resulting intersecting return-segment obstruction. No peer outcome label is used as a theorem.

## New universal lemma: one-sided fan corridor

Work in G1-S after the neutral pivot. Let `A` be one of the two opposite packed cycles and let distinct support witnesses `z1,z2 in B*` both be heavy on `A`. Put

`Fi = N+(zi) intersect A`,  `mi=|Fi|>=3`.

Assume the no-cross branch, so choose heavy-cycle inports `pi in A` with `pi->zi`. If `p1=p2` we are in the common-port branch. Suppose `p1!=p2`.

For a target `a in Fi`, write `A[a,pi]` for the forward directed A-segment from `a` to `pi`.

### Lemma 1: every pair of fan-return segments intersects

For all `a1 in F1` and `a2 in F2`,

`A[a1,p1] intersect A[a2,p2] != empty`.

Proof. If two such segments were vertex-disjoint, then

`K1 = p1 -> z1 -> a1 -> A[a1,p1]`
and
`K2 = p2 -> z2 -> a2 -> A[a2,p2]`

would be vertex-disjoint directed cycles, also disjoint from the untouched third packed cycle `C`. Their A-parts together use at most `|A|` vertices and they add only the two support vertices `z1,z2`. Since G1-S has at least three distinct witnesses on `B*`, `|B*|>=3`. Thus `(K1,K2,C)` covers at most `|A|+2+|C|`, strictly fewer than the globally minimum old packing `|A|+|B*|+|C|`. Contradiction.

### Lemma 2: cyclic interval equivalence

Let `P=(p1,p2)_A` and `Q=(p2,p1)_A` be the two open directed arcs. For `a in F1`, `b in F2`,

`A[a,p1]` and `A[b,p2]` are disjoint
iff
`a in Q` and `b in P`.

Indeed, in that case the two return segments lie on the two complementary closed sides and share neither endpoint. Conversely, if `a notin Q`, then `A[a,p1]` wraps through `p2`, so it meets every segment ending at `p2`; if `b notin P`, the second segment wraps through `p1`.

Combining Lemmas 1 and 2 gives the exact corridor alternative

`F1 subseteq (p1,p2]_A`
or
`F2 subseteq (p2,p1]_A`.                                      (C)

Consequently, with `d_A` denoting forward cycle distance,

`d_A(p1,p2) >= m1`
or
`d_A(p2,p1) >= m2`.                                            (S)

This is the new `BT4-G1-PORT-SPACING-v1` reduction. It converts the lead's qualitative interval-overlap obstruction into a one-sided fan confinement and a discrete port-spacing inequality.

Two immediate exact corollaries:
- in the no-cross branch `|A|>=mi+1>=4`, because orientation forbids `zi->pi`;
- if `|A|=4` and `mi=3`, distinct inports of two same-heavy witnesses cannot be opposite: opposite ports have both directed gaps two, violating (S). Thus they are common or adjacent.

## Sharpness: common-port strengthening is false

The tempting strengthening “two same-heavy G1-S witnesses must share a heavy inport” is false at the pure cycle-order level. On a directed 4-cycle take `p1=0`, `p2=1`, `F1={1,2,3}`, `F2={0,2,3}`. Every return segment for witness 1 meets every return segment for witness 2, yet `p1!=p2`.

More generally, whenever `d_A(p1,p2)>=m1`, choosing `F1` inside `(p1,p2]` forces every first return segment to contain `p2`, so the all-cross condition holds regardless of the second fan. Thus (C)/(S) is sharp without additional remainder/linkage information.

## Exact full-digraph constrained certificate

A fresh exact MILP constrained search found a 20-vertex oriented digraph with every vertex of outdegree exactly seven. Take `H=(0,1,2,3)`, `B=(4,5,6,7)`, `C=(8,9,10,11)`, `R={12,...,19}`, sink `x=19`, port `b=4`.

The exact checker verifies: all outdegrees seven; no loops or digons; H,B,C directed chordless; R acyclic; x is an R-sink with fan `(3,2,2)`; H,C have no return to x and B has unique port `4->19`; every arc is dominated; the graph is 3-vertex-strong; every packed-pair residual cross-fan is at most five; and the exact five-witness sets are HB `{8,9,19}`, HC `{6,7,19}`, BC `{0,1,2,14}`. After the canonical pivot `B*=(4,19,6,7)`, HC has `W={6,7,19}` wholly on `B*` and `W intersect R*=empty`, so this is an exact local G1-S realization.

It is deliberately NOT a BT4 counterexample. The new remainder contains the directed triangle `(5,13,17)`, giving the explicit four-cycle packing

`(0,1,2,3)`, `(8,9,10,11)`, `(4,19,6,7)`, `(5,13,17)`.

The same certificate exposes the port-spacing mechanism. Witnesses 6 and 7 are both heavy on C. Witness 6 has C-fan `{8,9,10}` and C-inport 11; witness 7 has C-fan `{8,10,11}` and C-inport 9. The return segments `C[10,11]={10,11}` and `C[8,9]={8,9}` are disjoint, producing the strict smaller three-packing `(11,6,10)`, `(9,7,8)`, `(0,1,2,3)` of total size 10 instead of 12.

Thus the search identifies the two global filters a genuine counterexample must satisfy: global minimum forbids disjoint return intervals, and post-pivot remainder acyclicity forbids the displayed fourth cycle.

## Exact computation and write boundary

The native checker returned success and exhaustively checked 542,530 heavy-fan cyclic configurations for cycle orders 4 through 8 and fan sizes 3 through 5 where available, with zero mismatches in the interval equivalence. The all-order proof is above.

Checker SHA-256: `5f941c6ea44133f24a0555244f3e28d9241b73d9dde4d038ba053a27d14f0d70`.
Output SHA-256: `b840eb93127668738c4fdd987f1c7cf8b30755cc751dad2e863732a4735a3e49`.

The checker/output upload itself was blocked by the platform safety layer. I did not retry that denied payload through another encoding, path, tool, or identity. Those hashes identify local current-run evidence only unless later materialized through an authorized path.

## First unpaid implication

G1-S is now split into cross transition, common heavy inport, or the ordered port-corridor branch (C)/(S). The first remaining implication is `BT4-G1-CORRIDOR-CLOSURE-v1`: combine the confined pair's unique remainder exits with the support-correct TCEX/linkage machinery to force a short/equality two-cycle bypass, forbidden inversion after a neutral exchange, a cross-packed splice, or a six-fan. Pure witness counting or interval overlap is certified insufficient.

No full BT4 proof or counterexample is claimed.
