PARTIAL

# I0103: Paley ETF restricted isometries

An unconditional, explicit sub-dictionary result is proved below. The full Conjecture 29 is neither proved nor refuted. No settlement was found in the literature checked through 13 November 2026. This is a bounded literature assessment, not an exhaustive certification that no settlement exists.

## Statement and scope

**Partial theorem.** Let \(0<\rho<1/16\) be fixed. For primes \(p\equiv1\pmod4\), set

\[
M_p=(p+1)/2,\qquad L_p=\lfloor p^{9/16-\rho}\rfloor,
\qquad D_p=\{0,1,\ldots,L_p-1,\infty\}.
\]

Here the finite labels and \(\infty\) denote the usual columns of the \(M_p\times(p+1)\) Paley ETF \(\Phi_p\). Its explicit sub-dictionary \(\Psi_p=(\Phi_p)_{D_p}\) has exactly

\[
N_p=L_p+1=p^{9/16-\rho}(1+o(1))
\]

columns and satisfies

\[
\|\Psi_p^*\Psi_p-I\|_{2\to2}
\le C_\rho p^{-\rho/3}+\sqrt{L_p/p}=o(1). \tag{1}
\]

Consequently, for **every** nonempty \(S\subseteq D_p\), the condition number \(\kappa_2((\Phi_p)_S)\) tends to 1, uniformly in \(S\). In particular, for any fixed

\[
0<\varepsilon<1/16-\rho,
\]

all \(\lfloor p^{1/2+\varepsilon}\rfloor\)-subsets of this sub-dictionary have bounded condition number, independent of \(p\).

This answers the permitted \(p^{1-\delta}\) sub-dictionary alternative with \(\delta=7/16+\rho\). It uses signed mixed character sums, not the absolute-value method of arXiv:2611.14475. For a concrete choice, \(\rho=1/32\) retains \(\lfloor p^{17/32}\rfloor+1\) columns and allows sparsity \(\lfloor p^{33/64}\rfloor\), with \(\varepsilon=1/64\).

The dictionary is tall: \(N_p/M_p\to0\). Its retained fraction of the full ETF tends to zero. Thus this does not give a positive-fraction sub-dictionary, an overcomplete RIP construction, or the full-frame conclusion of Conjecture 29. It is a direct application of an established mixed Burgess estimate; no novelty priority is asserted.

## Source and literature assessment

The exact source is **Afonso S. Bandeira, Daniil Dmitriev, Kevin Lucca, Petar Nizić-Nikolac, Almut Rödder, _Randomstrasse101: Open Problems of 2025_, arXiv:2603.29571v1**, submitted **31 March 2026**, with manuscript date 1 April 2026. Entry 12, **Conjecture 29, p.10**, is the stated Paley ETF condition-number conjecture. The “2025” is the year of the collected problems, not the arXiv submission year. [Source](https://arxiv.org/abs/2603.29571v1).

The following references were obtained as primary full texts. Unless otherwise indicated, page numbers below mean the ordinal page of the specified arXiv version, including any title pages, rather than journal pagination. Local filenames are in `sources/`; exact versions and response/text hashes are recorded in `data/source_manifest.jsonl`.

| Reference | Exact relevant locations and verified content |
|---|---|
| Afonso S. Bandeira, Matthew Fickus, Dustin G. Mixon, Percy Wong, _The road to deterministic matrices with the restricted isometry property_, J. Fourier Anal. Appl. **19** (2013), 1123–1149; [arXiv:1202.1234v2](https://arxiv.org/abs/1202.1234v2) | Section 5.3, pp.17–20, constructs/analyzes the Paley ETF. Theorem 20, p.14, relates clique size to exact small-order RIP constants. Lemma 22, p.17, gives \(\delta_K<1\) for \(K\le M_p\), without a uniform gap from 1. Theorem 23, pp.18–19, derives the clique bound \(\omega<\sqrt p\). Conjecture 25, p.20, proposes RIP at \(p/\mathrm{polylog}(p)\) sparsity. |
| Afonso S. Bandeira, Dustin G. Mixon, Joel Moreira, _A conditional construction of restricted isometries_, **International Mathematics Research Notices 2017**, no.2, **372–381**, DOI [10.1093/imrn/rnv385](https://doi.org/10.1093/imrn/rnv385); [arXiv:1410.6457v1](https://arxiv.org/abs/1410.6457v1) | Definition 2.1 and folklore Conjecture 2.2, p.2; **Theorem 2.3, p.3**, with proof pp.3–6: Paley discrepancy below exponent \(1/2\) implies beyond-square-root RIP with distortion tending to zero, which implies an improved clique bound. The allowed exponent satisfies \(1/2<\gamma<\min\{1/(2-\beta),1/(4\alpha)\}\). Proposition 3.2, p.4, is the flat-RIP-to-RIP estimate. |
| Shohei Satake, _On the restricted isometry property of the Paley matrix_, Linear Algebra Appl. **631** (2021), 35–47; [arXiv:2011.02907v2](https://arxiv.org/abs/2011.02907v2) | **Conjecture 7, p.4**, is a two-set Paley character-discrepancy conjecture. **Theorem 10, p.5**, proves beyond-square-root RIP assuming it, with proof pp.5–8. This is conditional. |
| Jean Bourgain, S. J. Dilworth, Kevin Ford, Sergei Konyagin, Denka Kutzarova, _Explicit constructions of RIP matrices and related problems_, Duke Math. J. **159** (2011), 145–185; [arXiv:1008.4535v3](https://arxiv.org/abs/1008.4535v3) | **Theorem 1, p.3**: an explicit \(n\times N\) family with order \(\lfloor n^{1/2+\varepsilon_0}\rfloor\) and distortion \(n^{-\varepsilon_0}\), for an effective positive \(\varepsilon_0\). This is not a theorem about all Paley ETF supports. |
| Dustin G. Mixon, _Explicit Matrices with the Restricted Isometry Property: Breaking the Square-Root Bottleneck_, [arXiv:1403.3427v1](https://arxiv.org/abs/1403.3427v1); book chapter (2015), pp.389–417 | **Theorem 2, pp.14–15**, is the generalized BDFKK construction mechanism. Section 4.2, pp.18–19, optimizes the exponent to approximately \(4.4466\cdot10^{-24}\). This numerical optimization is in a section, not a separately numbered theorem. |
| Kevin Ford, Denka Kutzarova, George Shakan, _Explicit RIP matrices: an update_, Acta Math. Hungar. **168** (2022), 509–515; [arXiv:2108.01794v3](https://arxiv.org/abs/2108.01794v3) | **Theorem 1, p.2**, takes its parameter \(\epsilon=3.26\cdot10^{-7}\), giving sparsity exponent \(1/2+\epsilon/4=1/2+8.15\cdot10^{-8}\). This later improvement must be included when describing the historical record. |
| Christian Kümmerle, Dustin G. Mixon, _Explicit restricted isometries with \(k=m^{2/3-o(1)}\)_, [arXiv:2611.14475v1](https://arxiv.org/abs/2611.14475v1), submitted **10 November 2026** | **Theorem 1, p.3**, is the new unconditional construction. Lemma 3, pp.5–6, and equation (9), p.6, give the density/hybrid estimate. **Theorem 4, pp.6–7**, gives the absolute-value barrier. Theorem 6, p.10, invokes Zahl; Lemma 7 and Proposition 8, p.11, select/control the subframe; equation (16), p.12, finishes RIP. **Proposition 10, pp.12–13**, gives a limitation for its two-distance construction. |
| Dmitriy Kunisky, Xifan Yu, _A degree 4 sum-of-squares lower bound for the clique number of the Paley graph_, CCC 2023, LIPIcs **264**, 30:1–30:25; [published text](https://doi.org/10.4230/LIPIcs.CCC.2023.30); [arXiv:2211.02713v2](https://arxiv.org/abs/2211.02713v2) | **Theorem 2, published p.30:4**, is \(\mathrm{SOS}_4(G_p)\ge c p^{1/3}\). It is **Theorem 1.2, p.4** in the expanded arXiv v2. This bounds a relaxation value; it does not establish a clique of that size or an RIP obstruction. |
| D. R. Heath-Brown, L. B. Pierce, _Burgess bounds for short mixed character sums_, J. London Math. Soc. **91** (2015), 693–708; [arXiv:1404.1677v1](https://arxiv.org/abs/1404.1677v1) | **Theorem 1.4, p.5**, is the unconditional, real-linear-phase mixed Burgess bound used in the partial theorem. Its length restriction and phase uniformity are essential. |

Two corrections to the supplied background matter. BFMW does not prove that an improved clique-number bound alone implies beyond-square-root Paley RIP: BMM's established implication goes from **discrepancy to RIP to clique bounds**. Also, BDFKK was the original unconditional breakthrough, but “the only” is no longer current after the November 2026 construction. Mixon's chapter credits the joint blog investigation with Bandeira on p.2; the [Bandeira project notes](https://afonsobandeira.wordpress.com/2013/12/04/deterministic-rip-matrices-a-new-cooperative-online-project/), the exact chapter, and the later Ford–Kutzarova–Shakan theorem were checked. Mixon's [11 November 2026 announcement](https://dustingmixon.wordpress.com/2026/11/11/explicit-restricted-isometries-well-beyond-the-square-root-bottleneck/) also states the equal-magnitude absolute-value obstruction. Both posts are retained as text; the theorem references above are to the papers.

The bounded search also examined these recent or adjacent primary texts:

- **Elisabeth Gaar and Dunja Pucher**, _The exact subgraph hierarchy and its vertex-transitive variant for the stable set problem for Paley graphs_, **arXiv:2412.12958v2, 9 November 2025**. Theorem 14, p.10, gives a range of hierarchy levels with no improvement over theta; Theorem 19, p.17, compares the two hierarchies. These concern clique/stability relaxations, not Paley RIP. [Text](https://arxiv.org/abs/2412.12958v2).
- **Emily J. King**, _\(k\)-Homogeneous Equiangular Tight Frames_, **arXiv:2505.00160v3, 28 September 2026**. Theorem 2.7, p.9, concerns symmetry groups of the \(q\equiv3\pmod4\) Paley ETF family; Conjecture 4.2, p.16, concerns its spark. It does not settle the real \((p+1)/2\times(p+1)\) family considered here. [Text](https://arxiv.org/abs/2505.00160v3).
- **Dongxiu Cai, Jiasheng Zeng, Xiao-Dong Zhang**, _Sharp Bounds for Guiduli-Type Hereditary Spectral Problems_, **arXiv:2606.08913v1, 8 June 2026**. Theorem 1.3, pp.3–4, concerns spectral bounds under hereditary edge-density constraints. Kümmerle–Mixon cites it for the density-to-spectral connection; it supplies no cancellation for the Paley signs. [Text](https://arxiv.org/abs/2606.08913v1).
- **Yifan Wang, Yanling Shen, Vladimir A. Kobzar**, _Lower Bound on the Block-Diagonal SDP Relaxation of the Clique Number for Seidel Spectrum Bounded Graphs_, author-hosted manuscript, date/version unspecified in the downloaded text. Theorem 3.4, p.9, and Corollary 3.10, p.11, give relaxation lower bounds, including Paley localizations. The search surfaced this as recent work; its date is not independently established. [Author copy](https://yw3762.github.io/assets/pdf/paley.pdf).
- **Dmitriy Kunisky**, _Spectral pseudorandomness and the road to improved clique number bounds for Paley graphs_, **arXiv:2303.16475v1**, published in Experimental Mathematics, DOI [10.1080/10586458.2024.2400182](https://doi.org/10.1080/10586458.2024.2400182), issue dated 2025. Appendix C, **PDF pp.43–44, printed pp.41–42**, explicitly discusses limitations for RIP: large special induced subgraphs are not a substitute for arbitrary small supports. [Text](https://arxiv.org/abs/2303.16475v1).
- **Shohei Satake**, _On the Paley RIP and Paley graph extractor_, **arXiv:2405.08608v2**. Theorem 18 and Corollary 21, p.6, deduce improved extractor properties **assuming** suitable Paley RIP; this is another implication, not a proof of its hypothesis. [Text](https://arxiv.org/abs/2405.08608v2).
- **Joshua Zahl**, _Sphere tangencies, line incidences, and Lie's line-sphere correspondence_, Math. Proc. Cambridge Philos. Soc. **172** (2022), 401–421, **arXiv:2002.11677v2**, Theorem 1.8, pp.4–5, is the geometric input specialized in Kümmerle–Mixon Theorem 6. [Text](https://arxiv.org/abs/2002.11677v2).
- **Alihan Kaplan, Volker Pohl, Holger Boche**, _Deterministic Matrices with a Restricted Isometry Property for Partially Structured Sparse Signals_, SampTA 2019, **Theorem 6, p.3**. The restricted supports concern a different concatenation of two bases; they do not imply the assertion here. [Primary text](https://sampta2019.sciencesconf.org/267683/Kaplan.pdf).

Exact-title searches, date-qualified Paley RIP/discrepancy/explicit-RIP searches, and reference-following found no full resolution. The source collection itself and the November 2026 paper continue to describe the Paley result as conjectural/conditional. Search-result summaries and other generated problem registries were not treated as proof sources.

## Proof of the partial theorem

Write \(e(t)=\exp(2\pi i t)\), and let \(\chi\) be the Legendre symbol modulo \(p\), with \(\chi(0)=0\). Use row labels \(\{0\}\cup Q\), where \(Q\) is the set of nonzero quadratic residues. Normalize the finite columns by

\[
(\phi_j)_0=p^{-1/2},\qquad
(\phi_j)_q=\sqrt{2/p}\,e(-qj/p)\quad(q\in Q),
\qquad \phi_\infty=e_0.
\]

All columns have norm one. The quadratic Gauss sum, using \(p\equiv1\pmod4\), gives for distinct finite indices

\[
\langle\phi_i,\phi_j\rangle
=\frac1p+\frac2p\sum_{q\in Q}e(q(i-j)/p)
=\frac{\chi(i-j)}{\sqrt p},
\qquad \langle\phi_j,\phi_\infty\rangle=p^{-1/2}. \tag{2}
\]

This also fixes the sign convention; BFMW/BMM contain the same Gram computation.

For \(I_L=\{0,\ldots,L-1\}\), let \(T_L\) have entries \((T_L)_{ij}=\chi(i-j)\). Equation (2) gives

\[
(\Phi_p)_{I_L}^*(\Phi_p)_{I_L}-I=p^{-1/2}T_L.
\]

Since \(\chi(-h)=\chi(h)\), this is a real symmetric Toeplitz matrix. Define its real trigonometric symbol

\[
F_L(\theta)=\sum_{h=-(L-1)}^{L-1}\chi(h)e(h\theta)
=2\operatorname{Re}\sum_{h=1}^{L-1}\chi(h)e(h\theta).
\]

For any \(z\in\mathbb C^L\), Fourier orthogonality gives exactly

\[
z^*T_Lz=\int_0^1 F_L(\theta)
\left|\sum_{j=0}^{L-1}z_j e(j\theta)\right|^2d\theta.
\]

Parseval therefore implies

\[
\|T_L\|\le\sup_{\theta\in\mathbb R}|F_L(\theta)|
\le2\sup_{\theta\in\mathbb R}
\left|\sum_{h=1}^{L-1}\chi(h)e(h\theta)\right|. \tag{3}
\]

The exact number-theoretic input is Heath-Brown–Pierce, **Theorem 1.4, arXiv:1404.1677v1, p.5**: for any fixed integer \(r\ge2\), any \(\eta>0\), and \(H<p^{1/2+1/(4(r-1))}\),

\[
\left|\sum_{A<n\le A+H}\chi(n)e(f(n))\right|
\ll_{r,\eta} H^{1-1/r}p^{1/(4(r-1))+\eta}, \tag{4}
\]

for real linear \(f\), uniformly in the starting point and coefficients. The implicit constant does not depend on \(f\); equivalently the paper's method bounds a supremum over such phases. The zero-slope case follows also by continuity. The degree-1 case is unconditional; it does not require the conjecture stated for higher-degree phases in that paper.

Take \(r=3\), \(A=0\), \(H=L-1\), and \(f(n)=n\theta\). Equations (3)–(4) give, whenever \(L-1<p^{5/8}\),

\[
\left\|(\Phi_p)_{I_L}^*(\Phi_p)_{I_L}-I\right\|
\ll_\eta L^{2/3}p^{-3/8+\eta}. \tag{5}
\]

Now set \(L=L_p\) and \(\eta=\rho/3\). The length restriction holds because \(9/16-\rho<5/8\). The exponent on the right of (5) is

\[
\tfrac23(\tfrac9{16}-\rho)-\tfrac38+\tfrac\rho3
=-\tfrac\rho3.
\]

Adjoining the special column gives the block Gram deviation

\[
\Psi_p^*\Psi_p-I=
\begin{pmatrix}p^{-1/2}T_{L_p}&p^{-1/2}\mathbf1\\
p^{-1/2}\mathbf1^T&0\end{pmatrix}.
\]

The off-block matrix has norm \(\sqrt{L_p/p}\). The triangle inequality proves (1). In particular, the second term is
\(O(p^{-7/32-\rho/2})\), so both terms tend to zero.

Every Gram deviation on \(S\subseteq D_p\) is a principal compression of this matrix. Writing the bound in (1) as \(E_p=o(1)\), all its eigenvalues lie in \([1-E_p,1+E_p]\). Hence, for sufficiently large \(p\),

\[
\kappa_2((\Phi_p)_S)
\le\sqrt{\frac{1+E_p}{1-E_p}}=1+o(1),
\]

uniformly in \(S\). Eventually \(E_p\le1/2\), giving the explicit uniform condition bound \(\sqrt3\). Finally \(p^{1/2+\varepsilon}=o(L_p)\) for the claimed range of \(\varepsilon\), so those subset sizes fit inside the dictionary. This proves the theorem.

The same proof covers finite column labels in any affine progression \(a+dI_L\), \(d\ne0\), with the special column optionally included: its finite Gram deviation is \(\chi(d)p^{-1/2}T_L\). This gives a structured family of beyond-square-root supports in the full ETF.

## What the November 2026 method gives for Paley

### (a) Its hypothesis fails for every sufficiently large support

For any \(s\)-element subset of Paley ETF columns, including subsets containing \(\infty\), equation (2) gives the exact identity

\[
|G_S-I|=p^{-1/2}(J_s-I_s),\qquad
\big\||G_S-I|\big\|=(s-1)/\sqrt p. \tag{6}
\]

Thus Kümmerle–Mixon's bound through \(\Delta_s=\max_{|S|\le s}\||G_S-I|\|\) cannot certify \(\delta_s<1\) once \(s>1+\sqrt p\). For \(s\asymp p^{1/2+\varepsilon}\), (6) diverges. This is an obstruction to that estimate, not a growing actual condition number.

The threshold graph makes the failure particularly explicit. The coherence is \(\mu=p^{-1/2}\). If the threshold \(\nu<\mu\), the large-entry support graph is \(K_s\). For its hereditary density requirement

\[
e(U)\le c|U|^{3/2},
\]

a set \(U\) of size \(u\) fails exactly when

\[
u(u-1)/2>cu^{3/2}.
\]

In particular, applying it to \(U=S\) forces \(c\ge(s-1)/(2\sqrt s)\); there is no uniform bounded density constant. If \(\nu\ge\mu\), all entries go into the small-entry part and its row-sum estimate is again \((s-1)/\sqrt p\). Excluding a family of Paley cliques, or any other exceptional supports, leaves identity (6) unchanged for every remaining support.

Kümmerle–Mixon's useful two magnitudes are approximately \(m^{-1/3}\) on a sparse graph and \(m^{-2/3}\) elsewhere. Its graph is the elliptic affine polar graph \(VO^-_4(q)\), \(q\equiv3\pmod4\), with \(m=(q-1)(q^2+1)\); the chosen norm-graph subframe has \(n=\lfloor\log q\rfloor q^3\) columns and \(k=\lfloor q^2/(\log q)^6\rfloor\). The avoided configurations are isotropic lines and complementary conics. There is no direct Paley counterpart to import here.

Logarithmic cliques are not an RIP counterexample. On a Paley clique of size \(t\), the finite Gram eigenvalues are \(1+(t-1)/\sqrt p\) and \(1-1/\sqrt p\). On an independent set they are \(1-(t-1)/\sqrt p\) and \(1+1/\sqrt p\). For \(t=O(\log p)\), both kinds have condition tending to 1. The absolute-value threshold graph remains complete even on an independent set. These are different graphs and different obstructions.

### Signed estimates: what is proved and what remains missing

Weil-type complete sums and the identity for the full quadratic-character convolution give its operator norm \(\sqrt p\). For arbitrary masks this only yields

\[
\left|\sum_{i\in I,j\in J}\chi(i-j)\right|
\le\sqrt{p|I||J|}.
\]

After normalization by \(\sqrt p\), this gives no small flat-RIP constant. A Burgess estimate over an interval cannot be substituted for a sum over arbitrary masks \(I,J\). The Toeplitz proof above succeeds because the support is contained in an arithmetic progression; its arbitrary coefficient vectors are handled by the Fourier integral rather than by applying Burgess to those coefficients.

For comparison, a precise sufficient statement for the full ETF is: fix \(\alpha<1/2\), \(\beta>0\), and suppose that for all disjoint finite \(I,J\) with \(p^\alpha<|I|,|J|\le k\),

\[
\left|\sum_{i\in I,j\in J}\chi(i-j)\right|
\le p^{-\beta}|I||J|. \tag{7}
\]

Set \(k=\lfloor p^{1/2+\varepsilon}\rfloor\), with
\(0<\varepsilon<\min\{\beta,1/2-\alpha\}\). If either set is small, the trivial bound gives normalized flat correlation at most
\(p^{-(1/2-\alpha-\varepsilon)/2}\). If both are large, (7) gives at most \(p^{\varepsilon-\beta}\). A set containing \(\infty\) adds at most \(\sqrt{k/p}\). BMM Proposition 3.2 therefore yields

\[
\delta_k\le150\log k\left(
\max\{p^{\varepsilon-\beta},
p^{-(1/2-\alpha-\varepsilon)/2}\}+\sqrt{k/p}\right)=o(1). \tag{8}
\]

This proves the stated sufficient reduction. Satake's named Paley graph discrepancy Conjecture 7 supplies (7); it is unproved. The established BMM/Satake conditional results are not new progress from this attempt. No uniform signed bound (7) for arbitrary beyond-square-root supports is proved here.

### (b) Sub-dictionaries

Equation (6) applies to every column sub-dictionary, irrespective of its size, so the Kümmerle–Mixon absolute-value argument still stops at square-root sparsity. The signed argument proves the explicit \(p^{9/16-\rho}\)-column result above. A positive fraction, or a sub-dictionary of size \(p^{1-o(1)}\), is not obtained.

### (c) Counterexample search

No family with diverging actual condition number was constructed. The divergence in (6) concerns an upper bound with the signs removed. BFMW Lemma 22 already ensures each fixed-prime restriction with at most \(M_p\) columns is nonsingular and has \(\delta_s<1\); its gap may depend on \(p\), which is exactly why it does not settle the conjecture.

## Checks, reproducibility, and limits

The proof is analytic and uses the published mixed Burgess theorem. Its load-bearing details were separately checked: the Gram normalization and Gauss-sum sign; uniformity in the real phase in Theorem 1.4; unconditionality for degree 1; the length restriction \(9/16-\rho<5/8\); the exponent arithmetic; the special-column border; and compression to every subset. No formal proof assistant or independent human verification is claimed.

`code/check_paley.py` uses one numerical thread, inherited nice **20** (at least the requested 10), and about **36.1 MB** peak resident memory. It tests primes **101, 257, 509, 1009, 2017**. It checks the Gram matrix in two ways, directly from Fourier columns and from Legendre symbols, with maximum error below \(2.5\cdot10^{-14}\). It also checks the conference identity exactly at the two smallest primes, affine-progression transformations, compression inequalities, the exact absolute-value norm, and the Toeplitz Fourier-integral identity by exact-degree quadrature up to rounding error. A separate finite circulant embedding supplies a numerical upper bound on the Toeplitz norm. Exact rational arithmetic rechecks the exponents.

For \(\rho=1/32\), the whole finite interval dictionaries gave:

| \(p\) | \(L_p\) | \(\|G-I\|\) | Condition, finite interval | Condition, with \(\infty\) |
|---:|---:|---:|---:|---:|
| 101 | 11 | 0.616772 | 1.723065 | 1.737518 |
| 257 | 19 | 0.445302 | 1.579187 | 1.579187 |
| 509 | 27 | 0.492722 | 1.705387 | 1.705950 |
| 1009 | 39 | 0.683029 | 1.543732 | 1.567312 |
| 2017 | 56 | 0.429211 | 1.494500 | 1.523358 |

These small values neither test the asymptotic implied constant in Burgess nor establish a monotone trend. The guarantee comes from (1).

The exploratory search used \(k=\lfloor p^{0.55}\rfloor\) and \(\lfloor p^{0.60}\rfloor\), three seeds (interval, random, greedy-clique padded), and 40 random swap proposals per seed, accepting increases in condition number. The largest observed condition was approximately **2.52018**, at \(p=101,k=15\). This bounded local search is evidence only; it is not exhaustive and gives no asymptotic lower or upper bound.

`code/audit_artifacts.py` independently reconstructed all ten saved search witnesses as Fourier column matrices and compared their singular values with the character-Gram eigenvalues. The maximum disagreement was below \(1.7\cdot10^{-14}\). It verified all 22 retained source-text hashes, checked that the report's math delimiters balance, and confirmed that no PDF or page-image files exist. The audit used one thread, nice 20, and about 37.6 MB peak RSS; results are in `data/audit.json`. `data/source_index.json` records extracted titles, authors, version histories, and page counts.

Reproduce with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/check_paley.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/audit_artifacts.py
```

Artifacts: `data/interval_checks.csv`, `data/search_results.json` (including selected column indices), `data/verification.json`, `data/source_manifest.jsonl`, `LOG.md`, and the plain-text source corpus. The source scripts convert PDF response bodies in memory; no PDFs, scans, or page images are stored. Work remained in this directory, with no publication or pushes and no subagents.

Task: “Open problem I0103” — received 13 November 2026, 21:34 +04.
