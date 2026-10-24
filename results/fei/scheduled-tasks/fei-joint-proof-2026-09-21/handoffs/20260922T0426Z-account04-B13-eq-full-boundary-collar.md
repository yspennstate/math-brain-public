# account04/B13 handoff — EQ_d has a full safe boundary collar for the stable gate candidate

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0426Z-eq-full-boundary-collar/REPORT.md` in `yspennstate/math-open-problems`, creation commit `2e2c7328ae624ad48358a8139cb2e1badc4f74cc`, readback blob `ae6b28a3f05cd91f24b344bdaa9d4a954e1b8d07`.

**Result.** For every fixed `d>=3`, for the stable candidate
`Gamma_*=Gamma_RO+0.2682048 p(1-p)` there is `eta_d>0` such that

`min_i {p_i,1-p_i} < eta_d  =>  D_{Gamma_*}(EQ_d;p)>0`.

Thus at positive Poincare currency the gate margin satisfies `c_EQ_d(p)<0` throughout a full boundary collar. Any counterexample in the antipodal family is confined to the compact box `[eta_d,1-eta_d]^d`.

**New mechanism.** Decompose the antipodal gate globally into its two one-corner read-once gates. If their exceptional-corner probabilities are `P=prod p_i`, `Q=prod(1-p_i)`, then

`D_EQ = D_A + D_B + Gamma(P)+Gamma(Q)-Gamma(P+Q) - (H_EQ-H_A-H_B)`.

When both corners are rare, the spectral interaction is bounded by a Fannes term `O_d(PQ log(1/PQ))`, while the exact source tail gives

`Gamma_*(P)+Gamma_*(Q)-Gamma_*(P+Q) = A(P+Q) h2(P/(P+Q)) + 2 a_* P Q`, `A=4.9096`,

which dominates the interaction for arbitrary relative rates. One-orientation faces are handled by strict one-corner read-once reserve; the only zero-reserve one-active-coordinate face has reserve `Theta(nu)` while the opposite-corner perturbation is `o(nu)`. Simultaneous all-zero/all-one vertices use account01/B16's hierarchical rare-corner theorem.

**Newest peer consumed.** account02/B18 `20260922T040428Z-random-block-currency`, blob `bd4972b11cb13989282f555deb9354509d1da590`. Its exact block identity changes the interpretation: every `(d-1)`-block restriction of `EQ_d` is constant or literal, hence

`B_{d-1}^{RO}(EQ_d)+a_* Q_{d-1}=D_{Gamma_*}(EQ_d)`.

So the boundary theorem supplies an explicit terminal-scale witness for `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1` on this family. This aggregate route deliberately avoids the now-refuted pointwise local-cap architecture; account03/B13's bent-swap report, blob `3f3e5294853654e0539f2e11fad49a3fed344136`, proves such local requested corrections are unbounded.

**Verification.** Committed checker blob `0c9b842b6cfb819a5bbc5f1568dc6ffe8c9eed33` is byte-identical to the locally executed checker (SHA-256 `11cec8cc35c0826b66a6b096b3ceb1ce09cc8a11ffd0c4255ee0c5f679d7bbdb`). Output blob `deb32a36e00ee95a3eacaaae916fcec272b1af54`, SHA-256 `f330927a5abd42cb6e06f8296991194b4f7b7dfa222024d297eaac84800fe7b9`, reports PASS over 744 numerical falsification cases. The proof is analytic; the checker is not promoted to proof evidence.

**Status.** Full FEI remains OPEN / NOT PROVED. The compact interior of `EQ_d` and unrelated composition-prime gates remain open. Account04/B18 mixed-curvature conservation and the exact zero-defect classification are preserved unchanged. Execution status: WITHOUT_VERIFIED_BRAIN.
