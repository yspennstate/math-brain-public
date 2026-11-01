# P26 ledger delta and readback — 2026-09-17 10:59 run

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**. GPT-6 / maximum was requested in prompt text only; exposed task controls do not authenticate or enforce model/reasoning.

## Immutable run report

- Path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_10-59-05__run-report.md`
- Creation commit: `72ff3749f7e513a9e350f8ffcd7f842df5cd2f41`
- Exact-commit readback blob: `92a9d397b1eb7e9c9d4dccecc5b184d0479a07b0`
- Readback status: complete; tail reached `End of complete P26 run report.`

## Exact reexecution artifact

- Path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_10-59-05__r16_bf03_exact_recheck.out`
- Creation commit: `fa5a64f47af50f12c8d94e55bdf3c25c45aae424`
- Exact-commit readback blob: `38ba2fc2dc9fed0ad19023e284192ebf4829c2aa`
- Terminal line: `P26-R16-BF03-EXACT-RECHECK: PASS`

## Fixed P26 metric delta

Metric: number of outside packages with two genuinely independent OTHER-track full-proof audits complete.

- Before: `14`
- After: `15`
- Supported unchanged count: `0 -> 0`
- New package counted exactly once: `R16-BF-01 / R16-BF-02 / R16-BF-03`, support-sensitive Beck-Fiala bound.
- P26 audit: `P26-AUDIT-R16-BF03-SUPPORT-SENSITIVE-ENDTOEND-17 = PASS_FULL_MATHEMATICAL_PROOF / LOCAL_PROOF_REPAIR_WRITTEN_HERE / EXACT_CORE_PASS / PRIOR_ART_UNVERIFIED`.
- Distinct audit: `R13-AUDIT-R16-BF03-20260916T143329Z = PASS`, report `runs/R13/20260916T143329Z_audit3-9f2c.md`, creation commit `f9c7f087d9a8cb371d6e47c6c70e2550ff060241`, blob `730e8ed2f81829c969b9dea044b1a7fa82252161`.
- Reconciliation: `P26-RECONCILE-R16-BF03-2OF2-17 = PASS`.
- Do not count repeated P26/R13 reviews again. Do not count this as another audit of the Guo-Fang-Lu universal Komlos package.

## Mathematical status

- R16-BF-03: `PROVED`.
- R16-BF-01 written source had one local separation-presentation gap; P26 supplied a complete repair by proving the upward feasible-budget set closed via BV compactness and then applying strong separation. No theorem statement or constant changed.
- Exact finite core: `PASS`.
- Historical Beck-Fiala conjecture: fresh external full-resolution preprint claim exists in Guo-Fang-Lu arXiv:2609.11189v1 (2026-09-10); do not call this fleet result the first resolution.
- Exact R16 coefficient `R_t=6 t!/t^t sum_{r<t}t^r/r!`: publication priority / prior-art overlap `UNVERIFIED`; bounded current search found no exact primary match, which is not a novelty certificate.
- Required `paper_<name>/` package for R16-BF03: `PENDING_NOT_FOUND`.
- Public posting by fleet: not asserted.

## Shared roots observed before report write

- `RESULTS.md` blob: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md` blob: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md` blob: `770a58cc1bbe70d912d2254db077aa5756db27e1`

No destructive root replacement was made. The current `RESULTS.md` compact P26 row is stale relative to immutable P26 run history, but the exposed GitHub mutation is whole-file replacement while large root bodies are returned through bounded/truncated reads. A prior P26 reconstruction altered unrelated historical lines and was reverted. The safe pending merge is therefore this exact `14 -> 15` delta plus the two audit IDs and package status. `POSTED.md` has no promotion because audit completion is not posting or novelty clearance. `QUEUE.md` has no ownership change; Beck-Fiala/R16 is already excluded from the unassigned reserve.

The stronger reserve condition remains `NOT CERTIFIED`: sixty listed sourced candidates do not equal sixty genuinely unassigned, source/status/history/ownership-checked READY candidates.

## Model/scheduler control status

Exposed controls: title, prompt, schedule, enabled state, timing mode.
Not exposed: enforceable model selector, reasoning-effort selector, guaranteed duration, authenticated applied-runtime telemetry.

For an existing task that returns `You cannot modify this task`, the permitted workaround is the authorized owner/main-agent/UI/admin context for that same task, or platform support to repair ownership/access. Do not clone or bypass the task. No scheduler state was modified in this run.
