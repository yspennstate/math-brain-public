# BT4 account02/B06 — three-slot neutral orbit adversary and cross-pair synchronization repair

Run: `b06-20260922T022914Z-bab71a0db9f7`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Primary outcome: `ESSENTIAL_STEP_APPLIED`  
Subcandidate outcome: `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Source-exact scope and controls

Target: prove the k=4 Bermond--Thomassen statement that every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles; opposite arcs/digons are allowed and all finite orders are included.

Fresh control source for this invocation was `yspennstate/math-research-brain` main commit
`63a7439240d9e98245277ac7ef03772949485b3b`, OWNER CONTROL revision `2026-09-22.2`.
The open-problems allocation supersedes the older installation/benchmark duties for B06.

Lead source consumed in full:
- account02/B04 run `20260922T011943Z-b04-bt4-r11`,
  `yspennstate/math-open-problems` commit
  `ca30763c69284b71c197ba0f49e37962f07e30c3`,
  report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`,
  candidate: equality completion plus off-pivot witness regeneration.

Named OTHER-account partner consumed in full and applied:
- account03/B04 run `20260922T011921Z-account03-B04-BT4-r12`,
  candidate `BT4-MENGER-COLLAR-v1`,
  `yspennstate/math-open-problems` commit
  `1e497832eeeb2409499cbfb97f1bdba544686844`,
  report blob `a11cd981b4d76eaeb6dd02b4820d16a740ee0057`.

Also used as a current compatible invariant statement:
- account04/B04 shared candidate `BT4-G1-WITNESS-INVARIANT-v1`,
  handoff blob `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`.

The exact graph below is reused from the preceding B06 sharp common-head certificate only as an
authenticated adjacency source:
- prior report commit `dcec1e0e1551da600b121c5a2e633212441526ce`,
  report blob `45711c01c403e84db6e8912d61ae7afcfc2aa029`,
  checker blob `9657654120fb10552cbe049f337a4afc175b7067`.
The orbit property proved here was not part of that prior certificate.

No authenticated brain retrieval/context was used.

## Conditional end-to-end frontier inherited from the lead

Assume a counterexample is reduced to the inherited oriented exact-outdegree-seven normal form:
a globally minimum-total three-cycle packing, acyclic remainder, chordless packed cycles,
every arc dominated, and 3-vertex-strongness. Pair deletion supplies the exact six/no-six deficit
dichotomy in every packing state. The lead closes every equality case of the repaired path-fan
bound by a neutral globally minimum exchange, and a neutral light pivot regenerates an off-pivot
degree-two witness for the unchanged deleted pair. The first genuinely global unpaid step is to
exclude a neutral exchange orbit of length at least three (or force it into six-fan/cross-splice
machinery).

The partner account03/B04 result is the heavy-witness amplifier used below: for a remainder vertex
heavy on a packed cycle, 3-vertex-strongness gives three return channels; either one hits another
packed cycle, or all three are pure-remainder collars. In the nonsaturated case the collars obey
the strengthened length pattern, while the lead's equality-completion principle makes any tight
case a neutral exchange even at saturation.

This run attacks exactly the first length-three neutral-orbit obstruction.

## False intermediate statement

A tempting strengthening of the lead's off-pivot lemma is:

> **BT4-FRESH-WITNESS-TERMINATION-v1 (false).**  
> Fix the deleted pair `A,C`. If every neutral pivot on the third packed cycle regenerates a
> degree-two witness outside the two vertices of the current pivot, then repeatedly pivoting to
> a fresh same-pair witness cannot return to the original globally minimum packing after three
> or more states.

This is false even under almost all of the local minimum-counterexample geometry.

## Exact adversary: a three-state fresh-witness neutral orbit

Use the 16-vertex exact-seven oriented graph recorded in `bt4_three_slot_orbit_checker.py`.
It has 112 arcs, every vertex has outdegree exactly seven, it remains strongly connected after
deletion of any at most two vertices, every arc is dominated, and it contains the two fixed
directed triangles

`C1=(A0,A1,A2)` and `C2=(B0,B1,B2)`.

Delete `C1 union C2` and call the residual digraph `Gamma`. Its exact residual-degree-two set is

`W={Z0,Z1,Z2}`.

For each `i in {0,1,2}` define

`Q_i = R0 -> R2 -> Z_i -> R0`.

Each `Q_i` is a directed triangle. The packing

`P_i=(C1,C2,Q_i)`

uses nine vertices, hence is globally minimum-total because the graph is oriented and every
directed cycle has length at least three. Its seven-vertex remainder is acyclic.

Now observe the one-slot neutral exchange

`Q_i -> Q_(i+1)`:

the common directed edge is `R0->R2`; the old slot vertex `Z_i` is freed; the new remainder
vertex `Z_(i+1)` is inserted using the two arcs

`R2 -> Z_(i+1) -> R0`.

Thus this is exactly a same-size one-vertex support pivot. In state `P_i`, the two other vertices
of `W` lie in the remainder and remain exact degree-two witnesses for the fixed deleted pair
`C1,C2`. Choosing the next one as the fresh off-pivot witness gives

`P_0 -> P_1 -> P_2 -> P_0`.

So a fresh off-pivot same-pair witness exists at every step and yet a genuine length-three neutral
orbit occurs. The orbit is not an artifact of a weak graph: exact seven, orientation,
3-vertex-strongness, arc domination, globally minimum triangle packings, and acyclic remainders all
hold simultaneously.

The graph is not a BT4 counterexample. The checker exhibits four vertex-disjoint directed cycles,
and, more pointedly for the repair below, every cross-pair residual used in the orbit already
contains two disjoint directed cycles. Therefore the missing ingredient is precisely the *other*
pair-deletion constraints, not another same-pair freshness argument.

This refutes `BT4-FRESH-WITNESS-TERMINATION-v1`.

## Repair lemma: cross-pair synchronization for a three-slot orbit

Here is the correct statement that a genuine counterexample must satisfy.

### Lemma (BT4-3SLOT-SYNC-v1)

Work in the inherited exact-outdegree-seven counterexample normal form. Let `A,C` be fixed disjoint
packed cycles. Suppose there are three globally minimum packing states

`P_i=(A,B_i,C)`, `i=0,1,2`,

forming a one-slot neutral orbit. Thus there is a three-element slot set
`X={x0,x1,x2}` such that `B_i` contains exactly `x_i` from `X`, while
`X\{x_i}` lies in the acyclic remainder `R_i`.

For `T in {A,C}`, let

`H_(i,T) = D - (V(B_i) union V(T))`.

Then, for every state `i` and each `T`, one of the following holds:

1. `H_(i,T)` has a vertex of residual outdegree at most one (the six-or-more cross-fan branch); or
2. `H_(i,T)` has at least three residual-degree-two vertices, and at least one of them lies outside
   the slot set `X`.

Consequently, if all six cross-pair checks (three states times two choices of `T`) stay in no-six,
every state has a genuine **off-slot** five-witness for each cross pair. Same-pair cycling on `X`
cannot be the whole obstruction.

#### Proof

If `H_(i,T)` has no vertex of residual outdegree at most one and has at most two vertices of
residual outdegree two, then every vertex has outdegree at least three except at most two vertices
of outdegree two. The known strengthened `k=2` Bermond--Thomassen theorem used by the lead then
gives two vertex-disjoint directed cycles in `H_(i,T)`. Together with the deleted disjoint cycles
`B_i` and `T`, these are four disjoint directed cycles in `D`, contradiction.

Hence persistent no-six forces at least three degree-two vertices. But `x_i` is deleted as part of
`B_i`, so `H_(i,T)` contains only the other two slot vertices from `X`. At least one of the three
degree-two witnesses is therefore outside `X`. QED.

### Corollary (common off-slot witness is automatically heavy on the moving support)

Fix state `i` and suppose it is no-six for both cross pairs. Let

`U_A = {v notin X : d^+_(D-(A union B_i))(v)=2}`,
`U_C = {v notin X : d^+_(D-(C union B_i))(v)=2}`.

Both sets are nonempty by the lemma. If they intersect, choose `w in U_A intersect U_C`.
Then `w` lies in the actual remainder `R_i`: it must survive both deletions, so it is on none of
`A,B_i,C`.

Put

`a=|N+(w) intersect A|`,
`b=|N+(w) intersect B_i|`,
`c=|N+(w) intersect C|`,
`r=|N+(w) intersect R_i|`.

The two degree-two equalities are

`c+r=2` and `a+r=2`.

Since `d+(w)=7` exactly,

`a=c=2-r`, `b=3+r`, with `r in {0,1,2}`.

Thus the only possible fan patterns are

- `r=0`: `(a,b,c;r)=(2,3,2;0)`;
- `r=1`: `(1,4,1;1)`;
- `r=2`: `(0,5,0;2)`.

In every case `w` is a remainder-supported heavy witness on the moving support `B_i`, with fan
`m=b>=3`. This is a direct input to the named partner account03/B04 Menger-collar theorem:
three `B_i`-to-`w` return channels exist; either a channel hits another packed cycle, or all three
are pure-remainder collars subject to the partner's length bounds. The lead's equality-completion
principle handles a tight collar even when `m=|B_i|`.

In particular, if the moving support `B_i` is a triangle, then `b<=3`, so necessarily

`r=0`, `(a,b,c)=(2,3,2)`.

Hence a common off-slot witness in a triangle slot orbit is exactly a remainder **sink** with
fan type `(2,3,2)`, i.e. the familiar no-six heavy-sink geometry, now regenerated by
cross-pair synchronization rather than assumed.

If `U_A` and `U_C` are disjoint, the state instead contains two distinct off-slot exact five-witnesses,
one for each cross pair. That is a genuine two-witness branch; it cannot be represented by the
three slot vertices alone.

This proves the advertised repair: a three-state neutral orbit is not forbidden by same-pair
freshness, but in a genuine counterexample it must continually create either a six branch, a
partner-compatible common heavy remainder witness, or two distinct off-slot cross-pair witnesses.

## Why the exact adversary is source-valid and where it fails

For the local three-state orbit above, the fixed-pair witness set really is invariant:
`W={Z0,Z1,Z2}`. However the two cross-pair audits fail the repaired lemma's counterexample
precondition exactly because the graph already has two disjoint cycles in each audited residual.

For example, in state `Q_0=(R0,R2,Z0)`:

- after deleting `C1 union Q_0`, the residual has minimum outdegree three and contains
  `(B0,R1,R4)` and `(B1,B2,R5)` as two disjoint directed triangles;
- after deleting `C2 union Q_0`, it contains
  `(A0,A1,Z1)` and `(A2,R1,R5)` as two disjoint directed triangles.

The checker records analogous certificates for all three states. This makes the repair exact:
the local orbit is not dismissed merely because the graph happens to contain a four-pack somewhere;
the precise pair-deletion theorem that a true counterexample must satisfy already detects it.

The orbit also shows why the current account04/B04 invariant `W` is necessary but not sufficient:
`W` can be perfectly invariant and still support a length-three neutral cycle. The next proof step
must exploit the other pair systems.

## New digon boundary adversary

A second tempting reduction is also false:

> “Contract a digon to one vertex, suppress duplicate arcs, and continue at minimum outdegree seven.”

Take the complete bidirected digraph on eight vertices. It is a legal target digraph and every
vertex has outdegree seven. Contract any digon and suppress duplicate ordered arcs to return to a
simple digraph. The result is the complete bidirected digraph on seven vertices, whose minimum
outdegree is six, not seven.

So contraction does not preserve the threshold either. The correct digon reduction remains the one
proved in the preceding B06 run: delete the two vertices of the digon, leaving minimum outdegree at
least five; apply the proved `k=3` theorem to obtain three disjoint cycles in the remainder; add the
digon as the fourth. This example prevents contraction from being substituted silently for that
argument.

## First essential missing implication after this run

The lead's generic “long neutral orbit” gap is now split more sharply for the first possible
three-state one-slot orbit.

At each state, audit the two changing cross pairs:

- a six branch exits the persistent no-six orbit immediately;
- an intersecting pair of off-slot witness sets produces an exact heavy remainder witness on the
  moving support and therefore re-enters account03/B04's Menger-collar / lead equality-exchange
  machinery;
- disjoint off-slot witness sets produce two different cross-pair witnesses.

The first unpaid implication is therefore:

> **Disjoint cross-pair witness closure.**  
> In a three-state one-slot neutral orbit, if every state remains no-six and the two off-slot
> cross-pair witness sets are disjoint, use the six distinct state/pair witness incidences plus
> support/remainder typing to force a strict exchange, a cross-packed two-cycle splice, or a
> common heavy witness at a later state.

This is strictly narrower than “fresh witnesses should terminate” and cannot be refuted by the
three-slot exact adversary, because that adversary fails the cross-pair deficit audit with explicit
two-cycle certificates.

For longer orbits or multi-slot exchanges, the same cross-pair audit remains mandatory, but the
simple cardinality argument “three witnesses versus only two surviving slot vertices” is specific
to the three-slot case and is not promoted beyond its hypotheses.

## Computation and exact output

`bt4_three_slot_orbit_checker.py` is a deterministic standard-library verifier. It revalidates:
exact outdegree seven, orientation, 3-vertex-strongness, arc domination, the invariant fixed-pair
witness set `W`, all three globally minimum triangle states, acyclic remainders, every neutral
pivot, fresh off-pivot witnesses, the exact three-state return, cross-pair residual degree tables,
explicit two-disjoint-cycle certificates for each cross-pair residual, the known explicit four-pack,
and the bidirected-`K8` digon-contraction boundary.

Native execution in this invocation returned `PASS`.

Checker bytes: `7611`  
Checker SHA-256: `35fdd77104503c453c3f9304e2aa123a21e66e63dc65b0306dc900f5cd1aabaf`

Output bytes: `6193`  
Output SHA-256: `c2c3c797ebae6faf79fceb1a9f417591ffcdc796e4f227314b36573bb34e6171`

No target-level proof, novelty claim, near-directed substitution, edge-disjoint substitute,
larger-threshold result, finite-order closure, peer-PASS truth promotion, or verified-brain claim is
made.

## Honest status

`ESSENTIAL_STEP_APPLIED`, with `CANDIDATE_REFUTED` for
`BT4-FRESH-WITNESS-TERMINATION-v1`.

The target remains open.
