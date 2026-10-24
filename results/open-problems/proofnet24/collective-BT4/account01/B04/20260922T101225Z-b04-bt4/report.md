# BT4 account01/B04 — neutral heavy pivot forces common-exterior loss witnesses and a Q-supported CROSS/BYPASS

Run: `20260922T101225Z-b04-bt4`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-NEUTRAL-HEAVY-COMMON-EXTERIOR-LIFT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact target and status

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are permitted in the source statement, so directed digons count.

The source boundary remains the one recorded in the collective target file. Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`, proves the genuine k=3 input: minimum outdegree at least five forces three vertex-disjoint directed cycles. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:`2608.12948` (13 August 2026), does not prove BT4 because it allows one reversed arc per cycle. No nearly-directed object is counted here.

## 2. Exact inherited mathematics consumed

### Team lead account02/B04

Latest complete lead report read this run:

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The inherited normal form is a hypothetical oriented exact-outdegree-seven BT4 counterexample D, arc-dominated and 3-vertex-strong, with three disjoint directed cycles chosen lexicographically: first minimum total packed order, then maximum number of arcs induced by the acyclic remainder. Every packed cycle in a minimum packing is chordless. The lead's `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` shows that a genuine mixed cycle plus the k=3 deletion theorem and arc domination emits a genuine packed CROSS or a same-support BYPASS with the exact minimum-packing length tax. It also correctly leaves coalesced-port splice closure unpaid.

### Named OTHER-account result actually applied: account02/B05

I apply the complete account02/B05 result

`BT4-R4-F3-HEAVY-ENTRY-LIFT-OR-NEUTRAL-v1`,

run `20260922T092501Z-b05-bt4-f61322da`, report Git blob `9c1fdfc53762f5c7d7bf858f1963f031909f6aff`.

In the canonical four-remainder F3 second-collar branch, after the neutral U-exchange the packing is `(H,S*,C_z)` with acyclic remainder

`R_0 = Q union {t}`,  where `Q={q,a,c}` and `t=u^-`.

The partner eliminates an isolated heavy entry except for one exact equality case. In that case there are vertices `d,r,e` consecutive on H,

`d -> r -> e`,  with `r=d^+`, `e=d^{++}`,

and arcs

`d -> t`, `t -> r`, `t -> e`.

The heavy cycle has an exact size-neutral pivot

`H_0 := H`,

`H_1 := d -> t -> e -> H_0[e,d] -> d`.

Thus `V(H_1)=V(H_0)-{r}+{t}` and `|H_1|=|H_0|`. The new remainder is

`R_1 = Q union {r}`.

In a true BT4 counterexample both `R_0` and `R_1` are acyclic, and both `(H_0,S*,C_z)` and `(H_1,S*,C_z)` have globally minimum packed order. The partner left this neutral branch inside `BT4-R4-F3-CROSS-OR-DOUBLE-NEUTRAL-CLOSURE-v1`.

## 3. Compact conditional end-to-end route

Assume BT4 false and enter the inherited exact-seven oriented minimum-counterexample normal form. Run the established three-cycle packing reductions into the four-remainder F3 second-collar branch. Account02/B05 then yields either an already-useful CROSS, a clean opposite pair, or the exact heavy neutral pivot above.

The first two outputs feed the lead's common CROSS/BYPASS splice frontier. The only new issue is whether the neutral heavy pivot can remain an interface-free two-state orbit. The theorem below shows it cannot: each of the two neutral heavy cycles has a mandatory three-hit deletion witness outside the entire swapped pair, and that witness yields a CROSS or BYPASS whose remainder interior is confined to the same fixed three-vertex set Q. Hence the neutral heavy pivot is reduced to a much smaller common-core splice problem.

Full BT4 is still conditional on closing that splice together with the separate SIX, remaining F2/F3, generic port-coalescence, and larger-remainder branches.

## 4. Universal exact deletion/contraction loss

For a directed cycle C and a vertex v outside C, write

`a_C(v) := |N^+(v) intersect V(C)|`.

### Lemma 4.1 — every cycle has a three-hit exterior witness

In the inherited exact-outdegree-seven BT4 counterexample, every directed cycle C has some `v notin C` with

`a_C(v) >= 3`.

#### Proof

If every outside vertex hit C at most twice, then every vertex of `D-C` would have outdegree at least

`7-2=5`.

The genuine k=3 theorem of Lichiardopol--Pór--Sereni would then give three vertex-disjoint directed cycles in `D-C`; together with C these are four disjoint directed cycles, contradiction. QED.

### Exact loss accounting

Deletion gives, exactly,

`d^+_{D-C}(v) = 7-a_C(v)`.

Hence the witness of Lemma 4.1 has deletion degree at most four.

If C is contracted to one vertex and parallel quotient arcs are coalesced, then for every outside v

`d^+_{D/C}(v) = 7-a_C(v)+1_{a_C(v)>0}`.

For the same mandatory witness this is at most five. Therefore **no directed-cycle contraction in an exact-seven BT4 counterexample can preserve the degree-seven hypothesis globally**: every cycle has a concrete exterior vertex at which contraction loses at least two units. This is stronger than merely warning that contraction might lose degree.

The contracted cycle vertex itself has outdegree equal only to the number of distinct external heads of C, which is a second independent possible failure of the degree-seven induction hypothesis.

## 5. The neutral heavy pair has exact local hit bounds

Retain the account02/B05 neutral-pivot notation. Thus H0 contains

`d -> r -> e`,

while H1 contains

`d -> t -> e`,

and the graph also has `d->t`, `t->r`, `t->e`, `d->r`, `r->e`.

### Lemma 5.1

`N^+(t) intersect V(H_0) = {r,e}`.

#### Proof

The two displayed arcs show `{r,e}` is contained in the hit set. Let `h in H_0` be any other outneighbor of t. Since D is oriented and `d->t`, we have `h!=d`. If h is not r or e, its forward distance from d on H0 is at least three. Then

`d -> t -> h -> H_0[h,d] -> d`

replaces a forward H0 segment of at least three edges by two edges, producing a directed cycle strictly shorter than H0 while leaving `S*` and `C_z` untouched. This contradicts global minimum packed order. QED.

### Lemma 5.2

`N^+(r) intersect V(H_1) = {e}`.

#### Proof

The arc `r->e` survives. Since `d->r` and `t->r`, orientedness gives `r not->d` and `r not->t`. Any other H1-target lies forward from d at distance at least three, and the cycle

`d -> r -> h -> H_1[h,d] -> d`

would be strictly shorter than H1, again contradicting global minimum. QED.

Thus the swapped-out vertex t is only a two-hit vertex for H0, while the swapped-out vertex r is only a one-hit vertex for H1.

## 6. New theorem — `BT4-NEUTRAL-HEAVY-COMMON-EXTERIOR-LIFT-v1`

Let

`B := V(H_0) intersect V(H_1) = V(H_0)-{r} = V(H_1)-{t}`.

For each `i in {0,1}` there exists a three-hit witness `w_i` for `H_i` such that

`w_i in V(S*) union V(C_z) union Q`.

Moreover one can choose a hit `h_i in B` and obtain one of the following:

1. a direct packed CROSS from `S*` or `C_z` into the common heavy body B; or
2. a packed-to-packed directed path `J_i` ending at `h_i`, whose internal vertices lie entirely in the fixed three-vertex set Q, and which is either a CROSS or a distinct-port same-support BYPASS of H_i.

In the BYPASS case, if `ell_i` is the path length and `dist_{H_i}(c_i,h_i)` is the forward support distance from its packed source `c_i` to its target, then

`ell_i >= dist_{H_i}(c_i,h_i)`.

### Proof

Apply Lemma 4.1 to H0. It produces `w_0 outside H_0` with at least three H0-hits. Lemma 5.1 excludes `w_0=t`; in the partition belonging to `(H_0,S*,C_z)` this leaves

`w_0 in S* union C_z union Q`.

Among at least three distinct H0-targets choose

`h_0 notin {r,e}`.

Then `h_0 in B`. If `w_0` is packed, it lies on `S*` or `C_z`, so `w_0->h_0` is already a direct packed CROSS.

Suppose instead `w_0 in Q`. Repeatedly apply the inherited arc-domination property to the arc `w_0->h_0`: if a common predecessor is still in the current remainder, continue backwards while keeping the same target `h_0`. The process cannot cycle because `R_0=Q union {t}` is acyclic. Crucially it can never use t: Lemma 5.1 says t sends to H0 only at r and e, whereas `h_0` is neither. Therefore every remainder vertex in the domination ladder lies in Q. The first packed predecessor gives a path

`J_0 : c_0 -> ... -> w_0 -> h_0`

with all internal vertices in Q. If `c_0` is not on H0 this is a CROSS. If `c_0` lies on H0, it is a same-support BYPASS. Replacing the forward H0 segment from `c_0` to `h_0` by `J_0` would strictly reduce packed order if the path were shorter, so global minimum yields the stated length tax.

Now apply Lemma 4.1 to H1. A three-hit witness `w_1` exists outside H1. Lemma 5.2 excludes `w_1=r`, hence again

`w_1 in S* union C_z union Q`.

Choose one of its at least three H1-targets outside the two-point set `{t,e}`. Call it `h_1`; then `h_1 in B`. A packed witness gives a direct CROSS. For `w_1 in Q`, repeat domination toward `h_1`. The omitted vertex r cannot occur in the ladder because Lemma 5.2 says r hits H1 only at e and `h_1!=e`. Hence the entire remainder interior again lies in Q, and the same CROSS/BYPASS dichotomy and minimum-length tax follow. QED.

## 7. What this pays for

The account02/B05 neutral-heavy output is no longer an interface-free leaf. The two size-neutral heavy cycles H0 and H1 each force a deletion witness in the **same common exterior** `S* union C_z union Q`, and after choosing a target away from the two local collar vertices, any domination lift is confined to the **same fixed three-vertex acyclic core Q**. The swapped vertices t and r cannot carry the obligation and cannot appear inside these chosen domination ladders.

This materially strengthens the partner's first unpaid `CROSS-OR-DOUBLE-NEUTRAL` closure: a repeated neutral switch cannot merely alternate t and r while postponing all routing information. Each side of the neutral pair already emits a Q-supported CROSS/BYPASS object whose heavy target lies in the common heavy body.

It also gives an exact answer to the B04 deletion/contraction assignment in this branch. For both H0 and H1, a common-exterior witness has deletion degree at most four and contraction degree at most five. Thus the failure of induction after contraction is forced away from the swapped vertex itself; it is not an artifact of the neutral exchange.

## 8. First essential unpaid implication

`BT4-R4-F3-COMMON-Q-SPLICE-v1`:

> In the exact neutral-heavy-pivot state above, take the Q-supported CROSS/BYPASS objects supplied for H0 and H1. Their heavy targets lie in the common body B and their remainder interiors lie in the same three-vertex acyclic set Q. Prove that either one combines with the inherited `S* <-> C_z` interfaces to give two vertex-disjoint replacement directed cycles, or two same-support outputs can be selected compatibly; otherwise show that their forced intersection inside Q or their support-segment overlap yields a strictly smaller three-packing, a directed cycle in one exchanged remainder, SIX, or a fourth directed cycle.

The remaining issue is therefore a bounded common-core intersection/order problem, not an unconstrained repeated-neutral orbit.

## 9. Failure checks and nonclaims

- Lemma 4.1 uses the genuine k=3 theorem; it does not use the 2026 one-reversed-arc relaxation.
- A mandatory three-hit witness is not itself a fourth cycle.
- A CROSS is not counted as a replacement cycle until an actual disjoint splice is constructed.
- A same-support BYPASS may be size-neutral; only a strictly shorter one contradicts global minimum.
- The proof does not assert that the two Q-supported outputs are internally disjoint or support-compatible. That is exactly the remaining implication in Section 8.
- No finite computation was needed; no numerical experiment is promoted to proof.
- The theorem is conditional on the exact inherited neutral-pivot state from account02/B05; it does not close SIX, other F2/F3 states, generic four-port coalescence, or larger-remainder branches.

## 10. Honest outcome

`ESSENTIAL_STEP_APPLIED`.

A new universal cycle-loss lemma identifies the exact forced degree loss under both deletion and contraction. Applied to the named account02/B05 neutral-heavy pivot, the swapped vertices are too low-fan to serve as the required witnesses; both neutral cycles therefore force common-exterior three-hit witnesses. Choosing targets off the local collar makes the domination ladders avoid the swapped vertices completely and confines them to the common three-vertex core Q, yielding CROSS/BYPASS interfaces on both sides of the neutral pair. BT4 remains open.
