# BT4 account01/B05 — integration with latest lead equality/off-pivot state

Run: `20260922T012616Z-b05-bt4-r11`  
Candidate extension: `BT4-DOUBLE-HEAVY-LINK-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

This note consumes the later campaign-lead handoff account02/B04 `20260922T011943Z-b04-bt4-r11`, candidate “equality completion and off-pivot witness regeneration,” after the primary B05 report was written. That lead result proves that every equality case is a legal neutral minimum-packing exchange, including the saturated case, and that a neutral light pivot regenerates an off-pivot five-witness. The argument below applies those conclusions to the saturated total-coalescence triangle and extracts a simultaneous two-witness interface.

## 1. Pairwise exposure, stronger than one-at-a-time exposure

Use the notation of the primary report. We are in the direct saturated total-coalescence branch with packed cycles `A,B,C`,

`C=(z0,z1,z2)`,

all three `zi` exact five-fan witnesses for the pair `A,B`, common R-exit `zi->h`, and a remainder vertex `x` with `h->x` and `x->zi` for all i.

For each i the triangle

`K_i = z_i -> h -> x -> z_i`

replaces `C` without changing total packing size. The new remainder is

`R_i=(R-{h,x}) union (C-{z_i})`.

The primary report noted that one old witness can be made a remainder sink. In fact the exchange is stronger:

**Pairwise exposure lemma.** For every i, both vertices of `C-{z_i}` are simultaneously R-supported exact five-fan witnesses for the unchanged pair `A,B` in the packing `(A,B,K_i)`.

Indeed their five arcs into `A union B` are intrinsic and unchanged. Of the two residual arcs of each old witness, `->h` now enters `K_i`; the old successor either enters `K_i` (for the predecessor of `z_i`) or goes to the other exposed old witness. Thus one exposed witness is an R-sink and the other has exactly one R-outarc. In particular, for any chosen pair `{z_p,z_q}` of the three old cycle-supported witnesses, choose the third index i; then both are legal remainder vertices in the same globally minimum packing.

This removes the support-location obstruction for every pair of old witnesses simultaneously, not merely one witness at a time.

## 2. Intrinsic heavy-label avoidance for all three old witnesses

Write

`a_j=|N+(z_j) intersect A|`, `b_j=|N+(z_j) intersect B|`.

Since `a_j+b_j=5`, exactly one of A,B receives at least three arcs from `z_j`; call it the heavy label `H_j`.

Choose any switched packing in which `z_j` lies in the remainder. The ordinary globally-minimum one-vertex exchange lemma is then legal: if any vertex of `H_j` sent an arc into `z_j`, the fan of `z_j` into `H_j` would be at most two, contradicting its definition. Therefore, in the ambient digraph itself,

`H_j -> z_j` has no arc at all.

This conclusion does not require the switched packing to remain globally NO-SIX; it uses only the intrinsic fan `>=3`, equal-size minimality, and the fact that `A,B` are untouched by the support switch.

By pigeonhole, two of the three witnesses, say `z_p,z_q`, have the same heavy label `H in {A,B}`. Let `L` denote the other of `{A,B}` and choose the third support index r, so that in the minimum packing

`(H,L,K_r)`

both `z_p,z_q` are remainder vertices. Then simultaneously

`|N+(z_p) intersect H|>=3`, `|N+(z_q) intersect H|>=3`,

and

`H -> {z_p,z_q}` is empty.

This is a new simultaneous double-heavy avoidance certificate.

## 3. Two-linkage from the common heavy cycle

Because the inherited exact-seven counterexample is 3-vertex-strong, the directed set version of Menger applied from `V(H)` to `{z_p,z_q}` gives two vertex-disjoint directed paths ending at the two distinct targets. (A single internal separator would contradict strong connectivity after deleting that vertex.) Trim each path to its last vertex on H. We obtain vertex-disjoint paths

`P_p: b_p -> ... -> z_p`,
`P_q: b_q -> ... -> z_q`,

with distinct starts `b_p,b_q in H` and no other H-vertex on either path. Since H has no arc into either target, neither path is a single H-to-target edge.

If either path internally meets `L` or `K_r`, we have an actual cross-packed transition and are in the lead/partner cross-cycle splice branch. Hence the genuinely new hard case is when both path interiors lie in the current remainder.

## 4. Exact circular two-splice criterion

Assume both `P_p,P_q` are remainder-internal after their starts. On the directed cycle H, the distinct anchors `b_p,b_q` partition H into two disjoint directed vertex intervals

`I_p = H[b_q^+, b_p]`,
`I_q = H[b_p^+, b_q]`.

Here `I_p` is the interval ending at `b_p` that avoids `b_q`, and `I_q` is the interval ending at `b_q` that avoids `b_p`.

Let

`F_p=N+(z_p) intersect H`, `F_q=N+(z_q) intersect H`.

If

`F_p intersect I_p != empty` and `F_q intersect I_q != empty`,

choose `a_p` and `a_q` in these intersections. Then

`D_p = P_p + (z_p->a_p) + H[a_p,b_p]`,
`D_q = P_q + (z_q->a_q) + H[a_q,b_q]`

are two genuinely directed vertex-disjoint cycles. Their H-parts lie in the disjoint intervals `I_p,I_q`; their off-H parts lie in the vertex-disjoint paths `P_p,P_q`. They are disjoint from the untouched packed cycles `L` and `K_r`. Therefore

`D_p, D_q, L, K_r`

are four vertex-disjoint directed cycles, contradicting BT4 counterexample status.

All affected vertices are explicit: H is split only along the two selected directed intervals, each remainder path is used by exactly one replacement cycle, and `L,K_r` are untouched.

Consequently, in any actual counterexample, every such pure-remainder double linkage must satisfy the **fan-concentration obstruction**

`F_p subset I_q` or `F_q subset I_p`.

Since each heavy fan has size at least three, the corresponding wrong-side interval contains at least three heavy fan targets. Equivalently, the only way the two-cycle augmentation can fail is that one heavy fan is completely trapped on the H-arc whose use would force the replacement cycle through the other linkage anchor.

This is the first essential missing implication after the latest lead update: prove that the regenerated off-pivot witness / residual-degree staircase forbids this fan concentration, or use the third old witness to force a second pair of anchors for which both correct-side intersections occur.

## 5. Compatibility with the residual staircase and negative control

The primary B05 report applied Lewandowski–Polcyn–Reiher’s complete k=2 outdegree-sequence theorem to show that in every NO-SIX pair deletion the residual degrees obey

`d1=d2=d3=2`, `dj<=j-1` for j>=4,

hence the pair fans form the staircase `5,5,5,>=4,>=3,>=2,...`. In the total-coalescence triangle this localizes an R-supported four-fan gate to the forward cone of h.

The latest lead’s off-pivot regeneration and the present pairwise-exposure lemma now put these facts in the same minimum packing: the three original degree-two witnesses persist in the pair-deletion residual graph, two can be made R-supported at once, and the staircase supplies additional lower fan mass beyond them.

The account02/B06 16-vertex local adversary realizes the three-state neutral support orbit, so a proof cannot claim that a neutral orbit of length three is impossible from degree, domination, 3-strongness, and support switching alone. In that adversary a four-pack exists, exactly as the circular two-splice philosophy predicts must be found using extra linkage/global information. Thus the correct next target is the fan-concentration obstruction above, not a cycle-length-only monotonicity claim.

## 6. Honest status

`ESSENTIAL_STEP_APPLIED`, not a full proof. The new result is a source-correct simultaneous exchange/linkage interface: any two of the original saturated cycle-supported five-witnesses can be exposed together as remainder witnesses; two sharing a heavy packed cycle have a two-linkage from that cycle; and unless one heavy fan is wholly concentrated on the wrong anchor arc, the linkage gives an explicit four-cycle packing. The unresolved case is now an exact circular fan-concentration configuration, to be combined with the residual fan staircase and the third witness.
