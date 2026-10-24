# BT4 shared handoff — arc-max remainder refinement forces triangular low-fan source

Source run: `20260922T051604Z-account04-B04-BT4-r14`  
Scientific report: `proofnet24/collective-BT4/account04/B04/20260922T051604Z-account04-B04-BT4-r14/report.md`  
Scientific commit: `af5371941de0cbc938dbc28a9c7c19b55e719f37`  
Candidate: `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact sources consumed

- Team lead account02/B04 run `20260922T041847Z-b04-bt4-r11`, primary blob `596929efe56393d3ab515544fa33ec6a19e75c83` and controlling strengthening blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`.
- Immediate account04/B04 predecessor `BT4-R4-LOWFAN-PORT-SPLIT-v2`, report blob `d113bed9a8c7d4573e4377ae39d98356ba50b4f8`.
- Named OTHER-account partner account01/B05 `BT4-R4-INPORT-TRIANGLE-3SWAP-v1`, run `20260922T043014Z-b05-bt4-r11`, report blob `96d3bc9140e9608b165d382851c332b3bbfa29be`.

## New theorem

Refine the globally minimum-total three-cycle packing by choosing, among all such packings, one maximizing the number of arcs induced by its acyclic remainder.

In the inherited `|R|=4`, global-NO-SIX source-pivot branch, suppose all immediate SIX, fan-at-least-three return-cross and second-packed-pivot outputs have been excluded, so the post-pivot state is F2-RONLY or F3-SINGLEPORT. Let `x` be the old remainder sink, `K=R-{x}`, and let `q` be the source-cycle vertex freed by the neutral source pivot.

In both F2 and F3 the new remainder has exactly one arc between `q` and each of the three vertices of `K`. Hence

`a(R*) = a(K)+3`.

Because `x` was a sink,

`a(R)=a(K)+d^-_R(x)`, with `d^-_R(x)<=3`.

The pivot is size-neutral and its remainder is acyclic unless four cycles already exist. Arc-maximality therefore forces `a(R)>=a(R*)`, so `d^-_R(x)=3`. Thus every vertex of `K` sends to `x`, and `x` is the unique old-remainder sink. Equality also shows the pivoted packing remains arc-maximal.

Now choose any `r in K` with `q->r` (two choices in F2, three in F3). Since the old source fan has `x->q`,

`q -> r -> x -> q`

is a directed triangle disjoint from the other two packed cycles. Replacing the old source cycle by this triangle and using global minimum total packed order forces the old source cycle itself to have order three.

Therefore every surviving canonical F2/F3 low-fan state has a triangular source and a unique old-remainder sink.

## Application of the named partner result

The latest account01/B05 three-edge-swap theorem starts from a long-source F2 configuration with two distinct old-remainder sinks and `|S|>=6`. The new arc-max theorem shows that neither feature occurs in the canonical arc-maximal minimum-packing representative. The partner theorem remains a valid exchange for noncanonical minimum packings, but its stated `R4-3SWAP-ORBIT-CLOSURE` is not an independent terminal branch of this refined structural tree.

## Further exact cover

Write the forced source triangle `S=p->q->s->p`.

- In F3, `q` dominates all three vertices of `K` and all three send to `x`. For every `r in K`, the triangle `q->r->x->q` has an external three-hit witness. Such a witness can only be `p` or the unique possible vertex `u in U` with `u->x`. Thus the three triangles are covered by at most two witnesses, so one of `p,u` hits at least two; if no U-inport exists, `p` hits all three.
- In F2, label `K={r0,r1,r2}` with `r0->q` and `q->r1,r2`. Each triangle `q->r_i->x->q` has an external three-hit witness in `{p,u,r0}`.

These are source-valid consequences of the genuine k=3 deletion theorem and the inherited light-inport uniqueness.

## First unpaid implication

`BT4-R4-ARCMAX-TRIANGLE-SPLICE-v1`: close the triangular F3 two-witness cover and triangular F2 `{p,u,r0}` cover by combining them with the lead's reciprocal/third-port interfaces, producing two disjoint replacement cycles, a strict smaller packing, a cyclic exchanged remainder, or a SIX state. Keep the lead's heavy-triangle port-disjointness branch and the separate SIX branch explicit.

No full BT4 proof is claimed.
