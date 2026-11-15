PARTIAL

# C0097: the inverse-dimension expansion of the SAW connective constant

The requested zero-radius statement for nearest-neighbour self-avoiding walk (SAW) on Z^d is **not proved here**. No published resolution was located in the literature search through 13 November 2026. Three related statements are proved below: divergence for the simple-random-walk Green and return-probability series; a positive radius for every fixed-memory walk; and a factorial lower bound for a diagonal family of one-loop lace coefficients. The first recovers a known spherical-model mechanism. No novelty is claimed for these partial results.

## 1. Statement and literature

Put s=1/(2d). Write the unique all-orders asymptotic expansion as

\[
 \mu(d)\sim s^{-1}+\sum_{k=0}^{\infty}a_k s^k.
\]

The target is

\[
 \limsup_{k\to\infty}|a_k|^{1/k}=\infty.
\]

An asymptotic expansion means that, for each fixed M, subtracting the terms through s^(M-1) leaves O(s^M) along positive integer dimensions. The error constant can depend on M. The finite pole s^-1 is irrelevant to the convergence question.

The requested passage is **Section 1.4**, not Section 1.5, of Bauerschmidt–Duminil-Copin–Goodman–Slade, arXiv:1206.2092, **pp. 4–5, equations (1.19)–(1.20)**. It credits Hara–Slade with the all-orders expansion, records the coefficients through power 11, and presents zero radius as unproved. [Source](https://arxiv.org/pdf/1206.2092).

The relevant literature and verified locators are:

| Reference | What it establishes; locator |
|---|---|
| T. Hara and G. Slade, *The self-avoiding-walk and percolation critical points in high dimensions*, Combin. Probab. Comput. **4** (1995), 197–215, DOI 10.1017/S0963548300001607 | All-orders integer-coefficient SAW expansion; inverse connective constant through d^-6 with O(d^-7) error; bond percolation through d^-3 with O(d^-4) error. The publisher abstract was checked. **The published full text and its theorem/page locator could not be obtained**, so no theorem number is asserted. The all-orders statement is also explicitly reproduced in the lecture source, pp. 4–5. [Publisher record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/selfavoidingwalk-and-percolation-critical-points-in-high-dimensions/34FE4DB4BC49D3718410598AF8B564EC). |
| N. Clisby, R. Liang and G. Slade, *Self-avoiding walk enumeration via the lace expansion*, J. Phys. A **40** (2007), 10973–11017, DOI 10.1088/1751-8113/40/36/003 | **Section 1.3, equation (1), author-version pp. 3–4** gives mu through s^11 with O(s^12) error and explicitly leaves divergence unproved. Section 6.4, author p. 41, uses truncation and Padé–Borel estimates as numerical methods. [Author text](https://personal.math.ubc.ca/~slade/se.pdf). |
| B. T. Graham, *Borel-type bounds for the self-avoiding walk connective constant*, J. Phys. A **43** (2010), 235001, 13 pp., DOI 10.1088/1751-8113/43/23/235001 | **Published Theorem 1.3, equation (1.3), p. 2** is the factorial remainder bound below; the coefficient bound is **published Lemma 5.1**. In **arXiv:0911.5163**, these are **Theorem 1.1, p. 2**, and **Lemma 4.1, p. 5**. The Borel discussion is Section 2, arXiv pp. 2–3. Published equation (1.2), p. 2 independently lists the 13 reciprocal coefficients. [arXiv text](https://arxiv.org/pdf/0911.5163), [journal DOI](https://doi.org/10.1088/1751-8113/43/23/235001). |
| P. R. Gerber and M. E. Fisher, *Critical temperatures of classical n-vector models on hypercubic lattices*, Phys. Rev. B **10** (1974), 4697–4703, DOI 10.1103/PhysRevB.10.4697 | The spherical-model expansion is rigorously divergent. This is stated in the original abstract and developed in Graham Section 2, arXiv p. 3; the latter also gives its Borel representation. **The original full-text internal locator was not verified.** This is an analogous resolved model, not a resolution of C0097. Graham's arXiv bibliography misnames the journal as J. Math. Phys.; the correct journal is Phys. Rev. B. [Original publisher abstract](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.10.4697). |
| Y. Mejía Miranda and G. Slade, *Expansion in high dimension for the growth constants of lattice trees and lattice animals*, Combin. Probab. Comput. **22** (2013), 527–565, DOI 10.1017/S0963548313000102 | **Theorem 1.1, arXiv:1208.3513v2 p. 2**, gives the first three critical-point terms. **Section 1, arXiv p. 3**, leaves all-orders existence, then zero radius and Borel summability, as further problems. It also describes SAW divergence as likely and Graham's result as partial. [Author preprint](https://arxiv.org/pdf/1208.3513). |
| M. Heydenreich and K. Matzke, *Expansion for the critical point of site percolation: the first three terms*, Combin. Probab. Comput. **31** (2022), 430–454; first online 2021, DOI 10.1017/S0963548321000365 | **Theorem 1.1, p. 431**, proves p_c=s+(5/2)s²+(31/4)s³+O(s⁴). The summability discussion **pp. 431–432, equations (1.6)–(1.8)** leaves divergence conjectural and complex continuation unavailable. It identifies the spherical model as the solved analogy and Graham as an upper-bound result. [Publisher text](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/expansion-for-the-critical-point-of-site-percolation-the-first-three-terms/4F13BE121491D96EFBF8E273B7023D01). |

### What Graham proves

For beta_c=1/mu with formal coefficients alpha_n, a constant C independent of d and M satisfies

\[
 \left|\beta_c(s)-\sum_{n=1}^{M-1}\alpha_n s^n\right|
 \le C^M M!s^M \qquad(d,M\in\mathbb N).
\]

Consequently |alpha_n|<=C^n n!: fix n, divide the remainder by s^n, and let integer d tend to infinity. Thus the Borel transform has a nonzero local radius. This proves neither divergence nor global Borel summability. The latter still needs suitable continuation, growth control, and identification with beta_c. Section 2 makes that distinction explicitly.

The convergence questions for mu and beta_c are equivalent: the normalized formal series F=s*mu and B=beta_c/s have constant term 1 and satisfy FB=1. Either is a convergent germ exactly when its reciprocal is. A factorial lower bound along infinitely many indices, or any super-geometric subsequence, would suffice for zero radius. No such bound for a_k or alpha_n was found or obtained.

### Search scope

The search combined SAW/connective constant/inverse dimension with zero radius, divergence, Borel summability, factorial coefficients and nonanalyticity, including year filters through 2026 and analogous percolation/tree/animal models. It inspected Slade's publication list, which includes 2026 preprints, and the later sources above. No later proof for SAW or the specified nearest-neighbour analogues was located. This is a bounded search, not a certification that no such publication exists. The unpublished 1993 Hara–Slade appendix is saved separately and is not being substituted for the 1995 article. Access failures and source-version distinctions are recorded in LOG.md and sources/literature_notes.txt.

## 2. Why the suggested direct attacks do not yet prove C0097

Counting many loops does not lower-bound an inverse-dimension coefficient after all cancellations. Coordinate embeddings produce factors

\[
 2^r(d)_r=s^{-r}\prod_{j=0}^{r-1}(1-2js),
\]

whose lower coefficients alternate. The lace expansion adds further signs, and evaluation at the unknown critical point and formal inversion introduce additional combinations. The sign change in the known coefficients rules out assuming positivity of the final sequence.

There is also a gap in the proposed implication from a convergent asymptotic series to analyticity of the physical mu. A convergent formal expansion supplies an analytic germ with those coefficients; it does not show equality with mu(d) at s=1/(2d). A nonzero flat term e^(-1/s) is smaller than every power on this sequence and changes no asymptotic coefficient. Multiplying that flat term by a polynomial permits arbitrary corrections at finitely many positive s-values. Thus mu(1)=1 or a value of mu(2) gives no contradiction. A singularity at a fixed nonzero s would only limit the radius, not force it to vanish. A complex-dimensional definition and singularities accumulating at zero, or a direct coefficient lower bound, would be needed for that approach. Neither has been established here.

## 3. A divergent related series: simple random walk

**Proposition 1.** Let G_d=sum_{n>=0} P_d(S_n=0) for nearest-neighbour simple random walk, d>2. Write its large-d expansion as G_d~sum_{m>=0} gamma_m s^m. There is an R with 0<R<infinity such that

\[
 \limsup_{m\to\infty}\left(\frac{|\gamma_m|}{m!}\right)^{1/m}
 =\frac2R\in(0,\infty).
\]

In particular, infinitely many gamma_m have a factorial lower bound and the series has zero radius. The formal inverse-dimension series for the eventual return probability also has zero radius.

**Proof.** Define the entire function

\[
 I_0(x)=\sum_{j\ge0}\frac{x^{2j}}{4^j(j!)^2},\qquad
 g(x)=x-\log I_0(x)
\]

near zero, with log I_0(0)=0. Since g(0)=0 and g'(0)=1, its local inverse is analytic:

\[
 h(t)=g^{-1}(t)=\sum_{n\ge1} b_n t^n,\qquad b_1=1.
\]

The Taylor radius R of h is positive and finite. To prove finiteness, suppose h were entire. The local identity

\[
 I_0(h(t))=\exp(h(t)-t)
\]

then holds everywhere by the identity theorem. Its right side never vanishes. But I_0 has at least two distinct zeros: J_0(x)=I_0(ix) is real, J_0(0)=1, and its alternating series gives

\[
 J_0(3)<\sum_{j=0}^{4}\frac{(-9/4)^j}{(j!)^2}
 =-\frac{4199}{16384}<0.
\]

The omitted tail starts negative and decreases in magnitude. By continuity, J_0 has a zero r in (0,3), giving the distinct zeros ir and -ir of I_0. Thus an entire h would omit both ir and -ir. Little Picard's theorem makes h constant, contradicting h'(0)=1. Hence 0<R<infinity.

Poissonization of the discrete random walk gives the exact integral

\[
 G_d=\int_0^\infty e^{-u}I_0(u/d)^d\,du
     =d\int_0^\infty e^{-d g(x)}\,dx.
\]

Indeed, a rate-one walk has independent signed coordinate jump counts of rates 1/(2d); its probability of being at the origin at time u is e^-u I_0(u/d)^d. Integrating its Poisson expansion gives one copy of every discrete-time return probability.

For real x>=0, the representation I_0(x)=pi^-1 integral_0^pi exp(x cos theta) dtheta shows that g'(x)>0. Also

\[
 e^{-x}I_0(x)\le Cx^{-1/2}\quad(x\ge1),
\]

by 1-cos theta>=2theta²/pi² and the Gaussian integral. Thus g tends to infinity and integral e^(-d_0 g(x)) dx is finite for d_0>2. For fixed delta>0, the part x>=delta is bounded by a constant times exp(-(d-d_0)g(delta)). It is exponentially small as d tends to infinity.

Change variables t=g(x) near zero and Taylor-expand h'. Integrating its Taylor remainder gives the all-orders expansion

\[
 G_d\sim\sum_{m\ge0}(m+1)!b_{m+1}d^{-m},\qquad
 \gamma_m=2^m(m+1)!b_{m+1}.
\]

The exponentially small tail just controlled justifies discarding the rest of the integral. Equivalently, the Borel transform is

\[
 \sum_{m\ge0}\frac{\gamma_m}{m!}t^m=h'(2t).
\]

Differentiation preserves a finite Taylor radius, so Cauchy–Hadamard gives the claimed limsup 2/R. More explicitly, for every 0<q<1/R, infinitely many n satisfy |b_n|>=q^n, and then

\[
 |\gamma_{n-1}|\ge 2^{n-1}n!q^n.
\]

Taking nth roots proves super-geometric growth.

Finally, the renewal decomposition gives G_d=1/(1-P_d), where P_d is the probability of a return after time zero. The formal series for P_d has constant term zero. If it converged near zero, then 1/(1-P_d) would converge there, contradicting the result for G_d. This proves divergence of the return-probability series as well. ∎

This is the same solvable mechanism as the spherical-model example: Graham's K_c(d) equals G_d/(2d). It is therefore a self-contained recovery of a known analogy, not a new proof for SAW. On the positive axis the same substitution gives the exact Laplace recovery

\[
 G_d=\frac1s\int_0^\infty e^{-t/s}h'(2t)\,dt\qquad(0<s<1/4).
\]

## 4. Every fixed-memory model has a convergent expansion

**Proposition 2.** For an integer tau>=2, let mu_tau(d) count walks excluding returns at time separations 1,...,tau. Put L=tau-1. The normalized connective constant s*mu_tau(d) is represented at all sufficiently large integer d by a holomorphic function lambda_tau(s) on

\[
 |s|<\frac{1}{24L^2},\qquad \lambda_\tau(0)=1.
\]

Hence the regular Laurent part of mu_tau has positive radius. Memory 1 is unrestricted simple random walk and has mu_1=2d.

**Proof.** Retain the last L increments. Modulo coordinate permutations and independent sign reversals, there are finitely many legal words, independent of d once d>=L. They are the self-avoiding L-step words in canonical signed-axis notation.

If a word uses k axes, a next step along an old signed axis has multiplicity 1 and is either allowed or forbidden. A step along a new axis is always allowed and has multiplicity 2(d-k). After shifting the retained word and canonicalizing, the quotient transition matrix therefore has the form

\[
 Q(s)=sM(d)=A+sB.
\]

A has exactly one 1 per row: it always appends a new axis. B records allowed old-axis choices and subtracts 2k at the new-axis destination. Thus ||B||_infinity<=4L.

After L new-axis steps every state becomes the all-distinct-axis state q_*. Consequently

\[
 A^L=P,\quad P^2=P,\quad AP=PA=P,
\]

where every row of P is concentrated at q_*. The eigenvalue 1 of A is simple and all other eigenvalues are zero. For z different from 0 and 1,

\[
 (zI-A)^{-1}=\sum_{j=0}^{L-1}z^{-j-1}A^j
             +\frac{z^{-L}}{z-1}P.
\]

On the circle |z-1|=1/(2L), one has |z|^-L<=2, giving ||(zI-A)^-1||_infinity<=6L. Therefore, when |s|<1/(24L²),

\[
 \|sB(zI-A)^{-1}\|_\infty<1.
\]

The contour remains in the resolvent of Q(s), and its Riesz projection has rank one throughout this disc. Its single enclosed eigenvalue lambda_tau(s) is holomorphic.

For positive physical s in this disc, Q(s) is nonnegative, with row sums between 1-2Ls and 1. Its spectral radius lies in that interval, which is inside the contour, so it equals lambda_tau(s). The initial distribution after L steps gives positive weight to every quotient state for d>=L. The total number of extensions thus has exponential growth rho(M(d)), by finite-dimensional nonnegative-matrix theory. Hence s*mu_tau(d)=rho(Q(s))=lambda_tau(s), as claimed. ∎

This argument also yields an exponential coefficient upper bound: if lambda_tau(s)=sum ell_n s^n, Cauchy's estimate gives

\[
 |\ell_n|\le\left(1+\frac1{2L}\right)(24L^2)^n.
\]

The radius bound shrinks with memory. There is no uniform analytic neighbourhood supplied as tau tends to infinity, so fixed-memory convergence does not imply convergence for SAW. Nor does the absence of a uniform bound prove divergence.

## 5. A factorial diagonal in a lace quantity

**Proposition 3.** Let pi^(1)_(2m)(0;d) count rooted, oriented self-avoiding returns of length 2m, the one-loop lace quantity in CLS Section 3.2, equation (25), author pp. 12–13. Define

\[
 \ell_m=[s^m]\{s^{2m}\pi^{(1)}_{2m}(0;1/(2s))\}.
\]

For every m>=2, ell_m>=(m-1)!.

**Proof.** Take the canonical words

\[
 (e_1,e_2,\ldots,e_m,-e_1,-e_{\sigma(2)},\ldots,-e_{\sigma(m)}),
\]

where sigma orders {2,...,m}. The first half visits the nested sets {1}, {1,2},...,{1,...,m}. After the step -e_1, each nonempty visited coordinate set omits coordinate 1, so none equals a nonempty first-half set. The second-half sets strictly decrease; the origin is reached only at the last step. These are (m-1)! different simple-return types.

Each type has 2^m(d)_m coordinate/sign embeddings. By the full coordinate-orbit decomposition, the number of 2m-step self-avoiding returns is a sum over r<=m of nonnegative canonical counts times 2^r(d)_r. After normalization, terms with r<m start above degree m, and the r=m term starts at degree m. The displayed family contributes

\[
 (m-1)!s^m\prod_{j=0}^{m-1}(1-2js),
\]

whose coefficient at degree m is (m-1)!. All other contributions at that degree are nonnegative. ∎

**Limitation:** ell_m is a diagonal across different fixed-length polynomials. It is not the degree-m coefficient of their sum over all lengths. Larger-dimensional contributions from shorter lengths can enter that degree with opposite signs; higher-loop terms and the critical-point equation create further cancellations. Proposition 3 supplies no lower bound on the final a_k or alpha_n.

## 6. Reproduced coefficients and growth evidence

The coefficients a_k, k=0,...,11, in the convention of this report are

```
-1, -1, -3, -16, -102, -729, -5533, -42229,
-288761, -1026328, 21070667, 780280468.
```

Together with a_-1=1 these are the 13 known coefficients. Exact formal inversion gives alpha_1,...,alpha_13:

```
1, 1, 2, 6, 27, 157, 1065, 7865, 59665, 422421,
1991163, -16122550, -805887918.
```

This independently matches Graham's published equation (1.2), p. 2. The highest known reciprocal order is 13 because beta=s/(s*mu).

Selected diagnostics, calculated without fitting a growth law:

| k | a_k | Absolute successive ratio | Borel absolute ratio |
|---:|---:|---:|---:|
| 5 | -729 | 7.147059 | 1.429412 |
| 6 | -5533 | 7.589849 | 1.264975 |
| 7 | -42229 | 7.632207 | 1.090315 |
| 8 | -288761 | 6.837979 | 0.854747 |
| 9 | -1026328 | 3.554247 | 0.394916 |
| 10 | 21070667 | 20.530149 | 2.053015 |
| 11 | 780280468 | 37.031598 | 3.366509 |

The last column is the absolute ratio of successive Borel coefficients a_k/k!. Its irregularity and the sign change make extrapolation unreliable. A finite prefix admits both an entire polynomial extension and a factorially divergent extension. These data provide evidence only; they determine neither radius nor a Borel singularity. Full signed rational Borel coefficients, reciprocal ratios, nth roots and partial sums at several d are in data/.

For comparison, the independently generated SRW Green coefficients begin

```
1, 1, 3, 12, 60, 355, 2380, 17430, 134190, 1027656,
6922146, 21248073, -601744143.
```

Even this rigorously divergent analogy has substantial sign cancellation. Its divergence was proved by the inverse-function argument, not inferred from this list.

## 7. Checks, reproducibility and remaining gap

Run from this directory:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/analyse.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/memory_walks.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/lace_family.py
```

All use the standard library and one thread. The launcher requests nice 10; an independent final read measured inherited niceness 15, so the computations ran at lower priority than nice 10. Attempts to change niceness again inside the sandbox were denied. Each numerical script took less than one second and reported peak resident memory below 25 MB.

* Reciprocal coefficients were checked by two exact recurrences and by multiplying the normalized series to obtain 1 through degree 12; the published alpha list provides an external cross-check.
* Forty SRW terms were generated by rational Bessel/Lagrange inversion. The first 13 were checked independently from
  C_(2n)(d)=(2n)! sum_r binom(d,r)[x^n](sum_(j>=1)x^j/(j!)²)^r,
  followed by division by (2d)^(2n) and summation. Only n<=12 can contribute through s^12. The return-series initial coefficients 0,1,2,7,35,215 and the rational upper bound for J_0(3) were checked exactly.
* Fixed-memory matrices for tau=2,4,6 had 1,6,109 states. The reset identity, norm bound and Taylor eigenvector equations were checked through degree 12. Independent literal enumeration in d=2 at length 8 gave the same counts 8748,6444,6028.
* All 5913 explicit polygon-family members for 2<=m<=8 were checked for simplicity. The general factorial claim follows from the proof, not this finite check.

PDF bytes were passed in memory to pdftotext; only text was retained. No PDFs, paper images, scans, publication, git commits or pushes were produced. Source manifest and check summaries are in data/. LOG.md records the work and the corrected intermediate floating-point mistake caught by the independent check.

The unresolved step for C0097 is a super-geometric lower bound after the complete signed lace and critical-point operations, or another argument forcing zero radius. None of the three propositions supplies that step. Thus PARTIAL records rigorous related-model results and a verified literature/coefficient audit, **not a solution of the SAW conjecture**.

Task: “Open problem C0097” — received 13 November 2026, 06:34 +04 (Asia/Tbilisi).
