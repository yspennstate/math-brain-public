# QFORM-FIXEDHUB-OVERLAP-SCHUR-PAY-v1

Let X have independent real coordinates with probability densities bounded by K. Let A=A^T, with arbitrary affine terms. Fix original coordinate h, put a=A_hh, and define Omega_h(A) as the sum of det A[S+{h},T+{h}]^2 over ordered disjoint two-sets S,T outside h. If a!=0 and Omega_h(A)>0, then

||p_Q||_infinity <= 8*2^(7/8) K^2 |a|^(-1/4) Omega_h(A)^(-1/8).

This proves essential boundedness in this scope; continuity is not asserted.

Write Y=X_{-h}, c=A_{-h,h}. Completing the physical square gives
Q=a(X_h+(c^T Y+b_h/2)/a)^2+R(Y),
where R has quadratic matrix S^(h)=A_{-h,-h}-a^(-1)c c^T.

For each ordered disjoint S,T outside h, the bordered determinant formula gives
det A[S+{h},T+{h}]=a det S^(h)[S,T].
Thus
Omega_h(A)=a^2 V_2(S^(h)).                                      (1)

Make a fair partition of the remaining original-coordinate indices into I,J. Each ordered disjoint two-row/two-column seed enters S^(h)[I,J] with probability 1/16, hence some literal cut M satisfies
E_2(M)>=V_2(S^(h))/16.                                         (2)

The source-pinned LPP grouped compiler gives
sup_t E|R-t|^(-1/2) <= 8*2^(3/8) K E_2(M)^(-1/8),
so by (2)
sup_t E|R-t|^(-1/2)
 <=8*2^(7/8) K V_2(S^(h))^(-1/8).                             (3)

Conditioning on Y, the scalar-square change of variables for the literal coordinate X_h gives
p_Q(t)<=K|a|^(-1/2) E|R-t|^(-1/2).
Combine with (1),(3) to obtain the claimed bound.

No random-variable rotation is used. Same-side curvature and all affine terms remain in R. The fair cut preserves original-coordinate product provenance, and the scalar-square step is a conditional domination statement, not an independence assertion.

Source for the half-potential compiler:
yspennstate/math-open-problems@94fcf7454085070f4a81b46d20cda28220ad0e1c
proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B18/20260924T142238Z-account03-B18-QFORM-fixed-multiplicity-audit-r1/LPP_SOURCE_TRANSFER.md
