# P0012: diagonal multilinear tensors, all p>=2

Label: proof for diagonal tensors in both the multilinear and homogeneous polynomial conventions, awaiting w346. The cached source defines I_p using one repeated vector; the last paragraph below covers that convention. No assertion about all symmetric tensors is made.

Let r>=2 be an integer and T_a(x1,...,xr)=sum_(j=1)^d a_j product_(k=1)^r xk_j. Define ||T||_(I_p)=sup {|T(x1,...,xr)|: ||xk||_p<=1 for every k}, with p in [2,infinity]. This is a multilinear norm; it must not be confused with the same-vector polynomial norm for even degree and mixed signs.

If p<=r, ||T_a||_(I_p)=||a||_infinity: Holder with r equal exponents bounds the sum of products by product ||xk||_r<=1, and a coordinate vector attains the largest coefficient. If p>r, let q=p/(p-r) (q=1 at p=infinity). Generalized Holder gives ||T_a||_(I_p)=||a||_q. For finite p equality is attained by choosing all coordinate magnitudes proportional to |a_j|^(1/(p-r)) and putting each coefficient's sign in the first vector. For p=infinity choose every magnitude one and signs in the first vector.

For diagonal tensors T_i=T_(a_i) and independent standard Gaussians g_i, put Z_j=sum_i g_i a_(i,j) and sigma_j^2=sum_i a_(i,j)^2. The coordinate Gaussians can be correlated; independence across j is not needed.

If p<=r, the Gaussian exponential-moment union bound gives

E||sum_i g_i T_i||_(I_p) <= sqrt(2 log(2d)) [sum_i ||T_i||_(I_p)^2]^(1/2).

If p>r and q>=2, Jensen and Gaussian moments give E||Z||_q <= c_q ||sigma||_q, where c_q=(E|g|^q)^(1/q). Minkowski in l_(q/2) gives ||sigma||_q <= [sum_i ||a_i||_q^2]^(1/2).

If p>r and 1<=q<2, use ||Z||_q<=d^(1/q-1/2)||Z||_2, E||Z||_2 <= [sum_i ||a_i||_2^2]^(1/2), and ||a_i||_2<=||a_i||_q. The result is

E||sum_i g_i T_i||_(I_p) <= d^(1/2-r/p) [sum_i ||T_i||_(I_p)^2]^(1/2),

with 1/p=0 at infinity. At q=2 the dimension factor is one. The exponent max(1/2-r/p,0) is no larger than the target 1/2-1/p, so this proves the desired dimension bound throughout the diagonal multilinear family, extending the old diagonal p<=r calculation. It leaves off-diagonal tensors unresolved.

The homogeneous polynomial convention can also be covered explicitly. Define P_p(a)=sup_(||x||_p<=1) |sum_j a_j x_j^r|. For p<=r it is again ||a||_infinity. For p>r, with q as above, odd r permits each sign to be selected in x, so P_p(a)=||a||_q. For even r, P_p(a)=max(||a_+||_q,||a_-||_q), because x_j^r is nonnegative and each sign-support optimization is Holder duality. Hence ||a||_q<=2^(1/q) P_p(a), while P_p(Z)<=||Z||_q. Applying the multilinear Gaussian estimates yields the same type-2 bounds for diagonal homogeneous forms, with an additional factor at most two for even r and p>r. This avoids importing an incorrect mixed-sign polynomial norm identity. For example r=2,p=infinity,a=(1,-1) has multilinear norm two and polynomial norm one.
