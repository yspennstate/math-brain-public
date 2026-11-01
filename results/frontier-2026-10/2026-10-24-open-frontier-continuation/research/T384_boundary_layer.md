# T384: the scalar stable-NTK switching boundary layer

**Status:** The joint-initialization lemma is now proved in `T384_marked_PPP.md` (with product-tail details in `T384_joint_limit.md`). Combining that lemma with the pathwise argument below gives the stated `J_1` boundary-layer limit. The earlier `T384_scalar_dynamics.md` independently proves the post-layer residual reduction without a joint limit. This is an internal mathematical proof, not an external review or a result for multiple inputs.

Fix `0<α<2`, one input `x=1`, and a fixed label `y`. The Favaro–Fortini–Peluchetti model [arXiv:2206.08065](https://arxiv.org/pdf/2206.08065) has iid symmetric standard `α`-stable `(W_i,U_i)`, output scale `a_m=(m log m)^(−1/α)`, continuous learning rate `η_m=(log m)^(2/α)`, and rescaled kernel

`H_m^(1)(t)=m^(−2/α)Σ_i W_i(t)²1_{U_i(t)>0}`, `H_m^(2)(t)=m^(−2/α)Σ_i (U_i(t))_+²`.

Let `L_m=(log m)^(1/α)` and inspect training at `t=s/L_m`, `0≤s≤S`. Define initial `F_m=a_mΣ_iW_i(U_i)_+`, `C_m=m^(−2/α)Σ_i(U_i)_+²`, and the marked endpoint point process

`N_m=Σ_i δ_(W_i/m^(1/α), U_i)` on `(R\{0})×R` (vague convergence away from `z=0`).

## Joint-initialization lemma

Write `c_α=lim_{x→∞} x^α P(W>x)=lim x^α P(W<−x)>0`. The needed statement is

`(F_m,C_m,N_m) ⇒ (F,C,N)` jointly, where `N` is a marked Poisson point process with intensity

`ν(dz,du)=α c_α |z|^(−1−α) dz P_U(du)` on both signs of `z`, and `(F,C)` is independent of `N` (indeed `F,C` should also be independent). For standard characteristic function `E e^{itW}=e^{−|t|^α}`, the candidate marginals are

`E e^{itF}=e^{−c_α|t|^α}`, `E e^{−λC}=e^{−c_α Γ(1−α/2)λ^(α/2)}`.

This lemma is proved in `T384_marked_PPP.md`: the product-stable `F_m`, positive-square-stable `C_m`, and endpoint process have distinct large-jump axes. A mixed one-sample Laplace/characteristic transform factors after cutting off jumps; overlaps between endpoint `W` jumps, product `WU_+` jumps, and `U_+²` jumps vanish. The centered discarded product jumps have variance `O(ε^(2−α))`, and the discarded positive-square jumps have mean `O(δ^(1−α/2))`. Removing cutoffs proves mutual independence in the limit, with the precise transforms above. This joint argument is needed: marginal limit theorems alone would not identify the initial residual inside the gate indicator.

Define `r_0=y−F`. This is nonzero almost surely since `F` has a continuous stable law. The boundary process is

`\mathcal K(s)=C+Σ_{(z,u)∈N} z² 1{u>0, u+r_0 z s>0}`, `s≥0`.

The sum exists almost surely: the number of points with `|z|>1` is finite, and `∫_{|z|≤1} z²ν(dz,du)<∞` precisely because `α<2`. Conditional on `r_0≠0`, each term with `u>0` is a right-continuous gate with either a strictly positive death time or no death; the sum of its dominating weights `Σz²1_{u>0}` is finite almost surely. Dominated convergence therefore proves right continuity at `s=0` and at every later time, even if death times accumulate at zero or are dense; monotonicity supplies left limits. Equivalently, the paths truncated to `|z|>ε` converge uniformly as `ε↓0`, since their uniform error is at most `Σ_{|z|≤ε}z²→0` almost surely. Thus `\mathcal K` is a càdlàg nonincreasing pure-jump process (possibly with infinitely many small jumps). The initial value is `C+A+B` with `A=Σ_{z>0,u>0}z²`, `B=Σ_{z<0,u>0}z²`; for `r_0>0`, its limit as `s→∞` is `C+A`, while for `r_0<0` the limit is `C+B`. These are the sign-selected rates in `T384_scalar_dynamics.md`.

## Pathwise scaled clock and residual

Set `β_m=η_ma_m=m^(−1/α)L_m`, `r_m(t)=y−f_m(t)`, and `σ_m=sgn r_m(0)`. The scalar ODE gives `r_m'=-K_m r_m`, so the sign is preserved. Let `q_m(t)=β_m∫_0^t|r_m(v)|dv`. Define the order-one scaled clock

`θ_m(s)=m^(1/α)q_m(s/L_m)=∫_0^s |r_m(v/L_m)|dv`.

Let `S_m=m^(−2/α)Σ(W_i²+U_i²)`, which is tight. On `|r_m(0)|≤R,S_m≤K`, `q_m(s/L_m)≤m^(−1/α)RS`; before a neuron deactivates its `(U_i,σ_mW_i)` vector undergoes the hyperbolic map, and deactivation removes a kernel summand. Hence `K_m(t)≤e^{2q_m(t)}S_m≤2K` on this shrinking time interval for all large `m`. It follows that

`sup_{s≤S}|r_m(s/L_m)−r_m(0)|≤2K|r_m(0)|S/L_m=o_P(1)`.

Consequently

`sup_{s≤S}|θ_m(s)−|r_m(0)|s|→_P0` and `sup_{s≤S}|q_m(s/L_m)|=O_P(m^(−1/α))`.

The coordinate-drift estimate in `T384_scalar_dynamics.md`, with `g(q)=2qe^q+q²e^(2q)`, implies uniformly over this time interval

`H_m^(2)(s/L_m)=C_m+o_P(1)` and

`H_m^(1)(s/L_m)=Σ_i (W_i/m^(1/α))² 1_{U_i(0)>0,U_i(s/L_m)>0}+o_P(1)`.

The errors here are bounded by `g(q_m(S/L_m))S_m=o_P(1)`; the gates, not the squares of weights, carry the nontrivial limit.

## Extreme atoms, small atoms, and process convergence

Fix `ε>0` and retain only neurons with `|W_i(0)|/m^(1/α)>ε`. Their number is tight and converges to the finitely many corresponding atoms of `N`; their `U_i(0)` marks are finite. While active, with `z_i=W_i(0)/m^(1/α)` and `u_i=U_i(0)`, the exact hyperbolic formula gives

`U_i(s/L_m)>0 ⇔ u_i>0 and u_i+σ_m W_i(0)tanh(q_m(s/L_m))>0`.

Uniformly for `s≤S`, `m^(1/α)tanh(q_m(s/L_m))=θ_m(s)+o_P(1)`; the latter is uniformly within `o_P(1)` of `|r_m(0)|s`. To formalize the jump-time statement, first retain a compact marked annulus `ε<|z|<R`, `|u|<M`, with continuity cutoffs. Under a joint-limit coupling, its finitely many atoms `(z_{m,i},u_{m,i})` match limit atoms `(z_i,u_i)`, and `r_m(0)→r_0≠0`; their residual signs eventually agree. For `r_m(0)≠0`, the exact residual equation keeps `|r_m(t)|>0` on finite intervals, so `θ_m` and `m^(1/α)tanh q_m(s/L_m)` are continuous and strictly increasing in `s`. The latter clocks converge uniformly to the positive-slope line `|r_0|s`. An initially active opposing atom hits its zero gate precisely when this clock reaches `u_{m,i}/|z_{m,i}|`; if its limiting time `u_i/(|r_0z_i|)` lies in `(0,S)`, the unique hitting time converges to that value. An opposed hit outside `[0,S]` stays outside for large `m`, and supporting-sign atoms never die. Conditional on `F`, the atomless stable marks ensure almost surely no `u_i=0`, no death at either endpoint `0,S` or any prescribed observation time, and no ties among the finitely many opposed death times. Thus the matched jump sizes and ordered hit times converge jointly. A piecewise linear increasing homeomorphism aligning those finitely many hits gives `J_1` convergence of the truncated paths; shifted jump indicators need not converge uniformly. Removing the mark and annulus cutoffs by their small-probability bounds gives the finite-`ε` paths in `D([0,S])` (and finite-dimensional convergence at all deterministic times).

The omitted small-weight part is uniformly bounded, up to the `o_P(1)` drift above, by

`Z_{m,ε}=m^(−2/α)Σ_i W_i(0)²1_{|W_i(0)|≤εm^(1/α)}`.

Stable-tail truncation gives `limsup_m E Z_{m,ε}≤C_α ε^(2−α)`. The matching Poisson sum has expectation

`E Σ_{|z|≤ε}z² =2αc_α ε^(2−α)/(2−α)`.

Both vanish as `ε↓0`. The finitely many large atoms `|z|>R` can also be removed with probability cost at most `2c_αR^(−α)` before `R↑∞`. For fixed `ε`, marks on `|z|>ε` are tight because the endpoint count is tight and their law is `P_U`; truncate marks at `M↑∞` in the finite-atom alignment step. The uniform small-atom bound permits the converging-together theorem in `J_1` (the `J_1` distance is bounded above by uniform error). Consequently,

`(F_m,C_m, (K_m(s/L_m))_{0≤s≤S}) ⇒ (F,C,(\mathcal K(s))_{0≤s≤S})`

in `R²×D([0,S])` with `J_1` topology. In particular the result holds for finite-dimensional distributions at any deterministic times `s≥0`; `s=0` is included. No fixed positive-width time is interchanged with the `s→∞` boundary limit: `T384_scalar_dynamics.md` separately proves the positive-time endpoint.

## Identified scalar training limit

The same joint initialization lemma and small-atom truncation at `s=0` yield

`(F_m,A_m,B_m,C_m) ⇒ (F,A,B,C)` jointly,

where `A_m` and `B_m` are the positive- and negative-`W_i(0)` parts of `H_m^(1)(0)` defined in `T384_scalar_dynamics.md`, and `A,B` are the corresponding Poisson sums above. The PPP restrictions to positive and negative `z` are independent. Each restriction also retains a mark with `u>0` with probability `1/2`; hence, with `β=α/2`,

`E exp(−λA)=E exp(−λB)=exp{−(c_α/2) Γ(1−β) λ^β}`.

The random variables `A,B,C,F` are mutually independent. Define `Q=C+A` when `y−F>0`, and `Q=C+B` when `y−F<0` (the equality event has probability zero). Because `A,B` are iid and independent of `F,C`, **`Q` and `F` are independent**, even though the choice between `A` and `B` is determined by `F`. Its explicit Laplace transform is

`E exp(−λQ)=exp{−(3c_α/2) Γ(1−β) λ^β}`.

The initial total kernel `A+B+C`, for comparison, has transform `exp{−2c_α Γ(1−β) λ^β}`. The continuous mapping theorem gives `(r_{0m},Q_m)⇒(y−F,Q)`. Combining this with the uniform-in-time approximation proved in `T384_scalar_dynamics.md` yields, for every finite `T`, the **full scalar residual functional limit** in `C([0,T])`:

`(r_m(t))_{0≤t≤T} ⇒ ((y−F)e^{−Qt})_{0≤t≤T}`.

Thus the surviving random rate is positive `α/2`-stable with the displayed exponent and is independent of the initial output fluctuation. This describes the scalar continuous-gradient-flow model; it does not establish the corresponding multi-input training limit.

## Boundary and proof obligations

1. The argument is complete under standard symmetric `α`-stable characteristic function `e^{−|t|^α}`; with a different scale convention replace `c_α` by that law's one-sided tail constant and adjust the initialization transforms. The scaling and pathwise result are unaffected.
2. This is an internally proved scalar theorem and has not been externally reviewed for novelty. It uses one input and continuous gradient flow. Multiple inputs have coupled residual components and activation hyperplanes, so this scalar clock proof cannot be asserted there.
