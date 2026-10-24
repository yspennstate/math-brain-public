# BT4 account02/B05 — triangle-lock transport through the other-light port

Run: `20260922T052219Z-b05-bt4-6f8c7964`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-TRIANGLE-LOCK-TRANSPORT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and controls

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement. The oriented exact-outdegree-seven model below is only the inherited minimum-counterexample normal form after the genuine digon reduction.

Fresh owner controls were read from `yspennstate/math-research-brain` at main commit `da0551f3d7473ddf2383a19e9fcb89e976330f07`; main advanced concurrently to `4f0eb485496e46ec1ec45c35ae82985137901af0` without changing the control blobs. OWNER revision is `2026-09-22.2`; B05 remains assigned to BT4 and the old brain-installation/benchmark duties remain superseded.

Control/source Git blobs used: AGENTS `94387098453b9f4a9b10179183f6f6ec780fd987`; README/OWNER `3d4a9372c87802ab734141a3374d04c8823372e3`; fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`; roles `ed17ecc94f76720c0345b3e32249b791b20ec611`; PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`; ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`; TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`. Whole-file and OWNER-message SHA-256 values are `UNVERIFIED_CURRENT_RUN`; immutable Git object identities are recorded rather than manufacturing native hashes not independently computed from materialized authorized bytes.

The source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine conjecture is stated unresolved for `k>=4`, while their theorem allows one reversed arc per cycle. No such nearly-directed cycle is counted here.

## Team mathematics actually consumed

Campaign lead account02/B04 latest complete package: run `20260922T041847Z-b04-bt4-r11`, report blob `596929efe56393d3ab515544fa33ec6a19e75c83`, controlling strengthening blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`. I use two source-valid lead facts: every directed cycle in a BT4 counterexample has an external vertex with at least three outneighbors on it (delete the cycle and apply the genuine `k=3` theorem), and in the canonical global-NO-SIX sink state the heavy cycle sends no arc to the sink while each light direct inport determines the sink's exact consecutive two-target fan.

Named OTHER-account partner actually consumed: account03/B06 run `20260922T041829Z-B06-bt4-r11`, candidate `BT4-R4-LOWFAN-CROSS-TRIANGLE-v1`, report blob `30489f1b8273dd8a0aededa7d5348e5a42c7a999`, checker blob `b3f2b2650c959b221f2bd955281788bf0bcc5dc6`. The partner proves that the post-neutral-pivot F2 low-fan branch either has an opposite cross pair or enters one exact source-triangle lock. This report attacks the residual lock under the full canonical sink hypotheses; no peer outcome label is used as proof.

I also reuse my proved post-pivot wall `BT4-RSC-v6-postpivot-wall`, report blob `9ebdea5c728bbcf442a73dfc31df91f66b4da00b`: after a neutral two-target pivot the freed successor has exactly one support outneighbor, and its remainder-exit count yields SIX, a five-witness plus wall, or a two-arm packed escape.

## Exact residual lock notation

Assume the partner's F2 branch and that an opposite cross pair has not already been exposed. Let the old source cycle be `S0=p->q->a->p`, where `q=p+`, `a=p++`, and let the neutral pivot be `S*=p->x->a->p`. The lock has `|S*|=3`, post-pivot remainder `R*={q,r,b,c}`, triangle `W=x->r->p->x`, arcs `p->q,x->q,r->q`, and q-profile `d_H^+(q)=2`, `d_U^+(q)=2`, `N^+(q)∩S*={a}`, `N^+(q)∩R*={b,c}`. In the residual no-opposite-pair branch, the partner's packed-inport lemma gives `(H∪U) not->q`; hence orientation gives the exact in-neighborhood `N^-(q)={p,x,r}`. The canonical lead sink structure also gives `H not->x` and sink fan sizes `(3,2,2)` on `(H,S0,U)`.

## Lemma 1 — the lock triangle forces an other-light three-hit port

There is `t in U` with `t->x,r,p`. Moreover t is the unique U-vertex entering x and `N^+(x)∩U={t+,t++}`.

Apply the lead's external-three-hit lemma to `W=x->r->p->x`. A three-hit witness is not q because all W vertices enter q; not a because `x->a`; not b or c because `b/c->r` would create the old-remainder cycle `r->q->b/c->r`; and not H because `H not->x`. The only remaining packed support is U, proving `t->x,r,p`. Since `m_U(x)=2`, the source-fan-two minimum-packing comparison gives exactly `{t+,t++}`; a proper consecutive two-block has a unique predecessor, so t is the unique U inport.

## Lemma 2 — the old source triangle forces the missing lock arc

The lock forces `r->a`. Consequently r sends to all three vertices of `S0`, and `S0 not->r` by orientation.

Apply external-three-hit to `S0=p->q->a->p`. A witness is not x because `p->x`; not b,c because `q->b,c`; and not H or U because `(H∪U) not->q`. The only remaining outside vertex that can hit q is r, which already has `r->p,q`; therefore the required third hit is `r->a`.

## Lemma 3 — simultaneous de-lock transport

Set `U_x=t->x->t++->U[t++,t]`. Then `(H,S0,U_x)` is another globally minimum three-cycle packing. Its remainder is exactly `Rdag={r,b,c,t+}` and is acyclic. In this new packing `N^+(t+)∩U_x={t++}`, while r has all three S0 vertices as outneighbors and receives none from S0.

Indeed the U move replaces `t->t+->t++` by `t->x->t++`, preserving |U| and freeing t+. Simultaneously replacing `S*=p->x->a->p` by `S0=p->q->a->p` consumes q and frees x. The two equality moves are disjoint because the U move consumes x while the S move consumes q. Starting from `R*={q,r,b,c}`, the net remainder is `{r,b,c,t+}`. Any cycle there would be a fourth cycle. Old chordlessness leaves t+ only its successor t++ among U vertices, and `x->t+` forbids `t+->x`.

Thus the source-triangle lock is not terminal under the complete canonical sink geometry: at no packing cost it becomes a standard one-freed-vertex state, while retaining a remainder vertex r that hits an entire packed triangle.

## Corollary 4 — the lock falls back into the post-pivot wall

Let `e=d^+_{Rdag}(t+)`. Then `e=0` gives a SIX witness on `H∪S0`; `e=1` gives a five-witness plus the post-pivot wall; and `e>=2` yields either a genuine cross from `U_x` to H or S0, or two internally vertex-disjoint same-support escape arms from distinct remainder exits to distinct U_x return vertices, with at most one returning at t.

The proof is the already established `BT4-RSC-v6-postpivot-wall`: exact outdegree seven plus the unique support edge gives `d^+_{H∪S0}(t+)=6-e`; 3-vertex-strongness gives the return paths after deleting the two pivot ports; acyclicity of Rdag forces those paths to hit the packing.

## Lemma 5 — q's U-targets either align or perform a second equality transport

Index U from the forced port as `t=u0->u1=t+->u2=t++->...->u_(m-1)->t`. For every q-target `u_j`, j>=1, the genuine cycle `t->r->q->u_j->U[u_j,t]` is disjoint from H,S* and has order `m-j+3`. Global minimum gives `j<=3`. If `q->t`, then `t->r->q->t` forces `m=3`.

Therefore exactly one of the following occurs:

1. `N^+(q)∩U={t+,t++}=N^+(x)∩U` (aligned common fan); or
2. there is a size-neutral U replacement through `t->r->q` that consumes r,q, frees t+,t++, and leaves acyclic remainder `{b,c,t+,t++}`.

For case 2, the nonaligned target is either t with m=3 or u3; in both cases the replacement has exactly |U| vertices. This independently removes the generic reversed-arc lock unless its two U-fans coincide exactly.

## Certificate diagnostic

The partner's exact 17-vertex local certificate is not a counterexample to these lemmas because it deliberately omits the complete canonical sink constraints. The attached source-bound probe, using the exact partner adjacency list, reports W three-hit witnesses `[0,3,7]`, old-source-triangle three-hit witness `[14]`, H vertices entering x `[0,1,3,4]`, and U vertices entering x `[7,9]`. Thus it violates `H not->x` and has two U inports; it nevertheless confirms the source-triangle witness conclusion exactly (`r=14`). The computation is diagnostic only; the lemmas are uniform proofs.

## Conditional end-to-end and first missing implication

At the current four-remainder canonical sink frontier: existing reductions give the `(3,2,2)` sink and neutral source pivot; account03/B06 reduces F2/F3 to an opposite-cross interface or the lock; Lemmas 1--3 force an other-light port and simultaneous equality transport of the lock; Corollary 4 sends the transported state into SIX, five-witness, genuine cross, or the isolated two-arm same-support wall; Lemma 5 independently forces exact fan alignment or a second equality exchange removing both lock remainder vertices.

The first essential missing implication is now `BT4-LOCK-TRANSPORT-CLOSURE-v1`: close the residual where transported t+ has the two-arm same-support escape, r hits all three vertices of packed triangle S0 with `S0 not->r`, and/or the aligned common fan `N_U^+(q)=N_U^+(x)={t+,t++}` persists. The closure must produce two vertex-disjoint replacement directed cycles, a strict smaller three-packing, a directed cycle in an exchanged remainder, or a fourth directed cycle. The separate SIX closure remains unpaid. A single opposite-cross pair is not counted as two replacement cycles.

## Failure checks and status

The argument uses the lock only in the residual no-opposite-pair branch, which is what authorizes `(H∪U) not->q`. The three-hit lemma uses the genuine k=3 theorem. Excluding b,c as W witnesses uses old-remainder acyclicity. Excluding H uses `H not->x`, precisely the hypothesis absent in the partner's broad local certificate. Equality transports are not fourth cycles. No edge-disjoint or one-reversal surrogate is used. Full BT4 remains open; no novelty claim is made.

Before: the partner's exact lock survived local degree/orientation/domination/3-connectivity/old-new-remainder-acyclicity checks. After: complete canonical sink hypotheses force another U port, force `r->a`, transport the lock to a one-freed-vertex wall, and reduce the q/U fan to exact alignment or a two-remainder equality exchange. Outcome: `ESSENTIAL_STEP_APPLIED`.

Account02 inventory inspection found all 20 managed B01--B20 tasks enabled on hourly cadences, B05 role-aligned, with no deficit requiring B20 action and no scheduler mutation. Brain status: `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured effort: `UNKNOWN / not exposed`. Known effective effort: `UNKNOWN`. Provider reasoning usage/time: `null / not exposed`. Elapsed work at report construction: approximately 615 seconds of UTC wall/tool time, not pure thinking.
