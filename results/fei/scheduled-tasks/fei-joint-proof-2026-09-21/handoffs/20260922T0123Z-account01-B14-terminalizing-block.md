# FEI handoff — account01/B14 terminalizing block for the prime n=18 obstruction

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T010918Z-prime-terminalizing-block/REPORT.md`, commit `c81a7001e59155f13c4a5cbf64eda6b9e815ead0`, blob `5b16ac695c4a95404fbd20d8a960bb7b7984760a`.

Classification: `AUXILIARY_ONLY`. Full FEI remains OPEN / NOT PROVED.

Source-bound peer consumed: account04/B14 `20260922T003849Z-prime-gate-falsifier`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`, which proves the Numaro balanced n=18 gate is composition-prime and supplies `I=261/128` and the certified entropy interval.

New exact identity for any product-biased physical block A and any gate potential Gamma:

`D_Gamma(G) = E_z D_Gamma(G_z) + P_A - Delta_A H - Lambda_A`,

where `P_A` is the exact removed-input payment and `Lambda_A=Gamma(p_out)-E Gamma(p_out(G_z))`. This retains the full child slack rather than dropping it.

Actual block policy: take an independent set B in the ANF nonlinear interaction graph and reveal A=B^c. Every child is affine on B, hence a signed character and has spectral entropy zero.

For the exact source-bound n=18 gate, reveal the nine core coordinates. The remaining nine host variables occur on pairwise-disjoint two-point core masks, so 494/512 branches are constant and 18/512 are dictators/negated dictators. Each host coordinate has influence `1/256`; therefore `I_A=513/256`, while `Delta_A H=H`. Hence

`Delta_A H / I_A < 3.382`.

The gate's large center requirement is isolated exactly to the output-potential current. Writing `C=Gamma(1/2)` and using `Gamma(0)=Gamma(1)=0`, all children have zero gate slack and

`D_Gamma(f)=C*(133/128)-H(f)`.

Therefore this source forces `C >= H/(133/128) = 6.521845710923046...`; changing Gamma away from the endpoint/center values cannot help this particular terminalization.

Interpretation: the strongest source-bound prime obstruction checked here does NOT obstruct a realizable physical block selector; it obstructs the potential through the 494/512 constant-child current. The universal missing implication is now to control that current (or replace it by a globally telescoping payment) for a source-valid block-selection policy on all composition-prime gates/all biases.

Late same-account refresh: account01/B16 has additionally delivered an explicit balanced composition-prime arity-10 gate with `I=257/128`, `H/(I-1)>6.459372281637855731` and read-once-base required margin `>0.018289126551422926`. It does not supersede the n=18 lower bound, but it is the next small prime witness on which to execute this terminalizing/current analysis.
