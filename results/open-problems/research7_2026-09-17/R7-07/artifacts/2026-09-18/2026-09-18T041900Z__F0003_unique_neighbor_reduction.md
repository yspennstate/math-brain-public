Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — unique-neighbour reduction for the sharp random-regular singularity exponent

Date: 2026-09-18 UTC.  
Target: Van Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 5 immediately after Theorem 5.2.  
Frozen R7-07 metric: `a_3 := sup{a : P(A_{n,3} singular) <= n^{-a+o(1)}}`; evidenced baseline `a_3 >= 1/9`; source-predicted target `a_3=1`.  
This artifact proves structural reductions only, so the frozen metric does **not** move.

The three methods in this research iteration are **B2 ATTACK THE NEGATION FIRST**, **B1 CHANGE THE MATHEMATICAL CATEGORY**, and **B21 IMPORT A TECHNIQUE FROM ANOTHER FIELD**. The previous R7-07 triple was B3/B22/B14, so there is no immediate repetition.

## 1. Idea before code

Vu records the lower scale `n^{-d+2}` because a very small local dependency can make the adjacency matrix singular. The natural negation of the hoped-for sharp exponent is that some *other* kernel-vector geometry contributes at the same or a larger polynomial scale.

Instead of trying immediately to improve Huang's global anti-concentration bound, first ask what a kernel vector forces combinatorially. If `x != 0` and `Ax=0`, with support `S`, then an outside vertex cannot have exactly one neighbour in `S`: its row equation would equal the unique nonzero support coordinate. Thus every kernel support is a failure of **unique-neighbour expansion**. Random regular graphs are easy to count in the configuration model under exactly this failure event.

This category change leads to a source-relevant theorem: at the `n^{-d+2}` scale, *all kernel vectors of support between 3 and `n^{1/20}` are negligible*. Therefore any non-twin mechanism capable of changing Vu's sharp exponent must be genuinely global, with support exceeding `n^{1/20}`.

## 2. B2 — attack the negation: exact local obstructions

### Lemma 2.1 — unique-neighbour obstruction

Let `G` be a finite simple graph with adjacency matrix `A`, let `0 != x in ker A`, and set

`S = supp(x) = {u : x_u != 0}`.

Then every vertex `v notin S` has either zero or at least two neighbours in `S`.

**Proof.** If `v notin S` had exactly one neighbour `u in S`, then

`(Ax)_v = sum_{w~v} x_w = x_u != 0`,

contradicting `Ax=0`. QED.

Call a set satisfying the conclusion **unique-neighbour-bad**.

### Lemma 2.2 — support two is exactly the twin event

Let `G` be simple and `d`-regular with `d>=1`. There is a nonzero kernel vector supported on exactly two vertices `u,v` iff `u,v` are nonadjacent twins:

`uv notin E(G)` and `N(u)=N(v)`.

In that case the support-two kernel is spanned by `e_u-e_v`.

**Proof.** Write `x=a e_u+b e_v` with `ab != 0`. If `uv` were an edge, the equation at `u` would contain the sole nonzero support-neighbour contribution `b`, impossible. Thus `uv` is absent. For every other vertex `w`,

`a 1_{w~u}+b 1_{w~v}=0`.

A vertex adjacent to exactly one of `u,v` is impossible, so the two neighbourhoods agree. Since `d>=1`, a common neighbour exists and its equation gives `a+b=0`. Conversely identical nonadjacent neighbourhoods make `A(e_u-e_v)=0`. QED.

Thus the source's `n^{-d+2}` local scale is not merely one example among support-two events: it is the **entire support-two singularity class**.

### Proposition 2.3 — in a cubic graph, support three is exactly a `K_{3,3}` component

Let `G` be a finite simple 3-regular graph. A nonzero kernel vector with support exactly three exists iff `G` has an isolated component isomorphic to `K_{3,3}` and the support is one of its bipartition classes. On that support the kernel condition is `x_1+x_2+x_3=0`.

**Proof.** Let the support be `{1,2,3}` and all three coordinates be nonzero.

First, the induced graph on the support has no edges. Indeed, an induced degree-one vertex would see a single nonzero support coordinate and violate its row equation. The only three-vertex induced graph with no degree-one vertices besides the empty graph is the triangle, but the triangle adjacency matrix has eigenvalues `2,-1,-1` and hence no nonzero kernel. Therefore the support is independent.

Every support vertex now has three crossing edges, for nine support-to-boundary incidences total. By Lemma 2.1, a boundary vertex uses either two or three of these incidences.

If a boundary vertex sees a pair `{i,j}`, then `x_i+x_j=0`. If a boundary vertex sees all three, then `x_1+x_2+x_3=0`. A pair equation and a triple equation together force the remaining coordinate to be zero, impossible. Hence either all boundary blocks have size two or all have size three. Nine incidences cannot be partitioned entirely into blocks of size two. Therefore every block has size three. Exactly three boundary vertices occur, each adjacent to all three support vertices. Since all six vertices already have degree three, they form an isolated `K_{3,3}` component. The converse is immediate: on one bipartition class, every vector of coordinate sum zero lies in the adjacency kernel. QED.

This finite classification was independently executed over exact rational arithmetic by

- `2026-09-18T041500Z__F0003_support3_exact_check.py`, creation commit `e145548cfffab1cc8f35c5c00f2ed2ba83ed9b15`;
- output `2026-09-18T041500Z__F0003_support3_exact_check.out`, creation commit `61dff524baface5f2fba4ecde0a3f890607eed57`.

The checker enumerated all nine degree-compatible incidence patterns and found the unique survivor

`internal_edges=(), boundary multiplicities=(0,0,0,3), rank=1`, followed by `EXACT_CHECK_PASS`.

A `K_{3,3}` component occurs with probability `O(n^{-3})` in the cubic configuration model (choose its six vertices, then force nine prescribed internal pairings), so it is already two powers below the cubic twin scale `n^{-1}`.

## 3. B1 — change category: kernel support becomes unique-neighbour expansion

The next theorem treats all fixed degrees and, importantly, support sizes growing as a small power of `n`.

### Theorem 3.1 — subpolynomial-support suppression

Fix `d>=3`. Let `G_{n,d}` be a uniformly random simple `d`-regular graph. Then

`P(there exists 0 != x in ker A_{n,d} with 3 <= |supp x| <= n^{1/20}) = o(n^{2-d}).`

More explicitly, if `U_k` is the event that some `k`-set is unique-neighbour-bad, then for all sufficiently large `n` and `3 <= k <= n^{1/20}`,

`P(U_k) <= d^2 k^2 [ e (2d)^d k^{d-1} n^{1-d/2} ]^k`

up to a multiplicative constant depending only on fixed `d` from conditioning the configuration model to be simple. Consequently

`sum_{k=3}^{floor(n^{1/20})} P(U_k) = O_d(n^{-3(9d-19)/20}) = o(n^{-(d-2)}).`

Since every kernel support is unique-neighbour-bad by Lemma 2.1, the kernel-vector statement follows.

### Proof

Work first in the standard configuration model with `d` labelled half-edges at each of `n` vertices and a uniformly random perfect matching of the `dn` half-edges. For fixed `d`, conditioning on simplicity costs only a bounded multiplicative factor because the configuration model is simple with probability bounded away from zero as `n -> infinity`.

Fix a vertex set `S` of size `k` and let

`h = d k`

be the number of half-edges incident to `S`. Suppose `S` is unique-neighbour-bad. Let `e` be the number of matching pairs internal to the `S` half-edges. Then

`r = h-2e`

half-edges of `S` cross to vertices outside `S`. Let `t` be the number of distinct outside vertices hit by those `r` crossing edges. Unique-neighbour-badness implies every hit outside vertex receives at least two such edges, hence

`t <= floor(r/2)`.

We overcount all partial pairings with these parameters.

1. Choose and pair the `2e` internal half-edges: at most `h^{2e}` possibilities.
2. Choose the `t` outside target vertices: at most `n^t` possibilities.
3. Assign the `r` labelled crossing half-edges to those targets: at most `t^r <= h^r` possibilities. We deliberately ignore the at-least-two constraint after using `t<=r/2`; this only overcounts.
4. Choose a target half-edge at each outside vertex occurrence: at most `d^r` possibilities.

Once these `e+r=h-e` matching pairs are prescribed, their probability in the uniform perfect matching is

`prod_{j=0}^{h-e-1} 1/(dn-(2j+1))`.

For `k <= n^{1/20}` and fixed `d`, `h=o(n)`, so for all sufficiently large `n` this is at most

`(2/(dn))^{h-e}`.

Thus, for fixed `e,t`, the contribution is at most

`h^{2e} n^t h^r d^r (2/(dn))^{h-e}`

`<= (2h)^h n^{t-h+e}`

because `2e+r=h` and the net power of `d` is `d^{-e}<=1`. Using

`t <= floor((h-2e)/2) = floor(h/2)-e`

gives

`t-h+e <= -ceil(h/2)`.

There are at most `h` choices for each of `e` and `t`. Therefore, for a fixed `S`,

`P(S unique-neighbour-bad) <= h^2 (2h)^h n^{-ceil(h/2)}.`

Union-bound over the `k`-subsets and use `binom(n,k) <= (en/k)^k` and `h=dk`:

`P(U_k)`
`<= binom(n,k) (dk)^2 (2dk)^{dk} n^{-ceil(dk/2)}`
`<= d^2 k^2 [ e (2d)^d k^{d-1} n^{1-d/2} ]^k.`

If `k<=n^{1/20}`, then

`k^{d-1} n^{1-d/2} <= n^{-(9d-19)/20}`.

Set `c_d=(9d-19)/20>0`. For large `n`, the geometric base `e(2d)^d n^{-c_d}` is less than `1/2`, so summing from `k=3` to `n^{1/20}` yields

`sum P(U_k) = O_d(n^{-3c_d}).`

Finally,

`3c_d-(d-2) = (7d-17)/20 > 0`

for every `d>=3`, so this is `o(n^{-(d-2)}) = o(n^{2-d})`. QED.

### Corollary 3.2 — every bounded non-twin support is one polynomial order smaller

For fixed `d>=3` and any fixed `K>=3`,

`P(exists kernel vector with 3 <= support size <= K) = O_{d,K}(n^{1-d}).`

Indeed the fixed-`k` exponent from the same count is

`k-ceil(dk/2) <= 1-d`

for every `k>=3`. By contrast, support two is exactly the twin mechanism and occurs on the source scale `n^{2-d}`.

### Source-relevant consequence

Let `T_d` be the event that `G_{n,d}` has nonadjacent twin vertices, and let

`G_d^{global} = {A_{n,d} has a nonzero kernel vector with support > n^{1/20}}`.

Then the theorem gives the exact reduction

`P(A_{n,d} singular) <= P(T_d) + o(n^{2-d}) + P(G_d^{global}).`

Therefore a source-level upper exponent `d-2` follows once one proves

`P(G_d^{global}) <= n^{-d+2+o(1)}`.

A stronger twin-dominance asymptotic would follow from `P(G_d^{global})=o(n^{2-d})` plus the corresponding twin asymptotic. The present artifact does **not** prove either global estimate.

For `d=3`, this says any non-twin singularity capable of contributing on the `n^{-1}` scale must be carried by a kernel vector with more than `n^{1/20}` nonzero coordinates.

## 4. B21 — import the sparse-rank/switching viewpoint

The exact-rank work for sparse Erdos-Renyi graphs succeeds by separating local dependencies from global rank deficiency and then using rank-boosting ideas. Theorem 3.1 supplies the analogous local/global separation for the fixed-degree regular model at the source polynomial scale.

The regular model has an additional natural tool: degree-preserving two-switches.

### Lemma 4.1 — exact kernel preservation under a two-switch

Let `a,b,c,d` be distinct vertices with `ab,cd` edges and `ac,bd` nonedges. Let `G'` be obtained from `G` by the legal two-switch

`ab, cd  ->  ac, bd`,

and write `A,A'` for the two adjacency matrices. If `Ax=0`, then the **same vector** remains in the new kernel, `A'x=0`, iff

`x_b=x_c` and `x_a=x_d`.

**Proof.** The update affects only the four displayed coordinates, and

`((A'-A)x)_a = x_c-x_b`,
`((A'-A)x)_b = x_d-x_a`,
`((A'-A)x)_c = x_a-x_d`,
`((A'-A)x)_d = x_b-x_c`.

Thus the update vanishes exactly under the two stated equalities. QED.

This gives a concrete route for the global-support event. If a large-support kernel vector has many coordinate classes rather than a few huge level sets, most legal two-switches destroy that vector. If it has only a few huge level sets, the equations `Ax=0` impose strong equitable-partition-type constraints. Either outcome is potentially countable.

The missing point is crucial: destroying one specific kernel vector does **not** imply that `A'` is nonsingular, because the switched graph may acquire or retain a different kernel vector. A valid switching proof therefore needs a rank-sensitive injection/preimage bound, or a way to expose a canonical kernel certificate whose destruction changes rank. I do not replace that missing global ingredient by the fixed-vector lemma.

## 5. What moved and what did not

New rigorous progress:

1. support two is proved to be exactly the nonadjacent-twin event;
2. support three in the cubic case is classified exactly as an isolated `K_{3,3}` component and independently certified by exact rational enumeration;
3. for every fixed `d>=3`, **all kernel supports of sizes `3..n^{1/20}` together contribute `o(n^{2-d})`**, so they cannot change the source sharp exponent;
4. the full source problem is reduced to a genuinely global-support singularity estimate;
5. a two-switch preservation identity isolates a specific candidate tool for that global regime.

Frozen metric:

`a_3: >=1/9 -> >=1/9` — **NO MOVEMENT**.

Reason: no new upper bound on the probability of global-support kernel vectors has yet been proved. The theorem is a source-relevant structural reduction, not a replacement metric.

## 6. Exact remaining blocker and next attack

The clean blocker is now

`P(A_{n,d} has a nonzero kernel vector with support > n^{1/20}) <= n^{-d+2+o(1)}`.

For the first milestone `d=3`, the needed statement is

`P(A_{n,3} has a kernel vector with support > n^{1/20}) <= n^{-1+o(1)}`.

A useful next nonrepeating triple should attack this global regime rather than generate more bounded-support checkers. Candidate methods: **B14 find the group acting** on switchings/kernel level sets; **B27 swap the quantifiers** by choosing a random legal switch after conditioning on a singular graph; **B10 derandomize** a rank-boosting switch witness. Those methods differ from this run's B2/B1/B21.

## 7. Scope and status

Status: **PARTIAL / SOURCE OPEN**. No source-level exponent has been settled. No novelty claim is made from the dated search miss. Independent P26 and distinct OTHER-track audits are `0/1` and `0/1` because there is no closure candidate to audit.
