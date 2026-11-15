PARTIAL

# D0070: the minimum connective constant at fixed degree

Let \(\mathcal G_\Delta\) consist of infinite, connected, vertex-transitive, simple graphs of degree \(\Delta\), and put
\[
\mu_{\min}(\Delta)=\inf_{G\in\mathcal G_\Delta}\mu(G).
\]
The full problem is not solved here. The literature search found no resolution. In particular, Grimmett's October 2026 revision of *Connective constants of Grigorchuk graphs* explicitly retains the unrestricted cubic question as Question 1.1, pp. 1–2. Its new results concern Grigorchuk Cayley graphs, not all transitive graphs. [arXiv:2608.19349v2](https://arxiv.org/abs/2608.19349v2).

This report proves the following partial statement, by an explicit family and an elementary asymptotic calculation:
\[
\boxed{\quad
\sqrt{\Delta-1}\leq \mu_{\min}(\Delta)
\leq \mu(K_\Delta*K_2)
=\Delta-(1+o(1))\sqrt{\Delta\log\Delta}.
\quad}
\]
Here \(*\) is the free product of rooted graphs, not a Cartesian product. The lower inequality is the published Grimmett–Li theorem. The free-product formula is also published; its specialization and the displayed asymptotic are proved below, without a novelty claim. A consequence is that **\(\mu_{\min}(\Delta)=\Delta-O(1)\) is false**. This does not determine the order of \(\mu_{\min}\), or even establish \(\mu_{\min}(\Delta)/\Delta\to1\).

For degree three, the verified general bounds remain
\[
\sqrt2\leq\mu_{\min}(3)\leq\phi=(1+\sqrt5)/2.
\]
No improved universal cubic lower bound, new class beyond the published results, or cubic counterexample was obtained. Complete elementary proofs of the ladder equality and the published transitive-height-function case are included to make the gap precise. Exact enumeration supplies evidence and checks, not a resolution.

## 1. Exact class and literature audit

The requested survey is saved in `sources/survey-1704.05884v1.txt`; its 2019 revision is also saved. Sections 2–3 of v1 were read in full: Section 2 starts on PDF p. 8, Question 2.3 is on p. 10, Section 3 starts on p. 11, and Question 3.4 is on p. 13. The section ends on p. 14. The authors' class \(\mathcal G\) is defined in Section 2.1, pp. 8–9, separately from the quasi-transitive class \(\mathcal Q\). Cayley graphs are a subclass of \(\mathcal G\), not the definition of the question's class. Rooting does not affect \(\mu\). [Survey, v1](https://arxiv.org/abs/1704.05884v1).

Three distinctions matter:

- The sharpness example \(B_\Delta\) for the square-root bound has parallel edges, so it cannot establish sharpness in \(\mathcal G_\Delta\).
- Replacing vertex-transitivity by quasi-transitivity changes the question: degree-regular examples with \(\mu=1\) exist. This is discussed before Theorem 4.1 of the regular-graph paper, author-final p. 6.
- A graph height function may be invariant under a group having several vertex orbits. The published cubic theorem requires a **transitive** graph height function. The bridge theorem alone does not remove that qualification.

The following table gives exact locations in the versions actually retained. “PDF p.” means the page of that source, identifiable by form-feed boundaries in the extracted text. Journal publication details and arXiv page numbers are kept separate.

| Source | Verified result and location | Consequence for D0070 |
|---|---|---|
| G. R. Grimmett and Z. Li, *Bounds on connective constants of regular graphs*, **Combinatorica 35** (2015), 279–294, DOI [10.1007/s00493-014-3044-0](https://doi.org/10.1007/s00493-014-3044-0); [arXiv:1210.6277v2](https://arxiv.org/abs/1210.6277v2) | Theorem 1.1, p. 1; Theorem 4.1, p. 6 in the arXiv text and author-final text: \(\mu\ge\sqrt{\Delta-1}\) for the simple transitive class. Author-final p. 6 explains the quasi-transitive obstruction. | Best unconditional degree-only lower bound verified in this search. The weaker hypotheses under which equality occurs do not make it sharp for simple transitive graphs. |
| Grimmett and Li, *Cubic graphs and the golden mean*, **Discrete Mathematics 343** (2020), article 111638, DOI [10.1016/j.disc.2019.111638](https://doi.org/10.1016/j.disc.2019.111638) | **Published text**: Theorem 3.1(b), p. 4, transitive graph height functions; Theorem 8.1, p. 15, the specified first-Grigorchuk Cayley graph; Theorem 9.1, p. 17, infinite transitive TLF-planar cubic graphs; Theorem 10.1, p. 25, two-ended Cayley graphs; Theorem 10.2, p. 25, qualified statements for infinitely many ends. | These are existing positive subclasses. Theorem 10.2 does not cover every infinitely-ended transitive cubic graph or every generating set in every case. |
| Grimmett and Li, *Connective constants and height functions for Cayley graphs*, **Transactions AMS 369** (2017), 5961–5980, DOI [10.1090/tran/7166](https://doi.org/10.1090/tran/7166); [arXiv:1501.00476v5](https://arxiv.org/abs/1501.00476v5) | Theorem 3.4, arXiv p. 6, constructs harmonic height functions under specified finite-index hypotheses. Theorem 4.1, arXiv pp. 7–8, characterizes group height functions by the relation coefficient matrix. | Provides existence machinery; it does not supply height functions for every Cayley graph. A nonzero homomorphism to \(\mathbb Z\) supplies a transitive height function. |
| Grimmett and Li, *Self-avoiding walks and amenability*, **Electronic Journal of Combinatorics 24** (2017), P4.38; [arXiv:1510.08659v2](https://arxiv.org/abs/1510.08659v2) | Theorem 6.2, arXiv p. 9: \(\mu\ge(\Delta-1)^{(1+c\lambda)/2}\), \(c=\Delta(\Delta-1)/(\Delta-2)^2\), \(\lambda=1-\rho\). Theorem 5.1, p. 8, excludes graph height functions on the first Grigorchuk Cayley graph. | Spectral information improves the lower bound for individual nonamenable graphs, but supplies no fixed positive spectral gap across the question's entire class. |
| C. Lindorfer, *A general bridge theorem for self-avoiding walks*, **Discrete Mathematics 343** (2020), article 112092, DOI [10.1016/j.disc.2020.112092](https://doi.org/10.1016/j.disc.2020.112092); [arXiv:1902.08493v2](https://arxiv.org/abs/1902.08493v2) | Theorem 3.2, arXiv p. 5: \(\mu=\max\{\beta(h),\beta(-h)\}\) for a graph height function, without unimodularity. | An equality of growth constants, not a numerical lower bound of \(\phi\) for arbitrary cubic graphs. No separate Lindorfer theorem settling the stated minimum was located. |
| A. Georgakopoulos and A. Wendland, *A study of 2-ended graphs via harmonic functions*, [arXiv:2304.13317v1](https://arxiv.org/abs/2304.13317v1) | Theorem 1.3, p. 3, and its proof, pp. 10–11: golden-mean lower bound for the nondegenerate two-ended transitive case, including every cubic graph in that class. | Extends the Cayley case to transitive graphs that need not be Cayley. The infinite path must be excluded: it has \(\mu=1\); the theorem's printed introductory wording omits this exception, while the surrounding discussion makes it clear. |
| C. Panagiotis, *Self-avoiding walks and polygons on hyperbolic graphs*, [arXiv:1908.00127v2](https://arxiv.org/abs/1908.00127v2) | Theorem 2, p. 2: for fixed face degree \(k\), the regular hyperbolic tessellations satisfy \(\mu(H(d,k))=d-1-O(1/d)\). | A family-specific asymptotic, not a lower bound for all degree-\(d\) transitive graphs. |
| L. A. Gilch and S. Müller, *Counting self-avoiding walks on free products of graphs*, **Discrete Mathematics 340** (2017), 325–332; [arXiv:1509.03209v1](https://arxiv.org/abs/1509.03209v1) | Theorem 3.3 and Corollary 3.4, arXiv p. 6: the free-product connective constant is determined by \(\sum_i M_i(z)/(1+M_i(z))=1\). Example 5.1, p. 8, gives \(\mu(K_3*K_2)\approx1.76929\). | Supplies explicit admissible families, including the upper construction in Section 4 below. |
| G. R. Grimmett, A. E. Holroyd and Y. Peres, *Extendable self-avoiding walks*, **Annales IHP D 1** (2014), 61–75; [arXiv:1307.7132v2](https://arxiv.org/abs/1307.7132v2) | Theorem 1, arXiv p. 2: equality of ordinary and forward/backward/doubly extendable growth constants under the stated quasi-transitive hypotheses. | Does not increase the numerical lower bound. |
| S. Martineau, *The set of connective constants of Cayley graphs contains a Cantor space*, [arXiv:1608.03478v2](https://arxiv.org/abs/1608.03478v2) | Unnumbered main Theorem, p. 1. | Richness of possible values does not determine their minimum at fixed degree. |
| N. Aubrun and N. Bitar, *Self-Avoiding Walks on Cayley Graphs Through the Lens of Symbolic Dynamics*, **Electronic Journal of Combinatorics 31** (2024), P4.24, [published text](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i4p24) | Theorem 63, p. 35, periodic-point approximation under transitive height functions; Proposition 65, pp. 36–37, a polygon-count criterion for lower bounds. | Bounds depend on the polygon counts; this is not a universal replacement for the square-root bound. |
| G. R. Grimmett, *Connective constants of Grigorchuk graphs*, [arXiv:2608.19349v2](https://arxiv.org/abs/2608.19349v2), 7 October 2026 | Question 1.1, p. 1, retains the general cubic problem. Theorem 1.2, p. 2, proves \(\mu\ge\phi\) for genuine cubic three-generator general Grigorchuk Cayley graphs, with strict inequality when the encoding contains all three symbols. Theorem 3.1(b,c), pp. 6–7, gives quantitative refinements. | Major later subclass result; explicitly not a general resolution. |
| B. Grant and Z. Li, *Self-avoiding walks on cubic graphs and local transformations*, [arXiv:2601.12571v2](https://arxiv.org/abs/2601.12571v2) | Theorem 3.3, p. 5: a generating-function substitution for symmetric three-port gadgets on quasi-transitive cubic graphs. | Does not guarantee vertex-transitivity of every transformed graph or solve the minimum problem. |
| G. R. Grimmett, *SAWs, trails, kites, patterns*, [arXiv:2611.00816v1](https://arxiv.org/abs/2611.00816v1), 31 October 2026 | Theorem 1.2, p. 2, compares SAW and trail constants under transitive height functions; Theorem 7.2, p. 31, concerns clique replacements and restricted SAWs. | No universal degree-only lower bound resolving D0070. |

The 2017–2026 search included the named authors and titles, later work citing the regular-graph and cubic papers, and searches for degree-dependent lower bounds, the sharp minimum, and the golden-mean conjecture. Search queries and scope are recorded in `data/literature-search.txt`. This is an audit of located sources, not a proof that no later or unindexed paper exists.

## 2. Extremal examples and the remaining gap

**Ladder.** On \(V=\mathbb Z\times\{0,1\}\), join \((x,i)\) to \((x-1,i),(x+1,i),(x,1-i)\). This is the Cayley graph of \(\mathbb Z\times C_2\) for the inverse-closed generating set
\[
\{(1,0),(-1,0),(0,1)\}.
\]
It is simple, connected, infinite, transitive and cubic. Section 3 proves \(\mu=\phi\), so the golden-mean conjecture, if true, is sharp and attained.

**Hexagonal lattice.** Its value is \(\sqrt{2+\sqrt2}\approx1.847759065>\phi\), not \(\phi\). It is a positive example for the conjecture, not an extremizer. The exact value is Duminil-Copin–Smirnov, *Annals of Mathematics* **175** (2012), 1653–1665, Theorem 1 (retained arXiv text p. 2); the survey records it in equation (1.4), p. 4. [Journal source](https://annals.math.princeton.edu/2012/175-3/p14).

**Regular tree.** \(\mu(T_\Delta)=\Delta-1\), since \(c_n=\Delta(\Delta-1)^{n-1}\) for \(n\ge1\). This is the upper extremum, not the lower one.

**Bridge multigraph.** On the vertex set \(\mathbb Z\), give successive links alternately one and \(\Delta-1\) parallel edges. A SAW moves monotonically along the underlying line; the product of the alternating multiplicities gives \(\mu=\sqrt{\Delta-1}\). The graph is transitive, but is not simple for \(\Delta\ge3\).

**Quasi-transitive obstruction.** For an explicit simple cubic example with \(\mu=1\), attach to every vertex of an infinite line a separate copy of \(K_4\) with one edge subdivided, joining the subdivision vertex to the line vertex by a new edge. Every degree is three and there are finitely many vertex orbits. A SAW can occupy an attached finite piece only at an end of its path; its middle travels monotonically along the line. Endpoint pieces have uniformly bounded size and finitely many possibilities, so the counts have at most polynomial growth and \(\mu=1\). This graph is not vertex-transitive.

The Fisher transformation must also be used with care. The survey's Theorem 3.1, pp. 11–12, proves convergence of iterated transformed **quasi-transitive** cubic graphs to \(\phi\). A replacement vertex corresponds to a flag of the old graph; transitivity on old vertices does not imply transitivity on flags. Iteration therefore does not automatically produce eligible examples in \(\mathcal G_3\).

## 3. Complete elementary proofs of the cubic benchmark cases

### 3.1 The ladder has connective constant \(\phi\)

Write \(E\) for a horizontal step to the right and \(V\) for a vertical rung. Every word in \(E,V\) with no consecutive \(V\)'s describes a SAW from a fixed root. Horizontal steps increase the column, and a column contains at most one rung step. The number \(a_n\) of such words of length \(n\) satisfies
\[
a_0=1,\quad a_1=2,\quad a_n=a_{n-1}+a_{n-2}.
\]
Thus \(a_n=F_{n+2}\) and \(\lim a_n^{1/n}=\phi\), by solving the recurrence with characteristic equation \(x^2=x+1\). This proves \(\mu\ge\phi\).

For the upper bound, ignore rung steps when listing the signs of the horizontal steps of an arbitrary ladder SAW. The sign changes at most twice. To prove this, a change of sign must use the rung at its turning column: immediate horizontal reversal would revisit the preceding vertex. At such a rung both vertices of that column have been visited, so the rest of the walk cannot cross that column. If there are two successive turns, say at columns \(b<a\), the later path is trapped strictly between these columns. The portion between the two turns already visited at least one vertex of every intervening column. A later rung there would therefore revisit a vertex. Consequently no third turn is possible. The same argument applies with left and right exchanged.

Split the walk at its horizontal direction changes into at most three horizontally monotone segments. A monotone segment of length \(j\), fixed starting vertex and fixed horizontal direction has at most \(a_j\le2\phi^j\) possibilities. There are at most \(2^3\) choices of the segments' directions and \(\binom{n+2}{2}\) length triples summing to \(n\); empty segments allow padding to three. Dropping intersection constraints only increases this count. Hence
\[
c_n\le64\binom{n+2}{2}\phi^n.
\]
Taking \(n\)-th roots proves \(\mu\le\phi\), completing the proof.

### 3.2 Transitive graph height functions imply the cubic bound

This is a reproof of the published Grimmett–Li Theorem 3.1(b), not a new subclass result. Suppose \(G\) is cubic and \((h,H)\) is a graph height function with \(H\) transitive. Thus \(h\) is difference-invariant under \(H\), and every vertex has both a strictly higher and a strictly lower neighbor.

The numbers of higher, lower and equal-height neighbors are constant over vertices: apply an automorphism in \(H\) carrying one vertex to another and use difference-invariance. If there are no equal-height neighbors, one of “higher” and “lower” has two neighbors everywhere. Reverse the sign of \(h\) if needed. Choosing either of two higher neighbors at each step gives \(2^n\) different SAWs of length \(n\), since height strictly increases. Thus \(\mu\ge2>\phi\).

Otherwise every vertex has exactly one higher, one lower and one equal-height neighbor. The equal-height edges form a matching. At each step allow the unique higher edge \(U\) or the unique equal-height edge \(V\), forbidding \(VV\). These walks are self-avoiding: height increases at each \(U\), while a height plateau contains at most one \(V\), between two distinct vertices. Distinct words give distinct vertex sequences. There are \(F_{n+2}\) allowed words, so \(\mu\ge\phi\).

For example, if a cubic Cayley graph has a nonzero group homomorphism \(h:\Gamma\to\mathbb Z\), its three distinct inverse-closed generators must be \(t,t^{-1},s\), with \(s\) an involution, \(h(t)\ne0\), and \(h(s)=0\). The same construction uses \(t\) and \(s\). Three involutions alone cannot have a nonzero homomorphism to \(\mathbb Z\).

The result does not settle all one-ended amenable cubic transitive graphs. The obstruction to extending this argument is exact: with a merely quasi-transitive height function, the counts of higher/lower/equal neighbors can vary between orbits. There need not be a single orientation offering two higher neighbors everywhere, or a matching of equal-height edges everywhere. Moreover, some transitive Cayley graphs have no graph height function at all. Lindorfer's bridge equality supplies no missing count of Fibonacci-many bridges in those situations.

## 4. A high-degree upper construction and its asymptotic

### 4.1 The graph and exact generating function

Fix an integer \(m\ge3\). Let
\[
\Gamma_m=C_m*C_2=\langle a,b\mid a^m=b^2=1\rangle,
\qquad
S_m=\{a,a^2,\ldots,a^{m-1},b\}.
\]
The Cayley graph \(X_m=\operatorname{Cay}(\Gamma_m,S_m)\) is infinite, connected, simple, transitive and of degree \(m\). The \(m-1\) nonidentity elements of \(C_m\) are distinct and inverse-closed, and \(b\) is a further involution. Left multiplication proves transitivity. Reduced alternating words prove infinitude.

Each coset of \(C_m\) induces a clique \(K_m\). Contract these cliques: the \(b\)-edges form an \(m\)-regular tree. Indeed, a nonbacktracking cycle in the contracted graph would give a reduced alternating word in the two free factors equal to the identity, impossible in a free product. In particular every \(b\)-edge is a bridge. A SAW cannot leave a clique and subsequently return, since returning requires retracing a bridge and revisiting a vertex.

From a specified entry vertex, the number of length-\(k\) SAWs within one clique is
\[
(m-1)_k=(m-1)(m-2)\cdots(m-k),\qquad 1\le k\le m-1.
\]
Set
\[
M_m(z)=\sum_{k=1}^{m-1}(m-1)_kz^k.
\]
Every SAW decomposes uniquely into alternating nonempty clique walks and single \(b\)-steps, with either kind allowed first or last. Consecutive \(b\)-steps are impossible because \(b^2=1\). Summing these alternating sequences gives the full rooted generating function
\[
C_m(z)=\sum_{n\ge0}c_n(X_m)z^n
=\frac{(1+z)(1+M_m(z))}{1-zM_m(z)}. \tag{4.1}
\]
This also follows from Gilch–Müller Theorem 3.3. Here the block decomposition supplies an independent proof for this family.

There is a unique positive solution \(r_m\) to \(r_mM_m(r_m)=1\): the left side is continuous and strictly increasing from zero to infinity. For \(|z|<r_m\), \(|zM_m(z)|\le |z|M_m(|z|)<1\), so (4.1) is analytic. At \(r_m\) the numerator is positive and the denominator vanishes, giving a genuine pole. Thus the radius of convergence is \(r_m\). The connective constant exists by transitivity and submultiplicativity; therefore
\[
u_m:=\mu(X_m)=r_m^{-1},\qquad
\boxed{\quad u_m=\sum_{k=1}^{m-1}\frac{(m-1)_k}{u_m^k}.\quad} \tag{4.2}
\]
For \(m=3\), \(u_3^3=2u_3+2\) and \(u_3=1.769292354\ldots\). For \(m=4\), \(u_4^4=3u_4^2+6u_4+6\) and \(u_4=2.516343165\ldots\). These are examples, not asserted minimizers.

### 4.2 Asymptotic calculation with both inequalities

Put \(N=m-1\) and
\[
S_N(u)=\sum_{k=1}^{N}\frac{(N)_k}{u^k}.
\]
The function \(S_N(u)-u\) is strictly decreasing for \(u>0\), and its unique zero is \(u_m\).

Fix \(c>0\), and, for sufficiently large \(N\), define
\[
v_c=N-c\sqrt{N\log N}>0,
\qquad \beta=\log(N/v_c).
\]
Taylor expansion of \(-\log(1-x)\) at zero gives
\[
\beta=c\sqrt{\frac{\log N}{N}}+O\left(\frac{\log N}{N}\right),
\qquad N\beta^2=c^2\log N+o(1). \tag{4.3}
\]
For every \(1\le k\le N\), using \(\log(1-x)\le-x\),
\[
\log\frac{(N)_k}{v_c^k}
=k\beta+\sum_{j=0}^{k-1}\log(1-j/N)
\le k\beta-\frac{k(k-1)}{2N}
=-\frac{(k-N\beta-1/2)^2}{2N}
 +\frac{(N\beta+1/2)^2}{2N}. \tag{4.4}
\]
A sum of a unit-height Gaussian over the integers is at most a constant plus its integral, hence at most \(2+\sqrt{2\pi N}\). Summing (4.4) and applying (4.3) yields
\[
S_N(v_c)\le N^{(1+c^2)/2+o(1)}. \tag{4.5}
\]
For the matching lower bound, restrict to the integer window
\[
|k-(N\beta+1/2)|\le\sqrt N.
\]
It contains order \(\sqrt N\) integers and lies inside \([1,N]\) for large \(N\). In this window \(k=O(\sqrt{N\log N})\). The estimate \(\log(1-x)=-x+O(x^2)\), uniform for \(0\le x\le1/2\), gives
\[
\sum_{j=0}^{k-1}\log(1-j/N)
=-\frac{k(k-1)}{2N}+O(k^3/N^2)
=-\frac{k(k-1)}{2N}+o(1).
\]
Consequently every term in the window is at least
\[
\exp\left(\frac{(N\beta+1/2)^2}{2N}-\frac12+o(1)\right)
=N^{c^2/2+o(1)}.
\]
Adding the window proves
\[
S_N(v_c)\ge N^{(1+c^2)/2+o(1)}. \tag{4.6}
\]
If \(0<c<1\), (4.5) is \(o(N)\), whereas \(v_c\sim N\). Hence \(S_N(v_c)-v_c<0\) and \(u_m<v_c\). If \(c>1\), (4.6) is larger than \(N\) by a factor tending to infinity, so \(S_N(v_c)-v_c>0\) and \(u_m>v_c\). Taking \(c=1-\varepsilon\) and \(1+\varepsilon\), for every fixed \(0<\varepsilon<1\), proves
\[
N-u_m=(1+o(1))\sqrt{N\log N},
\qquad
m-u_m=(1+o(1))\sqrt{m\log m}. \tag{4.7}
\]
Since \(X_m\in\mathcal G_m\), \(\mu_{\min}(m)\le u_m\). In particular \(m-\mu_{\min}(m)\ge m-u_m\to\infty\), which contradicts any bounded-deficit assertion \(\mu_{\min}(m)=m-O(1)\). No lower asymptotic of linear order for the full class follows from this construction.

For comparison with Cartesian products, let \(Y_m=K_m\square\mathbb Z\), of degree \(m+1\). Restrict SAWs to paths that move only to the next layer, making any simple path inside each visited clique before the next upward step. Their generating function is
\[
\frac{1+M_m(z)}{1-z(1+M_m(z))}.
\]
The same block argument proves this identity for the restricted walks. Its positive pole gives a **lower bound** on \(\mu(Y_m)\), not an upper bound: paths that return to a layer were omitted. We therefore do not substitute this directed-walk value for the full connective constant or use it as an upper example for \(\mu_{\min}\).

## 5. Computation: evidence and independent checks

`code/enumerate.cpp` counts rooted SAWs by exact depth-first search on a finite graph or a complete rooted ball. Vertices on the ball boundary need no outgoing edges beyond the ball: a length-at-most-\(n\) walk from the root never leaves its radius-\(n\) ball. Counts are unsigned 64-bit integers; the nonbacktracking bound at the chosen depths is far below overflow. `code/experiments.py` constructs the graphs and performs independent checks. All computation used one worker, one thread, inherited nice 10. The measured Python and enumerator memory peaks are recorded separately in `data/checks.json`: about 27 MB and 2 MB respectively, far below 4 GB.

There are **35 test cases**, including isomorphic cases and a cover comparison, rather than 35 asserted nonisomorphic graphs. Finite cases include \(K_4,K_{3,3}\), the cube (a prism), Petersen, \(K_5\), the octahedral graph, prisms, and small quartic tori. Infinite cases include the ladder, honeycomb lattice, cubic universal cover \(T_3\), four quartic cylinders, \(\mathbb Z\) with steps \(\pm1,\pm2\), the square grid, free products, and finite-group extensions of \(\mathbb Z\).

The latter are the connected Cayley components generated by
\[
(0,a),\quad(1,b),\quad(-1,b^{-1})
\]
in \(\mathbb Z\times D_q\) or \(\mathbb Z\times S_q\), where the involution \(a\) and permutation \(b\) are recorded explicitly in the JSON metadata. Each component is an infinite simple transitive cubic graph. The height is the integer coordinate. Reduction of that coordinate modulo \(L\) gives a finite voltage quotient; it is a cover, not an assertion that all covers are universal covers. In particular the universal cover of every connected simple cubic test graph is \(T_3\), while unrolling the cyclic coordinate of a finite prism gives the ladder.

Selected exact counts and diagnostics follow. A ratio is an estimate without an error bound. An \(n\)-th root is an upper bound for a transitive infinite graph; it is not a lower bound.

| Infinite graph | \(n\) | \(c_n\) | Ratio \(c_n/c_{n-1}\), evidence only | Exact value or rigorous information |
|---|---:|---:|---:|---|
| Ladder | 30 | 6,656,290 | 1.618028270 | \(\mu=\phi\), proved above |
| Honeycomb | 22 | 2,479,692 | 1.872884812 | \(\mu=1.847759065\ldots\), published exact theorem |
| \(\mathbb Z\square C_3\) | 16 | 2,491,666 | 2.294060239 | Bridge lower 2.207483734; root upper 2.510617861 |
| \(\mathbb Z\square C_4\) | 16 | 6,249,358 | 2.418457864 | Bridge lower 2.303211673; root upper 2.659130876 |
| \(\mathbb Z\) with steps \(\pm1,\pm2\) | 24 | 560,510,938 | 2.205569543 | Bridge lower 2.189916856; root upper 2.314857903 |
| Cubic \(\mathbb Z\times D_4\) component | 23 | 2,118,466 | 1.769877924 | Bridge lower 1.698613696; root upper 1.883841730 |
| Cubic \(\mathbb Z\times S_4\) component | 23 | 10,794,564 | 1.969018311 | Bridge lower 1.768850212; root upper 2.022048305 |
| \(K_3*K_2\) | 10 | 552 | 1.769230769 | \(\mu=1.769292354\ldots\), equation (4.2) |
| \(K_4*K_2\) | 10 | 18,684 | 2.513317191 | \(\mu=2.516343165\ldots\), equation (4.2) |

For the stated bridge bounds we counted walks with \(h(v_0)=0<h(v_i)\le h(v_n)\) for \(i>0\). Translating a second bridge to the endpoint of a first puts all its new vertices strictly above the first one's maximum. Thus concatenation is injective and \(b_{n+m}\ge b_nb_m\). It follows that \(\mu\ge b_n^{1/n}\). This argument applies to the recorded transitive height structures, and does not require a bridge-equality theorem to certify the lower bounds. Displayed decimals are rounded numerical presentations of exact-root inequalities, not directed-rounding certificates.

Checks performed:

1. For every graph, compare the C++ DFS counts through length 8 with an independent Python breadth-first list of explicit vertex sequences.
2. Verify \(c_{n+m}\le c_nc_m\) throughout every retained infinite-graph count range; verify bridge supermultiplicativity wherever bridge counts are used.
3. Verify the complete-graph counts \(c_k=(N-1)!/(N-1-k)!\) for \(k<N\), followed by zero, and the tree counts \(3\cdot2^{n-1}\).
4. Compare every ladder count through length 30 with its finite prism quotient of cyclic length 31. Compare the dihedral strips with voltage quotients of length 10 through walk length 9. No coordinate identification can occur within a path shorter than the quotient period.
5. Compare all free-clique-product counts through length 10 with the independent exact recurrence from (4.1).
6. Compute free-product roots by floating-point bisection and independently by 65-digit decimal arithmetic for degrees through 100. The asymptotic proof does not depend on these numerical computations.

For illustration, the high-degree family has \(u_{100}=83.95590950\ldots\), \(u_{10000}=9730.805003\ldots\), and \(u_{10^6}=996543.041653\ldots\). The ratios \((m-u_m)/\sqrt{m\log m}\) are about 0.748, 0.887 and 0.930 respectively, consistent with their proved limit 1. Full values are in `data/clique_family.csv`.

No cubic graph below \(\phi\) was found. This finite collection cannot exclude a counterexample elsewhere. Finite graphs eventually have no SAWs, so their terminal zeros and falling ratios carry no implication for the infinite-graph question.

Reproduction, from this directory with effective nice at least 10:

```sh
clang++ -O3 -std=c++17 code/enumerate.cpp -o code/enumerate
python3 code/family.py > data/family-run.txt
python3 code/experiments.py > data/enumeration-run.txt
python3 code/audit.py
```

Raw counts: `data/enumerations.jsonl`. Summary: `data/summary.csv`. Source URLs, hashes and page counts: `data/sources.jsonl`. Automatically indexed theorem locations: `data/source-index.json`. Only plain source text is retained; PDF bytes were converted through stdin/stdout in memory, with no PDFs, page images or scans written to disk.

Task: “Open problem D0070” — 13 November 2026, 08:29 local session clock (Asia/Tbilisi).
