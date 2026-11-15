---
name: t403_late_gain_at_n256_comes_with_rising_ixt_2026_11_01
description: [PROVISIONAL] T403 data sizes 32-256: compression null holds to N=128; at N=256 late phase cuts test err a fifth while I(X;T) rises
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T12:47:14+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T403 noisy tanh layer, width 8, 32 seeds per size, N = 32/64/128/256 training inputs, steps 3k to 40k (pushed 0978900, card claim_862113ce76cf42108b82af627e46ac35 export c30a37b, move be6c45cd).
Mean d test err +0.0006/-0.0005/-0.0020/-0.0056 (se <= 0.0012); median dI -0.170/-0.237/-0.055/+0.133; rho(dI, d test) -0.03/+0.25/-0.36/+0.34, none past Bonferroni 0.44.
At N = 256 only 12 of 32 seeds fit by 3k, and the late gain (a fifth of test error) is equal on fit and unfit seeds while I(X;T) rises in 23 of 32: the gain goes with norm growth and fitting, not compression.
N = 64 row reproduces the widths run digit for digit (a free check when changing one module constant).
My prediction that N = 256 would compress more was wrong.

**Why:** closes the one-data-size limit of the T403 notes.
**How to apply:** for a later first mark at N = 256 (fitting confounds the window), or to record train err at 40k, extend t403_sizes.py.

Related: [[t403_compression_barely_moves_test_error_2026_11_01]] - same set-up, one data size
Related: [[t403_null_holds_widths_4_to_32_ceiling_pins_2026_11_01]] - the widths version of this check

Update 1 Nov 12:57 (pushed 33562c4): marks 3k/10k/20k/40k at N = 256. 31 of 32 fit by 10k. Window 10k-40k: d test -0.0013 (se 0.0002), d train -0.0040, median dI +0.125, rho +0.06; 20k-40k: d test -0.0003. So the N = 256 gain is mostly fitting, and I(X;T) still rises after the fit. Nested windows on the same seeds, not independent.

Folder on research-repo: research_pushes/2026-11-01-loop-T403-sizes (T403_sizes.md, t403_sizes.py, the n32-n256 tables).

Folder: research-repo research_pushes/2026-11-01-loop-T403-late (the 1 Nov 12:57 update above)
