# P0157 — finite-population hub law for a maximal-degree root

**Scope.** This is a self-contained route theorem for the barely-subcritical configuration model. It proves a graph-level law of large numbers for the component of a chosen maximal-degree vertex in the high-degree self-averaging regime. It does **not** prove the source's full largest-component crossover theorem, and no novelty claim is made here.

## Theorem

Let `d^(n)=(d_1,...,d_n)` be a deterministic degree sequence with even total degree

\[
\ell_n:=\sum_{i=1}^n d_i,
\]

and let

\[
\nu_n:=\frac{\sum_i d_i(d_i-1)}{\ell_n},\qquad
\delta_n:=1-\nu_n>0,\qquad d_n:=\max_i d_i.
\]

Assume that for fixed constants `c,C>0`, eventually

\[
\ell_n\ge cn,\qquad \sum_i d_i^3\le Cn,
\tag{1}
\]

and that

\[
\delta_n\to0,\qquad n\delta_n^3\to\infty,
\qquad d_n\delta_n\to\infty.
\tag{2}
\]

Let `v_n` be any vertex of degree `d_n`, and let `C(v_n)` denote its component in the configuration model with degree sequence `d^(n)`. Then

\[
\boxed{
\frac{|C(v_n)|}{d_n/\delta_n}\xrightarrow{\mathbb P}1.
}
\tag{3}
\]

Consequently, if

\[
H_n:=\frac{d_n}{\delta_n},\qquad
E_n:=\delta_n^{-2}\log(n\delta_n^3)
\]

and `H_n/E_n -> infinity`, then (2)'s last condition is automatic and

\[
|C(v_n)|=(1+o_{\mathbb P}(1))H_n,\qquad
L_1\ge (1-o_{\mathbb P}(1))H_n.
\tag{4}
\]

Here `L_1` is the largest component order. Equation (4) is only a lower bound for `L_1`; it is not the full hub-dominant largest-component theorem.

## 1. Scale consequences of the hypotheses

From `d_n^3 <= sum_i d_i^3 <= Cn`,

\[
d_n\le C^{1/3}n^{1/3}.
\tag{5}
\]

Write

\[
x_n:=n^{1/3}\delta_n.
\]

Then `n delta_n^3 -> infinity` is exactly `x_n -> infinity`, and therefore

\[
\frac{d_n^2}{n\delta_n}=O(x_n^{-1})=o(1),
\qquad
\frac{d_n}{n\delta_n^2}=O(x_n^{-2})=o(1).
\tag{6}
\]

Set

\[
h_n:=\frac{d_n}{\delta_n},\qquad
M_n:=\lceil 2h_n\rceil,
\qquad
a_n:=\left(\frac{n\delta_n^2}{d_n}\right)^{1/2}.
\tag{7}
\]

Then `a_n -> infinity`, `M_n=o(n)`, and

\[
\frac{a_nM_n}{n\delta_n}
=O\!\left(\sqrt{\frac{d_n}{n\delta_n^2}}\right)=o(1).
\tag{8}
\]

## 2. Exact active-half-edge exploration

Explore the component of `v_n` by the usual pairing process. Let `A_t` be the number of active half-edges after `t` pairings, with

\[
A_0=d_n,
\]

and let

\[
\tau:=\inf\{t:A_t=0\}.
\]

For `t<tau`, choose one active half-edge and pair it uniformly to one of the

\[
D_t:=\ell_n-2t-1
\]

other unpaired half-edges. Let `U_t` be the set of unseen vertices. If the partner lies at an unseen vertex of degree `k`, then `Delta A_t=k-2`; if it is another active half-edge then `Delta A_t=-2`. Hence, exactly,

\[
b_t:=\mathbb E[\Delta A_t\mid\mathcal F_t]
=\frac{\sum_{i\in U_t}d_i(d_i-2)-2(A_t-1)}{D_t},
\tag{9}
\]

and

\[
q_t:=\mathbb E[(\Delta A_t)^2\mid\mathcal F_t]
=\frac{\sum_{i\in U_t}d_i(d_i-2)^2+4(A_t-1)}{D_t}.
\tag{10}
\]

The total excess satisfies

\[
\sum_i d_i(d_i-2)
=\sum_i d_i(d_i-1)-\ell_n
=-\ell_n\delta_n.
\tag{11}
\]

Let `R_t` be the set of non-root vertices discovered before time `t`, put

\[
s_i:=d_i(d_i-2),\qquad Z_t:=\sum_{i\in R_t}s_i,
\]

and write `s_r=d_n(d_n-2)` for the root contribution. Combining (9) and (11) gives the exact drift-defect identity

\[
\boxed{
 b_t+\delta_n
 =\frac{-\delta_n(2t+1)-s_r-Z_t-2(A_t-1)}{D_t}.
}
\tag{12}
\]

This identity is the finite-population replacement for an iid Galton--Watson coupling.

## 3. A size-biased depletion budget

For a vertex `i`, define

\[
g_i:=d_i+|d_i(d_i-2)|.
\]

For every integer `d_i>=1`,

\[
d_i g_i\le 2d_i^3.
\tag{13}
\]

Let

\[
G_t:=\sum_{i\in R_t}g_i.
\]

For `t<M_n` and `n` large, `D_t >= ell_n/2 >= cn/2`. At a pairing step, an unseen vertex `i` is discovered with conditional probability `d_i/D_t`, so

\[
\mathbb E[G_{t+1}-G_t\mid\mathcal F_t]
\le \frac{\sum_i d_i g_i}{D_t}
\le \frac{4C}{c}=:K.
\tag{14}
\]

Stopping at `tau` and summing,

\[
\mathbb E G_{M_n\wedge\tau}\le KM_n.
\]

Therefore Markov's inequality gives

\[
\mathbb P\left(G_{M_n\wedge\tau}>a_nM_n\right)
\le K/a_n=o(1).
\tag{15}
\]

On the complementary event, simultaneously for every `t<=M_n\wedge tau`,

\[
|Z_t|\le G_t\le a_nM_n,
\qquad
A_t\le d_n+\sum_{i\in R_t}d_i\le d_n+a_nM_n.
\tag{16}
\]

Using (12), (16), `D_t >= cn/2`, and (6)--(8), we obtain a deterministic sequence `rho_n ->0` such that on this event

\[
\sup_{t<M_n\wedge\tau}|b_t+\delta_n|
\le \rho_n\delta_n.
\tag{17}
\]

Indeed the numerator in (12) is bounded in absolute value by

\[
d_n^2+3a_nM_n+O(d_n+\delta_nM_n+1),
\]

and after division by `n delta_n` every term tends to zero by (6)--(8).

The conditional second moment is uniformly bounded on the same event. Since

\[
d_i(d_i-2)^2\le d_i^3
\]

for every nonnegative integer `d_i`, (10), (1), and (16) imply

\[
q_t\le K_2
\tag{18}
\]

for a constant `K_2=K_2(c,C)` and all `t<M_n\wedge tau`, for all large `n`. Here `a_nM_n=O(\sqrt{nd_n})=o(n)` by (5).

## 4. Doob decomposition and the extinction-time law

Stop the exploration when either `tau`, `M_n`, or the budget in (15) is exceeded. Up to this stopping time, define the martingale

\[
\mathcal M_t:=A_t-d_n-\sum_{s<t}b_s.
\]

By (18), its predictable quadratic variation up to `M_n` is at most `K_2M_n`. Doob's `L^2` inequality therefore yields, for every fixed `eps>0`,

\[
\mathbb P\left(\max_{t\le M_n}|\mathcal M_t|>\eps d_n\right)
\le \frac{4K_2M_n}{\eps^2d_n^2}
=O\!\left(\frac1{\eps^2d_n\delta_n}\right)=o(1).
\tag{19}
\]

Combining (15), (17), and (19), uniformly for `t<=M_n\wedge tau`,

\[
A_t=d_n-\delta_nt+o_{\mathbb P}(d_n).
\tag{20}
\]

Fix `eps in (0,1)` and put

\[
t_-:=\left\lfloor(1-\eps)d_n/\delta_n\right\rfloor,
\qquad
t_+:=\left\lceil(1+\eps)d_n/\delta_n\right\rceil.
\]

If `tau<=t_-`, then applying (20) at `t=tau` would give

\[
0=A_\tau\ge \eps d_n+o_{\mathbb P}(d_n),
\]

with probability tending to one, a contradiction. If `tau>t_+`, then (20) at `t=t_+` gives

\[
A_{t_+}\le -\eps d_n+o_{\mathbb P}(d_n),
\]

again impossible because `A_{t_+}>0`. Thus

\[
\boxed{
\frac{\tau}{d_n/\delta_n}\xrightarrow{\mathbb P}1.
}
\tag{21}
\]

## 5. Surplus edges vanish

For completeness, the cycle obstruction can be controlled without an iid approximation. Before extinction, every discovered non-root vertex has `s_i=d_i(d_i-2)>=-1`, and the root has nonnegative `s_r` eventually. Hence, for `t<=ell_n delta_n/4`, (9) implies

\[
b_t\le-\delta_n/2.
\tag{22}
\]

Also (10) is uniformly bounded there by a constant `B=B(c,C)`, because `sum_i d_i(d_i-2)^2<=Cn` and `A_t<=D_t+1`.

Let

\[
K_n':=\left(\frac{n\delta_n^2}{d_n}\right)^{1/2}\to\infty,
\qquad
T_n:=\left\lceil K_n'\frac{d_n}{\delta_n}\right\rceil.
\]

By (6), `T_n<=ell_n delta_n/4` eventually. Stopping at `S=T_n wedge tau`, (22) gives

\[
\mathbb E S\le \frac{2d_n}{\delta_n},
\tag{23}
\]

while applying the one-step identity for `A_t^2` and using (22) and the bounded second moment gives

\[
\delta_n\,\mathbb E\sum_{t<S}A_t
\le d_n^2+\frac{2Bd_n}{\delta_n}.
\tag{24}
\]

At time `t`, conditional on the exploration history, the probability that the partner half-edge is already active is exactly

\[
\frac{A_t-1}{D_t}.
\]

Using `D_t>=ell_n/2`, (23)--(24), and Markov's inequality,

\[
\mathbb P(C(v_n)\text{ contains a cycle})
\le \frac{2}{K_n'}
+O\!\left(\frac{d_n^2}{n\delta_n}
+\frac{d_n}{n\delta_n^2}\right)
=o(1)
\tag{25}
\]

by (6).

When the component is a tree, each pairing discovers exactly one of its edges and

\[
|C(v_n)|=\tau+1.
\]

Equations (21) and (25) prove (3).

## 6. Connection to the source scales

If `H_n/E_n -> infinity`, then

\[
\frac{H_n}{E_n}
=\frac{d_n\delta_n}{\log(n\delta_n^3)}\to\infty.
\]

Since `n delta_n^3 -> infinity`, the logarithm tends to infinity, so `d_n delta_n -> infinity`. The theorem applies and proves (4).

Thus the finite-population depletion/collision gap between the ideal hub branching process and the actual configuration model is closed for the **maximal-degree root** throughout the strong hub-dominant regime. The remaining source-level obligations are global: prove a matching largest-component upper bound in this regime, establish the Erdos--Renyi extreme scale under the full finite-third-moment assumptions in the opposite regime, and identify the order-one crossover.

## 7. Verification status

This is an asymptotic theorem with an on-page proof, not a finite exhaustive claim. No numerical scan or exact-arithmetic checker is used or needed. The argument should be treated as a **self-check / PARTIAL route result** until independently audited. Active-half-edge exploration, Doob decomposition, and size-biased exposure estimates are standard tools; no claim is made here that the theorem or its mechanism is absent from prior literature.