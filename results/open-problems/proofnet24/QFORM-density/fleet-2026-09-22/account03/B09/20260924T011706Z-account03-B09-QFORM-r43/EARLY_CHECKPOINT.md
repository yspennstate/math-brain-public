SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T01:17:06Z.
attacking: the exact rank-one-pair / diffuse rank-one-star collar with arbitrary same-leaf curvature; compile curvature transverse to the star into one original-coordinate disjoint cross packet before any reciprocal minor payment.

# Early calculation

Let H be a literal physical pair, I its active leaf bank, and suppose the pair-to-leaf cross block has rank one

A[H,I] = g r^T,

with g in R^2, r in R^I nonzero. Leave D=A[I,I] completely arbitrary symmetric. For each k in I let

M_k = A[H union {k}, I\{k}],

delta_k = dist(D[k,I\{k}], span(r_{I\{k}})).

If q=max_k r_k^2/||r||_2^2<1, then r_{I\{k}} is nonzero for every k. Because the two hub rows of M_k are g_1 r_{-k}^T and g_2 r_{-k}^T, Cauchy-Binet gives the exact physical-coordinate identity

Xi_k := e_2(M_k M_k^T)
      = ||g||_2^2 ||r_{-k}||_2^2 delta_k^2.

Put Xi=sum_k Xi_k and

d_* = inf_{lambda in R, Lambda diagonal} ||D-lambda r r^T-Lambda||_F.

Rowwise least squares plus symmetry gives

sqrt(Xi)/(||g||_2||r||_2) <= d_*
<= sqrt(2/(1-q)) sqrt(Xi)/(||g||_2||r||_2).

Sketch of the nontrivial upper direction: write D[k,-k]=alpha_k r_{-k}+e_{k,-k}, e_{k,-k} perpendicular r_{-k}, stack E=(e_k), and A0=alpha r^T. Symmetry gives skew(A0)=-skew(E). With lambda=(alpha.r)/||r||^2 and z=alpha-lambda r perpendicular r,

||sym(A0)-lambda rr^T||_F=||skew(A0)||_F=||skew(E)||_F.

After choosing a diagonal Lambda to cancel the physical diagonal,

d_* <= ||skew(E)||_F+||sym(E)||_F <= sqrt(2)||E||_F.

Since Xi >= ||g||^2||r||^2(1-q)||E||_F^2, the displayed upper bound follows. The lower bound holds because every candidate lambda rr^T+Lambda has kth off-diagonal row in span(r_{-k}), hence incurs at least delta_k in that row, while Xi <= ||g||^2||r||^2 sum_k delta_k^2.

A Bernoulli leaf partition I=S disjoint union T, with P(k in S)=1/3 independently, compiles the aggregate into one literal cut. Define

Z(S,T)=sum_{k in S} sum_{h in H} sum_{i<j in T} det A[{h,k},{i,j}]^2.

Every summand is a genuine 2x2 minor of A[H union S,T], and each summand from Xi survives with probability (1/3)(2/3)^2=4/27. Therefore some partition obeys

e_2(A[H union S,T]A[H union S,T]^T) >= Z(S,T) >= (4/27)Xi.

Thus if the diffuse-star gate q<1/16 holds and D is d_*-far from diagonal+lambda rr^T, then one original-coordinate disjoint cut has second cross-volume at least

(5/72)||g||_2^2||r||_2^2 d_*^2.

This is a structural reduction only: positive second cross-volume is not by itself a full density bound. The remaining analytic interface is to spend that rank-two crossing jointly with the nonzero rank-one physical pair core, or to route a rank-three physical subcut to an existing crossing theorem, without selecting a dimension-degrading tiny minor.
