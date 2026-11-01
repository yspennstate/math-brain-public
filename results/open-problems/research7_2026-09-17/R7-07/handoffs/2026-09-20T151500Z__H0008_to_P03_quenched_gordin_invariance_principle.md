# C06/H0008 -> P03 reusable lemma: quenched Gordin invariance principle from stationary full-state mixing

Source derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T151000Z__report.md`.

This handoff does **not** change P03 ownership, objective, source statement, or current proof status. It records one reusable probabilistic mechanism only.

## Lemma template

Let `K` be a Markov kernel on a state space with stationary ergodic law `mu`. Suppose a centered observable `f` admits a forward Poisson solution

`u = sum_{m>=0} K^m f`

with `u in L^p(mu)` for some `p>4`, so `f=u-Ku`. For the chain `Y_k` started from a fixed state `x`, define

`D_{k+1}=u(Y_{k+1})-Ku(Y_k)`,

`M_n=sum_{k<n} D_{k+1}`.

Then

`sum_{k<n} f(Y_k)=M_n+u(Y_0)-u(Y_n)`.

If

`v(x)=K(u^2)(x)-(Ku(x))^2`

has mean `sigma^2=mu(v)`, then for `mu`-almost every deterministic initial state `x`, the predictable quadratic variation satisfies

`(1/n) sum_{k<n} v(Y_k) -> sigma^2`

almost surely under `P_x`, by stationary Birkhoff plus disintegration.

If `u in L^{2+delta}` for some `delta>0`, the martingale Lindeberg condition follows from

`E[D_{k+1}^2 1{|D_{k+1}|>eps sqrt(n)} | Y_k]`
` <= eps^{-delta} n^{-delta/2} E[|D_{k+1}|^{2+delta}|Y_k]`

and another disintegrated ergodic theorem.

If an additional coboundary endpoint `W(Y_0)-W(Y_n)` is present with `W in L^p(mu)` for some `p>4`, then

`P_mu(max_{k<=n}|W(Y_k)|>eps sqrt(n))`
` <= C n^{1-p/2}`.

The right side is summable, so Tonelli implies that for `mu`-a.e. fixed start `x`,

`max_{k<=n}|W(Y_k)|/sqrt(n) -> 0`

in `P_x`-probability. Therefore the martingale functional CLT upgrades directly to a **quenched** FCLT from almost every deterministic starting environment.

## Why this may help P03

For Galton--Watson speed/regeneration roles, if an additive speed observable can be written as a stationary forward Poisson coboundary plus an all-moment endpoint, then an annealed stationary CLT need not be the endpoint: the same decomposition can yield a fixed-environment/quenched invariance principle without constructing a second regeneration hierarchy. The only model-specific work is the stationary law, the Poisson solution, and identification/positivity of `mu(v)`.

Do not import H0008's variance positivity or conductance identities into P03 without proving the P03-specific hypotheses.