# account04/B16 source-bound FEI handoff — cell-local quadratic MUX control

**Run:** `20260922T061055Z-account04-B16-fei-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI:** OPEN / NOT PROVED  
**Scientific package:** `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T061055Z-cell-local-mux-quadratic/` in `yspennstate/math-open-problems`  
**Scientific handoff commit:** `a08ecb7f2822e15d9ab6c75679f61b43f931bf45`

The live owner revision `2026-09-22.2` supersedes the old interface-C-only assignment where conflicting and directs all FEI workers to the all-gate reformulation. This run therefore attacked the live balanced unequal-MUX obstruction while preserving the older signed ledgers.

For balanced selector and same-side data, set
\[
p=(1-|1-q_0-q_1|)/2,\qquad
\rho=|q_1-q_0|/(1-|1-q_0-q_1|).
\]
If the three h96 source arguments `p`, `p(1-rho)`, `p(1+rho)` remain in one affine source cell of slope `sigma`, the exact midpoint loss is
\[
J_{\Gamma^\dagger}
=\frac{p\sigma}{2\ln2}
[(1-\rho)\ln(1-\rho)+(1+\rho)\ln(1+\rho)]
+a^\dagger p^2\rho^2.
\]
Thus the source loss is quadratic in relative data separation inside each cell.

For the current candidate `C^dagger=6.521851214`, `a^dagger=0.268204856`, the analytic bound gives
\[
\rho\le3/20\implies
D_{\Gamma^\dagger}(M)>0.0041127288\,p>0
\]
throughout every same-cell same-side region. The previous unconditional same-side collar was only `rho<=1/86`. If the source-cell slope is nonpositive, the gate is safe for every `rho<1`; more generally every cell with `sigma<=0.387748786` is safe for all relative separations.

Exact inherited interface-C sources re-read and preserved without reuse:

- account02/B16 `20260921T184541Z-actual-current-parent-mask-incidence`, theorem revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`;
- account03/B18 `20260921T185340Z-signed-flag-curvature`, theorem revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.

Their signed aggregation/orientation/opposite-sign overlap/dual-code multiplicity/negative-credit/terminal ledgers are untouched.

**Next decisive obligation:** source-knot crossing strips. Derive the exact two-adjacent-slope version of the midpoint formula using the committed h96 knots, rather than falling back to the global linear Lipschitz loss. This either closes the balanced same-side MUX plane or localizes a genuine all-gate falsification point.
