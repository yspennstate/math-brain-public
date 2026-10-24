# MOC4 source-bound handoff — account04/B08

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T091158Z-account04-B08-MOC4-r12`  
Status: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains OPEN / NOT PROVED / NOT DISPROVED.  
Execution: `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## Exact sources consumed

- Campaign lead: `proofnet24/collective-MOC4/account03/B07/20260922T074824Z-account03-B07-MOC4-r13/REPORT.md`, blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`, theorem `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.
- Assigned partner account01/B09: `proofnet24/collective-MOC4/account01/B09/20260922T074619Z-b09-moc4-r11/REPORT.md`, blob `09d12f95bbf37648773afe6ee08acf65343f149a`, theorem `MOC4-MIXED-SCHUR-GAP-CONDITIONING-CEILING-v1`.
- account03/B20: `proofnet24/collective-MOC4/account03/B20/20260922T084401Z-account03-B20-MOC4-r11/REPORT.md`, blob `197308f44d9e273a0d73ba89f691d3e85b4c23aa`, theorem `MOC4-MSQR-ORTHOGONAL-ROOT-FLOOR-v1`.
- account01/B07: `proofnet24/collective-MOC4/account01/B07/20260922T080631Z-account01-B07-MOC4-r13/REPORT.md`, blob `721ef994504083caf2a130649bdd4a03c4d9263f`, cross-root annihilator equation.

## New exact results

1. `MOC4-EXTERIOR-BLOCKROW-HALF-ENERGY-v1`. For any `2 x 2` block row of a genuine `O in SO(6)`, with `R_beta=||B_beta||_F^2/2` and `D_beta=det B_beta`,

   `E=sum_beta (R_beta^2-D_beta^2) <= 1/2`.

   Equality is exact: precisely two block Gramians are complementary rank-one projections and the third block vanishes.

2. Applying the assigned partner covariance payment gives the factor-two stronger mixed-Schur conditioning gate

   `16 h_e (gamma+r_tau)(gamma+r_tau^c) <= 1`,

   hence `gamma <= 1/(4 sqrt(h_e))`. Equality forces both participating exterior block rows onto the preceding two-rank-one boundary.

3. Combining the new ceiling with B20's two orientation payments gives the denominator-free residual anisotropy gate

   `|s_1(R)^2-s_2(R)^2| <= Lambda/(3 sqrt(h_e))`

   for every explicit adjacent-root cubic residual matrix.

4. `MOC4-C0-CROSS-ROOT-RANKONE-SPLIT-v1`. On the mixed-Schur `C=0` branch, write the nonzero rank-one kernel `Z*=rho x y^T`. The exact cross-root equation `cof(Z*)P+Z*Q=0` splits into

   `y_perp^T P=0` and `y^T Q=0`.

   Thus `rank P,rank Q <=1` and their column spaces are orthogonal. This strictly strengthens the previous exceptional conclusion `det Q=0`.

## Canonical delivery

Scientific report commit: `0193030ce0efb599ccdfa757ae023a8f85264b14`.  
Report blob: `a51e9a09e68c9d2c5f04f6a73f4a919f95ebb1df`.  
Verifier blob: `29bb6c1dbf371e6146a22aef69aba3efb182af26`.  
Verifier-output blob: `5d605fd1034e006bc6b29308fc1625d346ea82e6`.  
Verifier terminal marker: `PASS MOC4-B08-BLOCKROW-HALF-ENERGY-v1`.

## First unpaid implication

`MOC4-MSQR-SHARP-RESIDUAL-BOUNDARY-CLOSURE-v1`: exclude a positive-gap true-unitary mixed-Schur maximizer satisfying the lead full-Hessian/quartic reserve, B20 cross-root payments, the new sharp conditioning ceiling, residual anisotropy gate, same-unitary exterior compatibility and the exact `C=0` rank split. In the equality/near-equality conditioning regime exploit the two-rank-one-block boundary; away from it use the strict quantitative slack. The separate all-pair-negative-definite `NDI` branch remains after `MSQR`.
