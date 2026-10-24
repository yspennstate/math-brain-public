VERDICT: PASS

# Independent audit of P0177

Audit date: 2026-10-11. The mathematical result is correct and complete for the source's request to estimate large-time global mode locations. No mathematical fix is required. This verdict does not certify originality, optimal constants, or a full formal verification.

## Claim and exact scope

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md in the claimant's folder read-only. References below are to the 118-line ATTEMPT.md saved in ATTEMPT.md.numbered.txt in this audit folder.

ATTEMPT.md lines 5–10 claim the following for EVERY probability law of X satisfying alpha = E exp(epsilon X^2) < infinity for SOME epsilon > 0. Let m = EX, v = E(X-m)^2, and mu_k = E(X-m)^k. For classical convolution with N(0,t) and additive free convolution with the semicircle of variance t, there are unique global density maxima for all sufficiently large t, and

    M_c(t) = m - mu_3/(2t) + (mu_5 - 6v mu_3)/(8t^2) + O_mu(t^-3),
    M_f(t) = m - 3mu_3/t + (5mu_5 - 22v mu_3)/t^2 + O_mu(t^-3).

The constants and starting times in these asymptotics may depend on the law. Lines 101–110 additionally give explicit bounds using just the supplied epsilon and alpha. With L = log(alpha)/epsilon and Q = 8alpha[3/(2e epsilon)]^(3/2), they are

    |M_c(t)-m| <= Q/t,
        t >= 72 log(2alpha^2)/epsilon;
    |M_f(t)-m| <= 64[(sqrt(2)+2)^3 L^(3/2) + Q]/t,
        t > 7(7+4sqrt(2))L.

Lines 16–34 prove an additional free result: finite variance alone gives a unique global mode at t > 7(7+4sqrt(2))v and convergence to m; a finite third absolute central moment additionally gives the displayed law-dependent O(1/t) estimate. Finite seventh moment suffices for the free expansion. The classical finite-seventh-moment observation at line 63 is conditional on the preceding identification and bound for the global mode, rather than a claim of eventual classical unimodality under seventh moments alone.

I checked the journal version's Problem 4.6, p.367/PDF p.15, and Theorem 4.3, p.364. The problem says:

> Estimate the position of the mode of classical Brownian motion with initial distributions satisfying the assumption (4.13). Our proof shows that for t >= (36/epsilon) log(2alpha), the mode is located in the interval [-sqrt(t)/2, sqrt(t)/2]. How about free Brownian motion?

Assumption (4.13) is exactly the exponential quadratic moment above. Neither optimal estimates nor preservation of that particular starting time is demanded. A shrinking O(1/t) interval around the initial mean and explicit second-order asymptotics answer the classical request. The free global maximum is a legitimate analogous mode: the same source's Proposition 3.4 gives laws with this tail integrability that are never freely unimodal. Thus estimating every local peak, or proving eventual free unimodality, would be a different assertion. The claimant explicitly excludes those assertions at lines 13, 28, and 96.

## Step-by-step analytic checks

1. **Parametrization and global existence, lines 16–18.** Source equations (2.9)–(2.14), with the homeomorphism assertion immediately following (2.14), supply a continuous height eta_t and p_t(psi_t(u)) = eta_t(u)/(pi t). They apply to arbitrary probability measures, with no hidden compact-support hypothesis. For R>0, F(u,R) is strictly decreasing in R, with F_R = -E[(R+(u-X)^2)^-2] < 0. Jensen gives F(0,t-v) >= 1/t for centered X and t>v, hence R(0)>=t-v. Also F <= 1/R implies R<=t. For a fixed positive delta, dominated convergence with bound delta^-2 gives F(u,delta^2)->0 as |u|->infinity. Its monotonicity then makes eta_t(u)->0. Continuity, positivity at zero, and decay imply an attained positive global maximum. All of this remains valid for unbounded laws.

2. **Localization of every global maximizer, lines 20–22.** The identity E[q^2/(R*+q^2)] = 1-R*/t follows directly from F=1/t. On {|X|<=sqrt(2v)}, of probability at least 1/2, q^2 >= (|u*|-sqrt(2v))^2 when |u*|>sqrt(2v). Combining R*<=t with monotonicity of a^2/(t+a^2) yields the stated inequality. Rearrangement gives (t-2v)a^2 <= 2vt, and t>=4v gives a<=2sqrt(v). Thus EVERY global maximizer is in [-B,B], independently of remote atoms.

3. **Uniqueness, lines 24–28.** I expanded the rational identity exactly and differentiated F twice independently. Both formulas are correct. Since E(u-X)^2=u^2+v<=A on [-B,B], the pointwise lower bound yields F_uu(u,R*) <= -2R*^-2(1-6A/R*). The threshold is adequate: A=(7+4sqrt(2))v, A>=v, and t>7A implies R*>=t-v>6A. At a positive global height, F_R<0 permits implicit differentiation, so a global maximizer has F_u=0. All competing global maximizers would have the SAME R* and lie in [-B,B]. Strict concavity at that fixed height precludes two stationary points. This is a proof of global uniqueness, not an assumption that the entire density is unimodal. Maximizing the height and maximizing the density are equivalent under psi_t; no differentiability of psi_t is needed.

4. **Free convergence and rate, lines 30–34.** The normalized stationary equation is correct. Bounded u*, R*>=t-v, and domination by B+|X| let one pass to the limit along any convergent subsequence, obtaining its limit u=0. The same domination in the spatial map gives M_f->0. For the rate, |q|^3<=4(B^3+|X|^3) and 0<=1-(1+z)^-2<=2z give |u*|<=2D/R*. The spatial-map identity bounds |M_f| by 2D/R*+3tD/R*^2. R*>=t/2 gives 4D/t+12D/t=16D/t. The claimed factor 64 and its threshold are correct.

5. **Classical bound, lines 43–53.** Centering is legitimate because (epsilon/2)(X-m)^2 <= epsilon X^2+epsilon m^2. I checked the sign of the density derivative, the formula for H_h, and the pointwise inequality (1-z)e^-z/2 >= 1-3z/2 in both z ranges. Source Theorem 4.3 and (4.32) apply to the centered law with delta=epsilon/2 and alpha_c, giving a global mode in the stated interval. Jensen gives T_c>=36v; on that interval the derivative bound is 5/8-3v/(2t)>=7/12. The estimate |H(0,1/t)|<=M_3/(2t) and the mean value bound give |h_t|<=M_3/t. Strict negativity of H_h rules out a plateau of global maxima. In fact source (4.32) already gives uniqueness, so there is no gap in using it here.

6. **Classical expansion, lines 56–63.** Taylor's exponential remainder has magnitude at most s^3|q|^6/48 for s>=0. Multiplication by q needs precisely a seventh absolute moment. Since h_t=O(s), those moments are uniformly bounded for the shifted q. I checked every binomial coefficient and sign in line 62 and substituted the proposed expansion into the equation. The coefficients through s^2 cancel exactly. The preceding bound allows successive substitution with an O(s^3) remainder, without any claim of analyticity at s=0 for an unbounded law.

7. **Free expansion, lines 65–91.** Scaling R=tr and q=u-Y gives exactly the two equations in line 68. The inverse remainder is -z^3/(1+z), and the inverse-square third derivative is -24/(1+z)^5, giving the uniform bounds in lines 70–72. With r>=1/2 these integrated remainders are O(s^3); the first equation needs sixth moments, and stationarity and the spatial map need seventh moments. I independently obtained r=1-vs+(mu_4-v^2)s^2+O(s^3), u=-2mu_3 s+(3mu_5-14vmu_3)s^2+O(s^3). The map, which must not be confused with u itself, is 2u-2vu s+mu_3 s+(2vmu_3-mu_5)s^2+O(s^3). This gives exactly the claimed physical-mode coefficients. Exact symbolic substitution also verifies the cancellations.

8. **Degenerate cases, symmetry, sharp order, and parameter bounds, lines 93 and 101–110.** Zero variance gives the Gaussian and semicircle centered at m, with exact modes m for t>0. Symmetry plus global uniqueness gives the exact eventual mode m. The two-point example has v=2 and mu_3=2, confirming nonzero t^-1 terms and sharpness of the order in general. Jensen gives EX^2<=L and alpha_c<=alpha^2. Maximizing a^k e^-epsilon a^2 gives exactly alpha[k/(2e epsilon)]^(k/2) as a raw moment bound. The central third moment bound follows from |X-m|^3<=4(|X|^3+|m|^3) and |m|^3<=E|X|^3. All threshold substitutions are in the correct direction. Alpha=1 forces X=0 almost surely. No problematic zero-variance or zero-logarithm case remains.

## Independent computational checks

I wrote and ran my own programs, rather than relying on the claimant's scripts, self-audit, or Lean output.

- `verify_math.py`: SymPy exactly verifies the concavity identity, F_uu, the classical coefficients, free stationary coefficients, and conversion to the physical free mode. At 65 decimal digits, mpmath solves the stationary equations for four atomic laws at four times each: skew two-point, skew three-point, a tiny atom at distance 1000, and a symmetric law. All asserted height bounds, coordinate localization, free O(1/t) bounds, and fixed-height negative curvature on 101-point grids pass. Pointwise classical and rational remainder inequalities also pass on 201 logarithmically spaced positive arguments plus zero. Results are in `independent_math_results.json`.
- For the two-point law, t^3 times the classical second-order error approaches -2.375, and the free error approaches -138, as expected for O(t^-3) remainders. The tiny distant atom produces huge error constants and slow entry into the asymptotic regime; this is consistent with O_mu, whose constant and onset are not uniform over laws.
- `verify_unbounded.py`: the unbounded law (2/3)N(-1,1/4)+(1/3)N(2,1) has mean zero, v=2.5, mu_3=3.5, mu_5=44.375, and a finite exponential quadratic moment. Classical modes use the exact Gaussian-mixture density derivative. Free modes use independently generated Hermite quadrature with 100 and 200 nodes, followed by direct integration over the real line to check both defining equations. At t=1000, 10000, 100000, the two resolutions agree within 3e-16 and direct-integration residuals are below 3e-16. Both expansions are consistent with the computed modes. Results are in `unbounded_results.json`. Scaled third-order errors at very large t are subject to double-precision cancellation; the exact coefficient checks and analytic remainders supply the proof.

These computations can detect mistakes but do not prove a result for all laws or certify all global extrema. The analytic arguments above establish those statements. I did not re-run the claimant's Lean development; lines 96 and 115 correctly distinguish its algebraic scope from the measure-theoretic proof.

## Source verification and bounded literature search

The independent HTTPS journal download failed first with a closed connection and then with curl error 55. I therefore read the claimant's saved journal `source.pdf` read-only and extracted it into this folder as `published_source.txt`. I also fetched a fresh independent copy of https://arxiv.org/pdf/1710.08240 (306104 bytes), saved as `arxiv_source.pdf`, and extracted `arxiv_source.txt`. Its Problem 4.6, hypothesis, threshold, and Biane parametrization agree with the journal passages. The homeomorphism assertion immediately after (2.14) is explicit in the fresh PDF.

I independently queried arXiv for `all:"free Brownian" AND (all:mode OR all:maximum OR all:location)` (30-result limit) and `all:unimodality AND all:Brownian` (40-result limit). Raw responses are saved as `arxiv_modes.xml` and `arxiv_unimodality.xml`. Relevant results include the source and Hasebe–Ueda–Wang's arXiv:2009.13848, whose abstract concerns positive MULTIPLICATIVE free Brownian motion and log-unimodality, not additive real-line mode estimates. Other retrieved results about first-passage maxima, active particles, and elliptic Harnack inequalities do not answer this problem. An independent OpenAlex query for `Brownian motion mode location unimodality` returned HTTP 429; its failure is recorded, not counted as a negative search.

No exact earlier solution or counterexample to the claimed estimates was identified in these bounded searches. This is not proof of novelty or an exhaustive literature review. The source's counterexample to eventual free unimodality was explicitly checked and does not refute a unique GLOBAL maximum.

## Issues and limits of the verdict

No failing identity, inequality, unjustified exchange of limits, missing moment hypothesis, or quantifier restriction was found in ATTEMPT.md. No repair is needed for the mathematical result.

There is one dossier issue: CLAIMS.jsonl is empty, so it contains no machine-readable assertion to compare against ATTEMPT.md lines 5–10 and 118. STATUS.md and ATTEMPT.md nevertheless state the result unambiguously. Filling the claims ledger would fix that documentation omission; it does not change the mathematical verdict.

ATTEMPT.md line 39 discloses an earlier out-of-folder file write by the claimant. I did not inspect that outside location or attempt to verify or repair the operational incident. It is not a mathematical step and supplies no evidence for or against the theorem. This audit wrote only in its assigned folder.

What is proved: sufficiently-large-time existence and uniqueness of both global modes, convergence to the initial mean, the explicit O(1/t) estimates for every law in the source's class, and both stated second-order asymptotic expansions. What is not proved or claimed: optimal constants or starting times, eventual free unimodality, estimates for every local free peak, uniform O(t^-3) constants over the whole class, or novelty. None of those omitted assertions is required by the published Problem 4.6 as stated.
