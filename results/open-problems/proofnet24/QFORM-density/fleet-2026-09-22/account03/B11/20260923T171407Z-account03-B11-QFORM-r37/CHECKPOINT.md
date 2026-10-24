SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T17:14:07Z.
attacking: the true-near-coloop two-bank endpoint; force the newest projected-crossing row-marginal gate and compute its exact determinant currency before the reciprocal estimate is paid.

# Early substantive checkpoint: exact projected-crossing currency in the near-coloop chamber

Work in exact rank three: A=R M R^T, R^T R=I_3, signature (2,1) or (1,2), and s=min |lambda(M)|. In the r36 true-near-coloop state write r_0=sqrt(c)e with c>63/64 and, for j!=0, r_j=s_j e+w_j with w_j perpendicular to e. Then sum w_j w_j^T=I_2, sum s_j w_j=0, and sum s_j^2=1-c.

A first new gate uses the completed designated-partner account04/B11 pair-area theorem. Since g_{0j}=||r_0 wedge r_j||^2=c||w_j||^2, if some h_j:=||w_j||^2>=1/36 then

    g_{0j} > (63/64)(1/36)=7/256,

and account04/B11 gives

    ||p_Q||_infinity <= 128 sqrt(2)/(s sqrt(g_{0j}))
                       < 2048 sqrt(2/7)/s
                       = 1094.7020469.../s.

Thus the remaining chamber may assume h_j<1/36 for every leaf.

For the determinant-pair law mu_{jk}=det(w_j,w_k)^2, its inclusion marginal is h_j and sum_j h_j=2. Hence two iid mu-pairs are disjoint with probability

    d_perp >= 1-sum_j h_j^2 > 1-2/36=17/18.

Randomly two-color the original leaf coordinates into S,T. Exactly as in r36,

    E[det G_S det G_T]=d_perp/16>17/288,
    G_B=sum_{j in B}w_j w_j^T.

So one literal original-coordinate split satisfies

    det G_S det G_T>17/288,
    lambda_min(G_S),lambda_min(G_T)>17/288.

In particular every within-bank transverse row has relative leverage

    w_j^T G_B^{-1}w_j < (1/36)/(17/288)=8/17<1/2.

This is precisely the row-marginal threshold required by the new weighted-subset/projected-crossing theorem.

Now put m=M e and ell_B=R_B m. For orientation I=S,J=T let

    P_T=I-ell_T ell_T^T/||ell_T||^2,
    C_ST=A_{S,T}P_T.

Let H_T=R_T^T R_T and write, in the splitting e direct_sum e^perp,

    H_T=[[tau_T,h_T^T],[h_T,G_T]],
    rho_T=tau_T-h_T^T G_T^{-1}h_T.

Then the following exact identity holds:

    Z_2(C_ST):=e_2(C_ST C_ST^T)
      = |det M|^2 det(G_S) det(G_T) rho_T / ||ell_T||^2.       (CP)

Proof sketch. Choose orthonormal U spanning m^perp and E spanning e^perp. Since z perpendicular m implies Mz perpendicular e, write M U=E K. In orthonormal bases (m/||m||,U) and (e,E), expansion along the first row gives |det K|=|det M|/||m||. Also C_ST=W_S K D_T^T with D_T=P_T R_T U. Thus Z_2=det(G_S)|det K|^2 det(D_T^T D_T). Schur complementation of H_T in the direction m/||m|| gives det(D_T^T D_T)=||m||^2 det(H_T)/||ell_T||^2. Finally det(H_T)=det(G_T)rho_T. Multiplication proves (CP).

The physical hub cross row into T is A_{0,T}=sqrt(c) ell_T. Therefore the hub singular product S_T=||A_{0,T}|| satisfies the cancellation

    S_T^2 Z_2(C_ST)
      = c |det M|^2 det(G_S)det(G_T)rho_T
      > (119/2048) s^6 rho_T.                                  (CANCEL)

The volume row marginals of rank-two C_ST equal the leverage scores of W_S, hence are <8/17<1/2. Therefore the newest one-hub/ell=2 projected-crossing compiler applies whenever rho_T>0 and yields

    ||p_Q||_infinity
      <= 3*2^(7/6)*e^(1/3) [S_T^2 Z_2]^-1/6
      < (15.103/s) rho_T^-1/6.                                 (INT)

The reflected orientation gives the same bound with rho_S. Consequently, if max(rho_S,rho_T)>=1/4096, this chamber has a continuous density with ||p_Q||_infinity<60.412/s.

This does not yet close the rho_S,rho_T ->0 interpolation. Equation (CANCEL) is also a sharp scope diagnosis for the new projected-crossing theorem here: its third projected crossing volume vanishes exactly with the bank longitudinal Schur variance. The next step is therefore the product-safe near-two-plane endpoint/interpolation, not another attempt to force the projected-crossing constant to remain nondegenerate.
