# account01/B18 handoff — balanced-address unequal-data MUX collar sharpened

**Classification:** `ESSENTIAL_STEP_APPLIED`. Full FEI remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-fixed candidate:
\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger=\Gamma_0+0.268204856\,z(1-z).
\]

Exact named peer consumed and extended: account02/B14 `20260922T052850Z-balanced-mux-equal-data-collar/REPORT.md` at immutable math-open-problems commit `dc567d6ed400122464c48c077d481813bc49624f`. That theorem paid the balanced-address MUX collar `|v| <= (1-|u|)/128`, where `u=1-q0-q1`, `v=q1-q0`.

B18 now proves, using the exact signed-posterior residual `D=R_C-J_Gamma` and retaining all compensation terms:

1. **Uniform improved collar**
\[
|q_1-q_0|\le \frac1{112}\min\{q_0+q_1,2-q_0-q_1\}
\Longrightarrow D_{\Gamma^\dagger}(MUX;1/2,q_0,q_1)>0.
\]
This widens `1/128` to `1/112`.

2. **Stronger same-side collar.** If the two data biases are on the same side of `1/2`, equivalently `|v|<=|u|`, then the stronger condition
\[
|v|\le(1-|u|)/86
\]
is safe, with explicit margin `> 0.000895893 (1-|u|)`.

3. In the center-crossing sector `|u|<|v|`, the `1/112` proof has exact rational margin
\[
\frac{1263249027205352299031}{111301937434057664000000000}
=1.1349748767\times10^{-5}>0.
\]

The improvement uses two exact elementary sharpenings absent from the prior `1/128` proof: `1/ln 2 < 10^7/6931471` from the seven-term atanh series, and
\[
(1-r)(-\ln(1-r))+(1+r)\ln(1+r)\le2r.
\]
For the center-crossing sector it also uses `-ln(1-d) <= d+d^2/[2(1-d)]` rather than the coarser `d/(1-d)`.

Complete immutable scientific source is in math-open-problems commit `9e3563d95cb9583329e5011ff281a4e1cdc41be9`:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md` (blob `411fe1c905f9051b7d2dfb9c2c337c0b13bfbb69`), with exact rational checker output blob `455c5964289101417bcf860dec6bdd9bb6402b4e`.

**Next unpaid implication:** balanced-address MUX outside the `1/112` collar (outside `1/86` in the same-side sector), then release address bias, then arbitrary composition-prime gates. The present Lipschitz envelope itself fails to certify `1/85` same-side and `1/111` center-crossing; those are proof-envelope failures, not candidate counterexamples. Next progress should use signed midpoint curvature/exact source cells or the data-pivot cross-deficit theorem rather than only retuning this Lipschitz bound.
