Independent referee report — 15 November 2026, Asia/Tbilisi

Overall verdict: MINOR. I found no gap in Theorem 1.1 or Corollary 1.2. Two assertions are false as written: the equality assertion after the drift lemma and the numerical assertion about two standard errors. Neither affects the proof. The literature search found no earlier theorem covering a single infection for every q > 1/2; this is a search result, not a certification of priority.

All manuscript line numbers refer to claim_files/paper/main.tex as supplied. The manuscript, supplied code and supplied data were not edited. Source PDFs, pdftotext -layout output, DOI metadata and search responses are retained in sources/. Independent code and results are in referee_checks/. Theorem 1.1 and Corollary 1.2 below follow the request's names for thm:main and cor:conjectures. There is a numbering discrepancy: lines 5–9 put conjectures on the theorem counter, so the two preliminary conjectures make these results compile as Theorem 1.3 and Corollary 1.4. If 1.1 and 1.2 are intended, give the quoted conjectures a separate counter. This is a presentation issue only.

| Item | Verdict | Qualification |
| --- | --- | --- |
| Conjectures as quoted | SOUND | Equivalent restatements, not verbatim quotations |
| BCMRT13 input | SOUND | Dependence on theta must be retained; it is uniform for the laws used here |
| Section 2 lemmas and construction | SOUND | Backward-path termination can be made explicit |
| Lemma drift | MINOR | The lemma is valid; lines 251–253 misidentify the bound attaining equality |
| Theorem 1.1 | SOUND | Finite speed alone justifies the replacement |
| Corollary 1.2 | SOUND | Including the stretched-exponential conclusion |
| Proposition fronts | SOUND | Following prose should specify fixed observation windows |
| Proposition allq | SOUND | The explicit exponent follows from the stated density condition |
| Numerics | MINOR | Reproducible; two-standard-error claim is false; exhaustive check uses floating point |
| Bibliography | SOUND | All eleven entries identify real, matching records |
| Novelty | SOUND | No prior full q > 1/2 single-seed result found; Scholar search was blocked |

1. Conjectures and prior results

The requested survey is [Martinelli–Shapira–Toninelli, arXiv:2510.20461v1](https://arxiv.org/abs/2510.20461), submitted 23 October 2025. Section 1.1, page 2, contains both conjectures. The complete source lines are retained in sources/MST25.txt, lines 59–67. Short verbatim excerpts are:

- Conjecture 1, lines 59–60: “any function f depending on the state of finitely many vertices”.
- Conjecture 2, line 67: “then for all q > 0” and “is exponentially fast”.

The remaining hypotheses and conclusions, expressed in manuscript notation, are as follows. Conjecture 1 concerns every q in (0,1), every local f, and every probability law nu with nu(there exists an infection)=1. Its conclusion is convergence of the local expectation to pi(f). There is no product, translation-invariance, positive-density or uniform-gap assumption. Conjecture 2 assumes nu(no infection in [-ell,ell])=O(exp(-kappa ell)) for large ell, for some kappa>0, and asks for exponential convergence of those same local expectations throughout the model's q-range. It does not specify a universal rate or prefactor.

Manuscript lines 65–74 preserve this content. The event in Conjecture 2 is exactly {R>ell}, with lattice intervals understood by intersection with Z. Replacing a large-ell O-bound by A exp(-kappa ell) for every ell>=0 is equivalent after increasing A. Local functions on a finite binary configuration space are bounded automatically. Writing q in (0,1) explicitly follows the survey's parameter convention; the survey's shorthand q>0 in Conjecture 2 is not an assertion about q>1.

Fix: none mathematically. If literal quotation is intended, call these “equivalent formulations”; do not present their wording as verbatim source text.

MST25 does not establish both conjectures for the full interval q>1/2. Its Section 6 proves linear growth of the radius and diameter for finite nonempty infection sets, not local relaxation. Sources/MST25.txt lines 1323–1330 contain Theorem 6.2. The independent 2026 survey [Martinelli, Conjecture 2.11](https://epubs.siam.org/doi/10.1137/25M180425X) also still describes the general nonstationary relaxation question as conjectural. The later-paper search and its limits are recorded in item 8 below.

2. The BCMRT13 input and uniformity of constants

Theorem 2.1 of [BCMRT13](https://arxiv.org/abs/1205.4584), page 4, is at sources/BCMRT13.txt lines 205–219. It assumes q>1/2, a graph of polynomial growth, a local mean-zero function, and a probability law with sup_x E_nu(theta_0^{D_x}) finite for some theta_0>1. On Z its conclusion is exponential decay, originally stated for t>=2. The initial law is arbitrary and can be correlated and singular relative to equilibrium. The manuscript correctly specializes to Z, centers a general local f, absorbs the factor ||f-pi(f)||_infinity <= 2||f||_infinity, and covers t<2 by changing the prefactor.

The displayed dependence in the source is c(q,k,D,kappa,|supp(f)|); theta_0 is omitted there. One must not infer uniformity as theta_0 decreases to 1. The manuscript includes theta explicitly, which is the correct safe statement. In fact, taking Bernoulli initial infection densities tending to zero while choosing theta_0 tending to 1 can keep the moment bound bounded; finite propagation then precludes constants uniform over that family.

I checked the relevant proof, rather than relying on that displayed list. If necessary replace an input theta_0 by a fixed rho satisfying 1<rho<=theta_0 and rho<q/p. The initial rho-moment is at most K. Proposition 4.1 bounds subsequent moments by K+B_rho, with B_rho=q/(q-p rho), uniformly over time and over the initial law. Section 5 uses Markov's inequality at finitely many block centers to bound the probability of a bad block by a constant times rho to a negative multiple of the block length. The remaining estimates depend on q, the block geometry and the observable's support. Thus fixed q, theta_0, K and S give common relaxation constants. Relevant source locations: Proposition 4.1, lines 512–578; the final block estimate, lines 616–640.

There is a real defect in the printed exit-event estimate in BCMRT13 Section 3.2: a supremum over deterministic times cannot simply control a union over random update times without an argument. The manuscript already identifies and repairs the missing volume factor in lines 195–198. Here is a direct justification of its proposed estimate. For a finite chain of total jump rate at most |Lambda|, let B be the bad set and H the event of visiting B during [0,h]. Every path in H either ends in B or has a jump from B to its complement. Consequently

    P(H) <= P(X_h in B) + E[number of exits from B by h]
         <= P(X_h in B) + |Lambda| integral_0^h P(X_u in B) du
         <= (1+|Lambda|h) sup_{u<=h} P(X_u in B).

With |Lambda|=O(h), this introduces only a polynomial factor. For example h^2 exp(-alpha h) <= C_alpha exp(-alpha h/2), so exponential relaxation survives. [BDT19, Section 3](https://arxiv.org/abs/1803.08761) likewise retains a time-times-volume factor in its reproduction of the argument; see sources/BDT19.txt, proof of Proposition 3.1, pages 7–8.

Manuscript application, lines 263–284: theta=sqrt(q/p) lies strictly between 1 and q/p, K=1+B depends only on q, and every modified law has precisely this same moment bound. No conditional moment estimate given eta(s), independence of spins, stationarity, or density with respect to pi is needed. Applying BCMRT13 to the unconditional law of zeta is legitimate even though that law changes with eta and t. Fresh graphical randomness after time s provides the required semigroup evolution. The constants do not acquire a dependence on t or nu.

Fix: no change to the theorem is required. Add the preceding exit-count argument to Remark 2.3 if a self-contained justification of the source correction is desired.

3. Graphical construction and finite propagation

Lines 136–143 use the correct rate-one marked-clock construction and generator. The local constraint queries both nearest neighbors and is independent of the updated spin. Non-attractiveness has no bearing on existence of this construction.

Lemma lem:fp, lines 149–174, is valid with the stated constants. A newly created disagreement inside I requires a ring at that site and a disagreement at a neighbor just beforehand. Tracing this backward produces a nearest-neighbor clock path. Starting in S, it needs at least d steps to reach the complement. For a specified length-d sequence the expected number of ordered tuples is u^d/d!, including sequences that revisit sites: one uses the factorial moment measure at repeated sites. At most |S|2^{d-1} sequences suffice; the manuscript's |S|(2u)^d/d! is a looser valid bound. Finally d! >= (d/e)^d and d>=8eu give (2eu/d)^d<=4^{-d}.

The text says the backward construction stops. For complete detail, an infinite backward path can be ruled out using the same bound for every length n: |S|(2u)^n/n! tends to zero. This also supplies the usual finite-dependency justification of the infinite-volume construction. This is an omitted standard sentence, not a failure of the lemma.

Different adapted evolution outside I is allowed: the argument only uses the common update rule and common marks inside I. A frozen infected exterior, as used later, is covered. The lemma bounds disagreement at any time up to u, which is stronger than the single-time comparison needed in the theorem. There is no second independently stated first-passage lemma in the supplied manuscript; lem:fp is this finite-propagation statement.

Fix: optionally append the infinite-backward-path exclusion to lines 168–172.

4. Drift lemma, including attempts near q=1/2

The generator calculation in lines 218–230 is correct. The cases requiring separate inspection are:

- d>=1, one nearest infection y: its inward neighbor is healthy and becomes infected at rate q, reducing D_x by exactly one. The only possible increase is healing y. Its inward neighbor is healthy, so healing requires its outward neighbor to be infected. The new nearest distance is then exactly d+1, not an arbitrary jump. This increase has rate p when allowed, and zero otherwise.
- d>=1, two nearest infections: healing either one leaves the minimum unchanged. There is at least one facilitated inward site giving a rate-q decrease. At d=1 the two inward neighbors coincide at x, so the decrease rate is q, not 2q; the proof only uses q and remains valid.
- Updates at more distant sites cannot increase the minimum; possible additional decreases only improve the inequality.
- d=0: only healing x changes the distance. If legal, an infected neighbor is present, so the new distance is 1 and the rate is p. An isolated infection cannot heal. Therefore L(theta^{D_x})<=p(theta-1).

For d>=1 these cases give

    L(theta^{D_x}) <= theta^d (theta-1)(p-q/theta) = -lambda theta^d.

For d=0, adding b=q(theta-1)/theta gives -lambda+b=p(theta-1). Hence the combined bound Lg<=-lambda g+b is valid. The constants satisfy

    lambda=(theta-1)(q/theta-p)>0,   b/lambda=q/(q-p theta)=B.

The strict sign requires 1<theta<q/p, exactly where q>1/2 enters. With the manuscript's square-root choice, lambda=(sqrt(q)-sqrt(p))^2, giving an independent check of both sign and size. For q=0.500001 it is about 2.0e-12, positive but small; gamma is about 1.25e-7. The constants are allowed to deteriorate at the threshold. Nothing in the argument requires them to stay bounded as q decreases to 1/2.

Lines 232–248 handle the unbounded and nonlocal function properly. Take N large enough that x is inside Lambda_N. The same inequality holds with frozen zeros outside, including the case in which the nearest zero is frozen. The finite-state Dynkin estimate is valid. Initial distances can only decrease when the exterior is replaced by zeros. For fixed cutoff M, min(theta^{D_x},M) is local and bounded; finite propagation gives convergence of its expectation as N tends to infinity. Monotone convergence in M then gives the claimed moment estimate without an unjustified infinite-volume Dynkin formula. It also rules out loss of all infections at a finite time from an initially nonempty state.

Problem at lines 251–253: the positive-distance configuration described there attains Lg=-lambda g, whereas the referenced bound is Lg<=-lambda g+b with b>0. For infections exactly at d,d+1 and x=0, d>=1, the difference between left and right sides of that referenced inequality is -b. Thus the equality assertion is false.

Fix: replace that assertion by “The estimate Lg<=-lambda g for D_x>=1 is sharp,” followed by the same example. Alternatively, equality in the combined bound occurs when D_x=0 and x has an infected neighbor.

Remark rem:half, lines 393–400, passes the generator test. Specify d>=1. With infections exactly at d,d+1,

    Lg=theta^d(theta-1)(p-q/theta).

For q<=1/2 and theta>1 this is strictly positive. As d tends to infinity it cannot satisfy -lambda theta^d+b with fixed lambda>0 and finite b. This obstructs this particular Lyapunov function, not relaxation itself. The literature search found no resolution of the remaining single-infection small-q problem.

Independent exact-rational tests examined 6,320 generator cases, including q=0.500001, theta=1.000001 and q=0.501, theta=1.001. No positive slack occurred. These tests and the positive-generator checks at q=1/2 and q=0.49 are in referee_checks/independent.json.

5. Theorem 1.1 and Corollary 1.2

I checked each constant in lines 257–309.

Step 1: if R<=gamma t and |x|<=floor(gamma t), then D_x<=2gamma t. The initial exponential moment contribution after time s=(1-epsilon)t is bounded by

    exp[-lambda(1-epsilon)t+2a gamma t]
    = exp[-lambda(3/4-epsilon)t] <= exp(-lambda t/2) <= 1.

Thus every site of the retained interval has moment at most 1+B, uniformly over the starting configuration in the stated event.

Step 2: replacing the exterior by zeros decreases the distance to the nearest zero at that instant. This deterministic comparison of configurations is valid and does not compare two evolving FA processes by order. It gives the global moment bound for the random law mu, including value 1 outside the interval. This is the only order comparison being used.

Step 3: the original and replaced states agree on [-r,r]. For S contained in [-m,m], the actual distance to its complement is at least r+1-m. The manuscript uses the weaker r-m. For t>=2(m+1)/gamma,

    r-m >= gamma t-1-m >= gamma t/2 >= 8e epsilon t = 8e h,

where the last inequality follows even from epsilon<=gamma/(16e); the manuscript assumes the stricter epsilon<=gamma/(32e). The replaced region is therefore outside the graphical influence region except on an event of probability at most |S|4^{-gamma t/2}. Coupling error in an expectation is at most 2||f||_infinity times this probability. The coupling does not require that either evolving configuration stay ordered relative to the other.

Step 4: 4^{-gamma t/2}=exp(-gamma log(2)t). Taking c=min(c_0 epsilon,gamma log(2)) and C as in line 303 bounds both errors. The additional term 2 exp(c t_0) in C covers every t<t_0 using the elementary bound 2||f||_infinity. After integration, the good initial states contribute at most C||f||_infinity exp(-ct) and the remaining states contribute exactly the allowed bound 2||f||_infinity nu(R>gamma t). No conditioning probability or hidden normalization changes that coefficient. All constants depend on q and S only. If S is empty the observable is constant and the result is immediate.

The corollary follows. For finite R almost surely its tail vanishes. An exponential tail gives the claimed minimum of rates. For a stretched-exponential tail, set d=min(c,kappa gamma^beta). For t>=1, both contributions are bounded by ||f||_infinity(C+2A) exp(-d t^beta); enlarging the prefactor covers t<=1. For a deterministic infection at z, the tail term vanishes after |z|/gamma, and a prefactor depending on z covers the earlier interval. No exponential-moment hypothesis on the random law is needed for mere convergence.

Fix: none to either result or its proof.

6. The two propositions

Proposition fronts, lines 330–349: valid. A rightmost zero advances one step at rate q. It retreats one step precisely when it heals and its left neighbor is zero, at rate p; in particular it cannot retreat across a long healthy gap. The compensated displacement is a square-integrable martingale with predictable quadratic variation integral(q+p 1{left neighbor infected})<=t. The displayed dyadic Doob bound is conservative and summable. Applying Borel–Cantelli for a countable sequence of positive delta gives M(t)/t tending to zero for all real t. The drift is between q-p and q, as claimed. Reflection gives the left-front bounds. Nonextinction and finiteness of the infected set follow from the graphical construction and finite propagation.

Minor wording issue at lines 353–354: the corollary establishes equilibrium for each fixed local observation window. It does not by itself establish uniform relaxation in every moving window between the fronts. Such a reading would be false near a front, whose neighboring spins have a non-equilibrium law.

Fix: replace that prose with “every fixed finite observation window converges locally to equilibrium.” No change to Proposition fronts is needed.

Proposition allq, lines 360–380: valid. Couple the restrictions of nu and mu_r to agree on [-r,r]. The finite-propagation error is at most 2||f||_infinity |S| exp(-v log(4)t). If phi_r=d mu_r/d pi, then 0<=phi_r<=K exp(br), pi(phi_r)=1, and

    ||phi_r-1||_2^2 = pi(phi_r^2)-1 <= K exp(br).

Cauchy–Schwarz and spectral contraction give the second error at most

    2||f||_infinity sqrt(K) exp[b(m+2)/2] exp[-(g(q)-bv/2)t].

This proves the stated exponent and provides a finite prefactor. The ceiling in r is absorbed correctly. At t=0 one can use the true integer distance r+1-m>=2, so there is no issue from the displayed weaker bound d>=vt=0. The argument is a valid explicit-constant version of [CMST10, Theorem 2.1](https://arxiv.org/abs/0810.4237), whose scope includes general finite-range one-dimensional KCMs with positive gap, not only oriented examples.

The Markov-chain example, lines 382–390, is also valid: there are exactly 2r transitions in a word of length 2r+1. Their density ratio is bounded by the stated initial-state factor times exp(2delta r). Positivity of T ensures T_11<1 and nu(R>r)=alpha_1 T_11^{2r}. Distinct rows imply this positive stationary chain is not a product chain.

Fix: none to Proposition allq or the example.

7. Numerical audit

I ran the supplied script unchanged from referee_checks/, so it wrote referee_checks/data/checks.json without overwriting the supplied data. Every parsed JSON value matches claim_files/data/checks.json, including the seeded simulation output and floating-point slacks. The run took about 3.05 seconds. Its active-site continuous-time sampler uses the correct facilitated 1-to-0 rate q and 0-to-1 rate p, updates neighboring active sets correctly, and records observations before the next jump. Its unused T parameter is harmless.

Problem at manuscript lines 433–434: two of the recorded origin-infection estimates are outside two of their reported standard errors:

| q | t | Estimate | Equilibrium | Reported SE | Absolute discrepancy / SE |
| --- | --- | --- | --- | --- | --- |
| 0.6 | 45 | 0.6633333333 | 0.6 | 0.0272838305 | 2.3212772 |
| 0.75 | 70 | 0.8033333333 | 0.75 | 0.0229484124 | 2.3240533 |

The other 30 observable/time comparisons are within two reported standard errors. The two exceptions also remain above two standard errors if one uses the equilibrium Bernoulli variance instead. These modest deviations among many comparisons do not contradict convergence and do not estimate an exponential rate.

Fix: state the two exceptions explicitly, or replace the universal two-standard-error assertion by a description of the estimates and their sampling errors. Do not change seeds to remove them.

Problem at lines 429–430 and checks.py's opening description: the configurations are exhaustively enumerated, but arithmetic is binary floating point. In particular the recorded maximum slack at q=0.9 is 5.55e-17. This is consistent with rounding, but it is not exact arithmetic.

Fix: say “exhaustively in floating-point arithmetic,” or supply rational/interval verification. The independent rational check here supplies additional evidence but does not retroactively change the arithmetic of the supplied script.

Independent tests: referee_checks/independent.py imports no manuscript code and uses no external numerical library. It implements rate-one clocks by uniformization, retaining null rings, rather than using the supplied active-flip sampler. It ran 2,000 independent paths per q on [-439,439] with frozen healthy exterior, from a single zero at the origin, to time 20. The window exceeds 8e times the horizon. Finite propagation bounds the single-site finite/infinite-volume discrepancy probability by 4^-440. No simulated infection touched the boundary; maximum infection radii were 21 at q=0.6 and 30 at q=0.8.

Selected estimates of P(eta_0(t)=0), with one standard error:

| t | q=0.6 | q=0.8 |
| --- | --- | --- |
| 0 | 1.0000 | 1.0000 |
| 1 | 0.8955 ± 0.00684 | 0.9215 ± 0.00601 |
| 3 | 0.7070 ± 0.01018 | 0.8215 ± 0.00856 |
| 6 | 0.6370 ± 0.01075 | 0.8035 ± 0.00889 |
| 10 | 0.5720 ± 0.01106 | 0.7875 ± 0.00915 |
| 20 | 0.5845 ± 0.01102 | 0.8095 ± 0.00878 |

The q=0.6, t=10 value is itself about 2.53 estimated standard errors below equilibrium. There is no justification for claiming all independent estimates lie within two standard errors either. These simulations show relaxation on the observed timescale, with ordinary sampling fluctuations; they establish no asymptotic rate.

The independent generator test enumerated every state and every observation site for n=3,5,7, and added 500 random 31-site cases for each of four rational (q,theta) pairs. All 6,320 checks used exact Fraction arithmetic and had maximum slack zero. Separate two-infection examples give positive generator values at q=1/2 and q=0.49, confirming Remark rem:half.

The independent process used one thread, 31.58 seconds total, and peak RSS 15,990,784 bytes as reported by getrusage on macOS. A 1,100-second alarm and CPU limit were installed; no worker pool was used. The attempt to lower the supplied run's priority with nice was refused by the sandbox; the script still produced its complete output in about three seconds. Its time -l wrapper returned status 1 after a sandbox-denied sysctl. To resolve that status, I reran the supplied script directly under runpy with getrusage measurement: it exited zero and reproduced the supplied JSON again. That second run's elapsed time and peak memory are in referee_checks/supplied_direct.resources.json. Both numerical programs were single-threaded and below the requested resource limits. Results: referee_checks/independent.json, comparison.json, supplied_rerun.log and supplied_direct.log.

8. Bibliography and novelty search

All eleven bibliography entries were checked. Six journal/chapter DOI metadata records are retained as sources/*.crossref.json. Publisher records, arXiv title pages and the three GitHub references supply the remaining evidence. Capitalization, punctuation and conventional journal abbreviations are not discrepancies.

| Entry; manuscript lines | Verified record and result |
| --- | --- |
| BCMRT13; 466–468 | O. Blondel, N. Cancrini, F. Martinelli, C. Roberto, C. Toninelli; title matches; Markov Processes and Related Fields 19(3), 383–406 (2013); arXiv:1205.4584. [Publisher record](https://math-mprf.org/journal/articles/id1301/). No DOI is asserted in the manuscript. |
| BDT19; 469–470 | O. Blondel, A. Deshayes, C. Toninelli; title matches; Electronic Journal of Probability 24 (2019), paper 1, pages 1–32; DOI 10.1214/18-EJP246. [Journal record](https://doi.org/10.1214/18-EJP246), [arXiv:1803.08761](https://arxiv.org/abs/1803.08761). Crossref confirms pages 1–32. |
| CMRT08; 471–472 | N. Cancrini, F. Martinelli, C. Roberto, C. Toninelli; title matches; Probability Theory and Related Fields 140(3–4), 459–504 (2008); DOI 10.1007/s00440-007-0072-3. [Publisher](https://link.springer.com/article/10.1007/s00440-007-0072-3). The 2007 online date does not invalidate the 2008 volume year. |
| CMST10; 473–475 | N. Cancrini, F. Martinelli, R. Schonmann, C. Toninelli; title matches; Journal of Statistical Physics 138(6), 1109–1123 (2010); DOI 10.1007/s10955-010-9923-x; arXiv:0810.4237. [Publisher](https://link.springer.com/article/10.1007/s10955-010-9923-x). The preprint uses R. H. Schonmann; R. Schonmann is consistent with the publisher citation. |
| FA84; 476–477 | G. H. Fredrickson, H. C. Andersen; title matches; Physical Review Letters 53(13), 1244–1247 (1984); DOI 10.1103/PhysRevLett.53.1244. [APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.53.1244). |
| Mar26; 478–479 | F. Martinelli; title matches; ICM 2026 Proceedings, volume 5, 497–515; DOI 10.1137/25M180425X; published July 2026. [SIAM record](https://epubs.siam.org/doi/10.1137/25M180425X). Conjecture 2.11 is the asserted related convergence conjecture. |
| MST25; 480–481 | F. Martinelli, A. Shapira, C. Toninelli; title matches; 2025 preprint, arXiv:2510.20461. [arXiv record](https://arxiv.org/abs/2510.20461). Only v1 is listed. |
| MV19; 482–483 | T. Mountford, G. Valle; published title matches; Journal of Theoretical Probability 32(1), 282–302 (2019); DOI 10.1007/s10959-018-0812-6. [DOI record](https://doi.org/10.1007/s10959-018-0812-6), [arXiv:1609.01364](https://arxiv.org/abs/1609.01364). Crossref distinguishes online publication in February 2018 from print publication in March 2019. The preprint misspells Fredrickson; the manuscript uses the correct published spelling. |
| MathBrainRepo; 484–485 | [Public repository](https://github.com/yspennstate/math-brain-public) exists under the stated owner and is dated 2026. The citation's descriptive title identifies its contents. There is no claimed journal or DOI. |
| MathBrainPaper; 486–487 | [Linked paper directory](https://github.com/yspennstate/math-brain-public/tree/main/papers/math-brain-2026-10-24) contains main.tex and a PDF. Main.tex gives the stated author/title and date 26 October 2026, consistent with “October 2026.” |
| BrainFramework; 488–489 | [Public software repository](https://github.com/yspennstate/brain-framework-public) exists; owner, topic and 2026 date match. Its README identifies the brain framework. No journal or DOI is claimed. |

Fix: none required for these entries. Commit-pinned URLs would make the three mutable software references more reproducible, but their current citations are not false. The code-availability repository in line 432 also exists. The attempted published BDT19 PDF endpoint returned HTML; the usable full text here is the verified arXiv version, supplemented by the DOI metadata.

Search scope: since 2019, through 15 November 2026. I queried the arXiv API with a date-filtered Fredrickson search (61 records), a FA-1f/kinetically-constrained/one-facilitated search (48 records), and a Fredrickson/FA-1f plus single/convergence/relaxation search (15 records). Entire result sets fit within their requested page sizes. XML responses and screened abstracts are retained. I also searched titles and key phrases through web search and checked the bibliographies of the 2025 and 2026 surveys. These searches include the author's name as well as model terminology, so papers about variants can be separated from FA-1f.

Two requested Google Scholar searches were attempted with curl and a Mozilla user agent, restricting publication years from 2019. Both returned a “Verifying...” page, not search results: sources/scholar_single.html and scholar_relaxation.html. I did not obtain a completed Scholar search and make no claim to have done so.

Relevant comparisons:

- [Mountford–Valle, arXiv:1609.01364](https://arxiv.org/abs/1609.01364), published 2019: Theorem 1.1 treats a single seed, and Remark 1.2 allows origin-centered exponential tails, for q sufficiently close to 1. The proof explicitly uses that stronger restriction. It does not give all q>1/2. Their occupied spin is the facilitating state, so their spin convention must be reversed when comparing with this manuscript.
- [Blondel–Deshayes–Toninelli, arXiv:1803.08761](https://arxiv.org/abs/1803.08761), published 2019: Section 3 reproduces BCMRT-type local relaxation estimates for q>1/2 assuming initial infections already distributed through the relevant interval. The front LLN/CLT and process viewed from the front use a larger threshold. They do not supply the manuscript's unrestricted single-seed theorem.
- [Marêché, arXiv:1907.05844](https://arxiv.org/abs/1907.05844), published 2020: exponential convergence for supercritical KCMs with product initial laws and q close to 1. This does not establish the claimed full single-seed regime.
- [Ertul, arXiv:2103.00019](https://arxiv.org/abs/2103.00019), ALEA 19 (2022), 511–536: finite-interval cutoff and front results assume q above a contact-process threshold described as approximately 0.76. Proposition 4.1 reuses a q>1/2 relaxation estimate under a no-large-healthy-gap hypothesis; it does not remove the single-seed obstruction throughout q>1/2.
- [Hartarsky–Fabio Toninelli, arXiv:2212.08437](https://arxiv.org/abs/2212.08437), Probability and Mathematical Physics 5 (2024), 461–489: Theorem 3.3 assumes q sufficiently close to 1 and a product initial law (with extensions to suitable domination hypotheses). It does not cover arbitrary single-seed laws for all q>1/2. The second author here is Fabio, not Cristina Toninelli.
- [MST25](https://arxiv.org/abs/2510.20461) and [Martinelli's 2026 survey](https://epubs.siam.org/doi/10.1137/25M180425X) do not contain a proof of the claimed extension.
- [De Gaspari, arXiv:2508.06935](https://arxiv.org/abs/2508.06935): nonamenable graphs, high facilitating density in equilibrium and initially; no such theorem on Z.
- [Marić–Garrahan–Zadnik, arXiv:2609.18882](https://arxiv.org/abs/2609.18882), September 2026: low-temperature stochastic-generator expansions and metastable time scales after a quench. Inspection of its text found no fixed-q single-infection relaxation theorem.

I also screened [Shapira, arXiv:2005.13327](https://arxiv.org/abs/2005.13327), which concerns stationary spectral/persistence estimates, and the CBSEP comparison [arXiv:2006.01426](https://arxiv.org/abs/2006.01426), which supplies finite-graph mixing tools. Neither is the infinite-volume arbitrary-initial-law result here. Recent self-duality and relaxation-crossover papers concern different kinetic constraints or observables; e.g. [arXiv:2504.01258](https://arxiv.org/abs/2504.01258) studies DW/ZZZ/XOR variants and dynamical large deviations.

On the records examined, the new assertion is the transfer from a uniform spatial exponential-moment hypothesis to an origin-centered tail bound, yielding the full q>1/2 single-infection statement. The drift estimate itself is already present in BCMRT13 and should retain that attribution. The manuscript does retain it. Proposition allq is also correctly presented as a version of CMST10, rather than as a new general relaxation mechanism.

Required corrections before acceptance: fix lines 251–253; correct lines 433–434 and the exact-arithmetic wording at 429–430. Clarify the fixed-window scope at lines 353–354. No repair to Theorem 1.1 or Corollary 1.2 is needed on this audit.

Task: “You are an independent referee for a short probability paper. Work in this folder only.” Received 15 November 2026, 00:27 +04.
