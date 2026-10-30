# Fresh integration addendum

After the main B18 report was written, `proofnet24/P03-fei` master advanced with two relevant deliveries. I read them before closing this run.

1. fleet02/B17 `20260921T181122Z-positive-xor-coupling-obstruction/REPORT.md`, blob `3b37732ccb10fbdcf1d800f667edccee1b261436`, proves that even an exact positive classical XOR coupling of parent/child squared spectra can fail for genuine Boolean functions, with a quantitative subgroup-cut obstruction. This is independent of B18's bent-function refutation of “spectral block MI + Boolean convolution => near signed product”, but the two results point in the same direction: a universal integration proof cannot erase the signed/phase bank.
2. fleet02 interactive `20260921T174421Z-centered-critical-budget/REPORT.md` (manifest commit `a5d37408b0bb0a1ac90f82b9fe73ec3c659b2688`) proves exact centered restriction-budget telescoping and reduces a worst-ratio argument to primitive centered restriction-critical cores. It explicitly leaves full FEI OPEN and separately refutes every-prescribed-coordinate payment.

These additions do not change any theorem or classification in the main B18 report. They sharpen the next integrated target. On a primitive centered critical core of ratio `R`, the exact nonreuse identity says a universal FEI bound would follow from finding one visited block with entropy decrement paid by a constant times centered budget decrement. B18's new row theory supplies a phase-aware trichotomy for the derivative objects entering such a block:

- low depth defect: majority-sign subcube proxy, channel-stable Hellinger control, and off-axis mass `O(Delta/log(1/Delta))`;
- low reduced-state entanglement: near-product measurement law, with exact ternary tensor recursion at zero entanglement;
- large entanglement/mixed-axis/sign bank: must be charged through the signed B13/B16 mechanisms rather than through spectral MI or a positive classical coupling.

The remaining nonoverlapping implication is therefore an **existential centered block payment on primitive cores** that converts those three branches into `Delta_A <= C D_A` for at least one admissible block, or else produces a proper restriction with a strictly larger centered ratio. The latter alternative is forbidden by primitive criticality. Proving that payment would close the centered restriction induction; it is not proved here.

Status: **OPEN** for full FEI. This addendum is coordination/source integration, not a new theorem beyond the main report.
