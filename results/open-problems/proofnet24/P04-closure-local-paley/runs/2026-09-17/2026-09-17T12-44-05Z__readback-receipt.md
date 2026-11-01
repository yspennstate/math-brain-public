# P04/I0101 immutable readback receipt — 2026-09-17T12:44:05Z

Canonical report:
`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T12-44-05Z__run-report.md`

- report creation commit: `30378fdb2fc244279fb2ae9ed1910ae84f8f8ad0`
- verified report blob: `af5f4643a24980c5dd3a9ca37bb1382fed11ccf1`
- exact-commit readback: PASS in contiguous overlapping ranges
- terminal marker `**End of complete run report.**`: FOUND
- frozen metric readback: `4049 -> 4049`
- complete exact domain readback: `{149,257,1009,4001,4013,4021,4049}`
- unchanged streak readback: `1 -> 2`
- methods readback: `B19 / B10 / B30`
- promoted structural claims readback:
  - `P04-I0101-ANHARMONIC-J-PARITY-23 = PROVED / STRUCTURAL-PARTIAL`
  - `P04-I0101-MAXDET-SPARSE-TANGENT-ODE-24 = PROVED / STRUCTURAL-PARTIAL`
- P11 audit readback: `P04-AUDIT-P11-I0062-ENDPOINT-AMPLITUDE-13 = PASS (CLAIM-SCOPED)`

Exact symbolic self-check:
`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T12-44-05Z__anharmonic_j_parity_exact.py`

- creation commit: `5f05e8a060bd356d65ee2c81709825c819eec8ff`
- verified blob: `ba0df6481ee5c4c6efab46027484032b409679d9`
- exact-commit readback: PASS

Archived self-check output:
`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T12-44-05Z__anharmonic_j_parity_exact.out`

- creation commit: `c56dc1ed7b0188e378eb882d3e34a481c753c703`
- verified blob: `4cbd94850594042786c0bb03640dae6f18f73c43`
- marker `P04-I0101-ANHARMONIC-J-PARITY-23-SELFCHECK=PASS`: FOUND
- `FLOATING_POINT_USED=NO`: FOUND

## Immutable-report presentation note

Exact readback found one TeX delimiter typo in the immutable report: the display defining `J(x)` in equation (4.1) is missing the closing `\]` immediately after `\tag{4.1}`. The intended display is unambiguous from the raw text and should read

```tex
\[
\boxed{
J(x)=\frac{(x^2-x+1)^3}{x^2(1-x)^2}.
}
\tag{4.1}
\]
```

No algebraic identity, theorem statement, proof step, checker, metric, or conclusion changes. The immutable report was not overwritten.

Receipt status: **COMPLETE_READBACK_VERIFIED_WITH_ONE_DISPLAY_TYPO**.
