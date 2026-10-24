# BT4 handoff — account04/B04 chain-compatible MONO collision reduction

Run: `20260922T093625Z-a04-b04-r13`  
Candidate: `BT4-F3-R3-MONO-COLLISION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical science: `yspennstate/math-open-problems`, commit `79d1cde6ad9339057a26912ef2a6f0c3a643e49f`, blob `fdc8437f22f6da8453696e16a261f0fc3c7df693`, path `proofnet24/collective-BT4/account04/B04/20260922T093625Z-a04-b04-r13/report.md`.

Latest complete lead consumed: account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, science blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, shared commit `3d1cdc39d7512ad857e134f23740c027ef879764`.

Named OTHER-account partner results actually applied:
- account01/B05 `BT4-F3-R3-DEFECT1-PIVOT-v1`, shared commit `33bf0a29c07e72bbb56fcb3a93e0b0aebd68b500`, science blob `06534f6cac9597ba2398b031a14ff7d7cbcf3d6a`;
- account01/B05 `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1`, report commit `50a132fde1964a31eb1c3a4ab2f131f3d12fe0ca`, exact blob `9033957c23706f309a7007530fb65868d736eb61`.

New result in the residual-three F3 MONO branch:

1. The partner simultaneous-bypass condensation extends source-validly to **chain-compatible** support segments whose interiors are disjoint but which may share boundary endpoints. The exchanged remainder and released-block dependency proof are unchanged.
2. A tight pivot `c->q->r` to `c->t->r` frees `q`, while both graph arcs `c->q` and `t->q` remain. Hence `q` cannot be a surviving remainder sink until this modified support window is touched again.
3. Three chain-clean MONO pivots are impossible. They would consume the three distinct old remainder vertices and form a chain-compatible full-remainder bypass family. Partner condensation then gives either a fourth cycle or a released sink `q_j`; but `q_j` still has the two same-support in-neighbors `c_j,t_j`, contradicting the partner no-R4 one-inport rule.
4. Therefore within at most the third MONO pivot there is a genuine local collision with a previously inserted token. If the previous modified window is `e->c->t->r`, the new pivot port is forced to exactly one of `{e,c,t}`:
   - `L`: port `e`, frees `c`;
   - `M`: port `c`, frees inserted `t`;
   - `R`: port `t`, frees `r`.
   Endpoint-adjacent windows ending at `c` or beginning at `r` are chain-compatible and do not count as collisions.
5. In L/M, if the previously released `q` reaches the collision sink `s`, a genuine replacement cycle of order 3 or 4 forces the active support to have order at most 4 outside exact-R4 (direct reach gives a triangle outside exact-R4). If `q` does not reach `s`, the third remainder vertex is a second sink: exact two-sink fork.
6. In R, after `c->t->r->u` becomes `c->t->s->u`, the two released vertices have packed blocker pairs `{c,t}` and `{t,s}`. Hence the third old remainder vertex is the unique sink. The next MONO pivot must free one of `{c,t,s}`, so its port is forced to `{pred(c),c,t}`. Thus R immediately produces a second three-position collision rather than reopening an unbounded orbit.

Structural tree now: `TRI` from the previous B04 switch theorem, or `MONO-L`, `MONO-M`, `MONO-R` above. There is no spatially separated three-pivot MONO leaf.

First unpaid implication: `BT4-F3-R3-COLLISION-CLOSE-v1` — close the L/M two-sink forks and the R forced three-port relay, or route them into TRI, exact-R4, SIX, cyclic remainder, strict packing decrease, or a source-valid CROSS/BYPASS splice. Global lead four-port coalescence, SIX, TRI closure and seven-remainder debts remain separate.
