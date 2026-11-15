RESOLVED_IN_LITERATURE

# C0149: Bowen's essential-expansion conjecture

Kun proved the conjecture. A published statement with the unlabelled, bounded-degree hypothesis appears as **Theorem 1, p. 2378**, in Gábor Kun, “On sofic approximations of Property (T) groups,” a contribution on pp. 2378–2379 of *Measured Group Theory*, *Oberwolfach Reports* **13** (2016), no. 3, 2347–2397, DOI [10.4171/OWR/2016/41](https://ems.press/journals/owr/articles/14749). The volume is dated 2016; the publisher gives 22 April 2017 as its publication date. [The theorem is on printed p. 2378, PDF page 32.](https://ems.press/content/serial-article-files/46644)

The complete proof is Kun, [arXiv:1606.04471v5](https://arxiv.org/abs/1606.04471v5), 30 July 2019, **Theorem 1, pp. 1–2**. The first version was posted on 13 June 2016. The latest full paper formulates its main theorem for labelled sofic approximations, whereas the published announcement and the first version state unlabelled local convergence. This distinction requires attention; it is addressed below without assuming that unlabelled finite approximations can themselves be labelled. No journal publication of the full proof was identified.

The published result permits changing o(|V|) edges. The vertex-deletion formulation in Pete's notes follows by the pruning argument below. In particular, the expansion constant is fixed before epsilon is chosen. There is no remaining gap in the stated essential-expansion conclusion. Following the requested stopping rule, no SL(3) experiments, random-lift experiments, or new open-problem research were undertaken.

## Statement and conventions checked against Pete

The author's [homepage](https://math.bme.hu/~gabor/) links [*Probability and Geometry on Groups*](https://math.bme.hu/~gabor/PGG.pdf). The retrieved current file is dated **3 April 2024**. Chapter 14 occupies printed pp. 195–215; its table of contents has stale pagination. Conjecture 14.4 is on printed p. 201, as specified in the question. The complete notes and the entire chapter are saved as plain text.

Fix a finite symmetric generating set S of a countably infinite property-(T) group Γ, and write X=Cay(Γ,S), of degree d. Let (G_n) be finite graphs of uniformly bounded degree converging locally, with a uniform random root, to X. The required conclusion is

\[
\exists c=c(\Gamma,S)>0\quad\forall\epsilon>0\quad
\exists n_0\quad\forall n>n_0\quad\exists Z_n\subseteq V(G_n):
\quad |Z_n|\leq\epsilon|V(G_n)|,
\]

with every component of the **induced** graph G_n[V(G_n)\Z_n] having expansion at least c. The threshold n_0 may depend on the approximating sequence and epsilon. No assertion of connectedness of G_n, or of a single giant expander, is needed.

Conjecture 14.4 does not redefine “c-expander.” The preceding convention is Definition 7.8, p. 72, using the Markov-chain Cheeger constant from Theorem 7.6, p. 71. For a d-regular graph H,

\[
h_{\rm Pete}(H)=\min_{0<|A|\leq |H|/2}
\frac{|E_H(A,H\setminus A)|}{d|A|}.
\]

Kun instead uses the **unnormalized edge Cheeger constant**, defined in §2, p. 3 of v5:

\[
h_E(H)=\min_{0<|A|\leq |H|/2}
\frac{|E_H(A,H\setminus A)|}{|A|}.
\]

Thus h_E=d h_Pete on regular graphs. For a graph of maximum degree d, h_E≥a implies both outer-vertex expansion ≥a/d and random-walk conductance ≥a/d. For the latter, apply the edge bound to the side of smaller cardinality and use

\[
\min(\operatorname{vol}A,\operatorname{vol}A^c)
\leq d\min(|A|,|A^c|).
\]

The surviving induced graphs need not be regular. They may equivalently be made regular by adding holding half-loops; this leaves edge boundaries unchanged. Singletons satisfy the expansion condition vacuously. These bounded-degree conversions preserve the order of the quantifiers and settle the edge-versus-vertex normalization issue.

Pete's convergence here is **unlabelled**. Pages 199–200 explicitly distinguish it from labelled Cayley-diagram convergence, and describe Timár's example where a finite graph sequence cannot be given the desired labels. Treating these hypotheses as synonymous would be incorrect.

## The literature theorem and the vertex-deletion implication

Kun's published Theorem 1 assumes finite bounded-degree graphs locally converging to a Cayley graph of a countably infinite property-(T) group. It supplies d-regular graphs H_n on the same vertex sets such that

\[
|E(G_n)\mathbin\triangle E(H_n)|=o(|V(G_n)|),
\qquad
H_n=\bigsqcup_j H_{n,j},\qquad h_E(H_{n,j})\geq\gamma>0.
\]

The expansion parameter is independent of n and of the component. The proof fixes the group, generating set and Kazhdan spectral gap before the approximation-error parameters; the uniformity across approximation sequences is explained in the next section.

Here is a complete conversion to vertex removal. It also explains why merely deleting the endpoints of edited edges is an insufficient justification.

**Pruning lemma.** Let H have maximum degree d and h_E(H)≥γ. Given W⊆V(H), one can delete W and at most 2d|W|/γ further vertices so that the remaining induced graph is empty or has h_E≥γ/4.

Start with C=V(H)\W and potential b(C)=|E_H(C,V(H)\C)|≤d|W|. Whenever there is a nonempty U⊆C with |U|≤|C|/2 and

\[
q:=|E_H(U,C\setminus U)|<\frac\gamma4|U|,
\]

delete U. Since |U|≤|V(H)|/2, expansion in H gives, with r=|E_H(U,V(H)\C)|,

\[
q+r\geq\gamma|U|.
\]

The exact potential change is

\[
b(C\setminus U)=b(C)-r+q
=b(C)-(q+r)+2q
<b(C)-\frac\gamma2|U|.
\]

The potential is nonnegative. Summing over the disjoint removed sets gives total further deletion at most 2b(C_initial)/γ≤2d|W|/γ. The finite procedure terminates. Its stopping condition is precisely h_E(H[C])≥γ/4; a nonempty terminal graph with more than one vertex is connected. This proves the lemma.

Apply it in every component H_{n,j}, with W_n the endpoints of every edge in E(G_n)△E(H_n). Put m_n=|E(G_n)△E(H_n)|. Then |W_n|≤2m_n. Outside W_n, the two induced graphs agree, and there are no edges between distinct H_n-components. Consequently the total deletion satisfies

\[
|Z_n|\leq(1+2d/\gamma)|W_n|
\leq 2(1+2d/\gamma)m_n=o(|V(G_n)|).
\]

Every remaining component has h_E≥γ/4. One may therefore take c_E=γ/4, or c=γ/(4d) for outer-vertex expansion or Pete's conductance convention. For each prescribed epsilon, take n large enough that

\[
\frac{m_n}{|V(G_n)|}\leq
\frac{\epsilon}{2(1+2d/\gamma)}.
\]

The same c works for every epsilon. This is the requested conclusion, including induced components and arbitrary small deletion proportions.

If Γ is finite, a simpler argument suffices: local agreement out to a radius greater than the diameter identifies whole components isomorphic to its finite Cayley graph. All other vertices have vanishing proportion. Thus the countably infinite hypothesis of Kun's theorem omits no difficult finite-group case of Pete's formulation.

## Why the unlabelled hypothesis and uniform constant are valid

This section records the standard bridge between the published unlabelled statement and the formulation of Kun's latest full paper. The inputs are published invariant-decoration theory and Kun's graph-theoretic characterization, rather than a hypothetical labelling of each finite graph.

Let κ=κ(Γ,S)>0 be the displacement Kazhdan constant used by Pete on p. 81. For any unitary representation π, put A=d^{-1}Σ_s π(s), let F be its invariant subspace, and put Q=(I+A)/2. For v⊥F,

\[
\langle(I-A)v,v\rangle
=\frac1{2d}\sum_{s\in S}\|\pi(s)v-v\|^2
\geq\frac{\kappa^2}{2d}\|v\|^2.
\]

Q is a positive contraction and, on F-perp, has norm at most 1−δ, where δ=κ²/(4d)>0. Since (Q²−I)f⊥F,

\[
\|Q^4f-Q^2f\|_2
\leq(1-\delta)^2\|Q^2f-f\|_2. \tag{1}
\]

This uses a lazy operator. Edge expansion controls the top of the nontrivial spectrum; it does not exclude bipartiteness or eigenvalues near −1. Kun's arXiv version history explicitly warns about the distinction in earlier formulations. The argument here requires no two-sided gap for the original walk and uses only the forward decomposition implication of the analytic characterization.

For an unlabelled finite approximation, consider arbitrary vertex functions f_n with ||f_n||_infinity≤1 and pass to a subsequential local limit **including their vertex marks**. Compactness gives a unimodular marked rooted network whose underlying graph is X. A Cayley graph is transitive and unimodular. **Aldous–Lyons, Theorem 3.2**, “Invariance and Unimodularity,” in *Processes on Unimodular Random Networks*, *Electronic Journal of Probability* **12** (2007), 1454–1508, lifts this marked law to an Aut(X)-invariant probability law of marks on X. The downloaded author version, revised 26 June 2023, states and proves this theorem on pp. 17–18.

In particular, the law is invariant under Γ-translations. Its Koopman representation is a genuine unitary Γ-representation. The observable “mark at the identity” and its iterated Markov averages satisfy (1). Norms of these finitely supported local expressions are limits of their normalized finite-graph norms. Thus, for every α>0, all sufficiently large n satisfy, for every f,

\[
\|Q_n^4f-Q_n^2f\|_2
\leq(1-\delta)^2\|Q_n^2f-f\|_2
+\alpha |V(G_n)|^{1/2}\|f\|_\infty. \tag{2}
\]

Indeed, a failure of this uniform assertion supplies a subsequence of violating functions; normalize their sup norms to one and take the marked local limit just described. The strict violation by α passes to the limit and contradicts (1).

For technical regularity, vertices whose degrees differ from d form an o(|V|) set. Remove their incident edges and pad missing degrees with holding half-loops. Uniform bounded degree makes the number of affected edges o(|V|); the new graphs are d-regular as Markov multigraphs and still converge to X. Add d holding half-loops at every vertex to realize Q_n as a 2d-regular Markov graph. Such loops and walk multiplicities are compatible with Kun's analytic argument, which itself uses the graph of length-two walks. They do not contribute to any boundary.

Now apply **Kun v5, Theorem 3, implication (1)⇒(3)**, p. 2, proved on pp. 6–8, to (2). It gives a fixed η>0 and partitions into an exceptional part P_0 of vanishing size and parts P_i such that their total ambient boundary is o(|V|) and

\[
|E(U,V\setminus U)|\geq\eta|U|
\quad(U\subseteq P_i,\ 0<|U|\leq |P_i|/2).
\]

Here η is chosen from the fixed contraction parameter and degree; approximation accuracy changes the exceptional proportions and the index threshold. In Kun's proof this follows by smoothing small-boundary indicators and choosing level sets (Lemma 8, Corollary 9), then forming the partition. Thus η, and the final c, can be fixed from Γ,S alone.

For completeness, this partition already gives induced expanders without using the regularity-preserving rewiring. Delete P_0 and the endpoints W of every edge crossing between parts; |W|=o(|V|). For each i start at C_i=P_i\W. Its ambient-boundary potential is at most |∂P_i|+d|W∩P_i|, whose sum is o(|V|). Prune subsets U⊆C_i of size at most |C_i|/2 having internal boundary less than η|U|/4. The partition inequality applies because |U|≤|P_i|/2. Exactly the potential calculation above bounds total further deletion by 2Σ_i b(C_i)/η=o(|V|). No crossing edges remain. The surviving induced components have expansion ≥η/4. Transfer back across the initial o(|V|) regularization edits using the same endpoint deletion and pruning argument.

This supplies the unlabelled and uniform-constant interpretation of the published result. The finite graphs never needed consistent generator labels. A naive ultraproduct proof would fail precisely at the assertion that such labels automatically exist. A second insufficient argument would infer a full finite-graph spectral gap merely from convergence of spectral measures: Chapter 14, p. 206, explicitly explains why spectral supports do not converge. The marked-limit inequality and Kun's decomposition theorem are what handle these issues.

## Literature audit and surrounding results

Bowen's original source is cited by Kun as **L. Bowen, “Ergodic decompositions of sofic approximations,” manuscript, 2011**: reference [5], p. 13 of v5, and reference [2], p. 2379 of the published announcement. An accessible copy of that manuscript was not located. No theorem number or page in that unavailable manuscript is claimed. Pete's Conjecture 14.4 is the directly verified original problem statement.

The following primary texts were retrieved and their relevant statements checked. Page numbers below refer to the saved author/arXiv versions unless a journal page is specified.

| Work | Exact relevant location | What it establishes here |
|---|---|---|
| Pete, current notes, Chapter 14 | §§14.1–14.2, pp. 195–215; Conj. 14.4, p. 201 | Unlabelled convergence; the precise deletion quantifiers; the distinction from Cayley diagrams. |
| Kun, arXiv:1606.04471v5 (2019) | Thm. 1, pp. 1–2; Thm. 3, p. 2; Lemma 10, pp. 5–6; Prop. 11, p. 6; Lemma 14, p. 8 | Full proof of labelled essential expansion; Markov characterization; local Kazhdan estimate; rewiring. |
| Kun, published Oberwolfach contribution | Thm. 1, p. 2378; contribution pp. 2378–2379 | Explicit bounded-degree, unlabelled formulation resolving the conjecture. |
| Aldous–Lyons, *Processes on Unimodular Random Networks* | Thm. 3.2, author version pp. 17–18 | Unimodular decorations of a fixed transitive graph lift to invariant decorations; used above. |
| Lyons–Nazarov, *Perfect Matchings as IID Factors on Non-Amenable Groups*, EJC 32 (2011), 1115–1125 | Thm. 1.1, author version p. 2 | FIID perfect matchings in bipartite nonamenable Cayley graphs. It is a related factor-expansion result, not essential expansion for every approximation. |
| Abért–Elek, arXiv:1105.3200v3, *Hyperfinite actions on countable sets and probability measure spaces* | Thm. 1, p. 2 | Equivalent hyperfiniteness criteria for permutation actions, including hyperfinite Følner sequences. |
| Elek, arXiv:1204.0449v2, *Finite graphs and amenability*, JFA 263 (2012), 2593–2614 | Thms. 1–3, p. 3 | Hyperfiniteness of a convergent sequence iff that of its limit graphing; locality and strong equivalence of hyperfinite graphings. |
| Schramm, arXiv:0711.3808, *Hyperfinite graph limits*, ERA Math. Sci. 15 (2008), 17–23 | Thm. 1.1, preprint p. 3; quantitative Thm. 1.2, pp. 3–4 | Bounded-degree convergent sequences are hyperfinite iff their unimodular limits are hyperfinite. Pete restates the nontrivial direction as Thm. 14.8, p. 203. |
| Abért–Jaikin-Zapirain–Nikolov, arXiv:math/0701925v3, *The rank gradient from a combinatorial viewpoint*, GGD 5 (2011), 213–230 | Thms. 1, 3, p. 2; Thm. 5, p. 3 | Vanishing rank gradient in amenable cases; a strong-ergodicity trichotomy. These hypotheses differ from arbitrary sofic approximations. |
| Hutchcroft–Pete, arXiv:1810.11015v2, *Kazhdan groups have cost 1*, Invent. Math. 221 (2020), 873–891 | Thm. 1.2, p. 2 | Property-(T) groups have cost 1. This is distinct from expansion and does not assert fixed price 1. |
| Kun–Thom, arXiv:1901.03963v3, revised 4 August 2026 | Thm. 1.1 and Remark 1.2, p. 2; Thm. 1.4, p. 3 | Expanding Γ-generator subgraphs in approximations of Γ×Δ force Δ to be LEF. The single-expander hypothesis is stronger than Kun's decomposition. |
| Alekseev–Finn-Sell, arXiv:1608.02242v3, GGD 13 (2019), 191–234 | Thm. 7.4, preprint p. 29 | Independently restates Kun for bounded-degree, unlabelled Benjamini–Schramm convergence and negligible edge rewiring. |
| Bowen, arXiv:1704.06349v3 (2018), *Examples in the entropy theory of countable group actions* | §3.1.1, Example 1, p. 41 | Bowen himself records Kun's proof of the disjoint-expander conclusion for every sofic approximation. |
| Alekseev–Thom, arXiv:2406.06741v3, revised 15 June 2026 | Thm. 3.2, p. 6 | Restates Kun's essential-expander theorem and uses it in studying universal sofic groups. |
| Alekseev–Drigalla, arXiv:2511.16515v1 (2025) | Thm. B, p. 2 / Thm. 6.3, p. 30; Thm. C, p. 3 / Cor. 5.4, p. 20 | Strengthens the approximation statement to geometric property (T); characterizes approximate unions of expanders by ultraproduct spectral gap. |
| Alekseev–Thom, arXiv:2512.15494v1 (2025) | Def. 6.1 and following application of Kun, p. 12 | Explicitly uses the vertex-removal, induced-component version of essential expansion. |

Chapter 14 was read throughout, including unimodularity, the label obstruction, hyperfiniteness, spectral measures and their support warning, Lück approximation, tree entropy, graph polynomials, independence ratios, factor entropy, and percolation locality. The requested Lyons–Nazarov and Abért–Elek works were checked separately: Chapter 14 cites Lyons–Nazarov in its discussion of factors, but does not state those two papers' principal theorems there.

The local-versus-global comparison is particularly clear in Exercises 14.13 and 14.17, Definition 14.6, and Theorem 14.8: an expander limit must be nonamenable, but nonamenability alone does not force essential expansion; amenable limits force hyperfiniteness. Theorem 14.15 and Timár's example explain why graph limits do not automatically determine diagram limits.

This was a targeted search of the named works and later citations through **13 November 2026**, not an exhaustive citation index. No later paper checked reopens the essential-expansion conclusion. Unrelated recent claims about soficity were not used.

## Files and verification

- `sources/`: complete plain-text source conversions, including both Kun v1 and v5, the current Pete notes, all of Chapter 14, and the published announcement. No PDFs or images were written to disk.
- `data/source_manifest.jsonl`: source URLs, retrieval times, input-byte hashes, text hashes, byte counts and page counts. PDF input hashes were computed in memory before the bytes were discarded.
- `data/oberwolfach_crossref.json`: independent bibliographic check of the journal volume, issue, page range and actual publication date.
- `data/literature_search.txt`: search queries, primary landing pages, coverage and the unavailable Bowen-manuscript limitation.
- `code/fetch_text.py` and `code/fetch_related.py`: reproducible text-only retrieval, bounded downloads, sequential related-source processing.
- `LOG.md`: running task record.

Load-bearing checks were performed in two ways: Kun's theorem was read in both the journal announcement and the versioned full paper; the expansion normalization was compared directly with Pete's earlier definitions; the pruning bound was checked using the exact boundary identity and again by summing its nonnegative potential; publication details were cross-checked against publisher and Crossref metadata. The analytic discussion uses a lazy operator and only the forward part of Kun's characterization, avoiding an unwarranted absolute spectral-gap conclusion.

There are no simulation results: the literature stopping condition was met. All work stayed in this directory, with inherited nice priority 10, no subagents, and no heavy compute, publication or pushes.

Task: “Open problem C0149” — work began 13 November 2026, 09:13 +04 (Asia/Tbilisi); the prompt gives no separate receipt time.
