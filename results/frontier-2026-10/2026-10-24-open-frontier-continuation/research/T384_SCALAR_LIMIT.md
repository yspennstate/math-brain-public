# T384: the complete one-input stable ReLU training limit

**Status, 23 October 2026 UTC:** self-contained theorem assembled from independently reviewed probability and dynamics lemmas. This resolves the scalar first-layer-freezing and finite-time training-limit questions under the exact assumptions below. External novelty and expert review remain unverified. The general deep/multi-input T384 row remains open.

## Theorem

Fix `0<alpha<2`, one training input `x=1`, any deterministic label `y in R`, and finite `T>0`. All initial hidden and output weights `(U_i,W_i)` are independent standard symmetric alpha-stable variables with characteristic function `exp(-|z|^alpha)`. Use no biases and train both layers by continuous gradient flow on half the squared error, with

`f_m(t)=(m log m)^(-1/alpha) sum_i w_i(t)(u_i(t))_+`,

learning rate `(log m)^(2/alpha)`, and the absorbing ReLU flow at zero. The rate-scaled kernel is

`H_m(t)=m^(-2/alpha) sum_i [w_i(t)^2 1_{u_i(t)>0}+(u_i(t))_+^2]`.

Put `b=alpha/2`, `c_alpha=Gamma(alpha) sin(pi alpha/2)/pi`, and `g_b=Gamma(1-b)`. There exist mutually independent random variables F,Q,D with transforms

`E exp(iz F)=exp(-c_alpha |z|^alpha)`,

`E exp(-s Q)=exp[-(3c_alpha/2) g_b s^b]`,

`E exp(-s D)=exp[-(c_alpha/2) g_b s^b]`, `s>=0`,

such that the following limits hold jointly:

1. In `C([0,T])` with uniform norm,

   `f_m(.) => [t -> y-(y-F)exp(-Qt)]`.

2. For every `0<delta<T`, `sup_{delta<=t<=T}|H_m(t)-Q_m| -> 0` in probability, where Q_m is defined below. Consequently the kernel restricted to `[delta,T]` converges to the constant path Q in `D([delta,T])` with the J1 topology, jointly with `(F_m,H_m(0),f_m)`, and `H_m(0) => Q+D`.

3. For every fixed `t>0`,

   `(H_m(0),H_m(t),H_m(0)-H_m(t)) => (Q+D,Q,D)`.

In particular D is strictly positive almost surely. The first-layer kernel has exactly the same limiting loss D, while the second-layer kernel freezes. This is nonfreezing for every fixed label, not merely the large-label event used in the shorter counterexample.

The initial kernel value and the positive-time limit are intentionally recorded separately. A function taking Q+D at zero and Q at every positive time is not right-continuous at zero. We do not claim usual Skorokhod convergence on `[0,T]` to that function. Kernel paths on positive-time intervals may be viewed in `D([delta,T])`; the continuous output paths do converge in `C([0,T])`.

## Four independent initialization components

Define

`F_m=f_m(0)`,

`A_m=m^(-2/alpha) sum_i W_i^2 1_{U_i>0,W_i>0}`,

`B_m=m^(-2/alpha) sum_i W_i^2 1_{U_i>0,W_i<0}`,

`C_m=m^(-2/alpha) sum_i (U_i)_+^2`.

Then `(F_m,A_m,B_m,C_m) => (F,A,B,C)`, with all four limits independent,

`E exp(-s A)=E exp(-s B)=exp[-(c_alpha/2)g_b s^b]`,

`E exp(-s C)=exp[-c_alpha g_b s^b]`.

The proof is `T384_joint_limit.md`, independently checked in `../reviews/T384_joint_review.md`. Its nontrivial point is joint independence, not the separate stable limits. Product extremes use the `(m log m)^(1/alpha)` scale, whereas endpoint weight extremes use `m^(1/alpha)`. Their simultaneous large-jump probabilities vanish. Centered small product jumps have a vanishing second-moment bound after truncation; small positive endpoint jumps have a vanishing first-moment bound. The resulting limiting jump measure is supported on four independent coordinate axes. The product-tail calculation gives `P(WU_+>z)~alpha c_alpha^2 z^(-alpha)log z`, fixing the constant in F.

## The dynamic reduction

Let `r_0m=y-F_m` and set

`Q_m=C_m+A_m` when `r_0m>0`, and `Q_m=C_m+B_m` when `r_0m<0`.

The value at `r_0m=0` can be chosen arbitrarily. The residual is then identically zero; in the limit the event has probability zero. `T384_scalar_dynamics.md`, independently checked in `../reviews/T384_dynamics_review.md`, proves

`sup_{t<=T}|(y-f_m(t))-r_0m exp(-Q_m t)| -> 0` in probability,

`sup_{delta<=t<=T}|H_m(t)-Q_m| -> 0` in probability,

and `sup_{t<=T}|H_2m(t)-C_m| -> 0` in probability.

Here is the mechanism and the key quantitative control. The residual keeps its sign sigma. In the common clock

`s_m(t)=m^(-1/alpha)(log m)^(1/alpha) int_0^t |y-f_m(v)|dv`,

the active pair `(u_i,sigma w_i)` follows a hyperbolic rotation until u_i reaches zero. The total normalized change of ungated squared weights is `o_P(1)` on bounded physical-time intervals. However, an opposing extreme output weight of order `m^(1/alpha)` changes its hidden activation by order `(log m)^(1/alpha)`. At every fixed positive time, all surviving opposing weights contribute `o_P(1)` to the first-layer kernel. Indeed, after removing weights below `epsilon m^(1/alpha)`, whose expected normalized mass is `O(epsilon^(2-alpha))`, a surviving opposing extreme would require an independent hidden weight at least a fixed multiple of `(log m)^(1/alpha)`. A union bound makes that event `O(1/log m)`. Supporting-sign weights survive. Splitting the kernel time integral at a small delta removes the initial interval and gives the uniform residual approximation.

The absorbing flow is explicit. With continuous iid initialization there are almost surely no initially zero hidden weights. Every later finite gate hit has an opposing transformed output weight `-sqrt(W_i(0)^2-U_i(0)^2)<0`; it cannot depart the zero gate in either direction under the one-sided flow. Thus generic nonuniqueness examples for a discontinuous ODE with an initially zero, outward-pointing neuron do not obstruct this theorem.

## Composition and independence of the effective rate

Since F has a continuous density, the map selecting A or B according to `sgn(y-F)` is almost surely continuous for the initialization limit. Define

`S=A, D=B` on `{F<y}`, and `S=B, D=A` on `{F>y}`; set `Q=C+S`.

Conditional on any value of F, `(S,D)` has the same law as the independent identically distributed pair `(A,B)`. It follows that F,S,D,C are mutually independent. Adding the positive stable Laplace exponents of C and S yields the Q transform in the theorem. The continuous mapping theorem and the dynamic approximation now give the joint output and kernel conclusions.

This explains the coefficients: the initial full-kernel Laplace exponent is `2c_alpha g_b`; the surviving exponent is `(3c_alpha/2)g_b`; the removed exponent is `(c_alpha/2)g_b`. These are proportions of stable jump intensity, **not proportions of the realized kernel, and not ratios of finite means**. The positive stable variables have infinite mean.

## Consequences and boundaries

For any fixed `t>0` and any epsilon>0 at which the positive stable distribution is continuous,

`P(H_m(0)-H_m(t)>epsilon) -> P(D>epsilon)>0`.

The frozen-initial-kernel prediction `f_fr,m(t)=y-(y-F_m)exp[-H_m(0)t]` has joint limit

`f_fr(t)=y-(y-F)exp[-(Q+D)t]`.

For `t>0`, its difference from the actual limiting flow is

`f(t)-f_fr(t)=-(y-F)exp(-Qt)(1-exp(-Dt))`,

which is nonzero almost surely. Hence finite-time equivalence to the initial NTK fails. Both one-sample limiting flows still approach y as `t->infinity`; this theorem does not assert distinct fully trained predictions or settle a multi-input kernel-regression equivalence.

This result covers continuous full-batch training, one scalar input, fixed alpha<2, iid symmetric stable weights, and ReLU. It does not cover discrete step sizes, alpha=2 under this scaling, smooth activations, multiple interacting examples, deep networks, or dependent initial weights. Those are explicit next directions rather than implicit extensions.

## Provenance and literature boundary

The model and the previously open first-layer-fluctuation issue are in Favaro, Fortini and Peluchetti, [*Large-width asymptotics and training dynamics of alpha-Stable ReLU neural networks*, TMLR, November 2024](https://iris.unibocconi.it/retrieve/1d4101f5-ffcd-480d-8966-6c0f01de8f2b/2651_Large_width_asymptotics_a.pdf), equations (6), (8), (10)–(13), Proposition 3.2 and Section 4. Their second-layer control and exponential error bound do not give the sign-selected scalar limiting rate. Earlier Brain numerical nonfreezing evidence is credited in `sources/T384_pins.json`.

B01 derived the joint stable law; B06 derived the scalar dynamical reduction; root supplied the extreme-neuron route and composed the all-label limit. B03 independently reviewed the joint law and sign-selection independence; B04 independently reviewed the dynamics and kink qualification; B02 verified the published model and performed a bounded subsequent-literature search. All six GPT-6/max workers' notes and reviews are retained. The search found no equivalent exact-model theorem, but external priority is not established by that search.
