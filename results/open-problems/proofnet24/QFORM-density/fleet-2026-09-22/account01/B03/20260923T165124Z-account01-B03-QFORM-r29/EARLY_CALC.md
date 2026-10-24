SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T16:51:24Z.
attacking: remove the one-hub projected-crossing row-marginal gate by heavy-row peeling, while keeping a whole-copy dependence-safe time integral.

Early calculation (source status: supporting calculation, not full QFORM).

Let h be one original coordinate, split the remaining original coordinates as I union J, put m=A_{h,J}!=0, and for i in I write a_i=A_{i,J}. Let c_i=a_i(I-P_m), where P_m is orthogonal projection onto span(m), and

Z_2=sum_{i<j} |c_i wedge c_j|^2 >0.

Let alpha_i=Z_2^{-1} sum_{j!=i}|c_i wedge c_j|^2. If all alpha_i<=1/2, the completed projected-crossing theorem already gives

||p_Q||_infinity <= 3*2^(7/6)*exp(1/3)*(||m||^2 Z_2)^(-1/6).

If alpha_i>1/2, define d_j=P_{c_i^perp}c_j and F_i^2=sum_{j!=i}||d_j||^2. Exact exterior algebra gives

||c_i||^2 F_i^2 = alpha_i Z_2,

and the two-row crossing product after promoting i to a grouped hub is

sqrt(det([m;a_i][m;a_i]^T))=||m|| ||c_i||.

If max_j ||d_j||^2/F_i^2<=1/2, the k=2, ell=1 grouped-hub theorem gives

||p_Q||_infinity <=3*2^(5/6)*(||m|| ||c_i|| F_i)^(-1/3)
<6*(||m||^2 Z_2)^(-1/6).

If some j has ||d_j||^2>F_i^2/2, then the J-restriction of the three-row cross block (h,i,j) has volume

Delta_J=||m|| ||c_i|| ||d_j|| > (1/2)||m|| sqrt(Z_2).

The completed account02/B03 three-selector theorem therefore gives

||p_Q||_infinity <=3*sqrt(e)*Delta_3^(-1/3)
<=3*sqrt(e)*2^(1/3)*(||m||^2 Z_2)^(-1/6)
=6.2317759031...*(||m||^2 Z_2)^(-1/6).

Thus the heavy-row branches are strictly cheaper than the original diffuse constant 3*2^(7/6)*exp(1/3)=9.3991318878..., suggesting the alpha_i<=1/2 gate can be removed entirely without worsening the theorem constant. Full proof and the whole-copy time integral will be written in REPORT.md after the control/correction refresh.
