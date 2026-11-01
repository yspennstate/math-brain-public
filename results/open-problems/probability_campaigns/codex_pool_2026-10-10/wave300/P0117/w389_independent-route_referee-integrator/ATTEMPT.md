# P0117 independent route — initial commitment

2026-10-10. Written before opening w387/w388 mathematical artifacts.

Candidate method: derive a stationary mass-transport obstruction from the spatial density of vertices lying on bi-infinite geodesics. Study what an absence-of-density or bottleneck estimate would have to prove, and separate deterministic compactness from probabilistic control. The immediate difficulty is ruling out a positive-density stationary family without assuming every selected geodesic has a deterministic asymptotic direction. I will compare this boundary with recorded local routes before fixing a disjoint lemma.

No parent-problem proof or current-openness claim is made. Precise source hypotheses and previous routes are being checked.

## Elementary hypothesis counterexample

Claim C01: a universal assertion over all iid nonnegative laws is false. If every edge of Z^2 has weight 1, every horizontal line is a bigeodesic: a path from (m,0) to (n,0) needs at least |n-m| steps, and the horizontal segment attains that value. A non-atomic or other explicit exclusion is necessary. This is an elementary known boundary example, not a novel solution to P0117. Independent review is assigned to w392 and remains pending.

## Fixed route: finite-box congestion and stationary density

This follows the initial density/mass-transport commitment. It avoids choosing a random direction or choosing one infinite path per vertex. The recorded P0117-A001 approach tried to anchor geodesics between opposite axial endpoints; this route counts all boundary-to-boundary geodesics and does not infer an anchor for such a prescribed pair.

Assume a translation-stationary measurable field of finite nonnegative edge weights on the nearest-neighbor graph Z^2. All paths in the following definitions are self-avoiding, and geodesic means minimizing against ALL finite lattice paths between the endpoints, with no box restriction. Neither independence, uniqueness nor a moment bound is needed for this reduction.

Let B_n=[-n,n]^2 intersect Z^2 and let partial B_n={v: ||v||_infinity=n}. Let A be the set of vertices on some self-avoiding bigeodesic and p=P(0 in A). Define H_m(v) as the existence of a globally minimizing simple path (z_-m,...,z_m) with z_0=v. Define D_n as the vertices in B_n on at least one globally minimizing simple path between two vertices of partial B_2n. D_n is the union over ALL such paths; paths may leave B_2n.

### Claim C02: exact congestion-density identity (author proof; review pending)

For every n>=1,

    p <= E|D_n|/|B_n| <= P(H_n(0)),
    P(H_n(0)) decreases to p,
    lim_n E|D_n|/|B_n| = p.

Consequently absence of all bigeodesics almost surely is equivalent to E|D_n|=o(n^2). This is a reduction, not a proof that the o(n^2) bound holds for iid continuous weights.

Proof, including the compactness step:

1. Every subpath of a finite geodesic is a geodesic: replacing a non-minimizing subpath by a shorter competitor would lower the whole path's passage time. A resulting walk with repetitions is still an admissible competitor; alternatively erase its nonnegative loops. Thus H_(m+1)(v) is contained in H_m(v).
2. The finite globally minimizing simple centered paths form a rooted prefix tree, where deletion of the first and last vertex is the parent operation. There are finitely many possibilities at each level, since a centered path of 2m steps lies in a finite graph-distance ball. On the intersection of all H_m(v), this finitely branching tree has nodes at arbitrarily high levels. König's argument chooses an infinite branch (at each level retain a child with arbitrarily deep descendants). The branch gives a path indexed by Z, with all vertices distinct because any pair lies in a finite simple prefix. Every finite segment lies in one minimizing prefix and is therefore minimizing. This proves {v in A}=intersection_m H_m(v). All events are measurable: finite paths are countable and minimization is the comparison with countably many finite competitor paths. Continuity of probability from above gives P(H_m(v)) decreasing to P(v in A).
3. If v in A intersect B_n, both rays of its simple bigeodesic leave every finite set. Take the first hit of partial B_2n on each ray. The intervening segment is a finite geodesic containing v, so A intersect B_n is contained in D_n.
4. If v in D_n, each endpoint x on partial B_2n has ||x-v||_infinity>=n. Each arm of the chosen simple geodesic therefore has at least n steps. Truncating each arm to n steps witnesses H_n(v). Hence D_n is contained in {v in B_n: H_n(v)}.
5. Take cardinalities, expectations and use translation stationarity. This yields the two inequalities. Step 2 and the squeeze theorem yield the limit. If p=0, every lattice vertex has probability zero of lying on a bigeodesic, so a countable union rules out every bigeodesic. If the expected density tends to zero, the lower inequality gives p=0. The reverse implication follows from the upper inequality. No multiplication of conditional probabilities and no exchange of an uncountable union with probability occurs.

### Single hardest unresolved step

Prove E|D_n|=o(n^2) for the target iid atomless law, or prove a quantitatively sufficient estimate that implies it. A theorem for paths started at ONE origin does not automatically control the union over order-n boundary starting vertices. Boundary crossing counts alone also do not suffice: the stationary family of horizontal lines for weight 1 has O(n) components crossing a box and occupies every one of its order-n^2 vertices.

### Own-claim audit request

w392 is the designated independent referee for C01/C02. The compactness step, global-vs-confined minimization, treatment of ties, and the two set inclusions are the requested audit boundary. Until a receipt arrives, C02 stays author-checked draft material. No novelty claim is made for this elementary reformulation.

## Claim C03: the proposed shell-decay goal is impossible

This arose while auditing w388's ATTEMPT.md, C03. Let T_0 be the union of all infinite simple geodesic rays from 0; let q(x)=P(x in T_0); and S_n={x: ||x||_infinity=n}. Every simple infinite ray from 0 leaves B_(n-1), so it contains a vertex of S_n. Thus, without a stationarity assumption,

    sum_(x in S_n) q(x) = E|T_0 intersect S_n| >= P(T_0 is nonempty).

If a ray exists from 0 almost surely, the shell sum is >=1 for EVERY n. Since |S_n|=8n, sup_(x in S_n)q(x)>=1/(8n). Vanishing shell sum along a subsequence, or the uniform rate o(1/n), is then impossible.

Standard iid atomless finite weights admit such rays. One elementary justification is: positivity and iid give, for sufficiently large c, 4 E exp(-c t_e)<1. For any fixed K, a union bound over simple paths of length j and Markov's inequality bound the probability of a path of cost <=K by exp(cK)*(4 E exp(-c t_e))^j. Borel-Cantelli implies only finitely many simple paths from any fixed vertex have cost <=K. Compare against a fixed finite connecting path to obtain finite minimizers; take geodesics from 0 to vertices escaping to infinity and extract an infinite prefix branch in the finitely branching geodesic tree. This establishes a ray from 0. The lower-bound argument itself needs only existence of a ray, not this auxiliary iid proof.

The incidence inequality in w388 C03 is still correct:

    P(bigeodesic through 0) <= (1/2) sum_(x in S_n) q(-x).

But its proposed vanishing right side is an unattainable premise in this setting. The published uniform q(x)->0 theorem cannot fix that route by improving the rate to o(1/n). A useful replacement must count genuinely two-sided extension witnesses, or return to the full boundary-geodesic occupation D_n criterion, rather than count the unavoidable forward ray exits. This is an elementary audit scar, not a solution or novelty claim. Independent reviewer w392 remains requested.

Independent audit receipt, 2026-10-10: w392 KEEP for C02 and C03; exact receipts in AUDIT_RECEIPTS.jsonl. Relation wording fix applied in bundle_002.json. The iid estimate E|D_n|=o(n^2) is still the hardest missing step; no full P0117 solution is claimed.
