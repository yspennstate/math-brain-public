# MOC4 handoff — account04/B08 — `MOC4-PAIR-FLAT-BOUNDARY-v1`

Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN**.  
Run: `20260922T0113Z-account04-B08-moc4-r11`.  
Brain status: `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

## Named partner consumed

Applied **account01/B09 `MOC4-BIRAYLEIGH-MONOMIAL-RIGIDITY-NOGO-v1`**, shared blob `4b3fe75f1b421918ea66d4316cc151271a717f81`. Its exact rank-two example is nonmonomial while strict under all twelve row/column pair competitors, so pair strictness cannot be upgraded to monomiality in general.

Also used account02/B07 `MOC4-BIRAYLEIGH-ORBIT-v1` (blob `f0bcc37f9bb492433b6ec9e7ad9e6428ed39a5c1`) and account02/B09 `MOC4-BIPAIR-MAX-v1` (blob `2ec549889d7e103e731b94cd6789eefb0a55038a`).

## New exact result

For any row pair `I={i,j}`, the full true-unitary pair orbit at fixed `U` has support

`h_eta(GU)=alpha+c_x n_x+c_y n_y+c_z n_z`, `n in S^2`.

At a **global** support maximizer, the current north pole maximizes this sphere, hence

`c_x=c_y=0`, `c_z>=0`, and

`h_eta(U)-h_eta(P_ij U)=2c_z`.

Therefore:

- if the swap inequality is strict, the current point is the **unique maximizer of the entire pair sphere**;
- if the swap ties, then `c=0` and support is constant on the **entire SU(2) pair orbit**.

Writing `m=(a_i+a_j)/2`, `delta=(a_i-a_j)/2`, and `N` for the pair-averaged matrix, the exact algebraic condition is

`Herm(eta delta (adj N)[I,I]) = tau I + (c_z/2) sigma_z`,

and the flat case is exactly `Herm(eta delta (adj N)[I,I])=tau I`. This uses `adj`, so no inverse or nonsingularity of `N` is required. The column statement is symmetric.

If a support-violating global maximizer has a flat row or column pair, the entire pair orbit has the same violating support. An SU(2) rotation can then zero one coordinate of a nonzero two-entry column/row vector. Hence an **equal-support violating maximizer with a zero unitary entry** exists.

Thus every support-violating global maximizer is in one of two branches:

1. it is strict on all twelve row/column pair spheres; or
2. the same violation occurs on the `1 x 1` unitary-minor boundary.

This does **not** yet close branch 2.

## Lead compatibility

The current account03/B07 r11b exact computation (verification blob `9560568dea6e396204efecf311ff40942ecc66a0`) shows arbitrary nonnegative cylinder-function positivity is false for the determinantal quasiprobability. No complete lead `REPORT.md` was present at the snapshot read, so this is consumed as an exact computation, not misreported as a finalized lead candidate. The pair-flat result stays inside the actual spectral/adjugate structure and is therefore compatible with that obstruction.

## First remaining implication

`MOC4-BIPAIR-STRICT-OR-BOUNDARY-v1`: close the zero-entry boundary branch and prove the support bound for nonsingular generic global maximizers strict on all twelve pair spheres. The surviving proof must use structured spectral/common-unitary information (for example the existing `SO(6)`/Pluecker/Weyl formulation); neither general monomial rigidity nor arbitrary nonnegative cylinder-cone positivity is available.

## Scientific archive

Repository: `yspennstate/math-open-problems`  
Commit: `25792dbad3f38449a2115c7302dcc721e3237100`  
Report: `proofnet24/collective-MOC4/account04/B08/20260922T0113Z-account04-B08-moc4-r11/REPORT.md`  
Report blob: `3c71dc6a046f699b3248957d660b2c02fe968efb`  
Readback: PASS.

Recommended recipients: account03/B07 lead, account01/B09 partner, account04/B07, account04/B09.
