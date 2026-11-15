# T132: metric scaling limits of decorated random planar maps

Verification date: 14 November 2026. Author on each candidate: **OpenAI**. The dates below are the manuscript dates printed in their TeX, not independently established public posting dates. The follow-up papers say the related OpenAI release appeared on 6 October 2026.

The recommendation is **PARTIAL-CLAIMED for the row as written**. The first manuscript claims the central metric-measure convergence for the entire requested parameter range, but with an unspecified deterministic distance scale and with degree measure. It explicitly declines to assert a normalization power law. This is a statement comparison, not a judgment that its proof is correct.

## 1. Metric-measure limits of subcritical FK and spanning-tree planar maps — September 24, 2026

Opened the manuscript's [TeX entry point](https://github.com/openai/math/blob/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/main.tex) and [actual introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/01-introduction.tex). The PDF is named [main.pdf](https://github.com/openai/math/blob/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/main.pdf); its GitHub wrapper opened, but the PDF body was not readable through that route. The theorem below was read from the manuscript's own TeX, not from an abstract or a third-party transcription.

Theorem 1.1, exact source statement:

```latex
\begin{theorem}[Metric and measure convergence]\label{thm:main}\label{tree:thm:main}
For each fixed \(q\in(0,4)\) in the FK ensemble, and for the spanning-tree
ensemble, there are deterministic positive numbers \(a_n\to0\) such that
\[
          (V(M_n),a_nd_n,\mu_n)
             \xrightarrow[n\to\infty]{\mathrm{law}}
          (S,D_h,\mu_h)
\]
in Gromov--Hausdorff--Prokhorov topology on compact metric probability
spaces modulo measure-preserving isometry. The limit has the parameter
specified above. Convergence holds through all positive integers \(n\);
the root and decoration are forgotten.
\end{theorem}
```

The definitions immediately preceding it matter. Maps are rooted connected multigraphs embedded in the oriented sphere, with loops and multiple edges allowed, and exactly n edges. The law of a decorated FK pair is proportional to q^(ell(M,A)/2), where ell = k(A)+k(A*)−1 = 2k(A)+|A|−|V(M)|. This is the manuscript's self-dual critical FK ensemble; “subcritical” in the title means gamma<2, not an FK model below its critical point. The spanning-tree law is uniform on map–tree pairs, so the map marginal is weighted by its number of spanning trees. The metric uses every primal edge, of length one; mu_n(v)=deg(v)/(2n), with a loop counted twice. The target is the ordinary unit-area gamma-quantum sphere, with marks forgotten, its intrinsic LQG metric in a fixed deterministic normalization, and quantum area measure.

| Our words | Manuscript's assertion | Comparison |
| --- | --- | --- |
| Random planar maps weighted by critical FK | The explicit q^(ell/2) law on rooted spherical multigraphs with n edges | Matches this standard finite spherical ensemble; does not assert every possible face-restricted FK map model. |
| 0 ≤ q < 4 | Each fixed 0<q<4, plus a separate uniform map–spanning-tree ensemble | Covers our q=0 interpretation as well as all positive q in the row; it does not take q down to zero in the FK formula. |
| q=1 uniform map | At q=1 all 2^n decorations have equal weight for each n-edge map | Matches. |
| q=2 critical Ising map | FK–Ising at q=2 | Matches the FK interpretation of our wording. No assertion about a separately specified spin-map convention is needed or inferred. |
| q=2+2 cos(pi gamma²/2) | The same equation, with the unique gamma in (sqrt(2),2); gamma=sqrt(2) for trees | Matches. Substitution gives gamma=sqrt(8/3) at q=1 and sqrt(3) at q=2. |
| Distances rescaled by n^(−1/d_gamma+o(1)) | Only deterministic a_n>0, a_n→0 | **Not asserted.** Immediately after the theorem the paper expressly excludes a normalization power law. It does not supply the required asymptotic for a_n. |
| Distances | Shortest-path distance using every primal map edge | Matches the graph metric, not tree distance, a directed distance, or an encoding distance. |
| Gromov–Hausdorff–Prokhorov convergence | Convergence in law in exactly that topology, through every positive integer edge count | Matches the full convergence claim in this model, not just bounds, subsequences, or convergence at sampled points. |
| gamma-LQG metric sphere | Ordinary unit-area gamma-LQG sphere, intrinsic metric and area | Matches the finite spherical target with the stated area convention. |
| Discrete measure in our GHP statement | Our row leaves it unspecified; the paper fixes normalized degree measure | The row needs a measure convention. If it meant uniform vertex measure, that extra conclusion is absent: the paper explicitly says it requires a separate argument. |

Thus this is a claim of the main geometric limit across the requested q range, with one explicit missing clause from our statement: the n-dependent distance exponent. Unspecified deterministic rescaling is not, by itself, a proof of a particular power law. A separately established finite-ensemble distance-exponent estimate could identify the exponent, but no such deduction is asserted here or established in this verification. The measure issue is an ambiguity in our row, not an additional restriction on q.

## 2. The critical Liouville quantum sphere and geometric limits of FK maps at q=4 — September 24, 2026

Opened the manuscript's [TeX entry point](https://github.com/openai/math/blob/main/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/build/main.tex) and [actual introduction](https://raw.githubusercontent.com/openai/math/main/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/build/sections/00-introduction.tex). The [main.pdf wrapper](https://github.com/openai/math/blob/main/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/main.pdf) opened; the theorem text comes from TeX. The introduction identifies two main conclusions, quoted here exactly.

Theorem 1.1:

```latex
\begin{theorem}[The critical area-marked sphere]\label{thm:continuum}
As $\gamma\uparrow2$, the laws of $(H_\gamma,\nu_\gamma)$ converge to a unique nondegenerate probability law $\mathsf P_{\rm crit}$ in
\[
 H^{-1}(S^2,g_{\rm round})\times\mathcal P(S^2),
\]
with the norm topology in the first factor and the weak topology in the second. Let $(H,\nu)$ have this law and set $h=H+\log g_{\rm round}$ in local conformal coordinates. Then $\nu=\mu_h^{\rm crit}$, where on compact sets avoiding $0,1,\infty$,
\begin{equation}\label{intro:critical-area}
 \mu_h^{\rm crit}(\dd z)
 =\lim_{\eps\downarrow0}
  \bigl(2\log(1/\eps)-h_\eps(z)\bigr)
        \eps^2e^{2h_\eps(z)}\,\dd^2z
\end{equation}
locally weakly in probability. This positive measure extends across the three marks without atoms, has full support, and has total mass one.

After forgetting the three marks, sampling three new conditionally independent area points and normalizing them to $0,1,\infty$ recovers $\mathsf P_{\rm crit}$. If $f$ maps the new coordinate to the old one, the field transforms as
\[
 h_{\rm new}=h_{\rm old}\circ f+2\log|f'|.
\]

With any one fixed deterministic normalization of the Ding--Gwynne critical local metric, the compatible chart metrics define an intrinsic length metric on the sphere punctured at the three marks. Its completion adds exactly those marks and is a finite continuous metric $D_h$ on $S^2$, inducing the usual topology. The area and completed metric are measurable functions of the same field and obey the corresponding charge-$2$ coordinate rules.
\end{theorem}
```

Theorem 1.2:

```latex
\begin{theorem}[Joint critical universality]\label{thm:main}
For the finite law \eqref{intro:fk-weight}, there is a deterministic sequence $a_n>0$, with $a_n\to0$, such that through all positive integers $n$,
\begin{equation}\label{intro:joint-limit}
 \bigl((\phi_n)_*m_n,K_n(a_n),\Gamma_n\bigr)
 \ \xrightarrow{\ d\ }\
 \bigl(\mu_h^{\rm crit},
       \{(z,w,D_h(z,w)):z,w\in S^2\},\Gamma\bigr).
\end{equation}
Here $(H,\mu_h^{\rm crit})\sim\mathsf P_{\rm crit}$, the area topology is weak convergence, the distance-graph topology is the Hausdorff topology just defined, and the loop topology is convergence by $\eps$-matchings. All nesting and multiplicities are retained. In the same joint convergence,
\begin{equation}\label{intro:flag-mesh}
 \max_{T\ \text{flag of }X_n}\diam_\rho\phi_n(T)
       \ \xrightarrow{\ \Prob\ }0.
\end{equation}
The metric normalization is the one fixed in Theorem~\ref{thm:continuum}; changing it by a deterministic factor changes $a_n$ by that factor.
\end{theorem}
```

Here the law is proportional to 2^ell on n-edge rooted spherical maps, phi_n is the three-area-mark normalized equilateral-flag uniformization, m_n gives each of the 4n flags mass 1/(4n), K_n(a) is the graph of all rescaled original-primal-vertex distances in those coordinates, and Gamma is the independent nested CLE_4 decoration. Theorem 1.1 concerns the field and area limit as gamma increases to 2; it does not assert convergence of subcritical metrics to the critical metric. Corollary 1.3 explicitly gives the resulting degree-measure GHP convergence to the critical metric sphere.

Comparison: same type of finite spherical FK maps and the same original graph-distance quantity, but **q=4, gamma=2**, whereas our row expressly requires q<4, gamma<2. This candidate supplies no case within our row. It asserts a stronger joint embedded endpoint limit in its own regime, with an unspecified deterministic a_n; it also expressly disclaims a power law or formula for the critical metric dimension. Candidate verdict for T132: **NOT-THIS (excluded endpoint)**.

## 3. A Linear Clock for Random Walk on Tree-Weighted Planar Maps — October 5, 2026

Opened the manuscript's [TeX entry point](https://raw.githubusercontent.com/openai/math/main/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/build/paper.tex) and [actual introduction](https://raw.githubusercontent.com/openai/math/main/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/build/sections/01-introduction.tex). The PDF filename is [linear-clock-random-walk-tree-weighted-planar-maps.pdf](https://github.com/openai/math/blob/main/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/linear-clock-random-walk-tree-weighted-planar-maps.pdf).

Theorem 1.1, exact source statement:

```latex
\begin{theorem}[Linear clock and conditional laws]\label{thm:main}
For every finite $T>0$, define
\[
 Q_n^T=\Law\bigl((X^n_{nt})_{0\le t\le T}\mid M_n,T_n\bigr),
 \qquad
 Q_h^T=\Law\bigl((B^h_t)_{0\le t\le T}\mid h\bigr).
\]
With the spatial normalization \eqref{eq:spatial-normalization},
\[
 (V_n,a_nd_n,\mu_n,Q_n^T)
       \xrightarrow{\ d\ }(S,D_h,\mu_h,Q_h^T)
       \qquad\text{for }\delta_T,
\]
through all positive integers $n$. Thus the deterministic clock
multiplier for \eqref{eq:walk-generator} and \eqref{eq:continuum-form}
is $c=1$.
\end{theorem}
```

The ensemble is precisely the q=0 map–spanning-tree ensemble of candidate 1. The walk starts from degree measure, attempts moves at rate one, and chooses an incident half-edge uniformly, including loops and multiplicities. The continuum process is Liouville Brownian motion on the ordinary unit-area sqrt(2)-LQG sphere, with Dirichlet form (1/2) times the round Dirichlet integral. The metric delta_T includes GHP comparison and Prokhorov comparison of the conditional path laws in the Skorokhod J_1 topology.

Its spatial normalization is explicitly

    Delta_n = max{1, diam(V_n,d_n)}, Delta = diam(S,D_h),
    a_n = exp{m(log Delta) - m(log Delta_n)},

where m(Y) solves E[arctan(Y−m(Y))]=0 and the expectations use unconditional laws. Immediately after this definition, the manuscript takes the spatial GHP limit from the metric companion as an input.

Comparison: it retains a full measured graph-metric space in its conclusion, so it is more than a statement solely about a walk, but the new assertion concerns the **time** normalization and conditional path laws, only at q=0. It depends on candidate 1 for the spatial limit and gives no estimate a_n=n^(−1/d_sqrt(2)+o(1)). A time acceleration by n does not identify a distance exponent. Candidate verdict for this row: **PARTIAL-CLAIMED (q=0 spatial consequence, imported from the companion; new dynamical conclusion)**.

## Follow-ups and verification status

The following primary sources were actually opened. Search results and catalog descriptions were used only to locate them.

- **Nina Holden**, [The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity](https://arxiv.org/abs/2610.10501), submitted 7 October 2026; also opened its [full HTML](https://arxiv.org/html/2610.10501v1), especially the end-of-introduction statement. It treats a Boltzmann disk with macroscopic boundary, convergence under the Tutte embedding, and random walk modulo time parametrization. Holden explains that related OpenAI papers prompted posting, names the linear-clock paper and its metric and conformal companions, and credits them with resolving several listed future directions, including a metric-limit direction. This is relevant expert acknowledgement of the claims; it is not a stated audit of their proofs, and her disk embedding theorem does not prove our spherical GHP statement or its exponent clause. The paper's own AI statement says AI was used for proofreading and revision, not for mathematical ideas or manuscript writing; a search-index label calling it AI-generated was therefore not adopted.
- **Nina Holden and Pu Yu**, [The circle packing and Riemann uniformization embedding of tree-weighted planar maps converge to Liouville quantum gravity](https://arxiv.org/html/2610.10505v1), 7 October 2026; also opened its [arXiv abstract page](https://arxiv.org/abs/2610.10505). The title above follows the paper itself; the abstract page has a grammatical variant. It proves conformal-embedding convergence for tree-weighted maps in disk, sphere, and whole-plane topologies. Their statement says the OpenAI results do not imply theirs or conversely, to their knowledge. This does not independently establish graph-metric convergence.
- The release's [lean/docs/211.md](https://github.com/openai/math/blob/main/lean/docs/211.md) names only **Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four**. Its stated formalization scope is q>4, distance scale c(q)n^(−1/2), degree measure, and a Brownian CRT target. Opened [lean/ComparatorChallenges/FKCRT.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FKCRT.lean), whose MainStatement indeed quantifies q>4 and the CRT expectation limit. This is outside our parameter range and target. The `sorry` in that challenge file is a placeholder for a separately supplied solution, not by itself a proof defect. No Lean formalization of these three candidates' LQG conclusions was located. The [formalization index](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml) was also opened; it supplies no independent verification of T132 here.

A further later reference was opened: **Krzysztof Kapulkin and Nathan Kershaw**, [Reasoning is topologically simple](https://arxiv.org/html/2611.03739v1), 2 November 2026 (the [arXiv abstract page](https://arxiv.org/abs/2611.03739) lists the first author as Chris Kapulkin). Its Appendix B.3 includes the linear-clock manuscript in a corpus of papers for textual-topology analysis. This is a study of writing and reasoning traces, not a mathematical validation or refutation of the clock theorem.

The three community-note pages were also opened: [metric paper](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/), [critical q=4 paper](https://mathcommunity.github.io/oai-math-revised/papers/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/), and [linear-clock paper](https://mathcommunity.github.io/oai-math-revised/papers/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/). All displayed no contributed notes, with automatically collected material separately marked unreviewed. Their linked GitHub issue searches failed to open, so their issue contents could not be checked. No later mathematical follow-up specific to the q=4 candidate was located.

Searches used all three exact titles and combinations with “arxiv”, “error”, “gap”, “correction”, “refutation”, “referee”, “normalization”, and “exponent”. No same-title arXiv version, mathematical error report, refutation, or referee report was located. This is a limited negative search result, not evidence that none exists. No proof-correctness verdict is made. The dated expert remarks above warrant recording the release's claims, but not changing “claimed” to “proved and checked”.

Other pages opened as navigation or assessment leads: [Plectis Atlas family 211](https://wcook04.github.io/plectis-atlas/families/211.html), its [linear-clock reading page](https://wcook04.github.io/plectis-atlas/papers/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026.html), and the repository [LICENSE](https://github.com/openai/math/blob/main/LICENSE). Exact copies of the three introductions and the checked local-kernel section are saved in sources/, with the repository license in sources/LICENSE.txt. The exact theorem excerpts above preserve the source wording; the repository licenses its material under Apache 2.0. The primary TeX and arXiv sources, rather than these navigation sites, support the mathematical comparisons. Initial folder, guessed paper.tex/paper.pdf, and raw PDF attempts that failed are recorded in LOG.md.

## Recommended replacement for “where it stands”

OpenAI's unrefereed preprint “Metric-measure limits of subcritical FK and spanning-tree planar maps” (September 24, 2026) claims convergence of the full graph metric with normalized degree measure to the corresponding unit-area LQG sphere for every fixed 0<q<4 and for spanning-tree-weighted maps. It uses an unspecified deterministic distance rescaling and explicitly does not assert the n^(−1/d_gamma+o(1)) normalization in our statement; uniform vertex measure would also need a separate argument if that is intended. Record a partial claim for the row as written, with relevant expert acknowledgement but no located referee verification or Lean formalization of this LQG result.


## Spot check

Selected the **Ladder local limit and conditional paths** lemma (`loc:ladder-llt`) in the [metric manuscript's local-kernel section](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/03-local-kernels.tex); an exact local copy is [sources/metric-local-kernels.tex](sources/metric-local-kernels.tex). This is a load-bearing smoothing input to the FK conditional resampling laws, which in turn support the metric identification. The complete lemma and proof were read. This check concerns that input, not the whole rigidity or finite-sphere argument.

The lemma asserts an endpoint local limit of the form

    P(sum_(j≤m_N) (T_j,Y_j)=(k,l))
      = 2 N^(−3/2) [g_h(k/N,l/sqrt(N))+o(1)],
    m_N/sqrt(N) → h > 0,

on k+l congruent to m_N modulo 2, together with conditional first-passage-bridge convergence. Four checks of its proof give the following results.

1. **Density, normalization, and sign.** Write sigma²=(1−b_F)/2 and rho=b_F/(1−b_F), so 0<rho<1 for fixed 0<q<4. For the backward first coordinate hitting −h, the first-passage time has density

       f_h(t)=h/(sigma sqrt(2 pi) t^(3/2)) exp(−h²/(2 sigma² t)).

   The forward second-coordinate displacement conditional on that time is Gaussian with mean rho h and variance sigma²(1−rho²)t. Multiplying the two densities gives exactly the paper's

       g_h(t,y)=h/[2 pi sigma² sqrt(1−rho²) t²]
                exp{−h²/(2 sigma²t)
                    −(y−rho h)²/[2 sigma²(1−rho²)t]}.

   Integrating in y recovers f_h(t), and integrating in t gives total mass one. The positive mean rho h is consistent with reversing the backward second displacement. Thus the scale and sign in this density check out.

2. **Fourier domination.** The same Brownian decomposition gives the joint characteristic function

       E exp{i(s tau_h+t Y_h)}
         = exp{i rho h t − h sqrt((1−rho²)t²−2 i s/sigma²)},

   with the square root having nonnegative real part. If a=(1−rho²)t² and b=2s/sigma², the real part of sqrt(a−ib) is sqrt((sqrt(a²+b²)+a)/2). It is bounded below by a positive constant times sqrt(|s|)+|t| for fixed q<4. This verifies the strict modulus bound away from zero in the scaled annulus used in the proof. Given the stated iid-block stopped-contour invariance principle, taking m comparable to (sqrt(|s|)+|t|)^(−1) then gives the required near-zero characteristic-function bound. This argument loses uniform constants as rho tends to one; the theorem only fixes q<4.

3. **Lattice factor.** The four displayed support points (1,0), (2,1), (2,−1), (3,0) have differences generating the index-two lattice k+l even: the vectors (1,1) and (1,−1) have determinant −2. Every block has T+Y odd. Consequently the only dual modulus-one points are (0,0) and (pi,pi), and the two Fourier contributions add precisely on the feasible parity class. The leading factor 2 is consistent, as is N^(−3/2) from one time coordinate of scale N and one displacement coordinate of scale sqrt(N).

4. **Conditioned paths.** Reserving an epsilon fraction of the independent ladder blocks gives an endpoint-density tilt for the remaining path. On compact sets with h,t>0, the total endpoint density is bounded below, the remaining-block density is bounded above, and g_(epsilon h) is bounded and continuous after extending it by zero to nonpositive durations. Conversely the unreserved blocks' uniform upper bound controls the conditional probability of a large reserved duration or oscillation by its unconditional probability. Brownian first-passage scaling makes this probability tend to zero as epsilon decreases. These are the ingredients needed for the stated bridge argument; no contradiction was found in that step.

The local-limit calculation and the conditional-tilt mechanism survive this limited check. The stopped-contour invariance principle, the exact reconstruction of FK observations, and the later conditional-kernel/rigidity arguments were not independently verified. This finding therefore does not certify the lemma in its full surrounding framework, and does not certify the paper. It also supplies no asymptotic for the global distance scale a_n.
