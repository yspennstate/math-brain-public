SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B19, 2026-09-24T02:12:49Z.
attacking: the fleet03/B19 r46 two-star aligned-rank-two collar; sharpen one-sided alignment to a bilateral multiplicative collar using BOTH literal appended-star E3 blocks.

# Early substantive calculation

Let R,C be disjoint ORIGINAL-coordinate banks, p,q outside them (p=q allowed),

N=A[R,C],  u=A[R,p],  v=A[q,C],  delta=||u||_2 ||v||_2>0.

Put e=u/||u|| and f=v/||v||, and let

Z_L=E3([N u])=e_3(A[R,C union {p}]A[R,C union {p}]^T),
Z_R=E3([N;v^T])=e_3(A[R union {q},C]A[R union {q},C]^T).

Both are literal physical cross volumes even when p=q, since the row/column banks used in each block are disjoint.

For any matrix W with squared singular values x_1>=x_2>=..., if d_1(W)=dist_F(W,{rank<=1}), then

d_1(W)^4=(sum_{j>=2}x_j)^2 <= 2 e_2(WW^T).

Indeed x_1 sum_{j>=2}x_j >= sum_{j>=2}x_j^2, hence 2e_2 >= (sum_{j>=2}x_j)^2.

Apply the fleet03/B19 r46 appended-star exterior identity on BOTH sides:

Z_L >= ||u||^2 e_2((P_e^perp N)(P_e^perp N)^T),
Z_R >= ||v||^2 e_2((N P_f^perp)^T(N P_f^perp)).

Therefore, with

eta_L=dist_F(P_e^perp N,{rank<=1}),
eta_R=dist_F(NP_f^perp,{rank<=1}),

we get

eta_L^4 <= 2Z_L/||u||^2,
eta_R^4 <= 2Z_R/||v||^2,

and hence the multiplicative bilateral collar

(eta_L eta_R)^4 <= 4 Z_L Z_R/delta^2.                      (E1)

In the live r45/r46 packet delta>=2/9. If either Z_L or Z_R is >=2^-18, the already-completed literal physical-E3 receiver pays the full law by <=82.760672. Thus every unpaid two-star state has BOTH Z_L,Z_R<2^-18, and (E1) gives

boxed: eta_L eta_R < 3/512 = 0.005859375.                       (E2)

So the surviving two-star geometry is not merely one star-aligned rank two: the two opposite transverse rank-one defects have a dimension-free SMALL PRODUCT. In particular

min(eta_L,eta_R) < sqrt(3/512)=0.0765465544619743,

recovering the one-sided r46 collar, but (E2) is strictly stronger information.

If b is a leading left singular direction of P_e^perp N and d a leading right singular direction of NP_f^perp, define the opposite-star off-plane leakages

ell_L=||P_b^perp P_e^perp N f||,
ell_R=||P_d^perp P_f^perp N^T e||.

Best-rank-one approximation gives ell_L<=eta_L and ell_R<=eta_R, therefore

boxed: ell_L ell_R < 3/512.                                      (E3)

Thus every unpaid physical two-star packet is quantitatively one-sided after the E3 exits: robust bilateral off-axis leakage cannot survive.

Owner-pinned e5f71... source applied at an additional actual exit: its marginal-free D5 theorem gives for either literal appended-star block M in {[N u],[N;v^T]}

||p_Q||_infinity <=5 sqrt(2e) E5(M)^(-1/10).

Hence E5(M)>=2^-20 pays by

boxed: ||p_Q||_infinity <=20 sqrt(2e)=46.6328796319425.

Any survivor may therefore also assume E5<2^-20 on both appended physical blocks. This is independent of the E3 alignment calculation and retains all same-bank curvature and outside terms.

This early calculation does NOT delete the nonzero tails eta_L,eta_R and does NOT treat projected statistics as independent. It sharpens the first analytic debt to a one-sided/moving-ridge collar with the full tails retained.
