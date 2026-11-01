# T384: scope and literature audit for a first-layer-kernel nonfreezing result

Checked 2026-10-23. Target source: Favaro, Fortini and Peluchetti, *Large-width asymptotics and training dynamics of α-Stable ReLU neural networks*, published in **TMLR (11/2024)**, [published PDF](https://iris.unibocconi.it/retrieve/1d4101f5-ffcd-480d-8966-6c0f01de8f2b/2651_Large_width_asymptotics_a.pdf). Earlier [arXiv:2206.08065](https://arxiv.org/abs/2206.08065) versions use a different title and equation/theorem numbering; cite the published version when possible.

## Exact model and existing result

For α∈(0,2), the output weights `W_i` and hidden coordinates `U_{ij}` are all iid centered symmetric α-stable random variables of fixed scale σ>0 (published PDF §2, equation (6)). With input `x`, the network prediction is

`F_m(x;W,U)=(m log m)^(-1/α) Σ_{i=1}^m W_i ReLU(U_i·x)`.

The paper uses half the sum of squared errors over `k` training inputs, continuous gradient flow with learning rate `η_m=(log m)^(2/α)`, and the output dynamics `dF_m(X)/dt=−η_m H_m(W(t),X)(F_m(X)−Y)`, equation (8). The paper's scaled neural tangent kernel `\widetilde H_m=η_m H_m` splits as equations (11)–(13):

`\widetilde H_m^(1)[j,j'] = m^(-2/α) Σ_i W_i² (x_j·x_j') 1_{U_i·x_j>0}1_{U_i·x_j'>0}`,

`\widetilde H_m^(2)[j,j'] = m^(-2/α) Σ_i ReLU(U_i·x_j)ReLU(U_i·x_j')`.

Thus `H^(1)` is the hidden-weight-gradient kernel, and `H^(2)` is the output-weight-gradient kernel. Theorem 3.1 proves convergence of both at initialization to independent random α/2-stable matrices. Proposition 3.2(ii) proves `sup_{t≥0} ||\widetilde H_m^(2)(t)−\widetilde H_m^(2)(0)||_F < λ_0 m^(−γ/α)` with high probability for each `γ∈(0,1)` and a positive lower bound for the *full* kernel. It does **not** prove full-kernel freezing. Theorem 3.2 proves exponential training-error decay, using only the lower bound. Section 4 explicitly says fluctuations of `\widetilde H_m^(1)` during training remain unclear (published PDF pp. 9–10). It says a kernel-regression equivalence consequently remains open.

Proposition 3.2 and Theorem 3.2 require `k≥1` unit, linearly independent training inputs. `k=d=1`, `x_1=1`, **any fixed real target `y`** obey these assumptions. The paper's ReLU derivative is the strict-positive indicator, so the scalar flow convention `ReLU'(0)=0` is consistent with its stated formulas. Explicitly specify this convention at the kink when stating the scalar theorem.

Source locations: [published paper PDF](https://iris.unibocconi.it/retrieve/1d4101f5-ffcd-480d-8966-6c0f01de8f2b/2651_Large_width_asymptotics_a.pdf) pp. 4–10, particularly equations (6), (8), (10)–(13), Theorem 3.1, Proposition 3.2, Theorem 3.2 and §4. Web retrieval refs: `turn212view1`, `turn215view0`, `turn213view1`, `turn213view2`, `turn212view3`, `turn213view3`.

## Earlier direct positive-probability mechanism

Let `U_i` be the scalar hidden weight and `W_i` the scalar output weight. Put `q_m=(m log m)^(-1/α)` and `b_m=η_m q_m=m^(-1/α)(log m)^(1/α)`. If `F_m(0)<y` then the residual retains its sign because `d(y−F_m)/dt=−\widetilde H_m(t)(y−F_m)`. In the intrinsic clock

`s(t)=b_m ∫_0^t (y−F_m(v))dv`,

each active neuron obeys `dU_i/ds=W_i`, `dW_i/ds=U_i` until it hits zero. Thus, while active, `U_i(s)=U_i(0)cosh(s)+W_i(0)sinh(s)` and `W_i(s)=W_i(0)cosh(s)+U_i(0)sinh(s)`. An initially active pair with `U_i(0)∈[u_0,u_1]⊂(0,∞)` and `W_i(0)<−A m^(1/α)` hits zero by intrinsic time `atanh(U_i(0)/|W_i(0)|)≤(u_1/A+o(1))m^(−1/α)`, and subsequently stops. Its contribution to `\widetilde H_m^(1)` falls by at least `A²` up to a negligible change in its output weight. The event of at least one such pair has probability tending to `1−exp[−c_- A^(−α) P(U∈[u_0,u_1])] > 0`, where `c_-` is the negative stable-tail constant.

Potential rigorous closure: `B_m=m^(−2/α)Σ_i(W_i(0)²+U_i(0)²)=O_P(1)` and `F_m(0)=O_P(1)` (initial stable limits). Restrict to a fixed high-probability bound `B_m,|F_m(0)|≤M`; choose fixed `y>2M`. For `t_m=C(log m)^(−1/α)`, the clock is at most `C(y+M)m^(−1/α)`; the normalized kernel is bounded by `e^{2s}B_m`, so the residual remains at least `y/3` through `t_m` for large `m`. Hence `s(t_m)≥Cy m^(−1/α)/3`; choose `C>3u_1/(Ay)`. Every targeted extreme then dies by `t_m`. For all initially active survivors, the sum of their normalized changes in `W_i²` is at most `O(s(t_m)e^{2s(t_m)} B_m)=o(1)`; killed neurons contribute negative jumps relative to their initial `W_i²`, apart from the same small smooth correction. Initially inactive neurons cannot activate under the strict-positive ReLU derivative. Consequently on an event with asymptotically positive probability,

`\widetilde H_m^(1)(t_m)−\widetilde H_m^(1)(0)≤−A²+o(1)`.

This direct argument shows nonfreezing for sufficiently large fixed positive `y` at one deterministic shrinking time. It is now superseded in strength by the *all-label scalar law* below, but it independently identifies the physical clock of an extreme neuron. Keep the proof's event probability explicit and ensure the stable-tail and initial-output tightness constants are chosen in the right order (`A,u_0,u_1` first, then `M` large, then `y,C`).

## Stronger all-label scalar result: source comparison and constant audit

The separate local notes [T384_joint_limit.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_joint_limit.md) and [T384_scalar_dynamics.md](sandbox:/workspace/scratch/b6cbf133045d/continuation_2026_10_24/research/T384_scalar_dynamics.md) together give a much stronger, **one-input scalar** theorem. The following explicit constants assume standard independent symmetric stable initialization, `E exp(izU)=E exp(izW)=exp(−|z|^α)`; for the paper's general common scale `σ`, multiply `F,Q,D` by `σ²`. Put `β=α/2`, `c_α=Γ(α)sin(πα/2)/π`, and `h_β=Γ(1−β)`. Then, jointly, the initial output and marked endpoint sums converge

`(F_m,A_m,B_m,C_m) ⇒ (F,A,B,C)`, with all four limits independent,

`E exp(izF)=exp(−c_α|z|^α)`,

`E exp(−sA)=E exp(−sB)=exp(−(c_α/2)h_β s^β)`, and

`E exp(−sC)=exp(−c_α h_β s^β)`, where

`A_m=m^(−2/α)Σ_i W_i²1_{U_i>0,W_i>0}`, `B_m=m^(−2/α)Σ_i W_i²1_{U_i>0,W_i<0}`, `C_m=m^(−2/α)Σ_i(U_i^+)²`.

The published paper's Theorem 2.1 supplies an initial-output marginal stable limit; Theorem 3.1 supplies **only** joint initialization convergence of `H^(1)=A_m+B_m` and `H^(2)=C_m` to two independent stable quantities. It does not split first-layer extremes by the output-weight sign or state independence of the initial output from these two kernels. The four-way independence is an additional joint limit proved in the local note by disjoint coordinate-axis Lévy jumps. The constants cross-check the paper: `A+B` and `C` each have Laplace exponent `c_α h_β s^β`, matching its independent, identically scaled scalar initial-kernel components; the source uses `C_α=2c_α` in its symmetric-stable spectral-measure convention (equation (4)).

Fix **any** deterministic `y∈R`. Let `S=sgn(y−F)` (almost surely nonzero) and set `Q=C+A, D=B` if `S=+1`; `Q=C+B, D=A` if `S=−1`. Although the selection uses `F`, the equal independent laws of `A,B` imply **`F`, `Q`, `D` are mutually independent**. In particular,

`E exp(−sQ)=exp(−(3c_α/2)h_β s^β)`, and `E exp(−sD)=exp(−(c_α/2)h_β s^β)`.

The scalar-flow note proves, without assuming this joint limit, that for every finite `T`,

`sup_{0≤t≤T}|f_m(t)−[y−(y−F_m)exp(−Q_m t)]|→_P0`, and for every `0<δ<T`,

`sup_{δ≤t≤T}|\widetilde H_m(t)−Q_m|→_P0`, where `Q_m=C_m+A_m` or `C_m+B_m` according to the sign of `y−F_m`.

Combining these two notes by the continuous mapping and converging-together theorems gives the **process convergence in distribution** in `C([0,T])` to

`f(t)=y−(y−F)e^(−Qt)`.

Jointly, the scaled kernel at initialization tends to `Q+D`, while on every fixed interval `[δ,T]` away from zero its trajectory tends to the constant `Q`. With the strict-positive gate, finite-width kernels can jump down at death times, so the natural process space for the kernel is `D([δ,T])` with its Skorokhod topology; the displayed supremum approximation is stronger than needed there. More precisely, the width-dependent uniform approximation above implies that at every fixed `t>0`,

`(F_m,\widetilde H_m(0),\widetilde H_m(t)) ⇒ (F,Q+D,Q)`, hence `\widetilde H_m(0)−\widetilde H_m(t)⇒D>0` almost surely. The same nonzero drop occurs in the first-layer kernel, while `H^(2)` freezes. This gives **nonfreezing for every fixed label**, including `y=0`, and disproves a *fixed-initial-NTK* finite-time flow in this scalar case. Because `F,Q,D` are independent and `F` has no atoms, `y−F≠0` almost surely for every deterministic `y`; the two exponential flows with rates `Q` and `Q+D` genuinely differ at every `t>0` almost surely. An initial boundary layer removes the opposing-sign extreme contribution without changing the continuous limiting output path. There is no uniform-in-time convergence of the kernel to a constant on `[0,T]`; its value at zero has a different limit from every positive-time value. These claims do not describe the complete rescaled boundary-layer profile.

The source's Theorem 3.2 only bounds training-error decay by a random-width, high-probability exponential rate; it gives neither the exact scalar rate nor a limiting output path. Its §4 explicitly says fixed-initial-α-stable-NTK kernel-regression equivalence is open and the first-layer fluctuations are unresolved. The theorem above answers the latter **negatively in the admissible one-input specialization** and identifies the sign-selected effective rate. It does not settle arbitrary multi-input/deep geometries or test-point kernel-regression predictions.

## Subsequent literature checked and scope of novelty

Searches of primary sources through 2026-10-23 found no paper proving first-layer freezing or nonfreezing in **this exact iid symmetric α-stable, both-layers-trained, `(m log m)^(-1/α)` model**. This is a bounded literature-search conclusion, not a claim that no such paper exists. The 2024 published source itself explicitly leaves the first-layer question open. A 2025 TMLR paper, Caron et al., [*Over-parameterised Shallow Neural Networks with Asymmetrical Node Scaling*](https://arxiv.org/abs/2302.01002), analyzes a distinct model: its hidden weights initialize Gaussian (Assumption 2.3) and its output weights are held fixed (§2.1); its feature-learning conclusion does not answer Favaro–Fortini–Peluchetti's open first-layer fluctuation question. The 2025 [*Deep Kernel Posterior Learning under Infinite Variance Prior Weights*](https://openreview.net/forum?id=usFdPd4Ghs) is Bayesian posterior learning, rather than the cited gradient flow. Other deep-stable-network work studies the initialized prior/forward limit, not this kernel trajectory.

The further targeted 2025–2026 searches (`"alpha-stable ReLU" "first layer" "training"`, `"stable neural tangent kernel" "boundary layer"`, exact published title plus 2025/2026, and author publication lists) likewise surfaced no later primary paper with this four-way joint initialization law, sign-selected scalar flow, or positive-time first-layer-kernel limit. This remains a bounded search finding, not a global priority guarantee. Present the result as an **explicit scalar stochastic wide-limit with an initial kernel drop under both-layer continuous gradient flow**, not a solution of all multi-input/deep T384 or discrete gradient descent.
