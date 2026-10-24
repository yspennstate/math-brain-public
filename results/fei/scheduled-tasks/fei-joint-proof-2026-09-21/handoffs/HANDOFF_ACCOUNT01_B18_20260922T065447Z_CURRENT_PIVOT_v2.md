# FEI handoff — account01/B18 current-owner pivot

**Primary classification:** `CANDIDATE_REFUTED`.  
**Full FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Corrected scientific source:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T065447Z-two-level-anti-amplification/CURRENT_OWNER_PIVOT_CORRECTED.md`

at commit `3dc3688168fbabd58b8dd902ed3f6e1510f1a1eb`.

The later OWNER MESSAGE asks whether the current read-once base potential is worst on decomposable/AND gates or has a genuine gate demanding more. Exact peer work already settles this in the falsification direction.

Applied sources:

1. account04/B14 `20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`: Numaro's balanced 18-input source gate is composition-prime; all 262124 proper decomposition blocks fail the ANF rank-one criterion.
2. account03/B12 `20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`, blob `36fea824c2dcae8c65c3d485e5d5714899699855`: at `p_1=3/8`, all other biases `1/2`, output `967/2048`, the fixed `Gamma^dagger=Gamma_0+0.268204856 p(1-p)` has certified defect `-0.0176114199558...` and `W=1078193/4194304`.

With the source sign convention, the binding gate **maximizes**

`c_G = -D_{Gamma_0}/W`.

For this exact prime witness,

`c_G = 0.3367154558335169298319482272843...`,

far above the current AND/read-once correction floor `~0.0043974`; therefore AND/decomposable extremality for the current base potential is decisively false.

Any replacement `Gamma=Gamma^dagger+eta` must satisfy the exact witness affine constraint

`(57/256) eta(3/8) + (465/256) eta(1/2) - eta(967/2048) >= 0.0176114199558017537894958865691...`.

The earlier B18 depth-two selector files in the same run root are preserved as conditional calculations for the now-refuted `Gamma^dagger`; do not count them as current universal-candidate progress.

New first missing implication: construct a different symmetric nonnegative finite-cap all-gate potential respecting this prime-witness affine constraint while retaining the proved two-input/read-once inequalities. Test the replacement first on this exact 18-input gate and its one-coordinate bias line.
