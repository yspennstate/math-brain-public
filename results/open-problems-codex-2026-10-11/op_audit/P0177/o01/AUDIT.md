VERDICT: PASS

# Independent audit of P0177

Audit date: 2026-10-11. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md in the claimant's folder read-only. All audit downloads, scripts, computations, and this report are in the assigned audit folder. I did not rely on the claimant's numerical output, claimed Lean run, or its self-referee report.

## Exact claim and match to the question

ATTEMPT.md lines 5-10, 43-45, 65-93, and 99-110 claim the following. For every probability law of X with alpha = E exp(epsilon X^2) < infinity for some epsilon > 0, let m = E X, v = E(X-m)^2, mu_k = E(X-m)^k, and M_k = E|X-m|^k. Both noise laws have variance t: the classical law is mu * N(0,t), and the free law is mu boxplus S(0,t). Each continuous density has a unique GLOBAL maximizer for all sufficiently large t, and

    M_c(t) = m - mu_3/(2t) + (mu_5 - 6v mu_3)/(8t^2) + O_mu(t^-3),
    M_f(t) = m - 3mu_3/t + (5mu_5 - 22v mu_3)/t^2 + O_mu(t^-3).

The classical bound is |M_c-m| <= M_3/t for t >= T_c, where delta = epsilon/2, alpha_c = E exp(delta (X-m)^2), and T_c = 36 log(2alpha_c)/delta. The stronger free lemma asserts unique global maximization and convergence to m under finite variance alone, for t > 7(7+4sqrt(2))v. With finite M_3, it asserts

    |M_f-m| <= 64(B^3+M_3)/t,  B = (sqrt(2)+2)sqrt(v).

Finally, set L = log(alpha)/epsilon and Q = 8alpha[3/(2e epsilon)]^(3/2). The bounds solely in the source parameters are

    |M_c-m| <= Q/t,  t >= 72 log(2alpha^2)/epsilon;
    |M_f-m| <= 64[(sqrt(2)+2)^3 L^(3/2)+Q]/t,
        t > 7(7+4sqrt(2))L.

The zero-variance case is exact for every t > 0. The O_mu constants in the expansions depend on the law; uniform expansion remainder constants in epsilon and alpha are not claimed.

I independently downloaded the published paper from https://alea.math.cnrs.fr/articles/v15/15-15.pdf (382219 bytes), saved as published.pdf, and extracted published.txt. Problem 4.6, journal p.367/PDF p.15, states:

> Estimate the position of the mode of classical Brownian motion with initial distributions satisfying the assumption (4.13). Our proof shows that for t >= (36/epsilon) log(2alpha), the mode is located in the interval [-sqrt(t)/2, sqrt(t)/2]. How about free Brownian motion?

Theorem 4.3, journal p.364, confirms exactly the stated exponential quadratic hypothesis and classical threshold. Equations (2.9)-(2.14), pp.356-357, confirm the free parametrization and its normalization. Thus this is the full initial-law class requested, including unbounded laws, and the bounds improve a growing window to convergence to the initial mean with order 1/t and explicit constants. The problem specifies neither optimal constants nor a sharp transition time. The free answer estimates the global density maximum. This is a valid reading of the question: the source itself gives initial laws with arbitrarily strong integrability for which free unimodality never occurs (Theorem 1.2(2), equivalently Proposition 3.4). Unique global maximization does not imply unimodality, and the claimant does not make that inference.

## Issues found

No mathematical error, missing hypothesis, quantifier mismatch, or necessary repair was found in ATTEMPT.md. In particular, the finite-variance free lemma is not contradicted by the source's counterexamples to free unimodality.

Scope cautions, which are already correctly disclosed by the claimant:

- Lines 95-96 and 118 do not establish optimal thresholds, optimal constants, or eventual free unimodality. They need not establish these to answer Problem 4.6.
- Lines 113-115 describe supporting numerical and formal algebra checks. I have not independently certified those particular runs. My verdict rests on the written analysis and independent calculations below, not on the claimed Lean verification.
- Lines 39 and STATUS.md line 10 disclose a previous write outside the claimant's folder. That is an operational disclosure, not a failed mathematical step; I did not access that file or reproduce the write.
- Lines 118 and LITERATURE.md do not certify novelty. The bounded literature checks below likewise cannot certify novelty.

None of these requires a proof fix or a PASS_WITH_GAPS verdict.

## Re-derivation of the free global-mode lemma

**Lines 16-18: parametrization, positive height, and attainment.** The source supplies continuity of eta_t, a homeomorphism psi_t of R, the density eta_t(u)/(pi t) at psi_t(u), and the unique positive solution F(u,R)=1/t when eta_t(u)>0. Since F(u,R) <= 1/R, R <= t. For centered X and t>v, convexity of a -> 1/a gives

    F(0,t-v) = E[1/(t-v+X^2)] >= 1/t.

Because F is strictly decreasing in positive R, the positive root at zero is at least t-v. For fixed d>0, the integrand in F(u,d^2) tends pointwise to zero as |u| grows and is bounded by 1/d^2. Dominated convergence proves F(u,d^2)->0, hence eta_t(u)<d eventually. A continuous function tending to zero at both tails and positive somewhere attains a positive global maximum. Therefore t-v <= R* <= t. No assumption about bounded support enters.

**Lines 20-22: localization of EVERY global maximizer.** From F=1/t,

    E[q^2/(R*+q^2)] = 1-R*/t <= v/t,  q=u*-X.

Chebyshev gives mass at least 1/2 in |X|<=sqrt(2v). If a=|u*|-sqrt(2v)>0, that event has |q|>=a. Monotonicity in q^2 and R*<=t give a^2/[2(t+a^2)] <= v/t. Rearrangement is valid for t>2v and yields a^2<=2vt/(t-2v)<=4v for t>=4v. Thus |u*|<=B, including equality at the boundary. This controls small distant components of unbounded laws as well as central components.

**Lines 24-28: strict concavity at a fixed global height and uniqueness.** Independent symbolic expansion gives exactly

    (1-3z) - (1-6z)(1+z)^3 = z^2(15+17z+6z^2).

For z>=0 the right side is nonnegative. Consequently, with A=B^2+v and |u|<=B,

    E[(R*-3(u-X)^2)/(R*+(u-X)^2)^3]
        >= (R*)^-2[1-6(v+u^2)/R*]
        >= (R*)^-2[1-6A/R*].

I differentiated 1/(R+(u-X)^2) twice: its second derivative is -2(R-3(u-X)^2)/(R+(u-X)^2)^3. At fixed R*>0 these derivatives are bounded functions of u-X, so integration and differentiation commute. Since t>7A and v<=A, R*>=t-v>6A, and F(.,R*) is strictly concave on [-B,B]. Here A=(7+4sqrt(2))v, so the claimed time threshold is exact. It also implies t>4v, as needed for localization.

At any positive-height global maximum, F_R = -E[(R+q^2)^-2] < 0, so implicit differentiation applies and R'=0 implies F_u=0. All global maximizers share R* and are localized in the same interval. Strictly decreasing F_u permits at most one such stationary point. This argument remains valid if a maximizer equals B or -B: stationarity is in its open positive-height neighborhood, not an assumption of interiority in [-B,B]. The homeomorphism transports this unique maximum to the physical density. Concavity of eta_t over the whole real line is neither used nor proved.

**Line 30: convergence under finite variance.** For a convergent subsequence of bounded u*, R* tends to infinity and the stationarity integrand q/(1+q^2/R*)^2 is dominated by B+|X|. Its limiting expectation is the limiting u*, since E X=0. Thus every subsequential limit is zero. In the physical map, t/R*->1 and the integrand q/(1+q^2/R*) has the same integrable bound, so M_f->0. Finite variance provides the finite first moment needed here.

**Lines 32-34: explicit rate.** E|q|^3 <= 4(B^3+M_3)=D. For z>=0, 0<=1-(1+z)^-2<=2z (the upper bound follows, for example, by expanding 2z(1+z)^2-[(1+z)^2-1]=3z^2+2z^3). Stationarity therefore gives |u*|<=2D/R*. The exact physical-map identity yields

    |M_f| <= 2D/R* + 3tD/(R*)^2.

Since R*>=t-v>=t/2 at the asserted threshold, this is <=16D/t=64(B^3+M_3)/t. Translation restores m. Every stated constant is sufficient.

## Classical bound and asymptotic expansions

**Lines 43-53: centering, derivative bound, and uniqueness.** The inequality (X-m)^2<=2X^2+2m^2 gives alpha_c<=exp(epsilon m^2)alpha<infinity. The source theorem and its window can therefore be applied to the centered law. Differentiating H gives

    -H_h = E[(1-s(Y-h)^2)exp(-s(Y-h)^2/2)].

For 0<=z<=1, use exp(-z/2)>=1-z/2 to obtain (1-z)exp(-z/2)>=1-3z/2. For z>=1, multiplying exp(-z/2)<=1 by 1-z reverses the inequality and gives the same conclusion. Thus -H_h>=1-(3s/2)(v+h^2). Jensen implies log(alpha_c)>=delta v, hence T_c>=36v. On the entire source mode window the lower bound is 5/8-3v/(2t)>=7/12>1/2. Differentiation is justified by finite second moment on compact h intervals.

At zero, centering and 1-exp(-z)<=z give |H(0,s)|<=sM_3/2. Integrating the derivative bound between zero and the source's mode gives |h_t|<=M_3/t. At its root, H_h<0 gives a strict local maximum of the density. If a unimodal density had another global maximum, it would be constant between the two, contradicting that strict local maximum. The classical maximizer is therefore unique.

**Lines 56-63: classical coefficient and remainder.** Taylor's integral remainder for exp(-s q^2/2), s>=0, is bounded by s^3|q|^6/48. Multiplication by q and expectation use only the seventh absolute moment, uniformly since h_t=O(s). Direct binomial expansion of E(Y-h)^3 and E(Y-h)^5 gives line 62. Coefficient comparison gives first -mu_3/2 and then (mu_5-6v mu_3)/8. Substitution into the stationarity equation leaves O(s^3), and its linear term in h is -h, so the claimed O(s^3) error follows. No two-sided moment-generating function or power-series analyticity is needed.

**Lines 67-91: free coefficient and remainder.** Put s=1/t and r=R/t. The two defining equations become exactly E[(r+s q^2)^-1]=1 and E[q(r+s q^2)^-2]=0. Already u=O(s), 1-vs<=r<=1, and r>=1/2 eventually. For z>=0 the first Taylor remainder is -z^3/(1+z). The second is exactly -z^3(4+3z)/(1+z)^2, whose absolute value is <=4z^3. These are global real-variable bounds. Uniform seventh moments of q justify all integrated remainders, including the physical map.

Re-expansion of the first equation gives

    r=1-vs+(mu_4-v^2)s^2+O(s^3).

The second equation gives

    0=u+2mu_3 s+2v mu_3 s^2-6vu s-3mu_5 s^2+O(s^3),
    u=-2mu_3 s+(3mu_5-14v mu_3)s^2+O(s^3).

The SOURCE coordinate map, not just the maximizing u, must be expanded. It gives

    M_f=2u-2vu s+mu_3 s+(2v mu_3-mu_5)s^2+O(s^3),

and hence precisely -3mu_3 s+(5mu_5-22v mu_3)s^2+O(s^3). I checked these coefficients both by hand and with symbolic computation. The distinction between u and M_f is handled correctly.

**Line 93: degenerate, symmetric, and sharpness cases.** Variance zero means a point mass; normal and semicircular noise then have modes at m exactly. Symmetry and proved uniqueness force the sufficiently-large-time mode to be m. For masses 2/3 at -1 and 1/3 at 2, the mean is zero, v=2, mu_3=2, and mu_5=10. Thus the leading displacements are -1/t and -6/t. The next coefficients are -7/4 and -38. In particular, the order 1/t cannot be uniformly improved over this initial-law class.

**Lines 101-110: constants in the original parameters.** Jensen gives E X^2<=L, v<=L, and epsilon m^2<=log(alpha). Therefore alpha_c<=alpha^2, and the proposed classical threshold dominates T_c. Maximizing a^k exp(-epsilon a^2) gives [k/(2e epsilon)]^(k/2); multiplying by alpha bounds E|X|^k. The convexity estimate |X-m|^3<=4(|X|^3+|m|^3), together with |m|^3<=E|X|^3, gives M_3<=Q. Substitution proves both final bounds. If alpha=1, X=0 almost surely, as stated. No hidden parameter besides epsilon and alpha enters these estimates.

## Independent computations

The scripts and results are local audit artifacts, not copied claimant artifacts.

- independent_checks.py / independent_results.json: SymPy returns exactly zero for the concavity polynomial identity. Substituting the proposed classical and free coefficients into their stationarity equations gives O(s^3) residuals; independently expanding the free physical map gives -3mu_3 s+(5mu_5-22v mu_3)s^2+O(s^3).
- The same script solves the classical stationarity equation and the free two-equation system using mpmath at 65 decimal digits for three atomic laws, including an asymmetric four-point law and a symmetric law, at three increasing times each. For the sharpness law, t=200,600,2000 gives classical t^3-scaled second-order errors approximately -2.38150,-2.37720,-2.37566, and free errors -134.12772,-136.81816,-137.65639. These support bounded third-order remainders, rather than merely the leading-order shift. The symmetric modes are exactly zero in these computations.
- unbounded_checks.py / unbounded_results.json: independently tested 0.75 N(-1,0.16)+0.25 N(3,1.44), a mean-zero law satisfying an exponential quadratic moment. Its moments are v=3.48, mu_3=8.88, mu_5=179.04. The classical equation uses the exact Gaussian-mixture convolution formula. The free equations use 64- and 128-node Gauss-Hermite quadrature at t=1000,3000,10000. All free solves succeeded, residuals were at most 1.2e-16, and changing quadrature order changed modes by at most 2.2e-16. Classical t^3-scaled errors were approximately 29.5600,29.5014,29.4808; free errors approximately -787.68,-842.01,-861.80. These are numerical support, not proofs of the unbounded-law theorem or uniform error control.
- A nonnegative-z grid through 10^6 showed no violation of the classical derivative inequality or either bound on 1-(1+z)^-2. The exact arguments above, rather than the finite grid, establish those inequalities for all z>=0.

The scripts completed with exit code zero. Finite examples do not independently prove global maximization; the localization/uniqueness argument does that. I did not infer a proof from root finding.

## Bounded literature check and limits of the verdict

source_check.py independently fetched the published source and queried arXiv and OpenAlex; raw responses and parsed abstracts are saved locally in source_search_results.json, arxiv.xml, arxiv_modes.xml, and the published files. The arXiv unimodality/Brownian query returned 18 records, including the original paper and the positive multiplicative Brownian follow-up, arXiv:2009.13848. That follow-up's abstract concerns multiplicative log-unimodality, not real-line additive mode location. The narrow free-Brownian/mode query returned one unrelated single-molecule paper. OpenAlex returned HTTP 429; this is unavailable coverage, not evidence of absence.

literature_followup.py broadened the free-Brownian query to mode OR maximum OR location. Its four returned abstracts concern classical path maxima, permeable interfaces, random acceleration, and motion classification; none settles this additive free-probability question. The explicit arXiv:2007.06100 abstract fetch returned Ching-Wei Ho's paper on Brown measures of sums with elliptic elements and large-variance asymptotics. That abstract does not state the claimed mode theorem, so it supplies neither an earlier exact solution nor a counterexample. This abstract-only check does not rule out implications buried in its full paper. Responses are in arxiv_free_broad.json/.xml and arxiv_ho.json/.xml.

One attempted shell-inline follow-up query failed before making a request because Windows argument quoting broke the Python command. I replaced it with the saved script, which succeeded. No inference was drawn from that failed attempt.

No earlier exact solution or known counterexample was identified in this bounded search. This is not an exhaustive novelty investigation. The verdict is mathematical correctness and completeness as quantitative large-time GLOBAL mode-location estimates under the precise published hypothesis, including the two stated asymptotic expansions. Optimality beyond the exhibited order, eventual free unimodality, and literature priority are not proved or certified.
