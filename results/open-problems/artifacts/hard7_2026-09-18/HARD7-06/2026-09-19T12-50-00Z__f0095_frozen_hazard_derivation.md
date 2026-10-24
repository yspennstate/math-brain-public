# HARD7-06 / F0095 — frozen-pair hazard transport derivation

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

This note records the mathematical idea **before** any new checker is added. Novelty is not asserted. A bounded literature search located Culberson--Gent (2001), who explicitly study globally frozen pairs / frozen development in graph 3-colouring; the identities below are derived independently here and require a separate novelty review before any publication claim.

## Setup

Fix `n`, put

\[
N=\binom n2,
\]

and let `\mathcal C_m` be the set of labelled 3-colourable graphs on `[n]` with exactly `m` edges. Write

\[
a_m=|\mathcal C_m|,
\qquad
p_m=\frac{a_m}{\binom Nm}.
\]

For `G in \mathcal C_m`, let `Col(G)` be its set of proper 3-colourings and define

\[
u\sim_G v
\quad\Longleftrightarrow\quad
\sigma(u)=\sigma(v)\ \text{for every }\sigma\in Col(G).
\]

This is an equivalence relation. If its classes have sizes `c_1,...,c_r`, define

\[
D(G):=\sum_{i=1}^r\binom{c_i}{2}.
\tag{1}
\]

Every `\sim_G`-class is an independent set: if `uv in E(G)`, every proper colouring has `sigma(u) != sigma(v)`. Hence every pair counted by `D(G)` is a missing edge.

## Exact unsafe-edge interpretation

For a missing edge `e={u,v}`, the graph `G+e` is non-3-colourable iff every proper colouring of `G` gives `u` and `v` the same colour, i.e. iff `u~_G v`. Therefore

\[
\boxed{D(G)=\#\{e\notin E(G):G+e\text{ is not 3-colourable}\}.}
\tag{2}
\]

Thus the number of safe missing edges is

\[
S(G)=N-m-D(G).
\tag{3}
\]

Let

\[
A_m:=N-m,
\qquad
\mu_m:=\mathbb E_m D(G),
\]

where `E_m` is uniform expectation on `\mathcal C_m`.

Double count safe incidences `(G,e)` with `G in \mathcal C_m`, `e notin E(G)`, and `G+e in \mathcal C_{m+1}`. On the lower side their number is `sum_G S(G)`. On the upper side each `H in \mathcal C_{m+1}` has exactly `m+1` edge-deletion predecessors, all 3-colourable. Hence

\[
\sum_{G\in\mathcal C_m} S(G)=(m+1)a_{m+1}.
\tag{4}
\]

Using `\binom N{m+1}/\binom Nm=A_m/(m+1)`, (4) gives

\[
\boxed{
\frac{p_{m+1}}{p_m}
=1-\frac{\mu_m}{A_m}.}
\tag{5}
\]

Consequently the exact next-edge failure probability, conditioned on 3-colourability at layer `m`, is

\[
\boxed{r_m:=1-\frac{p_{m+1}}{p_m}=\frac{\mu_m}{A_m}.}
\tag{6}
\]

This turns the generic safe-edge hazard of the previous run into an exact statistic of the global frozen partition.

For every `t>=1` with the layers nonempty,

\[
\boxed{
-\log\frac{p_{m+t}}{p_m}
=\sum_{j=m}^{m+t-1}-\log(1-r_j).}
\tag{7}
\]

In particular, a linear sprinkling interval has exponential loss exactly when it accumulates linear logarithmic frozen-pair hazard. Since `-log(1-r)>=r`, a uniform positive lower bound on the average `r_j` over `Theta(n)` successive layers is sufficient.

## Monotone coarsening

If `G subset H` and `H` is 3-colourable, then `Col(H) subset Col(G)`. Thus

\[
u\sim_G v\implies u\sim_H v.
\]

The frozen partition can only coarsen under safe edge additions, and therefore

\[
\boxed{D(H)\ge D(G).}
\tag{8}
\]

This is a genuine monovariant, but by itself it does not imply that the layer-average hazard `r_m` is increasing, because conditioning on survival size-biases toward states with many safe extensions.

## Exact safe-incidence transport identity

Let `\nu_m` be the uniform law on safe incidences `(G,e)` from layer `m`, and put `H=G+e`. Then:

1. the `H`-marginal is uniform on `\mathcal C_{m+1}`, because each `H` has exactly `m+1` deletion predecessors;
2. the `G`-marginal is the uniform layer law size-biased by `S(G)=A_m-D(G)`.

Let

\[
v_m:=\operatorname{Var}_m(D),
\qquad
J_m:=\mathbb E_{\nu_m}[D(H)-D(G)]\ge0.
\tag{9}
\]

The size-biased lower expectation is

\[
\mathbb E_{\nu_m}D(G)
=\frac{\mathbb E_m[D(A_m-D)]}{A_m-\mu_m}
=\mu_m-\frac{v_m}{A_m-\mu_m}.
\tag{10}
\]

The upper marginal is uniform, so

\[
\boxed{
\mu_{m+1}
=\mu_m-\frac{v_m}{A_m-\mu_m}+J_m.}
\tag{11}
\]

Equation (11) isolates the two competing mechanisms exactly:

- `J_m`: actual coarsening of the frozen partition, which raises the hazard;
- `v_m/(A_m-\mu_m)`: survivor size-bias toward graphs with smaller `D`, which lowers the next layer average.

Using `r_m=\mu_m/A_m` and `A_{m+1}=A_m-1`, simple algebra gives

\[
\boxed{
r_{m+1}-r_m
=\frac{
J_m+\mu_m/A_m-v_m/(A_m-\mu_m)
}{A_m-1}.}
\tag{12}
\]

Therefore the discrete-IFR / rank-log-concavity inequality at this transition is equivalent to the exact condition

\[
\boxed{
J_m\ge \frac{v_m}{A_m-\mu_m}-\frac{\mu_m}{A_m}.}
\tag{13}
\]

A sufficient condition is

\[
\boxed{
v_m\le \frac{\mu_m(A_m-\mu_m)}{A_m},}
\tag{14}
\]

because `J_m>=0`. This also explains why monotone coarsening alone cannot prove IFR: variance-induced survivor bias can oppose it.

## Source-level route suggested by the identity

The previous HARD7-06 run reduced the fixed-`q=3` constant-location conjecture to convergence of the normalized stopping-time mean and isolated a missing exponential sprinkling mechanism. Equations (5)--(7) identify the exact local statistic that would supply such a mechanism:

> prove, in the uniform `m`-edge random graph conditioned on 3-colourability and in the source-relevant near-threshold regime, a positive linear-window lower bound on the **global frozen-pair density** `r_m=E[D]/(N-m)` (or directly on its logarithmic version).

This is stronger and structurally different from showing that a typical solution has many variables frozen inside one solution cluster. The relation `~_G` quantifies equality in **every** legal colouring of the graph.

## Prior-art caution

Culberson and Gent, *Frozen development in graph coloring*, Theoretical Computer Science 265 (2001), 227--264, DOI `10.1016/S0304-3975(01)00164-5`, explicitly define globally frozen vertex pairs and study graph collapse under frozen development, including empirical 3-colouring threshold behaviour. Hence the global-frozen-pair viewpoint itself is prior art, not a novelty claim.

Molloy, *The freezing threshold for k-colourings of a random graph*, STOC 2012, gives a rigorous freezing threshold for a cluster/local-reconfiguration notion of frozen variables. That is highly relevant but not identical to the global equivalence relation above; no implication sufficient for (7) is asserted here.

A bounded 2026-09-19 search did not locate the exact layer-incidence transport formula (11)--(13), but absence from a bounded search is not novelty evidence. Treat these identities as **newly derived in this repository, novelty UNVERIFIED**.
