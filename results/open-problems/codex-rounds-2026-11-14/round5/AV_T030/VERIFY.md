# T030 verification and round-5 continuation

Checked 15 November 2026. The earlier REPORT.md, LOG.md, PROOF.md where present, scripts and verification records in rounds 1, 3 and 4 were read without editing those folders. The first folder has no PROOF.md or computation scripts.

VERDICT: PARTIAL-CLAIMED bounded convex planar domains with smooth C-infinity boundary, for every nonzero real second Neumann eigenfunction, including multiplicity.

This is the literature verdict for the exact row. REPORT.md follows the later continuation instruction and reports the additional boundary-kernel lemma proved from the earlier interior result. Neither verdict certifies the complete preprint proof.

## Recommended new “where it stands” sentence

> OpenAI's unrefereed preprint *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026) claims both boundary-only extrema for every second Neumann eigenfunction on smooth bounded simply connected planar domains, including multiple eigenvalues, and thus covers smooth convex domains. The sources checked do not settle the full strict statement for arbitrary bounded convex planar domains. Later papers give conditional non-strict extensions or strict boundary maximum modulus, leaving the two signed boundary-only extrema on general nonsmooth convex domains uncovered.

Three sentences. The older special-case chronology in the supplied row is not independently re-audited here.

## 1. Relevant preprint: smooth hot spots

**OpenAI**, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, September 24, 2026. Opened the actual [main TeX](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/main.tex) and [introduction](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/01-introduction.tex), saved as source-hot-main.tex and source-introduction.tex. The main file gives the author and date above.

The setup is a nonempty bounded simply connected open set Ω in R² with C-infinity boundary. The eigenvalue μ=μ₁(Ω) is the mean-zero Neumann Rayleigh infimum; V is its real eigenspace. The text explicitly omits the constant mode from its numbering and identifies this μ₁ with μ₂ in the convention counting zero first.

Theorem 1.1, verbatim TeX:

```tex
\begin{theorem}\label{thm:main}
For every $0\ne u\in\V$,
\[
\grad u(x)\ne0\qquad(x\in\Omega).
\]
In particular,
\begin{equation}\label{eq:hotspots}
\min_{y\in\partial\Omega}u(y)<u(x)<\max_{y\in\partial\Omega}u(y)
\qquad(x\in\Omega).
\end{equation}
\end{theorem}
```

Our statement: “For a bounded convex domain in R^2, every eigenfunction of the second Neumann eigenvalue of the Laplacian attains its maximum and minimum only on the boundary.”

| Our words | Preprint | Coverage or gap |
|---|---|---|
| bounded domain | Nonempty bounded open connected domain | Same domain convention. |
| convex | Simply connected | Every convex planar domain has this topology. |
| in R² | In R² | Same Euclidean dimension and model. |
| No boundary regularity qualifier | C-infinity boundary | Additional hypothesis; arbitrary convex corners and other nonsmooth boundaries are excluded. |
| every eigenfunction | Every nonzero element of the real eigenspace V | Same universal quantifier, including multiplicity. |
| second Neumann eigenvalue of the Laplacian | First positive eigenvalue of −Δ with Neumann condition | Same spectral quantity; numbering convention differs. |
| maximum and minimum | Both strict inequalities against boundary extrema | Same two signed quantities, rather than maximum modulus alone. |
| only on the boundary | Strict interior inequalities, plus no interior critical points | At least the requested strength on the stated domain class. |
| Exact assertion for each bounded convex domain | Exact assertion for each smooth simply connected domain | No bound, asymptotic or generic-domain substitute. |

Thus it claims the whole conclusion on smooth convex planar domains. It does not state the arbitrary-convex-boundary conclusion. An approximation argument would have to preserve strictness and each member of a possibly multiple eigenspace; neither follows just by taking a limit of the displayed strict inequalities.

## 2. Optimal-transport candidate: NOT-THIS

**OpenAI**, *Global Support and Convex Injectivity Domains under Weak MTW*, September 25, 2026. Opened the actual [main TeX](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/main.tex) and [introduction](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/sections/introduction.tex), saved as source-mtw-main.tex and source-mtw-introduction.tex.

The model is a smooth connected compact Riemannian manifold (M,g) without boundary, dimension n≥2, with cost c(x,y)=d(x,y)²/2. I(x) is the tangent injectivity domain of expₓ; Gₓ is the closed minimizing-velocity domain. The referenced weak-MTW hypothesis is nonnegative MTW curvature on orthogonal pairs before cut. Potentials u and duals v are cost-transform pairs, not eigenfunctions; Γᵤ is the ordinary semiconvex subgradient graph, and Qₜ is squared-distance inf-convolution. Definitions and assumptions are in the saved introduction.

Theorem 1.1, verbatim TeX:

```tex
\begin{theorem}[Convexity of injectivity domains]\label{thm:main}
If $(M,g)$ satisfies \eqref{eq:weak-mtw}, then $I(x)$ is convex for
every $x\in M$. More precisely, for every $v_0,v_1\in I(x)$ and
$\theta\in[0,1]$,
\[
 (1-\theta)v_0+\theta v_1\in I(x).
\]
\end{theorem}
```

Theorem 1.2 is also a principal result. Verbatim TeX:

```tex
\begin{theorem}[Global support and intermediate geometry]
\label{thm:foundation}
Under \eqref{eq:weak-mtw}, every potential $u$, with its dual potential $v$,
has the following properties.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Every $p\in\partial u(x)$ belongs to $G_x$ and satisfies
\[
 u(x')\geq u(x)+c(x,\exp_xp)-c(x',\exp_xp)
 \qquad(x'\in M).
\]
For every $0<t<1$, the map $F_t:\Gamma_u\to M$,
$F_t(x,p)=\exp_x(tp)$, is a homeomorphism; $tp\in I(x)$ and $x$
is the unique global minimizing pole of $Q_tu$ at $F_t(x,p)$.
\item For every dual pair $(u,v)$, every $x$ and every $r$, the lifted section
\[
 \mathcal S_x(r)=\left\{p\in G_x:
 u(x)+\frac{|p|^2}{2}+v(\exp_xp)\leq r\right\}
\]
is compact and convex. If it is nonempty and $r\geq0$, then
\[
 \operatorname{diam}\mathcal S_x(r)^2
 \leq8\left(r+\osc_{p\in\mathcal S_x(r)}v(\exp_xp)\right).
\]
\item For $0<t<1$, one has $Q_tu=-Q_{1-t}v\in C^{1,1}(M)$.
Its $C^{1,1}$ seminorm and the Lipschitz constants of the pole and momentum
maps $F_t^{-1}$ depend only on $M,g,t$. There are also $r_t,b_t>0$,
depending only on $M,g,t$, such that, for $z=F_t(x,p)$,
\[
 u(x')+\frac{c(x',z)}t
 \geq u(x)+\frac{c(x,z)}t+b_t d(x,x')^2
 \quad\text{if }d(x,x')<r_t.
\]
These constants can be chosen uniformly on compact subintervals of $(0,1)$.
\end{enumerate}
No density hypothesis is required.
\end{theorem}
```

Comparison with our row: its ambient manifold is compact and has no boundary, rather than an arbitrary bounded convex subset of R² with a Neumann boundary condition. Although its dimension range includes two, its quantities are tangent injectivity domains, transport supports and potentials, with no second Laplace eigenvalue or eigenfunction. The conclusion concerns convexity, support and regularity, with neither signed extrema nor boundary-only attainment. Neither theorem covers a part of T030.

## 3. Complex-geometry candidate: NOT-THIS

**OpenAI**, *Symmetry of semialgebraic bounded domains with compact quotient*, September 24, 2026. Opened the actual [paper TeX](https://github.com/openai/math/blob/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex), saved as source-symmetry.tex. The author and date are in that file.

Theorem 1.1, verbatim TeX:

```tex
\begin{theorem}\label{thm:main}
Let \(U\) be a nonempty connected semialgebraic bounded open subset of a
complex affine variety. Suppose that a group \(\Gamma\) of
biholomorphisms acts properly discontinuously on \(U\) and that
\(U/\Gamma\) is compact. Then \(U\) is smooth and is biholomorphic to a
bounded symmetric domain.
\end{theorem}
```

Comparison: the ambient space is a complex affine variety embedded in Cᴺ, with arbitrary complex dimension, and openness is in its complex-space topology. The hypotheses are semialgebraicity and a properly discontinuous biholomorphic action with compact quotient. The quantity being classified is the complex domain itself; there is no Neumann eigenvalue or eigenfunction, nor a conclusion about either signed extremum. Even in complex dimension one, a biholomorphic classification does not state the Euclidean Neumann assertion. “Smooth” concerns the complex space U, not the boundary regularity of our real planar domains. This covers no part of T030.

## 4. Follow-ups actually opened

The update search was limited to five minutes. Web-tool queries included the exact hot-spots title, that title with error/refutation/correction, and hot spots/convex/November 2026/proof variants. No new full strict general-convex result or direct refutation appeared in the returned results; this is a bounded search finding. No SOLVED_ELSEWHERE.md is warranted.

- **Krzysztof Burdzy**, *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*, [arXiv:2610.12622v1, full HTML](https://arxiv.org/html/2610.12622v1), October 8, 2026; paper dated October 7. Opened the full paper, especially the human commentary, Theorem 2.1 and Corollary 2.2. It treats OpenAI's smooth theorem as an external input, assumes compact Neumann resolvent and a simple first-positive eigenvalue, and obtains a non-strict conclusion. It does not exclude an interior point sharing an extremal value. The commentary says the paper was generated by ChatGPT and that the human author has not checked every detail; it is not a referee certification of OpenAI's proof.

- **Rodrigo Bañuelos**, *Hot Spots: From Smooth to Nonsmooth Simply Connected Planar Domains*, [arXiv:2610.32920 abstract](https://arxiv.org/abs/2610.32920) and [full HTML v1](https://arxiv.org/html/2610.32920v1), submitted October 23, 2026; paper dated October 20. The author spelling follows the full paper; the abstract metadata has a typo. Theorem 1.2 is conditional on the smooth input, assumes finite area, compact Sobolev embedding and a simple first-positive eigenvalue, and gives non-strict boundary-layer extrema. For continuous eigenfunctions on bounded domains, boundary attainment follows, but interior equality is expressly not excluded. Section 6 explains the multiplicity obstruction; its favorable limiting eigenfunction does not give every prescribed eigenfunction.

- **Haiyun Deng, Xuyong Jiang, Xiaoping Yang**, *Near-boundary rigidity and strict maximum modulus for Neumann eigenfunctions on convex planar domains*, [full HTML arXiv:2610.18546v2](https://arxiv.org/html/2610.18546v2), November 2, 2026. Opened Theorem 1.2, the scope discussion and Example 4.4. It claims strict boundary maximum modulus for every second Neumann eigenfunction on arbitrary bounded convex planar domains, allowing multiplicity. This controls |u|, and does not alone control an extremum of smaller absolute value. The paper explicitly distinguishes this from the full strict hot-spots conclusion. Its centrally symmetric special case supplies both signed extrema, which still does not cover general convex domains.

Read-only GitHub issue search `repo:openai/math "hot spots"` returned an empty issue list. Earlier verification files record additional expositions, unrelated-candidate searches and a published comparator acceptance log; these are inherited records, not new independent validation in this session. No inaccessible lead or unopen paper is used as settlement evidence.

## 5. Lean artifacts opened

Opened and saved the actual [scope document 369](https://github.com/openai/math/blob/main/lean/docs/369.md), [HotSpots challenge target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.lean), and [supplied proof module Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Analysis/HotSpots/Main.lean). Local files are source-lean-scope.md, source-lean-target.lean and source-lean-main.lean.

The target includes SmoothBoundary in AdmissibleDomain, defines the first-positive value by the mean-zero Rayleigh infimum, and asks for nonvanishing gradient and both strict inequalities. Its `sorry` is a placeholder in the challenge statement; a separate supplied solution is present. The actual Main.lean contains `noncritical_at_disk`, `noncritical`, and `main_theorem`, importing further modules. No local Lean compilation, comparator replay, dependency audit or axiom audit was performed. Reading these files does not establish nonsmooth scope or certify the entire proof.

Also opened and saved the unrelated candidates' [scope 360](https://github.com/openai/math/blob/main/lean/docs/360.md) and [scope 058](https://github.com/openai/math/blob/main/lean/docs/058.md). The former concerns optimal transport and explicitly limits one intermediate assertion to finite target families; the latter concerns complex symmetry. Neither addresses T030.

## 6. Earlier result independently rechecked

The fresh hot-spots introduction and reciprocal-kernel section have the same source contents as round 4. Their GitHub blob identifiers are ca7f7f292379a95899f04a1de411eb610d1fe9ab and bcb125482dbfe6874ffe4582625c01ea66571ca9. The smooth-boundary scope finding remains unchanged.

Section 1 of [PROOF.md](PROOF.md) independently rederives the uniform Green moments by superlevel sets and by radial integration, then recovers the source error

\[
 \sup_x\|G(x,\cdot)-C_\epsilon(x,\cdot)\|_{L^2(\rho)}
 \le\epsilon\sqrt{3A/(2\pi)}.
\]

It also rechecks the Hilbert–Schmidt operator error, resolvent boundedness and the zero reciprocal diagonal. The round-4 main claim holds.

Command rerun without writing in the earlier folder:

`OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/AV_T030/check_singular_limit.py`

It passed exact moment recurrences, 28 high-precision regularization cases, four diagonal cases and 18 exact-rational correction checks. Inherited priority 20; peak RSS 15,204,352 bytes; under one second.

## Spot check

The chosen next step was `lem:bordered`, named in round 4's report. [PROOF.md](PROOF.md) now derives its full boundary passage from the earlier interior reciprocal-inertia proposition under the manuscript's stated bounded-density and strict-contraction assumptions. This is a check of this lemma, not a certification of the manuscript or a new class of hot-spots domains.

For density bounded by A, define H=12^(1/3) A/π, B=sqrt(A/(2π)) and m=q(D). Ordinary-area Hölder gives the uniform smoothing bound

\[
 \sup_{s,x}(TP_s)(x)\le H.
\]

Thus one Green integration puts every Poisson section into L²(q). The proof establishes

\[
 K(p,s)\le P_s(p)+H+\frac{BH\sqrt m}{1-d},
\]

and, for distinct boundary points,

\[
 R(s,t)\le\frac{2A}{\pi|s-t|}+\frac{AH}{2}+\frac{H^2m}{1-d}.
\]

The two radial normalizations are

\[
 G(rs,x)/(1-r)\longrightarrow P_s(x),\qquad
 G(rs,rt)/(1-r)^2\longrightarrow1/(\pi|s-t|^2),
\]

with the first convergence uniform on fixed compact interior sets. Explicit logarithms and independent boundary differentiation give the same factors. On compact support this gives L² source convergence and the required resolvent pairings. Positive diagonal congruence preserves inertia; its finite limit gives the compact-support bordered matrix. Nonnegative chain monotone convergence removes the support cutoff; the displayed estimates prove the limits finite. A second finite-matrix limit proves `lem:bordered` for the full q.

The stress case q=dx satisfies the form inequality with d=1/2, yet

\[
 \int_{|x|\le R}P_s(x)^2\,dx
 =[-R^2-2\log(1-R^2)]/(4\pi)\longrightarrow\infty.
\]

A local cone lower bound independently proves this divergence. Therefore an unrestricted L²(q) assertion for P_s would fail inside the permitted hypotheses; the preprint avoids it, and so does this audit. R(s,s) can be infinite, which is consistent with the distinct-point statement and zero reciprocal diagonal. No defect was found in the checked boundary passage.

Command:

`OMP_NUM_THREADS=1 nice -n 15 python3 check_boundary_limits.py`

It passed 120 one-boundary and 75 two-boundary high-precision cases, four independent Poisson-square integral checks, 20 exact-rational zero-potential inertia checks and 140 squared-distance/sign identities. The moment and Hölder constants were checked exactly. Peak RSS 14,827,520 bytes; priority 20; under one second. These arithmetic checks supplement the analytic proof and do not discretize the full eigenfunction problem.

Next: check the final bordered-form-to-conditional-negativity algebra, then `lem:hilbert` and the infinite-coordinate energy summation `eq:sum-energy`, including the trace-nullspace implication. The vector variational and eigenfunction arguments remain uncertified here.

Only this task folder was written. No git, posting, accounts, external state changes, subagents, GPU or heavy computation were used.

Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, 07:22 Asia/Tbilisi.
