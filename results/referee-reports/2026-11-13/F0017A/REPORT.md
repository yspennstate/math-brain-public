PARTIAL

# F0017: diagonal sign resilience of a random sign matrix

Task: “Open problem F0017” — 2026-11-13, approximately 08:25 Asia/Tbilisi.

No verified resolution of Vu's full conjecture was located in the literature search. The result proved here is resilience against every switching of at most \(cn\) diagonal entries, for each fixed \(c<1/2\), with exponentially high probability. It is a direct consequence of Tikhomirov's theorem, not a claimed new advance. The full conjecture, and even a positive constant asymptotic lower bound for full stubbornness, are not proved here.

## Statement and source

Let \(M_n\) have independent uniform entries in \(\{-1,1\}\). Write \(M^{(S)}\) for the matrix with the signs at positions \((i,i)\), \(i\in S\), switched. The matrix is **stubborn** when

\[
\det M^{(S)}\ne0\quad\text{for every }S\subseteq[n].
\]

Vu's Conjecture 11.6 asserts \(\Pr(M_n\text{ stubborn})=1-o(1)\). The precise source is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys **18** (2021), 179–200, DOI [10.1214/20-PS346](https://doi.org/10.1214/20-PS346), Section 11, printed p.195; arXiv:2005.02797v1, PDF p.17. The complete arXiv text, with PDF page markers, is in [sources/vu_2005.02797.txt](sources/vu_2005.02797.txt). Section 11 begins on PDF p.16 and was read in full. Its earlier questions concern irreducibility, spectral identification, and real eigenvalues. Its last two conjectures concern rank resilience and stubbornness.

The adjacent Conjecture 11.5 asks whether the minimum number \(\operatorname{Res}(M_n)\) of sign changes **anywhere** needed to make the matrix singular is \((1/2+o(1))n\), with high probability. For \(n\ge2\), there is a deterministic upper bound \(\operatorname{Res}(M)\le\lfloor n/2\rfloor\): if two rows differ in \(d\) coordinates, changing the first row into the second or its negative costs \(\min(d,n-d)\) changes. This also explains the survey's stated asymptotic upper bound. The rectangular result of Ferber–Luh–McKinley, Theorem 1.2, does not settle the square-matrix question; see the literature table below.

## Complete partial proofs

Throughout, logarithms are natural. We use the established theorem

\[
p_n:=\Pr(\det M_n=0)=\exp(-n\log2+o(n)), \tag{1}
\]

from Tikhomirov, Theorem A and its specialization on pp.593–594. No later preprint is needed for any deduction below.

### 1. Every sufficiently small deterministic family of switches

**Proposition.** If \(\mathcal F_n\subseteq2^{[n]}\) is deterministic and
\(\log|\mathcal F_n|\le(\log2-\delta)n\), for some fixed \(\delta>0\), then

\[
\Pr(\exists S\in\mathcal F_n:\det M_n^{(S)}=0)
\le \exp(-\delta n+o(n)). \tag{2}
\]

**Proof.** For any fixed \(S\), switching those entries is a bijection of the uniform sign-matrix space. Thus \(M_n^{(S)}\) has the same law as \(M_n\). The union bound gives \(|\mathcal F_n|p_n\), which is at most the right side of (2) by (1). There is no independence assumption between switchings. ∎

**Corollary: all switchings of at most \(cn\) entries, for any fixed \(0<c<1/2\).** Put \(h(c)=-c\log c-(1-c)\log(1-c)\). Then

\[
\Pr\bigl(\exists S,\ |S|\le\lfloor cn\rfloor:\det M_n^{(S)}=0\bigr)
\le \exp\{-[\log2-h(c)]n+o(n)\}=o(1). \tag{3}
\]

**Proof of the counting bound.** For \(j\le cn\),
\(c^j(1-c)^{n-j}\ge c^{cn}(1-c)^{(1-c)n}=e^{-nh(c)}\), since \(c/(1-c)<1\). The binomial theorem therefore implies

\[
1\ge\sum_{j\le\lfloor cn\rfloor}\binom nj c^j(1-c)^{n-j}
\ge e^{-nh(c)}\sum_{j\le\lfloor cn\rfloor}\binom nj.
\]

Apply (2), and use \(h(c)<\log2\). This includes every sequence \(k=o(n)\), by inclusion in any one fixed such ball for all sufficiently large \(n\). ∎

**Corollary: any prescribed \((1-\varepsilon)n\) diagonal positions.** For a deterministic \(T_n\subseteq[n]\) with \(|T_n|\le(1-\varepsilon)n\), all \(2^{|T_n|}\) switchings supported on \(T_n\) are nonsingular with failure probability at most \(\exp(-\varepsilon n\log2+o(n))\). This follows from (2). It is uniform in the choice of deterministic \(T_n\); it does not permit choosing \(T_n\) after seeing the matrix.

**Global rank-resilience lower bound.** For each fixed \(0<\delta<\log2\), with probability tending to one,

\[
\operatorname{Res}(M_n)>\left\lfloor\frac{(\log2-\delta)n}{\log n}\right\rfloor. \tag{4}
\]

**Proof.** Let the integer on the right be \(K\). A family of changes at at most \(K\) of the \(n^2\) positions has size at most \((K+1)(en^2/K)^K\) for large \(n\), using \(\binom{N}{j}\le(eN/j)^j\) and monotonicity up to \(K\). Its logarithm is \((\log2-\delta)n+o(n)\). Each fixed set of changes preserves the matrix law. Union bounding with (1) gives failure probability \(\exp(-\delta n+o(n))\). The elementary binomial bound follows from \(j!\ge(j/e)^j\), itself obtained by integrating \(\log x\) from 1 to \(j\). ∎

### 2. The polynomial and the actual missing estimate

Let \(A\) be the off-diagonal part of \(M_n\), with zero diagonal. For an absolute diagonal assignment \(x\in\{-1,1\}^n\), define

\[
P_A(x)=\det(A+\operatorname{diag}x)
=\sum_{S\subseteq[n]}\det A[S^c,S^c]\prod_{i\in S}x_i. \tag{5}
\]

The determinant of the empty matrix is 1. In particular the top coefficient is 1, coefficients of degree \(n-1\) vanish, and the other coefficients are strongly dependent principal minors. To verify (5), expand the determinant over permutations: choosing diagonal variables at indices \(S\) fixes those indices in the permutation; the remaining signed sum is exactly the principal determinant on \(S^c\). No additional sign occurs for those fixed points.

Let

\[
Z(A)=\#\{x:P_A(x)=0\},\qquad q_A(0)=2^{-n}Z(A).
\]

Stubbornness depends only on \(A\), not on the original diagonal, and is exactly \(Z(A)=0\). Also

\[
\mathbb E_A Z(A)=2^n p_n,\qquad
\mathbb E_A q_A(0)=p_n. \tag{6}
\]

Indeed a fresh independent uniform diagonal, combined with \(A\), is a uniform sign matrix. Equation (1) makes the naive first-moment bound only \(\exp(o(n))\), not a quantity known to tend to zero.

A sufficient random-coefficient polynomial Littlewood–Offord theorem would say, for some deterministic \(b_n<2^{-n}\),

\[
\Pr_A\{q_A(0)\le b_n\}=1-o(1). \tag{7}
\]

Because \(q_A(0)\) is a multiple of \(2^{-n}\), (7) forces it to be zero. Thus this is a *typical-coefficient*, target-zero statement at the lattice spacing of the entire Boolean cube. It is not a usual polynomially small small-ball estimate. An averaged bound \(\mathbb E_Aq_A(0)=o(2^{-n})\) would be sufficient but is false, as the next proposition shows. Nor can one ask for \(\sup_t q_A(t)<2^{-n}\): every function on a \(2^n\)-point space has some atom of at least \(2^{-n}\).

A potentially less circular sufficient estimate would identify an exceptional off-diagonal event \(B_n\) and prove

\[
\Pr(B_n)=o(1),\qquad \mathbb E[Z(A)\mathbf1_{B_n^c}]=o(1). \tag{8}
\]

Markov's inequality then proves the conjecture. Merely deleting proportional-pair obstructions and citing a sharp scalar singularity asymptotic does not establish the second part of (8).

For completeness, (5) gives the exact Fourier identities

\[
\sum_x P_A(x)=2^n\det A,\qquad
\sum_x P_A(x)\prod_i x_i=2^n. \tag{9}
\]

These follow by summing each monomial: every nonconstant character has zero sum. In particular at least one completion is nonsingular for every \(A\). Both identities are checked in every computational enumeration below.

### 3. Structured failures and the clustering obstruction

**Proposition.** Let \(n\ge3\), \(N=2\binom n2=n(n-1)\). There is an event \(B_n\) consisting of diagonal-repairable proportional row or column pairs such that

\[
N2^{3-n}-\binom N2 2^{10-2n}
\le\Pr(B_n)\le N2^{3-n}. \tag{10}
\]

Every \(A\in B_n\) has \(Z(A)\ge2^{n-2}\). Consequently

\[
\Pr(M_n\text{ not stubborn})\ge(8+o(1))n^2 2^{-n},\qquad
\mathbb E Z(A)\ge(2-o(1))n^2. \tag{11}
\]

**Proof.** For a row pair \(i,j\), let \(E^r_{ij}\) assert that for some \(s\in\{-1,1\}\),
\(a_{ik}=s a_{jk}\) for every \(k\notin\{i,j\}\). For each fixed \(s\), these are \(n-2\) independent fair constraints. The two signs give disjoint events when \(n\ge3\), so \(\Pr(E^r_{ij})=2^{3-n}\). On this event set
\(x_i=s a_{ji}\), \(x_j=s a_{ij}\). The two completed rows are proportional, irrespective of the other \(n-2\) diagonal signs. This supplies \(2^{n-2}\) distinct singular completions. Define \(E^c_{ij}\) by transposition and let \(B_n\) be the union of these \(N\) events.

For the intersection of two distinct row-pair events, fix their two proportionality signs and discard all columns in the union of their row indices, at most four columns. In each remaining column, the two constraints have probability \(1/4\): the graph of two distinct edges on the row indices is a forest with two edges, whether the edges are disjoint or meet. Columns are independent. Thus the fixed-sign intersection has probability at most \(2^{-2(n-4)}\). Sum over four sign pairs to get at most \(2^{10-2n}\). This bound also holds for two column-pair events by transposition; if \(n<4\), its right side exceeds 1 and is still valid.

For a row-pair event with rows \(i,j\) and a column-pair event with columns \(p,q\), retain the row constraints only in columns outside \(\{i,j,p,q\}\). There are at least \(n-4\) such constraints. They use no entries in columns \(p,q\). All \(n-2\) column constraints use entries in those two columns and are independent of the retained row constraints. For each fixed sign pair the probability is at most \(2^{-(2n-6)}\) when \(n\ge4\); summing over four sign pairs is bounded by \(2^{10-2n}\). Small \(n\) again follows trivially. This covers every distinct event pair.

The union bound and the first two Bonferroni terms prove (10). Its error is \(O(n^4 4^{-n})=o(n^2 2^{-n})\). Since \(B_n\) implies nonstubbornness and \(Z\ge2^{n-2}\) on \(B_n\), (11) follows. ∎

This proposed counterexample mechanism therefore has vanishing probability; its second moment does not disprove the conjecture. It explains why a large expected number of zero determinants is compatible with almost-sure eventual stubbornness. It also shows directly that the averaged strengthening following (7) is impossible. We do not prove that these pairs dominate all failures.

**A sufficient scalar-singularity strengthening.** Let \(F_n\) be the event that a uniform sign matrix is singular and has no two proportional rows or columns. If one could prove

\[
\Pr(F_n)=o(2^{-n}), \tag{13}
\]

then the full stubbornness conjecture would follow. In particular any bound \((1/2-\eta)^n\), for fixed \(\eta>0\), would suffice.

**Proof of this reduction.** If \(A\notin B_n\), none of its diagonal completions has two proportional rows or columns: such a pair would imply one of the off-diagonal events defining \(B_n\). Therefore

\[
\mathbb E[Z(A)\mathbf1_{B_n^c}]
=2^n\Pr(\det M_n=0,\ A\notin B_n)
\le2^n\Pr(F_n).
\]

Apply (8), using \(\Pr(B_n)=o(1)\) from (10). ∎

This distinguishes the missing estimate from a sharp leading asymptotic for \(p_n\): a remaining error \(o(n^2 2^{-n})\), or even \(O(n^{1+\varepsilon}2^{-n})\), need not be \(o(2^{-n})\). We do not establish (13).

### 4. Uniform exclusion of small-support kernel vectors

An elementary bound also removes a larger class of structured failures, simultaneously over the *entire* diagonal cube. Fix \(0<\alpha<1/2\) such that
\(h(\alpha)+2\alpha\log2<\log2\). With probability \(1-o(1)\), no diagonal completion has a nonzero right or left kernel vector supported on at most \(\alpha n\) coordinates. For example, \(\alpha=0.16\) is admissible. This is a standard rectangular-rank argument, included for its direct relevance rather than as a novelty claim.

**Proof.** A \(d\)-dimensional subspace of \(\mathbb R^m\) contains at most \(2^d\) sign vectors. Indeed, some \(d\) coordinate functionals restrict to a basis of its dual, giving an injective projection into \(\mathbb R^d\); sign vectors project into a set of size \(2^d\).

For a fixed support \(S\), \(|S|=s\le n/2\), a right kernel vector of a completed matrix, supported in \(S\), must lie in the kernel of the unchanged rectangular block \(A[S^c,S]\). Its \(s\) columns are independent uniform sign vectors in dimension \(m=n-s\). Exposing these columns, the chance the \(j\)-th lies in the span of the preceding columns is at most \(2^{j-1-m}\), by the subspace fact. Thus

\[
\Pr\{\operatorname{rank}A[S^c,S]<s\}
\le\sum_{j=1}^s2^{j-1-(n-s)}<2^{2s-n}.
\]

Union bounding over all \(S\) of size at most \(\alpha n\), using the entropy bound proved above, gives at most
\(\exp\{n[h(\alpha)+2\alpha\log2-\log2]\}\), which tends to zero exponentially. The same proof after transposition handles left kernel vectors; adding the two probabilities preserves exponential decay. The argument never fixes or counts diagonal assignments, since the rectangular blocks avoid the diagonal. ∎

The numerical boundary for this elementary argument is approximately \(\alpha=0.1705\). Excluding sparse kernel vectors leaves potential dependencies on a linear number of coordinates; those remain uncontrolled here.

## What polynomial anti-concentration currently supplies

Razborov–Viola, *Real Advantage*, Theorem 3.3, PDF p.4 in the saved June 3, 2013 version, give a point-mass bound \(O_d(r^{-1/(d2^{d+1})})\) when a degree-\(d\) multilinear polynomial has \(r\) disjoint nonzero degree-\(d\) monomials. The formulation uses \(\{0,1\}\) inputs; the affine change to signs preserves the relevant top-degree disjointness.

Meka–Nguyen–Vu, Theorem 1.6, arXiv:1507.00829v4, PDF p.2, give for rank \(r\ge2\) the bound

\[
\min\left\{\frac{B d^{4/3}\sqrt{\log r}}{r^{1/(4d+1)}},
\frac{\exp(Bd^2(\log\log r)^2)}{\sqrt r}\right\} \tag{12}
\]

for the probability of an interval of length 1, when the \(r\) disjoint top-degree coefficients have absolute value at least 1. For fixed degree the second expression is \(r^{-1/2+o(1)}\). The published version is Theory of Computing **12** (2016), Article 11, 1–17, DOI [10.4086/toc.2016.v012a011](https://doi.org/10.4086/toc.2016.v012a011); theorem locators here refer explicitly to the saved arXiv version.

For \(P_A\) in (5), the degree is \(n\) and there is exactly one monomial of that degree: its disjoint-monomial rank is 1. Thus (12) does not apply with useful rank, and the Razborov–Viola estimate is vacuous. Counting many lower-degree coefficients does not make them top-degree coefficients. After fixing all but \(m\) diagonal variables, the coefficient of their full product is the determinant of the complementary completed principal block. If it is nonzero, the restricted polynomial again has only one degree-\(m\) monomial; if it vanishes, separate structural analysis is required. Truncating terms changes the zero set and is not justified.

Kwan–Sauermann, *Resolution of the quadratic Littlewood–Offord problem*, Theorem 1.1, PDF p.3 of the saved December 21, 2023 version (arXiv:2312.13826), show \(\sup_z\Pr(Q=z)\le C/\sqrt m\) if no assignment of fewer than \(m\) variables fixes the value of a quadratic polynomial. This is an essentially optimal degree-two result, published online in Compositio Mathematica on March 30, 2026. It does not handle the degree-\(n\) determinant polynomial. Restricting (5) to two variables only gives a fixed-size quadratic problem, and polynomial bounds on one sampled diagonal fall far short of (7).

Even an ideal fixed-degree bound \(O(r^{-1/2})\), with \(r\le n\), would not certify the absence of all \(2^n\) zeros. The dependence and the rare large clusters have to be used, rather than treating the switchings separately.

## Literature audit

All page numbers below are PDF page numbers in the retained text unless explicitly labeled printed pages. Version differences matter; exact locators refer to the saved versions, whose URLs and hashes are recorded in [sources/manifest.jsonl](sources/manifest.jsonl). Full text is retained only as plain text. The web search terms, failures to access mirrors, and limits of the negative search are recorded in [sources/search_log.txt](sources/search_log.txt).

| Work | Checked locator and result | Relevance and limitation |
|---|---|---|
| Bourgain–Vu–Wood, *On the singularity probability of discrete random matrices*, J. Funct. Anal. **258** (2010), 559–603; [arXiv:0905.0461](https://arxiv.org/abs/0905.0461) | Theorem 2.2, p.7; sign-matrix specialization (2), p.2: \((1/\sqrt2+o(1))^n\). Theorem 1.4, p.5, concerns fixed initial rows. | Scalar singularity/fixed-row robustness, without a simultaneous adaptive diagonal guarantee. |
| Tikhomirov, *Singularity of random Bernoulli matrices*, Ann. Math. **191** (2020), 593–634; [journal](https://annals.math.princeton.edu/2020/191-2/p06) | Theorem A, printed pp.593–594, PDF pp.1–2; \(p_n=(1/2+o(1))^n\), including a least-singular-value statement. | Establishes (1) and therefore (2)–(4). Does not suffice for all \(2^n\) switchings. |
| Ferber–Luh–McKinley, *Resilience of the rank of random matrices*, Combin. Probab. Comput. **30** (2021), 163–174; [arXiv:1910.03619](https://arxiv.org/abs/1910.03619) | Theorem 1.2, p.2: for \(m\ge n+n^{1-\varepsilon/6}\), an \(n\times m\) sign matrix retains row rank after \((1-\varepsilon)m/2\) changes, a.a.s. | The partial result cited by Vu. The excess columns are essential to the stated hypothesis. It cannot be applied with \(m=n\). |
| Ferber–Jain–Luh–Samotij, *On the counting problem in inverse Littlewood–Offord theory*, J. London Math. Soc. **103** (2021), 1333–1362; [arXiv:1904.10425](https://arxiv.org/abs/1904.10425) | Counting theorem 1.7, p.5; applications Theorems 1.11, p.7, and 1.15, p.8, give stretched-exponential singularity bounds for signed regular and row-regular models. | Provides counting machinery used in rank resilience, not a stubbornness theorem. |
| Bandeira–Ferber–Kwan, *Resilience for the Littlewood–Offord problem*, Adv. Math. **319** (2017), 292–312; [arXiv:1609.08136](https://arxiv.org/abs/1609.08136) | Theorems 1.7–1.9, p.4: worst-case linear-sum resilience threshold \((1+o(1))\log_3\log n\); fixed-\(k\) failure probabilities. | Explicitly motivated by Vu's older matrix conjectures; the result concerns linear sums with fixed coefficients. |
| Jain–Sah–Sawhney, *Sharp invertibility of random Bernoulli matrices*; [arXiv:2010.06553](https://arxiv.org/abs/2010.06553) | Theorems 1.3 and 1.5, p.2: sharp biased Bernoulli singularity and \((1/2+o(1))^n\) for the central-slice row model. | Bias/slice results do not give adversarial diagonal uniformity for fair signs. |
| Jain–Sah–Sawhney, *Singularity of discrete random matrices*; [arXiv:2010.06554](https://arxiv.org/abs/2010.06554) | Theorem 1.2 and Corollary 1.3, p.2, for nonuniform finite-support laws; Theorem 1.4, p.2, for the general exponential rate. | The sharp nonuniform conclusion excludes the uniform sign law. No simultaneous diagonal statement. |
| Jain–Sah–Sawhney, *On the smallest singular value of symmetric random matrices*; [arXiv:2011.02344](https://arxiv.org/abs/2011.02344) | Theorems 1.1–1.2, p.2: \(C\varepsilon^{1/8}+2e^{-c\sqrt n}\), with a stronger logarithmic exponent for signs. | Symmetry is a different dependence structure; no adaptive diagonal guarantee here. |
| Campos–Jenssen–Michelen–Sahasrabudhe, *The singularity probability of a random symmetric matrix is exponentially small*, JAMS **38** (2025), 179–224; [arXiv:2105.11384](https://arxiv.org/abs/2105.11384) | Theorem 1.1, p.3 in saved arXiv version: \(e^{-cn}\) singularity bound. | A symmetric scalar-singularity theorem; the unspecified exponential constant does not overcome \(2^n\) choices. |
| Campos–Jenssen–Michelen–Sahasrabudhe, *The least singular value of a random symmetric matrix*, Forum Math. Pi **12** (2024), e3, 1–69; [DOI](https://doi.org/10.1017/fmp.2023.29) | Theorem 1.1, PDF p.3: \(C\varepsilon+e^{-cn}\) for subgaussian symmetric matrices; Theorem 1.2 on the same page concerns simple spectrum. | Stronger small-ball dependence on \(\varepsilon\), still a scalar result in the symmetric ensemble. |
| Jain–Sah–Sawhney, *The smallest singular value of dense random regular digraphs*; [arXiv:2008.04755](https://arxiv.org/abs/2008.04755) | Theorem 1.1, p.1: \(C_\lambda\kappa\sqrt n+2e^{-c_\lambda n}\) when \(\min(d,n-d)\ge\lambda n\). | Uniform regular digraphs with fixed degree constraints; this is a different model and perturbation question. |
| Ferber–Kwan–Sauermann, *Singularity of sparse random matrices: simple proofs*; [arXiv:2011.01291](https://arxiv.org/abs/2011.01291) | Theorems 1.1–1.2, p.1: nonsingularity above the \((1+\varepsilon)\log n\) sparsity threshold for independent Bernoulli and independent fixed-weight rows. | Checks the sparse-matrix direction of the search. Sparsity thresholds do not give diagonal sign resilience. |
| Nguyen–Vu, *Random matrices: Law of the determinant*, Ann. Probab. **42** (2014), 146–167; [arXiv:1112.0752](https://arxiv.org/abs/1112.0752) | Main Theorem 1.1, PDF p.3 in the electronic reprint: central limit law for the logarithm of the determinant, with rate \(\log^{-1/3+o(1)}n\). | A typical-size/logarithmic law does not estimate the exponentially rare zero event required here. |
| Hunter–Kwan–Sauermann, *Exponential anticoncentration of the permanent* (2025 preprint); [arXiv:2509.22577](https://arxiv.org/abs/2509.22577) | Theorems 1.1–1.2, pp.1–2: \(e^{-c n}\) point-mass bounds, extending to independent uniformly anticoncentrated entries. | The proof also works for determinants, but this is a scalar estimate with all-entry randomness, not (7). |
| Aigner-Horev–Rosenberg–Weiss, *Resilience of Rademacher chaos of low degree*, [arXiv:2402.10504](https://arxiv.org/abs/2402.10504), updated 2025 | Theorem 1.2, printed/PDF p.5, Corollary 1.3, p.6, and higher-order Theorem 1.7. | Instance-dependent low-degree chaos resilience bounds do not cover degree \(n\), rank-one top monomial, or all diagonal choices. |
| Hu–Song–Wu, *Sharp singularity asymptotics for discrete random matrices*, [arXiv:2609.39463v2](https://arxiv.org/abs/2609.39463v2), October 16, 2026 preprint | Theorem 1.1 and Corollary 1.2, p.2, claim \(p_n=(2+o(1))n^2 2^{-n}\), with additive \(O_\varepsilon(n^{1+\varepsilon}2^{-n})\) error. | Later primary preprint located and read; not independently proof-audited here and not used in our proofs. Even this sharper scalar asymptotic yields \(\mathbb EZ\sim2n^2\), not \(\Pr(Z>0)=o(1)\). |

The polynomial results of Meka–Nguyen–Vu, Razborov–Viola, and Kwan–Sauermann are detailed above. Searches covered the specified names, 2021–2026, “stubborn”, “diagonal resilience”, and the exact conjecture number. No verified resolution was found. This conclusion is limited by search indexing; it is not a certificate that all citing papers have been checked. The same question already appeared under the adjective “good” in Vu's 2006 survey, Conjecture 7.5.

## Computation

The main runs evaluated **4,293,332,502 exact integer determinants**: 33,620,502 across exhaustive representatives for \(n\le6\), and 4,259,712,000 across 12,100 independently seeded off-diagonal samples at every size \(7\le n\le24\). Every sample's entire diagonal cube was enumerated. Runs continued through all completions after finding zeros, so the recorded \(Z\) is the full count, not a stopping-time estimate. Validation reruns are additional to these totals.

### Why the exhaustive quotient is exact

Multiplication by diagonal sign matrices on the left and right preserves \(Z\): it multiplies determinants by a fixed nonzero sign and permutes the diagonal assignments by \(x_i\mapsto r_i c_i x_i\). For \(n\ge3\), view off-diagonal positions as edges of the connected bipartite graph \(K_{n,n}\) with its diagonal matching removed. Normalize these spanning-tree entries to +1:

\[
(1,j)\ (j>1),\qquad(i,1)\ (i>1),\qquad(2,3).
\]

There are \(2n-1\) such edges. To see they form a tree, the first two groups are two disjoint stars covering all row and column vertices, and the last edge joins them. Vertex sign choices normalize each edge successively along the tree and are unique up to reversing every vertex sign. Hence every orbit of off-diagonal assignments has exactly \(2^{2n-1}\) elements and exactly one normalized representative. The remaining \(n(n-1)-(2n-1)=n^2-3n+1\) edge signs are free and equiprobable. Thus the representative counts for \(n=3,4,5,6\) are \(2,32,2048,524288\), and averaging their histograms gives exactly the original uniform-matrix probability, including all possible original diagonals. The cases \(n=1,2\) are handled directly.

### Exact arithmetic and verification

[code/enumerate.cpp](code/enumerate.cpp) evaluates the multilinear determinant polynomial by branching on remaining diagonal signs and taking Schur complements over the prime field with
\(p=2^{61}-1\). For an invertible pivot block \(B\), block elimination gives
\(\det\begin{pmatrix}B&C\\D&E\end{pmatrix}=\det B\det(E-DB^{-1}C)\): multiply on the left by the block lower triangular matrix with blocks \(I,0,-DB^{-1},I\), which has determinant 1. The algorithm uses one-variable pivots, branches on an additional diagonal variable for a usable two-variable pivot when needed, and falls back to ordinary row-pivoting elimination on a degenerate branch. Direct formulas terminate at at most three remaining variables. At each branch only previously unassigned variables are fixed, so each absolute diagonal assignment occurs once.

The output is the actual signed integer determinant: Hadamard's inequality gives
\(|\det M|\le n^{n/2}\), and for every \(n\le24\),

\[
2n^{n/2}<p.
\]

In particular \(24^{12}=36{,}520{,}347{,}436{,}056{,}576\), whereas
\(\lfloor p/2\rfloor=1{,}152{,}921{,}504{,}606{,}846{,}975\).
The centered field residue therefore uniquely determines the integer. Zero modulo \(p\) is exactly zero over the integers here. Modular products use unsigned 128-bit integers, sufficient for products below \(p^2<2^{122}\). The Hadamard comparisons were also checked using integer squares, and the prime was checked with the 59-step Lucas–Lehmer test for exponent 61; see [data/arithmetic_checks.json](data/arithmetic_checks.json).

The checks were:

- Every enumerated off-diagonal matrix passed the visit count \(2^n\) and both exact Fourier identities (9).
- Independent arbitrary-precision Python Bareiss elimination matched 6,120 individual determinants across sizes 1–8; 96 random row/column-sign invariance checks passed. Full unreduced off-diagonal spaces at sizes 1–4 matched the symmetry quotient. See [data/validation.json](data/validation.json).
- A second C++ program, [code/integer_fourier.cpp](code/integer_fourier.cpp), expanded the determinant over all permutations to obtain its integer multilinear coefficients, then evaluated them by the Walsh transform. It uses no finite fields or elimination. It independently reproduced the **entire histogram at every size through 6**, including the 524,288 size-six representatives; see [data/independent_fourier_audit.json](data/independent_fourier_audit.json).
- Fifteen saved matrices at sizes 12,16,20,23,24 were re-enumerated. Counts, ranges and Fourier sums reproduced exactly, and an explicit zero and nonzero completion for each was checked by Python Bareiss elimination. See [data/large_witness_audit.json](data/large_witness_audit.json).

The runs used one computational thread at nice 10, about 444 seconds of timed main experiments on this machine. The large-cube algorithm retains fixed-size recursion matrices and aggregates, without a \(2^n\) array. The measured largest re-enumeration child peak RSS was 1,556,480 bytes (macOS units); the Python source-processing and analysis tasks were also small. The sandbox rejects OS address-space-limit calls, so no enforcement claim is made about the initially attempted limit. Memory stays under 4 GB by the bounded allocations and measured footprint. All work remained in this directory. No publication or pushes occurred.

### Results and distribution

The exact stubbornness probabilities through size six are

\[
1,\quad0,\quad0,\quad\frac1{32},\quad\frac3{256},\quad\frac{2845}{262144}.
\]

The table reports full-cube zero counts \(Z\). Confidence intervals use the number of independent off-diagonal samples, not the \(2^n\) dependent diagonal assignments. The 10% and 90% quantiles are interpolated between ordered observations. Full discrete histograms at every size are in [data/distributions.json](data/distributions.json), exact representative histograms in `data/exhaustive_*.json`, and each sampled matrix with its count in `data/monte_*.jsonl`. Summaries are available as [CSV](data/summary.csv) and [JSON](data/summary.json).

| n | matrices / representatives | stubborn | probability (95% Wilson for samples) | median Z | mean Z | 10%–90% Z |
|---:|---:|---:|---|---:|---:|---|
| 1 | 1 | 1 | 1.000000 exact | 0 | 0.000 | 0–0 |
| 2 | 1 | 0 | 0.000000 exact | 2 | 2.000 | 2–2 |
| 3 | 2 | 0 | 0.000000 exact | 5 | 5.000 | 4.2–5.8 |
| 4 | 32 | 1 | 0.031250 exact | 10.5 | 10.562 | 7.3–12 |
| 5 | 2,048 | 24 | 0.011719 exact | 22 | 20.984 | 14–26 |
| 6 | 524,288 | 5,690 | 0.010853 exact | 43 | 40.131 | 22–54 |
| 7 | 1,000 | 6 | 0.006000 [0.002753, 0.013028] | 77.5 | 73.617 | 37–103 |
| 8 | 1,000 | 5 | 0.005000 [0.002138, 0.011651] | 143 | 135.762 | 64–200 |
| 9 | 1,000 | 3 | 0.003000 [0.001021, 0.008783] | 226 | 226.907 | 95.9–359.1 |
| 10 | 1,000 | 5 | 0.005000 [0.002138, 0.011651] | 388 | 388.863 | 140.9–646 |
| 11 | 1,000 | 2 | 0.002000 [0.000549, 0.007263] | 569 | 618.884 | 197–1100.2 |
| 12 | 1,000 | 4 | 0.004000 [0.001557, 0.010240] | 772.5 | 898.734 | 235–1745.4 |
| 13 | 1,000 | 0 | 0.000000 [0.000000, 0.003827] | 1064 | 1334.568 | 356–2849.3 |
| 14 | 1,000 | 2 | 0.002000 [0.000549, 0.007263] | 1347 | 1897.192 | 438.7–4526 |
| 15 | 1,000 | 0 | 0.000000 [0.000000, 0.003827] | 1781.5 | 2482.372 | 522.8–4909 |
| 16 | 1,000 | 3 | 0.003000 [0.001021, 0.008783] | 2007.5 | 3165.574 | 609.5–6135.7 |
| 17 | 500 | 0 | 0.000000 [0.000000, 0.007624] | 2361.5 | 3953.430 | 731.9–7452 |
| 18 | 500 | 1 | 0.002000 [0.000353, 0.011241] | 2437 | 3826.898 | 660.9–7680.7 |
| 19 | 300 | 0 | 0.000000 [0.000000, 0.012643] | 2756.5 | 5080.647 | 600.7–9217.4 |
| 20 | 300 | 0 | 0.000000 [0.000000, 0.012643] | 2981 | 4217.347 | 929–8608 |
| 21 | 150 | 0 | 0.000000 [0.000000, 0.024970] | 2528.5 | 6802.267 | 806–6706.8 |
| 22 | 150 | 0 | 0.000000 [0.000000, 0.024970] | 2950 | 3823.400 | 743.8–7919.2 |
| 23 | 100 | 0 | 0.000000 [0.000000, 0.036993] | 2579.5 | 3272.910 | 569.6–7033.3 |
| 24 | 100 | 0 | 0.000000 [0.000000, 0.036993] | 2529 | 3316.120 | 578.2–6856.4 |

At size 24 there were no stubborn matrices among 100 samples; the 95% Wilson interval is [0, 0.036993]. Those samples had between 155 and 17,307 singular completions, with median 2,529. This is a finite-size observation, not a counterexample to an asymptotic conjecture.

Rare pairs visibly affect the count distribution. At size 21, one of 150 samples contained a repairable proportional pair and had 528,249 zero completions, at least the predicted \(2^{19}=524,288\). The sample mean is 6,802 while its median is 2,528.5. No repairable pair occurred in the samples at sizes 20,22,23,24, although all those sampled matrices still had singular completions. Thus these dimensions are far from a regime in which the pair mechanism explains all observed failures.

### Trend fits and their limits

An original vector plot is saved as [data/trend.svg](data/trend.svg). Two descriptive fits are recorded in [data/trend_fit.json](data/trend_fit.json).

For the median zero count over sizes 12–24, least squares gives

\[
\log\operatorname{median} Z_n
\approx -1.79943+1.54432n-\tfrac12\log(n!). \tag{14}
\]

Its root-mean-square residual on the logarithmic scale is 0.0602. A 300-resample within-dimension bootstrap gives an approximate interval [1.5313,1.5559] for the fitted linear coefficient, conditional on this model. Since the fitted ratio between consecutive sizes is \(e^{1.54432}/\sqrt{n+1}\), this curve peaks at size 21. It describes the observed flattening and subsequent decrease in the median count.

The factorial term is a heuristic choice, not an established asymptotic law for these zeros. A sign determinant is divisible by \(2^{n-1}\) (subtract the first row from all others) and has a natural magnitude scale near \(\sqrt{n!}\). A smooth local-density heuristic would then suggest a count scale proportional to \(4^n/\sqrt{n!}\). The fitted coefficient in (14) is free, and differs from \(\log4=1.38629\). Neither a smooth conditional density nor a Poisson law for \(Z\) has been proved or assumed in the mathematical arguments.

A binomial logistic fit to the actual stubborn/nonstubborn indicators at sizes 7–24 gives

\[
\operatorname{logit}\widehat{\Pr}(\text{stubborn at }n)
=-6.05170-0.18716(n-12), \tag{15}
\]

from 31 stubborn matrices among 12,100 samples. The approximate 95% slope interval is [-0.2995,-0.0748]. Within the sampled range this points downward, and there is no measured rise of stubbornness toward 1. Extrapolating (15) would conflict with Vu's conjecture, but this finite-range fit has no justification outside its training dimensions. Conversely, extrapolating the decreasing count tail in (14) might suggest eventual disappearance of generic zeros, but medians and means do not determine the probability of any zero. These two descriptive fits do not decide the conjecture.

## What remains open after this work

The report proves (2)–(4), the clustered obstruction bounds (10)–(11), the sufficient reduction (13), and uniform exclusion of kernel vectors on at most \(0.16n\) coordinates. It does not prove full stubbornness, a positive constant limiting lower bound for it, or a counterexample. The unresolved step is control of the probability that the random-coefficient determinant polynomial has **any** zero on the full diagonal cube, accounting for rare off-diagonal configurations that create large clusters of zeros. The literature search located no verified theorem that supplies that control.

Reproduction commands, seeds, encodings and memory behavior are documented in [code/README.md](code/README.md). The progress record is [LOG.md](LOG.md).
