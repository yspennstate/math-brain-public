SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T12:49:06Z.
attacking: compile diffuse singleton third-volume mass in a rank-two hub/star into one genuine original-coordinate cross cut before reciprocal minor payment.

# Early substantive checkpoint — aggregate singleton volumes compile into one physical cut

Let H be a physical hub bank and I a disjoint leaf bank. Assume the physical hub-to-leaf block has rank two and factorization

A[H,I] = P C^T,   P^T P = I_2,

with C in R^{|I| x 2}. Let D=A[I,I]. For k in I, put d_k=D[k,I\{k}] and let

M_k = A[H union {k}, I\{k}].

Because an orthogonal change of basis on the ROW INDEX SPACE H is only an algebraic singular-value calculation, not a rotation of random coordinates, M_k has the same nonzero singular values as [C_{-k}^T; d_k]. Define Gamma_k^2=e_3(M_k^T M_k), equivalently the squared product of the three nonzero singular values when rank M_k=3, and zero otherwise.

For a subset S of leaves, T=I\S, define the genuine original-coordinate cross cut

M_S=A[H union S,T]=[P C_T^T; D[S,T]].

After the same row-space orthogonal change on H, M_S becomes [C_T^T;0;D[S,T]]. Therefore e_3(M_S^T M_S) dominates the sum of squared 3x3 minors using the two active hub rows and exactly one moved leaf row.

Choose each leaf independently into S with probability p. For a fixed k and a fixed 3-column set J subset I\{k}, the minor det([C_J^T;D[k,J]]) is present in this selected subfamily exactly when k is in S and J subset T, an event of probability p(1-p)^3. Summing by Cauchy-Binet gives

E_S e_3(M_S^T M_S) >= p(1-p)^3 sum_k Gamma_k^2.

The factor is optimized at p=1/4, where p(1-p)^3=27/256. Hence there exists a literal source-coordinate partition S,T with

    e_3(M_S^T M_S) >= (27/256) sum_k Gamma_k^2.                (CP)

This is dimension-free and has no leverage, support, moment, sign, or diagonal assumptions. It converts the aggregate singleton defect from account03/B09 r31 into ONE actual cross cut before any reciprocal minor payment.

Remaining step for an end-to-end density exit: apply the current fractional three-volume theorem when the compiled cut's volume row marginals satisfy its admissibility gate; otherwise route the resulting concentrated-volume row/column geometry to a physical-minor/high-leverage endpoint. The full QFORM conjecture is not claimed solved by (CP).
