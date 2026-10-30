# Correction / strengthening — BT4 fleet02/B04 20260922T022208Z

This addendum is controlling for the report `report.md` created at commit `99c1f5c0ddb596d7bd3b1910bb59be58d94f30cc`.

## Quarantined sentence

The primary report correctly constructed an `R`-internal singleton bypass from the branch `A not-> z`, but then incorrectly invoked the fleet03/B05 marked-segment inequality on that bypass. The partner inequality assumes an incoming heavy-cycle arc `b->z` with `b in A`; that hypothesis is absent precisely in the branch `A not->z`.

Therefore the claims

`ell >= m`

and, in the strict case, `ell >= m+1`

for that specifically constructed branch-1 bypass are **not authorized** by the partner theorem and are quarantined. The bypass existence itself remains correct, but only the one-cycle minimum-packing bound is available from it without an `A` inarc.

A stronger valid argument eliminates the branch entirely into a cross-packed transition, so no weakened bypass estimate is needed.

## Corrected lemma — heavy-fan domination escape

Work in the inherited oriented exact-outdegree-seven minimum-counterexample normal form with globally minimum packing `(A,B,C)`, acyclic remainder `R`, chordless packed cycles, and every arc dominated.

Let `z in B` be any cycle-supported witness heavy on `A`; in particular

`N+(z) intersect A` is nonempty.

Assume

`A not-> z`.

Pick any `a in N+(z) intersect A`, so `z->a`. Dominate this **heavy-fan arc**. There is a vertex `q0` with

`q0->z` and `q0->a`.

Because `A not->z`, `q0 notin A`.

If `q0 in C`, then `q0->a` is already a genuine `C`-to-`A` cross-packed arc.

If `q0 in B`, chordlessness of `B` forces `q0=z^-`, hence `z^-->a` is a genuine `B`-to-`A` cross-packed arc.

It remains to consider `q0 in R`. Repeatedly dominate the arc `qi->z`: choose `q(i+1)` with

`q(i+1)->qi` and `q(i+1)->z`

as long as `qi in R`.

No remainder vertex can repeat: a repetition would give a directed cycle along the chain inside `R`. Since `R` is finite, the process reaches a first `qt notin R`. The terminal vertex still satisfies `qt->z`, so `qt notin A`. If `qt in C`, then

`qt -> q(t-1) -> ... -> q0 -> a`

is an `R`-internal `C`-to-`A` cross-packed transition. If `qt in B`, chordlessness forces `qt=z^-`, and

`z^- -> q(t-1) -> ... -> q0 -> a`

is an `R`-internal `B`-to-`A` cross-packed transition.

Thus:

> **Heavy-fan domination escape.** If a cycle-supported witness `z` is heavy on packed cycle `A` but receives no arc from `A`, then a genuine cross-packed transition exists, with all internal vertices in `R`.

This proof uses the same domination-ladder mechanism already validated elsewhere in the BT4 programme, but applies it to a heavy-fan arc `z->a`, not to the support arc `z->z+`.

## Correct null-free partner trichotomy

For a cycle-supported five-witness `z in B` heavy on `A` with fan `m>=3`, fleet03/B05's corrected trichotomy plus the new lemma gives:

1. a genuine cross-packed transition (this now includes the old branch `A not->z`);
2. or `A->z` and an `R`-internal bypass of a proper segment `S` of `B` containing `z`, in which case the partner hypotheses are satisfied and
   `ell >= m+|S|-1`, with equality a size-neutral two-cycle exchange;
3. or `A->z` and the partner's two internally vertex-disjoint `z^-`-to-`z+` paths in `D-z`, both entering `A union C` internally.

So in any state in which cross-packed transitions are excluded, **every cycle-supported heavy witness necessarily has a genuine heavy-cycle inport**, and every subsequent use of the TCEX inequality is hypothesis-correct.

## Further exact consequence for the live G1-S branch

Consume fleet04/B04 `BT4-G1-WITNESS-INVARIANT-v1`: in `G1-S` there are at least three cycle-supported fixed-pair five-witnesses on one complementary support cycle, and two witnesses `z1,z2` share the same heavy target `A`.

If no cross-packed transition is already available, the corrected lemma forces heavy inports

`p1->z1`, `p2->z2`

with `p1,p2 in A`.

For `i=1,2`, choose any fan target `ai in N+(zi) intersect A`. The directed cycle

`Ki = pi -> zi -> ai -> A[ai,pi]`

has vertex set `{zi} union V(A[ai,pi])`.

If the two forward `A`-segments `A[a1,p1]` and `A[a2,p2]` are vertex-disjoint, then `K1,K2,C` are three vertex-disjoint directed cycles. Moreover

`|K1|+|K2|+|C| <= |A|+2+|C| < |A|+|B|+|C|`

because the oriented packed cycle `B` has order at least three. This contradicts global minimum of the three-cycle packing.

Therefore:

> **Two-witness interval collision.** In a no-cross `G1-S` state, for the two same-heavy witnesses, every pair of fan-return segments `A[a1,p1]`, `A[a2,p2]` intersects. In particular, if `p1!=p2`, their respective shortest fan-return segments intersect; otherwise the two witnesses share a heavy inport.

This turns the remaining `G1-S` obstruction into a rigid same-heavy collision geometry: either a common heavy inport, or overlapping shortest return intervals, plus the fleet03/B05 bypass/double-linkage outputs.

## Updated blocker and status

The local `A not->z` null branch is genuinely closed, but not by the invalid TCEX invocation in the primary report. It is closed by a cross-packed transition from the heavy-fan domination ladder.

The remaining blocker is global: in the no-cross branch the same-heavy witnesses have actual heavy inports and pairwise interval collision, yet their marked bypasses / two-path linkages can still coalesce. One must turn this rigid collision geometry into a legal two-cycle splice, a strict minimum-packing reduction, a directed cycle in an exchanged remainder, or a six-fan.

Outcome remains `ESSENTIAL_STEP_APPLIED`. No full BT4 proof is claimed.
