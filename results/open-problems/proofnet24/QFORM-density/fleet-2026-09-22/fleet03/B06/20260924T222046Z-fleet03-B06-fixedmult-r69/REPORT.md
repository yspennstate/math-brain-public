SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-24T22:20:46Z.
attacking: four-eigenvalue exact-rank-two crossing plus projected self-curvature.

# r69 result

Run: 20260924T222046Z-fleet03-B06-fixedmult-r69
Execution: WITHOUT_VERIFIED_BRAIN.

New supporting theorem: QFORM-PROJECTED-2HUB-MARGINAL-FREE-TRANSVERSE-v1.

Let independent original-coordinate product banks H,L have scalar density caps one. Assume the H-to-L crossblock has exact rank two B=UM with U^T U=I_2. Split L=P disjoint_union J, assume M_J has rank two with singular-product S, put Pi=projection onto row(M_J), C=A_{P,J}(I-Pi), F=||C||_F. If F>0, then the full quadratic-plus-affine law has a continuous C_0 density and

||p_Q||_infinity <= 3 e 2^(1/6) (S F)^(-1/3) < 9.154 (S F)^(-1/3).

No projected first-volume row-marginal gate is needed. Diffuse rows use the grouped projected-crossing theorem with k=2, ell=1. If a row c_p is heavy, ||c_p||>F/sqrt(2), promote the literal original coordinate p. The crossing from H union {p} to J is [U M_J; a_p]; its three nonzero singular values have product exactly S||c_p|| because [U M_J; a_p]=diag(U,1)[M_J;a_p] and the Gram Schur complement is ||a_p(I-Pi)||^2. Exact-rank-three crossing then gives the stated bound.

Four-eigenvalue consequence: in the no-pivot s_4(A)>=1 chamber, the five-eigenvalue paper's sign proposition gives a partition with s_2(A_IJ)>gamma_2=(44-15sqrt(2))/96. If that crossing is exact rank two, Cauchy-Binet provides a secondary literal column bank with singular product >gamma_2^2/2. If its projected self-crossing F>=tau, the theorem gives ||p_Q||_infinity <30.084 tau^(-1/3). The remaining exact-rank-two obstruction is the common-plane/aligned collar F->0. General s4 remains open.

Designated partner fleet04/B06 at math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b is applied on the aligned/tangential face:
||p_(L,Y); |V-v_*|>r||_infinity <=4/(|lambda|r),
hence <=256/|lambda| at r=1/64. This pays the off-fold portion, not the near-fold common-plane remainder.

Five-eigenvalue Section 6/7 random-sign engine: PASS in a scoped reconstruction; not a new full-paper validation certificate.
General four-eigenvalue theorem OPEN. Full three-eigenvalue conjecture OPEN. Global continuity OPEN; this theorem's branch is C_0.
