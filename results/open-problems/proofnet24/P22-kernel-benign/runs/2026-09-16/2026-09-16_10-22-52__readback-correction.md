# ProofNet24 P22 — exact-SHA readback receipt and transport correction

**Canonical report:** `proofnet24/P22-kernel-benign/runs/2026-09-16/2026-09-16_10-22-52__run-report.md`  
**Creation commit:** `866cbe22f81e94656990ff764bd362ac0cf8d1df`  
**Verified report blob:** `17a09fd22af5f4ba97c00eb88b0a4702c19e358b`  
**Readback ref:** exact creation commit `866cbe22f81e94656990ff764bd362ac0cf8d1df`  
**Delivery:** GitHub only; no email/Gmail action.

The canonical report was read back from the exact creation commit in contiguous ranges covering its opening metadata and executive theorem, repository/source state, full Target-2 dependency audit, new U-statistic trace concentration theorem, new actual high-tail second-order trace theorem, consequences and falsifications, independent P20 transversality audit, primary-source verification, failures/limitations, cumulative ledger, next attack, and final verdict. A read starting at line 1461 returned empty content, confirming the report endpoint lies before that line.

Readback exposed one UTF-8/escape transport typo in two *repetitions* of the new high-tail formula: in Section 6.1 equation (6.1) and in the final displayed restatement, the TeX command `\frac` lost its initial `\f`, rendering `rac{n\zeta}{\tau^2}`. This is a presentation-only transport defect. The theorem is stated correctly in the executive equations (0.2)--(0.3) and proved correctly in equations (5.19)--(5.21).

The exact intended correction in both affected repetitions is

\[
\operatorname{Tr}(T^{-1}ST^{-1})
-\frac{n\zeta}{\tau^2}
\sim_P\left(\frac n{N_{d,k}}\right)^2.
\]

No mathematical statement, proof dependency, status, or coefficient changes. The immutable canonical report is not overwritten; this correction is appended as a separate immutable record in accordance with the shared protocol.
