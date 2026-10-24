# PROB20-17 — 2026-09-15T180036Z report, Part 2: executed checks and receipts

**STATUS: PARTIAL; this file supplements, and does not replace, `2026-09-15T180036Z__report.md`.**

The deterministic/random checker corresponding to the collision-coupling theorem was executed after the main mathematical Markdown was committed.

Artifact path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/artifacts/2026-09-15T180036Z__verify_collision_coupling.py`

The executed test bank used both real and complex PSD matrices, dimensions `2,3,4,6`, 3000 independent pairs per `(field,dimension)` bucket, and log-spread spectra.  It directly checked the proved inequalities
\[
Q_{31}^{\{A,B\}}\ge4(x+y)
\]
and
\[
Q_{31}^{\{A,B\}}\ge2Q_{22}^{\{A,B\}}-4p^2,
\]
where `p=||AB||`, `x=||A^2B^2||`, `y=||ABAB||`, and `Q22_pair=2(x+y+p^2)`.

All proved-coupling assertions passed.  The minimum observed ratio
\[
\frac{Q_{31}^{\{A,B\}}}{2Q_{22}^{\{A,B\}}-4p^2}
\]
over cases with positive denominator was
\[
1.0000000000004876.
\]
This near-equality is expected from nearly commuting/equal configurations and is corroborative only.

For the two explicitly **UNPROVED** diagnostic targets, the same test bank observed
\[
\min\frac{x+y}{2p^2}=1.0000000000003204,
\]
and
\[
\min\frac{xy}{p^4}=1.0000000000006404.
\]
These numerical values are not proof and are not used in any theorem or universal constant.

The main report was committed first, in accordance with the delivery requirement.  This Part 2 records the subsequently executed checker results without overwriting the mathematical report.

**Verification level:** self-check plus reproducible randomized diagnostics; no independent/formal review.
