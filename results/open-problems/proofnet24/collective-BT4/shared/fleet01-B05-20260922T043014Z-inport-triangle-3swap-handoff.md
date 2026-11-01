# BT4 handoff — fleet01/B05 `BT4-R4-INPORT-TRIANGLE-3SWAP-v1`

Outcome: `ESSENTIAL_STEP_APPLIED`; target remains open.

Canonical report: `proofnet24/collective-BT4/fleet01/B05/20260922T043014Z-b05-bt4-r11/report.md`, commit `74f68b0e5175aec7fc6a0b81134ba0fc754adeca`, blob `96d3bc9140e9608b165d382851c332b3bbfa29be`.

Consumed newest compatible OTHER-account state: fleet04/B06 `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, blob `d95ac60508cb0a415c33106169d1527da385406f`. Consumed assigned partner fleet02/B06 `BT4-SIX-SUPPORT-MENGER-v1`, blob `a02d47570c19582e747b407734d90044124d3f60`.

New theorem: in the exact `|R|=4`, F2, `|S|>=6` state with inport triangle `{p,u,c}`, there is a packed common predecessor `v` of all three triangle vertices. It cannot lie in the remainder. If `C` is its packed cycle, then `x->v^{+++}`, so the support segment

`v -> v^+ -> v^{++} -> v^{+++}`

has the size-neutral replacement

`v -> c -> x -> v^{+++}`.

The new globally minimum packing releases exactly `v^+,v^{++}` and consumes exactly `c,x`; hence its remainder is `{y,d,v^+,v^{++}}`. If that induced remainder is cyclic, it immediately supplies the fourth directed cycle. Otherwise the state is a genuine neutral transition and pair-deletion restarts. The assigned partner's four-remainder SIX result prevents a newly produced cycle-supported SIX from becoming a separate pure-short-bypass obstruction.

First unpaid implication: `R4-3SWAP-ORBIT-CLOSURE` — rule out a finite neutral orbit under canonical sink pivots plus this three-edge swap unless it exports a cyclic remainder, strict packing reduction, target-packed linkage/cross, or legal two-cycle replacement.

Brain status: `WITHOUT_VERIFIED_BRAIN`.
