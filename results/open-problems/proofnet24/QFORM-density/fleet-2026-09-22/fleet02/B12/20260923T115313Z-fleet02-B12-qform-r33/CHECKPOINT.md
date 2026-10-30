SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T11:53:13Z.
attacking: collective singular-reserve dilution — convert the latest partner rank-tail inequality into an l2-tail stability theorem under an arbitrary dense operator-norm tail, then feed the resulting actual cross-block gap into the pinned D5 theorem.

# Early substantive checkpoint

Full target remains OPEN. This checkpoint records a new deterministic implication before the final write-up.

Let M and E be compatible matrices, let q>=1 and r>=0, and suppose M has N>=r+q singular values at least kappa. Put

R_r(E)^2 := sum_{j>r} s_j(E)^2,
L := N-r-q+1.

The latest completed fleet03/B12 singular-reserve inequality gives, for every rank budget k,

s_q(M+E) >= s_{q+k}(M)-s_{k+1}(E).

Take k=N-q. Then s_{q+k}(M)=s_N(M)>=kappa. Since k+1=N-q+1=r+L and the tail singular values are decreasing,

L s_{N-q+1}(E)^2 <= sum_{j>r}s_j(E)^2=R_r(E)^2.

Therefore

s_q(M+E) >= kappa - R_r(E)/sqrt(L).

If T is any further matrix with ||T||op<=delta, Weyl gives

s_q(M+E+T) >= kappa-delta-R_r(E)/sqrt(N-r-q+1).                 (CP.1)

No probabilistic smallness of X^T T X is asserted.

For q=5 and an ACTUAL original-coordinate cross block, if the right side gamma is positive, the pinned newest-Claude D5 theorem at math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 gives

||p_Q||_infinity <= 5 sqrt(2e)/gamma,                              (CP.2)

with arbitrary same-bank quadratic blocks, outside couplings and affine terms. Thus the top r singular directions of E can be arbitrarily large, while the entire remaining tail is charged only by its Schatten-2 mass diluted across the baseline reserve count.

This l2-tail coefficient is sharp from the stated aggregate information: for M=kappa I_N, put r diagonal update entries at -kappa, the next L=N-r-q+1 update singular values equal -a with a=R/sqrt(L), and leave q-1 coordinates untouched. Then s_q(M+E)=kappa-a. Adding -delta I attains the dense-tail loss as well.

Remaining full-target gap: bare s_3(A)>=1 does not force such an N-direction original-coordinate reserve; this theorem is a stability/compiler result, not that structural extraction.
