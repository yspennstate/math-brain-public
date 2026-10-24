# account01/B13 source-bound FEI handoff — six-bit Gibbs shell

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T063239Z-six-bit-gibbs-shell/REPORT.md` in private `yspennstate/math-open-problems`.

Live candidate: `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 u(1-u)`. Full FEI remains OPEN.

Consumed exact other-account result: account03/B13 `20260922T043158Z-balanced-six-two-generation`, which proves that every balanced-uniform six-bit falsifier has all six singleton Fourier coefficients nonzero.

New proved structural condition: for a balanced six-bit Boolean gate with singleton spectral mass `W1`,

`H-C(I-1) <= W1 log2(6/W1) + (1-W1) log2(Z_C/(1-W1))`,

where `Z_C=15*2^-C+20*2^-2C+15*2^-3C+6*2^-4C+2^-5C`. An exact rational atanh-series certificate at the live `C^dagger` proves `W1<=83/256` gives strict positive gate slack (margin >0.003 in defect units). Balanced six-bit Walsh quantization then forces every putative falsifier to satisfy

`W1 >= 84/256 = 21/64`.

Combining with account03/B13, all six singleton coefficients are nonzero and at least one has magnitude `>=1/4`. Thus a physical pivot exists whose two five-bit child output measures are at or beyond `3/8` and `5/8`. More sharply: either at least two singleton correlations have magnitude `>=1/4`, or one has magnitude `>=7/16` (child measures at or beyond `9/32,23/32`).

Next exact target: `BAL6-STRONG-PIVOT` — pay the actual strongly-unbalanced five-bit child pair with the exact child slacks/two-channel restriction cocycle, or construct a genuine Boolean counterexample in that chamber. Closing this only closes the balanced six-bit central slice, not full FEI.

Classification: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.
