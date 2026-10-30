SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T16:08:24Z.
attacking: QFORM-SECONDANCHOR-CRITICAL-STABLERANK-RECEIVER-v1 by lifting D_k through an invertible physical anchor without shearing the residual product variables.

# Early checkpoint: anchor-to-Hilbert residual lift

Let a physical cross block be partitioned

B = [[P,R],[C,M]],

where P is an invertible 2x2 ORIGINAL-coordinate cross anchor, D=|det P|, and S=M-C P^{-1}R is the algebraic cross-Schur residual. Put T=||S||_F^2 and G=D^2 T.

After conditioning all outside original coordinates, write the row-side variables as (x,z) and column-side variables as (y,w), with x,y in R^2. Complete only the bilinear phase:

x^T P y + x^T Rw + z^T Cy + z^T Mw
 = (x+P^{-T}C^Tz)^T P (y+P^{-1}Rw) + z^T S w.

Changing integration variables only in the anchor variables x,y preserves their L2 norms. The normalized 2D bilinear Fourier operator is unitary, so

|phi_Q(t)| <= pi D^{-1/2}|t|^{-1} |J_S(t)|,

where J_S has the form

J_S(t)=E_{Z,W}[ exp(iF_t(Z)+iG_t(W)+2it Z^T S W) <u_Z,v_W> ]

for measurable Hilbert-space-valued u_Z,v_W with norms <=1, while Z,W remain the ORIGINAL independent residual coordinate banks.

Cauchy-Schwarz in Z gives

|J_S(t)|^2 <= E_{W,W'} prod_i |psi_i(2t(S(W-W'))_i)|.

Thus every volume-sampling D_k / sharp-Hausdorff--Young bound applies to J_S with the SAME residual matrix S: no post-Schur independence is asserted.

Two immediate exits are:

(1) If max residual row-energy marginal ||S_{i,*}||_2^2/T <=1/2 (or the analogous column condition after transposition), the k=1,q=1 volume argument gives

|J_S(t)| <= e^{1/4}(2pi)^{1/2} T^{-1/4}|t|^{-1/2}.

Hence

|phi_Q(t)| <= pi e^{1/4}(2pi)^{1/2} G^{-1/4}|t|^{-3/2},

and therefore ||p_Q||_infty <= 4.466 G^{-1/6}.

(2) For k=2,q=2 the reviewed sharp-HY formula is ungated:

|J_S(t)| <= e^{1/2}2^{-1/4}pi^{1/2} E2(S)^{-1/8}|t|^{-1/2}.

Hence, writing theta=E2(S)/T^2,

|phi_Q(t)| <= e^{1/2}2^{-1/4}pi^{3/2} theta^{-1/8}G^{-1/4}|t|^{-3/2}

and

||p_Q||_infty <= 3e^{1/3}2^{-1/6} theta^{-1/12}G^{-1/6}.

If epsilon=1-s1(S)^2/T >=1/8 then E2(S)=(T^2-sum s_j^4)/2 >= epsilon T^2/2 >= T^2/16, so this is <4.700 G^{-1/6}.

The only remaining subcase is epsilon<1/8 with both a row and a column carrying >T/2. The next step is to show the corresponding physical residual entry has |S_ij|>sqrt(T)/6; then the 3x3 physical cross block obtained by adjoining that row/column to P has determinant >sqrt(G)/6 and 3D bilinear Plancherel gives ||p_Q||_infty <=3*6^{1/3}G^{-1/6}<5.452G^{-1/6}. If verified, this closes the entire invertible second-anchor collar.

Sources actually used so far: required Claude package e5f71d79eff325201dd0274053d20268ce65b837; sharp-HY continuation c2414ef633b9d4b7f04a83e1aeefbe713ed82bba; fleet03/B02 r33 handoff 5b65776ffe5e68aebc70fbcad412ccc30e58b95f. Full QFORM remains OPEN.
