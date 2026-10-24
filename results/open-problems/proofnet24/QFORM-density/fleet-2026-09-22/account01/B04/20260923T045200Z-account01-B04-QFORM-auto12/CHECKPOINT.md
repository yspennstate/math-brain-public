SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T04:52:00Z.
attacking: entropy-flattened two-volume smoothing after one original-coordinate square, and a ridge-to-two-volume bridge using account02/B04's virtual-volume identity.

# Early substantive checkpoint

Full target remains open. Current control readback: QFORM-only, owner revision 2026-09-22.15.

Let an original coordinate Z be independent of all remaining coordinates Y and suppose after scalar completion

Q = a (Z+d(Y))^2 + R(Y),  a != 0.

Choose disjoint original-coordinate banks I,J among Y and write M for the cross block of the quadratic part of R. Let Omega_2 be the nonzero 2x2 minors M[S,T]. For any probability weight w on Omega_2 define row marginals alpha_i=P_w(i in S), column marginals beta_j=P_w(j in T), and

G_2(w)=exp(H(w)+sum_(S,T) w_(S,T) log det(M[S,T])^2).

If max_i alpha_i <= 1/2, the k=2 version of the volume-weight Brascamp--Lieb calculation gives

|phi_R(t)| <= min(1, 2 pi sqrt(e) |t|^{-1} G_2(w)^(-1/4)).

Combining with the exact half-Riesz inequality used in account02/B04,

sup_x E|R-x|^{-1/2} <= (2 pi)^(-1/2) int_R |t|^{-1/2}|phi_R(t)| dt,

yields the explicit aggregate bound

||p_Q||_infinity <= 8 e^(1/4) |a|^(-1/2) G_2(w)^(-1/8).

This is the first substantive implication of the run. It uses two-dimensional exterior volume rather than selecting two individually large singular values. The full proof, dual optimization, partner virtual-volume bridge, and a target-valid rotated indefinite family will follow in REPORT.md.

Status: SUPPORTING_THEOREM_CANDIDATE / FULL_TARGET_OPEN / continuity not yet claimed.
