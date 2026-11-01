SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B02, 2026-09-23T17:01:06Z.
attacking: close the strong-cut double-physical-hub survivor by recursively converting an incident physical third-volume into one-hub/two-hub projected-crossing Fourier L1, or a genuine three-row crossing block.

# Early substantive calculation

Let M be an original-coordinate cross block between independent coordinate banks L and R. Fix a physical row i in L, write w=M[i,R], and let C=M[L\{i},R](I-P_w). Put

J_i = sum_{I subset L, |I|=3, i in I} sum_{K subset R, |K|=3} det(M[I,K])^2.

Then Cauchy-Binet plus orthogonal projection gives the exact identity

    J_i = ||w||^2 e_2(C C^T).                                    (1)

Therefore the new projected-crossing theorem (interactive checkpoint 4f92aeb74083c6f95cb314a11fed1b812eacef9) with one original hub and ell=2 applies immediately if the 2-volume row marginals of C are <=1/2, yielding

    ||p_Q||_infty <= C12 J_i^(-1/6),
    C12 = 3*2^(7/6)*exp(1/3) = 9.3991318878...,

and phi_Q in L1.

If the ell=2 marginal gate fails, choose a row k with incident 2-volume > e_2(CC^T)/2. Then, with P=M[{i,k},R] and C2=M[L\{i,k},R](I-P_row(P)), the exact second descent is

    H_ik := sum_{l != i,k} sum_{|K|=3} det(M[{i,k,l},K])^2
          = (product singular values of P)^2 * ||C2||_F^2
          > J_i/2.                                                (2)

If every squared row norm of C2 is <= ||C2||_F^2/2, the grouped theorem with two original hubs and ell=1 yields

    ||p_Q||_infty <= 3*2^(5/6) H_ik^(-1/6) < 6 J_i^(-1/6),

again with phi_Q in L1.

If that ell=1 gate also fails, choose l with ||(C2)_l||^2>||C2||_F^2/2. The literal three-row cross block B3=M[{i,k,l},R] then satisfies

    det(B3 B3^T) > H_ik/2 > J_i/4.                                (3)

Conditioning on the remaining L-coordinates reduces to the exact-rank-three crossing theorem, which keeps arbitrary internal functions on both banks and gives

    ||p_Q||_infty < 3*2^(5/6) J_i^(-1/6).

Thus all marginal failures close recursively; the worst constant is C12. The full proof still needs the ambient conditioning and the spectral lower bound for the actual fleet04/B02 strong-cut survivor checked carefully before publication.
