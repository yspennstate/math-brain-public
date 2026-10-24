# account03/B04 -> BT4 team: port-path upgrade

Candidate: `BT4-HT-PORT-PATH-UPGRADE-v2`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Consumed assigned partner account04/B05 `BT4-HT-XFREE-HALL-v1`, run `b05-20260922t051421z-r34`, handoff commit `face1d9aa603ac2a2a1f0bef6e3e8306999f8dbf`, report blob `e63f331533e20a4a1231458a6c5c43c7eb5c4bf1`.

New exact reduction: each partner escape has shape

`h_{i-1}->a_i`, `h_{i-1}->r_{i-1}->a_i`, `b_i->a_i`, or `b_i->r_{i-1}->a_i`.

Hence, in the distinct-port Hall branch, the two escapes are fully vertex-disjoint except for the single state `LL-COMMON-START`, where both are light-started from the same packed vertex. The previous generic concern about H-support collision is unnecessary.

In the exact fan-collision branch, cyclically orient the pair as `h_i,h_{i+1}` with common extra port `a`; then `h_i->a` is a canonical direct R-free x-free cross arc and `h_i` dominates `h_{i+1}->a`.

For the partner equality return through `r2->h0`, the R suffix is exactly one of `r2`, `r1->r2`, `r0->r1->r2`, giving a finite collision map with the escapes.

Earliest remaining implication: `HT-START-ORDER-CLOSE-v2` — eliminate/splice `LL-COMMON-START` and settle cyclic endpoint order for the already-disjoint positive cases; combine the canonical direct cross arc with the cross/equality return in the fan-collision branch.

Primary recipient: assigned partner `account04/B05`. Secondary recipient: BT4 lead `account02/B04`.

Canonical scientific report: math-open-problems commit `1f2dda2793cc8b782d777ea93bb333c5e74b2fd8`, blob `5c0bcd93ccb8be7137d1edb1c37d9f12cf5968dd`. Canonical shared handoff: commit `4c881987e8565e496bfd4e8a57cff2b47851782d`, blob `14a1ba82917b30ecc6b2c7fc190e6f9f5b76c6a9`.

An earlier immutable draft in the same canonical run was corrected before handoff and must not be consumed; only `report-v2.md` is scientific evidence.

No full BT4 proof or novelty claim is made. Exact outdegree seven and asserted vertex-disjointness are preserved.
