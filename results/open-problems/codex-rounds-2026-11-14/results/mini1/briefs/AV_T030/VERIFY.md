# T030: Rauch's hot spots conjecture for convex planar domains

Checked 14 November 2026. The verdict concerns the exact row, including the word **only**, and records claims rather than certifying proofs.

## Conclusion and proposed row update

**PARTIAL-CLAIMED.** The relevant OpenAI preprint claims the strict conclusion for smooth convex planar domains and, more broadly, smooth simply connected planar domains. It does not state the result for arbitrary convex boundaries.

Recommended new “where it stands” text (three sentences):

> Known for several special classes, including all triangles; the full strict statement for arbitrary bounded convex planar domains is not established by the sources checked here. OpenAI's unrefereed preprint *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026) claims that every nonzero second Neumann eigenfunction on a smooth bounded simply connected planar domain has no interior critical point, including when the eigenvalue is multiple, and therefore covers smooth convex domains. Later sources give conditional non-strict extensions or strict boundary maximum modulus, which do not supply both boundary-only signed extrema for every nonsmooth convex planar domain.

The older special-case chronology in the supplied row was not separately audited. “Eigenfunction” is understood in the usual nonzero, real-valued sense.

## 1. The relevant candidate

OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, September 24, 2026. Opened the actual [main TeX]( https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/main.tex ) and [introduction]( https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/01-introduction.tex ). Local snapshots: [main](source-0-main.tex) and [introduction](source-0-introduction.tex).

The introduction assumes a nonempty bounded simply connected open set `Ω ⊂ R²` with `C∞` boundary, defines `μ=μ₁(Ω)` by the mean-zero Neumann Rayleigh quotient, and lets `V` be its real eigenspace. It explicitly says that its μ₁ counts only positive eigenvalues and equals μ₂ when the constant mode is counted first. In the literal source below, `\V` means that eigenspace and `\grad` means `\nabla`.

**Theorem 1.1, exact TeX:**

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

The exact domain and eigenvalue setup is retained in the local introduction snapshot so that the quotation is not read without its hypotheses.

### Comparison with our statement

Our statement: “For a bounded convex domain in R^2, every eigenfunction of the second Neumann eigenvalue of the Laplacian attains its maximum and minimum only on the boundary.”

| Phrase in our row | What the preprint actually claims | Match or gap |
| --- | --- | --- |
| “bounded … domain” | Nonempty bounded open connected domain | Same convention. |
| “convex” | Simply connected; no convexity assumption | Every planar convex domain is simply connected, so topology is compatible. The extra smoothness assumption still matters. |
| “in R²” | Ω ⊂ R² | Same dimension and Euclidean model. |
| No boundary regularity restriction | C∞ boundary | Genuine restriction: arbitrary convex domains, including polygons and other nonsmooth convex boundaries, are not in the stated theorem. |
| “every eigenfunction” | Every nonzero member of the real first-positive eigenspace, including multiplicity | Same universal quantifier; not merely a selected eigenfunction or a simple-eigenvalue case. |
| “second Neumann eigenvalue of the Laplacian” | First positive Neumann eigenvalue of −Δ, with constants omitted from numbering | Same spectral quantity; the index differs only by convention. |
| “maximum and minimum” | Both strict inequalities against boundary extrema | Same two signed extrema; not just maximum absolute value. |
| “only on the boundary” | Strict interior inequalities, and additionally ∇u ≠ 0 in the interior | At least the required strength on its domain class; also excludes saddle points. |
| Exact result for every domain | Exact pointwise conclusion | No asymptotic, approximate bound, or generic-domain qualifier. |

**Coverage:** the entire stated hot-spots conclusion for bounded convex planar domains with C∞ boundary. **Not covered by its statement:** the same conclusion on all nonsmooth convex planar domains. Being stronger in topology and in its conclusion does not remove its boundary regularity hypothesis. No passage to arbitrary convex boundaries is asserted in Theorem 1.1 or in its Lean target.

## 2. Optimal-transport candidate: NOT-THIS

OpenAI, *Global Support and Convex Injectivity Domains under Weak MTW*, September 25, 2026. Opened [main TeX](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/main.tex) and [introduction](https://github.com/openai/math/blob/main/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/sections/introduction.tex); exact snapshots are [main](source-1-main.tex) and [introduction](source-1-introduction.tex).

The model is a smooth connected compact Riemannian manifold (M,g) without boundary, dimension n ≥ 2, with cost c(x,y)=d(x,y)²/2. Here I(x) is the tangent injectivity domain of the exponential map. The assumption referenced as `eq:weak-mtw` is nonnegative Ma–Trudinger–Wang curvature on orthogonal pairs before cut:
`⟨ξ,η⟩ₓ=0 ⇒ S_(x,v)(ξ,η)≥0`, for x∈M, v∈I(x), ξ,η∈TₓM. The exact definitions are in the saved introduction.

**Theorem 1.1 (Convexity of injectivity domains), exact TeX:**

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

**Theorem 1.2 (Global support and intermediate geometry), exact TeX:**

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

The symbols in Theorem 1.2 are introduced in that same source: a potential is u(x)=max_y{−c(x,y)−v(y)}, with v its dual; Γᵤ is the ordinary semiconvex subgradient graph; Gₓ is the closed minimizing-velocity domain; Qₜ is squared-distance inf-convolution.

**Comparison:** this does not start with an arbitrary bounded convex subset of R², nor a Laplace eigenfunction. Even when n=2, M is a compact manifold without boundary, rather than our planar domain with Neumann boundary condition. The quantities are injectivity domains, cost supports and transport potentials, not the second Neumann eigenvalue or its eigenfunctions. The asserted convexity is a conclusion about tangent injectivity domains; it says nothing about locations of maxima or minima of Neumann eigenfunctions. It covers no part of T030 by its stated theorems.

## 3. Complex-geometry candidate: NOT-THIS

OpenAI, *Symmetry of semialgebraic bounded domains with compact quotient*, September 24, 2026. Opened the actual [paper TeX](https://github.com/openai/math/blob/main/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex); snapshot [source-2-main.tex](source-2-main.tex).

**Theorem 1.1, exact TeX:**

```tex
\begin{theorem}\label{thm:main}
Let \(U\) be a nonempty connected semialgebraic bounded open subset of a
complex affine variety. Suppose that a group \(\Gamma\) of
biholomorphisms acts properly discontinuously on \(U\) and that
\(U/\Gamma\) is compact. Then \(U\) is smooth and is biholomorphic to a
bounded symmetric domain.
\end{theorem}
```

The ambient affine variety is a reduced complex algebraic set embedded in Cᴺ, boundedness refers to that embedding, and “open” uses the complex-space topology. The source permits singular ambient varieties and finite stabilizers in the properly discontinuous action. “Smooth” here means that U is a complex manifold; it is not a conclusion that the boundary of a real convex domain is smooth.

**Comparison:** the theorem classifies complex domains with a semialgebraic description and a compact quotient by biholomorphisms. Its dimension is arbitrary complex dimension, its hypotheses impose neither our arbitrary convex planar domain class nor a Neumann spectral problem, and its conclusion is biholomorphic equivalence to a bounded symmetric domain. Even complex dimension one does not introduce the Euclidean Neumann Laplacian or its extrema. It covers no part of T030 by its stated theorem.

## 4. Follow-ups, comments and formalisation

### Hot-spots follow-ups actually opened

1. **Krzysztof Burdzy**, [*Removing Boundary Smoothness from the Hot-Spots Conclusion in the Simple-Eigenvalue Case*](https://arxiv.org/abs/2610.12622), arXiv:2610.12622, submitted October 8, 2026; manuscript dated October 7. Opened the abstract and [full HTML](https://arxiv.org/html/2610.12622v1), particularly Sections 1, 2 and 7. Theorem 2.1 assumes the OpenAI smooth-domain result as an external input, compact Neumann resolvent and a simple first positive eigenvalue. It obtains extremal values approached near the boundary; Corollary 2.2 gives equality of domain and boundary extrema when the eigenfunction extends continuously to the closure. The paper expressly leaves open whether an interior point shares an extremal value. Thus neither strictness nor arbitrary multiplicity is supplied. Burdzy states that he has not checked every detail of his ChatGPT-generated note and does not assess the OpenAI proof; this is not referee acceptance. His commentary also credits simultaneous work by Rodrigo Bañuelos.

2. **Haiyun Deng, Changfeng Gui, Xuyong Jiang, Xiaoping Yang, Ruofei Yao, Jun Zou**, [*Symmetry and critical points of second Neumann eigenfunctions on isosceles trapezoids and kites*](https://arxiv.org/abs/2604.19003), arXiv:2604.19003v4, revised October 11, 2026. Opened the abstract and [v4 full HTML](https://arxiv.org/html/2604.19003v4), including its closing Declaration. The authors explicitly distinguish their polygons from the smooth domains in OpenAI's theorem and explain that their methods differ. They claim no interior critical points for every real second eigenfunction in these two polygon classes. This is a special-case result and a scope comment, not a verification of the OpenAI proof or an extension to all convex domains.

3. **Haiyun Deng, Xuyong Jiang, Xiaoping Yang**, [*Near-boundary rigidity and strict maximum modulus for Neumann eigenfunctions on convex planar domains*](https://arxiv.org/abs/2610.18546), arXiv:2610.18546, submitted October 13, 2026, revised November 2, 2026 (v2). Opened the abstract and [v2 full HTML](https://arxiv.org/html/2610.18546v2), especially Theorem 1.2 and the scope discussion after Theorem 1.3. Theorem 1.2 states |u(x)| < max_(∂Ω)|u| in the interior for every second eigenfunction on an arbitrary bounded convex planar domain, without boundary smoothness or simplicity. This controls the larger absolute extremum, and does not by itself place the smaller signed extremum only on the boundary; the authors explicitly make this distinction. Their centrally symmetric corollary does give both signed extrema in that special class. They say their arguments do not rely on OpenAI or Burdzy.

4. A [community notes page](https://mathcommunity.github.io/oai-math-revised/papers/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/), opened as a discovery aid, lists a purported Jizhou Guo follow-up concerning non-strict extrema on arbitrary convex planar domains, allowing multiplicity. Its linked PDF and the repository README both returned 404, through web and connector attempts respectively. **The paper was not readable and is not used as mathematical evidence or included as a verified reference.** The community notes label their collected commentary unreviewed.

### Additional follow-up and exposition opened

- **Rodrigo Bañuelos**, [*Hot Spots: From Smooth to Nonsmooth Simply Connected Planar Domains*](https://arxiv.org/abs/2610.32920), arXiv:2610.32920, submitted October 23, 2026; manuscript dated October 20. The author name here follows the [paper HTML](https://arxiv.org/html/2610.32920), not the misspelled author metadata on its abstract page. Opened the abstract, full HTML, AI Disclosure, Theorem 1.2, Remark 1.3 and Section 6. Theorem 1.2 assumes the smooth-domain assertion, finite area, compact Sobolev embedding and a simple first positive eigenvalue. Remark 1.3 explicitly allows an interior point to share an extremal value. Section 6 asks about removing simplicity, even for bounded simply connected Lipschitz domains. The author reports checking the AI-assisted material but expressly does not assess OpenAI's proof. This supplies neither missing strictness nor arbitrary multiplicity.
- Opened the [Open Maths course page](https://openmaths.org/courses/strict-hot-spots-on-simply-connected-planar-domains/). It describes an exposition of OpenAI's smooth-domain argument and identifies itself as written and self-checked by Claude Opus 5.5, with independent review incomplete. It is an exposition, not independent certification.
- Opened community notes pages for [the MTW candidate](https://mathcommunity.github.io/oai-math-revised/papers/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/) and [the symmetry candidate](https://mathcommunity.github.io/oai-math-revised/papers/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/). They list formalisation and expository leads, but no direct error report or independent referee certification. Their automatically collected notes are explicitly unreviewed; their lists of older literature were not treated as newly verified references.


### Lean evidence actually opened

- OpenAI's [scope document 369](https://github.com/openai/math/blob/main/lean/docs/369.md) describes exactly the smooth-domain, every-eigenfunction claim.
- OpenAI's [HotSpots.lean target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.lean) defines Plane = EuclideanSpace ℝ (Fin 2), an admissible domain with smooth boundary, a weak first-positive Neumann eigenspace using the mean-zero Rayleigh infimum, and a conclusion combining nonzero interior gradient with strict boundary bounds. The universal quantifier and boundary regularity restriction are visible in the definitions.
- The target's `sorry` is a placeholder in a challenge statement. Opened the separate [proof module](https://github.com/openai/math/blob/main/lean/OAI/Analysis/HotSpots/Main.lean), its [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/HotSpots.json), and the [verification instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md). The proof module concludes the same named theorem through a closed-disk chart, Hilbert multipliers and a noncriticality theorem. Configuration permits propext, Quot.sound and Classical.choice.
- Opened the [community comparator log of October 26](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/HotSpots.log). It reports successful solution build and acceptance by Lean's default kernel. This is evidence of a reported run, not an independently replayed check here, and it does not add nonsmooth domains to the target.
- Opened [scope 360](https://github.com/openai/math/blob/main/lean/docs/360.md) for the MTW candidate and [scope 058](https://github.com/openai/math/blob/main/lean/docs/058.md) for the symmetry candidate. Both describe formalisation of their own unrelated geometry results. The MTW scope notes that its finite-target intermediate result does not cover the arbitrary-potential local-injectivity assertion.
- Opened the upstream [formalisation catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [repository README](https://github.com/openai/math/blob/main/README.md), and [history](https://github.com/openai/math/blob/main/history.md). They distinguish raw model output and verification stages. No withdrawal of these three candidates was listed in the opened history.

### Search scope and limits

Used the web search tool with the exact titles and combinations of “OpenAI”, “arxiv”, “error”, “refutation” and “proof”; also searched the row and the identified follow-up title. Read-only GitHub issue searches `repo:openai/math "hot spots"`, `repo:mathcommunity/oai-math-revised "hot spots"`, `repo:openai/math "Weak MTW"`, and `repo:openai/math "semialgebraic bounded"` each returned no issues.

No arXiv version of the three exact OpenAI titles, directly relevant refutation, error report or referee certification was found in the returned searches. This is a bounded search result, not proof that no such material exists. The current verdict is a comparison of the claims' scope, not a judgment of correctness.

## Spot check

**Selected lemma:** the bounded regularization of the disk Green kernel, labelled `lem:regularization` in [Section 5](https://github.com/openai/math/blob/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/build/sections/05-reciprocal-kernels.tex). The local snapshot is [source-0-05-reciprocal-kernels.tex](source-0-05-reciprocal-kernels.tex). This is the starting analytic input for the central reciprocal-kernel theorem: it must supply bounded kernels whose finite entrywise-reciprocal matrices have at most one positive eigenvalue. An error here would break the later resolvent construction.

The lemma states, verbatim:

> There are bounded continuous strictly positive kernels \(C_\epsilon\) on \(\mathbb D\times\mathbb D\), \(0<\epsilon\le1\), such that \(C_\epsilon\uparrow G\) as \(\epsilon\downarrow0\), including on the diagonal, and every finite matrix \((1/C_\epsilon(x_i,x_j))_{i,j}\) has (P).

Here (P) means at most one positive eigenvalue, counted with multiplicity. The following checks use the displayed calculations of this lemma, not a replacement proof of the hot-spots theorem.

1. **Green normalization and the one-positive-direction form.** With
   \(h(x,y)=|x-y|^2/[(1-|x|^2)(1-|y|^2)]\),
   Section 4 gives \(G=(4\pi)^{-1}\log(1+1/h)\), hence \(1/G=4\pi L(h)\), where \(L(h)=1/\log(1+1/h)\). Multiplication of \(h+1/2\) by the two positive disk factors gives exactly
   \[
   |x-y|^2+\tfrac12(1-|x|^2)(1-|y|^2)
   =\tfrac12(1+|x|^2)(1+|y|^2)-2x\cdot y.
   \]
   The sign and coefficient agree: a positive rank-one matrix minus a Gram matrix has at most one positive eigenvalue. Positive diagonal congruence preserves this count.

2. **The positive mixture for the correction.** Direct integration of
   \(h[(h+1)/h]^\alpha\) over \(0\le\alpha\le1\) gives \(L(h)\). For the probability density proportional to \(v^{\alpha-1}/(1+v)\) and \(r=1/(1+v)\), integration by parts gives \(\mathbb E_\alpha(1-r)=\alpha\); the endpoint term \(v^\alpha/(1+v)\) vanishes at both ends for \(0<\alpha<1\). Scaling the same integral gives
   \[
   h^{1-\alpha}(h+1)^\alpha
   =\mathbb E_\alpha\frac{h(h+1)}{h+r}.
   \]
   Polynomial division inside the expectation yields exactly
   \(h+(1-r)-r(1-r)/(h+r)\). Therefore the source's
   \(f(h)=h+1/2-L(h)=\int_0^1\mathbb E_\alpha[r(1-r)/(h+r)]\,d\alpha\)
   has the stated sign and \(f(0)=1/2\); also \(0\le f(h)\le1/2\). This checks the sign needed for subtraction below.

3. **Positive semidefiniteness, including the diagonal.** The source's
   \[
   k(x,y)=\frac1{1+h(x,y)}
   =\frac{(1-|x|^2)(1-|y|^2)}{|1-x\overline y|^2}
   \]
   is the product of a disk power-series Gram kernel with its conjugate and positive diagonal factors. For fixed \(0<r<1\), the geometric series
   \[
   \frac1{h+r}=\sum_{n\ge0}(1-r)^n k^{\,n+1}
   \]
   has the correct denominator and converges even at \(h=0\), since then \(k=1\) and \(1-r<1\). Schur powers preserve positive semidefiniteness; the positive mixture is finite because its diagonal is \(1/2\). Thus this part does give a positive semidefinite finite matrix for \(f(h(x_i,x_j))\), without omitting repeated points.

4. **Regularization bounds and limit.** The definition is
   \(1/C_\epsilon=4\pi[(h+1/2)-(1-\epsilon)f]=4\pi[L+\epsilon f]\).
   Subtracting the positive semidefinite matrix \((1-\epsilon)f\) cannot increase the number of positive directions. Independently,
   \(L+\epsilon f=\epsilon(h+1/2)+(1-\epsilon)L\ge\epsilon/2\).
   Consequently \(0<C_\epsilon\le1/(2\pi\epsilon)\), and on the diagonal equality holds. The sign of \(f\) makes \(C_\epsilon\) increase as \(\epsilon\) decreases; away from the diagonal its limit is the displayed Green function, while its diagonal diverges. The normalization and both limiting cases agree.

**Finding:** no algebraic defect was found in this regularization lemma in the checks above. This does not assess the correctness of the preprint's complete proof: the later quadrature/resolvent limits, boundary passage, vector variational principle and multiplicity argument have not been certified by this spot check. The scope gap in REPORT.md is independent of these calculations.


Task: “Verify: has open problem T030 been settled by the OpenAI math release?” — 14 November 2026, 20:58 Asia/Tbilisi.

