# BT4 account03/B06 — five-alternation obstruction in the triangular R3 pivot orbit

**Run:** `20260922T091836Z-b06-bt4-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Candidate:** `BT4-F3-R3-TRI-ALT5-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target status:** `OPEN_NOT_PROVED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and assignment

The target is the `k=4` Bermond–Thomassen statement in the exact collective scope: every finite loopless digraph with at most one arc per ordered pair, minimum outdegree at least seven, and digons allowed contains four pairwise vertex-disjoint genuinely directed cycles.

The account03/B06 role is exact constrained search and symbolic-family testing of the decisive BT4 lemma, retaining the original directed-cycle packing information. The named other-account partner is `account04/B04`.

The active owner control remains revision `2026-09-22.2`; no later stop was present at the pre-write control recheck. Old brain-installation/benchmark work remains superseded.

## 2. Named other-account result actually consumed

I read the newest canonical `account04/B04` scientific report available at the start of this run:

`proofnet24/collective-BT4/account04/B04/20260922T081403Z-a04-b04-bt4-r11/report.md`

Git blob `ba316d20d5fb068a75f817435e329ea1b4212b47`.

Its theorem is

`BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1`.

I use the following exact content from it.

We are in the inherited oriented, exact-outdegree-seven, arc-dominated, 3-vertex-strong minimal-counterexample normal form with a globally minimum three-cycle packing and an acyclic remainder. In the surviving residual-three F3 defect-one pivot orbit, a tight pivot on a light support replaces the successor of its unique return port by the current remainder sink and frees that successor into the remainder. The sink fan has type `(3,2,2)`. A newly freed successor has two packed in-neighbors on the pivoted support and therefore cannot be a later remainder sink while that support remains unchanged.

The partner proves that if the first two pivots use different light supports and the third pivot repeats one of them, then either an already-recognized exit occurs (SIX, cyclic remainder/fourth cycle, or exact R4 compression) or the repeated support has order exactly three. Consequently an alternating block `A,B,A,B` that survives forces both light supports `A,B` to be directed triangles, because tight pivots preserve support order.

The partner leaves the no-exit orbit split into a monochromatic same-support mechanism and a triangular mixed mechanism. The present run attacks the latter.

## 3. Compact conditional route and first missing implication

The inherited F3-R3 route is now:

1. use the minimal-counterexample normal form and NO-SIX reductions to reach the defect-one residual-three pivot orbit;
2. use `BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1` to show that any genuine support switch either exits or triangularizes the support that is repeated;
3. close the resulting triangular mixed orbit;
4. separately close the same-support/monochromatic token-exchange orbit, then merge with the team’s other SIX/R4/F2 branches.

The first missing implication in step 3 was that a triangular mixed orbit should not be able to alternate indefinitely. The tempting four-pivot version is too strong at the local symbolic level; the repaired five-pivot statement below is exact.

## 4. New theorem — `BT4-F3-R3-TRI-ALT5-v1`

### Statement

Consider a surviving defect-one residual-three F3 pivot orbit under the inherited oriented exact-seven normal form. Suppose five consecutive tight pivots use two persistent non-heavy-return supports in strict alternation

`A, B, A, B, A`

(or symmetrically `B,A,B,A,B`).

Then before the fifth successor state can remain in the same surviving F3 orbit, one of the recognized exits has already occurred. More explicitly, after applying the partner triangularization theorem:

- either the arcs forced by those pivots contain three vertex-disjoint directed triangles in the nine vertices `A union B union R`, which together with the untouched third packed cycle give four vertex-disjoint directed cycles in the original digraph; or
- the only remaining local states have next-sink fan profile `(3,1,3)` across `(H,A,B)`, not a permutation of `(3,2,2)`, so they are not F3 successor states.

Therefore **no five consecutive strictly alternating pivots survive**.

### Consequence

The partner’s TRI leaf is reduced to a same-support event: after both light supports have triangularized, every no-exit continuation must contain two consecutive pivots on the same support within at most five pivot positions. Thus the persistent R3 orbit is no longer split into an indefinitely alternating TRI mechanism versus MONO. Both are funneled into the same next debt: a same-support triangular token-exchange doublet/run.

## 5. Why the finite state model is source-valid

After an alternating block `A,B,A,B`, the partner theorem implies that both `A` and `B` have order three. Pivoting preserves order, so throughout any putative five-pivot alternating block both are triangles.

Fix the untouched third packed support as `H`. The relevant universe outside `H` contains exactly nine vertices:

- three vertices of the current `A` triangle;
- three vertices of the current `B` triangle;
- the three-vertex remainder.

For any remainder sink `s`, the F3 fan profile is a permutation of `(3,2,2)` across `H,A,B`, and `s` has no outneighbor in the current remainder. The pivoted support is a light support, so it contributes exactly two outneighbors of `s`. Put

`h(s)=|N+(s) intersect H|`.

Because `H` is untouched during the five-pivot block and the graph itself is fixed, `h(s)` is fixed whenever the same token reappears as a sink. There are only two possibilities:

- `h(s)=3`: `H` is heavy, so `s` has exactly two outneighbors in each of `A,B`;
- `h(s)=2`: `H` is light, so the nonpivoted one of `A,B` is heavy and all three of its vertices are outneighbors of `s`.

Exact outdegree seven now fixes the sink’s entire local outneighbor set among the nine vertices: it has size four in the first case and five in the second. This set is immutable when the token later reappears.

A tight pivot at port `p` of a directed triangle `(p,p+,p++)` with sink `s` forces

`p -> s`, `s -> p+`, `s -> p++`,

replaces `p+` by `s`, and frees `p+`. Orientation forbids every reverse arc of a forced arc. The current sink has no arcs to the other two remainder vertices. The inherited one-inport lemma eliminates any branch in which an already-forced second vertex of one support enters the same sink.

These are exactly the constraints encoded by `checker.py`. The code is deliberately conservative: it does **not** invent extra forbidden in-arcs when the inherited hypotheses do not force them. Thus it over-approximates possible original digraphs. If no five-pivot survivor exists in this larger symbolic state space, none exists in the actual branch.

Finally, because the inherited branch is oriented, any three vertex-disjoint directed cycles among these nine vertices must each have order three and therefore form a partition into three directed triangles. Such a partition, together with the untouched packed cycle `H`, is an actual four-cycle packing in the original digraph.

## 6. Exact enumeration

By rotation of the first triangular support, take the first pivot port to be `a0`. Let the initial remainder sink be `r0`. Its two old co-remainder vertices are symmetric before the first pivot; the checker nevertheless runs both mirror choices for the next sink (`r1` and `r2`) and obtains identical counts.

For each sink occurrence the checker branches over every source-valid heavy identity encoded by `h(s) in {2,3}`, every allowed target set on the nonpivoted triangle, every port, and every possible next remainder sink. It deduplicates exact labelled symbolic states but performs no random sampling.

For either mirror choice the exact counts are:

| pivot step | support | candidates | already force three local triangles | nonpack symbolic survivors |
|---:|:---:|---:|---:|---:|
| 1 | A | 4 | 0 | 4 |
| 2 | B | 48 | 0 | 48 |
| 3 | A | 384 | 0 | 384 |
| 4 | B | 768 | 576 | 192 |
| 5 | A | 216 | 213 | 3 |

The final three nonpack symbolic states are isomorphic up to rotation of the initial `B` triangle. In all three, the next remainder sink has fixed fan profile

`(|N+(s) intersect H|, |N+(s) intersect A|, |N+(s) intersect B|) = (3,1,3)`.

That is not a permutation of `(3,2,2)`, so none is a surviving F3 successor state. Hence the number of valid five-alternation survivors is exactly zero in the symbolic over-approximation.

The mirror choice of the other initial co-remainder sink gives the same `4,48,384,768,216` candidate history and the same `0,0,0,576,213` three-pack eliminations.

## 7. Failure of the stronger four-pivot shortcut and its repair

The stronger local forcing claim

> every surviving triangular `A,B,A,B` block already forces a four-pack

is false as a consequence of the encoded local axioms alone. After four pivots the exact enumerator still has 192 labelled nonpack symbolic states. This is **not** asserted to be 192 full BT4 counterexamples; they are local states consistent with all constraints used in the proposed shortcut.

The fifth pivot is the decisive extra information. Of its 216 exact continuations, 213 force three local triangles and the remaining three destroy the F3 `(3,2,2)` fan profile. Thus the correct universal statement is the five-pivot obstruction, not the four-pivot shortcut.

A representative fifth-step four-pack mechanism in one branch consists of the three forced local triangles

`(a0,r0,a2)`, `(b0,a1,b2)`, `(b1,r1,r2)`

on the nine local vertices. They are disjoint; adjoining the untouched packed support `H` gives the fourth directed cycle. Other branches are handled by the exact enumeration rather than by assuming this one representative pattern.

## 8. Exact artifacts

The immutable exact checker is

`proofnet24/collective-BT4/account03/B06/20260922T091836Z-b06-bt4-r11/checker.py`.

Its Git blob after readback is `6de2fe2ffaff4bb3374f17f84b0496cf0e5a16b7`.

The recorded exact output is

`proofnet24/collective-BT4/account03/B06/20260922T091836Z-b06-bt4-r11/checker_output.json`.

The output records all five step counts, the three fifth-step nonpack exceptions, their `(3,1,3)` profiles, and the zero surviving-state conclusion. The checker contains assertions for both mirror remainder choices.

No finite graph census and no finite graph-order cutoff is being used to infer BT4. This is an exhaustive finite state proof of one bounded structural implication after the partner theorem has reduced the support orders to three.

## 9. Next exact obligation

The next candidate is

`BT4-F3-R3-SAME-SUPPORT-DOUBLET-CLOSE-v1`.

In a no-exit defect-one R3 orbit, combine:

1. the partner fresh-successor block and one-inport property;
2. the present theorem, which prevents five alternating pivots;
3. the fact that an unchanged support preserves its blocked fresh successor;
4. exact-seven `(3,2,2)` fan accounting and global minimum packing;

and close a pair of consecutive pivots on the same triangular support. The desired output is a strict smaller three-packing, a cyclic exchanged remainder/fourth cycle, SIX/R4, or a source-valid cross/bypass into an already-covered branch.

This is genuinely narrower than the partner’s `MONO-or-TRIANGLE` debt: an indefinitely alternating triangular orbit is eliminated. The surviving mechanism must pay for a same-support run.

Separate SIX, F2, larger-remainder and lead-specific heavy-triangle debts remain open.

## 10. Status

`BT4-F3-R3-TRI-ALT5-v1` is an `ESSENTIAL_STEP_APPLIED` conditional structural theorem inside the inherited F3-R3 branch. It is not a proof of BT4. BT4 remains **OPEN / NOT PROVED**.
