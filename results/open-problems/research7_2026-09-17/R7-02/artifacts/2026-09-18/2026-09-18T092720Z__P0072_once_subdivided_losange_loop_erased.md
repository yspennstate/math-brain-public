# P0072 — loop-erased once-subdivided losange: exact extinction theorem

Status: **restricted theorem / PROVED CANDIDATE after self-review; full canonical P0072 remains OPEN; publication novelty UNVERIFIED.**

This note continues R7-02 after the STUCK1 diagnosis. It settles the loop-erased ant process on the first clean graph outside both previously solved loop-erased classes used by this track: take the five-edge losange and subdivide one edge of one branch once.

## 1. Graph and exact path-count coordinates

Let the terminals be `s,t`, and let the graph have vertices `s,x,a,b,t` and edges
\[
sx,\ xa,\ at,\ sb,\ bt,\ ab.
\]
All six original edge weights start at one. The unique graph geodesic is
\[
R:s-b-t,
\]
of length two. The other possible loop-erased simple `s`-`t` paths are
\[
L:s-x-a-t,\qquad
A:s-x-a-b-t,\qquad
B:s-b-a-t.
\]
Thus every edge of `L,A,B` that is not one of `sb,bt` is non-geodesic.

After `n` ants let `L,A,B,R` also denote the numbers of reinforced paths of those four types. Then
\[
L+A+B+R=n.
\]
The two series edges `sx,xa` always receive reinforcement together, so their common raw weight is
\[
u=1+L+A.
\]
Put
\[
v=1+L+B,\quad
w=1+A+B,\quad
d=1+R+B,\quad
e=1+R+A,
\]
for the weights of `at,ab,sb,bt` respectively. Hence, with
\[
t=n+2,
\]
we have the exact conservation identities
\[
u+d=t,\qquad v+e=t.
\]

## 2. B6 — exact deformation to an anisotropic losange

Suppress the degree-two vertex `x`. For weighted spanning trees, series reduction at `x` multiplies the reduced-tree partition function by the irrelevant factor `W_{sx}+W_{xa}=2u` and replaces the chain by one edge of conductance
\[
g=\frac{u\cdot u}{u+u}=\frac u2.
\]
Therefore the law of the `s`-`t` path in the weighted UST, and hence the source loop-erased reinforcement law, is exactly the law on the ordinary five-edge losange with conductances
\[
(g,v,w,d,e)=\left(\frac u2,v,w,d,e\right).
\]
When the reduced edge is reinforced its conductance increases by `1/2`; all other reduced edges increase by `1`. Thus this is precisely the anisotropic `lambda=1/2` deformation isolated in the preceding STUCK1 report.

For the reduced losange the weighted spanning-tree partition function is
\[
Z=gvw+gvd+gve+gwe+gde+vwd+vde+wde.
\]
The four possible UST `s`-`t` path probabilities are therefore
\[
q_L=\frac{gv(w+d+e)}Z,\qquad
q_A=\frac{gwe}Z,\qquad
q_B=\frac{vwd}Z,\qquad
q_R=\frac{de(g+v+w)}Z.
\]
These identities follow by enumerating the eight spanning trees of the five-edge losange; the two excluded three-edge subsets are its two triangles.

## 3. The exact non-geodesic-mass Lyapunov function

Define
\[
S=u+v+w,\qquad V=\frac{S}{t}.
\]
Because every non-right path `L,A,B` reinforces exactly two of `u,v,w`, whereas the geodesic path `R` reinforces none of them,
\[
S=3+2(L+A+B)=2n+3-2R.
\]
Consequently
\[
\boxed{V=2-\frac{2R+1}{t}.}
\tag{3.1}
\]

If `J_{n+1}` equals two on a non-right reinforcement and zero on a right reinforcement, then
\[
V_{n+1}-V_n=\frac{J_{n+1}-V_n}{t+1}.
\]
Conditioning on the current state gives
\[
\mathbb E[V_{n+1}-V_n\mid\mathcal F_n]
=-\frac{2\Delta_n}{t+1},
\qquad
\Delta_n:=q_R-\frac{R+1/2}{t}.
\tag{3.2}
\]

### Lemma 3.1 — exact strict drift

For every finite state,
\[
\boxed{\Delta_n>0.}
\tag{3.3}
\]

### Proof

Substitute the count formulas above into `q_R`. Exact simplification gives
\[
\Delta_n=\frac{P(L,A,B,R)}{4tZ},
\]
where `Z>0` and
\[
\begin{aligned}
P={}&6A^3B+4A^3R+5A^3+14A^2B^2+12A^2BL+14A^2BR+36A^2B\\
&+6A^2LR+9A^2L+4A^2R^2+20A^2R+20A^2\\
&+8AB^3+14AB^2L+14AB^2R+40AB^2+6ABL^2+12ABLR+38ABL\\
&+4ABR^2+38ABR+57AB+2AL^2R+4AL^2+2ALR^2+16ALR+20AL\\
&+7AR^2+27AR+24A+4B^3R+6B^3+6B^2LR+10B^2L\\
&+4B^2R^2+20B^2R+22B^2+2BL^2R+4BL^2+4BLR^2+18BLR+21BL\\
&+8BR^2+28BR+25B+2L^2R^2+4L^2R+3L^2+5LR^2+13LR+10L\\
&+5R^2+13R+9.
\end{aligned}
\]
Every coefficient is strictly positive and `L,A,B,R` are nonnegative integers. Hence `P>0`. ∎

Two immediate consequences are important.

First, `V_n` is a bounded nonnegative strict supermartingale, so
\[
V_n\to V_\infty\quad\text{a.s.}
\tag{3.4}
\]
and the Doob compensator is finite:
\[
\sum_n\frac{\Delta_n}{t_n}<\infty
\quad\text{a.s.}
\tag{3.5}
\]
(up to the immaterial replacement of `t_n+1` by `t_n`).

Second, since
\[
q_R=\frac{R+1/2}{t}+\Delta_n>\frac1{2t},
\]
we have
\[
\sum_n q_R(n)=\infty.
\]
Lévy's conditional Borel--Cantelli lemma therefore gives
\[
\boxed{R_n\to\infty\quad\text{a.s.}}
\tag{3.6}
\]

## 4. B20 — where the Lyapunov algorithm stops

The strict finite-state drift does not by itself imply `V_\infty=0`, because its leading drift vanishes on bad projective boundary faces.

Let
\[
\ell=\frac Lt,\qquad \alpha=\frac At,\qquad
\beta=\frac Bt,\qquad \rho=\frac Rt.
\]
Every subsequential limit lies in the simplex
\[
\ell+\alpha+\beta+\rho=1,\qquad
\ell,\alpha,\beta,\rho\ge0.
\]

The homogeneous degree-four part of the numerator `P` is
\[
\begin{aligned}
P_4=2(&3A^3B+2A^3R+7A^2B^2+6A^2BL+7A^2BR+3A^2LR+2A^2R^2\\
&+4AB^3+7AB^2L+7AB^2R+3ABL^2+6ABLR+2ABR^2\\
&+AL^2R+ALR^2+2B^3R+3B^2LR+2B^2R^2+BL^2R+2BLR^2+L^2R^2).
\end{aligned}
\tag{4.1}
\]
Every coefficient is positive, so its zero set on the simplex is exactly
\[
\boxed{
\{\rho=1\}
\;\cup\;
\{\rho=0,\ \alpha=0\}
\;\cup\;
\{\rho=0,\ \beta=0\}.
}
\tag{4.2}
\]

A standard slow-motion excursion argument upgrades (3.5) to the assertion that every projective limit point belongs to (4.2): if a limit point had `P_4>0`, then in a small neighborhood `\Delta_n` would be bounded below by a positive constant for all large `n`; the normalized count vector moves only `O(1/t_n)` per step, so every return to a smaller neighborhood would force an `O(1)` contribution to the divergent harmonic-time sum, contradicting (3.5).

By (3.1),
\[
V_\infty=2(1-\rho_\infty)
\]
along every convergent subsequence. Since `V_n` itself converges, (4.2) implies the dichotomy
\[
\boxed{V_\infty\in\{0,2\}.}
\tag{4.3}
\]
The value `0` is the desired geodesic face. The only remaining possibility is `V_\infty=2`, equivalently
\[
\rho_n=R_n/t_n\to0,
\]
with the projective state approaching the union of the two bad boundary edges in (4.2).

This is the exact place where the naive Lyapunov algorithm fails.

## 5. B29 — blow up the bad boundary and compute the invasion factor

We now compactify the bad boundary by comparing the vanishing right count with the other vanishing path count.

Use the homogeneous conductances associated with path proportions:
\[
g=\frac{\ell+\alpha}{2},\quad
v=\ell+\beta,\quad
w=\alpha+\beta,\quad
d=\rho+\beta,\quad
e=\rho+\alpha.
\]
The homogeneous right-path probability is still
\[
q_R^{(\infty)}
=\frac{de(g+v+w)}
 {gvw+gvd+gve+gwe+gde+vwd+vde+wde}.
\]

### Lemma 5.1 — uniform projective invasion

For any sequence of finite states satisfying
\[
R\to\infty,\qquad R/t\to0,
\]
and whose normalized path-count vector approaches the bad set
\[
\{\rho=0,\alpha=0\}\cup\{\rho=0,\beta=0\},
\]
one has
\[
\boxed{\liminf \frac{t\,q_R}{R}\ge\frac32.}
\tag{5.1}
\]

### Proof

There are three projective charts.

1. On the interior of the face `\beta=0`, write `B/R\to k\in[0,\infty]` and let `\alpha` denote the limiting `A/t`, so `\ell+\alpha=1`. Direct substitution and division by `\rho=R/t` gives, for finite `k`,
\[
\frac{q_R}{\rho}\longrightarrow
\frac{3(k+1)}{2-\alpha}\ge\frac32.
\tag{5.2}
\]
If `k=\infty`, the ratio diverges.

2. On the interior of the face `\alpha=0`, write `A/R\to k` and let `\beta=B/t`, so `\ell+\beta=1`. Then
\[
\frac{q_R}{\rho}\longrightarrow
\frac{(\beta+3)(k+1)}2\ge\frac32,
\tag{5.3}
\]
again with divergence when `k=\infty`.

3. At their intersection, the pure-`L` vertex, put
\[
A/R\to k_A,\qquad B/R\to k_B.
\]
Then
\[
\frac{q_R}{\rho}\longrightarrow
\frac{3(k_A+1)(k_B+1)}
     {2(k_A+k_B+1)}
=
\frac32\left(1+\frac{k_Ak_B}{k_A+k_B+1}\right)
\ge\frac32.
\tag{5.4}
\]
The same lower bound persists if one of the ratios diverges, by taking the corresponding limit.

These charts cover the entire bad set. ∎

## 6. A supercritical birth lemma

We use the following elementary conditional-growth fact.

### Lemma 6.1

Let `N_n` be a nondecreasing integer process with increments in `{0,1}`, conditional increment probability `p_n`, and deterministic scale `t_n=n+O(1)`. Assume
\[
N_n\to\infty,\qquad N_n/t_n\to0,
\]
and for some `c>1`,
\[
p_n\ge c\,\frac{N_n}{t_n}
\]
eventually. Then these assumptions are incompatible.

### Proof

Let `H_m=\sum_{j=1}^m j^{-1}`. When `N` jumps from `m` to `m+1`,
\[
H_{m+1}-H_m=\frac1{m+1}.
\]
Thus
\[
H_{N_n}=M_n+
\sum_{k<n}\frac{p_k}{N_k+1},
\]
where `M_n` is a martingale. Since `N_k\to\infty`, for every `c'` with `1<c'<c`,
\[
\frac{p_k}{N_k+1}\ge\frac{c'}{t_k}
\]
eventually. Hence the predictable term is at least
\[
c'\log n+O(1).
\]

Moreover,
\[
\mathbb E[(\Delta M_k)^2\mid\mathcal F_k]
\le
\frac{p_k}{(N_k+1)^2}.
\]
Relative to the predictable sum, this quadratic variation has an extra factor `(N_k+1)^{-1}\to0`; the standard square-integrable martingale strong law therefore gives
\[
M_n=o(\log n)\quad\text{a.s.}
\]
on the event under consideration. Consequently
\[
H_{N_n}\ge(c'-o(1))\log n.
\]
But `N_n\le n+O(1)`, so
\[
H_{N_n}\le\log n+O(1),
\]
contradicting `c'>1`. ∎

## 7. The once-subdivided losange theorem

### Theorem 7.1

For the source loop-erased ant process on the six-edge graph
\[
sx,\ xa,\ at,\ sb,\ bt,\ ab
\]
with unit initial weights,
\[
\frac{W_{sx}(n)}n,\;
\frac{W_{xa}(n)}n,\;
\frac{W_{at}(n)}n,\;
\frac{W_{ab}(n)}n
\longrightarrow0
\qquad\text{a.s.},
\]
while
\[
\frac{W_{sb}(n)}n,\;
\frac{W_{bt}(n)}n
\longrightarrow1
\qquad\text{a.s.}
\]
Thus the only linearly growing edges are exactly the two edges of the unique geodesic `s-b-t`.

### Proof

By Lemma 3.1 and Doob convergence, `V_n` has an almost-sure limit. Sections 4--5 show that either `V_\infty=0` or else `V_\infty=2`, and in the latter case the normalized path-count vector approaches the bad boundary while `R_n/t_n\to0`.

But (3.6) gives `R_n\to\infty`. Under the hypothetical `V_\infty=2`, Lemma 5.1 therefore yields, for example,
\[
q_R(n)\ge\frac54\,\frac{R_n}{t_n}
\]
for all sufficiently large `n`. Lemma 6.1 with `N_n=R_n` and `c=5/4` is a contradiction. Hence
\[
V_\infty=0.
\]

Since
\[
V_n=\frac{u_n+v_n+w_n}{t_n}
\]
and all three summands are nonnegative,
\[
u_n/t_n\to0,\qquad v_n/t_n\to0,\qquad w_n/t_n\to0.
\]
The two original series edges `sx,xa` both have weight `u_n`; `at` has weight `v_n`; and `ab` has weight `w_n`. Finally,
\[
d_n/t_n=1-u_n/t_n\to1,\qquad
e_n/t_n=1-v_n/t_n\to1.
\]
Replacing `t_n=n+2` by `n` does not alter the limits. ∎

## 8. Scope and what remains

This is a genuine source-relevant restricted theorem. It proves the loop-erased source conclusion on a six-edge graph obtained by one subdivision of the five-edge non-series-parallel losange. It is beyond the distance-two suspension theorem in the same R7-02 root, and its proof uses the exact projective boundary-invasion mechanism diagnosed in STUCK1.

It does **not** resolve canonical P0072:
- arbitrary finite graphs remain open in this track;
- the uniform-geodesic source rule remains separately open outside the already-published special classes;
- publication novelty of this six-edge theorem is UNVERIFIED pending broader literature review.

The frozen full-source metric therefore remains `C_P0072=0`.
