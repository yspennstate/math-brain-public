PARTIAL

# G0015: critical continuous-type cascades and the CRT

The exact-size conjecture is not proved here, and no retrieved theorem has been checked to cover it under precisely the source's hypotheses. This report proves a restricted version for continuous kernels with a finite-mixture representation, identifies its scale constant, proves regeneration and moment estimates under a stronger minorisation assumption, and supplies exact conditioned simulations through 100,000 vertices. The distinction between exact-size conditioning and survival conditioning matters: recent general Polish-type results cover the latter, but do not directly provide the former.

## 1. Source, exact statements, and scope

The matching source is **Achyut Kumar and Abhinav Duddala**, *Two problems for threshold cascades of interacting diffusions on unimodular random trees: front propagation with a Bramson correction, and the continuous-type limit theory*, [arXiv:2608.21125v1](https://arxiv.org/abs/2608.21125v1), submitted 21 August 2026. “Dudeja” in the task does not match the author metadata. The requested source identifier `kumar_dudeja_threshold_cascades_2026` is retained as the task's identifier; it maps to this paper because the title content, conjecture number, programme number, section, and PDF page all match.

The full downloaded text is [sources/kumar_duddala_2608.21125v1.txt](sources/kumar_duddala_2608.21125v1.txt). The original downloaded TeX is also present. **The exact, unaltered source statements** of Theorem 5.1, Theorem 6.1, Conjecture 7.2 and Programme 7.3 are machine-extracted in [sources/exact_requested_statements.tex.txt](sources/exact_requested_statements.tex.txt). This preserves formulas and reference labels that PDF-to-text conversion can damage. Theorem 6.1 occupies PDF pp. 6–7; Conjecture 7.2 and Programme 7.3 are on PDF p. 8. The following is a mathematical restatement and audit, not an endorsement of all the source's claims.

Definition 4.1, PDF p. 5, defines

\[
 Kf(x)=\bar\nu\int p(y)f(y)\Gamma(x,dy),\qquad
 f\in L^2(\mathbb R,\varpi),\qquad
 \bar\nu=m_*=g''(1)/g'(1).
\]

Here \(\Gamma\) is a Gaussian-type strength-response kernel, \(\varpi\) is a Gaussian reference law, and criticality means \(\rho(K)=1\). There is a modeling inconsistency to retain explicitly: the paragraph preceding the definition describes transmission by \(p(x)\), whereas the displayed definition uses \(p(y)\). Those yield different kernels. All constructions below use the **displayed definition**, sampling a potential child's strength before accepting it with probability \(p(y)\).

Theorem 5.1 assumes a jointly smooth Gaussian-type density with sub-Gaussian tails, \(p(x)\in[p_{\min},1]\), and Wasserstein-2 Lipschitz dependence of \(\Gamma(x,\cdot)\) on \(x\). It asserts Hilbert–Schmidt compactness; positivity improvement and a simple positive Perron eigenfunction \(h\), with a strict spectral gap; and that

\[
 P(x,dy)=\frac{h(y)}{\rho(K)h(x)}K(x,dy)
\]

has a spectral gap, a unique stationary law \(\varpi_*\), and uniform ergodicity. The proof additionally mentions a bounded Lipschitz Gaussian mean and bounds on \(h\) on an unspecified effective support; these are not quantitative assumptions in its statement. **No separate Harris recurrence, small-set, drift, Doeblin, or bounded-density-ratio hypothesis is stated.** Positivity and uniform ergodicity are conclusions there, rather than separately verified assumptions.

Writing \(Z_k=\sum_{|v|=k}\delta_{A_v}\), Theorem 6.1 asserts:

1. \(W_k=\rho(K)^{-k}\langle h,Z_k\rangle\) is a nonnegative martingale.
2. If \(\rho(K)>1\) and \(\mathbb E[\langle h,Z_1\rangle\log_+\langle h,Z_1\rangle]<\infty\), it converges almost surely and in \(L^1\), with positive limit precisely on survival. The source claims the moment is automatic from uniform ellipticity and finite degree variance.
3. With its additional second-moment assumption it asserts \(L^2\) convergence and almost-sure weak convergence, on surviving realizations, of
   \(\langle h,Z_k\rangle^{-1}\sum_{|v|=k}h(A_v)\delta_{A_v}\) to \(\varpi_*\).

Conjecture 7.2 adds criticality and an exponential moment for the offspring count to those hypotheses. For \(S_n\) distributed as the critical cluster conditional on \(|S|=n\), it asserts

\[
 (S_n,\Sigma_c n^{-1/2}d_{\rm gr},\operatorname{unif}_{S_n})
 \ \Longrightarrow\ (\mathcal T_e,d_e,\mu_e)
\]

in GHP, with a positive explicit constant described through \(\sigma^2_{\rm off}\) and \(\varpi_*\). **The source does not give a formula for \(\Sigma_c\).** Its Corollary 6.2 defines \(\sigma^2_{\rm off}\) as the variance of the ordinary child count when the parent's strength is averaged under \(\varpi_*\).

Programme 7.3 offers two approaches: finite partitions of the strength space, with a GHP discretisation error and tightness uniform in the partition; or an infinite-type invariance principle, citing de Raphélis and successors. It describes the remaining task as a tightness/second-moment estimate. The literature and hypothesis audit below finds additional issues before that reduction can be accepted.

The standing assumptions, PDF p. 2, also matter. The source inherits a finite-graph-to-UGW limit, the companion SDE and transmission rules, and its conditional reduction assumptions. Its front-decoupling statement (R1) is restricted to the dissipative region \(\kappa<1\), with iterated graph-size and saturation limits. Its error bound contains \((1-\rho(M))^{-1}\), so it does not itself give a critical, exact-size-conditioned approximation. The continuous-type construction is (R2). The companion is [arXiv:2608.15987](https://arxiv.org/abs/2608.15987), despite the placeholder identifier in the source bibliography. Hypothesis 2.4 of the companion is a branching-reduction assumption, not a consequence of the displayed mean kernel alone. The proofs and simulations here concern the specified **branching genealogy**. Transferring them to finite-graph diffusion clusters requires that additional reduction, with errors controlled under conditioning.

All limits conditioned on size must run through admissible integers. An offspring exponential moment alone does not state aperiodicity. Also, finite variance of the original degree does not imply finite variance of its size-biased forward degree; the latter ordinarily uses a third degree moment. A common exponential degree moment resolves this distinction.

## 2. Literature first: results and their applicability

A detailed search record is in [data/LITERATURE_AUDIT.md](data/LITERATURE_AUDIT.md), with search phrases and retrieval hashes beside it. All paper versions below were read as plain text converted from PDFs in memory. Page numbers here refer to the specified version; journal page numbers are supplied when verified.

### 2.1 Miermont and de Raphélis

[Miermont (2008)](https://www.numdam.org/article/AIHPB_2008__44_6_1128_0.pdf), AIHP 44, 1128–1161, defines assumption (H) on printed p. 1130: finitely many types, criticality, irreducibility, nondegeneracy, and finite second moments. Normalize its left and right Perron vectors by \(a\cdot1=a\cdot b=1\). Its variance is

\[
 \sigma^2=\sum_{i,j,k}a_i b_jb_k Q^{(i)}_{jk},
 \qquad Q^{(i)}_{jk}=\mathbb E_i[N_j(N_k-\mathbf1_{j=k})].
\]

Theorem 2, printed pp. 1133–1134, adds small exponential offspring moments and conditions on **one specified type count**. Its height limit is \(2e/(\sigma\sqrt{a_j})\). This is not a Polish-type theorem, and the printed conditioning is not directly total vertex count. Proposition 2 on p. 1134 explicitly supplies the single-type case.

[De Raphélis (2017), arXiv:1405.3916v3](https://arxiv.org/abs/1405.3916v3), Theorem 2, PDF p. 8, works with a **countable** type set, introduced on p. 6. The relevant assumptions, pp. 7–8, are:

- (HM): irreducible mean matrix with finite iterate entries; positive left and right eigenvectors, with \(\sum_xa_x=\sum_xa_xb_x=1\).
- (HQ): finite factorial second moments and finite \(\eta^2=\sum_{x,y,z}a_xb_yQ^x_{yz}b_z\).
- (HR\(_{x_0}\)): multiplying by \(t^2\), both the probability of an excursion of height greater than \(t\) avoiding the root type, and the expected number of first returns beyond height \(t\), tend to zero.

Its conclusion is convergence of the **unconditioned forest** height function to \(2|B|/\eta\), together with a tree-index limit and a height-tail asymptotic. It is not an exact-total-size-conditioned GHP theorem.

The source-to-theorem checks are therefore:

| Required input | Source model check |
|---|---|
| Countable type set | Fails for a non-atomic Gaussian kernel on \(\mathbb R\). |
| Singleton root-type return construction | A continuous density gives zero probability of an exact return to a prescribed singleton. |
| Positive normalized left/right Perron data | Claimed in part, but the left measure and its normalization need identification; an \(L^2\) spectral assertion alone does not supply all the required summability statements. |
| Weighted factorial variance (HQ) | Ordinary offspring-count moments suffice if \(h\) is uniformly bounded; source does not establish the needed global bound. |
| Return-height tail (HR) | Not stated or verified. A quantitative minorisation can replace this step in a new argument, but is not a direct application of the printed theorem. |
| Exact total-size conditioning | Not the conclusion of Theorem 2. |

Thus de Raphélis does not resolve Conjecture 7.2 as stated.

### 2.2 General Polish-type results found in the extended search

[Foutel-Rodier, arXiv:2412.16035](https://arxiv.org/abs/2412.16035), gives a genuinely relevant discrete-time Polish-type theory. Assumption 1, PDF pp. 3–4, requires a positive continuous **bounded** harmonic function \(h\), a left probability eigenmeasure \(\pi\) with \(\pi(h)=1\), uniform convergence of mean type measures against bounded continuous tests, uniform offspring moments of every order, and continuity of the offspring second moment. Its variance on p. 4 is

\[
 \Sigma^2=\int\pi(dx)\,\mathbb E_x\sum_{i\ne j}h(Y_i)h(Y_j).
\]

Theorem 1.1, p. 6, is an excursion-measure convergence theorem in marked Gromov-vague topology. Assumption 2, p. 7, asks for the uniform Kolmogorov estimate

\[
 \sup_x\left|n\mathbb P_x(Z_n>0)-2h(x)/\Sigma^2\right|\longrightarrow0.
\]

Theorem 1.2, p. 7, upgrades the excursion convergence to marked GHP. Corollary 1.3, p. 8, gives **survival-conditioned** and forest limits. It does not state conditioning on a single exact total mass. Uniform mean convergence and the uniform survival estimate are not verified by the source's \(L^2\) spectral argument. A type-uniform exponential moment would imply its all-order moments; a merely pointwise exponential moment would not.

[Horton–Powell, arXiv:2601.05906v2](https://arxiv.org/abs/2601.05906v2), Theorem 2, PDF p. 5, concerns **continuous-time** branching Markov processes conditioned to survive until time \(n\). The conclusion is Gromov–Hausdorff–weak convergence to a CRT conditioned to reach height one, using lifetime occupation mass. Assumption 1, pp. 2–4, includes bounded second moments (VAR), càdlàg motion (CAD), uniform exponential Perron convergence (PF), almost-sure extinction (EXT), a truncated pair-offspring lower bound (ERG), and a generator-domain condition (CC). The paragraph after Theorem 2 explicitly discusses the discrete-time extension as expected, rather than proved there. This does not apply directly to exact vertex-count conditioning.

[Powell (2019), arXiv:1512.00031](https://arxiv.org/abs/1512.00031), Theorem 1.1, PDF p. 2, treats killed branching diffusions on bounded domains, again with survival conditioning; it does not supply the requested exact-size theorem for the strength kernel on \(\mathbb R\).

These works show that Polish types alone are no longer the obstacle suggested by Programme 7.3. They do **not** eliminate the exact-size conditioning problem. Even excursion convergence with a total-mass density does not by itself give a local limit for a single lattice mass: conditioning on a shrinking event needs additional local control.

### 2.3 The finite-type theorem used below

[Addario-Berry, Beltran, Stufler and Thévenin, arXiv:2507.23241v2](https://arxiv.org/abs/2507.23241v2), revised 12 June 2026, Theorem 1.3, PDF pp. 5–6, gives rooted GHP convergence for critical irreducible **finite-type** trees with exponential offspring moments, conditioned on a nonnegative integer linear combination of type populations. The surrounding hypotheses include extinction possibility and nondegeneracy. For total size, choose \(\lambda=(1,\ldots,1)\); equation (1.3), p. 6, gives the variance above, and the scale is \(\sigma/2\). Theorem 1.4, p. 6, provides sub-Gaussian height tails. Every hypothesis is verified for the restricted theorem in Section 4.

### 2.4 Other requested directions

- Haas–Miermont, [arXiv:1003.3632](https://arxiv.org/abs/1003.3632), Theorems 5–6, published-version PDF p. 13, require size-only Markov branching and convergence of splitting measures. Hidden inherited types do not automatically give size-only Markov branching. Theorem 8, p. 15, does give the single-type finite-variance conditioned GW GHP limit.
- Stephenson, [arXiv:1412.6911](https://arxiv.org/abs/1412.6911), Theorem 3.1, PDF pp. 12–13, is a finite-type **local** limit towards a Kesten tree under population conditioning, rather than a compact-tree CRT limit.
- Abraham–Delmas–Hoscheit, [arXiv:1202.5464](https://arxiv.org/abs/1202.5464), Theorems 2.3, 2.7 and 2.9, PDF pp. 4–5, establish GHP metric-space and compactness foundations. A Polish space of measured trees is different from an invariance principle for branching with Polish marks.
- Janson, [arXiv:1112.0510](https://arxiv.org/abs/1112.0510), Theorem 7.1, PDF pp. 20–21, and Theorem 7.11, p. 22, concern simply generated trees and degree frequencies. The single-type allocation representation helps simulate the examples below; integrating out inherited marks does not automatically make a model simply generated.
- Biggins–Kyprianou (2004), [*Measure change in multitype branching*](https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/kyprianou/BK2004.pdf), Theorem 2.1, printed p. 548 / PDF p. 5, treats general-type martingale mean convergence through spine-series conditions. It does not state a critical, size-conditioned CRT theorem.
- Athreya–Ney, *Branching Processes*: the publisher/catalog contents place multitype theory in Chapter V, pp. 181–228, critical limits at p. 189 and supercritical limits at p. 192. Full theorem text was not obtained; no exact theorem application from this book is claimed. Accessible general-type martingale statements were checked in Biggins–Kyprianou instead.
- Berzunza, [arXiv:1605.04810v2](https://arxiv.org/abs/1605.04810v2), explicitly restricts its stable height limits to finitely many types. This does not address the continuous-type gap.
- Marzouk, [arXiv:1903.06138](https://arxiv.org/abs/1903.06138), Theorem 4, PDF p. 5, gives convergence of finite sampled reduced trees with prescribed degrees. The following paragraph explicitly distinguishes the remaining height-tightness issue. It does not identify the conditional degree-sequence law of the cascade.
- Angtuncio Hernández–Clancy, [arXiv:2502.04238](https://arxiv.org/abs/2502.04238), builds multitype Lévy limits retaining finitely many types, with a different conditioning involving the root monochromatic component; see the introduction, PDF pp. 3–4, and Section 6. It is not the requested theorem.

This is a documented search, not a proof of the absence of other literature. No `RESOLVED_IN_LITERATURE` verdict is justified.

## 3. What the reduction actually needs

### 3.1 Spectral and variance checks

Suppose at criticality that a left eigenmeasure \(\ell\) and right eigenfunction \(h\) satisfy

\[
 \ell K=\ell,\quad Kh=h,\quad\ell(1)=\ell(h)=1.
\]

Then the invariant probability measure of the spine is

\[
 \varpi_*(dx)=h(x)\ell(dx).
\]

Indeed, integrating \(P f=h^{-1}K(hf)\) against this measure gives \(\ell K(hf)=\ell(hf)\). For a non-self-adjoint kernel it is not generally \(h^2\varpi\). Even if \(\Gamma\) is reversible, multiplying on the right by nonconstant \(p\) need not leave \(K\) self-adjoint.

Define

\[
 V_h(x)=\operatorname{Var}_x\!\left(\sum_i h(Y_i)\right),\qquad
 \sigma^2=\int\ell(dx)\,\mathbb E_x\sum_{i\ne j}h(Y_i)h(Y_j).
\]

Whenever the displayed moments are integrable,

\[
 \sigma^2=\ell(V_h)
 =\int\frac{\varpi_*(dx)}{h(x)}V_h(x).                 \tag{1}
\]

**Proof.** Expand the variance as \(Kh^2(x)+\mathbb E_x\sum_{i\ne j}h(Y_i)h(Y_j)-h(x)^2\). The first and last terms cancel after integration because \(\ell K=\ell\). The change of measure gives the second equality. This is also exactly the variance appearing in Foutel-Rodier's general-state theorem and in the finite-type theorems. In the excursion normalization used here, the CRT scale is \(\sigma/2\). ∎

Ordinary offspring counts averaged under \(\varpi_*\) need not have mean one. For a simple exact algebraic check, take independent Poisson offspring vectors with mean matrix

\[
 M=\begin{pmatrix}1/2&1\\1/4&1/2\end{pmatrix},\quad
 a=(1/3,2/3),\quad b=(3/2,3/4).
\]

Here \(\rho(M)=1\), \(aM=a\), \(Mb=b\), and the spine law is \((1/2,1/2)\). Its ordinary count mean is \(9/8\), its mixed count variance is \(81/64\), whereas the correct factorial Perron variance is \(a\cdot b^2=9/8\). This refutes the **general algebraic inference** from spectral criticality to critical spine-averaged ordinary counts. It is not presented as a counterexample to the Gaussian-kernel conjecture. A smooth continuous example with independently checked constants appears in Section 4.4.

Nor does a spectral gap imply uniform ergodicity. For the stationary OU transition

\[
 P(x,\cdot)=N(rx,1-r^2),\qquad0<r<1,
\]

Hermite polynomials give eigenvalues \(1,r,r^2,\ldots\); the operator is Hilbert–Schmidt and has an \(L^2\) gap. Yet for every finite \(k\),

\[
 \sup_x\|N(r^kx,1-r^{2k})-N(0,1)\|_{\rm TV}=1.
\]

**Proof.** For \(x>0\), test the half-line above \(r^kx/2\), then let \(x\to\infty\). Its probability tends to one for the shifted normal and zero for the stationary normal. ∎

This disproves the abstract implication used in Theorem 5.1(3). If a separate bounded-mean Gaussian forcing hypothesis is imposed, a Doeblin bound may instead be proved directly; the OU calculation does not refute that stronger statement. Also, a Hilbert–Schmidt norm on \(L^2(\varpi)\) must use the density relative to \(\varpi\), not a Lebesgue density without conversion.

Finally, Theorem 6.1(3) must be read with care at criticality. If it is intended to assert critical \(L^2\) convergence under only the stated second moment, it already fails for ordinary critical GW: with \(h=1\), \(\mathbb E Z_k^2=1+k\operatorname{Var}(N)\). If (3) is intended to inherit supercriticality from (2), it is not a critical input for Conjecture 7.2. The many-to-one identity by itself also does not establish almost-sure empirical convergence.

### 3.2 A precise regeneration lemma

The following estimates isolate what a useful small-set reduction can supply. They are proved here, rather than inferred from a spectral gap.

**Lemma.** Suppose the critical branching model is generated from an independent common potential-child count \(D\), with \(\nu=\mathbb ED\in(0,\infty)\), and independent slots \(\Gamma(x,dy)\) accepted with probability \(p(y)\). Assume

\[
 0<h_-\le h(x)\le h_+<\infty,\qquad Kh=h,
 \qquad P(x,dy)\ge\varepsilon\zeta(dy),\quad0<\varepsilon<1.       \tag{2}
\]

Mark an accepted child of type \(y\) as a regeneration with probability
\(\varepsilon\,d\zeta/dP(x,\cdot)(y)\), using independent auxiliary uniforms. Stop a block at all its first regeneration descendants, excluding those descendants from the interior of the block. Then:

(a) The expected number of interior vertices at depth \(k\) is at most \((h_+/h_-)(1-\varepsilon)^k\). Consequently the block-height tail is bounded by this expression.

(b) If \(\mathbb Ee^{t_0D}<\infty\) for some \(t_0>0\), the block interior size \(C\) and its number of regeneration descendants \(B\) have a common type-uniform exponential moment.

(c) Regeneration types have law

\[
 \eta(dy)=\frac{\zeta(dy)/h(y)}{\zeta(1/h)},                  \tag{3}
\]

not generally \(\zeta\). They are independent of the block information revealed before their strengths are exposed, and independent across terminals. Starting the root with law \(\eta\), the tree of successive regeneration vertices is an ordinary GW tree with iid block decorations and \(\mathbb E_\eta B=1\).

**Proof.** Put \(P_0=P-\varepsilon\zeta\), and
\(K_0f=hP_0(f/h)\). The interior expected generation measure is \(K_0^k\), and

\[
 K_0^k1(x)=h(x)P_0^k(1/h)(x)
 \le(h_+/h_-)(1-\varepsilon)^k.
\]

This proves (a), by Markov's inequality for existence of a vertex at depth \(k\).

For (b), the active children have expected total \(h\)-weight \((1-\varepsilon)h(x)\), and the terminal count is bounded by \(D\). Test the recursion for the joint exponential moment against \(U(x)=e^{th(x)}\). With \(A\) denoting active children and \(J\) the terminal count, its one-step expression is

\[
 e^\theta\mathbb E_x\exp\{t\sum_{i\in A}h(Y_i)+\theta J\}.
\]

Since the exponent is at most \((th_++\theta)D\), the exponential moment of \(D\) gives a uniform Taylor bound, for sufficiently small \(t,\theta\), of

\[
 1+t(1-\varepsilon)h(x)+\theta(1+\nu)+C_0(t+\theta)^2.
\]

Choose \(\theta=t\varepsilon h_-/[4(1+\nu)]\), and then choose \(t>0\) sufficiently small that the quadratic remainder is at most \(t\varepsilon h_-/4\). The expression is at most \(1+th(x)\le U(x)\). Induction over a depth-truncated block, followed by monotone convergence, proves
\(\sup_x\mathbb E_xe^{\theta(C+B)}\le e^{th_+}\).

For (c), the probability measure of a terminal success in one potential-child slot is

\[
 \Gamma(x,dy)p(y)\,
 \varepsilon\frac{d\zeta}{dP(x,\cdot)}(y)
 =\frac{\varepsilon h(x)}{\nu}\frac{\zeta(dy)}{h(y)}.
\]

Its normalized type law is (3), independent of \(x\). Independence of potential-child slots implies the required factorization even after conditioning on the number and locations of terminal successes. Terminal strengths can therefore be withheld until their blocks start. The branching property then makes the successive block decorations iid for root law \(\eta\).

Write \(a_0=\eta(h)=1/\zeta(1/h)\). The expected terminal count \(F(x)\) satisfies
\(F=K_0F+K_{\rm reg}1\), where \(K_{\rm reg}=K-K_0\). More explicitly, \(K_{\rm reg}1=\varepsilon h/a_0\), so summing the resolvent gives
\[
 F=\sum_{k\ge0}K_0^k(\varepsilon h/a_0)=h/a_0.
\]
Thus \(\eta(F)=1\). All sums converge by (a). ∎

The uniform exponential block moments are exactly where an exponential offspring moment is useful: they control the entire excursion block, including the number of side branches, rather than just one spine trajectory. Positivity or Harris recurrence without quantitative return tails would not give this estimate.

There is also a normalization check. Suppose \(\ell\) is normalized as above and \(\varpi_*=h\ell\). Stationarity of the split spine gives
\(\varpi_*=\varepsilon\zeta\sum_{k\ge0}P_0^k\), hence

\[
 \eta\sum_{k\ge0}K_0^k=(a_0/\varepsilon)\ell,
 \qquad \mathbb E_\eta C=a_0/\varepsilon.                    \tag{4}
\]

If \(\beta=\mathbb E D(D-1)\), slot independence and \(Kh=h\) give
\(\sigma^2=(\beta/\nu^2)\ell(h^2)\). A factorial-moment recursion for terminal descendants gives

\[
 \operatorname{Var}_\eta B=\sigma^2/(\varepsilon a_0).       \tag{5}
\]

To check (5) directly, descendants contributed by different slots have conditional mean \(F(x)/\nu=h(x)/(\nu a_0)\). The within-slot factorial contribution is \(K_0Q\). Therefore
\(Q=K_0Q+\beta h^2/(\nu^2a_0^2)\). Integrating the resolvent using (4) gives (5), since \(\mathbb E_\eta B=1\).

These facts alone do **not** finish a size-conditioned CRT proof. Conditioning the original tree on \(\sum C=n\) does not condition its regeneration skeleton on a fixed number of vertices: \(B,C\), and edge lengths within a block are correlated. One still needs a joint local limit under this additive conditioning, a conditioned comparison of path lengths, and convergence of the vertex mass measure. A geometric regeneration time along the spine has mean \(1/\varepsilon\); the identities (4)–(5) make the candidate scale \(\varepsilon\sqrt{\operatorname{Var}(B)\mathbb EC}/2=\sigma/2\). This is a normalization identity, not an assertion that the missing conditioned invariance principle has been proved.

For an ordinary small set rather than a global bound (2), returns to the set must also have sufficiently strong uniform tails. A singleton return is unavailable in a non-atomic space; Nummelin's auxiliary mark, and a lift of that mark to the full offspring construction, are necessary. Minorisation of a mean kernel alone does not guarantee independence of blocks for an arbitrary correlated offspring point process. The independent-slot assumption in the lemma is substantive.

## 4. A proved continuous-type subclass

### 4.1 Statement

**Theorem A (finite-mixture reduction).** Let the type space be a Polish space \(E\). Independently at every vertex, draw a common potential-child count \(D\), with mean \(\nu>0\), finite exponential moment, and \(\mathbb P(D\ge2)>0\). Given the parent's type \(x\), potential children are independent; each has type law

\[
 \Gamma(x,dy)=\sum_{j=1}^q w_j(x)q_j(dy),
 \quad \sum_jw_j(x)=1,
 \quad w_j(x)\ge\epsilon_0>0,                              \tag{6}
\]

for a fixed finite \(q\). Accept a child of type \(y\) independently with probability \(p(y)\), where
\(0<p_-\le p(y)\le p_+<1\). Define

\[
 c_j=q_j(p),\quad \mu_j(dy)=p(y)q_j(dy)/c_j,
 \quad r_j(x)=c_jw_j(x),
 \quad M_{ij}=\nu\int\mu_i(dx)r_j(x).                     \tag{7}
\]

Assume \(\rho(M)=1\). Take the initial type with law \(\mu_i\) for any fixed \(i\), or a fixed mixture of these laws. If desired to regard \(K\) on \(L^2(\varpi)\), additionally assume \(dq_j/d\varpi\in L^2(\varpi)\).

Let \(aM=a\), \(Mb=b\), normalized by \(a\cdot1=a\cdot b=1\), and put

\[
 \ell=\sum_i a_i\mu_i,
 \qquad h(x)=\nu\sum_jr_j(x)b_j,
 \qquad \beta=\mathbb E[D(D-1)].
\]

Then the original tree, with continuous strengths forgotten, conditioned on total size \(n\), converges in rooted GHP to the standard excursion-coded CRT after distance multiplication by \(\Sigma_c/\sqrt n\), where

\[
 \boxed{\quad
 \Sigma_c=\frac12\sqrt{\frac{\beta}{\nu^2}\int h(x)^2\ell(dx)}
 =\frac12\sqrt{\int\ell(dx)\mathbb E_x\sum_{u\ne v}h(Y_u)h(Y_v)}.
 \quad}                                                   \tag{8}
\]

The type spine has invariant law \(\varpi_*=h\ell\) and satisfies a global Doeblin bound. In particular, this is a subclass with quantitative regeneration. There are constants \(C,c>0\) such that its size-conditioned maximum height satisfies
\(\mathbb P(H_n>x)\le C\exp(-cx^2/n)\).

The finite-mixture condition is a real restriction. A nonzero-correlation Gaussian OU transition on the whole line is generally not a finite mixture of fixed component laws. The theorem does not assert otherwise. Its allowed root laws are explicit; a fixed arbitrary initial strength is not silently included.

### 4.2 Complete reduction proof

Augment the sampling of each potential child by a latent class \(j\), chosen with probabilities \(w_j(x)\), before sampling its type from \(q_j\). Conditional on acceptance and class \(j\), the child's type has law \(\mu_j\), independent of its parent and of other children. The probability of this class and acceptance is \(r_j(x)\).

Consider a vertex whose latent class is \(i\). Its strength is a fresh sample from \(\mu_i\). Given this strength and \(D\), the accepted latent-class counts have a multinomial law with probabilities \((r_1(x),\ldots,r_q(x),1-\sum_jr_j(x))\). Integrating over \(\mu_i\) gives a fixed offspring-word law for class \(i\). The fresh strengths and the per-vertex random variables are independent across vertices. Equivalently, their joint density factorizes vertex by vertex as \(\mu_i(dx)\) times the parent's offspring mechanism. The latent-class genealogy is therefore **exactly** a finite-type GW tree, not a discretisation or an approximation.

Its mean is (7). Every matrix entry is positive because \(c_j\ge p_-\) and \(w_j\ge\epsilon_0\); hence it is irreducible and aperiodic. It is critical by assumption. Accepted child count is at most \(D\), so the finite family of offspring laws has a common exponential moment. A leaf has positive probability, since \(p_+<1\) and \(\mathbb E(1-p_+)^D>0\). At least two accepted children have positive probability, since \(p_->0\) and \(\mathbb P(D\ge2)>0\). Thus extinction possibility and nondegeneracy hold. These checks verify every hypothesis needed from Addario-Berry–Beltran–Stufler–Thévenin, Theorem 1.3. Conditional total size is the choice \(\lambda=(1,\ldots,1)\). All integers are in fact admissible: the offspring laws give positive probabilities of zero and one child, so chains of arbitrary finite length have positive probability.

For its factorial second moments, conditional on \(x\), distinct potential slots contribute independently. Thus

\[
 Q^{(i)}_{jk}=\beta\int\mu_i(dx)r_j(x)r_k(x).
\]

Consequently its finite-type variance is

\[
 \sum_{i,j,k}a_i b_jb_kQ^{(i)}_{jk}
 =\beta\int\ell(dx)\Big(\sum_jr_j(x)b_j\Big)^2
 =\frac\beta{\nu^2}\ell(h^2).
\]

Theorem 1.3 and equation (1.3) of that paper give exactly (8). Forgetting latent classes and strengths leaves the same vertex set, edges, graph distances and uniform measure. Conditioning on size also commutes with forgetting these labels. This transfers the GHP conclusion to the continuous-type tree without any metric error. Its Theorem 1.4, with all weights one and height at most \(n\), gives the stated height bound. ∎

### 4.3 Perron data, spine, and continuous-type variance

For completeness, these are also the Perron data of the continuous kernel. Let
\(Cf(x)=\nu\sum_jr_j(x)f_j\) for a finite vector \(f\), and \((Gg)_i=\mu_i(g)\). Then
\(K=CG\) and \(M=GC\). Their nonzero spectra coincide. The stated density condition makes these bounded maps on the specified \(L^2\) space, and \(K\) has finite rank. Directly,

\[
 Gh=GCb=Mb=b,\quad Kh=CMb=h,\quad
 \ell K=\ell,\quad\ell(h)=a\cdot b=1.
\]

The eigenfunction is bounded above and below:
\(\nu p_-\min b_j\le h(x)\le\nu p_+\max b_j\). In particular \(\varpi_*=h\ell\) is a probability law. For any fixed component \(j\),

\[
 P(x,dy)\ge\frac{\nu\epsilon_0c_jb_j}{h_+}\,
             \frac{h(y)\mu_j(dy)}{b_j}.
\]

The last factor is a probability measure, since \(\mu_j(h)=b_j\). This is an explicit Doeblin minorisation, proving uniform ergodicity without inferring it from an \(L^2\) gap. When the component densities are positive on \(\mathbb R\), it also supplies irreducibility and positive Harris recurrence.

In the original strength model, the expected accepted \(h\)-weight in one potential slot is \(h(x)/\nu\). Its distinct-child factorial moment is therefore \(\beta h(x)^2/\nu^2\). Integrating against \(\ell\) verifies the second expression in (8), independently of the finite-vector calculation. Identity (1) writes it through the stationary spine law and a weighted offspring variance. This identifies precisely how the tilted law enters; an ordinary spine-mixed child-count variance is insufficient in general.

### 4.4 A nonconstant smooth Gaussian-type example

Take \(q_1=N(-0.8,1)\), \(q_2=N(0.8,1)\),

\[
 w_1(x)=0.5+0.2\tanh x,\quad w_2=1-w_1,
 \qquad p(x)=0.55+0.15\tanh x.
\]

Let \(D\sim\operatorname{Poisson}(\nu)\), choosing \(\nu\) so that (7) is critical. This is an explicitly defined specialization of the **Gaussian-type strength-kernel framework**, not a claim that the paper supplies these parameter values or derives this mixture from its SDE. Its density is positive, smooth, Gaussian-tailed, and bounded between positive mixtures. The weight bounds are \(0.3\le w_j\le0.7\) and transmission bounds \(0.4<p<0.7\). The component density ratios relative to \(N(0,1)\) are square integrable.

It also has Wasserstein-2 Lipschitz dependence, as required by the source's analytic hypothesis. To see this, write \(f_s=s\phi_{-0.8}+(1-s)\phi_{0.8}\), \(s\in[0.3,0.7]\), and let \(F_s^{-1}\) be its quantile function. Differentiating the quantile identity gives

\[
 \int_0^1|\partial_sF_s^{-1}(u)|^2du
 =\int_{\mathbb R}\frac{(F_{-0.8}(y)-F_{0.8}(y))^2}{f_s(y)}dy.
\]

The right side is uniformly bounded in \(s\): on a compact interval this follows from a positive minimum density; in either tail, Gaussian tail bounds dominate the numerator squared by a constant times the slower component's squared tail, while the denominator is at least 0.3 times that component's density. The resulting Gaussian-density-over-a-quadratic tail is integrable. Integrating the quantile derivative proves \(W_2(q_s,q_t)\le C|s-t|\). Since \(w_1\) is Lipschitz, (6) is Wasserstein-2 Lipschitz in \(x\).

[code/finite_mixture_constants.py](code/finite_mixture_constants.py) evaluates the constants by both 160-point Gaussian quadrature and adaptive quadrature. The calculations are numerical checks of the explicit theorem, not proofs of rounded decimal equalities:

\[
 \nu\approx1.828705330954494,\qquad
 M\approx\begin{pmatrix}0.376269973760&0.647716179169\\
                         0.533160738610&0.446336039686\end{pmatrix},
\]

\[
 \sigma^2\approx1.000873065614738,\qquad
 \Sigma_c\approx0.500218218784247.
\]

The stationary-spine mean ordinary count is approximately \(1.001027942205\), and its mixed variance approximately \(1.002246313432\). Substituting that raw variance would instead give scale approximately \(0.500561263342\). The two independent integrations disagree by less than \(5\times10^{-16}\) in the recorded scalar values. This numerical agreement is an implementation check, not an error certificate for the quadrature. Exact finite-matrix and continuous factorial formulas are separately evaluated and agree. The explicit spine minorisation lower bound is about 0.2427. Full matrices, eigenvectors, normalizations and residuals are in [data/finite_mixture_constants.json](data/finite_mixture_constants.json).

## 5. Exact simulations: evidence only

The source does not supply a fully parameterized numerical strength kernel. We therefore choose a concrete member of its Gaussian OU family:

\[
 \Gamma(x,dy)=N(0.6x,0.64)(dy),\qquad p(y)=1/2,
 \qquad A_{\rm root}\sim N(0,1).                         \tag{9}
\]

This has a continuous inherited type, a Wasserstein contraction, a positive density and an \(L^2\) spectral gap. It is **not uniformly ergodic on all of \(\mathbb R\)**, as shown in Section 3.1. The single-type shape argument below needs none of that uniformity.

The primary simulation chooses \(g=\operatorname{Poisson}(2)\). The root degree and size-biased forward degree minus one both have law \(\operatorname{Poisson}(2)\). Thinning by one half gives a \(\operatorname{Poisson}(1)\) accepted child count at every vertex, independent of its strength. Thus

\[
 Kf(x)=\int f(y)\Gamma(x,dy),\quad h=1,\quad
 \ell=\varpi_*=N(0,1),\quad\sigma^2_{\rm off}=1,\quad\Sigma_c=1/2.
\]

The tree shape is exactly a critical single-type GW tree, even though its marks are correlated along edges. This proves the CRT statement for this chosen example by Miermont's single-type Proposition 2 / the classical finite-variance theorem. It does not test the difficult type-dependent reproduction case.

A secondary run uses \(D=2\) at every vertex, giving accepted count \(\operatorname{Bin}(2,1/2)\), \(\sigma^2=1/2\), and \(\Sigma_c=1/(2\sqrt2)\). This is a forward-tree experiment; the root of an unmodified 3-regular UGW cascade would have three potential children. The secondary run is not passed off as that modified-root cluster.

### 5.1 Sampling and independent checks

For Poisson reproduction, independent counts conditional on total \(n-1\) are multinomial: allocate \(n-1\) balls uniformly to \(n\) parents. For binomial reproduction, select a uniform \((n-1)\)-subset of \(2n\) Bernoulli slots and group them by parent. In both cases cyclically shift the degree sequence after its first global minimum. The cycle lemma produces the exact conditioned ordered GW tree. There is no rejection tolerance, MCMC mixing assumption, finite type partition, or rejection of large trees.

To verify the sampler rather than merely its output sizes, the code exhaustively enumerates all allocations at \(n\le5\). In the binomial model the number of allocations mapping to a plane tree with degrees \(d\) is \(n\prod_v\binom2{d_v}\); in the Poisson model it is \(n(n-1)!/\prod_v d_v!\). Those identities are checked for every enumerated tree. Partial sums, total degree, tree size, and consistency of generation sizes with parent offspring totals are checked in every simulation. Strengths are then generated recursively using (9), with a stationary Gaussian root; type means, second moments and edge products are recorded.

Writing \(H_n\) for height and \(W_n\) for maximum generation size, the independent CRT targets are

\[
 \frac{\sigma H_n}{2\sqrt n}\Rightarrow\max e,
 \qquad\frac{W_n}{\sigma\sqrt n}\Rightarrow\max e
 \quad\text{in marginal law}.
\]

The width statement and uniform integrability are checked against Addario-Berry–Devroye–Janson, [arXiv:1011.4121](https://arxiv.org/abs/1011.4121), equation (1.3), PDF p. 2, and Theorems 1.1–1.2, p. 3. The joint limits are not asserted equal. The target mean is \(\sqrt{\pi/2}=1.2533141373\); the target variance is \(\pi^2/6-\pi/2\). The code evaluates the excursion-maximum CDF through two equivalent theta-series and checks them against each other. KS distances are descriptive finite-sample discrepancies, not a proof or a rejection test for a finite-n CRT law.

### Poisson-degree example

| n | Replicates | Scaled height mean ± SE | Scaled width mean ± SE | Height KS | Width KS |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 400 | 1.1936 ± 0.0117 | 1.1269 ± 0.0125 | 0.1157 | 0.2174 |
| 3,000 | 400 | 1.2572 ± 0.0140 | 1.1431 ± 0.0118 | 0.0307 | 0.1749 |
| 10,000 | 300 | 1.2173 ± 0.0164 | 1.1790 ± 0.0143 | 0.1028 | 0.1271 |
| 30,000 | 200 | 1.2534 ± 0.0198 | 1.2054 ± 0.0175 | 0.0456 | 0.0940 |
| 100,000 | 300 | 1.2184 ± 0.0148 | 1.2301 ± 0.0147 | 0.0919 | 0.0573 |

Seed: 151520261114. One worker at nice 10; 33.14 seconds; peak RSS 138,510,336 bytes (132.1 MiB).

### Forward-binomial example

| n | Replicates | Scaled height mean ± SE | Scaled width mean ± SE | Height KS | Width KS |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 400 | 1.1745 ± 0.0124 | 1.1556 ± 0.0125 | 0.1103 | 0.1840 |
| 3,000 | 400 | 1.2060 ± 0.0128 | 1.1833 ± 0.0133 | 0.0841 | 0.1475 |
| 10,000 | 300 | 1.2204 ± 0.0152 | 1.2078 ± 0.0159 | 0.0896 | 0.1020 |
| 30,000 | 200 | 1.2102 ± 0.0185 | 1.2555 ± 0.0178 | 0.0791 | 0.0574 |
| 100,000 | 150 | 1.2221 ± 0.0187 | 1.2185 ± 0.0204 | 0.0934 | 0.0831 |

Seed: 151520261113. One worker at nice 10; 24.04 seconds; peak RSS 121,733,120 bytes (116.1 MiB).

Both limiting means are 1.2533141373. The finite samples have visible bias and Monte Carlo variation: in the primary Poisson run at n=100,000 the scaled height mean is about 2.35 Monte Carlo standard errors below the limiting mean and the width mean about 1.58 below it. These observations neither prove convergence nor refute it; they are not treated as an exact finite-n fit. No samples or seeds were discarded. The secondary run was retained in full. The choice of the Poisson run was made to match the root and forward degree laws, not to improve the numerical agreement.

Across the two runs there are 3,050 trees and 450 at n=100,000. Both runs stay far below 4 GB, use one numerical thread, and inherit nice 10. They simulate genealogical branching models, not diffusion paths on finite graphs.

The empirical CDFs at the largest size are plotted in [data/crt_comparison.svg](data/crt_comparison.svg).

The executable code is [code/simulate_ou_conditioned.py](code/simulate_ou_conditioned.py); all raw samples and a complete 100,000-vertex example for each model are in `data/`.

### 5.2 Final verification and reproduction

Run `python3 code/simulate_ou_conditioned.py --model poisson` for the primary experiment and omit `--model poisson` for the secondary experiment. These commands overwrite their corresponding data files; recorded seeds make the draws reproducible. The simulation enforces nice at least 10 and sets numerical-library thread counts to one. Run `python3 code/finite_mixture_constants.py` to reproduce the constant audit, and `python3 code/verify_artifacts.py` for the independent final checks. The recorded verification checks exact rational Perron arithmetic, recomputes both 100,000-vertex example geometries by breadth-first traversal, verifies every source-text hash, and checks the no-PDF/plain-source requirements. Summary means and standard errors were independently recalculated from CSV using scalar compensated sums.

## 6. What remains open here

For the full source conjecture, the unresolved points are a precise offspring law consistent with its displayed kernel, quantitative global control of its Perron function and spine, an exact-size local limit under regeneration or discretisation, and conditioned height/mass-measure comparison. The source's unconditional cascade-to-branching approximation must also be made valid at criticality and after rare-event conditioning if the target is the diffusion cluster itself.

The finite-mixture theorem proves a meaningful continuous-type subclass, including a nonconstant smooth positive example with a Doeblin bound and an explicit variance. The regeneration lemma proves the required uniform excursion and block-moment estimates under stronger assumptions, while leaving the additive-conditioning step visible. The computations check normalization in two exact single-type shape specializations. None of these is a proof or counterexample for Conjecture 7.2 under its original wording.

Task: “Open problem G0015” — received 2026-11-13, 10:27 +04 (Asia/Tbilisi).
