SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T03:35:08Z.
attacking: nested near-coloop volume concentration; descend 4-volume -> 3-volume -> 2-volume without selecting one minor, then apply the latest account03/B02 transverse/span-aligned packet theorem.

# Early substantive checkpoint

Let M=A[I,J], Z4=e4(M^T M)>0. If row i has four-volume marginal h_i and N=M[-i,:], then

h_i Z4 <= ||r_i||^2 Z3(N).

If row j of N has third-volume marginal g_j and P=N[-j,:], then the same exterior-product argument gives

g_j Z3(N) <= ||r_j||^2 Z2(P).

Hence the nested aggregate descendant obeys

Z2(P) >= h_i g_j Z4/(||r_i||^2 ||r_j||^2).        (C1)

This is the first useful new implication: two successive volume-coloop failures force a quantitative rank-two aggregate packet after deleting only original coordinates, with no local-minor selection.

If P has exact rank two, Delta=s1(P)s2(P)=sqrt(Z2(P)). Condition on X_j. For the remaining scalar z=X_i, x-bank I\{i,j}, y-bank J, the latest account03/B02 r18 theorem applies. If either coupling of z is transverse to Col(P)/Row(P), its exact-rank-three theorem closes with 6(Delta eta)^(-1/3). If both are span-aligned and d=A_ii !=0, put theta=beta^T P^+ alpha. Off exact resonance d=theta, r18 gives

||p_Q||inf <= 16*3^(-1/4) [Delta |d(d-theta)|]^(-1/4).              (C2)

Combining (C1) and (C2) produces an aggregate nested-star bound; the only exact-rank-two descendant residue is d=0 or the scalar Schur resonance d=theta, where the third resource must come from same-bank/global spectrum. The full QFORM target remains open.