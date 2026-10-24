SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T02:58:43Z.
attacking: apply the new fractional three-volume theorem with every marginal gate retained, then close the remaining span-aligned square/rank-two packet away from an exact Schur resonance.

# Early substantive checkpoint

Two calculations to complete rigorously in this run.

1. Let a genuine original-coordinate pivot d!=0 be completed as Q=d(Z+eta(W))^2+R(W). If a disjoint physical cross block M of the Schur remainder R obeys the new fractional three-volume hypotheses, then the source theorem gives ||p_R||_infinity <= H. The elementary potential split

  sup_y int p_R(s)|y-s|^{-1/2} ds <= 4 sqrt(H)

therefore yields ||p_Q||_infinity <=4 |d|^{-1/2} sqrt(H). Substituting H=3e/[(3-2q)sqrt(q)] E3(M)^(-1/6) gives a square-pivot fractional-volume bound with exponent E3^(-1/12), preserving all marginal gates.

2. In the r17 span-aligned packet

  Q=d z^2+2z(alpha^T x+beta^T y+c)+F(x)+G(y)+2x^T B y,

rank(B)=2, alpha in Col(B), beta in Row(B), d!=0. Completing the physical z-square changes the x-y cross block to C=B-alpha beta^T/d. Writing B=U Sigma V^T, alpha=Ua, beta=Vb and theta=b^T Sigma^{-1}a=beta^T B^+ alpha gives

  product_nonzero_singular_values(C)=Delta_B |1-theta/d|.

If d!=theta, C has exact rank two. The same projected-amplitude/bilinear-Plancherel argument used in r17 at rank three gives

  |phi_R(t)| <= min(1,2pi Delta_C^(-1/2)|t|^{-1}),

hence ||p_R||_3 <=6^(2/3) Delta_C^(-1/3). The square half-Riesz estimate then gives

  ||p_Q||_infinity <=16*3^(-1/4)|d|^(-1/2)Delta_C^(-1/4)
                   =16*3^(-1/4)[Delta_B |d(d-theta)|]^(-1/4).

Thus the only span-aligned case left by this mechanism is the exact scalar resonance d=theta. The final report will verify constants, state continuity separately, and apply the completed account04/B02 zero-diagonal-triple theorem to a genuine residual-square inequality.
