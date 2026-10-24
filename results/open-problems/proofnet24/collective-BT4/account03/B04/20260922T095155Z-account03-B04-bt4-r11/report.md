# BT4 account03/B04 — H-mediated cage forces an exact B two-fan and neutral F2-type pivot

Run: `account03-b04-20260922t095155z-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: extremal / shortest-cycle mechanism with explicit seven-outdegree bookkeeping  
Candidate: `BT4-R4-HMED-TWOFAN-NEUTRAL-PIVOT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source problem; the inherited minimal-counterexample normal form used below is oriented.

No full BT4 proof and no novelty claim are made here.

## 2. Exact other-account result consumed

Assigned partner `account04/B05`, run `b05-20260922t074314z-r35`, candidate `BT4-R4-DIRECT-3X3-CYCLE-FACTOR-v1`; canonical scientific report:

`proofnet24/collective-BT4/account04/B05/b05-20260922t074314z-r35/report.md`, Git blob `ab5f354238ef330125494b0afa5c8e4799716534`.

The exact partner state used here is its aligned four-remainder heavy-triangle cage, including the fixed path `P:p->x->b`, the reverse cross `q->a3`, and its observation that H mediation is an explicit alternative to the direct-3x3 order wall.

The controlling lead source is account02/B04

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The immediately preceding B04 correction is

`proofnet24/collective-BT4/account03/B04/20260922T085034Z-b04-r11/report.md`, Git blob `9ec384548d977e819194e58673a6a467f817c65b`, candidate `BT4-R4-DIRECT-3X3-VACUITY-v1`; it proves that the exact cage already contains the H-mediated connector `p->h0->r0->x->b`, so the partner's residual no-H-mediation branch is empty in this state.

## 3. Inherited exact cage

Assume BT4 false and work in the inherited normal form: `D` is oriented and exactly 7-outregular; `(H,A,B)` is a three-cycle packing minimizing total packed order and, subject to that, maximizing the number of arcs induced by the acyclic remainder. Packed cycles are chordless.

The live aligned four-remainder state is

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with saturation triangles

`Ti=hi->ri->x->hi` for `i=0,1,2`,

and exact old-remainder arcs

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`.

The cage also contains

`r0->h1`, `r1->h2`, `h0->r0`, `h1->r1`, `h2->r2`.

In the aligned long-support branch, `a3=p+++` on `A`,

`N+(h1) intersect A = {p+,p++,p+++}`,

and the fixed clean-cross data include

`p in A`, `p->h0,r0,x`,
`q in B`, `q->h1`,
`P:p->x->b` with `b in B`,
`Q:q->a3`.

The preceding B04 run observed the H-mediated connector `p->h0->r0->x->b`. The question here is what that H mediation actually forces rather than merely relabelling it as an exit.

## 4. Lemma — the neutral T0 exchange forbids h1--r2 adjacency

Let

`T0 = h0->r0->x->h0`.

Then `(T0,A,B)` is a three-cycle packing with exactly the same total packed order as `(H,A,B)`, because both `T0` and `H` are triangles. Its remainder is

`S0={h1,h2,r1,r2}`.

Since the original packing maximizes the number of induced remainder arcs among all minimum-total-order three-packings, and the old remainder has exactly five arcs,

`e(D[S0]) <= 5`.                                                   (1)

But the cage already gives five distinct arcs in `D[S0]`:

`h1->h2`, `h1->r1`, `r1->h2`, `r1->r2`, `h2->r2`.              (2)

Therefore equality holds in (1), these are all arcs of `D[S0]`, and in particular there is **no arc in either direction between `h1` and `r2`**.

Because the normal form is oriented, `r0->h1` and `x->h1` also forbid `h1->r0` and `h1->x`. Hence

`N+(h1) intersect R = {r1}`.                                      (3)

This is a direct consequence of the lexicographic packing choice; no linkage theorem is used.

## 5. Theorem — exact degree seven forces a two-fan on B

Chordlessness/orientation of the packed triangle `H` gives

`N+(h1) intersect H = {h2}`.                                     (4)

The shifted-triple theorem gives

`N+(h1) intersect A = {p+,p++,p+++}`.                            (5)

Together with (3), equations (4)-(5) account for exactly five of the seven outgoing arcs of `h1`. Since `V(D)=H union A union B union R`, exact outdegree seven therefore forces

`|N+(h1) intersect B| = 2`.                                      (6)

Moreover `q->h1`, so orientation forbids `h1->q`.

Let `y in N+(h1) intersect B`. The cycle

`C_y = q -> h1 -> y -> B[y,q]`

is simple and directed. It is vertex-disjoint from `T0` and from `A`, so `(T0,A,C_y)` is a legitimate three-cycle packing. If `d_B(y,q)` denotes forward distance from `y` to `q` on `B`, then

`|C_y| = 2 + d_B(y,q)`.

Global minimum of total packed order gives

`2 + d_B(y,q) >= |B|`,

hence

`d_B(y,q) >= |B|-2`.                                             (7)

Since `y!=q`, the only vertices of a directed cycle satisfying (7) are `q+` and `q++`. There are exactly two targets by (6), so

`N+(h1) intersect B = {q+,q++}`.                                 (8)

Thus the H-mediated branch does not leave an arbitrary H-to-B transition: it forces the exact inport/two-fan pattern

`q -> h1 -> {q+,q++}`.

The degree-seven hypothesis is essential in (6); the extremal minimum-packing hypothesis is essential in (7).

## 6. Neutral pivot and the freed q+ profile

Take the second target in (8). Since `d_B(q++,q)=|B|-2`, the cycle

`B* = q -> h1 -> q++ -> B[q++,q]`

has exactly `|B|` vertices. Consequently

`(T0,A,B*)`                                                       (9)

is another minimum-total-order three-cycle packing. It is pairwise vertex-disjoint: `T0` uses `{h0,r0,x}`, `A` is untouched, and `B*` uses `h1` together with all vertices of `B` except `q+`.

The new remainder is therefore exactly

`R*={h2,r1,r2,q+}`.                                               (10)

If `D[R*]` contains a directed cycle then (9) together with that cycle already gives four vertex-disjoint directed cycles. Hence in a BT4 counterexample `D[R*]` is acyclic. By the same remainder-maximality comparison used above,

`e(D[R*]) <= 5`.                                                  (11)

Three arcs of `D[R*]` are already fixed:

`r1->h2`, `r1->r2`, `h2->r2`.                                   (12)

Therefore `q+` is incident, in either direction, with at most two of `{h2,r1,r2}`. In particular

`d^+_{R*}(q+) <= 2`.                                              (13)

The new packed cycle `B*` contains every old `B` vertex except `q+`. Old chordlessness gives only the support-successor arc `q+->q++` from `q+` into those old B vertices, while (8) gives `h1->q+`, so orientation forbids `q+->h1`. Hence

`|N+(q+) intersect B*| = 1`.                                    (14)

Exact outdegree seven now gives the explicit residual budget

`|N+(q+) intersect (T0 union A)| = 6 - d^+_{R*}(q+) >= 4`.       (15)

Thus the H-mediated branch has been converted into a neutral exchanged four-remainder state in which the freed vertex `q+` has one support arc on `B*`, at most two remainder outarcs, and at least four outgoing arcs across the other two packed cycles.

More sharply:

- if `d^+_{R*}(q+)=0`, then `q+` has six outgoing arcs into `T0 union A` (the campaign's SIX-type pair overload);
- if `d^+_{R*}(q+)=1`, those two packed fans total five, so one has size at least three;
- if `d^+_{R*}(q+)=2`, those fans total four, and either one has size at least three or the unique balanced residual is the exact `2+2` split.

Therefore, after excluding SIX and a new heavy fan, the only degree-seven residual profile is

`(2,2,1,2)`

for the two non-support packed fans, the `B*` support fan, and the new remainder degree. This is precisely an F2-type neutral profile; it is not an arbitrary H-mediated state.

## 7. What this pays and what remains

The preceding B04 run left `BT4-R4-HMED-RECONSTRUCT-v1`: exploit the forced H-mediated connector without illegally counting the old `H` beside a path that uses `h0`.

The present theorem pays the first structural part of that debt:

`H-MEDIATION in the exact aligned cage`

`=> h1 and r2 are nonadjacent`

`=> N+(h1) cap B = {q+,q++}`

`=> neutral packing (T0,A,B*)`

`=> freed q+ has d_R*^+<=2 and at least four arcs into T0 union A`

`=> {SIX-type pair overload, new heavy fan, exact F2-type (2,2,1,2) residual}`.

This is a genuine state reduction and not a claim that H mediation itself is a fourth cycle.

The new first missing implication is

`BT4-R4-HMED-FREED-QPLUS-CLOSE-v1`:

> In the neutral exchanged state `(T0,A,B*)` above, close the SIX/heavy-fan alternatives with the existing source-valid splice machinery and eliminate or splice the exact balanced `(2,2,1,2)` freed-`q+` residual, while preserving vertex-disjointness. A valid closure must produce four disjoint directed cycles, a strict smaller three-packing, a cyclic exchanged remainder, or another already-proved campaign exit.

Primary recipient: assigned partner `account04/B05`. Secondary recipient: BT4 lead `account02/B04`.

## 8. Disjointness and hypothesis audit

- `T0`, `A`, and every `C_y` used for a packing comparison are pairwise vertex-disjoint by construction.
- `B*` uses `h1` and therefore the old `H` is **not** counted alongside it. The neutral packing uses `T0` instead of `H`.
- No path through a packed vertex is silently treated as disjoint from that packed cycle.
- The exact-seven hypothesis is invoked only after the local H/R/A neighborhoods of `h1` have been proved exact.
- Remainder-maximality is used only on three-packings with the same minimum total order as the chosen packing.
- The target remains open; the balanced F2-type residual, the broader SIX closure, other short-support states, and the seven-remainder branches are not claimed closed.

## 9. Operational scope

No authenticated brain retrieval or receiver-context use occurred. No installation/benchmark work, scheduler mutation, email, Drive, public posting, remote workflow, paid model/API/Codex, credential access, or unrelated private material was used. Status remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.
