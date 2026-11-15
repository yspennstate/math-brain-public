# T030 verification and continuation

Checked 15 November 2026. The earlier REPORT.md, LOG.md and VERIFY.md were read in the supplied read-only folder. It has no PROOF.md or scripts.

The literature verdict remains **PARTIAL-CLAIMED** for the exact row. This continuation verifies the next bounded-kernel resolvent step; it does not certify the preprint's complete proof.

## Recommended row update

> OpenAI's unrefereed preprint *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026) claims the strict conclusion for every second Neumann eigenfunction on smooth bounded simply connected planar domains, including multiple eigenvalues, and thus covers smooth convex planar domains. The sources checked do not settle the full strict statement for arbitrary bounded convex planar domains. Later papers give conditional non-strict extensions or strict boundary maximum modulus, leaving a gap for both boundary-only signed extrema on general nonsmooth convex domains.

This is three sentences. Eigenfunctions are nonzero and real-valued.

## Relevant candidate

OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, September 24, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/01-introduction.tex) and [reciprocal-kernel section](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/05-reciprocal-kernels.tex). Current snapshots are source-introduction-current.tex and source-reciprocal-current.tex. The earlier worker's main TeX was read locally and gives author OpenAI and the date above.

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

OpenAI, *Global Support and Convex Injectivity Domains under Weak MTW*, September 25, 2026. Opened the actual [introduction](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/sections/introduction.tex), saved as source-mtw-introduction-current.tex. Read the earlier worker's main TeX locally.

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

## Complex-geometry candidate: NOT-THIS

OpenAI, *Symmetry of semialgebraic bounded domains with compact quotient*, September 24, 2026. Opened the actual [paper TeX](https://github.com/openai/math/blob/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex), saved as source-symmetry-current.tex.

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

The update search took less than five minutes. Web searches used the exact title, error/refutation/correction terms, “hot spots conjecture 2026 proof convex”, “hot spots November 2026 convex proof”, and “hot spots 2611 convex”. No later full strict convex-planar resolution or direct refutation was found in the returned results. This is a bounded search finding, not proof that none exists.

- **Krzysztof Burdzy**, *Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*, [arXiv:2610.12622](https://arxiv.org/abs/2610.12622), submitted October 8, 2026; paper dated October 7. Opened the abstract and [full HTML](https://arxiv.org/html/2610.12622), especially the human commentary and Theorem 2.1/Corollary 2.2. It takes OpenAI's smooth result as an unassessed external input, assumes compact Neumann resolvent and a simple first-positive eigenvalue, and gives a non-strict boundary-layer conclusion. It explicitly does not exclude an interior point sharing an extremal value. The ChatGPT-generated note is not referee verification of OpenAI.

- **Rodrigo Bañuelos**, *Hot Spots: From Smooth to Nonsmooth Simply Connected Planar Domains*, [arXiv:2610.32920](https://arxiv.org/abs/2610.32920), submitted October 23, 2026. Opened the abstract and [full HTML](https://arxiv.org/html/2610.32920), especially Theorem 1.2 and Section 6. The author name follows the paper rather than its misspelled abstract metadata. The main extension is conditional, non-strict and assumes simplicity, finite area and compact Sobolev embedding. Section 6 explains that convergence of a spectral cluster need not approximate each prescribed eigenfunction by first-positive eigenfunctions when the eigenvalue splits. Proposition 6.1 obtains at least one favorable limiting eigenfunction without simplicity; it supplies neither every eigenfunction nor strictness.

- **Haiyun Deng, Xuyong Jiang, Xiaoping Yang**, *Near-boundary rigidity and strict maximum modulus for Neumann eigenfunctions on convex planar domains*, [arXiv:2610.18546](https://arxiv.org/abs/2610.18546), submitted October 13, 2026; v2 revised November 2. Opened the abstract and [v2 full HTML](https://arxiv.org/html/2610.18546v2), including Theorem 1.2 and the surrounding scope discussion. It claims \(|u(x)|<\max_{\partial\Omega}|u|\) for second eigenfunctions on arbitrary bounded convex planar domains, allowing multiplicity. It expressly distinguishes this from controlling the smaller signed extremum. The centrally symmetric special case gives both extrema, but does not cover all convex domains. The paper says its arguments are independent of OpenAI and Burdzy.

The earlier VERIFY.md records further opened polygonal special-case literature and expositions, an inaccessible Guo lead excluded from evidence, issue searches with no relevant result, and a published comparator log reporting acceptance. Those inherited records were read; their additional web pages and comparator log were not all reopened here and are not new verification in this continuation. No inaccessible lead is used as a solution.

## Lean artifacts reopened

Opened the [scope document 369](https://github.com/openai/math/blob/main/lean/docs/369.md), saved as source-lean-scope-current.md, and the actual [HotSpots target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.lean), saved as source-lean-target-current.lean. The target defines the plane as \(\mathbb R^2\), includes SmoothBoundary in AdmissibleDomain, uses the mean-zero Rayleigh infimum, and asks for nonvanishing gradient and both strict signed inequalities for each nonzero eigenfunction.

The target ends in a sorry placeholder as a challenge statement. The earlier worker separately opened the supplied solution module and a published accepted comparator run. No new Lean build or comparator replay was made here. Neither the target nor the inherited reported acceptance adds nonsmooth domains.

## Spot check

The earlier regularization algebra survives an independent derivation. Its correction has the explicit positive Stieltjes representation
\[
 f(h)=\int_0^1\frac{dr}
 {(h+r)\{\log^2((1-r)/r)+\pi^2\}},\qquad f(0)=\frac12.
\]
The diagonal normalization was independently integrated after substituting \(r=(1+e^t)^{-1}\). The Lorentz identity, Schur-power positivity and regularization bound agree with the earlier result.

The **new check** is the next bounded positive-kernel resolvent step. [PROOF.md](PROOF.md) supplies a finite Schur-complement derivation and passage from positive quadrature to a continuous compact-support kernel. Each elimination denominator is both
\[
 1-w_zH^A_{zz}>0
 \quad\hbox{and}\quad
 \det Q_{A\cup\{z\}}/\det Q_A.
\]
This independently verifies the node-update mechanism. Equations (10)–(11) of PROOF.md give an explicit error bound for quadrature resolvent evaluations and their entrywise reciprocals.

[audit_resolvent.py](audit_resolvent.py) passed all 34 exact-rational elimination orders across five fixtures. It compares direct full inverses, successive updates, determinant ratios and reciprocal inertia. Zero weights, duplicate nodes, repeated evaluation points and evaluation at integration nodes are included. Eighteen exact scalar cases attain equality in the perturbation bound, independently checking its constants.

Command: OMP_NUM_THREADS=1 nice -n 15 python3 audit_resolvent.py

Runtime was under one second, peak RSS 14,811,136 bytes, inherited priority 20. Full output is in LOG.md.

An attempted negative-coefficient extension fails: a \(3\times3\) example keeps all kernel entries positive but changes reciprocal inertia from \((1,1,1)\) to \((2,1,0)\). A one-node example becomes singular at the critical weight. These failures confirm the material hypotheses; they are not errors in the preprint, which requires nonnegative weights and a strict spectral margin.

**Limit:** this verifies the bounded continuous compact-support resolvent step. It does not verify the subsequent singular Green limit, radial boundary passage, cutoff removal, vector variational principle or multiplicity argument. It adds no new domain class to the hot-spots claim.

**Next checkable step:** audit the epsilon-to-zero passage in the proposition labelled prop:interior-reciprocal, retaining the logarithmic diagonal and independently proving the off-diagonal \(L^2(\rho)\) source bound. Then examine the radial boundary and cutoff limits.

Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, about 00:50 Asia/Tbilisi.

