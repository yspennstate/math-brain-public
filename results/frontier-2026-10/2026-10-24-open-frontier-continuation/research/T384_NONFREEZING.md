# T384: a scalar stable ReLU network whose NTK does not freeze

**Status:** complete scoped proof, independently reviewed in this campaign; external priority and human review unverified. This closes a negative-answer subproblem of T384, not the full deep/multi-input training-limit program.

## Model and theorem

Fix `0<alpha<2`. For one input `x=1`, initialize all `U_i,W_i` independently with characteristic function `exp(-|t|^alpha)`. At width `m>=2`, set

`c_m=(m log m)^(-1/alpha)`, `eta_m=(log m)^(2/alpha)`, `beta_m=eta_m c_m`,

`f_m(t)=c_m sum_i w_i(t) (u_i(t))_+`, `r_m(t)=y-f_m(t)`.

Train both layers on `r_m^2/2` by gradient flow at rate `eta_m`, using `ReLU'(0)=0` and the resulting absorbing flow when an active neuron reaches zero. Write the **rate-scaled** kernels

`H_1(t)=m^(-2/alpha) sum_i w_i(t)^2 1_{u_i(t)>0}`,

`H_2(t)=m^(-2/alpha) sum_i (u_i(t))_+^2`, `H(t)=H_1(t)+H_2(t)`.

There are deterministic constants `y`, `p>0`, depending only on alpha, such that for every fixed `T>0`,

`liminf_m P(H_1(0)-H_1(T)>=1/2) >= p`,

`liminf_m P(H(0)-H(T)>=1/2) >= p`.

Moreover, for each `T>0`, there is `epsilon_T>0` such that, with `f_fr(T)=y-r_m(0) exp(-T H(0))`,

`liminf_m P(|f_m(T)-f_fr(T)|>=epsilon_T) >= p`.

The same fixed `y,p` work for all fixed positive T; the minimum sufficiently large width may depend on T. The theorem concerns the non-Gaussian range alpha<2. No limiting claim for alpha=2 is made under the logarithmic scaling.

## 1. A positive-probability initialization event

Let `E_m` mean some neuron satisfies `0<U_i<1` and `-2m^(1/alpha)<=W_i<=-m^(1/alpha)`. Standard stable tails give

`P(E_m) -> p_*=1-exp[-c_alpha(1-2^(-alpha))P(0<U<1)]>0`,

where `c_alpha=Gamma(alpha) sin(pi alpha/2)/pi` is the one-sided tail constant. Both `f_m(0)` and `H(0)` are tight. A self-contained truncation proof is in `T384_probability.md`: product tails are at most `C t^(-alpha)(1+log t)`; squared weights have tail exponent alpha/2<1.

Choose finite M,K so the two respective tail errors are smaller than `p_*/4`, and set `y=M+1`, `R=2M+1`. On

`A_m=E_m intersect {|f_m(0)|<=M,H(0)<=K}`,

we have `1<=r_m(0)<=R` and `liminf P(A_m)>=p_*/2`. No joint independence assertion is used. In the rest of the proof work pathwise on A_m.

## 2. Exact flow and an absorbing gate

Almost everywhere,

`u_i'=beta_m r_m w_i 1_{u_i>0}`, `w_i'=beta_m r_m (u_i)_+`, `r_m'=-H r_m`.

Thus `r_m(t)>0` and `r_m(t)<=R`. Introduce `tau(t)=beta_m int_0^t r_m(s)ds`. An initially active neuron obeys

`u_i=U_i cosh(tau)+W_i sinh(tau)`,

`w_i=W_i cosh(tau)+U_i sinh(tau)`

until u_i first hits zero, after which it stays inactive. Initially negative u_i stay fixed. These piecewise formulas construct an absolutely continuous solution of the stated ODE and avoid an unstated smoothness assumption at the ReLU kink.

Let `Q_i=u_i^2+w_i^2` while active. Since `|dQ_i/dtau|=|4u_i w_i|<=2Q_i`, and deactivation removes a nonnegative contribution from H,

`H(t)<=exp(2tau(t))H(0)<=K exp(2 beta_m R T)` for `t<=T`.

Because beta_m tends to zero, this is at most 2K for sufficiently large m. Therefore `r_m(t)>=exp(-2Kt)`.

Set `t_m=4(log m)^(-1/alpha)`. Eventually `t_m<T` and `r_m(t)>=1/2` for `0<=t<=t_m`, so `tau(t_m)>=2m^(-1/alpha)`. The selected extreme neuron has hitting clock

`tau_i^*=artanh(U_i/|W_i|)<2m^(-1/alpha)`

for large m. It has therefore deactivated by t_m and remains inactive on `[t_m,T]`. Its initial H_1 contribution was at least 1.

## 3. Other weights cannot offset that loss

For a surviving neuron, integrate `|d(w_i^2)/dtau|=|2u_iw_i|<=Q_i(0) exp(2tau)` to obtain

`|w_i(t)^2-W_i^2| <= (exp(2tau(t))-1) Q_i(0)/2`.

Discarding other nonpositive changes from deactivating neurons gives, uniformly for `t in [t_m,T]`,

`H_1(t)-H_1(0) <= -1 + K(exp(2 beta_m R T)-1)/2 = -1+o(1)`.

For H_2, each `(u_i)_+^2` is continuous at deactivation and afterwards constant at zero. Integrating the same bound only until its stopping clock gives

`sup_{t<=T}|H_2(t)-H_2(0)| <= K(exp(2 beta_m R T)-1)/2=o(1)`.

Consequently `H(t)<=H(0)-1+o(1)` throughout `[t_m,T]`. At earlier times `H(t)<=H(0)+o(1)`. The two claimed nonfreezing inequalities follow on A_m, with for example `p=p_*/2`.

## 4. Failure of the finite-time frozen-initial-kernel trajectory

The preceding uniform estimates imply, eventually on A_m,

`int_0^T H(t)dt <= T H(0)-T/2`.

Since `r_m(T)=r_m(0) exp(-int_0^T H(t)dt)`,

`r_m(T)-r_m(0)exp(-T H(0)) >= exp(-KT)(exp(T/2)-1)`.

The right side is a fixed positive number. Choosing it as epsilon_T proves the third assertion. This is about the finite-time trajectory. Both a one-sample network and its frozen-kernel surrogate may still interpolate the single label as time tends to infinity, so the theorem does not assert different fully trained predictions.

## Sources, relation to the existing record, and remaining work

Primary source: Favaro, Fortini and Peluchetti, [arXiv:2206.08065v3](https://arxiv.org/pdf/2206.08065), equations (4)–(9), Theorem 4 and Section 4. Their data hypotheses allow one unit input. Theorem 4 controls H_2 and positivity; it does not assert that H_1 freezes. Our result addresses the latter issue and is consistent with their theorem.

Brain source pins: T384 dossier `ba319f075261925a8747ce1bf31fc4f4b5c29241`; moves `6289f46595e36a85cd9388d16c84f89bc57fc774`; numerical script `dd40da57d955aa8b7d8d0f3991cfd3d7f0153374`. Earlier numerical evidence is credited to the 18 October dossier. The extreme neuron's speed is `(log m)^(1/alpha)` on an order-one residual event; retaining this factor explains the vanishing boundary layer.

Independent probability proof: B01. Independent deterministic audit: B04. Independent complete proof: B06. Adversarial source-and-proof review: B03. All are AI-assisted internal checks; external expert review and external novelty have not been certified.

Next: characterize the scalar effective kernel and the joint initialization limit for arbitrary fixed labels; then investigate multiple inputs and non-absorbing smooth activation approximations. Do not retire the full T384 row on this theorem alone.
