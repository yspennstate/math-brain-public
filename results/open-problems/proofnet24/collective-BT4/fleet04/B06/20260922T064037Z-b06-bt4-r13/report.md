# BT4 fleet04/B06 — four-port coalescence collapses to BYPASS, fresh port, or a short support

Run: `20260922T064037Z-b06-bt4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-FOUR-PORT-COALESCENCE-SHORT-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and current source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source statement, so directed digons count.

The current external boundary was rechecked against Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract still states that the genuine conjecture is unresolved for every `k>=4`; its `2k-1` theorem permits a cycle made directed after reversing one arc and is therefore not a solution of BT4. The genuine `k=3` theorem and the strengthened `k=2` theorem used by the team remain inputs, not target closure.

No search miss is used as a novelty claim.

## 2. Exact team state consumed

Latest complete team-lead version actually read and applied: fleet02/B04 run `20260922T0619Z-b04-bt4-r11`, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, scientific commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The lead corrected a previous invalid direct use of `BT4-SC2-THIRD-PORT-v1`. In the clean four-port heavy-triangle state it instead proves, source-validly, that a genuine three-hit witness of the mixed cycle yields a packed-to-packed CROSS or a distinct-port same-support BYPASS. Its first local debt is the case where a remainder witness lifts only to crosses whose packed endpoints all belong to the old four ports.

Named OTHER-account assigned partner actually consumed and applied: fleet01/B04 run `20260922T054707Z-b04-bt4-r11`, candidate `BT4-HT-TRIANGLE-BOUNDARY-COLLAPSE-v1`, scientific commit `74d6202d71aebcda2580fe8e8db47ee29c013b1a`, report blob `36c1d8eb86ce397198545a2b021bd6f8effade4b`. It proves that the aligned triangular light-support boundary is SIX or has two distinct remainder exact-five/cross generators. This is used below to keep the support-size split exhaustive rather than silently discarding the short branch.

Essential same-account history also read: fleet04/B06 `BT4-TRIANGLE-PORT-LIFT-v1`, report blob `6a8b6182d0e1d602285139bb63b72cd17184cb52`. It takes the partner's two-generator triangular branch to a clean four-port opposite CROSS or a bounded same-support BYPASS. It is not counted as new work here.

## 3. Inherited exact long-support cage

Assume BT4 false and use the team's inherited minimum-counterexample normal form: `D` is oriented, every vertex has outdegree exactly seven, every arc is dominated, `D` is 3-vertex-strong, and `(H,A,B)` is a three-cycle packing minimizing total packed order and then maximizing the number of arcs induced by the acyclic remainder.

In the aligned four-remainder heavy-triangle cage,

`H = h0 -> h1 -> h2 -> h0`,

`R = {x,r0,r1,r2}`,

with saturation triangles

`Ti = hi -> ri -> x -> hi`.

The old remainder arcs are exactly

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`.

There is a port `p in A` with

`p->h0,r0,x`.

In the aligned long-support branch put

`a = p+++` on `A`.

The clean pair from the lead/partner state is

`P : p -> x -> b`,

`Q : q -> a`,

where `b,q in B`, `b!=q`, and in fact the construction also gives `q->h1`. The four packed ports are `p,a,b,q`. The mixed directed cycle is

`K = p -> x -> b -> B[b,q] -> q -> a -> A[a,p] -> p`.

The lead proves that an external three-hit witness for `K` either immediately produces a fresh packed port / same-support bypass, or lies in `R\{x}` and has a domination-lifted CROSS whose two packed endpoints are among `{p,a,b,q}`. The latter is the four-port-coalesced residual attacked here.

## 4. Compact conditional route before the new step

The current aligned heavy-triangle route is:

1. `|A|=3`: fleet01/B04 gives SIX or two exact-five/cross generators; fleet04/B06 `BT4-TRIANGLE-PORT-LIFT-v1` routes the non-SIX generator branch to clean CROSS or bounded BYPASS.
2. `|A|>=4`: fleet03/B05 / the lead produce the clean four-port pair `P,Q`; the lead's witness-lift theorem produces another CROSS or BYPASS.
3. The only local obstruction left by the lead is that the new CROSS may use no packed endpoint outside the old four ports.

The theorem below proves that this old-four-port obstruction cannot persist when both light supports have order at least five. It therefore reduces the coalesced debt to an explicit short-support boundary, without pretending that CROSS or BYPASS is already a four-cycle packing.

## 5. New theorem — four-port coalescence has a short-support escape

> **Theorem (`BT4-FOUR-PORT-COALESCENCE-SHORT-COLLAPSE-v1`).**  
> In the inherited clean four-port state above, suppose `|A|>=5` and `|B|>=5`. Let `v` be the remainder three-hit witness supplied by the lead for `K`. Then the old-four-port coalesced residual cannot persist. More precisely, at least one of the following occurs:
>
> 1. there is a distinct-port same-support `A`-BYPASS with remainder interior;
> 2. a packed endpoint outside `{p,a,b,q}` is forced, giving a genuinely fresh packed port for the CROSS/BYPASS splice frontier.
>
> Consequently, if the lead's four-port-coalesced residual has neither a same-support BYPASS nor a fresh packed port, then necessarily
>
> `|A|=4` or `|B|<=4`.

### Step 1 — the witness cannot hit `p` when `|A|>=5`

The mixed cycle `K` contains only one old remainder vertex, namely `x`. Hence its external three-hit witness has at least two packed hits. In the old-four-port residual every packed hit must be one of `{p,a,b,q}`: a hit at any other packed vertex would, by the lead's domination lift, already have a fresh packed target or produce a same-support bypass.

Because `v in R\{x}`, we have `v in {r0,r1,r2}`. There is a fixed directed path from `p` to every such `v`:

- `p->r0`,
- `p->r0->r1`,
- `p->r0->r1->r2`.

If `v->p`, closing the corresponding path gives a directed cycle of order at most four whose only packed vertex is `p`. It is disjoint from `H` and `B`. Replacing `A` by this cycle gives a three-cycle packing of strictly smaller total order because `|A|>=5`, contradicting global minimum. Therefore

`v not->p`.                                                   (1)

### Step 2 — a hit on `a=p+++` is already a BYPASS

If `v->a`, concatenate the fixed `p`-to-`v` path above with `v->a`. Since the forward distance from `p` to `a=p+++` on `A` is exactly three, this is a same-support path with remainder interior of length

- two if `v=r0`,
- three if `v=r1`,
- four if `v=r2`.

The `r0` case is impossible because length two would strictly shorten the `p`-to-`a` segment and hence the whole packing. The `r1` case is a neutral same-support BYPASS, and the `r2` case is a one-edge collar BYPASS. Thus a coalesced residual with no BYPASS has

`v not->a`.                                                   (2)

### Step 3 — without an A-hit the witness must hit both B ports

By (1)--(2), the witness has no old `A`-port hit. It has at least two packed hits on `K`, so in the strict old-four-port residual it must hit both remaining packed ports:

`v->b,q`.                                                     (3)

The required third hit is then `x` (and indeed every `ri` points to `x` in the exact remainder DAG). Thus the generic four-port collision has already collapsed to a three-vertex fan `{b,q,x}` from one of `r0,r1,r2`.

### Step 4 — `r1` and `r2` force `B` to be short

Suppose first `v=r1`. From (3), together with the clean-pair arc `q->h1` and the cage arc `h1->r1`,

`r1 -> q -> h1 -> r1`

is a directed triangle. It is vertex-disjoint from `T2=h2->r2->x->h2` and from `A`. Therefore

`(A, T2, r1 q h1 r1)`

is a three-cycle packing of total order `|A|+6`. Global minimality of `(H,A,B)`, whose total order is `|A|+|B|+3`, gives `|B|<=3`. In the oriented normal form a directed packed cycle has order at least three, so this forces `|B|=3`.

Now suppose `v=r2`. Then

`r2 -> q -> h1 -> r1 -> r2`

is a directed 4-cycle. It is vertex-disjoint from `T0=h0->r0->x->h0` and from `A`. Hence

`(A, T0, r2 q h1 r1 r2)`

has total order `|A|+7`, and global minimality gives `|B|<=4`.

Under the theorem's assumption `|B|>=5`, both possibilities are excluded. Therefore the only remaining witness is

`v=r0`.                                                       (4)

### Step 5 — the `r0` witness forces the direct cross `p->q`

Apply the lead's domination lift to the actual hit `r0->q`. If the lift produces a same-support bypass or a fresh packed source, the theorem is already proved. Thus remain in the strict old-four-port cross case.

The target is `q in B`, so an old-port cross source must lie on `A`, hence is either `p` or `a`. But `q->a` is already an arc and `D` is oriented, so `a->q` is impossible. Therefore the terminal domination apex is `p`, and in particular the direct cross arc

`p->q`                                                        (5)

exists.

### Step 6 — one domination of `p->q` forces a fresh port, except for one old-port case

Every arc is dominated. Choose `z` with

`z->p,q`.                                                     (6)

A remainder vertex cannot be `z`:

- `x->p` and `r0->p` are forbidden by the existing arcs `p->x` and `p->r0` in the oriented graph;
- if `z=r1`, then `p->r0->r1->p` is a directed 3-cycle replacing `A` and is strictly shorter than `A`;
- if `z=r2`, then `p->r0->r1->r2->p` is a directed 4-cycle replacing `A`, again strictly shorter because `|A|>=5`.

If `z` lies on `A`, chordlessness forces `z=p^-`. Since `a=p+++` and `|A|>=5`, `p^-` is not one of the old four ports: it is a fresh packed port.

If `z` lies on `H`, it is likewise a fresh packed port.

If `z` lies on `B`, chordlessness forces `z=q^-`. Unless `q^-=b`, this is a fresh packed port. Hence the sole way (6) can avoid a fresh packed port is

`z=b=q^-`, with `b->p,q`.                                    (7)

### Step 7 — dominating `b->p` kills the sole old-port exception

Assume (7). Dominate the arc `b->p`, obtaining `y` with

`y->b,p`.                                                     (8)

Again `y` cannot lie in the remainder. The cases `x,r0` are forbidden by orientation against `p->x,p->r0`; the cases `r1,r2` create the same strict 3- or 4-cycle replacement of `A` used above.

If `y` lies on `A`, chordlessness gives `y=p^-`, which is fresh because `|A|>=5`. If `y` lies on `H`, it is fresh. If `y` lies on `B`, chordlessness gives `y=b^-`. But (7) says `b=q^-`, so `q` is the support successor of `b`; in an oriented directed cycle of order at least three the predecessor `b^-` is not `q`. Hence `b^-` is a packed `B`-vertex outside `{b,q}`, again a fresh port.

Thus (8) always forces a packed endpoint outside `{p,a,b,q}`. This contradicts persistence of the old-four-port residual and proves the theorem. QED.

## 6. What the theorem pays for

The lead's previous debt was an unrestricted finite endpoint-coalescence problem: a remainder witness could in principle keep returning every domination lift to the same four packed ports. The theorem removes that phenomenon throughout the all-long region `|A|,|B|>=5`.

The mechanism is not another unsupported selection condition. It uses three already-paid ingredients directly:

1. the exact four-vertex remainder chain gives a short `p`-to-`v` path, so an `A`-port hit either strictly reduces the packing or is itself the required BYPASS;
2. the exact heavy-triangle cage makes `r1` and `r2` hits at `q` create explicit alternative three-packings, forcing `B` to have order at most three or four;
3. in the sole `r0` case, arc domination plus chordlessness forces a fresh predecessor port after at most two domination steps.

No finite enumeration, average-degree surrogate, reversed arc, or edge-disjoint substitute is used.

## 7. Assembled aligned heavy-triangle route after this run

Combining the named partner, the latest lead, and the theorem above gives the following conditional route for the aligned heavy-triangle branch:

- `|A|=3`: SIX or two exact-five/cross generators by fleet01/B04; the already-read B06 port-lift sends the non-SIX generator branch to clean CROSS or bounded BYPASS.
- `|A|=4`: retained explicit short-support boundary.
- `|A|>=5` and `|B|<=4`: retained explicit short-`B` boundary.
- `|A|>=5` and `|B|>=5`: the lead's mixed-cycle witness cannot remain four-port-coalesced; it yields a same-support BYPASS or a genuinely fresh packed port.

Thus the arbitrary-order aligned branch no longer has a generic all-long four-port coalescence obstruction. The remaining target-level debts are still real: the fresh-port/CROSS/BYPASS objects must be spliced disjointness-preservingly; the bounded supports of order at most four must be closed; and the separate general SIX/H5 and seven-remainder triangle-pinwheel/support-carried branches remain unpaid.

## 8. Failure checks and nonclaims

- A CROSS, fresh port, or BYPASS is not counted as a fourth directed cycle.
- The theorem is conditional on the exact inherited heavy-triangle cage and the lead's clean four-port state; it is not a general theorem about arbitrary pairs of cycles.
- The global minimum-packing comparisons use three actual pairwise vertex-disjoint directed cycles in every invocation of minimality.
- The `r1` comparison uses `(A,T2,r1-q-h1-r1)`; the `r2` comparison uses `(A,T0,r2-q-h1-r1-r2)`. No cycle shares a cage vertex in either triple.
- Chordlessness is used only inside a packed support, to identify a possible packed dominator of an incoming support arc with the support predecessor.
- The second domination step is essential: the first step can terminate at the old port `b=q^-`, but domination of `b->p` cannot remain inside the old four ports when `|A|>=5`.
- The short boundaries `|A|=4` and `|B|<=4`, the common CROSS/BYPASS splice, SIX/H5, and the retained seven-remainder branches are explicitly unproved.
- No code or numerical computation was used in this proof.
- Full BT4 remains open. No publication/novelty claim is made from this private proof attempt.

## 9. Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The latest lead reduced the aligned long-support branch to a CROSS/BYPASS witness with one residual old-four-port endpoint-coalescence case. This run proves that the coalescence case cannot survive when both light supports have order at least five: an `A` hit is already a quantified BYPASS; otherwise the witness is forced to `r0`, and two applications of arc domination force a genuinely fresh packed port. The only coalesced support-size residue is therefore `|A|=4` or `|B|<=4`.

Model self-report: `GPT-5.6 Sol`. Requested reasoning: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and provider-thinking-time telemetry: not exposed. Brain status: `WITHOUT_VERIFIED_BRAIN`.
