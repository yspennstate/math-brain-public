# T030 verification and round-4 continuation

Checked 15 November 2026. Both earlier REPORT.md and LOG.md files were read, together with the first audit’s VERIFY.md and saved sources and round 3’s VERIFY.md, PROOF.md, and audit_resolvent.py. The first folder has no PROOF.md or scripts. All new writes stay in this folder.

VERDICT: PARTIAL-CLAIMED smooth bounded convex planar domains, including every nonzero real second Neumann eigenfunction and multiple eigenvalues.

This is the literature verdict for the exact row. REPORT.md uses the continuation task’s requested verdict format and reports the additional singular interior-kernel result. The complete OpenAI proof is not certified here.

## Recommended row update

> OpenAI's unrefereed preprint *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026) claims the strict conclusion for every second Neumann eigenfunction on smooth bounded simply connected planar domains, including multiple eigenvalues, and thus covers smooth convex planar domains. The sources checked do not settle the full strict statement for arbitrary bounded convex planar domains. Later papers give conditional non-strict extensions or strict boundary maximum modulus, leaving a gap for both boundary-only signed extrema on general nonsmooth convex domains.

This is three sentences. Eigenfunctions are nonzero and real-valued.

## Relevant candidate

OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/01-introduction.tex) and [reciprocal-kernel section](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/05-reciprocal-kernels.tex). Current snapshots are source-introduction.tex and source-reciprocal-kernels.tex. The actual upstream main TeX was also reopened and gives author OpenAI and the date above.

The setup assumes a nonempty bounded simply connected open set \(\Omega\subset\mathbb R^2\) with \(C^\infty\) boundary. Its \(\mu_1\) is the first positive Neumann eigenvalue, defined by the mean-zero Rayleigh quotient; \(\V\) denotes its real eigenspace. The introduction explicitly identifies this eigenvalue with \(\mu_2\) when the constant mode is counted first.

Theorem 1.1, exact TeX:

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

| Our words | Preprint | Match or gap |
|---|---|---|
| bounded domain | Nonempty bounded open connected domain | Same convention. |
| convex | Simply connected | All convex planar domains satisfy this topology assumption. |
| in R² | In R² | Same Euclidean dimension and Laplacian. |
| No smoothness restriction | C-infinity boundary | Extra restriction; arbitrary convex corners and other nonsmooth boundaries are excluded. |
| every eigenfunction | Every nonzero member of the real first-positive eigenspace | Same quantifier, including multiplicity. |
| second Neumann eigenvalue | First positive, constants not counted | Same eigenvalue, different numbering. |
| maximum and minimum | Both strict signed inequalities | Both requested extrema, not maximum modulus alone. |
| only on the boundary | Strict interior inequalities plus nonzero gradient | At least the requested strength on its domain class. |
| Exact assertion for each domain | Exact assertion for each smooth simply connected domain | No asymptotic or generic qualifier. |

It claims the whole row for smooth convex domains. It does not state the arbitrary-convex-boundary result. Approximation would require preserving every eigenfunction and strictness; strict inequalities need not survive limits.

## Optimal-transport candidate: NOT-THIS

OpenAI, *Global Support and Convex Injectivity Domains under Weak MTW*, September 25, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/sections/introduction.tex), saved as source-mtw-introduction.tex. Also reopened the actual upstream build/main.tex for the author and date; an attempted build/paper.tex path failed because that is not its entry point.

The model is a smooth connected compact Riemannian manifold \((M,g)\) without boundary, dimension \(n\ge2\), cost \(c(x,y)=d(x,y)^2/2\). Here \(I(x)\) is the tangent injectivity domain; the referenced equation assumes nonnegative MTW curvature on orthogonal pairs before cut.

Theorem 1.1, exact TeX:

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

This concerns convexity of exponential-map injectivity domains on manifolds. It assumes neither an arbitrary bounded convex Euclidean planar domain nor a Neumann eigenfunction, and concludes nothing about either signed extremum. Even at \(n=2\), its compact boundaryless manifold is a different model. The additional global-support theorem in the saved introduction concerns cost potentials and their supports, also unrelated to T030. It covers no part of our row.


Theorem 1.2 is also a principal result. Its symbols refer to the same squared-distance cost, the closed minimizing domain G_x, and cost potentials u with dual v; it supplies no Neumann spectral conclusion. Exact TeX:

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

## Complex-geometry candidate: NOT-THIS

OpenAI, *Symmetry of semialgebraic bounded domains with compact quotient*, September 24, 2026. Opened the actual [paper TeX](https://github.com/openai/math/blob/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex), saved as source-symmetry.tex.

Theorem 1.1, exact TeX:

```tex
\begin{theorem}\label{thm:main}
Let \(U\) be a nonempty connected semialgebraic bounded open subset of a
complex affine variety. Suppose that a group \(\Gamma\) of
biholomorphisms acts properly discontinuously on \(U\) and that
\(U/\Gamma\) is compact. Then \(U\) is smooth and is biholomorphic to a
bounded symmetric domain.
\end{theorem}
```

This classifies complex domains under semialgebraicity and compact-quotient assumptions. Its ambient complex dimension is arbitrary; it has no Neumann spectral quantity and no statement about maxima or minima. Smoothness here concerns the complex space \(U\), not regularity of a real planar boundary. Even complex dimension one supplies no Euclidean Neumann assertion. It covers no part of our row.

## Follow-ups opened in this continuation

The initial update search took less than five minutes. Web searches used the exact title with error/correction/November 2026 terms, “hot spots conjecture 2026 November convex proof”, and “hot spots 2611 convex”. Later searches used the two unrelated titles with error/arxiv terms. No later full strict convex-planar resolution or direct refutation was found in the returned results. This is a bounded search finding, not proof that none exists.

- **Krzysztof Burdzy**, *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*, [arXiv:2610.12622](https://arxiv.org/abs/2610.12622), submitted October 8, 2026; paper dated October 7. Opened [full HTML](https://arxiv.org/html/2610.12622v1), especially the human commentary and Theorem 2.1/Corollary 2.2. It takes OpenAI's smooth result as an unassessed external input, assumes compact Neumann resolvent and a simple first-positive eigenvalue, and gives a non-strict boundary-layer conclusion. It explicitly does not exclude an interior point sharing an extremal value. The ChatGPT-generated note is not referee verification of OpenAI.

- **Rodrigo Bañuelos**, *Hot Spots: From Smooth to Nonsmooth Simply Connected Planar Domains*, [arXiv:2610.32920](https://arxiv.org/abs/2610.32920), submitted October 23, 2026. Opened [full HTML](https://arxiv.org/html/2610.32920v1), especially Theorem 1.2 and Section 6. The author name follows the paper rather than its misspelled abstract metadata. The main extension is conditional, non-strict and assumes simplicity, finite area and compact Sobolev embedding. Section 6 explains that convergence of a spectral cluster need not approximate each prescribed eigenfunction by first-positive eigenfunctions when the eigenvalue splits. Proposition 6.1 obtains at least one favorable limiting eigenfunction without simplicity; it supplies neither every eigenfunction nor strictness.

- **Haiyun Deng, Xuyong Jiang, Xiaoping Yang**, *Near-boundary rigidity and strict maximum modulus for Neumann eigenfunctions on convex planar domains*, [arXiv:2610.18546](https://arxiv.org/abs/2610.18546), submitted October 13, 2026; v2 revised November 2. Opened [v2 full HTML](https://arxiv.org/html/2610.18546v2), including Theorem 1.2 and the surrounding scope discussion. It claims \(|u(x)|<\max_{\partial\Omega}|u|\) for second eigenfunctions on arbitrary bounded convex planar domains, allowing multiplicity. It expressly distinguishes this from controlling the smaller signed extremum. The centrally symmetric special case gives both extrema, but does not cover all convex domains. The paper says its arguments are independent of OpenAI and Burdzy.

The earlier VERIFY.md records further opened polygonal special-case literature and expositions, an inaccessible Guo lead excluded from evidence, issue searches with no relevant result, and a published comparator log reporting acceptance. Those inherited records were read; their additional web pages and comparator log were not all reopened here and are not new verification in this continuation. No inaccessible lead is used as a solution.

## Lean artifacts reopened

Opened the [scope document 369](https://github.com/openai/math/blob/main/lean/docs/369.md), saved as source-lean-scope.md, and the actual [HotSpots target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.lean), saved as source-lean-target.lean. The target defines the plane as \(\mathbb R^2\), includes SmoothBoundary in AdmissibleDomain, uses the mean-zero Rayleigh infimum, and asks for nonvanishing gradient and both strict signed inequalities for each nonzero eigenfunction.

The target ends in a sorry placeholder as a challenge statement. Also opened the actual supplied [proof module](https://github.com/openai/math/blob/main/lean/OAI/Analysis/HotSpots/Main.lean), saved as source-lean-main.lean; it contains a noncritical theorem and imports further modules. The earlier worker separately opened a published accepted comparator run, which was not reopened here. No Lean build, dependency/axiom audit, or comparator replay was made here. These artifacts do not add nonsmooth domains.

Opened the unrelated candidates' scope documents [360](https://github.com/openai/math/blob/main/lean/docs/360.md) and [058](https://github.com/openai/math/blob/main/lean/docs/058.md), saved as source-lean-mtw.md and source-lean-symmetry.md. The MTW scope distinguishes finite-target intermediate estimates from the manuscript's arbitrary-potential local-injectivity assertion. The symmetry scope concerns bounded semialgebraic complex domains. Neither concerns the hot-spots row.

Also opened the [follow-up index “In the wake of AI papers”](https://kimballmartin.github.io/ai-wake/) as a discovery aid. The actual follow-up papers above were opened independently. Read-only GitHub issue search `repo:openai/math "hot spots"` returned no issues. Exact-title searches for the two unrelated candidates with error/arxiv terms located repository/catalogue pages but no relevant replacement or refutation in the returned results. No unopen paper or search snippet is used as settlement evidence.

## Recheck of the earlier result

The earlier scope comparison holds under fresh upstream source reads: the smoothness restriction, full real-eigenspace quantifier, and first-positive eigenvalue convention are unchanged. The hot-spots introduction and reciprocal-kernel source SHAs agree with the earlier snapshots.

The earlier bounded-resolvent result also holds. Section 1 of [PROOF.md](PROOF.md) rederives the finite update from an explicit triangular block factorization and obtains the strictly positive denominator both as a Schur complement and as a determinant ratio. A separate three-term expansion checks the earlier quadrature error estimate.

Re-ran without writing in the earlier folder:

`OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/AV_T030/audit_resolvent.py`

All 34 exact-rational elimination orders and 18 perturbation checks passed again, including zero weights, coincident nodes, and coincident evaluation points. Peak RSS was 14,761,984 bytes; inherited priority was 20. LOG.md records the results.

## Spot check

The chosen extension is the earlier report's next step: the epsilon-to-zero passage in `prop:interior-reciprocal`. It is now proved in [PROOF.md](PROOF.md), with a source/operator-norm argument independent of the manuscript's chain-limit argument.

For a measure with density bounded by A, the explicit disk formula gives the uniform bounds

\[
 \sup_x\int_{\mathbb D}G(x,y)^2dy\le\frac1{2\pi},\qquad
 \sup_x\int_{\mathbb D}G(x,y)^4dy\le\frac3{8\pi^3}.
\]

Polar integration and level sets give these constants independently. Every interior Green section belongs to L2(rho), including when the evaluation point lies in the integration support. With m=rho(D) and H=sqrt(3A/(2*pi)), the new quantitative estimates are

\[
 \sup_x\|G(x,\cdot)-C_\epsilon(x,\cdot)\|_{L^2(\rho)}
 \le H\epsilon,\qquad
 \|T_\rho-T_\epsilon\|\le H\sqrt m\,\epsilon.
\]

Both inverse resolvents remain bounded by 1/(1-d), using the preprint's strict contraction. This proves convergence of the finite correction at every interior pair, including its diagonal. The direct diagonal is C_epsilon(x,x)=1/(2*pi*epsilon), so the reciprocal full diagonal is bounded by 2*pi*epsilon and tends to zero. Off-diagonal reciprocals converge to those of the singular resolvent; fixed-size matrix limits preserve (P). The nonnegative chain expansion identifies the same limit a second way.

Created [check_singular_limit.py](check_singular_limit.py), run as

`OMP_NUM_THREADS=1 nice -n 15 python3 check_singular_limit.py`

It checks the moment constants by two exact-rational recurrences, 28 high-precision off-diagonal regularization cases, four diagonal cases, and 18 exact scalar correction estimates. All passed in under one second, peak RSS 14,155,776 bytes, priority 20. These arithmetic checks supplement the written proof; they are not PDE discretization evidence or formal certification.

Attempts to break the result identify material restrictions. An atom at an evaluation point makes the logarithmic Green section fail to lie in L2(rho), but such measures are excluded by the bounded-density assumption. At d=1, the inverse can be singular. The direct kernels do not converge uniformly across the infinite diagonal; the proof treats diagonal reciprocals separately.

No error was found in this checked passage. The boundary radial limit, removal of compact support, boundary-kernel estimates, vector variational principle, and eigenfunction argument remain unchecked here. This result adds no boundary class to the preprint's hot-spots claim.

**Next checkable step:** audit `lem:bordered`: take the radial boundary limit at fixed compact support, then remove that support. Check the constants in both radial Green limits and the finiteness of the full boundary kernels without treating individual Poisson kernels as L2(q) functions.

## Source snapshots

All snapshots are in this folder. Read-only GitHub tools were used; no git commands.

| Snapshot | Upstream blob SHA |
|---|---|
| source-introduction.tex | ca7f7f292379a95899f04a1de411eb610d1fe9ab |
| source-boundary-kernels.tex | 31fde0ba6a572f90d0003a7aa91dc96ee9dfdf5e |
| source-reciprocal-kernels.tex | bcb125482dbfe6874ffe4582625c01ea66571ca9 |
| source-mtw-introduction.tex | a17608323207e26c589bb4ed1f7b62f561d02dcd |
| source-symmetry.tex | 75578580f59258c45f53aafb6b8345ca2e354f11 |
| source-lean-scope.md | 303e026dc76b6d793b2b441e8bbc2ad3d88f0af7 |
| source-lean-target.lean | 9e8c905519d515e23be329f1e4a544618a9d2397 |
| source-lean-main.lean | 3a4d4d6f29c7a9de7065b17f01d741df3904a1d6 |

Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, about 04:14 Asia/Tbilisi.

