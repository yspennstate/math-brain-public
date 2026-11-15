ACCEPT

The corrected claim is proved. I found no mathematical error in Lemmas 1–5 or in the passage to all positive slices. In particular, the conditional moment argument is legitimate, and the union over slice parameters is paid for explicitly. This acceptance concerns the off-diagonal, positive-s statement; the literal printed problem is false. Novelty is not certified. A stronger d=5 assertion is already printed in a 2026 thesis; I found no verified printed resolution of the d=4 assertion.

The submitted REPORT.md and LOG.md were read. The checks below were written independently, without reading, importing, or reusing claim_files/code. Locations below refer to line numbers in claim_files/REPORT.md.

## Errors, gaps, and qualifications

There are no identified errors or gaps requiring correction in the submitted proof. The following qualifications delimit the acceptance.

1. **The original problem needs correction, already acknowledged in the submission** (lines 23–33; original Section 8.2, p.33). Equation (8.2) includes the diagonal, so its set has dimension at least 1 at every slice. At s=0 the entire quadrant is included and has dimension 2, even after deleting the diagonal. The repair is to require s>0 and u≠v. The submission makes both repairs and does not present these elementary objections as a solution of the intended question.

2. **Empty fibers require a dimension convention**, already specified (lines 17–21 and 33). The conclusion is dimension zero with dim_H(∅)=0. Under dim_H(∅)=−∞, write dimension at most zero, or equality zero for nonempty fibers. A fixed deterministic positive slice is almost surely empty off the diagonal in d=4,5. The source's second expression in (A.6), p.36, uses an infimum over positive exponents and gives dim_H(∅)=0.

3. **Literature priority is unresolved**, as the submission itself says (lines 7 and 250). The d=5 conclusion has a prior, stronger printed assertion, interpreted off the diagonal and at positive s, in Chen's 2026 thesis. Its literal statement and proof should not be cited without qualification: they repeat the boundary/diagonal omissions; (4.42) incorrectly identifies a difference of independent Brownian motions as a Brownian sheet; and (4.44) displays a small-ball exponent 2pd for a pd-dimensional vector. These are issues in that external source, not in the proof reviewed here. The fix is to describe what the thesis asserts, rather than treating it as independently verified proof. The submitted report already largely does this. No novelty claim for d=4 is justified by the limited coverage of the available citation index.

4. **The box-dimension assertion is local** (lines 205–215). Countable unions preserve the Hausdorff conclusion, but need not preserve upper box dimension. The submission correctly asserts upper box dimension zero on separated compact rectangles, not on the entire unbounded fiber or its closure along the diagonal. No repair is needed. The proof also extends the local assertion to arbitrary disjoint compact time sets: their positive separation permits a finite cover by separated dyadic interval rectangles, and upper box dimension is stable under finite unions.

## Original problem and its intended meaning

I obtained [arXiv:math/0510518](https://arxiv.org/abs/math/0510518) independently. The full plain text is in [sources/khoshnevisan_2005_arxiv.txt](sources/khoshnevisan_2005_arxiv.txt). The exact text extraction of Section 8.2 and the next page, including all the wording of Open Problem 2, is in [sources/problem_2_exact_extraction.txt](sources/problem_2_exact_extraction.txt). PDF page 33 agrees with printed page 33. The author's final version was fetched separately and checked too.

The exact displayed definition is

\[
Y_d(s):=\{(t_1,t_2)\in\mathbb R_+^2:B(s,t_1)=B(s,t_2)\}. \tag{8.2}
\]

It is introduced for every s≥0. The question's exact wording, with the mathematical typography normalized, is:

> Then is it the case that if \(d\in\{4,5\}\) then, outside a single null-set, \(\dim_H Y_d(s)=0\) for all \(s\ge0\)?

Equivalently, its precise probability statement is

\[
d\in\{4,5\}\quad\Longrightarrow\quad
\mathbb P\{\dim_HY_d(s)=0\text{ for all }s\ge0\}=1\;?
\]

The definition prints neither t1≠t2 nor an ordering of the times. This is not a matter of what R_+ means: the diagonal remains even if it denotes strictly positive numbers. The slice quantifier explicitly includes zero. With the accepted proof, the *literal* Y_d(s) has dimension exactly 1 for every s>0 and dimension 2 at s=0, almost surely.

The intended restriction is strongly supported by two comparisons in the same source. Equation (1.9), p.3, defines the exceptional-slice set using t2>t1>0. Open Problem 3, p.34, asks about finiteness of the same fibers for s>0; this question is meaningless with the diagonal retained. Thus ordered distinct positive times and positive slices are the natural intended question. The present proof even permits one of the two time coordinates to be zero. This interpretation is necessary, but it is not a restriction actually printed in (8.2).

## Verification of the proof

### Lemma 1: the direction of conditioning is correct

Fix s∈[a,b] with a>0 and one spatial coordinate W(t)=B_i(s,t). This is a Brownian motion with variance rate s. Let F be generated by the earlier pair differences, and G by W at all anchors in U∪V. Then F⊂G.

For this finite Gaussian family, conditional variances are deterministic squared distances in a Gaussian Hilbert space. Consequently

\[
\operatorname{Var}(X\mid\mathcal F)
\ge \operatorname{Var}(X\mid\mathcal G).
\]

This is a valid Gaussian statement even for singular observations. For general random variables a pointwise conditional-variance comparison would require more care; the proof does not make that general assertion.

For u between adjacent U-anchors l<r, the residual after conditioning on G is

\[
R_u=W(u)-\frac{r-u}{r-l}W(l)-\frac{u-l}{r-l}W(r),
\qquad
\operatorname{Var}R_u=s\frac{(u-l)(r-u)}{r-l}.
\]

Its covariance with every anchor observation is zero. The corresponding v-residual lies in a disjoint time interval and has zero covariance with R_u. The residuals are therefore independent, also under the conditional Gaussian law. This independence concerns bridge residuals; the unconditioned values W(u),W(v) need not be independent.

Writing x=u−l and y=r−u gives xy/(x+y)≥min(x,y)/2. Hence the two residual variances sum to at least

\[
\frac{s}{2}(\rho_U(u)+\rho_V(v))
\ge\frac a2(\rho_U(u)+\rho_V(v)).
\]

The interval endpoints ensure that both neighbors exist. They can be added as observations without having been earlier pair differences. Repeated anchors are simply removed when finding neighbors; at an anchor the residual and its rho are both zero. A deterministic observation at time zero causes no problem. The factor a/2 is valid. These arguments verify lines 91–112.

### Lemma 2: mean-uniform and degenerate cases

After conditioning on all earlier vector differences, the d spatial coordinates still have independent Gaussian residuals, with a common deterministic variance σ². Conditioning determines a possibly nonzero mean, which does not affect the maximum-density bound.

For d=4, the ball volume and Gaussian density give, for ρ=ρ_U+ρ_V>0,

\[
\mathbb P\{|X|\le r\mid\mathcal F\}
\le\min\left(1,\frac{r^4}{8\sigma^4}\right)
\le\min\left(1,\frac{r^4}{2a^2\rho^2}\right).
\]

Thus C=max(4,2/a²) suffices in (2), by separating ρ≤r² from ρ>r². When ρ=0, the right side of (2) is C; the trivial probability bound applies, even if σ²=0 and the conditional law is a point mass. No density is invoked in that case. The estimate is uniform over all conditioning values in the support of the Gaussian observations, or equivalently almost surely for a chosen conditional version. This verifies lines 114–124.

### Lemma 3: shell counting is safe

Assign each coordinate grid point to a nearest anchor, breaking ties deterministically. For an individual anchor, the set of points at distances in [jδ,(j+1)δ) lies in two intervals of length δ. The claimed bound of four lattice points is safe, including boundaries; half-open shells in fact allow a sharper bound of two. Removing points assigned to other anchors can only reduce this count.

For each anchor pair the shell indices j,l contribute at most 16 grid pairs. There are q+1 decompositions q=j+l. On the assigned pairs, the denominator is at least (r²+qδ)². Since the anchors here include the interval endpoints, all distances are bounded by the interval lengths, and the proposed finite cutoff Q=O(δ⁻¹) is valid.

With c=r²/δ≥1,

\[
\sum_{q=0}^{Q}\frac{q+1}{(c+q)^2}
\le\sum_{q=0}^{Q}\frac1{q+1}
\le1+\log(Q+1).
\]

Multiplying by 16(k+2)²r⁴δ⁻² proves (3). The zero-distance terms are retained. The assumptions δ≤r²≤1 are used exactly where required. This verifies lines 126–142.

### Lemma 4: the backwards induction does not assume independence

For a deterministic ordered tuple z1,…,zp, put A_j={|X_j|≤r}. The tower property gives

\[
\mathbb E\prod_{j=1}^p1_{A_j}
=\mathbb E\left[\prod_{j<p}1_{A_j}\,
 \mathbb P(A_p\mid X_1,\ldots,X_{p-1})\right].
\]

Lemma 2 bounds the conditional probability by a function of zp and the earlier *deterministic positions*, independent of observed values. Sum over zp before proceeding to p−1. Lemma 3 bounds that whole sum by C(p+1)²L, uniformly in the earlier positions, where L=r⁴δ⁻²(1+log(1/δ)). Thus, if T_p is the ordered p-tuple sum,

\[
T_p\le C(p+1)^2L\,T_{p-1},\qquad T_0=1,
\quad\text{so}\quad
T_p\le C^p((p+1)!)^2L^p.
\]

It would be incorrect to discard position dependence without this summation, but the submitted proof explicitly performs the summation first. Repeated pairs occur in the power expansion and are covered by the degenerate case of Lemma 2. The factorial and all constants are therefore correct; C may depend on a,I,J, but not on s,n,r or p. This verifies lines 144–160.

### Lemma 5 and the covering step

The coordinate increment variance on a bounded parameter rectangle is at most C‖(s,t)−(s′,t′)‖∞. Gaussian moments and the two-dimensional dyadic edge count yield a summable bound when q(1/2−α)>2. The chaining described in lines 168–178 gives a single finite random Hölder constant on the rectangle. It is valid at the time-zero boundary as well.

The bookkeeping in (6) is

\[
r_n^4\delta^{-2}=(2M)^4\delta^{4\alpha-2}
                  =(2M)^4\delta^{-\eta/4},
\]

and hence

\[
\mathbb P\{\max_{s\in K_n}N_n(s,r_n)>\delta^{-\eta}\}
\le C_{p,M}(1+n)^p
       \delta^{p\eta-p\eta/4-1}
=C_{p,M}(1+n)^p\delta^{3p\eta/4-1}.
\]

Here −1 is exactly the cost of the slice grid. For fixed η>0 choose an integer p>4/(3η). The geometric factor makes the bound summable. The constants may grow rapidly with p; p is fixed before n tends to infinity, so that causes no gap.

For each deterministic M the Borel–Cantelli event controls every slice grid point. Intersect these events over M∈N. Separately intersect with the common Hölder event and choose M≥H on a given path. There is no conditioning on the modulus event in a Gaussian estimate.

Dyadic endpoints make downward rounding stay in K,I,J for all sufficiently fine grids. If an exact pair at any real s is rounded to (s_n,u_n,v_n), the two sheet increments are each bounded by Hδ^α, giving precisely

\[
|B(s_n,v_n)-B(s_n,u_n)|\le2H\delta^\alpha\le r_n.
\]

Thus all exact pairs of that slice are covered by at most δ⁻η squares of diameter √2δ. The starting scale can depend on the path,M,η,K,I,J, but is uniform in s and the pair. Dyadic covering scales suffice for upper box dimension by monotonicity of covering numbers between consecutive scales. The β-dimensional Hausdorff cost is at most 2^{β/2}δ^{β−η}, which tends to zero for β>η.

Finally intersect over η=1/m and over the countable family of dyadic K bounded away from zero and separated dyadic I,J. Every distinct finite pair belongs to one such rectangle after reversing the coordinates if necessary. The Hausdorff conclusion follows by countable stability. At no point is an event proved merely for each fixed s intersected over uncountably many s. The first four coordinates of a five-dimensional sheet form a four-dimensional sheet, and the five-dimensional fiber is a subset of its fiber on the same probability-one event. The projection step preserves the simultaneous quantifier. This verifies lines 182–215.

## Sanity checks and independent code

In d=3, the small-ball kernel is Cr³/(r²+ρ)^{3/2}. Its shell sum is bounded by

\[
16(k+2)^2r^3\delta^{-3/2}
 \sum_{q\le C/\delta}\frac{q+1}{(r^2/\delta+q)^{3/2}}
\le C(k+2)^2r^3\delta^{-2}.
\]

The last sum grows like δ⁻¹/², rather than logarithmically. With α=1/2−η/16, target count δ^{−(1/2+η)}, and the slice union, the probability exponent is 13pη/16−1. This proves only local upper box dimension at most 1/2. It does not prove dimension zero. At a deterministic positive slice, the Brownian double-time dimension is 2−3/2=1/2; Rosen's formula is recorded in KWX (2006), (4.2), p.840. The signs and magnitudes agree.

In d=4, δ⁻η tends to infinity for every fixed η>0. Bounding the near-collision count by that quantity never forces the count to vanish. The argument therefore permits nonempty and even infinite zero-dimensional fibers. It is compatible with the exceptional-slice set having dimension 1, as in source (1.12), p.4, and with that set having zero Lebesgue measure. The uniformity in s is about the size of each fiber, not the absence of exceptional slices.

Run the independent checker from this directory:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  python3 code/independent_checks.py
```

It checks the conditional variance twice: an orthogonal projection of interval indicators in the independent Brownian-increment representation, and a Schur complement using the covariance kernel s times interval-overlap length. Singular cases use least squares and an eigenvalue pseudoinverse. The 2,100 configurations include continuous random times, lattice times, duplicate observations, linearly dependent four-pair cycles, repeated target pairs, and interval endpoints. The minimum conditional-variance-minus-exact-bridge difference was −2.78×10⁻¹⁷, consistent with rounding; the maximum discrepancy between the two variance calculations was 3.79×10⁻¹⁴.

The 112 lattice configurations use δ=2⁻ⁿ, n=3,…,9, up to nine additional anchors per interval, quarter-grid anchors, and r² equal to δ, δ^0.7, 1/2 or 1. The actual sum was bounded separately by the shell expression and by the harmonic bound in every case. The maximum observed number of points in an individual shell was two. The maximum actual sum divided by (k+2)²r⁴δ⁻²(1+log(1/δ)) was 1.139. Numerical d=3 and d=4 comparisons also show the expected power and logarithmic scales.

Full configurations and results are in [data/independent_checks.json](data/independent_checks.json); the compact output is in [data/check_summary.txt](data/check_summary.txt). The run used nice 10, one numerical thread, about 40 MB peak RSS, and less than one second. These finite checks support the analytic audit; they do not establish a universal inequality. The submitted near-hit simulations were not rerun and are not used as evidence of a Hausdorff dimension or of novelty.

## Literature result and value

The search covered the original and final survey, the named papers, exact and variant descriptions of the problem, the 2026 thesis, and forward citations over 2005–13 November 2026. Search details, URLs, and access limitations are in [sources/literature_search.txt](sources/literature_search.txt). Download metadata and hashes are in [sources/manifest.txt](sources/manifest.txt). All retained source artifacts are plain text.

| Source checked | Relevant result | Consequence for this claim |
|---|---|---|
| [Khoshnevisan (2005 preprint; published chapter 2008)](https://arxiv.org/abs/math/0510518), Theorems 1.2, 1.4, Section 8.2 | Uniform zero-*time* fibers in d=2,3; exceptional double-slice dimensions; asks the present double-time question | Supplies the problem and sanity checks, not its intended solution |
| [Dalang–Khoshnevisan–Nualart–Wu–Xiao (2012)](https://arxiv.org/abs/1009.0235), Theorem 1.1 and Corollary 1.3, reprint pp.1–2 | Decoupling for full-sheet pairs with unequal coordinates; no full-sheet double points at d=4N | For a two-parameter sheet the critical dimension is 8. Here the two parameter points share their s-coordinate. This does not imply the d=4,5 fiber bound |
| [Khoshnevisan–Wu–Xiao (2006)](https://www.stt.msu.edu/~xiaoyimi/KWXEJP06.pdf), Lemma 1.1 p.819, Theorem 1.3 p.820, Lemma 3.1 p.826, Theorem 4.1/(4.2) p.840 | Sectorial LND, uniform image dimensions and full-sheet multiple-point/time dimensions | Closely related high-moment method. Image dimension doubling for B is not a uniform fiber theorem for X(s,u,v)=B(s,v)−B(s,u). No direct implication identified |
| [Dalang–Mueller (2015)](https://arxiv.org/abs/1303.0403), Theorems 1.1–1.3, reprint pp.2–3 | Absence of k-multiple points when (k−1)d=2kN, including shared-coordinate configurations | Many double pairs need not share a common spatial value. These theorems do not supply the required fiber-dimension assertion |
| [Chen–Xiao (2012)](https://stt.msu.edu/~xiaoyimi/InterSection_CXRevised.pdf), Theorem 3.5/Corollary 3.6 | Hitting/intersection criteria for independent anisotropic Gaussian fields on deterministic parameter sets | Does not assert the required simultaneous bound over the common slice parameter |
| [Khoshnevisan–Xiao (2007), Images of the Brownian Sheet](https://www.math.utah.edu/~davar/PPT/IMAGE-BS/IMG8.pdf), Theorems 1.1, 1.2, 1.4 | Image capacity, interior points under rotations, and sectorial LND | Methodological background; no direct resolution found |
| [Chen–Woessner (2025), Zeros of the Brownian Sheet](https://link.springer.com/article/10.1007/s10959-024-01399-1), Theorems 1.2, 1.3, 1.5 and Proposition 3.1 | Projections of zero sets; answers survey Open Problem 4 | Does not answer Open Problem 2. Read in primary publisher HTML; the attempted PDF endpoint was unusable |
| [Keming Chen, EPFL thesis 11211 (2026)](https://infoscience.epfl.ch/entities/publication/a90f4af0-e1aa-47fa-929e-148198a9855b), Theorems 1.3.3/1.3.4, printed p.7, repeated pp.107–108 | Asserts finite fibers for d=5 and infinite fibers on exceptional slices for d=4 | d=5 dimension zero is a prior printed consequence under the intended interpretation. Infinite d=4 fibers need not have positive dimension. This thesis does not establish the d=4 claim reviewed here; see qualification 3 |

Mountford (1990), *Double points and the Ornstein–Uhlenbeck process on Wiener space*, Illinois J. Math. 34, 38–48, is the source credited for the exceptional-slice dimensions in (1.12). Its primary PDF endpoint returned an unusable response; I rely on the original survey's explicit attribution, not on a claimed reading of Mountford's proof. The stationary Wiener-space OU representation e^{−r/2}B(e^r,t) explains the relation to slices but does not convert an exceptional-slice dimension formula into a bound on every fiber.

The independent OpenAlex query found three indexed forward citations of the published chapter: the 2013 limsup-fractal paper, the 2013/2014 packing-dimension paper for additive Lévy processes, and Chen–Woessner (2025). The separately indexed arXiv record had zero indexed citers. The snapshots are retained. Such sparse coverage is not a complete list of actual citations. The thesis was located by independent searches, not by that index. I therefore make no assertion that the d=4 result was previously unknown.

The mathematical value is a short, sound, self-contained proof of the intended uniform d=4 dimension bound, with a stronger local upper box assertion. The d=5 dimension bound follows by projection and has a prior stronger printed assertion. No immediate deduction of the d=4 result from a theorem actually checked here was found. The method is a familiar sectorial-LND/high-moment covering method; priority of this particular application remains unverified.

Precisely, for a continuous two-parameter R^d-valued Brownian sheet, d=4 or 5, there is one probability-one event on which, for every s>0,

\[
\dim_H\{(u,v)\in[0,\infty)^2:u\ne v,\ B(s,u)=B(s,v)\}=0,
\]

with the stated empty-set convention. On every separated compact rectangle the fiber has upper box dimension zero as well. The proof does not establish finiteness, countability, emptiness, or a global upper box dimension for the entire fiber.

Task: “You are an independent referee … Break it if it is wrong.” — received 2026-11-13 09:45 +04 (Asia/Tbilisi).
