# Independent review of GLOBAL_REFLECTION.md

**Verdict: passes as a restricted internally proved theorem, subject to two proof-presentation repairs below.** I checked the proposed law against `agents/h01_entrance.md`, the prior `BOUNDARY_GRID.md`, `MACRO_COMPACTNESS.md`, `agents/g01_sliding.md`, and the prior relay/reflection result. I found no counterexample to the global fixed-horizon reflected law when \(0<\rho<1\) and the initial residual belongs to the strict double-sliding cone. This does not close T384 for other initial cones, more inputs, or test predictions.

The Volterra system has a standard pathwise uniqueness proof: the running-minimum reflection map is 2-Lipschitz on every prefix, its inputs are integrals of \(r\), and the right side has a Volterra Lipschitz bound with the finite random coefficient \(\|C\|+(P_1+P_2)O_\rho(1)\). Picard/Gronwall yields a global locally Lipschitz path. The signs and coefficients in (V) check: a positive-\(z\) survivor contributes \(z^2(u,v)\) to output; a negative-\(z\) survivor contributes \(-z^2(v_-,u_-)\). Each sign population is an independent thinning of the marked PPP with probability \(1/2\), giving the stated independent \(\alpha/2\)-stable \(P_1,P_2\), also independent of \((F,C)\).

**Repair 1: prove mixed-sign invariance before any endpoint selection.** Every subsequential limit in the prior macro theorem satisfies \(r'=-Q_{\rm eff}r\), where
\[
Q_{\rm eff}=C+\sum_i z_i^2D(\theta_i)G D(\theta_i).
\]
The series is bounded on each path by \(\|G\|\sum_i z_i^2<\infty\), and \((Q_{\rm eff})_{12}\ge0\): \(C_{12}\ge0\) because its ray vectors are coordinatewise nonnegative, and \(G_{12}=\rho>0\). With \(s=(-r_1,r_2)\),
\[
s'_1=-(Q_{\rm eff})_{11}s_1+(Q_{\rm eff})_{12}s_2,\qquad
s'_2=(Q_{\rm eff})_{12}s_1-(Q_{\rm eff})_{22}s_2.
\]
The positive orthant is invariant for this bounded Metzler system; indeed \(s_j(t)\ge s_j(0)e^{-K_*t}>0\) for a finite pathwise \(K_*\). This applies to **all** unselected inclusion limits. It removes any possible circularity between proving survivor support and using the selected reflected action to exclude a mixed-sign exit. The same calculation later verifies the explicit selected law.

**Repair 2: make the finite-cutoff and atomwise continuation quantifiers explicit.** For a finite deterministic marked cutoff, each frozen survivor/dead atom has a finite random critical-step certificate. Localize its maximum index by a deterministic \(N\) with probability tending to one as \(N\to\infty\); only then apply the fixed-\(N\) boundary-grid theorem and its threshold-null continuity. Localize the residual cone and macro bounds so these certificates persist through a common short *physical* interval for that finite set. The changing-weight sliding lemma then identifies each survivor there, while the macro small-atom estimate removes omitted rows. Use the prior joint countable cutoff extraction to obtain the result simultaneously for every PPP atom; there is no need for a common \(N\) or support margin across the infinite population.

For an individual positive-\(z\) survivor, pick \(0<\delta\) in the established local interval. Its supporting projection \(q_2(\delta)>0\). On the interval before its hypothetical first later support zero, the scalar relay has \(a=zr_1<0\), \(c=\rho zr_2>0\), so the run012528 uniqueness result identifies its normal coordinate with the nonnegative reflected path. The exact tangential cancellation, valid from time zero while support is open, gives
\[
q_2(t)=\rho q_1(t)+(1-\rho^2)z\int_0^t r_2(s)ds>0
\]
at that alleged first zero. This contradiction proves support persistence for that atom. For \(z<0\), the mirror identity is \(q_1(t)=\rho q_2(t)-(1-\rho^2)|z|\int_0^t r_1(s)ds>0\). Countable intersection handles all survivor atoms. Dead atoms remain exactly dead at finite width once both gates are strictly off. These arguments identify the macro residual identity with (V) over every fixed horizon; uniqueness then removes subsequences. At no point is a common positive support margin across atoms required.

On the zero set of a reflected normal coordinate, its derivative vanishes almost everywhere. The output action there is the Schur diagonal; where the normal is positive it is \(G\). Both matrices are PSD with nonnegative off-diagonal, so the selected-law energy and sign claims check. The fixed Schur matrix \(Q=C+(1-\rho^2)\operatorname{diag}(P_1,P_2)\) is valid only until first ratio-cone exit. Such an exit has positive probability; `agents/h03_audit.md` gives an explicit positive-probability construction. The reflected law correctly permits release and recapture thereafter, so the example is a scope check rather than a counterexample.

With those repairs stated, I see no unpaid interchange of fixed finite boundary steps with \(O(L)\) steps: the prior macro theorem supplies the growing-horizon tightness and small-atom estimates, while the local strict certificates and scalar relay identify its subsequential limits. The conditional formulation using the finite-width cone event is valid because the limiting residual has a full-dimensional continuous density and the cone boundary is null.
