SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T05:39:05Z.
attacking: coordinate-minor selection via the new 2/3 third-volume marginal gate, followed by an anchored Laplace compiler before any reciprocal minor payment.

# Early substantive checkpoint

Let M be an ORIGINAL-coordinate cross block and Z=E_3(M)>0. Under the squared third-minor law w(S,T)=det(M[S,T])^2/Z, let alpha_i=P(i in S), beta_a=P(a in T).

Using the new fractional-volume theorem from the 20260923T002323Z volume-stability package with q=4/3, if max_i alpha_i<=2/3 (or, after transposition, max_a beta_a<=2/3), then the full ambient Q has a continuous density and

||p_Q||_infinity <= (9 sqrt(3) e / 2) Z^(-1/6).

Otherwise there are physical i,a with alpha_i>2/3 and beta_a>2/3. Therefore the complete double-incident packet

W_ia=sum_{S contains i, T contains a} det(M[S,T])^2

satisfies W_ia/Z=P(i in S,a in T)>=alpha_i+beta_a-1>1/3. This is an aggregate anchor, not a one-good-minor assertion.

If an anchored residual row marginal and an anchored residual column marginal both exceed 1/2, their one-sided nest masses P_R,P_C each exceed W_ia/2>Z/6. For the row nest with fixed rows i,k and fixed column a, write, on residual columns C and residual rows R,

x=M_ia, y=M_ka, u=M_iC, v=M_kC, c=M_Ra, N=M_RC.

Laplace expansion along column a gives the exact pointwise identity

det M[{i,k,r},{a,b,d}] = x(v_b N_rd-v_d N_rb) - y(u_b N_rd-u_d N_rb) + c_r(u_b v_d-u_d v_b).

Hence, after summing squares,

P_R <= 3[x^2 A_v + y^2 A_u + ||c||^2 Delta(u,v)^2],

where
A_v=||v||^2||N||_F^2-||Nv||^2,
A_u=||u||^2||N||_F^2-||Nu||^2,
Delta(u,v)^2=||u||^2||v||^2-<u,v>^2.

Thus one of the three nonnegative resources exceeds P_R/9>Z/54. The remaining work in this run is to prove a dimension-free disjoint-bank extraction from the third resource and quantify the high-tail application, with an actual fleet04 result applied only at a scope where original-coordinate independence is genuine.

Status: supporting derivation in progress; full QFORM open.
