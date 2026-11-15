# T425: the second Kahn–Kalai conjecture

Checked 14 November 2026. Recommended classification: **SOLVED-CLAIMED** for the whole row. This records a full proof claim; it does not certify the proof.

## Candidate 1: The second Kahn–Kalai conjecture

OpenAI, September 24, 2026. Opened the actual TeX main file and all four sections, rather than relying on the title or catalogue. The main theorem is Theorem 1.1. Exact source quotation follows; the paper defines `\pc` as `p_{\mathrm c}`, `\pE` as `p_{\mathrm E}`, and `\ee` as the base of the natural logarithm.

```tex
\begin{theorem}\label{thm:main}
For every $n\ge2$ and every finite simple graph $H$ with $h=e(H)\ge1$
edges and at most $n$ vertices,
\begin{equation}\label{eq:stronger}
 \pc(n,H)\le
 \min\{1,\;2048\ee^{50}\pE(n,H)(1+\log_2 h)\}.
\end{equation}
In particular,
\[
 \pc(n,H)\le6144\ee^{50}\pE(n,H)\log_2 n.
\]
\end{theorem}
```

[Main file](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/build/source/main.tex), [theorem and definitions](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/build/source/sections/introduction.tex), [PDF](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf). Sources are also saved locally under sources/.

### Comparison with our statement

| Our words | Paper's statement and definitions | Consequence |
| --- | --- | --- |
| Simple graph H=H(n), at most n vertices | Every finite simple H with at most n vertices, all n≥2; explicitly allows H to vary with n | Same full range; no fixed-H, degree, density, or spanning restriction |
| G(n,p) | Independent edges on [n], probability p for each unordered pair | Same model; no directed graph, hypergraph, or higher dimension |
| Contains H | Ordinary copies; extra edges are allowed | Same non-induced containment event |
| Least p with containment probability ≥1/2 | Infimum over [0,1] of precisely that event; paper explains attainment | Same p_c |
| Expected unlabelled copies | N(G,F) counts subgraphs isomorphic to F; Section 4 gives N(K_n,F)=(n)_{v(F)}/|Aut(F)| for F without isolates | Same count, not labelled embeddings |
| Every nonempty edge-induced F⊆H | Every subgraph F⊆H, including subgraphs with isolated vertices | Same effective threshold; explanation below |
| Expectation at least 1/2 | Exactly 1/2 for every F | Same normalization |
| Original p_E | Constraint is E N(G(n,p),F)≥1/2 | No N(H,F) multiplicity factor and no substituted fractional threshold |
| C p_E log(2+e(H)) | Explicit universal 2048 exp(50), times p_E(1+log₂ e(H)), capped at 1 | Same strength up to a universal constant, for all finite n; not merely an asymptotic or special case |

Here “edge-induced” means a subset of edges on its incident vertices, as in the row's ordinary subgraph expectation threshold. For a nonempty edge graph F₀ on v vertices, adjoining t isolated vertices multiplies its expected number of ordinary unlabelled copies by binom(n−v,t)≥1 whenever v+t≤n. Thus the extra isolated-vertex subgraphs impose no stronger constraint. Edgeless subgraphs have deterministic copy count binom(n,t)≥1. These facts explain why the paper's “every subgraph” gives exactly our p_E. Isolated vertices of H also do not affect containment when |V(H)|≤n.

Writing h=e(H)≥1 and using natural logs,

\[
1+\log_2 h=\frac{\log(2h)}{\log 2}
\le\frac{2}{\log 2}\log(2+h).
\]

The last inequality follows from 2h≤(h+2)². Hence the paper claims our inequality with, for example, C=4096 exp(50)/log 2. The extra log₂ n corollary is weaker than the edge-count assertion and is not needed for the row. If H is edgeless, p_c=0 and the row is trivial, interpreting its empty set of edge constraints as p_E=0; the theorem's h≥1 restriction loses no substantive case.

The paper explicitly distinguishes the modified threshold from the original one in Section 1. Its modified constraint is E N(G(n,p),F)≥N(H,F)/2, while Theorem 1.1 uses 1/2. Thus it claims precisely the step missing from our earlier note.

## Candidate 2: A counterexample to Tachikawa's second conjecture

OpenAI, September 23, 2026. Theorem 1.1, copied exactly from the actual introduction source:

```tex
\begin{theorem}\label{thm:main}
Let
\[
 k=\mathbb F_2(q,H_1,H_2),
\]
where $q,H_1,H_2$ are algebraically independent.
There exist a finite-dimensional associative unital symmetric
$k$-algebra $A$ and a finite-dimensional unital left $A$-module $M$
such that $M$ is nonprojective and
\[
 \Ext_A^i(M,M)=0\qquad\text{for every integer }i>0.
\]
In particular, Tachikawa's second conjecture is false.
\end{theorem}
```

[Paper main file](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/paper.tex), [theorem source](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/sections/introduction.tex), [PDF](https://github.com/openai/math/blob/main/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf).

**NOT-THIS.** This is an existence statement about a finite-dimensional symmetric algebra and a nonprojective self-orthogonal module over a particular characteristic-two rational function field. Its quantities are positive-degree Ext groups, not p_c, p_E, or a graph-copy count. It covers no part of T425 and neither proves nor refutes its inequality.

## Candidate 3: A proof of Seymour's second-neighborhood conjecture

OpenAI, September 23, 2026. Theorem 1.1, copied exactly from the actual introduction source; `\abs` denotes absolute cardinality:

```tex
\begin{theorem}\label{thm:main}
Every nonempty finite oriented graph has a vertex \(v\) such that
\[
 \abs{N_1^+(v)}\leq \abs{N_2^+(v)}.
\]
\end{theorem}
```

[Paper main file](https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/main.tex), [theorem source](https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/build/source/00-introduction.tex), [PDF](https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf).

**NOT-THIS.** This concerns every nonempty finite oriented graph and compares the numbers of first and exact-distance-two out-neighbors of a vertex. It is deterministic and directed. There is no G(n,p), no containment threshold, no expectation threshold, and no logarithmic comparison. It covers no part of T425.

## Follow-ups and formalisation

### Primary repository material opened

- [Manuscript README](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/README.md) has the title, OpenAI authorship, date, and citation, with no withdrawal notice. [history.md](https://github.com/openai/math/blob/main/history.md), opened in full, records updates through October 29, 2026; no correction or withdrawal of this paper appears there. Absence from that file does not establish absence of errors.
- [Family 176 scope note](https://github.com/openai/math/blob/main/lean/docs/176.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), and [Lean README](https://github.com/openai/math/blob/main/lean/README.md) were opened. They identify the actual containment and expectation thresholds and both universal bounds.
- [Comparator challenge](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SecondKahnKalai.lean), [configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SecondKahnKalai.json), [solution Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GraphThreshold/Main.lean), and [ThresholdBounds.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/GraphThreshold/ThresholdBounds.lean) were opened and saved. The challenge defines independent Bernoulli weights on unordered non-loop edges, uses Mathlib `copyCount`, and quantifies over all `H.Subgraph`. Its theorem placeholder contains `sorry`, as expected for a Comparator challenge; the solution module supplies a proof. The permitted axioms in the configuration are `propext`, `Quot.sound`, and `Classical.choice`. The imported proof closure was not compiled or exhaustively audited here.
- For the two unrelated candidates, [family 173](https://github.com/openai/math/blob/main/lean/docs/173.md) describes the full Seymour assertion, and [family 199](https://github.com/openai/math/blob/main/lean/docs/199.md) describes the Tachikawa counterexample. The latter excludes its later field-extension and homological consequences from the formalisation scope. Neither changes T425.

### External evidence opened

- [MathVet fidelity table, frozen revision](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/fidelity-table.csv): the actual family 176 row says `full` and `comparator-sandboxed-pass`, with definitions of both thresholds matching the claim. Its [README](https://github.com/mathvet/mathvet/blob/main/README.md) calls the review pre-referee and explains that fidelity compares formal statements with headlines. This is an external reported machine check and scope assessment, not a specialist referee report.
- [Carlos Toledo's cert-machine statement report, frozen revision](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-statements.json): the actual family 176 row says `MATCHES`, records both clauses, and records no gap. This is a statement comparison report; it does not by itself establish proof correctness.
- [Plectis Atlas paper page](https://wcook04.github.io/plectis-atlas/papers/The-second-Kahn-Kalai-conjecture-September-24-2026.html) and [family 176 page](https://wcook04.github.io/plectis-atlas/families/176.html) were opened. They reproduce the result and aggregate external Comparator reports, including Neal McBurnett's. The latter report was not independently opened, so it is only an Atlas-reported lead here. Atlas warns that a machine proof and a faithful translation are separate questions.
- Shuchen Li and Ilias Zadik, [Functional inequalities from the fundamental limits of Bayesian estimation](https://arxiv.org/abs/2611.05831), submitted November 4, 2026: opened the arXiv record and [full HTML](https://arxiv.org/html/2611.05831v1). Section 1.1 describes OpenAI's second Kahn–Kalai proof as an announcement, mentions Bayesian resampling and Tran's decomposition, and cites the September 24 preprint. This is later mathematical commentary, not a proof verification or an arXiv version of the OpenAI paper. The nearby statement that the authors have not verified an OpenAI proof concerns the distinct logarithmic Sobolev claim in Section 1.2 and must not be misattributed to T425.

- The public repository acprk/openai-math-remarks contains an October 9, 2026 draft, [A remark on OpenAI family 176: the constant in the second Kahn–Kalai bound](https://github.com/acprk/openai-math-remarks/blob/main/remarks/R13-kahn-kalai-constant/note.tex). Opened the actual note.tex, its README, VERIFICATION.md, and the repository README. The author line is literally `[AUTHOR NAME]`; no named authorship is inferred. It claims a reduction of the constant to 10⁵ by changing numerical parameters. Its stated premise is the correctness of the original manuscript, and its checks are AI-assisted computations and reviews, with no human peer review or new Lean verification. It is a conditional follow-up, not independent confirmation of the full proof.

### Prior literature checked against the old note

Opened arXiv records for Elchanan Mossel, Jonathan Niles-Weed, Nike Sun, and Ilias Zadik, [On the Second Kahn--Kalai Conjecture](https://arxiv.org/abs/2209.03326) (September 7, 2022); Quentin Dubroff, Jeff Kahn, and Jinyoung Park, [On the “second” Kahn--Kalai Conjecture](https://arxiv.org/abs/2508.14269) (August 19, 2025); and Tuan Tran, [Fractional expectation thresholds and the “second” Kahn-Kalai conjecture](https://arxiv.org/abs/2609.20546) (September 17, 2026, revised September 24). Their opened records support the distinction in our note: the 2022 result uses the modified multiplicity threshold; the 2025 result has extra logarithmic losses; Tran's general fractional comparison retains a logarithmic loss, while giving the conjectured bound for specified classes. None is an arXiv version of the OpenAI manuscript, and none postdates its September 24 date in a way that supplies a later verification.

### Search coverage and negative findings

Used the web search tool for the exact title, OpenAI plus second Kahn–Kalai, arXiv, error, gap, refutation, and SecondKahnKalai/MathVet. Also searched the unrelated candidate titles with OpenAI/error and inspected their primary Lean scope notes. Read-only GitHub issue search `repo:openai/math "Kahn"` returned no issues. Search results alone were not treated as opened papers. No arXiv version of the OpenAI T425 paper, T425 refutation, withdrawal, error report, or specialist referee report was located in the opened sources. This is a bounded search result, not a claim that none exists.

The three supplied GitHub folder URLs initially failed in the web opener, but the read-only GitHub connector opened each folder and its actual TeX sources. The raw T425 PDF failed in the web tool because it was served as application/octet-stream; the complete TeX paper was readable and used instead. No Lean build was run.

## Recommended new “where it stands” sentence

OpenAI's preprint “The second Kahn–Kalai conjecture” (September 24, 2026) claims the full bound for the original unlabelled-copy expectation threshold, for every simple graph H with at most n vertices. A Lean formalisation and external reports of a matching statement and a successful Comparator check are available. Record this as SOLVED-CLAIMED; no specialist referee report or refutation was found in the sources checked.

## Spot check

The load-bearing step selected is Lemma 3.2, “Reduction,” in [trees.tex](https://github.com/openai/math/blob/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/build/source/sections/trees.tex). It is the simultaneous reduction that permits the same W to be used at every level. The check below takes the two explicit bounds of the preceding local resampling lemma as inputs; it does not claim a verification of the entire manuscript or its Lean closure.

Let ε_s=exp(−m_s), let d_v(W) be local failure mass, and let t_vb(W) be the nonfailure mass with target b. The identity d_v+Σ_b t_vb=1 is exact. Define D_v=(d_v+Σ_b t_vb D_b)/ε_s, with D=0 at leaves. If v is bad, its mass of nonfailing transitions to good children is less than 1−ε_s, so d_v+Σ_bad b t_vb>ε_s. Induction gives D_b>1 for bad children, and hence D_v>1. Thus P(root bad)≤E D_root; no independence between nodes was used here.

The critical dependence claim is valid for the fixed input tree: every label anywhere below child b is disjoint from the incoming label A_b, because that descendant label and A_b lie on a common full path. Every local transition only reads W on its child-label union. Consequently D_b(W), recursively defined before pruning, depends only on coordinates outside A_b. The local distortion estimate can therefore be applied to D_b itself, despite its dependence on the same W:

\[
\mathbb E[t_{vb}(W)D_b(W)]
\le e^{11m_s}\nu_v(b)\mathbb E D_b(W).
\]

Together with E d_v≤exp(−9m_s) and division by ε_s, this gives exactly

\[
\mathbb E D_v\le e^{-8m_s}
+e^{12m_s}\sum_b\nu_v(b)\mathbb E D_b.
\]

Unrolling over levels bounds the root expectation by

\[
\sum_{j=1}^k\exp\!\left(12\sum_{h<j}m_h-8m_j\right).
\]

Growth m_{j+1}≥16m_j gives Σ_{h<j}m_h≤m_j/15. Each exponent is therefore at most −(36/5)m_j, and in particular at most −7m_j. The m_j are distinct positive integers, so the sum is bounded by 1/(e⁷−1)<1/4. This independently reproduces the probability estimate with slack.

On success the retained mass γ_v is at least 1−ε_j. A retained fragment T=A_b∖W has size at most floor(m_j/2). For every transition T⊆A_source, while the source still has its original law at each fixed W. Thus for nonempty J,

\[
\Pr(J\subseteq T\mid\hbox{retained},W)
\le\frac{\alpha_j^{|J|}}{\gamma_v(W)}
\le\left(\frac{\alpha_j}{1-\varepsilon_j}\right)^{|J|}.
\]

This verifies the claimed spread loss. Labels remain subsets of their old labels, preserving disjointness. Every retained target satisfies A_b⊆W∪T, and good retained children have continuations, which verifies recovery of a full original path. Zero capacities after halving are handled explicitly in the next subsection by committing an empty prefix, so they do not create a missing terminal case.

Result: no gap found in this lemma conditional on the stated local resampling estimates. The reuse of W is paid for by the distortion factor e^{11m_s}, rather than by an unjustified independence assumption. This limited check does not change the SOLVED-CLAIMED verdict into a correctness certification.
