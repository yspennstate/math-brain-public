# T123 verification

Checked 14 November 2026. The release **claims the whole statement** in T123. This verdict concerns the scope of the claim, not the correctness of the proof.

## Recommended “where it stands” sentence

OpenAI's preprint *Nonuniqueness of percolation on nonamenable quasi-transitive graphs*, dated September 24, 2026, claims the triangle condition and mean-field critical exponents for Bernoulli bond percolation on every connected, locally finite, quasi-transitive nonamenable graph, through a stronger bound on the critical connection operator. Accompanying Lean statements and proofs are supplied, and MathVet reports a Comparator pass, but no refereed verification or detailed independent expert assessment of the complete argument was found in this search.

## 1. Nonuniqueness of percolation on nonamenable quasi-transitive graphs

Author: **OpenAI**. Date: **September 24, 2026**, printed in the [original main TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/main.tex). Opened the original TeX and the [actual 53-page PDF on the Mathcommunity mirror](https://mathcommunity.github.io/oai-math-revised/papers/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf). The supplied GitHub folder did not render; raw GitHub PDFs were rejected by the parser as application/octet-stream.

Theorem 1.1 (printed p. 3), copied exactly from the [original introduction TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/sections/introduction.tex), retaining its macros:

~~~tex
\begin{theorem}\label{thm:main}
Let $G$ be an infinite connected locally finite quasi-transitive graph
with $h_V(G)>0$. For Bernoulli bond percolation on $G$,
\[
 \sup_{0\le p<\pc}\norm{T_p}_{2\to2}
       =\norm{T_{\pc}}_{2\to2}<\infty,
 \qquad \pc(G)<\ptwo(G)\le\pu(G).
\]
There exist $\pc<p_1<p_2<1$ such that, in the coupling obtained from
independent uniform edge labels, almost surely there are infinitely
many infinite open clusters simultaneously for every $p\in[p_1,p_2]$.
\end{theorem}
~~~

Here \(\pc=p_c\), \(\ptwo=p_{2\to2}\), \(\pu=p_u\), and \(\norm{\cdot}\) is the norm. The connection kernel is \(T_p(x,y)=\mathbb P_p(x\leftrightarrow y)\), acting on counting-measure \(\ell^2(V)\). The constant \(h_V\) is the infimum of outer vertex-boundary size divided by finite nonempty set size.

Corollary 1.3, “Critical laws and exponential connectivity” (printed p. 6; same original introduction), explicitly states, for every vertex \(v\),
\[
\nabla_{p_c}(v)\le\|T_{p_c}\|_{2\to2}^{3}<\infty,
\qquad
\chi_v(p)\asymp(p_c-p)^{-1},
\qquad
\theta_v(p)\asymp p-p_c,
\qquad
\mathbb P_{p_c}(|C_v|\ge n)\asymp n^{-1/2}.
\]
The limits are respectively \(p\uparrow p_c\), \(p\downarrow p_c\), and \(n\to\infty\). It also gives intrinsic and extrinsic radius tails of order \(n^{-1}\) and exponential connectivity below \(p_{2\to2}\). The [original consequences section](https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/sections/consequences.tex) explains the deductions from the operator theorem and earlier conditional results.

### Comparison with our statement

| Our wording | Preprint statement | Comparison |
|---|---|---|
| Bernoulli bond percolation | Independent open edge bits of common parameter \(p\) | Same model; \(T_p=\tau_p\) |
| Connected, locally finite | Infinite connected locally finite undirected graph | Same relevant range: a nonamenable graph here is infinite |
| Quasi-transitive | Finitely many vertex orbits | Same, not restricted to transitive graphs |
| Nonamenable | \(h_V(G)>0\) | Equivalent here: quasi-transitivity and local finiteness give bounded degrees, so vertex and edge isoperimetry are equivalent |
| Triangle sum at \(p_c\) | \(\nabla_{p_c}(o)=\sum_{x,y}T_{p_c}(o,x)T_{p_c}(x,y)T_{p_c}(y,o)<\infty\) for every root | Exactly the requested sum and endpoint; operator boundedness is a stronger sufficient condition |
| \(\beta=\gamma=1,\ \delta=2\) | Two-sided order-parameter, susceptibility and cluster-volume-tail bounds | Same exponent claims; \(\delta\) is expressed by the tail \(n^{-1/\delta}\) |
| Every graph in the class | All such graphs, explicitly including every prescribed finite symmetric Cayley generating set | No hyperbolicity, girth, large-expansion, unimodularity, or chosen-generators exception |
| Dimension/range | No dimension restriction; critical and one-sided near-critical limits | Same requested range |

The \(\asymp\) statements give positive finite upper and lower comparison constants, allowed to depend on the graph and root. They do not assert an asymptotic equivalent with a limiting amplitude. Our row asks for exponent values, so this distinction leaves none of our stated claim uncovered. The theorem does not cover arbitrary non-quasi-transitive graphs or dependent percolation.

Section 10 (printed p. 49) explicitly identifies
\[
\nabla_{p_c}(o)=\langle\delta_o,T_{p_c}^{3}\delta_o\rangle
\le\|T_{p_c}\|_{2\to2}^{3}.
\]
Thus reading only \(p_c<p_u\) from the title would miss the claimed resolution of T123.

## 2. No percolation at criticality on quasi-transitive graphs

Author: **OpenAI**. Date: **September 24, 2026**, printed in [main TeX](https://raw.githubusercontent.com/openai/math/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/main.tex). Opened the [actual 42-page PDF](https://mathcommunity.github.io/oai-math-revised/papers/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf).

Theorem 1.1 (printed p. 2), copied exactly from the [original introduction TeX](https://raw.githubusercontent.com/openai/math/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/build/sections/introduction.tex), and checked against the PDF:

~~~tex
\begin{theorem}
\label{thm:main}
Let $G$ be an infinite connected locally finite quasi-transitive
undirected graph. If $\pc(G)<1$, then
\[
 \PP_{\pc(G)}(\text{there is an infinite open cluster})=0.
\]
Equivalently, $\PP_{\pc(G)}(|C_x|=\infty)=0$ for every vertex $x$.
\end{theorem}
~~~

Same bond model, and a graph class containing our nonamenable quasi-transitive class, which has \(p_c<1\). Its conclusion is only critical nonpercolation, equivalently \(\theta_x(p_c)=0\), without the triangle sum or exponent bounds. The larger graph class does not compensate for the weaker conclusion. It covers the continuity assertion in our background note but does not settle quantitative T123.

## 3. Critical bond and site percolation on the cubic lattice

Author: **OpenAI**. Date: **September 24, 2026**, printed on p. 1 of the [actual 20-page PDF](https://mathcommunity.github.io/oai-math-revised/papers/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf), which was opened. The [original README](https://raw.githubusercontent.com/openai/math/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md) agrees.

Theorem 1.1 (printed p. 1), copied exactly from the PDF, normalizing line breaks and the typography of \(\mathbb Z^3\):

> For nearest-neighbor Bernoulli bond percolation on \(\mathbb Z^3\), there is almost surely no infinite open cluster at the bond critical parameter. The same assertion holds for nearest-neighbor Bernoulli site percolation at the site critical parameter.

The graph is the three-dimensional nearest-neighbor cubic lattice, which is amenable and outside our nonamenable graph class. Its bond half shares our model; its site half uses independent vertex bits and a separate critical probability. The theorem gives critical nonpercolation without a triangle condition or mean-field exponents. This candidate is not T123, even as a special case of the row's nonamenable range.

## Follow-ups and formalization

### Repository materials opened

- [Repository README](https://raw.githubusercontent.com/openai/math/main/README.md) and [history](https://raw.githubusercontent.com/openai/math/main/history.md): the release presents model-produced research outputs. The available history lists changes through 29 October, with no named withdrawal or correction of these percolation papers.
- [Lean scope note 214](https://raw.githubusercontent.com/openai/math/main/lean/docs/214.md): explicitly includes the operator gap, coupled nonuniqueness interval, arbitrary-generating-set Cayley case, finite triangle diagram, and selected mean-field laws.
- [Family-214 Comparator specification](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/BenjaminiSchramm.lean), [configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/BenjaminiSchramm.json), and [solution Main.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/BenjaminiSchramm/Main.lean): selected declarations are full_main, cayley_main and critical_laws. Read the specification's definitions of the actual Bernoulli law, connection kernel, counting-measure Hilbert space, nonnegative extended-real triangle sum, and two-sided exponent laws. They express the requested quantities. The solution invokes imported proved inputs; the complete dependency tree was not audited.
- [Lean scope note 213](https://raw.githubusercontent.com/openai/math/main/lean/docs/213.md), [CriticalPercolation configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalPercolation.json), [its solution](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/CriticalPercolation/Main.lean), [CriticalZ3 configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/CriticalZ3.json), and [its solution](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/CriticalZ3/Main.lean): these address the two critical-nonpercolation statements.
- [Lean README](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), and [checking instructions](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md). Missing exact titles in the catalogue do not show absence of formalization: separate scope notes and Comparator files exist. Intentional sorry placeholders in Comparator specifications are separate from the supplied solutions. No local Lean replay was run.

### External checks and expert comments

- [MathVet's original fidelity table](https://raw.githubusercontent.com/mathvet/mathvet/main/reviews/openai-math/fidelity-table.csv), rows 213 and 214, records full statement fidelity and comparator-sandboxed-pass; row 214 explicitly includes the triangle and mean-field conclusions. The [review README](https://raw.githubusercontent.com/mathvet/mathvet/main/reviews/openai-math/README.md) describes a pre-referee third-party review and says second-reader and referee fields await the referee round. These are reported automated checks and preliminary scope assessments, not refereed certification. The table links release revision 4eaee87548250b2682affda7d05d947c05554bae, whereas the review README header still names the earlier adc7f124 snapshot; the available metadata are not a single synchronized revision.
- [Proofs and Prompts, “100+ reactions to 100+ solutions”](https://proofsandprompts.com/2026/10/08/100-reactions-to-100-solutions/), published 8 October: read the comments attributed to **Tasmin Chu** and **Inhyeok Choi**. Both discuss nonuniqueness; Choi gives a favorable initial impression while indicating a wish to understand the details. Neither passage supplies a detailed proof audit.
- **Olle Häggström**, [“What I write about the day after the most earth-shattering event in the history of mathematics”](https://haggstrom.substack.com/p/what-i-write-about-the-day-after), 7 October: opened the original post. It points to percolation claims without providing a detailed assessment of their proofs.
- Opened the Mathcommunity [nonuniqueness](https://mathcommunity.github.io/oai-math-revised/papers/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/), [general criticality](https://mathcommunity.github.io/oai-math-revised/papers/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/), and [cubic](https://mathcommunity.github.io/oai-math-revised/papers/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/) pages as discovery aids. Their collected notes are explicitly AI-generated and unreviewed. The [Latent Seminar exposition](https://lowrank.github.io/latent-seminar/openAI/214-nonamenable-percolation) opened with no readable content, so no mathematical assessment is attributed to it.

### Later research opened

- **Yan Ru Pei**, [*Nonuniqueness of site percolation on nonamenable quasi-transitive graphs*](https://hexagonmath.org/pdf/2611.00251v1), November 2026, Hexagon 2611.00251v1. Opened the actual 60-page paper and its [landing page](https://hexagonmath.org/2611.00251v1), whose displayed version date is 10 November. It claims a site version and explicitly adapts the OpenAI argument. The landing page says it relies on unrefereed inputs and has no formal verification. It is a follow-up claim, not independent confirmation of the bond proof. Its version-history prose also contains November 9; this discrepancy is not resolved by assumption.
- **Omer Angel, Daniel de la Riva, Christoforos Panagiotis, Yuliang Shi**, [*Continuity of the phase transition for long-range Bernoulli percolation with exponential decay on \(\mathbb Z^2\)*](https://arxiv.org/abs/2610.35233), arXiv:2610.35233v1, 26 October 2026. Opened the arXiv page and [full HTML](https://arxiv.org/html/2610.35233v1). Section 1.2 describes the general quasi-transitive criticality result as an OpenAI claim. Its own theorem concerns long-range percolation and gives no review of the nonamenable triangle theorem. It is not an arXiv version of an OpenAI manuscript.

Exact-title searches combined with arxiv, error, gap and review, and a search for “OpenAI nonamenable triangle percolation”, found no identifiable arXiv version of these OpenAI papers and no specific refutation or error report for the nonuniqueness theorem. The community issue search did not load, so the issue archive was not exhaustively inspected. No refereed verification of the complete argument was found. These are bounded search findings, not assertions that no correction or review exists anywhere.

### Independent comparison with the existing problem

Opened **Tom Hutchcroft**, [*The \(L^2\) boundedness condition in nonamenable percolation*](https://arxiv.org/abs/1904.05804), arXiv:1904.05804v2, revised 23 September 2020, and its [full HTML](https://arxiv.org/html/1904.05804). Section 1 states the operator conjecture and the triangle/mean-field consequences in the quasi-transitive setting. This is prior literature supporting the comparison, not a later endorsement. No paper is cited here solely from another paper's bibliography.

## Spot check

Selected **Lemma 7.7, “Two distinct exterior clusters”**, printed pp. 39–40 of the nonuniqueness PDF, with its original proof in [sections/deformation.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/sections/deformation.tex), lines 249–294. This is a central input to Proposition 7.5: it produces the product of deformed susceptibilities that drives the later differential inequality.

With \(T_0=T_p\), \(\chi_0^+=\sup_x\mathbb E_p|C_x|\), and \(p_c/2\le p<p_c\), the lemma claims
\[
\mathbb E_p[X_t^D(u)X_t^D(v);C_u^D\ne C_v^D]
\ge s_t^D(u)s_t^D(v)-C'(\chi_0^+)^2T_0^3(u,v),
\qquad C'=1+2d/p_c.
\]

The delicate step is conditioning on \(A=C_u^D\). It is finite in this subcritical range. Exposing its internal bits and closed boundary leaves bits with both endpoints outside \(A\) independent with parameter \(p\). A template's domain eligibility uses its retained path, permits raw excursions outside the domain, and keeps its full-graph weight fixed. These conventions make \(X_t^D(u)\) determined by this exposure, and leave weighted connections in a different cluster unchanged when \(A\) is deleted. Hence
\[
\mathbb E_p[X_t^D(u)X_t^D(v);C_u^D\ne C_v^D]
=\mathbb E_p[X_t^D(u)s_t^{D\setminus A}(v)].
\]
For \(v\in A\), both sides' corresponding contribution is zero.

The deletion estimate used next includes the full-graph neighbor set \(\operatorname{Nb}[A]\), not just \(A\). A lost connection or bypass visits \(A\); deleting an open blocker attached to a surviving corridor instead forces a visit to its surviving attachment vertex in \(\operatorname{Nb}[A]\). Splitting a simple visiting path gives edge-disjoint connection witnesses. Thus BK bounds the loss by \(\chi_0^+\sum_{z\in\operatorname{Nb}[A]}T_0(v,z)\), as required.

The error calculation can be re-derived directly. For neighbors \(a,z\), Harris association gives \(pT_0(v,z)\le T_0(v,a)\), and therefore
\[
\sum_{z\in\operatorname{Nb}[A]}T_0(v,z)
\le(1+d/p)\sum_{a\in A}T_0(v,a).
\]
Also \(X_t^D(u)\le|A|\). A tree connecting \(u,a,y\) has a branching vertex with three edge-disjoint legs, so union bound and BK give
\[
\mathbb E_p[|A|\mathbf1_{\{a\in A\}}]
=\sum_y\mathbb P_p(u\leftrightarrow a,\ u\leftrightarrow y\text{ in }D)
\le \chi_0^+T_0^2(u,a).
\]
Repeated terminals permit zero-length legs. Substitution yields error at most
\[
(1+d/p)(\chi_0^+)^2
\sum_a T_0^2(u,a)T_0(a,v)
=(1+d/p)(\chi_0^+)^2T_0^3(u,v).
\]
Finally \(1+d/p\le1+2d/p_c\) has the correct direction and no dependence on the domain, template length, or deformation time. Nonnegative sums permit Tonelli; subcritical susceptibility and the tree estimate supply the required moments.

No discrepancy was found in this local conditioning argument and error calculation. This does not validate the earlier amplification/subpower estimates, later path-selection argument, complete paper, or Lean dependency tree.

## Sources and access record

All three main preprints were read as PDFs through the Mathcommunity mirror. The first two main statements were also read in original GitHub TeX. The Atlas renderings of nonuniqueness and the cubic paper were opened, but their theorem numbering can differ; the numbering above is from the PDFs. The repository's [Apache-2.0 license](https://raw.githubusercontent.com/openai/math/main/LICENSE) was opened; the theorem excerpts above retain OpenAI attribution.

Failed requests included the supplied folder pages, guessed paper.tex and build/paper.tex files, raw-PDF parsing, cubic TeX filename guesses, a GitHub API listing, the community issue search, and some PDF screenshots. Successful alternatives and the access limits are recorded in LOG.md.

Task: “Verify: has open problem T123 been settled by the OpenAI math release?” — 14 November 2026, 21:06 Asia/Tbilisi.
