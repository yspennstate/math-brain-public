# P0306 — attempt and referee audit (2026-10-11)

## Exact target

Fix gamma in (0,2). Let h be a free-boundary (Neumann) GFF on the upper half-plane, normalized to have zero average on the unit semicircle. Let D_h be its gamma-LQG metric, continuously extended to the closed upper half-plane. A two-star point admits two nontrivial geodesics with disjoint interiors; shortening the geodesics if necessary gives two arcs meeting only at their initial point. Put S=T_{2-star} intersect R. The target is almost-sure dim_{D_h}(S)=1 for each fixed gamma. All boundary distances and diameters below use the ambient metric. No intrinsic boundary length metric is substituted.

Verified source: Bhatia–Gwynne–Harper, arXiv:2606.10496v1, Conjecture 1.4 (PDF p.7), definition p.4, Theorem 1.3(1) p.6, boundary metric construction p.13. Theorem 1.3 proves the lower bound only. The remaining target is dim_{D_h}(S)<=1.

## 1. A rigorous sufficient covering condition

This is a conditional reduction, not an estimate proved for LQG.

Let D be a random metric inducing the Euclidean topology on the closed half-plane. Suppose S is covered by countably many sets S_m. For each integer K>=1 and n>=1 let I_{n,j} be the 2K*2^n closed dyadic intervals partitioning [-K,K], of length r_n=2^{-n}. Let A_{m,n,j} be measurable events such that, for every outcome outside one common null set,

    S_m intersect I_{n,j} nonempty implies A_{m,n,j}.

Assume for a fixed s>1 that, for each m,K, there are constants C<infinity, eta>0 and n_0 with

    E[1_{A_{m,n,j}} diam_D(I_{n,j})^s] <= C r_n^{1+eta}       (1)

for all n>=n_0 and all those j. Then H_D^s(S)=0 almost surely.

**Proof.** Define W_n=sum_j 1_{A_{m,n,j}} diam_D(I_{n,j})^s. The sum is finite, nonnegative and measurable. Its expectation is at most 2K*C*2^{-n eta}. Consequently E[sum_{n>=n_0} W_n]<infinity by monotone convergence. A nonnegative random variable with finite expectation is finite almost surely, so sum_n W_n<infinity and W_n->0 almost surely. For a fixed outcome, the identity map from the compact Euclidean interval [-K,K] to its D-metric image is continuous and thus uniformly continuous. Hence delta_n=max_j diam_D(I_{n,j})->0. The intervals for which A_{m,n,j} occurs cover S_m intersect [-K,K], and their s-cost is W_n. For any delta>0, all sufficiently large n have delta_n<delta, so the delta-Hausdorff content is at most W_n for arbitrarily large n, and is zero. Thus H_D^s(S_m intersect [-K,K])=0. Intersect the probability-one events over m,K; countable subadditivity proves H_D^s(S)=0. QED.

If (1) holds for a sequence s_l decreasing to 1, intersecting another countable family of probability-one events proves dim_D(S)<=1. Combining with the source's lower bound would solve P0306.

No decomposition by rational target points is assumed. One can take S_m=S for every m. A potentially useful decomposition uses stars admitting two shortened arcs of metric length >=1/m, meeting only at the start. Every star belongs to some such class. Measurability of a chosen arm event and its uniform estimate are requirements, not silently assumed conclusions. In particular the covering theorem permits measurable supersets of potentially nonmeasurable hit events.

## 2. Exact Gaussian tilting formulation of the missing estimate

For each interval I of Euclidean length r, let H_I be the GFF semicircle average at a fixed point of I and radius r. For now the following is a general Gaussian statement: H_I is centered with variance v_I, and v_I=2 log(1/r)+O_K(1) uniformly on the compact boundary range. Put xi=gamma/d_gamma, Q=2/gamma+gamma/2. Define the normalized random variable by an identity, not an independence assertion:

    Z_I= r^{-xi Q} exp(-xi H_I) diam_D(I).

For s>0 let P_{I,s} have density exp(s xi H_I - (s xi)^2 v_I/2) relative to the original law. Its integral is 1 by the centered Gaussian moment-generating formula. For every nonnegative measurable Y, even if its expectation is infinite, this density gives

    E[exp(s xi H_I)Y] = exp((s xi)^2 v_I/2) E_{I,s}[Y].

In particular, exactly,

    E[1_A diam_D(I)^s]
      = r^{xi Q s} exp((s xi)^2 v_I/2) E_{I,s}[1_A Z_I^s].       (2)

The bounded variance error implies that the first two factors are bounded above by C_{K,s} r^{xi Q s-xi^2 s^2}. Therefore the following *unproved LQG input* suffices:

    E_{I,s}[1_{A_{m,I}} Z_I^s] <= C_{m,K,s} r^{q_s},
    q_s+xi Q s-xi^2 s^2>1.                                  (3)

Equation (2) and (3) imply (1) with eta=q_s+xi Q s-xi^2 s^2-1>0; Section 1 proves the consequence. No independence between the star event, average, or diameter is needed. In this formulation A and Z are the original measurable functionals viewed under a changed probability law; this is not a claim that a logarithmically shifted field has the same geodesics.

The variance normalization follows from the actual kernel on source p.13: its two singular logarithms each contribute log(1/r) on a boundary semicircle, while the normalizing terms remain bounded on a fixed compact boundary range. The logarithmic singularities in the angular double integral are integrable and give constants independent of r. The source's metric construction is consistent with xi and Q. Crucially, neither the kernel nor scaling proves (3).

## 3. Critical exponent and its exact checks

Write a=xi Q and b=xi^2. The critical value in this first-moment method is

    q_crit=1-a+b.

If the same exponent q_s=q_crit is available in (3) for s=1+e arbitrarily close to 1, then the summability gap equals

    q_crit+a(1+e)-b(1+e)^2-1 = e(a-2b-be).                   (4)

Thus a>2b and 0<e<(a-2b)/b give a positive gap. More generally q_s>=q_crit-o(s-1), as s decreases to 1, suffices. An error merely described as o(1) does not suffice.

For the LQG parameter range, the established bound d_gamma>=2 gives 2xi<=gamma, while Q-gamma=(4-gamma^2)/(2gamma)>0, so Q>2xi and a>2b. For explicit source verification of d_gamma>=2, the source appendix p.49 quotes [GP19, Corollary 2.5]: below sqrt(8/3), d_gamma>=(4+gamma^2+sqrt(16+gamma^4))/4>=2; above sqrt(8/3), d_gamma>=(4+gamma^2+sqrt(16+2gamma^2+gamma^4))/3>2. The reduction can also be used simply with a>2b as an explicit hypothesis without appealing to any dimension estimate. The parameter bound is used only to check the algebraic margin; it supplies no arm probability.

At Brownian parameters gamma=sqrt(8/3), d_gamma=4, a=5/6, b=1/6, q_crit=1/3. This is a required tilted weighted-arm exponent for this sufficient criterion; it is **not** a proved arm exponent or a proved Brownian special case. Rational checks and Lean algebra are in ExponentCheck.lean and exponent_checks.py.

A thickness optimization reaches the same value:

    t^2/4 - xi t + xi Q + q_crit - 1 = (t/2-xi)^2.

This identity is algebra only. Using it as a dimension calculation would additionally require joint multifractal/arm estimates not proved here.

## 4. A fully computed failure of an independence shortcut

Let L=log(1/r), H~N(0,2L), Z=1 and A={H>=cL}. The original event probability is the standard Gaussian upper tail at c sqrt(L/2). Tilting by exp(tH-t^2 L) changes H to N(2tL,2L), so its probability under the tilt is the tail at (c-2t)sqrt(L/2). This follows directly by completing the square in the Gaussian density. Taking c=1 and t=1/2 gives P_t(A)=1/2 for every r, while P(A) tends to zero. Exactly,

    E[1_A exp(tH)] / (P(A) E[exp(tH)]) = P_t(A)/P(A) -> infinity.

Thus even an exponentially small ordinary event probability cannot supply the tilted estimate (3). exponent_checks.py evaluates these tails at three dyadic scales using erfc; it does not simulate or approximate LQG. This is a counterexample to the probabilistic shortcut, not to P0306.

## 5. Special case and earlier obstruction, with full proof

In the Euclidean closed half-plane every boundary point x supports the horizontal segments [x-1,x] and [x,x+1] as two disjoint-interior geodesics. Hence S=R and dim_D(S)=1. For the upper bound, a bounded boundary interval is covered by N equal intervals of diameter L/N; for s>1 their total cost L^s N^{1-s} tends to zero. For the lower bound, any cover of an interval of length L by sets of Euclidean diameter d_j has sum_j d_j>=L: replace each nonempty set by a real interval of the same diameter, enlarge it arbitrarily slightly, and apply compactness and finite subadditivity of interval lengths. Therefore H^1 of a nontrivial interval is positive and dimension is at least 1. Countable unions give the result for R. This is gamma=0 intuition only, outside the stated gamma range; it does not establish any positive-gamma special case or convergence of dimensions.

The earlier brain argument is independently valid: for rho(x,y)=|x-y|^alpha with 0<alpha<1, every set has rho-diameter equal to its Euclidean diameter to the alpha power. Covers with rho-mesh delta correspond exactly to Euclidean-mesh delta^{1/alpha}, and their s-costs equal the alpha*s-costs. The preceding interval dimension calculation gives dim_rho([0,1])=1/alpha. The metrics have the same topology. This disproves the shortcut from a topological line to metric dimension one, but rho is not asserted to be a half-plane LQG metric.

## 6. Hostile referee checklist and remaining gap

* Same metric: yes, every interval diameter is measured by ambient distances between its boundary points; paths may enter the half-plane.
* Geodesic quantifiers: the cover must contain all star points, not only geodesics to chosen deterministic targets. No countable-target identification is claimed.
* Countable versus uncountable statements: probability-one intersections used above are countable (m,K,n,s_l). No claim holds simultaneously for all gamma.
* Mesh tending to zero: uniform continuity on each compact boundary interval is explicitly used.
* Measurability: the theorem assumes measurable events and diameter variables; measurable supersets of hit events are allowed. No unverified random-set measurability theorem is used.
* GFF dependence: (2) is exact, and the computed Gaussian example rules out factoring the mixed moment without proof.
* Exponent: (4) must be positive; a scale exponent equal to 1 alone need not give a summable cover. Lean checks only algebra, not random geometry.
* Prior/bulk results: the Brownian-map bulk formula 5-k is not a boundary upper bound; for other gamma the source itself says bulk dimensions are still open.

**Remaining gap:** prove the tilted weighted-diameter estimate (3) for a sequence s decreasing to 1, uniformly over intervals in each compact boundary range, for measurable arm events covering all boundary two-stars. Section 8 below constructs universally measurable exact hit events, usable on completed probability spaces. No estimate for those events or alternative LQG upper bound is proved here. Neither a proof nor a counterexample to P0306 has been obtained.

## 7. Additional routes tested and why they do not close the gap

* **Bulk dimension transplantation.** The source's exact Brownian-map bulk two-star dimension is 3, not 1. A general intersection dimension subtraction rule is unavailable because both the boundary and stars are field dependent. No independence or transversality hypothesis for such a rule has been established.
* **Covering by geodesic traces.** A countable union of geodesic images has metric dimension at most 1: each length-parametrized geodesic is an isometric interval and the interval covering calculation in Section 5 applies. But a two-star at a boundary point is the common endpoint of two geodesics, not necessarily an interior point of a single shortest path. Concatenating its arms need not be minimizing. Strong confluence statements concern agreement away from endpoints and do not by themselves put all these boundary endpoints into a countable union of traces. The countable cover inclusion required by this route is unproved.
* **Boundary KPZ.** The star set is determined by h. Applying an independence-based KPZ formula to it is unsupported. The worst-case bounds in the source are lower-bound tools and do not establish dimension <=1.
* **Mesh simulation.** A finite graph assigns only finitely many vertices to its star set, hence Hausdorff dimension zero; a fitted finite-scale slope needs a proved scaling limit and event correspondence before it bears on this question. No numerical graph exponent is claimed here. Exact Gaussian computations were preferred for the specific dependence assumption they can test.

## 8. Measurable exact arm events on the completed metric law

This removes the measurability construction from the main stochastic gap. Let X be the Euclidean closed half-plane. Regard a continuous metric D as an element of the Polish space M=C(X times X,R), equipped with uniform convergence on compact sets. Assume D is a measurable random element of M whose realizations are metrics inducing the Euclidean topology. These are the usual measurable continuous metric realizations; the following argument itself is deterministic descriptive set theory.

For ell=1/m and a compact boundary interval I define A_{m,I} to be the event that there are two paths P_1,P_2 in C([0,ell],X) with a common initial point in I, each isometric for D (D(P_i(t),P_i(u))=|t-u|), and their images intersect only at that initial point. This is an exact hit event for S_m, the stars supporting two shortened arms of length ell.

**Proof of universal measurability and countable coverage.** The path space is Polish for uniform Euclidean convergence. In the product of M with two path spaces, the initial-point conditions are closed. The isometry condition is equivalent, by continuity, to the countable conjunction of equalities for t,u in a fixed countable dense subset of [0,ell] containing the endpoints, and is Borel. For each integer k with 1/k<=ell, impose

    min_{t,u in [1/k,ell]} D(P_1(t),P_2(u)) > 0.              (5)

The displayed minimum is a continuous functional on this product: convergent paths have images in a common compact Euclidean subset, D converges uniformly there, and minima of uniformly convergent continuous functions on a fixed compact parameter square converge. Thus (5) is an open condition. Its countable conjunction is Borel. For metric realizations, this conjunction means exactly that the two positive-time images are disjoint. Indeed, if they meet at positive times, some k includes both times and the minimum is zero. Conversely, if they are disjoint, their truncated images are disjoint compact metric sets and have positive distance, for every k. Each isometric path is injective and never returns to its initial point, so these conditions also exclude a positive-time encounter with the initial point.

Projecting this Borel relation onto M gives an analytic set. By the standard analytic-set measurability theorem (analytic subsets of Polish spaces are universally measurable), A_{m,I} is measurable in the completion of every Borel probability law on M, and its pullback is measurable on the completed underlying probability space. Every two-star has two strictly positive length geodesics; shorten each below its original length and then to a common 1/m. All positive-time points of the shortened arcs lie in original interiors and are disjoint. Hence S=union_m S_m. Conversely, the witness for A_{m,I} is a pair of nontrivial disjoint-interior geodesics, so its initial point is a two-star in I. This proves both exact coverage and the claimed measurability. QED.

Completion causes no problem for the Gaussian tilt: its density is finite and strictly positive, so the original and tilted laws have the same null sets. Interval diameter is a measurable (indeed continuous in D on a fixed I) supremum over I times I. Therefore all mixed moments in Sections 1–2 are meaningful for these exact events. This does not give a probability bound for them.

For applicability to a random continuous metric given by deterministic-point distance variables, measurability as an M-valued variable follows from the countable dense evaluation criterion. The Borel sigma-field of M is generated by point evaluations on a countable dense subset of X times X: on each compact exhaustion the supremum norm is the supremum over a countable dense evaluation set, and the topology is separable. Each LQG distance at a fixed pair is measurable by its construction; continuity of the extended metric gives exactly this realization. No additional independence or confluence condition is needed for this measurability step.

## 9. A quantitative obstruction to using marginal estimates via Holder

Suppose, conditionally, that P(A_I)<=C r^p and E[diam_D(I)^t]<=C_t r^{a t-b t^2}, with b>0 and t>s. Holder's inequality with conjugate exponents t/s and t/(t-s) gives

    E[1_A diam_D(I)^s]
      <= P(A)^{1-s/t} E[diam_D(I)^t]^{s/t}
      <= C' r^{p(1-s/t)+a s-b s t}.                         (6)

For fixed p>0, the exponent is a s+p-s(bt+p/t). Since

    bt+p/t-2sqrt(bp) = (sqrt(bt)-sqrt(p/t))^2 >=0,

its maximum over t>0 is a s+p-2s sqrt(bp), attained at t=sqrt(p/b). This maximum is usable in (6) only when t>s and the indicated moment bound is available. A strict sufficient condition for this particular optimization to produce summability near s=1 is

    a+p-2sqrt(bp)>1,
    p>b.

When q_crit=1-a+b>=0 these two strict conditions reduce to

    p > (sqrt(b)+sqrt(q_crit))^2.

Indeed a+p-2sqrt(bp)-1=(sqrt(p)-sqrt(b))^2-q_crit; p>b selects the positive square-root branch. Strict positivity and t>1 persist for all s>1 sufficiently close to 1 by continuity. This proves the stated conservative sufficient threshold, assuming the required t-th moments; no LQG moment law or arm probability is asserted. The endpoint must also be examined: if q_crit>0, p=(sqrt(b)+sqrt(q_crit))^2<1, then t=sqrt(p/b)>1 and the optimized exponent is exactly 1+(s-1)(1-p). Thus equality at this threshold also suffices for s>1 close to 1. No strict necessity is claimed.

For a=5/6, b=1/6, q_crit=1/3, the threshold is 1/2+sqrt(2)/3, about 0.971405. At the critical value t=1+sqrt(2); since the threshold is below 1, equality also suffices. In contrast, an ordinary probability exponent p=1/3 gives an optimized exponent at s=1 of 7/6-sqrt(2)/3, about 0.695262, strictly less than 1. By continuity this stays below 1 for s>1 sufficiently close to 1. Thus such ordinary probability and unconditional moment estimates cannot, via Holder alone, establish dimension <=1. This is a limitation of that proof method, not a lower bound on the true arm exponent and not evidence against the conjecture.

Referee correction: an earlier formulation incorrectly called the strict threshold necessary. The equality endpoint calculation above corrects that claim; all recorded results use the corrected sufficient statement.

## Final validation and verdict

The corrected ExponentCheck.lean passed `lake env lean` from ~/lean_verify with exit code 0 on 2026-10-11. Its four algebraic lemmas are kernel checked, with no sorry or native_decide. The initial omitted-import failure and serial-run provenance are documented in LEAN_CHECK.md. Exact rational checks and Gaussian-tail computations are in exponent_results.json, reproducible with exponent_checks.py. These computations test algebra and a dependence shortcut; they are not numerical evidence for the LQG conjecture.

VERDICT: PARTIAL. This attempt ends with a proved covering/tilting reduction, exact measurable arm events, and a fully explicit remaining stochastic estimate. No positive-gamma upper bound, complete answer, or counterexample to P0306 is claimed.


## Serious second attempt, 11 October 2026

See SECOND_ATTEMPT.md for the two new approaches, the complete real-tree and Lipschitz-transfer proofs, and a proper planar geodesic countermodel to a deterministic record-set shortcut. See RECORD_REDUCTION.md for the cactus-map audit, an explicit cactus-leaf obstruction, a fully proved Brownian contour-record-image dimension bound, and a conditional Poisson calculation showing why boundary labels cannot replace full contour minima.

The original P0306 equality remains unproved. The additional sufficient reduction requires a countable Lipschitz cover of all relevant boundary two-stars by tree skeleton or full-contour record images. Such a cover was not proved. The Brownian coding alone also does not address arbitrary gamma or provide the necessary local-law transfer to the stated Neumann-GFF half-plane. The earlier Gaussian-tilted mixed arm/diameter estimate remains missing. None of the deterministic countermodels is asserted to be LQG.

The second approach was also made quantitative in BARRIER_REDUCTION.md. Its conditional-expectation proof gives an exact sufficient exponent, including a diameter-size-biased law formulation; the required LQG barrier and moment estimates are not proved. The full audit is in SECOND_REFEREE.md, with exact source excerpts in SECOND_SOURCE_EXCERPTS.md.
