# P0157 — matched-tail pair obstruction for the barely-subcritical configuration model

**Status.** R14 theorem-sized self-check / **PARTIAL** progress on van der Hofstad's finite-third-moment barely-subcritical configuration-model crossover problem. This note does **not** claim that the source problem is solved or refuted as phrased. It proves that the classical scalar data `H_n`, `E_n`, the local branching fluctuation `Q_n`, and even the limiting first three degree moments do not determine the largest-component scale under the source-level finite-third-moment hypotheses.

## 1. Matched families

Let `m -> infinity` through multiples of four. Let `K=K_m` be any integer sequence satisfying

\[
K_m\to\infty,\qquad K_m\log K_m=o(\log m).
\tag{1.1}
\]

Set

\[
n=8m^{2K+6},\qquad d=m^2.
\tag{1.2}
\]

For any integer `M`, define a degree sequence with `M` vertices of degree `d` and

\[
N_3=2m^{2K+6}-3m^{2K+5}-\frac{M}{4}(d-1)^2,
\tag{1.3}
\]
\[
N_1=6m^{2K+6}+3m^{2K+5}+\frac{M}{4}(d-1)^2-M.
\tag{1.4}
\]

For all sufficiently large `m` these are nonnegative integers. We compare two choices:

- **Family A (four-hub / sparse tail):** `M_A=4`;
- **Family B (staircase tail):** `M_B=m^{2K-1}`.

Let `CM_A,CM_B` be the corresponding configuration models, `L_1^A,L_1^B` their largest component orders, and for `X in {A,B}` write

\[
\nu_X=\frac{\sum_v d_v(d_v-1)}{\ell_X},\qquad
\delta_X=1-\nu_X,
\]
\[
H_X=\frac d{\delta_X},\qquad
E_X=\delta_X^{-2}\log(n\delta_X^3),
\qquad
Q_X=\frac{\operatorname{Var}(D_X^*-1)}{d\delta_X}.
\tag{1.5}
\]

### Theorem 1 (matched-tail separation)

The two families have the same `n` and the same maximal degree `d=m^2`. They both lie in the finite-third-moment barely-subcritical regime, and

\[
\frac{\delta_B}{\delta_A}\to1,
\qquad
\frac{H_B}{H_A}\to1,
\qquad
\frac{E_B}{E_A}\to1,
\qquad
\frac{Q_B}{Q_A}\to1,
\tag{1.6}
\]

with

\[
Q_A\sim Q_B\sim m^{-1},
\qquad
\frac{H_A}{E_A}\to\infty,
\qquad
\frac{H_B}{E_B}\to\infty.
\tag{1.7}
\]

Their empirical degree laws have the same limit

\[
\frac34\delta_1+\frac14\delta_3,
\tag{1.8}
\]

and their empirical third moments both tend to `15/2`. Nevertheless,

\[
\boxed{\frac{L_1^A}{H_A}\xrightarrow{\mathbb P}1,}
\tag{1.9}
\]

whereas

\[
\boxed{\frac{L_1^B}{K_m H_B}\xrightarrow{\mathbb P}1.}
\tag{1.10}
\]

In particular

\[
\frac{L_1^B/H_B}{L_1^A/H_A}\xrightarrow{\mathbb P}\infty.
\tag{1.11}
\]

Thus there is no universal source-level crossover law whose input consists only of the asymptotic values of `(H_n,E_n,Q_n)` together with the limiting first three degree moments. A correct general theorem must retain more information about the upper degree tail and its induced connectivity.

## 2. Exact scalar matching

For the general family (1.3)--(1.4), direct substitution gives

\[
\ell(M)
=12m^{2K+6}-6m^{2K+5}
-\frac M2(m^4-4m^2+3),
\tag{2.1}
\]

and, crucially,

\[
\boxed{
\ell(M)-\sum_vd_v(d_v-1)=12m^{2K+5},
}
\tag{2.2}
\]

**independently of `M`**. Hence

\[
\delta(M)=\frac{12m^{2K+5}}{\ell(M)}\sim m^{-1}.
\tag{2.3}
\]

Since

\[
\ell_A-\ell_B
=\frac{M_B-M_A}{2}(m^4-4m^2+3)
=O(m^{2K+3}),
\]

while `ell_A,ell_B=Theta(m^{2K+6})`,

\[
\frac{\delta_B}{\delta_A}=\frac{\ell_A}{\ell_B}=1+O(m^{-3}).
\tag{2.4}
\]

The same identity yields `H_B/H_A -> 1`. Moreover

\[
n\delta_X^3\asymp m^{2K+3}\to\infty,
\]

and

\[
\log(n\delta_X^3)=(2K+3+o(1))\log m,
\]

so

\[
\frac{H_X}{E_X}
=\frac{d\delta_X}{\log(n\delta_X^3)}
\sim \frac{m}{(2K+3)\log m}\to\infty.
\tag{2.5}
\]

The last limit follows from (1.1), which in particular implies `K log m=o(m)`.

For the size-biased forward offspring variable `xi=D^*-1`,

\[
\mathbb E\xi^2
=\frac{12N_3+d(d-1)^2M}{\ell(M)}.
\tag{2.6}
\]

Using `Var(xi)=E xi^2-(1-delta)^2` and (2.2), exact algebra gives, for Family A (eventually `K>=3`),

\[
Q_A
=m^{-1}-\frac12m^{-2}-m^{-3}+O(m^{-4}),
\tag{2.7}
\]

while for Family B,

\[
Q_B
=m^{-1}-\frac5{12}m^{-2}-m^{-3}+O(m^{-4}).
\tag{2.8}
\]

Thus `Q_B/Q_A -> 1`. The exact finite algebra is checked independently by `p0157_matched_tail_pair_exact.py`.

Finally, `M_A/n=o(1)` and `M_B/n=1/(8m^7)`. In both families `N_3/n->1/4`, `N_1/n->3/4`. The hub contribution to the empirical third moment is

\[
\frac{M_A d^3}{n}=O(m^{-2K}),
\qquad
\frac{M_B d^3}{n}=\frac1{8m},
\]

so both third moments tend to

\[
\frac34\cdot1^3+\frac14\cdot3^3=\frac{15}{2}.
\tag{2.9}
\]

This proves all matching assertions in (1.6)--(1.8).

## 3. Family A: four hubs but only one hub per component

Let `H` be the four degree-`d` vertices. The earlier P0157 marked-hub theorem proved for the actual configuration model that, with

\[
S_H=\sum_{h\in H}d_h,
\qquad
A_H=\sum_{\{i,j\}\subset H}d_i d_j,
\]

and

\[
\delta_H=\delta+\frac1\ell\sum_{h\in H}d_h(d_h-1),
\]

one has

\[
\mathbb P(\exists\text{ component containing two vertices of }H)
\le
\frac{4A_H}{3\ell\delta_H}
+\frac{32S_H}{\ell\delta^2}.
\tag{3.1}
\]

Here `S_H=4m^2`, `A_H=6m^4`, `delta_H~m^{-1}`, and `ell_A=Theta(m^{2K+6})`. Therefore the right side of (3.1) is

\[
O(m^{-2K-1})+O(m^{-2K-2})=o(1).
\tag{3.2}
\]

So the four hubs lie in four distinct components with high probability.

The earlier finite-population hub law also applies to each of these four vertices: under `ell>=cn`, `sum d_i^3<=Cn`, `delta->0`, `n delta^3->infinity`, and `d delta->infinity`, the component of any maximal-degree root obeys

\[
\frac{|C(v)|}{d/\delta}\xrightarrow{\mathbb P}1.
\tag{3.3}
\]

All of its hypotheses hold here, and `d delta~m->infinity`. Since there are only four hubs, a union bound gives

\[
\max_{h\in H}\left|\frac{|C(h)|}{H_A}-1\right|\xrightarrow{\mathbb P}0.
\tag{3.4}
\]

It remains to rule out a larger hub-free component. Explore a component from a vertex of degree at most three and stop if a hub is hit. On the hub-free event, each active-half-edge increment belongs to `{-2,-1,+1}`. Up to

\[
T=C\delta_A^{-2}\log n,
\tag{3.5}
\]

pairings, the exact finite-population drift is at most `-delta_A/2` for all sufficiently large `m`. Indeed the global excess is `-ell_A delta_A`, and removing at most `T` non-hub vertices can increase the unseen excess by at most `T`; hence the drift error relative to `-delta_A` is `O(T/ell_A)`, while

\[
\frac{T}{\ell_A\delta_A}
=O\!\left(\frac{\log n}{n\delta_A^3}\right)=o(1).
\tag{3.6}
\]

For `theta=2delta_A/9`, Hoeffding's conditional lemma for an increment in an interval of length three gives

\[
\mathbb E[e^{\theta\Delta A_t}\mid\mathcal F_t]
\le \exp(-\delta_A^2/18)
\tag{3.7}
\]

as long as the exploration remains hub-free and alive before `T`. Therefore, for a starting active queue at most three,

\[
\mathbb P(\tau>T,\ \text{no hub hit})
\le e^{3\theta}e^{-\delta_A^2T/18}.
\tag{3.8}
\]

Choose `C>40`. A union bound over all `n` starting vertices then shows that every hub-free component has

\[
O_{\mathbb P}(\delta_A^{-2}\log n)=O_{\mathbb P}(E_A)
\tag{3.9}
\]

vertices, because `log n/log(n delta_A^3)` stays bounded. By (2.5), `E_A=o(H_A)`. Combining (3.2), (3.4), and (3.9) proves

\[
L_1^A/H_A\to1
\]

in probability.

## 4. Family B: the staircase extends to every `K log K=o(log m)`

The preceding R14 staircase proof was written for the convenient choice

\[
K=\left\lfloor\sqrt{\frac{\log m}{\log\log m}}\right\rfloor.
\]

Its argument is in fact uniform under the weaker conditions (1.1). We record the dependence explicitly here.

Write

\[
a_m=\frac{6N_3}{\ell_B}=1-m^{-1}+O(m^{-2}).
\tag{4.1}
\]

For an ordered `K`-tuple of hubs, connect consecutive hubs by internally vertex-disjoint degree-three paths whose lengths lie in `[m,2m]`. The exact pairing count from the preceding proof gives

\[
\mathbb E Z_K
=(1+o(1))m c_0^{K-1},
\qquad
c_0:=\frac{e^{-1}-e^{-2}}{12}>0.
\tag{4.2}
\]

The error is uniform because each witness uses only `O(Km)` ordinary vertices and pairings, while

\[
\frac{K^2}{M_B}	o0,
\quad
\frac{K^2m^2}{N_3}	o0,
\quad
\frac{K^2m^2}{\ell_B}	o0.
\tag{4.3}
\]

Condition (1.1) implies `K=o(log m)`, so `c_0^K=m^{-o(1)}` and hence

\[
\mathbb E Z_K=m^{1-o(1)}\to\infty.
\tag{4.4}
\]

Conditioned on such a path skeleton, the total unexplored active queue is `O(Km^2)` and its subcritical mean exploration length is `O(Km^3)`. At each exposure the unseen-hub hazard is

\[
\frac{M_Bd}{\ell_B}=O(m^{-5}),
\]

so the probability of acquiring an additional hub is `O(Km^{-2})=o(1)`. The cycle probability is also `o(1)`. Thus the good-witness count `Z_K^g`, whose host is a tree with exactly these `K` hubs, has the same first-order expectation.

Two good witnesses in distinct host components have disjoint skeletons. A good tree host supports at most two orientations of its unique `K`-hub path. Exact perfect-matching factorization for disjoint skeletons therefore gives

\[
\mathbb E D_K^0=(1+o(1))(\mathbb E Z_K)^2,
\]

and pointwise

\[
(Z_K^g)^2\le2Z_K^g+D_K^0.
\tag{4.5}
\]

The second-moment inequality and (4.4) imply

\[
\mathbb P(H_{\max}\ge K)\to1.
\tag{4.6}
\]

For the reverse inequality, if a component contains `r=K+1` hubs, prune a minimal connecting tree and suppress ordinary relative-degree-two vertices. The resulting core has at most `r-2` ordinary degree-three branch vertices and at most

\[
\exp(O(K\log K))=m^{o(1)}
\tag{4.7}
\]

labeled topologies. Expanding each core edge into a degree-three chain yields the same rank-one factor as in the preceding proof,

\[
M_B^r\left(\frac{d^2}{\ell_B(1-a_m)}\right)^{r-1}
=\Theta(m^{2K+1-2r}).
\tag{4.8}
\]

At `r=K+1` this is `Theta(m^{-1})`; every ordinary branch vertex contributes an additional factor `O(m^{-1})`. Multiplication by (4.7) still gives `m^{-1+o(1)}=o(1)`. Core segments of length at least `m^2` contribute at most

\[
\exp\{O(K\log m)-cm\}=o(1),
\tag{4.9}
\]

because (1.1) implies `K log m=o(m)`. Therefore

\[
\mathbb P(H_{\max}\ge K+1)\to0.
\tag{4.10}
\]

Combining (4.6) and (4.10),

\[
\mathbb P(H_{\max}=K)\to1.
\tag{4.11}
\]

Finally, the compensated active-queue argument from the preceding P0157 proof is also uniform in this range. A component with `r<=K` hubs begins with effective queue `rd+o(rd)`, and, until extinction on the scale `rH_B`, the finite-population drift is `-delta_B(1+o(1))`. Its martingale fluctuations have exponential deviation cost at least `exp(-c_\varepsilon r d\delta_B)=exp(-c_\varepsilon r m)`. Uniformly over all hubs, the total error is bounded by terms of the form

\[
M_Be^{-c_\varepsilon m}
+\exp\{O(K\log m)-cm\}=o(1),
\tag{4.12}
\]

again because `K log m=o(m)`. Hence every component containing `r` hubs has

\[
|C|=(1+o_{\mathbb P}(1))rH_B
\tag{4.13}
\]

uniformly for `1<=r<=K`. Hub-free components are `O_P(E_B)=o_P(H_B)` by the same bounded-degree exploration argument as in Section 3. Together with (4.11), (4.13) proves

\[
L_1^B/(K H_B)\to1
\]

in probability.

This completes the proof of Theorem 1.

## 5. What the number `K` is really measuring

The staircase becomes more transparent after discretizing the upper tail. For Family B, the bulk-mediated connection probability between two prescribed hubs has first-order scale

\[
p_H\asymp\frac{d^2}{\ell_B\delta_B}\asymp m^{-(2K+1)}.
\tag{5.1}
\]

There are `M_B=m^{2K-1}` hubs, so the induced hub graph has mean-degree scale

\[
\lambda_H=M_Bp_H\asymp m^{-2}\to0.
\tag{5.2}
\]

The expected number of `r`-hub trees has scale

\[
M_B^r p_H^{r-1}\asymp m^{2K+1-2r}.
\tag{5.3}
\]

Thus the threshold lies exactly between `r=K` and `r=K+1`. Equivalently,

\[
\frac{\log M_B}{\log(1/\lambda_H)}=K+o(K).
\tag{5.4}
\]

This is the same counting mechanism that governs extreme component sizes in a very sparse Erdős--Rényi graph. The source problem therefore contains a **second-level random graph on the high-degree vertices**. The classical scalar `H=d_max/delta` describes the mass contributed by one hub, but the number of hubs that coalesce is controlled by this induced tail graph.

This suggests the following general object, stated only as a route and **not** as a proved theorem. For a suitable high-degree set `H_n`, form the rank-one kernel

\[
\kappa_{ij}\approx\frac{d_i d_j}{\ell\delta_H},
\tag{5.5}
\]

and let `G_H` be the corresponding sparse tail graph. A plausible corrected crossover functional is

\[
\max\left\{
E_n,
\frac1{\delta_n}
\max_{\mathcal C\subset G_H}
\sum_{i\in\mathcal C}d_i
\right\}.
\tag{5.6}
\]

The matched-pair theorem proves that **some** tail-connectivity information of this kind is necessary; it does not yet prove (5.6) in general.

## 6. Verification status

This is a theorem-sized self-check. The exact companion checker verifies only the finite algebra: integrality/positivity on a sanity grid, the `M`-independent deficit (2.2), positivity of `delta,Q`, the matched scalar convergence numerics, and the `+1/-1` hub-tree exponents. It is **not** a proof of the asymptotic probability claims.

The probability proof above builds explicitly on two earlier on-page P0157 route theorems already preserved in the repository:

- `artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`;
- `artifacts/hard7_2026-09-18/HARD7-04/p0157_hub_connection_kernel.md`;

and on the preceding R14 staircase proof:

- `artifacts/R14/p0157_growing_integer_staircase_obstruction.md`.

No independent audit is claimed. The source remains **OPEN / PARTIAL**.