PARTIAL

# D0073: strict decrease of connective constants under free quotients

The general question is not solved here. The literature search did not locate a printed resolution. This report proves a quantitative sufficient condition for quotients that collapse an edge in every fibre, gives complete proofs for trees and a reduction through a nontrivial normal core, and records a further deduction conditional on a 2026 pattern theorem. It does not establish the assertion for all non-normal free quotients, all amenable graphs, all Cayley graphs, or all graphs with a height function. No counterexample was found. No priority claim is made for the partial criteria.

Task: “Open problem D0073”, received/work begun 13 November 2026, 09:00 +04, Asia/Tbilisi.

## 1. Exact question and quotient conventions

Let $G=(V,E)$ be infinite, connected, locally finite, simple and vertex-transitive. The local-finiteness hypothesis is part of the survey's class $\mathcal G$, although it was omitted from the informal question in the prompt. Let $\Gamma\leq\operatorname{Aut}(G)$ be transitive, and let $1\ne A\leq\Gamma$ act freely on vertices: every nonidentity member of $A$ fixes no vertex. Put $q(v)=Av$.

For **Question 4.6** the graph $H=G_A$ is the **undirected simple** orbit quotient. Two distinct orbits are adjacent when some edge of $G$ joins them. Internal edges become no edge; parallel images are merged. Assume that **$\operatorname{Aut}(H)$ acts transitively**. There is no assumption that this group, or a transitive subgroup of it, lifts to automorphisms of $G$, and no requirement that $\Gamma$ act on $H$.

The question is

\[
                         \mu(H)<\mu(G).
\]

Here $c_n(X,x)$ counts rooted $n$-step vertex-self-avoiding walks. For infinite transitive locally finite $X$, $\mu(X)=\lim_n c_n(X,x)^{1/n}$. A finite quotient has $\mu=0$, so its case is immediate. All nontrivial discussion below concerns infinite $H$, for which $\mu(H)\geq1$.

The survey first defines a **different**, directed multigraph quotient $\vec G$: the multiplicity from $Av$ to $Aw$ is

\[
                         m(Av,Aw)=|\partial v\cap Aw|.
\]

This definition retains directed loops and parallel edges. The value is independent of the representative $v$, for any subgroup $A$: applying an element of $A$ bijects the relevant neighbour sets. It does not need normality. When parallel edges occur, their choices distinguish directed SAWs. Loops cannot belong to a positive-length vertex-SAW.

Survey locations: Section 4 is PDF pp. 14–18; the directed definition and Theorem 4.2 are on p. 15; the simple definition is on p. 16; Question 4.6 is on p. 17. These are PDF/preprint page numbers, not the pagination of the eventual book chapter. [Survey](https://arxiv.org/abs/1704.05884).

## 2. Literature check

The full sources are plain text in `sources/`; `data/source_index.json` gives their URLs, text hashes and theorem-to-PDF-page locations. `sources/LITERATURE_SEARCH.txt` records searches and reading scope. The source PDFs were fetched into RAM, converted to text, and never saved.

The exact arXiv identifier of the 2014 strict-inequality paper is **1301.3091**. Its published reference is G. R. Grimmett and Z. Li, *Strict inequalities for connective constants of transitive graphs*, SIAM J. Discrete Math. **28**(3) (2014), 1306–1333, DOI [10.1137/130906052](https://doi.org/10.1137/130906052).

| Source | Exact result/location checked | Relevance |
|---|---|---|
| Grimmett–Li, survey, [1704.05884](https://arxiv.org/abs/1704.05884) | Theorem 4.2, PDF p. 15; Questions 4.5–4.6 and following paragraph, pp. 16–17 | States the question and the additional cycle-length condition. |
| Grimmett–Li, [1301.3091](https://arxiv.org/abs/1301.3091), published text also saved | Theorem 3.8, journal p. 1312 / published PDF p. 7; Theorem 3.12, p. 1315 / PDF p. 10; Section 5, pp. 1316–1325 | Normal quotient theorem and the non-normal cycle-length extension. Non-normal proof outline: p. 1325 / PDF p. 20. |
| Grimmett–Li, *Locality of connective constants*, Discrete Math. **341** (2018), 3483–3497, [1412.0150](https://arxiv.org/abs/1412.0150) | Theorems 4.3, 5.1, 5.2, arXiv PDF pp. 11, 12, 13 | Bridge equality and locality; the displayed quotient application still assumes normality. A limiting equality is not a strict comparison for a fixed quotient. |
| Grimmett–Li, *Connective constants and height functions for Cayley graphs*, Trans. AMS **369** (2017), 5961–5980, [1501.00476](https://arxiv.org/abs/1501.00476) | Theorem 4.1, arXiv PDF pp. 7–8 | Existence/characterization of group height functions; does not supply the missing compatibility with arbitrary $A$. |
| Grimmett–Li, *Self-avoiding walks and amenability*, Electron. J. Combin. **24**(4) (2017), P4.38, [1510.08659](https://arxiv.org/abs/1510.08659) | Theorems 4.1 and 5.1, arXiv PDF pp. 7–8 | Elementary amenable groups have suitable height functions; amenability alone does not supply them. |
| C. Lindorfer, *A general bridge theorem for self-avoiding walks*, Discrete Math. **343**(12) (2020), 112092, [1902.08493](https://arxiv.org/abs/1902.08493) | Theorem 3.2, PDF p. 5 | $\mu=\max(\beta_+,\beta_-)$ without unimodularity. This is not a strict quotient theorem. |
| C. Panagiotis, *Self-avoiding walks and polygons on hyperbolic graphs*, [1908.00127](https://arxiv.org/abs/1908.00127) | Theorems 1–4, PDF pp. 2–3 | Strict comparison of polygon and walk growth, bounds, and ballisticity; different constants from those in D0073. |
| S. Martineau–F. Severo, *Strict monotonicity of percolation thresholds under covering maps*, Ann. Probab. **47**(6) (2019), 4116–4136, [1803.09686](https://arxiv.org/abs/1803.09686), DOI [10.1214/19-AOP1355](https://doi.org/10.1214/19-AOP1355) | **ArXiv numbering:** Theorem 2.1, PDF p. 3; Corollary 2.2, p. 4; Propositions 4.1–4.2, p. 8; Lemmas 7.1–7.2, pp. 15–16 | Resolves the non-normal free quotient question for $p_c$, assuming $p_c(G)<1$. The journal was renumbered; these theorem numbers refer explicitly to the saved arXiv version. |
| Grimmett–Li, *Cubic graphs and the golden mean*, Discrete Math. **343**(1) (2020), 111638, [1610.00107](https://arxiv.org/abs/1610.00107) | Published Theorems 1.2 and 3.1, article PDF pp. 2 and 4; both published and arXiv texts saved | Lower bounds for cubic graphs; not a resolution of Question 4.6. |
| Lehner–Lindorfer–Panagiotis, *Self-avoiding walk is ballistic on graphs with more than one end*, Forum Math. Sigma **13** (2025), e179, [2403.13121](https://arxiv.org/abs/2403.13121) | Theorems 1.1–1.3, saved arXiv PDF p. 3 | Many-ended growth and ballisticity; no general non-normal quotient strictness theorem found. |
| N. Aubrun–N. Bitar, *Self-Avoiding Walks on Cayley Graphs Through the Lens of Symbolic Dynamics*, Electron. J. Combin. **31**(4) (2024), P4.24, [2402.13944](https://arxiv.org/abs/2402.13944) | Theorem 2.11, PDF p. 9; Theorems C–D, p. 3 | Restates strictness for normal closures; entropy/periodic-point results do not remove normality. |
| G. R. Grimmett, *Connective constants of Grigorchuk graphs*, [2608.19349](https://arxiv.org/abs/2608.19349) | Theorem 1.2, PDF p. 2; Theorem 3.1, p. 6 | New cubic bounds, not the quotient question. |
| G. R. Grimmett, *SAWs, trails, kites, patterns*, [2611.00816](https://arxiv.org/abs/2611.00816), submitted 31 Oct. 2026 | Theorem 4.5, PDF p. 13; definitions pp. 10–12; connector exclusions pp. 20–21 | A recent pattern theorem gives the conditional deduction in Section 6 below. It does not state a solution of Question 4.6. |
| Martineau–Poudevigne–Rax, *Stochastic domination and lifts of random variables in percolation theory*, [2504.02427](https://arxiv.org/abs/2504.02427), revised March 2026 | Section 6, Theorem 6.1, PDF p. 26 | Reproves bond-percolation strictness using couplings rather than differential inequalities. Still a percolation theorem. |

This is a bounded search through 13 November 2026. No exact reference resolving D0073 was found; absence from these searches is not proof of absence from the literature. Consequently the report is **PARTIAL**, not RESOLVED_IN_LITERATURE.

## 3. What the normal proof does, and where normality enters

### Exact normal theorem

In Theorem 3.8, $A\trianglelefteq\Gamma$ is nontrivial and $\Gamma$ is transitive on $G$. Write

\[
 L=\min\{d_G(v,w):v\ne w,\ Av=Aw\}.
\]

The directed quotient has strictly smaller connective constant if $L=1$ or $L\geq3$. If $L=2$, either of these additional conditions suffices:

1. There is a two-step SAW $v,u,v'$, with $Av=Av'$, and $|\partial v\cap Au|\geq2$.
2. There is a SAW $v=w_0,\ldots,w_l=v'$, whose projected vertices before the last are pairwise distinct, with $Av=Av'$, and $v'=av$ for an $a\in A$ that fixes none of the vertices of the walk.

Thus the qualifications on the **directed multigraph** theorem matter. Its Example 3.9, journal p. 1313, has directed connective constant 2 both before and after quotienting a binary tree, but that action is not free. Its simple quotient is a line, with connective constant 1; it is not a counterexample to D0073.

### Mechanism

Fix edge labels so every directed quotient walk has a chosen lift from a chosen root. A quotient SAW lifts to a SAW because distinct orbits contain distinct vertices.

Choose a shortest path $p$ from $v$ to $av\ne v$. Its projection closes. Normality gives

\[
 \gamma(Av)=A\gamma v,\qquad
 Av=Aw\ \Longleftrightarrow\ A\gamma v=A\gamma w
 \quad(\gamma\in\Gamma).
\]

Consequently all translates of $p$ have the same orbit-return property, and form a family compatible with the transitive geometry.

The proof builds events $E_k$ saying that a quotient walk visits at least $k$ vertices of one of these projected cycles. Lemma 5.3 (p. 1318) converts a strict rate bound for avoiding $E_k$ into a strict rate bound for walks with too few local occurrences. Lemma 5.4 (pp. 1319–1323) bootstraps this to the full-cycle event. At separated occurrences, surgery goes once around the projected cycle and partway around again, switches the lift by a member of $A$, and moves the tail. The resulting walk in $G$ remains self-avoiding.

The counting step is essential because surgery changes length. If $T_n$ is a suitable set of quotient walks, choosing $\lfloor\delta n\rfloor$ sites among $\lfloor\kappa n\rfloor-O(1)$ sites gives, for constants $C,b$, an inequality of the form

\[
 |T_n|\binom{\lfloor\kappa n\rfloor-O(1)}{\lfloor\delta n\rfloor}
 \leq C^{\delta n+O(1)}
       \sum_{j\leq n+b\delta n+O(1)}c_j(G).
\]

For sufficiently small $\delta>0$, the binomial entropy, of order $\delta\log(1/\delta)n$, beats the bounded reconstruction and added-length costs, of order $\delta n$. Together with the low-occurrence estimate this gives a strict exponential gap. Equations (5.32)–(5.36), pp. 1323–1324, implement this argument. This is Kesten-style pattern surgery, not an invocation of a universal pattern theorem for all transitive graphs. Height-function unfolding is useful for bridge bounds and effective estimates, but is not an assumption of Theorem 3.8.

### Precise obstruction without normality

Lifting edges, lifting a quotient SAW, and applying an element of $A$ to a tail all remain valid without normality: $q(ax)=q(x)$ for every $a\in A$. The missing step is the supply of a **transitively transported family of nonclosing lifts of closed quotient patterns**. Translating $p$ by $\gamma$ only makes its endpoints equivalent under $\gamma A\gamma^{-1}$. Conversely, a quotient automorphism can move a cycle to one whose lifts close in $G$.

Theorem 3.12 bypasses that problem when the quotient has an $l$-cycle and $G$ has no $l$-cycle. Every lift of every quotient translate of that cycle is then nonclosing. Freeness supplies $ax\ne x$ in the surgery, specifically the analogue of equation (5.25). The proof expressly requires no relationship between the transitive groups on $G$ and on its quotient. For the simple quotient, ordinary cycles have length at least 3.

## 4. Martineau–Severo: what transfers and what does not

Their weak covering means that $q$ is 1-Lipschitz and each neighbour of $q(x)$ has a neighbour lifting it at $x$. Every orbit quotient has this property: move the endpoint of a representative edge to $x$ using $A$.

Two useful structural ingredients transfer directly.

**Disjoint tree lifts.** Lift any tree $T\subseteq H$ to a tree $T_x\subseteq G$ containing $x$. If $y=ax\ne x$, then $aT_x$ is another lift containing $y$. An intersection would give vertices $u,v\in T_x$ with $u=av$. Their projections agree, so injectivity of $q$ on $T_x$ gives $u=v=av$, contradicting freeness. Thus the lifts are disjoint. This is their Lemma 7.1.

**Uniformly close pairs in fibres.** In the transitive setting here, choose $u\ne v$ in one fibre and $R\geq d_G(u,v)$. The map $B_R(G,u)\to B_R(H,q(u))$ is onto and not injective, hence its domain is larger. Transitivity of both graphs makes this strict size inequality valid at every $x$. There are therefore $y,z\in B_R(G,x)$, $y\ne z$, with $q(y)=q(z)$. Lift a path of length at most $R$ from $q(y)$ to $q(x)$ disjointly from (y,z). Its endpoints are distinct members of the fibre of $x$, both within (2R) of $x$; at least one differs from $x$. This proves tame fibres, the transitive special case of their Lemma 7.2.

For percolation, these facts allow an exploration coupling with a positive-probability local bonus. Proposition 4.1 dominates an enhanced quotient cluster by the projection of a cluster upstairs. Proposition 4.2 proves that the bonus lowers the critical probability. The latter uses pivotal modifications and a Russo-type comparison $\partial_s\theta\geq c\partial_p\theta$. The 2025/2026 reproof replaces this part with cell-based couplings, but still compares connection events.

**That argument does not currently give a SAW proof.** A cluster may branch, and its exploration can use a connected ball in a way that cannot be encoded as a single path. Extracting a simple path can erase both length and insertion choices. The comparison of connection probabilities gives no bound on how many modified walks encode the same output. One needs a replacement counting or pattern argument with controlled added length and reconstruction multiplicity.

Nor can one simply substitute $1/\mu$ for $p_c$. The union bound gives only

\[
                            p_c(X)\geq1/\mu(X):
\]

if $p\mu(X)<1$, the probability of an open SAW reaching distance $n$ is at most $c_n(X)p^n\to0$. Two lower bounds of this kind and $p_c(G)<p_c(H)$ do not order the two connective constants. Thus the structural route transfers; the decisive strict-counting step remains missing in general.

D0073 also lacks the percolation hypothesis $p_c(G)<1$. Both the clique strips $K_m\square\mathbb Z$ and their smaller clique-strip quotients have $p_c=1$, although Section 5 proves a strict SAW gap. For $p<1$, all $m$ edges crossing a given integer-layer cut are closed with probability $(1-p)^m>0$. These events are independent for distinct cuts and almost surely occur infinitely often in both directions, making every cluster finite. Thus the percolation theorem cannot be applied directly even to these transitive examples.

## 5. Complete elementary partial results

### 5.1 Monotonicity for every orbit quotient

**Lemma.** If $q:G\to H$ is an orbit quotient and both connective constants exist, then $\mu(H)\leq\mu(G)$.

**Proof.** Fix a root $x$, and for every vertex $v\in G$ and each neighbour $w\in H$ of $q(v)$, choose one neighbour of $v$ projecting to $w$. Such choices exist by the weak lifting property. Recursively lift every rooted quotient SAW using these choices. The lift is self-avoiding, and different quotient walks have different lifts because projection recovers them. Hence $c_n(H,q(x))\leq c_n(G,x)$. Taking nth roots proves the assertion. Neither normality nor freeness was used. ∎

### 5.2 Uniform internal-fibre paths: a quantitative criterion

**Theorem A.** Let $q:G\to H$ be an orbit quotient of infinite transitive locally finite graphs. Suppose that, from every vertex $v\in G$, the subgraph induced by its fibre has at least $b_k$ rooted SAWs of length $k$, for $0\leq k\leq L$, where $b_0=1$ and all $b_k$ are fixed nonnegative integers. Put

\[
                     B(z)=\sum_{k=0}^L b_kz^k.
\]

If some $b_k>0$ for $k>0$, and $r>0$ is the unique solution of

\[
                        \mu(H)\,r B(r)=1,
\]

then

\[
                       \mu(G)\geq r^{-1}>\mu(H).
\]

In particular, if **each orbit contains an edge**, then

\[
 \boxed{\quad
 \mu(G)\ \geq\ F(\mu(H))
 :=\frac{\mu(H)+\sqrt{\mu(H)^2+4\mu(H)}}2
 >\mu(H).\quad}
\]

More generally, with at least $a\geq1$ neighbours in its own fibre at every vertex, replace $4\mu(H)$ by $4a\mu(H)$. No freeness or normality is needed for this criterion.

**Proof.** At every vertex choose $b_k$ distinct internal-fibre $k$-step SAWs, for each $k\leq L$, and fix the neighbour-lifting rule of Lemma 5.1.

Given a quotient SAW $w_0,\ldots,w_n$, start at the prescribed lift of $w_0$. Before taking the edge to $w_{i+1}$, choose and traverse one of the selected internal-fibre paths at the current vertex, and then lift that quotient edge from its endpoint. At the last vertex also choose an internal path. Each internal path is self-avoiding, and different stages lie in different fibres. Thus the whole output is a SAW in $G$.

Projection of the output is the original quotient SAW with each $w_i$ repeated consecutively. Compressing consecutive repeats recovers the quotient SAW, and the uncompressed output recovers every internal path. The construction is injective even when original walks of different lengths are considered together.

Write $\chi_X(z)=\sum_{n\geq0}c_n(X)z^n$. Comparing coefficients of formal power series gives

\[
                  \chi_G(z)\ \succeq\ B(z)\,
                                  \chi_H(zB(z)).
\]

The right-hand side diverges for every positive $z$ with $zB(z)>1/\mu(H)$. Hence the radius of convergence of $\chi_G$ is at most $r$, proving $\mu(G)\geq1/r$. The polynomial $zB(z)$ is strictly increasing on positive $z$, and $B(r)>1$; therefore $1/r=\mu(H)B(r)>\mu(H)$.

If every orbit contains an edge, transitivity of $A$ within that orbit gives an internal neighbour at every one of its vertices. Take $B(z)=1+z$ and solve the quadratic. With $a$ internal neighbours, take $B(z)=1+az$. ∎

The coefficient version for $B(z)=1+z$, also checked computationally below, is

\[
 c_N(G)\ \geq\sum_{n=0}^N c_n(H)\binom{n+1}{N-n},
\]

where a binomial coefficient outside its usual range is zero. This explicitly handles the change in walk lengths.

### 5.3 A class of non-normal Cayley subgroup quotients

**Corollary B.** Let $X$ be any infinite connected transitive locally finite simple graph, and let a nontrivial group $A\leq S_m$ act freely on the $m$ points of $K_m$. Let it act on $G=X\mathbin\square K_m$ by the second coordinate only. Write $r=|A|\geq2$ and $q=m/r$. Then

\[
 G_A\cong X\mathbin\square K_q,
 \qquad
 \mu(G)\geq F(\mu(G_A))>\mu(G_A).
\]

A stronger bound uses

\[
 B_r(z)=\sum_{k=0}^{r-1}\frac{(r-1)!}{(r-1-k)!}z^k
\]

in Theorem A.

**Proof.** Freeness makes every orbit have $r$ points. Each fibre induces $K_r$. Its internal SAWs have the displayed falling-factorial counts. The quotient of the complete finite factor is $K_q$, and Cartesian edges in the $X$ direction are preserved. Theorem A applies. ∎

For a Cayley example take

\[
 \Lambda=F\times\mathbb Z,\qquad
 S=((F\setminus\{1\})\times\{0\})\cup\{(1,1),(1,-1)\},
\]

where $F$ is finite, and take $A=A_0\times\{0\}$ for any nontrivial subgroup $A_0\leq F$, acting by left multiplication. Then $G=K_{|F|}\square\mathbb Z$, and the quotient is $K_{[F:A_0]}\square\mathbb Z$. This proves strictness even when $A_0$ is non-normal in the **Cayley group itself** and has trivial core, for example an order-two subgroup of $S_3$ or a reflection subgroup of $D_8$.

These examples do not satisfy the missing-cycle-length criterion: $G_A$ embeds in $G$ by choosing one finite-factor representative per orbit, so every cycle length downstairs already occurs upstairs. However, these product quotients also admit alternative normal presentations, using blockwise permutations of a partition of the clique. They are not claimed as a new solution of the intrinsically non-normal part of the problem.

**Cartesian doubling variant.** If a transitive $G$ contains a subgraph isomorphic to $H\square K_2$, then $\mu(G)\geq F(\mu(H))>\mu(H)$, by Theorem A applied to the projection $H\square K_2\to H$, followed by subgraph monotonicity. The embedding need not respect the original quotient map.

This covers a less uniform example. For

\[
 F=S_3=\langle r,t:r^3=t^2=1,\ trt=r^{-1}\rangle,
\]

use generators $r,r^{-1},t$, together with the two $\mathbb Z$ generators. The finite Cayley factor is the triangular prism $C_3\square K_2$. Quotient by the freely acting left subgroup $\langle t\rangle$ gives $K_3\square\mathbb Z$. Only one of the three finite-factor fibres contains an edge, so the uniform internal-edge hypothesis fails for this particular map. Nevertheless the graph upstairs is abstractly $(K_3\square\mathbb Z)\square K_2$, and the doubling bound proves strictness. The coset and graph calculations are checked in code.

### 5.4 All regular trees, with or without degree loss

**Theorem C.** Let $G=T_d$ be an infinite regular tree, and let a nontrivial freely acting subgroup have a transitive simple quotient $H$. Then $\mu(H)<\mu(T_d)$.

**Proof.** A finite $H$ is immediate. Suppose $H$ is infinite and has degree $k\leq d$. Then $k\geq2$, and nonbacktracking counting gives $\mu(H)\leq k-1$. If $k<d$, this is strictly smaller than $\mu(T_d)=d-1$.

Suppose $k=d$. At every vertex the neighbour map onto the $d$ quotient neighbours is a bijection. There can be no internal-fibre edge or multiplicity loss, so this is a classical graph covering. If $H$ were a tree, the projection of a tree geodesic would be nonbacktracking by local injectivity, hence a simple path in $H$. Two distinct vertices in one fibre would give a nonempty closed nonbacktracking path in a tree, impossible. Nontriviality and freeness give such a pair. Thus $H$ contains a cycle of some length $g\geq3$. This also excludes $d=2$ in the present infinite-quotient case.

Transitivity gives a $g$-cycle through every vertex of $H$. After any SAW prefix of positive length, choose an orientation of such a cycle whose first edge does not reverse the incoming edge. Traversing its $g$ edges is one of the $(d-1)^g$ nonbacktracking continuations, but is not self-avoiding. Consequently each positive-length SAW prefix has at most

\[
                             (d-1)^g-1
\]

self-avoiding extensions of length $g$. For $n=1+ag+b$, $0\leq b<g$,

\[
 c_n(H)\leq d\big((d-1)^g-1\big)^a(d-1)^b.
\]

Therefore

\[
                 \mu(H)\leq\big((d-1)^g-1\big)^{1/g}<d-1.
\]

This proves the result. ∎

The cycle case is already within the known theory. The proof also deals explicitly with degree-losing acyclic quotients, for which a new cycle length cannot be invoked.

### 5.5 Nontrivial normal core

**Proposition D.** Under D0073's assumptions, if

\[
              N=\bigcap_{\gamma\in\Gamma}\gamma A\gamma^{-1}\ne\{1\},
\]

then $\mu(G_A)<\mu(G)$.

**Proof.** The subgroup $N\trianglelefteq\Gamma$ is nontrivial and acts freely, being a subgroup of $A$. For completeness, a freely acting subgroup has symmetric orbit multiplicities: if $x=aw\in\partial v\cap Nw$, with $a\in N$, the corresponding neighbour of $w$ in $Nv$ is $a^{-1}v$. Uniqueness of $a$ follows from freeness, and this gives a bijection between the two neighbour sets.

If $N$ has type 2, a path $v,u,v'$ with $Nv=Nv'$ gives at least two neighbours of $u$ in $Nv$; symmetry gives at least two neighbours of $v$ in $Nu$. Thus condition (b)(i) of Grimmett–Li Theorem 3.8 holds. For types 1 and 3 its condition (a) holds. In every case,

\[
                   \mu(G_N)\leq\mu(\vec G_N)<\mu(G).
\]

The orbit relation of $N$ refines that of $A$. The simple quotient of $G_N$ by the induced action of $A/N$ is exactly $G_A$. Lemma 5.1 gives $\mu(G_A)\leq\mu(G_N)$. If $G_N$ is finite, so is $G_A$, and the conclusion is immediate as well. ∎

A concrete algebraic sufficient condition is: $A$ is infinite, has finitely many conjugates in $\Gamma$, and is commensurated in $\Gamma$. Indeed, each $A\cap\gamma A\gamma^{-1}$ has finite index in $A$; the finite intersection has finite index in $A$ and is therefore infinite. This is a reduction to the normal theorem, not an assertion for all subgroups whose normalizer is quasi-transitive.

## 6. A height-function criterion using the October 2026 preprint

This subsection is a deduction **conditional on Grimmett's stated preprint Theorem 4.5** in [2611.00816](https://arxiv.org/abs/2611.00816), PDF p. 13. Its proof is not independently re-proved here. The elementary results of Section 5 do not depend on it.

Use $K$ for the height-function symmetry group, to distinguish it from the quotient graph $H$. Suppose:

1. $G$ has a graph height function $(h,K)$, with $K$ quasi-transitive and $K\leq N_{\operatorname{Aut}(G)}(A)$.
2. There is a SAW $p=(p_0,\ldots,p_l)$, $l\geq1$, whose distinct endpoints lie in the same $A$-orbit.
3. The walk $p$ is an admissible bridgeable pattern for that theorem: it has neither a (+) nor a (−) cut-edge, occurs up to $K$-translation in a (+) or (−) bridge, and is outside the exceptional connector-pattern set $\Pi$.

For precision, a (+) bridge $w_0,\ldots,w_n$ satisfies $h(w_0)<h(w_i)\leq h(w_n)$ for $0<i\leq n$; reverse the inequalities for a (−) bridge. Its heights need not be monotone along the walk. The edge $p_i p_{i+1}$ is a (+) cut-edge when all heights up to time $i$ are at most $h(p_i)$ and all later heights are strictly larger; reverse the inequalities for a (−) cut-edge. In the quasi-transitive case $\Pi$ consists of patterns occurring in the finitely chosen connecting walks of Definition 5.4 and Proposition 5.3, PDF pp. 20–21. A sufficient way to avoid it is $|p|>\max|\text{connector}|$. For a transitive height function $\Pi=\varnothing$.

**Conditional Proposition E.** These hypotheses imply $\mu(G_A)<\mu(G)$.

**Proof of the deduction.** Since $K$ normalizes $A$, every $K$-translate of $p$, and of its reversal, has endpoints in one $A$-orbit. A lift of a quotient SAW visits each $A$-orbit at most once, so it contains none of those patterns. The canonical lift is injective by Lemma 5.1. Thus

\[
 c_n(G_A)\leq
 \#\{n\text{-step SAWs in }G\text{ avoiding }Kp\text{ and }Kp^{\rm rev}\}.
\]

Theorem 4.5(a) says the limsup nth root of the right side is strictly smaller than $\mu(G)$. Taking nth roots proves the result. ∎

This isolates a usable compatibility condition for quotients with a quasi-transitive group of lifts. It does not follow merely from existence of a height function: its group must normalize $A$, and the collision path must meet the pattern and bridgeability conditions. If $K$ is transitive, $A$ is normal in the transitive group $\langle K,A\rangle$, so that situation was already covered by the normal theorem. The potentially additional scope is the quasi-transitive case with these extra pattern hypotheses.

## 7. Exact finite enumeration: evidence and checks

`code/enumerate_saws.py` counts all rooted SAWs through a prescribed length on an actual radius-$N$ ball of each infinite graph. A walk of length at most $N$ cannot leave that ball; its boundary introduces no truncation error. DFS records counts at every prefix length. A separate dynamic program on `(endpoint, visited vertex set)` states checks every graph through length 6. There is no sampling and no extrapolated claim of an exact connective constant.

### Definitions of the examples

- **Square lattice:** neighbours $(x\pm1,y),(x,y\pm1)$. Quotient by $(x,y)\mapsto(x+m,y)$, $m=2,3,4$. Width 2 merges the two horizontal neighbours, giving the ladder. The subgroup is non-normal in the full lattice symmetry group, because a quarter-turn changes its translation direction, but is normal in the transitive translation group. These examples therefore test conventions and known strictness, not the unresolved obstruction.
- **Hexagonal lattice:** brick-wall neighbours $(x\pm1,y)$ and $(x,y+(-1)^{x+y})$. Quotient by even horizontal periods $m=2,4,6$. These are transitive: parity-preserving translations and the map $(x,y)\mapsto(x+1,-y)$ descend and move between vertex types. Width 2 has degree 2 and is a line. The relevant transitive lift group normalizes the period subgroup.
- **Trees:** reduced words in the free product of $d$ copies of $C_2$ give $T_d$, for $d=3,4$. The hexagonal lattice and ladder are quotients of $T_3$, and the square lattice is a quotient of $T_4$, via universal covering. Deck transformations act freely; nontriviality follows from cycles downstairs.
- **Infinite Cayley examples:** $S_3\times\mathbb Z$ and $D_8\times\mathbb Z$ with complete finite-factor generators as in Corollary B, quotienting by an order-two left subgroup. Here $D_8$ has order 8, with presentation $\langle r,s:r^4=s^2=1,srs=r^{-1}\rangle$. The simple quotients are $K_3\square\mathbb Z$ and $K_4\square\mathbb Z$. A sparse $S_3\times\mathbb Z$ example uses $r,r^{-1},t$. Explicit multiplication and coset enumeration verify freeness, non-normality, trivial normal core, and the quotient adjacencies.
- **Finite controls:** the complete Cayley graphs of (S_3,D_8) and their simple quotients are also counted to exhaustion. Their eventual connective constants are all zero. Those finite equalities do not meet the infinite-$G$ hypothesis and are not counterexamples.

### Counts at common lengths

| $G$ | Simple quotient $H$ | $n$ | $c_n(G)$ | $c_n(H)$ |
|---|---|---:|---:|---:|
| Square lattice | Circumference 2 | 14 | 2,374,444 | 3,002 |
| Square lattice | Circumference 3 | 14 | 2,374,444 | 472,906 |
| Square lattice | Circumference 4 | 14 | 2,374,444 | 1,055,730 |
| Hexagonal lattice | Circumference 2 | 18 | 199,350 | 2 |
| Hexagonal lattice | Circumference 4 | 18 | 199,350 | 33,632 |
| Hexagonal lattice | Circumference 6 | 18 | 199,350 | 95,500 |
| $T_3$ | Hexagonal lattice | 12 | 6,144 | 4,416 |
| $T_3$ | Ladder | 12 | 6,144 | 1,140 |
| $T_4$ | Square lattice | 10 | 78,732 | 44,100 |
| $S_3\times\mathbb Z$, complete factor | $K_3\square\mathbb Z$ | 9 | 3,081,772 | 7,186 |
| $D_8\times\mathbb Z$, complete factor | $K_4\square\mathbb Z$ | 8 | 6,828,628 | 27,452 |
| $S_3\times\mathbb Z$, sparse factor | $K_3\square\mathbb Z$ | 11 | 1,679,012 | 38,670 |

For a view of finite-length growth, at their maximum saved lengths the nth roots are: square 2.85363 $(n=14)$; ladder 1.73669 $(n=18)$; hexagonal 1.96980 $(n=18)$; width-4 hexagonal cylinder 1.78438 $(n=18)$; width-6 hexagonal cylinder 1.89089 $(n=18)$. These are finite-length upper bounds on the respective transitive connective constants, not estimates with error bars. Successive ratios and all integer counts are in `data/counts.csv`.

Finite count inequalities alone do not prove a strict inequality between limits. The proofs in Sections 5–6 are separate from this evidence.

### Independent audits

`code/verify_results.py` verifies the optional-edge coefficient inequality for all saved lengths in the three infinite group examples. It also verifies the finite complete-graph counts against

\[
 c_n(K_m)=\frac{(m-1)!}{(m-1-n)!}\quad(0\leq n<m),
 \qquad c_n(K_m)=0\quad(n\geq m).
\]

Tree counts match $c_n(T_d)=d(d-1)^{n-1}$. The separate definitions of $K_3\square\mathbb Z$ and the circumference-3 square cylinder give identical counts through length 14. The square lattice agrees with its standard initial sequence through length 10, in addition to the independent program's check through 6.

As another magnitude check, monotone walks on $K_m\square\mathbb Z$ give a rigorous lower bound $\lambda_m$, defined as the unique positive solution of

\[
 \sum_{k=0}^{m-1}\frac{(m-1)!}{(m-1-k)!}\lambda_m^{-(k+1)}=1.
\]

Indeed, in each new integer layer choose any internal clique SAW and then step to the next layer. Layers are distinct, so the concatenation is self-avoiding. Its generating series contains the geometric series with ratio $zB_m(z)$, proving the bound. Numerically $\lambda_3\approx2.269531$, $\lambda_6\approx4.349048$, $\lambda_8\approx5.804110$. These are evaluations of proved polynomial bounds, not fitted connective constants; their decimals are ordinary floating-point evaluations.

## 8. Reproduction, resources, and remaining gap

Run, in this directory:

```sh
python3 code/enumerate_saws.py
python3 code/verify_results.py
python3 code/source_audit.py
```

The counting program requires inherited nice at least 10, uses one worker and no numerical thread pool, and guards its graph and independent-check state sizes. The recorded peak resident memory is **94.5 MiB**. The host rejected attempts to lower virtual/data resource limits, so no OS-enforced memory cap is claimed; the bounded data structures and measured RSS stayed far below 4 GB. No subagents, publications, pushes, PDFs, page images or scans were produced. All authored files are inside this directory.

Outputs: `data/enumeration.json`, `data/counts.csv`, `data/verification.json`, `data/source_index.json`, the source text files, and `LOG.md`. Source-fetch scripts require `requests` and `pypdf`; counting and verification use only the Python standard library. Some PDF extraction introduces spacing or mathematical-glyph defects; page markers, source URLs and hashes are retained for checking. NUL extraction artefacts were converted to the literal text `[NULL]`.

The unresolved case includes a core-free free subgroup whose quotient has no new cycle length, has no uniform internal-fibre insertion, and has no demonstrated compatible bridgeable collision pattern. Disjoint lifts and tame fibres are available, but they do not yet supply the entropy/reconstruction estimate needed for SAWs. A proof that every such quotient admits the required count-preserving local surgery would close the gap; neither that statement nor its negation has been established here.
