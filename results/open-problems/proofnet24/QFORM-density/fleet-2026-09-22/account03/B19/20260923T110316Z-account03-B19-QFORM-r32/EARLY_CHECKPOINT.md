# account03/B19 r32 early checkpoint — TRIANGLE active-Gram reconditioning

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN.

Starting from account03/B19 r28's exact-rank-three TRIANGLE state, let `A=RMR^T`, `R^TR=I_3`, `s_min(M)>=1`, split ORIGINAL coordinates as `I union J`, put `H=R_J^T R_J`, `W=range(H)` (dimension two), and normalize the physical receiver rows by `v_j=(H|_W)^(-1/2)s_j`. The normalized rows form a Parseval frame on `W`. r28 gives an actual pair `T={j,k}` with

`d_T=det(v_j,v_k)^2 > d0:=377/1344`.

Let `K=I union T`, `L=J\T`, and `G_K=R_K^T R_K=I-R_L^TR_L`. Put `P_T=v_jv_j^T+v_kv_k^T`. Then `0<=P_T<=I_W`, `det P_T=d_T`, and

`R_L^TR_L = H_W^(1/2)(I_W-P_T)H_W^(1/2)` on `W` (zero on `ker H`).

Since `0<=H<=I`,

`lambda_max(R_L^TR_L) <= ||I-P_T|| = 1-lambda_min(P_T)`.

Because both eigenvalues of `P_T` are at most one and their product is `d_T`, `lambda_min(P_T)>=d_T`. Hence

`boxed: lambda_min(G_K)>=d_T>d0=0.2805059523...`.

Therefore the conditional active quadratic matrix `B_K=R_KMR_K^T` has exactly three nonzero eigenvalues, all of absolute value at least `d0`. After conditioning the ORIGINAL coordinates in `L`, the induced affine vector lies in `range(R_K)=range(B_K)` and is removed by a deterministic coordinatewise translation, preserving independence and the cap-one marginal densities.

Immediate consequence: if the active rank-three range projection has every physical leverage at most `1/2`, Claude Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies conditionally and gives

`||p_Q||_infinity <= 12/d0 < 42.780`,

with a continuous density in this subbranch. Thus the remaining TRIANGLE obstruction must contain an active physical row of leverage `>1/2`.

Next: combine the finite number of such high-active-leverage rows with the selected pair `T` and use bounded-dimensional spectral reception when their active Gram is robust; isolate the genuinely coupled complementary-source residue if it is not.
