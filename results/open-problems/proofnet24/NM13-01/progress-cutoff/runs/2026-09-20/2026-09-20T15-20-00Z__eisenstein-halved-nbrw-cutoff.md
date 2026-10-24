Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# NM13-01 / LIVE20 T08 — Eisenstein halved Cayley cutoff from NBRW shells

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A--D below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded dated search for combinations of `halved graph`, `Cayley bigraph`, `distance-2 graph`, `random walk cutoff`, and `biregular cutoff` found graph-theoretic halved-graph literature but no matching ordinary-SRW cutoff theorem for the class below. This is only negative evidence, not a priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/`.

## 0. Compact handoff, partner split, and preserved history

The newest own substantive report read before this run was

`2026-09-20T14-15-00Z__schreier-hecke-fiber-cutoff.md`.

It proved a stochastic Schreier-fiber transfer, an explicit finite nonnormal Schreier-fiber cutoff class, and the canonical lossless Hecke lift `A -> A/H` for every finite vertex-transitive graph. Its remaining structural obstruction was that the stabilizer may be large and nonnormal, so the resulting `H`-bi-invariant convolution can live in a high-dimensional noncommutative Hecke algebra with no separated uniformly gapped refresh component.

The newest relevant P26 report read was

`proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_16-56-12__hermitian-nbrw-berry-green-transfer.md`.

P26 now owns a quantitative Berry--Green finite-orbit shell transfer and Hermitianized two-step NBRW edge graphs on fully Ramanujan `(9,3)` arithmetic bigraphs. The present run deliberately does **not** reuse its Green-function cleanup or Hermitian edge operator. Instead it uses a transitivity-specific incidence refinement: a left-transitive Cayley bigraph, its left halved Cayley graph, and direct projection of NBRW to the halved shells.

The root `POSTED.md` exclusion for the Salez Problem 2.4 / Cayley product-condition manuscript was rechecked and is not reopened.

There is no intake-only or audit loop here. The substantive new work is Theorems A--D and their explicit Eisenstein application.

## 1. Exact source problem and current primary boundary

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), defines the continuous-time chain by inserting independent mean-one exponential holding times between jumps. For a discrete transition matrix `P`, the exact convention is

\[
H_t=e^{t(P-I)}=e^{-t}\sum_{j\ge0}\frac{t^jP^j}{j!}.
\tag{1.1}
\]

Problem 2.3 is exactly:

> Prove that all vertex-transitive expanders exhibit cutoff.

A fresh 20 September 2026 source check still leaves that problem open.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Hence long-range expansion is genuinely stronger than the spectral-expander hypothesis in Salez's problem.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026 (with a later July revision), prove a local-product / non-equilibrium-Poincare cutoff mechanism. The checked result does not deduce its non-equilibrium constant solely from transitivity plus the ordinary spectral gap.
* Shai Evra--Brooke Feigon--Kathrin Maurischat--Ori Parzanchevski, `Ramanujan Bigraphs`, `arXiv:2312.06507` (2026 revision), provide the new primary input used here. Their Theorem 8.3 constructs explicit Eisenstein Cayley bigraphs which are adj-Ramanujan but non-Ramanujan, satisfy Sarnak--Xue density, have logarithmic girth, and nevertheless have a quantitative bounded NBRW cutoff window.

The last item is important because the same paper explicitly notes after Corollary 4.12 that its SRW cutoff proof on a biregular bigraph needs **full** Ramanujan, not merely adj-Ramanujan. The present operation bypasses precisely that obstruction.

## 2. Original problem before / after

### Before this run

Salez Problem 2.3 was open. NM13-01 already had several bounded-degree vertex-transitive spectral-but-not-LRE cutoff classes, most recently finite stochastic Schreier fibers over a cutoff base. Those classes all exposed an exact macroscopic quotient and a separately dissipating fiber.

### After this run

Salez Problem 2.3 remains open.

The strict new proved scope is:

> **Eisenstein-halved class.** Fix a prime `p == 2 (mod 3)`. Let `X_E^{p,q}` be the Evra--Feigon--Maurischat--Parzanchevski Eisenstein Cayley bigraph as `q -> infinity` through allowed primes, and let `H_{p,q}` be its left halved graph: the vertices are the left vertices of `X_E^{p,q}`, with two joined when they share a right neighbor. Then `H_{p,q}` is a fixed-degree Cayley spectral-expander sequence, fails every fixed positive long-range-expansion constant, and rate-one continuous-time SRW on `H_{p,q}` has an explicit Gaussian TV cutoff profile with `O(sqrt(log n))` window and finite-size profile error `O_Z(log log n / sqrt(log n))`.

For the concrete `p=2` Eisenstein family, the output graphs are **18-regular Cayley graphs** with one-sided normalized spectral gap at least

\[
\boxed{\gamma_H\ge\frac12.}
\tag{2.1}
\]

Writing `n=|V(H)|`, the cutoff center is

\[
\boxed{T_n=\frac3{10}\log_2 n,}
\tag{2.2}
\]

and for every fixed `Z<infinity`, uniformly for `|z|<=Z`,

\[
\boxed{
 d_H\!\left(\frac3{10}\log_2 n+z\sqrt{\log_2 n}\right)
 =\Phi\!\left(-z\sqrt{\frac{125}{51}}\right)
 +O_Z\!\left(\frac{\log\log n}{\sqrt{\log n}}\right).
}
\tag{2.3}
\]

Consequently, for every fixed `epsilon in (0,1)`,

\[
\boxed{
 t_{\rm mix}(\epsilon)
 =\frac3{10}\log_2 n
 -\sqrt{\frac{51}{125}}\,\Phi^{-1}(\epsilon)\sqrt{\log_2 n}
 +O_\epsilon(\log\log n).
}
\tag{2.4}
\]

This is ordinary SRW on the **output Cayley graphs themselves**, in Salez's exact continuous-time convention.

## 3. Left halving of a Cayley bigraph is an ordinary Cayley graph

Let

\[
X=(L\sqcup R,E)
\]

be a simple `(K+1,k+1)`-biregular graph. Its **left halved graph** `Hal_L(X)` has vertex set `L`; distinct `x,y in L` are adjacent precisely when they have a common neighbor in `R`.

Now suppose

\[
X=\operatorname{CayB}(G,\{S^i\}_{i=1}^{K+1})
\tag{3.1}
\]

is a Cayley bigraph in the sense of EFMP Definition 2.4. Their Definition 2.1 gives pairwise disjoint sets `S^i`, each of size `k`, with

\[
S:=\bigsqcup_{i=1}^{K+1}S^i,
\qquad S^{-1}=S,
\qquad e\notin S.
\tag{3.2}
\]

The bi-Cayley axiom also says that if `s,t in S^i` are distinct, then `s^{-1}t in S`. The right vertex `[g,i]` is incident to `g` and to the `gs` with `s in S^i` (with the appropriate equivalent labels). Therefore any two distinct left vertices in one right block differ by an element of `S`, and every Cayley edge `g--gs`, `s in S`, lies in such a right block. Hence

\[
\boxed{
\operatorname{Hal}_L(X)=\operatorname{Cay}(G,S).
}
\tag{3.3}
\]

In particular it is vertex-transitive and has degree

\[
\boxed{D=|S|=(K+1)k.}
\tag{3.4}
\]

This is the first transitivity-specific ingredient: the incidence refinement produces a non-tree local geometry but the halved output remains an ordinary Cayley graph.

## 4. The halved biregular-tree cover and its scalar radial chain

Let

\[
T=T_{K+1,k+1}
\]

be the `(K+1,k+1)`-biregular tree and let

\[
Z=\operatorname{Hal}_L(T).
\tag{4.1}
\]

Each right vertex of `T` becomes a clique of size `k+1` in `Z`; each left vertex belongs to `K+1` such cliques. Thus `Z` is a tree of fixed cliques, not a tree.

Suppose `X` has girth greater than four. A graph cover `T -> X` induces a graph cover

\[
\boxed{Z\longrightarrow \operatorname{Hal}_L(X).}
\tag{4.2}
\]

Indeed, the `D=(K+1)k` neighbors of a left lift are exactly the two-step paths through one of its `K+1` right neighbors and then to one of the `k` other left vertices. Girth greater than four says their images are distinct, so the induced map is locally bijective.

Fix a root `o in Z`. The root stabilizer in `Aut(T)` is transitive on every left sphere, hence the lifted SRW is uniform on a sphere conditional on its radius. Put

\[
R_t=d_Z(o,Y_t).
\]

At every radius `r>=1`, a vertex has:

* one neighbor at radius `r-1` (through the incoming right block),
* `k-1` neighbors at radius `r` (the other vertices of that same clique), and
* `Kk` neighbors at radius `r+1` (through the other `K` right blocks).

Set

\[
Q:=Kk,
\qquad D=(K+1)k=Q+k.
\tag{4.3}
\]

For the discrete jump chain, away from zero the radial increment `xi` therefore has law

\[
\Pr(\xi=1)=\frac QD,
\qquad
\Pr(\xi=0)=\frac{k-1}{D},
\qquad
\Pr(\xi=-1)=\frac1D.
\tag{4.4}
\]

At the root the next radius is always one. Define

\[
\boxed{
 v:=\mathbb E\xi=\frac{Q-1}{D},
 \qquad
 a:=\mathbb E\xi^2=\frac{Q+1}{D}.
}
\tag{4.5}
\]

The sphere sizes are exact:

\[
\boxed{
|S_Z(o,0)|=1,
\qquad
|S_Z(o,r)|=D Q^{r-1}\quad(r\ge1).
}
\tag{4.6}
\]

Thus for an `n`-vertex quotient the entropic radius is

\[
\ell_n=\log_Q n.
\tag{4.7}
\]

### Boundary correction and a quantitative radial CLT

Let `xi_1,xi_2,...` be iid with law (4.4). Couple the discrete radial chain by using `xi_j` whenever the radius is positive and replacing the proposed increment by `+1` whenever the radius is zero. Then pathwise

\[
R_m=\sum_{j=1}^m\xi_j+C_m,
\qquad C_m\ge0.
\tag{4.8}
\]

Every boundary replacement changes the proposed increment by at most two. Starting from radius one, the probability ever to hit zero is exactly `1/Q`. To see this, the function

\[
h(r)=Q^{-r}
\]

is harmonic for (4.4) on the positive integers, equals one at zero and tends to zero. Hence, by the strong Markov property, the total number `V` of departures from zero has a geometric tail

\[
\Pr(V\ge m)=Q^{-(m-1)}.
\tag{4.9}
\]

Therefore

\[
0\le C_m\le C_\infty\le2V,
\tag{4.10}
\]

and `C_infinity` has a uniform exponential tail.

In the source rate-one continuous-time convention, the number of graph jumps by time `t` is an independent `N_t ~ Poisson(t)`. Hence

\[
S_t:=\sum_{j=1}^{N_t}\xi_j
\tag{4.11}
\]

is a compound Poisson variable with

\[
\mathbb ES_t=vt,
\qquad
\operatorname{Var}(S_t)=a t.
\tag{4.12}
\]

Since `xi` is bounded, the ordinary Berry--Esseen estimate for a compound Poisson sum gives

\[
\sup_x\left|
\Pr\!\left(\frac{S_t-vt}{\sqrt{at}}\le x\right)-\Phi(x)
\right|
\le\frac{C}{\sqrt{t+1}}.
\tag{4.13}
\]

From (4.8)--(4.10), for any `M>0`,

\[
\Pr(S_t\le x-M)-\Pr(C_\infty>M)
\le \Pr(R_t\le x)
\le \Pr(S_t\le x).
\tag{4.14}
\]

Taking `M=c log(t+2)` with `c` large enough and using (4.13) yields

\[
\boxed{
\sup_x\left|
\Pr\!\left(\frac{R_t-vt}{\sqrt{at}}\le x\right)-\Phi(x)
\right|
\le C_{K,k}\frac{\log(t+2)}{\sqrt{t+1}}.
}
\tag{4.15}
\]

No Green-function estimate is used here; the fluctuation calculation is a scalar consequence of the clique-block cover.

## 5. Shell laws are projections of even-time NBRW

Let `P_NB` denote NBRW on directed edges of `X`, and restrict even times to the directed left-to-right edges `LR->`. The stationary law there is uniform; denote it by `u_LR`.

For a root `o in L`, let `nu_r^o` be the projection to `Hal_L(X)` of the uniform radius-`r` sphere in `Z` under (4.2). Let `tail(e)` denote the left tail of a directed edge `e in LR->`. Then

\[
\boxed{
\nu_r^o
=
\operatorname{tail}_*\left[
\frac1{K+1}
\sum_{\substack{e:\operatorname{tail}(e)=o}}
\delta_e P_{NB}^{2r}
\right].
}
\tag{5.1}
\]

To verify (5.1), start from a directed edge `o -> r_0`. Two NBRW steps choose one of the `k` other left vertices in the same right block and then one of the `K` new right blocks. The final right-block choice does not change the projected left endpoint. Iterating gives exactly a geodesic in the halved tree, with `Q=Kk` choices per additional block. Conversely every halved-tree geodesic has exactly the same number of final outgoing-right-edge labels, so the pushforward is uniform on the sphere.

Since `tail_* u_LR` is uniform on `L`, data processing and convexity give the direct shell bound

\[
\boxed{
\|\nu_r^o-\pi_L\|_{TV}
\le
\sup_{e\in\overrightarrow{LR}}
\|\delta_eP_{NB}^{2r}-u_{LR}\|_{TV}.
}
\tag{5.2}
\]

This is the second transitivity-specific ingredient. It converts a sharp **edge geodesic-flow** statement into shell mixing for ordinary SRW, with no entropy or Green cleanup.

## 6. Theorem A — quantitative NBRW-shell transfer to ordinary SRW

Let `(X_n)` be a sequence of simple `(K+1,k+1)`-biregular graphs of girth greater than four, and assume their left halved graphs `H_n` are transitive. Write

\[
n=|V(H_n)|,
\qquad
\ell_n=\log_Q n,
\qquad Q=Kk>1.
\]

Assume there exist `h_n=O(log ell_n)` and `epsilon_n=o(1)` such that

\[
\sup_{r\ge\ell_n+h_n}
\sup_o\|\nu_r^o-\pi_n\|_{TV}
\le\epsilon_n.
\tag{6.1}
\]

Then, for every `t`,

\[
\boxed{
\Pr(R_t\le\ell_n-h_n)-C Q^{-h_n}
\le d_{H_n}(t)
\le
\Pr(R_t<\ell_n+h_n)+\epsilon_n.
}
\tag{6.2}
\]

**Proof.** For the lower bound, all shells of radius at most `ell_n-h_n` are supported in the image of the corresponding cover ball. By (4.6), its stationary mass is at most `C Q^{-h_n}`. Test TV against that ball.

For the upper bound, decompose the lifted walk by its radius. The total early-shell mass costs at most `Pr(R_t<ell_n+h_n)` in TV. Replace each late shell by stationarity and use convexity plus (6.1). `QED`

Combining (6.2) with (4.15) gives the quantitative profile. Put

\[
T_n=\frac{\ell_n}{v},
\qquad
\tau=\frac{\sqrt a}{v^{3/2}}.
\tag{6.3}
\]

If additionally `epsilon_n=O(ell_n^{-2})`, then for every fixed `Z`, uniformly for `|z|<=Z`,

\[
\boxed{
 d_{H_n}(T_n+z\sqrt{\ell_n})
 =\Phi\!\left(-\frac z\tau\right)
 +O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right).
}
\tag{6.4}
\]

Indeed,

\[
\frac{\ell_n\pm h_n-v(T_n+z\sqrt{\ell_n})}
{\sqrt{a(T_n+z\sqrt{\ell_n})}}
=-\frac{zv^{3/2}}{\sqrt a}
+O_Z\!\left(\frac{h_n+1}{\sqrt{\ell_n}}\right).
\tag{6.5}
\]

Inverting the profile yields

\[
\boxed{
 t_{\rm mix}(\epsilon)
 =\frac{\ell_n}{v}
 -\tau\Phi^{-1}(\epsilon)\sqrt{\ell_n}
 +O_\epsilon(\log\ell_n).
}
\tag{6.6}
\]

## 7. Theorem B — the EFMP Eisenstein family satisfies the shell hypothesis

Fix a prime

\[
p\equiv2\pmod3.
\]

EFMP Theorem 8.3 constructs, for allowed primes `q`, an Eisenstein Cayley bigraph

\[
X_E^{p,q}
=\operatorname{CayB}(G_q,\{S_{p,q}^i\})
\tag{7.1}
\]

with

\[
K=p^3,
\qquad k=p.
\tag{7.2}
\]

The theorem states that `X_E^{p,q}` is adj-Ramanujan but non-Ramanujan, satisfies Sarnak--Xue density, has girth larger than `2 log_p q`, and has quantitative NBRW cutoff. If `M=|E(X_E^{p,q})|` and `t_epsilon` is worst-start NBRW TV mixing time (restricted to the even times), then for

\[
0<\epsilon<\frac{p^{3/2}}6
\]

it gives

\[
\boxed{
 t_\epsilon
 <\frac12\log_p M+2\log_p\frac1\epsilon+3.
}
\tag{7.3}
\]

Here

\[
M=(p^3+1)n,
\qquad n=|G_q|=|L|.
\tag{7.4}
\]

Set

\[
Q=Kk=p^4,
\qquad
\ell_n=\log_Q n=\frac14\log_p n.
\tag{7.5}
\]

By (5.2), a radius-`r` shell is within `epsilon` of uniform as soon as `2r>=t_epsilon`. Therefore (7.3) implies

\[
\|\nu_r-\pi\|_{TV}\le\epsilon
\quad\text{whenever}\quad
r\ge
\ell_n+\frac14\log_p(p^3+1)
+\log_p\frac1\epsilon+2.
\tag{7.6}
\]

Choose

\[
\epsilon_n=\ell_n^{-3},
\qquad
h_n=3\log_p\ell_n+\frac14\log_p(p^3+1)+2.
\tag{7.7}
\]

Then `h_n=O(log ell_n)=o(sqrt(ell_n))` and (6.1) holds with `epsilon_n=ell_n^{-3}`. The girth bound in Theorem 8.3 is greater than four for all large `q`, so the halved-tree covering argument applies. Theorem A therefore proves ordinary source-continuous-time SRW cutoff on the halved graphs.

## 8. Theorem C — explicit spectrum and expander gap

Let `C` be the biadjacency matrix from the left side to the right side of `X_E^{p,q}`. For large `q`, girth greater than four implies that two distinct left vertices share at most one right neighbor. Hence the adjacency matrix `A_H` of the left halved graph satisfies

\[
\boxed{
CC^*= (K+1)I+A_H.
}
\tag{8.1}
\]

EFMP Corollary 3.3 states that adj-Ramanujan is equivalent to the nontrivial spectrum of `CC^*` lying in

\[
[K+k-2\sqrt{Kk},\ K+k+2\sqrt{Kk}]\cup\{0\},
\tag{8.2}
\]

apart from the trivial value `(K+1)(k+1)`.

Since `H` has degree `D=(K+1)k`, every nontrivial normalized eigenvalue is therefore at most

\[
\rho_{K,k}
=\frac{k-1+2\sqrt{Kk}}{(K+1)k}.
\tag{8.3}
\]

For the Eisenstein parameters `K=p^3`, `k=p`, `sqrt(Kk)=p^2`, this becomes

\[
\boxed{
\operatorname{gap}(H_{p,q})
\ge
1-\frac{2p^2+p-1}{p^4+p}>0.
}
\tag{8.4}
\]

Thus the outputs are a bounded-degree spectral-expander sequence for every fixed allowed `p`.

For `p=2`,

\[
K=8,\quad k=2,\quad Q=16,\quad D=18,
\]

and (8.4) gives the particularly clean value

\[
\boxed{\operatorname{gap}(H_{2,q})\ge\frac12.}
\tag{8.5}
\]

## 9. Theorem D — explicit cutoff constants and failure of LRE

For the Eisenstein parameters,

\[
D=p^4+p,
\qquad Q=p^4,
\tag{9.1}
\]

so the radial constants (4.5) are

\[
\boxed{
 v_p=\frac{p^4-1}{p^4+p},
 \qquad
 a_p=\frac{p^4+1}{p^4+p}.
}
\tag{9.2}
\]

With `n=|G_q|`, the center is

\[
\boxed{
T_n
=\frac1{v_p}\log_{p^4}n
=\frac{p^4+p}{4(p^4-1)}\log_p n.
}
\tag{9.3}
\]

On the `sqrt(log_{p^4} n)` time scale the Gaussian profile is

\[
\boxed{
 d_H(T_n+z\sqrt{\log_{p^4}n})
 =\Phi\!\left(-z\frac{v_p^{3/2}}{\sqrt{a_p}}\right)
 +O_Z\!\left(\frac{\log\log n}{\sqrt{\log n}}\right).
}
\tag{9.4}
\]

Equivalently, on the `sqrt(log_p n)` scale the coefficient in the Gaussian is doubled.

For `p=2`,

\[
v=\frac56,
\qquad a=\frac{17}{18},
\qquad
\frac{4v^3}{a}=\frac{125}{51},
\tag{9.5}
\]

which is exactly (2.2)--(2.4).

### The outputs are not fixed-constant long-range expanders

The cover ball in `Z` has size

\[
|B_Z(o,r)|
=1+D\frac{Q^r-1}{Q-1}
\le C_{p}Q^r.
\tag{9.6}
\]

Every path in `H` lifts from a fixed root, so the same upper bound holds for every output ball:

\[
|B_H(x,r)|\le C_p Q^r.
\tag{9.7}
\]

But the degree of `H` is `D`, and

\[
D-1=p^4+p-1>p^4=Q.
\tag{9.8}
\]

At

\[
r_n=\left\lfloor\frac12\log_{D-1}n\right\rfloor,
\]

we have `(D-1)^{r_n}=n^{1/2+o(1)}` and

\[
\frac{|B_H(x,r_n)|}{(D-1)^{r_n}}
\le
n^{-\beta_p+o(1)},
\qquad
\boxed{
\beta_p=\frac12\left(1-\frac{\log(p^4)}{\log(p^4+p-1)}\right)>0.
}
\tag{9.9}
\]

For `p=2`,

\[
\boxed{
\beta_2
=\frac12\left(1-\frac{\log16}{\log17}\right)
=0.010698915763548\ldots>0.
}
\tag{9.10}
\]

Since `(D-1)^{r_n}<3n/4` for large `n`, Altschuler's LRE inequality applied to a singleton would require a fixed positive multiple of `(D-1)^{r_n}`. Equation (9.9) rules that out for every fixed positive LRE constant.

Thus the new class is genuinely **spectral-expander but not long-range-expander**, so the cutoff theorem is not a disguised application of Altschuler's LRE result.

## 10. Mechanism-level obstruction removed

The source-level conjecture is unchanged, but a specific obstruction is removed.

EFMP explicitly observe that their direct **SRW** cutoff deduction on `(K+1,k+1)` bigraphs requires full Ramanujan and not only adj-Ramanujan. Their Eisenstein family is deliberately adj-Ramanujan but non-Ramanujan; Sarnak--Xue density is enough to recover sharp **NBRW** mixing, not their direct vertex-SRW theorem.

The halving operation changes that situation. It converts each two-step left-to-left geodesic move into one ordinary edge of a vertex-transitive Cayley graph. The local cover is then a tree of cliques with a scalar radial drift, and the NBRW law is exactly the late-shell law after projection. Consequently:

> **Full Ramanujan control of the ancestor is not necessary for ordinary SRW cutoff after a transitivity-preserving incidence halving. Sharp NBRW mixing from Sarnak--Xue density is sufficient.**

This also removes, for this class, the obstruction left by the preceding NM13 Hecke run: there is no need to find a small normal quotient or a separately gapped refresh inside a high-dimensional noncommutative Hecke algebra. A finite local block system and its geodesic flow supply the sharp macroscopic variable instead.

What remains for the general conjecture is narrower. An arbitrary vertex-transitive spectral expander need not admit a bounded-clique incidence cover whose shell law is governed by a sharp NBRW factor. The next algebraic target is therefore to extract an analogous finite local block/geodesic skeleton from root-stabilizer suborbits (or a bounded-rank coherent configuration), and failing that, to control the exact Hecke likelihood/varentropy without such a skeleton.

This is complementary to P26: P26 controls late shells by Green functions and finite-orbit spectral smoothing; the present route controls them by an exact transitive incidence refinement and a primary-source NBRW cutoff theorem.

## 11. Essential sanity checks

Executed checker:

`2026-09-20T15-20-00Z__check_eisenstein_halved.py`

Archived output:

`2026-09-20T15-20-00Z__check_eisenstein_halved.out`

It verifies exactly for `p=2`:

\[
K=8,\quad k=2,\quad Q=16,\quad D=18,\quad
v=5/6,\quad a=17/18,
\]

\[
\gamma_H\ge1/2,\qquad
T_n=(3/10)\log_2n,\qquad
c_{\rm profile}^2=125/51,\qquad
c_{\rm quantile}^2=51/125,
\]

and the sphere counts `1,18,288,4608,73728` through radius four. It also independently checks the matrix identity `A_H=BB^T-3I` on the Fano incidence graph and its resulting halved spectrum. The output ends

`ALL_EXACT_CHECKS_PASS`.

These finite/symbolic checks are sanity checks only. The asymptotic theorem is proved in Sections 3--9 and relies on the quantitative EFMP NBRW theorem, not on finite experimentation.

## 12. Short handoff

Parent status remains `OPEN`. The restricted theorem is `CANDIDATE_FULL`, publication novelty `UNVERIFIED`.

The next NM13 attack should stay algebraic/transitivity-specific rather than duplicating P26's Green route: start from the canonical `A/H` Hecke realization and look for a **bounded local block system** in the root-stabilizer suborbit graph whose block-geodesic flow has a sharp `O(log n)` entropic frontier. The halved-bigraphed theorem above shows that such a block skeleton can bypass both full Ramanujan control and separated-fiber dissipation. If no bounded block system exists, the fallback is the exact quotient likelihood/varentropy route already isolated in the earlier stabilizer report.
