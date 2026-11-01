# P0157 hub-scale branching-surrogate concentration

## Setup

Let `delta in (0,1)` and let `xi` be a nonnegative integer-valued offspring variable with

`E[xi] = 1-delta`,  `Var(xi)=sigma^2 < infinity`.

Let `W` be the total progeny of a Galton–Watson process started from one ancestor. For an integer `d>=1`, let

`T_d = 1 + W_1 + ... + W_d`,

where `W_1,...,W_d` are independent copies of `W`. In the local configuration-model approximation, `d` is the root degree and `xi` is the forward offspring law.

Define the hub scale

`H(d,delta)=d/delta`.

## Proposition 1 — exact first two moments

For every subcritical offspring law above,

`E[W] = 1/delta`,

`Var(W) = sigma^2/delta^3`.

Consequently,

`E[T_d] = 1 + d/delta`,

`Var(T_d) = d sigma^2/delta^3`,

and the normalized hub-fluctuation ratio is exactly

`Q(d,delta,sigma^2) := Var(T_d)/(d/delta)^2 = sigma^2/(d delta)`.

### Proof

The branching recursion is

`W = 1 + sum_{j=1}^{xi} W_j`,

with, conditionally on `xi`, iid copies `W_j` independent of `xi`.

Taking expectations and writing `m=E[xi]=1-delta`,

`E[W] = 1 + m E[W]`,

so

`E[W] = 1/(1-m)=1/delta`.

For the variance, the law of total variance gives

`Var(W) = E[ Var(sum_{j=1}^{xi} W_j | xi) ] + Var( E[sum_{j=1}^{xi} W_j | xi] )`

`= E[xi] Var(W) + Var(xi) (E[W])^2`

`= (1-delta) Var(W) + sigma^2/delta^2`.

Thus

`delta Var(W)=sigma^2/delta^2`,

hence `Var(W)=sigma^2/delta^3`. Independence of the `W_j` gives the formulas for `T_d`, and direct division gives `Q=sigma^2/(d delta)`. QED.

## Proposition 2 — explicit hub concentration

For every `a>0`,

`P( | T_d/H(d,delta) - (1+delta/d) | >= a ) <= sigma^2/(a^2 d delta)`.

In particular, for a sequence `(delta_n,d_n,sigma_n^2)` with

`delta_n -> 0`, `d_n delta_n -> infinity`, and `sup_n sigma_n^2 < infinity`,

we have

`T_{d_n}/(d_n/delta_n) -> 1`

in probability.

### Proof

Since

`E[T_d]/H(d,delta) = (1+d/delta)/(d/delta)=1+delta/d`,

Chebyshev and Proposition 1 give

`P( | T_d/H - E[T_d]/H | >= a )`

`<= Var(T_d)/(a^2 H^2)`

`= sigma^2/(a^2 d delta)`.

If `d_n delta_n -> infinity` and `sigma_n^2` is bounded, the right side tends to zero. Also `delta_n/d_n -> 0` because `d_n delta_n -> infinity` and `delta_n ->0` imply `d_n -> infinity`. Hence the centering tends to 1. QED.

## Corollary — the source hub-dominant regime automatically self-averages in the branching surrogate

For the P0157 barely-subcritical source problem, write

`delta_n = 1-nu_n > 0`,

`H_n = d_max/delta_n`,

`E_n = delta_n^{-2} log(n delta_n^3)`,

and suppose `n delta_n^3 -> infinity`.

Their exact scale ratio is

`R_n := H_n/E_n = d_max delta_n / log(n delta_n^3)`.

Assume the finite-third-moment hypotheses keep the forward-offspring variances `sigma_n^2` bounded. If the candidate hub scale dominates in the strong sense

`R_n -> infinity`,

then `log(n delta_n^3)->infinity`, and therefore

`d_max delta_n = R_n log(n delta_n^3) -> infinity`.

Proposition 2 yields

`T_{d_max}/H_n -> 1`

in probability in the ideal independent branching-process surrogate.

Thus the high-degree candidate scale is not merely an expectation in precisely the source regime where it dominates the Erdos–Renyi candidate scale: it is self-averaging in the canonical local surrogate.

## What this does and does not prove

This closes the specific gap in the old P0157 intake attempt, which had only the expectation `1+d/delta` and correctly noted that expectation alone does not give a high-probability statement.

It does **not** prove the configuration-model largest-component theorem. The remaining graph-level obligations include at least:

1. couple the exploration from the maximal-degree vertex to the independent branching surrogate uniformly up to size `d_max/delta_n` in the relevant regime;
2. control collisions/depletion and dependence among the `d_max` branches;
3. prove the corresponding lower bound for the maximal-degree component and a matching upper bound over all components;
4. in the `R_n -> 0` regime, recover the Erdos–Renyi extreme scale `E_n` under the source's general finite-third-moment degree assumptions;
5. understand the transition when `R_n` is order one.

The calculation is theorem-sized and fully proved above; it requires no finite exhaustive checker.