SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T02:13:15Z.
attacking: optimize the admissible three-volume certificate by constrained KL reweighting, and test it on a full-rank genuinely rotated indefinite family where canonical volume sampling approaches the forbidden 3/4 marginal boundary.

# Early substantive checkpoint

## Weighted three-volume certificate
Let M=A[I,J] be any original-coordinate cross block and
Z=e_3(M^T M)>0.  Let v_{S,T}=det(M[S,T])^2/Z on nonzero 3x3 minors.
For ANY probability law w on the same minor support, write alpha_i=P_w(i in S), beta_j=P_w(j in T), and K=KL(w||v).
Repeating the sharp-Hausdorff-Young volume proof with weighted AM-GM gives, for 1<=q<3/2 and max_i alpha_i<=q/2,

||p_Q||_infty <= [3e/((3-2q)sqrt(q))] Z^(-1/6) exp(K/6).

Indeed the determinant step becomes

det(D_J+M^T D_I M)
 >= Z exp(-K) prod_i d_i^{alpha_i} prod_j e_j^{1-beta_j},

and the rest of the q-proof is unchanged.  Thus the natural optimized effective volume is

Z_eff(q;M)=Z exp(- inf_{w: alpha_i<=q/2} KL(w||v)).

Finite-dimensional entropy duality gives the exact diagonal-scaling formula

Z_eff(q;M)= inf_{lambda_i>=0} exp((q/2) sum_i lambda_i)
             e_3(M^T diag(exp(-lambda_i)) M).

The optimizer, when finite, has Gibbs form
w_{S,T} proportional to v_{S,T} exp(-sum_{i in S} lambda_i),
with complementary slackness lambda_i(alpha_i-q/2)=0.

This turns the row-marginal gate into an exact convex optimization rather than a yes/no test of canonical volume sampling.

## A full-rank rotated family where this matters
Let U be the 7x7 orthogonal matrix with columns
u1=e1,
u2=(e2+e3)/sqrt2,
u3=(e4+e5)/sqrt2,
u4=(e6+e7)/sqrt2,
u5=(e2-e3)/sqrt2,
u6=(e4-e5)/sqrt2,
u7=(e6-e7)/sqrt2.
Let V=I-(2/7)11^T, let 0<epsilon<=1/2, Sigma=diag(1,1,1,1,epsilon,epsilon,epsilon), and M_epsilon=U Sigma V^T.  Put
A_epsilon=[[0,M_epsilon],[M_epsilon^T,0]].
Then A_epsilon has eigenvalues +/-1 (multiplicity 4 each) and +/-epsilon (multiplicity 3 each), so it is a genuinely rotated indefinite target matrix; M_epsilon is full rank and dense for generic epsilon in this range.

With t=epsilon^2,
Z=4+18t+12t^2+t^3,
p_H=(3+9t+3t^2)/Z,
p_L=t(6+8t+t^2)/Z.
The canonical row marginals are alpha_1=p_H and alpha_2=...=alpha_7=(p_H+p_L)/2.  As epsilon->0, alpha_1->3/4, so the canonical D' constant blows up.

Reweight only the event R={row 1 is selected}, changing P_v(R)=p_H to P_w(R)=1/2 while preserving both canonical conditional laws.  Symmetry gives alpha_1(w)=1/2 and alpha_2(w)=...=alpha_7(w)=5/12.  Data processing plus this explicit tilt show that it is the exact q=1 KL projection:

K_*=D_Ber(1/2 || p_H)
   = (1/2) log(1/(4 p_H(1-p_H))).

Therefore

||p_{X^T A_epsilon X}||_infty
 <= 3e Z^(-1/6) exp(K_*/6).

As epsilon->0 this stays finite and tends to
3e 4^(-1/6)(4/3)^(1/12)=6.629548713390117... .
At epsilon=0.05 the bound is 6.6131146576, while canonical D' is about 473.47.

Next: verify the exact KL/duality algebra, apply the completed fleet02/B04 rank-r theorem on the SAME M_epsilon, and compare the reciprocal product-of-singular-values cost with the new entropy-weighted aggregate bound.
