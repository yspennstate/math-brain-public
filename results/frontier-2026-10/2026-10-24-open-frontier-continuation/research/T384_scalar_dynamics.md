# T384: scalar training dynamics reduce to a sign-selected random kernel

**Claim (proved below, without a joint initialization limit).** Fix `0<α<2`, one input `x=1`, a deterministic label `y∈R`, and `T<∞`. Under the symmetric iid nondegenerate `α`-stable initialization and continuous squared-loss gradient flow of Favaro–Fortini–Peluchetti [arXiv:2206.08065](https://arxiv.org/pdf/2206.08065), put

`F_m=f_m(0)`, `r_{0m}=y−F_m`,

`A_m=m^(−2/α) Σ_i W_i(0)² 1_{U_i(0)>0,W_i(0)>0}`,

`B_m=m^(−2/α) Σ_i W_i(0)² 1_{U_i(0)>0,W_i(0)<0}`,

`C_m=m^(−2/α) Σ_i (U_i(0))_+²`, and

`Q_m=C_m+A_m` if `r_{0m}>0`, `Q_m=C_m+B_m` if `r_{0m}<0` (arbitrary at exact zero).

Then

`sup_{0≤t≤T} |r_m(t)−r_{0m} exp(−Q_m t)| → 0` **in probability**.

For each fixed `0<δ<T`, moreover,

`sup_{δ≤t≤T} |K_m(t)−Q_m| → 0` **in probability**, where `K_m(t)=H_m^(1)(t)+H_m^(2)(t)` is the rescaled instantaneous tangent kernel. The kernel assertion uses only the paper's marginal stable output limit to exclude an atom at `r_{0m}=0`; the residual assertion does not even need that exclusion. Neither assertion presumes joint convergence of `(F_m,A_m,B_m,C_m)`. If such a joint limit is separately proved, it can be inserted in the displayed formula to identify the scalar output process.

The conclusion is **not** fixed-initial-kernel dynamics: `K_m(0)=A_m+B_m+C_m`, while `Q_m` keeps only the first-layer weights supporting the initial residual sign. The opposing first-layer extreme neurons disappear in a vanishing initial time layer. The previous independent note `T384_independent.md` gives a direct positive-probability nonfreezing consequence.

## Exact ODE and common clock

Write `a_m=(m log m)^(−1/α)`, `η_m=(log m)^(2/α)`, `β_m=η_m a_m=m^(−1/α)(log m)^(1/α)`. With `f_m(t)=a_m Σ_i W_i(t)(U_i(t))_+`, `r_m(t)=y−f_m(t)`, the paper's equations (4)–(9) give, away from ReLU kinks,

`U_i'=β_m W_i 1_{U_i>0} r_m`, `W_i'=β_m (U_i)_+ r_m`,

`r_m'=−K_m r_m`, `K_m=m^(−2/α) Σ_i [W_i² 1_{U_i>0}+(U_i)_+²]≥0`.

At the kink use the **absorbing solution selection**: a coordinate at `U_i=0` is frozen. The initialized stable coordinates have continuous densities, so `P(∃i:U_i(0)=0)=0` at every finite `m`. This qualification matters only for exceptional deterministic starts: the pointwise value `ReLU'(0)=0` alone does not give uniqueness among all almost-everywhere Carathéodory solutions starting with `U=0` and an outward-pointing weight.

Thus the residual keeps its initial sign `σ=sgn(r_{0m})`. If `r_{0m}=0`, all weights and the residual are stationary and the residual claim is exact. Otherwise define

`s_m(t)=β_m ∫_0^t |r_m(q)|dq` and `V_i=σ W_i`.

For each active neuron `dU_i/ds=V_i`, `dV_i/ds=U_i`, so until it reaches zero,

`U_i(s)=U_i(0)cosh s+V_i(0)sinh s`, `V_i(s)=V_i(0)cosh s+U_i(0)sinh s`.

Initially inactive neurons stay inactive. An initially active neuron with `V_i(0)>0` stays active; one with `V_i(0)<0` may hit zero and then stays inactive under the paper's derivative `1_{U_i>0}`. If `|V_i(0)|>U_i(0)`, its hit clock is `artanh(U_i(0)/|V_i(0)|)`; if `|V_i(0)|≤U_i(0)`, it never hits. The latter possibility is explicitly handled below.

Indeed every *attained* zero has `V_i(s_*)=−sqrt(V_i(0)²−U_i(0)²)<0` (a zero can occur only when `V_i(0)<−U_i(0)`). As the residual sign remains fixed, positive-side departure from that zero would require `dU_i/ds=V_i<0`, and negative-side departure is impossible because the inactive derivative is zero. Thus absorption at any reached zero is forced even for absolutely continuous solutions of the a.e. ODE. The explicitly selected convention only resolves null-probability initially-zero configurations.

## Tightness and pathwise small motion

Let `S_m=m^(−2/α)Σ_i[W_i(0)²+U_i(0)²]`. Since the square of an `α`-stable variable has tail exponent `α/2<1`, the normalized sum `S_m` is tight (the usual stable-sum limit suffices). The paper's Theorem 1 gives tight `F_m`; Theorem 2 also gives tight `K_m(0)`. We use only `S_m` and `F_m` tightness. In particular `A_m+B_m+C_m≤S_m` and `Q_m≤S_m`.

For any `t≤T`, `|r_m(t)|≤|r_{0m}|`, hence `s_m(t)≤β_m |r_{0m}|T=o_P(1)`. Before deactivation, the Euclidean norm of `(U_i,V_i)` grows by at most `e^s`; afterward that neuron's two coordinates freeze. For the initially active neurons, uniformly `t≤T`,

`|U_i(t)−U_i(0)|∨|W_i(t)−W_i(0)|≤s_m(T)e^{s_m(T)}√(U_i(0)²+W_i(0)²)`.

Consequently, with `g(s)=2se^s+s²e^(2s)`, the normalized sums of squared-coordinate changes are bounded by `g(s_m(T))S_m=o_P(1)`:

`sup_{t≤T} m^(−2/α)Σ_i |W_i(t)²−W_i(0)²|≤g(s_m(T))S_m`,

`sup_{t≤T} |H_m^(2)(t)−C_m|≤g(s_m(T))S_m`.

For the second bound use that `z↦z_+` is 1-Lipschitz, and initially inactive neurons do not move. One also gets the pathwise kernel bound `0≤K_m(t)≤e^{2s_m(t)}S_m` (deactivation removes, rather than adds, a contribution). These estimates recover second-layer freezing in this one-input setting without appealing to Theorem 4.

## Opposing extreme weights vanish by every positive time

Fix `δ∈(0,T)` and constants `c,R,K>0`. Work on `G_m={c≤|r_{0m}|≤R, S_m≤K}`. Since `s_m(t)≤β_m RT`, for large `m`, `K_m(t)≤2K` throughout `[0,T]`. Hence

`|r_m(t)|=|r_{0m}| exp(−∫_0^t K_m(q)dq)≥c exp(−2KT)`

and

`s_m(δ)≥d β_m`, where `d=cδ exp(−2KT)>0`.

Let `D_m(t)=m^(−2/α)Σ_{U_i(0)>0,V_i(0)<0} W_i(0)² 1_{U_i(t)>0}`. This is nonincreasing. Fix `ε>0`. Its part with `|W_i(0)|<εm^(1/α)` is bounded by

`Z_{m,ε}=m^(−2/α)Σ_i W_i(0)²1_{|W_i(0)|<εm^(1/α)}`.

Regular variation (or the standard stable-tail bound) gives `sup_{m large} E Z_{m,ε}≤C_α ε^(2−α)`. Thus `lim_{ε↓0}limsup_m P(Z_{m,ε}>h)=0` for every `h>0`.

If an opposing neuron with `|W_i(0)|≥εm^(1/α)` survives until `δ` on `G_m`, the hyperbolic formula forces

`U_i(0)>|W_i(0)| tanh(s_m(δ))≥(dε/2)(log m)^(1/α)`

for large `m` (because `tanh(dβ_m)≥dβ_m/2`). Independence of its initialized `W_i,U_i` and their `α`-stable tail bounds imply

`P(∃i: |W_i(0)|≥εm^(1/α), U_i(0)>(dε/2)(log m)^(1/α))`

`≤m·O(ε^(−α)m^(−1))·O((dε)^(−α)(log m)^(−1))=O_{d,ε}((log m)^(−1))→0`.

This union bound is unconditional; the conditional event `G_m` is merely used to get the clock lower bound. In particular `D_m(δ)1_{G_m}→0` in probability by first taking `m→∞` and then `ε↓0`. The case `|V_i(0)|≤U_i(0)` presents no exception: such a surviving large-weight neuron necessarily has the very large `U_i(0)` captured by this union bound.

Supporting-sign initially active weights remain active. The coordinate-drift estimate now yields, on `G_m`,

`sup_{δ≤t≤T}|H_m^(1)(t)−(A_m 1_{σ>0}+B_m 1_{σ<0})|≤D_m(δ)+g(s_m(T))S_m→_P0`.

Adding `H_m^(2)` gives the claimed positive-time kernel convergence on `G_m`. Tightness lets `R,K→∞`; the paper's Theorem 1 gives `F_m⇒F_∞`, a nondegenerate scalar symmetric `α`-stable law with no atoms, so `lim_{c↓0}limsup_m P(|r_{0m}|<c)=0` for any fixed `y`. This removes `G_m` and proves the unconditional kernel assertion without a joint limit.

## Uniform residual convergence, including the initial layer

The exact solution is `r_m(t)=r_{0m} exp(−∫_0^t K_m(q)dq)`. For nonnegative `a,b`, `|e^(−a)−e^(−b)|≤|a−b|`, so

`sup_{t≤T}|r_m(t)−r_{0m}e^(−Q_m t)|≤|r_{0m}| sup_{t≤T}|∫_0^t(K_m(q)−Q_m)dq|`.

On `G_m`, for large `m`, `K_m≤2K` and `Q_m≤K`. Split the integral at `δ`: its initial piece is at most `3Kδ`; the rest is at most `T sup_{δ≤t≤T}|K_m(t)−Q_m|`. Thus the displayed residual error is at most

`R[3Kδ+T sup_{δ≤t≤T}|K_m(t)−Q_m|]`.

For fixed `c,R,K,δ`, the random second term vanishes in probability. Then let `δ↓0`, and let `R,K↑∞` by tightness. On the excluded event `|r_{0m}|<c`, both `|r_m(t)|` and `|r_{0m}e^(−Q_mt)|` are at most `c`, so the error is at most `2c` **without any information about the initialization's joint law or whether `r_{0m}` has an atom at zero**. Letting `c↓0` proves the uniform residual claim.

## Scope

All limits here are probability statements under the initialization for each `m`; the approximation uses the same width-dependent random `(F_m,A_m,B_m,C_m)` rather than silently positing their joint limit. The residual and output are continuous paths and the displayed residual approximation is in the `C([0,T])` uniform norm. `K_m` can jump when a gate dies; its positive-time result is a **uniform distance to the constant random comparator** `Q_m` on each `[δ,T]`, not a claim that `K_m` has continuous sample paths. If a joint law is supplied separately, this estimate may be combined with weak convergence in `D([δ,T])` for each `δ>0`; initial `K_m(0)` must be recorded separately because an order-one initial boundary layer prevents a single usual `D([0,T])` limit retaining both its time-zero and positive-time values. The model is scalar, one input, full-batch continuous gradient flow, and `0<α<2`, with no bias term and the ReLU gate convention in the paper. Extending to multiple inputs changes the common-clock reduction because gates interact across examples. The separate `research/T384_joint_limit.md` develops the joint initialization law needed to identify an explicit random scalar limiting flow; its proof is not a premise of this theorem.
