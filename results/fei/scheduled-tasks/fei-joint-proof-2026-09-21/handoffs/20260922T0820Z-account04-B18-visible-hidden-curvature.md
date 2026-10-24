# FEI handoff — account04/B18 visible/hidden mixed-curvature split

**Run:** `20260922T081002Z-b18-fei-r22`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Scientific source: `yspennstate/math-open-problems` commit `40d53b2d7f2c8b388a95d4abd82221321f6fcfcf`,
`proofnet24/P03-fei/fleet-2026-09-22/account04/B18/20260922T081002Z-visible-hidden-curvature-split/REPORT.md`, blob `b22432baafae5b44e2ca3f73d63fc4dcf95d96b9`.

Consumed source-exact universal inputs:
- account01/B18 curvature-refunded crossing theorem (`20260921T1856Z-curvature-refunded-crossing`);
- account04/B14 candidate-independent criticality-matched stopping theorem (`20260922T071120Z-criticality-matched-stopping`);
- account04/B18 mixed-curvature conservation and exact zero-defect rigidity (`20260921T191147Z-mixed-curvature-global-rigidity`).

Fresh fixed-`Gamma^dagger` results from account01/B18 and account04/B12-B13 were read but are not spent as universal currency because the fixed candidate is source-exactly refuted globally.

For survivor `j` and revealed singleton `i`, let `c_{j<-i}=c_j({i})`, and let `p_{ji},o_{ji},kappa_{ji}` be the support-boundary, opposite-sign, and mixed-curvature quantities of derivative row `g_j` in direction `i`.  Median centering gives

`2 c_{j<-i} <= p_{ji} <= kappa_{ji}`.

Hence the nonnegative hidden remainder

`omega_{ji}=p_{ji}-2c_{j<-i}+4o_{ji}`

satisfies the exact split

`kappa_{ji}=2c_{j<-i}+omega_{ji}`.

For `K>2` define

`S_K=sum_{i!=j}(K+j'(q_j))c_{j<-i}`,
`U_K=sum_{i!=j}(K+j'(q_j))omega_{ji}`.

Then exactly

`4 sum_j (K+j'(q_j)) d_j = 2 S_K + U_K`.

At an `F/J`-critical core of ratio `rho>=K`, account01/B18 gives `S_K<=S_rho<=P-DTC(X)`, so

`boxed(sum_j d_j <= [P-DTC(X)]/(2K) + U_K/(4K)).`

At the natural candidate-independent target `K=4`,

`sum_j d_j <= [P-DTC]/8 + U_4/16`.

Combining with the existing relative-1/16 robust-row theorem gives

`sum_{robust j} R_j^ent < 4.814274 J + 0.83425 U_4`.

For exact-subcube rows the sharper bound is

`sum R_j^ent <= (2/ln2)J + (1/2)U_4`.

Thus the old raw second-factorial depth bank is no longer the correct unpaid object: its crossing-visible part is already paid by the existing phase/crossing bank.  The explicit residual is the hidden noncrossing/orientation bank `U_4`.

The exact all-row zero-depth branch remains closed by the one-point-defect classification with `H<4J`; therefore any `F/J`-critical obstruction with ratio `>4` has positive depth defect somewhere.

**Still unpaid:** (1) dimension-free payment or realizable elimination of `U_4` on positive-defect `K=4` terminal critical cores; (2) nonrobust positive-defect rows outside the inherited relative-1/16 near-subcube regime.  No `sum d_j=O(J)` or `U_4=O(J)` claim is made.  Full FEI remains OPEN / NOT PROVED.
