# B16 handoff — balanced MUX becomes quadratic inside each h96 source cell

**Status:** `ESSENTIAL_STEP_APPLIED`, `WITHOUT_VERIFIED_BRAIN`, full FEI open.

Live all-gate candidate:
\[
C^\dagger=6.521851214,\quad
\Gamma^\dagger=\Gamma_0+0.268204856\,z(1-z).
\]

Consumed source-exact inputs:

- `fleet04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md` plus sharpened balanced collar continuation at commit `ad0f62b702b9301e401ac9102e8b85b140e26caf`;
- requested inherited interface-C source `fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`;
- requested inherited interface-C source `fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.

For the balanced-address same-side MUX, put
\[
p=(1-|1-q_0-q_1|)/2,
\qquad
\rho=|q_1-q_0|/(1-|1-q_0-q_1|).
\]
If the three logarithmic source arguments for `p`, `p(1-rho)`, `p(1+rho)` lie in one affine h96 cell with slope `sigma`, then exactly
\[
J_{\Gamma^\dagger}
=\frac{p\sigma}{2\ln2}
[(1-\rho)\ln(1-\rho)+(1+\rho)\ln(1+\rho)]
+a^\dagger p^2\rho^2.
\]
Thus the source loss is **quadratic rather than linear** in relative data separation inside a source cell.

Using `|sigma|<31`, the exact balanced-MUX reserve and the rational bound `1/ln2<10^7/6931471` gives
\[
\rho\le3/20
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(M)>0.0041127288\,p>0
\]
throughout every single-cell same-side region. This replaces the previous unconditional same-side collar `rho<=1/86` by a nearly 13x wider collar away from source knots.

Even stronger: if the containing source cell has `sigma<=0`, the MUX is safe for **all** `rho<1`, with residual coefficient at least `0.387748786 p`; more generally every cell with `sigma<=0.387748786` is safe for all relative separations.

**Next exact obligation:** enumerate the finitely many h96 knot-crossing strips and derive the two-adjacent-slope analogue of the exact formula. Do not revert to the old global `31*rho` Lipschitz loss. If those strips certify, the balanced same-side MUX plane closes; if not, they localize an authentic all-gate falsification candidate.

The inherited signed-current parent weights and signed flag curvature were not re-spent: orientation, opposite-sign overlap, dual-code multiplicity, negative credits, live-window/terminal terms remain at their earlier proved scopes.
