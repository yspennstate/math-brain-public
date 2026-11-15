# T030 verification and round-6 continuation

Checked 15 November 2026. Read the round-3, round-4 and round-5 reports, logs, proofs and scripts without editing them. Current source files and blob identifiers are recorded in sources_manifest.json.

Literature verdict: PARTIAL-CLAIMED smooth bounded convex planar domains, for every nonzero real second Neumann eigenfunction, including multiplicity. REPORT.md uses the continuation verdict format and concerns the additional conditional multiplier implication proved here. Neither verdict certifies the full preprint.

## Recommended new “where it stands” sentence

> OpenAI's unrefereed preprint *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026) claims boundary-only maxima and minima for every second Neumann eigenfunction on smooth bounded simply connected planar domains, including multiple eigenvalues, and thus covers smooth convex domains. The sources checked do not settle the full strict statement for arbitrary bounded convex planar domains. Later papers give conditional non-strict extensions or strict boundary maximum modulus, leaving the two signed boundary-only extrema on general nonsmooth convex domains uncovered.

Three sentences. The historical special-case chronology supplied in the original row is not independently re-audited here.

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

## 4. Follow-ups opened in this round

The initial search took less than five minutes. Queries and actual URLs opened are recorded in LOG.md. No later full strict convex-planar solution or direct refutation was identified in the returned results; this is a bounded search finding, not a proof of absence. No SOLVED_ELSEWHERE.md is warranted.

- **Krzysztof Burdzy**, *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*, [arXiv:2610.12622v1, full HTML](https://arxiv.org/html/2610.12622v1), October 8, 2026; paper dated October 7. Opened author information, commentary, Theorem 2.1 and Corollary 2.2. The result is conditional on the smooth OpenAI input, requires compact Neumann resolvent and a simple first positive eigenvalue, and asserts non-strict boundary-layer extrema. It expressly permits the possibility of an interior point sharing a boundary extremal value. The commentary says the human author has not checked every detail; this is not referee certification of the OpenAI proof.

- **Rodrigo Bañuelos**, *Hot Spots: From Smooth to Nonsmooth Simply Connected Planar Domains*, [arXiv:2610.32920v1, full HTML](https://arxiv.org/html/2610.32920v1), October 23, 2026; paper dated October 20. Author spelling follows the full paper. Opened the author information, disclosure, Hypothesis 1.1, Theorem 1.2 and the discussion of the multiplicity obstruction. It assumes the smooth-domain result, finite area, compact Sobolev embedding and a simple first positive eigenvalue. Its boundary-layer and continuous-boundary conclusions are non-strict; a favorable limiting eigenfunction in a multiple eigenspace does not give each prescribed eigenfunction. The disclosure says the smooth input proof is not assessed.

- **Haiyun Deng, Xuyong Jiang, Xiaoping Yang**, *Near-boundary rigidity and strict maximum modulus for Neumann eigenfunctions on convex planar domains*, [arXiv:2610.18546v2, full HTML](https://arxiv.org/html/2610.18546v2), November 2, 2026. Opened the author information, abstract, Theorem 1.2, Corollary 1 and the following scope discussion. Theorem 1.2 claims strict boundary maximum modulus for every second Neumann eigenfunction on every bounded convex planar domain, allowing corners and multiplicity. Maximum modulus controls the larger absolute extremum; it need not exclude an interior signed extremum of smaller absolute size. The paper explicitly distinguishes these statements. Central symmetry supplies both signed extrema in its stated special case, but leaves the general row uncovered.

Search-result expositions and catalogues were leads only and are not used as independent proof validation. Earlier rounds record additional catalogue, exposition and issue searches; those are inherited records, not fresh checks here. The two unrelated preprints were reopened through their actual main TeX and introduction/paper; no relevant Neumann assertion appeared in their principal statements.

## 5. Lean artifacts opened in this round

Freshly opened and saved [scope document 369](https://github.com/openai/math/blob/main/lean/docs/369.md), [the challenge target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.lean) and [the supplied Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Analysis/HotSpots/Main.lean). Their source contents and blob identities match round 5.

The scope says smooth bounded simply connected planar domains, every nonzero first-positive eigenfunction, and multiplicity allowed. The actual target includes SmoothBoundary in AdmissibleDomain, defines the value by a mean-zero Rayleigh infimum, and asks for nonvanishing gradient and both strict inequalities. The challenge has a `sorry` placeholder; a separately supplied proof module is present. Main.lean contains a proof term and imports TraceRank and further modules. No compilation, dependency audit, axiom audit or comparator replay was run. These reads do not establish nonsmooth scope or certify the complete proof.

## 6. Earlier result rechecked independently

The round-5 boundary reciprocal-inertia result holds under its stated interior-kernel and subcritical bounded-density hypotheses. Section 1 of [PROOF.md](PROOF.md) rederives both radial normalizations, the smoothing constant H0=12^(1/3)*A/pi and the finite boundary-chain bounds. Compact-support radial resolvent limits and nonnegative cutoff limits give the same bordered matrix, with zero diagonal. The individual Poisson sections are never assumed to be in L2(q).

Rerun command: `OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/AV_T030/check_boundary_limits.py`.

PASS: 120 one-boundary and 75 two-boundary high-precision cases, four Poisson-square series/primitive comparisons, 20 exact bordered inertia checks and 140 distance/sign identities. Peak RSS 14,303,232 bytes; inherited priority 20; under one second.

## Spot check

The selected extension is the final bordered algebra and Hilbert-multiplier implication, ending at the pointwise eigenfunction gradient traces after eq:sum-energy. [PROOF.md](PROOF.md) proves:

1. The exact inertia formula for [B,ell;ell^T,0] is the inertia of B on ker(ell^T), plus one positive and one negative direction. This proves conditional negativity after the correct scaling x_i=K_i*a_i. A separate positive-plane proof checks the implication.
2. The anchored Gram construction gives an injective Lipschitz map into a separable real Hilbert space, with squared distance K(s)K(t)/N(s,t), and each coordinate is a legitimate Lipschitz multiplier.
3. Assuming the stated vector variational positivity/equality and boundary representation inputs, signed dominated convergence gives sum_j E(b_j*g)=|W_g(p)|^2/2. At a critical point, every nonnegative summand is zero. The nullspace input and continuity give the claimed pointwise eigenfunction gradient traces. A nonnegative-tail argument checks the same limit.

No defect was found in this selected implication. The proof keeps the vector variational principle and its equality case as explicit inputs; it does not prove a new class of hot-spots domains or certify the entire manuscript.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 check_hilbert_energy.py`.

PASS: 63 arbitrary bordered inertia identities, 28 anchored Gram checks, 49 conditional-negativity/barycenter identities, 15 multiplier-subtraction identities, 15 atomic diagonal corrections, 240 infinite-coordinate distance/tail checks, 96 signed Fourier cancellations and 25 nonzero-mean sums, all exact rational arithmetic. Peak RSS 15,073,280 bytes; priority 20; under one second. The script uses no PDE discretization.

The infinite Fourier embedding has squared Lipschitz bound 20/27, derived by two geometric-moment methods. Its signed test has a first coordinate-pair energy -3/80 and positive tail 3/80, despite zero total. This shows why variational positivity is essential to the separate-zero-energy deduction; the test is deliberately not an eigenfunction variational model. The nonzero-mean test sums to 1/2, checking the factor. A nonzero last diagonal breaks the bordered implication, and atomic quadrature requires a diagonal correction; both are excluded from the continuum argument as stated.

Next: check prop:vector and its equality case, including the tangent H1 decomposition and the curvature identity's sign and trace passage. The later multiplicity/boundary-uniqueness contradiction also remains outside the selected audit.

Only this folder was written. No git, subagents, external mutations, accounts, posting, GPU or heavy computation.
