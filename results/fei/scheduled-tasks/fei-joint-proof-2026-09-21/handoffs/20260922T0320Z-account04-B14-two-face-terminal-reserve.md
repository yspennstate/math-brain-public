# account04/B14 — exact two-face terminal reserve under the fixed FEI gate candidate

**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_TERMINAL_DECOMPOSITION`; full FEI OPEN / NOT PROVED; `WITHOUT_VERIFIED_BRAIN`.

**Scientific source:** `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T030938Z-two-face-terminal-reserve/REPORT.md`, report blob `247ef5cdf541fccba63145dd9884f8c35b0be123`; checker/output are adjacent. Stable candidate consumed from account01/B18: `C_*=6.5218512`, `C_0=6.4548`, `Gamma_*=Gamma_RO+4(C_*-C_0)p(1-p)`.

For any uniform-cube Boolean `f`, any pair `i<j`, and the physical two-face obtained by freezing all other coordinates, let `X_ij` be the probability that the face is XOR/XNOR. With normalized mixed derivative

`D_iD_j f=(f00-f10-f01+f11)/4`, the two-variable gate classification gives the exact identity

`E_z D_{Gamma_*}(f_{ij|z}) = (C_*-C_0)||D_iD_j f||_2^2 + C_0 X_ij`.

Averaging pairs and using Parseval,

`avg_{i<j} E_z D_{Gamma_*}(f_{ij|z}) = ((C_*-C_0)/binom(n,2)) sum_S binom(|S|,2) fhat(S)^2 + (C_0/binom(n,2)) sum_{i<j} X_ij`.

The XOR/checkerboard surcharge is essential; deleting it repeats the known unsigned-curvature/orientation mistake. For monotone gates it vanishes exactly.

Applied to the exact prime monotone `G10`, all 11,520 physical two-faces are: 6,894 constant, 2,882 unary, 1,744 AND/OR, zero XOR. Hence `sum_{i<j}||D_iD_jG10||_2^2=109/64` and the mean terminal reserve is exactly `1522621/600000000 = 0.002537701666...`. The root fixed-candidate slack is in `(0.062967034911848520,0.062967034911848521)`, leaving a rigorous root-minus-mean-two-face corridor above `0.0604293332451818533`.

**Consumed curvature source and exact use:** account01/B18 `20260921T1856Z-curvature-refunded-crossing` remains valid but does not directly imply the all-gate candidate because it is formulated for the character-centered `F/J` restriction ledger. Its source-valid use here is structural: retain the nonmodular survivor/orientation refund. The two-face formula above is an exact terminal realization of that requirement under the current `Gamma_*`.

**Next arrow:** on the balanced-uniform prime-gate slice, prove that some physical pair satisfies

`D_{Gamma_*}(P) >= E_z D_{Gamma_*}(P_{ij|z})`,

or falsify this exact restriction compiler with a source-valid composition-prime gate. The RHS is now an explicit mixed-curvature + checkerboard bank. A counterexample to the pair compiler does not refute FEI unless the root gate defect itself is negative.

Known addressing/per-coordinate-erasure obstructions and the exact folded block drift `J-EJ_child` are preserved.
