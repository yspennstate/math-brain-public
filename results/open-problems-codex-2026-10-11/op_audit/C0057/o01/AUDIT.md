VERDICT: PASS (correct and complete)

Independent audit of C0057, 12 October 2026. I read STATUS.md, all 336 lines of ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's folder. I independently fetched the primary source and cited papers, re-derived the main argument, and wrote separate arithmetic checks. No substantive mathematical failure or missing hypothesis was found. The unrestricted affirmative conclusion follows from the written argument and the cited standard peeling identities; it is not inferred from numerical experiments or the Lean file.

## Exact claim and scope

ATTEMPT.md lines 5–7 and CLAIMS.jsonl claim: for each admissible critical face-weight sequence q in Curien's bipartite model, each finite initial half-perimeter l >= 1, and each continuing adapted filled-in peeling algorithm, the infinite q-Boltzmann map under P_infinity^(l) is exhausted almost surely. Independent auxiliary randomness is allowed. No regular variation, stable domain of attraction, regularity, or finite f''(Z) is assumed in the main argument.

This answers the intended open question immediately following Corollary 27 on PDF page 61, printed page 57, of the supplied preliminary notes. It concerns the infinite map of the plane, not the half-plane map. The quantifiers are “for each algorithm, probability one”; a single exceptional set working simultaneously for every conceivable algorithm is not claimed or needed.

The primary source's Proposition 5 and Definition 9 give f(Z)=1-1/Z and Z^2 f'(Z)=1. Theorem 8 applies to every admissible critical q and every l >= 1. Criticality itself forces a positive coefficient with index >= 2, so the nondegeneracy at line 18 does not remove any critical case. The source's type-3/2 classification is subcritical; its appearance in the printed Corollary 27 interval does not create an additional critical case that this proof omits.

## Issues found, with locations

These are presentation issues, not proof gaps requiring a new mathematical argument:

1. **Stopping convention, line 5 (“excluded, as in the source”).** The source actually permits the cemetery choice A(e)=dagger in its formal algorithm definition (PDF page 32). It also implicitly requires peeling the distinguished hole for filled-in explorations (PDF page 34). Corollary 27 does not explicitly restate a nonstopping condition. A rule that stops immediately cannot exhaust even a quadrangulation, so nonstopping is necessary for the intended corollary as well as its extension. The claimant states that condition correctly, but should describe it as the necessary continuing-exploration interpretation rather than an explicit exclusion in the source. This is not a restriction to a special class of critical weights.

2. **Forward references, lines 94 and 168.** The explicit definition of b(p) is at lines 258–259, and Lemma 6 is below, not “above,” line 168. Name those references correctly. The referenced definitions and arguments are present, and they suffice for the unrestricted proof.

3. **Formalization description, line 323.** Saying that the Lean file covers the Taylor identity and positivity “only” understates its actual six algebra lemmas, correctly listed at line 336. It also covers denominator comparisons and a recurrence factor identity. I read the file and recorded build log; I did not rerun Lean or verify the build environment. None of these lemmas formalizes the stochastic argument. The mathematical verdict here rests on independent checking of that argument.

No substantive failed inequality, unlicensed infinite-sum exchange, hidden finite-moment assumption, independence assumption, or unjustified passage from one-time scaling to pathwise growth was found.

## Independent mathematical verification

### Source identities and kernel: lines 15–69, 174–195

I fetched the supplied PDF directly and checked Definition 9, Lemma 11, Definition 17, equation (4.2), and equation (5.3). They supply the critical equations, harmonicity, the h-transform perimeter law, the specified-side probability with its factor 1/2, and the partition-function integral, respectively. Here d(j)=4^(-j) binom(2j,j) and h(j)=2j d(j).

I independently derive the kernel as follows. Put a_k=q_k binom(2k-1,k-1) Z^(k-1). Criticality implies sum k a_k=1. For J(r)=Zr(1-f(Zr)), therefore

    J'(r)=Z sum_{m>=1} (m+1)a_(m+1)(1-r^m).

This is a nonnegative, uniformly convergent series on [0,1], because sum k a_k is finite. It is strictly positive for r<1. Thus J maps [0,1] increasingly onto [0,1], and the substitution g=J(r) in source (5.3) is legitimate without finite f'' or analytic continuation beyond Z. In particular, g Z_(q_g)=Zr is the smallest solution: no earlier solution can exist on the strictly increasing branch of y(1-f(y)).

Tonelli gives

    integral_0^1 r^(k-1)J'(r)dr
      = (Z/k) sum_{m>=1} m(m+1)a_(m+1)/(m+k).

Since (m+1)a_(m+1)=(2m+1)d(m)nu(m), multiplication by 2 d(k-1)/c, with c=4Z, gives exactly

    nu(-k)=d(k)/(2k-1) sum_{m>=1} m(2m+1)d(m)nu(m)/(m+k).

There is no factor-of-two or parity discrepancy. As an independent published cross-check, Budd arXiv:1506.01590v3, Lemma 4 on PDF page 16 and its bipartite simplification on page 17, give exactly the same kernel after doubling the half-perimeter indices. That lemma assumes criticality, not regular criticality. The k=1 case gives nu(-1)=1/(2Z)=2/c, as required.

Harmonicity at p=1 yields sum_{m>=0}nu(m)h(m+1)=1. Hence sum sqrt(m)nu(m)<infinity. It follows that T(p) is finite and strictly positive for every p, even when sum m^(3/2)nu(m) is infinite. The denominator comparisons at lines 62–63 are correct term by term. R(p)=T(p)/sqrt(p) is positive, decreasing and bounded above by R(1).

### All one-state bounds: lines 73–98

I checked (A)–(D) independently using d(k) comparable to k^(-1/2) and w_m comparable to m^(3/2)nu(m):

- For k>=p, T(k)<=T(p), so the negative tail is at most C T(p) sum_{k>=p}k^(-3/2)=C R(p).
- For k<=p, T(k)<=p T(p)/k. The truncated negative second moment is bounded by C p T(p) sum_{k<=p}k^(-1/2)/p^2=C R(p).
- For m<=p, m^2<=sqrt(p)m^(3/2) and sum_{m<=p}w_m<=2p T(p). This proves the positive second-moment bound.
- For m>p/2, m+p<3m, so w_m/(m+p)>=c sqrt(m)nu(m), proving (D).

The corresponding negative tail with cutoff p/2 and h(p+m)/h(p)<=C sqrt(m/p) prove (E), including arbitrarily large upward overshoots. No logarithmic moment is used. For (F), restricting k to [ceil(p/2),floor(3p/4)] gives a linear number of admissible terms, h(p-k-1)/h(p) bounded below, and nu(-k-1)>=c p^(-3/2)T(p). The resulting lower bound is c R(p), not a finite-f'' substitute. Small perimeters are legitimately removed by a fixed cutoff.

### Escape and the reciprocal-h cancellation: lines 102–145

Direct substitution in the h-transform gives

    E_p[1/h(P_1)]=(1-delta(p))/h(p).

Telescoping and monotone convergence imply finite expected total sum of delta(P_n)/h(P_n). Each finite state has strictly positive such cost because the exact kernel makes every nu(-k)>0. Each finite state is therefore visited finitely often almost surely. This proves P_n -> infinity without irreducibility or a finite first moment.

The exact recurrence h(j+1)/h(j)=1+1/(2j) proves the small-jump Lipschitz bound for U=log h and the uniform bound on L. Combining it with (B),(C) proves (G).

For H=h(P_1)/h(p), E_p[1/H]=1-delta(p) is finite, so the identity E_p[1-1/H]=delta(p) is valid as an absolutely integrable expectation. On the large-jump set, the absolute contribution is sum nu(y-p)|H-1|, bounded by the transformed and untransformed large-jump masses. Both are O(R(p)); monotonicity of h handles the positive untransformed mass. On the small-jump set, the bounded Taylor remainder between log H and 1-1/H is O((log H)^2). This proves |E_p L|<=C R(p), including cancellation between the two signs of jumps. Replacing this step by a bound on positive drift alone would not be justified, but the claimant does not do that.

### Localization and divergence: lines 149–164

The increments D_n are martingale differences for the actual exploration filtration; independent algorithmic randomness may be included in that filtration. The event {n<tau_K} is F_n-measurable because A_n=sum_{i<n}R(P_i). There is no anticipatory stopping.

At tau_K, the accumulated rate overshoots K by at most R(1). Thus the predictable stopped quadratic variation has expectation at most C(K+R(1)). Orthogonality gives an L^2-bounded stopped martingale and almost-sure convergence. The same localization bounds the expected count of large relative jumps by C(K+R(1)), making that count finite almost surely.

On the event of a finite total rate, some integer K exceeds that total. For that K the stopping time is infinite, the drift is absolutely summable, the martingale converges, and only finitely many actual log increments differ from their truncations. Consequently log h(P_n) has a finite limit. This contradicts the independently established P_n -> infinity. All exceptional sets can be combined over countably many integers K. The universal divergence conclusion follows.

### Boundary geometry, survival and exhaustion: lines 168, 258–285

The geometric argument agrees with the source's edge-peeling definition on PDF page 32. There are 2p boundary occurrences, and a surviving occurrence has distance at most p on one of the two sides of the selected occurrence. A finite gluing event with k>=ceil(p/2) removes enough consecutive occurrences to reach strictly beyond that target. The factor 1/2 is appropriate because a single specified side is chosen; the proof does not add incompatible side probabilities. Edge occurrences, rather than presumed distinct embedded edges or vertices, handle lazy-boundary identifications correctly.

For T the target's interiorization time, r_n=P(T=n+1|F_n) vanishes after T. On survival, its lower bound is b(P_n). The claimed supermartingale is valid since exp(r)(1-r)<=1 for 0<=r<=1. Bounded optional stopping at sigma_K capped by N gives the exp(-K) survival bound. There is no asserted converse and no independent-trial assumption.

Rate divergence and eventual escape imply divergent swallowing hazard on infinite survival. Each boundary occurrence therefore becomes interior in finite time almost surely. Introduction steps and positions provide a countable enumeration; random introduction times are handled by conditioning or discarding a finite prefix. A finite dual path to any allegedly missing face then gives a boundary occurrence that could never become interior, a contradiction. Interiorization of the exposed occurrences also supplies their edge identifications; finite face degrees leave no missing part of the map. This finishes the unrestricted claim.

### Auxiliary argument and example: lines 202–312

The auxiliary finite-f'' proof is not needed for the main theorem, but its steps also check out. J''(1-)=-2D implies I_j~2D/j^2 by the stated exponentially small interior contribution and endpoint comparison. The coefficient asymptotics give the positive 3/2 moment; the negative tail has a finite first moment. Oscillation and the strong law then give zero centering.

The characteristic-function domination and both endpoint estimates in the Riemann sum are valid. The limiting spectrally negative 3/2-stable law has positivity parameter 2/3. I fetched Caravenna–Chaumont arXiv:math/0602306 and checked Theorem 1.1 on PDF page 4, as well as the explicit strictly-positive variant using V(x-) on page 2. It supplies the conditioned entrance limit used here. Jeulin's eventwise expectation proof at lines 269–273 is valid without independence and makes no pathwise growth assertion.

For the zeta example, direct differentiation verifies both critical equations and f''(Z); concavity verifies the smallest root. The radius is exactly Z, so the example is indeed nonregular. Multiplication by k^3(k+j) verifies the partial-fraction identity at line 310. The paired harmonic terms telescope to H_j/j^3, giving the displayed I_j and its limit 2D. No new gap is hidden in this example.

## Independent computation and literature search

`independent_checks.py` was written independently in this audit folder and ran successfully. Its results are in `independent_checks.json`:

- Six finite critical laws, 78 transition rows, perimeters from 1 through 256: exact rational normalization, exact reciprocal-h identities and exact h recurrence all passed. There was no truncation of a negative tail in the normalization tests: only the negative jumps leading to positive states belong in these rows.
- 150 exact rational comparisons of the integral-derived negative kernel with the displayed kernel passed.
- Observed maximum ratios to R(p): negative tail 0.870, negative truncated second moment 0.527, positive truncated second moment 1.697, positive large-jump moment 1.925, transformed large-jump probability 3.176, absolute truncated log drift 0.522, and truncated log second moment 0.293. Minimum tested b(p)/R(p), for p>=8, was 0.03614. These are sample checks, not proposed universal constants.
- 171,671 finite boundary-distance/cutoff cases passed.
- Independent 65-digit quadrature at j=1,2,7,20,100 matched the zeta-example integral formula with maximum absolute discrepancy below 1.5e-65. The identity between its two expressions for 2D also passed.

All infinite-tail bounds and stochastic conclusions were checked analytically above. Finite experiments cannot prove those conclusions.

Fresh direct HTTP requests, with raw responses preserved locally, were made to arXiv and OpenAlex; no built-in web search was used. `fetch_log.json` records successful source, Budd and conditioned-walk PDF fetches and the arXiv search query. OpenAlex returned HTTP 429, which is a limitation rather than evidence of absence.

I screened the returned arXiv titles and abstracts, including 2505.05447 (Markov-property characterization), 2304.01167 (3/2-stable maps), 1910.09623 (stable-map subdiffusivity), 1909.10217 (simple peeling) and 1902.10624 (roundish explorations). I also fetched and inspected the full texts of 2505.05447 and 1909.10217. The former's stopping-map characterization is not an exhaustion theorem; the latter's arbitrary-critical construction concerns the half-plane with simple boundary. The stable/type-specific papers do not settle all critical sequences. Budd's exact kernel is an established general input, but the inspected result does not state the final general exhaustion theorem.

No earlier solution or known counterexample to this exact unrestricted assertion was verified in this bounded search. Publication priority and exhaustive absence of earlier work remain unproved. The mathematical result audited here is proved by the supplied written argument under the continuing, adapted, filled-in exploration convention; it is not classified as SOLVED_IN_LITERATURE or as a fully formalized probability theorem.
