# T022 verification

Checked 14 November 2026 (Asia/Tbilisi).

The full statement is claimed in the first candidate. This is a statement-and-literature verification, not a finding that the proof is correct or that the conjecture has an accepted resolution.

## Our statement

In first-passage percolation on Z^2 with iid nonnegative continuous edge weights satisfying E[min(t_1,...,t_4)^2] < infinity, almost surely no bi-infinite geodesic exists. The four weights in the minimum are independent copies. Here “continuous” means an atomless distribution; it does not require a density.

## 1. No bigeodesics in planar first-passage percolation

Author as printed: OpenAI. Date as printed: September 24, 2026.

[Manuscript](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf); [actual theorem source](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex). Local unmodified extract: [source1.tex](source1.tex).

Theorem 1.1, copied verbatim as LaTeX (macros are those of the manuscript):

```tex
\begin{theorem}\label{thm:main}
Suppose that \(G\) has no atoms and that, for independent
\(X_1,X_2,X_3,X_4\) with law \(G\),
\begin{equation}\label{eq:minimum-moment}
 \EE\!\left[\min\{X_1,X_2,X_3,X_4\}^{\,2}\right]<\infty.
\end{equation}
Then, with probability one, there is no sequence
\((v_i)_{i\in\Z}\) of pairwise distinct vertices with consecutive
vertices adjacent and
\[
 \sum_{k=i}^{j-1}t_{\{v_k,v_{k+1}\}}=T(v_i,v_j)
 \qquad\text{for every }i<j.
\]
\end{theorem}
```

The immediately preceding setup specifies the unoriented nearest-neighbor edges of Z^2, independent edge weights with common Borel probability law G on [0,infinity), and T as the infimum of summed edge weights over finite walks. Thus the hypotheses implicit in G and T are the same model as our row.

| Our wording | Manuscript wording or definition | Comparison |
| --- | --- | --- |
| First-passage percolation | T is an infimum of summed edge weights | Same minimizing metric; not last-passage percolation. |
| Z^2 | Unoriented nearest-neighbor edges of Z^2 | Same graph, dimension, and undirected model. |
| iid | Independent weights with common law G | Identical. |
| Nonnegative | G is a law on [0,infinity) | Identical. Nonatomicity also rules out a zero atom. |
| Continuous edge weights | G has no atoms | Identical under the usual probabilistic meaning; singular continuous laws are included. If “continuous” were intended to require a density, the preprint claims more. |
| E[min(t_1,...,t_4)^2] < infinity | Four independent X_i with law G and exactly that second moment | Identical; no finite individual-edge mean or exponential moment is added. |
| Almost surely no bi-infinite geodesic exists | One probability-one event excludes every doubly infinite simple adjacent sequence whose every finite subpath attains T | Same quantity and full strength. End directions may depend on the environment; there is no restriction to a selected geodesic graph or fixed directions. |
| No shape assumptions | No differentiability, strict convexity, or curvature is assumed | Same scope. |

Covered: the entire row. Not claimed by this theorem: atom-bearing laws, higher dimensions, dependent edge weights, or removal of the minimum-second-moment assumption. None of those extensions is part of T022.

## 2. Strict convexity and differentiability of the planar exponential first-passage limit shape

Author as printed: OpenAI. Date as printed: September 24, 2026.

[Manuscript](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf); [main theorem source](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex); [consequences](https://github.com/openai/math/blob/main/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/consequences.tex). Local extracts: [source2.tex](source2.tex), [source3.tex](source3.tex).

Theorems 1.1 and 1.2, copied verbatim as LaTeX:

```tex
\begin{theorem}[The exponential limit shape]
\label{thm:exponential-shape}
For independent exponential edge weights of any rate $\lambda>0$,
the norm $\mu$ is Fr\'echet differentiable on $\R^2\setminus\{0\}$,
and its unit ball is strictly convex. In particular,
\[
 \mu((1-t)x+ty)<1
 \quad\text{if }x,y\in\partial\Bcal,\ x\ne y,\ 0<t<1,
\]
and $\partial\Bcal$ is a $C^1$ curve with a unique supporting line
at every point.
\end{theorem}
```

```tex
\begin{theorem}[Differentiability for Gamma weights]
\label{thm:gamma-differentiability}
For independent Gamma edge weights with any fixed shape $\kappa>0$
and rate $\lambda>0$, the norm $\mu$ is Fr\'echet differentiable at
every nonzero vector, and $\partial\Bcal$ is a $C^1$ curve.
\end{theorem}
```

Comparison: the graph and minimizing model are the same undirected nearest-neighbor FPP on Z^2. The exponential and Gamma laws are special cases of our atomless nonnegative laws; their minimum-of-four second moment is finite. The quantity in these main theorems is the deterministic limit-shape norm and boundary, rather than the existence of a random two-sided geodesic. Strict convexity is claimed for exponential laws only; differentiability is claimed for every positive Gamma shape and rate, without a general-law claim.

Its geodesic consequence fixes a deterministic direction u before choosing the probability-one event and excludes bigeodesics with an end in that direction, for exponential weights. The text expressly says this does not assert simultaneous absence of all bigeodesics. A separate paragraph obtains simultaneous absence for Gamma laws by citing Theorem 1.1 of the first candidate. That paragraph depends on the first paper; it is not a separate proof of T022. Therefore this candidate supplies related restricted-law shape and directional claims, not the whole row on its own.

## 3. Cylinder loop weights and planar nesting

Author as printed: OpenAI. Date as printed: September 26, 2026.

[Manuscript](https://github.com/openai/math/blob/main/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/main.pdf); [main theorem source](https://github.com/openai/math/blob/main/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/build/sections/00_introduction.tex). Local extract: [source4.tex](source4.tex).

Theorem 1.1, copied verbatim as LaTeX:

```tex
\begin{theorem}[Cylinder fugacity exponent]
\label{thm:04-cylinder-exponent}\label{E:cylinder-exponent}
For every fixed $\chi>0$, along even $N$,
\[
 Z_N(\chi)=N^{\tau(\chi)+o(1)},\qquad
 \tau(\chi)=
 \begin{cases}
 \displaystyle\frac16-\frac{2}{3\pi^2}
              \bigl(\arccos(\chi/2)\bigr)^2,&0<\chi\le2,\\[4pt]
 \displaystyle\frac16+\frac{2}{3\pi^2}
              \bigl(\operatorname{arcosh}(\chi/2)\bigr)^2,&\chi\ge2.
 \end{cases}
\]
\end{theorem}
```

Here rho=1/sqrt(2+sqrt(2)) is a fixed critical activity, and Z_N(chi) sums products of chi*rho^{|P|} over finite families of vertex-disjoint honeycomb polygons separating two prescribed markers on a balanced cylinder; N is even. It further asserts planar nesting mass P_chi(r)=r^{tau(chi)/2+o(1)}, with cylinder exponent 1/6 and planar/middle-strip nesting exponent 1/12 at fugacity two.

Comparison: this uses the honeycomb lattice and its cylindrical quotient, not the square-lattice iid random metric. Its weights are deterministic polygon activities and loop fugacities, not independent edge passage times. Its quantity is an asymptotic partition-function exponent, not an almost-sure existence statement for two-sided minimizing paths. Planarity and the word “weights” are the overlap. This candidate is NOT-THIS for T022.

## Follow-ups and formalisation

The [release README](https://github.com/openai/math/blob/main/README.md) describes manuscripts at different verification stages and possible issues in unformalized results. The [release history](https://github.com/openai/math/blob/main/history.md), opened in full, records no correction or withdrawal naming these three papers; its latest displayed entry was October 29, 2026. Each manuscript README was also opened; all retain the supplied September dates and contain no revision or withdrawal notice.

The [family 212 Lean scope document](https://github.com/openai/math/blob/main/lean/docs/212.md) links only the shape paper. It describes Gamma/exponential differentiability and C^1 boundary, expressly excludes exponential strict convexity from the selected statements, and identifies no no-bigeodesics formalisation. The [formalisation index](https://github.com/openai/math/blob/main/lean/formalization.yaml), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), and [comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md) were opened; further comparator checks and follow-up searches are recorded below. No Lean build was run.

The [Proofweave family 212 record](https://proofweave.org/publications/openai-math/212), indexed October 13, 2026 at source snapshot 1581d4cbdd69a0faf34b2089614fe2a814316a6a, identifies no formalisation coverage for the no-bigeodesics manuscript, no reviewed explanation, and a pending platform replay. This is a catalogue status, not a referee assessment.

### Later literature and public checks actually opened

| Source opened | Date/version stated there | What it adds |
| --- | --- | --- |
| [MathVet original fidelity table](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv), family 212 | Pinned revision 14c7f918cd336d0da03a02aae5a0eed4a429d4db | Reports sandboxed Comparator acceptance for GammaPassage and PlanarFirstPassage, but only partial coverage: the no-bigeodesics theorem and exponential strict convexity are absent from these targets. Actual CSV content was read, not only the GitHub wrapper. |
| [cert-machine original statements audit](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json), family 212 | Pinned revision 9814e4c06281e34a113ce853d7d99ccce160b750 | Its scope assessment is narrower/unlinked: no challenge states the bigeodesic claim. Actual JSON content was read. |
| [Plectis Atlas, family 212](https://wcook04.github.io/plectis-atlas/families/212.html) | Reports MathVet run October 8 and cert-machine run October 10, 2026 | Links the above primary audits and reports both differentiability targets accepted, including a cert-machine run using nanoda. The Atlas did not rerun them; this verification did not rerun them either. These passes do not cover T022. |
| [AI Proved What?, episode 212](https://aiprovedwhat.com/episodes/212-planar-first-passage-geometry-absence/) | Original October 17; remake October 22; status checked November 9, 2026 | Exposition distinguishing full bigeodesic claim from restricted Lean coverage. It reports neither FPP manuscript revised, no expert reaction found, and neither among OSVerify-reviewed papers. This is its stated search result, not evidence of universal absence of discussion. |
| [Orply exposition](https://orply.com/articles/perplexity/212-1-no-bigeodesics-in-planar-first-passage-percolation-23ca1170) | Post-release exposition; no exact publication date relied upon | Restates the claimed all-directions theorem with its moment condition; no independent proof validation identified. |
| [MathDB problem discussion](https://mathdb.com/p/331958/furstenberg-kesten-conjecture-on-bigeodesics-in-two-dimensio) and [Myeongjin Kang's manuscript abstract](https://mathdb.com/abs/2610.00759), plus its [Zenodo record](https://zenodo.org/records/23647122) | October 25, 2026, version 1 | *Removing the moment assumption from a stipulated planar no-bigeodesics theorem*, author exactly Myeongjin Kang. Its abstract expressly assumes the pinned OpenAI theorem and specified proof inputs; it proposes an extension to the infinite-minimum-second-moment class, not an independent validation of T022. Full PDF retrieval failed on both Zenodo routes; only the actual abstract and repository record were readable, so no judgment of its proof is made. This MathDB identifier is not an arXiv identifier. |
| [OSVerify cylinder case report](https://osverify.github.io/cases/cylinder-loop-weights-and-planar-nesting.html) and [index](https://osverify.github.io/case-studies.html) | Reviewed manuscript dated September 26, 2026; review publication date not shown | Reports a missing bounded bulk term in a global kernel estimate in Lemma 3.9, Section 3.6, p. 40; proposes replacing C/d(s) by C(1+1/d(s)), with the existing L2 term absorbing the correction. The individual page labels it Major; the index/search displayed Minor. This concerns the unrelated honeycomb paper and does not refute T022. |

The actual [PlanarFirstPassage target](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PlanarFirstPassage.lean) uses rate-one exponential iid weights and asserts time-constant norm differentiability and C1 charts; [GammaPassage](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/GammaPassage.lean) ranges over all positive Gamma shapes and rates. Neither states a bigeodesic exclusion. Rate-one versus arbitrary rate in the exponential target causes no obstruction for differentiability, since Gamma shape one includes every positive rate. Both target files and their JSON configs were opened and saved locally. The `sorry` tokens belong to the challenge statements, not to an inspected purported proof: the configs select separate solution modules, whose final theorem bodies were also opened ([BoundaryCurve.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean), [Differentiability.lean](https://github.com/openai/math/blob/main/lean/OAI/Probability/GammaPassage/Differentiability.lean)). No full dependency audit or local kernel replay was attempted.

Searches used the web search tool with each exact title, with arXiv/site:arxiv.org, and with OpenAI plus error, gap, and refutation. No post-release arXiv version of these three papers, no referee report validating the no-bigeodesics argument, and no specific refutation of that argument were found in those searches. This is a bounded negative search result. The cylinder report and the narrower Lean checks are affirmative findings and are recorded separately above.

The community-corrections pages for [the no-bigeodesics manuscript](https://mathcommunity.github.io/oai-math-revised/papers/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/) (updated November 4) and [the shape manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/) (updated November 9) were also opened. Both show no contributed notes; their automatically collected notes are marked unreviewed. They report October 26 Comparator acceptance for both differentiability targets and explicitly describe the narrower formalisation scope. Their family-level Lean badges therefore provide no additional evidence for the no-bigeodesics theorem. The linked run logs were not independently replayed here.

For completeness, the searches also led to and opened the older arXiv pages [Michael Damron and Jack Hanson, *Bigeodesics in first-passage percolation*, 1512.00804v2](https://arxiv.org/html/1512.00804v2), [Barbara Dembin, Dor Elboim and Ron Peled, *Coalescence of geodesics and the BKS midpoint problem in planar first-passage percolation*, 2204.02332](https://arxiv.org/html/2204.02332), and [Gerandy Brito, Michael Damron and Jack Hanson, *Absence of backward infinite paths for first-passage percolation in arbitrary dimension*, 2003.03367](https://arxiv.org/abs/2003.03367). These are prior literature, not later versions of the release. No new status conclusion is based on unopened historical papers named in our original note.

## Recommended replacement for “where it stands”

OpenAI’s preprint *No bigeodesics in planar first-passage percolation* (September 24, 2026) claims the full statement, with the same minimum-of-four second moment and no assumptions on the limit shape. Treat this as an unrefereed claimed solution: the release’s documented Lean coverage does not include the no-bigeodesics theorem, and no independent validation of that theorem was found in the sources checked.


## Spot check

The main step selected for checking is Lemma 4.4, *Half-plane transfer* (`lem:cut-transfer`), in [the actual source](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/04-exceptional.tex); saved in [exceptional.tex](exceptional.tex). It is central to the all-directions claim: it moves rays at environment-dependent exceptional labels into one environment while retaining opposite rays in an independent environment, so that fixed-label coalescence can be used without intersecting uncountably many probability-one events.

The claim is that a deterministic subsequence of increasingly deep cuts preserves any finite collection of upper rays, their exact labels and any finite set of Busemann evaluations; for each fixed cut it also preserves tails and labels of all lower rays in the complementary resampling.

The proof's barrier calculation was checked as follows. Write B(0,w)=rho(w)+a(w), with a(w)=o(|w|). For an upper label whose contact directions are strictly above the horizontal, compactness gives gamma>0 with m(d)-rho(d)>=gamma|d| for every downward displacement d. For a fixed finite set of starting points and z on the cut at height -n, |z-x| is comparable to |x|+|z|+n. Thus the claimed uniform metric error and the two Busemann errors are smaller than half of the linear gap at sufficiently deep subsequence cuts, giving T_V(x,z)-B(x,z)>=gamma|z-x|/2. The signs in this inequality agree with B(x,z)=rho(z-x)+a(z)-a(x).

For a competitor from x to p_j touching the cut, its last cut vertex z splits it into a prefix costing at least T_V(x,z) and an unchanged suffix costing at least B(z,p_j). Additivity therefore makes it strictly more expensive than the unchanged geodesic once the calibration defect T_U(x,p_j)-B(x,p_j) tends to zero. This establishes eventual equality of the relevant distances, not just a small relative error. For x=p_0 the defect is already zero, preserving the ray.

The moving-metric subsequence is legitimate conditional on the uniform metric input: E_n(T)=sup_{x,y}|T(x,y)-m(y-x)|/(|x|+|y|+n) tends to zero in each fixed typical metric. Because every V_n has the same iid marginal law, E_n(T_Vn) tends to zero in probability; a deterministic subsequence with summable failure probabilities then works by Borel--Cantelli. Independence between different cuts is unnecessary. Equality of Busemann values in an upper sector is then tested along ke_2 and k(e_1+e_2), identifying both label coordinates; merely preserving a single path would not have sufficed. The lower-tail proof uses a fixed complementary metric and the reversed barrier, with no convergence rate in n required. The retained U-edge sets in V_n and W_n are disjoint, so this pair is indeed independent.

The uniform metric citation was checked directly in Daniel Ahlberg and Christopher Hoffman, *Random coalescing geodesics in first-passage percolation*, [arXiv:1609.02447v2](https://arxiv.org/abs/1609.02447v2), revised July 18, 2019: Assumption A1, printed p. 7, permits exactly the iid continuous/minimum-of-four second moment; Proposition 3.4, printed p. 9, supplies the two-endpoint estimate used in [the preprint's preliminaries](https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/02-preliminaries.tex). Its conversion to an error o(|x|+|y|) follows by taking the larger endpoint as the basepoint.

No specific error was found in this barrier-and-transfer argument, conditional on the stated simultaneous all-ray Busemann asymptotics and sector geometry. Those structural inputs (including the appendix's replacement of a boundary-expectation argument), exceptional-label countability, the fork argument, label budget and perturbation construction have not been fully audited here. This spot check therefore gives no verdict on correctness of the full preprint.
