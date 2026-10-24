Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but no authenticated runtime metadata establishes that model/effort setting, so I do not claim otherwise.

# P26 / LIVE20 T08 — Green-shell transfer through biregular halving; cutoff on non-Ramanujan Eisenstein Cayley-bigraph halves

**Status:** `CANDIDATE_FULL` for the restricted transfer theorem and concrete application below, pending later independent review; `PARTIAL / OPEN` for Salez Problem 2.3. Worldwide publication novelty is `UNVERIFIED`.

Repository/branch: `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Report root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and complementary split with historical C28

The newest own report before this run was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_08-57-05__trimmed-green-bipartite-spherical-transfer.md`.

It allowed a subexponential number of exceptional eigenmodes in a regular-base NBRW shell argument and applied that to a mixed-distance graph on a bipartite double cover of an LPS family. Its next proposed route was to replace crude exceptional-mode counting by a weighted spectral-density Green bound.

The live successor of historical C28 is `NM13-01`. Its newest relevant report read in this run is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T06-20-00Z__arc-cover-hodge-orbit-drift.md`.

That route now owns oriented-edge covers, Hodge-Green `L^1` cancellation and finite-alphabet stabilizer-orbit drift. P26 therefore does **not** duplicate the arc-cover/orbit-factor program. Instead this run changes the base category: start from **biregular Cayley bigraphs** with a Sarnak--Xue nonbacktracking spectral-density theorem, pass to a regular transitive graph on one color class, and transfer the directed-edge Green estimate into exact continuous-time total variation.

This is not a stalled/checker run. The mathematical outputs are:

1. a quantitative Green-shell profile criterion;
2. a general cutoff theorem for left-halved graphs of left-transitive adj-Ramanujan bigraphs satisfying the Sarnak--Xue density hypothesis and logarithmic girth; and
3. a concrete application to the **non-Ramanujan** Eisenstein Cayley bigraphs of Evra--Feigon--Maurischat--Parzanchevski. For `p=2` their left-halved graphs are 18-regular vertex-transitive spectral expanders, are not fixed-constant long-range expanders, and have an explicit Gaussian rate-one continuous-time cutoff profile.

No historical/peer file, POSTED claim, shared root ledger, scheduler, permission, workflow, email/Drive object or public surface is modified.

## 1. Exact source convention and current scope boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), embeds a discrete transition matrix `T` in continuous time by independent mean-one exponential waiting times. Thus the exact convention is

\[
P_t=e^{t(T-I)}=e^{-t}\sum_{j\ge0}\frac{t^jT^j}{j!}.
\tag{1.1}
\]

His Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

Here expanders have diverging size, uniformly bounded degree and spectral gaps bounded away from zero.

Fresh exact-scope checks on 20 September 2026 give the following boundary.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves an explicit Gaussian cutoff profile for every fixed-degree **long-range expander** sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range}\Longrightarrow\text{spectral},
  \]
  with neither converse. Long-range expansion is therefore not synonymous with Salez's hypothesis.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345` (6 July 2026), prove a universal window theorem in terms of their non-equilibrium Poincare quantity `gamma_*`; no checked theorem there derives the needed estimate from vertex transitivity plus an ordinary fixed spectral gap alone.
* Shai Evra, Brooke Feigon, Kathrin Maurischat and Ori Parzanchevski, `arXiv:2312.06507v3` (revised 6 April 2026), construct explicit `(p^3+1,p+1)` Cayley bigraphs. Their Eisenstein family is adj-Ramanujan but genuinely non-Ramanujan, satisfies Sarnak--Xue density, has logarithmic girth, and has bounded-window cutoff for NBRW on directed edges. Their Theorem 4.17 supplies the quantitative `L^2` estimate used below.

The root `POSTED.md` exclusion for Salez Problem 2.4 / the Abelian-Cayley product-condition manuscript was rechecked and is not reopened. A bounded search for combinations of `halved graph cutoff`, `biregular half-square random walk cutoff`, `Ramanujan bigraph halved graph cutoff` and `distance-two biregular cutoff` found standard halved-graph/distance-biregular material but no theorem matching the regular transitive cutoff class below. This is negative evidence only; publication novelty remains `UNVERIFIED`.

## 2. Parent problem before / after

### Before

Salez Problem 2.3 was `OPEN`. P26 had transferred entropy/Green fronts through several fixed regular-graph operations, including line graphs, finite fibers and spherical distance kernels. The latest route could tolerate only a controlled exceptional sector in a **regular** base NBRW spectrum.

### After

Salez Problem 2.3 remains `OPEN`, but the proved scope enlarges in a qualitatively different direction:

> **Biregular-halving theorem.** Fix `K>=k>=2`. Let `X_n=(L_n \sqcup R_n,E_n)` be connected left-transitive `(K+1,k+1)`-biregular graphs with logarithmic girth, adj-Ramanujan adjacency spectrum and the Sarnak--Xue NBRW density hypothesis at the sharp exponent
> \[
> \delta=\frac{2}{1+\log_k K}.
> \]
> Let `Y_n` be the graph on `L_n` in which two left vertices are adjacent exactly when they share a right neighbor. Then, once the girth exceeds four, `Y_n` is a fixed-degree vertex-transitive spectral-expander sequence, is not a fixed-constant long-range-expander sequence, and exact rate-one continuous-time SRW on `Y_n` has a Gaussian total-variation cutoff profile with `Theta(sqrt(log |L_n|))` window.

The concrete `p=2` Eisenstein family gives a new 18-regular transitive class whose underlying bigraph is explicitly **non-Ramanujan**. This is the substantive parent-problem movement; the checker and commits are not counted as movement.

## 3. Quantitative Green-shell transfer criterion

Let `Y_n` be finite regular graphs with uniform stationary laws `pi_n`, and use the exact rate-one semigroup

\[
H_t^{(n)}=e^{t(Q_n-I)}.
\tag{3.1}
\]

Assume that from every start `x` there is a nonnegative integer radial process `R_t` and shell laws `nu_{n,r}^x` such that

\[
\boxed{
\delta_xH_t^{(n)}
=\sum_{r\ge0}\Pr(R_t=r)\,\nu_{n,r}^x.
}
\tag{3.2}
\]

Define the shell Green excess

\[
G_n(r):=\sup_x\chi^2(\nu_{n,r}^x\|\pi_n).
\tag{3.3}
\]

For any threshold `a`, convexity of total variation and Cauchy--Schwarz give

\[
\begin{aligned}
d_n(t)
&\le \Pr(R_t<a)
 +\sum_{r\ge a}\Pr(R_t=r)
   \|\nu_{n,r}^x-\pi_n\|_{TV}\\
&\le \boxed{
\Pr(R_t<a)+\frac12\sqrt{\sup_{r\ge a}G_n(r)}.
}
\tag{3.4}
\end{aligned}
\]

If every shell `nu_{n,r}^x` is supported in a set `B_n(x,r)`, then testing total variation on `B_n(x,a)` yields

\[
\boxed{
 d_n(t)\ge \Pr(R_t\le a)-\pi_n(B_n(x,a)).
}
\tag{3.5}
\]

Consequently suppose there are scales `ell_n -> infinity`, `w_n -> infinity`, a center `T_n`, and numbers `h_n -> infinity` with `h_n=o(w_n)` such that

\[
\sup_{r\ge \ell_n+h_n}G_n(r)\to0,
\qquad
\sup_x\pi_n(B_n(x,\ell_n-h_n))\to0,
\tag{3.6}
\]

and the radial front has a limit profile stable under `o(w_n)` threshold perturbations:

\[
\Pr(R_{T_n+zw_n}<\ell_n+o(w_n))\to F(z).
\tag{3.7}
\]

Then (3.4)--(3.5) give the full TV profile

\[
\boxed{
 d_n(T_n+zw_n)\to F(z).
}
\tag{3.8}
\]

A useful quantitative form is immediate: if

\[
\sup_{r\ge\ell_n+h}G_n(r)
\le A_n e^{-ch}
\tag{3.9}
\]

for `0<=h=o(w_n)` and `log A_n=o(w_n)`, the Green cleanup costs only `o(w_n)` radial layers. If `A_n=O(1)`, fixed accuracy costs only `O(log(1/epsilon))` layers. This criterion is deliberately shell-local: it does **not** require the global point-mass heat-kernel `L^2` norm to be small at the TV scale.

## 4. The left-halved graph of a biregular bigraph

Let

\[
X=(L\sqcup R,E)
\]

be a connected `(K+1,k+1)`-biregular graph, and assume `girth(X)>4`. Define its **left-halved graph** `Y=Half_L(X)` by

\[
V(Y)=L,
\qquad
x\sim_Y y\iff x\ne y\text{ and }x,y\text{ have a common neighbor in }R.
\tag{4.1}
\]

Because a pair of left vertices cannot have two common right neighbors without making a 4-cycle, `Y` is simple. Each `x\in L` has `K+1` right neighbors and, through each, exactly `k` other left neighbors, with no duplication. Therefore

\[
\boxed{D=(K+1)k}
\tag{4.2}
\]

is the degree of `Y`. Every automorphism of `X` preserving `L` preserves the shared-right-neighbor relation. Hence left transitivity of `X` implies vertex transitivity of `Y`. For a Cayley bigraph the left action is simply transitive, so the resulting `Y` is in fact a Cayley graph.

### 4.1 Exact spectral transfer

Let `M` be the `|L| x |R|` incidence matrix of `X`. The no-4-cycle assumption gives the exact adjacency identity

\[
\boxed{A_Y=MM^T-(K+1)I.}
\tag{4.3}
\]

Thus the normalized SRW kernel is

\[
\boxed{
Q_Y=\frac{MM^T-(K+1)I}{(K+1)k}.
}
\tag{4.4}
\]

If `s` is a singular value of `M`, the corresponding `Y` eigenvalue is

\[
q(s)=\frac{s^2-(K+1)}{(K+1)k}.
\tag{4.5}
\]

For an adj-Ramanujan bigraph, every nontrivial adjacency singular value is either zero or satisfies

\[
(\sqrt K-\sqrt k)^2
\le s^2\le
(\sqrt K+\sqrt k)^2.
\tag{4.6}
\]

Hence the largest nonconstant output eigenvalue is at most

\[
\beta_{K,k}
=\frac{K+k+2\sqrt{Kk}-(K+1)}{(K+1)k}
=\frac{k-1+2\sqrt{Kk}}{(K+1)k}.
\tag{4.7}
\]

Therefore

\[
\boxed{
\operatorname{gap}(Y)
\ge 1-\beta_{K,k}
=\frac{(\sqrt{Kk}-1)^2}{(K+1)k}>0.
}
\tag{4.8}
\]

So the halving operation converts the adj-Ramanujan biregular input into a genuine fixed-degree regular spectral expander.

## 5. Exact shell representation and radial CLT

Let `T_{K+1,k+1}` be the universal biregular tree of `X`, rooted at a left vertex `o`, and form its left-halved graph `\widetilde Y` by the same rule. Since `girth(X)>4`, the covering map `T_{K+1,k+1}->X` induces a graph covering

\[
\widetilde Y\longrightarrow Y:
\tag{5.1}
\]

local neighbors correspond uniquely to length-two paths through a right vertex.

Lift rate-one continuous-time SRW on `Y` to `\widetilde Y`. Let `R_t` be the base-tree distance from `o`, divided by two, of the lifted position. The stabilizer of `o` in the biregular-tree automorphism group is transitive on each left sphere. Conditional on `R_t=r`, the lifted endpoint is therefore uniform on that sphere. After projection to `X`, this is exactly the endpoint law `nu_r^x` of a uniformly chosen nonbacktracking path of length `2r` from `x`.

Thus we have the exact source-convention shell identity

\[
\boxed{
\delta_x e^{t(Q_Y-I)}
=\sum_{r\ge0}\Pr(R_t=r)\nu_r^x.
}
\tag{5.2}
\]

No lazification, discrete-time substitution or time renormalization has occurred.

For any radius `r>=1`, one step of `\widetilde Y` has the following radial multiplicities:

\[
\begin{array}{c|ccc}
\Delta R&-1&0&+1\\ \hline
\#&1&k-1&Kk.
\end{array}
\tag{5.3}
\]

Indeed, using the unique parent right vertex gives one grandparent left vertex and `k-1` siblings, while the other `K` right neighbors each supply `k` children. With `D=(K+1)k`, define

\[
\boxed{
v=\frac{Kk-1}{D},
\qquad
M_2=\frac{Kk+1}{D}.
}
\tag{5.4}
\]

The embedded radial jump chain is a skip-free walk with holding and positive drift. Starting from radius one, its return probability to zero is the usual birth--death ratio

\[
\frac{p_-}{p_+}=\frac{1}{Kk}<1.
\tag{5.5}
\]

Hence the total number of boundary visits has a geometric tail. Coupling after the final boundary visit with an unrestricted i.i.d. increment walk shows that the boundary contributes `O_P(1)` to `R_t`. Poissonizing at rate one gives the compound-Poisson CLT

\[
\boxed{
\frac{R_t-vt}{\sqrt{M_2t}}\Longrightarrow N(0,1).
}
\tag{5.6}
\]

The shell size in the universal cover is

\[
|S_0|=1,
\qquad
|S_r|=D(Kk)^{r-1}\quad(r\ge1).
\tag{5.7}
\]

Thus the entropic radius for `n=|L|` vertices is

\[
\ell_n=\log_{Kk}n+O(1).
\tag{5.8}
\]

At times

\[
t=\frac{\ell_n}{v}+z\sqrt{\ell_n}
\tag{5.9}
\]

the radial CLT gives

\[
\Pr(R_t<\ell_n+o(\sqrt{\ell_n}))
\longrightarrow
\Phi\!\left(-\frac{z}{\tau_{K,k}}\right),
\tag{5.10}
\]

where

\[
\boxed{
\tau_{K,k}^2
=\frac{M_2}{v^3}
=\frac{(Kk+1)D^2}{(Kk-1)^3}.
}
\tag{5.11}
\]

## 6. The Sarnak--Xue NBRW estimate supplies the Green shells

This is the key transfer step.

Let `N=|E(X)|`, which is also the number of directed edges in the `L->R` orientation class. For an initial directed edge `e` in that class, let `p_e^{2r}` be the law after `2r` NBRW transitions and let `u` be uniform on the orientation class.

Evra--Feigon--Maurischat--Parzanchevski Theorem 4.17 assumes a left-transitive adj-Ramanujan `(K+1,k+1)` bigraph family with Sarnak--Xue density

\[
\mathcal E_X<N^{\delta},
\qquad
\boxed{
\delta=\frac{2}{1+\log_kK}
=2\log_{Kk}k,
}
\tag{6.1}
\]

and logarithmic girth. Their proof, equations (4.15) through the logarithmic-girth estimate, gives for admissible `r` near and beyond the entropic scale

\[
\|p_e^{2r}-u\|_2^2
\le
\frac{K+1}{(Kk)^r}
\left[
\frac{\mathcal E_X}{N}\left(\frac Kk\right)^r+m^2
\right].
\tag{6.2}
\]

Since `u` is uniform on `N` states,

\[
\chi^2(p_e^{2r}\|u)=N\|p_e^{2r}-u\|_2^2,
\]

so (6.2) is equivalently

\[
\boxed{
\chi^2(p_e^{2r}\|u)
\le
(K+1)\left[
\mathcal E_X k^{-2r}
+m^2N(Kk)^{-r}
\right].
}
\tag{6.3}
\]

Put `L_N=ceil(log_{Kk}N)`. Because of the exact exponent identity in (6.1),

\[
k^{2L_N}\asymp N^{\delta}.
\tag{6.4}
\]

Therefore at `r=L_N+h`,

\[
\boxed{
\chi^2(p_e^{2r}\|u)
\le C_{K,k,m}\left[k^{-2h}+(Kk)^{-h}\right].
}
\tag{6.5}
\]

The proof of (6.2) is stated for convenient arithmetic progressions of times because it sets a shorter tree-like time `tau=r/m`. This causes no window loss: take the next admissible `r_0` above `L_N+h`, an `O(m)` shift, and then use `chi^2` contraction under the doubly-stochastic NBRW kernel for all later times. The logarithmic-girth inequality has linear slack, so every `h=o(L_N)` is admissible for large `N`.

Now compare with the left-vertex shell `nu_r^x`. Choose the first directed edge `(x,z)` uniformly over the `K+1` right neighbors of `x`, run NBRW for `2r` transitions, and project the resulting `L->R` edge to its left tail. That tail has law `nu_r^x`. Mixture convexity and data processing for `chi^2` therefore give

\[
\boxed{
\chi^2(\nu_r^x\|u_L)
\le \max_{e:e^-=x}\chi^2(p_e^{2r}\|u).
}
\tag{6.6}
\]

Combining (6.5)--(6.6), for any `h_n->infinity` with `h_n=o(sqrt(log n))`,

\[
\sup_{r\ge\ell_n+h_n}
\chi^2(\nu_r^x\|u_L)\to0.
\tag{6.7}
\]

This is exactly the Green hypothesis of Section 3, and quantitatively it needs only `O(log(1/epsilon))` excess radial layers for fixed accuracy.

## 7. Lower support and the Gaussian profile

The universal-cover bound (5.7) also gives, uniformly in the quotient,

\[
|B_Y(x,r)|
\le 1+D\sum_{j=0}^{r-1}(Kk)^j
\le C_{K,k}(Kk)^r.
\tag{7.1}
\]

Choose `h_n->infinity` with `h_n=o(sqrt(ell_n))`. Then

\[
\pi_Y(B_Y(x,\ell_n-h_n))
\le C(Kk)^{-h_n}\to0.
\tag{7.2}
\]

Apply the upper/lower Green-shell bounds (3.4)--(3.5), (6.7), (7.2) and the radial CLT (5.10). We obtain the complete profile theorem

\[
\boxed{
 d_Y\!\left(
 \frac{\ell_n}{v}+z\sqrt{\ell_n}
 \right)
 \longrightarrow
 \Phi\!\left(-\frac{z}{\tau_{K,k}}\right),
}
\tag{7.3}
\]

where

\[
v=\frac{Kk-1}{(K+1)k},
\qquad
\tau_{K,k}^2
=\frac{(Kk+1)((K+1)k)^2}{(Kk-1)^3}.
\tag{7.4}
\]

In particular, for every fixed `0<epsilon<1`,

\[
\boxed{
 t_{mix}^{Y}(\epsilon)
 =\frac{(K+1)k}{Kk-1}\log_{Kk}|L|
 +O_{K,k,m,\epsilon}(\sqrt{\log |L|}).
}
\tag{7.5}
\]

This is ordinary SRW on a regular graph in the exact Salez rate-one continuous-time convention. The source theorem used for the shells is an NBRW theorem on a **different biregular graph**; (5.2) and the radial analysis are the nontrivial transfer.

## 8. The output is not long-range expanding when k>=2

The output degree is

\[
D=(K+1)k,
\]

so a `D`-regular tree has branching factor

\[
D-1=Kk+k-1.
\]

But (7.1) shows that `Y` has at most `(Kk)^r` growth at radius `r`. For `k>=2`,

\[
\boxed{Kk<D-1.}
\tag{8.1}
\]

Take

\[
r_n=\left\lfloor\frac12\log_{D-1}|L_n|\right\rfloor.
\]

Then `(D-1)^{r_n}=O(sqrt{|L_n|})`, so the unsaturated singleton part of Altschuler's long-range definition would require a fixed `c>0` with

\[
|B_Y(x,r_n)|\ge c(D-1)^{r_n}.
\]

Instead

\[
\frac{|B_Y(x,r_n)|}{(D-1)^{r_n}}
\le C\left(\frac{Kk}{D-1}\right)^{r_n}\to0.
\tag{8.2}
\]

Thus no fixed long-range constant exists. The output graphs are spectral expanders by (4.8) but **not** long-range expanders. This directly enforces the scope distinction required by the T08 assignment.

## 9. Concrete new class: p=2 non-Ramanujan Eisenstein Cayley bigraphs

Take the Eisenstein family `X_E^{p,q}` of Evra--Feigon--Maurischat--Parzanchevski with `p=2` and primes `q` tending to infinity, `q notin {2,3}`. Their Theorem 8.3 gives:

* `(p^3+1,p+1)=(9,3)` biregularity, so `K=8`, `k=2`;
* the left side is the finite group `G_q` and the Cayley bigraph is left-transitive;
* the bigraph is adj-Ramanujan but **non-Ramanujan**, with exceptional NBRW eigenvalues `+- i p^{3/2}`;
* the exceptional multiplicity is in fact `O_epsilon(|X|^{3/8+epsilon})`, stronger than the Sarnak--Xue exponent `delta=1/2` needed here;
* girth is larger than `2 log_p q`, hence eventually exceeds four and is 6-logarithmic in their terminology; and
* their NBRW has bounded-window cutoff, consistent with the stronger Green estimate above.

Let

\[
Y_q:=Half_L(X_E^{2,q}).
\tag{9.1}
\]

Then `Y_q` is a simple **18-regular vertex-transitive (indeed Cayley) graph**. Its spectral transfer is exact. Here

\[
(K+k-2\sqrt{Kk},K+k+2\sqrt{Kk})=(2,18),
\]

so the nontrivial squared singular values lie in `[2,18]` or are zero. Equation (4.5) maps these to

\[
[-7/18,1/2]\quad\text{or}\quad -1/2.
\]

Hence

\[
\boxed{\operatorname{gap}(Y_q)\ge1/2.}
\tag{9.2}
\]

The interior radial multiplicities are

\[
\boxed{
\{-1:1,\;0:1,\;+1:16\},
}
\tag{9.3}
\]

so

\[
\boxed{
v=\frac56,
\qquad
M_2=\frac{17}{18},
\qquad
\tau^2=\frac{204}{125}.
}
\tag{9.4}
\]

Writing `n_q=|V(Y_q)|=|G_q|`, the rate-one continuous-time cutoff center is

\[
\boxed{
T_q=\frac65\log_{16}n_q+O(1)
=\frac3{10}\log_2 n_q+O(1),
}
\tag{9.5}
\]

and the full profile is

\[
\boxed{
 d_{TV}^{Y_q}\!\left(
 T_q+z\sqrt{\log_{16}n_q}
 \right)
 \longrightarrow
 \Phi\!\left(-z\sqrt{\frac{125}{204}}\right).
}
\tag{9.6}
\]

For the Green term one may use the source hypothesis at its sharp exponent `1/2`. The stronger arithmetic estimate makes the margin explicit: choosing their exponent `3/8+1/16=7/16`, at the entropic shell the exceptional contribution already carries a factor `N^{-1/16}`, and an excess `h` supplies an additional `4^{-h}`. The ordinary bulk term decays as `16^{-h}`.

Finally, the output cannot be long-range. Its universal-cover shell growth is `16^r`, while an 18-regular long-range expander requires the 17-branching scale. Explicitly,

\[
\frac{|B_{Y_q}(x,r)|}{17^r}
\le C(16/17)^r,
\tag{9.7}
\]

and the ratio tends to zero at `r=floor((1/2)log_17 n_q)`.

This application is structurally different from the earlier P26 regular-base exact-distance-two theorem: the input here is a **biregular, non-Ramanujan Cayley bigraph**, and the regular T08 object is created by one-color halving. The proof uses Sarnak--Xue control of exceptional NBRW modes rather than a Ramanujan regular-base polynomial bound.

## 10. Exact sanity check

The exact-arithmetic script

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_10-10-50__bigraph_halved_green.py`

was executed before persistence. It verifies, for the `p=2` application:

* `D=18` and radial counts `{-1:1,0:1,+1:16}`;
* `v=5/6`, `M2=17/18`, `tau^2=204/125`;
* center coefficients `6/5` against `log_16 n` and `3/10` against `log_2 n`;
* the adj-Ramanujan squared-singular-value interval `[2,18]` and its output image `[-7/18,1/2]`, plus the zero-mode image `-1/2`;
* spectral gap at least `1/2`;
* the arithmetic exceptional exponent `7/16` leaves the exact entropic Green margin `1/16`; and
* the strict long-range branching mismatch `16<17`.

The archived output is

`proofnet24/P26-progress-cutoff-transfer/artifacts/2026-09-20/2026-09-20_10-10-50__bigraph_halved_green.out`

and ends

`P26_T08_BIGRAPH_HALVED_GREEN_EXACT_PASS`.

Artifact commits: code `bd31f55a5ebb170b335081b5872a1f16bd6c64c0`; executed output `f56de4db27cc5d89a86dddebd1aab16fa536c197`.

## 11. Residual obstruction and next attack

This does not solve Salez Problem 2.3. The new theorem obtains a shell Green front from a **Sarnak--Xue density theorem** for a structured biregular ancestor. An arbitrary vertex-transitive spectral expander need not arrive with such an ancestor or such a directed-edge density estimate.

The important mechanism-level lesson is stronger than another construction, however: polynomially many non-Ramanujan directed-edge modes are harmless if their density sits exactly below the branching entropy budget, because the Green excess at radius `log_{Kk}N+h` is then only exponentially large in `-h`. This is the density-weighted refinement that the preceding trimmed-mode report was seeking.

The next P26 attack should therefore remove the arithmetic ancestor, not produce another distance set: seek a **transitivity-forced weighted NBRW density inequality** of the form

\[
\sum_{j:\,|\theta_j|>\sqrt{Kk}}
\left(\frac{|\theta_j|^2}{Kk}\right)^r
\le \exp(o(\sqrt{\log n}))
\tag{11.1}
\]

at the entropic radius (or an entropy analogue), allowing polynomially many exceptional modes provided their excess growth is compensated by multiplicity. NM13-01 remains complementary: it is attacking point-start cancellation and stabilizer/orbit structure directly on transitive graphs, while P26 now owns density-to-Green shell transfer.

No failed-recovery switch is triggered: this run strictly enlarges theorem scope and supplies a proved application.

## ledger_delta

```text
slot: P26
parent: T08 / Salez arXiv:2508.21055 Problem 2.3
parent_before: OPEN/PARTIAL; regular-base Green transfers known, latest allowing only controlled exceptional sectors
parent_after: OPEN/PARTIAL; added a general biregular-halving cutoff theorem and an explicit non-Ramanujan arithmetic application
source_convention: exact rate-one CT, H_t = exp(t(Q-I))
mechanism_advance: quantitative shell chi^2 -> TV profile criterion plus Sarnak-Xue density -> exponentially decaying shell Green bound after entropic radius
new_class: left-halved graphs of left-transitive adj-Ramanujan Sarnak-Xue-density logarithmic-girth bigraphs
explicit_application: Half_L(X_E^{2,q}); degree 18; vertex-transitive/Cayley; gap >= 1/2; not long-range; Gaussian cutoff
center: (6/5) log_16 n + O(1) = (3/10) log_2 n + O(1)
window: Theta(sqrt(log n)); profile Phi(-z sqrt(125/204))
status: CANDIDATE_FULL restricted theorem/application pending later independent review; parent OPEN
publication_novelty: UNVERIFIED
companion_split: NM13-01 owns arc-cover Hodge/orbit route; P26 owns density-to-Green shell transfer
failed_routes_this_run: none; prior crude exceptional-counting route is strictly refined by weighted density
next_attack: transitivity-forced weighted NBRW spectral-density bound without an arithmetic/biregular ancestor
artifacts: 2026-09-20_10-10-50__bigraph_halved_green.py ; 2026-09-20_10-10-50__bigraph_halved_green.out
```

End of complete P26 substantive T08 report.
