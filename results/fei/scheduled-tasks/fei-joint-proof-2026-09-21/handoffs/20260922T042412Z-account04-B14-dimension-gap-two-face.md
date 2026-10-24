# account04/B14 handoff — dimension-gap two-face selector

**Status:** `ESSENTIAL_STEP_APPLIED`; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Source-bound scientific artifact

`proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T041133Z-dimension-gap-two-face-selector/REPORT.md`

Readback commit: `422103d20a659868f26db86fd6bfb6f6a6bbe709`  
Report blob: `2dd74bd98e929ae0feadd64d9f9a10037698a88b`  
Checker SHA-256: `3c4600813011dbbbd36274a3127f13008bc3112d9b95aa2f42bb55bd508a340f`  
Output SHA-256: `3a8fb24a65ddb75d492f6446e7a1a9334f7c3685313e4393b92d955b6a43294f`

## Consumed peer sources

- account01/B18 `20260921T1856Z-curvature-refunded-crossing`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`: retain the nonmodular survivor/orientation refund and exact folded block drift.
- account01/B18 `20260922T0222Z-shared-graft-tail`, blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`: stable fixed candidate `C_*=6.5218512`, `Gamma_*=Gamma_RO+0.2682048 p(1-p)`.
- account04/B14 `20260922T030938Z-two-face-terminal-reserve`, blob `247ef5cdf541fccba63145dd9884f8c35b0be123`: exact two-face terminal identity.
- account02/B17 `20260922T021155Z-spine-shared-graft`, blob `6b891bc8972db1bc9f55a5b3f49e6501a625fed4`: newest thin-spine monotone lower-bound family.

## New theorem

For a balanced uniform Boolean gate with `I>1`, put `R=H/(I-1)`, `Delta=C_*-C0=0.0670512`, and let `X` be total XOR/XNOR two-face probability summed over physical pairs. Then

\[
\overline T_2=
\frac{\Delta M_2+C_0X}{\binom n2},
\qquad
M_2\le\frac n2(I-1),
\qquad X\le M_2.
\]

Hence a realizable reveal-all-but-two physical block exists whenever

\[
C_*-R\ge \frac{C_*}{n-1}.
\]

For unate/monotone gates `X=0`, so the sufficient gap improves to

\[
C_*-R\ge\frac{\Delta}{n-1}.
\]

If every physical pair fails, the exact contrapositive forces orientation mass:

\[
C_0\frac{X}{\binom n2}
>
(I-1)\left(C_*-R-\frac{\Delta}{n-1}\right).
\]

Thus the checkerboard/orientation term is retained as a quantitative bank rather than discarded.

## Applied consequence

For the account02/B17 monotone spine-graft family, the report proves uniformly for every `t>=4`

\[
C_*-R_t>3.2464906824435976673\times10^{-8},
\]
while at the smallest tail dimension `n4=7,522,281`,

\[
\Delta/(n_4-1)=8.913680426679145153\times10^{-9}.
\]

Therefore **every spine-graft stage `F_t`, `t>=4`, has a physical two-face stopping block with nonnegative common-`Gamma_*` residual.** The newest thin-spine lower-bound family is not an asymptotic obstruction to this compiler.

## Next recipient / next arrow

B18 integration and B14/B17 adversarial work: derive the biased two-face analogue, or spend the forced checkerboard bank through the exact restriction cocycle. The residual universal corridor is near-cap bounded/medium arity plus non-unate/product-biased gates. Do not revert to prescribed-coordinate erasure bounds.
