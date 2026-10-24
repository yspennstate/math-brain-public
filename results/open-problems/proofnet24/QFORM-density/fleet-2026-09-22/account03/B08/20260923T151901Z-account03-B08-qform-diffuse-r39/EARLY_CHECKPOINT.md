SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T15:19:01Z.
attacking: localized-triangle plus second-arm receiver with arbitrary curvature; seek a product-preserving physical-coordinate reduction that complements diffuse multihub estimates.

# Early substantive checkpoint — diffuse rank-two Schur residual via a Pluecker random cut

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Let a nonzero ORIGINAL physical pivot be written

A = [[a,b^T],[b,C]],   S=C-bb^T/a.

Since A0=[[a,b^T],[b,bb^T/a]] has rank one and A-A0=diag(0,S), the singular-value min-max principle gives

s_3(A) <= s_2(S).

Hence under s_3(A)>=L, an exact-rank-two Schur residual S has both nonzero singular values at least L.

Write S=U diag(lambda_1,lambda_2) U^T with U^T U=I_2 and row leverage ell_i=||U_{i,*}||_2^2. Put mu=max_i ell_i. For i<j define the Pluecker weights

w_ij = det(U[{i,j},:])^2.

Cauchy-Binet gives sum_{i<j} w_ij=1, while the contraction identity gives

sum_{j:j!=i} w_{min(i,j),max(i,j)} = ell_i.

Choose a random Bernoulli half-partition I,J of the residual ORIGINAL coordinates, and set G_I=U_I^T U_I, G_J=I_2-G_I. Then

det G_I = sum_{i<j in I} w_ij,

det G_J = sum_{k<l in J} w_kl.

Therefore

E[det G_I det G_J]
 = (1/16) sum_{P,Q: P cap Q=empty} w_P w_Q.

The total ordered overlap mass is at most

sum_i (sum_{P ni i}w_P)^2 = sum_i ell_i^2 <= mu sum_i ell_i = 2mu.

Thus for every mu<1/2 there exists an ORIGINAL-coordinate partition with

 det G_I det G_J >= (1-2mu)/16.                 (C1)

For the physical cross block M=S[I,J]=U_I diag(lambda_1,lambda_2) U_J^T, Cauchy-Binet again gives the exact identity

 E_2(M)=lambda_1^2 lambda_2^2 det G_I det G_J.  (C2)

Hence

 E_2(M) >= (1-2mu)L^4/16.                       (C3)

Combining (C3) with the already-completed scalar-Schur E2 receiver from account03/B08 r32,

 ||p_Q||_infinity < 36.443344938 |a|^{-1/2} E_2(M)^{-1/8},

gives the target-level conditional estimate

 ||p_Q||_infinity
 < 36.443344938 [16/(1-2mu)]^(1/8) |a|^{-1/2} L^{-1/2}.  (C4)

In particular, if |a|>=tau L and mu<=1/4,

 ||p_Q||_infinity < 56.204 tau^{-1/2} L^{-1}.             (C5)

This is a genuinely diffuse exact-rank-two Schur-residual receiver. If mu>1/4, the same argument does not pretend success: one actual residual coordinate carries >1/4 of the two-dimensional Schur spectral frame, so the state is routed to the localized-coordinate side.

The designated account04/B08 anisotropic family is the complementary endpoint: its residual two-frame has mu=1, so (C5) correctly refuses it, while the partner's grouped physical-coordinate theorem pays that family by <7.251/L.

Next in this same run: (i) verify all identities and constants computationally; (ii) use the newest c2414... collective-tail theorem on a compatible higher-rank subbranch rather than extrapolating (C3) through arbitrary Schur leakage; (iii) record the exact remaining low-rank/high-leverage gap.
