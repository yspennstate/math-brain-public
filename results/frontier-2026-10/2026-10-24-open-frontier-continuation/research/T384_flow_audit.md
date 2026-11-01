# T384 deterministic one-input ReLU gate-death audit

**Verdict.** The proposed deterministic implication is correct with the exact scaling and assumptions stated below. The order-one change in `H_1` comes from removing an active neuron's *entire* squared first-layer kernel contribution at its hitting time, not from an order-one relative change of its weight. The derivation requires an absorbing derivative choice at `u=0` and the active-set indicator in `H_1`; a smooth continuation of the hyperbolic formula beyond the first zero is wrong. This is a conditional finite-width construction, **not** a statement that its initialization event has nonvanishing probability under an `α`-stable law.

## Precise model

Fix `α>0`, `m>1`, one scalar input `x=1`, one scalar label `y`, and squared loss `L=(y−f)^2/2`, with

`c_m=(m log m)^(−1/α)`, `η_m=(log m)^(2/α)`, `β_m=η_m c_m=m^(−1/α)(log m)^(1/α)`,

`f=c_m Σ_{i=1}^m w_i (u_i)_+`, `r=y−f`.

Gradient flow means `θdot=−η_m ∇_θ L`; take `ReLU'(0)=0` **and explicitly select the absorbing solution at zero**: a neuron initially at zero or hitting zero remains there thereafter. For `u_i>0` this gives

`udot_i=β_m r w_i`, `wdot_i=β_m r u_i`;                              (1)

for `u_i≤0`, both derivatives are zero on the selected trajectory. The explicit absorbing selection matters for a merely almost-everywhere/Carathéodory notion of solution, as noted below. Set

`H_1(t)=m^(−2/α) Σ_{u_i(t)>0} w_i(t)^2`,

`H_2(t)=m^(−2/α) Σ_i (u_i(t))_+^2`, `H(t)=H_1(t)+H_2(t)`.

Assume `1≤r(0)≤R_0`, `H(0)≤K`, where `R_0,K` are fixed finite constants independent of `m`, and that one specified index `i_*` has

`0<u_{i_*}(0)<1`, `−2m^(1/α)≤w_{i_*}(0)≤−m^(1/α)`.               (2)

Necessarily `K≥1` for these conditions to be compatible. No assumption about the other neurons beyond `H(0)≤K` is needed. The rate `η_m=(log m)^(2/α)` is material: it makes `η_m c_m² m^(2/α)=1` exactly. If `rate logm^2/a` meant a different parenthesization, recompute this factor and the hitting-time assertion before reusing the proof.

## Residual and active-neuron dynamics

Away from the finitely many possible hitting times, differentiation of the output using (1) gives

`fdot=c_m β_m r Σ_{u_i>0}(w_i²+u_i²)=rH`,

because `c_m β_m m^(2/α)=η_m c_m² m^(2/α)=1`. Thus almost everywhere,

`rdot=−rH`, `r(t)=r(0) exp(−∫_0^t H(s)ds)∈(0,R_0]`.              (3)

The output and residual remain continuous when a neuron hits zero (`w_i(u_i)_+=0` on both sides), although `H_1` can jump. Equation (3) follows by absolute continuity across these isolated hitting times, so the positive residual **never reverses sign**. Equivalently `Ldot=−r²H≤0` almost everywhere.

Define integrated residual time `τ(t)=β_m∫_0^t r(s)ds`. It is strictly increasing, with

`0≤τ(t)≤β_m R_0 t`.                                             (4)

For any initially active neuron, *only until its first zero*, (1) has the exact solution

`u_i(τ)=u_i(0) cosh τ+w_i(0) sinh τ`,

`w_i(τ)=w_i(0) cosh τ+u_i(0) sinh τ`.                            (5)

The matrix in (5) has Euclidean operator norm `e^τ`, so its squared norm is at most `e^(2τ)(u_i(0)²+w_i(0)²)`. Any neuron that has hit zero is then excluded from `H`, and initially inactive neurons stay excluded. Therefore for every time,

`H(t)≤e^(2τ(t))H(0)≤K e^(2β_m R_0 t)`.                         (6)

This is the necessary energy estimate; it does **not** assume that `H_1` is continuous or conserved. The invariant `w_i²−u_i²` along (5) is an additional check, but it is not the kernel invariant because gate death removes `w_i²` from `H_1`.

For the specified neuron write `A=|w_{i_*}(0)|≥m^(1/α)` and `u_0=u_{i_*}(0)<1`. For sufficiently large `m`, `A>u_0`, `w_{i_*}(τ)` remains negative until death, and its unique active-phase zero occurs at

`τ_*=artanh(u_0/A)≤artanh(m^(−1/α))<2m^(−1/α)`.                 (7)

At that zero `w_{i_*}(τ_*)=−sqrt(A²−u_0²)<0`, so after the hit it stays frozen at `(u,w)=(0,−sqrt(A²−u_0²))`. The active `H_1` term jumps from `m^(−2/α)(A²−u_0²)` to zero. One cannot continue (5) into `u<0` under the chosen ReLU derivative.

## Hitting before the proposed time

Take `t_m=4/(log m)^(1/α)`. From (4), `τ(t_m)≤4R_0m^(−1/α)`. Equations (3) and (6) yield for `0≤t≤t_m`

`r(t)≥r(0) exp[−K t_m e^(8R_0m^(−1/α))]`.

Since `t_m→0`, this lower bound is at least `1/2` for all sufficiently large `m` (depending only on `α,R_0,K`). Consequently

`τ(t_m)=β_m∫_0^{t_m}r(s)ds≥(β_m t_m)/2=2m^(−1/α)>τ_*`.       (8)

Because `τ(t)` is continuous and strictly increasing, the neuron reaches its zero **strictly before** `t_m`. The use of the coupled residual in (8) is essential: replacing `r(t)` by `r(0)` without the bound (6) would be unjustified.

## Other neurons cannot mask the order-one kernel change

Fix any `T>0`. For large `m`, `t_m<T`, so neuron `i_*` is inactive at `T`. For an *other* initially active neuron before its own death, regard its orbit as a function of `τ` and calculate

`d(w_i²)/dτ=2w_i u_i≤w_i²+u_i²≤e^(2τ)[w_i(0)²+u_i(0)²]`.

If this other neuron dies, its contribution to `H_1` drops to zero, which only improves the desired upper bound. Thus, summing the increase of all other active `w²` terms up to the common `τ(T)` gives

`Σ_{i≠i_*} [1_{u_i(T)>0}w_i(T)²−1_{u_i(0)>0}w_i(0)²]
 ≤ (e^(2τ(T))−1)/2 · Σ_{i≠i_*,u_i(0)>0}(w_i(0)²+u_i(0)²)`.    (9)

Initially inactive neurons remain inactive, including neurons at zero under the absorbing convention. Combining (2), `H(0)≤K`, (4), and (9) proves the explicit finite-`m` bound

`H_1(0)−H_1(T) ≥ m^(−2/α)w_{i_*}(0)²−[K/2](e^(2β_m R_0 T)−1)
                  ≥1−[K/2](e^(2R_0T m^(−1/α)(log m)^(1/α))−1)`

for all sufficiently large `m`. Since `β_m→0`,

`liminf_{m→∞}[H_1(0)−H_1(T)]≥1`.                                (10)

The loss/residual remains well defined and bounded, and no explosion is hidden in this estimate: on each finite interval (4) and the hyperbolic norm estimate bound all active parameters, while frozen parameters remain fixed. Each neuron can hit zero at most once under the positive residual. The `H_1` jump itself may be almost one because `w_{i_*}` has barely changed; (9) rules out compensation by the remaining weights.

## Scope and failure modes

1. This proves only the deterministic implication (2) plus `r(0),H(0)` bounds. It supplies **no probability estimate** for this joint event under iid stable initialization and therefore does not establish non-freezing in probability or a Poisson-driven limiting feature-learning system for T384.
2. The kernel definition must use `1_{u_i>0}` at `x=1`. If `H_1` instead means the ungated sum `m^(−2/α)Σw_i²`, the proposed order-one drop is false: along the special orbit `w_i(0)²−w_i(τ_*)²=u_0²<1`, a vanishing normalized change.
3. The value `ReLU'(0)=0` **by itself does not imply uniqueness among Carathéodory solutions** of the discontinuous ODE. An initially zero neuron with `w_0>0` can be held at zero for an arbitrary delay and then depart into `u>0`, satisfying the ODE almost everywhere; its inactive `w_0²` is unconstrained by `H(0)≤K`, potentially invalidating (6) and (9). The theorem therefore requires the stated absorbing solution selection (or classical right-differentiability at the departure time, which rules out this delayed departure). For the specified neuron hitting zero with `w<0` and `r>0`, departure into `u>0` is inward-pointing the wrong way, so freezing is forced, but other zero neurons still require the global convention. The proof is piecewise classical on active intervals and absolutely continuous across hits with that selection; it does not differentiate through the ReLU kink.
4. The label sign matters. Positive `r(0)` stays positive by (3). For an initially negative residual the designated negative `w_i` drives `u_i` upward, so this particular gate-death argument fails.

Context: [Brain T384 dossier and its numerical lead](https://github.com/<private-repo>/blob/main/06_math_research/frontier/rows/T384/DOSSIER.md); [Favaro–Fortini–Peluchetti, shallow α-stable ReLU NTK](https://arxiv.org/abs/2206.08065). The calculation above is self-contained and does not invoke the paper's probability theorem.
