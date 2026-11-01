SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T17:47:34Z.
attacking: fixed-pair anchored fourth volume via the arbitrary-rank projected-crossing theorem and an ORIGINAL-coordinate hub-concentration cascade.

# Early substantive checkpoint

Let H={a,b} be two literal ORIGINAL coordinates and L=H^c. Define the fixed-pair anchored fourth-volume currency

U_H := sum_{S subset L, |S|=2} sum_{T subset L\S, |T|=4} det A[H union S,T]^2.

For a literal partition L=I disjoint_union J, put M=A[H,J], Delta=det(M M^T), Pi=projection onto row(M), and C=A[I,J](I-Pi). Then the exact Gram-Schur/Cauchy-Binet identity is

Delta * e_2(CC^T)
 = sum_{S subset I, |S|=2} sum_{T subset J, |T|=4} det A[H union S,T]^2.      (E1)

If each leaf goes to J independently with probability p, the expectation of the RHS is (1-p)^2 p^4 U_H, maximized at p=2/3 with value (16/729)U_H.

The new projected-crossing theorem at math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401, NEW_PROJECTED_CROSSING.md, with k=2, ell=2 and two literal hubs gives, whenever its ell=2 row-volume marginals are <=1/2,

||p_Q||_inf <= 4 exp(1/4) [Delta e_2(CC^T)]^(-1/8),

with a continuous density and the same coefficient times interval length.

For each physical leaf i let

U_i := sum_{j != i} sum_{T subset L\{i,j}, |T|=4} det A[H union {i,j},T]^2.

Then sum_i U_i=2U_H. If every U_i <= (8/729)U_H, a partition realizing (E1)>=(16/729)U_H automatically has all projected ell=2 row marginals <=1/2, because each selected row contribution is <=U_i<=W/2.

If instead U_i>(8/729)U_H, promote that same literal coordinate i to a third hub. Repeating the exact identity with k=3, ell=1 and a random split with p=4/5 yields a selected currency at least (256/3125)U_i. If its ell=1 row marginal is diffuse, NEW_PROJECTED_CROSSING gives coefficient 2^(7/4) times the selected currency^(-1/8). If concentrated, a second literal leaf j has four-row anchored cross determinant mass > (128/3125)U_i; promoting j gives four literal hubs and an exact rank-four physical crossing block, paid by the exact crossing theorem.

The three normalized constants are

C_A = 4 e^(1/4) (729/16)^(1/8) = 8.2786506268...,
C_B = 2^(7/4) (3125/256)^(1/8) (729/8)^(1/8) = 8.0832021885...,
C_C = 2 sqrt(2) [(8/729)(128/3125)]^(-1/8) = 7.4123290889....

Therefore the candidate theorem is

||p_Q||_inf < 8.279 U_H^(-1/8) whenever U_H>0,

uniformly in the physical 2x2 hub core and all same-side curvature, with continuity and direct O(|interval|). The remaining work in this run is to write the complete proof, check the exact row-marginal bookkeeping and apply the designated fleet02/B09 theorem to an actual target-valid family.

Status: supporting theorem under active proof; FULL QFORM remains OPEN.
