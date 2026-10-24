SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T18:53:17Z.
attacking: the Cauchy--Binet overlap decomposition of the third spectral volume; pay the disjoint-minor branch by the row-marginal-free rank-three crossing theorem and convert the one-shared-index branch into a scalar-square plus critical rank-two aggregate without selecting a tiny minor.

# Early calculation: overlap decomposition and the one-shared-index Schur identity

Let A=A^T and
E_3=e_3(A^2)=sum_{|S|=|T|=3} det(A_{S,T})^2.
Write E_3=E_0+E_1+E_2+E_3^{pr}, where E_r is the same sum restricted to |S cap T|=r. If s_3(A)>=s then E_3>=s^6.

For a random coordinate cut L subset [n], R=L^c, Cauchy--Binet gives
Z_3(A_{L,R})=sum_{S subset L, T subset R, |S|=|T|=3} det(A_{S,T})^2.
Every ordered disjoint pair (S,T) is captured with probability 2^-6, hence
E_L Z_3(A_{L,R})=E_0/64.
Therefore some physical cut has Z_3>=E_0/64. In particular, if E_0>=theta s^6, the completed account01/B03 rank-three crossing theorem yields a continuous density with
||p_Q||_infty <= [3*2^(3/2)*sqrt(e)] (64/theta)^(1/6) s^-1
=6*2^(3/2)*sqrt(e)*theta^(-1/6) s^-1.
For theta=1/4 this constant is 35.2522479993.

Now fix a physical coordinate h with a=A_hh !=0. Put Y=X_{-h}, c=A_{-h,h}, and S^(h)=A_{-h,-h}-a^-1 c c^T. Exact completion gives
Q=a(X_h+a^-1 c^T Y)^2+Y^T S^(h)Y.
Define
E_1(h)=sum_{I,K subset [n]\{h}, |I|=|K|=2, I cap K=empty} det(A_{h union I,h union K})^2.
The scalar Schur determinant identity gives
E_1(h)=a^2 sum_{I cap K=empty, |I|=|K|=2} det(S^(h)_{I,K})^2.
For a random cut L,R of [n]\{h},
E Z_2(S^(h)_{L,R})=E_1(h)/(16 a^2).
Hence some cut has Z_2>=E_1(h)/(16a^2). Applying the row-marginal-free critical two-volume theorem to the residual, then the exact physical square receiver, gives
||p_Q||_infty <= 8(2e)^(1/4)|a|^-1/2 Z_2^-1/8
<= 8 sqrt(2)(2e)^(1/4) [a^2 E_1(h)]^-1/8.
The numerical constant is 17.2757179198. This pays the entire overlap-one aggregate whenever a shared physical diagonal pivot has scale, without selecting any individual 3x3 minor.

The designated partner account02/B03 result at math-open-problems@38920ffa423ec07886112206314249deb7294dd4 is compatible with the heavy-row subbranch of the selected Schur cut: if its pair-volume row marginal alpha_i>1/2 and the projected one-volume marginals are diffuse, then its k=1,ell=1 critical crossing plus the same physical square gives
||p_Q||_infty <=8|a|^-1/2(alpha_i Z_2)^-1/8,
which after Z_2>=E_1(h)/(16a^2) is strictly below
8*2^(5/8)[a^2E_1(h)]^-1/8=12.3376866033[a^2E_1(h)]^-1/8.
This is an actual application of the completed partner estimate, not a transfer of conditional density caps.

Full QFORM remains open. The next structural survivor after this calculation has small disjoint 3-minor mass E_0 and, for every nonzero physical diagonal, small normalized overlap-one resource a_hh^2 E_1(h); the E_2 and principal-overlap sectors and the zero-diagonal part of E_1 remain to be routed.
