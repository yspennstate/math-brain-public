COUNTEREXAMPLE

# G0010: near-regular graphs can have polynomial subcritical components

For every fixed (0<\varepsilon<1) and
\[
  \delta>\frac{\varepsilon}{1-\varepsilon},
\]
there are connected finite simple graphs satisfying
\(\Delta(G)\le(1+\delta)\lambda(G)\) for which, at
\(p=(1-\varepsilon)/\lambda(G)\), the largest component has at least
\(n^c\) vertices with probability tending to one, for some fixed (c>0).
The examples can have \(\lambda,\Delta=\Theta(n^a)\) for any prescribed
(0\le a<1). Thus bounded maximum-degree-to-spectral-radius ratio, even a
ratio arbitrarily close to one, does not by itself give a logarithmic bound
uniformly over the subcritical margin.

The margin matters: if \((1-\varepsilon)(1+\delta)<1\), the standard
maximum-degree argument gives a tight-in-order logarithmic worst-case bound.
At equality, a further argument below gives \(O_\varepsilon((\log n)^3)\).
We also give a degree-sensitive refinement of the source's resolvent bound.
**These results do not determine the optimal bound for all triples
\((n,\Delta,\lambda)\), and do not settle Question 5.2 in full.**
The status line refers to the polynomial counterexample permitted in item 3
of the task, not to a counterexample to either source theorem. No priority
claim is made for the arguments here.

## Source and literature outcome

The source is Micha Christoph, Patryk Morawski and Yuval Wigderson,
[*The critical probability for percolation on finite graphs*,
arXiv:2608.19145v1](https://arxiv.org/abs/2608.19145), 19 August 2026.
Its text is saved in `sources/CMW_2608.19145v1.txt`. Theorem 1.4 is on PDF
pp. 4–5, its full proof is Section 4.1, pp. 14–16, and Section 5 occupies
pp. 19–20. Question 5.2 itself is on **PDF p. 20** in this version; its
introductory discussion begins on p. 19.

No located publication or preprint answers the general question. The review
was conducted before developing the proofs below. Exact references,
theorem numbers, retrieved-version PDF pages, and applicability checks are
in `sources/LITERATURE_REVIEW.txt`. A substantive later citation was found
and checked: Anastos–Frieze–Krueger, *Perfect matchings in a random k-out
subgraph of the hypercube*, author preprint dated 27 August 2026, cites the
source on PDF p. 2 and as reference [7] on p. 10; it does not answer the
question. Citation indexes and web search are incomplete, so this is a
search result, not an assertion that no answer can exist.

All asymptotics below are along the indicated graph sequences; logarithms
are natural, (n=|V(G)|), and (L_1) denotes largest-component order.
Graphs are undirected and simple. Edgeless graphs have \(L_1=1\); henceforth \(\lambda>0\). The feasible parameters satisfy \(\sqrt\Delta\le\lambda\le\Delta\le n-1\): the first inequality follows from \(e_x^TA^2e_x=d(x)\), and the second from the maximum row sum. Put (q=1-\varepsilon\in(0,1)).

## 1. Where the source's factor comes from

Let (A) be the adjacency matrix, \(\lambda=\|A\|_2\), and
\(W_k(x)=(A^k\mathbf1)_x\). For \(k\ge1\),
\[
 W_k(x)=\langle Ae_x,A^{k-1}\mathbf1\rangle
 \le \sqrt{d(x)}\lambda^{k-1}\sqrt n.
 \tag{1}
\]
The source's Lemma 2.4 (p. 9) uses the positive resolvent vector
\[
 u=\sum_{k\ge0}\frac{A^k\mathbf1}{[(1+\eta)\lambda]^k}.
\]
Consequently
\[
 1\le u_x\le 1+\frac{\sqrt{n\Delta}}{\eta\lambda},\qquad
 Au=(1+\eta)\lambda(u-\mathbf1).
 \tag{2}
\]
After dividing by a uniform upper bound \(U\) for \(u_x\), the weights
\(w=u/U\) lie between \(1/U\) and 1 and satisfy
\(Aw\le(1+\eta)\lambda w\). The weighted exploration estimate, Lemma 3.1(a)
on p. 11, makes the probability of a component of weight \(t\) exponentially
small in \(t\). A union bound over \(n\) roots gives weight \(O_\varepsilon(\log n)\).
Converting weight to vertex count costs \(U\), yielding
\[
 L_1=O_\varepsilon\!\left(\frac{\sqrt{n\Delta}}\lambda\log n\right)
 \quad\hbox{with high probability}.
\]
The loss comes from (1), followed by the global maximum-to-minimum weight
comparison. An actual Perron eigenvector can have very small coordinates;
the resolvent replaces it with a positive approximate eigenvector.

The separate proof of Theorem 1.3(II), pp. 18–19, counts all simple paths
using
\[
 \sum_{k\ge0}p^k\mathbf1^TA^k\mathbf1\le n/\varepsilon.
\]
A component of size \(s\) supplies at least \(s(s-1)/2\) nontrivial paths.
Markov's inequality gives \(L_1=O_{\mathbb P}(\sqrt n)\). This is tightness in
probability: it does **not** assert a fixed universal multiple of \(\sqrt n\)
with probability tending to one. Confusing these two proof mechanisms or
these two probability quantifiers obscures the gap.

## 2. A connected counterexample throughout the strict opposite regime

### Theorem A

Suppose \(q(1+\delta)>1\). There are integers \(k,b\) with
\[
 k\ge2\sqrt b,\qquad k\le b,\qquad
 b+1<(1+\delta)k,\qquad
 \mu:=b\left(1-e^{-q/(k+1)}\right)>1.
 \tag{3}
\]
For every fixed \(\tau\ge0\), let \(T_{b,h}\) be the complete rooted
\(b\)-ary tree with levels \(0,\ldots,h\). Join its root by one edge to one
vertex of \(K_{k+1}\); call the resulting graph \(H_h\). Replace every vertex
of \(H_h\) by an independent set of
\(m_h=\lceil b^{\tau h}\rceil\) vertices, and every edge by the complete
bipartite graph between its two sets. Call this graph \(G_h\).

These are connected simple graphs. If
\[
 n_h=m_h\left(k+1+\frac{b^{h+1}-1}{b-1}\right),\qquad
 p_h=q/\lambda(G_h),
\]
then
\[
 \Delta(G_h)=m_h(b+1)\le(1+\delta)\lambda(G_h),\qquad
 \lambda(G_h)=\Theta(n_h^{\tau/(1+\tau)}).
 \tag{4}
\]
For every
\[
 0<c<\frac{\log\mu}{(1+\tau)\log b},
 \qquad
 \mathbb P\big(L_1((G_h)_{p_h})\ge n_h^c\big)\longrightarrow1.
 \tag{5}
\]
The case \(\tau=0\) uses no vertex replacement. Taking
\(\tau=a/(1-a)\) gives the claimed spectral growth \(n^a\).

### Proof

**Parameter choice.** Choose a fixed \(r\) with \(1/q<r<1+\delta\), set
\(b=\lfloor rk\rfloor\), and let \(k\) be a sufficiently large integer.
Then \(b/k\to r\), \(k\ge2\sqrt b\), \(b\ge k\), and
\[
 b(1-e^{-q/(k+1)})\longrightarrow rq>1.
\]
The strict degree inequality in (3) also follows for all sufficiently large
\(k\). Hence (3) is feasible for every stated pair \((\varepsilon,\delta)\).

**Spectral estimate.** For every real vector \(x\) on the tree,
\[
 |x^TA_{T_{b,h}}x|
 \le\sum_{uv:\ u\text{ parent of }v}
       \big(b^{-1/2}x_u^2+b^{1/2}x_v^2\big)
 \le2\sqrt b\,\|x\|_2^2.
\]
Thus \(\lambda(T_{b,h})\le2\sqrt b\). The disjoint union of the tree and
the clique has spectral radius \(k\). The added bridge has symmetric
adjacency matrix of operator norm 1, so the Rayleigh variational principle
gives
\[
 k\le\lambda(H_h)\le k+1.
 \tag{6}
\]
For \(h\ge1\), the tree root after adding the bridge has degree \(b+1\),
and all degrees are at most \(b+1\). The replacement graph has adjacency
matrix \(A_{H_h}\otimes J_{m_h}\), so
\[
 \lambda(G_h)=m_h\lambda(H_h),\qquad \Delta(G_h)=m_h(b+1).
\]
This proves (4), including its growth assertion since
\(\log n_h=(1+\tau)h\log b+O(1)\).

**An embedded branching process.** Write \(m=m_h\). Inside the replaced
tree, start at one specified vertex in a root set. For each of its \(b\)
child sets, test its \(m\) edges to that set. If at least one is open, choose
one endpoint there by a fixed deterministic rule, and continue downwards
from that single chosen vertex. Distinct tested edge sets are disjoint.
Conditioned on all previous choices, success for each child set has
probability
\[
 a_h=1-(1-p_h)^m
 \ge1-\exp(-mp_h)
 \ge1-\exp[-q/(k+1)].
 \tag{7}
\]
There is only one selected vertex per visited set, and different vertices
have different child sets, so no collisions occur. Independent thinning of
the successes couples the selected process from below with a Galton–Watson
process with offspring \(X\sim\operatorname{Bin}(b,a_0)\), where
\(a_0=1-e^{-q/(k+1)}\) and \(\mathbb EX=\mu>1\).
Each selected vertex belongs to the actual open component.

Here is a finite-generation estimate, to avoid relying on an unproved
survival asymptotic. Let \(Z_0=1\) and \(Z_\ell\) denote this process's
size in generation \(\ell\), with \(\sigma^2=\operatorname{Var}X\).
Conditioning on \(Z_\ell\) gives
\[
 \mathbb EZ_\ell=\mu^\ell,\qquad
 \frac{\mathbb EZ_\ell^2}{\mu^{2\ell}}
 =1+\frac{\sigma^2}{\mu(\mu-1)}(1-\mu^{-\ell})\le C,
 \quad C:=1+\frac{\sigma^2}{\mu(\mu-1)}.
\]
Indeed the second formula follows by iterating
\(\mathbb EZ_{\ell+1}^2=\mu^2\mathbb EZ_\ell^2+
\sigma^2\mathbb EZ_\ell\). Cauchy–Schwarz, applied to
\(Z_\ell\mathbf1_{\{Z_\ell\ge\mathbb EZ_\ell/2\}}\), yields
\[
 \mathbb P(Z_\ell\ge\mu^\ell/2)\ge1/(4C)=:s_0>0.
 \tag{8}
\]

**Amplification to high probability.** Fix a small \(\eta\in(0,1)\), and
put \(j=\lfloor\eta h\rfloor\). The \(b^j\) descendant trees rooted at
level \(j\), including their replacement sets, have disjoint edge sets.
Run the preceding exploration from one specified vertex in each, without
using any edge to a parent or to the clique. Their successes in (8) are
independent. Therefore
\[
 \mathbb P\!\left(L_1<\tfrac12\mu^{h-j}\right)
 \le(1-s_0)^{b^j}\longrightarrow0.
 \tag{9}
\]
For any \(c\) in (5), choose \(\eta\) so that
\(c<(1-\eta)\log\mu/[(1+\tau)\log b]\).
Then \(\mu^{h-j}/2\ge n_h^c\) for sufficiently large \(h\).
This proves (5). The bridge need not survive: the large component already
exists within one descendant tree. ∎

For a concrete small-ratio example, take
\(\varepsilon=0.02,\ \delta=0.1,\ k=100,\ b=108\).
Then \(\Delta/\lambda\le109/100=1.09\),
\(\mu=1.0428532233\ldots\), and
\(\log\mu/\log108=0.0089618249\ldots\).
With \(m_h=108^h\), both \(\lambda\) and \(\Delta\) are of order
\(\sqrt n\), and \(L_1\ge n^{0.004}\) with high probability.
These exponents are conservative proven lower bounds, not fitted optimal
exponents. The example has many leaves; the source's definition of
“close to regular” controls \(\Delta/\lambda\), not minimum degree.

## 3. The logarithmic regime, and its boundary

### Proposition B: the known strict logarithmic regime

If \(p\Delta\le1-\kappa\) for a fixed \(\kappa\in(0,1)\), then for every
integer \(s\ge2\),
\[
 \mathbb P(L_1\ge s)\le
 n\exp[-\kappa^2(s-1)/2].
 \tag{10}
\]
Consequently, if \(\Delta\le(1+\delta)\lambda\) and
\(q(1+\delta)<1\), then
\(L_1=O_{\varepsilon,\delta}(\log n)\) with high probability, with the
explicit gap \(\kappa=1-q(1+\delta)\).

**Proof.** Breadth-first exploration of one component is dominated by a
branching process with offspring \(\operatorname{Bin}(\Delta,p)\), by
providing independent extra trials whenever the graph exploration has fewer
unseen neighbors. If the total progeny is at least \(s\), the first \(s-1\)
particles have at least \(s-1\) children in total. With \(N=s-1\), exponential
Markov at \(t=-\log(1-\kappa)\) bounds that probability by
\[
 \exp\{N[\kappa+\log(1-\kappa)]\}
 \le\exp(-N\kappa^2/2).
\]
Here the binomial moment generating function was bounded by that of a
Poisson variable with mean at most \((1-\kappa)N\).
Take a union bound over roots. ∎

This is an existing result, not a new theorem: Diskin–Erde–Kang–Krivelevich,
[arXiv:2209.03722](https://arxiv.org/abs/2209.03722), Theorem 2, PDF p. 3,
gives \(9\kappa^{-2}\log n\) for **any** host of maximum degree \(\Delta\).
The order cannot be improved uniformly: on \(C_n\), \(\lambda=\Delta=2\)
and \(p=q/2\). Partition its edges into disjoint paths of length
\(\ell=\lfloor c\log n\rfloor\), with \(0<c<1/|\log p|\).
The independent events that these paths are fully open have probability
\(p^\ell\), and their expected number is
\(\lfloor n/\ell\rfloor p^\ell\to\infty\). The probability that none
occurs is at most \(\exp[-\lfloor n/\ell\rfloor p^\ell]\to0\).
Hence \(L_1=\Omega_\varepsilon(\log n)\) with high probability, already
within the exactly regular case.

### Proposition C: a polylogarithmic bound at equality

If \(p\lambda\le q<1\) and \(p\Delta\le1\), then
\[
 L_1=O_\varepsilon((\log n)^3)\quad\hbox{with high probability}.
 \tag{11}
\]
In particular this applies at \(q(1+\delta)=1\). It is not asserted to be
sharp there.

**Proof.** The case \(p=0\) is immediate. Otherwise let
\(u=(I-pA)^{-1}\mathbf1\) and \(U=\max_x u_x\). This is finite because
\(p\|A\|_2\le q<1\). Put \(B=\sqrt{n\Delta}/\lambda\ge1\).
Using (1) and the elementary bound \(W_j(x)\le\Delta^j\),
\[
 U\le1+\sum_{j\ge1}\min\{1,Bq^j\}
 \le1+J+1/\varepsilon,
 \quad J=\left\lceil\frac{\log B}{\log(1/q)}\right\rceil.
 \tag{12}
\]
The first \(J\) terms are at most 1 and the remaining geometric tail is
at most \(1/\varepsilon\). Since \(B\le n\), \(U=O_\varepsilon(\log n)\).

Consider the multitype branching process whose types are vertices, in which
a particle of type \(x\) has an independent Bernoulli\((p)\) child of type
\(y\) for every neighbor \(y\) of \(x\). Copies of a type are allowed.
Graph component exploration is dominated by this process: ignore children
whose vertex labels were already discovered, and use fresh trials for all
remaining potential children. Its expected total progeny vector is \(u\),
and \(pAu=u-\mathbf1\).

Let \(a=1/(2U^2)\) and \(\theta=1/(4U^2)\). The exponential moment of
total progeny through any fixed generation, starting at type \(x\), is at
most \(e^{au_x}\). To prove this by induction on the number of generations,
use independence of the children and, for \(0\le z\le1\),
\(e^z-1\le z+z^2\). Since \(au_y\le1/2\), the induction step is bounded by
\[
 \begin{aligned}
 \exp\!\left[\theta+p\sum_{y\sim x}(e^{au_y}-1)\right]
 &\le\exp[\theta+a(u_x-1)+a^2U(u_x-1)]\\
 &\le\exp[au_x],
 \end{aligned}
\]
because \(\theta+a^2U^2=a\). The initial single-particle case also satisfies
the bound. Monotone convergence extends it to the full total progeny \(T\).
Thus, for every root,
\[
 \mathbb P(|C_x|\ge s)\le\mathbb P(T\ge s)
 \le\exp\!\left(\tfrac12-\frac{s}{4U^2}\right).
 \tag{13}
\]
A union bound at \(s=4U^2(3\log n+1)\) proves (11). ∎

## 4. A degree-sensitive refinement of the resolvent estimate

The following upper bound is useful beyond the strict logarithmic regime.
It is a refinement of the source's method, not a matching answer in general.
Write \(R=\Delta/\lambda\ge1\), \(B=\sqrt{n\Delta}/\lambda\), and choose
any fixed \(a\) with \(1<a<1/q\). Define
\[
 U_a=1+\sum_{j\ge1}a^{-j}\min\{R^j,B\},\qquad \theta=1-qa>0.
 \tag{14}
\]
For \(n\ge2\) and \(p\le q/\lambda\),
\[
 \mathbb P\!\left(L_1\ge
 \left\lceil4\theta^{-2}U_a(1+3\log n)\right\rceil\right)\le n^{-2}.
 \tag{15}
\]

**Proof.** Equations (1) and \(W_j\le\Delta^j\) give
\(1\le u_x\le U_a\) for \(u=\sum_{j\ge0}(A/(a\lambda))^j\mathbf1\).
The weights \(w=u/U_a\) obey \(0<w\le1\), \(w_x\ge1/U_a\), and
\(Aw\le a\lambda w\).

For completeness, the weighted exponential-tail argument is as follows.
Explore a root component by querying each boundary edge at most once.
Before trial \(i\), let \(z_i\in[0,1]\) be the weight of its as-yet-undiscovered
endpoint; pad exhausted exploration by trials of weight zero. Conditional
on the past its open indicator \(Y_i\) is Bernoulli\((p)\), so for
\(t\in[0,1/2]\),
\[
 \mathbb E[e^{tY_i z_i}\mid\mathcal F_{i-1}]
 \le\exp[p t(1+t)z_i].
\]
The product of the resulting exponential factors is a supermartingale with
initial value 1. Over the whole exploration,
\(\sum Y_i z_i=w(C)-w(x)\ge w(C)-1\), and
\(\sum z_i\le\sum_{v\in C}(Aw)_v\le a\lambda w(C)\).
Take \(t=\theta/2\). Since \(pa\lambda\le1-\theta\), the final
supermartingale is at least
\[
 \exp[\theta^2 w(C)/4-1].
\]
Markov's inequality yields
\(\mathbb P(w(C)\ge z)\le\exp(1-\theta^2z/4)\).
Use \(w(C)\ge|C|/U_a\) and a union bound to obtain (15). ∎

For \(R>1\), put \(J=\lfloor\log B/\log R\rfloor\). The sum is explicit:
\[
 U_a=1+\sum_{j=1}^{J}(R/a)^j+\frac{Ba^{-J}}{a-1}.
 \tag{16}
\]
For \(R=1\), \(U_a=a/(a-1)\). For fixed \(R,a\), (16) gives
\[
 U_a=\begin{cases}
 O_{R,a}(1),&R<a,\\
 O_a(1+\log B),&R=a,\\
 O_{R,a}(B^{1-\log a/\log R}),&R>a.
 \end{cases}
\]
When \(R>1/q\) is fixed, for every fixed \(\zeta>0\) we can choose \(a<1/q\)
sufficiently close to \(1/q\) to obtain
\[
 L_1=O_{\varepsilon,R,\zeta}
 \left(B^{\,\log(qR)/\log R+\zeta}\log n\right)
 \quad\hbox{with high probability}.
 \tag{17}
\]
Here the chosen exponent can be taken below 1. This improves the source's
\(B\log n\) when \(R\) is bounded. The upper exponent in (17) and the lower
exponent in Theorem A generally differ; no matching claim is made.

## 5. Constructions and what they establish

There is no complete known-to-this-review regime classification. The table
records constructions or bounds with their quantifiers, rather than filling
unresolved cells with conjectured optima.

| Regime/family | Parameters and established lower behavior at \(p=q/\lambda\) | Upper-bound comparison |
|---|---|---|
| Dense spectral regime, including \(K_n\) | If \(\lambda=\Theta(n)\), then \(B=O(1)\) and the source gives \(L_1=O_\varepsilon(\log n)\) whp; \(K_n\) attains \(\Omega_\varepsilon(\log n)\), proved below | Also covered by BBCR Theorem 3, PDF p. 8 / journal p. 156 |
| Cycle \(C_n\) | \(\Delta=\lambda=2\); \(L_1=\Theta(\log n)\) whp, proved above | Proposition B matches |
| Star \(K_{1,t}\) | \(n=t+1,\Delta=t,\lambda=\sqrt t\); \(L_1=1+\operatorname{Bin}(t,q/\sqrt t)=(q+o(1))\sqrt t\) whp | Theorem 1.3 has the right scale in probability; Theorem 1.4 loses a log |
| \(K_{s,t}\), fixed \(s\), \(t\to\infty\) | \(\Delta=t,\lambda=\sqrt{st}\); \(L_1=\Theta_{s,q}(\sqrt t)\) whp | For varying \(s\), constants cannot be made uniform in the same way: source pp. 4 and 19 |
| \(K_{s,s^3}\), \(s\to\infty\) | \(n\asymp s^3,\Delta=s^3,\lambda=s^2\); source Section 5, p. 20 and footnote 6, gives \(\Omega_q(s\log s)\) whp | Theorem 1.4 gives \(O_q(s\log s)\), matching |
| Clique core with a pendant star | \(K_m\) with \(t\) leaves at one core vertex; \(\Delta=m-1+t\). Radius given below. Retained leaves give \(\Omega_q(t/\lambda)\) whp if \(t/\lambda\to\infty\) | For \(m\asymp\sqrt t\), this realizes \(\Theta(\sqrt n)\) whp; proved below |
| Calibrated clique and separate star joined by a bridge | For integers \(k+1\le D\le k^2\), join \(K_{k+1}\) to a leaf of \(K_{1,D}\). Then \(\Delta=D,\lambda\in[k,k+1]\), \(n=D+k+2\), and \(L_1=\Theta_q(D/k+\log k)\) whp as \(k\to\infty\) | Gives explicit lower examples throughout \(\sqrt\Delta\lesssim\lambda\le\Delta\); a family-specific matching bound, not the universal optimum |
| Regular core, equal pendant stars | Attach \(t\) leaves to every vertex of a connected \(d\)-regular graph \(F\): \(n=(t+1)|F|\), \(\Delta=d+t\), \(\lambda=(d+\sqrt{d^2+4t})/2\) | Retained leaf stars give \(\Omega_q(t/\lambda)\) if this mean diverges; expansion of \(F\) alone does not remove this obstruction |
| Dense core plus pendant branching tree | Theorem A, \(m_h=1\), has fixed \(\Delta,\lambda\) with \(\Delta/\lambda<1+\delta\), and polynomial components whenever \(q(1+\delta)>1\) | Refined (17) improves the source but leaves a gap |
| Replaced core and branching tree | Theorem A with \(m_h\to\infty\): arbitrary \(\lambda,\Delta=\Theta(n^a)\), \(a<1\), and polynomial lower bound | Shows that the obstruction persists for growing spectral radius |
| Finite \(b\)-ary trees without a core | \(\Delta=b+1\), \(\lambda\le2\sqrt b\); if \(qb/(2\sqrt b)>1\), the same second-moment argument produces polynomial components | This is the type of bounded-radius example already noted in source footnote 7, p. 20; its ratio is much larger than 1 for large \(b\) |
| Disjoint unions and padding | \(\lambda(\bigsqcup H_i)=\max_i\lambda(H_i)\), likewise for \(\Delta\); isolated vertices increase \(n\) without changing either parameter | Repetition amplifies rare large components; padding alone does not prove a matching lower bound in the new \(n\) |

Here is a proof of the dense clique lower bound, also used for the
calibrated-core row. In \(G(N,c/N)\), fix \(c\in(0,1)\), and let \(X\) count
components that are paths on \(\ell=\lfloor a\log N\rfloor\) vertices.
There are \((N)_\ell/2\) distinct candidate paths, and
\[
 \mathbb EX=\frac{(N)_\ell}{2}(c/N)^{\ell-1}
 (1-c/N)^{\ell(N-\ell)+\binom\ell2-(\ell-1)}
 =\frac{N}{2c}\exp[\ell(\log c-c)+o(1)].
\]
Choose \(0<a<1/(c-\log c)\); this expectation diverges. Two different
candidate path-components that overlap have incompatible events. For two
vertex-disjoint candidates, their joint probability divided by the product
of their probabilities is \((1-c/N)^{-\ell^2}=1+O(\ell^2/N)\): only the
closed edges between the two paths were counted twice. It follows that
\[
 \operatorname{Var}X\le\mathbb EX+O(\ell^2/N)(\mathbb EX)^2,
\]
and Chebyshev implies \(X>0\) with high probability. This proves the
logarithmic lower bound. Monotonicity transfers it to \(p=q/(N-1)\).

For the separate star and clique joined by a bridge, attach the bridge to
a **leaf** of the star and to one clique vertex. The maximum degree is
exactly \(D\), since \(D\ge k+1\). Before the bridge the radius is
\(\max(k,\sqrt D)=k\), and the bridge norm is 1, proving
\(k\le\lambda\le k+1\). Retained core components have maximum order
\(O_q(\log k)\) by Proposition B and \(\Omega_q(\log k)\) by the preceding
path argument, using monotonicity from \(p\ge q/(k+1)\).
The star-center degree has mean between \(qD/(k+1)\) and \(qD/k\).
Chernoff bounds give order \(D/k\) whenever \(D/k\ge\log k\), and an upper
bound \(O_q(D/k+\log k)\) with high probability in all cases. If
\(D/k<\log k\), the core lower bound already suffices. At most one core
component and one star component can be joined by the bridge. Combining
these observations proves the table's family-specific
\(\Theta_q(D/k+\log k)\) assertion.

For fixed \(s\), the bipartite row has a direct proof. One vertex on the
small side has \(\operatorname{Bin}(t,p)\) neighbors with diverging mean
\(q\sqrt{t/s}\); Chernoff gives a lower bound. All nontrivial components
together use at most the total number of retained edges plus the \(s\)
small-side vertices; that edge count is \(\operatorname{Bin}(st,p)\)
with mean \(q\sqrt{st}\), giving the upper bound. The \(K_{s,s^3}\) logarithmic
lower bound is a cited source result, not claimed as independently proved
here. Its mechanism is a logarithmic cluster on the small side, with order
\(s\) private leaves per small-side vertex. It is essential that the small
side itself grows.

For the clique-plus-star construction, partition into the hub, the other
\(m-1\) core vertices and the \(t\) leaves. The symmetric quotient is
\[
 Q=\begin{pmatrix}
 0&\sqrt{m-1}&\sqrt t\\
 \sqrt{m-1}&m-2&0\\
 \sqrt t&0&0
 \end{pmatrix}.
 \tag{18}
\]
Its largest eigenvalue is the spectral radius: a positive eigenvector
constant on these classes is a positive eigenvector of the full connected
graph. If \(m\asymp\sqrt t\), it is \(\Theta(\sqrt t)\). The retained
star contributes \(\Theta(\sqrt t)\) whp, while the entire percolated clique
has only \(O(m)\) edges whp, since \(p=O(1/m)\). The whole graph then has
\(O(\sqrt t)\) retained edges whp, proving the matching upper bound for
this family. The clique is an expanding core; it does not suppress the star.

For equal pendant stars on a \(d\)-regular core, assign weight 1 to every
core vertex and \(1/\lambda\) to every leaf. The eigenvalue equation is
\(\lambda=d+t/\lambda\), giving the formula in the table; positivity and
connectedness identify the Perron eigenvalue. A pendant-star lower bound
again follows directly from its binomial degree.

For \(M\) disjoint copies of one graph with component maximum distribution
\(F(s)=\mathbb P(L_1\le s)\), independence gives
\(\mathbb P(L_1(\bigsqcup_{i=1}^M H_i)_p\le s)=F(s)^M\).
This explains why a fixed-confidence statement cannot silently be upgraded
to high probability uniformly over all hosts with the same local parameters.
Connecting copies by bridges changes the spectral radius, so any connected
version must recalculate \(p\); Theorem A does this explicitly.

## 6. Computational evidence

The completed run used 30 hosts and 40 independent percolation trials per
host, totaling 1,200 trials. The largest host had 1,118,688 vertices. The
simulation process inherited nice 10 and requested one numerical thread;
one additional thread checked peak RSS every 50 ms against a 3 GiB stop
threshold. Recorded peak RSS was **1,008,943,104 bytes** (about 1.01 GB),
and simulation wall time was 11.31 seconds. No dense million-vertex adjacency
matrix was formed. Managed macOS rejected OS resource-limit changes; the
recorded memory guard is a watchdog, not a claimed hard address-space limit.

Complete bipartite and clique edges were sampled by geometric waiting times
on their implicit edge lists, exactly implementing independent Bernoulli
retention. Replaced tree edges were sampled over implicit complete bipartite
blocks. The planted-hub host at each size was one seeded
\(G(n,6/(n-1))\) base with four added hubs of target degrees approximately
\(n^{0.6},n^{0.6}/2,n^{0.6}/4,n^{0.6}/8\), deduplicated to a simple graph.
Its spectral radius was computed from the **host**, before retention, using
the largest adjacency eigenpair; maximum absolute residual was
\(8.90\times10^{-10}\). Other radii used exact analytic or equitable-quotient
formulas. All samples used \(p=(1-\varepsilon)/\lambda\).

| Family | Largest tested \(n\) | \(\varepsilon\) | Median \(L_1\) | Empirical 10–90% interval | Descriptive power-fit slope |
|---|---:|---:|---:|---:|---:|
| Balanced complete bipartite | 1,000,000 | 0.2 | 168 | 142.9–203.7 | 0.269 |
| \(K_{s,s^3}\) | 1,000,100 | 0.2 | 712.5 | 400.1–1268.6 | 0.482 |
| Star | 1,000,000 | 0.2 | 800 | 758.7–824.8 | 0.491 |
| Star plus clique core | 1,000,000 | 0.2 | 784.5 | 758.0–820.6 | 0.520 |
| Random base with planted hubs | 1,000,000 | 0.2 | 54 | 47.9–66.0 | 0.178 |
| Clique plus 16-ary tree | 1,118,494 | 0.1 | 28.5 | 23.0–42.2 | 0.170 |
| Replaced clique plus tree | 1,118,688 | 0.1 | 41 | 34.9–63.0 | 0.195 |

The two near-regular families use \(k=12,b=16\), so their exact ratio is
at most \(17/12<1.5\). The replacement multiplicity is \(2^h\); this is
Theorem A with \(\tau=\log 2/\log16=1/4\). The tested heights are small.

Power slopes are ordinary least-squares fits of \(\log(\operatorname{median}
L_1)\) against \(\log n\), across all tested sizes, including the smallest.
They are **not asymptotic exponents**. The balanced bipartite control has a
positive apparent power slope despite its proved logarithmic asymptotics;
an affine fit in \(\log n\) has smaller original-scale error there. The
bipartite cubic family's expected logarithmic correction also inflates a
power-only slope above \(1/3\). The near-regular samples cannot distinguish
an eventual small power from slow polylogarithmic growth. Their polynomial
lower bounds rest entirely on Theorem A.

`data/fits.csv` contains power and affine-log fits, errors, and 1,000-resample
bootstrap intervals. These intervals measure percolation sampling variability
conditional on the chosen hosts; they exclude finite-size bias, uncertainty
in the fitted model, and planted-host randomness. The largest absolute
open-edge-count mean z-score across the 30 host cases was 3.392; this is a
diagnostic, not a proof of sampler correctness.

Reproduce from this directory:

```sh
python3 code/verify.py
python3 code/simulate.py --reps 40 > data/simulation_progress.txt 2>&1
python3 code/analyze.py
```

Installed versions used: NumPy 2.2.3 and SciPy 1.15.2. The machine already
provided these packages. No installation or external publication was needed.
Raw trials are in `data/trials.csv`, size summaries in `data/summary.csv`,
host seeds and hashes in `data/hosts.json`, and resource settings in
`data/simulation_metadata.json`. The standalone plot is
[data/scaling.svg](data/scaling.svg). No simulation is used as proof.

## 7. Verification and remaining scope

The theoretical work checks the exact inequality separating the two strict
near-regular regimes, the bridge perturbation, the degree of the connector,
the scaling of both spectral radius and maximum degree under replacement,
the independence of the descendant explorations, and amplification of a
constant success probability to high probability. In particular, root
survival alone would not have sufficed for the claimed probability.

A remaining gap is the optimal exponent above the boundary, even for many
fixed ratios \(\Delta/\lambda\). At the boundary the logarithmic lower bound
and the cubic-logarithmic upper bound here do not match. For ratios tending
to one with fixed \(\varepsilon>0\), Proposition B eventually applies and
gives the established logarithmic bound. The full prescribed-parameter
problem remains unresolved by this work.

Task: “Open problem G0010” — first local clock reading 2026-11-13 08:49:07 +04.
