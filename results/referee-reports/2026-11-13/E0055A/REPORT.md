PARTIAL

# E0055: projected power iteration for angular synchronization

Audit date: 13 November 2026. The substantive result is in the literature. With spectral initialization, the exact unshifted complex phase iteration converges linearly to the MLE when \(\sigma\le c_0\sqrt{n/\log n}\). This is a sufficient range, not a sharp constant-SNR threshold or a random-start theorem. The source does not specify a random initialization distribution. Per the requested stopping rule for a printed result covering a parameter range or initialization, this report stops at stage 1; no new convergence theorem or simulation is claimed.

## 1. Exact source and statement

The title is **Afonso S. Bandeira, *Ten Lectures and Forty-Two Open Problems in the Mathematics of Data Science***.

Two versions were obtained and saved as complete, page-labelled plain text:

| Copy | Date on title page | Model and MLE | Algorithm 10.1 and Open Problem 10.1 |
|---|---|---|---|
| [ETH author-hosted copy](https://people.math.ethz.ch/~abandeira/TenLecturesFortyTwoProblems.pdf), sources/bandeira_eth.txt | October 10, 2016 | printed/PDF p.132, equation (105) | printed/PDF p.133 |
| [MIT OCW copy](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-of-data-science-fall-2015/5f0f7205d1cf274e80d77345a7edbf2a_MIT18_S096F15_TenLec.pdf), sources/bandeira_mit.txt | December, 2015 | PDF p.144, equation (103) | PDF p.145 |

PDF page numbers here are one-based. The ETH copy has 152 pages, the MIT copy 165. Thus “2015, PDF p.133” combines two different versions. No arXiv identifier for these lecture notes was verified; the direct author and course URLs above identify the actual sources. Source hashes and retrieval times are in data/*_provenance.json.

In §10.2, *Angular Synchronization*, the unknown signal is
\[
z=(z_1,\ldots,z_n)\in\mathbb C^n,\qquad |z_i|=1,\qquad z_i=e^{\mathrm i\theta_i}.
\]
One observes noisy relative angles for every pair, written in matrix form in Open Problem 10.1 as
\[
Y=zz^*+\sigma W,\qquad \sigma\ge0.
\]
Equivalently, \(Y_{ij}=z_i\overline{z_j}+\sigma W_{ij}\). The p.132 prose abbreviates the entry noise law as \(W_{ij}\sim N(0,1)\). It does **not** fully spell out there the complex variance convention, upper-triangular independence, or diagonal convention. Those details must not be supplied as though they were explicit in the notes. The Hermitian Gaussian phase-synchronization model used by the resolving literature is specified below. Some overbars and radicals are lost by text extraction; the matrix expression \(zz^*\) fixes the conjugation.

The maximum-likelihood optimization problem (105) in the ETH version is
\[
\max_{x\in\mathbb C^n:\ |x_i|^2=1\ \forall i}x^*Yx. \tag{105}
\]
A common phase is unidentifiable: \(x\) and \(e^{\mathrm i\phi}x\) represent the same estimate. The noisy MLE is generally different from \(z\).

Algorithm 10.1 on p.133 takes \(Y\) and an initial vector described, verbatim, as “a original (maybe random) vector” \(x^{(0)}\). Until convergence or a chosen iteration limit it updates
\[
x_i^{(k+1)}=\frac{(Yx^{(k)})_i}{|(Yx^{(k)})_i|},\qquad i=1,\ldots,n. \tag{A10.1}
\]
There is no shift, stepsize, Onsager correction, initial correlation assumption, initial distribution, or rule for a zero denominator in the printed algorithm. In particular, an independent uniform phase start is a possible experimental choice, not “the stated initialization.” A leading eigenvector is another permissible choice.

The exact mathematical question in Open Problem 10.1, ETH p.133, is: for which values of \(\sigma\), under \(Y=zz^*+\sigma W\), does Algorithm 10.1 converge with high probability to the optimum of (105), or at least to an estimate well correlated with \(z\)? The full original wording is retained in sources/bandeira_eth.txt at the PDF PAGE 133 marker; in the 2015 copy the same question refers to (103). Neither a numerical conjectured threshold nor a quantified definition of “correlates well” is given in that problem statement. The nearby \(\widetilde O(\sqrt n)\) conjecture on ETH p.134 concerns SDP tightness, Open Problem 10.2.

This is \(U(1)\simeq SO(2)\) synchronization. The separate \(\mathbb Z_2\) discussion is on ETH p.136. A real sign iteration is not the exact problem on p.133.

## 2. Decisive literature theorem, with exact initialization

**Yiqiao Zhong and Nicolas Boumal, “Near-Optimal Bounds for Phase Synchronization,” SIAM Journal on Optimization 28(2) (2018), 989–1016, [DOI 10.1137/17M1122025](https://doi.org/10.1137/17M1122025).** The complete verified text here is [arXiv:1703.06605v1](https://arxiv.org/abs/1703.06605v1), submitted 20 March 2017, title page dated 21 March 2017, 34 pages. All theorem/page references in the next paragraphs refer explicitly to this arXiv edition, not inferred journal pagination. Journal publication data were independently checked on the author's [publication page](https://www.nicolasboumal.net/). The NSF journal mirror timed out and SIAM denied the full-text download.

Their Gaussian model, equations (1)–(2), p.2, is
\[
C=zz^*+\sigma W,
\]
with \(|z_i|=1\), independent standard complex Gaussian \(W_{ij}\) above the diagonal, \(W_{ji}=\overline{W_{ij}}\), and \(W_{ii}=0\). In particular \(C_{ii}=1\). Their formal theorems also allow independent centered sub-Gaussian real and imaginary upper-triangular entries with a uniform tail parameter; the exact assumptions and equation (19) are on p.11. Real Gaussian entries with zero imaginary part are included in that broader optimization result, though the Gaussian complex model is the MLE interpretation being used here.

**Algorithm 1, p.3:** choose \(x^0\) as an eigenvector for the largest eigenvalue of \(C\), scaled so \(\|x^0\|_2=\sqrt n\), and iterate
\[
x^{t+1}=\mathcal P(Cx^t),\qquad
\mathcal P(a)=\begin{cases}a/|a|,&a\ne0,\\1,&a=0.\end{cases}
\]
The initializer is the eigenvector itself, not its entrywise phase projection. The first update makes the entries unit modulus. The positive normalization of \(x^0\) has no effect on the first phase update. This is the unshifted rule (A10.1) with a specified, data-dependent initialization and a completed zero convention.

**Theorem 6, p.12:** there is a sufficiently small absolute constant \(c_0>0\) such that, if
\[
\sigma\le c_0\sqrt{n/\log n},
\]
then, with probability \(1-O(n^{-2})\), Algorithm 1 converges up to phase to some \(\widehat x\) and
\[
d_2(x^t,\widehat x)\le 2^{2-t}\sqrt n,\qquad t=0,1,2,\ldots,
\]
where \(d_2(u,v)=\min_\phi\|e^{\mathrm i\phi}u-v\|_2\).

**Theorem 7, p.12:** under the same assumptions, with probability \(1-O(n^{-2})\), this limit is the unique global optimum, up to phase, of their problem (P), which is exactly (105) with \(C=Y\). Furthermore, for an absolute constant \(C_0\),
\[
d_2(\widehat x,z)\le C_0\sigma,\qquad
\min_\phi\|e^{\mathrm i\phi}\widehat x-z\|_\infty
 \le C_0\sigma\sqrt{\log n/n}.
\]
Combining the two probability statements still gives \(1-O(n^{-2})\). The introductory **Theorem 2, p.3** states the global linear convergence conclusion directly. Theorem 5, p.12, concerns SDP tightness; it is not being mistaken for a theorem about the iteration.

Thus the MLE branch of the question is answered for this initialization and range. It also answers its correlation branch in that range. It does not assert convergence from an independent random start, every start, or every \(\sigma<\sqrt n\).

For comparison of normalizations, define
\[
M=Y/(\sigma\sqrt n)=\frac{\lambda}{n}zz^*+\frac{W}{\sqrt n},
\qquad \lambda=\frac{\sqrt n}{\sigma}\quad(\sigma>0).
\]
Positive scaling leaves (A10.1) unchanged. In this amplitude-SNR convention the theorem requires \(\lambda\ge c_0^{-1}\sqrt{\log n}\); in squared-SNR convention \(\lambda^2=n/\sigma^2\), it requires \(\lambda^2\ge c_0^{-2}\log n\). This is not a proof of a constant-SNR boundary such as \(\lambda=1\). A different variance convention changes constants, not the displayed order.

## 3. Proof content and checks

No new proof is offered. The global convergence assertion above is an application of the printed theorems, with the algorithm, initialization, diagonal and noise hypotheses matched explicitly. Their proof uses leave-one-out matrices \(W^{(m)}\) obtained by zeroing row and column \(m\), and corresponding auxiliary iterate sequences. Independence controls \(w_m^*x^{t,m}\); proximity of the auxiliary and actual iterates then controls \(\|Wx^t\|_\infty\), despite the dependence of \(x^t\) on \(W\). The relevant results in the verified edition are Lemma 14 p.17, Theorem 15 p.18, and Theorem 17 and Lemma 18 pp.19–20. Their main theorem proofs are on p.31.

The proof first controls finitely many iterations probabilistically, then controls the infinite tail deterministically. It proves contraction along the relevant iterates; it does not assume that an entire surrounding neighborhood is invariant. The limit is certified optimal by a positive semidefinite dual certificate, not by objective ascent alone.

Two elementary consequences were re-derived independently:

1. **Correlation from error.** For unit-modulus \(x,z\), direct expansion gives
   \[
   d_2(x,z)^2=2n-2|z^*x|.
   \]
   Hence Theorem 7 yields
   \[
   \frac{|z^*\widehat x|}{n}\ge1-\frac{C_0^2\sigma^2}{2n}
       =1-O(1/\log n)
   \]
   in the stated noise range. This is strong correlation, not exact recovery of the planted phases.

2. **An independent error bound from optimality.** Align \(\widehat x\)'s phase to \(z\), put \(d=\|\widehat x-z\|_2\), and use \(\widehat x^*C\widehat x\ge z^*Cz\). Then
   \[
   \frac n2d^2\le n^2-|z^*\widehat x|^2
     \le\sigma(\widehat x^*W\widehat x-z^*Wz)
     \le2\sigma\sqrt n\,\|W\|_{\rm op}d.
   \]
   For \(d>0\), this gives \(d\le4\sigma\|W\|_{\rm op}/\sqrt n\); the zero case is immediate. With the printed Gaussian spectral-norm bound this is \(O(\sigma)\), agreeing with Theorem 7. This deterministic calculation is already recorded as Theorem 3, equation (3), p.4 of the same paper; it is not a new result.

The certificate's sufficiency was also checked algebraically: if \(D\) is real diagonal, \(Cx=Dx\), and \(S=D-C\succeq0\) with kernel \(\operatorname{span}\{x\}\), then for every feasible \(y\),
\[
y^*Cy=\operatorname{tr}D-y^*Sy\le\operatorname{tr}D=x^*Cx.
\]
Equality forces \(y\) to be a global phase multiple of \(x\). The difficult probabilistic claim that the limit has such a certificate belongs to the cited literature.

Checks included reading the actual full theorem statements and algorithms, checking normalization twice, distinguishing convergence of iterates from bounded statistical error, and distinguishing the noisy MLE from the planted vector. A second text-extraction method was used on decisive pages where available; no page images were made. This is a source and implication audit, not a new line-by-line verification of every auxiliary lemma in the published proof.

## 4. Other literature searched, 2015–2026

Only primary papers or author/publisher pages support the following scope decisions. Exact theorem/page references below identify the particular edition read.

| Work | Finding and relevance |
|---|---|
| Boumal, [*Nonconvex phase synchronization*](https://arxiv.org/abs/1601.06114v3), SIAM J. Optim. 26(4), 2355–2377 (2016), DOI 10.1137/16M105808X | arXiv v3 **Theorem 3 and Lemma 5, p.4**, prove global convergence at \(\sigma=O(n^{1/6})\). **Algorithm 1, p.8**, uses a PSD-making diagonal shift and projected spectral initialization. This historical partial answer changes the iteration. The source author's [February 2016 update](https://afonsobandeira.wordpress.com/2016/02/01/generalized-power-method-for-so2-synchronization/) explicitly identifies it as progress on 10.1. Full text saved. |
| Liu–Yue–So, [*On the Estimation Performance and Convergence Rate of the Generalized Power Method for Phase Synchronization*](https://arxiv.org/abs/1603.00211v3), SIAM J. Optim. 27(4), 2426–2446 (2017) | arXiv v3 **Theorem 3, pp.13–14; Corollary 2, p.21**, give linear convergence to the MLE for \(\sigma=O(n^{1/4})\), from projected spectral initialization. Their **Algorithm 1, p.6**, uses \(\mathcal P((I+\alpha C/n)x)\). **Theorem 1, p.8**, also bounds statistical errors without assuming iterate convergence. These are different conclusions. Full text saved. |
| Chen–Candès, [*The Projected Power Method: An Efficient Algorithm for Joint Alignment from Pairwise Differences*](https://doi.org/10.1002/cpa.21760), CPAM 71(8), 1648–1714 (2018) | The [author-hosted manuscript](https://candes.su.domains/publications/downloads/JointAlign.pdf) concerns discrete modulo labels and lifted simplex projection with spectral initialization. Its title does not identify it with the scalar complex phase update here. Screened as a model/algorithm mismatch, not used as a resolving theorem. |
| Ling, [*Near-Optimal Performance Bounds for Orthogonal and Permutation Group Synchronization via Spectral Methods*](https://arxiv.org/abs/2008.05341v3), ACHA 60, 20–52 (2022) | Spectral estimation and rounding for orthogonal/permutation groups, rather than a sharp random-start threshold for (A10.1). Title and scope verified. |
| Ling, [*Improved Performance Guarantees for Orthogonal Group Synchronization via Generalized Power Method*](https://arxiv.org/abs/2012.00470v3), SIAM J. Optim. 32(2), 1018–1048 (2022) | Verified arXiv v3 **Theorems 3.1–3.2, pp.7–8**: spectral-start block-polar GPM converges linearly to the MLE/SDP solution at a near-optimal noise scaling; includes the real sign problem as \(d=1\). This is an extension to orthogonal groups, not a constant-SNR random-start theorem for the complex scalar iteration. Full text saved. |
| Ling, [*Solving Orthogonal Group Synchronization via Convex and Low-Rank Optimization: Tightness and Landscape Analysis*](https://arxiv.org/abs/2006.00902), Mathematical Programming 200, 589–628 (2023) | Relevant SDP/landscape work. The requested title “On the exactness of SDP relaxation for synchronization” was not found as an exact Ling title. His [author list](https://shuyang-ling.github.io/Publication_topic.html) instead lists this synchronization paper and [*On the Exactness of SDP Relaxation for Quadratic Assignment Problem*](https://arxiv.org/abs/2408.05942) (2024). Neither title is silently substituted for a theorem about (A10.1). |
| Gao–Zhang, [*Exact Minimax Estimation for Phase Synchronization*](https://arxiv.org/abs/2010.04345), IEEE TIT 67(12), 8236–8247 (2021) | **Theorem 2, journal p.8239 / PDF p.4**, gives a sharp statistical error bound for spectral-start GPM; at full observation, \(\sigma^2=o(n)\) gives error \((1+o(1))\sigma^2/2\). **Algorithm 1 and (12), pp.8238–8239**, use zero diagonal, unlike Zhong–Boumal's diagonal one. The theorem bounds error of later iterates, not convergence to an individual MLE. The diagonal change preserves the constrained objective's optimizers but changes the iteration. Full journal text saved. |
| Deshpande–Abbe–Montanari, [*Asymptotic Mutual Information for the Two-Groups Stochastic Block Model*](https://arxiv.org/abs/1507.08685) (2015 preprint); related Montanari AMP work | Information-theoretic/AMP results for binary spiked models and SBM do not establish convergence of the memoryless unit-phase update. Screened at primary abstract and through Zhong–Boumal's discussion, pp.3–4; not counted as a resolving theorem here. |
| Javanmard–Montanari–Ricci-Tersenghi, [*Phase Transitions in Semidefinite Relaxations*](https://arxiv.org/abs/1511.08769), PNAS 113, E2218–E2223 (2016) | The primary paper explicitly uses nonrigorous statistical-mechanics methods for SDP phase-transition predictions. It is not a rigorous convergence theorem for Algorithm 10.1. |
| Perry–Wein–Bandeira–Moitra, [*Message-passing algorithms for synchronization problems over compact groups*](https://arxiv.org/abs/1610.04583v1) (2016) | Discusses projected power iteration separately from AMP; numerical comparison in the real sign model is evidence, not the claimed complex convergence theorem. Its AMP recursion retains a memory correction and does not justify transferring state evolution to (A10.1). Full v1 text saved. |
| Li–Fan–Wei, [*Approximate message passing from random initialization with applications to Z2 synchronization*](https://doi.org/10.1073/pnas.2302930120), PNAS 120(31), e2302930120 (2023) | Addresses the random-initialization issue for AMP with a different recursion and a real binary signal. Not a random-start theorem for (A10.1). |
| Zhang–Zhou, [*Theoretical and Computational Guarantees of Mean Field Variational Inference for Community Detection*](https://arxiv.org/abs/1710.11268v3), Ann. Statist. 48(5), 2575–2598 (2020) | The identified Zhang–Zhou primary paper treats batch variational inference in SBM. No exact Gaussian complex PPM theorem was identified under that author cue. Also screened the separate [Wang–Liu–Zhou–So ICML 2021 PPM paper](https://proceedings.mlr.press/v139/wang21o.html), which treats SBM exact recovery. |
| Later work through 2026 | Screened Zhang's [2024 spectral minimax paper](https://arxiv.org/abs/2209.04962) and Ling's [2026 low-rank landscape paper](https://arxiv.org/abs/2601.20292v2) and [local-geometry paper](https://arxiv.org/abs/2311.18670). Spectral minimax risk and higher-rank factorization landscapes concern different estimators/iterations. No stronger matching random-start convergence theorem was verified. This bounded search is not a claim of exhaustive exclusion of all 2026 work. |

The search included the requested phrases “projected power method” / “spiked Wigner”, “generalized power method” / “Z2 synchronization” / “optimal threshold”, and explicit 2024, 2025 and 2026 variants. Secondary generated problem pages were not used as evidence of resolution. The search route and qualifications are recorded in LOG.md and data/literature_search.txt.

## 5. What remains, and why computation stopped

The verified partial answer is exact-MLE convergence for the original unshifted update, with spectral initialization, at \(\sigma\le c_0\sqrt{n/\log n}\). The remaining stronger questions are a sharp constant-SNR correlation threshold, a theorem from a specified independent random initialization, and exact-MLE convergence beyond the proved range. No impossibility result for this iteration below a matching boundary is claimed. The source itself does not fix enough initialization detail to state one unique random-start threshold.

Stages 2 and 3 were not run because the user explicitly required stopping on a printed parameter-range or initialization result. There is therefore no empirical transition table and no simulated evidence to interpret as proof. code/ contains reproducible source-acquisition and verification tools; data/ contains provenance and audit records. PDF bytes were fetched into memory and only plain text was saved. No PDFs, page images, scans, publication, commits or pushes were made by this task.

Task: “Open problem E0055.” Received 13 November 2026, approximately 13:02 +04 (Asia/Tbilisi).
