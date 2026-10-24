# B16 FEI signed-transport handoff — Shapley/plaquette bridge

Status: **PARTIAL / PROVED IDENTITIES / FULL FEI OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

This run connects three live signed routes exactly. For account02's weight-four q-flip relation basis, let `g_v` be the dual phase-quotient generator and `L_v` the exact Aumann--Shapley R32 charge. If `M` is the active syndrome set, define `C_v^M` as the Shapley-weighted sum of account04 plaquette curvatures encountered before `v`, and `Theta_v^M` as the Shapley share of the retained terminal response. Then, in the same entropy normalization as R32,

`(8/N)L_v = H(g_v) - C_v^M - Theta_v^M`.

The subset coefficient of a plaquette based at a prefix `S`, with `h` crossed before `v`, is exactly `|S|!(|M|-|S|-1)!/|M|!`. Summing over `v` returns the original R32 residual and keeps negative curvature/frustration credits and terminal payment exactly once.

For an ordered-min pivot basis the dual generator is explicit: its `-1` set is the descendant subcube of `v`, of codimension `c`; its squared spectrum is one mass `(1-2^(1-c))^2` and `2^c-1` equal masses `2^(2-2c)`. Randomizing the coordinate order preserves account02's pivot marginals. The expected raw positive generator-entropy baseline reaching a fixed physical edge, in relation-load units, is `(1/(2n)) sum_{c=2}^n (2^(c-1)-1) H_c = n+O(1)` bits. Thus unsigned baseline geometry still misses dimension-free payment by a factor of order `n`; the signed plaquette/terminal refund is essential.

A second exact bridge uses the original cut indicator `eta_i=(1-f(x)f(x+e_i))/2`. For a q-flip made of two parallel `i`-edges separated by nonzero `w` with `w_i=0`,

`Pr_a[qflip frustrated] = 4 sum_{U: U·w=1} eta_hat_i(U)^2`.

Averaging nonzero `w` gives `[2^n/(2^(n-1)-1)] Inf_i(f)(1-Inf_i(f))`. This is the same cut-Fourier field used by account01's signed noise-square `L2` payment.

Next target: substitute the exact signed Fourier log-cross-ratio for the plaquettes in the Shapley bank and group by the cut-spectrum identity above. Prove the resulting basis-averaged edge residual is `O(1/N)` per disagreement edge; do not absolute-value the cross-ratio bank, the R32 signs, or the terminal/R16 refunds.

Self-check: `check_shapley_plaquette_bridge.py`, SHA-256 `f1c95c87e0652fed0b7150a0594be15126bf4d7d51c6bbc8a4d59c754b8a189d`; output SHA-256 `88df68f14dc74e381b39ba796c3391f1083d414d1c3ff25dd332698b4bf775eb`. `py_compile` PASS; 814 dual checks, 182 Shapley/plaquette checks, 33 exact Aumann--Shapley checks, 2,336 exact cut-Radon checks and 800 exact averaged cut checks.
