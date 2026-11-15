PARTIAL

E0098: the minimum absolute coordinate of a real Wigner eigenvector.

The exponential limit is proved below for GOE, together with its Poisson process version. I did not find a printed theorem establishing this law for general fixed subgaussian Wigner atoms in the literature searched through 13 November 2026. I also did not prove it or find a Wigner counterexample. The missing input is a relative small-ball estimate at the coordinate scale n^{-3/2}. Ordinary Gaussian convergence, even for every sublinear collection of coordinates in total variation, does not imply the answer. A complete construction demonstrating that obstruction is given below. Numerical results are evidence only.

Statement and source.

The source is Sean O’Rourke, Van Vu, and Ke Wang, “Eigenvectors of random matrices: A survey,” Journal of Combinatorial Theory, Series A 144 (2016), 361–442, [arXiv:1601.03678v3](https://arxiv.org/abs/1601.03678v3). The question is on PDF p. 13 of that version, following Corollary 4.8; the journal location is p. 377. The complete extracted text is [sources/eigenvectors_survey_2016.txt](sources/eigenvectors_survey_2016.txt).

The exact question, with mathematical typesetting restored, is:

> Is the limiting distribution of \(\|v_j(W)\|_{\min}\) universal, or does it depend on the atom variables \(\xi\) and \(\zeta\)?

Here W is real symmetric. Its upper-triangular entries are independent, the off-diagonal entries are iid copies of centered ξ with variance one, and its diagonal entries are iid copies of centered ζ. Corollary 4.8 assumes both atoms are subgaussian, with constants depending on their laws. The natural interpretation here keeps those laws fixed as n grows. The eigenvectors have Euclidean norm one, and the eigenvalues are in increasing order. The statistic is min_{1≤k≤n}|v_j(k)|. A sign convention has no effect on it. Scaling W by n^{-1/2} also has no effect on it.

The question itself does not specify an index regime or write a rescaling. Its context is a given eigenvector, with no bulk restriction. A precise candidate statement is: for each deterministic sequence j_n∈{1,…,n},

\[
 n^{3/2}\min_k|v_{j_n}(k)|\ \Rightarrow\ \operatorname{Exp}(c),
 \qquad c=\sqrt{2/\pi}.
 \tag{1}
\]

This includes fixed edge ranks and bulk ranks, such as j_n=⌊n/2⌋. Uniformity over the choice of deterministic j_n would be stronger than a bulk-only result. It still would not give the distribution of min_{j,k}|v_j(k)|. Without rescaling, every unit vector has minimum absolute coordinate at most n^{-1/2}, so the distribution tends trivially to a point mass at zero.

The printed Corollary 4.8 says that there are C,c_*,c_0,c_1>0 such that, for n^{-c_0}<α<c_0 and δ≥n^{-c_0/α},

\[
 \sup_{1\le i\le n}\mathbb P\!\left(
  \|v_i(W)\|_{\min}\le {\delta\over n^{3/2}(\log n)^{c_1}}
 \right)
 \le {C\delta\over\sqrt\alpha}+C\exp(-c_*\log^2 n).
 \tag{2}
\]

This is a lower-tail bound uniform in a single chosen index, rather than a simultaneous event for all i or a two-sided asymptotic. For example, taking α fixed and δ=1/log n gives a rigorous high-probability lower bound with an extra logarithm. No limiting law follows from (2).

Literature checked first.

All page numbers in the following table refer to PDF pages in the specific saved arXiv version, including its title page. Text files preserve those boundaries as form-feed characters. A file’s first line records the retrieval URL, date, number of pages, and SHA-256 of the PDF that was converted in memory. No PDF was saved. The search terms and citation-chain checks are recorded in [sources/SEARCH_LOG.txt](sources/SEARCH_LOG.txt). Failure to locate a theorem is a bounded search result, not proof that no such theorem exists.

| Primary source and saved version | Exact result and PDF pages | What it provides, and the gap for (1) |
|---|---|---|
| [Bourgade–Yau, 1312.1301v6](https://arxiv.org/abs/1312.1301v6), CMP 2017 | Theorem 1.2 and Corollary 1.3, pp. 5–6; Corollary 1.4, p. 6 | Generalized Wigner matrices with uniformly bounded normalized moments of every order. Fixed-dimensional Gaussian moments for entries/projections; QUE for growing sets. The printed eigenvector index set includes the bulk and ranks within n^{1/4} of either edge, with intervening regimes omitted. The number of entries in the Gaussian marginal is fixed. |
| [Benigni, 1711.07103v3](https://arxiv.org/abs/1711.07103v3), AIHP 2020 | Theorem 1.3 and Corollary 1.4, p. 5; Theorem 1.7, p. 6 | Bulk Gaussian projections/finite-coordinate marginals for mesoscopic deformations of diagonal matrices, with a nonconstant variance profile; strong QUE under smoothness. A different model and no lower-extreme law. |
| [Benigni, 1908.10855v2](https://arxiv.org/abs/1908.10855v2), PTRF 2021 | Theorem 1.2, p. 4; Theorem 1.5, p. 6 | Fermionic flow and decorrelation of partial masses/overlaps on n^ϑ≤|I|≤n^{1−ϑ}. These are averaged polynomial observables. |
| [Benigni–Lopatto, 2007.09585v2](https://arxiv.org/abs/2007.09585v2), Advances in Mathematics 2022 | Theorems 1.2 and 1.3, p. 3; Theorem 1.4, p. 4 | Optimal upper delocalization for generalized Wigner matrices throughout the spectrum, under uniform subexponential tails; sharp leading upper constants, with additional smoothness in Theorem 1.4. Bounds the largest coordinate. |
| [Benigni–Lopatto, 2103.12013v3](https://arxiv.org/abs/2103.12013v3), CMP 2022 | Theorem 1.2, p. 2; Theorem 1.4, p. 3 | Generalized Wigner, all indices, uniformly bounded moments of every order. Gaussian fluctuations of a sum of squared orthogonal projections on n^ε≤|I|≤n^{1−ε}, and high-probability QUE/QWM. This is not joint entrywise normality of n^{1−ε} entries. |
| [Marcinek–Yau, 2005.08425v1](https://arxiv.org/abs/2005.08425v1), CMP 2022 | Theorem 2.5, p. 14; Theorem 2.8, p. 14 | Gaussian-divisible regular bulk models, then generalized Wigner bulk eigenvectors. Every fixed polynomial in a fixed number of projections has Gaussian asymptotics, with an error exponent depending on the polynomial. “High dimensional” does not mean an order-n coordinate marginal with microscopic relative errors. |
| [Cipolloni–Erdős–Schröder, 2012.13215v4](https://arxiv.org/abs/2012.13215v4), CMP 2021 | Theorem 2.2, p. 5 | ETH: bounded deterministic observables are approximately scalar in the Wigner eigenbasis, with error n^{-1/2+ε}, simultaneously in eigenvector indices, under bounded normalized moments. It does not count coordinates in a shrinking window at zero. |
| [Cipolloni–Erdős–Schröder, 2103.06730v3](https://arxiv.org/abs/2103.06730v3), Annals of Probability 2022 | Theorem 2.2, p. 6 | Bulk Gaussian fluctuations of quadratic forms with nonvanishing normalized traceless variance. No coordinate minimum. |
| [Knowles–Yin, 1102.0057v4](https://arxiv.org/abs/1102.0057v4), PTRF 2013 | Theorem 1.6, pp. 4–5; Theorem 1.10, pp. 5–6 | Fixed collections of edge eigenvector observables under two-moment comparison and level repulsion; bulk comparison with four matching moments, under the paper’s subexponential-tail assumptions. No relative small-ball asymptotics at width 1/n in rescaled coordinates. |
| [Tao–Vu, 1103.2801v2](https://arxiv.org/abs/1103.2801v2), RMTA 2012 | Theorem 7, p. 6; Theorem 8, p. 7 | Polynomially growing collections for smooth observables, with four off-diagonal/two diagonal matching moments and sufficiently many finite moments. Derivative restrictions and additive error prevent substituting the microscopic minimum event. Rademacher atoms do not satisfy the four-moment Gaussian match. |
| [Tao–Vu, 1412.1438v1](https://arxiv.org/abs/1412.1438v1) | Theorem 1.3, p. 2; Proposition 2.2, p. 3 | Superpolynomial simplicity and a bound on a deleted row being orthogonal to any eigenvector of its independent minor, under a fixed nontrivial off-diagonal atom law. The latter directly rules out zero coordinates, as explained below. |
| [Rudelson–Vershynin, 1506.04012v1](https://arxiv.org/abs/1506.04012v1), GAFA 2016 | Theorem 1.3, p. 3; Theorem 1.5, pp. 3–4 | No-gaps mass bounds for continuous and discrete distributions under the stated independence, anticoncentration, and norm hypotheses. In this saved version the meaningful general discrete range has |I| bounded below on a power scale (Remark 1.6), rather than |I|=1. No minimum law. |
| [Aggarwal–Lopatto–Marcinek, 2002.09355v3](https://arxiv.org/abs/2002.09355v3), Annals of Probability 2021 | Theorems 2.9 and 2.10, p. 8 | Fixed families of entries/projections for α-stable Lévy matrices, 0<α<2, with model-dependent variance mixtures. Infinite-variance atoms are outside the survey corollary’s setting. |
| [Benigni–Cipolloni, 2212.10694v1](https://arxiv.org/abs/2212.10694v1), EJP 2024 | Theorem 2.2, p. 4 | Joint Gaussian fluctuations of finitely many bulk quadratic forms, with sufficiently large effective rank. A nonlinear count of tiny coordinates is not one of these forms. |
| [Benigni–Rezaei Feyzabady, 2509.19581v1](https://arxiv.org/abs/2509.19581v1), RMTA 2026 | Theorem 1.2, p. 2 | Functional limits for bulk quadratic-form processes with deterministic Hölder-regular observables. Not the near-zero coordinate point process. |
| [Benigni–Lopatto, 2606.06419v2](https://arxiv.org/abs/2606.06419v2), September 2026 preprint | Theorem 1.2, p. 3; Theorem 1.3 and Corollary 1.4, pp. 3–4; Theorems 1.6–1.7, pp. 4–5 | All-index generalized Wigner results. The Poisson process is for the largest squared entries, centered at 2 log n−log log n−log π, under subexponential tails. Smooth entries permit a growing number of projections and explicit additive errors. This process is not centered at zero. |
| [Bao–Bucht–Schnelli, 2606.17425v1](https://arxiv.org/abs/2606.17425v1), June 2026 preprint | Theorem 1.5, p. 3; Theorems 1.7 and 1.9, p. 4 | Generalized Wigner edge eigenvectors, bounded normalized moments. Upper extremes and intermediate order statistics; a general smooth comparison for arbitrary ranks. For the smallest squared coordinate the relevant variation is n^{-2} after multiplying by n, whereas the comparison allows only much coarser derivatives. |
| [Osman, 2609.11630v1](https://arxiv.org/abs/2609.11630v1), September 2026 preprint | Theorem 1.2, p. 3; Theorem 1.3, p. 4 | Gumbel laws for largest entries: an individual eigenvector nearest a fixed energy, and the whole eigenbasis under the stated complex/four-moment real hypotheses. Fixed energy is different from a chosen ordered index; neither result concerns the minimum. |
| [Fyodorov–Shcherbina–Shcherbina, 2611.12858v1](https://arxiv.org/abs/2611.12858v1), November 2026 preprint | Theorem 2.4, pp. 10–11; Corollary 2.3, p. 11 | A genuine lower-extreme Poisson/exponential result for squared occupations in the complex GUE Rosenzweig–Porter model, with 1<γ<2 and a fixed-energy Kac–Rice eigenpair law. The scaling is n^{1+γ} for the squared minimum, with a disorder factor. Dominant diagonal disorder and complex symmetry exclude its use as a resolution or counterexample here. |

In particular, the 2026 growing-coordinate statement has Q total projections spanning a space of dimension R and requires RQ≤Cn^{1/2−b}, with 0<b≤1/2. For Q distinct coordinates of one eigenvector, R=Q, so it allows Q≤n^{1/4−ε}, under smoothness. Theorem 1.7 gives additive rectangular Kolmogorov error O(n^{-b+κ}); even for one coordinate the best stated exponent is 1/2−κ. The Gaussian probability of |√n v(k)|≤t/n is about ct/n. An additive n^{-1/2+κ} error cannot determine its leading constant. For r coordinates, the needed probability is order n^{-r}. Likewise, smoothing a cutoff on width 1/n costs second derivatives of order n², beyond Theorem 1.6’s δ_2<b condition. These are explicit failures of a proposed deduction, not a claim that the papers’ methods could never be extended.

Proof 1: the Gaussian and GOE limit, including the rate constant.

Let G_1,…,G_n be iid N(0,1). Their absolute-value density on [0,∞) is

\[
 f(x)=\sqrt{2/\pi}\,e^{-x^2/2},\qquad
 F(x)=cx+O(x^3)\quad(x\downarrow0).
\]

Thus for fixed t≥0,

\[
 \mathbb P\{n\min_k|G_k|>t\}
 =\bigl(1-F(t/n)\bigr)^n
 \longrightarrow e^{-ct}.
 \tag{3}
\]

Indeed nF(t/n)→ct and nF(t/n)^2→0, so expanding log(1−F(t/n)) proves (3). Consequently the limiting mean is 1/c=√(π/2), not 1.

Put S_n=(n^{-1}∑G_k²)^{1/2} and U=G/||G||_2. The strong law gives S_n→1 almost surely. For any orthogonal O, OG has the law of G, hence U is uniform on the unit sphere. This also follows directly from the Gaussian density in polar coordinates. It follows that

\[
 n^{3/2}\min_k|U_k|={n\min_k|G_k|\over S_n}
 \Rightarrow\operatorname{Exp}(c).
 \tag{4}
\]

No independence between numerator and denominator is needed. For example, on |S_n−1|≤η, the survival event in (4) is sandwiched between the numerator’s survival events at t(1+η) and t(1−η); let n→∞ and then η↓0.

A GOE density is proportional to exp(−Tr W²/4), so it is invariant under W↦OWOᵀ. Its spectrum is simple almost surely: the discriminant is a nonzero polynomial in the entries, whose zero set has Lebesgue measure zero. Each ordered eigenline therefore has a rotation-invariant distribution; after an independent random sign its unit eigenvector is uniform on the sphere. The absolute coordinates already have that law without adding the sign. This proves (1) for every GOE index j_n, exactly the same marginal law for each index, covering both edges and the bulk.

There is a stronger GOE statement:

\[
 \sum_{k=1}^n\delta_{n^{3/2}|U_k|}
 \Rightarrow\operatorname{PPP}(c\,dx)
 \quad\text{on }[0,\infty).
 \tag{5}
\]

To prove it first omit S_n. For a nonnegative continuous compactly supported f,

\[
 \mathbb E\exp\!\left(-\sum_k f(n|G_k|)\right)
 =\left[1-\int_0^\infty(1-e^{-f(nx)})f_{|G|}(x)\,dx\right]^n
 \longrightarrow
 \exp\!\left[-c\int_0^\infty(1-e^{-f(y)})\,dy\right].
\]

The change of variables y=nx and dominated convergence give the last step. This is the Laplace functional of the stated Poisson process. Dividing every point by S_n does not change the limit: if supp f⊂[0,B] and S_n∈[1/2,2], only points n|G_k|≤2B matter; their expected number nF(2B/n) is bounded. Their number is therefore tight. Uniform continuity of f and S_n→1 make the difference of the two sums tend to zero in probability, first on a bounded-count event and then without that restriction. Their exponentials lie in [0,1], so expectations also converge. This proves (5). The survey supplies the spherical representation as Lemma 10.1, PDF p. 23; the limit calculation above is provided in full here.

Proof 2: a sufficient rare-event criterion and the role of symmetrization.

For an arbitrary random unit vector V_n define

\[
 X_{n,k}=\sqrt n\,|V_n(k)|,\qquad
 N_n(t)=\sum_{k=1}^n\mathbf1\{X_{n,k}\le t/n\}.
\]

Suppose that for every fixed positive integer r and each t>0,

\[
 \sum_{k_1,\ldots,k_r\ \mathrm{distinct}}
 \mathbb P\{X_{n,k_a}\le t/n\ \text{for every }a\}
 \longrightarrow (ct)^r.
 \tag{6}
\]

Then N_n(t)⇒Poisson(ct), and n^{3/2}min_k|V_n(k)|⇒Exp(c).

Here is a complete proof. The left side of (6) is E(N_n(t))_r, where (q)_r=q(q−1)…(q−r+1). Write λ=ct. For integers q,l≥0 and K≥0 the truncated sum

\[
 \sum_{s=0}^K(-1)^s{l+s\choose l}{q\choose l+s}
 ={q\choose l}\sum_{s=0}^K(-1)^s{q-l\choose s}
\]

is interpreted as zero if q<l. When q=l it equals one. When q>l, it is zero once the sum includes all terms; otherwise the final sum equals (−1)^K {q-l-1\choose K}, by Pascal’s identity and cancellation. It follows that odd truncations bound 1_{q=l} from below and even truncations bound it from above. Taking expectations with q=N_n(t), each fixed truncation tends by (6) to

\[
 {\lambda^l\over l!}\sum_{s=0}^K{(-\lambda)^s\over s!}.
\]

Let K tend to infinity through either parity. Both bounds tend to e^{-λ}λ^l/l!, proving convergence of every point probability to the Poisson probability. These probabilities sum to one, so convergence in distribution follows. At l=0 the event N_n(t)=0 is exactly n^{3/2}min_k|V_n(k)|>t. The exponential CDF is continuous; the survival limits for t>0 therefore prove the asserted weak limit, including at zero by letting t↓0.

For permutation-exchangeable absolute coordinates, (6) reduces to

\[
 \mathbb P\{X_{n,1},\ldots,X_{n,r}\le t/n\}
 ={(ct)^r+o(1)\over(n)_r}.
 \tag{7}
\]

One may always apply an independent uniform random permutation without changing the minimum. The probability on the left then equals the average of the original distinct-coordinate probabilities, so no unjustified symmetry of a chosen eigenvector basis is necessary. In the iid-atom Wigner setting, matrix permutation invariance also gives the natural exchangeability on the simple-spectrum event. For generalized Wigner variance profiles, averaging is the safer formulation.

A convenient sufficient condition for (7) is a local joint density f_{n,r} of the signed √n coordinates, after an independent global random sign if necessary, satisfying

\[
 \sup_{|x_a|\le t/n}
 |f_{n,r}(x)-(2\pi)^{-r/2}|\to0.
\]

Integration over the box gives (7), since (2t/n)^r(2π)^{-r/2}=(ct/n)^r. A uniform o(n^{-r}) error for these box probabilities also suffices, without any density, and can apply to discrete atoms. By contrast, a weak Gaussian limit only says that the probabilities of these shrinking boxes tend to zero; it does not identify their n^{-r} leading term. None of the printed theorems identified above supplies (6) or (7) in the real fixed-atom Wigner setting. Only fixed r is needed in this criterion; a simultaneous Gaussian approximation of order n coordinates is not logically necessary.

There is an independent check of the GOE rate using the exact spherical density computed in Proof 3. With d=n and m=r fixed, its prefactor tends to (2π)^{-r/2}, by Γ(z)/Γ(z−r/2)∼z^{r/2}, and its nonconstant factor tends uniformly to one on |y_a|≤t/n. Integration gives the local probability (ct/n)^r(1+o(1)), so Proof 2 recovers the same exponential law. For n>r+2, the exact bounds on n^r times that probability are

\[
 (2t)^r C_{n,r}(1-rt^2/n^3)^{(n-r-2)/2}
 \ \le\ n^r\mathbb P\{\sqrt n|U_a|\le t/n,\ a\le r\}
 \ \le\ (2t)^r C_{n,r},
 \quad C_{n,r}={\Gamma(n/2)\over\Gamma((n-r)/2)(\pi n)^{r/2}},
\]

provided rt²<n³. Both bounds tend to (ct)^r. The gamma ratio follows directly from Stirling’s formula with fixed r. These bounds were also evaluated numerically at t=1, r≤4, n≤8192, separately from the eigenvector simulations.

Proof 3: sublinear Gaussian marginals do not determine the minimum.

The following are counterexamples to an inference about random unit vectors, not counterexamples to Wigner universality. For every m_n=o(n), they have Gaussian m_n-coordinate marginals in total variation, uniformly in the coordinate subset.

Choose I uniformly from {1,…,n}. Put Z_n(I)=0, and on the other n−1 coordinates put an independent uniform unit vector in R^{n−1}. This gives an exchangeable unit vector with an exactly zero minimum. Nevertheless,

\[
 d_{\rm TV}\!\left(\mathcal L(\sqrt n(Z_n(k))_{k\in J_n}),
                       N(0,I_{m_n})\right)\longrightarrow0
 \quad (|J_n|=m_n=o(n)).
 \tag{8}
\]

There is also a version with no zero coordinates. Fix a>0, for n large enough that a²<n³. Set Z_n(I)=ε a n^{-3/2}, where ε is an independent random sign; make the remaining vector uniform on the sphere of radius R_n=√(1−a²/n³) in R^{n−1}. It is exchangeable and sign symmetric, all its coordinates are nonzero almost surely, and (8) still holds. By (4) in dimension d=n−1,

\[
 n^{3/2}\min_k|Z_n(k)|
 \Rightarrow\min(a,E),\qquad E\sim\operatorname{Exp}(c).
 \tag{9}
\]

In particular the limiting law has an atom of mass e^{-ca} at a, unlike (1). This also shows why absence of exact zeros does not fill the universality gap.

For completeness, a density and entropy argument proves (8) even when m_n=n^{1−ε}. If U is uniform on the unit sphere in R^d and Y=√d(U_1,…,U_m), its density is

\[
 p_{d,m}(y)=
 {\Gamma(d/2)\over\Gamma((d-m)/2)(\pi d)^{m/2}}
 \left(1-{\|y\|^2\over d}\right)^{(d-m-2)/2}
 \mathbf1_{\{\|y\|<\sqrt d\}}.
\]

To obtain this, split d independent Gaussian squares into the first m and last d−m; their half-sums are independent Gamma(m/2,1) and Gamma((d−m)/2,1). Changing variables to their sum and ratio gives a Beta(m/2,(d−m)/2) ratio, independent of the sum. The direction of the first block is uniform. Polar integration, or the beta integral, gives the displayed density and its normalizing constant. In particular E||Y||²=m and

\[
 \mathbb E\log(1-\|Y\|^2/d)=\psi((d-m)/2)-\psi(d/2),
\]

by differentiating the beta integral. Let z=d/2, u=m/2, b=z−u. Relative to the standard m-dimensional Gaussian, the entropy is therefore

\[
 D(u)=\log\Gamma(z)-\log\Gamma(b)-u\log z
       +(b-1)(\psi(b)-\psi(z))+u.
\]

For fixed z, differentiation gives

\[
 D'(u)=\psi(z)-\log z+1-(b-1)\psi'(b)\le {1\over b}
 \quad(b\ge1).
\]

Here ψ(z)=E log T≤log ET=log z for T∼Gamma(z,1), by differentiating the gamma integral and Jensen’s inequality. Also ψ'(b)=∑_{k≥0}(b+k)^{-2}≥∫_0^∞(b+x)^{-2}dx=1/b. The series follows by differentiating Euler’s product for Γ; it converges absolutely for b>0. Since D(0)=0, integration proves

\[
 D(u)\le\log{d\over d-m},\qquad
 d_{\rm TV}(\mathcal L(Y),N(0,I_m))
 \le\sqrt{\tfrac12\log(d/(d-m))}\to0\quad(m=o(d)).
 \tag{10}
\]

The last step is Pinsker’s inequality. One short justification is to coarse-grain both densities onto an event attaining their total variation: the log-sum inequality makes entropy decrease under this coarse-graining, and Bernoulli relative entropy is at least twice the squared difference of its probabilities, as follows by its second derivative in the first probability being 1/[p(1−p)]≥4 and its value and first derivative vanishing at p=q.

For a fixed coordinate set J of size m, P(I∈J)=m/n. Conditional on I∉J, the selected coordinates are a projection of a sphere in d=n−1 dimensions. Their scaling differs from √d only by s_n=√(n/d) in the zero version, or s_n=√(n/d)R_n in the nonzero version. In both cases s_n²=1+O(1/n). Scaling preserves total variation, and the entropy between N(0,s_n²I_m) and N(0,I_m) is

\[
 {m\over2}(s_n^2-1-\log s_n^2)=O(m/n^2).
\]

Combine this with (10), Pinsker, and the mixture weight m/n to prove (8), uniformly in J. Finally, in the nonzero version the scaled minimum of the remaining coordinates equals (n/d)^{3/2}R_n times the d-dimensional spherical scaled minimum. Its multiplier tends to one. Taking the minimum with the planted value a proves (9).

Thus even Gaussian total variation convergence on every n^{1−ε} coordinate subset, together with exchangeability, unit normalization, and nonvanishing, is insufficient by itself. A sampled sublinear subset misses the planted exceptional coordinate with probability tending to one. Random symmetrization does not change this fact.

Proof 4: exact zeros cannot give the proposed fixed-atom Bernoulli obstruction.

The survey already states a stronger nonvanishing result as Theorem 1.4, PDF p. 3: with subgaussian atoms, the probability that any coordinate of any eigenvector is zero is O_A(n^{-A}) for every fixed A>0. It also gives the same superpolynomial simplicity bound for any nondegenerate off-diagonal atom. This directly includes Rademacher ξ and either Rademacher or zero ζ.

The underlying primary source was also checked: Tao–Vu, [“Random matrices have simple spectrum,” 1412.1438v1](https://arxiv.org/abs/1412.1438v1), Theorem 1.3 (PDF p. 2) and Proposition 2.2 (p. 3). The proposition bounds the probability that the last off-diagonal column X is orthogonal to any nontrivial eigenvector of the independent principal minor by O_A(n^{-A}). Its hypotheses require a nontrivial off-diagonal atom with a fixed upper bound below one on point masses. This gives a direct proof of nonvanishing: write W in blocks as [[A,X],[Xᵀ,a]]. An eigenvector (u,0) must satisfy Au=λu and Xᵀu=0, precisely the event in the proposition. Use the proposition with exponent A+2 and union over the n deleted indices. This yields O_A(n^{-A}) for any zero coordinate of any eigenvector, without selecting a basis in a repeated eigenspace. A fixed nondegenerate Rademacher law satisfies the atom hypothesis.

One can also recover the chosen-basis nonvanishing conclusion from the printed Theorem 4.7, PDF p. 13. Its bound is the right side of (2) for each event |v_i(k)|≤δ/[√n(log n)^{c_1}]. Given A>0, set B=A+3, α=c_0/(B+1), and δ=n^{-B}. For sufficiently large n, n^{-c_0}<α<c_0 and δ≥n^{-c_0/α}=n^{-(B+1)}. Since the threshold is strictly positive,

\[
 \mathbb P\{v_i(k)=0\}
 \le C_A n^{-B}+C e^{-c_*\log^2n}.
\]

Union over n² pairs gives O_A(n^{-A}); the exponential-logarithmic term is smaller than every inverse power after the union. On the simple-spectrum event this holds for all unit eigenvectors, and its complement is also O_A(n^{-A}) by Theorem 1.4. This proves that a non-o(1) exact-zero probability cannot refute (1) under these assumptions. It says nothing sufficient about nonzero coordinates of size t n^{-3/2}.

Finite-size exact zeros do occur. For

\[
 A=\begin{pmatrix}1&1&1\\1&1&1\\1&1&-1\end{pmatrix},
 \qquad v=2^{-1/2}(1,-1,0)^T,
\]

Av=0 and the characteristic polynomial is x(x²−x−4). The other eigenvalues (1±√17)/2 are distinct and nonzero, so this is a simple-spectrum example in the support of the fully Rademacher ensemble. For a general fixed pair of labels, (e_1−e_2)/√2 is an eigenvector whenever W_11=W_22 and W_{k1}=W_{k2} for k≥3. For fully Rademacher entries this mechanism has probability 2^{-(n−1)}. Union over label pairs is at most {n choose 2}2^{-(n−1)}→0; it cannot establish a positive asymptotic obstruction.

The exhaustive counts below are over all upper-triangular sign assignments with the indicated diagonal law. “With a zero” counts matrices with simple spectrum having at least one zero eigenvector coordinate; repeated-spectrum matrices are listed separately, because individual basis vectors are ambiguous there.

| Diagonal law | n | Matrices | Simple spectrum | Simple spectrum with a zero |
|---|---:|---:|---:|---:|
| Rademacher | 2 | 8 | 8 | 0 |
| Rademacher | 3 | 64 | 48 | 48 |
| Rademacher | 4 | 1024 | 768 | 576 |
| Zero | 2 | 2 | 2 | 0 |
| Zero | 3 | 8 | 0 | 0 |
| Zero | 4 | 64 | 48 | 48 |
| Zero | 5 | 1024 | 0 | 0 |

These are finite-n facts, not trend evidence for a limiting zero probability. To certify zeros exactly, let p(x)=det(xI−A) and p_i(x)=det(xI−A^{(i)}). For a simple eigenvalue λ_j, the resolvent identity gives

\[
 {p_i(x)\over p(x)}=(xI-A)^{-1}_{ii}
 =\sum_j{|v_j(i)|^2\over x-\lambda_j}.
\]

Taking residues gives |v_j(i)|²=p_i(λ_j)/p'(λ_j). Thus a zero coordinate occurs precisely when p and p_i share a root. For a real symmetric simple-spectrum matrix all roots are real and simple, so polynomial gcds detect exactly the event being counted. The code also checks gcd(p,p')=1 before counting.

[code/exact_zeros.py](code/exact_zeros.py) exhausts the full sign space. [code/audit_exact_zeros.py](code/audit_exact_zeros.py) independently fixes the first off-diagonal row to +1 by diagonal sign conjugation, computes determinants and resultants, and weights each representative by 2^{n−1}. Such conjugation preserves eigenvalues and zero coordinates, and each sign-switching orbit has exactly that multiplicity after fixing the first diagonal sign to +1. Every row agrees; see [data/exact_zero_audit.json](data/exact_zero_audit.json).

Numerical evidence and audit.

The primary run used seed 980013 and independent matrices in each ensemble, with 1,000 matrices at n=128, 400 at n=512, 160 at n=1024, and 50 at n=2048, per ensemble: 4,830 matrices and 14,490 selected eigenvectors. The selected increasing-order indices were j=1, j=⌊n/2⌋+1, and j=n. Eigenvectors from the same matrix were used in separate index groups; they were not treated as independent observations within a pooled test.

The three ensembles, before the irrelevant scalar division by √n, were: GOE with off-diagonal N(0,1) and diagonal N(0,2); Rademacher entries on and above the diagonal; and centered Bernoulli entries (B−p)/√[p(1−p)] on and above the diagonal, with p=0.1 fixed. Centering is essential: an uncentered adjacency matrix has an outlier eigenvector and is a different experiment. The Bernoulli model is only sparse-ish at these finite sizes; p does not decrease with n.

The comparison distribution was fixed in advance of fitting any data: CDF 1−exp(−√(2/π)t), mean 1.2533141373, and median 0.8687311606. The primary summaries are:

| Ensemble | n | Matrices | Mean: lower edge | Mean: bulk | Mean: upper edge | Largest KS distance of the three |
|---|---:|---:|---:|---:|---:|---:|
| goe | 128 | 1000 | 1.2619 | 1.3089 | 1.2279 | 0.0261 |
| goe | 512 | 400 | 1.3046 | 1.0951 | 1.1858 | 0.0702 |
| goe | 1024 | 160 | 1.2795 | 1.3068 | 1.2807 | 0.0700 |
| goe | 2048 | 50 | 1.2318 | 1.3459 | 1.3947 | 0.1083 |
| rademacher | 128 | 1000 | 1.3460 | 1.2182 | 1.2777 | 0.0336 |
| rademacher | 512 | 400 | 1.2140 | 1.2380 | 1.4952 | 0.0806 |
| rademacher | 1024 | 160 | 1.3006 | 1.4788 | 1.3047 | 0.0849 |
| rademacher | 2048 | 50 | 1.0765 | 1.3459 | 1.1149 | 0.1455 |
| bernoulli_p010 | 128 | 1000 | 1.1353 | 1.1748 | 1.0766 | 0.0755 |
| bernoulli_p010 | 512 | 400 | 1.2271 | 1.1903 | 1.2630 | 0.0379 |
| bernoulli_p010 | 1024 | 160 | 1.1117 | 1.2788 | 1.0568 | 0.0906 |
| bernoulli_p010 | 2048 | 50 | 1.0607 | 1.3421 | 1.2573 | 0.1408 |

The full results, including medians, CDF values, standard errors, KS statistics/p-values, and the first two factorial moments of N_n(1) and N_n(2), are in [data/summary.csv](data/summary.csv). The expected Poisson moments are ct and (ct)². Those empirical moments are descriptive; they cannot verify the fixed-r asymptotics in (6). The CDF comparison is available as [an SVG figure](data/minimum_cdf.svg) and [a PNG preview](data/minimum_cdf.png), both generated from these data.

The plots show approximate agreement at the sampled larger sizes, with substantial sampling uncertainty at n=2048. For one group the distribution-free 95% DKW half-width is √[log(40)/(2M)]: 0.04295, 0.06791, 0.10737, and 0.19206 for M=1000,400,160,50. Simultaneous 95% bands across all 36 groups use √[log(2·36/0.05)/(2M)], giving 0.06030, 0.09534, 0.15075, and 0.26967. No independence across groups is required for that union bound. In particular the largest-n sample cannot distinguish modest changes in a limiting rate.

There are finite-size discrepancies. Five of 36 primary pointwise KS p-values are below 0.05; one is below 0.05/36: Bernoulli p=0.1, n=128, upper edge, D=0.07553, p=2.082×10^{-5}. At n≥1024 all primary p-values exceed 0.1355. These tests compare each finite-n law to the limiting exponential, not to its unknown finite-n correction; even GOE has no exact exponential finite-n identity.

Because of the n=128 discrepancy, a separate adaptive validation used seed 980014, with 2,000 fresh Bernoulli matrices at n=128 and 1,000 at n=512, all three indices. The n=128 lower/bulk/upper means were 1.15408, 1.19320, 1.16033 and their KS p-values were 0.00984, 0.03196, 0.09748. The n=512 means were 1.21642, 1.22487, 1.26530, with p-values 0.37050, 0.40116, 0.50880. The original upper-edge rejection was not reproduced at the pointwise 0.05 level; no validation p-value is below 0.05/6. Small-n deviations and sampling fluctuations remain visible. This validation was selected after seeing the primary results and is reported separately in [data/validation_summary.csv](data/validation_summary.csv), not silently pooled. It does not establish convergence, a rate of convergence, or atom dependence of a limiting law.

Resource and numerical checks: one sequential worker, BLAS/OpenMP/Accelerate thread limits set to one, with nice 10 inherited from the supplied launcher. The sandbox prevents an independent process-priority inspection. The main numerical run took 588.84 seconds and reached 418,922,496 bytes peak RSS (0.419 GB), well below 4 GB. The compute governor was checked before computation and every ten matrices; it did not enter distress. Maximum main eigenpair residual was 5.0412×10^{-15}, maximum norm error 6.662×10^{-16}; all statistics were finite. No computed minimum equaled floating-point zero, which is not used as an exact nonvanishing proof.

A separate check on fresh n=128 and n=512 matrices of every ensemble compared narrow MRRR eigenpair solves (`evr`) to a full divide-and-conquer solve (`evd`). Maximum scaled-minimum disagreement was 2.980×10^{-11}. Exact-zero enumerations were independently reproduced by the switching/resultant calculation described above. The constant c was checked a second way from erf(h/√2)/h at h=10^{-7}, giving 0.7978845608028637 versus √(2/π)=0.7978845608028654. Exact spherical-density bounds supply the separate analytical check of the rate and normalization.

Reproduction commands, from this directory, are:

```sh
python3 code/fetch_batch.py
python3 code/exact_zeros.py
python3 code/audit_exact_zeros.py
python3 code/simulate.py --tag main --spec 128:1000,512:400,1024:160,2048:50 --seed 980013
python3 code/verify_math.py
python3 code/summarize.py
python3 code/simulate.py --tag validation --spec 128:2000,512:1000 --ensembles bernoulli_p010 --seed 980014
python3 code/summarize_validation.py
python3 code/audit_artifacts.py
```

The numerical programs set thread limits before importing numerical libraries. `simulate.py` refuses to overwrite an existing sample file, so use a fresh tag for a repeat; summary scripts refer to the recorded `main` and `validation` tags. Fetching requires network access and `pdftotext`; analysis uses Python, NumPy, SciPy, SymPy, Matplotlib, and threadpoolctl. Exact versions and seeds are saved in the metadata. No dependency installation was performed. Only extracted text is retained for papers; no source PDF, page image, or scan was written. No publication or push was made.


What remains open in this report.

No Wigner theorem supplying (6), (7), or a near-zero Poisson process was found. No proof has been supplied for general Wigner atoms, for a bulk-only subcase, or for an edge-only subcase. No admissible atom-dependent limiting law has been demonstrated. The unconditional proof is for GOE; the general criterion is conditional, and the planted-coordinate construction concerns arbitrary exchangeable sphere vectors. Hence the first-line status is PARTIAL.

Task: “Open problem E0098” — 13 November 2026, approximately 11:10 Asia/Tbilisi.
