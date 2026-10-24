SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T19:00:48Z.
attacking: the exact dual-zero-aggregate diffuse rank-three carrier, then the rank-four near-rank-three tail-stability endpoint without deleting the diagonal twist.

# Early substantive checkpoint

The newest completed account03/B09 r38 gives, at exact two-sided singleton aggregate zero and under its no-coloop hypotheses, an original-coordinate decomposition

A = D_0 + S,

where D_0 is physical diagonal, rank S <= 4, and range(S) lies in a four-dimensional carrier W=diag(P,R) with W^T W=I_4.  Here P is the normalized two-frame on the H bank and R=C(C^T C)^(-1/2) is the whitened two-frame on the I bank.  Thus the physical carrier leverage is

q = max_i ||W^T e_i||^2 = max(q_H,q_I).

The first unpaid endpoint can already be reduced further.

## Lemma (diffuse exact rank-three carrier)

Assume s_3(A)>=1, ||D_0||_op<=tau<1, q<=1/2, and rank S=3.  Then the law of X^T A X has a continuous density and

||p_(X^T A X)||_infinity <= 12/(1-tau).

Proof. Weyl gives s_3(S)>=s_3(A)-||D_0||_op>=1-tau.  Write the rank-three spectral decomposition S=sum_(j=1)^3 lambda_j v_j v_j^T with orthonormal v_j.  Because range(S) is contained in range(W), the row leverage of the eigenframe V=[v_1,v_2,v_3] obeys

||V^T e_i||^2 <= ||W^T e_i||^2 <= 1/2.

Apply the completed Fresnel--Brascamp--Lieb Theorem F from math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 to A=D_0+S.  Its Gram is I_3 and |lambda_1 lambda_2 lambda_3|>=(1-tau)^3, hence

||p||_infinity <=12 |lambda_1 lambda_2 lambda_3|^(-1/3) <=12/(1-tau).

The theorem gives an L^1 characteristic-function envelope, so the density is continuous and the same constant multiplies interval length.  No random coordinate is rotated; only the deterministic coefficient frame is diagonalized. QED.

The same calculation for rank S=4 with kappa=s_4(S)>0 uses the rank-four form of the same Fresnel/BL argument and gives

||p||_infinity <= 8[(1-tau)^3 kappa]^(-1/4).

Therefore in the diffuse small-diagonal chamber (for example q<=1/2 and tau<=1/2), exact rank three is paid uniformly (<=24), and rank four is paid uniformly away from kappa=0 (for kappa>=1/2, <=16).  The precise new debt is the rank-four-to-rank-three transition kappa downarrow 0 while retaining the physical diagonal twist exactly.

## Sharp structural stress family for that transition

Let P_N,C_N be two disjoint-bank N x 2 Walsh frames with orthonormal columns and row leverage 2/N.  Put W=diag(P_N,C_N) and

K_epsilon = [[N_0,I_2],[I_2,M_epsilon]],
N_0=diag(1,0),  M_epsilon=diag(1+epsilon,0), epsilon>=0.

Then S_epsilon=W K_epsilon W^T has coefficient-space spectrum

{ 1,-1, (2+epsilon+sqrt(4+epsilon^2))/2,
       (2+epsilon-sqrt(4+epsilon^2))/2 }.

Thus every epsilon>=0 satisfies the owner target with at least three eigenvalues of modulus >=1.  At epsilon=0 the carrier has rank three; for epsilon>0 it has rank four and its fourth singular value tends to zero like epsilon/2.  All physical coefficients are O(1/N), q=2/N, and because each same-side block stays inside its cross two-plane, every singleton augmented third volume on both sides is exactly zero.  Hence neither the target spectrum, diffuseness, nor the two-sided G_* currencies can force a positive fourth-carrier scale.

This is not a QFORM counterexample.  It identifies the exact analytic stability transition left after the partner collapse.
