MINOR

Theorems 1 and 2 withstand this audit. I found no counterexample and no mathematical gap requiring repair in their proofs. In particular, the arbitrary remainder is genuinely absorbed, the reservoir marginals are recovered with the correct size weighting, the weak-limit argument has the needed compactness and convergence of centers, and the convolution argument covers odd as well as even dimensions. The constant in (1) is sufficient as printed. The recommendation is MINOR for reproducibility defects in the supplied bundle, not for a defect in either theorem.

The affirmative result is already in the November 2026 the author repository identified by the submission. CLAIM.md explicitly credits it, so this is a verification and exposition of that result rather than a second discovery. Yin–Zhu's asserted counterexample addresses exactly the same question and is absolutely continuous; its universal nonmixability assertion is incompatible with the valid construction audited here.

Errors and gaps requiring correction

1. **Reproduction working directory.** CLAIM.md, Section 6.5, lines 414–425 says to run commands “from this folder,” but the scripts and data are in `claim_files/`, whereas CLAIM.md is in its parent. For example, `python3 numerics.py --self-check` from the submission directory fails to locate the script. Required fix: explicitly begin that block with `cd claim_files`, or give paths and working-directory instructions for the submitted layout. I did not execute or reuse those scripts.

2. **Source-archive manifest differs from the supplied files.** CLAIM.md Section 6.5, line 412, and `claim_files/sources/manifest.json` / `SHA256SUMS` refer to `wang_survey.pdf`, `wang_wang_2011.pdf`, `wang_wang_2016.pdf`, and `detection.pdf`; none of those four PDFs is in the supplied source directory. Text extracts are present. Required fix: distinguish externally retrieved originals from bundled files and provide retrieval/hash-check instructions, or include the listed PDFs. This does not undermine the proof: I independently retrieved the 2011 PDF and checked the other relevant primary sources online.

There are no additional mathematical errors or proof gaps in Theorems 1–2 that I can substantiate. The observations below explain the checks, including places where a superficially similar argument would fail but the submitted argument does not.

Theorem 2: detailed verification

**Input theorem and Lemma 4 (lines 84–103).** The Wang–Wang result concerns a probability law whose density is monotone on its bounded support interval, with density zero outside, and the mean condition
\[
u+(v-u)/k\le m\le v-(v-u)/k.
\]
Their Theorem 2.4 states the decreasing-density case on [0,1]; Corollary 2.9 and Remark 2.3 give the increasing/decreasing versions and necessity when the endpoints are those of the support hull. Neither symmetry nor strict positivity at both endpoints is a hypothesis. I checked the actual text in an independently downloaded [2011 author manuscript](https://sas.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf), now saved under `audit_sources/`.

For the submitted linear density, integration gives mass 1 and mean beta H/3. It is nonnegative for |beta|<=1 and increasing, decreasing, or constant according to beta's sign. Its support hull remains [-H,H] even when it vanishes at one endpoint. The mean condition becomes
\[
|\beta|H/3\le H-2H/k,
\]
which holds for every k>=3, including equality when k=3 and |beta|=1. The input theorem is used only on these conditional linear densities, never on the possibly atomic or singular remainder.

**Lemma 5 (lines 105–110).** For each coordinate, randomizing the stratum index uniformly makes (sigma(i)+W)/k uniform on (0,1). Random permutation gives exchangeability. For every stratum, the sample quantile and the stratum's average quantile both lie between its endpoint quantiles. The sum of these interval lengths telescopes to at most R. Consequently |S-k m_T|<=R, while E S=k m_T follows separately from the marginals. Atoms and gaps cause quantile jumps but do not invalidate this bound. Finite endpoint values can be assigned consistently with monotonicity. The k=0 case is supplied separately in Proposition 6.

**Decomposition (line 119).** For q<1,
\[
T=(G-qU[c-H,c+H])/(1-q)
\]
is a nonnegative probability measure supported in the same compact interval as G. This uses measure domination, not an assertion that G has a density. Also [c-H,c+H] lies inside that interval, so 2H<=R and |m_T-c|<=R. For q=1, G is exactly the uniform law and the harmless choice T=delta_c receives zero positions. There is no division by 1-q in that case.

**Random counts (lines 121–126).** Writing m=N(1-q), randomization between floor(m) and ceil(m) gives E K=m and |K-m|<1 for every value having positive probability. These counts are valid nonnegative counts of positions. Under (6),
\[
M=N-K>Nq-1\ge 3(2R+L)/H\ge12.
\]
Thus at least 13 reservoir positions are available, more than the three needed for Lemma 4. The strict inequality remains valid when m is an integer, and at the printed non-strict threshold for N. Conditional sampling of the remainder is independent of the chosen set of positions, as required for the later marginal calculation.

**Error absorption (lines 128–140).** Recomputing the algebra gives
\[
C=(m-K)(m_T-c)-(S-Km_T)-(Y-m_E).
\]
The three absolute errors are bounded respectively by R, R, and L. Hence |C|<=2R+L and beta=3C/(MH) satisfies |beta|<=1. Lemma 4 supplies M variables with the specified linear density and sum M beta H/3=C. It follows pathwise that
\[
S+Mc+C+Y=N\mu+m_E.
\]
This explains exactly how the remainder is handled: its joint sum is balanced to within R by a quantile construction, the count error costs another R, and linear tilts of the selected uniform positions absorb the total. No regularity of T is used.

For finite-support T and E there are finitely many possible (K,S,Y), even though W is continuous. A coupling for each possible linear tilt can therefore be chosen from a finite list. The proof does not smuggle in an unproved measurable-selection step. Each chosen coupling must have the stated linear density in every coordinate, which is exactly what complete mixability supplies. Conditional laws of the remainder given its sum need not equal T, and the argument does not assume that they do.

**Marginal recovery (lines 142–152).** This is the most delicate step, and it is correct. A coordinate is selected for the remainder with probability E K/N=1-q, and its integrated contribution is (1-q)T. A reservoir coordinate sees the distribution of beta biased by the number M of reservoir positions. Its contribution is
\[
E\left[\frac{M}{N}\ell_{H,\beta}(z)\right]
=\frac{E M}{2HN}+\frac{z}{2H^2N}E[M\beta]
=\frac{q}{2H}.
\]
Indeed M beta=3C/H and E C=0, using E[S|K]=K m_T and E K=m. Unweighted E beta=0 would generally be false and would not justify the claim. The submission explicitly uses the weighted identity. My exact-rational check even produced a valid input with E beta=3/4940 while E[M beta]=0. Thus every coordinate has exactly G, rather than merely a matching mean or an approximately uniform reservoir component.

**Approximation and closure (lines 154–159).** The closure statement actually needed is the following fixed-dimensional joint version: if marginal laws P_ij converge weakly to P_i, their couplings pi_j have constant sums c_j, and all coordinates lie in fixed compact intervals, then, provided c_j->c, a subsequential limiting coupling has marginals P_i and sum c. Compactness gives a tight family of couplings. Marginal projections are continuous. For the bounded continuous function h(x)=(sum x_i-c)^2 on the compact product,
\[
\int h\,d\pi=\lim_j\int h\,d\pi_j
=\lim_j(c_j-c)^2=0.
\]
This proves the closure assertion directly. The familiar fixed-center n-CM weak-closure result is [Puccetti–Wang–Wang (2012), Theorem 3.1](https://sas.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf); the direct argument also handles the changing centers here.

All hypotheses hold: the dimension N+1 is fixed during the limit; T_j and E_j stay in their respective original compact intervals; G_j retains the same uniform component and q,H,R; and compact support implies convergence of their means, hence of c_j=N mu_j+m_Ej. One must not infer convergence of means from arbitrary weak convergence, or approximate all of G in a way that loses its uniform component. Neither error occurs here. The extra law's interval need not be inside G's interval.

**Constant and q dependence (lines 114–161).** With L=0 the required reservoir capacity is M H/3>=2R. The inequality M>Nq-1 explains both terms in
\[
n\ge (6R/H+1)/q.
\]
The factor 6 is 3 times the two R errors; the extra 1 covers integer rounding; 1/q converts expected reservoir count into total count. No further factor of q is lost in the marginal calculation. Since n is integral, the usable threshold is ceil((6R/H+1)/q). The bound is deliberately conservative. The endpoint-atom example below proves that order 1/q is unavoidable. Translation, reflection, and common scaling leave the condition consistent.

Theorem 1 and recovery of the original marginals

Lemma 7 (lines 165–172) is valid for any nonzero absolutely continuous part. The truncated density g=min(f,B) belongs to L1 and Linfinity, is nonzero, and F dominates g dx. Thus F*F dominates (g*g) dx. The submitted translation estimate proves continuity of g*g; its integral is (integral g)^2>0. Nonnegativity and continuity give an interval on which g*g>=delta>0. Setting q=2H delta is legitimate and automatically q<=1. The density of F need not contain any interval on which it is bounded below. This smoothing step is what covers positive-measure supports with no interior, as well as atoms and singular components added to such densities.

Lemma 8 (lines 174–176) is also valid. On these standard Borel spaces, take the regular conditional law kappa(s,du,dv) of an independent F pair given its sum. It is supported on u+v=s for F*F-almost every s. Mixing kappa against the F*F marginal recovers F tensor F, hence each original marginal F. Each block sum P_j has that marginal even though the different blocks are dependent. Its exceptional kernel set therefore has probability zero; the finite union over blocks is still null. Conditional sampling of all the pairs preserves every block sum. Independence within the unconditional pair is recovered automatically; independence between blocks is neither required nor asserted.

For the final thresholds, substitute R_G=2R into Proposition 6. Even blocks require a>=(12R/H+1)/q. Odd dimensions use the extra original law E=F, L=R, so a>=(15R/H+1)/q. If A=ceil((15R/H+1)/q), every n>=2A has floor(n/2)>=A. Thus (10), N(F)=2A, really covers both parities; an argument proving only even dimensions would not have been enough. Here q,H describe the uniform component of F*F, not necessarily that of F itself.

The supplementary norm argument in Proposition 3 also checks out: for u in [-M,M], lambda d>=d+M gives the two stop-loss inequalities used there; outside that interval the stated zero/Jensen bounds apply. Equal means and stop-loss domination give the convex-order comparison. It implies all of the claimed Lp inequalities. It does not establish sufficiency of these necessary conditions, and the submission does not claim that it does.

Independent numerical work and stress laws

I wrote `independent_checks.py` and `audit_supplement.py`. Neither reads, imports, copies, or runs a program from `claim_files/`. The main LP uses integer-programming pricing rather than the submitted dynamic-programming implementation; supplemental three-variable refinements enumerate all admissible sorted triples. All LPs use floating-point HiGHS; the numerical dual bounds are not interval-arithmetic certificates. For each cell j the LP keeps a mass p_j and lower/upper endpoints l_j,u_j, with exact point cells for atoms. A possible occupation vector k must satisfy
\[
\sum k_j=n,\qquad\sum k_jl_j\le n\mu\le\sum k_ju_j.
\]
Columns are k/n, and the LP minimizes the L1 marginal error. Mixed-integer optimization searches all admissible count vectors for a negative reduced-cost column. A pricing-corrected dual lower bound accompanies exclusions. Twenty-five small pricing cases were checked against exhaustive enumeration. The uniform positive control and an endpoint-mean negative control passed.

The independent rearrangement algorithm uses 4,000 midpoint quantiles, two seeded restarts, and up to 35 sweeps. The n=1210 case uses 1,000 rows and six sweeps. RMS refers to the error of the row sum from n times the true mean. Exact atoms are retained. This avoids replacing an atom by a uniform cell or mistaking sample mean drift for variance. The 50-term numerical evaluation of the Yin–Zhu geometric mixture omits total weight 2^-50 before normalization; its CDF error is at most that order.

The main run has 43 cases: 39 LPs (17 exclusions, 2 with no admissible tuple, and 20 outer-feasible) and 43 rearrangements. Maximum LP primal residual was 7.33e-15. The exact reservoir integration covered 24 rational inputs and 178 finite states, with zero failures. The final run took 66.8 seconds and peaked at 179,453,952 bytes of resident memory. Solvers and numerical libraries were limited to one computational thread; no worker pools or subagents were used. Data are in `independent_results.json` and `.csv`; refinements and structured controls are in `supplement_results.json`.

The supplemental full-enumeration LP independently reproduces the 80-bin quadratic result using all 3,280 admissible sorted triples. At 160 bins, all 12,960 such triples give optimum 0.331766471354, versus 0.321433854167 at 80 bins and the continuous middle-mass lower bound 41/120. Structured endpoint-atom controls at n=20 and 40 and the distant-uniform control at n=20 have zero row-sum error and quantile marginal error at most 2.23e-16. Exact rational pair disintegration recovers all four original marginals for F=(delta_0+2 delta_1+delta_2)/4. Additional rearrangements test nonintegral expected reservoir counts: q=0.1,n=131 gives RMS 8.68e-4; q=0.07,n=186=ceil(13/q) gives 1.13e-3; and the distant uniform law at n=1211 gives 4.52e-4. These remain heuristic positive checks. The completed supplement took 43.4 seconds and peaked at 143,687,680 bytes. The log retains unsuccessful optional finer-grid attempts, from which no numerical conclusion is drawn.

| Law on [0,1] | Parameters in (1); sufficient N | Independent results |
| --- | --- | --- |
| 0.9 delta_0 + 0.1 U[0,1] | R=1,H=1/2,q=0.1; N=130 | LP excludes n=10,19; passes at 20,21,30. RA RMS at 19 is 9.94e-3, at 20 is 4.16e-3, at 130 is 8.72e-4. |
| 0.95 delta_0 + 0.05 U[0,1] | R=1,H=1/2,q=0.05; N=260 | LP excludes 20,39; passes at 40,41. RA RMS is 7.02e-3 at 39 and 1.76e-3 at 260. |
| f(x)=1/10+(27/10)(2x-1)^2 | R=1,H=1/2,q=0.1; N=130 | LP excludes n=3 with lower bound 0.321434 at 80 bins; passes at 4,5,7,15,30. RA RMS: 0.156828 at 3, 5.64e-5 at 4, 2.86e-5 at 130. |
| 0.9 delta_0 + 0.1 U[0.9,1] | R=1,H=0.05,q=0.1; N=1210 | No admissible tuple at n=9,11. LP excludes 10,19,21,29,31; passes at 20,30,100. RA RMS: 0.269211 at 19, 1.62e-4 at 20, 4.56e-4 at 1210. |
| 0.49 delta_0+0.49 delta_1+0.02 U[0.4,0.6] | R=1,H=0.1,q=0.02; N=3050 | LP excludes odd n=3,15,49,51; passes at even 4,50,150. A coarse LP also passes at 149, although the analytic argument below excludes it. |
| Rescaled Yin–Zhu mixture, alpha_m=2^-m | R=1,H=1/16,q=1/(8 pi sqrt(3)); N=4223 | LP excludes odd 3,5,7; passes at 11,21. RA RMS is 0.139445 at 7, 9.48e-6 at 11, and 3.67e-6 at 21. |

Here “passes” means only that the outer LP has zero marginal error. Neither that nor a small rearrangement residual proves a continuous coupling. Conversely, an unstructured rearrangement can stall even when an exact coupling is known. This distinction matters in these actual results, not just in principle.

For F=(1-q)delta_a+q U[a,b], affine normalization gives mean q/2 and support hull [0,1]. Necessity gives n>=2/q. This threshold is exact for integers n>=2: approximate the endpoint atom by U[0,epsilon]. The resulting decreasing density has mean (q+(1-q)epsilon)/2 and satisfies the monotone mean condition whenever n>=2/q, for sufficiently small epsilon. Compact weak closure gives the original mixture. Thus the exact thresholds in the first two rows are 20 and 40, versus sufficient 130 and 260. At n=20,q=0.1 there is an even simpler exact construction: select two positions uniformly, fill them by U and 1-U, and put zeros elsewhere. The structured finite-quantile version checks every marginal and the constant sum directly, despite the unstructured RA residual above.

For the quadratic law, direct integration gives
\[
P(1/4<X<3/4)=1/20+9/80=13/80<1/3.
\]
Any triple with sum 3/2 must have a coordinate in that middle interval, apart from zero-probability boundary cases: two coordinates below 1/4 make the sum less than 3/2; two above 3/4 make it greater. Hence 3-CM would require middle probability at least 1/3, a contradiction. Formula (1) gives 130, not 3, so there is no inconsistency. The older full-support lower-density theorem already gives the sharper sufficient 30 here. Symmetry supplies all even dimensions, including 2 and 4.

For the distant-uniform law the mean is 0.095, far from its uniform center 0.95. If K counts nonzero coordinates, a constant sum requires
\[
0.9K\le0.095n\le K,\qquad E K=0.1n.
\]
These requirements explain all listed exclusions, including cases satisfying the simple necessary mean condition. For example, at n=19 only K=2 is allowed, contradicting E K=1.9; at n=21 only K=2 is allowed, contradicting E K=2.1. At n=20 choose two positions and use U and 1.9-U in them. At 30 and 100, choose respectively three and ten uniform positions and use complete mixability of the uniform law there. The theorem tolerates the large displacement because it budgets the bounded count and sum errors; it never assumes the uniform interval contains the overall mean.

For the atomic-endpoint/thin-middle law, every odd-dimensional constant sum n/2 needs middle coordinates. K=0 is impossible by parity. K=1 forces the lone continuous coordinate to equal 1/2, an event of probability zero; K=2 has middle sum in [0.8,1.2], which cannot be a half-integer. Thus K>=3 almost surely and 0.02n=E K>=3. In particular every odd n<150, including 149, is impossible. The coarse LP's feasibility at 149 is a real discretization false positive. It does not challenge the sufficient 3050. This example checks an arbitrary atomic remainder and a gap simultaneously.

Literature and novelty

The original question is indeed Open Problem 7, Section 2.6, of [Wang's 2015 survey](https://arxiv.org/abs/1411.6190). It asks eventual complete mixability of absolutely continuous distributions on bounded intervals. Theorem 1 answers it affirmatively and is stronger because positive absolutely continuous mass suffices.

| Primary source | What it establishes or claims; relationship to this submission |
| --- | --- |
| [Wang–Wang (2011)](https://sas.uwaterloo.ca/~wang/papers/2011Wang-Wang-JMVA.pdf), Theorem 2.4 / Corollary 2.9 | Monotone-density complete mixability under the mean condition. It supplies the linear-tilt input. It does not cover an arbitrary remainder or arbitrary bounded densities. |
| [Puccetti–Wang–Wang (2012)](https://sas.uwaterloo.ca/~wang/papers/2012Puccetti-Wang-Wang-JAP.pdf), Theorem 3.1; [2013 paper](https://doi.org/10.1016/j.insmatheco.2013.09.017), Theorem 3.4 as identified in the author catalogue | Weak closure and classical sufficient conditions, including a density lower bound over the whole support interval. The submitted theorem permits a lower bound on just one subinterval, arbitrary remainder, and then removes even that local condition by convolution. |
| [Wang–Wang (2016), Joint Mixability](https://doi.org/10.1287/moor.2015.0755), Theorem 3.2 | Joint mixability for densities all decreasing, or all increasing by reflection, under the joint mean inequality. This is a later generalization of the input, not the eventual arbitrary-density theorem. The submission's two-band n=19 construction uses it correctly: each conditional family has a common direction of monotonicity and its displayed endpoint/mean inequalities hold. |
| [Yin–Zhu, arXiv:1706.05499v4](https://arxiv.org/html/1706.05499v4), Example 2.4 | Makes a negative claim about this very question, for the fully absolutely continuous mixture analyzed below. It is not a singular counterexample, a different open question, or merely an obstruction in one fixed dimension. |
| [Komisarski–Labuschagne, online 25 September 2023, J. Theoret. Probab. 37 (2024), 2121–2129](https://doi.org/10.1007/s10959-023-01277-2), Theorem 1 | For a bounded Borel set B, constructs one marginal law such that, for every n>=3, arbitrary prescribed laws on B can be realized as the distribution of the average. It does not say that an arbitrary given bounded marginal becomes n-CM. For B containing distinct possible constant averages, their universal marginal cannot have a finite first moment; their construction uses unbounded marginals. Its quantifiers and support condition are different. Theorem 1 here is a new conclusion relative to that paper. |
| [Koike–Lin–Wang, arXiv:2204.11438v4](https://arxiv.org/html/2204.11438v4), published 2024 | Studies compatibility of joint mixes with negative dependence and related transport problems. It does not establish eventual complete mixability of all bounded absolutely continuous laws. |
| [the author repository, pinned commit 4bd67dbdd5b621c08a813b909d10219d4dd2d18f](https://github.com/yspennstate/complete-mixability-large-n/blob/4bd67dbdd5b621c08a813b909d10219d4dd2d18f/paper/paper.tex), commit dated 11 November 2026 | Already contains both main theorems, the exact (6R/H+1)/q bound, the extra-variable proposition, quantile coupling, weighted tilt recovery, convolution, disintegration, and the Yin–Zhu contradiction with the same constants. No main theorem or proof mechanism in CLAIM.md is new relative to this manuscript. |

I retrieved the pinned repository file and commit independently through the connected GitHub service. The stored source is `audit_sources/prior_paper.tex`; the returned blob SHA is `eeca6ff94d51a38ded3cb9be4e1191548dd0de65`. The submission's principal additions relative to it are the Lp stop-loss analysis, the sharp two-band example, and numerical tables and refinements. This is a statement of differences, not a verified priority claim for every supplementary result. The submission's rounded all-parity threshold is consistent with the repository's real-valued threshold and the same block argument.

Searches on 13 November 2026 covered exact open-problem wording, “absolutely continuous,” “bounded interval,” “eventual,” “large n,” the specified authors, and 2016–2026 combinations. I checked [Wang's working-paper catalogue](https://www.math.uwaterloo.ca/~wang/pages/WPS3.html), which includes 2025 work, and the primary papers above. A 2026 [Martinevski preprint page](https://math.a-martinevski.com/publications/P02/) concerns characteristic-function optimization and particular uniform/spline marginals, not this general assertion. Apart from the identified the author manuscript, I located no 2016–2026 paper or repository proving the same general affirmative statement. This bounded search cannot certify the nonexistence of unindexed work, and a repository posting is not evidence of journal acceptance.

Yin–Zhu reconciliation in detail

Their v4 was revised 11 May 2023. Example 2.4 defines normalized densities
\[
f_m(x)=C_m x^{2m}/\sqrt{1-x^2},\quad -1<x<1,
\qquad f=\sum_{m\ge1}\alpha_m f_m,\quad\alpha_m>0,\ \sum\alpha_m=1,
\]
then asserts failure in every odd dimension and identifies this as a counterexample to Wang's question. This is a genuine conflicting assertion about an absolutely continuous probability law. The series defines a density by Tonelli; endpoint singularities do not create atoms.

Here is an explicit reconciliation, rather than reliance on publication status. C_1=2/pi, and f_1 is increasing on (0,1). At x=1/2 it equals 1/(pi sqrt(3)). Therefore
\[
F\ge\frac{\alpha_1}{4\pi\sqrt3}\,U[1/2,3/4].
\]
Substitution of R=2, H=1/8 into the independently verified Theorem 2 gives
\[
n\ge(96+1)\frac{4\pi\sqrt3}{\alpha_1}
=\frac{388\pi\sqrt3}{\alpha_1}.
\]
Thus the claimed failure in every odd dimension is false. This is the same calculation in CLAIM.md, and its constants are correct. For alpha_m=2^-m the integer bound is 4223, while numerics already become compatible with mixing at odd 11 and 21; those numerical observations alone do not prove mixing there.

The finite-dimensional obstruction in their preceding Example 2.1 needs the central probability P(|X|<=r/(r+1)) to be at most 1/(2r+1). For any fixed one of these absolutely continuous mixtures, the former tends to 1 and the latter to 0. Changing the density with r can produce successively harder finite-dimensional examples, but does not produce one fixed counterexample for all large dimensions. Example 2.4 supplies no proof of that missing quantifier step. Failure of a sufficient obstruction alone would not prove mixability; the reservoir construction above is what supplies the positive proof.

As an additional issue in the external source, Example 2.1 turns a non-strict CDF hypothesis into a strict tail inequality without justification. Its equality case is actually false as stated. Take independent U uniform on [0.9,0.99] and V uniform on [-0.01,0.01], and randomly permute (U+V,-U+V,-2V). These three variables sum to zero and have a common symmetric density, with support hull [-1,1]. Exactly one coordinate lies in [-1/2,1/2], so the common CDF has F(1/2)=2/3, satisfying their n=1 non-strict hypothesis, despite being 3-CM. This separate equality defect is in Yin–Zhu, not in CLAIM.md; it is not needed to validate Theorems 1–2.

All work stayed in this directory; no publication or remote mutation was performed. To reproduce my checks, run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 independent_checks.py`, then the same prefix with `python3 audit_supplement.py`. No conclusion above relies on a feasible discretization as an exact continuous existence proof.

Task: “Your job is to break it if it is wrong” — received 13 November 2026, 03:04 Asia/Tbilisi (local audit-start clock).
