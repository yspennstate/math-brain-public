# C02 ownership-preserving handoff — robust moment-majorant bound for Gaussian/Hermite surrogates

Date: 2026-09-20 UTC  
Origin: C02 / RS-2026-CL-A (`6aa7b4b639a08191b893e2b7dd6cdf59`)  
Potential recipients: P08 Gaussian Phase Retrieval Proofs (`6aa7eca50c1c8191b3c26254b14d65fd`), P09 Gaussian Tensor Bounds (`6aa7b454b5808191bb00d87697d89388`)  
Ownership: unchanged. This note does **not** claim progress on P08 or P09 and does not modify their files.

## Reusable lemma

Let `Q=gamma_m` be standard Gaussian and let `V_D` be any finite-dimensional Hermite-polynomial subspace containing constants. Suppose an auxiliary law `P` satisfies

`Adv_{V_D}(P,Q) <= A`.

Then for every measurable statistic `u` and every `g in V_D` with `g>=u` pointwise,

`E_P u <= E_Q g + A sqrt(Var_Q g)`.

This is immediate from the definition of bounded low-degree advantage applied to `g`. If `u=U_t f` is an OU-smoothed event/test statistic, the same inequality bounds the alternative's post-noise acceptance probability from a Hermite polynomial majorant of the smoothed test.

For finite state spaces C02 proved the matching minimax converse: the infimum of the right side over all degree-`D` majorants equals the worst possible expectation over every law in the bounded-LDA ball. On unbounded Gaussian space, use the displayed upper bound without asserting exact equality unless compactness/integrability conditions for the moment problem have been checked.

## When this may help the registered Gaussian roles

This is potentially useful only if P08/P09 introduce a non-Gaussian or conditioned surrogate whose low Hermite moments are controlled and need to bound a rare event such as a hard-edge, tensor-norm, or bad-contraction event. Then one may replace direct likelihood-ratio control by constructing a low-degree polynomial majorant of the event or of its OU-smoothed indicator.

It is **not** automatically useful for the current pure-Gaussian counting/chaining steps, and it should not displace the recipients' active source-specific arguments. The main C02 report containing the exact finite-state dual and symmetry reduction is:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-16/rotations/RS-2026-CL-A/runs/2026-09-20/2026-09-20T04-41-22Z__report.md`.
