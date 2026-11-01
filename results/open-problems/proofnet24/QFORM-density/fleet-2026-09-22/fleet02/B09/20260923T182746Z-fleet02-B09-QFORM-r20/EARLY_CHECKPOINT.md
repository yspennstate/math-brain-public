# fleet02/B09 r20 early checkpoint — dual-zero carrier receivers

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

## First unpaid implication

`QFORM-DUALZERO-R4-OVERLAPPING-RANKTRANSITION-v1`: after fleet03/B09 r38 collapses exact two-sided singleton aggregate zero to an original-coordinate diagonal plus a rank-at-most-four carrier, pay the genuinely overlapping rank-four carrier uniformly as its fourth carrier eigenvalue tends to zero, without deleting that small non-diagonal spectral tail and without absolute-value decoupling. High carrier leverage is a separate endpoint.

## New bridge 1: the diffuse exact rank-three carrier is already paid

Use fleet03/B09 r38. At exact dual aggregate zero and away from coloops, write

A = D0 + S,
S = U0 K0 U0^T,
U0 = diag(P,R),  U0^T U0 = I4,
R = C(C^T C)^(-1/2).

The physical row leverage of U0 is exactly q=max(q_H,q_I), where q_H=max_h ||p_h||^2 and q_I=max_i c_i^T(C^T C)^(-1)c_i.

If rank(K0)=3 and q<=1/2, diagonalize K0=O Lambda O^T on its three-dimensional range. Then V=U0 O has orthonormal columns and every physical row leverage of V is <=q<=1/2. The general-rank Fresnel--Brascamp--Lieb Theorem F from the pinned e5f71d79 source applies directly to

A = D0 + sum_{j=1}^3 lambda_j v_j v_j^T

with no decoupling. Therefore

||p_Q||_infinity <= 12 |lambda_1 lambda_2 lambda_3|^(-1/3).

If additionally s3(A)>=1 and ||D0||op<=tau<1, the r38 spectral transfer gives s3(S)>=1-tau, hence

||p_Q||_infinity <= 12/(1-tau),
P{Q in L} <= 12 |L|/(1-tau).

The characteristic function is L1 in this branch, so the density is continuous.

For rank(K0)=4 the same undecoupled theorem gives

||p_Q||_infinity <= 8 |det K0|^(-1/4)
<= 8[(1-tau)^3 s4(S)]^(-1/4).

Thus the only diffuse exact-carrier rank transition not paid by this absolute Fresnel receiver is precisely s4(S)->0 through nonzero values.

## New bridge 2: a source-separated aligned rank-four family is uniform through that transition

Let N be even and P_N=R_N have rows (1,s_i)/sqrt(N), with N/2 signs +1 and N/2 signs -1. Put U=diag(P_N,R_N) and, for epsilon in [0,1],

K_epsilon = [[diag(1+epsilon,0), I2],
             [I2, diag(1+epsilon,0)]],
A_epsilon = U K_epsilon U^T.

The carrier spectrum is exactly {2+epsilon, epsilon, 1, -1}; hence every A_epsilon satisfies the owner target, including epsilon=0. Both singleton third-volume aggregates vanish exactly, every carrier row leverage is 2/N, and D0=0. The same-side blocks are dense aligned rank-one matrices.

Rotate only the two-dimensional coefficient bases by 45 degrees. The two hub frame columns then have disjoint ORIGINAL-coordinate supports (the + and - sign classes), while the leaf rank-one square direction is (c1+c2)/sqrt(2), transverse to the retained cross direction c1. Condition the other physical hub bank and apply the already-completed fleet02/B09 r18 source-separated grouped-hub corollary, whose analytic engine is fleet03/B09 r29 grouped mixed-hub smoothing. The mixed leaf Gram determinant is 1/2. Its Pluecker basis law chooses one + leaf and one - leaf uniformly, so the disjoint-basis mass is

rho_N=(1-2/N)^2.

Thus, uniformly for every epsilon in [0,1],

||p_{X^T A_epsilon X}||_infinity
 <= 3e [ (1+epsilon) rho_N /2 ]^(-1/3)
 <= 3e [ rho_N/2 ]^(-1/3),

and the same constant multiplies |L|. No probability squaring occurs. At N=8 the uniform constant is <12.447 and as N->infinity it tends to 3e 2^(1/3)<10.275.

This is an actual near-rank-three interpolation: the raw rank-four Theorem-F estimate 8[(2+epsilon)epsilon]^(-1/4) diverges as epsilon->0, while source-coordinate grouped mixed-hub smoothing stays bounded and retains the dense same-side hub and leaf rank-one couplings.
