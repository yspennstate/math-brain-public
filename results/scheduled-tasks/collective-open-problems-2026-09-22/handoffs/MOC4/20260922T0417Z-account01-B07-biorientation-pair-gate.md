# MOC4 handoff — account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1`

Run: `20260922T040155Z-a01-b07-moc4-r12`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical private mathematical report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account01/B07/20260922T040155Z-a01-b07-moc4-r12/REPORT.md`, creation commit `a643a4e465e4f0243a961c10cad73aeb60089be2`, blob `629288d290e89315693afda2f95b48ad8c23a8e3`. Exact Fraction verifier blob `3e67229f7e732774b853d5148b8efc0db7095432`; captured output blob `a1f323533c7cbec33a470380121d4d625624729d`.

## Team state consumed

- Latest complete campaign lead: account03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`, report commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. Any support violation `h(U)=M+gamma` obeys `0<gamma<=(3d-Delta-G/2)/4`.
- Named assigned OTHER-account partner consumed and applied: account02/B08 `MOC4-CIRCLE-FACE-REDUCTION-v1`, report commit `290ef6e19e8d1bd99decc388191b3dd1fccdb0f8`, blob `5e52a9d9463e30108d1de0c5269d693dfd4e4ef3`. It closes common-circle data and sharpens the repeated/common-block boundary, so the new gate is aimed at the simple-spectrum irreducible residual.
- Compatibility dependency: account03/B09 `MOC4-ODD-TWIST-MASS-v1` supplies 16 true-exterior-square channel-mass inequalities.

## New exact mixed-minor gate

In the exact `SO(6)` exterior-square block form let `D_ab=det B_ab`, `R_ab=||B_ab||_F^2/2`, so the nonconstant support is `k+x=<D,K>+<R,X>/2` and `D=(1/4)E^T P E` for `P=|U|^2`.

At a **global true-unitary support maximizer**, for every row-plane pair `alpha<gamma`, define

`T^L_ag = sum_b(K_ab D_ab + K_gb D_gb) + (1/2) sum_b (X_ab-X_gb)(R_ab-R_gb)`

and

`C^L_ag = sum_b(K_ab D_gb + K_gb D_ab)`.

Then

`T^L_ag >= |C^L_ag|`.

The identical column version holds:

`T^R_bd >= |C^R_bd|`.

Proof: for each sign `eps=+/-1`, swap the two selected real complementary-pair planes using the genuine `SO(6)` block map `[[0,Z],[-Z^T,0]]` with `Z in O(2)`, `det Z=eps`. Spin(6)=SU(4) makes both swaps actual unitary competitors. They exchange the two `R` rows (or columns) and send the two `D` rows to `eps` times each other. Global maximality gives `T-eps C>=0` for both signs, hence the absolute-value gate. No inverse, independent-bistochastic lift, or phase relaxation is used.

Summing the three row gates and separately the three column gates yields

`2k+3(x-cbar) >= max( sum_{a<g}|(K D^T + D K^T)_ag|, sum_{b<d}|(K^T D + D^T K)_bd| )`.

Together with the lead inequalities, every residual violator must satisfy

`max{ Ccross(D,K), 6 gamma + G/2 } <= 2k+3(x-cbar) <= 3d+2 gamma-Delta`.

Eliminating `gamma` gives the necessary P-side band

`Ccross(D(P),K) <= (9/2)d - (3/2)Delta - G/4`.

This is a new exact `P/R` maximizer restriction inside the lead's positive-reserve branch.

## Decisive exact application

The earlier source-valid generic datum that refuted universal `MOC4-PARITY-SLACK-v1` is **not** in the new maximizer core. For its column complementary-pair planes `12|34` and `14|23`, exact Fraction arithmetic gives

`T = 24555162551497262400033111 / 156250012500000250000000000`,

`C = -27515600499968722687177263 / 156250012500000250000000000`,

so

`T-|C| = -370054743558932535893019 / 19531251562500031250000000 < 0`.

Thus the genuine orientation-reversing pair-plane swap strictly raises support by the opposite positive amount (about `0.01894680135447`). This exactly explains why that hard generic datum cannot be a global maximizer; it remains only a counterexample to the old parity-slack proof mechanism, not to MOC4.

## First remaining implication

`MOC4-RESIDUAL-PR-BIORIENTATION-v1` (OPEN): on the simple-spectrum irreducible positive-reserve branch, exclude every actual common-unitary exterior-square point satisfying `D=(1/4)E^TPE`, full block orthogonality, the 16 odd-twist mass inequalities, all six new row/column bi-orientation gates, and the lead residual sandwich; or construct a genuine spectral/common-unitary counterexample satisfying all of them. Formal `S4`, 48-colour, low-frequency, or independent-bistochastic witnesses do not count.

Recommended consumers: account03/B07 lead, account02/B08 assigned partner, account03/B09 compatibility lane, account03/B20 integrator.
