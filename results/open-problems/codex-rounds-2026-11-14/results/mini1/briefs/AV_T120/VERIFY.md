# T120 — Finding large independent sets in sparse random graphs

Checked on 14 November 2026. Verdict: **NOT-THIS for all three candidates.** None claims either branch of T120. This report compares statements and records follow-ups; it does not certify the preprints' proofs.

## The statement being compared

The supplied statement, verbatim:

> In G(n, d/n) with d large, the independence number is (2 + o_d(1))(log d/d)n, while simple greedy algorithms find independent sets of size (1 + o_d(1))(log d/d)n. Prove that no polynomial-time algorithm finds an independent set of size (1 + ε)(log d/d)n with high probability, for fixed ε > 0 and all large d, or find one.

The input is an Erdős–Rényi graph \(G(n,d/n)\): each possible edge is present independently with probability \(d/n\). The target is a polynomial-time algorithm finding an independent set of at least \((1+\varepsilon)(\log d/d)n\) vertices with high probability, for a fixed positive improvement \(\varepsilon\) and all sufficiently large \(d\), or a hardness theorem excluding such algorithms without restricting them to a particular algorithmic class. The asymptotic independence-number and greedy-size facts in the supplied row are background; the unresolved part is the algorithmic gap.

The relevant order of limits is \(n\to\infty\) for each sufficiently large fixed \(d\), followed by \(d\to\infty\). “High probability” here concerns the random input and any algorithmic randomness. None of the three theorem statements below has this combination of model, target, and quantifiers.

## Candidate 1: three-colorable independent sets

**OpenAI, _Hardness of finding large independent sets in three-colorable graphs_, September 24, 2026.** Author and date are as printed in the [manuscript root](https://raw.githubusercontent.com/openai/math/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/main.tex) and [citation README](https://raw.githubusercontent.com/openai/math/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/README.md). Theorem 1.1 is quoted verbatim as LaTeX from the [actual introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/introduction.tex); source macros and labels are preserved.

```tex
\begin{theorem}\label{thm:main}
For every fixed real $0<\delta<1/3$, there is a deterministic
polynomial-time algorithm $R_\delta$ that maps each explicitly encoded
Boolean $3$-CNF formula $\phi$ to a nonempty finite simple undirected
unweighted graph $G_\phi$ such that
\[
 \begin{array}{ll}
 \phi\text{ is satisfiable}
   &\Longrightarrow G_\phi\text{ is three-colorable},\\[2pt]
 \phi\text{ is unsatisfiable}
   &\Longrightarrow \alpha(G_\phi)<\delta\,|V(G_\phi)|.
 \end{array}
\]
The running time and explicit output size are polynomial in the ordinary
binary encoding length of $\phi$. Their constants and polynomial degree
may depend on the fixed $\delta$, but not on $\phi$.
The coloring in the first implication covers every vertex and is not
supplied with the graph.
\end{theorem}
```

**Comparison.** The quantity \(\alpha(G)\) is the same independence number, and both problems concern finite simple unweighted graphs. Everything that specifies the computational problem differs: these inputs are outputs of a worst-case deterministic reduction from 3SAT, with three-colorability in the satisfiable case, rather than draws from \(G(n,d/n)\). There is no random-edge law, average-degree parameter \(d\), large-degree limit, or “with high probability over the input” assertion. The density parameter \(\delta\) is an arbitrary fixed number below \(1/3\); it is not a gain of \(1+\varepsilon\) over \(\log d/d\).

The claimed gap is between three-colorability (which implies \(\alpha(G)\ge |V|/3\)) and \(\alpha(G)<\delta |V|\). It is worst-case NP-hardness, whose algorithmic exclusion requires the relevant complexity assumption; it is not an unconditional impossibility theorem for all polynomial-time algorithms on typical random graphs. Even setting \(\delta=(1+\varepsilon)\log d/d\) for a fixed large \(d\) would leave the input distribution completely unaddressed. No average-case reduction to Erdős–Rényi graphs is supplied by the theorem.

**Covered:** worst-case constant-density independent-set gap with a three-colorable completeness promise. **Not covered:** either T120 branch, its independence-number asymptotic, or its greedy threshold. **Verdict: NOT-THIS.**

## Candidate 2: maximum matching

The folder name says “Sparse General Graphs,” but the manuscript's printed title is **OpenAI, _Almost-Linear-Time Maximum-Cardinality Matching in General Graphs_, September 24, 2026**. See the [manuscript root](https://raw.githubusercontent.com/openai/math/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/main.tex) and [citation README](https://raw.githubusercontent.com/openai/math/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/README.md). Its Theorem 1.1 is quoted verbatim from the [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/01-introduction.tex).

```tex
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

Here \(\nu(G)\) denotes maximum matching size. The surrounding computational model is a randomized word-RAM with words of \(\lceil c_0\log_2(n+2)\rceil\) bits; input is an explicit adjacency-list representation. All input/output and multiword arithmetic costs count toward the bound.

**Comparison.** The input class includes sparse Erdős–Rényi graphs as particular graphs, and the claimed algorithm is polynomial time, indeed almost linear. However, its output is a set of **edges with disjoint endpoints**, not a set of pairwise nonadjacent **vertices**. It optimizes \(\nu(G)\), not \(\alpha(G)\). Exact maximum matching has long been polynomial-time solvable; the claimed improvement concerns its running time. Its success probability is at least \(2/3\) on every graph, rather than an independent-set density guarantee with high probability under \(G(n,d/n)\). Probability amplification would not change the output quantity.

A matching is an independent set in the line graph, but this does not turn this result into maximum independent set in the original graph, and a line-graph transformation does not preserve the Erdős–Rényi model. The paper's prescribed-degree-factor application likewise selects edges of a spanning subgraph; it supplies no independent-set threshold.

**Covered:** an exact maximum-matching running-time claim on all simple graphs, including sparse ones. **Not covered:** T120's vertex-independent-set target or hardness alternative. **Verdict: NOT-THIS.** OpenAI's family number **120** is a catalogue identifier for matching and is unrelated to our row identifier **T120**.

## Candidate 3: Anderson disorder

**OpenAI, _Fixed-energy universality for weak Anderson disorder on random regular graphs_, October 5, 2026.** See the [manuscript root](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex) and [citation README](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md). Its Theorem 1.1 is quoted verbatim from the [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex).

```tex
\begin{theorem}[Fixed-energy universality]\label{thm:main}
For every $d\ge3$ and every $0<\kappa<2\sqrt{d-1}$, there is
$w_0=w_0(d,\kappa)>0$ with the following property.  For each fixed
$0<w<w_0$, the restriction of $\nu_{d,w}$ to an open neighborhood of
\[
 I_{d,\kappa}=[-2\sqrt{d-1}+\kappa,\,2\sqrt{d-1}-\kappa]
\]
has a continuous density $\rho_{d,w}$, strictly positive on
$I_{d,\kappa}$.  For every fixed $E\in I_{d,\kappa}$, set
\[
 \Xi_{n,E}=\sum_{i=1}^n
       \delta_{n\rho_{d,w}(E)(\lambda_i-E)}.
\]
Then, for every nonnegative $f\in C_c(\RR)$,
\begin{equation}\label{eq:main-laplace}
 \left|
 \EE\exp\left(-\int f\,d\Xi_{n,E}\right)
 -\EE\exp\left(-\int f\,d\Xi_n^{\GOE}\right)
 \right|\longrightarrow0
\end{equation}
as $n\to\infty$ through all sizes $n>d$ with $nd$ even.
\end{theorem}
```

The objects in this statement are as follows. The graph is uniform among labelled simple \(d\)-regular graphs, with \(nd\) even. Its adjacency matrix is perturbed to \(H_{n,d,w}=A_{n,d}+w\operatorname{diag}(\omega_1,\ldots,\omega_n)\), where the independent \(\omega_v\) are uniform on \([-1,1]\) and independent of the graph. The \(\lambda_i\) are its eigenvalues, and \(\nu_{d,w}\) is the expected root spectral measure of the corresponding infinite-tree operator. The comparison process is \(\Xi_n^{\mathrm{GOE}}=\sum_i\delta_{(n/\pi)\mu_i}\) for normalized GOE eigenvalues \(\mu_i\).

**Comparison.** A uniform regular graph has exactly degree \(d\) at every vertex; it is not \(G(n,d/n)\), where edges are independent and degrees vary. The theorem treats each fixed \(d\ge3\), fixed positive sufficiently small disorder \(w\), a fixed bulk energy, and \(n\to\infty\) through admissible sizes. It does not give uniform large-\(d\) algorithmic bounds. Its asymptotic is a limit of Laplace functionals of microscopic eigenvalue point processes, not an asymptotic for \(\alpha(G)\) or the size achieved by an algorithm. The extra diagonal disorder is absent from T120. No polynomial-time independent-set algorithm or hardness theorem is stated. A spectral universality limit alone supplies neither.

**Covered:** a spectral-statistics claim for a different random-graph ensemble with additional random potentials. **Not covered:** any part of T120's algorithmic alternative. **Verdict: NOT-THIS.**

## Comparison at a glance

| Requirement in T120 | Three-colorable paper | Matching paper | Anderson paper |
| --- | --- | --- | --- |
| Input law \(G(n,d/n)\) | No; reduction outputs | All graphs allowed, but no independent-set output | No; uniform regular graphs plus disorder |
| Quantity \(\alpha(G)\) or a constructed vertex independent set | Yes, in a different promise problem | No; \(\nu(G)\), an edge matching | No; eigenvalues |
| Target \((1+\varepsilon)n\log d/d\) | No; fixed \(\delta n\) gap | No | No |
| Every sufficiently large fixed \(d\), then \(n\to\infty\) | No \(d\) parameter | No density/degree threshold | Fixed \(d\ge3\), but spectral quantity |
| High-probability success or failure on random inputs | No; worst-case NP-hardness | Constant success for a different task | Convergence in law for a different observable |
| Unrestricted polynomial-time independent-set algorithm or exclusion | Neither | Neither | Neither |

## Follow-ups and formalisation

Searches used the web search tool for each exact title and combinations with “arXiv,” “error,” “refutation,” and “proof,” together with sparse-random independent-set/OpenAI/2026 searches. The [release history](https://raw.githubusercontent.com/openai/math/main/history.md), opened in full, contains no withdrawal or repair notice naming these three papers. This is a bounded search as of the date above; failure to find a report is not evidence that a proof is correct.

- **Three-colorable paper.** Opened [lean/docs/106.md](https://raw.githubusercontent.com/openai/math/main/lean/docs/106.md), the [formalisation catalogue](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [challenge statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/IndependentSets.lean), [Comparator configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/IndependentSets.json), and [solution Main.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Combinatorics/IndependentSets/Main.lean). The named declaration is `OAI.LargeIndependentSets.mainTheoremReal`. Its challenge defines a polynomial-time binary 3SAT-to-graph reduction, three-colorability, and independence-density soundness; it contains no Erdős–Rényi distribution. The challenge's `sorry` is a statement placeholder; a separate solution module is configured, with permitted axioms `propext`, `Quot.sound`, and `Classical.choice`. No Lean compilation or Comparator execution was performed here. The [community manuscript page](https://mathcommunity.github.io/oai-math-revised/papers/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/), opened, reports an accepted Comparator run on October 26 but explicitly says nobody has checked whether the formal statements express the paper's claims. This report does not adopt that run as independent mathematical verification.

- **Matching paper.** Opened the [Readable Intelligence exposition](https://readable-intelligence.com/paper/669239fdc7f9?view=readable); it explicitly says its proofs have not been independently checked. Opened **George Z. Li, Jason Li, Junkai Zhang**, [_Maximum Cardinality Matching in \(n^{2+o(1)}\) Time_](https://arxiv.org/abs/2610.40591), submitted October 29, 2026, and its [full text](https://arxiv.org/html/2610.40591v1). Their concurrent-work paragraph acknowledges OpenAI's October 6 release and says the approaches appear orthogonal. This is a separate matching algorithm, not an arXiv version or validation of the OpenAI proof. Also opened the [spele1100/reverse-matching reference implementation](https://github.com/spele1100/reverse-matching). Its README describes AI-assisted reproduction with exact substitutes for the pricing/data-structure engine and expressly says the almost-linear running time is not reproduced. Its tests were not run here, and this is not verification of the claimed runtime. The [community matching page](https://mathcommunity.github.io/oai-math-revised/papers/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/) was also opened. No matching formalisation entry was located in the opened release catalogue.

- **Anderson paper.** Opened the [community manuscript page](https://mathcommunity.github.io/oai-math-revised/papers/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/), which distinguishes the clean-model companion from the positive-disorder paper and lists related work. No Anderson-disorder formalisation entry was located in the release catalogue. Opened **Yukun He, Jiaoyang Huang, Xiaoyu Wang**, [_Bulk universality of random regular graphs_](https://arxiv.org/abs/2610.08127), submitted October 6, 2026: its abstract treats the clean adjacency model, without diagonal disorder, so it is related work rather than a same-statement version of this candidate. Opened [Latent Seminar's _Microscopic spectra of random regular graphs_](https://lowrank.github.io/latent-seminar/OpenAI-Math/219-random-regular-spectra), dated October 6, 2026; it expressly limits its review to statements and selected mechanisms. A requested slatinwine exposition URL returned a cache miss and was not read.

The three community pages carry automatically collected, unreviewed notes rather than referee reports. No candidate-specific refutation, error report, or completed expert/referee assessment was located in the searches so far; no same-title arXiv version was identified. Read-only issue and pull-request searches in `openai/math` for the candidate topics returned no matches; initial queries without an explicit issue type failed and were retried.

The [Lean library README](https://raw.githubusercontent.com/openai/math/main/lean/README.md) and [Comparator instructions](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md) were opened; these are checking instructions, not a report that these results were checked here.

The complete release [CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) was also opened and searched for random-graph and independent-set language. It did not reveal a direct T120 claim. This search does not assert that every proof in the release has been audited.

## Existing row references checked

Opened **Alexander S. Wein**, [_Optimal Low-Degree Hardness of Maximum Independent Set_](https://arxiv.org/abs/2010.06563): its abstract explicitly treats sparse Erdős–Rényi graphs and the half-optimal threshold for low-degree polynomial algorithms. Opened **Brice Huang, Mark Sellke**, [_Strong Low Degree Hardness for Stable Local Optima in Spin Glasses_, v2](https://arxiv.org/abs/2501.06427v2), revised March 31, 2026: although the title concerns spin glasses, the abstract expressly includes a strong-low-degree-hardness improvement for maximum independent set. Thus the title alone is not grounds for deleting that citation; its detailed independent-set theorem is a separate scope check. Neither abstract claims unrestricted polynomial-time hardness. The other references in the supplied note were not independently audited in this report.

## Recommended replacement “where it stands” (three sentences)

The unrestricted polynomial-time problem of beating \((\log d/d)n\) by a fixed factor in \(G(n,d/n)\) remains open in the literature checked; the cited barriers apply to restricted classes of algorithms. OpenAI's _Hardness of finding large independent sets in three-colorable graphs_ (September 24, 2026) claims worst-case hardness for a different input promise and does not settle this random-graph question. Its _Almost-Linear-Time Maximum-Cardinality Matching in General Graphs_ (September 24, 2026) and _Fixed-energy universality for weak Anderson disorder on random regular graphs_ (October 5, 2026) concern different quantities and also leave this question untouched.

## Opened-material record

The exact theorem sources, citation READMEs, manuscript roots captured locally, formalisation catalogue and relevant Lean files are in [sources/](sources/). Other opened primary documents and follow-up pages are linked at their point of use above. The supplied GitHub folder URLs initially failed in the browser, after which their directory listings and source files were successfully opened through the read-only GitHub connector. No title-match score was used as mathematical evidence.

## Spot check

**Selected lemma:** distributional alignment, Lemma 5.1 of the three-colorable independent-set paper, with its full proof in Section 8. Sources: [statement](https://raw.githubusercontent.com/openai/math/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/alignment.tex), [proof](https://raw.githubusercontent.com/openai/math/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/sections/alignment-proof.tex); local copies are in sources/. This is the combinatorial step that chooses a sampling law before the independent set, avoiding dependence on the Label Cover alphabet. The symbol \(d\) in this lemma bounds list sizes; it is unrelated to T120's random-graph average degree.

For fixed \(s,d,\eta>0\), the lemma produces \(r\ge s\) and a rational law \(\mu\) on \(s\)-subsets \(B\) of \([r]\). Every family of lists \(A_I\), of size at most \(d\), that is disjoint on separated sets (\(\max I<\min J\)) must, with probability at least \(1-\eta\), admit an assignment of each label to one index common to all its occurrences within \(B\).

The following checks concern the full stated quantifiers, not just a fixed label universe.

1. **Finite reduction and minimax.** There are finitely many list slots for fixed \(r,s,d\). List lengths and equivalence relations among occupied slots determine both separated disjointness and failure of alignment. Thus there are finitely many relevant patterns even for an infinite label universe. Failure of a universal sampling law at tolerance \(\xi>0\) gives, by finite minimax, a random allowed pattern making each \(s\)-set bad with probability at least \(\xi\). This reverses the required quantifiers in exactly the needed direction.

2. **Ramsey limit.** For each fixed pattern size \(t\), its probability simplex is finite dimensional. Discretizing each coordinate, homogenizing all sizes \(t\le k\) on a \(k\)-set, and taking a diagonal subsequence gives laws consistent under every increasing restriction. The lower bound on badness survives because it is a finite-pattern event. These consistent laws construct a countable array on rational indices. Separated disjointness, transitivity of slot equality, and distinctness within lists are all finite constraints, hence survive.

3. **The crucial cut.** For a label occurring at a fixed finite index set \(I\), define
   \[
   p=\sup\{\min J:\text{the label occurs at }J\}.
   \]
   Its own occurrence gives \(p\ge\min I\), while separated disjointness gives \(p\le\max I\). Under every increasing rational automorphism fixing \(I\), the selected slot and occupancy event stay fixed and \(p\) transforms by the induced real homeomorphism. Consequently its subprobability law is invariant under those maps. For consecutive \(a<b\) in \(I\), any two rational points \(q<q'\) in \((a,b)\) can be related by such a map taking \(q\) to \(q'\). Equality of the two cumulative probabilities gives zero mass to \((q,q']\). Countably many such intervals cover the whole gap, including irrational points. The cut therefore belongs to \(I\) almost surely. This step supplies an actual common index, not merely overlap of the convex hulls of occurrence sets.

4. **Simultaneity.** There are countably many rational-indexed slots. The preceding conclusion holds simultaneously for all occupied slots outside one null event. Equivalent slots have the same occurrence family, hence the same \(p\); that \(p\) lies in every occurrence set. Every label in any finite \(B\) is therefore alignable, contradicting its positive badness probability.

5. **Rational law and uniform error.** Approximate the finite real sampling law in \(\ell^1\) by a rational one with error below \(\eta-\xi\). Since every badness indicator lies in \([0,1]\), its expectation changes by at most that same \(\ell^1\) error, uniformly over all patterns. Thus rationalization does not lose the “before the lists” requirement. The proposed exhaustive finite linear-program search is independent of the input formula; its potentially enormous cost is a fixed-parameter constant rather than a hidden dependence on the formula size.

No gap was identified in these inspected combinatorial steps. This does not check the analytic extraction of the lists, the coefficient estimate, the PCP inputs, the complete reduction, or the Lean dependency tree, and makes no correctness judgment on the preprint as a whole. Even a valid alignment lemma would give no average-case reduction or algorithm for T120.

