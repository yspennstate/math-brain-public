# BT4 account02/B04 — equality completion and off-pivot witness regeneration

Run: `20260922T011943Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four vertex-disjoint genuinely directed cycles. Opposite arcs and hence digons are allowed in the target statement.

The current relaxation of Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 August 2026), explicitly leaves the genuinely directed Bermond--Thomassen conjecture unresolved for every `k>=4`. It proves at the same threshold `2k-1` only four vertex-disjoint cycles each of which is directed or becomes directed after reversing one arc. No near-directed cycle is promoted here to a directed cycle.

The lower-k inputs used are the Lichiardopol--Pór--Sereni 2009 results: minimum outdegree five gives three vertex-disjoint directed cycles, and more strongly a digraph in which all vertices have outdegree at least three except at most two vertices of outdegree two has two vertex-disjoint directed cycles.

The inherited lead state is account02/B04 report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72` plus correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`. I also use these exact completed OTHER-account results:

- named partner account03/B05, `BT4-TCEX-v2.1-linkage`, shared commit `5d6f5aca03679094f820de73cbd226a056a77499`, scientific segment blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`, linkage blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`, corrected Menger blob `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`;
- account01/B04 `BT4-MCR-v3-dynamic-deficit`, scientific commit `3396295d7e80542c72bb43ec86696795e4a70a23`, blob `f073bf10037d0c0961265275170680b13070b833`;
- account03/B04 `BT4-MENGER-COLLAR-v1`, scientific commit `1e497832eeeb2409499cbfb97f1bdba544686844`, blob `a11cd981b4d76eaeb6dd02b4820d16a740ee0057`;
- account01/B06 `BT4-REROUTE-v1-support-transfer`, scientific commit `119633c34a37481842cbc84e728e057c56c9cd11`, blob `0af4b6dbda55cf1126d73d0688744bb2ba4496d9`.

The named partner's exact theorem used below is its support-correct segment-bypass bound: for a cycle-supported witness `w` heavy on another packed cycle with fan `m`, an `R`-internal bypass of a proper support-cycle segment `S` has length at least `m+|S|-1`; equality is a size-neutral two-cycle exchange. Its corrected 3-connectivity trichotomy is also retained. I do not infer any target-level conclusion from the peer's `PASS`/outcome label.

## Inherited normal form

Assume for contradiction that BT4 is false. The inherited reductions allow work in an oriented spanning counterexample `D0` with:

1. every vertex of `D0` having outdegree exactly seven;
2. a globally minimum-total three-cycle packing `P=(C1,C2,C3)`;
3. acyclic nonempty remainder `R=V(D0)\setminus(V(C1)\cup V(C2)\cup V(C3))`;
4. each packed cycle chordless;
5. every arc dominated;
6. `D0` 3-vertex-strong.

The strengthened `k=2` input applies after deleting any two disjoint directed cycles. Hence for every packed pair either one residual vertex has outdegree at most one (a six-or-more cross-fan) or there are at least three distinct residual vertices of outdegree exactly two (five-cross-fans in the exact-seven normal form). This deficit statement regenerates after every size-neutral exchange because it is valid for every disjoint cycle pair, not just the initial packing.

For an `R`-internal path

`P: b=p0 -> p1 -> ... -> p_L=x`

from a packed cycle `C` to `x in R`, put `m=|N+(x) intersect V(C)|`. The repaired path-fan lemma gives

`L >= m-1`.

Every fan target other than possibly `b` lies among the first `L+1` forward successors of `b` on `C`.

## Lemma 1 — equality in the repaired path-fan bound always gives a neutral exchange

Assume `L=m-1`.

### Nonsaturated case `m<|C|`

If `x->b`, then `P+x->b` is a directed cycle on exactly

`L+1=m<|C|`

vertices. Its internal vertices lie in `R`, so replacing `C` by this cycle while keeping the other two packed cycles would strictly decrease the total size of the globally minimum packing. This is impossible. Therefore `x->b` is absent.

The repaired target restriction now leaves exactly `m=L+1` allowable fan targets, namely

`b+, b++, ..., b^(+m)`.

Since the fan has size `m`, all of them occur. Thus

`b -> p1 -> ... -> x -> b^(+m) -> ... -> b`

is a directed cycle of the same length as `C`: it replaces the `m-1` consecutive vertices

`F={b+, ..., b^(+(m-1))}`

by the `m-1` remainder vertices

`Q={p1,...,x}`.

So the new three-cycle packing is again globally minimum, and its remainder is

`R'=(R\Q) union F`.

Because a directed cycle in `R'` would be a fourth cycle disjoint from the three new packed cycles, `R'` is acyclic.

### Saturated case `m=|C|`

Now `x` sends an arc to every vertex of `C`, so in particular `x->b`. The cycle

`b -> p1 -> ... -> x -> b`

has `L+1=m=|C|` vertices. It is therefore itself a size-neutral replacement for `C`. It swaps the `m-1` vertices `C\{b}` with the `m-1` remainder vertices `Q={p1,...,x}`, and the new remainder is again acyclic.

### Consequence

The earlier equality caveat is narrower than previously recorded: the exceptional arc `x->b` blocks the *successor-block* exchange only in the saturated case, but in precisely that case it closes the path itself and gives a different neutral exchange. Therefore:

> **Equality-completion principle.** Every return path attaining the lower bound `L=m-1` yields an explicit globally minimum size-neutral packing exchange, with no extra `x->b` hypothesis.

This does not make equality contradictory. It makes equality actionable and puts both saturated and nonsaturated cases into the same finite neutral-exchange dynamics.

## Corollary 2 — the saturated heavy-triangle case joins the same exchange dynamics

In the global no-six branch, every sink of `D0[R]` has fan type `(3,2,2)` up to permutation. Let `x` be such a sink and `C` its unique heavy cycle, so `m=3`.

Account03/B04's corrected Menger argument gives three `C`-to-`x` paths pairwise vertex-disjoint except at `x`. If a path meets another packed cycle before `x`, there is a genuine cross-packed transition. Otherwise all three have internal vertices in `R`, and each has length at least two.

By Lemma 1, if any one has length exactly two, there is a neutral exchange, whether `|C|>3` or `|C|=3`. If no equality occurs, all three paths have length at least three. Their internal vertices are disjoint, so

`|R| >= 1 + 3*(3-1) = 7`.

Hence, without treating the saturated directed triangle as a separate unresolved exception,

> for a no-six sink, either there is a cross-packed transition, or there is a neutral minimum-packing exchange, or `|R|>=7`.

In particular, when `|R|<=6`, the old saturated-triangle branch cannot remain inert: it is forced into either cross-cycle geometry or the neutral-exchange graph.

## Lemma 3 — a no-six light pivot forces an off-pivot five-witness

This directly attacks the neutral two-state orbit that otherwise just flips a sink into a light support cycle and immediately flips it back.

Let `x` be a sink of `R` in the global no-six branch. Relabel so its fan triple is

`(a_A(x),a_B(x),a_C(x))=(3,2,2)`,

with `A` heavy. The inherited light-return lemma gives a direct return `b->x` from at least one light cycle; say `b in B`. The one-vertex exchange restriction and absence of digons force

`N+(x) intersect B = {b+,b++}`.

Perform the neutral light pivot

`B* = b -> x -> b++ -> ... -> b`.

It has the same length as `B`; its new remainder is

`R*=(R\{x}) union {b+}`,

which is acyclic. The other packed cycles remain `A,C`.

In the graph obtained by deleting `A union C`, the vertex `x`, now lying on `B*`, has exactly two residual outarcs:

- the support-cycle successor `x->b++`;
- the canonical remainder exit `x->b+`.

Its other five outarcs are the old `3+2` fan into `A union C`. Thus `x` is a cycle-supported five-witness for the pair `{A,C}`.

Now reapply the full strengthened `k=2` theorem to the **new** pair `{A,C}`.

- If the first branch appears, some residual vertex has outdegree at most one: a six-fan branch has been created, so the proof has left the persistent no-six regime.
- Otherwise there are at least three distinct residual degree-two vertices, i.e. at least three five-witnesses for `{A,C}`.

One of them is `x`. Since the set `{x,b+}` has only two vertices, at least one five-witness

`z notin {x,b+}`

must exist.

Therefore:

> **Off-pivot witness lemma.** A neutral light pivot in a persistent no-six state can never have the canonical reverse move as its only surviving obstruction. It either creates a six-fan immediately or regenerates a same-pair five-witness supported on a genuinely different vertex `z` outside the pivot pair `{x,b+}`.

The support of `z` is automatically safe under the corrected witness split. If `z in R*\{b+}`, it is an `R`-supported five-witness and the one-vertex/path-fan machinery is valid. If `z in B*\{x}`, chordlessness of the new globally minimum support cycle and residual degree two force exactly one support successor and one `R*` exit, so the named partner account03/B05 segment-bypass/linkage machinery applies without pretending that `z` lies in the remainder.

This is the promised substantive use of the named partner result: the pivot plus regenerated deficit theorem manufactures a fresh input to exactly the partner's support-correct dichotomy.

## What this removes from the first missing inference

Two previously live loopholes are now gone.

First, equality `L=m-1` no longer has an unresolved exceptional-arc subcase. Nonsaturation excludes `x->b` by strict packing minimality; saturation makes `x->b` itself close an equal-size replacement. Equality always moves to another globally minimum packing.

Second, in the no-six `(3,2,2)` sink regime, the most obvious closed orbit

`R-sink x  <->  cycle-supported x`

cannot be treated as the whole obstruction. After the light pivot, the strengthened `k=2` theorem forces either a six-fan or at least one off-pivot same-pair five-witness `z`.

What remains genuinely unpaid is a longer dynamic obstruction:

> Starting from the off-pivot witness `z`, combine its safe support type with account03/B05's segment-bypass/linkage trichotomy and the universal regenerated pair deficits to force a strict exchange, a cross-packed two-cycle splice, or a six-fan branch; equivalently, exclude a neutral exchange orbit of length at least three whose every state remains no-six and whose strict pure-`R` heavy collars all have length at least three.

The strict-collar alternative already carries a quantitative price: at every no-six sink where no cross transition and no equality exchange is used, `|R|>=7`.

## Complete conditional k=4 proof at the current frontier

The current argument is complete conditional on three explicit closure statements, with no hidden near-directed substitution:

1. **Six-fan closure.** Every exact six-cross witness (including the corrected third-cycle `6-cross/0-R-exit` form) yields a legal two-cycle splice or another strict contradiction.
2. **Cross-linkage closure.** The cross-packed transitions / segment-bypass outputs produced by the account03/B05 trichotomy can be paired to replace two packed cycles by two vertex-disjoint directed cycles, or else force a strict packing reduction.
3. **Long neutral-orbit closure.** In the persistent no-six branch, the off-pivot witness process above cannot form a neutral exchange cycle of length at least three while avoiding both 1 and 2 and maintaining all heavy pure-`R` collars strict.

Given these three statements, assume a minimum counterexample. Pair-deletion amplification puts each state into the six or no-six regime. Statement 1 closes the six regime. In no-six, every remainder sink is `(3,2,2)`; a light pivot is always available. Lemma 3 makes every such pivot produce either Statement 1 or a fresh off-pivot five-witness. The named partner's support-correct trichotomy handles every cycle-supported fresh witness, while the corrected path-fan machinery handles every `R`-supported one. Strict undercuts contradict global packing minimality; equality is converted by Lemma 1 into another globally minimum state and all deficits regenerate. Cross transitions close by Statement 2. If neither strict nor cross behavior occurs, only the long neutral/strict-collar dynamics of Statement 3 remains, which closes by assumption. This contradiction yields four disjoint directed cycles.

No one of statements 1--3 is claimed proved here; this is a conditional end-to-end proof with the first two equality/support loopholes removed.

## Failure checks and nonclaims

- The target permits digons, but the inherited minimum-counterexample argument eliminates them before the oriented normal form is used.
- A peer outcome label is not used as proof; exact statements and hypotheses above are the parts consumed.
- The new off-pivot lemma does **not** say the fresh witness is new globally, only that it is distinct from the two vertices of the current pivot.
- It does **not** exclude a neutral orbit of length three or more.
- The `|R|>=7` conclusion applies only to the pure-`R`, all-strict heavy-collar branch at a no-six sink; it is not a global lower bound in the presence of a cross transition or equality exchange.
- No edge-disjoint, near-directed, tournament-only, larger-degree, or finite-order substitute is used.
- No computational certificate is needed for the new lemmas.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The first missing inference has been narrowed from an equality exception plus arbitrary neutral flip to the genuinely global problem of exploiting an off-pivot regenerated witness (or closing the six/cross branches) and excluding neutral cycles of length at least three. Full BT4 is not proved.
