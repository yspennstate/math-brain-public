# P12 run-report erratum — 2026-09-17T04-20-46Z

This immutable erratum corrects one contradictory displayed line in

`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T04-20-46Z__run-report.md`

at Section 2.

The report correctly states immediately before and after the display that **no qualifying P26 P12 full-package audit exists and obligation 5 remains OPEN**. The displayed formula was accidentally written as

\[
A_{26}(P_{\mathrm{frozen}})=\mathrm{PASS}.
\]

That is the **required closure condition**, not the current state. The current state is

\[
\boxed{A_{26}(P_{\mathrm{frozen}})=\mathrm{MISSING/PENDING}},
\]

and the closure condition still to be supplied is

\[
\boxed{A_{26}(P_{\mathrm{frozen}})=\mathrm{PASS}}.
\]

No metric, theorem statement, audit credit, status, or `ledger_delta` changes: P12 remains `2 -> 2`, `PARTIAL / AUDIT-GATED`, with obligation 5 OPEN, obligation 6 DONE by P11, and obligation 7 OPEN.

The original report remains immutable; this erratum is the authoritative correction to that single display.
