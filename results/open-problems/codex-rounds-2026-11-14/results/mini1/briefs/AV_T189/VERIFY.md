# T189: verification of the claimed general-graph FPRAS

Checked 14 November 2026. Verdict: **SOLVED-CLAIMED**, in the usual finite simple undirected graph model. This records the scope and supporting literature of a claim without adjudicating proof correctness.

## 1. Direct match: the FPRAS paper

**OpenAI, “A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs”, September 23, 2026.** Opened the actual [TeX source](https://github.com/openai/math/blob/main/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/main.tex), saved as [fpras.tex](fpras.tex), and the [author/date record](https://github.com/openai/math/blob/main/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/README.md). Immediately before Theorem 1.1, the source defines \(G=(V,E)\) to be a finite simple undirected graph and \(Z(G)\) to be its number of perfect matchings.

Theorem 1.1, copied exactly from the source, including its TeX notation (\(\eps=\varepsilon\), \(\Prb=\mathbb P\)):

```latex
\begin{theorem}\label{thm:main}
There is a uniform classical randomized algorithm which, given $G$ and
rational parameters $0<\eps<1$ and $0<\delta<1/2$, returns a nonnegative
rational number $\widehat Z$ such that
\[
 \Prb\bigl[(1-\eps)Z(G)\le \widehat Z\le(1+\eps)Z(G)\bigr]
 \ge 1-\delta.
\]
If $Z(G)=0$, the output is zero with certainty. The worst-case bit running
time is polynomial in the input encoding length, $\eps^{-1}$, and
$\log\delta^{-1}$.
\end{theorem}
```

### Comparison with every requirement in our row

| Our statement | The theorem | Comparison |
| --- | --- | --- |
| “arbitrary finite graph” | Finite simple undirected graph, with no density, expansion, planarity, connectivity or bipartiteness promise | Same standard model; arbitrary orders. |
| “number of perfect matchings” | \(Z(G)=\#\{M\subseteq E:M\text{ is a perfect matching of }G\}\) | Exactly the requested count, not all matchings or maximum matching size. |
| “given … \(\varepsilon>0\)” | Rational \(0<\varepsilon<1\) | Usual finite-input FPRAS convention. Larger tolerances can use a fixed smaller one; arbitrary unencoded real numbers are not computational inputs. |
| “within a factor \(1\pm\varepsilon\)” | \((1-\varepsilon)Z(G)\le\widehat Z\le(1+\varepsilon)Z(G)\) | Identical relative-error interval, at every input size. |
| “probability at least \(3/4\)” | Success at least \(1-\delta\), rational \(0<\delta<1/2\) | Set \(\delta=1/4\); confidence is adjustable too. |
| “time polynomial in \(n\) and \(1/\varepsilon\)” | Worst-case bit time polynomial in input encoding length, \(1/\varepsilon\), \(\log(1/\delta)\) | Same FPRAS requirement, including failed runs. A simple graph has polynomial-size explicit encoding in \(n\); parameter encoding lengths are charged too. |
| No promise a perfect matching exists | Zero returned with certainty if \(Z(G)=0\) | Includes odd order and other infeasible cases; the source gives the empty graph count one. |
| “without assuming \(G\) bipartite” | No bipartiteness hypothesis | Covers the missing general-graph case outright. |

There is no fixed-parameter restriction or asymptotic-only accuracy guarantee. This is a uniform classical randomized algorithm. Weighted colored graphs occur internally; the preliminaries expressly say the main theorem does not claim an algorithm for compressed edge multiplicities or singleton-covering loops. “The whole statement” therefore refers to the customary simple undirected meaning of our row; alternative graph conventions should be specified separately.

## 2. Entropy candidate: related, but not the requested FPRAS

**OpenAI, “Entropy and Face Dimension of the Perfect-Matching Polytope”, September 23, 2026.** Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/main.tex), its actual [introduction](https://github.com/openai/math/blob/main/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/sections/01-introduction.tex), and [polytope section](https://github.com/openai/math/blob/main/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/sections/02-polytope.tex); saved as entropy.tex, entropy-introduction.tex and entropy-polytope.tex.

Here \(P(G)\) is the perfect-matching polytope; \(H(x)\) is the maximum entropy of a law on perfect matchings with edge means \(x\); \(F(x)=-\sum_e x_e\log x_e\); \(B(x)=-\sum_e(1-x_e)\log(1-x_e)\); and \(0\log0=0\). The main pointwise theorem, quoted exactly:

```latex
\begin{theorem}[Pointwise entropy bounds]\label{ent:main}
Let $G$ be a loopless multigraph on $2m\ge2$ vertices with at least one
perfect matching. For every $x\in P(G)$,
\begin{equation}\label{intro:main-bound}
                  F(x)-\left(2-\frac2m\right)B(x)
                  \le H(x)\le F(x).
\end{equation}
\end{theorem}
```

The introduction also states this algorithmic main theorem, quoted exactly:

```latex
\begin{theorem}[Deterministic approximate counting]
\label{thm:main}\label{thm:algorithm-guarantee}
There is one uniform deterministic algorithm which, on a graph on $n$
vertices with nonnegative binary integer pair multiplicities, returns an
integer $A\ge0$ satisfying
\[
                         N(G)/512^n\le A\le N(G).
\]
Its running time and output length are polynomial in the input bit length.
In particular, $A=0$ exactly when $N(G)=0$. The guarantee includes a compact
input consisting of binary $n$ and a list of positive pair records.
\end{theorem}
```

Its graph model allows distinguished parallel edges, and its algorithm allows binary multiplicities. The pointwise result assumes a feasible marginal and at least one perfect matching; it bounds entropy rather than outputting the count. The deterministic algorithm handles zero and runs in polynomial bit time, but its factor \(512^n\) grows exponentially with the vertex count and cannot be prescribed as \(1\pm\varepsilon\). Thus it gives a coarse approximation to a related counting problem, not a subclass FPRAS for T189.

Its geometric claim is \(|\operatorname{supp}x|-\dim F_x\le3m-2\), where \(F_x\) is the minimal face containing \(x\). The polytope section states the positive-support version as a proposition, then obtains the supported version by deleting zero coordinates. This dimension inequality is not an approximation scheme. The introduction explicitly refers to the separate FPRAS manuscript for arbitrary simple graphs.

## 3. Maximum-cardinality candidate: a different output problem

**OpenAI, “Almost-Linear-Time Maximum-Cardinality Matching in General Graphs”, September 24, 2026.** This is the manuscript's actual title; “Sparse” occurs only in the supplied folder name. Opened [main.tex](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/main.tex) and its actual [introduction](https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/01-introduction.tex), saved as maximum.tex and maximum-introduction.tex.

Theorem 1.1, quoted exactly:

```latex
\begin{theorem}[Exact matching in almost-linear input-size time]\label{thm:main}
There are a single uniform randomized word-RAM algorithm, fixed constants
$c_0\ge2$ and $C\ge1$, and a nonincreasing function
$\eta:\mathbb N_{\ge1}\to\mathbb R_{\ge0}$ with $\eta(q)\to0$ as
$q\to\infty$ such that the following holds.
For every input graph $G=([n],E)$ with $m=|E|$ and $p=n+m$, the algorithm
halts on every computation path in at most
\[
                          C p^{1+\eta(p)}
\]
instructions. With probability at least $2/3$ it outputs an explicit list of
edges of a matching of size $\nu(G)$.
\end{theorem}
```

The preceding model is a simple undirected unweighted graph with explicit adjacency lists, including isolates, \(n\ge1\), and \(O(\log(n+2))\)-bit word-RAM instructions. Random bits and multiword arithmetic are charged. All densities are covered; \(m=O(n)\) specializes the running time to almost-linear in \(n\).

The quantity \(\nu(G)\) is the number of edges in one largest matching. The output is that matching's edge list. It neither counts perfect matchings nor samples them approximately uniformly, and has no relative-count error parameter. Raising its \(2/3\) confidence would still leave the count uncomputed. For T189 this candidate is **NOT-THIS**.

## 4. Follow-ups and scrutiny

### Later proof claim

Opened the [arXiv abstract and version record](https://arxiv.org/abs/2610.26803) and [full HTML manuscript](https://arxiv.org/html/2610.26803v1) of **Chenghua Liu and Boning Meng, “A simplified proof of the FPRAS for counting perfect matchings”**, submitted 19 October 2026, arXiv:2610.26803v1. The record displayed only v1 and no journal reference.

Their Theorem 1.1 credits OpenAI and claims the same general-graph relative-error FPRAS, with polynomial worst-case bit time and fair-random-bit use. Their new comparison proof isolates cycles on the original vertices, avoiding the original auxiliary-vertex and tree construction. It retains and explains the original sampling/counting framework. This is a later simplified proof claim, not a referee certification. No separate arXiv posting of OpenAI's original manuscript was located.

### Lean artifacts actually opened

Opened OpenAI's [scope note, lean/docs/113.md](https://github.com/openai/math/blob/main/lean/docs/113.md), [Lean README](https://github.com/openai/math/blob/main/lean/README.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml), and [Comparator instructions](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/README.md), then:

- [MatchingFPRAS.lean: challenge statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/MatchingFPRAS.lean), saved as fpras-statement.lean.
- [MatchingCount/Main.lean: proof entry point](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/MatchingCount/Main.lean), saved as fpras-main.lean.
- [MatchingFPRAS.json: comparison configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/MatchingFPRAS.json), saved as fpras-comparator.json.
- [PerfectMatching/Main.lean](https://github.com/openai/math/blob/main/lean/OAI/Combinatorics/PerfectMatching/Main.lean), saved as matching-main.lean: this is an entropy module, not the FPRAS entry point.

The FPRAS challenge defines actual finite simple graphs, their exact count, binary input and rational output encodings, and a single randomized Post-Turing machine with a finite transition table. It bounds time by
\[
C(\text{input length}+\lceil\varepsilon^{-1}\rceil+
 \operatorname{clog}_2\lceil\delta^{-1}\rceil+1)^d.
\]
It requires nonnegative rational output on every bounded random tape, zero on every tape when the count is zero, and a good-tape fraction at least \(1-\delta\). These definitions visibly address the row's model, quantity, confidence and worst-case polynomial time. The proof entry point invokes separate time, output and success results; the import closure was not audited.

The challenge intentionally ends in “sorry”: it specifies the goal. The separate entry point contains a proof term. The JSON compares OAI.MatchingFPRAS.thm_main, lists no replaceable definitions, permits only propext, Quot.sound and Classical.choice, and disables nanoda. The challenge placeholder alone does not establish a gap in the solution.

Opened the community's [published MatchingFPRAS Comparator log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/MatchingFPRAS.log) and [check documentation](https://github.com/mathcommunity/oai-math-revised/blob/main/docs/LEAN_CHECKS.md), saved locally. The log reports acceptance by Lean's default kernel and “Your solution is okay!” The documentation dates the runs to 25–26 October 2026 and records the snapshot/tools; it discloses precompilation in the same workspace, a departure from the strictest adversarial procedure. This is published checking evidence, not a locally repeated run or a completed mathematical referee review.

For the entropy companion, the scope note includes the refined entropy bound and coarse counting guarantees, but says the sharp global face-dimension bound is not part of the selected triangle-expansion statement. No formalization of the maximum-cardinality manuscript was found in the catalogue checked.

### Error reports, comments and other later material

Opened the [repository README](https://github.com/openai/math/blob/main/README.md), [history](https://github.com/openai/math/blob/main/history.md), and all three manuscript READMEs. No matching-paper withdrawal or correction notice appears there. The history's withdrawals of unrelated papers do not establish an error here.

Opened the community pages for the [FPRAS manuscript](https://mathcommunity.github.io/oai-math-revised/papers/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/), [entropy manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/), and [maximum-matching manuscript](https://mathcommunity.github.io/oai-math-revised/papers/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/). Their collected notes are explicitly unreviewed and AI-collected. The FPRAS page links a correction to an outside catalogue's confusion between counting all matchings and counting perfect matchings; that PR could not be opened, so its comment was not independently verified.

Opened the later implementation's [own README](https://github.com/spele1100/reverse-matching/blob/main/README.md). It substitutes exact methods for the maximum-matching paper's pricing machinery and expressly does not reproduce the almost-linear running-time guarantee. It supplies no counting FPRAS evidence. Also opened the [arXiv page](https://arxiv.org/abs/2610.40591) for **George Z. Li, Jason Li and Junkai Zhang, “Maximum Cardinality Matching in \(n^{2+o(1)}\) Time”**, submitted 29 October 2026. Its abstract concerns finding a maximum matching, not counting. Neither source was treated as validating or refuting OpenAI's proof.

Opened the [AI Proved What? exposition](https://aiprovedwhat.com/episodes/113-counting-perfect-matchings-fpras/), whose status section last checked 10 November says no peer or expert review had been seen. It is not itself an expert review. A latent-seminar exposition lead was inaccessible and is not evidence.

Searches combined exact titles with OpenAI, arXiv, error, correction, refutation, referee, expert, Sinclair and Vigoda, and targeted indexed GitHub issues in both repositories. No direct refutation, counterexample, named expert validation or completed referee report was located. This is a bounded search result as of 14 November, not a claim that none exists anywhere. LOG.md records the queries and failed accesses.

## Recommended new “where it stands” text

OpenAI's preprint *A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs* (23 September 2026) claims an FPRAS for every finite simple undirected graph, with polynomial worst-case bit time and exact zero detection. Chenghua Liu and Boning Meng's *A simplified proof of the FPRAS for counting perfect matchings* (arXiv:2610.26803, 19 October 2026) gives a later simplified proof claim, and OpenAI has published a Lean formalization with a reported community Comparator acceptance. Neither manuscript is refereed, and no direct refutation or completed expert review was found in the sources checked as of 14 November 2026.

## Spot check

**Selected bottleneck: Lemma 6.4, “Encodings with a bounded number of preimages”** (source label lem:encoding). Theorem 6.1's restricted pair-energy inequality is the central sampling comparison; this lemma bounds the weight distortion and congestion of its switch and context-error terms. Liu–Meng also identify this encoding as an input to their comparison. The lemma is copied exactly:

```latex
\begin{lemma}[Encodings with a bounded number of preimages]
\label{lem:encoding}
Every switch demand has an encoding $(A_P,B)$ by two perfect
matchings, and every error demand has encodings
$(A^{(j)},B^{(j)})$ for $j=0,1$, with the following properties.
\begin{enumerate}[label=\textup{(\roman*)}]
 \item For each encoding $(A,B)$,
 $\rho(d)\le A_0^4\pi(A)\pi(B)$.
 \item For each encoding type and each fixed output pair, there are
 at most $\calT$ demand preimages.  This bound includes the choices
 of cycle, cell, opposite pair, and context.
 \item For an error demand, both guide matchings satisfy
 $C_X\subseteq B^{(j)}$.
\end{enumerate}
\end{lemma}
```

Here \(\rho(d)=\pi(I_1)\pi(I_2)\), \(A_0=1000D\), and \(\mathcal T=(10N)^{30}\). Checked the definitions of the arc patterns, the cell matchings and both error contexts in Sections 5–6, the full encoding proof, and its immediate conditional-mass application.

1. **Legality and constant-size change.** On a long odd arc, removing the through pattern's first and last edges frees its two endpoints and two distinct internal leaves. A good-side leaf repair rematches the leaves. Removing an opposite pair frees each of the four cell corners once. For switch encodings the union adds two chords and \(r\) repairs and drops \(2+r\) edges, where \(r\le2\); hence both lists have size at most four. Error context zero makes the same number of changes. Context one swaps two complete matching patterns on the same arc, preserving the multiset union; the opposite arc \(X\) is vertex-disjoint, so the guide retains \(C_X\). This also works for length-three arcs.

2. **Weight ratio, checked two ways.** Section 5's cell comparison puts every added/dropped edge in a common activity range with ratio at most \(A_0\). For lists of equal length \(k\le4\), the ratio of their products is at most \(A_0^k\le A_0^4\). Equivalently the log-weight change is at most \(k\log A_0\). The two \(Z_w\) normalizers cancel exactly. No weight loss depending on cycle length is inserted at this step. This check uses the cell-comparability result as an input, rather than assuming arbitrary graph weights are comparable.

3. **Inverse and tag count.** Given the output pair and the lists of added/dropped colored edge occurrences, undoing those changes restores the original degree-two multiset union. Its component containing the first tagged corner is the active discrepancy cycle. One orientation bit recovers both alternating layers there; elsewhere the output layers were unchanged. The deterministic quadrangulation and the four corners recover the cell; the fixed flags recover the demanded term. Colors and repeated occurrences must be retained, as the proof explicitly requires. The stated tag estimate is consistent:
\[
128N^4(1+2N^2)^8\le128\cdot3^8 N^{20}
=839808N^{20}<(10N)^{30}\quad(N\ge2).
\]
Thus the displayed bound is polynomial, even though the cycle itself may be long.

4. **Rare guide events.** Retaining \(C_X\subseteq B\) gives a demand-mass bound \(A_0^4\mathcal T\,\pi(A)p_X\), with \(p_X=\pi(B\supseteq C_X)>0\). Conditional Jensen introduces exactly \(1/p_X\), which cancels this factor. The application does not assume a polynomial lower bound on the probability of the guide event. This is necessary: discarding the factor would leave an uncontrolled inverse rare-event probability.

As a separate finite check of the matching bookkeeping, [check_encoding.py](check_encoding.py) enumerated every four-corner cell anchored at vertex zero with four odd arc lengths on cycles of orders 4, 6, 8, 10, 12 and 14 in a single complete bag. It checked perfect-matching legality, at most four added/dropped edge occurrences, union restoration, guide containment, and preservation of product union in both error contexts. Output: 126 cells, 252 switch encodings and 140 ordered error encodings (both contexts checked), all assertions passed. The counts agree independently with odd-composition counts: for order \(2k\), cells number \(\binom{k+1}{3}\), and ordered opposite-long-side choices number \(4\binom{k-1}{3}\), with out-of-range binomial coefficients zero.

**Scope of the check.** The local reconstruction, weight and conditioning accounting exposed no discrepancy. The enumeration uses one bag, uncolored edges and one active cycle; it does not check all label trees or establish the quadrangulation lemma. Neither this limited check nor the published Comparator log is a correctness verdict on the complete preprint.

Task: “Verify: has open problem T189 been settled by the OpenAI math release?” — 14 November 2026, 21:11 +04.

