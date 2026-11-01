# Consequences of the C30 compensated clade-count martingale

This is an additive artifact to the immutable first C30 run report. It does not replace or edit that report.

Let, for fixed `r>=2`,

`M_r(N)=N_r(T_N)-A_r(N)`,

where

`A_r(N):=sum_{n=1}^{N-1} G_r(T_n)`

and `G_r` is the explicit predictable drift derived in the run report.

## 1. The martingale error is sublinear almost surely

For every hit clade `C`, the one-step count change `d_r(T,C)` lies in `{-1,0,1}`. Hence `G_r(T)`, being a convex combination of the `d_r(T,C)`, lies in `[-1,1]`. Therefore every martingale increment satisfies

`|Delta M_r|=|d_r-G_r|<=2`.

Azuma-Hoeffding gives, for every `x>0`,

`P(|M_r(N)|>=x) <= 2 exp(-x^2/(8(N-1)))`.

Taking `x=epsilon N` and summing over `N` gives a finite series for every fixed `epsilon>0`. Borel-Cantelli therefore yields

`M_r(N)/N -> 0` almost surely.

Equivalently,

`N_r(T_N)/N - A_r(N)/N -> 0` almost surely.      (C30-LLN-reduction)

Thus the explicit compensator captures the complete linear-order behavior of the final fixed-size clade count; the martingale noise is sublinear without any mixing assumption.

A slightly sharper direct corollary is that for every constant `C>sqrt(8)`,

`|M_r(N)| <= C sqrt(N log N)`

eventually almost surely, by applying the same bound with `x=C sqrt(N log N)` and Borel-Cantelli.

## 2. Exact first-order mean of the compensator

The source overview defines the occupation probability `a(N,r)` and proves

`E[N_r(T_N)] = N a(N,r)/r`

and, for fixed `r>=2`,

`a(N,r) -> a(r) = 6 h_{r-1}/(pi^2 (r-1))`.

Since `M_r` starts at zero and has mean zero,

`E[A_r(N)] = E[N_r(T_N)]`.

Consequently

`E[A_r(N)]/N -> a(r)/r
 = 6 h_{r-1}/(pi^2 r(r-1)).`       (C30-MEAN-COMPENSATOR)

For example the limiting mean compensator per growth step is `3/pi^2` for 2-clades.

These two statements give a concrete usefulness criterion for the martingale: proving a law of large numbers (or fluctuation limit) for the explicit predictable quantity `A_r(N)` immediately transfers to the actual final clade count `N_r(T_N)`, while the source already supplies the exact target first-order mean. The remaining nontrivial work is therefore to control the random compensator and the predictable bracket, rather than the martingale noise itself.

Source for the occupation formula and limit: Aldous–Janson, arXiv:2303.02529v3, equations (50)–(54), https://arxiv.org/html/2303.02529v3 .
