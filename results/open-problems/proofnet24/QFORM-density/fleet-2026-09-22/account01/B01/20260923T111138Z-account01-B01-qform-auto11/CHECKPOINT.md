SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T11:11:38Z.
attacking: a one-source-square frequency-averaged compiler for rank-two physical cross packets, using account02/B01's scalar L4 square-phase theorem and two-dimensional original-coordinate Plancherel.

# Early substantive checkpoint

Status: WORKED PARTIAL DERIVATION; full QFORM still open.

Let original coordinates split disjointly as P={p1,p2}, Z={z}, J, W. Condition on X_W=w. Suppose

Q_w(U,Z,Y)=q_w(U)+2 U^T K Y + a Z^2 + ell_w(U) Z + G_w(Y),

where U=(X_p1,X_p2), Y=X_J, a!=0, rank(K)=2, and there are no Z-J quadratic couplings. The blocks P-P, J-J, P-Z, all W couplings, and all induced affine terms are otherwise arbitrary. Put Delta=sigma_1(K)sigma_2(K).

Designated partner input: account02/B01 at math-open-problems commit 8a1e6a8429cc6895c7f06c885bd372a29bb341e0 proves uniformly in the linear term

  integral_R |E exp(it[a Z^2 + ell Z])|^4 dt <= 27 pi/(2|a|).

For m(u)=f_p1(u1)f_p2(u2) and

  h_(t,w)(u)=m(u)e^{it q_w(u)} E_Z e^{it(aZ^2+ell_w(u)Z)},
  A_w(t)=||h_(t,w)||_2,

Cauchy/Jensen with integral m^2<=1 gives

  integral A_w(t)^4 dt <= 27 pi/(2|a|).

Averaging w preserves the L4 bound by Minkowski.

Push the complex leaf phase e^{itG_w(Y)} through L=2 K Y. The two-dimensional product-projection bound gives ||p_L||_infinity<=1/(2 Delta), hence its complex pushforward eta has ||eta||_2<=(2 Delta)^(-1/2). Two-dimensional Plancherel in the ORIGINAL U coordinates then gives

  |phi_Q(t)| <= min{1, sqrt(2) pi Delta^(-1/2)|t|^(-1) A(t)}.

Therefore for T>0,

  integral |phi_Q(t)|dt
  <= 2T + sqrt(2)pi Delta^(-1/2)(27pi/(2|a|))^(1/4)
            * 6^(3/4) T^(-1/4).

Optimizing T should give the homogeneous bound

  ||p_Q||_infinity <= [15/4 * 12^(1/5)] Delta^(-2/5)|a|^(-1/5)
                    = [15/4 * 12^(1/5)] (Delta^2 |a|)^(-1/5),

with an L1 characteristic function and hence a continuous C0 density. Constant and all scope details will be checked in the final report.

Connection to the current volume-stability source c2414ef633b9d4b7f04a83e1aeefbe713ed82bba: its two-large-singular-directions-plus-tail theorem has T2=sum_(j>=3)s_j(K)^2 and is silent for exact rank two (T2=0). The present derivation would pay that exact rank-two branch whenever a source-disjoint physical square satisfies sigma_1(K)^2 sigma_2(K)^2 |a| >= eta^5, with density <=(15/4)12^(1/5)/eta, while retaining arbitrary nonseparable J-J curvature.
