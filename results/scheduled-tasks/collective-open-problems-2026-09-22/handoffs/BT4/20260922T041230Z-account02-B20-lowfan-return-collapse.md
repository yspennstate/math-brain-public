# BT4 handoff — account02/B20 — lowfan return collapse

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T040022Z-account02-B20-bt4-r13`  
Candidate: `BT4-R4-LOWFAN-RETURN-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
FULL_TARGET_CHANGE: `NONE`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Canonical report:
- `proofnet24/collective-BT4/account02/B20/20260922T040022Z-account02-B20-bt4-r13/report.md`
- creation commit `e37b86dfef98b2fcfee9d5dbc6b00cbfa5a5e4ba`
- Git blob `6853a3c598df8ccda437934fdf1a2d5549d0f2c6`.

Exact inputs actually used:
- lead account02/B04 `BT4-R4-SINK-v7`, blobs `42ccbd25b6972637cd4fae8ff257dfde354e55a6` and frontier `a9064e9a9c82130029ee90f37991af3a34e75c54`;
- named OTHER-account partner account04/B06 `BT4-SINKLINK-v1`, blob `e925675bebb02129deeec2b1902cc11b5e246dde` (used in the exact-six conditional skeleton; not transplanted into the remainder-supported lowfan state);
- account02/B05 two-arm post-pivot theorem, blob `7c14eaf41ddd4761ee256eb82e7e2994fac4806a`;
- OTHER-account account04/B04 `BT4-R4-FREED-PROFILE-v1`, blob `91963fe8256cc0fce04d2f737e14915cb331bea5`;
- OTHER-account account03/B04 `BT4-R4-F3-TWOFAN-COLLAPSE-v1`, blob `76bf4e46377212afac499a6be37410387cb5c183`.

## New reduction

Use the lead's post-neutral-pivot four-remainder state `(S*,H,U;R*)`, with `S*=p->x->p++->...`, freed `q=p+ in R*`, and q having exactly one support outneighbor `p++`.

1. **F3 (`e=3`) closes to CROSS/FOUR_CYCLES.** B05 gives two internally disjoint q-exit return arms. If neither hits H/U and both same-support bypasses were strict, write `k_i` for the number of non-q remainder vertices used on arm i. Then `k1+k2<=3`, `ell_i=k_i+2`, so strictness gives `d1+d2<=5`. Distinct first hits exclude p (distance 0) and x (distance 1), hence `d1+d2>=2+3=5`. Equality forces a distance-3 arm `p->q->r->s->p+++`. F3 has `q->s`, shortening it to the neutral bypass `p->q->s->p+++`. After this neutral exchange old sink x returns to the four-vertex remainder with support degree 1, remainder degree 1 and a 3+2 packed fan; cyclic remainder gives four cycles, otherwise account04/B04's `e>=1` heavy-fan lemma gives a genuine cross.

2. **F2 reverse-inport subbranch closes.** Write `R*={q,r0,r1,r2}`, with `q->r1,q->r2`, `q!->r0`, and assume account04/B04's alternative `r0->q`. No first-hit return arm can use r0, else it closes a directed cycle in acyclic R*. Under B05's internally-disjoint two-arm conclusion, both no-cross arms therefore have length 3. If both were strict, their distinct S* hits would both have distance <=2 while excluding p,x, forcing both to equal p++, impossible. Hence one is neutral, and the same old-x argument gives CROSS/FOUR_CYCLES.

3. **Residual F2 direct-packed-inport becomes an explicit neutral orbit.** If `r0!->q`, account04/B04 forces `t->q` from T in {H,U}. F2 gives q two targets on T. Minimum packing applied to `t->q->b->T[b,t]` gives distance <=2; orientation excludes b=t, so the two targets are exactly `{t+,t++}`. Thus `T'=t->q->t++->T[t++,t]` is a size-neutral exchange freeing `t+`.

## First unpaid universal step

`BT4-R4-F2-NEUTRAL-ORBIT-CLOSURE`: prove that successive F2 direct-packed-inport neutral exchanges cannot form a closed orbit without a strict smaller three-packing, an exchanged-remainder directed cycle/fourth cycle, a SIX witness, or a cross that current two-cycle replacement machinery legally converts to strict improvement.

Suggested next method: lexicographic monovariant on freed-vertex position / remainder-exit profile / forced-inport support distance. If it fails, expose the periodic orbit and combine repeated incidences with the lead's three x-free crosses or account03/B05's corrected two-linkage trichotomy.

No full BT4 proof is claimed; a CROSS is not promoted to a fourth cycle.
