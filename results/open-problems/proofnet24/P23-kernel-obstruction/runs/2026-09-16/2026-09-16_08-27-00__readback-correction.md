# ProofNet24 P23 — immutable readback correction / receipt

**Parent report:** `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_08-27-00__run-report.md`  
**Parent creation commit:** `9d2e1c0dd8f6e67cca5082462d0db85ba5e88b5d`  
**Parent report blob:** `50de1e217c37eb12452f35e97d793d50b309c53d`

The parent report was read back from the exact creation commit in contiguous ranges through end-of-file. The theorem statements, proof sections, peer audit, ledger, and delivery checklist are present. Exact-commit readback found four notation-only TeX transport defects. The immutable parent is not overwritten; the intended readings are recorded here.

1. In Section 6, the line rendered as

`f(y_{-A})/y_{-A} = rac1{1+y_{-A}}`

must be read as

`f(y_{-A})/y_{-A} = 1/(1+y_{-A})`.

2. In the same Section 6 paragraph, `nabla Q(f(y))` must be read as the gradient notation `∇Q(f(y))`.

3. In equation (10.14), the rendered term

`- rac{4d}{m-1}`

must be read as

`- 4d/(m-1)`.

4. In equation (10.15), the same rendered term

`- rac{4d}{m-1}`

must likewise be read as

`- 4d/(m-1)`.

These are notation/transport corrections only. They change no theorem statement, inequality, constant, proof dependency, source identifier, peer-audit verdict, status ledger, or next-attack conclusion. In particular the following remain unchanged:

- `P23-T3-ANNEALED-BILATERAL-43 = PROVED`;
- `P23-T3-ANNEALED-ARCHITECTURE-43 = PROVED`;
- the exact rational Target-3 certificate `3882594969529/12500000000000`;
- the stronger analytic architecture lower bound `mathfrak C_infty(r_*)`;
- `P23-AUDIT-P26-INVERSE-DIAGONAL-JORDAN-43 = PASS`;
- P04 Target 3 remains `PROVED / AUDIT-CLOSED`;
- P04 Target 4 and `e_2=O(d^-1)` remain `OPEN`.

No email/Gmail action was used.