SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T06:53:55Z.
attacking: the exact two-sided tri-hub survivor by decomposing all physical E2 mass around one hub pair, then stress-testing whether tri-hub concentration really implies a bounded physical core.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

The previous same-hour B13 attempt is not being repeated: its common-envelope L^{3/2} gluing step was corrected because the hyperbolic envelope has a nonzero constant tail. This run changes mechanism to exact exterior-volume structure.

## 1. Exact hub-pair decomposition of second exterior volume

For a real cross block, isolate one physical row i and column j and write

    M = [[a, p^T],
         [q, R]].

Then the complete squared 2x2-minor mass admits the exact orthogonal-by-support decomposition

    e2(M^T M)
      = e2(R^T R)
        + ||p||^2 ||R P_{p^perp}||_F^2
        + ||q||^2 ||P_{q^perp} R||_F^2
        + ||a R - q p^T||_F^2.                                  (C1)

The convention for p=0 or q=0 is that the corresponding orthogonal projection is the identity. Proof: classify 2x2 minors according as they contain neither hub index, only the distinguished row, only the distinguished column, or both. The only-row minors are p_r R_{ks}-p_s R_{kr}; Lagrange's identity sums their squares to ||p||^2||R P_{p^perp}||_F^2. The column formula is symmetric, and the both-hub minors are aR_{kr}-q_k p_r.

Thus if J_ij:=||aR-qp^T||_F^2 carries a fraction 1-delta of the total E2 mass, all three residual currencies are individually <=delta E2(M). At the exact endpoint J_ij=e2(M^TM), rank R<=1 and the row/column alignment terms vanish; a short case split on p,q shows rank M<=2. This is a quantitative support-safe stability statement in exterior/star currencies, not a small-operator perturbation claim.

## 2. A valid target family showing tri-hub does NOT imply a bounded physical core

Fix 0<beta<1. For m>=1 let u=m^{-1/2}(1,...,1) in R^m and

    A_m = [[0,1],[1,0]]  direct_sum  [[0,beta],[beta,0]]  direct_sum  u u^T.   (C2)

Its spectrum is {1,-1,beta,-beta,1,0,...,0}; hence it satisfies the exact target spectral hypothesis for every m. For arbitrary independent cap-one inputs,

    Q_m = 2 X1 X2 + 2 beta X3 X4 + (u.Y)^2.                      (C3)

Every original-coordinate cross block A_m[I,J] has rank at most three: each of the first two 2x2 blocks contributes at most one rank-one crossing edge and the diffuse leaf bank contributes rank at most one. Therefore the pinned Claude D5 currency is identically zero on EVERY cut,

    e5(A_m[I,J]^T A_m[I,J])=0.                                  (C4)

If a cut has positive third volume, all three rank-one components must cross. Every nonzero 3x3 minor then contains the unique crossing row from each of the two pair blocks, so the natural third-volume row marginals of those two physical rows equal one. Hence the pinned D' gate max alpha_i<h<3/4 fails on every cut with e3>0. This is a genuine inequality-level obstruction to the D'/D5 cross-volume package, not a failure of QFORM.

For the cut I={1,3} union I_L, J={2,4} union J_L, every nonzero 2x2 minor uses at least one of rows {1,3} and at least one of columns {2,4}; thus 100 percent of E2 mass lies in a two-sided 2-by-2 hub set. Nevertheless any principal submatrix with three eigenvalues of modulus >=1 must contain both coordinates 1,2 and ALL m diffuse leaves: a k-leaf compression of uu^T has sole nonzero eigenvalue k/m, while the beta block has eigenvalues +/-beta. Hence the minimum physical-core dimension grows at least m+2.

So the implication "finite two-sided tri-hub E2 concentration => bounded-dimensional physical localization" is false even inside the exact target class. The closure must aggregate the diffuse bank jointly with the hub blocks rather than localize it away.

Next step in this run: prove a dimension-free density bound for (C3) directly from the designated partner's physical-pair L^{3/2} theorem plus a cap-one linear-projection/square estimate, so the family is certified as a mechanism counterexample rather than a QFORM counterexample; then record the exact finite-mixture/product-indicator transfer and the sharpened unpaid implication.
