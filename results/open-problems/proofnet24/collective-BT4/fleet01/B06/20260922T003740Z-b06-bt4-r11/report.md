# BT4 fleet01/B06 — support-transfer rerouting and the no-six sink core

Run: `20260922T003740Z-b06-bt4-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Candidate: `BT4-REROUTE-v1-support-transfer`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and assignment

The target is the `k=4` Bermond–Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement and a digon counts as a directed cycle. The present worker is assigned directed rerouting/linkage lemmas for the deficient packing chosen by the BT4 lead; nothing below substitutes edge-disjoint cycles or the recent one-reversed-arc relaxation.

The current source boundary used by the team is Bessy–Muis–Sereni–Steiner–Wiederrecht, arXiv:2608.12948 (13 August 2026): the exact directed conjecture remains unresolved for `k>=4`, while their theorem at the `2k-1` threshold allows a cycle made directed by reversing one arc.

## Exact peer state consumed

The lead snapshot actually consumed is fleet02/B04, run `20260922T001806Z-b04-bt4-a1ceeb3c`:

- main report commit `a95b20d733b75b91a40c16c2faa225846f54973e`, blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`;
- correction/addendum commit `a0d5649a60d02bf6289208d581d979102e31d227`, blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`.

I also applied the later compatible fleet03/B06 tight-port snapshot, scientific commit `4e204703776c90319afc67c4a03d56d474272d9c`, report blob `81a20ff15088e74009551fffd8e9f4812b781819`, and the fleet03/B05 segment-bypass handoff, scientific commit `adaaeb54de01856eb5e865104f59ee1a7119f299`, report blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`.

The inherited sound normal form is the following. Work in an exact-outdegree-seven oriented counterexample carrying a globally minimum-total three-cycle packing `(C1,C2,C3)` with DAG remainder `R`. The cycles are chordless. Every remainder sink `x` has fan numbers

`m_i(x)=|N+(x) intersect V(C_i)|`, with `m_1+m_2+m_3=7`.

Every sink has a direct return from a light packed cycle: for some `C_l` there is `b in C_l` with `b->x` and `m_l<=2`; moreover the one-vertex minimum-packing exchange gives

`N+(x) intersect C_l subset {b+,b++}`.

For every deleted pair `{C_i,C_j}`, the strengthened `k=2` theorem gives the exact dichotomy: either a surviving vertex has pair fan at least six, or at least three surviving vertices have pair fan exactly five. A five-witness on the complementary packed cycle `C_k` has, by chordlessness and exact outdegree seven, precisely its cycle successor plus one unique `R`-exit outside `C_i union C_j`.

The lead's first unpaid implication is to turn these amplified pair witnesses into a strict return/legal exchange, or in the complementary-cycle saturation branch into a genuine two-cycle splice. The fleet03/B04 correction forbids treating a cycle-supported witness as if it were already in `R`.

## 1. The global no-six branch forces every sink to be `(3,2,2)`

Call a packing in the **global no-six branch** when, for each pair of packed cycles, no vertex surviving that pair deletion has pair fan at least six. Then every pair is necessarily in the three-five-witness alternative.

**Lemma 1 (sink normal form in the no-six branch).** Every sink `x` of `R` has fan triple `(3,2,2)` up to permutation. In particular it has a unique heavy cycle, of fan three, and two light cycles, each of fan two.

**Proof.** For each `k`, the sink `x` survives deletion of the other two cycles. No-six gives

`m_i+m_j <= 5`,

hence, because the three fans sum to seven, `m_k>=2`. Thus all three fans are at least two and sum to seven, so they are exactly `3,2,2`. QED.

Consequently the lead's direct light return in this branch always has fan **exactly two**. If `b->x` is such a return from `C_l`, then

`N+(x) intersect C_l = {b+,b++}`.                                      (1)

This equality is the key rerouting coordinate below.

## 2. Neutral sink pivot and exact support flip

**Lemma 2 (neutral light pivot).** Let `x` be a sink in the global no-six branch and let `b->x` be a direct return from a light cycle `C_l`. Replace the segment

`b -> b+ -> b++`

of `C_l` by

`b -> x -> b++`.

The resulting directed cycle `C_l^x` has exactly `|C_l|` vertices. Together with the other two packed cycles it is again a globally minimum-total three-cycle packing, and the new remainder

`R_x = (R minus {x}) union {b+}`

is acyclic.

**Proof.** Equation (1) supplies `x->b++`, so the displayed replacement is genuinely directed. It removes exactly `b+` from the old cycle and inserts exactly `x`; therefore total packing size is unchanged. If `R_x` contained a directed cycle, that cycle plus `C_l^x` and the other two packed cycles would be four vertex-disjoint directed cycles, contrary to the counterexample assumption. QED.

Now fix the pair formed by the two cycles other than `C_l`. Before the pivot, `x` has pair fan five because `m_l=2`. After the pivot, `x` lies on the complementary cycle `C_l^x`; its successor there is `b++`, while its second old outneighbor on `C_l`, namely `b+`, has moved to the remainder. Thus:

**Corollary 3 (R-sink witness to cycle witness).** The neutral pivot turns the `R`-supported sink five-witness `x` into a complementary-cycle-supported five-witness for the **same pair**, with the exact unique remainder exit

`x -> b+`.

Moreover its predecessor/successor on the new cycle have the canonical two-edge remainder bypass

`b -> b+ -> b++`.                                                       (2)

This is a genuine directed support flip; no edge-disjoint surrogate is used.

## 3. Two-step bypass transposition: cycle witness back into `R`

The reverse mechanism does not require that the bypass vertex be the witness's own unique exit.

**Lemma 4 (two-step bypass transposition).** Let `w` be a cycle-supported five-witness for the pair `{C_i,C_j}`, lying on the complementary packed cycle `C_k`. Write `w-` and `w+` for its predecessor and successor on `C_k`. Suppose there exists `q in R` with

`w- -> q -> w+`.                                                        (3)

Then replacing `w` by `q` on `C_k` gives a directed cycle `C_k'` of the same length and another globally minimum-total three-cycle packing. The new remainder

`R'=(R minus {q}) union {w}`

is acyclic, and `w` is now an **R-supported five-witness for the same pair `{C_i,C_j}`**.

If `r` is the unique old `R`-exit of `w`, then in `R'` the new vertex `w` has `R'`-outdegree zero when `q=r`, and `R'`-outdegree one when `q!=r`.

**Proof.** The bypass (3) replaces the two cycle arcs `w-->w->w+` by the two arcs `w-->q->w+`, swapping one cycle vertex for one remainder vertex. Hence the cycle length and total packing size are unchanged. A directed cycle in `R'` would be a fourth cycle disjoint from the three packed cycles, so `R'` is acyclic.

The five arcs from `w` into `C_i union C_j` are untouched by the swap. In the old packing, exact residual outdegree two after deleting `C_i,C_j` consists of the cycle-successor `w+` and the unique remainder exit `r`. In the new packing `w+` remains on the complementary cycle. If `r=q`, that second residual head has also moved onto the complementary cycle; otherwise `r` remains in the new remainder. Thus `w` is in `R'`, keeps pair fan five, and has new remainder outdegree respectively zero or one. QED.

The case `q=r` is exactly inverse to Lemma 2/Corollary 3: the new `R`-vertex `w` is a sink with complement fan two. Therefore a cycle-supported five-witness admitting a two-step predecessor-to-successor bypass is **not an irreducible third-cycle obstruction**; it can be moved into the all-`R` witness side by a neutral directed rerouting.

Equivalently, after declining this legal transfer, the genuinely hard cycle-supported five-witness branch may be assumed to satisfy the local bypass-free condition

`N_R^+(w-) intersect N_R^-(w+) = emptyset`.                            (4)

This condition is strictly sharper than merely saying that the witness has one `R` exit. It is also exactly aligned with the fleet01/B05/fleet03-B05 predecessor-to-successor bypass mechanism: their longer bypass inequalities now need only attack the branch in which the decisive length-two transfer (3) is absent.

## 4. Applying the lead's canonical collar: pair-witness transfer map

Let `z in C_k` be a cycle-supported five-witness for the pair `{C_i,C_j}`. By the lead correction it has a unique exit `z->r` into `R`. Follow a directed path in the finite DAG from `r` to a sink `x`. Let `C_l` be a direct light-return cycle into `x` supplied by the lead.

In the global no-six branch Lemma 1 gives `m_l(x)=2`; therefore `x` is itself an `R`-supported five-witness for the pair complementary to `C_l`.

This yields the exact transfer rule on the triangle of packed-cycle pairs:

- if `l=k`, then `x` is an `R`-supported five-witness for the **same pair `{C_i,C_j}`** as `z`;
- if `l=i`, then `x` is an `R`-supported five-witness for `{C_j,C_k}`;
- if `l=j`, then `x` is an `R`-supported five-witness for `{C_i,C_k}`.

Thus a third-cycle five-witness always exports a genuine `R` witness after following its unique exit to a sink; the only question is whether the pair label is preserved or rotates to an adjacent pair.

There is also a directed linkage interpretation in the rotating case. If `l!=k`, apply the neutral pivot of Lemma 2 on `C_l`. The collar path

`z -> r -> ... -> x`

then becomes a directed path from `C_k` to the pivoted cycle `C_l^x`, internally disjoint from all three packed cycles: its internal vertices remain in `R_x`, and its endpoint `x` has moved onto `C_l^x`. Hence the rotating transfer produces a concrete cross-cycle linkage, not only a count.

No reciprocal linkage is asserted here; obtaining a compatible return without destroying disjointness remains part of the two-cycle-splice obligation.

## 5. Sink-incidence count: a four-sink remainder already yields a clean three-witness pair

For a sink `x` in the no-six branch, let `h(x)` be its unique heavy cycle. Let `s_t` be the number of sinks with heavy cycle `C_t`.

**Lemma 5 (sink witness incidence).** The number of sinks that are five-witnesses for pair `{C_i,C_j}` is exactly

`s_i+s_j`.

**Proof.** A sink is a five-witness for `{C_i,C_j}` exactly when the complementary fan `m_k` equals two. Under the `(3,2,2)` normal form this is equivalent to saying that the unique heavy cycle is `C_i` or `C_j`. QED.

**Corollary 6.** If `R` has at least four sinks, then some pair of packed cycles has at least three **distinct sink-supported five-witnesses in `R`**. Conversely, if no pair has three sink-supported witnesses, then `R` has at most three sinks; and if it has exactly three, the heavy labels are exactly one sink of each type.

**Proof.** If all three pair counts were at most two, then

`(s_1+s_2)+(s_1+s_3)+(s_2+s_3) <= 6`,

so `2(s_1+s_2+s_3)<=6`. Thus there are at most three sinks. Equality with three sinks and every pair count at most two forces `(s_1,s_2,s_3)=(1,1,1)`. QED.

Therefore the global no-six branch has a new clean split: with at least four sinks, one pair already supplies the full three-five-witness alternative using only `R`-sinks; the genuinely sink-sparse residual has at most three sinks, with the three-sink extremal case carrying one heavy label of each color.

## 6. Updated conditional end-to-end route

The lead's source-valid chain now reads as follows.

1. Reduce to the exact-seven oriented counterexample with a globally minimum three-cycle packing and DAG remainder.
2. For every pair deletion use the exact `one six-fan OR three five-fans` dichotomy.
3. In the six-fan/U1 branch use the fleet03/B06 tight-port, neutral-exchange and inversion constraints; that branch remains unpaid.
4. In the global no-six branch every sink is `(3,2,2)` (Lemma 1).
5. A cycle-supported five-witness with a two-step `R` bypass is transferred, by Lemma 4, into an `R`-supported five-witness for the same pair. Hence a hard third-cycle witness must satisfy the explicit bypass-free condition (4).
6. Independently, following any cycle witness's unique exit to a sink gives the exact pair-transfer map of Section 4. Same-support return gives an `R` witness for the same pair; rotating return gives an actual directed cross-cycle linkage after the neutral pivot.
7. If the remainder has at least four sinks, Corollary 6 supplies a pair with three distinct sink-supported witnesses. If not, the hard no-six core has at most three sinks.

The first essential missing implication is therefore narrower than the lead's earlier generic “two-cycle splice” request:

> **BT4-REROUTE-v1 residual.** In the global no-six branch, either force a two-step predecessor-to-successor `R` bypass (3) for one of the required cycle-supported five-witnesses, thereby transferring it into `R`; or, assuming all such witnesses satisfy the bypass-free condition (4) and the remainder has at most three sinks, use the three five-witnesses together with the existing missing-arc saturation/forced-exit certificates to construct two vertex-disjoint directed reroutings that yield the required splice.

This residual is source-valid and support-correct. It does not treat a third-cycle witness as a remainder witness without an explicit neutral rerouting, and it does not infer a directed cycle from the one-reversed-arc relaxation.

## Status

`ESSENTIAL_STEP_APPLIED`, not a full proof. The new proved contributions are the exact neutral witness-support flip, the general two-step bypass transposition, the pair-label transfer through the lead's sink collar, and the sink-incidence reduction to a <=3-sink hard core in the global no-six branch. Full BT4 remains open on the current evidence.

Next recipients: BT4 lead `fleet02/B04`, exchange workers B05, and the B06 linkage/search workers. The most direct next attack is the bypass-free <=3-sink residual above; the six-fan/U1 branch should remain separate rather than be hidden inside the no-six argument.
