PARTIAL

# C0092: sharpness of the random-cluster transition below one

The general assertion for \(0<q<1\) on \(\mathbb Z^d\), \(d\ge2\), is not proved here. The literature audit did not locate a theorem covering that range. The proved results below are a quantitative comparison interval near \(q=1\), sharpness for the free model on regular trees, an explicit obstruction to the unmodified OSSS argument, and a conditional sharpness theorem with its missing covariance hypotheses stated precisely. The comparison and tree calculation are established facts, reproduced with proofs; no novelty is claimed for them. Neither a lattice perturbation theorem nor a large-d sharpness theorem was obtained.

## 1. Statement and infinite-volume convention

For a finite graph \(G=(V,E)\), including isolated vertices in the component count, let
\[
\phi_{G,p,q}(A)=Z^{-1}p^{|A|}(1-p)^{|E|-|A|}q^{k(A)},\qquad 0<p<1,\quad q>0.
\]
A boundary condition identifies specified boundary vertices before counting components.

The source is M. Heydenreich and R. van der Hofstad, *Progress in high-dimensional percolation and random graphs* (Springer, 2017), Open Problem 16.10, published p. 254. In the [author-hosted March 17, 2017 manuscript](https://rhofstad.win.tue.nl/survey-high-d-percolation.pdf), the same problem is on p. 242, at the end of §16.4, pp. 239–242. Chapter 16, pp. 227–242, was read, including the preceding negative-association problem. Its range is explicitly **q > 0**, not only q >= 1.

For an infinite-volume family \((\mu_p)\), write
\[
\chi(p)=\sum_x\mu_p(0\leftrightarrow x)=\mathbb E_{\mu_p}|C(0)|,\qquad
\theta(p)=\mu_p(|C(0)|=\infty),
\]
\[
p_T=\sup\{p:\chi(p)<\infty\},\qquad
p_P=\inf\{p:\theta(p)>0\}.                                      \tag{1}
\]
The requested assertion is \(p_T=p_P\).

The source's infinite-volume paragraph does not specify a unique canonical measure below one. Compactness gives subsequential finite-volume limits, but does not by itself give uniqueness, a full limit for every p, or independence of the boundary condition. Those points cannot be inherited from the attractive case. Unless stated otherwise, comparisons below apply to every weak limit of finite-box FK measures with arbitrary boundary partitions, and also to periodic-torus limits. The conditional theorem in §5 specifies its limit family.

At a fixed p, finite susceptibility implies zero percolation probability. Without p-monotonicity this implication alone does **not** order the supremum and infimum in (1): it does not exclude a finite-susceptibility parameter above a different percolative parameter. No such behavior is asserted here.

## 2. Literature result

Duminil-Copin, Raoufi and Tassion, *Sharp phase transition for the random-cluster and Potts models via decision trees*, Ann. Math. **189** (2019), 75–99, **Theorem 1.2, p. 80**, proves sharpness for \(q\ge1\) on locally finite transitive weighted graphs, with the extensions stated there. On \(\mathbb Z^d\), exponential one-arm decay implies finite susceptibility. Its decision-tree inequality, **Theorem 1.1, p. 77**, assumes a monotonic measure. [Published article](https://annals.math.princeton.edu/2019/189-1/p02).

The most directly relevant recent below-one results found were:

- Beffara–Faipeur–Oke, *A new bound for the critical point of the FK model for q<1*, arXiv:2512.16486v1 (2025), **Theorem 1.4, p. 6**, strictly extends the Bernoulli comparison regions for every fixed q<1 on all hypercubic lattices d>=2 (and the stated quasi-transitive graphs). **Theorems 1.10 and 1.11, p. 11**, give strong uniqueness in the extended subcritical region and, in the plane, an extended supercritical region. Their **§1.4, p. 10**, explicitly leaves existence of a critical point below one open. This is the closest lattice result located, not a sharpness theorem. [Preprint](https://arxiv.org/abs/2512.16486).
- Park, arXiv:2608.08565v1 (2026), **Theorem 5.5, p. 21; Theorem 5.8 and Corollary 5.9, p. 26**: wired DLR uniqueness and phase diagram on regular trees, all \(0<q<1\), degree \(\Delta\ge3\). The branch correlation results are **Theorem 6.4, p. 30**, and **Corollary 6.5, p. 31**. They concern separated branches. [Preprint](https://arxiv.org/abs/2608.08565).
- Tang–Zhang, arXiv:2609.11578v2 (2026), **Theorem 1.2, p. 6**: pairwise negative correlation at fixed p on high-degree regular graph sequences satisfying explicit isoperimetric hypotheses. This is not critical-p sharpness on a fixed infinite lattice. [Preprint](https://arxiv.org/abs/2609.11578).
- Çiçeksiz–Ravichandran, arXiv:2610.00549v1 (2026), **Theorem 1.9, p. 6**: pairwise negative correlation on complete graphs with common activity at least one, plus other restricted results. [Preprint](https://arxiv.org/abs/2610.00549).

These preprints do not cover every \(q\in(0,1)\) and every \(d\ge2\), and do not justify RESOLVED_IN_LITERATURE.

[LITERATURE.md](LITERATURE.md) records the requested Grimmett, Kahn, Pemantle, Dubédat, Lyons–Peres, Hutchcroft, lecture-note and forest searches, with theorem numbers, page distinctions and parameter ranges. Full text conversions are in sources/; sources/manifest.jsonl.txt records URLs, retrieval times and hashes. Hutchcroft's volume-tail theorem requires \(q\ge1\); the nonamenable Ising result concerns q=2. The arboreal-gas results concern a q→0 scaling limit, not fixed positive q.

**Monotonicity conclusion.** General monotonicity of the percolation probability in p for fixed \(q\in(0,1)\) on \(\mathbb Z^d\) is not established by the literature located in this audit; it remains an unresolved input here. Grimmett's §5.8 deliberately works without stochastic ordering; Beffara–Faipeur–Oke, §1.4, p. 10, still treats existence of a critical point below one as open. This is not a claim that \(\theta\) is nonmonotone: loss of FKG and of monotone conditional probabilities does not itself disprove unconditional p-monotonicity. Mean total edge count is increasing in p, but that is weaker.

## 3. Exact proof obstructions and surviving identities

### Single-edge rule and energy

Let e have endpoints x,y. Conditional on all other edges \(\eta\), including the boundary identifications, put
\[
a=a_q(p)=\frac{p}{p+q(1-p)}.
\]
If x,y are already connected, opening e leaves k unchanged, so its open/closed weight ratio is \(p/(1-p)\). Otherwise opening e reduces k by one, and the ratio is \(p/[q(1-p)]\). Hence
\[
r_e(\eta)=\phi(\omega_e=1\mid\eta)=
\begin{cases}p,&x\leftrightarrow y\text{ off }e,\\
a,&\text{otherwise}.
\end{cases}                                                    \tag{2}
\]
For q<1, \(p<a<1\). Conditional on only some other edges the probability is an average of these values, still in [p,a]. Both edge states have uniformly positive conditional probabilities at fixed p,q. The domain Markov property also survives: conditioning on an exterior configuration leaves an FK law with its induced connectivity partition. No association is required.

### Derivative and the missing Russo term

Differentiating the finite sum for the partition function, for p-independent f and \(N=\sum_e\omega_e\),
\[
\frac{d}{dp}\phi(f)=\frac{\operatorname{Cov}(f,N)}{p(1-p)}.        \tag{3}
\]
Indeed the logarithmic weight derivative is \(N/p-(|E|-N)/(1-p)\); subtracting its mean proves (3). For f=N this is \(\operatorname{Var}(N)/[p(1-p)]\ge0\). For increasing f its sign is not determined. This is Grimmett's Theorem 3.12, p. 41, valid for every q>0.

There is an exact correction to the pivotal formula. Let \(C_e=1_{\{x\leftrightarrow y\text{ off }e\}}\), \(g_e(\eta)=\mathbb E[f\mid\eta]\), and \(\Delta_e f=f(\eta,1)-f(\eta,0)\). Conditional covariance gives
\[
\operatorname{Cov}(f,\omega_e)
=\mathbb E[r_e(1-r_e)\Delta_e f]-(a-p)\operatorname{Cov}(g_e,C_e). \tag{4}
\]
The first term is the conditional covariance; the second follows from \(r_e=a-(a-p)C_e\) and the law of total covariance. For an increasing indicator the first is a nonnegative weighted pivotal probability. The second is an uncontrolled global correction. For example, the explicit additional hypothesis
\[
(a-p)\sum_e\operatorname{Cov}(g_e,C_e)
\le(1-\lambda)\sum_e\mathbb E[r_e(1-r_e)\Delta_e f],\quad\lambda>0 \tag{5}
\]
would give a positive Russo-type lower bound by (4). Inequality (5) is not proved here and alone would not provide the decision-tree inequality.

### A triangle rules out the unmodified covariance OSSS inequality

On a triangle let \(v=p/(1-p)>0\) and let X,Y be two edge indicators. After cancelling a common factor,
\[
Z=q^3+3vq^2+3v^2q+v^3q,\quad
Z_X=vq^2+2v^2q+v^3q,\quad Z_{XY}=v^2q+v^3q.
\]
Multiplication and subtraction give
\[
\operatorname{Cov}(X,Y)
=\frac{ZZ_{XY}-Z_X^2}{Z^2}
=-\frac{v^3q^2(1-q)(v+q)}{Z^2}<0,\qquad 0<q<1.                 \tag{6}
\]
This explicitly disproves FKG.

More precisely take \(f=X\lor Y\), and query X first, then Y only if X=0. If \(s=\mathbb P(X=Y=0)\), \(u=\mathbb EX\), \(w=\mathbb EY\), the revealments are 1 and 1-u, and
\[
\operatorname{Cov}(f,X)=us,\quad
\operatorname{Cov}(f,Y)=ws,\quad
\operatorname{Var}(f)=s(1-s).
\]
The third edge is never queried. Thus
\[
\operatorname{Var}(f)-\sum_e\delta_e\operatorname{Cov}(f,\omega_e)
=s\{uw-\mathbb E[XY]\}=-s\operatorname{Cov}(X,Y)>0.              \tag{7}
\]
This is a counterexample to a direct application of DRT Theorem 1.1 below one, not a counterexample to sharpness. Also, disjoint occurrence for all events cannot hold here: \(\{X=1\}\) and \(\{Y=0\}\) depend on disjoint edges but have positive covariance by (6). BK restricted to increasing events is a different conjecture.

### Audit of the proof steps

| Step | Required property | Status below one |
|---|---|---|
| Attractive update coupling and usual boundary comparisons | Conditional edge probabilities increase in the exterior | Fails at (2): adding an alternative route changes a to the smaller p. Reversing the entire comparison is not justified either. |
| DRT Lemma 2.1, pp. 83–84 | Sequential conditional sampling | Survives for positive finite measures. |
| DRT proof of Theorem 1.1, pp. 85–86, (7) and (10) | Monotonicity of the uniform-variable encoding, then Harris/FKG to bound two cross terms | The encoding need not be increasing. The independent uniforms still satisfy Harris; its hypotheses on the encoded functions fail. The resulting inequality itself fails by (7) above. |
| Shell algorithm, DRT Lemma 3.2, pp. 88–90 | Geometry to bound revealment | Survives; proved in §5. Replacing edge-dependent revealments by a maximum also requires nonnegative covariances or cancellation control. |
| DRT derivative and finite-volume passage, pp. 90–91 | Covariance derivative, p-monotonicity, boundary comparisons to identify limits | The finite derivative survives. The other ingredients are not available in general below one. Tori remove spatial boundary comparison but not the covariance or limit issues. |
| DRT analytic Lemma 3.1, pp. 87–88 | Increasing functions of p and a differential inequality | Pure analysis; valid once the hypotheses have been established. |
| Menshikov pivotal-chain argument | Russo pivotal derivative, BK bounds for disjoint connections, independence of separated revealed pieces | Equation (4) replaces the pivotal formula with an uncontrolled correction. Increasing BK is not generally proved. The domain Markov property does not give independence of arbitrary unrevealed pieces. |
| Aizenman–Barsky magnetization inequalities | Product factorization/BK for disjoint witnesses, pivotal derivatives in p | Independent ghost marks still yield \(M(p,h)=\mathbb E[1-e^{-h|C|}]\) and its direct h-derivative for h>0. The necessary p and disjoint-connection inequalities do not follow. The Ising extension uses special current inequalities unavailable at arbitrary q<1. |

Pairwise negative correlation, negative association on disjoint fixed supports, conditional negative association, and BK for configuration-dependent disjoint witnesses are distinct. In particular, signs of \(\operatorname{Cov}(\omega_e,\omega_f)\) do not control \(\operatorname{Cov}(1_{\{0\leftrightarrow\partial\Lambda_n\}},\omega_e)\).

## 4. Unconditional results with complete proofs

### Proposition 1. Bernoulli comparison

For \(0<q\le1\), every finite graph and boundary partition satisfy
\[
\operatorname{Ber}(p)\preceq\phi_{p,q}
\preceq\operatorname{Ber}(a_q(p)).                              \tag{8}
\]
The same holds for every weak infinite-volume limit. If \(a_q(p_1)\le p_2\), then, on the same finite edge set with arbitrary boundary conditions,
\[
\phi_{p_1,q}\preceq\phi_{p_2,q}.                               \tag{9}
\]

**Proof.** Enumerate edges and reveal them using independent uniforms \(U_i\). The conditional probability \(r_i\) of the next edge being open is in [p,a], by (2) and conditional expectation. Set its state to \(1_{\{U_i\le r_i\}}\). Multiplication of conditional probabilities shows that the resulting configuration has law \(\phi\). It lies coordinatewise between \(1_{\{U_i\le p\}}\) and \(1_{\{U_i\le a\}}\), proving (8) without attractiveness. Weak convergence preserves comparison for increasing cylinder functions. Monotone approximation extends it to arm events, percolation probability and expected cluster size. Insert \(\operatorname{Ber}(a_q(p_1))\preceq\operatorname{Ber}(p_2)\) between the two applications of (8) to get (9). □

These are Grimmett's (5.117)–(5.118), p. 131. They compare separated p-values, not infinitesimally nearby values: (9) requires an odds ratio of at least 1/q.

### Corollary 2. A quantitative interval near one

Let \(t=p_c^{\rm Bern}(\mathbb Z^d)\) and
\[
\ell(q)=\frac{qt}{1-t+qt}.
\]
Every weak-limit state has finite susceptibility for \(p<\ell(q)\), and positive percolation probability for \(p>t\). For any selected family in (1),
\[
p_T,p_P\in[\ell(q),t],\qquad
|p_T-p_P|\le\frac{(1-q)t(1-t)}{1-(1-q)t}.                       \tag{10}
\]

**Proof.** The inequality \(p<\ell(q)\) is equivalent to \(a_q(p)<t\). Ordinary Bernoulli sharpness gives finite susceptibility at \(a_q(p)\), transferred by (8). For p>t, Bernoulli(p) has positive origin percolation probability, also transferred by (8). Thus all p below \(\ell(q)\) have finite susceptibility and no percolation, while all p above t percolate and have infinite susceptibility. This bounds the two extrema separately; subtracting the endpoints gives (10). No ordering of the two extrema was used. □

The imported result is Bernoulli sharpness, for example Heydenreich–van der Hofstad, Theorem 3.1 and the exponential version in Theorem 3.2, saved manuscript p. 27. For \(q=1-\varepsilon\), (10) is \(\varepsilon t(1-t)+O(\varepsilon^2)\). On \(\mathbb Z^2\) it is exactly \((1-q)/[2(1+q)]\). This is a conservative bound: Beffara–Faipeur–Oke, Theorem 1.4, improves both endpoint regions for each fixed q<1; it does not close the interval. This approaches zero as q approaches one but does not vanish at any fixed q<1. It is an interval estimate, not perturbative sharpness. In high dimensions, inserting the known Bernoulli asymptotic \(t\sim1/(2d)\) only shrinks the absolute interval; it does not establish equality.

There is a self-contained small-p bound needing no Bernoulli sharpness theorem. On any maximum-degree-\(\Delta\) graph there are at most \(\Delta(\Delta-1)^{r-1}\) simple paths of length r from a vertex. A specified path is open with probability at most \(a^r\), by (8). Every connection to another vertex has a simple path. Summing over paths and lengths gives
\[
\chi(p)\le1+\frac{\Delta a}{1-(\Delta-1)a},
\qquad (\Delta-1)a<1.                                        \tag{11}
\]
The probability of radius at least r is at most \(\Delta a[(\Delta-1)a]^{r-1}\). On \(\mathbb Z^d\), this applies for \(p<q/(2d-2+q)\). It uses energy and counting, not FKG or BK.

### Proposition 3. Free regular-tree sharpness

On the infinite \(\Delta\)-regular tree, \(\Delta\ge3\), the free finite-volume limit has a single sharp threshold for every q>0:
\[
p_T=p_P=\frac{q}{\Delta-2+q}.                                 \tag{12}
\]
Below it,
\[
\chi(p)=1+\frac{\Delta a_q(p)}{1-(\Delta-1)a_q(p)}.              \tag{13}
\]
At the threshold susceptibility is infinite and percolation probability is zero.

**Proof.** Any subgraph of a finite tree is a forest, with \(k(A)=|V|-|A|\). The weight factors as a constant times
\[
\prod_{e\in E}(p/q)^{\omega_e}(1-p)^{1-\omega_e}.
\]
Thus free edges are independent with parameter a. The finite laws are consistent and give the product law on the infinite tree. There are \(\Delta(\Delta-1)^{r-1}\) vertices at distance r, each connected by its unique path with probability \(a^r\). Summing proves (13), with divergence when \((\Delta-1)a\ge1\).

Explore away from the root. Every reached nonroot vertex has independent \(\operatorname{Bin}(\Delta-1,a)\) offspring. The probability of extinction by generation n is the nth iterate from 0 of
\[
G(s)=(1-a+as)^{\Delta-1};
\]
this follows by conditioning on the first generation and induction. Its limit is the least fixed point of G in [0,1]. If \(G'(1)=(\Delta-1)a\le1\), convexity, strict for 0<a<1, implies \(G(s)>s\) for s<1, so the least fixed point is 1. If \(G'(1)>1\), then \(G(1-h)<1-h\) for small h>0, whereas G(0)>0, giving a fixed point z<1. The root's survival probability is
\[
1-(1-a+az)^\Delta,
\]
positive exactly in the latter regime. Solving \((\Delta-1)p/[p+q(1-p)]=1\) proves (12). Endpoint p=0,1 follows directly. □

For \(\Delta=2\), the line has threshold p=1. Regular trees of degree at least three are nonamenable transitive graphs, so this supplies an exact result within that class, not on all nonamenable graphs.

Wiring the finite-tree boundary destroys the product factorization. The wired below-one threshold is also known: Grimmett, Theorem 10.82, p. 307, on the binary tree, and Park's general-degree results cited in §2. The free proof is not a proof that the supercritical wired law is product.

### Distinguishing q→0 limits

On a finite connected graph write the weight as \(q^{k(A)}v^{|A|}\). If \(v=q\beta\), the identity
\[
k(A)+|A|=|V|+c(A)
\]
expresses the exponent through cycle rank c. Removing \(q^{|V|}\) leaves \(q^{c(A)}\beta^{|A|}\), selecting forests. At fixed v>0, only the smallest component count k=1 survives as q→0, selecting connected spanning subgraphs. Finally, if v→0 and q/v→0, divide the weight by \(qv^{|V|-1}\); the remaining factor
\[
(q/v)^{k(A)-1}v^{c(A)}
\]
selects spanning trees. Finite summation and normalization prove these limits. They do not justify interchanging q→0, volume→infinity and critical-parameter limits.

## 5. Conditional sharpness with a quantitative negative-covariance bound

The following reduction separates a geometric fact from two unproved inequalities. Ordinary negative association is not asserted to imply its hypotheses.

Fix d>=2 and q in (0,1). Let \(\mu_{L,p}\) be FK on the side-L periodic lattice. Assume there is one sequence \(L_j\to\infty\) along which local laws converge to \(\mu_p\) for every p in (0,1). For L>4n, define
\[
f_n=1_{\{0\leftrightarrow\partial\Lambda_n\}},\quad
\theta_{n,L}=\mu_{L,p}(f_n),\quad \theta_{0,L}=1,\quad
S_{n,L}=\sum_{i=0}^{n-1}\theta_{i,L},
\]
\[
c_e=\operatorname{Cov}_{\mu_{L,p}}(f_n,\omega_e),\qquad
V=\sum_e(c_e)_+,\qquad N_-=\sum_e(-c_e)_+.
\]
The connection event is determined inside the sup-norm box \(\Lambda_n\): a path first hits its boundary before leaving it.

For k=1,...,n let \(T_{n,k}\) explore all open clusters inside \(\Lambda_n\) that meet \(\partial\Lambda_k\), querying incident edges with a fixed tie rule. Stop when the value of \(f_n\) is determined. Suppose that on every compact p-interval \([a,b]\subset(0,1)\), constants \(C<\infty\) and \(0\le\kappa<1\), independent of p,n,L, satisfy
\[
\operatorname{Var}(f_n)
\le C\sum_e\delta_e(T_{n,k})|c_e|
\quad\text{for each }k,                                      \tag{AO}
\]
\[
N_-\le\kappa V.                                               \tag{NC-budget}
\]
The budget sums over **all torus edges**, including unqueried ones, because those edges occur in the p-derivative. Constants may depend on a,b,d,q. The hypotheses are only for these arm events and shell algorithms.

**Theorem 4.** Under the local-limit hypothesis, (AO) and (NC-budget), there is a single \(p_*\in(0,1)\) for the family \((\mu_p)\). For p<p_* the one-arm probabilities decay exponentially and susceptibility is finite. For p>p_*, percolation probability is positive, with a locally uniform linear lower bound in p-p_*. Thus \(p_T=p_P=p_*\) for this family.

**Geometric revealment bound.** Every path from 0 to \(\partial\Lambda_n\) meets \(\partial\Lambda_k\), so the exploration determines the event. An edge xy can be queried only if x or y is connected to that sphere inside the box. For a vertex at radius r, such a connection entails reaching distance at least |r-k| from that vertex. Translation invariance on the torus gives
\[
\delta_{xy}(T_{n,k})\le
\theta_{|\|x\|_\infty-k|,L}+\theta_{|\|y\|_\infty-k|,L}.
\]
For 1<=r<=n, every possible distance 0,...,n-1 occurs at most twice as k varies. For r=0 the sum is \(\sum_{k=1}^n\theta_{k,L}\le S_{n,L}\), since arm probabilities decrease with radius. Hence
\[
\frac1n\sum_{k=1}^n\delta_e(T_{n,k})\le\frac{4S_{n,L}}n.        \tag{14}
\]
This bound uses geometry and translation invariance only.

**Covariance and derivative bound.** Put \(\rho=(1+\kappa)/(1-\kappa)\). The budget implies
\[
\sum_e|c_e|=V+N_-\le\rho(V-N_-)=\rho\sum_ec_e.
\]
Averaging (AO) in k, using (14), then the exact derivative (3), yields
\[
\theta'_{n,L}\ge
\frac{n}{4C\rho p(1-p)S_{n,L}}\theta_{n,L}(1-\theta_{n,L}).      \tag{15}
\]
In particular the finite-volume arm probabilities are increasing in p under these hypotheses.

For p<=b<1, revealing the 2d incident edges successively and using (2) gives probability at least
\[
\varepsilon_b=(1-a_q(b))^{2d}>0
\]
that they are all closed. Thus \(1-\theta_{n,L}\ge\varepsilon_b\). Since \(4p(1-p)\le1\), (15) implies
\[
\theta'_{n,L}\ge c\,\frac n{S_{n,L}}\theta_{n,L},\qquad
c=\frac{\varepsilon_b(1-\kappa)}{C(1+\kappa)}>0.                \tag{16}
\]

**Integrated passage to the limit.** Set \(\theta_n(p)=\mu_p(f_n)\), \(\theta_0=1\), \(S_n=\sum_{i<n}\theta_i\), and \(\theta=\lim_n\theta_n\). The last limit is the infinite-cluster probability by continuity for decreasing arm events. The functions are increasing in p. Integrating (16) before taking L→infinity gives
\[
\log\theta_n(v)-\log\theta_n(u)
\ge cn\int_u^v\frac{dt}{S_n(t)},\qquad a\le u<v\le b.           \tag{17}
\]
Bounded convergence applies because \(1\le S_{n,L}\le n\). Logarithms are finite since a specified length-n path has probability at least \(u^n\), by (2). Differentiability of the infinite-volume functions is not assumed.

**Subcritical bound.** Define
\[
p_*=\inf\left\{p:\limsup_{n\to\infty}
                   \frac{\log S_n(p)}{\log n}=1\right\}.       \tag{18}
\]
Because \(1\le S_n\le n\), the limsup is in [0,1]. The set is upward closed. It is nonempty: for p above the Bernoulli threshold, (8) implies \(\theta(p)>0\), hence \(S_n\ge n\theta(p)\). It stays away from zero: Corollary 2 and Bernoulli exponential decay give bounded S_n on a nonempty small-p interval. Therefore \(0<p_*<1\).

Take u<u'<v<p_*. At v the limsup in (18) is strictly less than one, so \(S_n(v)\le n^{1-\alpha}\) eventually, for some alpha>0. Monotonicity in p and (17) give
\[
\theta_n(u')\le \exp[-c(v-u')n^\alpha]
\]
for large n. Thus \(K=\sum_{n\ge0}\theta_n(u')<\infty\). A second use of (17), between u and u', gives
\[
\theta_n(u)\le \exp[-c(u'-u)n/K].                              \tag{19}
\]
Every u<p_* admits such u',v inside one compact interval, proving exponential decay throughout that region.

**Supercritical bound.** For n>=2 define
\[
T_n(p)=\frac1{\log n}\sum_{i=1}^n\frac{\theta_i(p)}i.
\]
It tends to \(\theta(p)\): split the sum at a fixed large index where \(\theta_i\) is close to its limit, then use \(\sum_{i\le n}1/i\sim\log n\).

At finite L, (16) implies
\[
T'_{n,L}\ge\frac c{\log n}\sum_{i=1}^n\frac{\theta_{i,L}}{S_{i,L}}
\ge\frac c{\log n}\log S_{n+1,L}.
\]
Indeed, \(\theta_i/S_i\ge\log(S_i+\theta_i)-\log S_i
=\log S_{i+1}-\log S_i\), and \(S_1=1\). Integrating from \(p_0\in(p_*,p)\) to p, using monotonicity of S, and passing L→infinity gives
\[
T_n(p)-T_n(p_0)\ge
c(p-p_0)\frac{\log S_{n+1}(p_0)}{\log n}.
\]
The limsup of the last ratio is one: every p0>p_* belongs to the upward-closed set in (18). Along a subsequence realizing that limsup,
\[
\theta(p)-\theta(p_0)\ge c(p-p_0).
\]
Let p0 decrease to p_* inside a single fixed compact interval to obtain \(\theta(p)\ge c(p-p_*)>0\).

Finally there are only polynomially many lattice sites at sup-norm distance r, and \(\mu_p(0\leftrightarrow x)\le\theta_r(p)\) for such a site. Equation (19) gives finite susceptibility below p_*. Positive percolation probability gives infinite susceptibility above it. This proves the equality of the two extrema. □

The analytic mechanism is DRT Lemma 3.1, reproduced here in integrated form to avoid differentiating infinite-volume limits. The missing inequalities are substantial. Neither edge-negative correlation nor ordinary negative association establishes (AO) or the uniform NC-budget. The fixed-point/tree and high-degree finite-graph results cited in §2 supply neither. To solve C0092 independently of boundary choice, one must also identify the intended infinite-volume state(s), not merely one torus limit family.

The alternative exact correction formula (4) offers another concrete target, (5), for controlling p-monotonicity. It does not by itself replace (AO). No step above treats any of these targets as already proved.

## 6. Numerical evidence

All numbers are finite-volume evidence. A finite torus has neither a literal susceptibility blow-up nor an infinite cluster. The code therefore compares several explicitly defined proxies; it does not estimate two infinite-volume thresholds independently.

### Model, observables and runs

The sampler is random-scan single-edge heat bath using (2), with q=0.25,0.5,0.75. One sweep makes |E| random edge choices. A uniform U<p opens the selected edge; U>=a closes it; in the remaining interval a BFS checks connectivity after removing that edge. This implements the exact conditional law. No q>=1 Chayes–Machta activation probability is used. Positive update probabilities give irreducibility and aperiodicity on each finite graph; conditional resampling preserves the FK law, proving the stated stationary distribution. This does not certify mixing in a finite run.

Exact enumeration stores integer histograms indexed by open-edge count and component count. Side-2 periodic tori retain both parallel nearest-neighbor bonds. Winding is detected with integer lift displacements in union-find; a nonzero displacement around an open cycle marks a wrapping component.

For N=L^d, the saved observables include
\[
\chi_L=N^{-1}\sum_C|C|^2,\quad
\chi_L^{\rm excl}=N^{-1}\left(\sum_C|C|^2-|C_{\max}|^2\right),\quad
\chi_L^{\rm nw}=N^{-1}\sum_{C\ {\rm nonwrapping}}|C|^2,
\]
the indicator of any wrapping, the largest-component fraction, edge density and component density. The latter two susceptibility expressions are modified observables, not the susceptibility in (1). Removing one largest component also removes that component below the transition, causing potentially substantial finite-size bias.

The main scan uses 2D sides 8,12,16 and 3D sides 4,6,8. Each parameter has two independent chains, one empty and one full initially: 400 burn-in sweeps, 1600 measurement sweeps, every fourth sweep retained. The original 2D grid used the self-dual value as a heuristic center; it is not invoked as a proved critical value for q<1. Lower-p points were added when some largest-cluster-deleted susceptibility peaks fell at a scan boundary. There are 294 parameter points and 235,200 retained main-scan samples after this extension. The 3D grid is .04,.06,...,.30; the combined 2D grid has maximum spacing .02.

### Checks and uncertainty

- Exact totals: 256 configurations on the 2D side-2 torus, 262,144 on the 2D side-3 torus, and 16,777,216 on the 3D side-2 torus. Every fixed-edge-count slice equals the corresponding binomial coefficient. At q=1, the partition functions equal one at three tested p-values.
- An independent Python DFS/lift implementation reproduces the entire side-2 2D histogram, including winding and cluster sums.
- Single-edge detailed balance is checked on every side-2 2D configuration, every edge, three q-values and three p-values. Maximum relative discrepancy is \(7.73\times10^{-16}\).
- Exact rational enumeration at nine triangle parameter pairs independently verifies (6)–(7).
- Heat-bath samples are compared to exact answers at both small torus geometries, three q-values, three p-values and six observables: 108 comparisons. The largest final discrepancy is 2.775 estimated standard errors. This is a diagnostic, not a theorem about mixing or a simultaneous confidence guarantee.

The initial validation of nonwrapping susceptibility at d=3,L=2,q=.25,p=.6 underestimated a rare-event contribution: the short chains scarcely saw the rare connected nonwrapping configurations. Its nominal discrepancy was 12.64 standard errors. That diagnostic is retained in data/initial_sampler_validation.csv. The targeted check was increased to one million measured sweeps per chain, sampled every tenth sweep. With the other validation runs, there are 268,000 retained validation samples. The discrepancy no longer persists; it illustrates why a small empirical standard error is not enough when an observable has rare large contributions.

Time-block standard errors use block lengths 20 and 40 retained observations, retaining the larger estimate. Split R-hat and initial-positive-pair autocorrelation ESS are also saved. For wrapping in the phase window \(0.1<\mathbb E[\mathrm{wrap}]<0.9\), the worst split R-hat is 1.0141, the smallest combined ESS is 534, and the largest empty/full mean difference is 2.76 estimated standard errors. These checks do not prove stationarity. Constant wrapping samples have nominal zero empirical error but do not certify probabilities zero or one.

Five hundred block-bootstrap replications quantify sampling variation in the finite-grid proxies. They omit mixing bias, grid discretization and finite-size bias. Full intervals and all 18 size/parameter combinations are in [data/NUMERICS.md](data/NUMERICS.md); raw and summarized data are retained.

### Comparison

For the largest simulated size in each dimension:

| d | q | L | wrapping probability = 1/2 | peak of chi excluding largest | peak of nonwrapping chi | full chi at wrapping midpoint |
|---|---|---|---|---|---|---|
| 2 | .25 | 16 | .3323 | .2133 | .2733 | 177.7 |
| 2 | .50 | 16 | .4008 | .3142 | .3742 | 148.7 |
| 2 | .75 | 16 | .4408 | .3641 | .4041 | 128.2 |
| 3 | .25 | 8 | .1143 | .0800 | .1000 | 172.7 |
| 3 | .50 | 8 | .1714 | .1600 | .1600 | 125.9 |
| 3 | .75 | 8 | .2156 | .2000 | .2200 | 103.3 |

The finite-size susceptibility proxies and wrapping midpoint differ visibly, especially in 2D. For example, at q=.25 the largest-cluster-deleted peak moves from p=.16 on side 8 to p=.2133 on side 16, while the wrapping midpoint stays near .33. For q=.50 in 3D, the deleted peak moves .14→.16 and the midpoint .1826→.1714 as side length goes 4→8. These are finite-size observations, not evidence of a proven infinite-volume gap. The nonwrapping susceptibility has yet another peak. The full susceptibility grows strongly with volume near the wrapping midpoint; it has no finite-p singularity on any of these graphs.

Choosing a 50% wrapping probability is an arbitrary finite-size convention. Its critical value need not be 50%, even when the infinite-volume threshold is known. No finite-size scaling fit, extrapolated critical value, or claimed equality is reported.

[The generated comparison plot](data/finite_size_comparison.svg) shows the deleted susceptibility curves and wrapping probabilities. It is generated from our own data; no paper figures or page images were retained.

### Reproduction and resources

[code/README.md](code/README.md) gives the exact commands and job formats. Code is in code/, data and seeds in data/, full source text in sources/. The original numerical scan, including all three enumerations, took 155.69 wall-clock seconds; the numerical child's maximum resident memory was 3,604,480 bytes according to macOS getrusage. Validation and the extended grid were run afterward. Final analysis peak RSS was 220,200,960 bytes (about 210 MiB), below 4 GB. All numerical jobs use one thread and inherit nice 10; BLAS thread counts are set to one for analysis.

No PDF, scan or paper page image was saved in this directory. PDFs were downloaded into RAM and piped to text conversion. No publication, commit or push was made.

## 7. What remains unresolved

No new fixed-q lattice sharpness result is proved. The comparison interval, exact tree calculation, and conditional reduction do not bridge the full \(0<q<1\) regime on \(\mathbb Z^d\). A volume-uniform replacement for the attractive covariance estimates and a justified infinite-volume family remain missing. Even proving ordinary negative association would not license the signed OSSS step disproved in (7). The finite-size calculations establish neither equality nor a gap between the infinite-volume thresholds.

Task: “Open problem C0092”, received 2026-11-13 at 09:30 +04 (launch record; seconds unavailable).
