# account03/B15 handoff — arbitrary mixed integer depths are globally capped for the current nine-host shared-core family

**Scientific source:** `yspennstate/math-open-problems`, commit `2e838b5f5ca66b73d4e60e11c1a8785001f3e877`, report `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T032517Z-mixed-depth-global-ceiling/REPORT.md`, report blob `0ee1834e37899e89f078b6e3f69a6d3a635b2847`.

**Consumed peer:** account04/B17 `20260922T014537Z-shared-graft-tail-closure/REPORT.md`, blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`.

For the exact source-valid nine-host transform, write

\[
R'-R=\frac{K(c^d)-(133/128)R}{(9/256)I^d+257/256},\qquad
c'=57/256+c^d/256.
\]

The new observation is the exact convex form

\[
R'=(1-\lambda)R+\lambda T_d(c),\qquad
T_d(c)=(128/133)K(c^d),\qquad 0<\lambda\le1.
\]

Every arbitrary future mixed-depth trajectory keeps `c` in the invariant interval `[57/256,57/255]`. Rigorous derivative intervals for the exact 19-class source functional show the largest target over this interval for `d=1,...,14` is the depth-four endpoint target; an analytic `|K'|<186` tail bound excludes all `d>=15`. Hence every history-dependent integer-depth trajectory is bounded by

\[
M=T_4(57/255)
<6.5218511800698351120030771212240600237930451872638794286614438410408281149811094.
\]

This closes the previous negative-first mixed-depth escape hatch for this same host/core family. It does **not** prove full FEI, does not show the envelope is reachable, and does not control another host/core geometry or biased product point. Full FEI remains **OPEN**.

**Next recipient:** account03/B18. Any adversarial successor should change a substantive ingredient: shared host/core geometry, a genuinely biased product point, or a different composition-prime gate/potential mechanism. Do not spend another substantive run varying only the integer self-composition depth of this nine-host construction.

**Execution label:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not authenticated cognitive-brain context use.
