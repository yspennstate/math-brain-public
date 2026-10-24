# P0117: deleted-edge threshold route

Author w384, 2026-10-10. Independently checked proof: **none yet**. Current openness and novelty: **UNKNOWN**. This packet proves reductions and a non-explosion lemma; it does not prove absence of bigeodesics.

## Exact working target and source scope

On the undirected nearest-neighbor graph Z^2 let (t_f) be iid finite nonnegative weights with nonatomic distribution F. A finite geodesic minimizes the sum of its edge weights among all finite paths between its endpoints. A bigeodesic is an injective sequence (v_i) indexed by Z, with adjacent consecutive vertices, whose every finite subpath is a finite geodesic. The target rules out all such paths simultaneously, almost surely; it does not merely rule out a prescribed direction. For the standard moment-restricted formulation also assume E[min(t_1,t_2,t_3,t_4)^2] < infinity. No shape curvature or differentiability is assumed. Nonatomicity implies t_f>0 almost surely.

The dated ranking is not a complete statement. The exported original P0117 card identifies Auffinger-Damron-Hanson, 50 years of first-passage percolation, Section 4.5, Question 31: "Do geodesic lines exist?" The card's page-98 locator differs from the current public PDF's page index 85. The original campaign registry path has disappeared. SOURCE_STATUS.json therefore distinguishes that broader recorded question from the exact min-of-four moment formulation pinned in Ahlberg-Hanson-Hoffman Section 2.4 (A1) and in the September 24, 2026 primary manuscript's Theorem 1.1. The latter manuscript claims the full moment-restricted result; its whole proof has not been audited here. STATEMENT_FOR_ADVERSARY.md was saved before this route was sent. The reduction below needs no upper-tail moment assumption, and no new-theorem novelty is certified. The newer manuscript's Lemma 2.1 also gives a moment-free finite-minimizer proof.

## Prior attempt digest

The 2026-09-07 rank-sheet row 116 for P0117 records the compactness approach with endpoints -n e_1 and n e_1. Its identified missing input is that the geodesics remain anchored in a fixed bounded set. Endpoints going to opposite infinity alone do not provide that anchor. Here the anchor is a fixed edge e; we do not assume that it is used at arbitrarily large scales. Fixed-direction exclusion and fixed-endpoint midpoint decay leave the simultaneous random-path assertion unproved.

## Lemma 1: properness without an upper-tail moment

Assume iid finite positive edge weights on Z^2. There exist deterministic delta>0 and rho<1 such that, for each vertex x and n>=1,

P(there exists a simple n-edge path from x of weight <=delta n/2) <= (4/3) rho^n.

Proof. Choose delta with p=P(t_f<=delta)<1/144; this is possible because P(t_f=0)=0. A path with weight <=delta n/2 must have at least ceil(n/2) edges of weight <=delta. Its edges are distinct, so their weights are independent. Summing over subsets gives probability at most 2^n p^{n/2}. There are at most 4*3^(n-1) simple n-edge paths from x. The union bound gives rho=6 sqrt(p)<1/2. No independence between different paths is asserted or needed.

The sum over n converges. Borel-Cantelli and a countable intersection over x imply that almost surely, for every x, all sufficiently long simple paths from x have weight >delta n/2. Hence bounded passage-time balls are finite. For each x,y a deterministic finite path has finite weight; all paths with cost no larger have bounded length, so the infimum is attained among finitely many simple paths. Every finite modification of positive edge weights preserves this conclusion: a simple path uses each modified edge at most once, so its cost changes by at most the finite sum of absolute changes. Deleting an edge preserves the lower bound; deleting one edge leaves Z^2 connected. Therefore the deleted-edge metric and every positive replacement of that edge have finite geodesics and finite metric balls. This is an author proof awaiting independent review, not a formal-check receipt.

## Lemma 2: exact single-edge metric formula

Fix an edge e={u,v}. Condition on all weights other than t_e. Let d be passage time on the graph with e deleted. Work on an outside environment with all positive weights, finite d, and finite d-balls, as supplied by Lemma 1. Give e a variable weight s>0 and write T_s for the resulting metric. Define

c_e(x,y)=min{d(x,u)+d(v,y), d(x,v)+d(u,y)},

D_e(x,y)=d(x,y)-c_e(x,y).

Then for all vertices x,y and s>0,

T_s(x,y)=min{d(x,y), s+c_e(x,y)}.

Proof. A simple minimizing path either avoids e, or traverses it exactly once in one of the two orientations. Its e-free pieces cost at least the relevant d-distances, giving the lower bound. Conversely concatenate minimizing e-free paths with e; these are allowed walks. Removing cycles cannot increase their weight and gives the reverse bound. Positive weights and properness guarantee attainment. If s<D_e(x,y), every minimizing path traverses e; if s>D_e(x,y), no minimizing path traverses e. Equality permits a tie, and will be excluded probabilistically rather than ignored.

Triangle inequalities for d give D_e(x,y)<=d(u,v). In particular all positive thresholds are bounded by a finite e-free detour cost.

## Lemma 3: decreasing boundary capacity and two-sided compactness

Let B_n={x:||x||_infinity<=n}, S_n={x:||x||_infinity=n}, and take n large enough that u and v are strictly inside B_n. Define the outside-measurable quantity

H_n=max{0, max_{x,y in S_n} D_e(x,y)}.

For s>0, s<H_n if and only if some pair x,y in S_n satisfies T_s(x,y)<d(x,y). Such a geodesic uses e strictly in preference to every e-avoiding route.

H_(n+1)<=H_n. To prove this without assumptions about independence, let 0<s<H_(n+1), and take a strictly e-using geodesic between S_(n+1) endpoints. Orient it through u,v. On each arm, take the first S_n vertex encountered when going outward from e. The intervening subpath is a geodesic. If it had an e-avoiding competitor of equal or smaller weight, replacing it in the outer path would yield an e-avoiding outer walk of no greater weight; cycle removal would contradict the strict preference for e. Thus s<H_n. Since this holds for every positive s<H_(n+1), the clipped thresholds are decreasing. They lie in [0,d(u,v)], so H_infinity=lim_n H_n exists and is outside-measurable.

If for every n there is a geodesic through e between S_n endpoints in the actual environment, then a bigeodesic through e exists. Orient all these geodesics from u to v. Both arms have arbitrarily many edges because their endpoints escape every finite lattice ball. At each fixed arm length there are only finitely many possibilities, since the lattice has degree four. A diagonal subsequence stabilizes both arms at every length. The limiting doubly infinite path is injective: any repeated vertices would occur in one of the finite stabilized simple geodesics. Every finite subpath is a geodesic because it is eventually exactly a subpath of those geodesics. Conversely every bigeodesic through e meets every S_n on both arms and yields such finite subpaths. Thus anchored compactness is proved; existence of the anchors is not.

## Proposition 4: conditional bigeodesic probability

Suppose additionally t_e is independent of the outside environment and has nonatomic distribution F, with P(t_e>0)=1. Let A_e be the event that a bigeodesic traverses e. Then, modulo a null set,

A_e={t_e<H_infinity},

P(A_e | sigma(t_f:f!=e))=F(H_infinity),

P(A_e)=E[F(H_infinity)].

Proof. Each H_n and H_infinity depends only on the outside environment. Independence and nonatomicity give P(t_e=H_n)=P(t_e=H_infinity)=0, including the countable union over n. Off this null set, Lemma 2 identifies the boundary geodesic event with {t_e<H_n}. Their intersection is {t_e<H_infinity}, with a possible limiting equality already removed. Lemma 3 identifies that intersection with A_e. Conditional expectation now integrates precisely one independent weight; it does not multiply any conditional per-scale probabilities. F may be singular continuous; no density is assumed. Standard iid FPP finite-path uniqueness holds off a null set, but the strict-inequality argument above does not need it.

Let a=essential infimum of t_e. Since F is nonatomic and positive weights are finite, F(h)=0 exactly when h<=a, for h>=0. It follows that P(A_e)=0 if and only if H_infinity<=a almost surely. Taking the countable union over lattice edges and the two translation classes gives the full no-bigeodesic conclusion if this holds for both orientations. The iid isotropic model identifies their laws by lattice rotation.

## Lemma 5: lowering one edge produces a uniform bypass penalty

Suppose a positive proper metric contains a bigeodesic gamma through e of weight t_e, and replace only that weight by s with 0<s<t_e. The same gamma is a bigeodesic in the new metric. For any finite gamma segment with endpoints on opposite sides of e, every e-avoiding competitor exceeds that segment's new cost by at least t_e-s.

Proof. Any such straddling segment decreases in cost by Delta=t_e-s. A simple competitor either avoids e, and has unchanged cost, or uses it once, and decreases in cost by exactly Delta. Since the original segment was minimizing, it stays minimizing after replacement; avoiding competitors have the asserted penalty. For an arbitrary gamma subsegment on one side, extend it in gamma to a finite straddling segment. The latter is minimizing in the new metric, so each of its subsegments is minimizing. This proves the entire doubly infinite assertion, including subsegments not containing e. It uses neither independence nor a density assumption.

A legitimate probabilistic use is available. If P(A_e)>0 in the iid nonatomic model, continuity gives numbers a<b<c with P(A_e and t_e>=c)>0 and F(b)>0: these follow by countable exhaustion of the positive t_e-a gap. Draw a new edge weight s independently with law F. On the event s<=b and A_e with t_e>=c, the unchanged bigeodesic has a uniform bypass penalty at least c-b. This event has probability F(b)*P(A_e and t_e>=c)>0, because the new draw is independent. Resampling one iid coordinate leaves the environment's marginal law unchanged. Thus absence can be reduced to excluding, under the original iid law, a bigeodesic pinned at a fixed edge by some strictly positive uniform bypass penalty. This multiplication is justified by the explicitly fresh independent draw, not by the geometry of the selected path. For a fixed epsilon>0 the strict-pinning event is measurable: it is equivalent to H_n>=s+epsilon for every n. The outer-to-inner replacement argument shows that an inner bypass excess is at least the outer excess, so the same two-sided diagonal extraction retains the penalty for every finite straddling segment. Conversely a pinned bigeodesic supplies boundary witnesses on every scale. The lemma does not show that such a pinned path is impossible.

## The single hardest remaining gap

**Support-collapse lemma, UNPROVED:** For the outside environment of iid nonatomic planar FPP in the exact target regime, H_infinity<=a almost surely.

This is an equivalent reformulation of the hard part of P0117, not a theorem secretly supplied by compactness. The packet does not show it. Propositions 2-4 and Lemma 1 remain useful even if P0117 is already settled in a newer source.

Geometric version for the attempted finite-energy route: exclude a bigeodesic whose every straddling segment has an e-avoiding bypass penalty bounded below by one fixed epsilon>0. Lemma 5 legitimately upgrades any positive-probability existence claim to this strict-pinning event. No planar argument eliminating strict pinning is proved here; this is the same remaining input, not a second claimed theorem.

## Substantive attempt on support collapse

1. The finite-energy step succeeds in Lemma 5: resample exactly one independently chosen edge and retain the entire bigeodesic with a strictly positive, uniform bypass penalty. A completion would need a planar delocalization or label argument excluding those strictly pinned bigeodesics. Local detours give only H_infinity<=d(u,v), generally far above a, and do not yield decay with n.
2. First-order shape estimates control d(x,y) and c_e(x,y) at order n. Their difference D_e(x,y) is bounded at order one by the local detour. The order-n terms can cancel for opposite directions, while the known error is much larger than the desired order-one threshold. The shape theorem alone does not prove D_e(x,y)<=a uniformly over selected endpoints.
3. Fixed endpoint midpoint bounds control each individual event. There are |S_n|=8n boundary vertices and at most 64n^2 ordered pairs. A uniform bound p_n would give P(A_e)<=64n^2 p_n. Qualitative p_n->0, or the known small polynomial exponents under extra hypotheses, does not make this quantity vanish. This very strong sufficient union-bound rate is not claimed available or plausible.
4. Trying to choose only one promising endpoint pair after seeing the outside environment does not remove this loss: the selected event has the maximum threshold H_n. A bound for each deterministic pair does not transfer to an environment-selected pair. Conditioning on the outside is useful because it preserves independence of t_e, not independence among different endpoint capacities or across scales.
5. A putative repeated-barrier proof would need a uniform lower bound on a barrier's failure probability conditional on a stated filtration before multiplying survival bounds. Revealing the optimizing endpoints or an entire geodesic can bias the unopened corridors. No such valid filtration estimate has been supplied here. The exact residual lemma remains support collapse, rather than an unsupported product of per-scale bounds.

## Boundary controls and verification limits

For constant weights c>0, any horizontal lattice line is a bigeodesic; the bare iid title is false. For e={(0,0),(1,0)} and x=(-n,0), y=(n,0), deleting e makes d(x,y)=(2n+2)c and c_e(x,y)=(2n-1)c, so D_e(x,y)=3c. Also d(u,v)=3c, hence H_n=H_infinity=3c. This confirms that local properness and planarity alone cannot force support collapse. This atomic control is outside the target assumptions, and the nonatomic equality argument must not be applied to it as though it were a target counterexample.

Finite graph checks can test the metric formula, strict threshold classification, boundary monotonicity, tie handling, and the atomic control. They cannot establish an infinite-volume limit, certify novelty, or prove support collapse. MEASUREMENTS.json records the finite checks separately.
