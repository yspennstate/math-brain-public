SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T09:16:13Z.

attacking: spectral-window complementary Schur shielding for arbitrary extra signed spectrum, allowing an arbitrary singular/unbounded complementary tail and charging only its coupling leakage.

# Early substantive checkpoint

Let an actual original-coordinate principal block be represented, for deterministic matrix algebra only, in an orthogonal decomposition W + P + Q as

H = [[C, Bp, Bq], [Bp^T, Dp, 0], [Bq^T, 0, Dq]],

where C and Dq are arbitrary symmetric, Dp is symmetric with every singular value at least mu>0 and dim(P)>=3. Put rho=||Bp Dp^{-1}||op and ell(rho)=(sqrt(rho^2+4)-rho)/2. Account04/B12's completed complementary-Schur shield applied to the active W+P block gives

s3([[C,Bp],[Bp^T,Dp]]) >= ell(rho)^2 mu.

Setting Bq=0 makes H a direct sum of that active block with Dq, hence s3(H0)>=ell(rho)^2 mu regardless of every eigenvalue of Dq. The omitted symmetric off-diagonal block has operator norm exactly ||Bq||op, so Weyl gives the new implication

s3(H) >= ell(rho)^2 mu - ||Bq||op.

Thus an arbitrary additional spectral tail in Dq, of any rank, signs, magnitudes, and including exact zero modes, costs nothing; only its coupling leakage Bq is charged. A further dense perturbation T costs ||T||op deterministically. This is the core implication to be completed and checked this run.

Full QFORM remains open; this checkpoint is not a full solution and makes no continuity claim.
