# Referee log

Task: “refereeing a short mathematical paper before it is made public”; started 2026-11-12 03:36 +04. PAPER.tex will remain unchanged. All generated artifacts stay in this directory. No network, agents, or external writes. The later task-specific restriction overrides the global mesh/checklist/brain writes; startup notes and compute status were read without running those writers. Computations run sequentially, single-threaded, at nice 10, with a 285-second process alarm.

## Step 1 — free setup
CORRECT: variance-t semicircle normalization, boundary height, homeomorphism and density formula agree with the subordination convention G(z)=E[(z-X)^(-1)], G=G_mu(z-tG). At v_t=0 the expectation in psi is absolutely integrable by Cauchy–Schwarz from E[(u-X)^(-2)]<=1/t. The semicircle and both two-atom checks agree; largest density discrepancy 9.14598e-14 (double precision; see step1.json). Numerical checks support, rather than establish, the cited general boundary theorem.

## Step 2 — classical proof
CORRECT: density normalization and g-prime=H/t; [eq:Hprime] and bounded differentiation; [lem:c-window], Jensen, split and Chebyshev (exp(-1/32)+16/600=0.995899901143 < .9960 < exp(-1/1200)=0.999167013792); [lem:c-slope], both cases of (1-z)exp(-z/2)>=1-3z/2, and 5/8-1/400=.6225>1/2. CORRECT: existence by continuity/decay, exclusion outside the window, Fermat stationarity even at window endpoints, strict decrease of H, [eq:c-mvt], [eq:c-H0], and both minimum bounds. Therefore [thm:classical] is CORRECT.

CORRECT (numerical corroboration): 320 random atomic laws at each of t/v=600,5000, plus centred exponential and Student t(4). No bound violation or duplicate global maximum observed. Full ratios in step2.json. Smallest positive ratio tested was .01; this is an observation on this finite sample, not a uniform uniqueness threshold. nice(10) was denied by the sandbox; these small single-threaded processes ran sequentially with their 285-second alarms.

## Step 2 — classical proof
CORRECT: density normalization and g-prime=H/t; [eq:Hprime] and bounded differentiation; [lem:c-window], Jensen, split and Chebyshev (exp(-1/32)+16/600=0.995899901143 < .9960 < exp(-1/1200)=0.999167013792); [lem:c-slope], both cases of (1-z)exp(-z/2)>=1-3z/2, and 5/8-1/400=.6225>1/2. CORRECT: existence by continuity/decay, exclusion outside the window, Fermat stationarity even at window endpoints, strict decrease of H, [eq:c-mvt], [eq:c-H0], and both minimum bounds. Therefore [thm:classical] is CORRECT.

## Step 2 — classical proof
CORRECT: density normalization and g-prime=H/t; [eq:Hprime] and bounded differentiation; [lem:c-window], Jensen, split and Chebyshev (exp(-1/32)+16/600=0.995899901143 < .9960 < exp(-1/1200)=0.999167013792); [lem:c-slope], both cases of (1-z)exp(-z/2)>=1-3z/2, and 5/8-1/400=.6225>1/2. CORRECT: existence by continuity/decay, exclusion outside the window, Fermat stationarity even at window endpoints, strict decrease of H, [eq:c-mvt], [eq:c-H0], and both minimum bounds. Therefore [thm:classical] is CORRECT.

CORRECT (numerical corroboration): 320 random atomic laws at each of t/v=600,5000, plus centred exponential and Student t(4). No bound violation or duplicate global maximum observed. Full ratios in step2.json. Smallest positive ratio tested was .01; this is an observation on this finite sample, not a uniform uniqueness threshold. nice(10) was denied by the sandbox; these small single-threaded processes ran sequentially with their 285-second alarms.

## Step 3 — free proof
CORRECT: [lem:f-max], convex Jensen at positive t-v, positivity and root monotonicity, decay via domination by delta^(-2), attainment, R*<=t, and equality characterization. If v_t=0, compare R* with R*/2 to obtain the strict inequality. CORRECT: [eq:f-mass] and [lem:f-window], Chebyshev >=1/2, b^2(t-2v)<=2vt, hence b^2<=4v. CORRECT: [lem:f-concave], second derivative, exact polynomial identity, R*>=t-v>(7a-1)v>6av since a>1.
CORRECT: uniqueness follows from strict concavity plus the common global upper bound 1/t; [eq:f-stat], [eq:f-u], [eq:f-M], R*>=6t/7, both rational minimum inequalities, quadratic and cubic moment bounds, and [eq:f-u3]. The first arithmetic factor is 3.939710014258<4; 77K/12=(77/3)(B^3+beta3)<26(B^3+beta3). The coefficient 26(21+14sqrt(2))=1060.773736703807<1061. Thus [thm:free] is CORRECT.

CORRECT (numerical corroboration): 320 atomic laws and centred exponential at both requested free times; all global counts are one, window and R inequalities and both location bounds pass. CORRECT: the named three-atom example has two local maxima at t=233.636121605; see step3.json for both positive peak heights. This establishes the claimed phenomenon for that law at this tested time.

## Step 4 — remainders and expansions
CORRECT: exponential rho lies in [0,min(x,x^2/2)] and |rho_3|<=x^3/6. CORRECT: [eq:exp1], exact geometric remainders; [eq:exp2], nonnegative rho_2<=min(2z,3z^2) and |sigma_2|<=4z^3 by Taylor bounds. CORRECT: classical dominated convergence uses (|Y|+1)^3/2. Free rho_2 term after division by s is dominated by a fixed multiple of (|Y|+B)^3 since r>=1/2 eventually; rho_1 uses the same integrable envelope. In each case the minimum tends to zero pointwise and q converges to the centred Y or its negative.
CORRECT: part (b) classical remainder uses seventh absolute moment; free mass remainder uses sixth, stationarity and location remainders use seventh. Bounded shifted moments are justified by the earlier O(s) displacement bounds. [eq:c-moments], [eq:f-moments], [eq:f-system] and every substitution yield the claimed coefficients, subject to the moment qualifications noted below.

CORRECT (independent symbolic derivation): classical coefficients -mu3/2 and (mu5-6v mu3)/8; free u coefficients -2mu3 and 3mu5-14v mu3; free location coefficients -3mu3 and 5mu5-22v mu3. The mass expansion r=1-vs+(mu4-v^2)s^2 is correct. Classical/free fifth cumulants have partition counts 10/5; both introductory cumulant forms are correct. Exact formulas and independently derived third-order limits are in step4_symbolic.json.

CORRECT (numerical corroboration): 70-digit arithmetic on four distinct asymmetric laws, t=10^4 through 10^8, saved with 60 significant digits. Scaled two-term errors approach the independently derived third coefficients; maximum equation residuals are recorded in step4_highprecision.json.

CORRECT (part (a) numerical corroboration): centred Pareto(shape 4), mu3=20/27, finite third but infinite fourth/fifth moment. At t=10^9, t(M_c-m)=-0.370317558125 and t(M_f-m)=-2.22142860423, approaching -10/27 and -20/9; details in step4_heavy_tail.json.

## Step 5 — corollaries
CORRECT: [cor:HU], Jensen gives E X^2<=log(alpha)/eps, hence v<=L and |m|<=sqrt(L). Maximizing x^k exp(-eps x^2) gives the stated absolute-moment bound; |X-m|^3<=4(|X|^3+|m|^3) and |m|^3<=E|X|^3 give beta3<=Q. Finite exponential-square moment supplies beta7. Both combined classical thresholds and the strict free threshold transfer correctly. CORRECT: for a continuous density, any unimodality mode has density at least that at every other point by monotonicity and continuity; unique global maximum therefore gives a unique mode. This uses unimodality as a separate hypothesis.
CORRECT: [cor:compact], v<=D^2/4 (variance minimizes squared distance), mean lies inside the support interval, |Y|<=D, beta3<=Dv<=D^3/4. 7a/4=22.14949493661166534161182<23, and 26((2+sqrt(2))^3/8+1/4)=135.8467170879758247204768<136. The stated thresholds exceed the cited 4D^2 threshold; compact support supplies all moments. These conclusions use HU unimodality results as cited; source attribution is considered in Step 7.

## Step 6 — example and Table 1
CORRECT: exact rational moments m=0, v=2, mu3=2, mu5=10; the expansions are -1/t-7/(4t^2) and -6/t-38/t^2. All twelve entries in Table 1 agree with independent 80-digit root computations at their displayed precision. Full values are in step6.json. The t=1000 classical entry is below the sufficient uniqueness threshold 600v=1200, so it needs separate justification; for this two-atom mixture t=1000 is globally strictly log-concave, because (log density) double-prime=-1/t+Var_t(X)/t^2 <=-1/t+9/(4t^2)<0. The free sufficient threshold already applies at all three rows.

## Step 7 — introduction, references and novelty (memory only)

CORRECT as far as I can assess from memory: the variance convention and general Biane description; Hasebe–Ueda's compact-support/free and exponential-square/classical sufficient unimodality results are consistent with the cited statements, as are the non-unimodality counterexample descriptions. GAP (verification only): I cannot certify the exact theorem/proposition numbering, weak endpoint inequalities, verbatim Problem 4.6 quotation, equation numbering in HU, bibliographic metadata, or DOI strings without the source. No source was browsed. These are audit limitations, not demonstrated errors in the cited results.

CORRECT: Haldane's nearly normal mode relation and Hall's sum-mode context make the attribution of mean minus mode approximately kappa3/(2kappa2) fair. This is an asymptotic relation under appropriate regularity, not a statement for every distribution described as nearly normal. CORRECT: the Chistyakov–Goetze attribution of asymptotic expansions in the free CLT is fair at this level of generality. GAP (verification only): precise hypotheses, priority and metadata cannot be authenticated from memory.

GAP (novelty verification): I know no specific prior theorem giving these free mode coefficients, these explicit finite-variance uniqueness thresholds, or the full fixed-law large-time location statements. I do know the classical leading cumulant relation is old; neither that fact nor my lack of a remembered matching free result proves novelty. A literature search would be needed for a priority claim, and was prohibited here.

## Presentation and reproducibility findings

GAP (minor qualification, no failure of the proof): lines 405–407, “E q^5=...” and “and E q^4=mu_4+O(s)”. State explicitly that these require beta5<infinity and beta4<infinity respectively. A centred Pareto law of shape 4, allowed in (a), has both moments infinite. The proof of (a) uses neither of these higher identities; the proof of (b) has beta7<infinity, so the qualification repairs the presentation without strengthening the theorem. The preceding “whenever beta_k<infinity” makes the intended reading recoverable.

GAP (reproducibility evidence): lines 525–532 refer to code/mode_checks.py in “the repository of the paper”; that code and an unambiguous paper repository are not supplied in this folder. The reported original run cannot be audited. The independent scripts and raw outputs produced here substantiate the numerical conclusions checked here.

CORRECT: all mathematical theorem and corollary conclusions survived the independent proof audit. No counterexample was found. Overall mathematical verdict: SOUND, with the local qualification and external-source verification limits above. This does not certify novelty.

Numerical harness correction: early continuous-grid summaries counted small numerical tail ripples as global peaks; the corrected summary compares the candidate heights with the largest height. Atomic scanning now brackets sign changes of the derivative, which also detects the symmetric small-time pair reliably. These corrected results supersede the early stdout; step2.json and step2_raw.json hold the corrected values. Step3 saved its numerical output and verdict before a stdout-only NumPy integer serialization error; its saved data are complete.
## Step 3 — free proof
CORRECT: [lem:f-max], convex Jensen at positive t-v, positivity and root monotonicity, decay via domination by delta^(-2), attainment, R*<=t, and equality characterization. If v_t=0, compare R* with R*/2 to obtain the strict inequality. CORRECT: [eq:f-mass] and [lem:f-window], Chebyshev >=1/2, b^2(t-2v)<=2vt, hence b^2<=4v. CORRECT: [lem:f-concave], second derivative, exact polynomial identity, R*>=t-v>(7a-1)v>6av since a>1.
CORRECT: uniqueness follows from strict concavity plus the common global upper bound 1/t; [eq:f-stat], [eq:f-u], [eq:f-M], R*>=6t/7, both rational minimum inequalities, quadratic and cubic moment bounds, and [eq:f-u3]. The first arithmetic factor is 3.939710014258<4; 77K/12=(77/3)(B^3+beta3)<26(B^3+beta3). The coefficient 26(21+14sqrt(2))=1060.773736703807<1061. Thus [thm:free] is CORRECT.

CORRECT (numerical corroboration): 320 atomic laws and centred exponential at both requested free times; all global counts are one, window and R inequalities and both location bounds pass. CORRECT: the named three-atom example has two local maxima at t=233.636121605; see step3.json for both positive peak heights. This establishes the claimed phenomenon for that law at this tested time.

## Final independent consistency audit

CORRECT: all 1,280 saved atomic cases pass direct recomputation of the stated bounds and stationary equations. On 501 points in each window the classical slope stays above 1/2 and the scaled free second derivative is negative. Saved JSON contains no NaN or Infinity, and the PAPER.tex hash agrees with the report. Details: audit_results.json.

## Step 3 — free proof
CORRECT: [lem:f-max], convex Jensen at positive t-v, positivity and root monotonicity, decay via domination by delta^(-2), attainment, R*<=t, and equality characterization. If v_t=0, compare R* with R*/2 to obtain the strict inequality. CORRECT: [eq:f-mass] and [lem:f-window], Chebyshev >=1/2, b^2(t-2v)<=2vt, hence b^2<=4v. CORRECT: [lem:f-concave], second derivative, exact polynomial identity, R*>=t-v>(7a-1)v>6av since a>1.
CORRECT: uniqueness follows from strict concavity plus the common global upper bound 1/t; [eq:f-stat], [eq:f-u], [eq:f-M], R*>=6t/7, both rational minimum inequalities, quadratic and cubic moment bounds, and [eq:f-u3]. The first arithmetic factor is 3.939710014258<4; 77K/12=(77/3)(B^3+beta3)<26(B^3+beta3). The coefficient 26(21+14sqrt(2))=1060.773736703807<1061. Thus [thm:free] is CORRECT.

CORRECT (numerical corroboration): 320 atomic laws and centred exponential at both requested free times; all global counts are one, window and R inequalities and both location bounds pass. CORRECT: the named three-atom example has two local maxima at t=233.636121605; see step3.json for both positive peak heights. This establishes the claimed phenomenon for that law at this tested time.

## Final independent consistency audit

CORRECT: all 1,280 saved atomic cases pass direct recomputation of the stated bounds and stationary equations. On 501 points in each window the classical slope stays above 1/2 and the scaled free second derivative is negative. Saved JSON contains no NaN or Infinity, and the PAPER.tex hash agrees with the report. Details: audit_results.json.

## Final itemized verdict register

- CORRECT: Abstract; thm:classical. Unique global maximum and both bounds follow from the window and slope lemmas.
- CORRECT: Abstract; thm:free. The fixed-height F argument gives uniqueness and both stated bounds.
- CORRECT: thm:expansion (a). Third absolute moment suffices for both dominated-convergence arguments.
- CORRECT: thm:expansion (b); eq:exp-c, eq:exp-f. Seventh moment controls the remainders; both coefficient pairs agree with independent algebra.
- CORRECT: cor:HU (i)–(iii). Moment estimates and thresholds transfer correctly, using the cited HU unimodality result.
- CORRECT: cor:compact. Variance, third moment, strict threshold, 136 constant, and mode conclusion follow.
- CORRECT: Introduction: definitions of unimodality and mode. Usual atom-plus-monotone-density definition; a continuous density removes the atom.
- CORRECT: Introduction: v=0 case; translation to m=0. Both convolutions translate; point masses give the stated Gaussian and semicircle laws for t>0.
- CORRECT: Introduction: symmetry and sixfold leading displacement. Symmetry plus uniqueness fixes the maximum at m; sixfold nonzero leading displacement holds when mu3 is nonzero.
- CORRECT: eq:HU. This is the assumed exponential-square integrability condition, not an automatic finite-variance property.
- CORRECT: eq:cum-c; kappa2, kappa3, kappa5. Classical cumulants add; kappa5=mu5-10v mu3, and expansion in t+v gives the stated second coefficient.
- CORRECT: eq:cum-f; r2, r3, r5. Free cumulants add; r5=mu5-5v mu3; only r2 gains t.
- CORRECT: Section 3: F and v_t definitions. With variance t, the boundary equation is F=1/t, not a rescaled time.
- CORRECT: Section 3: psi, homeomorphism, eq:biane. Standard semicircular subordination boundary description; all three closed-form checks agree.
- CORRECT: psi when v_t=0. E[(u-X)^(-2)]<=1/t implies absolute integrability of (u-X)^(-1).
- CORRECT: F as a function of R. Continuous and strictly decreasing for R>0, bounded above by 1/R.
- CORRECT: Section 2: density, g-prime=H/t. Differentiate the Gaussian kernel; the positive factor is (2 pi t)^(-1/2).
- CORRECT: eq:Hprime; interchange of derivatives. The sign and factors agree; kernels and their derivatives are uniformly bounded in the random variable.
- CORRECT: lem:c-window: Jensen. Convexity of exp(-x/(2t)) gives g(0)>=exp(-v/(2t)).
- CORRECT: lem:c-window: split, Chebyshev. Outside the central kernel event, |Y|>sqrt(t)/4; its probability is at most 16v/t.
- CORRECT: lem:c-window: numerical comparison. 0.995899901143 < 0.9960 < 0.999167013792.
- CORRECT: lem:c-slope: scalar inequality. Both z<=1 and z>1 cases preserve the required inequality direction.
- CORRECT: lem:c-slope: expectation and arithmetic. E(Y-h)^2=v+h^2, and 5/8-1/400=0.6225>1/2.
- CORRECT: Classical proof: existence, window, stationarity. Continuous positive function decays at infinity; a maximizer is an interior point of R, including window endpoints.
- CORRECT: Classical proof: unique zero in window. H is strictly decreasing throughout the window; every global maximizer is a zero there.
- CORRECT: eq:c-mvt. The segment from 0 to h_t lies in the window; the derivative magnitude exceeds 1/2.
- CORRECT: eq:c-H0. Centering permits subtracting E Y; absolute value removes the harmless sign reversal.
- CORRECT: Classical proof: both bounds. min(1,z)<=sqrt(z) and min(1,z)<=z give the variance and third-moment bounds.
- CORRECT: lem:f-max: Jensen at t-v. t-v>0; F(0,t-v)>=1/t gives a positive root with square at least t-v.
- CORRECT: lem:f-max: decay and attainment. Domination by delta^(-2) gives F(u,delta^2)->0, hence v_t(u)->0.
- CORRECT: lem:f-max: R*<=t. At a positive maximizer, 1/t=F(u,R*)<=1/R*.
- CORRECT: lem:f-max: equality set, v_t>0. Strict monotonicity in R gives equality exactly at the largest root.
- CORRECT: lem:f-max: equality set, v_t=0. F(u,R*)<F(u,R*/2)<=1/t, so no zero-height point is mistaken for a maximum.
- CORRECT: eq:f-mass. E[q^2/(R*+q^2)]=1-R*/t<=v/t.
- CORRECT: lem:f-window: Chebyshev and algebra. Mass at least 1/2 in |Y|<=sqrt(2v); b^2(t-2v)<=2vt yields b^2<=4v.
- CORRECT: lem:f-concave: differentiation. F_uu=-2 E[(R-3q^2)/(R+q^2)^3]; the derivatives are bounded.
- CORRECT: lem:f-concave: rational identity. The difference equals z^2(15+17z+6z^2)/(1+z)^3.
- CORRECT: lem:f-concave: threshold. R*>=t-v>(7a-1)v>6av, since a>1.
- CORRECT: Free proof: uniqueness. Two equal-height global maxima inside the concavity window would force a larger midpoint value.
- CORRECT: eq:f-stat. F_u=0 at a maximum on R; multiplying by a positive power of R* gives this form.
- CORRECT: eq:f-u. Subtract stationarity from E q=u*.
- CORRECT: eq:f-M. Rewrite q/(1+q^2/R*) as q-q^3/(R*+q^2).
- CORRECT: Free proof: R*>=6t/7. The hypothesis is stronger than v<t/7.
- CORRECT: Free proof: 1-(1+z)^(-2) bound. It lies between 0 and min(1,2z), which is at most sqrt(2z).
- CORRECT: Free proof: q^3 rational bound. R*+q^2>=2 sqrt(R*) |q|, so the absolute expectation is at most E q^2/(2 sqrt(R*)).
- CORRECT: Free proof: first arithmetic constant. (13 sqrt(2)/6+7/12)sqrt(7/6)=3.939710014258...<4.
- CORRECT: Free proof: K and eq:f-u3. E|q|^3<=4(B^3+beta3); |u*|<=2K/R*.
- CORRECT: Free proof: second arithmetic constant. 77K/12=(77/3)(B^3+beta3)<26(B^3+beta3).
- CORRECT: After thm:free: 1061 beta3/t. Lyapunov gives v^(3/2)<=beta3 and 26(21+14sqrt(2))=1060.7737367...<1061.
- CORRECT: Remark after free theorem; Section 6 final example. The named law has two distinct positive local peaks at the tested time above 7av.
- CORRECT: Section 4: h=O(s), u=O(s), r=1+O(s). Earlier third-moment bounds and t-v<=R*<=t give these estimates.
- CORRECT: eq:c-moments. Binomial identities; the fifth identity is explicitly restricted to finite beta5.
- CORRECT: Classical (a): rho. 0<=exp(-x)-1+x<=min(x,x^2/2).
- CORRECT: Classical (a): domination and limit. After division by s, dominate by (|Y|+1)^3/2; the minimum factor tends to zero pointwise.
- CORRECT: Classical (a): coefficient. E q^3=mu3+O(s), giving h=-mu3 s/2+o(s).
- CORRECT: Classical (b): rho3 and remainder. |q rho3(sq^2/2)|<=s^3 |q|^7/48.
- CORRECT: Classical (b): first substitution. The h^3 and shifted fifth-moment terms contribute only O(s^3) or smaller.
- CORRECT: Classical (b): final substitution. h=-(mu3/2)s+O(s^2) yields (mu5-6v mu3)/8 at s^2.
- CORRECT: eq:f-moments: algebra. All signs, including -mu3 and -mu5, agree with q=u-Y.
- GAP — minor qualification: Lines 405–407: domain of higher moments. The fifth identity and E q^4=mu4+O(s) need finite beta5 and beta4; add an explicit proviso.
- CORRECT: eq:f-system: all three relations. R*=r/s and t=1/s give exactly the displayed mass, stationarity, and location equations.
- CORRECT: eq:exp1: rho1, sigma1. rho1=z^2/(1+z); sigma1=-z^3/(1+z), with the stated bounds.
- CORRECT: eq:exp2: rho2, sigma2. rho2=z^2(3+2z)/(1+z)^2; sigma2=-z^3(4+3z)/(1+z)^2 satisfy all bounds.
- CORRECT: Free (a): stationarity remainder. After division by s, dominate by a constant times (|Y|+B)^3; r is bounded away from zero.
- CORRECT: Free (a): location remainder. rho1 uses the same integrable third-moment envelope and pointwise vanishing factor.
- CORRECT: Free (a): u and maximum. u=-2mu3 s+o(s); M=2u+mu3 s+o(s)=-3mu3 s+o(s).
- CORRECT: Free (b): mass remainder. The sigma1 remainder requires E|q|^6, supplied by beta7.
- CORRECT: Free (b): r and its inverses. r=1-vs+(mu4-v^2)s^2+O(s^3), with the stated inverse expansions.
- CORRECT: Free (b): stationarity remainder and expansion. The remainder needs E|q|^7; its expansion is u-6vsu+2mu3s+(2vmu3-3mu5)s^2.
- CORRECT: Free (b): u coefficients. u=-2mu3s+(3mu5-14vmu3)s^2+O(s^3).
- CORRECT: Free (b): last three location lines. 2u-2vsu+mu3s+(2vmu3-mu5)s^2 gives -3mu3 and 5mu5-22vmu3.
- CORRECT: After expansion proof: cumulant conversion. Expanding (t+v)^(-1) and (t+v)^(-2) reproduces both coefficients.
- CORRECT: cor:HU proof: L and absolute moments. Jensen and the scalar maximum x^k exp(-eps x^2) give all claimed estimates.
- CORRECT: cor:HU proof: Q. beta3<=4(E|X|^3+|m|^3)<=8 E|X|^3.
- CORRECT: cor:HU proof: mode argument. Continuity makes each unimodality mode a global density maximum; uniqueness then identifies it.
- CORRECT: cor:HU proof: thresholds and (iii). Maximum of the two classical thresholds is sufficient; free inequality is strict; all moments exist.
- CORRECT: cor:compact proof: support estimates. The midpoint gives v<=D^2/4; the mean lies in the interval, so beta3<=Dv.
- CORRECT: cor:compact proof: 23 and 136. 7a/4=22.1494949...<23; the location constant is 135.8467171...<136.
- CORRECT: Section 6: moments and two expansions. Exact rational moments are 0,2,2,10 for m,v,mu3,mu5.
- CORRECT: tab:example: all three rows. All displayed values agree with independent 80-digit computations and rounding.
- CORRECT: Section 6: global classical maximum at t=1000. Although below 600v, the mixture is strictly log-concave for every t>9/4.
- GAP — verification: Section 6: claims about code/mode_checks.py. The program and an unambiguous paper repository are absent from the supplied files.
- GAP — verification: HU Theorems 3.2, 4.3; Propositions 3.4, 4.2; Problem 4.6. Consistent with memory, but exact source text, numbering and endpoints cannot be certified here.
- CORRECT: Haldane and Hall attribution. Fair attribution of the classical nearly normal leading mode displacement; not a universal assertion without regularity.
- CORRECT: Chistyakov–Goetze attribution. The general attribution to free-CLT asymptotic expansions is fair; exact hypotheses were not source-checked.
- GAP — verification: Novelty and bibliography metadata. No matching free coefficients or finite-variance thresholds are known to me; that is not a priority search.

The symmetric free peak refinement was corrected by a wider stationary-root bracket. A continuous-quadrature grid reduction lowered the measured free-test peak memory from 767,279,104 bytes to 126353408 bytes. The consistency audit now passes. REPORT.md contains all requested numerical tables, commands, qualifications and source-check limits.

Overall mathematical verdict: SOUND. PAPER.tex remains unchanged.
