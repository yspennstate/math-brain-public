# ProofNet24 P20 — immutable logical wording correction for 2026-09-16 05:09:04 report

**Canonical report:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_05-09-04__run-report.md`  
**Report creation commit:** `b186666d4b26efeddbaa7ed14798ec7fa291e4e7`  
**Verified report blob:** `17df2aee8c6ef69b61dd27544132eec6ea732a00`

During adversarial post-readback checking, one sentence in Section 6 was found to overstate the logical direction of the new positive Ward identity. The report says that an order-one Jordan defect could occur "if, and only if" the affine--Jordan alignment is linearly large. The proved identity is

\[
e_2+2E\mathcal T_2=-\frac4dE\langle a,J(P_2)\rangle,
\qquad \mathcal T_2\ge0.
\]

The rigorous implication is only

\[
\boxed{
e_2=\Omega(1)
\Longrightarrow
-E\langle a,J(P_2)\rangle=\Omega(d).
}
\]

The converse is **not** proved: a linearly large negative affine--Jordan correlation could in principle be absorbed partly or entirely by the nonnegative leakage term `2E\mathcal T_2` while `e_2` remains small.

Therefore the corrected wording is:

> A linearly diverging negative affine--Jordan alignment is a **necessary**, not sufficient, condition for a persistent order-one Jordan defect under the new Ward identity.

No displayed theorem, formula, audit verdict, rank-two cubic balance, status classification, or next target changes. The sufficient direction used for the next attack remains valid:

\[
-E\langle a,J(P_2)\rangle=O(1)
\Longrightarrow e_2=O(d^{-1}).
\]

The original immutable report is intentionally not overwritten.