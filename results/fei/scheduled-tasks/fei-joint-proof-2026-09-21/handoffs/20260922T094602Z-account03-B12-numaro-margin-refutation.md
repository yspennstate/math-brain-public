# account03/B12 handoff — Numaro prime gate refutes AND extremality for the owner margin

Source run: `20260922T094602Z-account03-B12-7aecd43a`.

Scientific artifact: `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T094602Z-numaro-margin-refutation/REPORT.md`, scientific commit `a15bf667e4d04097e95481dc97e0d1c1554409a6`, report blob `3e9409f4513ca905593c16872d848670e733e7c5`.

## Result

For the current read-once base potential `Gamma_0`, let

`Q_G = I(G;p)/4 - p_out(1-p_out)` and `c_G=-D_{Gamma_0}/Q_G` when `Q_G>0`.

Consumed peer artifact: account01/B16 `20260922T0912Z-tilted-quartic-strong-prime-refutation/REPORT.md`, blob `10493748314dbe8071acefcf62c5befcf4aacfab`.  It certifies on the exact composition-prime 18-input Numaro gate at

`p_1=223/456`, `p_2=...=p_18=1/2`, `p_out=1019/2048`

that `D_{Gamma^dagger}<-38023/10^6` for

`Gamma^dagger=Gamma_0+0.268204856 p(1-p)`.

Affine dependence of the defect gives the exact identity

`D_{Gamma^dagger}=D_{Gamma_0}+0.268204856 Q_G`.

The exact pivotal data imply

`Q_G=62098577/239075328`.

Therefore

`c_G > 3218187637329239/7762322125000000 = 0.4145908383477759...`.

The existing all-bias read-once interval certificate proves two-input AND is valid for `Gamma_0+0.01 p(1-p)`, hence every defined positive AND margin satisfies `c_AND<=0.01`.  Thus the live operational claim that AND/decomposable gates maximize the owner-normalized margin is rigorously refuted, with certified gap exceeding `0.4045908383`.

This is **not** a counterexample to FEI and is **not** a universal lower bound on the optimal FEI constant; it eliminates the stated `Gamma_0`/AND-extremality closing mechanism.

## Required integration

- candidate_version: `OWNER-CG-EXTREMALITY-v1`
- prior_missing_implication: prove AND/decomposable extremality for `c_G`, or find a genuine gate/bias above AND
- new_result: `CANDIDATE_REFUTED`
- replacement_obligation: use a different symmetric potential shape or a universal theorem that permits genuinely prime extremizers; test the `223/456` Numaro witness first
- consumed_peer_artifact: account01/B16 `20260922T0912Z-tilted-quartic-strong-prime-refutation`, blob `10493748314dbe8071acefcf62c5befcf4aacfab`
- applied_to_claim: owner-normalized AND extremality
- next_recipient: account03/B18
- remaining_implication_to_full_FEI: construct and prove one finite-cap symmetric potential satisfying the all-gate inequality for every Boolean gate and every product bias
- full_FEI_status: `OPEN / NOT PROVED`
- execution: `WITHOUT_VERIFIED_BRAIN`
