# B09 substantive checkpoint — intrinsic one-hub mixed frame

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains open.

Let h be one literal source coordinate, I a disjoint leaf bank, J the conditioned remainder. Assume on I

A_II = D + V Lambda V^T,

where D is diagonal, V has r orthonormal columns v_1,...,v_r, and Lambda=diag(lambda_1,...,lambda_r) has nonzero entries. Let c=A[I,h] be the actual hub-to-leaf star, L=range(V), and c_perp=(I-VV^T)c. Put W=[V,c]. If c_perp !=0 then

G=W^T W = [[I,V^T c],[c^T V,||c||^2]],

det G = ||c_perp||^2,

and the row quantities rho_i^T G^{-1}rho_i from the e5f71d79... mixed-hub theorem are exactly

ell_i=(P_{L + span(c_perp)})_ii.

Thus, if max_i ell_i<=1/2, Theorem H at math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 gives

||p_Q||_infinity <= C_r [ |pdet(V Lambda V^T)| ||c_perp||^2 ]^(-1/(r+2)),

C_r = 4 (r+2)/r * 2^(-2/(r+2)),

uniformly over arbitrary A_hh, A_hJ, A_IJ, A_JJ and affine terms. The same coefficient multiplies |L0| for every target interval L0. No probability squaring or post-rotation independence is used.

For r=2, choose m>=8 with flat mutually orthonormal Walsh vectors c,v_1,v_2 and

Q_m=2 X_h <c,Y> + 2<v_1,Y>^2 + 3<v_2,Y>^2.

Then the active spectrum is {1,-1,2,3}, G=I_3, all ell_i=3/m<=1/2, and

||p_Qm||_infinity <= 4 sqrt(2) 6^(-1/4) = 3.6144080144...,
P(Q_m in L0) <= 3.6144080144... |L0|.

This is an actual target-valid diffuse source-coordinate star with dense same-side rank-two curvature.

Remaining structural debt: when max ell_i>1/2, use the exact identity
ell_i=||P_L e_i||^2+|c_perp,i|^2/||c_perp||^2
to route a literal localized source coordinate without conditioning away the transverse third direction. Partner fleet03/B09 r26 supplies the analogous determinant-basis collision-to-high-leverage mechanism for two-frames.
