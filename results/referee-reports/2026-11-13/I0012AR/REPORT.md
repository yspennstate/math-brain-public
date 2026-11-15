MINOR

The claimed critical-exponent theorem is correct. The last-backbone-collision transport is valid, including the squared degree weight and the quenched conclusion. I found no hidden use of gamma > 1/3 in the geometry needed for the backbone heat-kernel lower bound. However, the submitted report overstates how cleanly the printed proof of Lemma 4.9 can be used: its dependency chain contains incorrect statements and omitted qualifications. These should be acknowledged and repaired. Below I supply an independent proof of exactly the lower bound needed for (A), so the verdict does not rest on overlooking those defects.

The result appears to be a new application of an existing method, rather than a new mass-transport principle. I found no published resolution of this endpoint, but the literature search cannot certify priority.

1. Errors, gaps, and fixes

1. **Submitted REPORT, “Checks and limitations”: the source audit is too categorical.** The required exponent range is right, but saying the dependency proofs check without qualification misses the defects below. Fix: distinguish the finite-scale lower bound actually needed from the stronger, incorrectly printed statement of Lemma 4.8. Include the independent finite-scale argument in item 4 below, or an equivalent correction of the source proof. No change to the claimed critical theorem is needed.

2. **Source Lemma 4.8, p.28, (4.68): missing upper time restriction.** It states a polynomial lower bound for every n >= N^delta_2 in one fixed, finite killed rectangle. This is false as n tends to infinity with N fixed: the killed transition matrix has spectral radius less than one, so its diagonal decays exponentially. In the proof, the choice k of order n^((1+gamma)/4) must fit inside the available killing rectangle; this restriction is omitted. Fix: restrict to the applicable finite-scale time range and enlarge the killing constant as necessary. Lemma 4.9 only needs n between two fixed multiples of N^(4/(1+gamma)). The unrestricted backbone bound needed here is proved independently below. This defect is present throughout the source's parameter range; it is not an endpoint obstruction.

3. **Source p.31, (4.91): wrong event/inequality.** Bounds (4.85)–(4.90) make the probability of missing w before time n or exit at most 1/2. The conclusion should be P_v(tau_w <= n wedge tau_{B^c}) >= 1/2, equivalently P_v(tau_w > n wedge tau_{B^c}) <= 1/2. The printed display gives the opposite inequality for the latter event. Fix the complement. It is the corrected hitting probability that enters (4.84).

4. **Source pp.17–21: asymptotic constants and small-height bookkeeping.** In (4.4), the binomial success probability is exactly P(H_0 in [2^ell,2^(ell+1))), not exactly C 2^(-gamma ell)(1-2^(-gamma)); only the latter asymptotic follows from (1.7). The analogous fixed multiplicative identity asserted after (4.10) is also only asymptotic. Low dyadic bins can have zero probability, making the ratios in (4.1)/(4.9) undefined. The slice sum in (4.70) omits the backbone layer. Fix: use the actual bin probabilities, uniform two-sided bounds for sufficiently large ell, omit zero-mass bins, handle the finitely many lower bins separately, and add O(k) backbone volume. The concentration exponent and the volume order are unchanged. The polynomial prefactor in the union bound (4.8) need not have its printed precise power: an O(N^3) prefactor suffices against its stretched exponential. At the end of Lemma 4.5, use rho(b) = [2 c_eff c_tilde_eff/(b-1) + b^(-2/(1+gamma))]^(-1), or any smaller function tending to infinity; the printed expression does not correctly invert the preceding sum.

5. **Source Proposition 4.6 and Lemma 4.7, pp.22–28: details missing from the submitted dependency audit.** The interval in the sentence before (4.43) should start at n^(-epsilon), not n^epsilon. The coarse hitting times (4.53) must record a visit to a *different* site of F; successive returns to F as printed include returns to the same site and do not define the stated non-lazy simple walk. A fixed-t estimate followed by a spatial union bound in Case 1 does not itself prove simultaneous control of a continuum of t; use a geometric grid, monotonicity, adjusted constants, and the slack in alpha. In Case 2, the sentence claiming that exp(-c n^a) directly becomes exp(-c t^(-beta)) for all t < n^(-epsilon) omits a range argument. One repair is: when t^(1/2-alpha)n^(2/(1+gamma)) < 1, the bad event is empty once every exit path encounters a positive tooth; otherwise t >= n^(-[2/(1+gamma)]/(1/2-alpha)), and beta can be reduced to make the asserted conversion valid. The good events ensure the required positive teeth. In (4.65), gamma+2 in the depth exponent should be gamma+1. The final choice of beta_tilde must use the **minimum**, not the maximum, of beta(1/2-alpha) and alpha when combining two stretched exponentials. Finally, applications to boxes near the edge of an ambient interval require an enlarged ambient interval; this is suppressed in several uniformity statements. In fact Proposition 4.6 as literally stated can fail if P(H_0=0)>0: start at x=N with H_N=0 and follow a path exiting to the right without returning to N. Its positive probability of seeing no positive tooth *inside* [-N,N] contradicts the asserted bound as t tends to zero. Enlarging the interval in the definition of L^deep repairs this boundary issue. None of these repairs needs gamma > 1/3. The independent argument below bypasses Proposition 4.6 and Lemma 4.7 altogether, so I do not treat their printed all-t proof as an unqualified black box.

6. **Submitted REPORT, Proof 1: constants should include a nonempty time window.** Lemma 4.9 prints c_9,c_l,c_u > 0 without expressly printing c_l < c_u, and its proof never specifies c_u. The submitted argument correctly needs c_l < c_u. Fix: state the intended nonempty window explicitly; after establishing the hitting estimate and a finite-scale diagonal estimate, one may take c_u = 2 c_l with a suitable larger killing domain. The independent proof below uses just this choice. The proof also treats a start in the boundary-augmented rectangle as if it lay in the unaugmented one; enlarge N by one, or the fixed geometric constants, to handle this rounding issue.

7. **Submitted REPORT, literature conclusion: novelty is not established by an unsuccessful search.** The theorem is not an immediate application of Hutchcroft–Peres Theorem 1 or 4 to the comb rooted on its backbone. Those theorems require a suitable full-graph rooted law. The submitted direct transport supplies the missing variant, but its historical novelty remains provisional. Fix: describe the result as an apparently new deduction, with the search date and limitations. The source itself already cites Hutchcroft–Peres [20].

These are the issues found in the claim and its cited lower-bound chain. I found no error in (B)–(D), no missing environmental independence assumption in that calculation, and no counterexample to the theorem under (1.7). The MINOR classification concerns the corrected exposition and source qualification; the essential new argument survives.

2. Exact model, source statement, and dependency audit

Primary source: [De Ambroggio–Ng–Nitzschner–Scali, arXiv:2609.05343v1](https://arxiv.org/abs/2609.05343v1). I independently downloaded it, converted the PDF entirely through memory/stdin, and saved the 48-page text in sources/2609.05343v1.txt. Printed page numbers below agree with its form-feed pages. No PDF, page image, or scan was saved.

The law in (1.7), p.3, is

    P(H_0 > z) / (C z^(-gamma)) -> 1 as z -> infinity,
    C > 0, gamma in (0,1].

The heights are i.i.d. nonnegative, real-valued random variables. The graph uses their integer parts: vertices (x,h), x in Z, 0 <= h <= floor(H_x); edges are horizontal nearest-neighbor edges at height zero and vertical nearest-neighbor edges within each tooth. Heights are finite almost surely. No normalization, minimum positive height, or arbitrary slowly varying factor is assumed.

The walk is the synchronous, non-lazy, discrete-time simple random walk with K_1(u,v)=1/deg(u) on an edge, zero elsewhere; (2.3), p.6. The two walks are independent **conditional on the same environment**. A collision is equality of their vertices at one integer time. Opposite crossings of an edge do not count. ICP means infinitely many such times with quenched probability one from a common starting vertex; the recurrent-graph zero–one law makes the choice of that common vertex immaterial. Opposite bipartition starts cannot collide at all.

Theorem 4.1, p.16, has exactly two parts, under (1.7) and for P-almost every environment:

    (1) gamma > 1/3: ICP.
    (2) gamma < 1/3: finite collision property.

The parameter range of this theorem is the standing (0,1], so (1) includes gamma=1 and (2) means (0,1/3). Part (2) is supplied by the stronger Theorem 4.16 in Section 4.8, pp.37–40, using only an eventual lower tail bound. The source credits Koops (2020) with the earlier result under an additional tail restriction. It uses a cluster-corrected first-moment argument of Krishnapur–Peres type, not finiteness of expected total collisions. The display (4.137), if read as applying to every positive t, is impossible near zero; it must be understood eventually, which is all this argument requires.

The paragraph after Theorem 4.1 conjectures ICP at gamma=1/3 and attributes its omission to uniform estimates needed for the second-moment argument. Section 4.1, p.17, explicitly restricts gamma to (0,1) until Section 4.7; it does **not** restrict to (1/3,1). There is no additional moment or positive-height assumption there.

Write a=2/(1+gamma), alpha=4/(1+gamma), kappa=(3-gamma)/(1+gamma). In source notation,

    R_z^N(M) = {(x,h): |x-z|<=N, h<=M},
    D_z^N = all complete teeth over |x-z|<=N,
    bar R_N(N^a) = R_N(N^a) union its lateral and upper boundary.

Boundaries are vertices one step outside the rectangle, as in (2.2), p.5. The upper boundary can be empty. The kernel in (2.4) is the symmetric density

    p_n^{omega,A}(u,v)
      = P_u^omega(X_n=v, tau_{A^c}>n)/deg(v).

Every degree here is the degree in the original comb, including when the walk is killed.

**Lemma 4.9, pp.30–31, (4.83), with all of its stated constants and hypotheses:** there exist deterministic c_9,c_l,c_u>0 and b_tilde>1 such that, P-almost surely, for all N >= N_2(omega), all integer n in [c_l N^alpha,c_u N^alpha], and uniformly for

    v in bar R_N(N^a),  w in R_N(N),
    n-d(v,w) in 2 N_0,

one has

    p_n^{omega,R_{b_tilde N}((b_tilde N)^a)}(v,w)
      >= c_9 n^(-(3-gamma)/4).

Here d is ordinary graph distance; n-d in 2 N_0 includes reachability as well as parity. N_2 is the almost surely finite random cutoff introduced in Lemma 4.8. The source gives no numerical values for these constants, no explicit c_u, and no formula for N_2. Constants depend on the height law, gamma, and the auxiliary fixed choices, not on omega,N,n,v,w; the cutoff does depend on omega. Interpret the time window as nonempty after the repair in item 6.

Here is the complete relevant dependency chain, rather than an inference from the lemma's heading alone:

| Input | Exact content relevant to Lemma 4.9 | Endpoint check |
|---|---|---|
| Lemma 4.2, pp.17–18 | For each delta_1>0 there is a.s. finite N_0 such that every disk D_z^k inside D_N, k>=N^delta_1, is ell-good for ell=0,...,u(k), u(k)=floor(log_2(k^a))+1. Good means the counts in [2^ell,2^(ell+1)) and above 2^(ell+1) are within factors 1/4 and 4 of their expectations, with zero bins interpreted as above. | The least large-bin mean is of order k^((1-gamma)/(1+gamma)). At 1/3 this is k^(1/2). Chernoff plus a polynomial union bound is summable in N. |
| Corollary 4.3, p.18 | For every delta_1>0, deterministic c_vol>1, same cutoff N_0, same disks and k, and ell<=u(k), the volume of the dyadic height slice is between c_vol^(-1) and c_vol times its mean. | Integrating the tail gives truncated volume of order k^kappa; kappa=2 at the endpoint. Requires gamma<1, not 3gamma>1. |
| Corollary 4.4, pp.18–20 | For each delta_1>0, deterministic c_tilde_eff>1, same N_0 and contained disks k>=N^delta_1, R_eff(b_x,(R_x^k(k^a))^c) is within c_tilde_eff of its expectation. Deterministic c_eff>1 bounds that expectation between c_eff^(-1)k and c_eff k for all x,k. | The tall-tooth count has order k^((1-gamma)/(1+gamma)); divided by height k^a it gives conductance of order 1/k. The parallel-law and Jensen steps (4.13)–(4.19) use no endpoint-excluding inequality. |
| Lemma 4.5, pp.20–21 | A deterministic function rho(b)>0 tending to infinity bounds P_v(tau_w>tau_{R_{bN}((bN)^a)^c}) by 1/rho(b), uniformly for v in R_N(N^a), w in R_N(N), N>=N_0. | The proof splits off the starting tooth, then uses graph distance O(N) divided by escape resistance of order bN. Both b^(-a) and 1/(b-1) vanish at 1/3. Correct rho as above. |
| Proposition 4.6, pp.21–27 | For all sufficiently small delta,eta_0>0 (eta_0 is called alpha in the source), there are beta,C_6,c_6>0 and a.s. finite N_1 such that, for N>=N_1, n in [N^delta,N], t in (0,1], uniformly over x in [-N,N], P_x^Z(L_N^deep(T_{n,x}^{ex},sqrt(t)n^a) <= t^(1/2-eta_0)n^a) <= C_6 exp(-c_6 t^(-beta)). Ambient interval enlargements are understood for edge-centered boxes. | In (4.39) the gap between 4/(1+gamma) and 3-2gamma/(1+gamma) is (1-gamma)/(1+gamma), equal to 1/2 at the endpoint. In (4.41) choose epsilon with 5epsilon smaller than this gap. In (4.47)–(4.63) the other stretched-exponential exponents include epsilon gamma/12 and epsilon gamma/36, both positive. See item 5 for the actual proof corrections. |
| Lemma 4.7, pp.27–28 | For every sufficiently small delta>0 there are beta_tilde,C_7,c_7>0 such that, with N_1 as above, for N>=N_1, n in [N^delta,N], t in (0,1], and a start (x_1,h) in D_N, P(tau_{x_1,n}<t n^alpha) <= C_7 exp(-c_7 t^(-beta_tilde)). | Deep-tooth trials have success probability of order t^(-1/2)n^(-a); combining with Proposition 4.6 yields positive exponents without 3gamma-1. Correct the exponent typo and use the minimum of the two exponents. |
| Lemma 4.8, pp.28–30 | For delta_2>0 sufficiently small and b_tilde>1 sufficiently large, deterministic c_8>0 and a.s. finite N_2 give the printed bound p_{2floor(n/2)}^{omega,R_{b_tilde N}^{x_1}((b_tilde N)^a)}(x,x)>=c_8 n^(-(3-gamma)/4), for x in R_N(N), n>=N^delta_2. | Add the missing upper time qualification. The proof uses volume O(k^kappa), an O(1) survival probability, and k of order n^(1/alpha). The relation delta_2=4 max(delta,delta_1)/(1+gamma) allows arbitrarily small choices. Vertical diffusion costs height squared, namely k^alpha. No 3gamma-1 occurs. |
| Lemma 4.9 proof, pp.30–31 | (4.84) reduces off-diagonal density to hitting w before n/exit times the even-time diagonal density. (4.85)–(4.90) bound the failures by mean exit/hitting times and Lemma 4.5. Choose enlargement first and c_l afterward. | R times volume is N^(1+kappa)=N^alpha, and the vertical starting segment has squared-height time N^alpha. Correct (4.91), complete the constants and finite-window diagonal argument. |

The N_0 Borel–Cantelli step is valid because exp(-c N^(delta_1(1-gamma)/(1+gamma))) beats every polynomial. At gamma=1/3 it is exp(-c N^(delta_1/2)). The quenched N_1 step uses the same principle after Markov's inequality on the annealed concentration bound, with positive powers fixed before taking the environmental exceptional set. To obtain a common N_2, take the maximum of the applicable N_0,N_1, the deterministic rounding thresholds, and the finitely many cutoffs for the fixed enlarged ambient boxes. All enlargement factors are fixed before this maximum. Countably many shifts can be intersected afterward. There is no Borel–Cantelli summation requiring 3gamma-1>0 in this construction. The finite-time qualification of Lemma 4.8 must nevertheless be supplied; its printed all-time version is not justified by this maximum.

The first explicit *use* of gamma>1/3 in this random-comb proof, beyond announcing the target regime, is on p.35 immediately after (4.120): it chooses delta_4>0 so that N^(8delta_4) is absorbed into N^((3gamma-1)/(1+gamma)). Lemma 4.13's first-moment bound remains meaningful at the endpoint: it is of constant order per scale. Proposition 4.14's estimates (4.123) and (4.126) additionally sum k^(-(5-3gamma)/4); at 1/3 this becomes a harmonic sum. Thus simply substituting 1/3 in the source's uniform second-moment conclusion is invalid. Lemma 4.9 and all its geometric inputs are upstream of that obstruction.

3. Checking (A) and (B)–(D)

Let b_x=(x,0), d_x=deg(b_x) in {2,3}, and K_n(u,v)=P_u(X_n=v). Removing killing increases K_n and p_n. Since p_n=K_n/deg(target), the conversion is K_n(b_0,b_x)=d_x p_n(b_0,b_x), not division by d_x.

At gamma=1/3, alpha=3 and (3-gamma)/4=2/3. Given a nonempty constant window [c_l,c_u], choose a_* strictly between its endpoints and N=round((n/a_*)^(1/3)). Then N tends to infinity and n/N^3 tends to a_*; every sufficiently large integer n lies in the required window for this N. There are at least N integers in [-N,N] with x congruent to n modulo 2. For those integers graph distance is |x|, and n>=|x| holds eventually. Hence

    Q_n := sum_x K_n(b_0,b_x)^2
         >= 4 c_9^2 N n^(-4/3) >= c/n.

This is an eventual lower bound, not an asserted asymptotic equivalent. Its sum diverges. As a second arithmetic check, a scale-N window has order N^3 time points, N targets, and squared kernel of order N^(-4); each window contributes a positive constant. Disjoint geometrically spaced windows give the same divergence.

The remainder of the argument is independent of the heat-kernel proof. In a fixed environment define q_0(x) as the probability of no backbone collision at positive times, q_fin(x) as the probability of finitely many backbone collisions, and q_last(x,y) as the probability that the last such collision is b_y, for two walks from b_x. Time zero ensures that every finite realization has a unique last backbone collision. For each deterministic time n the pair Markov property gives

    q_last(x,y) = sum_{n>=0} K_n(b_x,b_y)^2 q_0(y),
    sum_y q_last(x,y) = q_fin(x) <= 1.

The random last time is not used as a stopping time. Instead, each deterministic-time term says that a collision occurs there and none occurs later. These events are disjoint over the possible last times. Collisions away from the backbone after this time are allowed and do not affect this identity.

For definiteness let (T_z omega)_x=H_{x+z}(omega). Relabeling b_{x+z} as b_x is a graph isomorphism preserving transition probabilities and backbone collision events. Consequently

    F_{T_z omega}(x,y)=F_omega(x+z,y+z),
    F_omega(x,y)=d_x^2 q_last(x,y).

The product height law is invariant under T_1, even though a sample environment usually is not. Covariance and Tonelli give

    E sum_y F(0,y) = sum_y E F(-y,0) = E sum_x F(x,0).

No unimodularity of the comb rooted on all its vertices, reflection invariance, or finite mean height is being assumed. Shift stationarity on the index set Z suffices.

Detailed balance in each fixed environment is

    d_x K_n(b_x,b_0)=d_0 K_n(b_0,b_x).

Squaring it is precisely why d_x^2 gives an exact incoming expression. Thus

    E sum_{n,x} d_0^2 K_n(b_0,b_x)^2 q_0(0)
      = E[d_0^2 q_fin(0)] <= 9.

All sums and expectations are of nonnegative quantities. Avoid the notation 0 times infinity: if q_0(0)>0, the displayed sum is infinite whenever G_B(0)=infinity. Its finite expectation therefore implies q_0(0)=0 almost surely. By stationarity and countability q_0(x)=0 simultaneously for every x, outside a single null set. Substitute those zeros into the termwise last-collision identity to obtain q_fin(x)=0 for every x. This is probability one under each surviving quenched law, not just a positive annealed probability.

For a common tooth start v, both walks can follow the same finite downward path with positive probability. After that they have infinitely many backbone collisions. The graph is recurrent: the complete teeth over [-r,r] form a finite set, and its edge boundary consists of two horizontal edges; the successive disjoint cutsets give infinite resistance to infinity. Barlow–Peres–Sousi Proposition 2.1 then upgrades positive probability of infinitely many total collisions to probability one, at every common start. This theorem was checked in its actual text, p.4. Its tail-triviality proof also applies to the backbone-collision event itself, so even that stronger conclusion can be transferred. For different starting vertices the corresponding statement holds only for the same bipartition class; simultaneous finite paths can be padded by two-step backtracks. Opposite classes never meet. The submitted common-start assertion has no parity gap.

4. Independent finite-scale repair of the lower-bound input

This proof establishes the unrestricted backbone estimate required in (A), for every fixed 0<gamma<1 under (1.7). It avoids the incorrect all-time killed assertion in Lemma 4.8 and the uniform-in-t details of Proposition 4.6. It is included so that acceptance of the critical theorem is not conditional on unproved repairs to the source.

Put

    a=2/(1+gamma), kappa=(3-gamma)/(1+gamma),
    alpha=1+kappa=2a=4/(1+gamma),
    eta=(1-gamma)/(1+gamma)>0.

For a large integer r, let D=R_z^r(r^a), a finite rectangle centered at b_z, and let L=floor(r^a). The following quenched bounds hold eventually and uniformly for centers in any fixed multiple of [-r,r]:

    |D| <= C r^kappa,
    R_eff(b_z,D^c) >= c r,
    |R_z^{epsilon r}((epsilon r)^a)| >= c_epsilon r^kappa

for every fixed epsilon>0 sufficiently small. They follow directly from (1.7), as follows. For Y=1+min(floor(H_0),L),

    E Y is of order L^(1-gamma),
    E Y^2 <= C L^(2-gamma).

Bernstein's inequality for the sum of O(r) bounded independent variables gives relative-volume failure probability at most C exp(-c r L^(-gamma)) = C exp(-c r^eta). The count M of teeth crossing height L has mean of order r L^(-gamma) and the same concentration order. Polynomially many centers and scales are therefore handled by a union bound and Borel–Cantelli. The same argument gives the lower volume bound for the smaller core. Degrees lie between one and three, so counting vertices or summing degrees changes constants only.

For resistance, separating the horizontal and upper exit sets gives

    R_eff(b_z,D^c)^(-1)
      <= R_eff(b_z,lateral exits)^(-1)
         + R_eff(b_z,upper exits)^(-1)
      <= 2/(r+1) + M/(L+1) <= C/r.

The first inequality is the subadditivity of capacity for a union of target sets. For the upper exits, shorting the backbone puts the M surviving teeth in parallel, giving the stated upper bound on conductance. If M=0 its contribution is zero. This also supplies a direct corrected proof of the particular resistance estimate used here.

Let g_D be the Green density of the killed walk. The voltage interpretation gives g_D(b_z,b_z)=R_eff(b_z,D^c)>=cr. Its variation across one unit-conductance edge is at most one, because the total injected current is one. Choose fixed epsilon<c/4. At backbone vertices within epsilon r the voltage remains at least cr/2. Along each attached tooth it is constant if the tooth ends inside D, and decreases linearly to zero at height L+1 otherwise. In the core with height at most (epsilon r)^a<=L/2 it is at least cr/4. Consequently

    E_{b_z} tau_{D^c}
      = sum_{v in D} deg(v) g_D(b_z,v)
      >= c r * c_epsilon r^kappa >= A r^alpha.

There is also a uniform upper bound over all starts in D:

    max_{v in D} E_v tau_{D^c} <= B r^alpha.

For a backbone start b_x in D, its resistance to a horizontal exit is at most 2r+1. The maximum principle and symmetry imply g_D(b_x,v)<=g_D(b_x,b_x)<=2r+1. Summing against degrees and using the volume upper bound gives C r^(1+kappa). For a start above the backbone, stop at its base or the upper exit first; the one-dimensional expected time is at most (L+1)^2. Continue from the base if necessary. Since 2a=1+kappa=alpha, this proves the uniform upper bound.

By the Markov property at deterministic m,

    E_{b_z} tau_{D^c}
      <= m + P_{b_z}(tau_{D^c}>m) max_v E_v tau_{D^c}.

Thus for m<=A r^alpha/2 the survival probability is at least A/(2B). Cauchy–Schwarz for the killed symmetric kernel yields

    p_{2m}^D(b_z,b_z)
      >= P_{b_z}(tau_{D^c}>m)^2 / sum_{v in D}deg(v)
      >= c r^(-kappa).

Choosing r to be an integer of order m^(1/alpha), with the multiplicative constant large enough, proves

    p_{2m}(b_z,b_z) >= c m^(-kappa/alpha)
                         = c m^(-(3-gamma)/4).

This is an unrestricted diagonal estimate. The auxiliary killing domain grows with m; it is never held fixed while m tends to infinity. The preceding uniform concentration covers the centers needed below.

Now fix |x|<=N. Take a larger rectangle D'=R_0^{bN}((bN)^a) with fixed b sufficiently large. The escape-before-hit resistance inequality (source (2.12), also obtainable directly from voltage) gives, for x nonzero,

    P_{b_0}(tau_{D'^c}<tau_{b_x})
      <= R_eff(b_0,b_x)/R_eff(b_0,D'^c)
      <= N/(c bN) <= 1/4.

For x=0 hitting is immediate. The uniform exit-time upper bound just proved gives

    P_{b_0}(tau_{b_x} wedge tau_{D'^c}>n)
      <= E_{b_0} tau_{D'^c}/n
      <= C (bN)^alpha/n <= 1/4

when n>=c_l N^alpha for a fixed sufficiently large c_l. Therefore the probability of hitting b_x by n before exit is at least 1/2, uniformly in |x|<=N. Set c_u=2c_l.

When n-x is even, every hitting time tau_{b_x} has the parity of x. The strong Markov property at that hitting time expresses p_n(b_0,b_x) as the expectation of p_{n-tau}(b_x,b_x) on tau<=n. Even-time diagonal densities are nonincreasing in their time index, by the spectral representation or the contraction identity for the self-adjoint transition operator. Since n-tau is even and at most 2floor(n/2),

    p_n(b_0,b_x)
      >= (1/2) p_{2floor(n/2)}(b_x,b_x)
      >= c n^(-(3-gamma)/4).

This holds for the fixed nonempty window [c_l N^alpha,2c_l N^alpha] and every sufficiently large N, on one full-measure environmental set. At gamma=1/3 it is precisely the n^(-2/3) estimate used in (A). The only strict exponent restriction in this independent argument is eta>0, or gamma<1. This resolves the load-bearing source qualification without assuming the source's collision theorem or any second moment.

5. Why the source used a second moment; relation to earlier work

The short argument is a variant of [Hutchcroft–Peres (2015)](https://arxiv.org/abs/1505.02484), particularly the last-collision decomposition and transport on preprint p.4. Their full-graph transport uses deg(u)q_last(u,v); reversibility then recovers the full return Green function, which diverges by recurrence. Here transport runs only between indexed backbone vertices, and uses deg(u)^2 to recover the restricted collision Green sum. This sum need not diverge from recurrence alone. Lemma 4.9 or the independent argument above supplies that additional fact at the critical exponent.

The law of (comb,b_0) is not stationary for the full walk: a walk step can place the root above the backbone, an event to which the original root law gives probability zero. Nor is it full-graph unimodular. To see the latter concretely, send unit mass from every vertex to the base of its tooth. A backbone root sends one but receives floor(H_0)+1, whose expectation is infinite here. No probability normalization by expected tooth length is available. Applying Hutchcroft–Peres directly without addressing this would be wrong; the submitted proof addresses it correctly by proving a Z-transport identity instead.

[Barlow–Peres–Sousi](https://arxiv.org/abs/1003.3255) supply the recurrent zero–one law and a uniform killed-Green criterion, both checked independently in their text. Their criterion works for many deterministic combs but does not by itself provide the critical random-profile estimate. [Krishnapur–Peres](https://arxiv.org/abs/math/0406487) give recurrent combs with finitely many collisions, despite infinite expected total collisions; this prevents replacing the restricted Green calculation with the assertion that recurrence alone is enough. Their infinite-tooth comb does not satisfy the needed backbone Green divergence.

Chen–Wei–Zhang's earlier polynomial-growth sufficient condition, and [Chen–Chen's wedge-comb criteria](https://arxiv.org/abs/1010.5366), do not settle this heavy-tail endpoint. In particular, finite-mean random-tooth results do not apply when the tail exponent is 1/3. The older continuous-time statements must also be distinguished from this synchronous discrete-time model. I checked the theorem statements in the author preprint available in the submitted sources for Chen–Wei–Zhang; it has a strict alpha<1/5 growth hypothesis. That source is used only for comparison, not as a proof input.

The source mentions Hutchcroft–Peres in its introduction and bibliography, but has no last-collision mass transport or backbone-restricted version of that argument. Its chosen proof establishes uniform probabilities of a collision from pairs of starts in large rectangles and iterates at exits. That requires the second-moment estimates. The transport instead exploits stationarity of the ensemble and can force the result from a common backbone start once the restricted Green sum diverges. Thus the source's longer method does not furnish a counterargument to the short proof. I cannot infer why the authors did not make this deduction; it is neither necessary nor justified to attribute a motivation to them.

6. Independent numerical evidence

I wrote code/check_backbone.py from scratch; no submitted simulation code was reused. It computes Q_n=sum_x K_n(b_0,b_x)^2 rather than inferring it from cumulative collision counts.

For each gamma in {0.28,1/3,0.40}, the run samples eight independent environments and evolves 4,000 independent walks in each environment up to time 4,096. The law is H=floor(U^(-1/gamma)), which satisfies (1.7) with C=1. Heights above the reachable horizon are represented by T+1; no tooth tip that can affect a path by time T is changed. Horizontal coordinates outside [-T,T] cannot be reached. Backbone choices are left/right/up with probability 1/3 each; internal tooth vertices move up/down equally, and tips move down deterministically. The walks are non-lazy and share each sampled environment.

If C_x is the number of walkers at b_x, the estimator is

    Q_hat_n = sum_x C_x(C_x-1) / (M(M-1)).

It is conditionally unbiased. Using sum C_x^2/M^2 instead would introduce self-pair bias of size 1/M, larger than the measured critical Q_n at the longest time. Uncertainty below is the standard error across independent environments, including their Monte Carlo variability; the correlated pairs within one environment are not treated as independent observations.

| gamma | mean n Q_hat_n, n=64 | n=256 | n=1024 | n=4096 |
|---|---:|---:|---:|---:|
| 0.28 | 0.471 (0.057) | 0.411 (0.040) | 0.389 (0.029) | 0.373 (0.027) |
| 1/3 | 0.474 (0.047) | 0.444 (0.038) | 0.475 (0.012) | 0.441 (0.027) |
| 0.40 | 0.699 (0.094) | 0.941 (0.166) | 0.967 (0.152) | 0.968 (0.166) |

The critical values are consistent with 1/n order. The nearby exponents are too close, and the horizon and ensemble too small, to distinguish their asymptotic powers reliably. These data establish neither a quenched lower bound nor an infinite-time collision property. Moreover, (A) itself proves only a lower bound, not an exact asymptotic for Q_n.

For an independent implementation check, exact probability propagation on the toothless line agrees with Q_n=binom(2n,n)/4^n to maximum absolute error 2.78e-17 through n=32. Exact propagation on one sampled finite light cone was compared with 100,000 independent walkers at n=16,32,64; absolute discrepancies were 0.000305,0.000220,0.0000864, respectively. Exact propagation conserves probability and has zero mass on the forbidden parity. These are checks of the implementation, not additional evidence for the theorem.

Data and seeds are in data/backbone_kernel.csv, data/summary.csv, and data/validation.json. The recorded run took 6.59 seconds, one worker, with inherited nice 10 verified through libc getpriority. Arrays are small and thread counts are forced to one. The run stayed far below 4 GB.

7. Literature result and exact value of the claim

As checked on 13 November 2026, the [arXiv listing](https://arxiv.org/abs/2609.05343) has only v1, submitted 4 September 2026 at 16:45:39 UTC. A direct v2 request did not yield a version; the positive evidence for the version history is the listing itself. Searches by arXiv identifier, full title, author names with the endpoint, and backbone/mass-transport terms found the original article and discovery/review pages, but no subsequent research paper settling the boundary case or applying this particular criterion to it. The Semantic Scholar citation API returned HTTP 429; this is recorded in sources/citation_api.txt and supplies no citation count. Failure of an index is not evidence of zero citations.

The related 2026 paper [Astoquillca–Martinez-Arevalo, arXiv:2607.04002](https://arxiv.org/abs/2607.04002) develops full-graph unimodular collision criteria and applications to geometric graphs and long-range percolation. I inspected its text for comb/backbone/critical-endpoint treatment. It predates the September source and does not establish the present endpoint. Its existence reinforces the need to distinguish full-graph rooted criteria from the restricted transport here. No search can rule out an unindexed manuscript; priority remains a qualified conclusion, not a proved mathematical assertion.

Exactly what is established: for every i.i.d. nonnegative height law with P(H_0>t)~C t^(-1/3), C>0, there is a full-measure set of environments in which two independent non-lazy synchronous simple random walks started at any common backbone vertex have infinitely many backbone collisions with quenched probability one. Consequently each such comb has ICP from every common vertex. The same-parity extension follows as described above. The proof does not classify arbitrary t^(-1/3)L(t) with nonconvergent slowly varying L, prove any triple-collision statement, or derive an exact limiting constant for n Q_n.

Task: “You are an independent referee” — I0012 critical random-comb collision claim; recorded start 13 November 2026, 14:52 +04.
