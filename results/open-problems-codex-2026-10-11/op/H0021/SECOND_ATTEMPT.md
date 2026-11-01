# Second serious attempt — 2026-10-12

The remaining gap in ATTEMPT.md is simultaneous vertex-disjoint spanning completion at p=(1+ε)log n/n, already for Δ=3.

Two approaches not tried in the first attempt:

A. Expose a Hamilton cycle independently of a fresh sprinkle. For a three-arm spanning spider, split the longest arm into two cycle intervals and connect them by two fresh chords, with both chord lengths varying with the split. Extract many candidates using pairwise disjoint fresh edge sets. If successful, pursue the construction beyond one branch vertex and count the limitations of a fixed cycle skeleton.

B. Upgrade the adaptive k-neighbor reservoir to a capacitated Hall reservoir by jointly repairing deficient sets rather than isolated demands. Look for an augmenting-path/alternating-tree invariant that also maintains Montgomery extendability. This would address multiple demands competing for the same reservoir vertices, but requires choosing the unused set compatibly with the old embedding; merely proving domination is insufficient.

Selection: A is more promising for this round because it has a concrete finite construction and a uniform probability estimate to test. B remains a research proposal, not a proof or claimed reduction.

Brain query (read-only): math_recall.py "spanning tree absorption extendability Montgomery rollback completion bounded degree random graphs". It returned generic random-tree and spanning-tree discrepancy cards, no completion theorem or directly relevant absorption lemma. In particular none of these cards is being imported as a solution.

## Working calculation: two variable chords
Cycle vertices are Z/nZ in forward order. A spider has positive arm lengths a,b,c, with a+b+c=n−1, and c the longest. Fix center v and split integer 2≤t≤c−1.
Retain the cycle path from v−a to v+b through v. The other c vertices are the two intervals
[v+b+1,...,v+b+t] and [v+b+t+1,...,v−a−1].
Add chords {v,v+b+t} and {v+b+1,v+b+t+1}.
The third arm visits the first interval backwards, then the second forwards; its length is c. All arithmetic is modulo n. Need to check that all vertices are distinct, both added edges are distinct non-cycle edges, and no vertex other than v has degree 3.

Probability idea: for each fixed spider there are n(c−2) candidates. Each unordered possible chord occurs in at most four candidates (two orientations in each of the two chord roles). A candidate conflicts with at most six others. Greedy selection therefore gives at least n(c−2)/7 candidates with pairwise disjoint two-edge sets. Independent sprinkle success probability q² for each would give exp(−Ω(n²q²)) failure. At q≈ε log n/(2n), this beats a union bound over O(n²) spiders. These assertions must be written and checked fully before being marked proved.
## Theorem A: sharp-density universality for at most three leaves
For every fixed ε>0, whp G(n,(1+ε)log n/n) simultaneously contains every n-vertex tree with at most three leaves. No novelty is claimed; the theorem is a special case of the target, not its solution.

### Proof, including the finite construction
Write C for any fixed Hamilton cycle on n≥28 vertices, labeled in its cyclic order by Z/nZ. Fix positive integers a,b,c with a+b+c=n−1, choosing c≥max(a,b). Let S(a,b,c) be the spider formed by three paths of lengths a,b,c sharing only their first vertex. For each v∈Z/nZ and t∈{2,...,c−1}, define the following three vertex sequences:
A=(v,v−1,...,v−a),
B=(v,v+1,...,v+b),
D=(v, v+b+t,v+b+t−1,...,v+b+1, v+b+t+1,v+b+t+2,...,v+b+c).
All residues are taken modulo n. The last term v+b+c equals v−a−1 modulo n.

The sequence from v−a through v to v+b is a contiguous arc with a+b+1 vertices. The complementary arc has exactly c vertices, with consecutive offsets b+1,...,b+c from v. The two parts of D partition this complementary arc into intervals of sizes t and c−t. Both are nonempty, and neither overlaps A or B except that all three arms start at v. The endpoints of A and B are distinct because a+b<n. Thus the arms together visit every vertex exactly once apart from the common center, and their union is a connected acyclic spanning tree with arm lengths a,b,c. Specifically, the third arm has 1+(t−1)+1+(c−t−1)=c edges.

Every edge used is an edge of C except the two chords
E_1(v,t)={v,v+b+t},
E_2(v,t)={v+b+1,v+b+t+1}.
For E_1, its forward difference b+t lies between 3 and b+c−1=n−a−2≤n−3. For E_2, the forward difference is t∈[2,c−1]⊆[2,n−4]. Neither edge is a loop or a cycle edge. They are distinct: a common unordered edge would require either v=v+b+1, which is impossible since 2≤b+1<n, or v=v+b+t+1, which is impossible since b+t+1≤b+c=n−a−1<n. These bounds are ordinary integers before reducing modulo n, so no modular wrap-around case is omitted.

There are N=n(c−2) labeled candidates (v,t). For any fixed unordered host edge e={x,y}, it occurs in at most two candidates in role E_1: assign either endpoint as v and the other as v+b+t; that determines t uniquely modulo n, and the allowed interval for t has length less than n. It also occurs in at most two candidates in role E_2: assign either endpoint as v+b+1 and the other as v+b+t+1, again determining v and t uniquely. Thus e belongs to at most four candidates in total, including possible repeated two-edge sets with different candidate labels.

Construct a conflict graph on the N candidate labels, joining candidates if their chord sets intersect. For each of a candidate's two distinct edges, at most three other candidates contain that edge, so its conflict degree is at most six. Repeatedly choose one remaining candidate and delete it together with its neighbors. Each choice deletes at most seven candidates, so the chosen family has m≥N/7 members and its two-edge sets are pairwise disjoint. This is a deterministic extraction from C,a,b,c, independent of any subsequent sprinkle.

Since c≥(n−1)/3 and n≥28, c−2≥(n−7)/3≥n/4. Hence m≥n²/28.

Let R∼G(n,q) be independent of C. Each selected candidate has its two required chords in R with probability q². These m success events are mutually independent because their edge sets are disjoint; sharing a vertex does not spoil edge independence in G(n,q). Therefore
P(C∪R contains no copy of S(a,b,c))
≤(1−q²)^m≤exp(−n²q²/28).
The event on the left could fail to be captured by our particular construction only in the favorable direction: another embedding can exist even if all selected candidates fail. Thus the inequality has the correct direction.

There are at most n² positive ordered arm-length triples summing to n−1. Every triple can be relabeled so that the longest arm is c. A union bound gives, uniformly over the chosen cycle C,
P(C∪R misses some n-vertex three-arm spider)≤n²exp(−n²q²/28).
A Hamilton cycle already contains a spanning path.

Now put p=(1+ε)log n/n and p_1=(1+ε/2)log n/n, and sample independent G_1∼G(n,p_1), R∼G(n,q), where
q=(p−p_1)/(1−p_1).
For sufficiently large n these are valid probabilities. Their union has exactly the G(n,p) distribution, since 1−(1−p_1)(1−q)=p edge by edge. Also q≥(ε/2)log n/n. The primary Hamilton-cycle theorem already checked in ATTEMPT.md §1 implies G_1 is Hamiltonian whp. On that event choose a Hamilton cycle C by a fixed deterministic rule depending only on G_1. Conditional on G_1, R remains an independent binomial graph. The preceding estimate applies to every possible C, with no union bound over Hamilton cycles and no conditioning on R.

Thus the probability the union misses a spider is at most
P(G_1 is not Hamiltonian)+n²exp(−ε²(log n)²/112)=o(1).

Finally, for any tree T on n≥2 vertices, the degree sum gives
sum over nonleaf v of (deg_T(v)−2) = number_of_leaves(T)−2.
Indeed deg_T(v)≥1 for every v, there are n−1 edges, and subtracting 2n from the degree sum 2n−2 gives this identity after moving the −1 contribution of each leaf to the right. All summands on the left are nonnegative integers. If there are two leaves, all other degrees equal 2 and T is a path, as proved in ATTEMPT.md. If there are three leaves, exactly one vertex has degree 3 and every other nonleaf has degree 2. Removing that vertex produces three unbranched paths ending at the three leaves, so T is S(a,b,c) for positive a,b,c. A tree with fewer than two leaves is impossible for n≥2 by the same identity. This classifies every target in the theorem and completes its proof.

The only external mathematical input is the explicitly sourced Hamilton-cycle theorem. The construction, extraction, independence estimate, union bound and tree classification are proved here. This result establishes simultaneous universality for a strictly larger family than the previous path-only special case, while leaving the full Δ=3 family unresolved.

## Referee audit of Theorem A
- Every candidate spans all n vertices and realizes exactly the prescribed arm lengths; the count does not merely produce a nonspanning subdivision.
- The two chords vary with the split. The total incidence bound is four per unordered edge, accounting for both orientations and both roles, even if candidates repeat.
- The extracted events use disjoint edge sets. No independence of events sharing chords is assumed.
- The extraction is done before inspecting R. Selecting C from G_1 preserves conditional independence of R.
- The probability bound is uniform over all arm lengths, including two arms of length 1. The third arm is always linear because it is chosen longest.
- “At most three leaves” does not mean “maximum degree at most three”: trees with two or more degree-3 vertices are not covered.
- The numerical checks corroborate the finite construction but are not used as a replacement for this proof. The Lean certificate verifies one finite disjoint packing, not the asymptotic theorem or all modular identities.
## Theorem B: a limitation of the fixed-cycle route
Fix d>0 and η∈(0,1). Let C be a predetermined Hamilton cycle on n vertices, let R∼G(n,q) with q=d log n/n be independent, and put K=floor((1−η)log n/log log n). Consider any n-vertex tree T having two distinct, nonadjacent degree-3 vertices. Then whp C∪R has no embedding of T using at most K edges outside C. This conclusion concerns embeddings with few non-cycle edges only; it is not a noncontainment statement for C∪R and is not a counterexample to H0021.

### Full proof
For an injective spanning embedding f of T into C∪R, let F⊆E(T) be the set of tree edges whose images are not cycle edges, and h=|F|. Every remaining edge lies in C. Thus T−F has maximum degree at most 2 and is a forest of h+1 path components (singletons allowed). Each of the two specified degree-3 vertices must be incident to an edge of F. Since they are nonadjacent, the two chosen incident edges are distinct. There are at most 3·3=9 ways to choose these two edges. Consequently, for a given h≥2, the number of possible F is at most
9 binom(n−1,h−2).
This overcounts sets with multiple choices of witnesses, which is harmless. For h=0 or 1 no embedding is possible.

For each admissible F, an embedding of the spanning path forest T−F into C maps each path component to a contiguous interval of the cycle: after the first path edge, a simple path cannot reverse along a degree-2 cycle without repeating a vertex. The intervals partition all n vertices. Choose a circular order of the h+1 labeled components, a direction for each component, and the starting position of the first component. These choices determine the entire mapping. They give at most
n (h+1)! 2^{h+1}
embeddings, with any multiplicity or redundant direction for a singleton merely increasing the bound.

We count only those mappings for which all h edges of F have images outside C. These images are h distinct unordered pairs because f is injective. They all must be present in R, which has probability q^h. Removing the restriction on F's images when bounding the number of mappings is valid; we retain the restriction when assigning probability q^h. Thus a union bound gives
P(∃ embedding with 2≤h≤K)
≤Σ_{h=2}^K 9 binom(n−1,h−2) n (h+1)! 2^{h+1} q^h.
Using binom(n−1,h−2)≤n^{h−2}/(h−2)! and q=d log n/n, the h-th term is at most
(18/n)(h−1)h(h+1)(2d log n)^h.
For sufficiently large n, 2d log n≥1 and K≥2, so the entire sum is at most
18 K^4 (2d log n)^K / n.
Write L=log n and ℓ=log log n. Its logarithm is at most
log 18+4 log K−L+K(ℓ+log(2d))
≤−ηL+O(L/ℓ)+O(ℓ)→−∞.
Hence the probability tends to zero, proving the claim. The estimate is uniform in the choice of T and C; T is allowed to depend on n but C is independent of R.

An explicit relevant example is T_n consisting of two degree-3 vertices connected by a path of length n−5, with two pendant leaves attached to each endpoint (n≥7). It has four leaves and maximum degree 3. The theorem says that embedding it into the fixed cycle plus sprinkle requires at least order log n/log log n non-cycle edges whp. In particular no extension of the two-chord proof using a bounded number of fresh chords can cover even this family.

The original random graph G_1 contains many edges in addition to the selected Hamilton cycle. Theorem B does not apply when those additional base edges are used, or when the Hamilton cycle is chosen after observing R. It exposes a limitation of the particular reduction rather than a limitation of the conjectured host.

## What remains after Theorems A and B
The path-only special case has been strengthened to every spanning three-leaf tree. The first missing structural family has two branch vertices, for which a fixed independent cycle and boundedly many fresh chords are insufficient. A genuine extension must vary the skeleton using further base edges, or allow a growing collection of reroutings while maintaining exact vertex and path-length constraints. The required growing scale log n/log log n agrees with the linking-depth scale in the source, but that agreement is a heuristic guide, not an implication establishing universality.
### Extension of the fixed-cycle barrier to b separated branch vertices
Fix an integer b≥2. If T_n has b pairwise nonadjacent vertices of degree 3, then, for any fixed d>0 and ζ∈(0,b−1), a fixed cycle plus independent G(n,d log n/n) whp has no embedding of T_n using at most
K=floor((b−1−ζ)log n/log log n)
non-cycle edges.

To check this extension rather than merely extrapolate Theorem B, select one deleted edge incident to each branch vertex. Nonadjacency makes the b witness edges distinct; at most 3^b choices suffice. For h≥b the number of deletion sets is therefore at most 3^b binom(n−1,h−b). Multiplying by the same spanning path-forest embedding bound and q^h gives the h-th probability contribution at most
2·3^b n^{1−b} [(h+1)!/(h−b)!] (2d log n)^h.
The factorial ratio has b+1 factors, each at most h+1. Summing h≤K gives at most
2·3^b n^{1−b} K(K+1)^{b+1}(2d log n)^K.
Its logarithm is at most −ζ log n+O_b(log n/log log n)+O_b(log log n), which tends to −∞. This proves the extension for every fixed b. It does not assert uniformity when b grows with n, nor simultaneous exclusion for all choices of T_n at once. The result reinforces the need for repeated rerouting or a skeleton selected using more of the original graph.
## Theorem C: a checked reduction to a stronger pre-existing special case
A subsequent primary-source search recovered Richard Montgomery, *Sharp threshold for embedding combs and other spanning trees in random graphs*, arXiv:1405.6560v1, submitted 26 May 2014. Theorem 1.2, page 2, states (verbatim mathematical transcription):
> “Let α, ε, ∆ > 0. The random graph G(n, (1 + ε) log n/n) almost surely contains a copy of every tree T ∈ T(n, ∆) which has at least αn/log^9 n disjoint bare paths with length ⌈log^9 n⌉.”

This is simultaneous universality for a restricted class. It already implies the three-leaf special case and substantially more. Theorem A is an independent elementary proof for spiders, not an improvement over the known special-case frontier. This literature theorem is NOT a solution to Conjecture 1.4, because many bounded-degree trees lack the specified bare paths. The theorem is used here as a published input, not reproved; primary PDF and page-marked text are montgomery_combs.pdf and montgomery_combs.txt.

### Explicit stronger corollary and full structural reduction
Fix ε>0 and integer ∆≥2. Let m=⌈log^9 n⌉. Then whp G(n,(1+ε)log n/n) is simultaneously universal for all n-vertex trees of maximum degree ≤∆ with at most n/[8(m+1)] leaves.

To prove the reduction, let T have l leaves and b vertices of degree ≥3. The degree-sum identity in Theorem A implies b≤l−2. Suppress all degree-2 vertices of T. The resulting graph is a tree: suppressing a degree-2 vertex replaces its two incident edges with an edge between its distinct neighbors, preserving connectedness and introducing no cycle (a new cycle would give an old cycle through the suppressed vertex). Repeating terminates with a tree on l+b vertices and hence l+b−1 edges. Its edges correspond to the maximal paths whose internal vertices had degree 2. Thus there are at most 2l−3 such segments. Their interior degree-2 vertices partition all n−l−b≥n−2l+2 degree-2 vertices of T.

Write their respective interior counts as r_i, and put M=l+b−1≤2l−3. On each segment, group its interior vertices consecutively into blocks of m+1 vertices, discarding a final shorter block. Each full block gives a path of length m, all of whose vertices have degree 2 in T; in particular it is a bare path. Blocks are vertex disjoint both within and between segments because endpoints of the suppressed kernel were excluded. Their number k satisfies
k=Σ_i floor(r_i/(m+1))
≥[Σ_i r_i−Mm]/(m+1)
≥[n−2l+2−(2l−3)m]/(m+1)
=(n−1)/(m+1)−(2l−3).
The first inequality follows by writing each r_i=(m+1)q_i+s_i, with 0≤s_i≤m; thus the discarded remainder in each segment is at most m. No disjointness convention for bare-path endpoints can invalidate this construction, because the whole vertex sets of the blocks are disjoint.

If l≤n/[8(m+1)], then
k≥(3n/4−1)/(m+1)+3≥n/(2m)
for m≥2. For the last inequality subtract n/(2m); the result is
n(m−2)/[4m(m+1)]+3−1/(m+1)≥0.
Put A=log^9 n. For A≥2, m=⌈A⌉≤A+1≤3A/2, so k≥n/(3A). Every target therefore satisfies the primary theorem with α=1/3, the same fixed ε, and the same fixed ∆. The primary theorem's one high-probability universality event covers all these targets; no union bound over individual tree probabilities is substituted. This proves the corollary.

This strengthens the recorded partial family to a growing, sublinear bound on the number of leaves, but is explicitly a corollary of a pre-existing theorem rather than a new full resolution.

### A precise remaining family not covered by this reduction
For integers l≥3, take any tree skeleton with l leaves and l−2 degree-3 vertices and no degree-2 vertices (for l≥4, form a chain of l−2 branch vertices, attach two leaves at each end and one at each internal branch vertex; for l=3, attach three leaves to a single branch vertex). It has 2l−2 vertices and 2l−3 edges. Replace every edge by a path of k edges. The resulting subcubic tree has
n=(2l−3)k+1,
exactly l leaves and l−2 branch vertices. Every maximal bare path has length k, since passing through a branch vertex would make a degree-3 vertex internal. Thus no bare path has length greater than k.

For example let l=j→∞ and k=floor(log j/log log j), restricting to sufficiently large j. Then log n~log j and log log n~log log j, so k~log n/log log n, and l~n/(2k). This family has no bare paths of length ⌈log^9 n⌉, and its number of leaves exceeds n/[8(⌈log^9 n⌉+1)] by a diverging factor of order (log n)^8 log log n. It also has more than three leaves. Neither Theorem A nor Theorem C covers it. These trees are valid concrete test targets for the remaining source conjecture, not counterexamples to random-graph containment.

### Corrected interpretation of the remaining gap
Theorem B isolates the first failure of the *two-chord proof method*, not the first family unknown in the literature. Theorem C already covers every fixed number of leaves, including the four-leaf example in Theorem B. The unresolved source problem still concerns all bounded-degree trees, with the uniformly subdivided, many-branch family above in the uncovered middle regime. The Hall-reservoir proposal B at the start of this record has not been proved; it would need a common completion event for this broader family, not just for spiders or long-path trees.


## Executed verification and final referee disposition
- second_experiment.py checked 73,680 explicit two-chord spanning constructions for n from 5 through 34, all permissible arm lengths and split points, at centers 0, floor(n/2), n−1. It checked vertex coverage, arm lengths, degree sequence, distinct non-cycle chords and the exact non-cycle-edge set. Cyclic translation invariance is proved in the construction, rather than inferred from testing only three centers.
- Complete candidate families at n=12,24,40,100 passed the incidence ≤4 and conflict degree ≤6 bounds. Greedy disjoint packings had sizes 18/48, 116/456, 242/680, and 1883/5700 (packing/candidates), satisfying 7m≥N. The largest instance needed only 5,700 candidate pairs.
- The 27 sparse sprinkle trials found candidates in 24 cases and missed three. These sampled targets do not test full simultaneous universality; their finite failure is explicitly retained. All found embeddings passed their spanning-geometry checks. Script calculation time was 4.23 seconds.
- cycle_barrier_check.py exhaustively enumerated 7!,8!,9! spanning vertex maps for the four-leaf double-cherry trees. Every mapping used at least two non-cycle edges; the witness and forest-count inequalities passed for every non-cycle count. The calculation took 1.34 seconds. The displayed logarithmic upper bound is uninformative at the smallest tested log n=20 and negative at the larger displayed scales; its asymptotic convergence follows from the proof, not these numbers.
- bare_path_packing_check.py ran 4,947 structural checks, including all 986 unlabeled tree types on 2–12 vertices, path sizes up to 2,000, and a 1,481-vertex subdivided 20-leaf tree. All degree-2 segment counts, whole-vertex disjointness and algebraic packing bounds passed. Its calculation took 0.23 seconds. The tests verify the finite structural argument for varying m; they do not simulate the asymptotic log^9 n density theorem.
- ChordCertificate.lean was checked with `lake env lean ~/brain_workers/TRIO_1011/op/H0021/ChordCertificate.lean` from ~/lean_verify, with a one-hour process timeout and one Lean run at a time. It imports only Mathlib.Data.Finset.Card. Final exit code 0; all three named theorems print only [propext, Classical.choice, Quot.sound], no sorryAx. `decide +kernel` verifies the 18-element packing cardinality, pairwise edge disjointness of its list and equality of that list's finite set with the recorded packing. No native_decide or sorry is present. Earlier failed attempts used an unavailable Finset.Pairwise field and then lacked a decidable universal subtype instance; the final certificate uses decidable List.Pairwise and fully checks. The asymptotic and general finite constructions remain written proofs, not Lean formalizations.

The full conjecture survives these checks as unresolved. Theorem A supplies an independent complete proof of a known small-leaf special case. Theorem C supplies a rigorously checked stronger corollary of existing literature. Theorem B and its extension identify a genuine constraint on a proposed proof method but not a graph-theoretic counterexample. Approach B (Hall repair plus extendability) remains unproved and was not silently assumed. No sketch is counted as a full solution.

STATE: DONE. VERDICT: PARTIAL. The next concrete mathematical task is a simultaneous completion/rerouting theorem for the uniformly subdivided subcubic family with branch count Θ(n log log n/log n), preserving exact path lengths and exhausting the host's vertices at coefficient 1+ε. Neither the fixed-cycle two-chord method nor the existing log^9 n bare-path theorem supplies it.
