# HARD7-03 idea before code — break the nonnested centre pair by a first-layer extreme event

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

The admitted target remains `D0025`, Seppäläinen Problem 4, frozen at `K=2` and `Q=(1/2)delta_{1/2}+(1/2)delta_1`. The tracked quantity is the rigorous lower bound `L <= Delta_2(Q)`. Carry-in from the 15:23Z checkpoint is

`L = 625000/7314597`.

That checkpoint removed the common-window decoupling exactly on the nested edge and near-edge adjacent-pair classes. The only pair class still using the crude common-window inequality is the genuinely nonnested centre pair.

This run uses **B1 / B11 / B15**.

## B1 — change category: centre pair as a joint-CDF / common-core kernel

For one centre adjacent pair, let

`R=max(Y_{-1},Y_0)`, `X=Y_{-2}`, `Z=Y_1`,

and predecessor maxima

`S=max(R,X)`, `T=max(R,Z)`.

The fresh clocks `C,D` are independent `Exp(1)`. For deterministic predecessor values `s,t`, with `q=1-theta` and `a=2-theta`, the exact two-clock kernel is

`K_theta(s,t)=E exp(theta min(s+C,t+D))`

`= q^{-1} exp(theta min(s,t)) - theta/(q a) exp(min(s,t)-q max(s,t))`.

In particular `K_theta(R,R)=2 exp(theta R)/a`. The centre-pair problem can therefore be attacked by proving a positive expectation for `K_theta(S,T)-K_theta(R,R)`, without solving the full joint law of `(S,T)`.

## B11 — dualize the loss through a one-sided gap transform

Monotonicity of `K_theta` gives, for `g>0`,

`K_theta(R+g,T)-K_theta(R,R) >= K_theta(R+g,R)-K_theta(R,R)` whenever `T>=R`.

The right-hand side is exact:

`exp(theta R) * theta/(q a) * (1-exp(-q g))`.

Thus any event producing a certified one-sided predecessor gap yields a rigorous centre correction. This is the dual object to the old common-window lower bound: instead of integrating the whole pair law, integrate the positive gap transform that the old bound discarded.

## B15 — break the symmetry on purpose

Condition on the disjoint first-layer extreme event

`E_L={A_{-1} >= A_0,A_1}`.

On `E_L`, the three shifts in `X,Y_{-1},Y_0` coincide:

`X=A_{-1}+B_{-2}` and `R=A_{-1}+M`, where `M=max(B_{-1},B_0)`.

On the subevent `B_{-2}>M`, the left predecessor has gap `g=B_{-2}-M>0`. Therefore the centre-pair gain is at least

`theta/(q a) * E[e^{theta A_{-1}} 1_{E_L}] * E[e^{theta M}(1-e^{-q(B_{-2}-M)}) 1_{B_{-2}>M}]`.

Both factors are elementary Laplace integrals. With `b=3-theta`,

`E[e^{theta A_{-1}} 1_{E_L}] = 1/q - 2/a + 1/b = 2/(q a b)`,

and, since `M` has density `2e^{-m}(1-e^{-m})`,

`E[e^{theta M}(1-e^{-q(B-M)})1_{B>M}] = 2q/(a^2 b)`.

Hence the **left-extreme** event alone contributes

`delta_L = 4 theta/(q a^4 b^2)`.

The reflected event `E_R={A_1 >= A_{-1},A_0}` is disjoint a.s. and gives the same amount. Thus one centre adjacent pair gains at least

`delta_ctr = 8 theta/(q a^4 b^2)`

over the old common-window pair bound. There are two reflected centre adjacent pairs, and each adjacent pair appears in two fourth-step predecessor windows, so the total pair subtraction improves by

`DeltaC_ctr = 4 delta_ctr = 32 theta/(q a^4 b^2)`.

Therefore, if `U4_nested` is the exact 15:23Z four-step moment bound,

`U4_new = U4_nested - DeltaC_ctr/q`.

At the inherited rational `theta=723/1250`, exploratory exact arithmetic gives `delta_ctr` about `0.45825`, `DeltaC_ctr` about `1.83300`, and `U4_new` about `866.28527`. This should certify the smaller shape constant

`A=116947/40000 = 2.923675`

by the same exact truncated-exponential comparison, moving

`L=625000/7314597` to `L=10000/116947`.

The checker will verify all rational identities, positivity, and the final Taylor margin before any theorem-level claim is made. No simulation or continuum discretization is involved.