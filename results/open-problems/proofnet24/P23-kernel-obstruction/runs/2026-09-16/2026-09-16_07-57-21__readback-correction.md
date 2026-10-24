# ProofNet24 P23 — immutable readback correction

**Parent report:** `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_07-57-21__run-report.md`  
**Parent creation commit:** `5388e7620a95347fbbb6955170e87879209dac4b`  
**Parent report blob:** `483c14f1b475761a07b91335a1011bee700dcfa6`

Exact-commit readback of the parent report found one notation-only TeX transport defect in Section 6.1.

The displayed line rendered as

` s_0 = f(y_0)/y_0 = rac1{1+y_0} `

must be read as the ordinary algebraic identity

` s_0 = f(y_0)/y_0 = 1/(1+y_0). `

This is the only correction recorded here. It changes no theorem statement, inequality, constant, proof dependency, peer-audit verdict, or ledger status. In particular `P23-T3-ANNEALED-MULTIWINDOW-LIFT-42`, `P23-T3-ANNEALED-10WINDOW-42`, the exact rational constant `3882594969529/12500000000000`, and `P23-AUDIT-P04-SECOND-TOP-ONEDELETE-42` are unchanged.

The parent report was otherwise read back at its exact creation commit in contiguous ranges through end-of-file; the GitHub commit metadata records 1,494 additions and zero deletions.