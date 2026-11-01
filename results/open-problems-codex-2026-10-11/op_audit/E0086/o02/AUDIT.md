VERDICT: PASS (correct and complete)

Independent audit, 12 October 2026. This passes as the explicitly claimed negative answer to existence of a deterministic almost-sure equivalent under the source's unrestricted moving-offset hypotheses. It is not a classification of all offset sequences or a theorem giving the asymptotics for regular sequences. No fatal proof error or necessary mathematical repair was found.

## Claim and source fidelity

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md from the claimant's folder without modifying them. Locations below are line numbers in the audited ATTEMPT.md.

The principal claim (lines 140–152, 194–196) is: for each fixed 1/4 < alpha < 1/2 there is a deterministic sequence of nonzero singleton offset sets H_n in the fixed class H(1), with n^alpha < |h_n| <= 2n^alpha, such that almost surely

    limsup M_{H_n}(n)/(log n)^2 = 1/pi,
    limsup_m M_{H_{2^m}}(2^m)/(log 2^m)^2 <= 4alpha(1-alpha)/pi < 1/pi.

Furthermore there is no deterministic eventually positive function f(n), even one depending on this whole deterministic sequence and allowed to oscillate, with M_{H_n}(n)/f(n) -> 1 almost surely. At alpha = 3/8 the two constants are 1/pi and 15/(16pi).

I independently downloaded https://arxiv.org/pdf/1606.03787. PDF pages 2–4 and 6 confirm the corrected objects in lines 9–19: H is a class of bounded-cardinality offset sets, not a region of candidate sites; the symbol in Open problem 2 is membership, not intersection. A site x qualifies when x is visited and every x+h, h in H, is unvisited. The source specifies positive-time hitting times and first hit of the inner disc boundary for tau_n. The singleton construction satisfies the admissibility condition P(T_x<T_H)>0 for every x outside H, including x=0. The source imposes no monotonicity, fixed direction, or temporal regularity on H_n. The counterexample therefore meets the actual source's hypotheses, including its emphasized nonempty power-annulus restriction. The problem title and the supplied description of an annular site maximum would be misleading if used instead of the PDF definitions.

The PDF really prints M_{H_n}(n) = max_x K(tau_n,x) in its subsidiary conjecture. Page 2 really gives deterministic-time constant 1/pi and radius-n stopped constant 4/pi. Thus the claimant's literal refutation of that displayed equality is correct. It must not be presented as refuting an unprinted corrected-time conjecture.

## Issues and limits of the verdict

1. **Scope of SOLVED (lines 3–5, 152, 227).** The result rules out a deterministic almost-sure equivalent in the full unrestricted class by an admissible counterexample. It does not give all possible random asymptotic descriptions, exact liminf of the example, a matching constant for alpha <= 1/4, or an asymptotic for fixed-direction/regular sequences. The attempt expressly states these limits. No special-case formula is passed off as a universal formula. The counterexample is sufficient for the claimed negative conclusion, but SOLVED must retain that qualification.

2. **Historical claim metadata.** Early CLAIMS.jsonl entries still describe the main annular regime as unresolved or record a remaining lower-bound gap. Those statements describe the earlier positive-asymptotic work; they do not invalidate the later counterexample. A universal positive-equivalent theorem is disproved, while the stated restricted lower-bound questions remain unresolved. This is a bookkeeping ambiguity, not a proof gap.

3. **External inputs and verification scope (lines 23, 41, 154, 204–212).** This is a written proof using classical theorems, not a complete Lean formalization. The finite checks do not prove the asymptotics. I independently checked the needed covered-disc theorem and potential-kernel statements in their cited full texts. The 2001 maximum-local-time theorem was checked against its explicit statement in the original problem source and the independent 2025 version of the Hao–Li–Okada–Zheng paper; I retrieved the 2001 bibliographic record through Crossref, not its full proof. Nothing in the argument requires treating the claimant's simulations or its Lean result as proof of a probabilistic theorem.

## Independent derivation of the proof

**Results 1–2, lines 23–37.** A coordinate increment has mgf (1+cosh t)/2 <= exp(t^2/2). Coordinate Chernoff bounds and a union over both coordinates and j <= n give 4n exp(-r^2/(4n)). At r=n^(1/2+epsilon)/3 this is summable over all integer n. The resulting range diameter is less than the offset norm, so every visited site qualifies. The ratio comparison with the stopped maximum is then at most 1/4. The eight-point detour cycle consists of nearest-neighbor steps and avoids the removed point; the separate two-step return loop handles positive-time T_0. These checks establish H_n in the same H(1) at every n.

**Result 3, lines 41–72.** For g(z)=a(z)+a(h)-a(z-h), g(0)=0, g(h)=2a(h), and (P-I)g=delta_0-delta_h. The logarithmic asymptotic makes g bounded for each fixed h. Stopping at T_h wedge m, bounded convergence on the left and monotone convergence on the occupation count give E N_h=2a(h). Strong Markov at returns to 0 gives the geometric tail with success probability 1/(2a(h)). Including the time-zero visit explains the exponent k-1. An eligible site's first visit is one of n+1 deterministic candidate times; conditioning at each time and discarding the first-visit restriction only enlarges the event. The finite-time inequality has the correct direction.

For dyadic blocks there are O(N^(2alpha)) offsets and O(N) start times. The tail exponent is 1+2alpha-pi*c/(4alpha)+o(1). A strictly negative exponent is summable along N=2^m; summability over every integer N is neither claimed nor needed. This is a simultaneous bound and allows unrestricted temporal variation. Letting rational alpha decrease to zero proves the subpolynomial-offset conclusion. The alternating example in result 4, lines 76–86, follows: the even offset exceeds every possible range diameter, and the odd offsets have subpolynomial norm. The empty-set observations are unnecessary for the final result.

**Result 5, lines 100–136.** The killed-disc transition matrix is symmetric, so its Green matrix is symmetric. Strong Markov at T_h gives the exact Schur identity

    B_{R,h} = G_R(0,0) - G_R(0,h)^2/G_R(h,h).

The number of returns counted in B is geometric because the process restarts at 0 and terminates on hit of h or disc exit. Stopping the potential-kernel increment identity gives G_R(x,z)=E_x a(S_sigma-z)-a(x-z). Exit occurs at distance between R and R+1; with |h|=Theta(n^alpha), R=n^s, s>1/2, the kernel expansion is uniform and gives leading coefficients (2/pi)s, (2/pi)s and (2/pi)(s-alpha) for the three Green entries. I recomputed the elimination coefficient:

    (2/pi)[s-(s-alpha)^2/s]
      = (2/pi)(2alpha-alpha^2/s) = b_s(alpha).

The bounded errors remain O(1) after division because the denominator is Theta(log n). As s decreases to 1/2 this coefficient decreases to g(alpha)=4alpha(1-alpha)/pi.

On the global confinement event, displacements after a candidate's first visit stay within R/2, hence cannot exit the translated radius-R disc before time n. Eligibility forces avoidance of h as well. The event can thus be enlarged to k geometric visits before either killing mechanism, conditional at its candidate start time. This gives the stated confinement term plus (n+1) exp(-(k-1)/B). No conditioning on confinement is incorrectly substituted for the ordinary Markov law. Choosing b_s(alpha)<c gives a polynomially decaying fixed-time tail. The temporal-witness-set union for result 5(ii) adds precisely its cardinality factor; no independence is needed.

**Result 6 construction and hole lemma, lines 158–180.** The common block annulus uses lower radius (2N)^alpha and upper radius 2N^alpha. These are in the correct order. Its O(N^(2alpha)) lattice points fit inside N time slots eventually, since 2alpha<1. At every actual scan time the same offset lies strictly outside n^alpha and at most 2n^alpha. The fallback also obeys both inequalities, including small n.

Writing L=2^alpha, c=(L+2)/2 and d=(2-L)/4, I recomputed c-d-L=d and 2-c-d=d. Rounding the center loses at most 1, absorbed eventually by d*N^alpha. Thus the common annulus contains a closed lattice disc of radius d*N^alpha. Coverage of the entire translated annulus would imply coverage of this disc. The independently fetched Dembo–Peres–Rosen Theorem 1.1 gives largest covered radius (2N)^(1/4+o(1))=o(N^alpha). Its centers are unrestricted. Its open-disc convention suffices for the needed upper-bound contradiction with a covered closed disc. This argument supplies a hole uniformly over every x on the same sample path, rather than falsely asserting avoidance of every prescribed offset.

**Limsup and dyadic bound, lines 182–192.** Choose a favorite at the block start N. A hole at time 2N stays a hole until its assigned scan time. That favorite is already visited and its local time cannot decrease, so the scanned boundary maximum is at least L_N. Although the successful index depends on the walk, the schedule does not. The logarithms of N and its scan time are asymptotically equal; the global maximum theorem supplies the lower limsup 1/pi and the global upper bound supplies equality. At the deterministic dyadic times, the fixed-time polynomial tails from result 5 are summable. Borel–Cantelli therefore proves the smaller dyadic limsup. This step does not confuse convergence in probability with almost-sure convergence.

**Exclusion of all deterministic equivalents, line 194.** If f/(log n)^2 exceeds some d>g along a deterministic subsequence, almost-sure M/f -> 1 forces M/(log n)^2>c for any g<c<d along that subsequence eventually. Bounded convergence of the event indicators forces probabilities to tend to 1, contradicting result 5(i). Hence deterministic limsup f/(log n)^2 <= g. Combining this with ratio convergence would force pathwise limsup M/(log n)^2 <= g, contradicting 1/pi. This additional argument is essential: nonconvergence on the log-squared scale alone would not exclude an oscillating deterministic equivalent. It is valid as written.

## Independently executed checks and literature search

All audit scripts, fetched documents and logs are in this audit folder. I did not execute or copy the claimant's check scripts.

- `independent_checks.py` enumerated all 16,384 seven-step paths, checking three offset boundary tails and truncated killed-visit tails for every k=1,...,9. The exact small kernel values used were 1, 4-8/pi and 4/pi. It also checked far-offset equality pathwise for offset (8,0). All assertions passed.
- Nine independently assembled sparse killed-chain calculations used radii 6,11,17 and offsets (1,0),(2,1),(4,0). Direct trap removal agreed with Green elimination to maximum absolute error 1.333e-15; symmetry was checked separately.
- Nine scan-geometry cases used alpha=0.26,0.375,0.49 and N=512,8192,131072, checking membership at actual scheduled times whenever the scan fits, plus contained-disc membership. Non-fitting finite blocks were recorded, not silently treated as fitting. Five seeded N=8192 walk checks verified the favorite/hole implication for the deterministic alpha=3/8 schedule. These finite checks supplement the analytic proof only. Results are in `independent_checks.json`.
- I fetched Dembo–Peres–Rosen, https://arxiv.org/pdf/math/0503139, and verified Theorem 1.1 on PDF page 2. I fetched Lawler–Limic, https://www.math.uchicago.edu/~lawler/srwbook.pdf, and verified Proposition 4.4.1, Proposition 4.4.2 and Theorem 4.4.4 on pages 86–88, including the exact 2/pi normalization and constant term.
- Fresh arXiv API searches used Okada with boundary/favorite terms and a focused random-walk plus favorite-sites/generalized-boundary query. The focused search returned the 2026 one-dimensional transient paper and arXiv:2409.00995v2 among related records. I fetched the latter PDF: its Theorems 1.1–1.2 concern cardinality of simultaneous favorite sites, not changing-offset boundary maxima. Its equation (1.1) independently states the deterministic-time maximum theorem used here. The other recent favorite-site abstracts inspected concerned one-dimensional walks. No earlier annular-scanning solution or counterexample was identified in these bounded searches.
- The fresh OpenAlex works search returned HTTP 429, so it provides no negative literature evidence. Crossref successfully identified the 2001 Dembo–Peres–Rosen–Zeitouni article and DOI 10.1007/BF02401841. Network evidence is saved in `fetch_log.json` and `followup_log.json`. These searches do not establish novelty or exhaust the literature.

The established result is the stated admissible counterexample and consequent failure of deterministic almost-sure equivalents in the unrestricted class. Regular-sequence asymptotics and the smaller-alpha matching-constant questions are not proved by this attempt.
