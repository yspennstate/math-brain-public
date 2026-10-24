SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T04:18:14Z.
attacking: pair-anchored fourth-volume -> row-marginal-free product-Fourier receiver, then apply account04/B04's double-anchor packet.

Early substantive calculation.

Let M=A[I,J] be a literal original-coordinate cross block and fix two rows a,b in I. Put D2=det Gram(m_a,m_b)>0, project all remaining rows orthogonally off span(m_a,m_b), and call the residual row matrix C. The pair-anchored fourth-volume currency

H_ab := sum_{R subset I, |R|=4, {a,b} subset R} det Gram(M_R)

satisfies the exact factorization

H_ab = D2 * E2(C).

If the canonical E2(C) row marginals are all <=1/2, the grouped projected-crossing theorem with k=2, ell=2, d=4 applies after conditioning all coordinates outside I union J. Using the sharp two-subset entropy inequality H(w)+sum alpha log alpha <= log 2, its constant is

2 * 2^((2+6)/8) * 2^(1/8) = 2^(17/8),

and the geometric factors cancel:

S^(-1/4) E2(C)^(-1/8) = [D2 E2(C)]^(-1/8) = H_ab^(-1/8).

If some residual row has E2-marginal >1/2, promote it to a third literal hub; its anchored fourth-volume H_abc exceeds H_ab/2. The k=3, ell=1 receiver then costs at most 2^(15/8) H_ab^(-1/8), unless the remaining E1 law has a heavy row. In that final case a four-row determinant D4 exceeds H_ab/4, and the exact rank-four crossing theorem gives at most 2^(7/4) H_ab^(-1/8). Therefore the diffuse first branch dominates and suggests the row-marginal-free theorem

||p_Q||_infinity <= 2^(17/8) H_ab^(-1/8) = 4.362030930661031... H_ab^(-1/8),

with a continuous C_0 density.

This is not the full QFORM theorem. The next step is to write the conditioning/projection identities carefully, verify all constants, and spend the designated account04/B04 pair mass >2/75 at an actual inequality.
