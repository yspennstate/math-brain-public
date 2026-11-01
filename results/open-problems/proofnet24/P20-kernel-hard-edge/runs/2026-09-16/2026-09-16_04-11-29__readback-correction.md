# ProofNet24 P20 — immutable readback correction for 2026-09-16 04:11:29 report

**Corrected report path:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_04-11-29__run-report.md`  
**Report creation commit:** `fc0ea6465560c1cfef769b6f94bd8be27e37a945`  
**Verified report blob:** `26ca7ece6dea97924be3547bb84e74b480c431d9`  
**Status:** notation/proof-line clarification only; no theorem statement, status, dependency, audit verdict, or next attack changes.

During complete readback, Section 4.3 equations (4.14)--(4.15) were mathematically correct but the prose immediately after (4.14) cited the wrong inequality direction for the final comparison to `beta_3`.

The report says the super-polynomial tail is bounded by `C beta_3` and mentions `beta_3<=rho`. The needed lower comparison is instead

\[
\boxed{\beta_3(A)=\sum_j|\lambda_j|^3\ge \rho(A)^3,}
\]

because one eigenvalue has magnitude `rho(A)`. Consequently, for sufficiently small `rho`,

\[
e^{-c\rho^{-2/3}}\le C\rho^3\le C\beta_3(A),
\]

and likewise

\[
e^{-c/\rho^2}\le C\rho^3\le C\beta_3(A).
\]

Thus the middle- and high-frequency bounds used to obtain

\[
\int_{\mathbb R}(1+|t|)\,|\psi_A(t)-e^{-t^2/2}|\,dt
\le C\beta_3(A)
\]

remain valid exactly as claimed. The separate true inequality `beta_3(A)<=rho(A)` is still useful elsewhere, but it is not the inequality that justifies the final tail-to-`beta_3` comparison.

The original immutable report is intentionally not overwritten. This correction is part of the run's canonical readback record.
