Model actually run: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — the model family is exposed by the runtime, but no separately authenticated effort metadata is available.

# NM13-01 / LIVE20 T08 — endpoint-clique reversal cutoff and localized odd-sector resolvent control

**Parent status before:** `OPEN` for Salez Problem 2.3.

**Parent status after:** `OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved.

**Restricted theorem status:** `CANDIDATE_FULL` pending later independent review.

**Publication novelty:** `UNVERIFIED`. The repository and a bounded dated web search were checked for the exact construction below; no matching cutoff theorem was located. This is negative evidence only, not a worldwide priority claim.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Short handoff, correction of the immediately preceding lineage, and partner split

The latest own substantive artifact read before doing new mathematics was

`2026-09-20T16-04-21Z__synchronous-tensor-common-clock-cutoff.md`.

The latest P26 handoff then exposed an important lineage fact that must be preserved rather than papered over: historical R16 had already proved the ordinary synchronous direct/tensor-square theorem with kernel `P tensor P`, at

`runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`.

Therefore the 16:04 synchronous-tensor class is **not counted as a genuinely new class in this run**. Its artifact is left untouched, but the present ledger corrects the progress accounting.

The newest P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_19-01-50__spherical-synchronized-green-transfer.md`.

P26 now has a dependent-shell Green transfer with correlated radial fronts and a synchronized distance-two spherical Cayley class. A nearby P26 construction,

`2026-09-20_15-59-31__partitioned-green-clique-insertion-transfer.md`,

uses the clique-inserted graph on oriented edges with **same-tail** clique edges plus reversal. Earlier NM13-01 work at 07:22 used nonbacktracking predecessor/successor edges plus reversal.

The graph below is different from both:
it has **same-tail clique edges, same-head clique edges, and reversal**. Its reversal-odd spectrum contains slow positive modes inherited from the *negative* base spectrum, which neither of those two constructions has in the same form. This slow odd sector is the mechanism addressed here.

The root `POSTED.md` registry was checked. In particular, the posted Salez Problem 2.4 Abelian-Cayley/product-condition material is not reopened.

## 1. Exact source convention and current primary boundary

Salez, `arXiv:2508.21055` (28 August 2025), embeds a discrete transition matrix `T` in continuous time by inserting independent mean-one exponential waiting times. Hence throughout this report

\[
P_t=e^{t(T-I)}
=e^{-t}\sum_{k\ge0}\frac{t^kT^k}{k!}.
\tag{1.1}
\]

His Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree and one-sided spectral gap bounded away from zero.

The fresh primary boundary checked on 20 September 2026 is still narrower.

* Dylan J. Altschuler, `arXiv:2609.14945` (14 September 2026), proves Gaussian-profile cutoff for every fixed-degree long-range-expander sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}
  \Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Long-range expansion is therefore not interchangeable with Salez's source hypothesis.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345` (6 July 2026), prove a local-product/non-equilibrium-Poincare criterion with window controlled by `gamma_*`; the checked theorem does not derive the needed `gamma_*` bound solely from vertex transitivity plus an ordinary fixed spectral gap.
* Kaufman--Lubotzky, `arXiv:1108.2960`, Theorem 3, give `(q+1)`-regular edge-transitive Ramanujan Cayley graphs on suitable `PSL_2/PGL_2` groups. For the `PGL_2` branch the graph is bipartite. We use `q=5` for an explicit degree-six base family.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was open. NM13-01 already had several source-valid spectral-but-not-LRE cutoff classes, including:

* line graphs of edge-transitive LRE bases;
* nonbacktracking arc variants;
* reversal-augmented predecessor/successor arc graphs;
* finite and growing hidden-memory Cayley lifts;
* an Eisenstein halving/NBRW class.

P26 independently owns Green/spherical-shell transfer mechanisms and several other classes.

### After this run

Salez Problem 2.3 remains open. The proved restricted scope is enlarged by the following class.

> **Theorem A — two-sided endpoint-clique reversal cutoff.**
> Fix `d>=3`. Let `(G_n)` be connected simple `d`-regular **edge-transitive fixed-constant long-range expanders**, with
> \[
> n=|V(G_n)|\to\infty.
> \]
> Let `Y_n=Y(G_n)` have vertex set the oriented edges
> \[
> \vec E(G_n)=\{(u,v):u\sim v\}.
> \]
> From `(u,v)` join:
> 1. every `(u,w)` with `w~u`, `w!=v`  (same-tail clique);
> 2. every `(w,v)` with `w~v`, `w!=u`  (same-head clique);
> 3. the reversal `(v,u)`.
>
> Then `Y_n` is a simple `(2d-1)`-regular vertex-transitive spectral-expander sequence, fails every fixed positive long-range-expansion constant, and rate-one continuous-time SRW in the Salez convention has total-variation cutoff at
> \[
> \boxed{
> T_n=\frac{2d-1}{d-2}\log_{d-1}n
> }
> \tag{2.1}
> \]
> with
> \[
> \boxed{O(\sqrt{\log n})=O(\sqrt{\log |V(Y_n)|})}
> \tag{2.2}
> \]
> window.
>
> If the normalized base gap is at least `gamma`, then
> \[
> \boxed{
> \operatorname{gap}(Y_n)\ge
> \min\left\{
> \frac{d\gamma}{2d-1},
> \frac{2}{2d-1}
> \right\}.
> }
> \tag{2.3}
> \]

For the Kaufman--Lubotzky `q=5` edge-transitive Ramanujan bases (`d=6`), the outputs are degree 11, have `N_n=6n` vertices, and

\[
\boxed{
T_n=\frac{11}{4}\log_5n
=\frac{11}{4}\log_5(N_n/6)
}
\tag{2.4}
\]

with `O(sqrt(log N_n))` window. The Ramanujan bound gives

\[
\gamma_G\ge1-\frac{\sqrt5}{3}
=\frac{3-\sqrt5}{3},
\]

hence

\[
\boxed{
\operatorname{gap}(Y_n)
\ge
\frac{2(3-\sqrt5)}{11}
=0.1388967313\ldots .
}
\tag{2.5}
\]

For the bipartite `PGL_2` branch, the base eigenvalue `-1` produces an exact reversal-odd output eigenvalue `9/11`. That slow positive mode is useful below: it shows that a crude global `L^2` point-source bound genuinely does not prove the required orientation mixing at the cutoff front.

## 3. Construction, simplicity, connectivity and vertex transitivity

For a connected simple `d`-regular graph `G`, define `Y(G)` as in Theorem A.

The three neighbor families are pairwise disjoint.

* A same-tail move `(u,w)` has tail `u`, while the reversal `(v,u)` has tail `v!=u`.
* A same-head move `(w,v)` has head `v`, while the reversal has head `u!=v`.
* If `(u,w)=(x,v)` is simultaneously a same-tail and same-head candidate, then `x=u` and `w=v`, which is the starting arc and is excluded in both lists.

Thus `Y(G)` is simple of degree

\[
(d-1)+(d-1)+1=2d-1.
\tag{3.1}
\]

It is connected because the subgraph containing only same-tail edges and reversal is exactly the clique-inserted graph `L(Sd(G))`, which is connected when `G` is connected.

Let `J` reverse orientation:

\[
J(u,v)=(v,u).
\tag{3.2}
\]

The graph `Y(G)` is invariant under `J`: reversal swaps the same-tail and same-head neighbor families and preserves the reversal matching.

If `G` is edge-transitive, any underlying edge can be sent to any other by an automorphism of `G`. If the resulting orientation is wrong, compose with `J`. Hence the group generated by `Aut(G)` and `J` is transitive on `\vec E(G)`. Therefore `Y(G)` is vertex-transitive under the hypothesis in Theorem A.

This differs structurally from both nearby earlier graphs:

* P26's clique-inserted graph keeps only same-tail edges plus reversal and has degree `d`;
* NM13-01's 07:22 graph uses nonbacktracking successors/predecessors plus reversal and has degree `2d-1`.

On a bipartite base their odd spectra are different: the present graph has the slow eigenvalue `1-2/(2d-1)`, whereas the 07:22 reversal-augmented predecessor/successor graph has a uniformly fast odd sector. Thus this is not a relabeling of that earlier theorem.

## 4. Exact lumping to a lazy line graph

Project an oriented edge to its underlying unoriented edge:

\[
\rho(u,v)=\{u,v\}.
\tag{4.1}
\]

Let `Q` be SRW on `Y(G)` and `Q_L` SRW on the line graph `L(G)`.

From `(u,v)`, each same-tail or same-head move projects to a distinct line-graph neighbor of `{u,v}`, and together these `2(d-1)` moves exhaust all line-neighbors. The reversal projects to a hold.

Therefore `rho` is a strong lumping and the projected discrete kernel is

\[
\boxed{
K=
\frac1{2d-1}I+
\frac{2(d-1)}{2d-1}Q_L.
}
\tag{4.2}
\]

Put

\[
c_d=\frac{2(d-1)}{2d-1}.
\tag{4.3}
\]

Then

\[
K-I=c_d(Q_L-I),
\tag{4.4}
\]

so under the exact source continuous-time convention the projected law at time `t` is exactly the line-graph continuous-time law at time `c_d t`.

The already proved NM13-01 line-graph theorem gives, for the present edge-transitive LRE bases,

\[
T_L=
\frac{2(d-1)}{d-2}\log_{d-1}n,
\qquad
w_L=O(\sqrt{\log n}).
\tag{4.5}
\]

Thus the projected candidate front is

\[
\frac{T_L}{c_d}
=
\boxed{
\frac{2d-1}{d-2}\log_{d-1}n
},
\tag{4.6}
\]

with an `O(sqrt(log n))` projected window. What remains is to show that the hidden orientation defect is negligible on that window.

For completeness, the essential dependency behind (4.5) is the exact incidence factorization from the earlier line-graph report. If `C` sends an edge to a uniformly chosen endpoint and `D` sends a vertex to a uniformly chosen incident edge, then

\[
DC=\frac{I+P}{2},
\qquad
Q_L-I=\frac{d}{d-1}(CD-I).
\tag{4.7}
\]

Combining this intertwining with Altschuler's source-valid LRE cutoff theorem gives (4.5).

## 5. Even/odd reversal decomposition and exact spectrum

Because `JQ=QJ`, functions on oriented edges split into the `J=+1` and `J=-1` sectors.

### 5.1 Even sector

An even function is determined by a function `phi` on unoriented edges:

\[
f(u,v)=\phi(\{u,v\}).
\]

On this sector, `Q` is exactly the lazy line kernel `K` from (4.2).

If `lambda` is a normalized base eigenvalue of `P`, then the corresponding line adjacency eigenvalue is `d lambda+d-2`. Hence the corresponding even eigenvalue of `Q` is

\[
\boxed{
\mu_+(\lambda)
=
\frac{d\lambda+d-1}{2d-1}.
}
\tag{5.1}
\]

The remaining line-cycle eigenvalues are

\[
-\frac1{2d-1}.
\tag{5.2}
\]

If `1-lambda_2(P)>=gamma`, the even-sector gap is therefore at least

\[
\frac{d\gamma}{2d-1}.
\tag{5.3}
\]

### 5.2 Odd sector

For an odd arc function `f`, define tail divergence

\[
(Df)(u)=\sum_{v\sim u}f(u,v),
\tag{5.4}
\]

and for a vertex function `g` define the gradient

\[
(\nabla g)(u,v)=g(u)-g(v).
\tag{5.5}
\]

A direct neighbor sum gives, for odd `f`,

\[
\sum_{\substack{w\sim u\\w\ne v}}f(u,w)
=
Df(u)-f(u,v),
\tag{5.6}
\]

while oddness implies

\[
\sum_{\substack{w\sim v\\w\ne u}}f(w,v)
=
-Df(v)-f(u,v).
\tag{5.7}
\]

The reversal contributes `-f(u,v)`. Therefore

\[
\boxed{
Qf=
\frac{\nabla Df-3f}{2d-1}
\qquad (Jf=-f).
}
\tag{5.8}
\]

Also

\[
\boxed{
D\nabla=d(I-P).
}
\tag{5.9}
\]

Consequently, if `Pg=lambda g` and `g` is nonconstant, then

\[
\boxed{
Q\nabla g
=
\frac{d(1-\lambda)-3}{2d-1}\nabla g.
}
\tag{5.10}
\]

Every divergence-free odd flow (`Df=0`) has eigenvalue

\[
-\frac3{2d-1}.
\tag{5.11}
\]

Since `lambda>=-1`, every odd eigenvalue is at most

\[
\frac{2d-3}{2d-1}
=
1-\frac2{2d-1}.
\tag{5.12}
\]

Thus the odd-sector gap is at least `2/(2d-1)`, proving the second term in (2.3).

For a bipartite base, `lambda=-1` exists and (5.10) attains (5.12). In degree six this is the exact odd eigenvalue `9/11`.

## 6. Why global point-source L2 is insufficient

The slow odd mode matters analytically.

For the degree-six bipartite Ramanujan examples, the odd gap is only

\[
\frac2{11}.
\tag{6.1}
\]

At the candidate cutoff front

\[
T_n=\frac{11}{4}\log_5n,
\tag{6.2}
\]

a generic point-source stationary-`L^2` estimate carries a `sqrt(n)` dimensional prefactor and only gives

\[
\sqrt n\,e^{-(2/11)T_n}
=
n^{\,1/2-1/(2\log 5)}.
\tag{6.3}
\]

Numerically,

\[
\frac12-\frac1{2\log5}
=
0.1893325327\ldots>0.
\tag{6.4}
\]

So the crude bound actually diverges polynomially and yields no orientation mixing information at the cutoff front.

This is the obstruction addressed in the next section: exploit the **localized form of the point-start odd defect**, not the dimension of the full odd representation.

## 7. Localized odd Hodge/resolvent estimate

Fix an oriented edge

\[
a=(u,v),\qquad \bar a=(v,u),
\]

and let

\[
f_0=\delta_a-\delta_{\bar a}.
\tag{7.1}
\]

Then

\[
Df_0=\delta_u-\delta_v=:h.
\tag{7.2}
\]

Assume the normalized base gap is at least `gamma>0`. On mean-zero vertex functions define

\[
g=\frac1d(I-P)^{-1}h
=
\frac1d\int_0^\infty e^{-s(I-P)}h\,ds.
\tag{7.3}
\]

Equation (5.9) gives

\[
D\nabla g=h,
\]

so

\[
c:=f_0-\nabla g
\tag{7.4}
\]

is divergence-free.

From (5.8),

\[
L^-:=Q-I
=
\frac{\nabla D-(2d+2)I}{2d-1}
\qquad\text{on the odd sector}.
\tag{7.5}
\]

Hence the divergence-free part evolves exactly as

\[
e^{tL^-}c
=
e^{-\frac{2d+2}{2d-1}t}c.
\tag{7.6}
\]

For a gradient, use (5.9):

\[
L^-\nabla
=
\nabla\,
\frac{-2I-d(I+P)}{2d-1}.
\tag{7.7}
\]

Therefore

\[
\boxed{
e^{tL^-}\nabla g
=
e^{-\frac{2t}{2d-1}}
\nabla
e^{-\frac{dt}{2d-1}(I+P)}g.
}
\tag{7.8}
\]

The unusual semigroup with `I+P` is harmless in `L^1`. Indeed, for every signed vertex function `z`,

\[
e^{-s(I+P)}
=
e^{-s}\sum_{k\ge0}\frac{(-s)^k}{k!}P^k,
\]

and stochasticity of `P` gives

\[
\boxed{
\|e^{-s(I+P)}z\|_1
\le
e^{-s}\sum_{k\ge0}\frac{s^k}{k!}\|P^kz\|_1
\le
\|z\|_1.
}
\tag{7.9}
\]

Also

\[
\|\nabla z\|_{\ell^1(\vec E)}
\le2d\|z\|_{\ell^1(V)}.
\tag{7.10}
\]

It remains to bound the localized resolvent vector `g`.

The heat semigroup is `L^1`-contractive, so

\[
\|e^{-s(I-P)}h\|_1\le2.
\tag{7.11}
\]

On the mean-zero subspace, the spectral gap gives

\[
\|e^{-s(I-P)}h\|_2
\le
e^{-\gamma s}\|h\|_2
=
\sqrt2\,e^{-\gamma s}.
\tag{7.12}
\]

Thus

\[
\|e^{-s(I-P)}h\|_1
\le
\min\{2,\sqrt{2n}\,e^{-\gamma s}\}.
\tag{7.13}
\]

Split the integral in (7.3) at

\[
s_0=\frac{\log n}{2\gamma}.
\]

Then

\[
\|g\|_1
\le
\frac1d
\left(
2s_0+
\int_{s_0}^\infty
\sqrt{2n}\,e^{-\gamma s}\,ds
\right)
\le
\boxed{
\frac{\log n+\sqrt2}{d\gamma}.
}
\tag{7.14}
\]

Put

\[
L_n=\frac{\log n+2}{\gamma}.
\tag{7.15}
\]

Equations (7.10) and (7.14) give

\[
\|\nabla g\|_1\le2L_n,
\qquad
\|c\|_1\le2+2L_n.
\tag{7.16}
\]

Combining (7.6)--(7.9),

\[
\begin{aligned}
\|e^{tL^-}f_0\|_1
&\le
(2+2L_n)e^{-\frac{2d+2}{2d-1}t}
+
2L_n e^{-\frac2{2d-1}t}\\
&\le
\boxed{
(2+4L_n)e^{-\frac2{2d-1}t}.
}
\end{aligned}
\tag{7.17}
\]

This is the decisive estimate. The full odd space may have dimension `Theta(n)` and may contain the slow eigenvalue in (5.12), but the **specific point-start odd defect costs only `O(log n)` in `L^1`**.

No lower spectral-edge hypothesis is used.

## 8. Exact TV sandwich and cutoff

Let `mu_t^a` be the law on oriented edges at time `t`, started from `a`. Write its reversal-even and reversal-odd parts as

\[
\mu_t^+
=
\frac{\mu_t^a+J\mu_t^a}{2},
\qquad
\mu_t^-=
\frac{\mu_t^a-J\mu_t^a}{2}.
\tag{8.1}
\]

Let `nu_t=rho_*mu_t^a` be the projected law on unoriented edges.

Because `mu_t^+` is `J`-invariant and projects to `nu_t`, it is exactly the uniform-orientation lift of `nu_t`. Uniform stationarity on oriented edges is similarly the uniform-orientation lift of uniform stationarity on base edges. Hence

\[
\boxed{
\|\mu_t^+-\pi_{\vec E}\|_{\rm TV}
=
\|\nu_t-\pi_E\|_{\rm TV}.
}
\tag{8.2}
\]

Moreover,

\[
\mu_t^-=
\frac12 e^{tL^-}f_0.
\tag{8.3}
\]

Projection contracts TV, while the triangle inequality and (8.2)--(8.3) give

\[
\|\nu_t-\pi_E\|_{\rm TV}
\le
\|\mu_t^a-\pi_{\vec E}\|_{\rm TV}
\le
\|\nu_t-\pi_E\|_{\rm TV}
+
\frac14\|e^{tL^-}f_0\|_1.
\tag{8.4}
\]

Using (4.4) and (7.17),

\[
\boxed{
d_L(c_dt)
\le
d_Y(t)
\le
d_L(c_dt)
+
\left(
\frac12+\frac{\log n+2}{\gamma}
\right)
e^{-\frac2{2d-1}t}.
}
\tag{8.5}
\]

Edge transitivity of the base and vertex transitivity of the output make the chosen starts immaterial.

At

\[
t=
T_n+z\sqrt{\log n},
\qquad z=O(1),
\]

equation (2.1) gives

\[
e^{-\frac2{2d-1}t}
=
n^{-\frac{2}{(d-2)\log(d-1)}+o(1)}.
\tag{8.6}
\]

Thus the additive error in (8.5) is `o(1)` uniformly for bounded `z`.

Since `d_L(c_dt)` has cutoff at `T_n` with `O(sqrt(log n))` window by (4.5), (8.5) proves Theorem A.

The argument actually gives more than cutoff: any limiting profile already established for the projected line-graph walk transfers unchanged after the deterministic time rescaling `c_d`, because the orientation error is `o(1)` throughout bounded multiples of the square-root window.

## 9. Spectral expansion and explicit degree-six constants

Combining the even gap (5.3) with the odd gap from (5.12) proves

\[
\operatorname{gap}(Y)
\ge
\min\left\{
\frac{d\gamma}{2d-1},
\frac2{2d-1}
\right\}.
\]

For `d=6`, Ramanujan means every nontrivial normalized eigenvalue away from the bipartite sign satisfies

\[
|\lambda|\le\frac{2\sqrt5}{6}=\frac{\sqrt5}{3}.
\]

Hence

\[
\gamma\ge1-\frac{\sqrt5}{3}
=\frac{3-\sqrt5}{3},
\]

and

\[
\frac{d\gamma}{2d-1}
=
\frac{6}{11}\cdot\frac{3-\sqrt5}{3}
=
\boxed{\frac{2(3-\sqrt5)}{11}}
=
0.138896731363675\ldots.
\tag{9.1}
\]

This is below `2/11`, so it is the displayed uniform gap lower bound.

For the bipartite branch, `lambda=-1` gives from (5.10)

\[
\mu_-(-1)
=
\frac{12-3}{11}
=
\frac9{11}.
\tag{9.2}
\]

Thus the slow odd mode used in Section 6 is exact, not hypothetical.

## 10. Quantitative failure of long-range expansion

Every step of `Y(G)` either

* reverses orientation without changing the underlying base edge, or
* changes the underlying base edge to a line-graph neighbor.

Therefore, for `a` over the base edge `e`,

\[
\rho(B_Y(a,r))
\subseteq
B_{L(G)}(e,r),
\tag{10.1}
\]

and each unoriented edge has exactly two orientations. Hence

\[
|B_Y(a,r)|
\le
2|B_{L(G)}(e,r)|.
\tag{10.2}
\]

The universal `d`-regular tree gives

\[
|B_{L(G)}(e,r)|
\le
1+2\sum_{j=1}^r(d-1)^j
\le
C_d(d-1)^r.
\tag{10.3}
\]

Thus

\[
\boxed{
|B_Y(a,r)|
\le
C'_d(d-1)^r.
}
\tag{10.4}
\]

But `Y` has degree

\[
D=2d-1,
\]

so the long-range-expansion tree benchmark is

\[
(D-1)^r
=
[2(d-1)]^r.
\tag{10.5}
\]

Let `N=|V(Y)|=dn` and choose

\[
r_N=
\left\lfloor
\frac12\log_{2(d-1)}N
\right\rfloor.
\tag{10.6}
\]

At this radius the LRE singleton benchmark is still of order `sqrt(N)`, well below saturation, whereas

\[
\frac{|B_Y(a,r_N)|}{[2(d-1)]^{r_N}}
\le
C'_d\,2^{-r_N}
=
N^{-\beta_d+o(1)}
\tag{10.7}
\]

with

\[
\boxed{
\beta_d=
\frac{\log2}{2\log(2(d-1))}
>0.
}
\tag{10.8}
\]

Therefore no fixed positive LRE constant can hold along the output sequence.

For `d=6`,

\[
\boxed{
\beta_6
=
\frac{\log2}{2\log10}
=
0.150514997831991\ldots.
}
\tag{10.9}
\]

So the new family is genuinely a bounded-degree vertex-transitive **spectral** expander cutoff family outside Altschuler's long-range-expansion hypothesis.

## 11. Mechanism-level obstruction removed

The source-level theorem scope and the mechanism-level progress are distinct.

**Source-level:** Salez Problem 2.3 remains open; Theorem A adds one new restricted class with an explicit square-root window.

**Mechanism-level:** this run removes a specific obstruction that survives ordinary spectral decomposition.

In a transitive lift, a hidden representation sector can be both:

1. high dimensional (`Theta(n)`), and
2. spectrally slow because base eigenvalues near `-1` turn into positive lifted eigenvalues near `1`.

The degree-six bipartite example makes this concrete: the odd lifted eigenvalue is exactly `9/11`, and the standard `sqrt(n) e^{-gap*t}` point-source `L^2` estimate diverges at the true cutoff time.

Nevertheless, that does **not** imply persistent hidden information. The point-start defect has special incidence form `delta_(u,v)-delta_(v,u)`. Hodge decomposition turns it into a divergence-free part plus the gradient of the localized resolvent

\[
\frac1d(I-P)^{-1}(\delta_u-\delta_v),
\]

whose `L^1` mass is only `O(log n)`. The slow negative-spectrum contribution is then controlled by the signed contraction

\[
\|e^{-s(I+P)}\|_{1\to1}\le1.
\]

So:

> **High dimension plus a slow hidden sector is not itself an obstruction to cutoff. A localized start can have only polylogarithmic mass in the relevant Hodge/resolvent geometry, defeating the stationary-dimension `sqrt(n)` penalty.**

This is transitivity/incidence specific and complementary to P26's entropy/Green/spherical-shell program. No shell Green estimate, entropy estimate or radial-front independence is used here.

The remaining general barrier is narrower: an arbitrary vertex-transitive spectral expander need not come with an exact two-orientation incidence complex. A promising next target is the root-stabilizer/Hecke decomposition from the earlier NM13 work: for a localized point-start likelihood defect, prove an analogue of

\[
\|(\text{sector resolvent})(\text{localized defect})\|_1
\le(\log n)^{O(1)}
\]

uniformly over nontrivial stabilizer sectors, rather than paying `sqrt(dim sector)`. That would turn the present Hodge cancellation into a genuinely general transitivity tool.

## 12. Sanity checks

The archived checker performs exact symbolic calculations on `K_4` and `K_{3,3}`.

It verifies:

* strong lumping `Q Rho = Rho K`;
* reversal commutation `QJ=JQ`;
* the exact odd identity
  \[
  Q|_-=(\nabla D-3I)/(2d-1);
  \]
* `D\nabla=d(I-P)`;
* exact even/odd spectra:
  * on `K_4`, even `{1,1/5,-1/5}` with correct multiplicities and odd `{1/5,-3/5}`;
  * on `K_{3,3}`, the bipartite slow odd eigenvalue is `3/5=1-2/5`;
* the finite-state TV sandwich at several times.

It also records the degree-six constants:

\[
D=11,\quad
T/\log_5n=11/4,\quad
\gamma_Y\ge0.1388967313\ldots,
\]

the non-LRE exponent

\[
0.1505149978\ldots,
\]

and the contrast

\[
\frac1{2\log5}=0.3106674672\ldots,
\qquad
\frac12-\frac1{2\log5}=0.1893325327\ldots>0.
\]

The checker ends

`ALL_EXACT_AND_SANITY_CHECKS_PASS`.

These finite calculations are sanity checks only. The asymptotic cutoff theorem is proved analytically in Sections 4--8.

## 13. Handoff

Preserve all prior NM13-01 results, but correct the progress accounting: the 16:04 common-clock tensor result overlaps historical R16 and is not a new class.

The new durable theorem is the endpoint-clique reversal class in Theorem A. Its useful mechanism is not the graph operation itself but the localized odd-sector resolvent estimate (7.17), which succeeds exactly where a global spectral `L^2` estimate fails.

Next transitivity-specific attack:

1. use the canonical stabilizer/Hecke realization from the 14:15 NM13 report;
2. identify localized point-start defects in each nontrivial Hecke sector;
3. seek `L^1` resolvent bounds from ordinary expansion plus bounded local incidence, avoiding any `sqrt(dim)` penalty;
4. keep P26 on conditional Green/radial-shell transfer rather than duplicating it.

No claim is made that this closes Salez Problem 2.3.
