# Source-bound FEI handoff — optimized Holevo collar / child-slack starvation

Source report:
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0711Z-holevo-collar-slack-starvation/REPORT.md`.

Consumed peer source:
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T055830Z-holevo-low-delta-collar/REPORT.md`, blob `d31f54036cbc71c9ed9850b6da5c2b093f2f77e1`.

For the live fixed candidate `C^dagger=6.521851214`, balanced-child local gluing with `0<delta<=1/4` is strictly positive whenever

`u <= 2^(-87/10) delta^(8881/1000)`.

This uniformly enlarges fleet02/B13's `2^-10 delta^9` forbidden collar by at least `2^1.538 = 2.9039165598...`.

More importantly, at a minimum-essential-arity global-bias-minimizing counterexample in the rare-bias regime `u<=2^-10`, set

`R = B log2(1/delta) - A log2(1/u) - C`,

with the exact `A,B,C` from fleet02/B13.  Negative balanced-child gluing forces `R>0` and

`(1-u)d_common + u d_rare < u delta R`,

hence

`d_rare < delta R`,
`d_common < [u/(1-u)] delta R`, and
`|d_1-d_0| < delta R`.

Thus a boundary prime obstruction must starve the continuation slack of its proper restrictions; the common branch gets an additional factor `u`.  The next target is a nondecomposable slack-gap theorem ruling out simultaneous all-pivot starvation, while unequal child output measures/intermediate biases remain open.

Full FEI remains OPEN / NOT PROVED.  No assumption `sum d_k=O(J)` is used; fleet04/B18 mixed-curvature integrability is preserved.
