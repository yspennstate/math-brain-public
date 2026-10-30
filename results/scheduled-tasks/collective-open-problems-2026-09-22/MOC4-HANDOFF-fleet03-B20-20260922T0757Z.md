# MOC4 source-bound handoff — fleet03/B20

Run: `20260922T074718Z-fleet03-B20-MOC4-r11`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific source: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/fleet03/B20/20260922T074718Z-fleet03-B20-MOC4-r11/REPORT.md`, written in the scientific lineage ending at commit `bb50e416e732f881c9e29e7cda0855d8ebd4d5aa` after report + exact calibration verifier + output.

Consumed exact lead: fleet03/B07 `20260922T064004Z-fleet03-B07-MOC4-r12`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`, `MOC4-KERNEL-QUARTIC-RESERVE-v1`.

Consumed assigned OTHER-account partner: fleet04/B09 `20260922T060924Z-b09-moc4-r12`, report blob `d61d1dae159fd54105764b822385ba7389f0bddb`, `MOC4-ROOT-SATURATION-EXCLUSION-v1`.

Also used compatible fleet04/B07 `20260922T071214Z-fleet04-B07-MOC4-r14`, `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`.

New theorem: **`MOC4-GLOBAL-LS-CROSS-SPLIT-PAYMENT-v1`**.  At a true-unitary global support maximizer, let one genuine Spin(4) pair slice contain a mixed-Schur Hessian-kernel vector.  Split the full SU(4) tangent Hessian `A=-H >= 0` into pair/complement blocks

`A=[[A0,C],[C^T,D]]`, cubic covector `ell=(u,v)`, and set

`Sigma=D-C^T A0^+ C`, `g=v-C^T A0^+u`.

Then the full Lyapunov-Schmidt reserve decomposes exactly as

`<ell,A^+ell> = u^T A0^+u + g^T Sigma^+ g`.

Thus in fleet04/B07's simple mixed-Schur SVD notation,

`R_pair + R_cross <= A B delta`, `R_cross=g^T Sigma^+ g >= 0`.

For every transverse tangent direction `w`,

`(g.w)^2 <= (A B delta-R_pair) (w^T Sigma w)`.

If the known pair reserve saturates, then the full same-unitary cross-split identity

`v=C^T A0^+u`

is forced.  This is not the previous same-pair trust-region reformulation: it is the exact nonnegative reserve from the other SU(4) tangent directions.

Next exact obligation: **`MOC4-MIXED-SCHUR-CROSS-SPLIT-EVALUATION-v1`**. Express `C`, `v`, and `Sigma` in the campaign's existing Spin(6)/spectral variables for all six left/right pair choices; combine the scalar cross-payment inequalities with fleet03/B09's 144 same-unitary cofactor identities and endpoint roofs. Exclude every mixed-Schur candidate by an overdraw of pair slack, or produce a true-unitary/spectrum witness satisfying all constraints with positive support gap. The separate all-negative-definite `NDI` branch remains open.
