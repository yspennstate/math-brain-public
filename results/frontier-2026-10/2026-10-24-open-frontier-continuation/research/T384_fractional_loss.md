# T384 scalar limit: annealed fractional training loss

**Scope.** Fix `0<α<2`, one input `x=1`, any deterministic `y∈R`, and iid independent *standard* symmetric `α`-stable hidden/output initial weights. Train both layers by the continuous squared-error gradient flow, scaled as in [Favaro–Fortini–Peluchetti, TMLR 2024](https://iris.unibocconi.it/retrieve/1d4101f5-ffcd-480d-8966-6c0f01de8f2b/2651_Large_width_asymptotics_a.pdf), equations (6), (8), (10)–(13), with `ReLU'(0)=0`. Write `f_m(t)` for the one-point prediction and `r_m(t)=y−f_m(t)`. The full scalar process limit and joint-law proof are in local [T384_SCALAR_LIMIT.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_SCALAR_LIMIT.md), [T384_joint_limit.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_joint_limit.md), and [T384_scalar_dynamics.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_scalar_dynamics.md).

## Corollary

Put `β=α/2`, `c_α=Γ(α)sin(πα/2)/π`, and `κ_α=(3c_α/2)Γ(1−β)`. Let `F` be symmetric stable with `E exp(izF)=exp(−c_α|z|^α)`. Then, for **every** `0<p<α` and fixed `t≥0`,

`lim_{m→∞} E|y−f_m(t)|^p = E|y−F|^p exp[−κ_α (pt)^β]`.  (1)

The right-hand prefactor is finite and positive. The limiting rate `Q` satisfies `E exp(−sQ)=exp(−κ_α s^β)` and is independent of `F`. Conditional on `(F,Q)`, the limiting residual is `(y−F)e^(−Qt)`, exponentially decaying at the realized rate `Q`; taking expectation produces a stretched exponential in `t` with exponent `β∈(0,1)`. Equation (1) concerns the initialization-averaged **fractional absolute error**, not the squared objective used to define the training flow.

The convergence in (1) is also uniform in `t` on each fixed compact interval `[0,T]`. No claim is made about interchanging `m→∞` with `t→∞`.

## Uniform integrability: all details

Let `X=W(U)_+`, where `W,U` are independent standard symmetric `α`-stable variables, and `a_m=(m log m)^(1/α)` for `m≥2`. Then `F_m=f_m(0)=a_m^(−1)Σ_{i=1}^m X_i`. The standard stable one-sided tail bound and independence give, for `z≥e`,

`P(|X|>z)≤C z^(−α)(1+log z)`, and `E[X²1_{|X|≤z}]≤C z^(2−α)(1+log z)`.

The second estimate follows by integrating the first; adjust `C` for smaller `z`. This truncation is centered since `W` is symmetric, even conditional on `U`. For `M≥1` put `b=Ma_m`. Separating the event of any `|X_i|>b`, then applying Chebyshev to the independent centered truncated summands, gives

`P(|F_m|>2M)≤mP(|X|>b)+(m/b²)E[X²1_{|X|≤b}]`

`≤ C m b^(−α)(1+log b)≤C' M^(−α)(1+log M)`  (2)

**uniformly over `m≥2`**. The last step uses `m a_m^(−α)=1/log m` and `sup_{m≥2}(1+log a_m)/log m<∞`. This is the estimate already established in local [T384_probability.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_probability.md), equations (1)–(3). Tail integration of (2) yields

`sup_{m≥2} E|F_m|^q<∞` for every `0<q<α`,  (3)

because `∫_1^∞ z^(q−1−α)(1+log z)dz<∞`.

The exact scalar output ODE is `r_m'(t)=−H_m(t)r_m(t)` almost everywhere and the rate-scaled tangent kernel satisfies `H_m(t)≥0`. It follows **pathwise for all `t≥0`** that

`|r_m(t)|=|y−F_m| exp[−∫_0^t H_m(v)dv]≤|y−F_m|`.  (4)

Choose `q` with `p<q<α`. Equations (3)–(4), together with `|y−F_m|^q≤C_q(|y|^q+|F_m|^q)`, imply `sup_{m≥2,t≥0}E|r_m(t)|^q<∞`. Therefore `{|r_m(t)|^p:m≥2,t≥0}` is uniformly integrable. This step is necessary: convergence in distribution alone cannot establish (1).

By the scalar process theorem, for every finite `T`, `r_m(·)⇒[(y−F)e^(−Qt)]` in `C([0,T])`, with `F` independent of the positive `β`-stable `Q`. For a fixed `t`, uniform integrability of `|r_m(t)|^p` upgrades convergence in distribution to convergence of expectations, and independence evaluates that expectation:

`E[|(y−F)e^(−Qt)|^p]=E|y−F|^p E e^(−ptQ)=E|y−F|^p e^(−κ_α(pt)^β)`.

For uniformity in `t∈[0,T]`, take any sequence `m_j→∞` and `t_j∈[0,T]`. A subsequence of `t_j` tends to `t`; process convergence and continuity of evaluation at `(path,t)` imply `r_{m_j}(t_j)⇒(y−F)e^(−Qt)`. The same uniform-integrability estimate gives convergence of the corresponding expectations. The right-hand side of (1) is continuous in `t`; compactness then rules out a nonvanishing supremum discrepancy on `[0,T]`.

## Squared-error boundary

Since `α<2`, the nondegenerate `α`-stable variable `F` has `E|y−F|²=∞` for every finite `y`. Independence and `E e^(−2tQ)=e^(−κ_α(2t)^β)>0` show that

`E|(y−F)e^(−Qt)|²=∞` for every finite `t≥0`.

Indeed, weak convergence of `r_m(t)` to this limiting residual and truncation of the nonnegative square imply `liminf_{m→∞}E|r_m(t)|²=∞` in the extended sense. This does **not** state that any given finite-width expected squared loss is finite. It explains why the annealed law (1) is restricted to `p<α`, even though each sample path was trained using squared error and has a nonincreasing realized squared residual.
