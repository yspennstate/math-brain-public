# MOC4 source-bound handoff — account03/B08 — 20260922T0638Z

Run: `20260922T062315Z-account03-B08-moc4-r11`  
Outcome: **AUXILIARY_ONLY** with a mechanism pivot to the campaign lead's live zero-entry branch. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific report: `proofnet24/collective-MOC4/account03/B08/20260922T062315Z-account03-B08-moc4-r11/REPORT.md` in `yspennstate/math-open-problems`, latest report commit `ad5cb2c1f6b674a0fbd8e4789d260d89e3c93162`, report blob `763f018f7d41fe9aa5eb76b06f09e9369b2649c0`. Exact verifier blob `bcae0104d6680be45047764a554b11b0be9789bf`; captured exact output blob `895c68203c6837bd5f95f34a007959c9b2c593be`.

## Named partner consumed and applied

Consumed the assigned OTHER-account partner account04/B09 `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`, shared blob `b43dadfd41d8c061a3c6a0690c84e884c1e225f0`, and its full canonical report. The exact pair-circle theorem says a serious true-unitary support maximizer must satisfy continuous stationarity, not merely endpoint gates. I applied that criterion by constructing an explicit rational true-unitary support-increasing rotation of the candidate below.

Also consumed the campaign lead account03/B07 `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`, shared blob `e8be78c7c511c05966e55ca471c2ac6f2130546c`. It makes the zero-entry face a live target branch: mixed-Hessian saturation of a hypothetical support violator transports at equal gap to a genuine zero-entry unitary.

## New exact chart: `MOC4-ZERO-FACE-U3xU3-CHART-v1`

Every true `4 x 4` unitary with one zero entry can, after row/column permutations, be written with `u_44=0` as

`U(V,W) = [[V P W*, V e3],[(W e3)*,0]]`, `P=diag(1,1,0)`,

for some `V,W in U(3)`. Proof: write `U=[[C,y],[z*,0]]`; unitarity gives `Cz=0`, `C* y=0`, `CC*=I-yy*`, `C*C=I-zz*`, and unit `y,z`. Taking `V e3=y`, `W e3=z`, the upper `2 x 2` block of `V* C W` is unitary and can be absorbed into `V`. Conversely the displayed form is unitary. This is a true-unitary coordinate chart, not a bistochastic surrogate.

## Exact dense zero-face stress datum

For

`a=(-12+13i,1-24i,-22+12i,1-19i)`,

`b=(7+11i,-18-5i,-7+24i,10-13i)`,

and an exact rational-complex chart unitary with only `u_44=0`, the determinant is

`D=681177468907/9965689-(540878230401/9965689)i`.

For the one common support direction

`L(z)=-158949 Re(z)-904287 Im(z)`,

exact enumeration of all 24 target vertices gives

`M=54642495840`, attained only at `1423` and `2431`, and exact gap

`M-L(D)=163713444895903416/9965689>0`.

The normalized gap is

`6821393537329309/446580733297283910 ~= 0.015274715250172653`.

This is **not** a counterexample. An exact nonnegative three-vertex Caratheodory certificate places `D` in `conv(v_1234,v_1243,v_1423)`.

## Partner stationarity test rejects the candidate

A genuine exact left row-plane rotation preserving `u_44=0`, with rows `2,3` and rational half-angle `t=-1/1000`, increases the same common support by

`130344534495211750236720000/9965708931387965689 > 0`.

Hence the candidate is not a zero-face local maximizer and cannot be the support-violating global maximizer targeted by the partner theorem. The improved point still has strictly positive target gap and an exact three-vertex hull certificate (`1423,3421,4312`).

## Next exact obligation

`MOC4-ZERO-FACE-STATIONARY-ADVERSARY-v1`: enforce genuine left/right `U(3)` stationarity in the exact `U(V,W)` chart before searching for a negative common-direction gap, or prove that every such stationary zero-face point obeys the 24-vertex support bound. The lead's inherited transverse Hessian-nullity from saturation should be combined with these zero-face equations and same-unitary `P/R/D` constraints. A negative formal coefficient remains irrelevant unless it comes with actual spectra, a true unitary and one common separating direction.

No singular/repeated-spectrum closure is claimed in this run; the chart itself has no simplicity or nonsingularity hypothesis. No target proof or disproof is claimed.
