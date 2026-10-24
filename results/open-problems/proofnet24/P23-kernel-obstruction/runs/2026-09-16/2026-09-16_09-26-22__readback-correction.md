# ProofNet24 P23 — immutable readback correction / receipt

**Parent report:** `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_09-26-22__run-report.md`  
**Parent creation commit:** `d4f4a4afdf556d632ec1604738ffdb50882ef901`  
**Parent report blob:** `90d63b34828d605a057ef17465eba87a410dd71b`

The parent report was read back from the exact creation commit in contiguous ranges through end-of-file and also fetched directly by the returned blob SHA. The theorem statements, complete proof sections, source ledger, peer audit, finite checks, cumulative status table, remaining obligations, and delivery checklist are present.

Exact-commit readback found one notation-only TeX transport defect in the executive summary, Section 0.5. The immutable parent report is not overwritten.

The line rendered as

`E_{Q_P}K_P^p =rac12E_\mu R_P^{1-p}`

must be read as

`E_{Q_P}K_P^p = \frac12 E_\mu R_P^{1-p}`.

The same identity is rendered correctly later in Section 6 of the parent report, where its proof and use are given. This is therefore a notation/transport correction only. It changes no theorem statement, constant, proof dependency, peer-audit verdict, status ledger, or next-attack conclusion.

In particular, all of the following remain unchanged:

- P04 Target 3 is `PROVED / AUDIT-CLOSED` at the exact expectation level;
- the explicit rational certificate `3882594969529/12500000000000` is retained;
- `P23-T4-LOW-JORDAN-PAIR-DENSITY-44 = PROVED`;
- `P23-T4-LOW-JORDAN-SELECTED-PIVOT-44 = PROVED`;
- the actual-plane good-tail event has failure probability at most `256/d + 512 d^(-1/755)`;
- conditional selected reciprocal-pivot moments of every order `q<2` converge in probability to the inverse-`chi_4^2` moments;
- unconditional moments of every order `q<3/2` converge, using the previously proved all-plane negative-moment theorem;
- `P23-AUDIT-P20-SHARED-FACTOR-PIVOT-44 = PASS`;
- all-plane `L^p` control at `p>=3/2` remains disproved by the exact shared-factor plane;
- P04 Target 4 and the Haar-scale endpoint `e_2=O(d^-1)` remain `OPEN`.

No email or Gmail action was used.