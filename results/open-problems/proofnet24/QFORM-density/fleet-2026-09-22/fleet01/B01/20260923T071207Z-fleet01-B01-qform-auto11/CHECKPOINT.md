SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T07:12:07Z.
attacking: near-singular overlap-two pair bases via a weak-L2 scalar kernel and the aggregate sub-half-Riesz compiler.

# Early substantive checkpoint

The previous pair-log compiler deteriorated as a physical 2x2 base became nearly singular, while the exact rank-one endpoint was paid separately. The following calculation removes that discontinuity.

Let S={1,2}, K=S^c, write
B=A[S,S]=[[a,b],[b,c]],  a!=0,
M=A[S,K]=[u^T;v^T],  C0=A[K,K].
Set
  delta=c-b^2/a,
  z=v-(b/a)u,
  C=C0-a^{-1}uu^T,
  G=delta C-zz^T.
Completing the first physical coordinate gives
  Q=a(X1+(bX2+u.XK)/a)^2 + T,
  T=delta X2^2+2X2(z.XK)+XK^T C XK.
If delta!=0, completing X2 gives
  T=delta(X2+delta^{-1}z.XK)^2 + delta^{-1} XK^T G XK.

Scalar kernel claim: for every probability density f<=1, every h in R and q!=0,
  int f(x)| (x-h)^2-q |^{-1/2} dx <= 2^(7/4)|q|^{-1/4}.
Indeed k_q(x)=|x^2-q|^{-1/2} has weak-L2 norm at most 2^(3/4)|q|^{-1/4}; layer cake with int f=1 and f<=1 gives the extra factor 2.

Therefore, for delta!=0,
  H_{1/2}(T)<=2^(7/4) H_{1/4}(XK^T G XK).
Applying the completed fleet02/B01 global sub-half-Riesz theorem at beta=1/4 gives
  H_{1/2}(T)<=2^(7/4) C_off F(G)^(-1/8),
  C_off=5.095453495355205...
provided F(G)=sum_{k!=l}G_kl^2>0.

The exact compound-Schur identity is
  det(B)C0-M^T adj(B)M = aG.
Hence for the ordered overlap-two star
  W2(S)=sum_{k!=l} det A[S union {k},S union {l}]^2 = a^2 F(G).
The outer shifted-square kernel now yields the candidate uniform bridge
  ||p_Q||_infinity <= 2^(7/4)C_off |a|^(-1/4) W2(S)^(-1/8)
                    =17.1389943134... |a|^(-1/4)W2(S)^(-1/8),
with NO determinant or smallest-eigenvalue denominator. The delta=0 endpoint is already paid by the prior exact rank-one compiler with a smaller constant, so this would cover every pair base having at least one nonzero diagonal and W2(S)>0.

Remaining checks for the final report: prove the weak-L2 constant exactly for both signs of q; handle the null level set rigorously; apply the newest volume-stability source and the designated partner to concrete inequalities; refresh corrections before publication.
