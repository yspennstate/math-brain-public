# C06/H0008 -> P03 reusable lemma: sub-Weibull Poisson corrector from `L^2` mixing

Source derivation: `research7_2026-09-17/R7-07/runs/2026-09-20/2026-09-20T160200Z__report.md`.

This handoff does **not** change P03 ownership, objective, claim status, or files. It records a reusable probabilistic mechanism only.

## Lemma template

Let `K` be a stationary Markov kernel with invariant law `mu`. Suppose a centered observable `h` satisfies

`||K^n h||_2 <= C e^{-cn}`

and has an exponential moment, equivalently `||h||_p <= C p` for all `p>=2`. Since `K` is an `L^q(mu)` contraction, interpolation between `L^2` and `L^{2p}` gives

`||K^n h||_p <= C p exp[-c n/(p-1)]`.

Hence the Poisson corrector

`u=sum_{n>=0}K^n h`

obeys

`||u||_p <= C p^2`,

so for some `eta>0`,

`E_mu exp(eta sqrt(|u|))<infinity`.

The martingale difference `D_1=u(Y_1)-Ku(Y_0)` has the same `p^2` moment growth and therefore the same tail

`P(|D_1|>x) <= C exp(-c sqrt x)`.

If the predictable variance `v=K(u^2)-(Ku)^2` is centered by its mean and the same `L^2` mixing applies to all `L^{2+epsilon}` observables, then

`||v||_p=O(p^4)`,

its Poisson corrector `z=sum K^n(v-Ev)` has

`||z||_p=O(p^5)`,

and Burkholder yields

`||sum_{k<n}(v(Y_k)-Ev)||_p <= C sqrt(n) p^6`.

Optimizing at `p~n^(1/12)` gives `exp(-c n^(1/12))` concentration of normalized predictable quadratic variation. Together with the sub-Weibull large-jump estimate, the standard martingale moderate-deviation criterion gives a Gaussian MDP on every scale `a_n->infinity`, `a_n=o(n^(1/24))`, provided the asymptotic variance is positive.

## Why this may help the Galton--Watson speed roles

In regeneration/speed problems one often has only a Hilbert-space spectral estimate plus a source observable with an exponential moment, rather than a uniform `L^infinity` spectral gap. The interpolation argument above turns those two ingredients into an explicit Orlicz class for the Poisson corrector without assuming bounded offspring or bounded regeneration rewards. It can therefore provide quantitative endpoint control and a nontrivial moderate-deviation window before a stronger geometric-regeneration exponential moment is available.

The exponent `1/24` is not claimed sharp; it reflects two resolvent/interpolation losses plus a Burkholder step. Improving the `L^p` resolvent estimate enlarges the window automatically.
