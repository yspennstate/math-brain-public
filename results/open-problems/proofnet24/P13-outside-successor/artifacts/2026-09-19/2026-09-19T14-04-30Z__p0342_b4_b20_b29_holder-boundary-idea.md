# P13 / P0342 research idea — B4, B20, B29

UTC run: 2026-09-19.  
Target: current exclusive P13 successor `P0342`, Aldous--Janson Open Problem 12.  
Frozen source metric is already `M_P0342=2/2`; nothing below changes its denominator or reopens a completed source obligation.

## Why this route

The existing positive-variance counterexample works by adding to a genuinely local Gaussian mark `Psi` a bounded continuous perturbation `Phi` which is exactly zero on every infinite fringe tree but accumulates coherently over all `n` finite leaf rerootings. The preceding run showed the sharp amplitude threshold `n^{-1/2}` for that explicit root-split family. The natural next question is not another amplitude calculation but: **what quantitative form of locality actually forbids this entire boundary-invisible mechanism?**

I will try three new-method moves, different from the previous B2/B7/B12 triple.

### B29 — add the points at infinity

View finite leaf-rooted full binary trees as approaching the boundary of infinite one-ended leaf-rooted trees in the standard local metric. For a finite rerooting `T_i`, let `d_i` be the graph distance from the distinguished leaf `i` to the original phylogenetic root (the unique degree-two vertex in the unrooted finite tree). Attach an infinite binary spine beyond that original root. This produces an infinite one-ended extension `T_hat_i` agreeing with `T_i` through radius `d_i-O(1)`.

Thus a boundary-vanishing functional `g` with Holder modulus `|g(S)-g(T)| <= C d_loc(S,T)^beta` obeys

`|g(T_i)| <= C_beta 2^{-beta d_i}`.

The leaf depths satisfy the exact Kraft equality

`sum_i 2^{-d_i} = 1`.

This converts topology into a deterministic summability statement.

### B20 — find why the counterexample algorithm fails

The P0342 counterexample algorithm is: choose a perturbation invisible on every infinite fringe tree, let it decay slowly enough along finite approximants, and exploit the fact that all leaf rerootings see the same global event. The proposed failure mechanism under Holder regularity is that Kraft summability beats coherent accumulation:

for `0 < beta <= 1`,

`sum_i 2^{-beta d_i} <= n^(1-beta)`;

for `beta >= 1`, the sum is at most `1`.

Hence

`n^(-1/2) sum_i |g(T_i)| <= C_beta n^(1/2-beta)` for `1/2 < beta <= 1`, and `O(n^-1/2)` for `beta >= 1`.

So any boundary-vanishing Holder perturbation with exponent strictly greater than `1/2` is uniformly invisible at the CLT scale, for **every** finite full binary tree, not only DTCS(n).

### B4 — prove a weaker statement completely, including sharpness

Do not claim this proves the source transfer theorem for all Holder functionals: it only eliminates the exact boundary-invisible perturbation mechanism. Prove that narrower theorem fully, and prove the exponent is sharp.

Define `rho(T)=2^{-h(T)}` for a finite leaf-rooted tree, where `h(T)` is the distance to its unique degree-two original root, and `rho=0` on an infinite one-ended tree. Local-ball comparison should make `rho` Lipschitz (up to the harmless convention constant in `d_loc`). Then for `0<beta<=1`, `g_beta=rho^beta` is beta-Holder and vanishes on the infinite boundary.

On the perfect balanced tree with `n=2^h` leaves, every leaf has depth `h`, so

`n^(-1/2) sum_i g_beta(T_i) = n^(1/2-beta)`.

Therefore `beta=1/2` gives a nonzero constant and `beta<1/2` diverges. The deterministic threshold `beta>1/2` is sharp.

Finally diagnose the historical root-split perturbation `Phi_alpha`: on the n-leaf comb, choose the deepest leaf. Its distance to the original root is `n-1`, the root split has smaller side 1 so `B_n=1`, and `|Phi_alpha| ~ (1/2)n^{-alpha}` while the local distance to the infinite comb is exponentially small in `n`. Therefore `Phi_alpha` is not Holder of any positive exponent. Its worst boundary modulus is only logarithmic/polynomial in the visible radius, of order `h^{-alpha}` along combs. This should explain precisely how it evades the Holder stability theorem.

## Scope guard

If the proof closes, the result is a **scope-strengthening / repair theorem for the P0342 mechanism**, not new source-metric movement and not a universal positive answer to a modified Open Problem 12. Closure of P0342 still requires the mandated independent P26 audit, one distinct OTHER-track end-to-end audit, and final prior-art gate.
