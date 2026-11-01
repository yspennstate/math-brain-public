Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0169 boundary-rigidity artifact erratum

In `2026-09-19T083400Z__P0169_degree5_boundary_rigidity_and_13var_bound.md`, Section 4.1 contains a typesetting-only typo introduced in delivery: the displayed eleven-variable sparse-dual identity begins `\rac{b_0-b_{11}}{16}`. It must read

\[
L=\frac{b_0-b_{11}}{16}+\frac{b_3-b_8}{80}.
\]

The immediately following bound, equality conditions, exact checker, run report, and all mathematical deductions use this correct formula. No numerical value, proof step, metric, or status changes.