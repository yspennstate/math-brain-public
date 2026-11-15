# T132: metric scaling limits of decorated random planar maps

Round 5 reader's note: the theorem quotations and the literature history below are inherited from earlier workers; the round-5 record at the end distinguishes the sources reopened in this session. All four theorem quotations were checked against fresh source TeX again. The round-3 conditional normalization proof is in [PRIOR_PROOF.md](PRIOR_PROOF.md), the round-4 moment proof is in [ROUND4_PROOF.md](ROUND4_PROOF.md), and this session's interior-localization result is in [PROOF.md](PROOF.md). The latest recommendation is at the end.

Original verification date: 14 November 2026; continuation: 15 November 2026. The original theorem comparisons and follow-up record are retained below. The three introduction sources were independently re-fetched and checked in this continuation; follow-up pages not explicitly listed in the continuation record were opened by the previous worker, not reopened here. Author on each candidate: **OpenAI**. The dates below are the manuscript dates printed in their TeX, not independently established public posting dates. The follow-up papers say the related OpenAI release appeared on 6 October 2026.

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

Thus this is a claim of the main geometric limit across the requested q range, with one explicit missing clause from our statement: the n-dependent distance exponent. Unspecified deterministic rescaling is not, by itself, a proof of a particular power law. A separate argument is needed to identify the exponent. The continuation below gives a conditional deduction for q=0 from later assertions inside this same preprint; it was absent from the earlier verification. The measure issue is an ambiguity in our row, not an additional restriction on q.

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

OpenAI’s unrefereed preprint “Metric-measure limits of subcritical FK and spanning-tree planar maps” (September 24, 2026) claims full graph-metric GHP convergence with normalized degree measure for each fixed 0<q<4 and for spanning-tree-weighted maps. Its main theorem leaves the scale unspecified, but its internal tree-scale assertions imply n^(−1/d_sqrt(2)+o(1)) for q=0 if those assertions hold; this implication does not verify their proofs. The whole row remains only partially claimed as written: no distance-exponent deduction for general 0<q<4 was established here, and uniform vertex measure would require a separate argument if intended.

## Earlier spot check (14 November 2026; retained)

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

## Continuation: q=0 normalization exponent (15 November 2026)

The new result is the conditional implication proved in [PRIOR_PROOF.md](PRIOR_PROOF.md). This changes the earlier assessment of what can be *deduced* for the spanning-tree clause, while leaving its literal transcription of Theorem 1.1 intact. It is not an independent scaling-limit theorem and does not certify the paper.

Read the following additional sections of OpenAI’s metric manuscript itself, not third-party summaries:

- [Tree background](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/background.tex), defining p=1/d_sqrt(2), internal graphs, and the volume-growth input; saved as [background.tex](sources/background.tex).
- [Internal moments](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/moments.tex), defining A_j and supplying fixed-window moment compactness and uniform integrability; saved as [moments.tex](sources/moments.tex). The web reader returned a cache miss for this section; the read-only GitHub connector retrieved the source.
- [All-scale bootstrap](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/bootstrap.tex), particularly `tree:prop:internal_norm_comparison`, `tree:prop:bootstrap`, and `tree:thm:bilateral_limit`; saved as [tree-bootstrap.tex](sources/tree-bootstrap.tex).
- [Tree sphere](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/sphere.tex), particularly `tree:prop:sphere_identification` and the final normalization; saved as [sphere.tex](sources/sphere.tex).
- [Measured convergence](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/02-measured-convergence.tex), the arctan-center and normalization lemmas; saved as [measured-convergence.tex](sources/measured-convergence.tex).

For every fixed integer offset i, the claimed universal comparison is alpha C 2^(−ip) <= q_i <= beta C 2^(−ip), with the same alpha,beta for all offsets and laws. The unit norm makes C lie between 1/beta and 1/alpha. The all-scale extraction and moment convergence therefore bound every cluster value of A_(j+m)/A_j between R_0^(−1)2^(mp) and R_0 2^(mp), where R_0=beta/alpha is independent of the fixed m. Iterating the resulting eventual m-step bounds along residue classes and then sending m to infinity gives log_2(A_j)/j -> p. This yields B_(2n)=n^(p+o(1)); the sphere identification and deterministic normalization give a_n B_(2n) bounded above and away from zero, hence a_n=n^(−p+o(1)).

Two independent formulations of the elementary argument and a check using diameter tightness are in PRIOR_PROOF.md. The constants need to be independent of m; their failure to be uniform would invalidate the deduction. The paper explicitly includes negative offsets and fixed finite enlargements, and states the needed uniform integrability. Neither a single record subsequence nor just its s=p/2 bound would suffice. No adjacent-ratio limit is used or obtained.

### Current follow-up record

The bounded initial search on 15 November used the web search tool for the exact metric and clock titles, planar-map metric error reports, and later FK/Liouville results. It found no later full solution or primary mathematical error report. Reopened the arXiv abstract pages [2610.10501](https://arxiv.org/abs/2610.10501), by Nina Holden, and [2610.10505](https://arxiv.org/abs/2610.10505), by Nina Holden and Pu Yu; they still concern conformal embeddings, rather than the requested finite spherical graph-metric limit with its normalization exponent. The metric paper’s [community page](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/) still displays no contributed notes. These negative findings are limited to the searches and pages described.

Independently re-fetched the release’s [lean/docs/211.md](https://github.com/openai/math/blob/main/lean/docs/211.md) and [FKCRT.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/FKCRT.lean), saved under sources/. The documented scope remains q>4 and a Brownian CRT, outside this row. No Lean check was run. The earlier source and license copies are preserved, and fresh source hashes are recorded in LOG.md.

## Spot check

The new check is the normalization implication in PRIOR_PROOF.md, conditional on the source propositions listed above. The load-bearing unverified assertion is `tree:prop:internal_norm_comparison`, especially its maximizing-zoom upper bound H<=beta C. The proof says that vanishing ambient comparison forces vanishing internal unit endpoint cost after lifting interior routes and controlling two omitted tip pieces. This implication uses earlier certificate, nonzero-local-cost, and moment lemmas; those inputs have not been audited here. They should be the next verification target. No concrete contradiction in that argument is asserted.

## Round 4 verification (15 November 2026)

The earlier sections above preserve the first two workers' theorem transcriptions and literature record. Their claims about sources opened refer to those workers unless a source is listed again below. The round-3 normalization proof is preserved separately as [PRIOR_PROOF.md](PRIOR_PROOF.md); the current [ROUND4_PROOF.md](ROUND4_PROOF.md) contains the new moment audit and an independent recheck of that earlier implication. No source file outside the present folder was changed.

### Opened in this session

- The three introduction TeX files quoted above, re-fetched with the read-only GitHub connector. The four main theorem blocks were checked against these fresh files. Their literal scope remains as recorded above.
- The metric paper's [main.tex](sources/main.tex), [bootstrap.tex](sources/bootstrap.tex), [moments.tex](sources/moments.tex), [certificates.tex](sources/certificates.tex), and [comparison.tex](sources/comparison.tex), fetched from build/sections/tree/ except the entry point. In particular, the maximizing-zoom proof, the moment lemmas, and the nonzero-local-cost and interior reconstruction passages were read. The incorrectly guessed build/tree/ paths failed with cache misses; the corrected build/sections/tree/ paths succeeded through the connector.
- [Nina Holden, The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10501](https://arxiv.org/abs/2610.10501), and [Nina Holden and Pu Yu, The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10505](https://arxiv.org/abs/2610.10505): primary abstract pages reopened. Both show only the 7 October 2026 submission; their conclusions concern conformal embeddings, not the requested spherical graph-metric theorem with its exponent.
- The metric paper's [community page](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/) reopened; it still says there are no contributed notes. Initial web searches for the metric title with error/correction/November and for spanning-tree metric/OpenAI/November found no later full solution or primary error report. This is a bounded negative finding, not evidence that no criticism exists.
- [lean/docs/211.md](sources/211.md) and [FKCRT.lean](sources/FKCRT.lean) re-fetched. The documented and stated scope remains q>4 with a Brownian CRT target. No Lean build or LQG formalization was verified.

### Spot check: the maximizing-zoom moment step

The analytic moment step in Proposition tree:prop:internal_norm_comparison holds under its stated retained interval structure. For a stationary subadditive family with independent disjoint interval costs and dyadic norms at most 2^(-lp), [ROUND4_PROOF.md](ROUND4_PROOF.md) establishes

\[
 \mathbb E[X^k{\bf1}_{\{X>R\}}]
 \le (1+2^{kp-1})R^{-(kp-1)/(k-1)},\qquad R\ge1.
\]

The proof uses only a finite dyadic partition, the multinomial formula, independence, and Holder's and Markov's inequalities. It is uniform over different continuum laws and deterministic zooms. The maximizing normalization satisfies 1/2<||X||_k<=1, so any weak limit retains kth moment at least 2^(-k). The estimate also implies a uniform moment of order k+delta for every 0<delta<(kp-1)/(k-1), and therefore moment passage on every fixed dyadic enlargement. No numerical value of d_(sqrt(2)) was assumed.

Two attempts to break the argument identify indispensable assumptions. A single rare Bernoulli amplitude shared by all intervals satisfies stationarity, subadditivity and the dyadic norm bounds, but loses its kth moment in the limit; it violates independence. A normalized rare-jump Poisson process has independent additive interval costs and loses its kth moment at the boundary kp=1. Neither is a counterexample under the preprint's hypotheses. The positive threshold and the tail exponent were also re-derived by first fixing the partition size and by balancing the two tail terms.

The remaining geometric step is explicit: in the limit C_r/H_r -> 0, the proof needs the spatial upper-certificate comparison to give zero compactly local costs and then needs those certificates to lift to paths internal to the unit interval cell. That is the content used from Proposition tree:prop:certificate_limit, Lemma tree:lem:chart_reconstruction and Lemma tree:lem:nonzero_local_cost. Their relevant passages were read, but their geometric hypotheses and full proofs were not independently established. No concrete refutation of these passages is asserted.

### Recommended replacement for “where it stands”

OpenAI's *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026; AI-generated and not refereed) claims graph-metric Gromov–Hausdorff–Prokhorov convergence for every fixed 0<q<4 and for spanning-tree-weighted maps, with degree measure and an unspecified deterministic distance scale. For q=0, its later internal assertions imply the requested distance exponent conditionally; the present check verifies the moment-preservation step but leaves the geometric comparison unverified. The complete statement should remain recorded as a partial claim rather than a verified settlement.

Validation: OMP_NUM_THREADS=1 nice -n 15 python3 audit.py passed with exit 0. It checked all four theorem quotations against fresh TeX, unchanged scope sources, 700 multinomial exponent vectors, exact rational tail exponents and dyadic-rounding bounds, and the Bernoulli and Poisson counterchecks. The full output and hashes are in LOG.md.

## Round 5 verification (15 November 2026)

The bounded opening search found no later full solution or primary mathematical error report. It used the web search tool with the metric title plus error/correction/November, OpenAI planar-map metric refutation, and tree-weighted planar-map metric November 2026. This is a search-limited finding. No solved-elsewhere conclusion is warranted.

### Opened in this session

- The actual theorem-bearing introductions of all three candidates, using the raw source URLs linked in sections 1–3 above and the read-only GitHub connector. Exact copies are saved as metric-introduction-fresh.tex, critical-introduction-fresh.tex and clock-introduction-fresh.tex under sources/. All four theorem blocks quoted above agree exactly with these files. No change to the model, parameter ranges, degree-measure convention or unspecified spatial normalization was found.
- The metric paper's [certificates.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/certificates.tex) and [background.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/build/sections/tree/background.tex), reopened through the same connector and saved with -fresh suffixes under sources/. They agree byte-for-byte with the earlier saved versions. Read the full finite-band reconstruction proof, the nonzero-local-cost proof, raw path-range definitions and approximation paragraphs, exact discrete sewing rules, cell-interior preimage argument and topology assertions. Also read the inherited moments.tex and bootstrap.tex, including the maximizing-zoom proof; those two sources were not freshly fetched in round 5.
- [Nina Holden, The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10501](https://arxiv.org/abs/2610.10501), primary abstract page. It shows only v1, 7 October 2026, and a Boltzmann-disk embedding and random-walk conclusion.
- [Nina Holden and Pu Yu, The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10505](https://arxiv.org/abs/2610.10505), primary abstract page; this title follows that page verbatim. It shows only v1, 7 October 2026, and conformal-embedding convergence in disk, sphere and whole-plane settings. Neither abstract gives the requested graph-metric GHP theorem and its distance exponent.
- The metric paper's [community page](https://mathcommunity.github.io/oai-math-revised/papers/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/), updated 14 November 2026. It still says “No notes yet”; its automatically collected notes are expressly unreviewed. Its reported accepted comparator run concerns the q>4 CRT statement, not this manuscript's LQG limit.
- [lean/docs/211.md](https://raw.githubusercontent.com/openai/math/main/lean/docs/211.md) and [lean/ComparatorChallenges/FKCRT.lean](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/FKCRT.lean), reopened through the read-only GitHub connector. Fresh copies agree with the inherited files. Both specify q>4 and a Brownian continuum random tree. No Lean build or formalization of the LQG conclusion was verified.

### Independent check of the earlier result

The round-4 tail estimate holds under its stated independence and interval assumptions. For a dyadic partition into m pieces, write the kth power of their sum as pure monomials P plus mixed monomials Q. Independence gives E P <= m^(1-kp), and with u=k/(k-1) gives ||Q||_u <= m^(k-kp). Holder and Markov then give the earlier bound after choosing m near R^(1/(k-1)); both its exponent (kp-1)/(k-1) and constant 1+2^(kp-1) are recovered. This recheck does not validate the retained probabilistic structure or geometric compactness.

### Spot check: internal lifting of compact interior paths

The selected passage is the final clause of Lemma tree:lem:chart_reconstruction:

> The same conclusions hold inside the interior of a fixed interval cell, using only links witnessed within that interval.

The limited assertion needed for actual sewn-graph certificate approximants follows directly from the raw contour ranges. [PROOF.md](PROOF.md) proves this as a deterministic localization lemma. A compact range inside the cell has all its contour preimages a positive time distance from the interval endpoints. Every sufficiently late approximating path then has every used representative inside the interval. The entire witnessing interval of each first-coordinate identification is internal. Both complete steps of a second-coordinate match are internal as well, because its terminal times differ from its recorded primal representatives by one mesh step. Thus the path uses only internal links, with exactly its original cost, regardless of how many crossings it makes.

The no-outside-preimage condition itself follows from the exact swept-area identity: images of disjoint time intervals have zero area overlap, while an outside visit to an interior point would put a positive-length outside interval entirely inside the cell. This argument does not require disk topology. The connected interior, actual certificate approximation, local joining modulus and jointly retained endpoint modulus are explicitly retained as separate inputs when deriving the resulting nonzero-local-cost contradiction.

Two counterchecks show why the hypotheses matter: ranges converging to a cell boundary can retain outside times, and a curve without the preimage property can visit an interior compact from outside times. A third check detects the one-step edge issue: for increments (0,1),(1,0),(0,-1), the matched edge has primal representatives 0,2 inside [0,2], but its down-step ends at 3 and is absent from that internal graph. The positive limiting interior margin rules this out; mere membership of the two primal representatives is insufficient at a fixed mesh.

The new result establishes interior localization for actual approximants, not the general realization of arbitrary formal chart outputs or their conditional field-local laws. In particular it does not justify recovering an earlier graph with disabled active windows merely by restricting spatial ranges. The next unverified step is bootstrap.tex lines 120–129: turning ambient comparison constants tending to zero into zero-cost local certificates in the joint limit under changing laws and quantum-scale zooms. The coupled reference-metric and upper-certificate closure arguments remain to be checked. No proof-correctness verdict on the preprint follows from this spot check.

### Latest recommended replacement for “where it stands”

OpenAI's *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026; AI-generated and not refereed) claims graph-metric Gromov–Hausdorff–Prokhorov convergence for every fixed 0<q<4 and for spanning-tree-weighted maps, using degree measure and an unspecified deterministic distance scale. For q=0, later assertions in the manuscript conditionally imply the requested exponent; the moment estimate and deterministic interior-localization implication check out, while the upper-certificate limit and other geometric inputs remain unverified. The complete row should remain recorded as a partial claim rather than a verified settlement.

Validation in this session: `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` passed (exit 0). It checked 21,844 axial walks, 730,604 subintervals, 3,779,478 first-coordinate equivalence pairs, 99,204 internal vertical-match occurrences and 40 rational tail-exponent cases, plus the four exact theorem quotations and fresh-source equality. Runtime was 3.378 seconds; peak resident memory was 19,038,208 bytes, with inherited process priority 20. The earlier document-link failure and repair are recorded in LOG.md.
