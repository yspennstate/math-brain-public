# P0157 — dyadic top-band Steiner penalty and rank-one tree upper bound

**Status.** R14 theorem-sized self-check / **PARTIAL** progress on van der Hofstad's finite-third-moment barely-subcritical configuration-model crossover problem. This note does **not** claim the source problem is solved. It proves a general upper bound showing when higher-order bulk Steiner branching among a prescribed dyadic band of high-degree vertices is negligible compared with the rank-one tree term.

## 1. Setup

Let `d=(d_1,...,d_n)` be a deterministic degree sequence with even total degree

\[
\ell=\sum_i d_i,
\]

and assume fixed constants `c,C>0` such that

\[
\ell\ge cn,
\qquad
\sum_i d_i^3\le Cn.
\tag{1.1}
\]

Write

\[
\nu=\frac{\sum_i d_i(d_i-1)}{\ell},
\qquad
\delta=1-\nu>0.
\tag{1.2}
\]

For a threshold `a>=1`, let

\[
H_a=\{i:d_i\ge a\},
\qquad
B_a=[n]\setminus H_a,
\tag{1.3}
\]

and define the deficit of the bulk obtained by treating `H_a` as absorbing,

\[
\delta_a
:=1-\frac1\ell\sum_{v\in B_a}d_v(d_v-1)
=\delta+\frac1\ell\sum_{h\in H_a}d_h(d_h-1)
\ge\delta.
\tag{1.4}
\]

Fix a set `A subset H_a` of cardinality `r>=2` satisfying the dyadic-band condition

\[
a\le d_i<2a\qquad(i\in A).
\tag{1.5}
\]

Put

\[
S_A=\sum_{i\in A}d_i,
\qquad ra\le S_A<2ra.
\tag{1.6}
\]

Let `omega>=2` and set

\[
R=\left\lfloor\frac{\ell\delta}{4\omega}\right\rfloor,
\qquad
\Delta_a:=\delta_a-\frac{\delta}{2\omega}>0,
\qquad
g:=\frac1{\ell\Delta_a}.
\tag{1.7}
\]

We call a connecting witness for `A` **tail-exact at level `a`** if it is a tree in the configuration-model multigraph whose marked vertices are exactly `A` and whose other vertices all lie in `B_a`. Equivalently, no other vertex of `H_a` is allowed as an internal Steiner vertex. A witness is **short** if it has at most `R` edges.

The event that `A` is exactly the set of `H_a`-vertices in one component implies the existence of such a tail-exact connecting tree, obtained from a spanning tree of that component and then taking the minimal subtree spanning `A`.

## 2. The theorem

Let

\[
C_0:=C/c,
\qquad
\eta:=\frac{2e^2C_0r}{a\Delta_a}.
\tag{2.1}
\]

### Theorem 2.1 — short-witness rank-one upper bound

If `eta<1`, then in the configuration model with degree sequence `d`,

\[
\boxed{
\Pr(\text{there is a short tail-exact connecting tree for }A)
\le
\frac1{1-\eta}
\,g^{r-1}
\Big(\prod_{i\in A}d_i\Big)
S_A^{r-2}.
}
\tag{2.2}
\]

The `t=0` term on the right is exactly the weighted-Cayley tree sum for the rank-one kernel `d_i d_j/(ell Delta_a)`:

\[
\boxed{
 g^{r-1}\Big(\prod_{i\in A}d_i\Big)S_A^{r-2}
 =
 \sum_{T\in\mathcal T(A)}
 \prod_{\{i,j\}\in E(T)}\frac{d_i d_j}{\ell\Delta_a}.
}
\tag{2.3}
\]

Thus every additional unmarked bulk branch vertex is penalized geometrically by at most `eta`.

### Corollary 2.2 — asymptotic rank-one dominance

Suppose along a sequence that

\[
\frac r{a\delta_a}\to0,
\qquad
\frac r\omega\to0.
\tag{2.4}
\]

Then `Delta_a/delta_a ->1` on the relevant `r`-edge exponential scale, and

\[
\Pr(\text{short tail-exact connection of }A)
\le
(1+o(1))
\frac{\big(\prod_{i\in A}d_i\big)S_A^{r-2}}
     {(\ell\delta_a)^{r-1}}.
\tag{2.5}
\]

This is an upper bound, not a two-sided coupling theorem.

### Proposition 2.3 — long-exploration error

Assume additionally the barely-subcritical finite-third-moment regime

\[
\delta\to0,
\qquad n\delta^3\to\infty.
\tag{2.6}
\]

If `tau_h` denotes the active-half-edge exploration time of the component of `h`, then for every `h in A`,

\[
\Pr(\tau_h>R)
\le
\frac{8\omega d_h}{\ell\delta^2},
\tag{2.7}
\]

and hence

\[
\boxed{
\Pr(\exists h\in A:\tau_h>R)
\le
\frac{8\omega S_A}{\ell\delta^2}.
}
\tag{2.8}
\]

Consequently, whenever

\[
\frac{\omega S_A}{\ell\delta^2}\to0,
\tag{2.9}
\]

the long-witness contribution is negligible. Under (2.4), (2.9), and the source regime, prescribed top-band tail connectivity is therefore controlled to first order by the rank-one weighted tree sum (2.3), up to the still-unproved matching lower bound / Poissonization step.

## 3. Suppressing degree-two bulk vertices

Take a short tail-exact connecting tree and suppress every unmarked bulk vertex having tree-degree two. The resulting core is a finite tree whose marked vertices are the `r` vertices of `A` and whose unmarked core vertices all have degree at least three. Let `t` be the number of these unmarked branch vertices.

For a tree with `r` marked vertices and `t` unmarked vertices, degree counting gives

\[
t\le r-2,
\qquad
|E_{\rm core}|=r+t-1.
\tag{3.1}
\]

The paths replacing the core edges have internal vertices in `B_a`, all of tree-degree two. The key point is that the one-dimensional chains can be summed exactly enough, while each genuine bulk branch vertex carries a third-moment penalty.

## 4. Summing a bulk chain

Let

\[
S_2(B_a):=\sum_{v\in B_a}d_v(d_v-1)=\ell(1-\delta_a).
\tag{4.1}
\]

Because the complete witness uses at most `R` paired edges, every relevant pairing denominator is at least

\[
D:=\ell-2R\ge \ell\left(1-\frac\delta{2\omega}\right).
\tag{4.2}
\]

For one oriented core edge, allowing `k>=0` internal bulk degree-two-in-tree vertices gives the upper bound

\[
D^{-1}\left(\frac{S_2(B_a)}D\right)^k.
\]

Summing over `k` yields

\[
\sum_{k\ge0}D^{-1}\left(\frac{S_2(B_a)}D\right)^k
=\frac1{D-S_2(B_a)}
\le\frac1{\ell\Delta_a}=g.
\tag{4.3}
\]

This is the absorbing-bulk Green factor. It is the same `1/(ell times deficit)` structure that produced the earlier two-hub kernel.

## 5. A branch vertex costs a third-moment factor

For `s>=3`, define

\[
M_s(B_a):=\sum_{v\in B_a}(d_v)_s,
\qquad (x)_s=x(x-1)\cdots(x-s+1).
\]

Since every `v in B_a` has `d_v<a`,

\[
(d_v)_s\le d_v^s\le a^{s-3}d_v^3.
\]

Using (1.1),

\[
\boxed{
M_s(B_a)\le C_0\ell\,a^{s-3},
\qquad C_0=C/c.
}
\tag{5.1}
\]

Thus an unmarked core branch vertex of degree `s` contributes at most `C_0 ell a^{s-3}` after summing its possible labels and half-edge choices.

## 6. Weighted Cayley sum and the Steiner penalty

Temporarily label the `t` unmarked branch vertices. This overcounts actual cores and is therefore harmless for an upper bound. Let `q_x` denote the degree of a vertex `x` in a labeled core tree.

For marked `i in A`, bound `(d_i)_{q_i} <= d_i^{q_i}`. For each labeled bulk branch vertex `u`, combine (5.1) with its degree `q_u>=3`:

\[
M_{q_u}(B_a)\le C_0\ell a^{q_u-3}.
\]

After expanding each of the `r+t-1` core edges into a bulk chain and applying (4.3), the contribution of all labeled cores with exactly `t` branch labels is at most

\[
W_t
\le
(C_0\ell)^t a^{-3t}g^{r+t-1}
\sum_{T\in\mathcal T_{r+t}}
\prod_{i\in A}d_i^{q_i(T)}
\prod_{u=1}^t a^{q_u(T)}.
\tag{6.1}
\]

The weighted Cayley identity gives

\[
\sum_{T\in\mathcal T_{r+t}}
\prod_{i\in A}d_i^{q_i(T)}
\prod_{u=1}^t a^{q_u(T)}
=
\Big(\prod_{i\in A}d_i\Big)a^t
(S_A+ta)^{r+t-2}.
\tag{6.2}
\]

Therefore

\[
\boxed{
W_t
\le
(C_0\ell)^t a^{-2t}g^{r+t-1}
\Big(\prod_{i\in A}d_i\Big)
(S_A+ta)^{r+t-2}.
}
\tag{6.3}
\]

For `t=0`,

\[
W_0=g^{r-1}\Big(\prod_{i\in A}d_i\Big)S_A^{r-2}.
\tag{6.4}
\]

For `1<=t<=r-2`, divide (6.3) by (6.4):

\[
\frac{W_t}{W_0}
\le
(C_0\ell g)^t
\left(\frac{S_A}{a^2}\right)^t
\left(1+\frac{ta}{S_A}\right)^{r+t-2}.
\tag{6.5}
\]

Using `S_A<2ra`, `S_A>=ra`, `t<=r`, and

\[
\left(1+\frac tr\right)^{2r}\le e^{2t},
\]

we obtain

\[
\boxed{
\frac{W_t}{W_0}
\le
\left[
\frac{2e^2C_0r}{a\Delta_a}
\right]^t
=\eta^t.
}
\tag{6.6}
\]

Summing `t=0,...,r-2` proves (2.2).

This is the promised monovariant: **every extra unmarked Steiner branch vertex pays one more factor of order `r/(a delta_a)`**. The combinatorial growth of core topologies does not overcome that penalty in the regime `r=o(a delta_a)`.

## 7. Why the `t=0` term is rank one

For a tree `T` on the marked vertex set `A`,

\[
\prod_{\{i,j\}\in E(T)}\frac{d_i d_j}{\ell\Delta_a}
=(\ell\Delta_a)^{-(r-1)}
\prod_{i\in A}d_i^{\deg_T(i)}.
\]

Another application of the weighted Cayley identity gives

\[
\sum_{T\in\mathcal T(A)}
\prod_{i\in A}d_i^{\deg_T(i)}
=
\Big(\prod_{i\in A}d_i\Big)S_A^{r-2},
\]

which is (2.3).

Thus the pair kernel

\[
\kappa_{ij}^{(a)}=\frac{d_i d_j}{\ell\delta_a}
\tag{7.1}
\]

is not merely suggested by the two-hub marginal: it is the exact leading tree weight after all degree-two bulk chains are summed, provided higher Steiner branching is suppressed by (6.6).

## 8. Long exploration

The predecessor finite-population exploration argument gives, uniformly up to times `t<=ell delta/4`, the upper drift bound

\[
\mathbb E[\Delta A_t\mid\mathcal F_t]\le-\delta/2.
\tag{8.1}
\]

For a component exploration started with `d_h` active half-edges and stopped at `tau_h wedge R`, optional stopping yields

\[
\mathbb E(\tau_h\wedge R)\le\frac{2d_h}{\delta}.
\tag{8.2}
\]

Therefore

\[
\Pr(\tau_h>R)
\le\frac{2d_h}{\delta R}
\le\frac{8\omega d_h}{\ell\delta^2},
\tag{8.3}
\]

up to the harmless integer-rounding change in `R`. Summing over `h in A` proves (2.8).

The source regime and the finite-third-moment bound imply

\[
\frac{d_{\max}}{\ell\delta^2}=o(1),
\tag{8.4}
\]

so one may choose `omega -> infinity` slowly enough that the single-root long-exploration error still vanishes. For a set `A`, condition (2.9) is the corresponding aggregate requirement.

## 9. What this proves and what it does not

This theorem moves the marked-tail route from a pairwise heuristic toward a general upper approximation:

1. after localizing to a dyadic top-degree band, degree-two bulk chains sum to the absorbing Green factor `1/(ell delta_a)`;
2. the no-bulk-branch (`t=0`) contribution is exactly the weighted tree sum of a rank-one graph with edge scale `d_i d_j/(ell delta_a)`;
3. every genuine unmarked bulk Steiner branch vertex incurs a geometric penalty `O(r/(a delta_a))`;
4. long explorations are separately controlled by (2.8).

It does **not** yet prove that the induced tail graph is asymptotically an independent Norros--Reittu graph, does not supply a matching lower bound, and does not establish the source's complete largest-component crossover. Those require overlap control / Poissonization of the surviving pairwise tree witnesses and then a uniform bulk-mass map for the resulting marked components.

## 10. Relation to the nested sparse-graph picture

The predecessor matched-pair and staircase examples showed that scalar data such as `H_n`, `E_n`, `Q_n`, and limiting moments cannot determine `L_1`; the population and connectivity of the upper degree tail matter. This note identifies the rank-one pair graph as the correct **leading upper-bound object on a broad dyadic slice**, rather than merely guessing it from one explicit family.

The surviving weighted-tree expression is the same combinatorial shape that appears in rank-one inhomogeneous random graphs such as Norros--Reittu. That analogy is methodological only. No external rank-one theorem is silently transferred to the dependent configuration-model tail graph here.

The natural next theorem would be a two-sided Poisson/switching approximation for these tail-exact tree witnesses, followed by a theorem that the bulk mass attached to a marked tail component is asymptotic to `delta^{-1}` times its total marked degree. Those two steps would turn the candidate object

\[
\max\left\{
\delta^{-2}\log(n\delta^3),
\frac1\delta\max_{\mathcal C\subset G_H}\sum_{i\in\mathcal C}d_i
\right\}
\]

from a route into a genuine crossover theorem.

## 11. Verification status

This is a theorem-sized asymptotic counting argument with the proof written on the page. No finite arithmetic assertion required a new checker, so no checker-only artifact was manufactured. It remains an R14 self-check pending independent audit.