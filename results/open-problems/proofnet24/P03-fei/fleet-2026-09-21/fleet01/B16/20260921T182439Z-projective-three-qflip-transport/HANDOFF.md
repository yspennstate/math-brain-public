# B16 handoff — projective three-q-flip transport

**Full FEI remains OPEN.** Execution: `WITHOUT_VERIFIED_BRAIN`. No novelty claim.

For arbitrary translations `u,v,w`, let `A` be the three spectral-parity bits and `B` the three physical q-flip sensitivity bits. With
\[
\beta_f(t)=\frac{1-|E f(X)f(X+t)|}{2},
\]
the new sharp theorem is
\[
W_1^{Ham}(\operatorname{Law}A,\operatorname{Law}B)
\le 2\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}
\le \frac23(\beta_f(u)+\beta_f(v)+\beta_f(w)).
\]
Equivalently,
\[
|\tau_f(u,v,w)-c_f(u+v+w)|
\le4\min\{\beta_f(u),\beta_f(v),\beta_f(w)\}.
\]
The constants are sharp on a two-dimensional one-minority-vertex Boolean function.

The proof is projective: at rank three, twist by one character to minimize all three q-flip marginals simultaneously, then use the exact alternating cubic perturbation of the two three-bit laws and positivity of a one-bit slice. At rank two, the discrepancy is exactly plaquette frustration and the projective plaquette bound gives the same estimate. Rank at most one is exact.

For any weighted triple family with maximum physical coordinate incidence `L_*`,
\[
\sum_r\lambda_r W_{1,r}\le \frac{2L_*}{3}J(f).
\]
Thus the arbitrary-q-flip third-curvature source frame is now paid directly by the folded/original-coordinate budget once the compiler provides bounded triple incidence.

A stronger noise form needs only marginals, not independence: for any correlated triple `(U_p,V_q,W_r)` whose three marginals are physical product-noise laws,
\[
E W_1(U_p,V_q,W_r)\le2\min(p,q,r)J(f),
\]
hence
\[
\int_{[0,1/2]^3}\frac{E W_1}{pqr}\le6J(f),
\]
and the corresponding cubic-correlation defect costs at most `12J`.

The exact checker passed 951,328 function/triple instances (all Boolean functions through dimension three plus 200 deterministic dimension-four truth tables, every ordered translation triple).

**Next attack:** compute the three translation marginals induced by the actual pair-thinning/double-resolvent curl after same-syndrome signed aggregation. A bounded physical-incidence law or correlated product-noise marginals now close the source-side three-curvature payment. If neither holds on authentic compiler coefficients, retain more signed cancellation before taking the local transport norm.
