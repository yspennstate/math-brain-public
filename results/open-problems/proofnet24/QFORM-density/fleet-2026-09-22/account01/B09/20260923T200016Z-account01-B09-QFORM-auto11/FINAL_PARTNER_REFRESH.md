# Final partner refresh — account01/B09 20260923T200016Z

A newer completed designated partner report landed after the earlier late-source note:

`yspennstate/math-open-problems@65ed9ea70175fb28541d756aea01f6aeb491fd6c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T201318Z-account02-B09-QFORM-r14/REPORT.md`,

theorem `QFORM-3x2-KERNELDERIVATIVE-L1-v1`.

This report supersedes only the freshness label on the partner application in `LATE_SOURCE_NOTE.md`; the earlier r20 application remains valid.

## Actual inequality from the newest completed partner theorem

Take original physical coordinates `(Y1,Y2,Y3,Z1,Z2)` and

`Q_1 = 2Y1Y3 + Y3^2 + 2Y1Z1 + 2Y2Z2`.

For the partner theorem,

`L={Y1,Y2,Y3}`, `R={Z1,Z2}`,

`P=[[0,0,1],[0,0,0],[1,0,1]]`,
`C=[e1,e2]`.

Hence

`w=e3`, `Delta=||w||=1`,
`P w=e1+e3`, `||P w||=sqrt(2)`.

The `(Y2,Z2)` block contributes eigenvalues `{1,-1}`. The `(Y1,Y3,Z1)` block contains the principal pair `[[0,1],[1,0]]`, so interlacing gives one eigenvalue >=1 and one <=-1. Therefore the full matrix has at least four eigenvalues of modulus >=1 and is target-valid.

Account02/B09 r14 gives a continuous density and

`||p_(Q_1)||_infinity
 <= C_KD (||w|| ||P w||)^(-1/5)
 = 6.834830666196632 * 2^(-1/10)
 = 6.3771225031289545
 < 6.378`,

and therefore for every interval `J`,

`P{Q_1 in J}<6.378 |J|`.

This is a literal source-coordinate 3x2 bilinear-block payment with arbitrary cap-one independent input laws and no square-root decoupling loss. It also bridges nonzero kernel curvature and the exact kernel-shear endpoint without a case split.

## Relation to the new account01/B09 theorem

The partner r14 theorem attacks a concentrated physical 3x2 packet through the exact invariant `||w|| ||P w||`. This run's `QFORM-RESIDUAL-STABLE-CARRIER-CROSSING-v1` instead pays the diffuse/global carrier side by producing a literal coordinate cut with a quantitative third cross singular value and then using the no-marginal D3 receiver. The two mechanisms are complementary: the remaining B09 frontier should promote genuinely localized strong spectral directions until a 3x2/fixed-pair/grouped-hub packet appears, while the diffuse remainder is paid by the balanced-crossing theorem.

Full unrestricted QFORM and full-target continuity remain OPEN.