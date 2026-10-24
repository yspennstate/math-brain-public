# BT4 handoff — common-port support collapse to B3/B4

Source worker: `account03/B04`  
Run: `20260922T065047Z-account03-B04-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-HT-COMMON-PORT-SUPPORT-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact peer consumed

Assigned partner `account04/B05`, run `b05-20260922t061406z-r34`, candidate `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`, canonical report blob `4720ee1408bd58b0ce7ca36ef05b402600f0a5c8`.

That result removes the two pure-remainder equality collars in the same-heavy-`A` triangular common-port branch and forces a genuine packed cross. Its first unpaid implication is `HT-CROSS-HALL-SPLICE`.

## New derived step

Canonical report: `proofnet24/collective-BT4/account03/B04/20260922T065047Z-account03-B04-r11/REPORT.md` in `yspennstate/math-open-problems`, commit `4c97192bb64e669a614ddb94e3600ca23d996790`, blob `6367a31cb85bf0d3b333a866471933a4614ac690`.

In the exact four-remainder cage with `A=p->u->v->p`, let `r_k` be the common `u,v` remainder outneighbor, heavy on the other light support `B`.

The new theorem proves:

- every `b in B` requires a remainder exit by exact outdegree seven plus global `NO-SIX`;
- if `k=1`, then `|B|=3`;
- the arc `r1->h0` is impossible because it immediately gives the two disjoint cycles `h0->r0->r1->h0` and `h1->h2->r2->x->h1`, disjoint from `A,B`;
- if `k in {0,2}` and `|B|>=4`, then `r1` must hit all of `A` and has a unique `B` target `b*`;
- global minimum of the three-cycle packing then allows at most two `B`-inports to `r1`, while the remainder-exit budget requires at least `|B|-2`; hence `|B|=4`;
- writing `B=b0->b1->b2->b3->b0` with `b0=b*`, the exact hub is `b2,b3->r1->b0`, while `b0,b1` use `x` and the remaining side port (`r2` for `k=0`, `r0` for `k=2`) bijectively.

So the same-heavy-`A` compulsory-cross branch no longer has arbitrary `B`: only `B3` and one exact `B4` funnel remain.

## Next recipient and first remaining implication

Primary recipient: `account04/B05` (assigned partner).  
Secondary recipient: BT4 lead `account02/B04`.

Next exact obligation: close `HT-CROSS-HALL-SPLICE` separately on (i) the `B3` support and (ii) the exact `B4` funnel above, using the already-forced genuine packed cross and the x-free Hall/reciprocal interfaces. Preserve vertex-disjointness explicitly. The alternative same-heavy-`B` Hall branch is not closed by this theorem.

No full BT4 proof or novelty claim is made.
