# P0157 — growing integer-staircase obstruction in the barely-subcritical configuration model

**Status.** Theorem-sized R14 self-check / PARTIAL progress on the source problem. This note proves a new explicit family theorem inside the source's finite-third-moment barely-subcritical configuration-model regime. It does **not** claim that van der Hofstad's full crossover question is solved or refuted as phrased, and it makes no novelty claim beyond the bounded literature search recorded in the accompanying run report.

## 1. Statement

Let `m -> infinity` through even integers and put

\[
K=K_m:=\left\lfloor\sqrt{\frac{\log m}{\log\log m}}\right\rfloor,
\]

for all sufficiently large `m` so that `K>=2`. Define

\[
n=8m^{2K+6},\qquad M=m^{2K-1},\qquad d=m^2,
\]

and

\[
x=3m^{2K+5}+\frac{M}{4}(d-1)^2.
\]

Since `m` is even, `x` is an integer. Let the deterministic degree sequence contain

\[
N_d=M,\qquad N_3=2m^{2K+6}-x,\qquad N_1=6m^{2K+6}+x-M
\tag{1.1}
\]

vertices of degrees `d,3,1`, respectively. Call the degree-`d` vertices **hubs**. Let `CM_m` be the corresponding configuration model and `L_1=L_1(CM_m)` its largest component size.

Let

\[
\nu_m=\frac{\sum_vd_v(d_v-1)}{\sum_vd_v},\qquad
\delta_m=1-\nu_m>0,
\]

and define

\[
H_m:=\frac d{\delta_m},\qquad
E_m:=\delta_m^{-2}\log(n\delta_m^3).
\]

Let `xi_m=D_m^*-1` be the usual size-biased forward offspring variable and

\[
Q_m:=\frac{\operatorname{Var}(\xi_m)}{d\delta_m}.
\]

### Theorem 1 — growing staircase

For the family (1.1),

\[
\boxed{\frac{L_1}{K_mH_m}\xrightarrow{\mathbb P}1.}
\tag{1.2}
\]

Moreover,

\[
\boxed{\frac{H_m}{E_m}\to\infty,\qquad
Q_m=\frac1m-\frac{5}{12m^2}+O(m^{-3})\to0,\qquad
\frac{L_1}{H_m}\xrightarrow{\mathbb P}\infty.}
\tag{1.3}
\]

In fact, if `H_max` denotes the largest number of designated hubs lying in one connected component, then

\[
\boxed{\mathbb P(H_{\max}=K_m)\to1.}
\tag{1.4}
\]

Thus the previous fixed coefficient-three stress family is one point on an **unbounded integer staircase**: under the same limiting degree law, the same `delta_m~m^{-1}`, the same vanishing local fluctuation ratio `Q_m~m^{-1}`, and still `H_m/E_m->infinity`, the ratio `L_1/H_m` can diverge.

This is a certified obstruction to any route that tries to decide the source's high-degree side using only `H_m/E_m` and the one-root fluctuation scalar `Q_m`. It does not, by itself, determine the correct full source theorem, which may require an upper-tail point process / connectivity functional in addition to the two classical scales.

## 2. Exact source-regime checks

The total degree is

\[
\ell=N_1+3N_3+dM.
\]

Substituting (1.1) gives the exact factorization

\[
\boxed{
\ell=\frac{m^{2K-1}}2
\left(24m^7-12m^6-m^4+4m^2-3\right).
}
\tag{2.1}
\]

Also

\[
\sum_v d_v(d_v-1)=6N_3+d(d-1)M,
\]

and a direct cancellation gives

\[
\boxed{
\ell-\sum_vd_v(d_v-1)=12m^{2K+5}.
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\delta_m=
\frac{24m^6}{24m^7-12m^6-m^4+4m^2-3}
=\frac1m\left(1+O(m^{-1})\right),
}
\tag{2.3}
\]

which is independent of `K` after cancellation. In particular

\[
n\delta_m^3\asymp m^{2K+3}\to\infty.
\tag{2.4}
\]

The empirical degree distribution converges to

\[
\mathbb P(D=1)=\frac34,\qquad \mathbb P(D=3)=\frac14,
\tag{2.5}
\]

because `M/n=1/(8m^7)` and `x/n=O(m^{-1})`. The third moments converge as well: the hub contribution is exactly

\[
\frac{Md^3}{n}=\frac1{8m}\to0,
\tag{2.6}
\]

while the degree-1/3 bulk tends to `15/2`. Thus this family stays in the finite-third-moment configuration-model regime used by the source.

Since

\[
H_m\asymp m^3,
\]

while

\[
\log(n\delta_m^3)
=(2K+3+o(1))\log m,
\]

we have

\[
\frac{H_m}{E_m}
=\frac{d\delta_m}{\log(n\delta_m^3)}
\sim \frac{m}{(2K+3)\log m}\to\infty,
\tag{2.7}
\]

because `K=O(sqrt(log m/log log m))`.

For the local branching variance,

\[
\mathbb E\xi_m^2
=\frac{12N_3+d(d-1)^2M}{\ell}.
\]

After cancelling the common factor `m^{2K-1}`, one obtains an exact rational function of `m` alone. Writing

\[
P(m)=24m^7-12m^6-m^4+4m^2-3,
\]

the exact expression for `Q_m` is

\[
Q_m=
\frac{
576m^{14}-528m^{13}-456m^{12}-240m^{11}+118m^{10}
+336m^9-151m^8-144m^7+20m^6+70m^4-42m^2+9
}{24m^8P(m)}.
\tag{2.8}
\]

Hence

\[
\boxed{Q_m=m^{-1}-\frac5{12}m^{-2}-m^{-3}+O(m^{-4}).}
\tag{2.9}
\]

The accompanying exact checker verifies (2.1), (2.2), the `K`-independence of (2.8), and the exponent identities used below over a finite sanity grid. The asymptotic proof is the algebra above, not the checker.

## 3. Why the hub threshold is `K`: the rank-one exponent

The degree-three bulk has one-step nonbacktracking weight

\[
a_m:=\frac{6N_3}{\ell}.
\]

Since

\[
1-a_m
=\delta_m+\frac{Md(d-1)}\ell
=\frac1m+O(m^{-2}),
\tag{3.1}
\]

we have

\[
a_m^m\to e^{-1},\qquad a_m^{2m}\to e^{-2}.
\tag{3.2}
\]

The first-order connection scale between two prescribed hubs through a degree-three chain is

\[
\frac{d^2}{\ell(1-a_m)}
=\Theta\!\left(m^{-(2K+1)}\right).
\tag{3.3}
\]

With `M=m^{2K-1}` hubs, the first-moment scale for a fixed `r`-hub tree is therefore

\[
M^r\left(\frac{d^2}{\ell(1-a_m)}\right)^{r-1}
=\Theta\!\left(m^{2K+1-2r}ight).
\tag{3.4}
\]

Thus `r=K` has scale `m`, while `r=K+1` has scale `m^{-1}`. The rest of the proof makes this moving-threshold heuristic rigorous despite `K=K_m->infinity`.

The choice

\[
K=\left\lfloor\sqrt{\frac{\log m}{\log\log m}}\right\rfloor
\tag{3.5}
\]

is deliberately very slow. It gives

\[
K\log K=o(\log m),\qquad K\log m=o(m),
\tag{3.6}
\]

which absorbs every finite-core topology factor and every polynomial union bound below.

## 4. Lower bound: a good `K`-hub path exists with high probability

A **path witness** consists of an ordered tuple of `K` distinct hubs `(h_1,...,h_K)` and, for every `j<K`, a simple path from `h_j` to `h_{j+1}` of length

\[
r_j\in[m,2m],
\]

such that the `K-1` paths are internally vertex-disjoint, all their internal vertices have ambient degree three, and no internal path vertex is a hub. We only prescribe the path-pairing edges; the unused third half-edge of every degree-three path vertex remains free.

Put

\[
R=\sum_{j=1}^{K-1}r_j,
\qquad q=R-(K-1).
\]

For a uniform perfect matching, the exact expectation of the witness count `Z_K` is

\[
\mathbb EZ_K
=(M)_K d^K(d-1)^{K-2}
\sum_{r_1,...,r_{K-1}=m}^{2m}
\frac{(N_3)_q6^q}{D_R},
\tag{4.1}
\]

where

\[
D_R=(\ell-1)(\ell-3)\cdots(\ell-(2R-1)).
\]

Because `R=O(Km)`, (3.6) and the enormous bulk size imply uniformly over the summation range

\[
\frac{(M)_K}{M^K}=1+o(1),
\quad
\frac{(N_3)_q}{N_3^q}=1+o(1),
\quad
\frac{\ell^R}{D_R}=1+o(1),
\quad
\frac{(d-1)^{K-2}}{d^{K-2}}=1+o(1).
\tag{4.2}
\]

Therefore (4.1) factorizes asymptotically:

\[
\mathbb EZ_K
=(1+o(1))
\frac{M^Kd^{2K-2}}{\ell^{K-1}}
\left(\sum_{r=m}^{2m}a_m^{r-1}\right)^{K-1}.
\tag{4.3}
\]

By (3.1)-(3.2),

\[
\frac1m\sum_{r=m}^{2m}a_m^{r-1}
\longrightarrow e^{-1}-e^{-2}.
\]

Hence, with

\[
c_*:=\frac{e^{-1}-e^{-2}}{12}\in(0,1),
\]

we obtain

\[
\boxed{
\mathbb EZ_K=(1+o(1))m\,c_*^{K-1}.
}
\tag{4.4}
\]

Since `K=o(log m)`, the right side tends to infinity.

### 4.1 A prescribed witness is good with probability `1-o(1)`

Call a witness **good** when its host component is a tree and contains exactly its `K` prescribed hubs.

Condition on all path edges of one witness. Its residual active queue has size

\[
A_0=Kd+O(Km)=O(Km^2).
\]

Until another hub is found, the residual bulk exploration has negative drift of order `delta_m`, so the usual stopped active-queue estimate gives expected residual pairing time

\[
O(A_0/\delta_m)=O(Km^3).
\tag{4.5}
\]

At each pairing the hazard of hitting one of the other hubs is at most

\[
\frac{2Md}{\ell}=O(m^{-5}).
\]

Thus the conditional probability of acquiring an extra hub is

\[
O(Km^{-2})=o(1).
\tag{4.6}
\]

The square-queue drift estimate gives expected active-area `O(K^2m^5)`; divided by `ell` this makes the residual collision/cycle probability `o(1)`, uniformly in the witness. Hence

\[
\mathbb E Z_K^{g}=(1-o(1))\mathbb EZ_K,
\tag{4.7}
\]

where `Z_K^g` counts good witnesses.

### 4.2 Second moment without an overlap taxonomy

Let `D_K^0` count ordered pairs of path-witness skeletons using disjoint hub sets and disjoint internal degree-three vertices. The same exact pairing-factor ratio as in the fixed-three-hub calculation yields, uniformly because `K^2/M`, `(Km)^2/N_3`, and `(Km)^2/ell` all vanish,

\[
\boxed{
\mathbb ED_K^0=(1+o(1))(\mathbb EZ_K)^2.
}
\tag{4.8}
\]

A good host is a tree with exactly `K` hubs. If it contains one of the path witnesses above, the unique minimal subtree joining those hubs is a path, so the host contributes at most the two orientations of that same path. Therefore pointwise

\[
(Z_K^g)^2\le 2Z_K^g+D_K^0.
\tag{4.9}
\]

Combining (4.4), (4.7), (4.8), and (4.9),

\[
\frac{\mathbb E[(Z_K^g)^2]}{(\mathbb EZ_K^g)^2}\to1.
\]

Paley-Zygmund gives

\[
\boxed{\mathbb P(Z_K^g>0)\to1.}
\tag{4.10}
\]

Thus with high probability some component contains at least `K` hubs.

## 5. Upper bound: no component contains `K+1` hubs

Set `r=K+1`. If a component contains at least `r` hubs, take a spanning tree of that component, form the minimal subtree containing all its hubs, and repeatedly prune a marked leaf and its incident branch until exactly `r` marked hubs remain. The resulting tree contains exactly `r` hubs and no other hubs.

Suppress every ordinary degree-three vertex of relative degree two. The resulting finite **core** has

- `r` labeled hub vertices;
- `t` ordinary branch vertices of relative degree three, where `0<=t<=r-2`;
- `e=r+t-1` core edges.

The number of labeled core topologies is at most

\[
(r+t)^{r+t-2}=\exp(O(K\log K)).
\tag{5.1}
\]

by Cayley's bound.

First restrict every expanded core edge to fewer than `m^2` internal degree-three vertices. Uniformly over all such expansions, finite-population corrections are `1+o(1)`. Summing the geometric chain lengths gives at most `C/[ell(1-a_m)]` for each core edge. The sum of hub core degrees is

\[
2e-3t=2r-t-2.
\]

Consequently the expected number of such `r`-hub Steiner trees with `t` ordinary branch vertices is bounded by

\[
\exp(O(K\log K))
\frac{M^rN_3^t d^{2r-t-2}6^t}
{\{\ell(1-a_m)\}^{r+t-1}}.
\tag{5.2}
\]

Since `6N_3/ell=1+o(1)` and `d(1-a_m)~m`, this is

\[
\exp(O(K\log K))
\left[
M^r\left(\frac{d^2}{\ell(1-a_m)}\right)^{r-1}
\right]
O((d(1-a_m))^{-t}).
\tag{5.3}
\]

At `r=K+1`, (3.4) makes the bracket `Theta(m^{-1})`; each branch vertex contributes another `O(m^{-1})`. Since `K log K=o(log m)`, summing `0<=t<=K-1` gives

\[
\mathbb E\{\text{short-edge Steiner cores containing }K+1\text{ hubs}\}
=m^{-1+o(1)}\to0.
\tag{5.4}
\]

It remains only to justify the `m^2` edge-length cutoff. A core edge longer than `m^2` contains a simple path with at least `m^2` consecutive ambient degree-three vertices. The expected number of oriented degree-three paths of that length anywhere in the configuration model is at most

\[
\ell\,\{a_m(1+o(1))\}^{m^2}
\le \exp\{O(K\log m)-c m\}=o(1),
\tag{5.5}
\]

using (3.1) and `K log m=o(m)`. Therefore (5.4) covers all relevant core edges with probability `1-o(1)`.

Markov's inequality now gives

\[
\boxed{\mathbb P(H_{\max}\ge K+1)\to0.}
\tag{5.6}
\]

Together with (4.10),

\[
\boxed{\mathbb P(H_{\max}=K)\to1,}
\]

proving (1.4).

## 6. Component mass: the compensated queue works uniformly for growing `K`

Explore a component by active-half-edge pairing. Let `A_t` be the active queue and `H_t` the number of designated hubs discovered by time `t`. Use the HARD7-04 compensation

\[
C_t:=A_t-dH_t.
\tag{6.1}
\]

The four possible increments are unchanged:

\[
\Delta C_t\in\{-2,-1,+1\}.
\tag{6.2}
\]

With `R_{1,t},R_{3,t}` the ordinary degree-1/3 vertices already exposed, the exact conditional drift identity is

\[
\boxed{
\mu_t:=\mathbb E(\Delta C_t\mid\mathcal F_t)
=
\frac{-\ell\delta_m-Md^2-3R_{3,t}+R_{1,t}-2C_t+2}
{\ell-2t-1}.
}
\tag{6.3}
\]

The family scaling gives

\[
\frac{Md^2}{\ell\delta_m}=O(m^{-2}),
\qquad
\frac{KH_m}{\ell\delta_m}=o(1),
\qquad
\frac{Kd}{\ell\delta_m}=o(1).
\tag{6.4}
\]

Hence, uniformly for `t<=2KH_m` before extinction,

\[
\mu_t\ge-(1+o(1))\delta_m,
\tag{6.5}
\]

and, as long as `H_t<=K`,

\[
\mu_t\le-(1-o(1))\delta_m.
\tag{6.6}
\]

Let

\[
\mathcal M_t=C_t-C_0-\sum_{s<t}\mu_s.
\]

Its increments are uniformly bounded, so Azuma-Hoeffding gives, for `T=O(KH_m)` and `x=Theta(Kd)`,

\[
\mathbb P\left(\max_{t\le T}|\mathcal M_t|\ge x\right)
\le \exp\{-\Theta(Km)\}.
\tag{6.7}
\]

The exponent dominates every union bound needed here because

\[
\log n=O(K\log m)=o(Km).
\tag{6.8}
\]

### 6.1 Global upper mass bound

Fix `eps>0` and put

\[
t_+=(1+\varepsilon)KH_m.
\]

Start from any hub. Then `C_0=0`. On survival through `t_+` with `H_t<=K`,

\[
C_{t_+}\ge1-Kd.
\]

By (6.6), the compensating drift contributes at most

\[
-(1-o(1))\delta_mt_+=-(1+\varepsilon-o(1))Kd.
\]

Thus survival to `t_+` forces a positive martingale deviation of at least `eps Kd/2` for large `m`. By (6.7), uniformly in the starting hub, this costs `exp{-Theta_eps(Km)}`. Union over all `M` hubs remains `o(1)`.

By (1.4), no component has more than `K` hubs with probability `1-o(1)`. Hence every hub-containing component has at most `(1+eps)KH_m+o(H_m)` vertices with high probability.

For a hub-free component, start from an ordinary vertex and run the same argument to time `eps K H_m`; now `C_0<=3` and `H_t=0`. Survival forces a deviation `Theta(eps Kd)`, again costing `exp{-Theta_eps(Km)}`. The union over all `n` vertices is still `o(1)` by (6.8). Therefore

\[
\boxed{L_1\le(1+\varepsilon)KH_m+o(H_m)\quad\text{whp}.}
\tag{6.9}
\]

### 6.2 Lower mass bound from a good path witness

Condition on one of the path-witness skeletons from Section 4. It has total path length `R=O(Km)`. The residual active queue satisfies

\[
A_0=Kd+O(Km),\qquad H_0=K,
\qquad C_0=O(Km)=o(Kd).
\tag{6.10}
\]

For a good witness the residual host is a tree and never discovers another hub. Suppose its total component size were below `(1-eps)KH_m`. Up to the negligible `O(Km)` skeleton size, its residual exploration would then become extinct by time

\[
T_-=(1-\varepsilon/2)KH_m
\]

for all large `m`. At extinction `C_\tau=-Kd`. By the lower drift bound (6.5),

\[
\sum_{s<\tau}\mu_s\ge-(1+o(1))\delta_m\tau
\ge-(1-\varepsilon/3)Kd
\]

for large `m`. Thus such premature extinction forces a negative martingale deviation of magnitude at least `c\varepsilon Kd`, whose conditional probability is at most

\[
\exp\{-c_\varepsilon Km\}.
\tag{6.11}
\]

This bound is uniform over all prescribed witness skeletons. Since `EZ_K<=m^{1+o(1)}`, the expected number of path witnesses whose host is prematurely small is `o(1)`. Combining with `P(Z_K^g>0)->1` from (4.10),

\[
\boxed{L_1\ge(1-\varepsilon)KH_m\quad\text{whp}.}
\tag{6.12}
\]

Equations (6.9) and (6.12), for every fixed `eps>0`, prove (1.2).

## 7. Consequence for the source route

This family has all of the following simultaneously:

\[
\delta_m\sim m^{-1},\qquad
n\delta_m^3\to\infty,
\qquad
\frac1n\sum_vd_v^3\to\frac{15}{2},
\]

\[
\frac{H_m}{E_m}\to\infty,
\qquad
Q_m\sim m^{-1}\to0,
\qquad
\frac{L_1}{H_m}\sim K_m\to\infty.
\]

Therefore the pair of scalar diagnostics

\[
(H_m/E_m,\ Q_m)
\]

cannot by itself yield a universal bounded-coefficient high-degree law under the source's broad finite-third-moment hypotheses. The missing state variable is genuinely global: the number and connectivity of near-maximal hubs. The previous rank-one marked-hub kernel is the natural replacement language.

This is deliberately labeled **PARTIAL**, because the source's prose asks for the correct phase-transition/crossover behavior, not for the false stronger statement that `H_m/E_m->infinity` alone forces `L_1/H_m->1` or even a universal bounded ratio.

## 8. Verification and audit status

This proof is an R14 self-check. It inherits the already established compensated-queue identities from HARD7-04 but rederives the scaling needed for growing `K`. No independent audit has yet been requested or received. The accompanying exact-arithmetic checker verifies only the family algebra and finite exponent identities; it is not a proof of the asymptotic probability statements.

Closure status of P0157 remains **SOURCE OPEN / PARTIAL**.
