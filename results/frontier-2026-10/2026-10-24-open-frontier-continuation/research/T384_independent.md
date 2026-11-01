# T384 independent audit: first-layer stable NTK does not freeze

**Result.** For every `0<α<2` and every fixed `T>0`, there is a fixed deterministic label `y` for a single input `x=1` such that the paper's actual squared-loss gradient flow satisfies

`liminf_{m→∞} P[ H_m^(1)(0) − H_m^(1)(T) ≥ 1/2 ] > 0`.

This is a nonfreezing counterexample for the **first-layer** part of the rescaled kernel, not a contradiction of Favaro–Fortini–Peluchetti Theorem 4. Theorem 4 controls `H_m^(2)` and lower-bounds the full kernel; the discussion explicitly leaves freezing of `H_m^(1)` open. It does not prove a fixed-kernel regression equivalence. The counterexample uses one linearly independent normalized input, allowed by its `k≥1` hypothesis. See primary paper [arXiv:2206.08065](https://arxiv.org/pdf/2206.08065), equations (4)–(9), Theorems 1, 2, 4 and Section 4; Brain `06_math_research/frontier/rows/T384/DOSSIER.md` blob `ba319f075261925a8747ce1bf31fc4f4b5c29241` and `stable_ntk_move.py` blob `dd40da57d955aa8b7d8d0f3991cfd3d7f0153374` motivated the question. Paper-specific facts below were checked in the paper; the deduction is mine.

## Exact model and ODE

Let `u_i,w_i` be independent iid symmetric nondegenerate `α`-stable variables (`i=1,…,m`), `m≥2`. Put

`a_m=(m log m)^(-1/α)`, `η_m=(log m)^(2/α)`, `β_m=η_m a_m=m^(-1/α)(log m)^(1/α)`.

For `x=1`, let `f_m=a_m Σ_i w_i (u_i)_+`, `r_m=y−f_m`, and `L=r_m²/2`. At all differentiable times, with the paper's `1_{u_i>0}` convention,

`u_i'=β_m w_i 1_{u_i>0} r_m`, `w_i'=β_m (u_i)_+ r_m`,

`r_m'=−K_m r_m`, where `K_m=H_m^(1)+H_m^(2)`,

`H_m^(1)=m^(−2/α) Σ_i w_i² 1_{u_i>0}`, `H_m^(2)=m^(−2/α) Σ_i (u_i)_+²`.

At `u_i=0` take the explicit **absorbing solution selection**: a coordinate at zero freezes. The iid stable initial `u_i` have continuous densities, so no coordinate starts at zero almost surely at each finite width. The pointwise choice `ReLU'(0)=0` alone can leave nonuniqueness for exceptional initially-zero, outward-pointing coordinates among almost-everywhere Carathéodory solutions; those configurations have probability zero here.

The `log m` factors exactly cancel from both kernel summands after multiplying the raw NTK by `η_m`. In particular an extreme `|w_i|≈m^(1/α)` contributes order one to `H_m^(1)`, while its first-layer speed is **order `(log m)^(1/α)`** when residual is order one. The dossier's wording that this speed is merely order one misses the logarithm, though its numerical nonfreezing inference is consistent with the corrected scale.

Since `K_m≥0`, a positive `r_m(0)` remains positive. Introduce a common increasing clock

`s_m(t)=β_m ∫_0^t r_m(q)dq`.

As long as a neuron is active, `du_i/ds=w_i`, `dw_i/ds=u_i`, and hence

`u_i(s)=u_i(0) cosh s + w_i(0) sinh s`, `w_i(s)=w_i(0) cosh s + u_i(0) sinh s`.

When `u_i` reaches zero with a negative weight, it becomes inactive and stays there under the selected convention. More strongly, an attained hit requires `w_i(0)<−u_i(0)` and has `w_i(s_i^*)=−sqrt(w_i(0)²−u_i(0)²)<0`: active-side motion from zero would point back into the inactive half-line, while inactive-side velocity is zero. Hence such a hit cannot reactivate even under an almost-everywhere ODE interpretation. Initially negative neurons never move, and initially zero ones occur with probability zero.

## Positive-probability extreme-weight event

Let `E_m` be the event that at least one index has

`−2m^(1/α) ≤ w_i(0) ≤ −m^(1/α)`, `0<u_i(0)<1`.

The negative tail of a symmetric `α`-stable variable has constant `c_->0`, so `m P(w_i∈[−2m^(1/α),−m^(1/α)])→c_-(1−2^(−α))`. Independence gives

`P(E_m)→p=1−exp{−c_-(1−2^(−α))P(0<u_i<1)}>0`.

Theorem 1 of the paper makes `f_m(0)` tight at fixed `x=1`; Theorem 2 makes `K_m(0)` tight. Pick finite `R,C` large enough that, for all sufficiently large `m`, `P(|f_m(0)|>R)+P(K_m(0)>C)<p/4`. Set the fixed label `y=R+1`. Then

`A_m=E_m ∩ {|f_m(0)|≤R} ∩ {K_m(0)≤C}`

has `liminf P(A_m)≥3p/4` (a weaker `p/2` is enough), and on `A_m`, `1≤r_m(0)≤2R+1=:R_0`. No independence between `E_m`, output, and kernel is assumed in this intersection bound.

## Uniform flow bounds and kernel loss

For an initially active neuron before it deactivates, `d(w_i²+u_i²)/ds=4w_i u_i≤2(w_i²+u_i²)`. Deactivation removes its nonnegative contribution; initially inactive neurons stay inactive. Therefore, pathwise,

`0≤K_m(t)≤e^{2s_m(t)}K_m(0)`.

The residual is positive and decreasing, so for `t≤T`, `s_m(t)≤β_m R_0 T=o(1)`. On `A_m`, for sufficiently large `m`, `K_m(t)≤2C` and hence

`r_m(t)=r_m(0) exp(−∫_0^t K_m(q)dq)≥exp(−2CT)`.

Consequently `s_m(T)≥β_m T exp(−2CT)`. For the selected neuron of `E_m`, its exact hitting-clock threshold is

`s_i^*=artanh(u_i(0)/|w_i(0)|)≤2m^(−1/α)`

for large `m`, since `u_i(0)<1` and `|w_i(0)|≥m^(1/α)`. But `s_m(T)/m^(−1/α)≥T exp(−2CT)(log m)^(1/α)→∞`. Thus it is inactive by time `T`, and an initial `w_i(0)²/m^(2/α)≥1` has disappeared from `H_m^(1)`.

Other active neurons cannot offset this loss. For a neuron active all the way to clock `s≥0`, the exact hyperbolic formula and `2|w_i(0)u_i(0)|≤w_i(0)²+u_i(0)²` give

`w_i(s)²−w_i(0)² ≤ [(e^{2s}−1)/2] [w_i(0)²+u_i(0)²]`.

Neurons that deactivate contribute zero at `T`. Summing the possible increases of surviving neurons yields the deterministic bound on `A_m`

`H_m^(1)(T)−H_m^(1)(0) ≤ −1 + [(e^{2β_m R_0 T}−1)/2] K_m(0) ≤ −1+o(1)`.

The last term is uniform on `A_m`; for sufficiently large `m`, the drop is at least `1/2`, proving the result. The selected neuron in fact dies on an `O((log m)^(−1/α))` time window with an event-dependent constant, even while the second-layer kernel can freeze as in Theorem 4.

## Scope and next step

This direct argument establishes nonfreezing in probability for the first-layer kernel under the published parametrization, with a fixed but sufficiently large `y`. It uses the paper's indicator formula with explicit absorption at a kink. The kernel is allowed to jump at death, so the conclusion compares its values at `0` and `T`; it does not assert convergence of kernel paths in `C([0,T])`. This note by itself does **not** identify complete limiting output dynamics or cover every fixed label. The subsequent `research/T384_scalar_dynamics.md` and `research/T384_joint_limit.md` address those separate all-label scalar questions; multiple inputs and deep-network limits remain outside their scope. The earlier independent counterexample and its credit stand without assuming either subsequent proof.
