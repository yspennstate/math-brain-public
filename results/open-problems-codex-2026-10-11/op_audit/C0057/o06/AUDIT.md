VERDICT: PASS (correct and complete)

# Independent audit of C0057

Date: 12 October 2026. Claimant verdict: SOLVED. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md read-only. Locations below are line numbers in the claimant's ATTEMPT.md as read during this audit. Downloads, independent scripts and results are confined to this audit folder.

## Claim and scope

ATTEMPT.md lines 5–7 claims: for every admissible critical face-weight sequence in Curien's bipartite model, every initial half-perimeter p >= 1, and every continuing adapted filled-in peeling algorithm, the infinite Boltzmann map is exhausted almost surely. Independent algorithmic randomness is permitted. The quantifier is that each such algorithm has almost-sure exhaustion; no simultaneous assertion over an uncountable collection of algorithms is needed or proved.

This answers the source question. I independently downloaded the supplied preliminary notes. PDF page 61, printed page 57, contains Corollary 27 and immediately asks, “Is the last corollary true for any critical weight sequence?” The infinite-plane model is expressly the admissible critical bipartite model in Theorem 8 (PDF page 48). Its criticality definition is Z^2 f'(Z) = 1 (PDF page 27). Thus restricting to bipartite maps is the source's scope, not an evasion. Continuing adapted algorithms are the meaningful scope: a rule that voluntarily stops plainly cannot satisfy exhaustion. The result is not limited to the type-a classes, finite f''(Z), or regular weights.

The mathematical argument establishes the affirmative exhaustion conclusion. It does not establish that the deduction is historically new, that no earlier solution exists, or that it is formally verified in Lean. Those are separate matters.

## Issues found

No mathematical failure or missing hypothesis affecting the exhaustion theorem was found.

Two editorial defects do not require mathematical repairs:

1. Lines 94–98 refer to “b(p) defined earlier,” although the summed swallowing rate b(p) is actually defined later, at lines 256–259. The earlier display at line 28 defines the individual side probability, not this sum. The intended rate is unambiguous when read with Lemma 4. Name the later definition explicitly.
2. Line 168 refers to “Lemma 6 above”; Lemma 6 is below, at lines 275–285. Change “above” to “below.” Its auxiliary proof invokes Lemma 5, but the universal argument has already supplied the same needed divergence in sections 2–5. This is a valid substitution, not an illicit use of the finite-f'' hypothesis. Lines 265 and 277–285 provide the geometry and compensator needed in the universal proof.

The absence of an identified earlier published solution is only a bounded search result. The report's references to a “new” result (lines 34, 170 and 330) should not be read as verified priority claims. This limitation does not affect the proof verdict.

## Verification of the unrestricted proof

### Source identities and exact kernel: lines 15–69 and 172–195

I checked the source definitions of h, the critical equations, the gluing probabilities in Definition 17 (PDF page 49), and the partition integral (5.3) (PDF page 54). They agree with the half-perimeter conventions used here. Each gluing side contributes nu(-k-1)/2 times h(p-k-1)/h(p); the factor 1/2 is necessary and correct.

I also independently fetched Budd, arXiv:1506.01590v3. Lemma 4, equation (40), on PDF page 16 applies when h_r^(1) is harmonic, without a regularity hypothesis. The bipartite simplification on PDF page 17 is precisely

    R_1(2k,2m) = d(k)d(m)m(2m+1)/((m+k)(2k-1)).

It transfers to the attempted half-perimeter kernel without a parity averaging factor.

More importantly, I re-derived the kernel directly from Curien's integral, independently of that notation transfer. With a_l = q_l binom(2l-1,l-1) Z^(l-1), criticality and admissibility give sum l a_l = 1. Therefore

    J'(r) = Z sum_{l>=2} l a_l (1-r^(l-1)).

The derivative is continuous up to 1 because sum l a_l is finite; finite f'' is unnecessary. The map G(y) = y(1-f(y)) has G(0)=0, G(Z)=1, G'(Z)=0 and G''(y)<0 in the interior, so G is strictly increasing on [0,Z]. The smallest-root identification for the tilted weights is valid. The change of variables g=G(Zr) in (5.3) consequently holds, including the endpoint where the derivative vanishes.

Nonnegativity permits Tonelli, and integration of each term gives

    integral_0^1 r^(k-1) J'(r) dr
      = (Z/k) sum_{m>=1} m(m+1)a_{m+1}/(m+k).

The identity a_{m+1} = ((2m+1)/(m+1)) d(m) nu(m), c=4Z, and d(k)=((2k-1)/(2k))d(k-1) yield the exact asserted kernel. At k=1 it yields nu(-1)=1/(2Z)=2/c. There is no exchange of a signed divergent series here.

Harmonicity at p=1 gives sum_{m>=0} nu(m)h(m+1)=h(1)=1. Since h(m+1) is comparable to sqrt(m), the positive sqrt moment is finite. Thus T(x) is finite for every x>0, despite possible infinite sum w_m. Nondegeneracy supplies a positive atom, so T and R are strictly positive. The two displayed comparisons for T follow individually from the ratios (m+p)/(m+k), with the stated directions.

### One-state bounds: lines 73–98

I re-derived each estimate (A)–(F):

- (A): for k>=p, T(k)<=T(p); summing k^(-3/2) gives R(p). The p/2 cutoff has the same bound by T(p/2)<=2T(p).
- (B): T(k)<=p T(p)/k for k<=p; summing k^(-1/2) after multiplication by k^2 gives p^(3/2)T(p).
- (C): m^2<=sqrt(p)m^(3/2) on m<=p, while sum_{m<=p}w_m<=2p T(p).
- (D): on m>p/2, m+p<3m and w_m/(m+p) is bounded below by a constant times sqrt(m)nu(m).
- (E): h is increasing, so downward transformed mass is no larger than untransformed mass. Upward jumps above p/2 have h(p+m)/h(p)<=C sqrt(m/p). Applying (A) and (D) proves the asserted bound, including arbitrarily large upward jumps.
- (F): for k in [ceil(p/2),floor(3p/4)], there are linearly many terms, the surviving h ratio is bounded below, and nu(-k-1)>=c p^(-3/2)T(p). The range lies within k<=p-2 for sufficiently large p. Summation gives b(p)>=c R(p).

All constants are independent of p. Finitely many exceptional p can be handled since R(p)>0. None of these arguments presumes regular variation, a first jump moment, or finite f''.

### Escape: lines 102–110

The reciprocal-h drift identity is exact:

    E[1/h(P_{n+1}) | P_n=p] = (1-delta(p))/h(p).

Telescoping expectations and monotone convergence give a finite expected sum of delta(P_n)/h(P_n). Each finite state contributes a fixed strictly positive amount whenever visited, because the exact kernel makes every negative atom positive. Consequently every finite state has finitely many visits. Taking finite unions over p<=M proves P_n tends to infinity. No irreducibility or scaling theorem is needed.

### Truncated logarithm and cancellation: lines 114–145

The recurrence h(j+1)/h(j)=1+1/(2j) is correct. It implies |log h(y)-log h(p)|<=C|y-p|/p when |y-p|<=p/2, including small states after a harmless adjustment. The h ratios in this region are bounded. Squaring and applying (B),(C) gives (G).

The delicate mean estimate also checks out. Under K, E[1/H]=1-delta(p), hence E[1-1/H]=delta(p). Absolute integrability follows from E[1/H]<=1. On the large-jump set, the absolute transformed expectation equals sum nu(y-p)|H-1|, which is bounded by transformed plus untransformed mass. Both are O(R(p)): negative untransformed mass is controlled by the negative tail, and positive untransformed mass is at most transformed mass because H>=1. Thus the small-jump mean of 1-1/H is O(R(p)). The Taylor remainder of u-(1-exp(-u)) is O(u^2) on the bounded small-jump interval. This proves (H).

This reasoning does not require E|log H| for the entire jump distribution. Omitting the truncation could indeed invalidate such a proof; the submitted proof retains it throughout.

### Divergence of the rate sum: lines 149–164

The localization is predictable. A_n is F_n-measurable, tau_K is a stopping time, and 1_{n<tau_K} is F_n-measurable. The increment that crosses K contributes at most R(1), so the displayed overshoot bound K+R(1) is correct, rather than K alone.

The stopped martingale has bounded total expected conditional variance and is L^2 bounded. Standard martingale convergence therefore applies. Simultaneously, the stopped count of large relative jumps has finite expectation by (E), so it is finite almost surely. These conclusions hold on a common probability-one event for all integer K. On the event sum R(P_n)<infinity, choose an integer K larger than that sum: the stopping time is infinite, the drift is absolutely summable, the centered truncated increments converge, and only finitely many actual log increments differ from them. Every individual omitted increment is a finite real number even if its distribution has no log moment.

It follows that log h(P_n) has a finite limit on that event, contradicting the independently established escape P_n -> infinity. Thus sum R(P_n)=infinity almost surely. The proof does not apply a convergence theorem after conditioning on the possibly nonmeasurable-at-finite-time event of finite rate sum; localization avoids that error.

### Target survival and map exhaustion: lines 168, 254–265 and 275–285

I checked the deterministic boundary geometry rather than assuming a perimeter hazard automatically discovers a target. There are 2p cyclic edge occurrences. From the peeled edge to any other marked occurrence, one of the two directed distances is at most p. A gluing with finite half-perimeter k pairs the peeled edge with the occurrence at distance 2k+1 on the chosen side and fills the intervening finite hole. If k>=ceil(p/2), the marked occurrence is strictly inside that swallowed arc, so it becomes interior. The chosen side's probability is exactly the summed b(p). If the target itself is peeled, it becomes interior immediately. Repeated vertices cause no problem when occurrences are marked.

For a target introduced at a finite time, its interiorization time is an exploration stopping time. The stopped hazard r_n is zero after discovery and, on survival, is at least b(P_n). I recomputed the supermartingale step:

    E[Z_{n+1}|F_n] = Z_n exp(r_n)(1-r_n) <= Z_n

on survival, with both sides zero otherwise. Bounded optional stopping at the first compensator crossing of K and then letting the horizon increase proves the stated bound exp(-K). Since P_n eventually exceeds the cutoff and sum R(P_n) diverges, sum b(P_n) diverges; thus perpetual target survival has probability zero. This is only a sufficient hazard condition, as the submission correctly notes.

There are countably many introduced boundary occurrences, each finite step introducing finitely many. Conditioning at introduction, or splitting according to its finite introduction time, extends the argument to each. Finally, a finite dual path from the root face to any missing face would have a first unexplored face across an exposed edge from an explored face. Interiorizing that edge requires the adjacent unexplored side to have been explored or filled, contradicting permanent absence. Connectivity and finite face degrees finish exhaustion. These steps do not use the auxiliary finite-f'' result.

## Auxiliary argument: lines 200–312

I checked it separately; the unrestricted proof does not depend on it. For finite f''(Z), J''(1-)=-2-Z^3 f''(Z)=-2D, so J'(r)~2D(1-r). The endpoint integral is asymptotic to 2D/j^2; multiplication by d(j) yields the stated partition and negative-tail constants. The contribution away from 1 is exponentially small.

The coefficient comparison in Lemma 2 gives precisely the positive 3/2 moment. The negative tail gives a finite first moment. Source oscillation plus the strong law then forces mean zero. In the characteristic-function argument, |exp(ix)-1-ix|<=C min(x^2,|x|) is valid; the positive contribution is little-o by dominated convergence. The negative Riemann sums have integrable bounds at both endpoints for alpha=3/2 and give uncentered spectrally negative stable attraction, with positivity parameter 2/3.

I fetched Caravenna–Chaumont, arXiv:math/0602306v2. Theorem 1.1 (PDF page 4) applies to stable attraction with positivity parameter in (0,1) and rescaled starting positions converging to zero. PDF page 2 explicitly extends the result to strict positivity by V(x-). The submitted application uses the correct conditioning and starting scale. The Jeulin argument at lines 269–273 correctly uses convergence in distribution and Tonelli; independence is not needed.

For the explicit zeta example, summing the defining coefficients reproduces both critical equations and f''(Z)=C Z^(-2)(zeta(2)-3zeta(3)+2zeta(4)). Its coefficient radius is Z, so it is genuinely nonregular. The partial fraction identity at line 310 is exact; the last two summed terms give H_j/j^3. The resulting I_j formula and the two expressions for D agree.

## Independent computation

I wrote and ran checks.py without running or copying the claimant's test scripts. Output is checks.json.

- 80 exact rational comparisons of the kernel with the independently integrated partition formula, for four finite-support critical laws and negative indices 1–20: all equal exactly.
- 64 exact rational transformed transition-row normalization and reciprocal-h drift checks, at p=1–16: all passed. All tested delta(p) were positive.
- Exact recurrence checks for h at j=1–29: all passed.
- Exhaustive cyclic-distance checks for every marked position, p=8–100, and every admissible k>=ceil(p/2): the chosen-side arc strictly passes the target.
- 36 floating-point transition rows at perimeters up to 4096, including a positive atom at 1,000,000 and a mixture of widely separated atoms. Largest normalization error was 1.052e-9. Largest ratios to R(p) were 2.0001 (large-jump mass), 0.5215 (absolute truncated drift), and 0.2923 (truncated second moment). The smallest tested b(p)/R(p), p>=8, was 0.06065. The rounding tolerance was 2e-8.
- Independent 45-digit quadrature of the zeta-example partition integral at j=1,2,7,30 agreed with the closed formula to absolute error at most 7.01e-46.

These finite tests support the algebra and indexing; they do not prove uniform bounds over all laws or test infinite f'' directly. The general inequalities, endpoint justification, and localization were checked analytically above. I did not rerun Lean or treat the claimant's Lean results as formal verification of the probability theorem.

## Literature check and limits

All network reads used Python requests, with no built-in web search. The supplied notes, Budd's paper and the conditioned-walk paper were fetched independently, HTTP 200, and their relevant statements inspected. Local PDF text extractions and request metadata are retained.

I queried the arXiv API for peeling with criticality/exhaustion, then the narrower peeling-and-Boltzmann query (arxiv.xml and arxiv_boltzmann.xml). Relevant abstracts included Budd's 2015 paper; Geometry of infinite planar maps with high degrees (1602.01328); Markovian explorations of random planar maps are roundish (1902.10624); Simple peeling of planar maps with application to site percolation (1909.10217); Infinite stable Boltzmann planar maps are subdiffusive (1910.09623); On large 3/2-stable maps (2304.01167); and Characterisation of Markov property on planar maps (2505.05447). The inspected statements concern regular/stable laws, half-plane constructions, or Markov-property characterizations. None of these inspected statements settles this exact unrestricted exhaustion question or supplies a counterexample.

An independent OpenAlex search for filled peeling critical Boltzmann maps returned HTTP 429. I do not infer nonexistence of an earlier solution from that failure or from the bounded arXiv screening. This is a verified written-proof verdict, not SOLVED_IN_LITERATURE and not a certification of priority. No claim about nonbipartite models, anticipating or stopping algorithms, scaling limits for arbitrary weights, or exhaustive formalization follows from this audit.
