Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — the model family is authenticated by the runtime, but no separate authenticated maximum-effort metadata is exposed.

# P26 / LIVE20 T08 — quantitative Berry–Green transfer and Hermitianized two-step NBRW edge graphs

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The restricted proved class is strictly enlarged; the parent conjecture is not claimed solved.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–D and the explicit degree-32 class below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded fresh search for combinations of `symmetrized nonbacktracking`, `Hermitian Hashimoto`, `edge graph`, `biregular Ramanujan`, and `cutoff` found nonbacktracking-spectral papers but no matching ordinary-SRW cutoff theorem for the graph class below. This is negative evidence only, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, failed-route preservation, and C28 split

The latest own substantive report read before this run was

`2026-09-20_15-59-31__partitioned-green-clique-insertion-transfer.md`.

It proved a quotient-conditioned Green transfer for shells which remain permanently far from global equilibrium because of a finite color label, and applied it to degree-six clique-inserted edge-transitive Ramanujan Cayley graphs. Its next proposed attack was a positive matrix filter for slow positive exceptional NBRW modes.

That positive-exceptional-mode obstruction is **preserved**. I do not count it as solved here. The older Ihara/first-repeated-directed-edge tangle route also remains incomplete, and the global point-source heat-kernel `L^2` route remains too strong.

The present run deliberately takes a different productive route rather than forcing an unproved matrix filter: it proves a **quantitative Berry–Esseen refinement of finite-orbit Green transfer** and applies it to a new noncommutative edge geometry, the Hermitianized two-step NBRW graph. The application is not a framework-only result.

The necessary earlier P26 dependency also read was

`2026-09-20_14-57-03__biregular-line-finite-orbit-green-transfer.md`.

That report established the finite-orbit shell representation and the EFMP Green estimate for edge-regular fully Ramanujan `(9,3)` arithmetic bigraph ancestors. The present run reuses only that shell input, not its line-graph radial clock.

The newest relevant historical-C28 successor report read was NM13-01

`2026-09-20T13-02-22Z__conditional-fiber-supercritical-cutoff.md`.

NM13-01 owns an algebraic growing-quotient / conditional residual-fiber route with nonnormalizing voltages and pathwise `L^2` contraction. P26 remains complementary: covering shells, edge Green functions, explicit edge spectra and radial Markov-additive clocks.

The root `POSTED.md` registry was read. In particular, nothing below reopens the excluded Salez Problem 2.4 / Abelian Cayley product-condition manuscript.

## 1. Exact source convention and current exact boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), inserts independent mean-one exponential waiting times between discrete transitions. If `P` is the discrete transition matrix, the exact convention is

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

There an expander sequence has diverging size, uniformly bounded degree, and one-sided spectral gap bounded away from zero.

The fresh 20 September 2026 source check leaves the target open.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves an explicit Gaussian cutoff profile for every fixed-degree **long-range expander** sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow \text{long-range}\Longrightarrow\text{spectral},
  \]
  with neither converse. His exact LRE definition requires
  \[
  |B(S,r)|\ge \min\{3n/4,\;c|S|(d-1)^r\}
  \]
  uniformly in `S,r`. Thus LRE is not synonymous with Salez's spectral-expander hypothesis.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345` (6 July 2026), prove a cutoff-window bound through a non-equilibrium Poincare constant `gamma_*`; the checked statement does not derive `gamma_*` from transitivity plus a fixed ordinary spectral gap.
* Shai Evra--Brooke Feigon--Kathrin Maurischat--Ori Parzanchevski, `arXiv:2312.06507v3` (6 April 2026), prove sharp edge-NBRW estimates for Ramanujan bigraphs. Their Corollary 4.12 gives
  \[
  \|B^{2t}|_{L^2_0(E)}\|_2
  \le t\sqrt{2(Kk)^{t+1}},
  \tag{1.2}
  \]
  and their Theorem 8.7 gives an Eisenstein `p=2` lattice acting simply transitively on edges of the `(9,3)` Bruhat--Tits tree; its proof invokes their Ramanujan automorphic criterion.

## 2. Parent before/after versus mechanism progress

### Parent before

Salez Problem 2.3 was open. P26 already had qualitative finite-orbit Green transfer and a degree-10 line-graph class on edge-regular fully Ramanujan `(9,3)` bigraphs.

### Parent after

Salez Problem 2.3 remains open.

The strict new restricted scope is:

> Ordinary rate-one continuous-time SRW on the **Hermitianized two-step NBRW edge graphs** of suitable edge-regular fully Ramanujan `(9,3)` arithmetic bigraphs has a quantitative Gaussian TV profile.

The outputs are degree `32`, vertex-transitive Cayley spectral expanders with gap at least

\[
\boxed{
\frac34-\frac{9\sqrt2}{32}
=0.3522524355\ldots,
}
\tag{2.1}
\]

they fail every fixed positive long-range-expansion constant, and their TV profile has an explicit finite-size error

\[
O_Z\!\left(\frac{\log\log n}{\sqrt{\log n}}\right)
\tag{2.2}
\]

uniformly for profile coordinates `|z|<=Z`.

### Mechanism-level movement

The reusable new theorem upgrades the previous qualitative shell squeeze to a **quantitative Berry–Green profile transfer**. Under exponential/polynomial Green cleanup and a finite-state bounded-increment Markov-additive radial clock, it gives both:

1. an explicit profile error `O(log ell / sqrt(ell))`; and
2. a second-order mixing-time expansion with deterministic remainder `O(log ell)`.

The application requires a new radial process with jumps `{-2,-1,+1,+2}` and a new exact Hermitian edge-spectrum calculation. Neither calculation is inherited from the degree-10 line graph.

## 3. Theorem A — finite-orbit Green squeeze

Let `Y_n` be finite transitive regular graphs with uniform stationary law `pi_n`. Assume the exact source-continuous-time walk has a lifted decomposition

\[
\delta_xH_t
=\sum_{r\ge0}\sum_{\sigma\in\Sigma}
p_{n,t}(r,\sigma)\nu^x_{n,r,\sigma},
\tag{3.1}
\]

where `Sigma` is fixed and finite. Let `R_t=r` on the summand `(r,sigma)`. Suppose, for every `h>=0`,

\[
\sup_{x,\sigma}\sup_{r\ge\ell_n+h}
\chi^2(\nu^x_{n,r,\sigma}\Vert\pi_n)
\le G_n(h)
\tag{3.2}
\]

and all shell supports with `r<=ell_n-h` lie in a set `A_{n,x}(ell_n-h)` satisfying

\[
\sup_x\pi_n(A_{n,x}(\ell_n-h))\le L_n(h).
\tag{3.3}
\]

Then

\[
\boxed{
\Pr(R_t\le\ell_n-h)-L_n(h)
\le d_n(t)
\le
\Pr(R_t<\ell_n+h)+\frac12\sqrt{G_n(h)}.
}
\tag{3.4}
\]

The proof is the support test for the lower bound and convexity plus `TV <= (1/2)sqrt(chi^2)` for the upper bound. This is recalled because the quantitative theorem below uses the exact error terms rather than only their convergence to zero.

## 4. Theorem B — quantitative Berry–Green transfer

Assume Theorem A and `ell_n -> infinity`. Suppose there are fixed constants `A,a,b>0` such that for all `0<=h<=ell_n/2`,

\[
L_n(h)\le Ae^{-ah},
\qquad
G_n(h)\le A(\ell_n+h+2)^b e^{-ah}.
\tag{4.1}
\]

Assume also that outside a fixed radial boundary set the pair `(R_t,S_t)` is a rate-one continuous-time finite-state Markov-additive process with:

* a fixed finite type set;
* bounded integer increments;
* irreducible aperiodic type chain;
* tilted one-jump matrix `M_theta`;
* a simple Perron eigenvalue `lambda(theta)` analytic near zero;
* positive speed and nonzero variance
  \[
  v=\lambda'(0)>0,\qquad \sigma^2=\lambda''(0)>0;
  \tag{4.2}
  \]
* an exponentially integrable total boundary correction.

Write

\[
\tau^2=\frac{\sigma^2}{v^3},
\qquad
t_n(z)=\frac{\ell_n}{v}+z\sqrt{\ell_n}.
\tag{4.3}
\]

Then for every fixed `Z<infinity`,

\[
\boxed{
\sup_{|z|\le Z}
\left|
d_n(t_n(z))
-\Phi\!\left(-\frac{z}{\tau}\right)
\right|
\le
C_Z\frac{\log\ell_n}{\sqrt{\ell_n}}
}
\tag{4.4}
\]

for all sufficiently large `n`.

Consequently, for every fixed `epsilon in (0,1)`,

\[
\boxed{
t_{\rm mix}^{(n)}(\varepsilon)
=
\frac{\ell_n}{v}
-\tau\Phi^{-1}(\varepsilon)\sqrt{\ell_n}
+O_\varepsilon(\log\ell_n).
}
\tag{4.5}
\]

### Proof

Choose

\[
h_n=c_0\log\ell_n
\tag{4.6}
\]

with `c_0>(b+4)/a`. Then (4.1) gives

\[
L_n(h_n)+\sqrt{G_n(h_n)}=O(\ell_n^{-2}),
\qquad
h_n=O(\log\ell_n)=o(\sqrt{\ell_n}).
\tag{4.7}
\]

It remains to estimate the radial CDF quantitatively.

For the homogeneous Markov-additive process, let the jump type be `J_m` and cumulative radial increment `S_m`. Poissonization at rate one gives the matrix transform

\[
\mathbb E_\alpha[e^{\theta S_{N_t}};J_{N_t}=\cdot]
=
\alpha\exp\{t(M_\theta-I)\}.
\tag{4.8}
\]

At `theta=0`, Perron--Frobenius gives a simple eigenvalue `lambda(0)=1`; all other eigenvalues are separated from `1`. Analytic perturbation therefore gives, uniformly for bounded `u`,

\[
\lambda(iu/\sqrt t)-1
=
\frac{iuv}{\sqrt t}
-\frac{\sigma^2u^2}{2t}
+O\!\left(\frac{|u|^3}{t^{3/2}}\right).
\tag{4.9}
\]

The complementary spectral subspace contributes `O(e^{-ct})`. Applying the standard Esseen smoothing inequality to (4.8), first for `|u|<=c\sqrt t` and then using bounded increments outside this range, gives the finite-state Markov-additive Berry--Esseen estimate

\[
\sup_y
\left|
\Pr\!\left(\frac{S_{N_t}-vt}{\sigma\sqrt t}\le y\right)
-\Phi(y)
\right|
\le Ct^{-1/2}.
\tag{4.10}
\]

This argument is self-contained at the level needed here: the only inputs are a fixed finite matrix, a simple Perron root, bounded third moments, and a fixed spectral separation.

By assumption the actual radial process differs only through a finite boundary perturbation whose total time and displacement have a uniform exponential moment. Truncate that perturbation at `C_1 log t`; its tail is `O(t^{-3})`. Conditional on the truncated correction, (4.10) at a threshold shifted by `O(log t)` changes the Gaussian CDF by at most

\[
O\!\left(\frac{\log t}{\sqrt t}\right).
\]

Therefore

\[
\sup_y
\left|
\Pr\!\left(\frac{R_t-vt}{\sigma\sqrt t}\le y\right)
-\Phi(y)
\right|
\le
C\frac{\log t}{\sqrt t}.
\tag{4.11}
\]

For `t=t_n(z)`, `|z|<=Z`,

\[
\frac{\ell_n-vt}{\sigma\sqrt t}
=
-\frac{zv^{3/2}}{\sigma}
+O_Z(\ell_n^{-1/2}).
\tag{4.12}
\]

Replacing the threshold `ell_n` by `ell_n +/- h_n` changes the standardized threshold by

\[
O(h_n/\sqrt{\ell_n})
=
O(\log\ell_n/\sqrt{\ell_n}).
\tag{4.13}
\]

Insert these two radial CDF bounds into (3.4), use (4.7), and obtain (4.4). Since the standard normal density is positive at every finite fixed quantile, inversion of (4.4) gives (4.5). `QED`

The role of the exact continuous-time convention is visible in (4.8): the cumulant exponent is `lambda(theta)-1`, not `log lambda(theta)`.

## 5. New graph operation — Hermitianized two-step NBRW edge graph

Let

\[
X=(L\sqcup R,E)
\]

be a simple `(K+1,k+1)`-biregular graph, `K>k>=1`, with girth greater than four.

On `ell^2(E)`, let `C_L` be adjacency inside the star of a left endpoint and `C_R` adjacency inside the star of a right endpoint:

\[
(C_Lf)(e)=\sum_{\substack{e'\ne e\\e'\cap e\in L}}f(e'),
\qquad
(C_Rf)(e)=\sum_{\substack{e'\ne e\\e'\cap e\in R}}f(e').
\tag{5.1}
\]

Define

\[
\boxed{
Y=\mathsf{HN}_2(X),
\qquad
A_Y=C_LC_R+C_RC_L.
}
\tag{5.2}
\]

Equivalently, two ancestor edges are adjacent in `Y` when they are the outer edges of a nonbacktracking three-edge path in `X`; the two summands correspond to the two possible side orders. It is the self-adjoint/Hermitianized version of a two-step oriented NBRW edge move.

Because `girth(X)>4`, two distinct such macro paths never join the same pair in both orders. Thus `A_Y` is a `0-1` adjacency matrix with no diagonal and

\[
\boxed{\deg(Y)=2Kk.}
\tag{5.3}
\]

Every edge automorphism of `X` acts on `Y`. Hence if a group acts transitively (respectively regularly) on `E(X)`, then `Y` is vertex-transitive (respectively Cayley).

For the arithmetic family used below, the ancestor edge action is regular.

## 6. Theorem C — exact spectrum of the Hermitianized edge graph

Let `M` be the left-right biadjacency matrix of `X`. Define incidence lifts

\[
(Uf)(e)=f(\ell(e)),
\qquad
(Vg)(e)=g(r(e)).
\tag{6.1}
\]

Then

\[
C_L=UU^*-I,\qquad C_R=VV^*-I.
\tag{6.2}
\]

Let `f,g` be a singular pair

\[
Mg=sf,\qquad M^*f=sg,
\qquad x=s^2.
\tag{6.3}
\]

On the span of `Uf,Vg`,

\[
A_Y(Uf)
=
(x-2K)Uf+s(K-1)Vg,
\tag{6.4}
\]

\[
A_Y(Vg)
=
s(k-1)Uf+(x-2k)Vg.
\tag{6.5}
\]

Therefore the two formal eigenvalues are

\[
\boxed{
\Lambda_\pm(x)
=
x-(K+k)
\pm
\sqrt{(K-k)^2+x(K-1)(k-1)}.
}
\tag{6.6}
\]

On the orthogonal complement of `im U+im V`, both `C_L` and `C_R` equal `-I`, so

\[
A_Y=2I.
\tag{6.7}
\]

At the top singular value `x=(K+1)(k+1)`, the Perron value is `2Kk`; the second formal branch reduces to the flat value `2`.

Thus all normalized output eigenvalues are supplied by

\[
q_\pm(x)=\frac{\Lambda_\pm(x)}{2Kk}
\tag{6.8}
\]

plus `1/(Kk)`.

Now assume `X` is fully Ramanujan. Every nontrivial singular value satisfies

\[
x\in
[(\sqrt K-\sqrt k)^2,(\sqrt K+\sqrt k)^2]
\quad\text{or}\quad x=0.
\tag{6.9}
\]

Since `Lambda_+(x)` is increasing in `x`, the largest nonconstant normalized eigenvalue is bounded by its value at the upper tree edge.

For `(K,k)=(8,2)`, the upper edge is `x=18`, and

\[
\Lambda_+(18)
=
8+\sqrt{162}
=
8+9\sqrt2.
\tag{6.10}
\]

Hence

\[
\boxed{
\operatorname{gap}(Y)
\ge
1-\frac{8+9\sqrt2}{32}
=
\frac34-\frac{9\sqrt2}{32}
>0.35225.
}
\tag{6.11}
\]

This is a direct ordinary spectral-expander estimate for the output graph.

## 7. Exact shell Green front on the new universal cover

Let `T=T_{K+1,k+1}` be the biregular tree and fix a root edge `e_0`. The operation (5.2) is local, so it lifts to

\[
\mathsf{HN}_2(T)\to\mathsf{HN}_2(X).
\tag{7.1}
\]

Use as radial coordinate **ancestor edge distance**

\[
R(e)=\operatorname{dist}_{L(T)}(e_0,e).
\tag{7.2}
\]

The root-edge stabilizer has two orbits on each nonzero ancestor sphere, according to whether the endpoint of `e` nearer the root lies in `L` or `R`. Conditional on `(R_t=r,S_t=sigma)`, symmetry makes the lifted endpoint uniform on that orbit.

Projecting an orbit to `X` gives exactly an `r`-step edge-NBRW endpoint law, started with the appropriate orientation; forgetting final orientation is a stochastic projection. Therefore the finite graph has the exact shell decomposition required by Theorem A.

The ancestor edge spheres are

\[
|\mathcal S_{2m}|=2(Kk)^m,\qquad
|\mathcal S_{2m+1}|=(K+k)(Kk)^m.
\tag{7.3}
\]

For `n=|E(X)|=|V(Y)|` the entropic radius is

\[
\boxed{
\ell_n
=
\log_{\sqrt{Kk}}n+O(1)
=
2\log_{Kk}n+O(1).
}
\tag{7.4}
\]

The early support bound is

\[
L_n(h)\le C_{K,k}(Kk)^{-h/2}.
\tag{7.5}
\]

For a fully Ramanujan ancestor, EFMP Corollary 4.12 and their Theorem 4.13 proof give, at even NBRW time `2t`,

\[
\chi^2(p_e^{2t}\Vert u)
\le
2(Kk)n\,t^2(Kk)^{-t}.
\tag{7.6}
\]

A single NBRW step between orientation classes is doubly stochastic, hence contracts chi-square; odd times obey the corresponding bound. Consequently, uniformly over both shell types,

\[
\boxed{
G_n(h)
\le
C_{K,k}(\ell_n+h+2)^2(Kk)^{-h/2}.
}
\tag{7.7}
\]

Thus (4.1) holds with exponential Green cleanup. Taking

\[
h_n=8\log_{Kk}\ell_n
\tag{7.8}
\]

already gives

\[
L_n(h_n)=O(\ell_n^{-4}),
\qquad
\sqrt{G_n(h_n)}=O(\ell_n^{-1}),
\tag{7.9}
\]

well below the Berry–Esseen error.

## 8. The new radial Markov-additive clock

Away from radii `0,1`, let type `L` mean that the endpoint of the current ancestor edge nearer the root lies in `L`; define type `R` analogously.

A macro step in `Y` consists of changing ancestor edge once through one side and once through the other side. Exact tree counting gives the following rows.

For type `L`:

\[
\begin{array}{c|rrrr}
\Delta R&-2&-1&+1&+2\\ \hline
\#&1&k-1&(K-1)k&Kk.
\end{array}
\tag{8.1}
\]

For type `R`:

\[
\begin{array}{c|rrrr}
\Delta R&-2&-1&+1&+2\\ \hline
\#&1&K-1&(k-1)K&Kk.
\end{array}
\tag{8.2}
\]

Each row sums to `2Kk`.

The `+/-2` jumps preserve type and the `+/-1` jumps switch type. Hence the type chain is symmetric:

\[
P_{\rm type}
=
\frac1{2Kk}
\begin{pmatrix}
Kk+1&Kk-1\\
Kk-1&Kk+1
\end{pmatrix},
\qquad
\pi_{\rm type}=(1/2,1/2).
\tag{8.3}
\]

The tilted one-jump matrix is

\[
M_\theta
=
\frac1{2Kk}
\begin{pmatrix}
e^{-2\theta}+Kke^{2\theta}
&
(k-1)e^{-\theta}+(K-1)ke^\theta
\\
(K-1)e^{-\theta}+(k-1)Ke^\theta
&
e^{-2\theta}+Kke^{2\theta}
\end{pmatrix}.
\tag{8.4}
\]

Writing

\[
a(\theta)=\frac{e^{-2\theta}+Kke^{2\theta}}{2Kk},
\]

and `b_L,b_R` for the off-diagonal entries, the Perron branch is exactly

\[
\lambda(\theta)
=
a(\theta)+\sqrt{b_L(\theta)b_R(\theta)}.
\tag{8.5}
\]

Differentiation at zero gives the closed forms

\[
\boxed{
v
=
\frac{3Kk-K-k-1}{2Kk},
}
\tag{8.6}
\]

\[
\boxed{
\sigma^2
=
\frac{5K^2k^2-K^2-k^2-3}
{2Kk(Kk-1)}.
}
\tag{8.7}
\]

These are the **continuous-time** drift and variance rates because the outer clock has rate one and the cumulant exponent is `lambda(theta)-1`.

For the boundary control, both conditional drifts in the concrete `(8,2)` case are positive:

\[
m_L=43/32,\qquad m_R=31/32.
\tag{8.8}
\]

Hence for sufficiently small `c>0`,

\[
\sup_{\sigma\in\{L,R\}}
\mathbb E[e^{-c\Delta R}\mid\sigma]<1
\tag{8.9}
\]

outside `{0,1}`. Optional stopping of the corresponding exponential supermartingale gives an exponentially small probability of returning from a large radius. Repeated excursions from the finite boundary therefore have a geometric count, and their total holding time and displacement have a uniform exponential moment. This verifies the boundary hypothesis of Theorem B.

## 9. Concrete degree-32 Cayley class and quantitative profile

Use the edge-regular fully Ramanujan `(9,3)` arithmetic bigraph quotient family already isolated in the preceding P26 line-graph report from EFMP Theorem 8.7 and their Ramanujan automorphic criterion. The edge action is regular, girth tends to infinity, and thus for all sufficiently large quotients (5.2) is a simple Cayley graph.

Here

\[
K=8,\qquad k=2,\qquad Kk=16,
\qquad \deg(Y_n)=32.
\tag{9.1}
\]

The exact radial rows are

\[
L:\{-2:1,-1:1,+1:14,+2:16\},
\tag{9.2}
\]

\[
R:\{-2:1,-1:7,+1:8,+2:16\}.
\tag{9.3}
\]

Equations (8.6)--(8.7) give

\[
\boxed{
v=\frac{37}{32},
\qquad
\sigma^2=\frac{403}{160}.
}
\tag{9.4}
\]

Therefore

\[
\boxed{
\tau^2
=
\frac{\sigma^2}{v^3}
=
\frac{412672}{253265}.
}
\tag{9.5}
\]

Since

\[
\ell_n
=
\log_4 n+O(1),
\tag{9.6}
\]

Theorem B gives, uniformly on every compact `z` interval,

\[
\boxed{
d_{\rm TV}\!\left(
\frac{32}{37}\log_4 n
+
z\sqrt{\log_4 n}
\right)
=
\Phi\!\left(
-z\sqrt{\frac{253265}{412672}}
\right)
+
O_Z\!\left(
\frac{\log\log n}{\sqrt{\log n}}
\right).
}
\tag{9.7}
\]

Equivalently, on the `sqrt(log_16 n)` scale,

\[
\boxed{
d_{\rm TV}\!\left(
\frac{64}{37}\log_{16} n
+
z\sqrt{\log_{16}n}
\right)
\to
\Phi\!\left(
-z\sqrt{\frac{253265}{825344}}
\right).
}
\tag{9.8}
\]

For every fixed `epsilon in (0,1)`,

\[
\boxed{
t_{\rm mix}(\varepsilon)
=
\frac{32}{37}\log_4 n
-
\sqrt{\frac{412672}{253265}}\,
\Phi^{-1}(\varepsilon)\sqrt{\log_4 n}
+
O_\varepsilon(\log\log n).
}
\tag{9.9}
\]

This is ordinary SRW in Salez's exact continuous-time convention. EFMP NBRW is used only as the late-shell Green input.

## 10. These outputs are spectral but not long-range

One output step in `Y_n` moves at most two ancestor edge transitions. Hence an output radius-`r` ball is contained in an ancestor edge ball of radius `2r`. By (7.3),

\[
|B_{Y_n}(e,r)|
\le C( Kk)^r
=
C\,16^r.
\tag{10.1}
\]

But `Y_n` is degree `32`, so Altschuler's exact singleton LRE condition would require growth at the tree branching rate

\[
31^r
\tag{10.2}
\]

up to a fixed multiplicative constant before macroscopic saturation.

Take

\[
r_n=\left\lfloor\frac12\log_{31}n\right\rfloor.
\tag{10.3}
\]

For every fixed `c>0`, `c31^{r_n}<3n/4` for all large `n`, while

\[
\frac{|B_{Y_n}(e,r_n)|}{31^{r_n}}
\le
C\left(\frac{16}{31}\right)^{r_n}
\longrightarrow0.
\tag{10.4}
\]

Therefore no fixed positive LRE constant exists. The new cutoff theorem is not an application of Altschuler's long-range-expander theorem to the output graph.

## 11. Exact sanity checks executed in this run

The archived exact checker verifies:

1. the `2x2` singular-value block and discriminant
   \[
   4\{(K-k)^2+x(K-1)(k-1)\};
   \]
2. the `(8,2)` bulk endpoint
   \[
   \Lambda_+(18)=8+9\sqrt2;
   \]
3. the gap
   \[
   3/4-9\sqrt2/32;
   \]
4. both radial rows and their total degree `32`;
5. the exact tilted-matrix derivatives
   \[
   v=37/32,\quad \sigma^2=403/160;
   \]
6. the profile constants
   \[
   \tau^2=412672/253265,\qquad
   2\tau^2=825344/253265;
   \]
7. a complete finite matrix test on the incidence bigraph of `K_4`, a `(3,2)`-biregular girth-six graph, where the constructed edge graph is simple `4`-regular and its exact numerical spectrum is
   \[
   -2^{(\times5)},0^{(\times3)},2^{(\times3)},4;
   \]
8. the strict branching mismatch `16<31`.

The terminal checker marker is

`P26_T08_HERMITIAN_NBRW_BERRY_GREEN_EXACT_PASS`.

## 12. Residual obstruction and next attack

The parent obstruction is not the radial CLT anymore on the classes treated here: Theorem B makes the profile transfer quantitative once an entropic shell Green front is available.

The remaining T08 obstruction is still the **positive exceptional NBRW sector** for a general vertex-transitive spectral expander. In particular, full Ramanujan control of the edge-NBRW Green operator is stronger than Salez's hypothesis.

This run adds one useful structural clue for the next attack. The new output transition is the self-adjoint combination

\[
Q=\frac{C_LC_R+C_RC_L}{2Kk},
\tag{12.1}
\]

and its spectrum depends on ancestor singular values through the explicit scalar transform (6.6), despite `C_L` and `C_R` being noncommuting. The next P26 attack will therefore test a **self-adjoint anticommutator filter** for exceptional NBRW modes:

\[
\mathcal H_m
=
\frac12\left(C^m+(C^*)^m\right)
\quad\text{or short positive combinations thereof},
\tag{12.2}
\]

with the goal of converting a nonnormal exceptional sector into a tractable Hermitian spectral-density defect before applying the Green theorem. This is distinct from NM13-01's conditional-fiber voltage route.

No claim is made yet that (12.2) handles arbitrary transitive spectral expanders; that next step is **CONJECTURAL** until a source-valid Green bound is proved.

## ledger_delta

```yaml
ledger_delta:
  parent_problem:
    id: "Salez arXiv:2508.21055 Problem 2.3"
    before: "OPEN/PARTIAL"
    after: "OPEN/PARTIAL"
    changed: false
  mechanism_advances:
    - id: "P26-T08-BERRY-GREEN-01"
      status: "CANDIDATE_FULL"
      statement: "Finite-orbit exponential shell Green cleanup plus a bounded finite-state Markov-additive radial clock with exponentially integrable boundary correction yields a uniform Gaussian TV-profile error O(log ell/sqrt ell) and t_mix(epsilon)=ell/v-tau Phi^{-1}(epsilon)sqrt ell+O_epsilon(log ell)."
    - id: "P26-T08-HERMITIAN-EDGE-SPECTRUM-01"
      status: "CANDIDATE_FULL"
      statement: "For the Hermitianized two-step NBRW edge graph A=C_L C_R+C_R C_L of a girth>4 (K+1,k+1)-bigraph, the nonflat spectral branches are Lambda_pm(x)=x-(K+k) +/- sqrt((K-k)^2+x(K-1)(k-1))."
    - id: "P26-T08-HERMITIAN-RADIAL-01"
      status: "CANDIDATE_FULL"
      statement: "The universal-cover radial clock has two types, jumps {-2,-1,+1,+2}, speed (3Kk-K-k-1)/(2Kk), and exact rate-one continuous-time variance (5K^2k^2-K^2-k^2-3)/(2Kk(Kk-1))."
  proved_application:
    id: "P26-T08-HERMITIAN-93-01"
    status: "CANDIDATE_FULL"
    class: "degree-32 Cayley Hermitianized two-step NBRW edge graphs from edge-regular fully Ramanujan (9,3) arithmetic bigraphs"
    spectral_gap_lower_bound: "3/4 - 9*sqrt(2)/32"
    cutoff_center: "(32/37) log_4 n + O(1)"
    profile_variance_on_sqrt_log4: "412672/253265"
    quantitative_profile_error: "O_Z(log log n / sqrt(log n))"
    long_range_expansion: "fails every fixed positive LRE constant; output ball branching <=16 versus degree-32 tree benchmark 31"
  preserved_failed_or_unproved_routes:
    - "Ihara / first-repeated-directed-edge tangle decomposition remains incomplete."
    - "Global point-source heat-kernel L2 control remains too strong."
    - "Positive exceptional NBRW modes remain unresolved; no matrix-filter theorem is claimed."
  C28_coordination:
    live_successor: "NM13-01"
    split: "NM13-01 owns growing quotient / conditional residual fiber / nonnormalizing voltage transfer; P26 owns shell Green / edge spectrum / radial Markov-additive transfer."
  next_attack:
    status: "CONJECTURAL"
    statement: "Test self-adjoint anticommutator filters (C^m+(C*)^m)/2 and short positive combinations as a way to turn positive nonnormal exceptional NBRW mass into a weighted Hermitian defect compatible with the Berry-Green transfer."
  exact_checker:
    terminal_marker: "P26_T08_HERMITIAN_NBRW_BERRY_GREEN_EXACT_PASS"
  publication_novelty: "UNVERIFIED"
```

End of complete P26 substantive T08 report.
