# P0157 — absorbing hub kernel and an actual-configuration-model no-merger criterion

**Scope.** This is a HARD7-04 route result for the barely-subcritical finite-third-moment configuration model. It does **not** solve van der Hofstad's full subcritical crossover problem and it does **not** claim novelty. The first theorem identifies the rank-one connection kernel in an ideal absorbing branching surrogate. The second theorem is graph-level: it gives a sufficient upper-tail condition under which no component contains two selected high-degree vertices. Together they replace the refuted scalar `d_max/(1-nu)`-only route by an upper-tail interaction statistic.

Throughout let

\[
\ell=\sum_{v=1}^n d_v,\qquad
\nu=\frac{\sum_v d_v(d_v-1)}{\ell},\qquad
\delta=1-\nu>0,
\]

and assume

\[
\ell\ge cn,\qquad \sum_v d_v^3\le Cn,
\qquad \delta\to0,\qquad n\delta^3\to\infty.
\tag{1}
\]

Let `H` be any deterministic set of marked vertices, put `B=[n]\\H`, and define

\[
S_H:=\sum_{h\in H}d_h,
\qquad
A_H:=\sum_{\{i,j\}\subset H}d_i d_j,
\tag{2}
\]

and the **absorbing bulk deficit**

\[
\delta_H
:=1-\frac1\ell\sum_{v\in B}d_v(d_v-1)
=\delta+\frac1\ell\sum_{h\in H}d_h(d_h-1).
\tag{3}
\]

In particular `delta_H>=delta`.

## 1. Two source-scale consequences used below

Write `d_max=max_v d_v`. From (1),

\[
d_{\max}\le (Cn)^{1/3}.
\]

Since `n delta^3 -> infinity`, equivalently `n^{1/3}delta -> infinity`,

\[
\frac{d_{\max}}{\ell\delta^2}=o(1),
\qquad
\frac{d_{\max}^2}{\ell\delta}=o(1).
\tag{4}
\]

Because `delta_H>=delta`, the same statements hold after replacing `delta` in the denominators by `delta_H`.

## 2. The exact absorbing branching surrogate

Fix two distinct marked vertices `i,j in H`. Consider the following with-replacement branching process started from one half-edge of `i`.

At each particle, independently sample one vertex-label/absorbing type from the size-biased half-edge law:

- hit `j` with probability `d_j/ell`; this is a success and produces no children;
- hit another marked half-edge with probability `(S_H-d_j)/ell`; this produces no children and is not a success;
- hit `v in B` with probability `d_v/ell`; this produces `d_v-1` children.

Its mean offspring number is

\[
\frac1\ell\sum_{v\in B}d_v(d_v-1)=1-\delta_H<1,
\]

so it dies out almost surely. Let `x_j` be the probability that one initial particle eventually hits `j`.

### Proposition 2.1 — exact fixed point and first-order kernel

`x_j` is the unique solution in `[0,1]` of

\[
x_j
=\frac{d_j}{\ell}
 +\frac1\ell\sum_{v\in B}d_v\{1-(1-x_j)^{d_v-1}\}.
\tag{5}
\]

Moreover, uniformly in `j in H`,

\[
\boxed{
 x_j=\frac{d_j}{\ell\delta_H}(1+o(1)).
}
\tag{6}
\]

If the `d_i` initial half-edges of root `i` are taken independent in this ideal surrogate, then the probability `p^BP_{ij}` that at least one line hits `j` satisfies uniformly in distinct `i,j in H`

\[
\boxed{
 p^{\rm BP}_{ij}
 =\frac{d_i d_j}{\ell\delta_H}(1+o(1)).
}
\tag{7}
\]

Thus the first-order induced hub kernel is rank one:

\[
\kappa_{ij}=\frac{d_i d_j}{\ell\delta_H}.
\tag{8}
\]

### Proof

Let `q_j=1-x_j` be the no-hit probability. Conditioning on the first sampled type gives

\[
q_j=\frac{S_H-d_j}{\ell}
 +\frac1\ell\sum_{v\in B}d_v q_j^{d_v-1},
\]

which is (5). Subcriticality gives the minimal fixed point and uniqueness for the success probability.

For every integer `r>=0` and `x in [0,1]`,

\[
rx-\binom r2x^2\le1-(1-x)^r\le rx.
\tag{9}
\]

Applying the upper inequality in (5) yields

\[
\delta_H x_j\le \frac{d_j}{\ell}.
\tag{10}
\]

Put

\[
\beta_H:=\frac1\ell\sum_{v\in B}d_v(d_v-1)(d_v-2).
\]

The lower inequality in (9) gives

\[
\delta_H x_j
\ge \frac{d_j}{\ell}-\frac{\beta_H}{2}x_j^2.
\tag{11}
\]

By (1), `beta_H=O(1)`. Substituting (10) into the error term gives

\[
\frac{d_j}{\ell\delta_H}
\left(1-O\!\left(\frac{d_j}{\ell\delta_H^2}\right)\right)
\le x_j\le
\frac{d_j}{\ell\delta_H}.
\tag{12}
\]

Equation (4) and `delta_H>=delta` make the relative error uniform and prove (6).

Finally

\[
p^{\rm BP}_{ij}=1-(1-x_j)^{d_i}.
\]

Uniformly,

\[
d_i x_j\le \frac{d_{\max}^2}{\ell\delta_H}=o(1)
\]

by (4), so `1-(1-x_j)^{d_i}=d_i x_j(1+o(1))`, proving (7). `square`

**Interpretation.** The extra factor `1/delta_H` relative to a direct configuration-model edge is the expected length amplification of a subcritical bulk exploration before absorption. Equation (7) is proved only for the ideal independent-with-replacement surrogate; it is not silently promoted to an asymptotic independence theorem for the actual configuration model.

## 3. A graph-level upper bound for mergers among marked hubs

Let `CM(d)` be the actual configuration-model multigraph. Let

\[
\mathcal M_H:=\{\text{some connected component of }CM(d)
\text{ contains at least two vertices of }H\}.
\]

### Theorem 3.1 — actual CM no-merger bound

Under (1), for all sufficiently large `n`,

\[
\boxed{
\mathbb P(\mathcal M_H)
\le
\frac{4A_H}{3\ell\delta_H}
+\frac{32S_H}{\ell\delta^2}.
}
\tag{13}
\]

Consequently, if

\[
\frac{A_H}{\ell\delta_H}\to0,
\qquad
\frac{S_H}{\ell\delta^2}\to0,
\tag{14}
\]

then with high probability every component contains at most one vertex of `H`.

### Proof

Set

\[
R:=\left\lfloor\frac{\ell\delta}{8}\right\rfloor.
\tag{15}
\]

Since `ell delta -> infinity`, eventually

\[
\frac{\ell\delta}{16}\le R\le\frac{\ell\delta}{8}.
\tag{16}
\]

If two marked vertices are connected, choose a shortest path between a pair of marked vertices. Its internal vertices lie in `B`; otherwise an internal marked vertex would give a shorter marked-to-marked subpath.

Let `N_r` be the number of simple marked-to-marked paths of length `r` whose internal vertices lie in `B`, with each unordered endpoint pair oriented canonically. For a fixed sequence of distinct internal vertices, the usual configuration-model pairing calculation gives

\[
\mathbb E N_r
\le
\frac{A_H\left(\sum_{v\in B}d_v(d_v-1)\right)^{r-1}}
{(\ell-1)(\ell-3)\cdots(\ell-(2r-1))}.
\tag{17}
\]

For `r<=R`, every denominator factor is at least

\[
\ell-2R\ge \ell(1-\delta/4).
\]

Using `sum_{B}d_v(d_v-1)=ell(1-delta_H)`,

\[
\sum_{r=1}^{R}\mathbb E N_r
\le
\frac{A_H}{\ell(1-\delta/4)}
\sum_{r\ge1}
\left(\frac{1-\delta_H}{1-\delta/4}\right)^{r-1}
=
\frac{A_H}{\ell(\delta_H-\delta/4)}
\le \frac{4A_H}{3\ell\delta_H}.
\tag{18}
\]

It remains to control a marked-to-marked path longer than `R`. Explore the component of a fixed marked root `h`. Let `A_t` be the active-half-edge count and `tau_h` its extinction time in pairing steps. Exactly as in the active-half-edge calculation used in the earlier HARD7-04 maximal-root theorem,

\[
b_t:=\mathbb E[A_{t+1}-A_t\mid\mathcal F_t]
=\frac{\sum_{v\in U_t}d_v(d_v-2)-2(A_t-1)}{\ell-2t-1}.
\tag{19}
\]

Since `sum_v d_v(d_v-2)=-ell delta` and `d(d-2)>=-1` for every integer degree `d>=1`, before extinction

\[
\sum_{v\in U_t}d_v(d_v-2)-2(A_t-1)
\le -\ell\delta+t+1.
\tag{20}
\]

For `t<=ell delta/4` and large `n`, (20) implies

\[
b_t\le-\delta/2.
\tag{21}
\]

Stop at `S=tau_h wedge R`. Since `R<=ell delta/8`, summing (21) and using `A_S>=0` gives

\[
\mathbb E S\le \frac{2d_h}{\delta}.
\tag{22}
\]

By (16),

\[
\mathbb P(\tau_h>R)
\le\frac{\mathbb E S}{R}
\le\frac{32d_h}{\ell\delta^2}.
\tag{23}
\]

If the shortest marked-to-marked path has length greater than `R`, then the exploration from either endpoint lasts more than `R` pairing steps. A union bound over `h in H` and (23) costs at most `32S_H/(ell delta^2)`. Combining this with Markov's inequality applied to the path count in (18) proves (13). `square`

## 4. What the new variables say on the previous multi-hub stress family

For the explicit family from the preceding HARD7-04 run,

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

with `M` hubs of degree `d`, `ell~12m^12`, and `delta~m^{-1}`. Taking `H` to be all hubs,

\[
S_H=Md=m^7,
\qquad
A_H=\binom M2d^2\sim\frac12m^{14},
\tag{24}
\]

and

\[
\delta_H
=\delta+\frac{Md(d-1)}{\ell}
\sim m^{-1}.
\tag{25}
\]

The two natural rank-one diagnostics are therefore

\[
\Lambda_H:=\frac{A_H}{\ell\delta_H}
\sim \frac{m^3}{24}\to\infty,
\tag{26}
\]

and

\[
\rho_H:=\frac{\sum_{h\in H}d_h^2}{\ell\delta_H}
\sim\frac1{12m^2}\to0.
\tag{27}
\]

So the stress family lies in a genuinely non-scalar boundary regime:

- the expected **global number** of hub-hub contacts in the branching-kernel picture diverges (`Lambda_H -> infinity`);
- the expected contact degree of any **fixed** comparable hub vanishes (`rho_H ->0`).

This is exactly compatible with the previous run's phenomenon: a preselected hub is asymptotically isolated, yet somewhere among `m^5` hubs mergers occur with high probability.

For equal hubs the branching-kernel edge scale is

\[
p_m\sim\frac{d^2}{\ell\delta_H}\sim\frac1{12m^7}.
\tag{28}
\]

If one temporarily replaces the true dependent hub graph by the independent rank-one surrogate, the first-moment tree hierarchy is

\[
M^k p_m^{k-1}\asymp m^{7-2k}.
\tag{29}
\]

Thus pairs occur on scale `m^3`, three-hub trees on scale `m`, while four-hub trees already have scale `m^{-1}`. This **does not prove** that the actual largest configuration-model component contains exactly three hubs; it identifies a sharp next finite-order target for a coupling/second-moment argument.

## 5. Consequence for the source route

The source's suggested subcritical transition cannot be parameterized by the two scalar quantities `d_max` and `delta` alone under the full finite-third-moment hypotheses. A viable theorem has to retain at least some upper-tail profile information. The quantities

\[
\Lambda_H=\frac{A_H}{\ell\delta_H},
\qquad
\rho_H=\frac{\sum_{h\in H}d_h^2}{\ell\delta_H}
\tag{30}
\]

are concrete candidates:

- Theorem 3.1 rigorously certifies one no-merger regime from the marked tail mass.
- Proposition 2.1 derives the corresponding rank-one interaction kernel in the ideal branching limit.
- The stress family shows that `Lambda_H -> infinity` and `rho_H ->0` can coexist, so global multiplicity and local spectral intensity are different axes of the crossover.

The remaining hard step is a **two-sided actual-graph approximation** to the hub kernel on a tail set `H=H_n`, strong enough to transfer component-size information from the rank-one marked graph back to the configuration model. Neither independence nor a lower connection bound is proved here.

## 6. Verification status

Both results are theorem-sized asymptotic arguments written on the page. There is no finite exhaustive claim and therefore no checker artifact is manufactured for this run. The path-count identity, the negative-drift estimate, and the branching fixed-point bounds are elementary exact calculations. This note is a **self-check / PARTIAL route result**, not an independent audit and not source closure.
