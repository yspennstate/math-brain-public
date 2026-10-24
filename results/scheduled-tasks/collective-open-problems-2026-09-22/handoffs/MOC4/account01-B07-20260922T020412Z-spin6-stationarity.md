# account01/B07 MOC4 handoff — exact Spin(6) stationarity balances

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T020412Z-b07-moc4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact scientific delivery

Private scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account01/B07/20260922T020412Z-b07-moc4-r11/REPORT.md`, report commit `ebf5fd79e719931fbacc23a12ce7c06a456c0019`.

Exact verifier creation commit: `507162df01bbbd674ecd6dfa48f6603e3c3a8248`.  
Captured exact output commit: `fbca9facc01fa9cc3ea90da03c548205a3e4726b`.

## Named OTHER-account result consumed

Assigned partner **account02/B08 `MOC4-REPEATED-MINIMAL-LIFT-v2`**, scientific commit `fab8368ce6b7854675947d7808cf85989623fbf8`: repeated-eigenvalue faces admit a smaller source-valid fractional orientation lift, with a strict collar away from the explicit zero-nonrepeated-row / supported-collinearity strata. This is used to keep the residual interior branch honest rather than silently discarding repeated spectra.

Also consumed: account04/B07 `MOC4-SPIN6-BLOCK-v1` (scientific commit `7dc542c7644686c649d19b90e7001a64be711355`) and account02/B09 `MOC4-BIPAIR-MAX-v1` plus its r12 exact six-fiber compression.

## New exact result

For the exact Spin(6) block objective

`Q(O)=sum_ab [ K_ab det(B_ab) + X_ab ||B_ab||_F^2/4 ]`,

put

`G_ab = K_ab cof(B_ab) + (X_ab/2) B_ab`.

For each distinct block-row pair `alpha,gamma`, define the 2x2 matrix

`N_ag = sum_beta [ G_ab B_gb^T - B_ab G_gb^T ]`.

Because `SU(4)->SO(6)` is onto, arbitrary off-diagonal 2x2 skew-block tangent directions are genuine unitary variations. Therefore every critical point, in particular every global support maximizer, satisfies the **complete nontrivial first-order system**

`N_12=N_13=N_23=0`.

The omitted three tangent directions rotate the individual 2-planes and are exact symmetries of Q.

Writing each real 2x2 block as `z -> m_ab z + n_ab conjugate(z)` and

`u_ab=X_ab/2+K_ab`, `v_ab=X_ab/2-K_ab`,

the objective is exactly

`Q=sum_ab [u_ab |m_ab|^2 + v_ab |n_ab|^2]`,

and stationarity is equivalently, for every `alpha<gamma`, the two complex equations

`sum_b [(u_ab-u_gb)m_ab conjugate(m_gb) + (v_ab-v_gb)n_ab conjugate(n_gb)] = 0`,

`sum_b [(u_ab-v_gb)m_ab n_gb + (v_ab-u_gb)n_ab m_gb] = 0`.

These equations retain the actual shared complementary-minor phases and do not assume a positive common permutation lift.

For the scalar block-plane mixing circle, the objective is exactly

`Q(t)=C + (H_ag/4) cos(2t) + (J_ag/2) sin(2t)`,

where

`H_ag=sum_b [2(K_ab-K_gb)(D_ab-D_gb)+(X_ab-X_gb)(R_ab-R_gb)]`.

Hence a global maximizer has `J_ag=0` and the entirely phase-free necessary inequality `H_ag>=0`. Summing all left-coordinate second variations yields the further exact maximizer condition

`4<D,K> + 3<R,X> >= sum_ab X_ab`.

## Exact application to the prior generic parity witness

The account01/B07 r11b true-unitary datum refuting the unconditional parity-slack gate is **not stationary**. Exact Gaussian-rational differentiation under the genuine row-pair `(1,3)` conjugation gives

`d/dt Re det(A+G_13(t) U B U* G_13(t)*)|_0 = 284796813152662076044041 / 244140644531250390625000 > 0`.

Thus that source-valid counterexample to the old proof gate cannot be a global support maximizer; it does not obstruct a maximizer-local proof.

## Compact conditional end-to-end chain

The exact target support inequality is the account02/B09 six-fiber inequality

`theta=<D,K>+<R,X>/2 <= max_rho {c_rho-2m_rho(K)}`.

If MOC4 fails in a fixed support direction, a violating global maximizer exists. The residual pair-strict maximizer must satisfy block orthogonality and the exact matrix stationarity balances above. Therefore the first interior implication is now:

**`MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`** — prove the six-fiber support inequality from true block orthogonality + `N_12=N_13=N_23=0` + the structured spectral form of `(K,X)` at a global maximizer.

This is source-faithful and strictly narrower than the already-refuted unconditional parity-slack, scalar-roof, positive common-lift and spectral-only upper-facet shortcuts. The separate lead branch `MOC4-ZERO-FACE-SUPPORT-v1` remains unpaid; no full-proof claim is made.
