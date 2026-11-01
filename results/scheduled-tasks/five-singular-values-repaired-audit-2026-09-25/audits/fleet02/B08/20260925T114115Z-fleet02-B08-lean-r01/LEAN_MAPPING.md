# fleet02/B08 — Lean coverage reconciliation

Fresh control contains the later 25 Sep 2026 12:29 owner directive to pivot open-problem mathematics work to Lean verification of the repaired five-singular-value paper. This run therefore performed Lean-coverage reconciliation rather than another prose audit.

Exact repaired source: `math-open-problems@4e530247ec0ef4101a6e5ecf621bd35a969c42aa`, blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`, SHA-256 `90f859b7e52d0f57574a4f2e93e522177a715a3107173884c142dd84484560bb`.

## Fully closed: repaired Lemma 4.2, lines 260–269

The current central coverage table says `none`, but the existing compiled theorem `QformNine.entropy_lemma` in `lean/shared/QformNine2.lean` (blob `3ffc452a441f3371af4ee28a2df913adb984eb2d`) proves the repaired entropy lemma exactly: a nonnegative probability weight on the m-subsets of a finite set, m>=1, with marginals alpha_i, satisfies
`H(w)+sum alpha_i log alpha_i <= log(m^m/m!)`.

The theorem's finite-support, nonnegativity and total-mass hypotheses are exactly the paper's probability-distribution hypotheses. Its filtered sums are exactly the paper's marginals. Its RHS is exactly `log omega(m)`. The zero-weight convention agrees because the zero terms contribute zero.

Supporting Lean theorems in the same file are `pow_succ_ge` and `factorial_mul_esymm_le`, and the Jensen step uses Mathlib's concavity theorem for `Real.log`.

The file has no `sorry`, `admit` or explicit `axiom`. The committed `lean/shared/axioms_file2.log` (blob `8c62a00f65137e2c2b926fd57bef3627a81109fb`) reports for `QformNine.entropy_lemma` only `propext`, `Classical.choice`, and `Quot.sound`. Source and log were introduced together by commit `47b4d8b244bdf4bc25cb0f74e0b4314c1ad278b7` and are unchanged on current master.

**Status: repaired Lemma 4.2 is FULLY KERNEL-VERIFIED by an existing compiled theorem.**

## Additional formal coverage found

- Repaired line 385: `QformNine.omega_step` proves the nontrivial monotonicity `omega(k) <= omega(k+1)`. This is a kernel-verified subclaim of the heavy-row coefficient step; the greedy H construction/full theorem is not thereby formalized.
- Repaired Lemma 2.7(b), lines 163–172: `QformNine.gram_factor` proves the block Gram Schur-factorization core. The finite-index row-selection/permutation bridge to literal `Theta(H union T)` is still missing, so this is partial coverage.
- Repaired lines 471–475: `QformNine.concentration_constant_lt`, with `gamma_five_quarters_le` and `gamma_quarter_le`, proves the exact Gamma/log-convexity coefficient (<19). Thus repair 20's constant certificate is kernel-verified, although the full probabilistic Lemma 5.4 remains unformalized.

## Build honesty

This runtime has no `lean` or `lake`, so no fresh build was possible. No uncompiled code is counted as verified. Formal credit above is based on exact statement comparison plus the unchanged committed Lean source and its committed axiom-log evidence.

Next B08 Lean target: formalize the finite greedy-promotion lemma behind repaired lines 380–385 and bridge `omega_step` to the exact `a_k` inequality, then connect the determinant-weight setup to the hub lemma.
