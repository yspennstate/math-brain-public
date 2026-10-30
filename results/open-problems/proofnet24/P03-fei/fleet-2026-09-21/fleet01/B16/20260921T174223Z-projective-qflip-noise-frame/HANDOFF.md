# B16 handoff — projective q-flip metric and noise-frame payment

**Full FEI remains OPEN.** Execution: `WITHOUT_VERIFIED_BRAIN`. No novelty claim.

This run closes a source-side gap in the arbitrary-q-flip frame reduction.

For every Boolean phase and translation `u`, define
\[
\beta_f(u)=\min\{I_f(u),1-I_f(u)\}=\frac{1-|c_f(u)|}{2}.
\]
Then `beta_f` is a translation pseudometric:
\[
\beta_f(u+v)\le\beta_f(u)+\beta_f(v).
\]
Hence, in physical coordinates, `beta_f(u)<=sum_{i:u_i=1} beta_f(e_i)` and `J(f)=sum_i beta_f(e_i)` is a path budget for every q-flip direction.

With `E_u=I_u(1-I_u)=beta_u(1-beta_u)`,
\[
E_u^2\le\frac4{27}\beta_u.
\]
Combining this with the existing arbitrary-pivot central source bound `S_u<=E_u^2/40` gives
\[
\sum_u\lambda_u S_u
\le\frac1{270}\sum_i\beta_i\sum_{u:u_i=1}\lambda_u.
\]
Thus a compiler pivot measure with maximum physical weighted incidence `L` is paid by `L J/270`.

For edge pivots `u_ab=h_a+h_b`,
\[
\sum_{a<b}\lambda_{ab}S_{h_a+h_b}
\le\frac1{270}\sum_a d_a\beta(h_a),
\quad d_a=\sum_{b\ne a}\lambda_{ab}.
\]
This converts the newest parity-current bridge into a weighted **vertex-load** obligation.

For product-noise directions `U_p` in the original physical basis,
\[
E\,S_{U_p}\le\frac{p}{270}J,
\qquad
\int_0^{1/2}\frac{E\,S_{U_p}}p\,dp\le\frac{J}{540}.
\]
So a positive product-noise mixture with bounded first moment is automatically a dimension-free q-flip frame.

A second source lemma controls the exact dependent-face transport itself. For
\[
P_f(u,v)=p_u(v)
=\Pr[f(X)f(X+u)f(X+v)f(X+u+v)=-1],
\]
\[
P_f(u,v)\le2\min\{\beta(u),\beta(v),\beta(u+v)\}.
\]
Consequently, for independent physical product-noise directions `U_p,V_q`,
\[
E P_f(U_p,V_q)\le2\min(p,q)J,
\]
and the double inverse-noise payment is finite with an explicit constant:
\[
\int_0^{1/2}\!\int_0^{1/2}
\frac{E P_f(U_p,V_q)}{pq}\,dp\,dq\le2J.
\]

The exact checker for the main theorem exhausts all 65,812 Boolean functions through dimension four: 16,793,872 projective triangle instances, 1,050,696 scalar capacity instances, and 263,008 product-noise instances; PASS.

**Next attack:** take the actual fully refunded parity-current pivot measure after same-syndrome signed aggregation and compute either (a) its physical weighted incidence, or (b) a positive product-noise-mixture representation. If either is dimension-free, the arbitrary-q-flip frame obstruction closes immediately by the formulas above. If authentic compiler coefficients force growing incidence, preserve that as the rigorous obstruction and retain more signs before squaring.
