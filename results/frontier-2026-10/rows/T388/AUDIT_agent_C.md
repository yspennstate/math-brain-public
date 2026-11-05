# T388 review: the partial-trace statistic and one-pass Oja (agent C, 4 Nov 2026)

The check scripts and their outputs named below are in audit_C/.

Source: T388_partial_trace_d2.md, t388.py, t388_oja.py and both outputs, in this folder.

## Part 1: the offline claim

### The identity: correct, and exact

Writing y = z + beta g u, the fourth cumulant of y is kappa4(g) beta^4 u^(x4) = -2 beta^4 u^(x4), because z is Gaussian
and g = +-1 has kappa4 = 1 - 3 = -2. Whitening by S = (I + beta^2 u u^T)^(-1/2) maps u to u/sqrt(1+beta^2), so
cum4(x) = kappa u^(x4) with kappa = -2 beta^4/(1+beta^2)^2. With Cov x = I,
E[|x|^2 x_i x_j] = (d+2) delta_ij + kappa u_i u_j, so E[(|x|^2 - d - 2) x x^T] = kappa u u^T. Nothing is approximate.
Two side facts the review needs: E a = -2 (not 0), and Var a = 2d + kappa.

### It is FOBI

M_n + (d+2) I = (1/n) sum |x_i|^2 x_i x_i^T is the FOBI matrix of Cardoso (1989): whiten, then diagonalise the
|x|^2-weighted covariance. The shift by (d+2) I changes no eigenvector. So the "partial trace of the fourth-moment
tensor" is FOBI, and its use for a single non-Gaussian direction is FOBI's use for non-Gaussian component analysis.
The source says the method is "probably known in some form"; it is known in exactly this form.
- arXiv:1406.4765 (Miettinen, Taskinen, Nordhausen, Oja, "Fourth moments and independent component analysis") studies
  FOBI, JADE and FastICA as fourth-moment functionals: estimating equations, algorithms, asymptotic variances, at
  fixed d with n growing.
- arXiv:1701.06836 (Nordhausen, Oja, Tyler, Virta) builds asymptotic and bootstrap tests for the dimension of the
  non-Gaussian subspace on FOBI, again at fixed d.
What neither gives (as far as the abstracts show; the full texts are the next check) is the high-dimensional rate:
how n must grow with d for the FOBI eigenvector to find u. That rate, n of order d^2, is the only candidate for
something new here, and it has to be compared with the non-Gaussian component analysis literature before any claim.

### The rate: holds, with a sharper constant than the source states

Source claim: noise norm about 2 sqrt 2 d/sqrt n, transition between c = 8 and 32 at n = c d^2.

Independent check (t388_check.py -> .json, my own sampler, 4 seeds per cell, d = 16/32/64,
c = 4, 8, 16, 32, 128). With n/d large the centred noise behaves like a Wigner matrix whose off-diagonal entries
have variance v/n, v = E[a^2 x_j^2 x_k^2]. Size-biasing two Gaussian coordinates turns |x|^2 into a chi-square on
d + 4 degrees of freedom, so v = 2(d+4) + 4 = 2d + 12. Measured v/2d: 1.36, 1.18, 1.09 at d = 16, 32, 64, which is
2d + 11.5 each time. So sigma^2 = d(2d+12)/n, the noise edge is 2 sigma, and the BBP picture predicts
- weak recovery once |kappa| > sigma, i.e. n > 2(d^2 + 6d)/kappa^2 (c* = 8(1 + 6/d) at beta = 1: 11, 9.5, 8.75);
- overlap^2 = 1 - 2(d^2+6d)/(kappa^2 n), bottom eigenvalue kappa + sigma^2/kappa.

| d | c | noise norm | edge 2 sigma | source 2 sqrt2 d/sqrt n | overlap | predicted |
|---|---|---|---|---|---|---|
| 16 | 32 | 0.66 | 0.59 | 0.50 | 0.79 | 0.81 |
| 16 | 128 | 0.31 | 0.29 | 0.25 | 0.95 | 0.96 |
| 32 | 32 | 0.55 | 0.54 | 0.50 | 0.84 | 0.84 |
| 32 | 128 | 0.25 | 0.27 | 0.25 | 0.97 | 0.96 |
| 64 | 32 | 0.54 | 0.52 | 0.50 | 0.88 | 0.85 |
| 64 | 128 | 0.27 | 0.26 | 0.25 | 0.97 | 0.97 |

Above threshold the overlap and the bottom eigenvalue match the prediction within 0.03. Near and below it
(c = 4-16) the measured overlaps scatter (0.18-0.74) as finite-size BBP does. The source's edge drops the 6/d term
(19 percent low at d = 16, 4 percent at d = 64); its tables agree with mine.

Verdicts so far:
1. Identity E[(|x|^2-d-2) x x^T] = kappa u u^T: ACCEPT.
2. "Elementary, probably known": REVISE to known. It is FOBI (Cardoso 1989), studied at fixed d in 1406.4765 and
   1701.06836. Not new as an algorithm.
3. "Finds u at n = O(d^2 log d), threshold n ~ d^2": ACCEPT numerically, with the sharper form
   n > 2(d^2+6d)/kappa^2 for weak recovery and 1 - overlap^2 = 2(d^2+6d)/(kappa^2 n) above it. No log factor is
   needed for weak recovery; the log is an artefact of the Bernstein bound. But the BBP formula is a heuristic here:
   the noise is a weighted sample covariance with weights that depend on |x|^2, not a Wigner matrix, and the source's
   own Bernstein sketch is not a proof either (see below).
4. Proof gaps in the source's sketch, still to be written out in part 2:
   - matrix Bernstein needs bounded terms; the source truncates a at sqrt(d) polylog d but bounds neither the
     truncation bias E[a 1{|a|>t} x x^T] (which must be o(|kappa|)) nor the |x|^2 factor in the term norm;
   - the variance proxy is quoted as about 2d^2, but its exact value is d(2d+12) off the diagonal plus a diagonal
     contribution, and the u-direction has different moments;
   - Davis-Kahan needs the gap |kappa| minus twice the noise, so the stated confidence and accuracy constants
     depend on kappa^2 through n >~ d^2 log d/kappa^2: correct in form, not derived.

Part 2 (next loop step): the one-pass Oja claim against a streaming theorem that allows signed, unbounded
matrices (truncation, eta schedule, the c ~ 16x offline constant), and the novelty comparison against the
non-Gaussian component analysis literature for the n ~ d^2 rate. The catalog row stays OPEN; this is not the
ReLU-GD theorem and no count changes.

## Part 2a: the one-pass Oja claim (4 Nov 2026 13:4x +0200)

### Which theorem applies to the signed matrices

Jain, Jin, Kakade, Netrapalli, Sidford, arXiv:1602.06929 (read from the paper, Definition 1 and Theorem 1.2):
the A_i are independent, "not necessarily symmetric"; only E[A_i] = Sigma must be symmetric PSD; ||A_i - Sigma|| <= M
almost surely; V bounds the variance; the step is eta_t = alpha/((lambda_1 - lambda_2)(beta + t)); the guarantee
holds with constant probability (boost by the median of independent runs). So a theorem for SIGNED A_i exists. For
T388 take A_i = -a_i x_i x_i^T: E A = |kappa| u u^T is PSD with gap |kappa|, and the individual A_i are indefinite,
which Definition 1 allows. The source cites Jain et al. and Allen-Zhu and Li but never checks the hypotheses. Two do
not hold as stated:
- M: a x x^T is unbounded (|a| has Gaussian-like tails of scale sqrt(2d), |x|^2 chi-square-like). One must run Oja
  on truncated A_i (|a| <= t, |x|^2 <= d + s), with t ~ sqrt(d log n), s ~ sqrt(d log n). Then
  M ~ d^(3/2) log n, and M enters Theorem 1.2 only through the burn-in beta, not the leading error term.
- The truncation bias B = E[A 1{truncated}] must satisfy ||B|| << |kappa|, so that the truncated mean keeps
  the top eigenvector near u (Davis-Kahan with gap |kappa| - 2||B||). With the tail scales above,
  ||B|| ~ d^(3/2) n^(-c'), which is negligible for polynomial n. This is routine but it has to be written; the source
  does not mention it.
V for this statistic: ||E[(A - EA)^2]|| = E[a^2 |x|^2 x_j^2] ~ 2(d+2)^2 + 8(d+2) (size-biasing x_j^2 makes |x|^2 a
chi-square on d + 2 degrees of freedom); V/kappa^2 ~ 8 d^2 at beta = 1. Leading term of Theorem 1.2:
sin^2 <~ alpha^2 V/(kappa^2 n) up to constants and a log factor in the second term; so one pass needs n ~ d^2 for a
constant error, the same order as offline.

### Is the 16x factor streaming, or the step rule?

t388_oja_check.py -> .json: d = 32, 3 seeds, one data stream per seed with all step rules run side by side on
it, and offline FOBI on the same samples. "dec a, b" is eta_t = a/(|kappa| (b V/kappa^2 + t)).

| c (n = c d^2) | offline FOBI | source rule (2 log n/(|kappa| n), constant) | dec a2 b1 | dec a4 b4 |
|---|---|---|---|---|
| 32 | 0.81, 0.91, 0.91 | 0.31, 0.13, 0.37 | 0.21, 0.40, 0.73 | 0.47, 0.28, 0.54 |
| 128 | 0.98, 0.96, 0.95 | 0.04, 0.31, 0.29 | 0.93, 0.86, 0.91 | 0.85, 0.94, 0.89 |
| 512 | 0.99, 0.99, 0.99 | 0.90, 0.84, 0.91 | 0.99, 0.98, 0.99 | 0.98, 0.97, 0.99 |

With the source's rule one-pass Oja at c = 128 is barely above a random start (overlap 0.04-0.31, against 1/sqrt(32)
= 0.18 for a random vector). With the decaying rule of Theorem 1.2 it reaches 0.86-0.93 at c = 128, which offline
FOBI reaches near c = 32. So the one-pass penalty is about 4x in samples in this run, not 16x. Most of the source's
factor comes from a constant step tuned to the end of the stream (2 log n/(|kappa| n)): it is too small to leave the
random start in the first half of the data.

Verdicts on the Oja section:
5. "One pass suffices at n of order d^2": ACCEPT, and the numbers support it better than the source's own table:
   with a Jain-type step the one-pass cost is about 4x the offline sample size at d = 32 (one d only; the c-collapse
   across d is still to be shown for this rule).
6. "The constant is about 16 times the offline one, from log n and the variance-to-gap ratio": REVISE. It is mostly
   the step rule; the variance-to-gap ratio is the same V/kappa^2 for both methods.
7. "Streaming-PCA bounds require n of order (variance/gap^2) log d": REVISE the citation. Jain et al. Theorem 1.2
   is the right theorem and does allow indefinite A_i, but it needs ||A_i - Sigma|| <= M a.s.; a truncated version
   with its bias bound is required before it applies. Allen-Zhu and Li 2017 is cited without checking its
   hypotheses; I have not checked them either.
8. "The d^3 of online SGD belongs to learners that see x only through <w, x>": scope REVISE. It is the information
   exponent picture of Ben Arous, Gheissari and Jagannath (online SGD on a single-index loss with exponent k needs
   about d^(k-1)); the |x|^2-weighted loss has exponent 2 in m because the weight already contracts the fourth
   cumulant. Correct as a reading, not a new result, and it says nothing about whether the ReLU network of
   2312.14922 builds the weighting.

Still open for part 2b: the novelty of the n ~ d^2 rate for FOBI in high dimension against the non-Gaussian component
analysis literature (and whether 2312.14922 itself discusses a degree-4 spectral method), then a board post of parts
1-2.

## Part 2b: what is known about the n ~ d^2 rate (4 Nov 2026 13:5x +0200)

Read: the abstracts of 2312.14922, 1406.4765, 1701.06836, and the full text of Tan and Vershynin, "Polynomial time and
sample complexity for non-Gaussian component analysis: spectral methods", arXiv:1704.01041 (Theorem 2.4, Lemmas 5.4-5.5,
Section 6).
- 2312.14922 (Szekely, Bardone, Gerace, Goldt) proves n >~ d for statistical distinguishability and n >~ d^2 for
  low-degree polynomial tests, and shows networks learn at roughly quadratic sample size numerically. Its abstract names no
  spectral algorithm reaching d^2; I have not read its body for one.
- 1406.4765 and 1701.06836 treat FOBI at fixed dimension (asymptotic variances; dimension tests). No high-dimensional rate.
- Tan-Vershynin's Reweighted PCA diagonalises the covariance reweighted by exp(-alpha |x|^2). For small alpha that
  weight is 1 - alpha |x|^2 + ..., so at first order it is FOBI's |x|^2 weighting. Their guarantee is polynomial but
  loose: N >= C K^2 d^(3/2) (n + log(1/delta))/(beta_1^2 eps^2) with beta_1 proportional to alpha^(r-1) and
  alpha < 1/(C K^2 n) (n the ambient dimension there), which at r = 4 is of order n^7 for fixed subspace dimension. They say
  themselves the eigengap bound is crude.
So the algorithm is old (Cardoso 1989; Tan-Vershynin 2017 for NGCA in high dimension), and none of the sources I read
states the d^2 log d finite-sample rate for the |x|^2-weighted matrix. That rate is the right order (it meets the
2312.14922 low-degree bound) and is the kind of statement the tensor-unfolding / partial-trace literature for tensor PCA
and the NGCA upper and lower bounds of Diakonikolas and Kane would contain; those were not read here, so no novelty
endorsement. The most the source can claim is a written finite-sample bound for FOBI in this model, once the truncation
and bias steps of parts 1 and 2a are done.

## Summary verdicts for the board

1. Identity E[(|x|^2-d-2) x x^T] = kappa u u^T: ACCEPT (exact).
2. Method: KNOWN. It is FOBI (Cardoso 1989) shifted by (d+2) I; FOBI at fixed d is 1406.4765 / 1701.06836; a
   reweighted-PCA relative in high dimension is 1704.01041.
3. Offline rate n ~ d^2: ACCEPT numerically, sharper: weak recovery at n > 2(d^2+6d)/kappa^2, overlap^2 =
   1 - 2(d^2+6d)/(kappa^2 n), checked within 0.03 at c >= 32 for d = 16, 32, 64. The source's noise edge omits the 6/d
   term. The proof sketch lacks the truncation-bias bound, the exact variance proxy and derived Davis-Kahan constants.
4. One pass at n ~ d^2: ACCEPT, stronger than claimed: with Jain et al.'s decaying step the one-pass cost is about 4x the
   offline sample size at d = 32 (the source's 16x is its constant step). Jain et al. Definition 1 does allow indefinite
   A_i, but it needs a.s. bounded A_i, so a truncated version with its bias bound must be written before it applies.
5. Reading of the d^3 online-SGD cost: correct as the information-exponent picture of Ben Arous, Gheissari and
   Jagannath; not new; says nothing about whether the ReLU network of 2312.14922 builds the |x|^2 weighting.
6. Novelty: none endorsed. At most a finite-sample FOBI bound in this model; the tensor-PCA partial-trace and NGCA
   literature must be compared before any claim. The catalog row (ReLU GD) stays OPEN; no count changes.
