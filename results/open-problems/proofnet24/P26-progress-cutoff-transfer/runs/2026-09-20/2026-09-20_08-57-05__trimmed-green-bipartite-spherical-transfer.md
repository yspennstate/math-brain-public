Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but no authenticated runtime metadata establishes that model/effort setting, so I do not claim otherwise.

# P26 / LIVE20 T08 — trimmed Green-shell transfer with exceptional modes; mixed-parity spherical cutoff on bipartite Ramanujan covers

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem and concrete application below, pending later independent review; `PARTIAL / OPEN` for Salez Problem 2.3. Worldwide publication novelty is `UNVERIFIED`.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and complementary route with historical C28

The newest P26 report before this run was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_07-58-10__ramanujan-spherical-set-transfer.md`.

It proved a spherical-set transfer theorem for high-girth **non-bipartite Ramanujan** bases and, in particular, a distance-`{2,3}` output class. Its next attack was a trimmed Green/entropy criterion which tolerates exceptional spectral modes rather than requiring the whole nontrivial spectrum to lie in the Ramanujan interval.

The live successor of historical C28 is `NM13-01`. Its newest relevant report read in this run is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T05-00-20Z__exact-distance-k-orbit-compression.md`.

NM13-01 proves pure exact-distance-`k` classes and a canonical stabilizer-orbit factor preserving point-start information exactly. Its remaining obstruction is controlling a potentially high-rank transitivity quotient from a spectral gap alone. I therefore do **not** duplicate pure distance powers or the stabilizer quotient. P26 takes the complementary route: quantify how much NBRW Green mass may lie in a small exceptional spectral subspace while still leaving enough time for total-variation cleanup.

This run has two mathematical outputs:

1. a **trimmed Green-shell profile theorem** allowing `M_n` exceptional eigenmodes with `log(1+M_n)=o(sqrt(log n))`; and
2. a proved application to a new class: the distance-`{3,4}` graph of the canonical bipartite double cover of a degree-six high-girth non-bipartite LPS Ramanujan family. The base has a genuine spectral mode `-1` outside the non-bipartite Ramanujan interval, but the mixed-parity output contracts that mode to `2/3`. The output is a 900-regular vertex-transitive spectral expander, is not a fixed-constant long-range expander, and has an explicit Gaussian TV cutoff profile.

No stagnation trigger applies: the previous P26 runs each enlarged proved theorem scope, and this run changes the spectral mechanism rather than producing another receipt.

## 1. Exact source convention and current exact-scope boundary

Justin Salez, arXiv:2508.21055v1 (28 August 2025), defines continuous time by independent mean-one exponential holding times. If `P` is the discrete transition matrix, the semigroup is exactly

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{k\ge0}\frac{t^kP^k}{k!}.
\tag{1.1}
\]

Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here an expander sequence has diverging size, uniformly bounded degree, and one-sided spectral gap bounded away from zero.

Fresh source checks on 20 September 2026 give the following boundary.

* Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026, proves cutoff with explicit Gaussian profile for every fixed-degree long-range-expander sequence. His Definition 1.3 requires, for some fixed `c>0`,
  \[
  |B(S,r)|\ge \min\{3n/4,\;c|S|(d-1)^r\}
  \]
  for every set and radius. He proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range}\Longrightarrow\text{spectral},
  \]
  with neither converse. Long-range expansion is therefore strictly stronger than Salez's hypothesis.
* Francesco Pedrotti--Justin Salez, arXiv:2607.05345 (6 July 2026), prove the local-product/non-equilibrium-Poincare cutoff criterion with window `O(1/gamma_*)`; no checked theorem there derives the needed non-equilibrium constant from vertex transitivity plus an ordinary spectral gap alone.
* Lubotzky--Phillips--Sarnak provide fixed-degree Cayley Ramanujan families with logarithmically growing girth. A non-bipartite degree-six family is enough below; its canonical bipartite double cover is again degree six, vertex-transitive, Ramanujan in the bipartite sense, and has at least the same girth.

A bounded fresh search for `bipartite double cover + cutoff + distance graph`, `distance-3 distance-4 Ramanujan cutoff`, and `spherical graph Ramanujan random walk cutoff` did not recover the mixed-parity class below. This is negative evidence only, not a worldwide priority claim.

The posted Abelian-Cayley/Product-Condition material for Salez Problem 2.4 remains excluded and is not reopened.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. P26's strongest same-vertex Green/spherical theorem required a non-bipartite Ramanujan base, i.e. every nontrivial base eigenvalue was inside the Ramanujan interval. It did not quantify what happens when a small exceptional spectral subspace lies outside that interval.

### After

Salez Problem 2.3 remains `OPEN`, but the proved transfer scope strictly enlarges:

> **Trimmed Green-shell theorem (informal statement).** Let `(G_n)` be fixed-degree vertex-transitive graphs. Suppose all but `M_n` nontrivial eigenvalues lie in the Ramanujan interval and
> \[
> \log(1+M_n)=o(\sqrt{\log n}).
> \]
> For a fixed spherical output kernel `Q_n=F(P_n)` having a uniform spectral gap both on the Ramanujan bulk and on the exceptional modes, the NBRW shell collision cost at the entropic radius is still `exp(o(sqrt(log n)))`. Hence a shell front with `sqrt(log n)` radial fluctuations transfers to a Gaussian total-variation cutoff profile after only `o(sqrt(log n))` spectral cleanup.

The concrete new class is obtained from the canonical bipartite double cover of a non-bipartite degree-six LPS family and the mixed distance set

\[
\boxed{J=\{3,4\}}.
\]

The output graphs are 900-regular, vertex-transitive spectral expanders, fail every fixed long-range-expansion constant, and have rate-one continuous-time cutoff at

\[
\boxed{
T_N=\frac{225}{769}\log_5 N+O(1)
}
\tag{2.1}
\]

with profile

\[
\boxed{
 d_{\rm TV}\!\left(T_N+z\sqrt{\log_5 N}\right)
 \longrightarrow
 \Phi\!\left(-z\sqrt{\frac{909513218}{293371875}}\right)
}
\tag{2.2}
\]

for fixed real `z`, where `N` is the output vertex count.

This theorem-class enlargement, not the checker or commit count, is the substantive movement.

## 3. A quantitative Green-shell cleanup criterion

Let `X` be a finite `D`-regular graph with uniform law `pi`, discrete SRW kernel `Q`, and exact rate-one continuous-time semigroup

\[
S_t=e^{t(Q-I)}.
\tag{3.1}
\]

Assume the one-sided continuous-time gap satisfies

\[
1-\lambda_2(Q)\ge\eta>0.
\tag{3.2}
\]

For any probability law `mu`, write

\[
\chi^2(\mu\|\pi)=\sum_y\frac{(\mu(y)-\pi(y))^2}{\pi(y)}.
\]

Because `S_s` contracts the mean-zero `L^2(pi)` norm by `e^{-eta s}`,

\[
\chi^2(\mu S_s\|\pi)
\le e^{-2\eta s}\chi^2(\mu\|\pi).
\tag{3.3}
\]

By Cauchy--Schwarz,

\[
\|\mu S_s-\pi\|_{\rm TV}
\le \frac12 e^{-\eta s}\sqrt{\chi^2(\mu\|\pi)}.
\tag{3.4}
\]

Now suppose that, for a second fixed-degree transitive graph structure on the same vertex set, there are probability kernels `K_r` and a radial process `R_t` such that point-start laws of the `X` walk have the exact shell representation

\[
\boxed{
\delta_xS_t=\sum_{r\ge0}\Pr(R_t=r)K_r(x,\cdot).
}
\tag{3.5}
\]

Fix a shell threshold `L` and define

\[
C_L:=\sup_{r\ge L}\chi^2(K_r(x,\cdot)\|\pi).
\tag{3.6}
\]

Transitivity makes the right side independent of `x` in our application. Evolve (3.5) for a further time `s` and use convexity of TV, the trivial bound `1` for shells `r<L`, and (3.4) for shells `r>=L`. This gives the exact quantitative upper transfer

\[
\boxed{
 d_X(t+s)
 \le
 \Pr(R_t<L)+\frac12e^{-\eta s}\sqrt{C_L}.
}
\tag{3.7}
\]

This is the Green-function counterpart of the previous entropy-cleanup lemma. It has a particularly transparent window cost: if

\[
g_L:=\log(1+C_L),
\]

then choosing

\[
s=\frac{g_L+u}{2\eta}
\tag{3.8}
\]

makes the second term at most `e^{-u/2}/2` (up to the harmless replacement of `C_L` by `1+C_L`). Therefore any shell collision cost with

\[
\boxed{g_L=o(w_L)}
\tag{3.9}
\]

can be erased inside an `o(w_L)` fraction of a radial window of width `w_L`.

There is a matching geometric lower bound. If each `K_r(x,.)` is supported in a base ball `B_G(x,r)`, then for every `h>=0`,

\[
\boxed{
 d_X(t)
 \ge
 \Pr(R_t\le L-h)-\pi(B_G(x,L-h)).
}
\tag{3.10}
\]

Indeed take the test set `B_G(x,L-h)`.

Consequently, if `L_n->infinity`, `w_n->infinity`, `g_{L_n}=o(w_n)`, `pi(B_G(x,L_n-h_n))->0` for some `h_n->infinity` with `h_n=o(w_n)`, and the radial front obeys

\[
\Pr\!\left(R_{L_n/v+zw_n}<L_n\right)
\to \Phi(-z/\tau),
\tag{3.11}
\]

uniformly under `o(w_n)` time/radius perturbations, then (3.7)--(3.10) yield

\[
\boxed{
 d_X(L_n/v+zw_n)\to\Phi(-z/\tau).
}
\tag{3.12}
\]

This is the transfer criterion used below.

## 4. Trimming exceptional spectrum in the NBRW Green function

Let now `G_n` be `d`-regular and vertex-transitive on `N_n` vertices. Put `q=d-1` and let `P_n` be normalized adjacency. Let `K_r` be the length-`r` NBRW endpoint kernel. As in the preceding P26 reports,

\[
K_r=p_r(P_n),
\tag{4.1}
\]

where

\[
p_0=1,\qquad p_1=x,\qquad
p_{r+1}(x)=\frac d q x p_r(x)-\frac1q p_{r-1}(x).
\tag{4.2}
\]

Because `K_r` is symmetric and stochastic,

\[
|p_r(\lambda_i)|\le1
\tag{4.3}
\]

for every actual eigenvalue `lambda_i` of `P_n`.

Let

\[
\rho_d:=\frac{2\sqrt q}{d}
\]

and suppose that, besides the stationary eigenvalue `1`, at most `M_n` eigenvalues lie outside `[-rho_d,rho_d]`. Call them **exceptional modes**. For bulk eigenvalues in the Ramanujan interval the Chebyshev form gives

\[
|p_r(\lambda)|\le C_d(r+1)q^{-r/2}.
\tag{4.4}
\]

Transitivity and symmetry give the exact Green trace identity

\[
\chi^2(K_r(x,\cdot)\|\pi)
=N_n\sum_yK_r(x,y)^2-1
=\operatorname{tr}(K_r^2)-1
=\sum_{i=2}^{N_n}p_r(\lambda_i)^2.
\tag{4.5}
\]

Using (4.3) on the exceptional modes and (4.4) on the bulk,

\[
\boxed{
\chi^2(K_r\|\pi)
\le M_n+C_d^2N_n(r+1)^2q^{-r}.
}
\tag{4.6}
\]

Set

\[
L_n=\lceil\log_qN_n\rceil.
\tag{4.7}
\]

For all sufficiently large `n`, `(r+1)^2q^{L_n-r}` decreases for `r>=L_n` up to a fixed harmless factor, hence

\[
\boxed{
C_{L_n}
\le M_n+C'_dL_n^2.
}
\tag{4.8}
\]

Therefore

\[
\boxed{
\log(1+C_{L_n})
\le O_d(\log L_n)+\log(1+M_n).
}
\tag{4.9}
\]

In particular, the collision cleanup cost is `o(sqrt(L_n))` whenever

\[
\boxed{
\log(1+M_n)=o(\sqrt{L_n}).
}
\tag{4.10}
\]

This is the promised trimmed Green criterion. It permits far more than a constant number of outliers: `M_n` may grow as `exp(o(sqrt(log n)))`.

## 5. Spherical output kernels with exceptional modes

Fix a nonempty finite distance set `J subset {1,...,m}`. Assume `girth(G_n)>2m` eventually. Then the exact-distance-`j` graph has degree

\[
D_j=dq^{j-1}
\tag{5.1}
\]

and SRW kernel exactly `K_j`. Hence the union-of-spheres graph has degree

\[
D_J=\sum_{j\in J}D_j,
\]

and kernel

\[
\boxed{
Q_J=\sum_{j\in J}w_jK_j=F_J(P_n),
\qquad
w_j=D_j/D_J,
\qquad
F_J=\sum_{j\in J}w_jp_j.
}
\tag{5.2}
\]

Suppose

\[
\sup_{|x|\le\rho_d}|F_J(x)|\le\beta_{\rm bulk}<1
\tag{5.3}
\]

and every exceptional eigenvalue obeys

\[
|F_J(\lambda_i)|\le\beta_{\rm exc}<1.
\tag{5.4}
\]

Then every nonconstant output eigenvalue has modulus at most

\[
\beta:=\max(\beta_{\rm bulk},\beta_{\rm exc})<1,
\]

so the continuous-time gap is at least

\[
\eta=1-\beta>0.
\tag{5.5}
\]

The exact shell representation needed in (3.5) follows from spherical polynomial algebra and does **not** lose the exceptional modes. On the infinite `d`-regular tree, let the discrete output step choose shell length `j` with probability `w_j` and then a uniformly random vertex at distance `j`. If `R_m` is its radius after `m` steps, radial isotropy gives

\[
F_J(P_T)^m=\sum_r\Pr(R_m=r)p_r(P_T).
\]

The spectrum of `P_T` contains an interval, so this is a polynomial identity. Substituting `P_n` yields

\[
Q_J^m=\sum_r\Pr(R_m=r)K_r.
\tag{5.6}
\]

Poissonizing at rate one gives the exact Salez-convention identity

\[
\boxed{
 e^{t(Q_J-I)}
 =\sum_r\Pr(R_t=r)K_r.
}
\tag{5.7}
\]

Thus Sections 3--4 apply verbatim.

## 6. Concrete class: bipartite double covers and `J={3,4}`

Take a non-bipartite degree-six high-girth LPS Ramanujan Cayley family `(G_n)`, with normalized transition kernel `P_n`. Form its canonical bipartite double cover `B_n`:

\[
V(B_n)=V(G_n)\times\{0,1\},
\]

and

\[
(x,i)\sim(y,1-i)\quad\Longleftrightarrow\quad x\sim y\text{ in }G_n.
\tag{6.1}
\]

If `G_n=Cay(Gamma_n,S_n)`, then

\[
B_n=Cay(\Gamma_n\times\mathbb Z_2,\{(s,1):s\in S_n\}),
\]

so `B_n` is vertex-transitive Cayley. Covering maps are local isomorphisms, so

\[
\operatorname{girth}(B_n)\ge\operatorname{girth}(G_n)\to\infty.
\tag{6.2}
\]

The normalized adjacency of the cover is the block matrix

\[
\widetilde P_n=
\begin{pmatrix}0&P_n\\P_n&0\end{pmatrix},
\]

so its spectrum is exactly

\[
\{\pm\lambda_i(P_n)\}.
\tag{6.3}
\]

Because `G_n` is non-bipartite Ramanujan, all these eigenvalues except `+1` and `-1` lie in

\[
[-\sqrt5/3,\sqrt5/3].
\]

Thus, relative to the non-bipartite Ramanujan bulk interval, `B_n` has exactly

\[
\boxed{M_n=1}
\tag{6.4}
\]

exceptional nonstationary mode, namely `-1`. This is the minimal nontrivial test of the trimmed theorem: the old P26 theorem excluded it, while (4.8) handles it with only constant extra Green mass.

Now define `X_n` on `V(B_n)` by joining vertices whose `B_n`-distance is either three or four. For large `n`, `girth(B_n)>8`, so the two spheres are disjoint and geodesically unique. With `d=6,q=5`,

\[
D_3=6\cdot5^2=150,
\qquad
D_4=6\cdot5^3=750,
\]

hence

\[
\boxed{D_X=900},
\qquad
w_3=1/6,
\qquad
w_4=5/6.
\tag{6.5}
\]

The spherical polynomials are

\[
p_3(x)=\frac{36x^3-11x}{25},
\qquad
p_4(x)=\frac{216x^4-96x^2+5}{125},
\tag{6.6}
\]

and

\[
F(x)=\frac16p_3(x)+\frac56p_4(x).
\tag{6.7}
\]

On the exceptional bipartition mode,

\[
\boxed{F(-1)=\frac{-1+5}{6}=\frac23}.
\tag{6.8}
\]

On the Ramanujan bulk, the standard envelope

\[
|p_r(x)|\le 5^{-r/2}\frac{2+4(r+1)}6
\]

gives

\[
|p_3(x)|\le\frac{3}{5\sqrt5},
\qquad
|p_4(x)|\le\frac{11}{75}.
\]

Therefore

\[
\beta_{\rm bulk}
\le\frac{1}{10\sqrt5}+\frac{11}{90}
<\frac23.
\tag{6.9}
\]

Combining (6.8)--(6.9), every nonconstant eigenvalue of `X_n` has modulus at most `2/3`. Hence

\[
\boxed{\operatorname{gap}(X_n)\ge1/3}.
\tag{6.10}
\]

In particular the mixed-parity distance graph is connected and non-bipartite even though the base cover is bipartite.

## 7. Green cost and exact radial profile

Let `N=|V(B_n)|=|V(X_n)|` and

\[
L_N=\lceil\log_5N\rceil.
\]

By (4.8) with `M_n=1`,

\[
C_{L_N}\le1+C L_N^2,
\qquad
\log(1+C_{L_N})=O(\log\log N).
\tag{7.1}
\]

Since the output gap is at least `1/3`, choose for example

\[
s_N=10\log\log N.
\]

Then `s_N=o(sqrt(log N))` and the cleanup term in (3.7) tends to zero.

It remains to compute the radial front. On `T_6`, once the current radius is at least four, a uniformly chosen distance-three endpoint has radial increments and multiplicities

\[
3:125,\quad 1:20,\quad -1:4,\quad -3:1,
\]

while a uniformly chosen distance-four endpoint has

\[
4:625,\quad 2:100,\quad 0:20,\quad -2:4,\quad -4:1.
\]

Because the output chooses uniformly among all `900` distance-three/four neighbors, the combined interior increment table is

\[
\begin{array}{c|rrrrrrrrr}
\xi&-4&-3&-2&-1&0&1&2&3&4\\\hline
\#&1&1&4&4&20&20&100&125&625.
\end{array}
\tag{7.2}
\]

Thus

\[
\boxed{
v:=\mathbb E\xi=\frac{769}{225}},
\qquad
\boxed{
M_2:=\mathbb E\xi^2=\frac{1159}{90}}.
\tag{7.3}
\]

The radial chain differs from the compound-Poisson sum of i.i.d. increments `xi` only inside the finite boundary set `{0,1,2,3}`. Since `v>0`, for sufficiently small `theta>0`,

\[
\mathbb E e^{-\theta\xi}<1.
\]

The usual exponential supermartingale outside the boundary gives an exponentially decaying return probability from large radius. Repeatedly restart when the chain exits the boundary: each excursion has a fixed positive probability of never returning, so the number of boundary excursions has a geometric tail. After the final boundary excursion, the walk can be coupled to a fresh i.i.d. increment sequence, and the accumulated boundary correction is tight. Therefore the finite-boundary perturbation does not affect the `sqrt(t)` CLT:

\[
\frac{R_t-vt}{\sqrt{M_2t}}\Longrightarrow N(0,1).
\tag{7.4}
\]

Equivalently, at

\[
t_N(z)=\frac{L_N}{v}+z\sqrt{L_N},
\]

\[
\Pr(R_{t_N(z)}<L_N)
\longrightarrow
\Phi\!\left(-z\frac{v^{3/2}}{\sqrt{M_2}}\right).
\tag{7.5}
\]

The base-ball term needed for the lower bound is automatic:

\[
|B_{B_n}(x,L_N-h)|\le C5^{L_N-h},
\]

so, for any `h_N->infinity`,

\[
\pi(B_{B_n}(x,L_N-h_N))=O(5^{-h_N})\to0.
\tag{7.6}
\]

Take `h_N=o(sqrt(L_N))`. Combining (3.7), (3.10), (7.1), (7.4)--(7.6) gives the full profile

\[
\boxed{
 d_{X_n}\!\left(
 \frac{225}{769}L_N+z\sqrt{L_N}
 \right)
 \longrightarrow
 \Phi\!\left(-z\sqrt{\frac{909513218}{293371875}}\right).
}
\tag{7.7}
\]

Indeed

\[
\frac{M_2}{v^3}
=\frac{293371875}{909513218}.
\tag{7.8}
\]

This proves cutoff with a `Theta(sqrt(log N))` window in the exact rate-one continuous-time convention.

## 8. The output class is spectral but not long-range

The output degree is `D_X=900`, so its LRE tree branching benchmark is

\[
q_X=D_X-1=899.
\]

Every output step moves at most four edges in the degree-six base cover. Consequently

\[
B_{X_n}(x,r)\subseteq B_{B_n}(x,4r)
\]

and the universal-tree degree bound gives

\[
|B_{X_n}(x,r)|\le C5^{4r}=C625^r.
\tag{8.1}
\]

If a fixed `c>0` made `(X_n)` a `c`-long-range-expander sequence in Altschuler's Definition 1.3, apply the condition to `S={x}` and

\[
r_N=\left\lfloor\frac12\log_{899}N\right\rfloor.
\]

For large `N`, the LRE minimum is the second term and would require

\[
|B_{X_n}(x,r_N)|\ge c899^{r_N}.
\]

But (8.1) gives

\[
\frac{|B_{X_n}(x,r_N)|}{899^{r_N}}
\le C\left(\frac{625}{899}\right)^{r_N}
\longrightarrow0,
\]

a contradiction. Thus

\[
\boxed{(X_n)\text{ is not a fixed-constant long-range-expander sequence}.}
\tag{8.2}
\]

The cutoff theorem above is therefore not an application of Altschuler's output hypothesis under a different name.

## 9. Exact executed sanity check

The exact checker is

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_08-57-05__trimmed_green_bipartite_spherical.py`

created at commit

`8c052522a8cf6931a78c32f36fac6820d368fc8d`.

Its archived executed output is

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_08-57-05__trimmed_green_bipartite_spherical.out`

created at commit

`37092199c3060797c8ad6aa13efc9480f4d142d7`.

It exactly verifies the spherical polynomial recurrence for `p_3,p_4`, the degrees and weights, `F(-1)=2/3`, the bulk envelope being strictly below `2/3`, all nine radial multiplicities, the exact drift and second moment, the profile constant, and `625<899`. The terminal marker is

`P26_T08_TRIMMED_GREEN_BIPARTITE_SPHERICAL_EXACT_PASS`.

The checker is a sanity check of the finite algebra; the theorem proof is on this page.

## 10. Failed/avoided routes and residual obstruction

### Avoided route 1: force global output-NBRW `L^2`

NM13-01 already produced a transitive cutoff family whose raw output NBRW collision trace is polynomially large at the nominal entropic radius. Therefore a universal theorem of the form “transitivity + spectral expansion implies small output-NBRW `L^2` trace” is too strong. This run instead trims a small exceptional spectral subspace in the **base shell law** and uses output spectral cleanup.

### Avoided route 2: hide the bipartite eigenvalue inside the word “Ramanujan”

Altschuler's Ramanujan definition explicitly allows the exceptional eigenvalue `-1` in the bipartite case. For the transfer mechanism here that mode cannot be ignored: a pure even-distance output would preserve it at `+1` and disconnect. The mixed-parity set `{3,4}` is chosen precisely so that the exceptional mode is contracted to `2/3`. This is a real spectral condition, not terminology.

### Residual parent obstruction

The criterion now tolerates `exp(o(sqrt(log n)))` exceptional eigenmodes, but a general vertex-transitive spectral expander can have a positive fraction of its spectrum outside the Ramanujan interval. The remaining gap toward Salez Problem 2.3 is therefore:

\[
\boxed{
\text{control the information/Green contribution of a 
large exceptional spectral subspace using transitivity itself.}
}
\]

Counting exceptional eigenvalues is insufficient once `M_n` is polynomial in `n`.

## 11. Next attack

Stay complementary to NM13-01's stabilizer-orbit/direct-transitivity route. P26's next attack is a **weighted trimmed Green criterion** replacing the crude exceptional count

\[
\sum_{i\in E}p_r(\lambda_i)^2\le |E|
\]

by a spectral-density integral weighted by the actual NBRW polynomial decay. The target is to prove cutoff whenever the exceptional empirical spectral measure satisfies a moderate-deviation estimate of the form

\[
\sum_{i:\,|\lambda_i|>\rho_d+\delta}
 p_{L_n}(\lambda_i)^2
\le \exp(o(\sqrt{\log n})),
\]

while allowing polynomially many exceptional eigenvalues. A successful version would materially approach arbitrary transitive spectral expanders and is designed not to require raw output-NBRW `L^2` control.

## 12. ledger_delta

```yaml
parent: T08 Salez arXiv:2508.21055 Problem 2.3
parent_before: OPEN/PARTIAL
parent_after: OPEN/PARTIAL
source_level_movement:
  - proved trimmed Green-shell TV profile transfer with log(1+M_n)=o(sqrt(log n)) exceptional-mode allowance
  - proved new mixed-parity spherical class on bipartite double covers of high-girth LPS bases
  - new output: degree 900 vertex-transitive spectral expanders, non-LRE, Gaussian cutoff profile
mechanism_advance:
  - quantitative inequality d_X(t+s) <= P(R_t<L) + (1/2)e^{-eta s}sqrt(C_L)
  - exact trimmed trace bound C_L <= M_n + O((log n)^2)
  - exceptional bipartition mode -1 is explicitly contracted to 2/3 by J={3,4}
continuous_time_convention: H_t = exp(t(Q-I)), rate-one Poissonization
application:
  base: canonical bipartite double cover of non-bipartite degree-6 high-girth LPS Ramanujan family
  output_distance_set: {3,4}
  output_degree: 900
  output_gap_lower_bound: 1/3
  output_not_LRE: true
  radial_drift: 769/225
  radial_second_moment_rate: 1159/90
  cutoff_center: (225/769) log_5 N + O(1)
  profile_tau_squared: 293371875/909513218
  profile: Phi(-z sqrt(909513218/293371875))
status_restricted: CANDIDATE_FULL_PENDING_REVIEW
worldwide_novelty: UNVERIFIED
companion: NM13-01 (historical C28 successor)
companion_split: NM13-01 stabilizer-orbit/direct transitivity; P26 trimmed base-shell Green transfer
stagnation_trigger: no
checker_commit: 8c052522a8cf6931a78c32f36fac6820d368fc8d
checker_output_commit: 37092199c3060797c8ad6aa13efc9480f4d142d7
next_attack: weighted exceptional spectral-density Green bound allowing polynomially many outliers
```

End of complete P26 substantive T08 report.
