# F0034 — research record, 12 October 2026

## Outcome and exact scope

The full bubble hypothesis is NOT solved here. A proof of part (a), using the source's infinite-horizon relevant-point density and backbone reversibility, is given below. Part (b) is reduced to exclusion of an inverse chain converging to one finite backbone point, with both endpoint times converging to the same time. That exclusion remains unproved. These are results of this attempt, not a claim of a solution in print or of novelty.

Work is on the **standard**, stationary Brownian-net backbone described in Section 8.2 of Schertzer–Sun–Swart, arXiv:1506.00724v3. Write B for its set of complete paths, N for its graph, S for its separation points, M for its meeting points, and add the two formal endpoints as in the question. Write f=φ, a map on S*∪M*. At a finite separation, f is the first reunion of the extreme forward paths, or +∞; at a finite meeting, it is the first reunion of the extreme **backbone** histories read backward, or −∞. The two formal endpoints map to one another. In particular, backward histories below are not dual-net paths.

The target is the simultaneous almost-sure absence of (a) injective forward f-chains and (b) injective inverse f-chains. The statement and source definitions were checked directly on PDF pages 70–71; the exact conjecture is quoted in LITERATURE.md.

## Inputs from the source (not new assertions)

1. N is the graph of complete backbone paths and has the image-set property: a complete continuous path lying in that graph belongs to B. Source Proposition 3.17 and Section 8.2, page 70. Consequently finite pieces of complete paths may be concatenated at common vertices, with complete past and future pieces added. This yields a complete backbone path.
2. Left/right extremal paths contain other paths. Proposition 3.14, page 22: a net path to the right of a left-web path at an interior time cannot subsequently cross to its left; the reflected assertion holds for right-web paths. At a separation point the outgoing extremal paths continue incoming paths: explicitly noted after Definition 4.5, page 30. Since the separation is on the backbone, their continuations can be attached to a complete incoming backbone path. For completeness, Remark 3.27 bounds every incoming backbone path near the separation between the unique incoming p-pair of equivalent web paths. By Definition 3.23 that pair coincides along a sequence of times increasing to the separation. At one of these times both web paths therefore intersect the incoming backbone path, strictly after their starting times and strictly before the separation. Proposition 3.15(i) attaches the complete backbone past there to each incoming web path; their extremal outgoing continuations give the desired complete extensions. Thus the extreme outgoing branches used below have complete backbone extensions. This avoids applying random-time hopping to a path which starts at the hopping time, which Proposition 3.15 does not authorize.
3. The law of the collection B is invariant under space-time reflection, Remark 3.20, page 24, and under time reversal as explained in Section 8.2, page 71. Thus pathwise assertions holding almost surely for all forward backbone paths also hold almost surely for all reversed backbone paths. Reversed paths are the actual backbone histories, not the usual dual paths.
4. The net is a compact collection of continuous paths, in the usual compactified path topology. On a finite time interval where a family of paths stays in a common finite spatial interval, compactness gives uniform equicontinuity in the ordinary coordinates. A quick justification: failure of equicontinuity would give a sequence of paths and pairs of times coalescing to a common finite time but with a fixed spatial displacement; a convergent subsequence in the path topology contradicts continuity of its limit. This applies to complete backbone paths passing through a fixed finite vertex, since they form a closed subfamily and barriers bound their finite future intervals.
5. Definition 4.5 and Proposition 4.7, page 30, allow deterministic horizons −∞≤S<U≤∞. If R_{S,U} is the relevant separation-point set, then for Borel A⊂R×(S,U),

   E[#(R_{S,U}∩A)] = 2∫_A Ψ(t−S)Ψ(U−t) dx dt,

   Ψ(h)=e^(−h)/√(πh)+2Φ(√(2h)), 0<h≤∞, with Ψ(∞)=2.

   On the backbone, R_{−∞,∞} is exactly the separations whose extreme paths never meet, as stated on page 71. R_{−∞,U} consists of the backbone separations at times t<U whose extremes stay distinct on (t,U). A reunion exactly at U is allowed. We will only use chains with reunion strictly after U.

All uses of these probabilistic inputs are on simultaneous probability-one events for countably many deterministic horizons and barriers. No conditioning at a random separation point, no orbit Markov property, and no independent increment law along an orbit are assumed.

## Lemma 1: geometric monotonicity and ancestry

Suppose s∈S and m=f(s)∈M are finite, at times a<b. If s'=f(m) is finite, at time c, then c≤a, and there is a backbone path from s' to s. If c=a, then s'=s. Hence, if s'≠s, then c<a. By reversal: if m∈M, s=f(m)∈S and m'=f(s) are finite, then time(m')≥time(m), m is an ancestor of m', and equality of their times implies m'=m.

**Proof.** Let l,r be the complete extensions of the extreme forward branches from s up to m. They are distinct on (a,b), and both are backbone histories ending at m. Let L,R be the extreme backbone histories ending at m, written in ordinary forward coordinates. Their extremality means that every complete backbone history through m is between them at each earlier time. If their first backward reunion had time c>a, the two histories l and r would have to coincide at c, which contradicts their distinction on (a,b). Thus c≤a.

At c the histories L,R have the same spatial coordinate, that of s'. Therefore the complete extension of l, also bounded by them, passes through s'. Its segment from c to a connects s' to s. If c=a, its coordinate is also the coordinate of s, so s'=s. Reflect this argument to obtain the meeting-point assertion. ∎

This proves monotonicity of endpoint **times**. It does not assert containment of the entire geometric regions between forward extreme branches. No nested-region assertion from the earlier intake attempt is used.

## Lemma 2: a universal linear spatial bound for ancestors and descendants

Almost surely, for every finite backbone vertex w there is a finite random constant C_w such that every backbone ancestor (x,t) of w satisfies |x|≤C_w(1+|t|), t≤time(w). The analogous statement holds for descendants at t≥time(w). In particular all descendants of w in a bounded time interval lie in a compact rectangle.

**Proof.** First establish the forward statement, simultaneously for all possible starting vertices. Fix integers q and j≥1. For positive integers K take the left-web path l_K from (−K,q) and the right-web path r_K from (K,q). They have the marginal laws of Brownian motions with drifts −1 and +1, respectively. For each fixed j, Brownian maximal tail bounds imply

   ∑_{K≥1} P(sup_{q≤t≤q+j}|l_K(t)+K+(t−q)|>K/2) <∞,

and the corresponding right-path sum is finite. For example the reflection bound gives an upper bound of 4 exp(−K²/(8j)), with a harmless adjustment for small K. Independence across K is not needed. Borel–Cantelli implies that, for any finite R, sufficiently large K satisfy l_K(t)<−R and r_K(t)>R throughout [q,q+j]. This holds simultaneously for all integer q,j,R.

Each of the countably many paths l_K,r_K also has at most linear growth on [q,∞), because a Brownian motion W has W(h)/h→0 almost surely. Its continuous behavior on bounded intervals is bounded as well.

Given any w=(x_0,t_0), choose q<t_0<q+j and integer R>|x_0|, and then one of the preceding barrier pairs. A complete backbone path through w lies strictly between these barriers at t_0. Proposition 3.14 traps its entire future between them. Their linear growth bounds every such future path by a common C_w(1+|t|). The events used were countable and concern deterministic barriers, so the conclusion holds simultaneously for random w too. Finally apply the same probability-one property to the reversed backbone collection, using its equal law, to obtain the ancestral bound. ∎

## Lemma 3: finite returning separations in a cone

For each rational U define

   D_U = R_{−∞,U} \ R_{−∞,∞}.

These are backbone separations still open through (t,U) but eventually returning at a finite time ≥U. For rational T<U and positive integer K, almost surely D_U has only finitely many points in

   A_{K,T} = {(x,t): t≤T, |x|≤K(1+|t|)}.

**Proof.** For any bounded Borel A at positive time distance below U, both relevant-point counts have finite expectations by Proposition 4.7. Since R_{−∞,∞}⊂R_{−∞,U}, subtraction gives

   E[#(D_U∩A)] = 4∫_A [Ψ(U−t)−2] dx dt.

Exhaustion by bounded sets and monotone convergence extends this equality to A_{K,T}. The difference is nonnegative because it is a counting-measure density. It also satisfies the elementary bound

   0≤Ψ(h)−2 = e^(−h)/√(πh) − erfc(√h) ≤ e^(−h)/√(πh).

Here erfc(v)=(2/√π)∫_v^∞e^(−u²)du≥0. Nonnegativity also follows directly by bounding u/v≥1 in that integral when v>0. For δ=U−T>0,

   E[#(D_U∩A_{K,T})]
   ≤8K∫_{−∞}^T (1+|t|) e^(−(U−t))/√(π(U−t)) dt <∞.

After the substitution h=U−t, the lower integration limit is δ and the integrand is bounded by a constant times (1+h)e^(−h)/√h, which is integrable. A nonnegative integer-valued extended random variable with finite expectation cannot equal ∞ on an event of positive probability. Take the countable intersection over U,T,K. ∎

This is the reason the earlier heavy-tail argument is not applicable here: subtracting the **never-returning** separations leaves an exponentially decaying density of finite-returning separations of long duration. The density is not a probability distribution at an arbitrary randomly chosen separation point.

## Theorem 4: part (a) of Conjecture 8.1

Almost surely there is no infinite injective forward f-chain.

**Proof.** Work on the probability-one event of Lemmas 1–3. If a forward orbit encounters either formal endpoint, it enters their two-cycle immediately, so it cannot be injective. Otherwise all vertices are finite. Deleting at most its initial meeting vertex, write any hypothetical injective orbit as

   s_0, m_0, s_1, m_1, ...,
   f(s_n)=m_n, f(m_n)=s_{n+1}.

Put a_n=time(s_n) and b_n=time(m_n). Lemma 1 gives a_{n+1}≤a_n and b_{n+1}≥b_n. In fact these are strict for an injective orbit, but weak inequalities suffice. It also gives a backbone path from s_{n+1} to s_n. Concatenating finitely many such segments using the image-set property shows that every s_n is a backbone ancestor of s_0.

Choose rational numbers T,U with a_0<T<U<b_0. For every n, a_n≤a_0<T and b_n≥b_0>U. Thus s_n∈R_{−∞,U}. Its image m_n is finite, so s_n∉R_{−∞,∞}; therefore s_n∈D_U.

By Lemma 2, all s_n lie in the ancestral linear cone of s_0. Choose an integer K at least its random finite cone constant. Then every s_n lies in D_U∩A_{K,T}, a finite set by Lemma 3. This contradicts their pairwise distinction. It also handles escape to negative infinite time: the cone in Lemma 3 extends over the entire past. Since the event was fixed before choosing the hypothetical orbit, the argument excludes every orbit simultaneously. ∎

Corollary: every forward orbit is eventually a two-cycle. Indeed absence of an injective forward orbit forces a repeated vertex; determinism of f makes the subsequent orbit periodic. Lemma 1 precludes any finite cycle longer than two: on a cycle separation times cannot strictly decrease under f², so equality forces f²(s)=s. The formal endpoints already form a two-cycle.

## Theorem 5: localization of the unresolved part (b)

Almost surely, any hypothetical infinite injective inverse chain, after deleting a finite prefix, converges to a single point (x,τ)∈N. Its separation and meeting times approach τ from below and above. In particular an inverse chain with a positive limiting time gap is impossible.

**Proof.** A chain has at most two formal endpoints; delete a prefix containing them and, if necessary, one further vertex. Write the remaining chain as

   s_0,m_0,s_1,m_1,...,
   f(m_n)=s_n and f(s_{n+1})=m_n.

All vertices are finite. Lemma 1 applied to s_{n+1} gives a_n≤a_{n+1}; applied to m_{n+1} gives b_{n+1}≤b_n. It also shows that s_n is an ancestor of s_{n+1}. The backward paths defining f(m_n)=s_n give a path from s_n to m_n. Concatenation therefore makes every chain vertex a descendant of s_0.

We have a_n<b_n, and indeed a_n<b_m for every n,m: at index k=max(n,m), monotonicity gives a_n≤a_k<b_k≤b_m. Consequently a_n increases to a finite α and b_n decreases to a finite β with a_0≤α≤β≤b_0. The descendants' spatial bound in Lemma 2 traps every vertex in a fixed compact rectangle.

If α<β, choose rational U∈(α,β). For n≥1, s_n has time a_n≤α<U and f(s_n)=m_{n−1} has finite time b_{n−1}≥β>U. Thus these distinct points all lie in D_U in a fixed compact rectangle at positive distance below U. Proposition 4.7 (or Lemma 3 after enlarging a cone) makes this set finite. Contradiction. Therefore α=β=τ.

To verify spatial convergence rather than just extract a subsequence, let ω be a uniform continuity modulus for complete backbone paths through s_0 on [a_0,b_0], whose existence follows from input 4 and the common spatial barriers. For m≥n, concatenate a path from s_0 through s_n to s_m and extend its future. Then

   |x(s_m)−x(s_n)|≤ω(a_m−a_n)≤ω(τ−a_n).

Thus x(s_n) is Cauchy. A complete path through s_0,s_n,m_n similarly gives

   |x(m_n)−x(s_n)|≤ω(b_n−a_n)→0.

Both spatial sequences converge to the same x. The closedness of N gives (x,τ)∈N. ∎

The converse is not asserted: arbitrary small bubbles approaching a point need not form an inverse chain. Nor does eventual two-cycling of all forward orbits exclude infinitely deep trees of preimages.

## Corollary 6: the remaining limit time must be exceptional

Any limit (x,τ) in Theorem 5 has x as a cluster point of the backbone time slice ξ_τ. Moreover the set of possible inverse-chain limit times has Hausdorff dimension at most 1/2, using the independently retrieved related theorem of R. Kou, arXiv:2512.10761v1, Theorem 1, PDF page 2. This is an application of that theorem, not an exact solution in the literature.

**Proof.** The endpoint monotonicities are strict in an injective chain, by the equality clause in Lemma 1. Thus a_n<τ<b_n for every n. Let l_n,r_n be the extreme forward branches from s_{n+1} until their first reunion m_n. At τ they are distinct and both belong to the backbone. Concatenate their pasts to a path through s_0. The common uniform continuity modulus from Theorem 5 gives

   |l_n(τ)−x(s_{n+1})|≤ω(τ−a_{n+1}),
   |r_n(τ)−x(s_{n+1})|≤ω(τ−a_{n+1}).

Both tend to x, while l_n(τ)<r_n(τ) for every n. If only finitely many time-slice coordinates occurred near x, eventually both coordinates would have to equal x, a contradiction. Thus x is a cluster point of ξ_τ.

Choose an integer q<a_0. All these complete paths through s_0 have restrictions starting at q, and hence their positions at τ also belong to the point-set process started from the whole line at time q. Restriction stability follows immediately from the net path characterizations. Thus τ is a special time for that deterministic-q process. Kou's Theorem 1 says that the set of such times for the process started at 0 has dimension 1/2 almost surely. Time translation gives the same result for each integer q simultaneously. The set of all candidate limit times is contained in the countable union of these sets, so its Hausdorff dimension is at most 1/2. ∎

In particular a prescribed deterministic time cannot be a limit time almost surely, since the backbone slice at that time is a locally finite Poisson process. The quantifier does not extend to all random times. Applying Proposition 4.7 at the random terminal horizon U=τ would be invalid without an additional theorem; its deterministic-horizon local finiteness alone does not give the required uniform event.

For a purely functional boundary test, take symbols s_n,m_n for n≥0, with times −2^(−n), +2^(−n), respectively. Set f(s_0)=m_0, f(m_n)=s_n for all n, and f(s_n)=m_{n−1} for n≥1. Every forward orbit reaches the two-cycle s_0,m_0, all the f² time inequalities hold, yet s_0,m_0,s_1,m_1,... is an infinite injective inverse chain with times collapsing to zero. This is NOT a Brownian-net counterexample; it proves that forward termination and the temporal inequalities alone cannot close the remaining gap.

## Hostile-referee checks and limitations

- **Density input at −∞ is load-bearing.** Proposition 4.7 explicitly permits −∞ and ∞; its factor Ψ(∞)=2 gives R_{−∞,U} density 4Ψ(U−t) and permanent separation density 8. Using a finite start time here without a proved limit would invalidate Theorem 4.
- **Subtraction cannot be ∞−∞.** It is done first on bounded sets at positive distance from U with finite expectations, then extended by monotone convergence. The cone has an explicit cutoff T<U. This avoids the h↓0 singularity as well.
- **Finite versus permanent.** A finite forward orbit image puts each s_n in the set difference. Counting all relevant separations, including permanent ones, over an infinite cone would have infinite expectation and prove nothing.
- **Ancestry is essential.** Lemma 1 proves it using extreme histories through m, and the image-set property legitimizes concatenation. Merely monotone times, without the spatial ancestral cone, would not exclude escape in space.
- **Backward containment.** It is containment by extremes of the reversed backbone collection. A dual-net path cannot be substituted. Reversibility applies to the complete path collection, not merely a one-time Poisson marginal.
- **Random-vertex quantifiers.** The barrier and cone arguments use countably many deterministic paths, horizons and integer constants, then cover all vertices. No assertion proved only at a deterministic starting point is silently used at a random separation.
- **No uniform bound on inverse depth was inferred.** Theorem 4 proves finite orbit length for each point, not a uniform bound over a compact set and not local finiteness of all complexity classes.
- **Compactness in Theorem 5.** It is used only after common finite spatial barriers are established on a finite interval; compactified equicontinuity alone at spatial infinity would be insufficient.
- **Remaining failure mode.** An infinite injective inverse chain can still have a_n↑τ and b_n↓τ. The density of separations of duration h behaves singularly as h↓0. Our finiteness estimate has no uniform bound as the cutoff approaches τ. Classification of the limiting point has not supplied a contradiction.

## Computation and formal verification

`checks.py` generates 1,000 finite planar directed graphs, each with 100 single split/merge events on ordered strands and explicit boundary vertices. It computes forward and backward extreme first reunions directly. These are finite combinatorial stress tests, not Brownian-net samples and not evidence of continuum tightness. Results: 50,138 finite f² temporal checks and 50,138 ancestry checks passed; 44,088 detected cycles had length two; maximum transient length observed was 7. Values of Ψ(h)−2 at h=.01,.1,1,2,5,10,20 were positive and below the exponential upper bound. Raw results are in checks_results.json.

The first graph implementation appended edges in event-creation order instead of spatial strand order and failed a temporal inequality. This was a test-generator error: children of a split can receive events in either time order. The corrected implementation fixes left/right child slots at split creation and fills each slot when that strand next encounters an event. The rerun passed all checks. This correction and the failed first run are retained here; no claim relies on the faulty run.

`TemporalSqueeze.lean` formalizes the exact algebraic squeeze used in Theorem 5: monotone a, antitone b and a_n<b_n imply a_n<b_m for all n,m, and all endpoints stay in [a_0,b_0]. It imports only Real.Basic and Monotone.Basic, contains no sorry, no axioms beyond the imported theory, and no native_decide. It does not formalize the Brownian-net inputs or the probabilistic proof. Compiler outcome is recorded in lean_check.log after completion.

## Precise remaining task

Exclude, or construct with positive probability, an injective inverse f-chain converging to a finite backbone point with zero limiting time gap. The source statement asks for absence of even one such chain on a probability-one event. Theorems 4 and 5 do not settle that event. No candidate counterexample in the Brownian net has been established.


## Second serious attempt (2026-10-12)

See SECOND_ATTEMPT.md for two new approaches, complete proofs of the common-bottleneck reduction and one-sided scalar-excursion reduction, and an explicit infinite deterministic planar ladder. The ladder has an infinite inverse chain despite trivalence, planarity and a compact Lipschitz complete-path family. It is NOT a Brownian-net counterexample; it shows precisely why a purely geometric completion of the one-sided reduction fails. Part (a) survives the new audit. Part (b) remains unproved: the missing issue is the probability of an infinite backward-compatible excursion ladder in the actual Brownian-net law, including two-sided Cn limits.

The second attempt also computes the exact finite-return duration intensity nu(dh)=(2/sqrt(pi))exp(-h)h^(-3/2)dh. Consequently any hypothetical inverse-chain widths are p-summable for all p>1/2 and decrease faster than n^(-2+epsilon) for every epsilon>0. Complete proofs and the rapid-collapse obstruction are in SECOND_ATTEMPT.md, Result B1.
