# B06 BT4 proof attempt — primitive-torus order obstruction

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Candidate result: `BT4-PRIMITIVE-TORUS-NO-CANONICAL-2SPLICE-v1`

## 1. Controlling inputs actually consumed

Campaign lead: account02/B04.

Latest complete lead finish consumed: `516cb1a3eb9e66d9b0835c1cf32068579e40744c`, whose mathematical delta is `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`: an aligned clean four-port heavy-triangle state emits either a genuine cross-packed transition or a distinct-port same-support remainder bypass. Its stated next debt is `BT4-FOUR-PORT-COALESCENCE-v1`.

Named OTHER-account live result/version consumed and applied: account02/B04 run `20260922T092109Z-b04-bt4-r11`, `primitive_torus_no_splice_check.py` at commit `64350e0e6a48089ba675c6d604135b9e089edfd3`, with output at `a20b6962be6005d323183d7bb19849b2aea7d55d`. The checker encodes the surviving coalescence order as a primitive monotone staircase on `Z_m x Z_n`; for every tested `3 <= m,n <= 7` it found zero canonical two-splices, even though many states have four distinct A-ports and four distinct B-ports (for example at `m=n=4`, 6 four-port states and 0 canonical two-splices).

The current lead run is newer than the latest finalized lead report, so the checker is treated as live mathematical evidence, not as a finalized theorem. The argument below proves its zero-splice phenomenon for all `m,n`, removing the finite-search limitation.

## 2. Compact conditional end-to-end argument

In the lead's globally minimum deficient three-cycle packing, the clean aligned four-port branch is reduced by `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` to either an already-recognized cross/bypass exit or the coalesced endpoint case. The natural hoped-for closure of the coalesced case was to use two plus-type and two minus-type port states on the primitive torus trace and pair them into two canonical directed splice cycles whose A-support segments and B-support segments are simultaneously vertex-disjoint.

The theorem below proves that this canonical closure mechanism is impossible on every primitive monotone torus trace, not merely absent in the current finite search. Consequently the remaining end-to-end proof must use extra graph structure not represented by the primitive trace alone: an endpoint-matched remainder path, an additional cross/third-support transition, SIX/R4, a cyclic exchanged remainder, or a noncanonical support replacement that changes the cyclic-order requirement.

## 3. Primitive staircase model

Let `w=w_0...w_{m+n-1}` be a cyclic word containing exactly `m` plus signs and `n` minus signs. Associate coordinates `c_t=(a_t,b_t) in Z_m x Z_n` exactly as in the lead checker: traversing a `+` step decreases the first coordinate by one and traversing a `-` step decreases the second coordinate by one, with the closing step identified cyclically. Thus one circuit has primitive winding `(-1,-1)`.

A plus-state is a coordinate `P=(i,j)` attached to a `+` occurrence; a minus-state is a coordinate `Q=(k,l)` attached to a `-` occurrence. For two plus states

`P_1=(i_1,j_1), P_2=(i_2,j_2)`

and two minus states

`Q_1=(k_1,l_1), Q_2=(k_2,l_2)`,

assume the four first coordinates `i_1,i_2,k_1,k_2` are pairwise distinct and the four second coordinates `j_1,j_2,l_1,l_2` are pairwise distinct. This is exactly the checker's four-distinct-port condition.

For a pairing of `P_r` with `Q_r`, the checker's canonical splice uses the positively oriented support arcs

`A[ k_r , i_r ]` and `B[ j_r , l_r ]`.

A canonical two-splice would require the two A-arcs to be vertex-disjoint and the two B-arcs to be vertex-disjoint.

## 4. Common cyclic-order lemma

**Lemma.** For any four selected staircase states whose first coordinates are pairwise distinct and whose second coordinates are pairwise distinct, the cyclic order of those four states induced by the positive first-coordinate orientation is identical to the cyclic order induced by the positive second-coordinate orientation.

**Proof.** List the four selected occurrences in their cyclic order along `w` as `s_1,s_2,s_3,s_4`. Let `alpha_r` be the number of plus steps in the cyclic word interval `(s_r,s_{r+1}]`, indices modulo four. Because the selected first coordinates are pairwise distinct, no `alpha_r` can be zero: if there were no plus step between two consecutive selected occurrences, their first coordinates would agree. Also `sum_r alpha_r=m`, because the four intervals partition one circuit. Hence from `s_r` to `s_{r+1}` the first coordinate decreases by the positive amount `alpha_r`, and all four points are encountered in the order `s_1,s_2,s_3,s_4` in the negative first-coordinate orientation. Equivalently their positive first-coordinate cyclic order is the reverse order.

Apply the same argument with `beta_r`, the number of minus steps in `(s_r,s_{r+1}]`. Pairwise distinct second coordinates imply every `beta_r>0`, and `sum_r beta_r=n`. Hence the positive second-coordinate cyclic order is also the reverse of `s_1,s_2,s_3,s_4`. The two positive coordinate orders are therefore identical. QED.

No functional/orientedness hypothesis is needed for this lemma beyond the primitive monotone word and pairwise-distinct coordinates. In particular it applies to every state admitted by the lead's stricter `valid_functional` test.

## 5. No-canonical-two-splice theorem

**Theorem (`BT4-PRIMITIVE-TORUS-NO-CANONICAL-2SPLICE-v1`).** In the primitive staircase model above, no pairing of two plus states with two minus states having four distinct A-ports and four distinct B-ports can produce two canonical splice cycles with simultaneously vertex-disjoint A-support segments and vertex-disjoint B-support segments.

**Proof.** Fix either pairing and relabel it `(P_1,Q_1),(P_2,Q_2)`.

On an oriented circle, two closed directed arcs `C[x_1,y_1]` and `C[x_2,y_2]` with four distinct endpoints can be vertex-disjoint only if the positive cyclic endpoint order is

`x_1, y_1, x_2, y_2`

up to cyclic rotation and exchange of labels 1 and 2.

Apply this to the A-support arcs `A[k_1,i_1]` and `A[k_2,i_2]`. Their disjointness would force the positive A-coordinate cyclic order of the four selected states to be

`Q_1, P_1, Q_2, P_2`.          (A)

Apply the same circle fact to the B-support arcs `B[j_1,l_1]` and `B[j_2,l_2]`. Their disjointness would force the positive B-coordinate cyclic order to be

`P_1, Q_1, P_2, Q_2`.          (B)

The cyclic orders (A) and (B) are different: starting (A) at `P_1` gives `P_1,Q_2,P_2,Q_1`, not `P_1,Q_1,P_2,Q_2`. But the common cyclic-order lemma says the positive A- and B-coordinate orders of these four states must be identical. Contradiction. QED.

The proof works for every `m,n` for which four distinct ports can exist. It therefore analytically explains all of the lead's finite zero-splice counts and shows that extending the same checker to larger support lengths cannot rescue the canonical two-splice mechanism.

## 6. Explicit source-valid local counterexample to the four-port => canonical-splice implication

A smallest clean example inside the lead's exact word model occurs at `m=n=4` with

`w = ++-+--+-`.

The checker recurrence gives the cyclic signed states

`+(0,0), +(3,0), -(3,3), +(2,3), -(2,2), -(2,1), +(1,1), -(1,0)`.

Choose

`P_1=(0,0), P_2=(1,1), Q_1=(3,3), Q_2=(2,2)`.

All four A-coordinates are distinct and all four B-coordinates are distinct. For the direct pairing, the A-arcs are `[3,0]={3,0}` and `[2,1]={2,3,0,1}`, so they intersect. For the crossed pairing, the A-arcs are `[2,0]={2,3,0}` and `[3,1]={3,0,1}`, so they also intersect. Hence four distinct ports do not imply a canonical two-splice.

This is a counterexample only to that local closure implication. It is not a counterexample to BT4, not a counterexample to the lead's witness-lift theorem, and not a claim that the full exact-seven digraph can realize no other rerouting.

## 7. Consequence for the campaign lead

The coalescence branch cannot be closed by the statement

`four distinct trace ports => two canonical disjoint support splices`.

That implication is false for structural order reasons, independently of support length. The endpoint-matched remainder path/direct terminal arc in the lead's stated `BT4-FOUR-PORT-COALESCENCE-v1` debt must therefore perform an actual order-breaking job: it must replace at least one canonical trace segment by a noncanonical directed route, introduce a usable endpoint/transition outside the primitive trace, or trigger a recognized exit (same-support bypass, third-support mediation, SIX/R4, cyclic exchanged remainder, strict packing decrease, or the fourth disjoint cycle).

A precise next lemma is:

`BT4-FOUR-PORT-ORDER-BREAK-v1`: in the coalesced clean four-port branch, combine the direct terminal cross with its endpoint-matched remainder path and exact-seven/no-SIX constraints to force either (i) a noncanonical rerouting whose A/B endpoint orders differ, permitting two vertex-disjoint directed replacement cycles, or (ii) one of the recognized exits above.

Any proof that uses only the primitive trace's four selected port states and the two canonical support-arc orientations is now ruled out.

## 8. Honest status

This is an essential negative/structural step, not the full Bermond-Thomassen k=4 proof. It converts a finite computational obstruction in the current lead run into a general theorem and identifies exactly what extra linkage structure the next proof step must exploit. The target remains `OPEN_NOT_PROVED`.

A fresh public-source check during this invocation also found the August 13, 2026 Bessy--Muis--Sereni--Steiner--Wiederrecht preprint still describing the original Bermond--Thomassen conjecture as unresolved for every `k>=4`; their theorem proves a near-directed relaxation, not BT4 itself.
