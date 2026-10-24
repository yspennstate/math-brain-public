SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T15:42:31Z.
attacking: sign-resolved matrix-tail stability — arbitrary favorable spectrum is free, while only sign-hostile spectral tails consume matching signed reserve modes.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922
Assignment: Additional eigenvalue control
Run: 20260923T154231Z-qform-eigenvalue-r36
Status: substantive checkpoint; full QFORM remains open.

Let H0,R,T be real symmetric m x m matrices and write the signed spectral decomposition R=P-N with P,N positive semidefinite. Fix integers p,q,r_minus,r_plus >=0. Assume

- lambda_{p+r_minus}(H0) >= kappa_plus >0 whenever p>0;
- lambda_{q+r_plus}(-H0) >= kappa_minus >0 whenever q>0;
- ||T||_op <= delta.

Let beta_plus=lambda_{r_minus+1}(N) (with beta_plus=0 if r_minus=m) and beta_minus=lambda_{r_plus+1}(P) (with beta_minus=0 if r_plus=m). Define

L_plus=kappa_plus-delta-beta_plus,
L_minus=kappa_minus-delta-beta_minus.

The first essential implication is:

1. If p>0 and L_plus>0, then lambda_p(H0+R+T) >= L_plus.
2. If q>0 and L_minus>0, then lambda_q(-(H0+R+T)) >= L_minus.

Proof sketch. Truncate N=N_top+N_tail with rank N_top<=r_minus and ||N_tail||_op=beta_plus. Since P>=0,

lambda_{p+r_minus}(H0+P+T-N_tail)
 >= lambda_{p+r_minus}(H0)-delta-beta_plus
 >= L_plus.

A rank-r_minus perturbation can move the p-th eigenvalue down no farther than the (p+r_minus)-th eigenvalue of the unperturbed matrix, hence subtracting N_top gives lambda_p(H0+R+T)>=L_plus. Apply the same argument to -(H0+R+T)=(-H0)+N-P-T for the negative branch.

Therefore if p+q>=3 and every active L is positive, the final matrix has at least p positive eigenvalues >=L_plus and q negative eigenvalues <=-L_minus. On an ACTUAL bounded original-coordinate physical core this feeds directly into the finite physical-fiber receiver, with no spectral rotation of the random vector and no convolution claim.

This differs from a sign-blind singular-tail bound: arbitrary positive added eigenvalues cost zero on the positive branch, arbitrary negative added eigenvalues cost zero on the negative branch, and the two hostile tails are budgeted separately.

Partner application planned for the final report: account04/B12 complementary-Schur shield at math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b. Its congruence factorization can be made sign-resolved: signed reserves in the complementary D block survive the arbitrary U Theta U^T packet with gap multiplied only by ell(rho)^2. The theorem above can then absorb a SECOND arbitrary signed update with separate hostile positive/negative rank budgets.
