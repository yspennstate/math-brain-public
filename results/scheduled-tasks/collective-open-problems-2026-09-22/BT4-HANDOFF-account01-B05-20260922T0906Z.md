# BT4 handoff — account01/B05 20260922T0906Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Result: `BT4-F3-R3-PIVOT-GUARD-v1`  
Target: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

Canonical report: `proofnet24/collective-BT4/account01/B05/20260922T085440Z-b05-bt4-r11/report.md`, creation commit `7f56e338eba93850130bb51d86a84182ced1b520`, readback blob `1125f16076f30ff05f44ea72e9ddfceb42f8c48f`.

Consumed partner result: account02/B06 `BT4-RANK2-PORT-PARITY-v1` (report blob `0e2262187f4ba70675c24940d913532224bc88c1`). Do not treat bidirectional rank two as an automatic splice: both support orders must be non-BLOCK and have matching ID/SW parity.

## New local theorem

In the residual-three F3 defect-one state, execute a tight light-support pivot at `b`:

`Z' = b -> t -> b++ -> Z[b++,b]`,

where the old sink `t` enters the support and the old successor `x=b+` becomes residual. The new residual is exactly `(R-{t}) union {x}` and the ambient arcs `b->x` and `t->x` persist.

If `x` were the new residual sink, no-SIX and exact outdegree seven force its packed fan profile to be `(3,2,2)`. The defect-one collar from the packed return `b->x` puts every `Z'` target of `x` within distance three from `b`. But `x->b` and `x->t` are both forbidden by orientedness because `b->x` and `t->x`. A 3-fan on `Z'` is therefore impossible; a 2-fan must use the distance-three position, which gives an exact-R4 compression. Hence, in a no-SIX/no-R4 survivor, the fresh hole `x` is not a residual sink.

The obstruction persists while the support edge `b->t` remains unchanged. A later tight pivot on the same support destroys that protected adjacency only if its pivot site is `b` (removing `t`) or `b^-` (removing `b`). Thus an old hole cannot later become a sink unless the orbit first performs one of two local guard-breaking pivots.

If two consecutive tight pivots occur on distinct light supports, exposing holes `x` then `y`, then both holes are forbidden as sinks (fresh-hole for `y`, persistence guard for `x`). The unique possible sink in the new three-vertex acyclic residual is therefore the one residual vertex retained through both pivots.

## First unpaid implication

`BT4-F3-R3-LOCAL-PIVOT-ORBIT-CLOSE-v1`: close the finite bounded-support pivot choreography under the rule that a prior hole may become a sink only after a neighboring guard-breaking pivot on its support. Any connector closure must satisfy the B06 port-parity criterion. Desired outputs remain exact R4, pair-SIX, cyclic residual, strict packing decrease, matching-parity non-BLOCK two-splice, or a fourth cycle.
