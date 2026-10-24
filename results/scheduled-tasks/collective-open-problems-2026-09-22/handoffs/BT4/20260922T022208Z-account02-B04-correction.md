# BT4 correction handoff — account02/B04 — heavy-fan domination escape

This file **supersedes the TCEX-bound claim** in `20260922T022208Z-account02-B04.md` for the specific branch `A not->z`. Preserve the earlier handoff as history, but use this correction as controlling.

Run: `20260922T022208Z-b04-bt4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Canonical controlling addendum: `yspennstate/math-open-problems`, `proofnet24/collective-BT4/account02/B04/20260922T022208Z-b04-bt4-r11/correction.md`, commit `fa3038109977a1f4490d4efd616e7ae8acc45bf8`, Git blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`, SHA-256 `d597258dfe7ecfa6f27f131809b6483e23bb3b1af7843fca09c69e4ec65b18ba`, 5,686 bytes.

## Correction

The first handoff built a singleton `R`-bypass under `A not->z` and then invoked account03/B05's marked-segment inequality. That invocation is invalid because the partner inequality requires an incoming heavy-cycle arc `b->z` with `b in A`, absent in this branch. The bypass itself remains valid, but the quoted `ell>=m` / `ell>=m+1` consequence is quarantined.

## Stronger valid replacement

Let `z in B` be a cycle-supported witness heavy on `A`, and assume `A not->z`. Pick a heavy fan target `a in A` with `z->a`. Dominate the **fan arc** `z->a`, obtaining `q0->z,a`. Since `A not->z`, `q0 notin A`.

- If `q0 in C`, `q0->a` is already a cross-packed `C->A` arc.
- If `q0 in B`, chordlessness forces `q0=z^-`, so `z^-->a` is a cross-packed `B->A` arc.
- If `q0 in R`, repeatedly dominate `qi->z`. Acyclicity prevents repetition, so the chain reaches a first packed `qt notin A`. If `qt in C`, the chain followed by `q0->a` is an R-internal `C->A` transition; if `qt in B`, chordlessness forces `qt=z^-` and gives an R-internal `B->A` transition.

Hence the old null branch `A not->z` always yields a genuine cross-packed transition. In any **no-cross** state every cycle-supported heavy witness necessarily has a heavy-cycle inport, so subsequent account03/B05 TCEX use is hypothesis-correct.

## New G1-S rigidity

Apply account04/B04 `BT4-G1-WITNESS-INVARIANT-v1` (shared blob `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`): choose two same-heavy support witnesses `z1,z2` on `B`, heavy on `A`. In a no-cross state the corrected lemma gives heavy inports `p_i->z_i`, `p_i in A`.

For arbitrary fan targets `a_i in N+(z_i)∩A`, the cycles

`K_i = p_i -> z_i -> a_i -> A[a_i,p_i]`

would form, together with `C`, a strictly smaller three-cycle packing whenever the two forward A-segments `A[a1,p1]` and `A[a2,p2]` were vertex-disjoint. Therefore **every such pair of fan-return segments intersects**. In particular the two shortest fan-return segments intersect unless the witnesses share the same heavy inport.

So the live G1-S obstruction is now a rigid same-heavy collision: common inport or overlapping shortest return intervals, plus the partner's marked-bypass / double-linkage outputs. The unpaid work is global coalescence/splice, not local absence of a heavy inport.

Named partner actually used: account03/B05 `BT4-TCEX-v2.1-linkage`, shared blob `5bbaf8123ad5cdcd3ce19e92f38587e79aefc69f`, corrected scientific blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

No full BT4 proof, near-directed substitution, edge-disjoint substitute, or peer-outcome truth promotion is claimed.
