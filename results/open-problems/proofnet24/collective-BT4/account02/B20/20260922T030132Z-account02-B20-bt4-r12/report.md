# account02/B20 BT4 report — aligned ladder–ray exchange tax

Run: `20260922T030132Z-account02-B20-bt4-r12`  
Classification: **ESSENTIAL_STEP_APPLIED**  
BT4 target status: **OPEN**; no full proof candidate is claimed.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Exact target and sources consumed

Target: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons are allowed and all orders are included.

Fresh campaign lead consumed: account02/B04, `proofnet24/collective-BT4/account02/B04/20260922T022208Z-b04-bt4-r11/report.md`, blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`. Its conditional end-to-end skeleton reduces a hypothetical counterexample to a globally minimum three-cycle packing `(A,B,C)` with acyclic remainder `R`, then needs three universal closures: exact-six (`H6`), cross-linkage (`HX`), and strict-collar/neutral-orbit (`HS`).

Named OTHER-account partner consumed: account04/B06, `proofnet24/collective-BT4/account04/B06/20260922T021002Z-b06-bt4-r12/report.md` (`BT4-SIX-DUAL-COLLAR-v1`). In its `C4` exact-six branch, a cycle-supported exact-six witness `z in B` has two incoming support-entry ladders through `R`; if `H5` fails, `p=z^-` has at least two `R` exits, each yielding an outgoing ray to packed support. A ray returning to `B` at forward distance `d>=2` has length `ell>=d`, with equality the neutral case and strict inequality a collar. If an incoming ladder reaches an outgoing ray inside `R`, the partner splice gives a cross transition/support bypass/closed-cycle outcome.

Newest compatible OTHER-account refinement also consumed: account03/B05, `proofnet24/collective-BT4/account03/B05/20260922T024158Z-b05-bt4-r11/report.md`. It eliminates the partner's residual dual-reachability wall: 3-vertex strong connectivity through `D-{p,z}` forces either a genuine cross transition or a proper strict support bypass. I therefore do **not** count wall elimination as new work here.

## Conditional end-to-end argument and first unpaid implication

Conditional on `H6+HX+HS`, the lead's minimum-packing deficit alternative closes every fixed pair deletion: a six-fan is discharged by `H6`; otherwise regenerated five-witnesses and their cross-linkages are discharged by `HX`, while neutral exchanges/strict collars terminate under `HS`. That contradicts existence of a BT4 counterexample.

After the account03/B05 wall elimination, the first unpaid universal implication is the **splice/coalescence step** in the exact-six `C4` branch: every transition/strict-bypass/collar output must force either a strict reduction of the globally minimum three-cycle packing or four vertex-disjoint directed cycles, uniformly over all ladder apices, target distributions, ray returns, overlaps in `R`, digons, and arbitrary cycle lengths.

The new step below gives an exact quantitative exchange law whenever a support-entry ladder is target-aligned with a returning collar. It converts one part of the qualitative `H6/HX/HS` interface into a numerical obligation.

## New lemma: aligned ladder–ray exchange tax

Work in a hypothetical BT4 counterexample in the lead's globally minimum three-cycle packing `(A,B,C)`, with acyclic remainder `R`. Let `z in B` be an exact-six cycle-supported witness in the partner's `C4` branch and set `p=z^-` on the directed cycle `B`.

Let

`L: s=l_0 -> l_1 -> ... -> l_lambda=z`

be one incoming ladder, where `s` lies on one packed cycle `X in {A,C}` and every internal ladder vertex `l_1,...,l_{lambda-1}` lies in `R`. Let `a in N^+(z) cap V(X)` and let

`d_X = dist_X(a,s)`

be the number of directed `X`-edges on the forward segment `X[a,s]`.

Let

`P: p=r_0 -> r_1 -> ... -> r_ell=t`

be one outgoing ray whose internal vertices lie in `R` and whose terminal vertex `t` lies on `B`. Write

`d_B = dist_B(p,t) >= 2`.

Then:

**Lemma.** If the internal `R`-vertex sets of `L` and `P` are disjoint, then

`ell - d_B >= |X| - d_X - lambda - 1`.          (1)

Here cycle size and directed segment length are counted in edges (equivalently vertices for a directed cycle).

### Proof

The ladder, fan arc, and target return segment form the genuine directed cycle

`C_X = L + (z->a) + X[a,s]`,

with

`|C_X| = lambda + 1 + d_X`.

The outgoing ray and complementary support segment form the genuine directed cycle

`C_B = P + B[t,p]`,

with

`|C_B| = ell + |B| - d_B`.

Because `d_B>=2` and `p=z^-`, the forward skipped segment `B[p,t]` contains `z` as an internal vertex. Hence the complementary segment `B[t,p]`, and therefore `C_B`, avoids `z`. By hypothesis the `R` interiors of `L` and `P` are disjoint. Thus `C_X` and `C_B` are vertex-disjoint. They are also disjoint from the third packed cycle `Y={A,C}\{X}`.

Therefore `(C_X,C_B,Y)` is another triple of pairwise vertex-disjoint genuine directed cycles. Global minimality of `|A|+|B|+|C|` gives

`(lambda+1+d_X) + (ell+|B|-d_B) + |Y| >= |X|+|B|+|Y|`.

Rearranging is exactly (1). QED.

No orientation reversal, edge-disjoint substitution, or relaxed-cycle theorem is used.

## Universal local fork produced by the lemma

For every partner `C4` incoming-ladder / `B`-return-ray pair:

1. If their `R` interiors meet, the partner splice mechanism applies and produces a cross-transition/support-bypass/closed-cycle output.
2. If they are `R`-disjoint and the ladder apex `s` lies on a packed support `X` that receives at least one fan arc from `z`, inequality (1) applies. Choosing `a` to minimize `d_X(a,s)` gives the strongest compulsory collar excess:

   `ell-d_B >= max_{a in N^+(z) cap X} (|X|-dist_X(a,s)-lambda-1)`.

3. If a ladder apex is `p=z^-`, that ladder itself is a strict `B`-bypass replacing the single support edge `p->z`: it has at least one internal `R` vertex, so its length is at least two.
4. If a support apex `s in X` is not target-aligned, i.e. `N^+(z) cap X` is empty, then all six exact fan arcs lie on the other packed support cycle. This isolates the concentrated exact-six subbranch rather than hiding it inside the wall case.

Thus the former `C4` wall is sharpened to: **splice output, quantitative collar tax, immediate strict support bypass, or a six-on-one-support concentration.**

## What this does and does not move

**FULL_TARGET_CHANGE:** `NONE`. BT4 remains open and no unrestricted Bermond-Thomassen conclusion is claimed.

**MECHANISM_CHANGE:** yes. The previous B20 runs localized neutral/collision cages and reserved exits. This run switches to a two-cycle exchange comparison and derives a quantitative tax from global minimum packing. It is not another restatement of the same collision funnel.

**ESSENTIAL_STEP_APPLIED:** the aligned ladder–ray subcase of the exact-six splice problem now has a proved numerical exchange constraint; partner wall outputs are no longer merely qualitative in this subcase.

The tax alone is not yet a contradiction because strict collars may be arbitrarily longer than their skipped support segments and distinct rays may merge in `R`. Therefore it is not a full `H6`, `HX`, or `HS` proof.

## First remaining implication, with quantifiers

Prove the following universal coalescence statement in the same source model:

> For every hypothetical finite loopless simple digraph `D` with `delta^+(D)>=7` and no four vertex-disjoint directed cycles, every globally minimum three-cycle packing `(A,B,C)` and every partner `C4` exact-six witness `z`, the finite family of incoming ladders and outgoing rays satisfying the fork above necessarily yields either (i) a strict smaller three-cycle packing, or (ii) four pairwise vertex-disjoint genuine directed cycles.

It is enough to show that the quantitative taxes from all target-aligned disjoint ladder/ray pairs cannot all be paid simultaneously once one also accounts for (a) the two distinct first `R` exits from `p`, (b) account03/B05's forced switch when a ladder can reach a ray, and (c) account01/B06's transverse gate-escape strict bypass. The unresolved difficulty is nonreuse: rays can merge in `R`, and strict excess cannot simply be summed without a disjointness/charging theorem.

## Next method

Build a **nonreuse/merge dichotomy** for the two partner rays. If their `R` tails are disjoint, charge (1) simultaneously against the target complements and combine with the transverse gate bypass. If they merge, use the first merge vertex and 3-vertex connectivity to force a new packed-support escape before the merge or a second strict bypass. This attacks the exact missing resource-sharing issue rather than another local fan count.

## Stagnation check

Last three B20 substantive mechanisms were: neutral-equality/triple-dominator localization; two-pivot/collision funnel with reserved exits; and the present two-cycle exchange tax. The method changed materially in this run, so the three-unchanged-run pivot trigger is not active.

## Safety/provenance

No brain installation or benchmark work was performed. No benchmark gold, credentials, scheduler identifiers, machine paths, raw private transcript, email, Drive, public post, paid model/API/Codex, remote workflow, permission change, or other-account authentication was used. Existing peer artifacts were read only and not overwritten.
