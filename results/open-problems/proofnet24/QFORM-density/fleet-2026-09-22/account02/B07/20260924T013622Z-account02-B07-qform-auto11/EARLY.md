SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T01:36:22Z.
attacking: the account03/B07 r42 near-rank-two common crossing plus low-diagonal/low-internal cloud receiver — determine whether the extracted rank-two tube is quantitatively two-directional, and if not give a target-valid obstruction while preserving all determinant weights.

# Early mathematical checkpoint

Incoming completed partner r42 leaves, after its new internal-edge Z3 exit fails, a low-diagonal bank carrying >0.32768 of projected Z2 mass on anchors h with |A_hh|, ||A[h,J]||_2 and ||A[h,H_lo\{h}]||_2 all <1/64. The compatible account02/B07 previous router says that, unless physical E3(K) already pays, the common crossing K is within sqrt(3)*2^(-9) in Frobenius norm of rank two or else a large diagonal cloud remains.

First new deterministic observation: the phrase “rank-two carrier” cannot be read as two singular directions of comparable absolute size. For a p x q matrix K, with x_j=s_j(K)^2 and r=min(p,q),

  E2(K):=e2(KK^T)=sum_{j=2}^r x_j sum_{i<j}x_i
       <= (r-1) s_2(K)^2 ||K||_F^2.

Therefore a bounded physical support does give the safe aggregate estimate

  s_2(K) >= [E2(K)/((r-1)||K||_F^2)]^(1/2)
           >= [E2(K)/((r-1)pq L^2)]^(1/2)

when |K_ij|<=L. No individual 2x2 minor is selected. Conversely, with support allowed to grow, fixed E2 alone cannot bound s_2.

Exact target-valid stress to be completed in REPORT.md: let K_m=m u_1v_1^T+m^(-1)u_2v_2^T on two large physical banks, with flat orthonormal pairs. Then E2(K_m)=1, E3(K_m)=0 and s_2(K_m)=m^(-1)->0. Add a diffuse low-diagonal cloud a_m I with a_m->0 and weighted packet sum_h a_m^2 Z_h=1, plus an independent diffuse rank-one +1 block. The total matrix has eigenvalues +m,-m,+1,+m^(-1),-m^(-1) (plus tiny cloud eigenvalues), so it is inside the full owner target while every fixed-cardinality physical principal block tends to zero. This will refute any bounded-core or balanced-rank-two inference from the r42 survivor.

The pinned e5f71d79... Fresnel-Brascamp-Lieb theorem is designed for the same stress: the complete non-diagonal rank-five part has coordinate leverage <=1/2 and eigenvalue-product one, so its |t|^(-5/2) bound should give ||p_Q||_infinity<=20/3 after exact integration, with the cloud retained as an arbitrary diagonal twist. This uses the small +/-m^(-1) tail rather than deleting it.

Full QFORM remains open; continuity is separate. No moment/support/log-concavity/iid/post-rotation-independence assumption is introduced.
