# T384 scalar all-label limit — statement and composition audit

**Status.** This is a short formal statement obtained by composing the separate joint-initialization proof in `research/T384_joint_limit.md` with the pathwise stochastic approximation in `research/T384_scalar_dynamics.md`. The present note checks the continuous-mapping step, sign selection, independence, path topology, and the frozen-kernel comparison. It does not independently redo the full triangular-array proof of the joint initialization law. The model is the shallow, one-input, bias-free, full-batch continuous-flow subcase of Favaro–Fortini–Peluchetti, [arXiv:2206.08065](https://arxiv.org/pdf/2206.08065); it does not solve the full multi-input or deep T384 row.

## Precise theorem, given the joint initialization law

Fix `0<α<2`, put `β=α/2`, and initialize each `U_i,W_i` independently as symmetric standard `α`-stable variables with characteristic function `exp(−|t|^α)`. Fix **any** deterministic `y∈R`, one input `x=1`, and `T<∞`. Let

`c_m=(m log m)^(−1/α)`, `η_m=(log m)^(2/α)`,

`f_m(t)=c_m Σ_i W_i(t)(U_i(t))_+`, `r_m(t)=y−f_m(t)`,

`K_m^(1)(t)=m^(−2/α)Σ_i W_i(t)²1_{U_i(t)>0}`, `K_m^(2)(t)=m^(−2/α)Σ_i(U_i(t))_+²`, `K_m=K_m^(1)+K_m^(2)`.

Use the absorbing-at-zero ReLU flow selection. Since the stable `U_i(0)` have continuous densities, no coordinate starts at zero almost surely at finite `m`; every later zero has transformed opposing weight `V_i=sgn(r_m(0))W_i<0` at the hit and is necessarily absorbing even for an a.e. ODE solution. Thus this selection does not alter an almost-sure trajectory.

At initialization define `F_m=f_m(0)` and

`A_m=m^(−2/α)Σ_iW_i(0)²1_{U_i(0)>0,W_i(0)>0}`,

`B_m=m^(−2/α)Σ_iW_i(0)²1_{U_i(0)>0,W_i(0)<0}`,

`C_m=m^(−2/α)Σ_i(U_i(0))_+²`.

The separate joint-law result asserts `(F_m,A_m,B_m,C_m)⇒(F,A,B,C)` with **independent** coordinates and, writing `c_α=Γ(α)sin(πα/2)/π` and `h_β=Γ(1−β)`, transforms

`E e^(itF)=exp(−c_α|t|^α)`,

`E e^(−sA)=E e^(−sB)=exp[−(c_α/2)h_β s^β]`,

`E e^(−sC)=exp[−c_α h_β s^β]`.

For the limit let `S=A,D=B` when `F<y`, and `S=B,D=A` when `F>y`; the event `F=y` has probability zero. Put `Q=C+S` and `H=Q+D=A+B+C`. Then **`F,Q,D` are mutually independent**. In particular `Q,D>0` almost surely and

`E e^(−sQ)=exp[−(3c_α/2)h_β s^β]`, `E e^(−sD)=exp[−(c_α/2)h_β s^β]`.

For every fixed `0<δ<T`, jointly in `C([0,T]) × R × D([δ,T]) × D([δ,T])`, with the uniform/J1 topologies as appropriate,

`(f_m(·), K_m(0), K_m^(1)|_[δ,T], K_m|_[δ,T])`

`⇒ (y−(y−F)e^(−Q·), H, [t↦S], [t↦Q])`.                     (1)

Also `sup_{0≤t≤T}|K_m^(2)(t)−C_m|→_P0`; the kernel assertions in (1) are positive-time statements. The width-dependent comparator form is even stronger:

`sup_{0≤t≤T}|r_m(t)−(y−F_m)e^(−Q_m t)|→_P0`,

`sup_{δ≤t≤T}|K_m(t)−Q_m|→_P0`,

where `Q_m=C_m+A_m` if `y−F_m>0`, and `Q_m=C_m+B_m` if `y−F_m<0`. The initial full kernel is **exactly** `K_m(0)=A_m+B_m+C_m`; the vanished opposing mass at positive time is `D` in the limit. First-layer kernel sample paths may jump at gate death. The uniform distance to a constant comparator on `[δ,T]` does **not** assert `C([δ,T])` paths; càdlàg `D([δ,T])` is an admissible embedding. No usual `D([0,T])` limit can retain both `K(0)=H` and `K(t)=Q` for all `t>0` when `D>0`, since that proposed path is not right-continuous at zero. Equivalently, store the initial kernel separately and use local positive-time convergence (or an `L¹(0,T)` limit, which ignores the single time-zero value).

## Why the independence survives residual-sign selection

Let `σ(F)=+` on `F<y` and `−` on `F>y`. Conditional on either value of `F`, `(S,D)` has the same product law `(A,B)` or `(B,A)` because `A,B` are iid and independent of `F,C`. For bounded measurable `g,h,j`,

`E[g(F)h(Q)j(D)] = E[g(F)] E[h(C+A)] E[j(B)]`.

This factorization proves mutual independence of `F,Q,D`, not merely identical marginal laws of the selected kernel for the two signs. It also shows that the all-label theorem's selected effective kernel `Q` has the same law for every deterministic `y`, though the output depends on `y−F`.

The scalar-dynamics note supplies its comparison using only tightness, the common hyperbolic clock, and two-scale deletion of initially opposing extremes; it **does not assume** this joint law. To obtain (1), apply continuous mapping to `(F_m,A_m,B_m,C_m)` at `F≠y`, then Slutsky to the uniform-in-time comparison. The atomless stable `F` makes the sign discontinuity null. The paper's marginal stable-output Theorem 1 is enough for the scalar note's positive-time comparison; the explicit transforms and independence here require the separate joint proof.

## Frozen-initial-kernel comparison and infinite time

Define the same-width frozen surrogate `f_m^fr(t)=y−(y−F_m)e^(−K_m(0)t)`. Jointly with (1), its path in `C([0,T])` converges to

`f^fr(t)=y−(y−F)e^(−(Q+D)t)`.

For every fixed `t>0`, the limiting absolute finite-time discrepancy is

`|f(t)−f^fr(t)|=|y−F|e^(−Qt)(1−e^(−Dt))>0` almost surely.           (2)

Thus the frozen **initial** kernel fails to describe the finite-time training trajectory, for every deterministic label, and the full kernel as well as its first-layer part lose a strictly positive random amount at each fixed positive time. In particular, by Portmanteau (choose continuity levels if needed), for every sufficiently small fixed `ε>0` the finite-width probability of a discrepancy above `ε` has a strictly positive liminf; as `ε↓0`, these lower probabilities tend to one. This strengthens, but does not invalidate or replace the independently proved fixed-label positive-probability counterexample in `research/T384_independent.md`.

Both limiting paths nevertheless satisfy `f(t)→y` and `f^fr(t)→y` as `t→∞`, because `Q>0` and `Q+D>0` almost surely. Equation (2) concerns finite-time dynamics, **not** a different infinite-time prediction at the sole training input; it gives no claim for additional test inputs or a deep/multiple-input network. The order of limits here is width first at each fixed finite horizon, then time to infinity for the *limiting* paths. Do not silently exchange those limits to assert a finite-width uniform-in-time theorem.
