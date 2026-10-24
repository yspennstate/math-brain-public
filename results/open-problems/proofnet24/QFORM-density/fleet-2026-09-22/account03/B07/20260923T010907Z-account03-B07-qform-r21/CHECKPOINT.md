SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T01:09:07Z.
attacking: finite-bank overlap receiver — apply the newest three-volume theorem to the disjoint q=0 packet, and derive a quantitative physical-core alternative; also isolate an exact rank-one receiver for the singular q=2 packet.

# Early substantive checkpoint

Full QFORM remains open. This checkpoint records two calculations to be completed/audited in the final report.

## A. q=0 three-volume-or-physical-core alternative

Let

T_k = ||wedge^k A||_F^2 = e_k(lambda_1(A)^2,...,lambda_n(A)^2).

Since at least three squared eigenvalues are >=1,

T_1 <= 2 T_2,                 3 T_3 >= T_2.                       (A.1)

Indeed

2T_2 = sum_i x_i sum_{j!=i} x_j >= sum_i x_i = T_1,

because after deleting one index at least two of the three distinguished x's remain, hence the remaining sum is >=1; similarly

3T_3 = sum_{i<j}x_ix_j sum_{k notin{i,j}}x_k >= sum_{i<j}x_ix_j=T_2,

because after deleting two indices at least one distinguished x remains.

Suppose the q=0 overlap class of the third-compound is dominant. The preceding B07 coloring theorem gives disjoint original-coordinate banks L1,L2,L3,R1,R2,R3 whose rainbow packet P0 obeys

P0 >= T_3/5184.                                                     (A.2)

Put L=L1 union L2 union L3, R=R1 union R2 union R3 and M=A[L,R]. Then

Z:=e_3(M^T M) >= P0 >= T_3/5184.                                  (A.3)

Let alpha_i be the row third-volume marginals of M. The newest volume theorem says: for 1<=q<3/2, if max_i alpha_i<=q/2, then the full ambient quadratic-plus-affine form has a continuous density satisfying

||p_Q||_infinity <= 3e/[(3-2q)sqrt(q)] Z^(-1/6).                  (A.4)

Thus, taking q=1, either

||p_Q||_infinity <= 3e*5184^(1/6) < 33.926,                       (A.5)

or there is an original physical row i in L with alpha_i>1/2. The exact volume-marginal inequality W<=(E2/Z)MM^T gives

alpha_i Z <= E_2(M) ||M_{i,*}||_2^2.                              (A.6)

Since E_2(M)<=T_2<=3T_3 and Z>=T_3/5184,

||M_{i,*}||_2^2 > (1/2)(T_3/5184)/(3T_3)=1/31104,                 (A.7)

hence

||A[i,R]||_2 > 1/sqrt(31104) = 0.005670115145... .                (A.8)

This is a dimension-free ORIGINAL-coordinate physical-core alternative, obtained from aggregate third-compound mass rather than selecting one principal minor. More generally, for theta in [1/2,3/4), q=2theta gives either the volume bound

3e/[(3-4theta)sqrt(2theta)] * 5184^(1/6)

or an original row star with squared norm > theta/15552. At theta=2/3 the two constants are <88.142 and >1/23328 respectively.

## B. singular q=2 rank-one pair receiver

Let H={h1,h2} and suppose the physical principal block B_H has rank one. Write

B_H=lambda v v^T, |v|=1, lambda!=0,

and let w be the unit null vector. For r,c outside H, the bordered determinant identity gives

det A[H union {r}, H union {c}]
 = -lambda (w^T A[H,r])(w^T A[H,c]).                              (B.1)

Thus if beta_j=w^T A[H,j], every q=2 shared-minor bank factorizes exactly:

sum_{r in R,c in C} det A[H union {r},H union {c}]^2
 = lambda^2 ||beta_R||_2^2 ||beta_C||_2^2.                        (B.2)

For a full quadratic form, condition on all outside original coordinates Z. With X_H=(X1,X2), decompose the cross coefficient into range/null components m(Z), ell(Z):

Q=lambda(v.X_H)^2+2m(Z)(v.X_H)+2ell(Z)(w.X_H)+G(Z).               (B.3)

If ell is a nonzero original-coordinate linear projection with coefficient vector beta=A[H^c,H]w, direct conditioning on one of the two PHYSICAL variables gives

||p_{Q|Z=z}||_infinity <= 2^(5/4) / sqrt(|lambda ell(z)|).         (B.4)

The sharp cap-one linear-projection theorem gives ||p_ell||infinity<=sqrt(2)/||beta||_2. The one-dimensional bathtub bound then yields

E |ell|^(-1/2) <= 2sqrt(2) (sqrt(2)/||beta||_2)^(1/2),

so

||p_Q||_infinity <= 8 / sqrt(|lambda| ||beta||_2).                (B.5)

This retains arbitrary outside quadratic curvature G and does not rotate the independent random coordinates. It will be written carefully in the final report, including the conditioning calculation and its precise scope. The beta=0 endpoint remains outside (B.5).

Status: supporting partial progress; full target and global continuity remain open.
