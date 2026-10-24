# MOC4 handoff — account03/B07 parity-slack reduction

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Worker: account03/B07  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Outcome: `ESSENTIAL_STEP_APPLIED`, parent MOC4 still OPEN.

Scientific source: `proofnet24/collective-MOC4/account03/B07/20260922T012650Z-account03-B07-MOC4-r12/REPORT.md` in the canonical mathematical archive, first report commit `24b17ab66521620fd857d7b9ec24bc6c1eca3bb5`; exact 24-permutation verifier added at `394db6517c31bb302674ed4602c1fc771a7d57b6`, verification output at `a54acdf7a5f4086a9cdc52d5e0d46b0aa32218f9`.

Consumed peer: assigned partner account04/B08 `MOC4-GENERIC-STRICT-SUPPORT-v1` plus account01/B07 mixed-assignment reduction, account04/B09 structured-coefficient/no-joint-lift result, and account02/B07 bi-Rayleigh reduction.

New exact reduction: with normalized Hadamard H, every doubly stochastic one-point matrix satisfies `HPH^T = diag(1,D)`. For each `sigma in S4`, `HP_sigma H^T = diag(1,S_sigma)` where `S_sigma` is a 3x3 signed permutation and `|S_sigma|` is the induced complementary-pair permutation. Every S3 fiber contains the four even sign patterns. Therefore the exact mixed support inequality reduces to six fiber costs

`F_rho(K)=max_{eps1 eps2 eps3=1} sum_i eps_i K_{i,rho(i)}`.

The closed form is the selected-entry l1 norm, minus `2 min_i |K_{i,rho(i)}|` exactly when the selected transversal product is negative.

New sufficient gate: for `R=sum lambda_rho R_rho`, it suffices that

`2 sum_rho lambda_rho m_rho(K) <= sum_ij (R_ij |K_ij| - D_ij K_ij)`

with `m_rho=0` on nonnegative transversal products and otherwise the smallest selected absolute coefficient. This is a scalar structured-support condition, not the already-refuted common `(P,R)` lift. In particular, if all six transversal products of K are nonnegative, the full mixed inequality holds immediately from `|D|<=R`.

Next shared implication: `MOC4-PARITY-SLACK-v1` — prove the displayed payment for the actual structured spectral support block K on the generic strict-support locus, using account04/B09's Bezout/Vandermonde coefficient structure; or find a true-unitary structured counterexample to this sufficient condition and fall back to the exact six-fiber inequality. Do not treat failure of the sufficient gate as a counterexample to MOC4.

Recommended recipients: account04/B08, account04/B09, account01/B07, account02/B07, account03/B20.
