# H0021 research attempt — 2026-10-12

## Exact target and outcome
For every fixed ε>0 and fixed integer Δ≥2, prove that G(n,(1+ε)log n/n) simultaneously contains, as non-induced spanning subgraphs, copies of every n-vertex tree of maximum degree at most Δ. This is Conjecture 1.4, page 7 of arXiv:2608.06358v1. The first unresolved degree is Δ=3. No proof or counterexample of the full conjecture was obtained. The structural theorem below is PARTIAL and no novelty is claimed.

All logarithms are natural, limits are n→∞, and edge probabilities are understood only for sufficiently large n, when they lie in [0,1]. The integers Δ and k and the real c are fixed before taking the limit.

## 1. The Δ=2 special case (complete reduction to a published theorem)
A tree with at least two vertices and maximum degree ≤2 is a path. To prove this, choose a longest simple path. If a vertex were outside it, connectedness gives a path from an outside vertex whose first intersection with the chosen path is w. If w is internal, its two path neighbors and the preceding outside neighbor give degree ≥3. If w is an endpoint, appending the outside path contradicts maximality. Thus every vertex is on the path. There are no additional edges because the tree is acyclic. For n=1 the assertion is immediate.

Glebov–Krivelevich, arXiv:1207.2748v1, Theorem 1, page 2, states that above p=(log n+log log n+ω(1))/n the number of Hamilton cycles is n!p^n(1-o(1))^n a.a.s. In particular it is positive whp. This is a cited theorem, not a theorem reproved here; the downloaded primary text is hamilton_correct.txt.
For p=(1+ε)log n/n, the surplus ω(n)=ε log n−log log n tends to infinity. The theorem therefore supplies a Hamilton cycle whp. Deleting one edge gives a spanning path, and the classification just proved shows that the graph is T_{n,2}-universal. No union bound over trees is used because there is one isomorphism class. This proves the original assertion for Δ=2 only.

## 2. The leading constant cannot be below 1 (self-contained proof)
Fix 0<c<1 and let p=c log n/n. Let X count isolated vertices and a=(1-p)^{n-1}. Then μ=EX=na=n^{1-c}(1+o(1))→∞, since log(1-p)=−p+O(p²) and np²=o(1).
For distinct u,v, their isolation requires absence of 2n−3 edges, so E[I_u I_v]=(1-p)^{2n-3}=a²/(1-p). Hence
Var(X)/μ²=(1-a)/(na)+(1−1/n)p/(1-p)≤1/μ+p/(1-p)→0.
Chebyshev gives P(X=0)≤Var(X)/μ²=o(1). An isolated vertex cannot belong to a spanning connected tree when n≥2. Thus the graph is not universal for any Δ≥2 whp. This is a lower bound consistent with the conjecture, not a counterexample to it.

## 3. Sharp asymptotic size of an adaptive attachment reservoir (self-contained theorem)
Call S⊆V(G) a k-neighbor reservoir if every v∉S has at least k distinct neighbors in S. Let γ_k(G) be the smallest size of such a set. A set V(G) always qualifies, so this parameter is well defined even if the graph has small minimum degree.

**Theorem.** For each fixed c>1 and integer k≥1, with p=c log n/n,
γ_k(G(n,p)) / [n log log n/(c log n)] →1 in probability.

This theorem concerns local attachment possibilities. It asserts neither an injective allocation of attachment vertices nor a spanning-tree embedding.

### Upper bound by random selection and repair
Put L=log n, ℓ=log log n, M=nℓ/(cL), λ=ℓ+(k+2)log ℓ, and q=λ/(cL). For sufficiently large n, 0<q<1. Sample G and, independently, include every vertex in R with probability q.

First, G has minimum degree ≥k whp. For D∼Bin(n−1,p), for 0≤j<k,
P(D=j)=binom(n−1,j)p^j(1-p)^{n−1−j}
≤((np)^j/j!)exp(−p(n−1−j)).
Summing over these finitely many j gives P(D<k)=O(n^{-c}L^{k-1}). A union bound over n vertices gives O(n^{1-c}L^{k-1})=o(1).

Let B={v∉R: |N(v)∩R|<k}. For a fixed v conditional on v∉R, the indicators that u∈R and uv∈E(G), for u≠v, are independent Bernoulli(pq). Therefore |N(v)∩R| is Bin(n−1,pq) under this conditioning. We do not assume independence between the badness events for different vertices. Its mean is λ(1−1/n), pq=λ/n, and for fixed k the same elementary binomial estimate yields
P(v∈B)≤O(exp(−λ)λ^{k−1})=O(1/[Lℓ³]).
The last equality uses exp(−λ)=L^{-1}ℓ^{-(k+2)} and λ/ℓ→1. Thus E|B|=O(n/[Lℓ³])=O(M/ℓ⁴).
Markov yields P(|B|>M/ℓ)=O(ℓ^{-3})→0.

Also ER=nq=(1+o(1))M, Var(|R|)≤nq, and nq→∞. Chebyshev (for example with relative deviation (nq)^{-1/4}) gives |R|=(1+o(1))M whp.

On the event δ(G)≥k, choose, for every v∈B, a set W_v of k distinct neighbors of v in G. Define
S=R ∪ ⋃_{v∈B} W_v.
Then |S|≤|R|+k|B|=(1+o(1))M. If v∉S and v∉B, then v∉R and it has ≥k neighbors in R⊆S. If v∉S and v∈B, its k neighbors W_v lie in S. These two cases exhaust all v∉S. Witness sets may overlap; overlaps only decrease |S| and do not invalidate the k distinct neighbors for any one vertex.

The construction succeeds with probability 1−o(1) over the joint pair (G,R). If a graph G admits no reservoir of this size, the construction fails for every R. Consequently the probability over G that no such reservoir exists is at most the joint failure probability. This justifies passing from the auxiliary randomized construction to the claimed whp existence in G.
The finite union cardinality bound used here is kernel-checked in Reservoir.lean; the probabilistic estimates are proved above, not formalized in Lean.

### Lower bound for all possible choices of S, including adaptive choices
Fix δ∈(0,1) and r=floor((1−δ)M). For a fixed r-set S, the events that the different outside vertices have at least one neighbor in S depend on disjoint sets of crossing edges and hence are independent. Its probability of being a 1-neighbor reservoir is exactly
[1−(1-p)^r]^{n−r}≤exp(−(n−r)(1-p)^r).
Here r=o(n), pr=(1−δ)ℓ+o(1), and rp²=o(1). Hence (1-p)^r=(1+o(1))L^{-(1−δ)}. There are at most (en/r)^r choices of S. A union bound gives
P(∃ dominating r-set)≤exp(r log(en/r)−(n−r)(1-p)^r).
The positive term is O(nℓ²/L). The negative term is (1+o(1))n/L^{1−δ}; their ratio is O(ℓ²/L^δ)→0. The entire exponent tends to −∞, so the probability tends to zero.

Any k-neighbor reservoir is also a 1-neighbor reservoir, and any smaller dominating set can be padded to size r while preserving domination of the remaining outside vertices. Therefore γ_k>r whp. Since δ>0 was arbitrary, this and the upper bound prove the theorem in probability.

## 4. Why a predetermined reservoir fails on the same scale
For a deterministic r-set R independent of G, let Y count vertices outside R with no neighbor in R. Exactly
Y∼Bin(n−r,(1-p)^r).
For r=(1+o(1))M, (1-p)^r=L^{-1+o(1)}, so EY=n/L^{1+o(1)}→∞. Variance ≤EY and Chebyshev give Y/EY→1 in probability. In particular R is not even a 1-neighbor reservoir whp. More generally for r=ρn+O(1), 0<ρ<1, EY=(1−ρ)n^{1−cρ}(1+o(1)). When cρ<1 there are many missed vertices whp. When cρ>1 the expectation tends to zero, so the fixed set does dominate whp by Markov. Nothing here applies to a set deliberately selected after observing G.

## 5. Hostile referee checks and the precise gap
1. Fixed quantifiers: all bounds use fixed c>1 and fixed k; no growing Δ statement is established.
2. Joint versus conditional law: only each vertex's marginal badness was used for the upper bound. Linearity and Markov do not need independence of B. The lower-bound crossing events are independent for a fixed S; union bounding over S covers adaptive selection.
3. Repair does not remove vertices or edges. Minimum degree ≥k guarantees W_v exists. No restriction says W_v must lie outside B or outside R, and none is needed. A bad vertex moved into S no longer needs domination, which is consistent with the definition.
4. Cardinality versus routing: k neighbors per outside vertex cannot imply a simultaneous matching into S for arbitrary large root sets. Even a complete bipartite graph with parts S and V\S supplies arbitrarily many neighbors per outside vertex but cannot inject more than |S| outside demands into distinct vertices in S. Thus the inference from domination to absorption is invalid.
5. Leaves, long paths and branching configurations: a universal host must realize all these with the same high-probability host event. The reservoir theorem supplies no common full-tree embedding event.
6. Source typo: the paragraph preceding Conjecture 1.4 prints C/n; Theorem 1 and the conjecture use C log n/n and (1+ε)log n/n. We use the actual theorem and conjecture, not that inconsistent sentence.
7. Literature incompleteness: OpenAlex and Semantic Scholar are rate limited. No inference that the conjecture remains open everywhere is made from unavailable results.

The unresolved step is a spanning completion theorem, already for Δ=3, allowing simultaneous capacity and disjoint routing at p=(1+ε)log n/n. Neither local k-neighbor domination, the earlier almost-spanning expansion reduction, nor Hamiltonicity proves this. No bridge between the adaptive reservoir and such a completion theorem was found.

## 6. Computation and formal verification
See experiment.py and experiment_results.json for exact graph enumeration at n=5, covariance and reservoir probability checks, and bounded-size random trials of the repair construction. These are checks, not asymptotic proofs. See Reservoir.lean and lean_check.txt for the finite cardinality theorem; no sorry or native_decide is used. All results and any limitations are reported below after execution.


### Executed verification results
- experiment.py finished its computations in 0.42 seconds. It enumerated all 1,024 labeled five-vertex graphs. Among them 633 contain a spanning path and 561 are universal for the two subcubic tree types; the difference is 72 (60 four-edge hosts and 12 five-edge hosts). The full edge-count arrays are in experiment_results.json.
- independent_check.py decoded all 5^3 Prüfer words by a separate leaf-removal algorithm, obtaining all 120 labeled maximum-degree-3 trees, then recovered the same universality counts. This checks completeness of the tree-family enumeration independently of NetworkX's nonisomorphic-tree generator.
- At p=0.23, exact weighted enumeration verifies both the isolation variance formula and the fixed-reservoir binomial mean/variance to error below 10^{-10}.
- Nine sparse random trials used c=1.5, k=2, and n=500, 2000, 8000. Six had minimum degree ≥2; all six passed the outside-neighbor and cardinality checks. Three lacked the minimum-degree premise and were skipped, not counted as successes. Initial reservoir sizes are roughly 2–2.5 times the limiting leading-order size at these finite n. This illustrates slow convergence; no finite-size sharpness conclusion is drawn.
- The auxiliary logarithmic-scale calculation is numerical evidence only: the lower-bound entropy/error ratio is not small at the first tested scales and is nonmonotone there. Its eventual convergence to zero follows from the proved analytic limit (log L)^2/L^δ→0, not from those finite values.
- Reservoir.lean was checked with `lake env lean ~/brain_workers/TRIO_1011/op/H0021/Reservoir.lean` from ~/lean_verify. Final exit code 0; printed axioms [propext, Classical.choice, Quot.sound], with no sorryAx. Only Mathlib.Algebra.Order.BigOperators.Group.Finset is imported. The first two runs failed (UTF-8 BOM and a missing order import); these were corrected before the successful check. The final proof uses standard finite-set and sum inequalities, no decision procedure and no native_decide. The probability theorem itself is not Lean formalized.

## 7. Final disposition
STATE: DONE, VERDICT: PARTIAL. The original problem is unresolved by this attempt. The full source statement was confirmed and no source-matching literature solution was found; two literature services remained inaccessible. The precise future research obligation is to construct and prove a uniform, vertex-disjoint spanning-completion method at coefficient 1+ε, already for subcubic trees. The results here identify and certify the adaptive reservoir scale but do not supply that method.


## 8. Requested second serious attempt — 2026-10-12
The detailed continuation is SECOND_ATTEMPT.md, which records two new proposed approaches and pursues the Hamilton-cycle/chord route. It proves an independent uniform three-leaf theorem, a quantitative obstruction to fixed-cycle embeddings using few fresh chords, and an explicit reduction to Montgomery's pre-existing Theorem 1.2 (arXiv:1405.6560v1, page 2). That primary theorem yields universality for all fixed-Δ trees with at most n/[8(⌈log^9 n⌉+1)] leaves. It already implies the spider special case; no novelty or new general degree bound is claimed. New finite computations and a kernel-checked chord certificate are documented there.

Theorem B's first two-branch obstruction is a failure of the two-chord proof method, not a family unknown in the literature. The unresolved source conjecture still includes subcubic trees whose many branch vertices are separated by paths of length about log n/log log n. Their explicit construction and the failure of the long-bare-path reduction are in SECOND_ATTEMPT.md. This continuation ends STATE: DONE, VERDICT: PARTIAL, with the full statement unproved and unrefuted.
