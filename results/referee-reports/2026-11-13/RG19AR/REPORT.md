Overall verdict: ACCEPT

I found no mathematical error or missing load-bearing step in the stated continuous-time result. In particular, the conditioning in the common-clade argument is valid, the accumulated errors are bounded in L2 rather than merely in mean, and the separating-cut estimate supplies the uniform bound needed for polarization. The estimates include adjacent leaves and offsets near half the cycle. This verdict concerns the proof in PAPER.tex; it does not certify unavailable bibliographic sources or the sharper numerical conjecture about bounded errors.

Line references below refer to PAPER.tex. I read the supplied checks and Lean file but did not execute or import the authors' programs. All computations reported here use the three independent programs saved alongside this report. No browsing was used.

## Theorem 1.1 (thm:main): SOUND

Statement: lines 65–71. Proof: lines 247–285.

The continuous-time normalization is correct. Independently, the beta-splitting weights at beta = -1 satisfy

\[
\binom mi B(i,m-i)=\frac{m}{i(m-i)}.
\]

Their normalized probabilities are therefore
\(m/[2h_{m-1}i(m-i)]\). Giving a clade an exponential clock of rate \(h_{m-1}\) produces exactly the cut rates at lines 45–48. The factor 2 is necessary and is present.

For the actual covariance argument:

* Lines 247–251: both tagged processes are martingales in the full tree filtration. Revealing the two labels initially does not change any clade's future cut intensities. Their terminal times have all moments for each fixed n, which justifies the stopping operations below.
* Line 253: the initial-potential estimate is genuinely an L2 estimate. Each of the two logarithmic terms has squared mean at most 2 by the decreasing-function integral comparison. Thus \(\|F_0-\log n\|_2\le2\sqrt2\), uniformly in n. Independence between these terms or between the two leaves is unnecessary.
* Lines 255–259: the cyclic closing is handled by the correct mixture of two **linear** gaps. With probability \((n-r)/n\), the gap is r and the left position is uniform on \(1,\ldots,n-r\); otherwise the gap is n-r and the left position is uniform on \(1,\ldots,r\). The original interval tree is not assumed to be invariant under cyclic shifts. Writing x = r/n, the logarithmic mixture minus \(\log(n/r)\) is \(x\log(x/(1-x))\), which is bounded on \(0<x\le1/2\). Proposition 3.2 therefore gives the stated uniform mean separation time.
* Lines 261–268: sorting the two labels is measurable at time zero. The sum of their squared initial-potential errors is unchanged. At separation the potential difference is exactly G, including the jump at S. Lemma 4.1 bounds its second moment under the correct separating-cut law, and Lemma 2.2 bounds both integrated drift errors. Consequently \(\mathbb E N_S^2=O(1)\). There is no replacement of an expectation bound by a second-moment bound here.
* Lines 270–277: the cross bracket includes the separating jump. After S the clades have independent clocks and no simultaneous jumps, so the cross bracket stops. Polarization gives

\[
\mathbb E\!\int_0^S\beta_t\,dt
=c_2\mathbb ES-\tfrac12\mathbb E\!\int_0^S(e_2^{(1)}+e_2^{(2)})\,dt
-\tfrac12\mathbb E N_S^2
=c_2\mathbb ES+O(1).
\]

  The terminal martingale product has this expectation. One can justify uniform integrability directly by the integrable bound on the suprema of the stopped martingales obtained from their bounded potentials and the heights' finite moments.
* Lines 279–283: each remainder R has bounded L2 norm, whereas each terminal martingale has L2 norm \(O(\sqrt{\log n})\). Expanding the covariance and applying Cauchy–Schwarz therefore gives exactly the claimed error. No independence of R and M is asserted or needed. For the ordered pair, reflection of the interval tree exchanges the two heights, conditionally on either linear-gap case. Their means are equal; their sum and product are the original heights' sum and product. Hence this covariance is the requested one.
* Line 283, variance: the same decomposition gives \(\operatorname{Var}D_n=c_1^{-2}\mathbb EM_D^2+O(\sqrt{\log n})\), and \(\mathbb EM_D^2=c_2c_1^{-1}\log n+O(1)\). The coefficient is therefore \(c_2/c_1^3\), not \(c_2/c_1^2\).

The constants in these estimates are uniform in both gap cases, including the case where the linear gap exceeds n/2. The proof does not discard the wrapped pairs.

## Corollary 1.2 (cor:rho): SOUND

Lines 73–79.

Put \(L=\log n\) and \(A=\log(n/r)\). Since \(0\le A\le L\), dividing \(\sigma^2 A+O(\sqrt L)\) by \(\sigma^2 L+O(\sqrt L)\) gives \(A/L+O(L^{-1/2})\) uniformly in r. The denominator is bounded below by \(\sigma^2 L/2\) for all sufficiently large n. Small n can be absorbed in the absolute constant; the variance is positive because the independent root holding time has positive variance.

If \(\log r_n/\log n\to0\), the correlation tends to 1, including fixed r and any subpolynomial r. If the ratio tends to 1, the correlation tends to 0, including r near n/2 and also sublinear sequences such as \(n/\log n\). Neither endpoint requires a separate argument or a lower bound on \(\log r\).

## Remark 1.3 (rem:oriented): SOUND

Lines 81–83 and 285.

In fact the covariance is exactly symmetric under r being replaced by n-r: average \(H_JH_{J+r}\) over J and change the summation index. Both marginals remain uniform. Thus the extension with \(\min(r,n-r)\) follows immediately from Theorem 1.1. An unrestricted oriented sequence r = n-1 would have logarithmic exponent 1 but the adjacent-leaf correlation tending to 1. The restriction in the paper avoids this genuine endpoint pitfall.

## Remark 1.4 (separation-time interpretation): SOUND

Lines 85–87.

The displayed interpretation follows from Proposition 3.2, the cyclic mixture, and the bracket calculation above. The bounded-error assertion mentioned afterward is explicitly a suggestion from simulations, not a proved strengthening used later. The simulations cannot establish either an O(1) bound uniformly in n and r or a sharp lower bound on the rate of convergence. Read “of order 1/log n” here as the suggested upper rate, not an established two-sided asymptotic claim.

## Lemma 2.1 (lem:drift): SOUND

Lines 97–138, including the potential and loss formulas preceding the lemma.

The identity \(ab-m=(a-1)(b-1)\) gives the asserted range and the endpoint zero of F. Removing l leaves on one side leaves the opposite rank unchanged, giving exactly the two losses at line 103. These losses are nonnegative, including zero losses when a rank equals m.

For k at least 2, both a and b are strictly below m. The substitution at line 123 is bijective on the stated open intervals and has the stated logarithmic derivative. Each side's continuous integral is \(p!\zeta(p+1)/2\), so the two sides give \(c_1=\zeta(2)\) and \(c_2=2\zeta(3)\). The series and integral interchanges use nonnegative terms.

The positive-coefficient expansion at line 129 proves monotonicity for both p = 1 and p = 2. It yields the sign of the sum/integral deficit and bounds that deficit by the last unit interval, despite the integrable singularity at a. On that interval the rate is at most \(2/q\), and the logarithm is at most \(\log((q+1)/u)\). The integral of its p-th power has the required bound. The two values of q are at least k-1. The decreasing comparison function used in line 137 is indeed decreasing for both p. The k = 1 case must be separate and is correctly treated; it includes m = 1.

There is no missing contribution from exponential holding times to the bracket constant. For a compensated jump martingale the bracket rate is the rate-weighted squared jump, which is d2 here.

## Lemma 2.2 (lem:errors): SOUND

Lines 140–151.

Each rank is nonincreasing, so a dyadic k-bin can be visited at most once. Conditional on entering a bin, the cuts listed at line 147 have combined exit intensity at least 1/4 at every state inside it. This gives an exponential upper tail for the entire residence time even if other cuts occur before exit. Integrating the tail gives \(\mathbb E T_q^2\le32\). At k = 1 the singleton-isolating cut has intensity at least 1/2, giving \(\mathbb E T_0^2\le8\).

The deterministic coefficients \((1+(q+2)^p)2^{-q}\) are summable. Minkowski thus gives a uniform bound for the **second moment of the whole accumulated error**, not just for each state's error or for its expected sum. Since the errors are nonnegative, stopping earlier only decreases the integral pathwise; no independence of residence times is needed. This proves the assertion for every stopping time in the lemma, and also suffices for S in the larger tree filtration.

## Lemma 2.3 (lem:mart): SOUND

Lines 153–163.

Applying the finite-state generator to F gives -d1 and its squared jump rates give d2. The sign in \(c_1D=F_0+M_D+\int e_1\) is correct. Holding times can be coupled to independent standard exponentials divided by rates at least 1; there are at most m-1 jumps. This supplies the moment and stopping justification, rather than finite state space alone. Lemma 2.2 then gives the uniform expectation error and the martingale second-moment bound. All statements remain valid for m = 1.

## Lemma 3.1 (lem:pair): SOUND

Lines 167–183.

The claim is about the natural history of the common-clade size, not about conditioning on the full tagged tree history. For a specified retained size k, either admissible side maps its eligible starting positions bijectively to \(1,\ldots,k-r\). Its rate is independent of that position. Adding the sides gives

\[
a_r(m,k)=\frac{m(k-r)}{(m-r)k(m-k)}.
\]

For k = m/2 the two disjoint sets of eligible starts arise at the same cut; adding their masses is still correct. The rate identity and the summed killing rate are exact.

Crucially, **every** cut of the common clade either changes its size or kills the process. There are no unobserved, size-preserving cuts. The total clock rate \(h_{m-1}\) is independent of the left position. Waiting times therefore convey no additional information about that position, and induction over the observed size history establishes the claimed conditional uniformity. This is why averaging the rates really does produce a Markov chain here.

At the killing transition, the uniform position is tilted by the actual cut intensity. The resulting joint mass is proportional to \(1/[i(m-i)]\), not uniform in the separating cut. The lemma includes this necessary tilt. Conditioning on the final holding time does not alter it because that holding time has the same rate for every possible starting position.

## Proposition 3.2 (prop:sep): SOUND

Lines 185–209.

The cemetery value g = 0 correctly accounts for the killing term. Substituting the exact rate deficit yields line 196 with the stated signs. The function phi in line 198 is decreasing, its integral is zeta(2), and the omitted endpoint integral bounds the Riemann-sum error at line 200.

For m at least 2r, the factorial bound and the harmonic-sum bound give the two corrections in line 204. For r < m < 2r, dropping the negative correction and bounding the positive correction gives \(0\le\delta_r(m)\le\zeta(2)+1\). The remaining range below 4r is covered by the previous bound.

Below 4r the killing intensity is greater than 1/4. In a bin with L = \(4r2^q\), there are L/2 valid targets below L, all at least 2r, whose combined intensity is at least 1/8. Monotonicity of the size makes these one-visit occupation estimates. The coefficient sum is uniform in r because \((1+\log r)/r\) is bounded for r at least 1, and the factors in q decay geometrically. Thus the integrated drift discrepancy is bounded in expectation. Only an expectation estimate is needed for this proposition. Dynkin's formula then proves the result.

For the extreme linear gap r = n-1, separation occurs at the first cut and \(\mathbb ES=1/h_{n-1}\). This is compatible with the proposition's bounded additive error, even though it is not comparable to \(\log(n/(n-1))\). No relative-error estimate is claimed.

## Lemma 4.1 (lem:rect): SOUND

Lines 213–243.

The after-cut ranks in line 217 are correct; hence the formula for G is exactly the after-cut potential difference. Interchanging the two rectangle coordinates preserves G and the weights, so s at least r may be assumed. Reflection sends i to m-i and G to -G. The reduction to weight 1/i applies to reflection-invariant quantities; the proof uses it for P squared, and correctly uses the full weight for A squared.

The harmonic bounds at line 228 imply \(Z\ge r\log(1+s/r)\). The decreasing-function moment comparison gives factorial bounds for powers of both logarithms in P. The cubic inequality at line 232 controls the mixed term without assuming independence. This proves the P bound.

For A, the first integral in line 240 is uniformly finite after scaling x by theta. For the second part, splitting j at s/2 yields the stated \(Cr^2/s\) and \(Cr^3(1+L)/s^2\) bounds. The logarithmic moment in b is controlled by the same factorial comparison. Since r is at most s, both are at most \(Cr(1+L)\), and division by Z is harmless because \(L\ge\log2\).

Both improper integrals used here converge at both endpoints. In particular this argument has no hidden dependence on s/r. At r = 1, G is identically zero; at r = s the same estimates apply with L = log 2. These cover the potentially problematic thin and balanced rectangles.

## Independent computations and outputs

The programs do not import anything from code/ or lean/. They use small arrays, one numerical thread, a 220-second wall deadline checked during loops, and a 240-second CPU limit. Observed runs were all below seven seconds and below 40 MiB peak resident memory. The saved programs, outputs, and report are far below 200 MB. The independent numerical programs were run sequentially. The original paper and author checks were left unchanged.

An initial attempt to lower process priority with `nice` was denied by the sandbox; it did not prevent execution. An initial version using NumPy matrix products emitted floating-point warnings despite finite results. I replaced those products by elementwise sums and reran the checks; the final saved output is warning-free, preserves the reported results, and agrees with the separate rational joint-moment calculation where their ranges overlap.

### referee_checks.py — referee_checks_output.txt

This program enumerates the original cut/position outcomes with fractions, computes potential losses directly from the before/after states, solves accumulated-error first and second moment recursions, and checks separation drift and rectangle moments.

Selected output:

```text
c1=1.644934066848226 c2=2.404113806319188 sigma^2=0.540143976690403
Exact beta weights, uniform-tag kernel, pair kernel, killing and separating weights: PASS; 190 pair states, m<=20
Direct original-cut drift/bracket: 12912 states; max normalized errors [1.16566914 2.13016925]
center m=65536: d1=1.6445742055 d2=2.4000289869
Accumulated error reward recursion, all positions m<=192: max L2 norms [3.88794733 7.42703052]
Separation drift from original cuts, all r<m<=64: max discrepancy 3.29e-14
Rectangle weighted moment, 64 aspect-ratio cases: max E[G^2] (4.586127509924017, (2048, 2048))
ALL INDEPENDENT CHECKS PASSED; wall_seconds=4.963 peak_RSS_MiB=36.38
```

For an independent check on the variance constant, averaging the original split rates over a uniform tag gives the size-chain rates \(q(m,k)=1/(m-k)\). Its first two logarithmic jump moments converge to

\[
\int_0^1\frac{-\log x}{1-x}\,dx=\zeta(2),\qquad
\int_0^1\frac{\log^2x}{1-x}\,dx=2\zeta(3).
\]

The program also evaluates these integrals with 45-digit quadrature. More directly, it solves the following first-step moment recursions, which do not use the positional potential:

\[
\mu_m=\frac{1+\sum_{k<m}q(m,k)\mu_k}{h_{m-1}},\qquad
v_m=\frac{\sum_{k<m}q(m,k)\{v_k+(\mu_m-\mu_k)^2\}}{h_{m-1}}.
\]

The variance recurrence follows by conditioning on the first exponential holding time and then subtracting the squared mean. The logarithmic drift and bracket predict \(v_m\sim c_2c_1^{-3}\log m\); the independent recurrence checks the normalization numerically:

| n | Variance v_n | v_n minus sigma² log n | (v_n minus v_(n/2))/log 2 |
| ---: | ---: | ---: | ---: |
| 32 | 2.787592674 | 0.915596301 | 0.565442658 |
| 512 | 4.302199996 | 0.932606525 | 0.541851567 |
| 8192 | 5.800929544 | 0.933738975 | 0.540254818 |
| 16384 | 6.175367404 | 0.933777560 | 0.540199644 |

For the accumulated errors, the program uses the reward recursions \(hA=e+\sum\lambda A_{child}\) and \(hB=2eA+\sum\lambda B_{child}\). Thus its L2 check includes random holding times and cross terms between different visits. The finite grid corroborates, but does not replace, the analytic uniform proof.

### referee_joint_moments.py — referee_joint_moments_output.txt

This independently computes every fixed-position mean and joint height moment from the original split law. At a separating cut the children's future heights are independent; before separation their joint moment is inherited from the appropriate child. If \(U_m(j)=\mathbb EH_j\) and \(V_m(j,k)=\mathbb EH_jH_k\), the recursion is

\[
h_{m-1}V_m(j,k)=U_m(j)+U_m(k)+\sum_i\lambda_m(i)T_i(j,k),
\]

where T is the child's joint moment or the product of the two children's means, as appropriate. This incorporates the shared exponential holding time exactly. I used fractions through n = 9 and floating arithmetic through n = 160.

```text
n=2 mean=1 variance=1 cyclic_covariances=1
n=3 mean=4/3 variance=4/3 cyclic_covariances=2/3
n=4 mean=17/11 variance=559/363 cyclic_covariances=1649/2178,148/1089
Fraction/float maximum joint-moment discrepancy 2.66e-15; reflection PASS
wall_seconds=0.357 peak_RSS_MiB=38.64
```

At n = 32 this gives covariance 1.878919235 at r = 1 and -0.068626290 at r = 16. At n = 160, the covariance residuals after subtracting sigma² log(n/r) are +0.017960 at r = 1, -0.700799 at r = 13, and -0.452661 at r = 80. Negative covariance near half the cycle is possible; it is not a contradiction to an additive asymptotic estimate.

### referee_simulation.py — referee_simulation_output.txt

This generates **complete trees**, not just tagged lineages. Every nonsingleton clade gets an independent exponential holding time of rate h. A finite harmonic inverse-CDF draw K with mass \(1/(Kh_{m-1})\), followed by a fair choice of cut K or m-K, has exactly the required split probabilities. No large-m approximation or asymptotic tree law is used; ordinary floating-point evaluation of the CDF and exponential draws is the numerical limitation.

The simulation measures all cyclic pairs in each tree. Separate trees are the independent units for standard errors; the n leaves are not treated as independent observations. Variance and covariance estimates are centered at the mean obtained by the independent first-step recursion. Seed: 202611140109. The full output also includes r = 2, n/2-1, and n-1; the last agrees with r = 1 tree by tree.

Here “V error” means estimated Var minus sigma² log n; “C error” means estimated Cov minus sigma² log(n/r). The SE column is the covariance standard error, not an asymptotic error bound.

| n | Independent trees | r | Estimated Var | Estimated Cov | Cov SE | V error | C error | Correlation | 1-log r/log n |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 32 | 12000 | 1 | 2.809212 | 1.893895 | 0.012350 | +0.937215 | +0.021898 | 0.674173 | 1.000000 |
| 32 | 12000 | 6 | 2.809212 | 0.256822 | 0.007948 | +0.937215 | -0.647367 | 0.091421 | 0.483007 |
| 32 | 12000 | 16 | 2.809212 | -0.065619 | 0.009884 | +0.937215 | -0.440018 | -0.023358 | 0.200000 |
| 256 | 8000 | 1 | 3.940883 | 3.029143 | 0.013349 | +0.945689 | +0.033949 | 0.768646 | 1.000000 |
| 256 | 8000 | 16 | 3.940883 | 0.789186 | 0.011033 | +0.945689 | -0.708411 | 0.200256 | 0.500000 |
| 256 | 8000 | 128 | 3.940883 | -0.070499 | 0.009573 | +0.945689 | -0.444898 | -0.017889 | 0.125000 |
| 4096 | 2500 | 1 | 5.424020 | 4.511954 | 0.022189 | +0.931228 | +0.019162 | 0.831847 | 1.000000 |
| 4096 | 2500 | 64 | 5.424020 | 1.521564 | 0.021179 | +0.931228 | -0.724832 | 0.280523 | 0.500000 |
| 4096 | 2500 | 1024 | 5.424020 | 0.095172 | 0.011561 | +0.931228 | -0.653627 | 0.017546 | 0.166667 |
| 4096 | 2500 | 2048 | 5.424020 | -0.091071 | 0.014779 | +0.931228 | -0.465470 | -0.016790 | 0.083333 |

Variance SEs are 0.014686, 0.013822, and 0.022223 for n = 32, 256, and 4096 respectively. At n = 4096 the exact-recursion variance is 5.426453440. Across these sizes, the largest absolute displayed covariance error divided by sqrt(log n) is approximately 0.348, 0.301, and 0.251 respectively; the corresponding variance ratios are 0.503, 0.402, and 0.323. The observed errors are consistent with the theorem, although the finite-n correlations remain substantially below their limits. These finite experiments do not prove the claimed uniform estimates.

```text
PASS mean/variance calibration and offset reflection; wall_seconds=6.894 peak_RSS_MiB=27.55
```

## Corrections

No correction is required for the theorem, corollary, lemmas, or proposition.

One wording clarification concerns line 86: if “is of order 1/log n” is intended to assert a sharp, two-sided rate, replace it by “would be O(1/log n).” Bounded covariance and variance errors imply that upper bound after division, not a nonzero lower bound. This does not affect any proved result; the passage is presented as numerical speculation.

## Citation and formal-check audit

The bibliography's external papers are not supplied here. Under the instruction not to browse, I cannot certify their exact theorem wording, version numbering, or bibliographic metadata. The distinction below is between what the manuscript uses and what can actually be checked from the supplied text.

| Reference | Use in this paper | Assessment |
| --- | --- | --- |
| Aldous 1996 (Ald96), lines 44 and 338–339 | Identifies beta = -1 in the beta-splitting family. | The beta-weight calculation above independently confirms compatibility. No external theorem from it is needed in the proof. |
| Aldous–Janson II (AJ), lines 44, 54–63 and 340–341 | Interval model; statement of the open problem; historical comparison at alpha = 1. | Consistent with the problem supplied for this review, with the explicit shortest-offset qualification. Exact quotation and source numbering remain unverified offline. |
| Aldous–Pittel (AP), lines 44, 52, 63 and 346–347 | Model, known one-leaf mean/variance, and a result on uniformly sampled pairs. | The model and constants are independently checked here. Theorem 1.1 does not invoke the uniform-pair result to cover fixed macroscopic offsets. Such an implication would require justification, but it is not a step of this proof. The arXiv numbering qualification at line 347 is explicit. |
| Aldous–Janson IV (AJ4), lines 52, 289 and 343–344 | Historical constant-term results and the comparison constant zeta(3)/zeta(2)^2 + gamma/zeta(2). | Used only as context and numerical comparison. The independent mean recursion agrees with the stated constant; the source itself was not available for inspection. |
| Kolesnik (Kol), lines 52 and 352–353 | Background assertion of a CLT. | Not used in the proof. The external statement is unverified offline. |
| Iksanov–Nikitin–Yakymiv (INY), lines 52 and 349–350 | Background assertion of a joint discrete/continuous CLT for a uniform leaf. | Not used in the proof. The external statement is unverified offline. |
| MathBrainRepo, MathBrainPaper, BrainFramework, lines 321 and 334–359 | Describes research infrastructure and provenance. | None is used as a mathematical premise. Provenance claims and external repositories were not independently checked. |

The supplied Lean file proves elementary algebra, a few integer inequalities, and polarization. It does not formalize the probabilistic conditioning, occupation bounds, rectangle integrability, optional stopping, or the main theorem. The paper's description at line 308 confines its role to those finite/algebraic checks and does not claim a formal proof of the theorem. I checked the relevant identities independently; the saved Lean log is author-supplied evidence, not an independently reproduced compilation. Likewise, the finite grids in the authors' code cannot establish uniformity in unbounded parameters; the analytic arguments above do that work.

Task: “You are refereeing a mathematical paper that has been posted.” Review begun 2026-11-14 at approximately 01:08, Asia/Tbilisi; the exact incoming-message time was not exposed.
