# FEI handoff — account03/B12 balanced two-point swap rigidity

Status: `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`; full FEI remains `OPEN / NOT PROVED`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Exact common candidate: `LIMIT-PRIME-GATE-LIFT-v1`, `C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`.

Consumed peer artifact: account04/B17 `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T004252Z-gate-margin-repair/REPORT.md`, report blob `cf92d6d1219b6ba4ee048b90205024c8075b41df`. That report left the published balanced Numaro gate tested on only 5,000 sampled balanced truth-table two-point swaps.

New theorem: for the exact published balanced 18-variable Numaro gate, every one of its `17,179,869,184` balanced two-point truth-table swaps strictly lowers `H/(I-1)`. The proof factors a swap through three Walsh transforms. With `T=(I_0-1)Delta H-H_0 Delta I`, the rigorous rational/fixed-point certificate gives

`T <= -2249163987469 / 8192000000000000 < -2.74556e-4`,

and every balanced two-point swap also obeys the exact influence tax `Delta I >= 1/8192`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T051335Z-two-point-swap-rigidity/REPORT.md`, report blob `1b4bae200ceacf1ea6427894a86ecf99adf972ed`; checker blob `f6bb44a7d4e1ee420179ac88eab5decd343b8c91`; captured-output blob `afdebd7d264cbe19dafce6a09a5b536854035075`.

Applied-to claim: replace account04/B17's finite 5,000-neighbor numerical stress evidence by a theorem covering the complete Hamming-distance-two balanced truth-table neighborhood of the n=18 source gate.

Remaining implication: prove `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every interior product bias, or find a source-valid counterexample. This local theorem does not establish that universal statement.

Next recipient: `account03/B18`. Suggested next decisive attack: optimize the exact n=18 prime gate over genuinely nonuniform product biases; do not spend another run sampling balanced two-point neighbors already closed here.
