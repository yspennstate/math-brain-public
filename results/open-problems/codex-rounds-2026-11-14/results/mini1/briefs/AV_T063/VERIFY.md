# T063: Gaussian free field limit of the six-vertex height function

Checked 14 November 2026. **SOLVED-CLAIMED** for the balanced zero-slope plane state: the September 23 six-vertex manuscript claims the entire parameter interval in our row and an explicit variance multiplier. This classification records the theorem claimed; it does not certify its proof or establish community acceptance. The row does not specify a Gibbs state; it should specify the balanced plane state when citing this claim.

## 1. Balanced six-vertex manuscript

Author as printed: **OpenAI**. Title: *The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)*. Date: **September 23, 2026**.

Opened the manuscript's actual LaTeX entry point `build/main.tex` and introduction, rather than relying on its title or abstract. [Theorem 1.1 source](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/build/sections/01-introduction.tex); local exact source: [sources/candidate1/introduction.tex](sources/candidate1/introduction.tex).

The main theorem is copied verbatim below, including the source's labels and references:

```latex
\begin{theorem}\label{thm:main}
For every fixed \(c\in(0,2]\), the prescribed iterated balanced-torus limit
\(\P_c\) exists. Define
\begin{equation}\label{eq:multiplier}
 \Delta=1-\frac{c^2}{2},\qquad
 \sigma(c)^2=\frac2{\arccos\Delta}=\frac1{\arcsin(c/2)}.
\end{equation}
As \(\delta\downarrow0\) through arbitrary positive real values,
the fields \(h_\delta\) converge to
\(\sigma(c)\Gamma\) in each of the following senses.
\begin{enumerate}
\item For every finite family \(\mu_1,\ldots,\mu_m\) of compactly supported
finite signed measures of total mass zero and finite energy,
\[
 \bigl(\langle h_\delta,\mu_j\rangle\bigr)_{j=1}^m
 \ \Longrightarrow\
 \mathcal N\!\left(0,
       \bigl(\sigma(c)^2\mathcal E(\mu_i,\mu_j)\bigr)_{i,j=1}^m\right).
\]
\item For every bounded open \(U\subset\R^2\) and \(-1<\alpha<0\),
there is convergence in law, with tightness, in the ordinary restriction
spaces
\[
 \mathcal C^\alpha_{\mathrm{res}}(U):=B^\alpha_{\infty,\infty}(U),
 \qquad B^\alpha_{p,q}(U),\qquad W^{\alpha,p}(U),
 \quad 1\le p<\infty,\quad 1\le q\le\infty,
\]
modulo constants. Convergence also holds in the outward completion
\eqref{eq:source-holder} defined below. No regularity of
\(\partial U\) is required. One may fix a smooth compactly supported
\(\rho\) of integral one and replace each field \(X\) by
\(X-\langle X,\rho\rangle\), using the same pinning for the limit.
\item For every \(k\ge1\) and every tuple
\((u_i,u_i')_{i=1}^k\) with
\(\{u_i,u_i'\}\cap\{u_j,u_j'\}=\varnothing\) for \(i\ne j\),
\begin{equation}\label{eq:increment-main}
 \E_c\prod_{i=1}^k
    \bigl(h_\delta(u_i')-h_\delta(u_i)\bigr)
 \longrightarrow
 \sigma(c)^k\sum_{\pi}\prod_{\{i,j\}\in\pi}C_{ij},
\end{equation}
where the sum is over pairings of \(\{1,\ldots,k\}\), is zero for odd \(k\),
and
\[
 C_{ij}=G(u_i',u_j')-G(u_i',u_j)-G(u_i,u_j')+G(u_i,u_j).
\]
The convergence is uniform on compact sets of such tuples.
\end{enumerate}
\end{theorem}
```

The definitions immediately before the theorem matter. The graph is the square lattice, with a=b=1 and the two c-type vertices weighted c. Heights live on faces, with unit jumps and the face to the left of an arrow higher. The plane law P_c is the local weak limit of M-by-L tori conditioned to have L/2 left and L/2 right horizontal arrows in every vertical column, taking M to infinity first and even L to infinity second. The rescaled field is h_delta(x)=h(x/delta), with the stated floor convention. Gamma is the plane GFF modulo constants with Green kernel -(2 pi)^(-1) log|x-y|; finite energy requires absolute integrability of the logarithmic singularity against the total variation measures.

### Comparison with our statement

| Words in T063 | What this theorem claims | Coverage |
|---|---|---|
| “six-vertex model on Z^2” | Square-lattice six-vertex arrows and their face height | Same model and dimension |
| “weights a=b=1” | Four local configurations weighted one; two weighted c | Same weights |
| “c in (0,2)” | Every fixed c in (0,2], hence every Delta in [-1,1) | Entire requested open interval; adds c=2 (Delta=-1) |
| “Delta=1-c²/2 in (-1,1)” | Exactly the same definition; no perturbative restriction | Entire requested Delta range |
| “height function” | Unit face-height jumps in the prescribed balanced zero-slope plane law | Same observable, with an essential state and normalization specification absent from our wording |
| “converges in the scaling limit to a Gaussian free field” | Joint Gaussian test laws, distribution-space convergence with tightness, and separated-increment moment asymptotics | Full GFF convergence claimed, stronger than merely logarithmic variance or a covariance bound |
| “variance is an explicit function of Delta” | Squared field multiplier sigma²=2/arccos(Delta)=1/arcsin(c/2) | Explicit covariance factor in the printed height/Green convention |

The amplitude is sigma, the square root of the displayed factor. “Variance” here means covariance normalization of the limiting distribution, not a finite pointwise GFF variance. Multiplying the microscopic height by a constant multiplies the covariance factor by its square.

Not covered: arbitrary slopes or arbitrary Gibbs states, different orders or shapes of thermodynamic limits, general anisotropic weights a!=b, c>2, c=0, uniform estimates as c tends to zero, or a direct bounded-domain theorem with arbitrary boundary data. These are not requirements of the stated plane T063 row once its equilibrium state is made explicit. If the row was intended to quantify over every Gibbs state, this manuscript does not claim that stronger statement.

The parameter conversion can be checked without a literature assumption: for theta=arcsin(c/2) in (0,pi/2], cos(2 theta)=1-c²/2=Delta, hence arccos(Delta)=2 theta. At the free-fermion point c=sqrt(2), Delta=0, sigma²=4/pi; at c=2, sigma²=2/pi. These are squared multipliers, not amplitudes.

## 2. Weighted integer Lipschitz manuscript, October 6

Author as printed: **OpenAI**. Title: *Gaussian free-field limits of weighted integer Lipschitz heights*. Date: **October 6, 2026**. [Theorem 1.1 source](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/build/sections/01-introduction.tex); [local source](sources/candidate2/introduction.tex).

Its main theorem, verbatim:

```latex
\begin{theorem}\label{thm:main}
For every fixed $x\in[1/\sqrt2,1]$ there exists
$\sigma(x)\in(0,\infty)$, independent of $D$ and of the inside approximation
in Definition~\ref{def:approximation}, such that
\[
 \frac{h_\delta}{\sigma(x)}\ \Longrightarrow\ \Phi_D
 \qquad\text{in }\mathcal D'(D).
\]
In particular, the fields are tight as random distributions and, for every
$k\ge1$ and $f_1,\ldots,f_k\in C_c^\infty(D)$, the vector
$(h_\delta(f_i)/\sigma(x))_{i=1}^k$ converges to
$(\Phi_D(f_i))_{i=1}^k$.  All mixed moments of these vectors converge.
\end{theorem}
```

The preceding definitions specify integer heights on the triangular lattice (face centers of the hexagonal lattice), adjacent differences of absolute value at most one, zero height on the boundary layer, and probability proportional to x^N, where N counts unequal neighboring heights. D is a bounded simply connected domain with C² Jordan boundary; approximating cycles lie inside D, exhaust its compact subsets, and have boundary parametrizations converging uniformly. Heights are paired using Euclidean area. Phi_D is the zero-Dirichlet GFF with covariance (-Delta_D)^(-1).

This is **NOT-THIS** for T063. It has the same ambient dimension and the same kind of limiting random field, but a different lattice and microscopic model: neighboring differences may be zero, and the contours give a hexagonal loop O(2) law. The parameter is x in [1/sqrt(2),1], not c or Delta, and no identification with the square-lattice six-vertex weights is proved by this theorem. Its boundary condition is fixed zero in a bounded domain; its normalization is an unspecified positive sigma(x), explicitly stated in the introduction to have no formula here. Thus it supplies neither a six-vertex subinterval result nor the explicit Delta-dependent variance requested in T063.

The [October 6 README](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/README.md) calls this a revision supplying the annulus proof of the circuit estimate used in the discrete argument and links the September 25 version.

## 3. Weighted integer Lipschitz manuscript, September 25

Author as printed: **OpenAI**. Same title, *Gaussian free-field limits of weighted integer Lipschitz heights*. Date: **September 25, 2026**. [Theorem 1.1 source](https://github.com/openai/math/blob/main/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-September-25-2026/build/sections/01-introduction.tex); [local source](sources/candidate3/introduction.tex).

Its main theorem, independently opened and copied verbatim:

```latex
\begin{theorem}\label{thm:main}
For every fixed $x\in[1/\sqrt2,1]$ there exists
$\sigma(x)\in(0,\infty)$, independent of $D$ and of the inside approximation
in Definition~\ref{def:approximation}, such that
\[
 \frac{h_\delta}{\sigma(x)}\ \Longrightarrow\ \Phi_D
 \qquad\text{in }\mathcal D'(D).
\]
In particular, the fields are tight as random distributions and, for every
$k\ge1$ and $f_1,\ldots,f_k\in C_c^\infty(D)$, the vector
$(h_\delta(f_i)/\sigma(x))_{i=1}^k$ converges to
$(\Phi_D(f_i))_{i=1}^k$.  All mixed moments of these vectors converge.
\end{theorem}
```

The theorem blocks in the two versions are byte-identical. The model, domain conditions, parameter interval, implicit normalization, and comparison with T063 are the same. Verdict for this candidate: **NOT-THIS**. The October version adds an annulus appendix to support the circuit estimate; it is not a second independent claimed solution of T063.

## Follow-ups and verification status

The following were actually opened, not inferred from search snippets:

1. [OpenAI repository README](https://github.com/openai/math/blob/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), and all three manuscript READMEs. The repository describes its manuscripts as model outputs with differing verification status. The history records October 7 repairs to four Lipschitz/Ashkin–Teller manuscripts; the weighted-height README gives the specific annulus-proof revision. No six-vertex withdrawal or correction was found in these notices.
2. [Yan Ru Pei, *Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*, November 2026](https://hexagonmath.org/pdf/2611.00291v1), a 33-page Hexagon PDF (its number is not evidence of an arXiv posting). Read its introduction, Section 1.3, Corollary 1.6, and the identification argument. It reports that a uniqueness citation used to identify nearly balanced sectors with the balanced plane law needs justification for diagonal height interactions. It proposes a repair for 1<c<=2, but assumes the OpenAI state's existence and free-energy minimality, without checking those proofs. It leaves the rest of the OpenAI argument unassessed. This is a conditional repair report, not a full verification or a refutation of the claimed GFF limit.
3. [Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers, Ioan Manolescu, *Conformal invariance of the six-vertex model's height function*, arXiv:2610.07454](https://arxiv.org/abs/2610.07454). Opened arXiv page and PDF. Submitted October 5, 2026. It proves domain convergence using full-plane GFF input over its stated range; its abstract does not assert the whole interval (-1,1). This is separate work, not an arXiv version or endorsement of OpenAI's manuscript.
4. [Hugo Duminil-Copin, Karol Kajetan Kozlowski, Piet Lammers, Ioan Manolescu, *Gaussian free field convergence of the six-vertex model with -1<=Delta<=-1/2*, arXiv:2603.06268](https://arxiv.org/abs/2603.06268). Opened arXiv page and PDF. Submitted March 6, 2026, hence prior work rather than a follow-up. It already treats the full-plane subinterval [-1,-1/2]; the original row should retain this separate prior result.
5. [The oai-math-revised six-vertex page](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/), plus a connected GitHub search of that repository's issues for “six-vertex” (no results). The page supplies catalogue/prior-literature context, not a referee report. The official repository's all-state issues endpoint returned four maintenance/release pull requests, with no candidate-specific error report.
6. [Latent Seminar, *The balanced six-vertex height and its Gaussian limit*, October 6, 2026](https://lowrank.github.io/latent-seminar/OpenAI-Math/225-six-vertex-height), and [AI Proved What, episode 232, October 2026](https://aiprovedwhat.com/episodes/232-lipschitz-heights-gff/). These are expositions, not independent checks. Technical conclusions above come from primary manuscript text, not these summaries.
7. [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md), the Lean and OAI directory listings, and the OAI.lean import entry point. No matching six-vertex or weighted-height source title occurs in the catalogue or import entry point. Recursive full Lean/OAI tree responses were truncated and cannot establish absence. The separate untruncated `lean/docs` tree has 245 entries and neither `225.md` nor `232.md`, the family numbers of the candidates. No matching Lean formalization was located; no Lean build was run.

The untruncated Probability and MathematicalPhysics Lean subtree listings were also searched for six-vertex, weighted heights, Lipschitz, GaussianFree, FreeField, GFF, and VertexModel names. They contained no matching six-vertex or Lipschitz-height development (the Lipschitz matches concern other models). This supports the catalogue finding without relying on the truncated full tree.

Web searches used exact titles and variants with “arxiv”, “error”, “gap”, “refutation”, and “revision”, plus repository-specific queries. No separate arXiv version of the three OpenAI manuscripts, complete referee report, or independent verification of their full proofs was located. This is a search result as of November 14, not a claim that no such material exists. Initial web access to the supplied GitHub folders failed; connected GitHub reads supplied the actual manuscript sources. The attempted Hexagon abstract URL and a Chinese exposition URL were inaccessible.

## Recommended new “where it stands” sentence

OpenAI's unrefereed preprint *The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)* (September 23, 2026) claims the full range 0<c<=2 for the balanced zero-slope plane state, with variance multiplier 2/arccos(Delta) for unit height jumps and Green kernel -(2 pi)^(-1)log|x-y|. This is a claimed resolution of our plane statement, with no matching Lean formalization or complete independent verification located; Yan Ru Pei's November 2026 follow-up proposes a conditional repair of one state-identification gap. The two versions of *Gaussian free-field limits of weighted integer Lipschitz heights* (September 25 and October 6, 2026) concern a different triangular-lattice model.

## Spot check

Selected bottleneck: the lemma **“Boundary division and scalar continuation”**, label `lem:scalar-continuation`, in [Section 4 source](https://github.com/openai/math/blob/main/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/build/sections/04-angular-plane.tex), saved locally as [angular-plane.tex](sources/candidate1/angular-plane.tex). This lemma supplies the common analytic neighborhood and the inner spectral functions used to obtain the chiral currents. Without that analytic control, the later Gaussianity argument has no established spectral foundation.

The printed lemma claims a radius independent of the even chain length on which both marked/unmarked transfer-matrix quotients are holomorphic and uniformly bounded. It then claims strong endpoint limits and analytic, zero-free continuation of almost every scalar spectral function across common boundary bands.

I checked its finite local step directly using the actual R matrix from [Section 2](sources/candidate1/finite-rows.tex). Put
$$
 a(u)=\frac{\sin(\lambda-u)}{\sin\lambda},\quad
 b(u)=\frac{\sin u}{\sin\lambda},\quad
 r(u)=1-b(u)^2,\quad
 \Phi=\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$
Here the displayed formulas use the manuscript's spin basis. With tensor order auxiliary a, auxiliary a', quantum spin j, set
$$
 G(u)=R_{aj}(u)R_{a'j}(-u)^{t_{a'}}.
$$
The key identity is
$$
 G(u)(\Phi\otimes e_s)=r(u)(\Phi\otimes e_s),\qquad s=0,1.
$$
For example, on the unnormalized vector |000>+|110>, the first factor applied (the partial transpose) gives
$$
 a(-u)|000\rangle+|011\rangle-b(u)|110\rangle.
$$
Applying R_aj(u) cancels the |011> coefficient. The remaining coefficients are a(u)a(-u) and 1-b(u)^2, which agree by
$$
 \sin(\lambda-u)\sin(\lambda+u)=\sin^2\lambda-\sin^2u.
$$
The other quantum spin follows by spin reversal. At u=0, R(0) is the swap, and the partially transposed swap followed by the other swap has range in C Phi tensor C². Thus the complementary lower-right block vanishes at zero. Analyticity gives its O(u) bound for fixed lambda. Shrinking the disc makes that block's norm at most 1/4, so multiplying the triangular blocks gives the geometric-series bound and a complementary product of norm at most 4^(-L), as used in the proof.

An independent standard-library numerical calculation constructed the 8-by-8 operators for lambda=0.3, 1.2, pi/2, 2.5 and u=0, 0.001, 0.05, 0.03+0.02i. All 16 invariant-line checks passed, with maximum residual 2.23e-16; the range assertion at u=0 also passed. The process inherited nice priority 20 and used no numerical libraries.

**Finding:** the inspected finite local block identity and the resulting geometric-series mechanism check out. This does not check the whole lemma: the passage from finite-chain vector continuation through Gram limits to scalar analytic representatives with one common radius, and its compatibility with all previous thermodynamic estimates, remains unaudited. No conclusion about correctness of the full preprint follows from this spot check. The distinct reported state-identification gap remains the follow-up issue described above.


