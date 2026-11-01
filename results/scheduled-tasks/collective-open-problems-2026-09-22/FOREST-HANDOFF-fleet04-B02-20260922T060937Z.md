# FOREST handoff — fleet04/B02 — 20260922T060937Z

Outcome: `ESSENTIAL_STEP_APPLIED`. Parent FOREST remains `OPEN`. `WITHOUT_VERIFIED_BRAIN`.

Consumed named other-account results: fleet01/B01 `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1` (shared blob `4cee205cb7d254caf785692838111988a0b8a155`) and partner fleet01/B03 complete run `20260922T052013Z-b03-forest-r11-d011c5` (report blob `d975b5c7b4257aee81eb4ee136b0cccce64b5033`).

New exact obstruction to the partner's missing Hall step: write `L=(N\A)xD`, `R=A x (B\D)` and `mu_g(F,H)=1[g in F]+1[g in H]`. Every fleet01/B03 full-radius reconnection has `F'=F\T,H'=H union T` with `T` absent from `H`, hence preserves the entire vector `mu`.

For disjoint marks `e=01,f=23` in `K5`, fix the fibre with multiplicity one on `{02,03,12,13}` and zero on every other base edge. It has exactly four left states but only two right states. Therefore no injection or fractional unit-capacity transport preserving `mu` can close the residual comparison, even with unlimited radius and arbitrary within-fibre recolouring. Across all multiplicity fibres of this `K5` instance, the exact zero-defect capacity is `1924<2030`, so at least 106 left states must cross multiplicity fibres. The target itself has strict slack `Delta=210` (`N=134,A=B=64,D=29`).

A one-multiplicity-coordinate-defect capacitated fibre flow repairs this exact instance: integer max flow `2030/2030`. This is finite evidence only, not a theorem. The exact next candidate is the universal capacitated Hall inequality over fibre vectors with Hamming-distance-at-most-one adjacency. The proved lesson is narrower and unconditional: **any universal direct exchange/coupling must sometimes change the two-coordinate multiplicity of at least one base edge**; continuing to optimize only the partner's multiplicity-preserving full-radius path moves cannot succeed.

Canonical run root: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B02/20260922T060937Z-fleet04-B02-forest-exchange-r13/`.
