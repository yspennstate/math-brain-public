# BT4 handoff — fleet02/B20 port-triangle / triple-dominator reduction

Source run: `proofnet24/collective-BT4/fleet02/B20/20260922T013238Z-fleet02-B20-bt4-r11/report.md`
Outcome: `ESSENTIAL_STEP_APPLIED`, not a full proof.

Inputs actually consumed: fleet02/B04 lead/correction (`d82fc84180bc66fd660c6c79f9a7f26332bdae72`, `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`), fleet04/B06 named-partner saturation report (`08cf8f4283de825d533677d6edf5707523744a22`), and fleet03/B05 corrected marked-segment/linkage package (`f1545c2e4a546d17150bb20bbc59650a29eb2672`, `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`).

New reusable facts in the neutral marked-segment equality `ell=m+s-1`:

1. If `c in C` sends `c->w`, then every `d in N+(w)∩C` satisfies `d_C(c,d)<=m`. Proof: replace `B` by the bypass cycle and `C` by `c->w->d->C[d,c]`; minimum total packing gives `ell+d_C(d,c)+1>=s+|C|`.
2. For a cycle-supported six-fan with split `(3,3)`, if the equality cage has no `R`-inlink, then the same bypass is neutral for both heavy targets, the two target inports are unique, and for shortest source cycle `B` in the quadratic-minimum packing all three cycle lengths differ by at most one.
3. Let `p=w^-` and let `b,c` be the unique target inports. Arc domination forces `{p,b,c}` to induce a directed triangle `T`.
4. Since `D-T` cannot have three disjoint directed cycles, the k=3 theorem forces `q outside T` with arcs to all three ports. Chordlessness localizes `q` to `R`, `b^-`, `c^-`, or `p^-`.
5. If `q in R`, then `q,w` are nonadjacent and the exact fleet04/B06 missing-arc saturation lemma produces three disjoint directed cycles plus a bounded `q`-to-`w` path avoiding `N+(w)`; its final port is one of `p,b,c`.

Next exact target: eliminate/splice the four `q` locations. Start with `q in R` using the saturation certificate and port triangle; handle `q=b^-`, `c^-`, `p^-` via simultaneous two-cycle surgery using the forced cross-arcs. Keep asymmetric six-fans and five-fans as separate branches. Do not repeat static fan counting and do not claim BT4 closure.
