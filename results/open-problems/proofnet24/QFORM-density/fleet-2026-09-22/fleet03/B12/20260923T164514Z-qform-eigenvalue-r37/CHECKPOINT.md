SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T16:45:14.687605Z.

attacking: orthogonal spectral-tail conservation across an original-coordinate cut.

Early substantive checkpoint. Let A=A0+R be symmetric with A0 R=0 (equivalently, A0 and R are supported on orthogonal spectral subspaces, exactly the decomposition obtained by selecting any subset of eigenpairs of A and putting all remaining eigenpairs into R). Fix an ORIGINAL-coordinate cut I union J and write C=A[I,I], M=A[I,J]. Since A0R=RA0=0,

A^2=A0^2+R^2,

hence on I,

C^2+MM^T=(A^2)[I,I] >= (A0^2)[I,I].

If lambda_k((A0^2)[I,I]) >= gamma^2, then for every p,q>=1 with p+q=k+1, Weyl's upper inequality for the PSD sum C^2+MM^T gives

gamma^2 <= lambda_k(C^2+MM^T) <= s_p(C)^2+s_q(M)^2.

For k=3 this yields the three exact tradeoffs

s1(C)^2+s3(M)^2 >= gamma^2,
s2(C)^2+s2(M)^2 >= gamma^2,
s3(C)^2+s1(M)^2 >= gamma^2.

Thus arbitrary additional eigenvalues of either sign and arbitrary magnitude cannot erase a certified three-mode baseline compression: any loss of modes from the final self-compression is exported quantitatively to the final cross block. This is deterministic matrix algebra, not an independent-convolution argument. Next: prove the counting form, apply the volume-stability receiver in the zero-self-mode branch, and seed gamma from the completed fleet04/B12 complementary-Schur theorem.