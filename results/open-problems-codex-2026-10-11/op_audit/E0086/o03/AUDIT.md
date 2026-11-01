VERDICT: PASS

Independent audit of E0086, 12 October 2026.

The counterexample is correct and complete for its stated negative conclusion: the source's unrestricted moving-offset hypotheses do not guarantee any deterministic almost-sure equivalent. This is not a classification of all offset sequences. No mathematical repair is necessary.

## Claim and source match

I read STATUS.md, all 227 lines of ATTEMPT.md, all 17 entries of CLAIMS.jsonl, and LITERATURE.md in the claimant's directory, read only.

ATTEMPT.md lines 138-196 claim that for every fixed alpha in (1/4,1/2), there exists a deterministic singleton sequence H_n in H(1), contained in {h: n^alpha < |h| <= 2n^alpha}, such that almost surely

    limsup_n M_{H_n}(n)/(log n)^2 = 1/pi,
    limsup_m M_{H_{2^m}}(2^m)/(log 2^m)^2 <= g(alpha),
    g(alpha) = 4 alpha(1-alpha)/pi < 1/pi.

Moreover no deterministic eventually positive f(n), even one depending on the entire offset schedule and allowed to oscillate, satisfies M_{H_n}(n)/f(n) -> 1 almost surely. At alpha=3/8, g(alpha)=15/(16 pi); the arithmetic checks.

I independently fetched https://arxiv.org/pdf/1606.03787 and checked PDF pages 2-4 and 6. The intake description misreads membership in H as intersection and describes an annular region of candidate sites. The source instead defines a class H of bounded-cardinality offset sets and

    partial_H G = {x in G: x+H is contained in G^c},
    M_H(n) = max_{x in partial_H R(n)} K(n,x).

Open problem 2 specifies D-tilde_n in H, outside D(0,a_n), particularly in its radius-[a_n,2a_n] annulus. It imposes no nesting, fixed direction, or temporal regularity. The construction meets these exact hypotheses with cardinality one, without empty sets or adaptive offsets. A counterexample at one admissible alpha already defeats general existence of a deterministic equivalent. This is not passing a positive special-case theorem off as the whole problem.

This PASS certifies the negative result for the actual source observable. It does not certify a solution for a different annular candidate-site maximum or a new covered-disc-radius theorem.

## External inputs independently checked

The fetched source, PDF page 2, explicitly states L_n/(log n)^2 -> 1/pi and J_n/(log n)^2 -> 4/pi almost surely, where L_n=max_x K(n,x), J_n=max_x K(tau_n,x). It defines tau_n as first hitting the inner boundary of the closed lattice disc and T_A as positive-time hitting. PDF page 6 really prints deterministic time n on one side of its conjectural equality and tau_n on the other.

I independently fetched https://arxiv.org/pdf/math/0503139, version 3. Dembo-Peres-Rosen, Theorem 1.1, PDF page 2, gives largest completely covered disc radius t^{1/4+o(1)} at deterministic time t, with unrestricted center, and the different radius-r exit-time exponent 1/2. The global upper bound over centers is precisely what the hole lemma needs. The open-disc convention is harmless: a covered closed lattice disc has a covered open subdisc of the same radius.

I fetched https://www.math.uchicago.edu/~lawler/srwbook.pdf. Pages 86-88, Proposition 4.4.1, Proposition 4.4.2, and Theorem 4.4.4 confirm the mean 2a(h), (P-I)a=delta_0, and

    a(h)=(2/pi)log|h|+(2 gamma+log 8)/pi+O(|h|^{-2}).

The maximum-local-time theorem is a classical input with constants independently verified in the source. Crossref identified the original Acta Mathematica article, DOI 10.1007/BF02401841. My Project Euclid PDF request returned HTML, so I do not claim to have inspected the original 2001 proof. That does not invalidate the standard input used here.

## Proof audit by ATTEMPT.md location

Lines 21-37, far offsets and admissibility. The coordinate MGF (1+cosh t)/2 <= exp(t^2/2) gives the stated bound 4n exp(-r^2/(4n)). At r=n^{1/2+epsilon}/3 the integer-time series converges. Range diameter is at most twice maximal displacement, so eventually no sufficiently long offset connects visited points. Boundary equality follows, including the pathwise/adaptive version. The eight-point cycle gives a finite detour around a nonzero singleton. For x=0, a two-step loop through a neighbor different from h handles positive-time return. Thus every singleton used belongs to H(1).

Lines 27-29, printed conjecture. M_{H_n}(n)<=L_n and the positive J_n limit imply limsup M_{H_n}(n)/J_n<=1/4, precluding eventual equality. This correct objection to the printed time mismatch is separate from the main annular counterexample.

Lines 39-55, killed returns. For g(z)=a(z)+a(h)-a(z-h), I checked g(0)=0, g(h)=2a(h), and (P-I)g=delta_0-delta_h. For fixed h, the kernel asymptotic makes g bounded. Stopping at T_h intersect m and using recurrence, bounded convergence, and monotone convergence yields E N_h=2a(h). Strong Markov at visits to zero gives the geometric law counting the initial visit, with tail (1-1/(2a(h)))^{k-1}. The finite-time argument correctly unions over visit indices, not sites. Removing first-visit restrictions and permitting the unrestricted future only enlarge the events.

Lines 57-86, uniform bound and exterior example. There are O(N^{2alpha}) possible offsets and O(N) start indices in a dyadic block. The exponent 1+2alpha-pi c/(4alpha)+o(1) is negative at the claimed threshold and summable over N=2^m. The event already covers every time in the block; no extra time union is omitted. Countable intersection and alpha decreasing to zero justify the subpolynomial conclusion. Alternating offsets beyond the deterministic range diameter with logarithmic offsets gives the exterior example's claimed normalized liminf and limsup. The empty-set variant is unnecessary for result 6.

Lines 100-124, disk Green function. Strong Markov at T_h and symmetry of the killed transition matrix give

    B_{R,h}=G_R(0,0)-G_R(0,h)^2/G_R(h,h).

The denominator is positive; finite exit expectation follows from a uniform finite path-to-exit probability. Stopping the kernel gives G_R(x,z)=E_x a(S_sigma_R-z)-a(x-z), with correct sign. At exit R<|S_sigma_R|<=R+1. For R=n^s, s>1/2, and n^alpha<|h|<=2n^alpha, alpha<1/2, the boundary expansion is uniform. The diagonal coefficient is 2s/pi and the off-diagonal coefficient is 2(s-alpha)/pi. Independent algebra gives

    2s/pi - [2(s-alpha)/pi]^2/(2s/pi)
      = (2/pi)(2alpha-alpha^2/s).

The error remains O(1) after division by a denominator of order log n. This coefficient decreases to g(alpha) as s decreases to 1/2.

Lines 126-136, finite-time and block tails. On confinement, both y and the original walk lie within R/4 of the origin, so future displacements from y stay within R/2. Eligibility implies k visits before hitting h or exiting the translated radius-R disc. The probability is bounded without conditioning on the future-dependent confinement event; no independence is assumed. The killed return count is geometric with mean B_{R,h}. This yields

    P(M_{H_n}(n)>=k) <= 4n exp(-n^{2s-1}/64)
                              +(n+1)exp(-(k-1)/B_{R,h_n}).

For c>g(alpha), taking s close enough to 1/2 makes 1-c/b_s(alpha) negative. This gives polynomial decay, stronger than convergence in probability. The witness-diversity factor N^{rho+eta} in the block argument is correctly paid.

Lines 158-180, scan and hole lemma. A_N={(2N)^alpha<|h|<=2N^alpha} is valid at every scheduled time in [N,2N). Its O(N^{2alpha})=o(N) offsets eventually fit. The fallback floor(n^alpha)+1 meets both annular inequalities for all n>=1. For L=2^alpha, c=(L+2)/2, d=(2-L)/4, the identities c-d-L=d and 2-c-d=d are exact. Once dN^alpha>1, the floor error is dominated and D(q_N,dN^alpha) lies in A_N. Complete coverage of x+A_N would imply a covered translated disc of that radius. The global covered-disc theorem rules this out simultaneously for all x when alpha>1/4.

Lines 182-186, all-time limsup. The favorite chosen at block start N has at least L_N visits at any later scan time. A hole absent at 2N remains absent at its scheduled time. The schedule is deterministic; only the successful witness index is random. Thus M_{H_{n_N}}(n_N)>=L_N. Since log n_N/log N tends to one, limsup>=1/pi. The global bound M_{H_n}(n)<=L_n supplies the reverse inequality.

Lines 188-192, dyadic limsup. Explicit polynomial tails are summable at n=2^m. Borel-Cantelli and a countable decreasing sequence of thresholds give the bound g(alpha). There is no invalid inference from convergence in probability alone.

Line 194, deterministic equivalents. If deterministic f had normalized limsup above g(alpha), choose a deterministic subsequence where f>=d(log n)^2 with g(alpha)<c<d. Assumed ratio convergence makes the indicators of M>c(log n)^2 tend to one almost surely along that subsequence. Bounded convergence makes their probabilities tend to one, whereas the established upper tail makes them tend to zero. Any proposed f must therefore have normalized limsup<=g(alpha), and ratio convergence would force the same bound on M. This contradicts the proven limsup 1/pi. The argument excludes oscillating equivalents too.

## Independent computations

I wrote and ran referee_verify.py in this directory without reusing claimant scripts or outputs. Detailed results are in referee_verify_results.json.

- Enumerated all 4^8=65,536 eight-step paths. For h=(1,0),(2,0),(1,1), nine thresholds each were checked against killed-return and boundary union bounds using a(h)=1,4-8/pi,4/pi. All 27 pairs passed. Integer counts were exact; analytic comparisons used floating point. The h=(9,0) displacement identity passed on every path.
- Independent killed-matrix solves for radii 4,9,17 and traps (1,0),(2,1),(3,0) checked Green elimination and symmetry. All nine passed; maximum discrepancy 1.333e-15.
- Enumerated scan annuli and contained discs for alpha=0.26,0.375,0.45 and N=512,4096,32768. All nine geometry cases passed. Actual assigned-time annular membership was checked whenever the scan fit. Non-fitting finite blocks occur and are handled by the fallback.
- Twelve independently seeded walks through 2N, with N=4096 and alpha=3/8, checked the witness implication against a schedule fixed beforehand. Every run had an end-of-block hole around the start favorite; at its scan time it preserved eligibility and at least the start favorite's local time.

Finite checks supplement the proof and do not prove asymptotic theorems. I did not rerun the claimant's Lean job or rely on its claimed formalization. The displacement lemma was checked directly and on exhaustive paths.

## Issues and limits

No failed mathematical step or missing hypothesis was found in result 6.

ATTEMPT.md line 200 informally calls tau_n an exit time, although line 9 correctly defines inner-boundary hitting. The wording should say inner-boundary hitting time. This is editorial: sigma_R is separately and consistently an actual exit time at line 100; no counterexample estimate interchanges these conventions. The source explicitly supplies the constants used in result 2. No proof repair is required.

The SOLVED label must retain the negative-answer scope stated in ATTEMPT.md lines 3,152,196,227. Proved: some admissible deterministic annular sequences lack every deterministic almost-sure equivalent. Not proved: complete liminf/limsup classification; matching constants for regular or fixed-direction sequences; a theorem for every sequence with alpha<=1/4; or the exact liminf of this example. The claimant expressly acknowledges these limits. An assertion that regular sequences have constant g(alpha) remains conjectural here. Internal priority and unpublished lower-bound reports were not independently authenticated and are not inputs to this verdict.

## Brief literature search

I independently queried the arXiv export API for random walk + boundary + local time; random walk + moving offset/generalized boundary/annular; and favorite sites + random walk. Requests and returned titles/abstracts are recorded in referee_search_log.json, with raw responses saved locally. Returned abstracts were inspected. ArXiv:2409.00995 concerns simultaneous favorite-site counts, while 1911.11810 and 1903.04045 concern exceptional points in finite-domain cover-time regimes. They do not settle or contradict the scan result. Both OpenAlex requests returned HTTP 429. Crossref located the classical 2001 reference.

No earlier matching solution or known counterexample was identified in this bounded search. That does not establish novelty or exhaustive coverage. Independently fetched inputs are saved as source.pdf, covered.pdf, and potential.pdf, with extracted text. All audit writes stayed in this directory; the claimant's directory remained read only.
