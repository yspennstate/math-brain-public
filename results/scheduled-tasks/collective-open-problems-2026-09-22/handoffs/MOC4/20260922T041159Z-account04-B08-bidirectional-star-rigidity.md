# MOC4 handoff — account04/B08 bidirectional pair-gap ceiling

Run: `20260922T041159Z-account04-B08-moc4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account04/B08/20260922T041159Z-account04-B08-moc4-r11/REPORT.md`, creation commit `baddf2866a8e694bd2bd74c6dfee666dd3c6dd8d`. Exact verifier creation commits: `7922254dd2da662a6516d39bf449c285a1df2e0b` and `81f25d6285c772ed9182ecd23f466e7913acf2cf`; captured primary output creation commit `8431561ddd63c7fbcb7f52ecab2f9ef35a4778b1`.

## Named results consumed

- Campaign lead account03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`, report blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`.
- Assigned OTHER-account partner account01/B09 `MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1 = REFUTED`, report blob `ac3bec22cb51296419870e462aa83e585795088a`.
- account03/B09 `MOC4` cycle-separator no-go, shared handoff blob `ca3b1f48004bb6c9c29de34e29b64f39380b1641`, used to keep the remaining step support-specific.

## New theorem 1: bilateral ceiling

For endpoint support values `H_sigma`, write `M=max H`, `m=avg H`, `d=M-m`, let `Q` be the maximal `V4`-coset average and `Delta=M-Q`. Define

`g_out(tau)=2M-max_sigma(H_sigma+H_{tau o sigma})`,
`g_in(tau)=2M-max_sigma(H_sigma+H_{sigma o tau})`,

with sums `G_out,G_in` over the six transpositions. Every genuine support violation `h(U)=M+gamma` obeys

`0 < gamma <= R_bi/4`,

where

`R_bi = 3d-Delta-(1/2) max(G_out,G_in)`.

Proof: apply the lead theorem once to `(a,b,U)` and once to the swapped datum `(b,a,U*)`. The determinant is unchanged, while the swapped endpoint support is `H'_(sigma)=H_(sigma^{-1})`. Inversion preserves the `V4` fiber roof because `V4` is normal and exchanges the two transposition-composition sides.

## New theorem 2: exact zero-reserve endpoint-star rigidity

For any maximizing endpoint `sigma_*`, set

`B_*=(1/4) sum_{v in V4} H_(sigma_* o v)`.

For either composition side, let `e_tau(sigma_*)` be the excess of the global pair roof above the pair edge incident to `sigma_*`. Then exactly

`R_side = 3d-Delta-G_side/2 = (Q-B_*) + (1/2) sum_tau e_tau(sigma_*)`.

Hence each one-sided reserve is nonnegative, and it is zero iff the maximizing endpoint lies in a `Q`-maximal `V4` fiber **and all six incident transposition edges attain their corresponding pair roofs**. This is an exact characterization of the endpoint degeneracy that closes a support direction.

## Decisive correction to the preceding residual example

For the campaign lead's exact datum `a=(-1,2,1,0)`, `b=(-1,1,-2,2)`, real support:

`M=36`, `m=29/6`, `Q=15`, `d=187/6`, `Delta=21`.

The lead side has gaps `36,9,36,32,4,24`, sum `141`, reserve `2`, reproducing its `gamma<=1/2` allowance. The opposite side has gaps `36,36,9,4,36,24`, sum `145`, so its reserve is exactly `0`. Therefore the exact spectra/direction is safe for every true unitary. The unique maximizing endpoint has `B_*=Q=15`; all six opposite-side star excesses vanish. The lead's abstract half-integer witness remains valid only for its stated one-sided relaxation and does not survive the bilateral source-valid roof system.

## Assigned-partner negative control and next obligation

On account01/B09's simple-complex spectrum datum in real support, exact endpoint arithmetic gives `G_out=862`, `G_in=746`, one-sided reserves `529` and `587`, hence `R_bi=529`. Its maximizing endpoint is in a `Q`-maximal fiber, but the six-edge star-excess sums are `1058` and `1174`. The partner's actual dense unitary is already exactly certified inside the target hull and has a nonzero pair derivative, so it is not a residual maximizer/counterexample.

The first unpaid implication is now **`MOC4-BIDIRECTIONAL-RESIDUAL-PR-v1`**: on `R_bi>0`, exclude a genuine common-unitary global support maximizer with `0<gamma<=R_bi/4` using the exact `P-R-D`, pair-Rayleigh, Cartan/Hessian and structured spectral-normal constraints, or construct a genuine target counterexample. Transport-only or positive-lift surrogates are already refuted.

A separate attempt to persist the second verifier's captured-output text was denied by platform safety review; no bypass was attempted. The verifier source and the primary exact verifier/output are preserved.
