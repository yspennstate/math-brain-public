SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T04:50:00Z.
attacking: the high-leverage/small-tail boundary by exploiting commutation of the third-volume marginal matrix with the top-two singular projection.

# Early substantive checkpoint

For an original-coordinate cross block M with squared singular values lambda_j=s_j(M)^2, let E_k=e_k(lambda), T2=sum_{j>=3}s_j(M)^2, and let W be the exact third-volume row-marginal matrix

W = U diag(p_j) U^T,  p_j=lambda_j e2(lambda without j)/E3.

The current volume-stability package gives W<=I and, using fleet01/B20's T2 E2<=3E3 identity,

W <= (E2/E3) M M^T <= (3/T2) M M^T.

New observation: if P2 is the orthogonal projection onto any compatible top-two left-singular subspace of M, then P2 commutes with W. Hence for l_i=(P2)_ii,

alpha_i=e_i^T W e_i
       =(P2 e_i)^T W(P2 e_i)+((I-P2)e_i)^T W((I-P2)e_i)
       <= l_i + (3/T2)||M^T(I-P2)e_i||^2
       <= l_i+3(s3(M)^2/T2)(1-l_i).

Thus, writing L=max_i l_i and rho=s3(M)/sqrt(T2), whenever rho^2<=1/3,

max_i alpha_i <= A_spec(L,rho):=L+3rho^2(1-L).

This removes the cross term in the prior triangle bound [sqrt(L)+sqrt(3)rho sqrt(1-L)]^2. At the worst leverage L=1/2, the finite q<3/2 gate becomes 1/2+(3/2)rho^2<3/4, i.e. T2/s3^2>6, instead of the prior sufficient threshold 59.3938....

Next: feed this sharper marginal gate into the already-checked q-dependent fractional-volume Fourier theorem and record exact constants, a target family, and scope. Full QFORM remains open.
