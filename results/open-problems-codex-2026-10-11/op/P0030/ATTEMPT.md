# P0030 working mathematics, 2026-10-12

Source: Krzysztof Burdzy and Michael Scheutzow, Forward Brownian motion, arXiv:1302.6958v4 (29 March 2013), Problems 7.1–7.3, pp.25–26. Published DOI confirmed by Crossref: 10.1007/s00440-013-0524-x.

Exact source questions:

> Problem 7.1. Assume that X is a decomposable FBM which is also a BBM (we may or may not assume that the BBM is decomposable). Do these assumptions imply that X is 2BM?

> Problem 7.2. Assume that X is an FBM and BBM and there exists a random time T such that the processes X_{T+t} − X_T, t ≥ 0 and X_{T−t} − X_T, t ≥ 0 are independent. Do these assumptions imply that X is 2BM?

> Problem 7.3. Assume that X is an FBM and there exist random times S and T such that the processes X_{T+t} − X_T, t ≥ 0 and X_{T−t} − X_T, t ≥ 0 are independent and such that X_{S−t} − X_S, t ≥ 0 is Brownian motion. Do these assumptions imply that X is 2BM?

Mathematical notation in these quotes is transcribed from PDF typography. FBM has random starting times tending to minus infinity, each giving an unconditional standard Brownian future. BBM is the time reversal of an FBM. 2BM already permits a random centering time. Decomposable means, after a random shift, independent stopped Brownian pieces indexed by all integers, finite nonnegative durations whose sums diverge both ways; strong decomposability adds identical distributions. The stopping times may use normal filtrations larger than the natural Brownian filtration.

## Proof in progress

Stationary-increment special case: a continuous process X on the real line with stationary centered path law under every deterministic translation, and even one finite random S giving a Brownian future, has the centered 2BM(0) law. Plan: local bounded continuous cylinder observables have Brownian empirical averages along the positive trajectory; continuous-time averages avoid random lattice phases; stationarity identifies their expectation.

This extra stationarity is not a hypothesis of Problems 7.1–7.3. No answer to those questions is claimed.

## Theorem A (proved special case: stationary increments)

Let X be a continuous real-valued process indexed by R. Assume that for each deterministic a in R,

    (X(a+t)-X(a))_{t in R} has the same law as (X(t)-X(0))_{t in R}.

Assume also that there is an a.s. finite real random variable S for which B(u)=X(S+u)-X(S), u>=0, is a standard Brownian motion in its unconditional path law. Then (X(t)-X(0))_{t in R} has the standard two-sided Brownian law. In particular X is 2BM with centering time zero. Neither BBM nor decomposability nor independence at a random cut is needed under this additional stationarity assumption.

### Proof

Fix d>=1, t_1,...,t_d in R, and a bounded Borel real function f on R^d. Choose a deterministic M>=0 with |t_i|<=M for all i. Put K=sup |f| and let W have the standard two-sided Brownian law centered at zero. Define

    mu = E f(W(t_1),...,W(t_d)),
    g_X(r) = f(X(r+t_1)-X(r),...,X(r+t_d)-X(r)), r in R,
    g_B(u) = f(B(u+t_1)-B(u),...,B(u+t_d)-B(u)), u>=M.

All integrals below are Lebesgue integrals. Continuity of X and B gives joint measurability of these bounded integrands.

For every deterministic u>=M the vector (B(u+t_i)-B(u))_i has the law (W(t_i))_i. To verify this directly, increments to the right of u have Brownian law, while increments B(u-r)-B(u), 0<=r<=M, have Brownian law as a process in r by Gaussian independent increments and symmetry. The left and right increments depend on disjoint Brownian time intervals, so are independent. This establishes the claimed joint law, and E g_B(u)=mu.

For integers k>=0 put

    H_k = integral_{M+k}^{M+k+1} g_B(u) du.

This is a measurable function of the Brownian increment path on [k,k+2M+1]. Indeed, every time u+t_i and u occurring in the integral belongs to that interval, and every difference cancels the level B(k). Thus H_k is measurable with respect to sigma(B(v)-B(k): k<=v<=k+2M+1). Integrating a jointly measurable function yields the asserted measurability. It is bounded by K and Fubini gives E H_k=mu. The H_k all have the same law, since their defining increment paths on equal length intervals have the same Brownian law.

Choose an integer q>2M+1. For each residue j in {0,...,q-1}, the intervals [j+nq,j+nq+2M+1], n>=0, are pairwise disjoint. Their Brownian increment sigma fields are independent: independence holds first for finite collections of increments by the Brownian independent increment property, and extends to the path sigma fields using rational evaluation times and the monotone class theorem. Consequently (H_{j+nq})_{n>=0} is an i.i.d. bounded sequence with mean mu. The ordinary i.i.d. strong law gives

    (1/N) sum_{n=0}^{N-1} H_{j+nq} -> mu a.s.

Intersect these probability-one events over the finitely many residues. Splitting the first N terms H_0,...,H_{N-1} by residues, each residue has count either floor(N/q) or ceil(N/q), whose ratio to N tends to 1/q. The weighted average therefore converges to mu. Equivalently,

    (1/N) integral_M^{M+N} g_B(u) du -> mu a.s.

For real R->infinity the same conclusion holds: with N=floor R, the extra interval has length <1 and integrand bounded by K, while the change of denominator contributes at most K(R-N)/R. Thus the difference between the R-average and N-average is at most 2K/R (for N>=1).

The process B derived at S has precisely Brownian path law, so this path-functional probability-one assertion applies to it. It does not require any independence of B and S. Pathwise, g_X(S+u)=g_B(u) for u>=M. Set c=S+M, finite a.s. Then

    (1/R) integral_c^{c+R} g_X(r) dr -> mu a.s.

This is the preceding Brownian average after changing variables r=S+u. Since |g_X|<=K, for every finite c (positive or negative),

    |integral_0^R g_X(r) dr - integral_c^{c+R} g_X(r) dr| <= 2K|c|.

For overlapping intervals this follows by cancelling their common part; for disjoint intervals the bound 2KR is even smaller than 2K|c|. Divide by R. Hence

    (1/R) integral_0^R g_X(r) dr -> mu a.s.

Stationarity of the centered increment law gives E g_X(r)=E g_X(0) for every deterministic r. Boundedness and Fubini imply

    E[(1/R) integral_0^R g_X(r) dr] = E g_X(0).

Dominated convergence now gives E g_X(0)=mu. This holds for every d, every finite list of times, and every bounded Borel f; thus all finite-dimensional laws of X-X(0) equal those of W. Both have continuous paths, and rational evaluations generate the Borel sigma field of continuous paths with the topology of uniform convergence on compact sets. Their path laws are equal. In particular the two halves at zero are independent standard Brownian motions. QED.

## Corollary B (proved reduction to stationarization)

For any FBM X, the following are equivalent:

1. X is 2BM in Definition 2.1.
2. There is an a.s. finite random R such that Y(t)=X(R+t)-X(R) has stationary centered increment law under every deterministic time translation.

Proof. If X is 2BM, its defining centering shift produces standard two-sided Brownian law, which has stationary centered increment law by Brownian independent increments. Conversely, let R be such a stationarizing shift and let S be any Brownian future starting time for X (one exists by FBM). For A=S-R,

    Y(A+u)-Y(A)=X(S+u)-X(S), u>=0.

A is a.s. finite, and the right side is standard Brownian motion. Theorem A applies to Y. Therefore Y is centered two-sided Brownian motion, and R is a 2BM shift for X. QED.

## Proposition C (proved boundary case: path-independent random durations)

In Definition 2.2, suppose in addition that each T_k is independent of the entire Brownian path B^k. No identical distribution or moment assumption is needed. Then the concatenated X (with S_0=0) has 2BM(0) law.

Proof. The pairs (T_k,B^k stopped at T_k) are independent. Conditional on all durations, their stopped paths are independent Brownian paths on the now deterministic intervals [0,T_k]. This follows by the product disintegration of independent pairs, and independence of T_k from B^k makes each conditional kernel the ordinary stopped Brownian law. Fix a duration sequence with finite nonnegative entries and divergent sums in both directions. On any compact time interval only finitely many indexed pieces occur: both partial sums diverge, so indices intersecting that interval are bounded. Zero length pieces can be ignored. Split any finite list of disjoint increment intervals at the finitely many joining points. In every piece the resulting Brownian increments are independent centered Gaussians with the prescribed lengths as variances, and pieces are independent of one another. Summing gives independent centered Gaussian original increments with variances equal to original lengths. Increments on the negative half have the sign reversal appropriate to the backward parameter, which preserves the centered Gaussian law and independence. Continuity and X(0)=0 identify the 2BM(0) law conditional on the durations. This conditional law does not depend on the durations, so the unconditional law is the same. QED.

This is the observation of Remark 7.6 extended to independent nonidentically distributed path-independent durations. Infinite mean alone is therefore not an obstruction. Path-dependent stopping times are the unresolved regime.

## Hostile referee checks and precise gap

- Theorem A uses stationarity of the **joint centered increment law**, not merely stationary one-dimensional marginals. The proof needs E g_X(r)=E g_X(0) for all cylinder tests.
- No conditioning on S was used. Such conditioning could spoil Brownian law. All pathwise strong-law statements are made for the unconditional Brownian path B.
- A discrete average on integer times after a random S would have a random lattice phase. The continuous-time integral and its finite-shift bound avoid that unjustified step.
- H_k need not be independent for adjacent k. Only separated residue classes are independent; their Brownian intervals are disjoint because q>2M+1.
- The strongly decomposable finite-mean case is already Theorem 5.1 in the source. It is not a published answer to Problem 7.1 with arbitrary independent stopping pieces.
- Problem 7.1 supplies independence of forward and backward paths at a decomposition boundary, and a Brownian future there. Its BBM hypothesis supplies other backward starting times. It does not assert a Brownian past at that boundary, nor stationary increments there.
- Taking the minimum, maximum, or any future-dependent selection of Brownian starting times need not preserve Brownian marginals; source Remark 2.3 provides a counterexample to alignment by minimum/maximum. The earlier toy mean calculation is also valid.
- The older result's phrase 'finite Brownian bridge' was audited as incorrect. A pinned bridge U on [0,L] with U(L)=0 gives zero endpoint variance, unlike Brownian motion with variance L>0. Only an ordinary Brownian-motion middle segment is valid.
- Proposition C is conditioned only on path-independent durations. Conditioning on arbitrary stopping durations biases the stopped path and invalidates that proof.

Remaining gap: no construction of a finite random R with stationary centered increment law from any of the exact hypotheses of Problems 7.1–7.3. No counterexample satisfying decomposability plus BBM (7.1), or the additional independent cut of 7.2/7.3, has been constructed. All three questions remain unresolved in this attempt. Corollary B is a reformulation/reduction, not an affirmative answer.

## Finite checks (2026-10-12)

check_finite.py produced checks.json. It verified 400 interval-separation instances and 35 bounded-integral translation instances (including negative shifts and disjoint integration intervals). These are arithmetic sanity checks, not substitutes for the analytic proof.

A discrete obstruction was enumerated exactly through length 10: let a simple symmetric random walk stop at the first equal consecutive pair of increments. The stopped word has length n with probability 2^{-(n-1)}, n>=2 (there are exactly two words of each length). Thus E T=3. Every reversed stopped word starts with two equal increments, whereas an ordinary symmetric random walk has probability 1/2 of that event. Enumeration captured mass 1-2^{-9}=0.998046875 and the equality probability 1 exactly on that mass. Analytically the equality holds on the full stopped law by definition of T. This discrete model demonstrates why independently concatenated forward stopping pieces need not give a Brownian/random-walk past at their original boundary. It is not a counterexample to any source question, which permits a random shift. The source's Example 2.10 uses this stopping rule.

Lean verification file WindowSeparation.lean formalizes the supporting-interval separation inequality and normalization by a positive denominator. It does not formalize Brownian path laws, strong laws, stationarity, or Theorem A itself. The result of the compiler will be recorded separately in lean_check.txt.

Additional counterexample route examined: source Remark 7.6 suggests a strongly decomposable infinite-mean renewal clock which is identifiable from the unmarked, recentered path. Such a clock cannot be made stationary by a finite shift and would obstruct 2BM. To turn this into a counterexample to 7.1 one must ALSO prove BBM, with its sequence of backward Brownian starts tending to plus infinity. The source's identifiable-clock discussion does not provide that BBM property. For example, first hitting -1 pieces have infinite mean but drift to plus infinity backwards (Example 2.8) and fail BBM. Finite-mean identically distributed stopping rules are ruled out as counterexamples by Theorem 5.1. Thus neither a bare infinite-mean clock nor a locally biased reverse segment supplies the required counterexample; no candidate here passed all hypotheses.

For the discrete check's mean-length assertion: there are exactly two stopped words at each n>=2, each of probability 2^{-n}, so P(T=n)=2^{-(n-1)} and sum_{n>=2} P(T=n)=1. From sum_{n>=1} n/2^n=2 (differentiate the absolutely convergent geometric series), E T=2(sum_{n>=1} n/2^n-1/2)=3. The stopped word's terminal equal pair becomes the initial equal pair of its reversal. This verifies the analytic assertion on the full distribution, not just on the enumerated truncation.

## Theorem D (proved reduction: quantitative finite-window total variation)

Let X be any continuous real-valued process on R, and let S be an a.s. finite random time such that B(u)=X(S+u)-X(S), u>=0, has standard Brownian law. Fix M>=0 and R>0. Let U_R be uniform on [0,R], independent of (X,S), on an auxiliary product probability space if necessary. Let P_R^M be the law on C([-M,M]) of

    t -> X(U_R+t)-X(U_R),

and let W_M be standard centered two-sided Wiener law restricted to [-M,M]. With d_TV(P,Q)=sup_A |P(A)-Q(A)|,

    d_TV(P_R^M,W_M) <= E min(1, |S+M|/R) -> 0 as R -> infinity.

No moment bound on S, decomposability, BBM or stationarity is needed.

### Proof

Fix any Borel set A in C([-M,M]). Define the bounded measurable function

    g_X(r)=1_A((X(r+t)-X(r))_{|t|<=M}), r in R.

The shifted-window map is jointly measurable (in fact continuous as a map from a continuous sample path and its shift parameter to a finite window), so all integrals and Fubini uses are justified. Put

    g_B(u)=1_A((B(u+t)-B(u))_{|t|<=M}), u>=M.

For every deterministic u>=M the centered Brownian window has law W_M: its two half paths have Brownian law and independent increments on disjoint sides of u. Consequently E g_B(u)=W_M(A).

For every sample, set c=S+M. Then

    (1/R) integral_c^{c+R} g_X(r) dr
       = (1/R) integral_M^{M+R} g_B(u) du.

Its expectation is W_M(A), by Fubini applied at deterministic Brownian times u. This identity uses no conditional distribution given S.

For any measurable g with values in [0,1], any finite real c, and R>0,

    |integral_0^R g(r) dr - integral_c^{c+R} g(r) dr|
       <= min(R, |c|).

To prove the bound, cancel the intersection of the two intervals. Their respective differences have the same length ell=min(R,|c|). Both remaining integrals belong to [0,ell], so their difference has absolute value at most ell. This handles positive and negative shifts, overlapping and disjoint intervals.

Taking expectation of this pathwise inequality and dividing by R gives

    |P_R^M(A)-W_M(A)| <= E min(1, |S+M|/R),

because independence and uniformity of U_R identify P_R^M(A) with E[(1/R) integral_0^R g_X(r) dr]. The bound is independent of A, so take the supremum over Borel A. Finally |S+M| is finite a.s.; the bounded integrand min(1,|S+M|/R) tends to zero a.s. Dominated convergence proves the limit. QED.

### Short second proof of Theorem A

Under stationary centered increment law, P_R^M equals the unshifted centered window law for every R. Theorem D forces that window law to equal W_M exactly. Apply this for every positive integer M, and use continuity/rational evaluation generation of the full path sigma field. This proves Theorem A without a strong law. The longer independent-residue proof above remains valid and has separately checked supporting inequalities.

### Why this still does not solve the original problem

Theorem D applies even to Example 2.8, which is not BBM and not 2BM. Thus local total-variation convergence along uniform shifts escaping to plus infinity does not supply a finite random centering time. The random variables U_R are not tight: for every fixed K>=0, P(U_R<=K)=min(1,K/R)->0. No limit random time can be extracted from this family by a tightness argument. A different, tight construction of finite centers would be needed. The additional BBM or independent-cut hypotheses have not yet supplied one.

A further obstruction to transplanting source Theorem 5.1: in the i.i.d. case the conditional stopped-path kernel Q_t given a duration t is the same at every piece index. Stationarizing the renewal times can therefore stationarize the marked Brownian pieces, as the source proof makes explicit on pp.18–19. With independent nonidentically distributed stopping rules, the kernels Q_{k,t} can depend on k. Stationarizing the unmarked clock alone would not establish stationary centered path law. Conversely, a nonstationarizable clock is an obstruction to stationary path law only if the clock is measurably identifiable from the centered path. Neither common conditional kernels nor that identifiability is assumed in Problem 7.1. This is why the renewal proof cannot simply be extended by changing its moment hypothesis.

Final verification (2026-10-12): Lean compiler exited 0 for WindowSeparation.lean after adding the explicit Mathlib.Data.Real.Basic import and removing the BOM. Both supporting inequalities were kernel checked; no sorry, axiom, or native_decide occurs. Earlier failed compiler outputs are retained as lean_check_first_failed.txt and lean_check_second_failed.txt. The full probability theorems are proved on paper, not formalized in Lean. The sharpened [0,1]-valued translation bound in Theorem D also passed 54 deterministic checks.


# Second attempt, 2026-10-12

The remaining gap is to produce an exact finite stationarizing shift, rather than finite-window limits with centers escaping to infinity. Two approaches not pursued in the first attempt:

1. **Orbit laws and shift coupling.** On two-sided continuous paths, integer recentering is an invertible ergodic transformation of Wiener measure. Thorisson's invariant-sigma-field criterion may convert full-path absolute continuity (or equality on invariant events) into an exact finite random shift. Test whether the independent cut plus FBM/BBM forces those invariant-event laws, and prove any valid full-law domination special case. The earlier proof used local total variation only, which does not give this full-path condition.
2. **Kakutani equivalence of independent stopped-piece laws.** Compare nonidentically distributed stopped pieces with a common finite-mean stopping law, whose concatenation is 2BM by source Theorem 5.1. Summable Hellinger discrepancies may make the entire product law absolutely continuous. Transport the reference stationarizing kernel, then use orbit-law shift coupling to remove the resulting Wiener tilt. This could extend Theorem 5.1 to genuinely path-dependent, nonidentically distributed stopping rules. Alternatively, divergence of the Hellinger sum may identify where a counterexample must lie, though singular marked laws alone are not a counterexample for unmarked paths.

Initial choice: pursue approach 2, supported by a fully proved orbit-law/filling lemma from approach 1. No claim yet that the source hypotheses imply any absolute continuity condition.


## Lemma E (proved: forward filling from a dominated law to the invariant law)

Let (E,P) be a standard Borel probability space and theta an invertible measurable P-preserving ergodic transformation with measurable inverse. Let Q=fP be any probability measure, where f>=0 and integral f dP=1. For Z with law Q, on an extension carrying an auxiliary uniform random variable there is an a.s. finite nonnegative integer N such that theta^N Z has law P. N may depend on the entire state Z and is not asserted to be a stopping time. Neither equivalence Q~P nor a finite mean for N is asserted or needed.

### Full proof

Choose measurable versions of all densities. Let a_0=f, b_0=1. Recursively define

    h_n = min(a_n,b_n),
    a_{n+1} = (a_n-h_n) composed with theta^{-1},
    b_{n+1} = b_n-h_n.

Every density is nonnegative and integrable. The measures h_n P are the mass accepted at step n, expressed at its destination. Preservation of P gives

    integral a_{n+1} dP = integral a_n dP - integral h_n dP,
    integral b_{n+1} dP = integral b_n dP - integral h_n dP.

Thus integral a_n = integral b_n for all n. The b_n decrease pointwise to b_infty, with 0<=b_n<=1.

Pull remaining source mass back to its original location: s_n(x)=a_n(theta^n x). The recursion gives

    s_{n+1}(x)=s_n(x)-h_n(theta^n x).

Therefore 0<=s_n<=f, s_n decreases to s_infty, and

    sum_{n>=0} h_n(theta^n x)=f(x)-s_infty(x).

These identities hold simultaneously off a P-null set, which can be enlarged by its countably many theta-translates so that every required orbit evaluation is valid. Dominated convergence, using f for s_n and 1 for b_n, and preservation of P show

    integral s_infty dP = integral b_infty dP.

Suppose b_infty is not zero P-a.e. Choose epsilon>0 with P(D)>0 for D={b_infty>=epsilon}. By the pointwise ergodic theorem for 1_D, for P-a.e. x the orbit theta^n x visits D infinitely often (indeed with limiting frequency P(D)>0). At any such x with s_infty(x)>0,

    h_n(theta^n x)
       = min(a_n(theta^n x),b_n(theta^n x))
       >= min(s_infty(x),epsilon) * 1_D(theta^n x).

The right side sums to infinity over n, whereas the preceding telescoping identity bounds the sum of the left side by the finite number f(x). Contradiction. Hence s_infty=0 P-a.e., which implies integral b_infty=0 and contradicts the supposition. We conclude that b_infty=s_infty=0 P-a.e.

For x with f(x)>0 define

    p_n(x)=h_n(theta^n x)/f(x).

These are nonnegative measurable functions summing to one for Q-a.e. x. At the irrelevant remaining x assign p_0=1 and p_n=0 for n>0. With an independent U uniform on [0,1), set N to the first n with U < sum_{j=0}^n p_j(Z). This is measurable and finite a.s. For every measurable A,

    P_Q(theta^N Z in A)
       = sum_n integral 1_A(theta^n x) p_n(x) f(x) P(dx)
       = sum_n integral_A h_n(y) P(dy)
       = integral_A (1-b_infty(y)) P(dy)
       = P(A).

Tonelli justifies the nonnegative sum and change of variables uses P preservation. This proves the lemma. QED.

The lemma is a classical filling/shift-coupling mechanism, with a new application here rather than a claim of a new ergodic-theory theorem. The brain's recalled lemma had the opposite source/target direction; that recalled statement was not used as a proof of this one.

## Corollary F (proved: full-law absolute continuity is sufficient)

Let W be centered two-sided Wiener law on C_0(R), and theta w(t)=w(t+1)-w(1). If a centered continuous process has full path law Q<<W, then on a probability-space extension it becomes standard two-sided Brownian motion after an a.s. finite nonnegative integer shift.

Proof of the required ergodicity. Under W, the unit increment paths w(k+u)-w(k), 0<=u<=1, k in Z, are independent and identically distributed standard Wiener segments. They determine w uniquely, including negative times, and theta shifts their indices. This is the bilateral i.i.d. shift. To verify ergodicity explicitly, let A be invariant and approximate A in probability by a finite-coordinate cylinder C with P(A symmetric_difference C)<delta; such approximations exist because finite-coordinate cylinders generate the product sigma field. For a sufficiently large integer m, C and theta^{-m} C use disjoint coordinates, hence are independent. Invariance of A yields

    |P(A)-P(A)^2|
       <= |P(A intersection theta^{-m} A)-P(C intersection theta^{-m} C)|
          + |P(C)^2-P(A)^2|
       <= 2 delta + 2 delta = 4 delta.

Let delta tend to zero. Thus P(A) is 0 or 1. The map theta and its inverse are measurable and preserve W. Lemma E applies and gives the required exact shift. QED.

A more general stability statement follows. If a continuous centered path law mu is absolutely continuous with respect to a path law nu that already admits a finite random shift to W, then mu also admits such a shift on an extension. Indeed, take a joint law of (x,R) witnessing nu's shift to W and disintegrate R given x, obtaining a probability kernel K(x,dR). The joint law mu(dx)K(x,dR) is absolutely continuous with respect to nu(dx)K(x,dR): a joint null set has K-section measure zero nu-a.e., hence mu-a.e. Its shifted-path image has law lambda<<W. Apply Corollary F to that image, with integer shift N. The combined real shift R+N is finite and gives W exactly. The cocycle identity theta_N(theta_R x)=theta_{R+N}x verifies that this is a shift of the original path, not a change to the trajectory.

Scope convention: these statements explicitly allow auxiliary randomness on an extension. They do not claim that the integer shift is a deterministic function of the canonical path. The source uses distributional random-shift constructions; regardless of its underlying-space convention, no inference to the full Problems 7.1–7.3 is made from this added absolute-continuity condition.

## Lemma G (proved: one-way Kakutani product domination)

Let P_0 be a probability law on a standard Borel space E, and let Q_j=f_j P_0, j>=1, be probability laws. Define rho_j=integral sqrt(f_j) dP_0. If sum_j (1-rho_j)<infinity, then product_j Q_j << product_j P_0.

### Full proof

By Cauchy-Schwarz, 0<rho_j<=1. Positivity follows because f_j>=0 integrates to 1. Work on the reference product P. Put F_n=product_{j=1}^n f_j(x_j), and H_n=sqrt(F_n). Independence gives integral H_n^2 dP=1. For m>n,

    integral H_n H_m dP = product_{j=n+1}^m rho_j,
    ||H_m-H_n||_2^2 = 2(1-product_{j=n+1}^m rho_j)
                       <= 2 sum_{j=n+1}^m (1-rho_j).

The finite product inequality follows by induction from 1-ab=(1-a)+a(1-b)<= (1-a)+(1-b) when a,b in [0,1]. The summability hypothesis makes H_n Cauchy in L^2. Let H be its L^2 limit. Passing to an a.e. convergent subsequence ensures H>=0. Norm continuity gives ||H||_2=1. By Cauchy-Schwarz,

    ||F_n-H^2||_1
       <= ||H_n-H||_2 (||H_n||_2+||H||_2)
       = 2 ||H_n-H||_2 -> 0.

Thus F=H^2 is a probability density with respect to P. For any event C depending on the first r coordinates, for n>=r independence gives

    integral_C F_n dP = (product_{j=1}^r Q_j)(C).

L^1 convergence gives the same identity with F in place of F_n. Consequently FP and product_j Q_j agree on every finite-coordinate cylinder; the pi-lambda theorem makes them equal on the product sigma field. Hence product Q_j=FP<<P. QED.

This is the sufficient one-way direction of Kakutani's product-measure result, proved here without assuming every coordinate law is equivalent. We need domination, not reverse domination.

## Theorem H (proved special case: summably perturbed stopped-piece laws)

Let P_0 be the law of a Brownian stopped piece (T,B stopped at T) with 0<E_{P_0} T<infinity and an a.s. finite nonnegative stopping time for a normal filtration. Let the actual decomposable process be constructed from independent stopped Brownian pieces with laws Q_k, k in Z. Assume

    Q_k << P_0 for every k,
    sum_{k in Z} [1-integral sqrt(dQ_k/dP_0) dP_0] < infinity.

Then, in the distributional sense allowing a probability-space extension, the actual process is 2BM after a finite random shift. BBM need not be separately assumed. The Q_k need not be identical, and their stopping rules may depend on their Brownian paths.

### Full proof

Represent a stopped piece as (T,b), with b(t)=B(t min T), in [0,infinity) times C_0([0,infinity)); the consistency condition b(t)=b(T) for t>=T is Borel, so this is a standard Borel piece space. Enumerate Z by 0,1,-1,2,-2,... and apply Lemma G. The actual product of piece laws Q is absolutely continuous with respect to the i.i.d. reference product P=product_{k in Z} P_0.

Under P, the durations sum to infinity in both directions a.s. For example choose epsilon>0 with P_0(T>=epsilon)>0, which exists because E T>0. In each direction independent trials give infinitely many such durations by the second Borel-Cantelli lemma. This a.s. event also holds under Q by domination. Thus both concatenations are defined on all of R. The concatenation map Phi from the piece sequence to a centered continuous path is measurable: joining times are finite sums of coordinate durations; at any fixed rational time a countable Borel partition selects its containing index, and evaluation of that coordinate's continuous path at the corresponding measurable offset is measurable. Continuity and rational evaluations then give path-valued measurability. On the null set of nondivergent clocks choose an arbitrary fixed continuous path.

The reference process is strongly decomposable and has finite mean durations; source Theorem 5.1 (pp.18–19) gives a joint law of reference pieces and a finite real shift R_0 such that theta_{R_0} Phi has law W. Disintegrate the shift given the entire reference piece sequence to obtain a kernel K. Put the same kernel on the actual product Q. The resulting joint actual law is absolutely continuous with respect to the joint reference law, as proved in Corollary F. Hence the actual shifted path Y=theta_{R_0} Phi has some law lambda<<W. Corollary F gives a further finite nonnegative integer shift N with theta_N Y law W. Therefore R_0+N is a finite centering time of the original concatenated path and witnesses 2BM. If the original decomposition itself required a shift U, add U to this combined shift. QED.

Only source Theorem 5.1 is imported in this proof; all product-domination and tilt-correction steps are proved above. No claim of originality is made for combining these classical tools.


## Example I (proved: nonidentical path-dependent bounded stopping rules)

For every k in Z take independent standard Brownian motions B^k and independent uniforms V_k. Let epsilon_k=1/[8(1+|k|)], and

    p_k(z)=1/2+epsilon_k tanh(z),
    T_k=1 if V_k<=p_k(B^k(1)), and T_k=2 otherwise.

Use the normal filtration generated by B^k up to time t and V_k at time zero, with usual augmentation. B^k remains Brownian because V_k is independent. T_k is a stopping time: before 1 its stopped event is empty, between 1 and 2 it is the F_1-measurable event above, and at 2 it is certain. The stopped pairs are independent across k. All durations lie in {1,2}, so both clock sums diverge.

Let P_0 be the law of a stopped Brownian path with a duration chosen independently from {1,2}, each with probability 1/2. Its mean duration is 3/2. Relative to P_0, the actual stopped-piece density is

    f_k(T,b)=1+2 epsilon_k tanh(b(1)) when T=1,
              1-2 epsilon_k tanh(b(1)) when T=2.

To verify the density, integrate any bounded measurable test of a stopped piece conditional on B^k: stopping at 1 has conditional probability p_k(B^k(1)), while continuing to 2 has probability 1-p_k(B^k(1)). Dividing those weights by the corresponding reference weight 1/2 gives exactly f_k. The value b(1) is observed in the stopped path for both durations. Thus this is domination of the full stopped-pair law, not only the clock law. In fact f_k is strictly positive and bounded, because |2 epsilon_k tanh|<=1/4.

Since integral f_k dP_0=1,

    1-rho_k = (1/2) integral (sqrt(f_k)-1)^2 dP_0
             = (1/2) integral (f_k-1)^2/(sqrt(f_k)+1)^2 dP_0
             <= (1/2) integral (f_k-1)^2 dP_0
             <= 2 epsilon_k^2.

The sum of epsilon_k^2 over Z is finite: it is 1/64 times [1+2 sum_{j>=1}(1+j)^{-2}], and the p-series converges (or use the integral test). Theorem H applies. Since this particular reference concatenation has 2BM(0) law by Proposition C, the preliminary reference shift can be zero: Corollary F directly produces a finite nonnegative integer centering shift for the actual path.

The centered actual path at its original joining time is NOT 2BM(0). Take the final negative-index piece, k=-1. For its T in {1,2}, the backward increment of length 1 is

    X(-1)-X(0)=B(T-1)-B(T).

With Z=B(1) and D=B(2)-B(1), the independent centered normal variables Z,D are also independent of V. Consequently

    E[X(-1)-X(0)]
       = -E[Z p_{-1}(Z)] - E[D(1-p_{-1}(Z))]
       = -epsilon_{-1} E[Z tanh Z] < 0.

The first equality follows by conditioning on (Z,D), and the second uses E Z=0 and independence/centering of D. Strict positivity of E[Z tanh Z] follows because its integrand is positive for Z!=0 and is bounded by |Z|, which is integrable. Hence the original backward increment is not a centered normal increment. These bounded, genuinely path-dependent stopping rules are not covered by Proposition C, and their laws are not identical, so source Theorem 5.1 is not applied directly to them. Nevertheless the product-domination argument proves exact 2BM after a finite shift. QED.

## Referee objection resolved: the summability condition is additional

BBM does not force summable Hellinger discrepancies for a given decomposition. Consider independent ordinary Brownian pieces with deterministic durations alternating 1 and 2 in both directions. Proposition C makes the concatenated unmarked process 2BM(0), hence BBM, although its two alternating stopped-pair laws Q^(1),Q^(2) have disjoint duration supports.

For any putative common reference P_0 dominating both laws, write a_i=P_0(T=i), i=1,2. By Cauchy-Schwarz on the duration-i support,

    rho_i=integral sqrt(dQ^(i)/dP_0) dP_0 <= sqrt(a_i).

Since a_1+a_2<=1, they cannot both equal 1. At least one rho_i is strictly below 1 and its deficiency occurs infinitely many times, so the Hellinger sum diverges. Thus even an already two-sided Brownian path need not satisfy Theorem H's hypothesis in its presented marking. A different decomposition of the same path might satisfy it; existence of such a representation has not been proved for arbitrary decomposable FBM+BBM.

This also blocks an invalid counterexample strategy: singularity or Hellinger divergence of the marked product laws does not imply non-2BM of the unmarked path. The concatenation/forgetful map can erase the distinction entirely.


## Theorem J (proved stronger special case: only negative pieces need domination)

In Theorem H the summable Hellinger condition can be imposed only on k<0. All nonnegative-index pieces may follow arbitrary independent Brownian stopping rules allowed by Definition 2.2, subject to the assumed divergence of their total durations. More generally it suffices that the joint law of all negative stopped pieces is absolutely continuous with respect to the negative half of an i.i.d. finite-mean stopped-piece reference law P_0.

### Full proof

Work at the decomposition boundary S_0=0. The negative-time path is a measurable function solely of the stopped pairs indexed k<0. The nonnegative-time path is a measurable function solely of the stopped pairs indexed k>=0. Those two sigma fields are independent under Definition 2.2. The latter path has standard Brownian law, independently of the choice of nonnegative stopping rules. Here is the Brownian-law verification behind this fact: replacing a Brownian post-stopping-time continuation by an independent standard Brownian continuation preserves its law by the strong Markov property for the given normal filtration. Apply this successively for any finite number of independent stopped pieces, appending a Brownian continuation after the last piece. The resulting entire one-sided path has Brownian law and agrees with the desired concatenation until the corresponding joining time. As the number of pieces tends to infinity those joining times tend to infinity a.s.; on every compact time interval the constructed path therefore eventually agrees with the actual concatenation. Finite-dimensional distributions (or bounded continuous compact-window functionals) give the Brownian law of the limit. This is also the assertion immediately after Definition 2.2 in the source.

Let Q^- be the actual product law of negative pieces and P^- the negative product of P_0. By hypothesis Q^-<<P^-; under the summable negative-index Hellinger condition this follows from Lemma G with enumeration -1,-2,... . Let W_+ be one-sided Wiener law. Then

    Q^- times W_+ << P^- times W_+.

To check this domination, if a joint measurable set has zero P^- times W_+ mass, its W_+-section measure is zero P^--a.e. by Fubini, hence zero Q^--a.e.; another Fubini application gives zero actual mass. Map each pair of a negative piece sequence and a Brownian future to the full centered path by concatenating the negative pieces backwards from zero and using that future on t>=0. This map is measurable by the same evaluation argument in Theorem H. Its reference image has exactly the unmarked path law of the fully i.i.d. P_0 concatenation: the latter has this reference past and an independent standard Brownian future. Its actual image has the law of the given decomposable process. Thus the actual unmarked path law is absolutely continuous with respect to the reference unmarked path law.

The reference law admits a finite shift to W by source Theorem 5.1. The absolute-continuity stability result in Corollary F now gives a finite shift to W for the actual law, on an extension. QED.

This is stronger than Theorem H: summability or identical distribution of the positive pieces is irrelevant to the unmarked path law. The argument still adds a genuine condition on the infinite negative sequence. BBM alone has not been shown to imply that condition.

## Second-attempt hostile referee ledger

1. **Transport direction:** Lemma E starts with Q=fP and targets P. Its probability weights pull accepted destination mass back by theta^n, then divide by f; reversing that direction without changing weights would be wrong. Both the source-row sums and destination-column sums were checked exactly in finite models.
2. **Why mass is exhausted:** residual source and target have equal integrals, and the source can only decrease along its orbit. If residual target has positive mass, ergodicity forces every surviving source orbit to encounter it infinitely often, contradicting finite original source density. The residual identity is essential; recurrence alone without mass conservation is insufficient.
3. **Where auxiliary randomness enters:** the measurable kernel p_n(x) is sampled with an independent uniform. No deterministic-path integer shift is claimed. Arbitrary f cannot in general be implemented by a deterministic integer selection; this is a stated scope restriction of E/F/H/J, not hidden in the proof.
4. **Full product law versus local laws:** Lemma G obtains an L^1 probability density with total mass one. Mere finite-dimensional domination without Hellinger summability would not suffice. The first attempt's local total-variation limit is not substituted for this density.
5. **Correct comparison space:** the affinities compare (T,entire stopped Brownian path), not durations alone. Example I computes that density explicitly, including both the stop and continue decisions.
6. **Reference random shift:** it is sampled by disintegration on the entire piece sequence. Domination passes to that joint law and then to shifted paths. It is not assumed independent of the stopped pieces or unchanged in law after a tilt. Corollary F corrects precisely that remaining tilt.
7. **Actual stopping rule:** Example I retains an unconditioned Brownian motion and changes only the decision at time 1 using an independent uniform and B(1). Its T is a genuine stopping time in a normal filtration. Tilting an arbitrary stopped pair and assuming the tilted B is Brownian would not be justified; the example avoids that error by construction.
8. **Unmarked versus marked singularity:** the alternating deterministic-duration example disproves the attempted deduction that BBM forces a finite Hellinger sum for the supplied decomposition. Singularity of clocks does not by itself obstruct unmarked 2BM.
9. **No full-source inference:** the full problems allow arbitrary independent stopped pieces, potentially no common dominating reference, and arbitrary independent cut laws. Neither negative product domination nor equality on all invariant events has been derived from these hypotheses.

Updated precise remaining gap: for an arbitrary decomposable FBM which is BBM, show that its unmarked law agrees with Wiener law on shift-invariant events (possibly after a preliminary shift), or find a shift-invariant null event distinguishing it. Product domination provides one sufficient route, but fails for some harmless markings and is not a necessary condition on the given decomposition. For 7.2/7.3, independence of the two selected halves has not been shown to determine those full-path invariant-event probabilities. All full questions remain unresolved here.


## Example L (proved special case: one infinite-mean hitting piece)

The domination result also permits an actual infinite-mean stopping law; finite mean is required for the reference, not for every actual piece. Let B be standard Brownian motion, tau=inf{t>=0:B(t)=-1}, and E an independent exponential time of rate 1, revealed at time zero in the stopping filtration. Let P_0 be the stopped-pair law for T_0=min(tau,E). Then 0<E T_0<=1, and the normal filtration with E added leaves B Brownian. T_0 is a stopping time.

Let Q be the untruncated first-hitting stopped-pair law for tau. On the reference stopped-pair space its density is

    f(t,b)=exp(t) * 1_{b(t)=-1}.

Indeed, the reference endpoint equals -1 exactly when tau<=E, up to a null tie. For every nonnegative measurable g,

    E_{P_0}[f(T_0,b)g(T_0,b)]
       = E_B[exp(tau)g(tau,B stopped at tau)P(E>=tau | B)]
       = E_B[g(tau,B stopped at tau)] = E_Q g.

This proves full stopped-pair domination, with integral f dP_0=1. Its affinity is

    rho=E_{P_0} sqrt(f)=E_B exp(-tau/2)=exp(-1)>0.

For completeness the hitting-time Laplace identity follows from the exponential martingale exp(-aB(t)-a^2 t/2), a=sqrt(2 lambda), stopped at t min tau. Before hitting -1 this stopped martingale is bounded by exp(a), so bounded optional stopping gives expectation 1 and dominated convergence gives exp(a)E exp(-lambda tau)=1. Finiteness of tau a.s. follows from reflection: P(tau>t)=2 Phi(1/sqrt(t))-1 tends to zero. That same reflection formula has tail asymptotic sqrt(2/pi)/sqrt(t), making E tau=infinity by integration of the tail.

Take independent reference pieces P_0 at all indices except k=-1, where use Q. The Hellinger sum has just the finite nonzero term 1-exp(-1). Theorem H (or J) therefore proves a finite random shift to two-sided Wiener law on an extension, although the actual k=-1 duration has infinite mean. The reference clock sums diverge a.s. and product domination transfers this event to the actual system; directly, all the infinitely many remaining i.i.d. positive-duration pieces also suffice.

At the original boundary zero, on every sample the final negative piece stays strictly above its endpoint before tau, hence X(-s)>X(0) for all 0<s<tau. Standard Brownian motion started at zero has probability zero of remaining nonnegative on a whole positive interval: reflection gives P(min_{0<=s<=h}B(s)>=0)=0 for every h>0, and a countable union over rational h treats a random positive interval. Thus the original backward half is not Brownian at zero. This is another example where correcting the random center is necessary. It is an affirmative nonidentical stopped-piece special case, not a counterexample to 7.1. QED.

## Periodic finite-mean control (proved special case used in the probe)

If stopped-piece laws repeat with a finite period p and the sum of their mean durations over one period is finite and positive, group consecutive p pieces starting at indices mp, m in Z. A group is a stopped Brownian piece by finite strong-Markov concatenation; its endpoint time is a stopping time in the concatenated filtration, since successive component stopping decisions are adapted until the end of each component. The grouped stopped pairs are independent and identically distributed, and their mean duration is the finite positive sum over a period. Source Theorem 5.1 applies to the grouped decomposition. Thus periodic finite-mean decompositions are 2BM after a shift. This justifies the alternating-rule positive control below; it does not extend to arbitrary nonperiodic laws.

## Supplementary bounded-rule likelihood probe

For the duration-1-or-2 model, write epsilon_j for the parameter of the negative piece at index -(j+1), p_j(z)=1/2+epsilon_j tanh z. Let F_{j,n}(y_1,...,y_n) be the density of its first n backward unit increments, including subsequent pieces, relative to n independent standard normals. Conditioning on whether the current piece has length 1 or 2 gives the exact finite recurrence

    F_{j,0}=1,
    F_{j,1}(y)=p_j(-y)+1/2,
    F_{j,n}(y)=p_j(-y_1)F_{j+1,n-1}(y_2,...,y_n)
               +[1-p_j(-y_2)]F_{j+1,n-2}(y_3,...,y_n), n>=2.

For length 1 the observed increment is -B(1), weighted by its stop probability. For length 2 the first observed increment is -(B(2)-B(1)) and the second -B(1), weighted by the continue probability evaluated at the second one. These two normal increments and the remaining pieces are independent before that weight. For n=1, integrating the unobserved B(1) in the length-2 branch gives E[1-p_j(B(1))]=1/2 by oddness of tanh. This proves the recurrence, not only its numerical implementation.

second_likelihood_probe.py computes that recurrence by dynamic programming and estimates its first two reference moments with 500 normal samples at n=16,64,128. Controls are constant epsilon=0.24 (source Theorem 5.1), alternating +/-0.24 (periodic grouping above), and epsilon_j=0.125/(j+1) (Theorem J). The unproved test is epsilon_j=0.24*(-1)^{floor(log2(j+1))}, which has growing blocks of opposite signs and fails the simple common-reference Hellinger summability condition.

The unproved test's estimated second moments at 16,64,128 were respectively 1.1222,1.1088,1.1395; estimated means stayed within 0.008 of 1. No density-collapse or counterexample signal appeared in this bounded run. These estimates do not prove uniform integrability, full Brownian-path domination, BBM, or a finite exact shift. Even a proven assertion for these integer increments would need the conditional intra-unit path laws to yield full continuous-path domination. The remaining original gap is unchanged.

Second-attempt verification: second_checks.json records 140 exact rational finite-cycle filling cases, the nonergodic residual 1/2, four product-overlap enumerations with maximum error 4.4408920985e-16, four Hellinger-affinity quadratures, and the 200000-sample original-boundary mean check. second_lean_check.txt records compiler exit 0 for HellingerFilling.lean, with narrow imports, no sorry and no native_decide. The infinite-dimensional product and Brownian proofs remain paper proofs, not Lean formalizations.

Technical clarification for Theorem J: Definition 2.2 asserts independence of stopped pairs, not necessarily of their originally supplied full Brownian continuations. For the strong-Markov gluing proof one may realize independent copies of each full Brownian/stopping-time/filtration system on their product space; their stopped-pair joint law is the same independent product as originally supplied. This proves the concatenated path law without assuming independence of unused continuations in the original realization.


## Reduction M (proved using Thorisson's shift-coupling theorem)

Let mu be any centered continuous real-path law, and W centered two-sided Wiener law. Let I_R be the Borel sets A of C_0(R) such that theta_t^{-1}A=A for every real t, where theta_t x(s)=x(t+s)-x(t). In the distributional sense allowing an extension, mu admits a finite real random shift to W if and only if

    mu(A)=0 for every A in I_R with W(A)=0.

Necessity is elementary: for a pathwise finite shift R and invariant A, 1_A(theta_R x)=1_A(x), so the probabilities of every invariant event are unchanged by the random shift.

For sufficiency first observe that W is ergodic under the real recentering group: any real-invariant event is in particular invariant under the integer shift, whose ergodicity was proved in Corollary F. Thus W(A) is 0 or 1 for A in I_R. The null-set condition, applied also to complements, implies that mu and W agree on I_R.

To apply the cited ordinary-time shift-coupling criterion to a recentering action, encode a centered path x as the continuous E-valued trajectory Z_x(t)=theta_t x, with E=C_0(R). The map (t,x)->theta_t x is continuous for the compact-open topologies, so x->Z_x is measurable into C(R,E). Its image O consists exactly of trajectories Z satisfying Z(t)=theta_t Z(0) for every t. The equalities at rational t suffice by continuity, so O is Borel; O is invariant under ordinary translation of the parameter t. The encoding is one-to-one with measurable inverse Z->Z(0), and obeys Z_{theta_s x}(t)=Z_x(t+s).

An invariant Borel event H of these E-valued trajectories pulls back to an event in I_R. Conversely, for A in I_R the event O intersection {Z:Z(0) in A} is Borel and invariant under ordinary time translation, with pullback A. Hence the two encoded process laws agree on their invariant sigma field. Thorisson's continuous-path shift-coupling criterion, reproduced as Pitman–Tang Theorem 5.9 on p.19, gives a finite random ordinary time shift of Z_mu with law Z_W. Evaluating at time zero gives theta_R x with law W. This proves sufficiency. QED.

This is a genuine full-path reformulation of the remaining gap, not a solution: the source assumptions have not been proved to exclude every Wiener-null real-shift-invariant event. Replacing I_R by the larger integer-invariant sigma field would add a stronger condition and is not justified for a question permitting arbitrary real shifts. The filling lemma's integer correction is used only after full domination by W has been obtained.


Second-attempt closing verdict (2026-10-12): PARTIAL. Both new approaches were recorded and the product-domination approach was carried through to exact finite shifts in additional special cases, with explicit auxiliary-randomness scope. The general compatibility questions are still unresolved. The next mathematical step would be to prove equality on the real-shift-invariant sigma field using only the independent cut plus Brownian certifications, or exhibit an invariant-null-event obstruction satisfying those hypotheses. A finite-window limit, marked-product singularity, or a failed integer-shift condition is insufficient.
