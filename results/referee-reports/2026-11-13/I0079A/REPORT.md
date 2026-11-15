COUNTEREXAMPLE

# I0079: nonunique low-intensity Bernoulli–Voronoi limits

There is a counterexample on the standard Cayley graph of
\[
\Gamma=C_2*C_3=\langle a,b\mid a^2=b^3=e\rangle,
\qquad S=\{a,b,b^{-1}\}.
\]
With Bernoulli nuclei of density \(p\), and ties resolved by one independent continuous priority per nucleus, the laws of the Voronoi equivalence relations have at least two different subsequential limits as \(p\downarrow0\). Uniqueness fails in the source's topology on IREs, already on the cylinder event \(e\mathrel r a\).

**Attribution and scope.** This example is already in Sandeep Bhupatiraju's 2019 thesis, Theorem 2.2, printed pp. 63–65 (PDF leaves 69–71). It is not a new counterexample. The classification above uses the requested status for a nonuniqueness example; the negative example was found in the literature. The proof below independently derives its marginal and proves the oscillation analytically, replacing the numerical separation at the end of the thesis proof. The same argument also covers \(C_2*K\) for every finite group \(K\) of order at least three, with generating set \(\{a\}\cup(K\setminus\{e\})\). No novelty claim is made for that extension.

This disproves unconditional uniqueness for all nonamenable groups, all exact groups, all groups of cost greater than one, all nonamenable free products, or all groups with infinitely many ends. It does not classify the groups or metrics with uniqueness, or settle the Kazhdan-group case. The metric and tie rule are fixed throughout; this is not a comparison between different metrics or different refinements.

## 1. Source identification and precise definitions

The intake source is **Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, [arXiv:2502.11622](https://arxiv.org/abs/2502.11622)**. Version 1 was submitted 17 February 2025; the accepted version, v2, is dated 27 March 2026. Question 2 is on v1 p. 18 and v2 p. 21. Both versions were retrieved. Its bibliography labels Bhupatiraju's thesis [Bhu10] and dates it 2010; the thesis title page and author's website establish May 2019.

Here are the definitions, with the mathematical conditions retained and prose restated.

**IRE and topology.** For a countable group \(\Gamma\), let
\[
\mathcal E=\{r\subseteq\Gamma\times\Gamma:r\text{ is an equivalence relation}\}
\subseteq\{0,1\}^{\Gamma\times\Gamma},
\qquad
(g\cdot r)(x,y)=r(g^{-1}x,g^{-1}y).
\]
Use the subspace product topology. An IRE is a \(\Gamma\)-invariant Borel probability measure on \(\mathcal E\). A FIRE has only finite classes almost surely. Weak convergence means convergence of the probabilities of every event specifying finitely many pairwise equivalences and inequivalences. The spaces \(\mathcal E\) and \(\operatorname{IRE}_\Gamma\) are compact metrizable. References: Definition 3.1, v1 p. 7 / v2 p. 8; finite and amenable IREs: Definition 3.6, v1 p. 8 / Definition 3.7, v2 p. 10.

**Amenable IRE.** There must be Borel maps \(\lambda_n:\mathcal E\to\operatorname{Prob}(\Gamma)\) such that for almost every \(r\) and every \(g\in[e]_r\),
\[
\|g^{-1}\cdot\lambda_n^r-\lambda_n^{g^{-1}\cdot r}\|_1\longrightarrow0.
\]
The restricted rerooting relation is
\[
R_{\rm re}=\{(r,g^{-1}\cdot r):g\in[e]_r\}.
\]
For a free IRE, amenability of this relation and of the IRE agree. For a nonfree IRE they need not agree; the corresponding restricted groupoid gives the general equivalence. References: Definition 3.8 and Remark 3.9, v1 p. 9; Definition 3.9 and Remark 3.10, v2 p. 10.

**Exactness.** A countable group is exact if it admits a topologically amenable action on a compact metrizable space \(X\). Topological amenability here means continuous maps \(\eta_n:X\to\operatorname{Prob}(\Gamma)\), with the \(\ell^1\) topology on probabilities, satisfying, for every \(g\in\Gamma\),
\[
\sup_{x\in X}\|g\cdot\eta_n^x-\eta_n^{g\cdot x}\|_1\longrightarrow0.
\]
This is Definition 2.1 and the following paragraph, v1 pp. 3–4.

**Bernoulli and ideal Bernoulli Voronoi tessellations.** Fix a proper left-invariant metric \(d\) on \(\Gamma\). For a nonempty nucleus configuration \(\omega\) and \(z\in\omega\), its unrefined cell is
\[
V_\omega(z)=\{x\in\Gamma:d(x,z)\le d(x,w)\text{ for every }w\in\omega\}.
\]
Boundary ties must be refined measurably and equivariantly to obtain a partition. The source allows several refinements and fixes one. For \(\Pi_p\) consisting of independently retained vertices with probability \(p\), the resulting partition law is \(\mathrm{BVT}_p\). Its cells are finite almost surely by Lemma 6.1, v1 p. 17 / v2 p. 20. The source calls subsequential weak limits as \(p\downarrow0\) ideal Bernoulli Voronoi tessellations; on a nonamenable group they cannot be the full IRE. These definitions are in §6, v1 pp. 17–18 / v2 pp. 19–21.

For our fixed refinement, take iid \(U_z\sim\mathrm{Unif}[0,1]\), declare \(z\) a nucleus when \(U_z<p\), and allocate \(x\) to the nucleus minimizing \((d(x,z),U_z)\) lexicographically. Conditional on occupancy, the priorities are iid continuous variables, so this is exactly the usual independent-priority refinement. It is fixed for all \(p\), is equivariant, and gives geodesically connected cells.

**Ideal Poisson–Voronoi tessellation.** In the metric-measure setting, replace Bernoulli nuclei by a PPP of intensity \(\lambda\mu\); the cells satisfy the same weak distance inequalities. An IPVT is the nontrivial limiting diagram when such a low-intensity limit exists, or an appropriate subsequential ideal diagram when only subsequences are available. In a boundary description its nuclei are \((\theta_i,\delta_i)\), with horofunctions \(h_{\theta_i}\) normalized at an origin, and
\[
C_i=\{x:h_{\theta_i}(x)+\delta_i\le h_{\theta_j}(x)+\delta_j\text{ for all }j\}.
\]
For real hyperbolic space \(\mathbb H_d\), the full Poisson limit exists and has locally finite convex cells with disjoint interiors. Diagrams are treated as ordered sequences of closed sets with the product Fell topology, not as the discrete equivalence-relation space above. See D'Achille–Curien–Enriquez–Lyons–Ünel, arXiv:2303.16831v3, §2, pp. 7–10, Theorem 2.3, and Theorem 1.1, p. 3. In general graphs, weak cells may overlap, so an unrefined ideal diagram is not automatically an IRE.

**Cell selection and indistinguishability.** The source identifies \(r\) with \(x\mapsto[x]_r\). Its displayed definition requires a measurable equivariant map
\[
\phi:\mathcal E\longrightarrow(2^\Gamma)^\Gamma,
\qquad \phi_r(x)\in\{[x]_r,\varnothing\}.
\]
It describes such a map as selecting cells, and calls selection of every cell or of no cells trivial. An IRE is called indistinguishable when it admits no nontrivial cell selection rule. This is the paragraph after Question 2, v1 p. 18 / v2 p. 21, leading to **Question 3**. It concerns selection within a sampled tessellation, not uniqueness of its law as intensity tends to zero.

**The source's theorem.** For every countable discrete group,
\[
\Gamma\text{ exact}\quad\Longleftrightarrow\quad
\overline{\operatorname{FIRE}_\Gamma}
=\operatorname{AIRE}_\Gamma.
\]
For arbitrary groups every AIRE belongs to that closure (Proposition 3.10, v1 p. 9; Proposition 3.11, v2 pp. 10–11). For exact groups the reverse inclusion is Theorem 4.5, v1 p. 11 / v2 p. 14, announced as Theorem 1.2, p. 2. Every nonexact group has a nonamenable weak limit of FIREs: Theorem 5.1, v1 p. 12 / v2 p. 15, announced as Theorem 1.1, p. 2. Thus all ideal Bernoulli limits on an exact group are amenable IREs. No uniqueness assertion follows. The quantifier covers every countable exact group, not just a particular family of Cayley graphs; the negative theorem covers every countable nonexact group.

## 2. Analytic proof of the counterexample

Write \(o=e\), \(v=a\), and \(q=1-p\). The \(a\)-edge \(\{o,v\}\) is a bridge. Removing it gives two isomorphic rooted halves, each a tree of triangles. In the half rooted at \(o\), the numbers of vertices at distance \(n\) are
\[
h_n=2^{\lceil n/2\rceil}\quad(n\ge0).
\]
Indeed, a reduced word in that half starts with \(b\) or \(b^{-1}\) and then alternates a two-choice \(C_3\)-letter with the unique \(a\)-letter. On the other half every distance from \(o\) is one larger than its distance from \(v\).

Let \(s_n=|S(o,n)|\), \(B_n=|B(o,n)|\). Consequently,
\[
s_{2k}=2\,2^k\ (k\ge1),\qquad s_{2k+1}=3\,2^k\ (k\ge0),
\]
\[
B_{2k}=7\,2^k-6,\qquad B_{2k+1}=10\,2^k-6\quad(k\ge0).
\tag{1}
\]
In particular \(B_0=1\). These reproduce the thesis's equation (2.41), p. 62.

### The single-edge marginal

Denote the selected nucleus of \(x\) by \(c(x)\). If \(c(v)\) lies on the \(o\)-side of the bridge, then \(c(o)=c(v)\): a closest-nucleus allocation with global priorities is constant along a shortest path to its nucleus. Conversely, if both endpoints share a nucleus, that nucleus lies on one of the two sides. The two possible crossing events are disjoint and have the same probability by symmetry.

The probability that \(c(v)\) is at distance \(n+1\) is \(q^{B_n}-q^{B_{n+1}}\). Conditional on this distance it is uniform on that sphere, by exchangeability of the iid labels, irrespective of the graph's sphere symmetries. Exactly \(h_n\) of the \(s_{n+1}\) sphere vertices lie across the bridge. Therefore, for every \(0<q<1\),
\[
P_p:=\mathbb P(c(o)=c(v))
=2\sum_{n\ge0}\frac{h_n}{s_{n+1}}
       (q^{B_n}-q^{B_{n+1}}).
\tag{2}
\]
All terms are nonnegative. The ratio is \(1/3\) for even \(n\) and \(1/2\) for odd \(n\). Splitting off a telescoping sum gives the exact formula
\[
P_p=\frac{2q}{3}
 +\frac{q^{-6}}{3}\sum_{k\ge1}
       (q^{5\,2^k}-q^{7\,2^k}).
\tag{3}
\]
This derivation does not assume that the whole Cayley graph is bipartite. It contains triangles; only the bridge property is used. The thesis's sentence calling it bipartite on p. 62 is unnecessary and incorrect.

### Phase limits and a nonzero Fourier coefficient

Put \(t=-\log q\). For any fixed \(c>0\), take
\[
t_N=c\,2^{-N},\qquad p_N=1-\exp(-t_N).
\]
Reindexing the series in (3) yields
\[
\lim_{N\to\infty}P_{p_N}
=\frac23+\frac13F(c),\qquad
F(c)=\sum_{j\in\mathbb Z}
       (e^{-5c2^j}-e^{-7c2^j}).
\tag{4}
\]
For \(c\) in a compact subinterval of \((0,\infty)\), the negative tail is bounded by a constant times \(\sum_{j<0}2^j\), and the positive tail by a doubly exponentially decaying series. This proves local uniform convergence and justifies the limit. In particular \(F\) is continuous and \(F(2c)=F(c)\).

To prove that this periodic function is nonconstant without numerics, set
\[
L=\log2,\qquad \omega=2\pi/L,\qquad H(x)=F(e^x).
\]
Its first Fourier coefficient is, by absolute integrability and periodization,
\[
\begin{aligned}
\widehat H(1)
&=\frac1L\int_0^L H(x)e^{-i\omega x}\,dx\\
&=\frac1L\int_0^\infty
  (e^{-5u}-e^{-7u})u^{-i\omega-1}\,du\\
&=\frac{\Gamma(-i\omega)}L
       (5^{i\omega}-7^{i\omega}).
\end{aligned}
\tag{5}
\]
The last identity follows by integration by parts and the gamma integral at \(1-i\omega\); both boundary terms vanish. The gamma factor is nonzero, for instance by
\(\Gamma(i\omega)\Gamma(-i\omega)=\pi/(\omega\sinh(\pi\omega))>0\).
The other factor could vanish only if \(\log_2(7/5)\) were an integer, whereas \(1<7/5<2\). Thus \(\widehat H(1)\ne0\), so \(F\) is nonconstant. Equations (4)–(5) prove that the edge marginal has at least two distinct limits.

### From a marginal to two ideal IRE laws

Each finite-intensity partition is invariant and has finite classes. For completeness, send mass one from each vertex to its nucleus. Invariance gives
\(\mathbb E[\mathbf1_{\{e\text{ nucleus}\}}|C(e)|]=1\), hence every nucleus cell is finite almost surely; use countability to cover all nuclei.

Choose \(c_1,c_2>0\) with \(F(c_1)\ne F(c_2)\). Compactness of \(\operatorname{IRE}_\Gamma\) gives a weakly convergent subsubsequence of each corresponding phase sequence. If the limiting laws are \(\rho_1,\rho_2\), then the clopen event \(\{r:o\mathrel r v\}\) has respective probabilities \(2/3+F(c_i)/3\), so \(\rho_1\ne\rho_2\). Both are ideal Bernoulli Voronoi tessellations in the source's definition.

They are nontrivial. Every summand in \(F(c)\) is positive, and
\[
e^{-5c2^j}-e^{-7c2^j}
< e^{-5c2^j}-e^{-10c2^j}.
\]
Summing the latter telescopically over \(j\in\mathbb Z\) gives one. Hence \(0<F(c)<1\), and both displayed edge probabilities lie strictly between \(2/3\) and one. Neither limiting law is the full or equality IRE. Moreover every limiting class is infinite: for fixed \(R\), failure of an open path from a vertex to its radius-\(R\) sphere is a finite-edge event and, at positive intensity, forces the cell's nucleus into the radius-\(R\) ball. Its probability is at most \(p|B_R|\), which tends to zero. Apply this for all vertices and radii. This last observation is not needed to distinguish the laws.

### A family of counterexamples

Let \(K\) be any finite group with \(|K|=m\ge3\), put \(a=m-1\) in the following formulas, and equip \(C_2*K\) with \(S=\{\text{the }C_2\text{ generator}\}\cup(K\setminus\{e\})\). Its Cayley graph is a tree of complete \(m\)-vertex graphs joined by bridge edges. The preceding calculation gives
\[
h_n=a^{\lceil n/2\rceil},\quad
B_{2k}=\frac{3a+1}{a-1}a^k-\frac{2(a+1)}{a-1},\quad
B_{2k+1}=\frac{a(a+3)}{a-1}a^k-\frac{2(a+1)}{a-1}.
\]
Write
\[
A=\frac{a+3}{a-1},\quad B=\frac{3a+1}{a-1},\quad D=\frac{2(a+1)}{a-1}.
\]
The bridge marginal is
\[
P_p=\frac{2q}{a+1}
 +\frac{a-1}{a+1}q^{-D}
       \sum_{k\ge1}(q^{Aa^k}-q^{Ba^k}).
\tag{6}
\]
Its phase function is \(F_a(c)=\sum_{j\in\mathbb Z}(e^{-Ac a^j}-e^{-Bc a^j})\). The Fourier coefficient in (5), with \(L=\log a\), is proportional to \(A^{i\omega}-B^{i\omega}\). It is nonzero because
\[
1<\frac BA=\frac{3a+1}{a+3}<a\qquad(a\ge2).
\]
Thus the same nonuniqueness conclusion holds for the whole family.

These groups are nonamenable, virtually free, exact, and have infinitely many ends: the kernel of the natural map to \(C_2\times K\) has index \(2m\) and is free of rank \(m-1\ge2\). Their fixed price is
\[
(1-1/2)+(1-1/m)=3/2-1/m>1,
\]
by the finite-group cost formula and free-product additivity. For the original example it is \(7/6\). References: Gaboriau, *Coût des relations d'équivalence et des groupes*, [author's copy](https://perso.ens-lyon.fr/gaboriau/Travaux-Publi/Cout/Cout.pdf), Proposition III.3, printed p. 58, and Theorem IV.15, printed p. 63. These properties therefore do not guarantee uniqueness for a fixed Cayley metric. There is no conflict with the source's exactness theorem: the distinct limits are all amenable IREs.

## 3. Literature audit

Page numbers below refer to the saved arXiv version's printed pages, except where thesis or journal pagination is expressly given. Source text files retain form-feed page boundaries. This audit was conducted on 13 November 2026.

| Work | Exact result checked | Relevance and limitation |
|---|---|---|
| Bhupatiraju, *The Low-Intensity Limit of Bernoulli–Voronoi and Poisson–Voronoi Measures*, Indiana University PhD thesis, May 2019. [Repository text source](https://scholarworks.iu.edu/dspace/bitstreams/145f12de-8c9f-4192-ba8f-a533f7f4fed4/download). | Theorem 2.1, p. 6: full nontrivial Bernoulli limit on regular trees. **Theorem 2.2, pp. 63–65: no full limit on the standard Cayley graph of \(C_2*C_3\)**. Model and tie rule: p. 5. | The decisive negative result, predating the intake paper. PDF leaves are printed page plus six in Chapter 2. |
| Thomas Budzinski, Nicolas Curien, Bram Petri, *On Cheeger constants of hyperbolic surfaces*, [arXiv:2207.00469v1](https://arxiv.org/abs/2207.00469); Invent. Math. 242 (2025), 511–530. | Theorem 1, arXiv p. 1: asymptotic upper bound \(2/\pi\) for the Cheeger constants in large genus; §2.2 develops the low-intensity hyperbolic Voronoi argument. | Earlier “pointless” tessellation motivation, not general Bernoulli uniqueness. |
| Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson–Voronoi tessellations on hyperbolic spaces*, [arXiv:2303.16831v3](https://arxiv.org/abs/2303.16831), 10 June 2025; Ann. Probab. 54 (2026), 846–891. | Theorem 1.1, p. 3: full Poisson convergence on \(\mathbb H_d\), \(d\ge2\). Theorem 2.3, pp. 9–10: deterministic diagram convergence. Theorem 6.2, p. 46: vertex restrictions of edge-Poisson tree limits have the same law for all phases, citing Bhupatiraju. Proposition 6.4, p. 47: the full metric-tree diagrams retain the phase. | A continuum diagram can be nonunique even when its restriction to vertices is unique; this cannot be transferred indiscriminately to IREs. |
| Mikołaj Frączyk, Sam Mellick, Amanda Wilkens, *Poisson–Voronoi tessellations and fixed price in higher rank*, [arXiv:2307.01194v1](https://arxiv.org/abs/2307.01194), 3 July 2023. | Theorem C, p. 2, and Theorem D, p. 3: fixed price one for higher-rank semisimple real Lie groups/products of regular-tree automorphism groups and their lattices. Theorem 3.6, p. 18: limiting invariant measure. Theorem 6.1, p. 29: unbounded IPVT cell walls. | Boundary measure construction and fixed price do not themselves prove full low-intensity convergence of diagrams on arbitrary Cayley graphs. |
| Sam Mellick, *Indistinguishability of cells for the ideal Poisson Voronoi tessellation*, [arXiv:2408.10009v3](https://arxiv.org/abs/2408.10009); Proc. AMS 154 (2026), 1589–1596. | Theorem 1, arXiv p. 1: indistinguishable cells on symmetric spaces and products of regular trees. | Answers the continuum cell-selection question, not Question 2 about uniqueness of laws. |
| Matteo D'Achille, *Ideal Poisson–Voronoi tessellations beyond hyperbolic spaces*, [arXiv:2412.00822v1](https://arxiv.org/abs/2412.00822). | Theorem 1.1, p. 2, expanded as Theorem 2.1, pp. 4–5: full convergence on \(\mathbb H_2\times\mathbb H_2\) with the \(L^1\) metric. Theorem 1.3, pp. 2–3: unbounded equal-separation sets. | A specific continuum product metric, not arbitrary lattices with word metrics. |
| Jan Grebík, Konstantin Recke, *Poisson-Voronoi percolation in higher rank*, [arXiv:2504.02435v1](https://arxiv.org/abs/2504.02435). | Theorem 1.1, p. 1: the colored-percolation uniqueness threshold tends to zero for higher-rank symmetric spaces with property (T). Remark 1.2, p. 2, explicitly distinguishes this from convergence of the underlying tessellations. | A “uniqueness threshold” is not uniqueness of an ideal tessellation law. |
| Ali Khezeli, *Products of Infinite Countable Groups Have Fixed Price One*, [arXiv:2509.08325v4](https://arxiv.org/abs/2509.08325), 4 January 2026. | Theorem 1.1, p. 2: fixed price one for products of two infinite countable groups. | Uses suitable subsequential horoball constructions; does not assert universal Bernoulli-limit uniqueness. |
| Erin Bevilacqua, Lewis Bowen, *Metric criteria for fixed price of countable groups*, [arXiv:2510.05459v1](https://arxiv.org/abs/2510.05459). | Theorem 1.2, p. 5: product fixed-price criterion under metric growth hypotheses. | A metric criterion for fixed price, not a general uniqueness theorem. |
| Matteo D'Achille, Jan Grebík, Ali Khezeli, Konstantin Recke, Amanda Wilkens, *Vanishing uniqueness thresholds in Voronoi percolation on products*, [arXiv:2511.23317v1](https://arxiv.org/abs/2511.23317). | Theorems 1–2, p. 2: vanishing colored-percolation uniqueness thresholds for equal-degree tree products and products of hyperbolic spaces. | Again concerns percolation thresholds, not full uniqueness in Question 2. |
| Matteo D'Achille, Ali Khezeli, *Convergence towards Ideal Poisson–Voronoi tessellations with a focus on Diestel–Leader graphs*, [arXiv:2606.30517v2](https://arxiv.org/abs/2606.30517), 20 July 2026. | Proposition 1.1, p. 4: full continuum convergence on symmetric spaces. Theorem 1.2, p. 4: necessary/sufficient criteria for shifted nuclei convergence, plus diagram convergence under nondegeneracy. Theorem 1.3, p. 5: graph phase limits. Lemma 4.9, p. 25: Poisson/Bernoulli equivalence for vertex nuclei under stated growth hypotheses. Theorem 1.5, p. 6, and Corollary 1.6, pp. 6–7: phase independence on vertices/midpoints for certain **edge-measured** graphs. | Important new convergence results, but they distinguish vertex nuclei, edge nuclei, and tie-sensitive restrictions. No assertion of uniqueness for all nonamenable, cost-greater-than-one, free-product, or Kazhdan groups. |
| Matteo D'Achille, Christoph Thäle, *Face volume densities of positive-intensity and ideal Poisson–Voronoi tessellations in hyperbolic spaces*, [arXiv:2606.26049v1](https://arxiv.org/abs/2606.26049). | Theorem 1.1, p. 5: hyperbolic Poisson face-volume-density formulas. | Geometric statistics, not a group uniqueness result. |
| Colin Davalo, J. Maxwell Riestenberg, Anna Wienhard, *Ideal Poisson–Voronoi tessellations for Finsler metrics on symmetric spaces*, [arXiv:2610.17045v1](https://arxiv.org/abs/2610.17045). | Theorem B, p. 6 (Theorem 5.2): convergence of renormalized measures for polyhedral Finsler norms to a specified invariant horofunction measure. | Further metric-dependent continuum theory, not universal uniqueness of Bernoulli partitions. |

For the requested Paquette branch, the retrieved primary works are **Itaï Benjamini, Elliot Paquette, Joshua Pfeffer**, *Anchored expansion, speed, and the hyperbolic Poisson Voronoi tessellation*, [arXiv:1409.4312v2](https://arxiv.org/abs/1409.4312), Theorem 1.4, p. 4 (positive anchored expansion at positive intensity), and **Elliot Paquette**, *Distributional Lattices on Riemannian symmetric spaces*, [arXiv:1707.00308v2](https://arxiv.org/abs/1707.00308), Theorems 1.6–1.7, p. 6 (amenability characterizations). These do not prove low-intensity uniqueness. I found no matching ideal-tessellation paper coauthored by Lafont–Raimbault, nor a joint “Mellick–Bhupatiraju–…” paper. Those author strings are unverified intake hints; no title or theorem has been invented for them.

## 4. Verification and reproducibility

The proof of nonconvergence is (1)–(5); numerical values play no role in it. The broader family follows from (6) by the same Fourier calculation.

`python3 code/check_counterexample.py` independently enumerates reduced words in \(C_2*C_3\), checks sphere and ball counts through radius 14, and checks that distances across the bridge differ by one. It also computes the same finite-volume edge probability in two ways using exact rational arithmetic: integrating each candidate nucleus's priority against its closer/tied competitors, and summing the two bridge-crossing events. All three rational checks agree. There are 890 normal forms in the checked radius-14 ball. Two further exact checks verify the finite-cutoff telescoping identity behind (3); 209 checks compare the family's ball formulas with sums of its half-shell counts.

As evidence only, 60-digit decimal evaluation gives phase edge limits approximately 0.828476562095073 and 0.828474706825824 for the thesis's phase choices 0.2 and 0.1. The report proves they cannot all coincide by the nonzero Fourier coefficient, rather than by these decimals. Checks and values are saved in `data/counterexample_checks.json`.

All downloaded papers were converted to plain text using `pdftotext -layout - -`, with PDF bytes held in memory only. `code/fetch_text.py` records URLs, retrieval dates, hashes, and page counts in `data/sources.jsonl`; the directly fetched thesis and Gaboriau paper have separate manifest entries. `data/source_index.json` records actual version strings read from the saved texts, their page counts, and hashes. There are 18 plain-text source files; `sources/INDEX.txt` gives their pagination. No PDFs, images, scans, publications, or pushes were created. Conversion and check scripts inherited nice 20, with numerical-library thread counts set to one; no simulations or subagents were used.

Task: “Open problem I0079” — 13 November 2026; first recorded local clock time 19:57 +04.
