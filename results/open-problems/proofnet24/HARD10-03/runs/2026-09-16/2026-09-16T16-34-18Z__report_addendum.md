# HARD10-03 addendum — immutable serialization correction and delivery receipt

Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum. The scheduler exposes no model selector or reasoning-effort selector.

This addendum is append-only. It does not overwrite the mathematical report, peer/history files, or shared ledgers.

## 1. Immutable serialization correction

Exact-commit readback of the main report found a text-serialization defect in two occurrences of the TeX command for a fraction in Section 4: the intended expression was rendered as `rac1{16e\log2}`.

The mathematical expression of record is

`epsilon_rep = 1/2 + (16 e log 2)^(-1)`.

Equivalently,

`epsilon_rep = 0.5331711153389402...`.

The surrounding derivation in (4.2) is intact and gives the same expression directly from

`(log 2)/2 + 1/(16e)`

as the natural-log rate per block. Dividing by `log 2` gives the corrected base-two exponent above. No theorem statement, hypothesis, event, scale map, or numerical value changes.

## 2. Exact self-check completed after the report

The exact-arithmetic self-check was executed and archived at

`proofnet24/HARD10-03/artifacts/2026-09-16T16-34-18Z__replica_cut_exact_check.py`.

Creation commit:

`b21c436f1ccc13e29a58913264fc6ef694a4e8a9`

Exact-create-commit readback blob:

`3813d01cd27f6ca629dcc7287ba6c9101c8e8e34`

The executed output is

`proofnet24/HARD10-03/artifacts/2026-09-16T16-34-18Z__replica_cut_exact_check.out`.

Creation commit:

`7f81889546f53e43983e5c98ac0c706c2640fb2f`

Exact-create-commit readback blob:

`a1fa692a588683ea4e3a5337b9364c8228315af6`

The output ends `ALL_EXACT_CHECKS_PASS` and certifies, using rational upper bounds on `e` and `log 2`, the coarse strict inequality

`epsilon_rep > 53/100`.

This is a self-check only; the theorem proof is on the main report page.

## 3. Main report and ledger delivery

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T16-34-18Z__report.md`

Creation commit:

`8f0b78082d884d4697d9cdf5ab28d4c28ddabb47`

Exact-create-commit readback blob:

`1681b2fdb17403a8438f9824b1f8841e7dd0b8d0`

Delivery status: **VERIFIED**, subject to the immutable formatting correction in §1 above.

Task-local ledger delta:

`proofnet24/HARD10-03/artifacts/2026-09-16T16-34-18Z__ledger_delta.yaml`

Creation commit:

`c7f9e518bcc563f2fe227d4d5f3ce3b69913ca44`

Exact-create-commit readback blob:

`56d795d683505fff619bce07f5ac1fd6fb00138e`

Delivery status: **VERIFIED**.

## 4. Scope check

- Source Tóth `d=3` conjecture: **OPEN**.
- Run status: **PARTIAL**.
- Frozen deterministic block-leakage exponent moved from `0.4723613755576205...` to the proved exact expression `1/2 + (16 e log 2)^(-1)`.
- Same frozen event, heat hypothesis, and scale map were retained.
- Physical finite-dependence orbit-propagating cube exponent: **UNMEASURED**.
- Explicit source-level `beta_0`: **NOT PROVED**.
- Positive-density macroscopic-cycle finite-box milestone: **NOT PROVED**.
- Infinite-volume `d=3` passage: **NOT PROVED**.
- P26 audit of the same full source claim: **MISSING**.
- Second distinct qualified-task audit of the same full source claim: **MISSING**.

No permission, approval, security, or usage denial occurred. No email/Gmail, Drive, public posting, paid compute, new schedule, force-push, access/settings/workflow changes, credential inspection, shared-ledger edit, or peer/history-file edit was performed.
