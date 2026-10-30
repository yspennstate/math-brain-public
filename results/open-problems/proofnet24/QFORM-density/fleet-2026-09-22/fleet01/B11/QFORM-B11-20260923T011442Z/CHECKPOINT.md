SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T01:14:42Z.
attacking: the remaining zero-diagonal indefinite exact-rank-three chamber by putting its null rows on the projective conic and extracting an exact projective-variance third-direction certificate.

# Early substantive checkpoint

Status: PARTIAL DERIVATION; full QFORM remains open.

Let A=RMR^T, R^TR=I_3, with M invertible of inertia (2,1) or (1,2), and assume diag(A)=0. By Sylvester congruence there are epsilon in {+1,-1} and invertible T such that M=epsilon T^T J T for

J=[[0,0,1],[0,-2,0],[1,0,0]].

For z_i=T r_i the zero diagonal says z_i^T J z_i=0. Every nonzero real J-null vector is, after one sign, a Veronese vector nu(q)=(u^2,uv,v^2). Thus there are q_i=(u_i,v_i) !=0 and signs d_i such that z_i=d_i nu(q_i). Reflecting the ORIGINAL independent variables X_i by d_i preserves independence and the cap-one hypothesis. In those reflected coordinates,

    epsilon A_ij = det(q_i,q_j)^2  (i!=j),   A_ii=0,

because nu(q)^T J nu(q')=det(q,q')^2. Consequently, with

    L_20=sum_i u_i^2 X_i,
    L_11=sum_i u_i v_i X_i,
    L_02=sum_i v_i^2 X_i,

we have the exact product-structure-preserving identity

    epsilon Q = 2(L_20 L_02 - L_11^2).

This is a canonical determinant/discriminant representation of every zero-diagonal exact-rank-three indefinite form; it uses no rotation of the independent variables.

Fix a hub h. An SL(2,R) change of the q-parameters preserves every det(q_i,q_j), so put q_h=(0,1). For every active residual j with det(q_h,q_j)!=0 write q_j=u_j(1,t_j), rho_j=u_j^2=|A_hj|. Then

    |A_hj|=rho_j,
    |A_jk|=rho_j rho_k (t_j-t_k)^2.

Let W=sum_j rho_j^2=||A_{h,-h}||_2^2 and pi_j=rho_j^2/W. Using the prior exact identity a^T B a=det(M)c_h for a=A_{-h,h}, B=A_{-h,-h}, together with the above chart gives

    a^T B a = 2 epsilon W^2 Var_pi(t),
    u^T B u = 2 epsilon W Var_pi(t), u=a/sqrt(W).

The already-proved matched-curvature estimate |u^T B u|>=s/2, s=min|lambda(M)|, therefore yields the new exact quantitative certificate

    W Var_pi(t) >= s/4.

Thus the rank-two logarithmic saddle corresponds to zero projective variance; the third rank-three direction is exactly a nonzero weighted projective variance in original-coordinate data.

A useful corollary: if every residual physical pair satisfies |A_jk|<=delta s, then

    (sum_j rho_j)^2 / W >= 1 + 1/(2 delta).

Indeed W Var=(1/W) sum_{j<k} rho_j^2 rho_k^2(t_j-t_k)^2 <= (delta s/W)sum_{j<k}rho_jrho_k, and compare with s/4.

Remaining gap: convert this forced projective variance plus the many-small hub star into a uniform density/small-ball estimate before paying any tiny physical minor. The latest partner D0 cut theorem and the current fractional-volume exit will be applied in the final report to isolate the only residual high-leverage chamber.
