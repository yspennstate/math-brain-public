# Independent adversarial review — T384 scalar dynamics and nonfreezing

**Verdict: PASS for the stated scalar, one-input, finite-time claims, with two precision edits recommended.** I checked `research/T384_scalar_dynamics.md` against the model and scaling in Favaro–Fortini–Peluchetti ([arXiv:2206.08065](https://arxiv.org/pdf/2206.08065), Theorem 1, equations (4)–(9), Theorem 4), and checked the strengthened full-kernel/frozen-trajectory claims in `research/T384_NONFREEZING.md`. I found no missing contribution of the initially opposing weights or incorrect use of a joint initialization limit. The common-clock and truncation arguments give the advertised convergence in probability. This review does not independently certify the separate four-coordinate joint limit in `research/T384_joint_limit.md` or any external novelty claim.

## Exact flow and both residual signs

With `c_m=(m log m)^(−1/α)`, `η_m=(log m)^(2/α)`, `β_m=η_m c_m`, the identity `η_m c_m²m^(2/α)=1` gives

`r'=−r m^(−2/α)Σ_{U_i>0}(W_i²+U_i²)=−rK_m` almost everywhere.

The output is continuous at a gate hit because `W_i(U_i)_+` vanishes there, even though `K_m` jumps. Thus the integrated residual identity is valid through the finite number of possible hits, `r(t)=r_0 exp(−∫_0^tK_m)`, preserving sign. If `r_0=0`, every coordinate is stationary on the selected flow and the residual approximation is exact.

For `r_0≠0`, set `σ=sgn(r_0)`, `V_i=σW_i`, `s=β_m∫|r|`. Since `ds/dt=β_m|r|`, on the active side `dU_i/ds=V_i`, `dV_i/ds=U_i`, for **either** `σ=+1` or `σ=−1`. An initially active `V_i>0` remains active; `V_i<0` is the opposing class. The exact survival condition at clock `s` is

`U_i(0)>|V_i(0)| tanh s`.

It includes `|V_i(0)|≤U_i(0)`, which never hits at finite `s`, rather than treating that case as an exception. Therefore the note's `Q_m=C_m+A_m` for positive residual and `Q_m=C_m+B_m` for negative residual is the correct sign selection. In particular, when `r_0<0`, **positive** initial `W_i` are opposing and are removed, while negative initial `W_i` support the motion.

## Uniform square drift and the kernel bound

For any initially active neuron up to its hit, the hyperbolic matrix has norm at most `e^s`. After its hit both coordinates freeze. Uniformly for `t≤T`, each coordinate difference has magnitude at most `s_m(T)e^{s_m(T)}||(U_i(0),W_i(0))||`. Hence the elementary inequality `|z_t²−z_0²|≤2|z_0||z_t−z_0|+|z_t−z_0|²` proves the stated common bound

`m^(−2/α) Σ_i |W_i(t)²−W_i(0)²|≤g(s_m(T))S_m`,

`g(s)=2se^s+s²e^(2s)`, uniformly in `t`. The same argument after the 1-Lipschitz positive-part operation bounds `|H_m^(2)(t)−C_m|`. It is valid for giant individual coordinates because it sums **their initial squares** into the tight `S_m`; no per-neuron uniform boundedness is assumed. Dropping deactivated neurons gives `K_m(t)≤e^(2s_m(t))S_m`, including at jump times under the `1_{U_i>0}` convention.

Since `S_m=m^(−2/α)Σ(U_i(0)²+W_i(0)²)` is tight for `α/2<1`, `r_{0m}=y−F_m` is tight, and `β_m→0`, we have `s_m(T)≤β_m T|r_{0m}|=o_P(1)` and `g(s_m(T))S_m=o_P(1)`. Thus coordinate-square drift cannot mask the gate changes; also `H_2` freezes uniformly on bounded time intervals.

## Elimination of opposing mass

On `G_m={c≤|r_0|≤R,S_m≤K}`, `K_m(t)≤2K` eventually and `s_m(δ)≥dβ_m`, `d=cδ e^(−2KT)>0`. If an initially opposing weight has `|W_i(0)|≥εm^(1/α)` and remains active at `δ`, the survival condition forces

`U_i(0)≥(dε/2)(log m)^(1/α)`

for large `m`. Independence of initialized `U_i,W_i` gives the unconditional union bound

`m P(|W|≥εm^(1/α))P(U≥(dε/2)(log m)^(1/α))=O_{d,ε}(1/log m)→0`.

The entire normalized mass of smaller opposing weights is at most `Z_{m,ε}` with `E Z_{m,ε}≤C ε^(2−α)` uniformly in large `m`, so Markov's inequality followed by `ε↓0` removes it. This two-scale argument is necessary: tightness of `S_m` and small coordinate motion alone would not remove the activation indicator of an extreme weight. It also disposes of the rare `|V_i(0)|≤U_i(0)` large-weight survivors. Monotonicity of gate loss and the uniform coordinate bound then establish

`sup_{δ≤t≤T}|K_m(t)−Q_m|→_P0`

for every fixed `δ>0`. The marginal stable output limit in the paper's Theorem 1 is nondegenerate at `x=1`, hence atomless, so `P(|r_{0m}|<c)` vanishes in the iterated limit `m→∞`, `c↓0`. No joint limit with `A_m,B_m,C_m` is used.

## Near-zero residual and limit topology

The residual statement is stronger than the positive-time kernel statement in its handling of `r_0≈0`. On `|r_0|<c`, both actual and proposed residuals have magnitude at most `c`, so their difference is at most `2c` regardless of gate behavior. On `G_m`, split `∫(K_m−Q_m)` at `δ`: the first piece is at most `3Kδ`, and the rest is controlled by positive-time kernel convergence. Taking `m→∞`, then `δ↓0`, `R,K↑∞`, and finally `c↓0` proves

`sup_{t≤T}|r_m(t)−r_{0m}e^(−Q_mt)|→_P0`

without an atomlessness assumption. The text should keep this distinction: the **kernel** convergence needs to rule out persistent `r_0=0` mass; the **residual** convergence does not.

The convergence is to a **width-dependent random comparator**, not by itself a weak process limit. If the separate joint initialization theorem is accepted, the continuous mapping theorem applies at `F≠y` and yields `Q=C+A` on `F<y`, `Q=C+B` on `F>y`; the residual/output paths then converge in `C([0,T])` to `(y−F)e^(−Qt)` and `y−(y−F)e^(−Qt)`. Under that theorem's claimed independence and identical laws of `A,B`, the selected `Q` is independent of `F` and has Laplace transform `E e^(−sQ)=exp[−(3c_α/2)Γ(1−α/2)s^(α/2)]`. This is a consequence **conditional on** the separate joint proof, not a premise of the scalar dynamics argument. The kernel has separate limits `K_m(0)⇒H=A+B+C` and `K_m|_[δ,T]⇒Q` uniformly on every fixed positive-time interval. Since `H−Q` is a positive opposing mass almost surely under the proposed joint stable law, do **not** claim convergence of `K_m` in the usual `C([0,T])` or right-continuous `D([0,T])` topology to a path with its old value at zero and new value for every `t>0`; that putative path is not right-continuous at zero. The current scalar-dynamics note correctly avoids such a claim.

## Kink selection: earlier generic caveat is harmless almost surely here

For a discontinuous Carathéodory ODE, merely specifying `ReLU'(0)=0` can allow delayed departure from an *initially zero* neuron with outward `V>0`; this was the caveat in `research/T384_flow_audit.md`. In the present iid stable model, the initialization has a continuous density, so `P(∃i:U_i(0)=0)=0` at each finite `m`. Initially negative `U_i` cannot move to zero. Every *attained* zero of an initially active neuron requires `V_i(0)<−U_i(0)` and has

`V_i(s_*)=−sqrt(V_i(0)²−U_i(0)²)<0`.

With `r` retaining its sign, departure from that zero toward `U>0` would have negative active-side derivative `dU/ds=V<0`, while departure toward `U<0` has zero inactive-side derivative. Neither is possible for an absolutely continuous forward solution. Thus every attained zero is necessarily absorbing, even under the a.e. ODE interpretation; the initially-zero nonuniqueness event is null. The explicit absorbing selection in the note is entirely valid and removes any residual ambiguity for exceptional deterministic starts. This argument needs to be stated if someone invokes my earlier generic kink caveat against the stochastic theorem.

## Check of the strengthened nonfreezing claims

`research/T384_NONFREEZING.md` couples a positive-probability extreme opposing neuron with bounded initial output and bounded `H(0)` by a union bound; no false independence is assumed. Its deterministic clock bound removes that neuron before `t_m→0`. Other `H_1` weights increase by at most `K(e^(2β_mRT)−1)/2=o(1)`, and `H_2` changes by at most the same order. Therefore `H(0)−H(t)≥1−o(1)` uniformly for `t∈[t_m,T]`, while `H(t)≤H(0)+o(1)` on the earlier interval. Integrating gives `∫_0^T H(t)dt≤T H(0)−T/2` eventually on the event. With `r_0≥1` and `H(0)≤K`,

`|f_m(T)−[y−r_0e^(−TH(0))]|≥e^(−KT)(e^(T/2)−1)>0`.

The full-kernel and frozen-trajectory consequences check. They concern finite `T`; both true and frozen scalar systems can still interpolate the label as `T→∞`.

## Recommended precision edits, no theorem change

1. In the scalar note, state that `S_m` tightness follows from the standard `α/2`-tail truncation bound, or cite `research/T384_probability.md` §2; invoking the stable-sum theorem is also sufficient. Name the ReLU convention as a **solution selection** for exceptional initially-zero coordinates, while noting that continuous iid initialization and inward-pointing hits eliminate this ambiguity almost surely.
2. If the joint initialization limit is imported later, specify the target topology: residual/output in `C([0,T])`, kernel locally uniform away from `t=0` with its initial value recorded separately. Its jump is concentrated in a vanishing boundary layer, so a single ordinary càdlàg kernel limit retaining both values is impossible.

**Sources checked:** [Favaro–Fortini–Peluchetti PDF](https://arxiv.org/pdf/2206.08065), especially Theorem 1 and Theorem 4; [Brain T384 dossier](https://github.com/<private-repo>/blob/main/06_math_research/frontier/rows/T384/DOSSIER.md). The paper says that Theorem 4 controls fluctuations of its second-layer kernel while first-layer fluctuations were unresolved there; the present proof's claim is narrower than the full T384 multi-input/deep question.
