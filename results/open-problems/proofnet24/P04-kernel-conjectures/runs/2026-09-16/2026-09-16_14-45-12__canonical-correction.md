Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; the scheduler exposes no model selector or reasoning-effort selector.

# Canonical correction — P04 run 2026-09-16 14:45:12 +03:00

Original immutable report:

`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_14-45-12__run-report.md`

Original creation commit:

`e67dddbdfb3c6cc4c5f13502cc61d07980fe59f2`

Original verified blob:

`762ba8d76c4d8adfc1e90de920f343b6234a999c`

Exact-commit readback reached the terminal marker `**End of complete run report.**` and found one local LaTeX transport defect in Section 2.1. The intended line was the elementary normalization identity

`1/(2N) = 1/(4n).`

In the immutable historical report, the second `frac` command in that display was malformed during transport and appears as a newline followed by `rac1{4n}`. The equation immediately before it already defines `N=2n`, and all subsequent normalization formulas, including the exact total first-order cost `K/(4 sqrt(d))`, are intact.

This correction changes **no theorem, hypothesis, status, audit count, metric, proof dependency, path/SHA reference, literature conclusion, or peer-audit verdict**. It only restores that one display to the intended plain-text identity above.

The canonical content of this run is therefore the original complete report together with this immutable correction.

Status: `CANONICAL_CORRECTION_APPLIED`.

**End of canonical correction.**