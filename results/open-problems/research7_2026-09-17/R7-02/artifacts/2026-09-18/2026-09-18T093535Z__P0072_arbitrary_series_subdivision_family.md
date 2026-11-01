# P0072 — an infinite non-series-parallel family: arbitrary series subdivision of one losange branch

Status: **restricted theorem / PROVED CANDIDATE after exact symbolic verification and self-review; full canonical P0072 remains OPEN; publication novelty UNVERIFIED.**

This note strengthens the preceding once-subdivided-losange theorem from one six-edge graph to an infinite family. It uses the same three recovery methods B6/B20/B29 and keeps the full-source metric unchanged.

## 1. The graph family

Fix an integer `m >= 2`. Let `G_m` be obtained from the five-edge losange by replacing the edge from the left terminal `s` to the left middle vertex `a` by a simple chain of `m` edges. Retain the four other losange edges

\[
a-t,\qquad s-b,\qquad b-t,\qquad a-b.
\]

All original edges start with weight one. There are exactly four simple `s`-`t` paths:

- `L`: the `m`-edge chain from `s` to `a`, followed by `a-t`;
- `A`: the chain, followed by `a-b-t`;
- `B`: `s-b-a-t`;
- `R`: `s-b-t`.

For every `m >= 2`, `R` is the unique geodesic, of length two. Every edge not in `R` is non-geodesic.

Let `L,A,B,R` also denote the numbers of ants whose loop-erased reinforced path is of the corresponding type after `n` ants. Then

\[
L+A+B+R=n.
\]

All `m` chain edges always receive reinforcement together, so their common raw weight is
\[
u=1+L+A.
\]
Write
\[
v=1+L+B,\qquad w=1+A+B,\qquad d=1+R+B,\qquad e=1+R+A
\]
for the weights of `a-t,a-b,s-b,b-t`. Put
\[
t=n+2.
\]
Then, exactly,
\[
u+d=t,\qquad v+e=t.
\tag{1.1}
\]

## 2. B6 — deform the solved graph by the series length

Suppress the `m-1` degree-two chain vertices in the weighted spanning-tree law. Since all chain conductances are `u`, their series conductance is
\[
\boxed{g=\frac{u}{m}.}
\tag{2.1}
\]
The usual degree-two series reduction preserves the `s`-`t` path law in the weighted UST. When the chain is reinforced, `u` increases by one and therefore `g` increases by `1/m`.

Thus the source loop-erased process on `G_m` is exactly an anisotropically reinforced five-edge losange with conductances
\[
(g,v,w,d,e)=\left(\frac{u}{m},v,w,d,e\right).
\]

The weighted spanning-tree partition function is
\[
Z_m=gvw+gvd+gve+gwe+gde+vwd+vde+wde,
\tag{2.2}
\]
and the four UST path probabilities are
\[
q_L=\frac{gv(w+d+e)}{Z_m},\qquad
q_A=\frac{gwe}{Z_m},\qquad
q_B=\frac{vwd}{Z_m},\qquad
q_R=\frac{de(g+v+w)}{Z_m}.
\tag{2.3}
\]
The exact checker archived with this note verifies `q_L+q_A+q_B+q_R=1` symbolically.

## 3. A strict Lyapunov drift for every integer m >= 2

Define
\[
S=u+v+w,\qquad V=\frac{S}{t}.
\]
As before, every one of `L,A,B` increments exactly two of `u,v,w`, while `R` increments none. Therefore
\[
S=3+2(L+A+B)=2n+3-2R,
\]
so
\[
\boxed{V=2-\frac{2R+1}{t}.}
\tag{3.1}
\]
Consequently
\[
\mathbb E[V_{n+1}-V_n\mid\mathcal F_n]
=-\frac{2\Delta_m}{t+1},
\qquad
\Delta_m:=q_R-\frac{R+1/2}{t}.
\tag{3.2}
\]

### Lemma 3.1
For every integer `m >= 2` and every finite state,
\[
\boxed{\Delta_m>0.}
\tag{3.3}
\]

### Proof
Exact simplification gives
\[
\boxed{
\Delta_m=\frac{N_m(L,A,B,R)}{2m\,t\,Z_m}.
}
\tag{3.4}
\]
The numerator has the identity
\[
\boxed{
N_m=N_2+(m-2)(B+R+1)Q_0,
}
\tag{3.5}
\]
where `N_2` is exactly the strictly positive-coefficient polynomial `P` displayed in the preceding artifact

`2026-09-18T092720Z__P0072_once_subdivided_losange_loop_erased.md`,

and
\[
\begin{aligned}
Q_0={}&2A^3+6A^2B+4A^2L+2A^2R+9A^2
+4AB^2+6ABL+4ABR+15AB\\
&+2AL^2+2ALR+10AL+5AR+12A
+2B^2R+3B^2+4BLR+5BL+6BR+8B\\
&+2L^2R+2L^2+5LR+6L+4R+5.
\end{aligned}
\tag{3.6}
\]
Both `N_2` and `Q_0` have strictly positive coefficients. Since `m-2 >= 0` and all path counts are nonnegative, `N_m>0`. Also `m,t,Z_m>0`, proving (3.3). The accompanying executed exact-arithmetic checker verifies (3.4)--(3.6), including coefficient positivity. ∎

Hence `V_n` is a bounded nonnegative supermartingale and
\[
V_n\to V_\infty\quad\text{a.s.},
\qquad
\sum_n\frac{\Delta_m(n)}{t_n}<\infty\quad\text{a.s.}
\tag{3.7}
\]
The second assertion follows from the Doob decomposition: the predictable decreasing compensator has bounded expectation and is nonnegative.

Moreover
\[
q_R=\frac{R+1/2}{t}+\Delta_m>\frac1{2t},
\]
so conditional Borel--Cantelli gives
\[
\boxed{R_n\to\infty\quad\text{a.s.}}
\tag{3.8}
\]

## 4. B20 — the only possible projective bad faces

Let
\[
\ell=L/t,\quad \alpha=A/t,\quad \beta=B/t,\quad \rho=R/t.
\]
The normalized path-count vector lies asymptotically in the compact simplex
\[
\ell+\alpha+\beta+\rho=1.
\]

Let `N_{m,4}` be the homogeneous degree-four part of `N_m`. At `m=2` its zero set on the simplex was proved in the preceding artifact to be
\[
\{\rho=1\}
\cup\{\rho=0,\alpha=0\}
\cup\{\rho=0,\beta=0\}.
\tag{4.1}
\]
For `m>=2`, equation (3.5) only adds a nonnegative homogeneous degree-four polynomial. That added degree-four part vanishes on all three sets in (4.1), so the zero set is unchanged. For a direct check on the `rho=0` face, the exact factorization is
\[
\boxed{
N_{m,4}\big|_{R=0}
=A B(A+B+L)\,[2(m+1)A+4mB+2(m+1)L].
}
\tag{4.2}
\]
If `R>0` and the point is not the pure-`R` vertex, the positive-coefficient `N_{2,4}` already contains a positive monomial, hence `N_{m,4}>0`.

The finite compensator in (3.7), together with the fact that normalized path counts move by only `O(1/t)` each step, gives the standard slow-motion conclusion: every projective limit point must lie in the zero set (4.1). Indeed, around any point where `N_{m,4}>0`, `Delta_m` is bounded below by a positive constant; entering a smaller compact neighborhood then requires order `t` steps to leave a slightly larger one, contributing a fixed positive amount to `sum Delta_m/t`, which cannot happen infinitely often.

Since `V_n` converges and
\[
V_n=2-\frac{2R_n+1}{t_n},
\]
the only possible limits are
\[
\boxed{V_\infty\in\{0,2\}.}
\tag{4.3}
\]
If `V_\infty=0` we are done. It remains to rule out `V_\infty=2`, which would mean
\[
R_n/t_n\to0
\]
and approach to the two bad boundary edges in (4.1).

## 5. B29 — a uniform invasion exponent on the blown-up boundary

Use homogeneous conductances
\[
g=\frac{\ell+\alpha}{m},\quad
v=\ell+\beta,\quad
w=\alpha+\beta,\quad
d=\rho+\beta,\quad e=\rho+\alpha.
\tag{5.1}
\]
We compute the ratio `q_R/rho` on all projective charts of the bad set.

### Face beta=0
If `B/R -> k` and `A/t -> alpha`, then `ell+alpha=1` and
\[
\boxed{
\frac{q_R}{\rho}\longrightarrow
\frac{(m+1)(k+1)}{2-\alpha}
\ge\frac{m+1}{2}\ge\frac32.
}
\tag{5.2}
\]

### Face alpha=0
If `A/R -> k` and `B/t -> beta`, then `ell+beta=1` and
\[
\boxed{
\frac{q_R}{\rho}\longrightarrow
(k+1)\frac{\beta(m-1)+m+1}{\beta(m-2)+2}.
}
\tag{5.3}
\]
For `m>=2` and `0<=beta<=1`, the fraction is at least `3/2`. Indeed, after multiplying by the positive denominator, the desired inequality is equivalent to
\[
2(m-2)+\beta(4-m)\ge0,
\]
whose minimum over `beta in [0,1]` is `min(2m-4,m)>=0`.

### Pure-L intersection
If `A/R -> k_A` and `B/R -> k_B`, then
\[
\boxed{
\frac{q_R}{\rho}\longrightarrow
\frac{(m+1)(k_A+1)(k_B+1)}{2(k_A+k_B+1)}
\ge\frac{m+1}{2}\ge\frac32,
}
\tag{5.4}
\]
because `(k_A+1)(k_B+1)>=k_A+k_B+1`.

The same bounds persist for projective limits with one of the ratios infinite. Equivalently, if a sequence approaches the bad set with `R->infinity` and `R/t->0`, every subsequence has a further compactified projective subsequence covered by one of these charts, and therefore
\[
\boxed{
\liminf\frac{tq_R}{R}\ge\frac32.
}
\tag{5.5}
\]
The exact checker independently verifies all three rational chart formulas.

## 6. A rigorous supercritical-birth exclusion lemma

The preceding six-edge note used the right idea but compressed the martingale justification. Here is the fully summable version.

### Lemma 6.1
Let `N_n` be nondecreasing and integer-valued with increments `Y_{n+1}=N_{n+1}-N_n in {0,1}` and conditional probability
\[
p_n=\mathbb P(Y_{n+1}=1\mid\mathcal F_n).
\]
Let `t_n=n+O(1)`. There is no event on which simultaneously
\[
N_n\to\infty,\qquad N_n/t_n\to0,
\]
and, for some constant `c>1`,
\[
p_n\ge cN_n/t_n
\]
eventually.

### Proof
Set `H_j=sum_{r=1}^j 1/r`. Then
\[
H_{N_{n+1}}-H_{N_n}=\frac{Y_{n+1}}{N_n+1}.
\]
Hence
\[
H_{N_n}=H_{N_0}+M_n+
\sum_{k<n}\frac{p_k}{N_k+1},
\tag{6.1}
\]
where
\[
M_n=\sum_{k<n}\frac{Y_{k+1}-p_k}{N_k+1}
\]
is a martingale. Its conditional quadratic variation satisfies
\[
\sum_k\mathbb E[(\Delta M_k)^2\mid\mathcal F_k]
\le
\sum_k\frac{p_k}{(N_k+1)^2}.
\]
Taking expectations and using conditional expectation,
\[
\mathbb E\sum_k\frac{p_k}{(N_k+1)^2}
=
\mathbb E\sum_k\frac{Y_{k+1}}{(N_k+1)^2}
\le
\sum_{j=N_0}^\infty\frac1{(j+1)^2}<\infty.
\tag{6.2}
\]
Thus the quadratic variation is finite almost surely and `M_n` converges almost surely.

Choose `1<c'<c`. Since `N_n->infinity`, eventually
\[
\frac{p_n}{N_n+1}
\ge
\frac{cN_n}{t_n(N_n+1)}
\ge\frac{c'}{t_n}.
\]
Therefore (6.1) gives
\[
H_{N_n}\ge c'\log n+O(1)
\]
almost surely on the event in question. But `N_n<=N_0+n`, hence
\[
H_{N_n}\le\log n+O(1),
\]
a contradiction because `c'>1`. ∎

## 7. Main family theorem

### Theorem 7.1
For every integer `m>=2`, consider the source loop-erased ant process with unit initial edge weights on `G_m`, obtained by replacing one left losange edge by a chain of `m` edges. Then almost surely every non-geodesic edge has sublinear weight, while both edges of the unique geodesic `s-b-t` have asymptotic normalized weight one:
\[
\frac{W_e(n)}n\to0
\quad\text{for every }e\notin\{s-b,b-t\},
\]
and
\[
\frac{W_{s-b}(n)}n,\frac{W_{b-t}(n)}n\to1.
\]

### Proof
Suppose the undesired alternative `V_\infty=2` in (4.3) occurs. Then `R_n/t_n->0`. By (3.8), `R_n->infinity`. By the projective invasion bound (5.5), for any fixed `c` with `1<c<3/2`, eventually
\[
q_R(n)\ge c\frac{R_n}{t_n}.
\]
Applying Lemma 6.1 to `N_n=R_n` gives a contradiction. Therefore `V_\infty=0` almost surely.

Since
\[
V_n=(u_n+v_n+w_n)/t_n
\]
and all summands are nonnegative,
\[
u_n/t_n\to0,\qquad v_n/t_n\to0,\qquad w_n/t_n\to0.
\]
Every one of the `m` chain edges has weight `u_n`; `a-t` has weight `v_n`; and `a-b` has weight `w_n`, so all non-geodesic edges are sublinear. Finally (1.1) gives
\[
d_n/t_n=1-u_n/t_n\to1,\qquad e_n/t_n=1-v_n/t_n\to1.
\]
Since `t_n=n+2`, the same limits hold with denominator `n`. ∎

## 8. Exact verification and scope

The exact symbolic checker executed in this run is

`2026-09-18T093140Z__P0072_m_subdivision_exact_checker.py`

with archived output

`2026-09-18T093140Z__P0072_m_subdivision_exact_checker.out`.

It ends `ALL_EXACT_CHECKS_PASS` and verifies the path-probability identity, the exact drift numerator decomposition (3.5), coefficient positivity, the leading boundary factor (4.2), and all three projective chart formulas (5.2)--(5.4).

This proves an **infinite finite-graph family** beyond the single five-edge losange and beyond the distance-two suspension class. It does not settle arbitrary finite graphs and does not address the separate uniform-geodesic rule on general graphs. Therefore canonical P0072 remains **PARTIAL / SOURCE OPEN**, and the frozen source metric remains

`C_P0072: 0 -> 0 (NO MOVEMENT)`.
