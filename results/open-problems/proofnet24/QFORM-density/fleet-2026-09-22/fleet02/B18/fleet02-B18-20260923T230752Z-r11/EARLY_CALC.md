SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T23:07:52Z.
attacking: a tetrahedral four-bank exact-rank-three family, to compare the newest fleet03/B18 four-source compiler against the pinned e5f Fresnel theorem and quantify the fixed-physical-core loss.

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Let m=4N with N>=2. Partition the original coordinates into four disjoint banks I_1,...,I_4 of size N. Put
  eps_1=(1,1,1), eps_2=(1,-1,-1), eps_3=(-1,1,-1), eps_4=(-1,-1,1),
and let every row of R in bank I_k equal eps_k/sqrt(m). Then
  R^T R=(N/m) sum_k eps_k eps_k^T=I_3.
Therefore A_m=RR^T is an exact rank-three orthogonal projection and
  spec_nonzero(A_m)={1,1,1}.
Every physical row has leverage 3/m <=3/8<1/2. The pinned e5f Theorem F therefore applies with B=0, I=all coordinates, det G=1, and gives the genuine target inequality
  ||p_{X^T A_m X}||_infinity <= 12
for every independent cap-one product law and every m>=8.

Now define the original-coordinate bank sums
  S_k=N^(-1/2) sum_{i in I_k} X_i.
The four S_k are genuinely independent because their supports in the ORIGINAL coordinates are disjoint. Moreover
  R^T X=(1/2) sum_k eps_k S_k,
so
  Q=X^T A_m X=S^T K S,
  K=(1/4)(eps_k dot eps_l)_{k,l}=I_4-(1/4)11^T,
with spectrum {1,1,1,0}. Livshyts--Paouris--Pivovarov Theorem 1.1 gives ||p_{S_k}||_infinity<=sqrt(2), since each S_k is a one-dimensional orthogonal marginal of its original product block. Scaling T_k=sqrt(2)S_k makes four independent cap-one variables and changes the effective matrix to K/2. Thus the newest completed fleet03/B18 four-source theorem gives the dimension-free bank certificate
  ||p_Q||_infinity < 1184.
No independence is inferred after a spectral rotation.

In contrast, take any four PHYSICAL coordinates J. The active 3x3 Gram matrix of the principal compression is
  S_J=R_J^T R_J,
with trace 4*(3/m)=12/m. If rank(S_J)=3, then sigma_min(S_J)<=4/m. Hence the generic four-source fleet03/B18 certificate 592/s_J is at least 148m; if rank(S_J)<3 it is unavailable. If J has exactly one coordinate from each bank then S_J=(4/m)I_3, so the certificate is exactly 148m.

Thus this exact target family separates fixed four-coordinate selection from original-coordinate bank aggregation: fixed physical four-cores lose at least linearly in m, while four disjoint banks give <1184 and the pinned diffuse Fresnel theorem gives <=12. This is an obstruction to a fixed-four-physical-core use of the new compiler, not a QFORM counterexample.
