Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 7 — priority-weighted representative and a joint one-rescue compiler

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN**.

**SOURCE-METRIC NO MOVEMENT.**  For the exact model fixed by the owner, the externally literature-supported explicit-decimal bracket remains

`[alpha_L,alpha_U]=[3.52,4.4898]`,

hence

`W_verified=alpha_U-alpha_L: 0.9698 -> 0.9698`.

The new mathematical movement is auxiliary but substantive: the previous best one-rescue cutoff penalty at the rounded Díaz saddle,

`J_5 = 1.869587880794033e-7`,

is replaced by a proved **priority-weighted all-class penalty**

`J_rank = 3.706534502036171...e-7`,

and, jointly with the already-proved `j>=2` Hamming-rescue term,

`J_total = 3.711902852733471...e-7`.

Thus the local rounded-saddle mechanism gain is about `1.9854 x` over the preceding best `J_K` and about `106.05 x` the source's printed rounded log margin.  This is **not** an interval-certified global reoptimization, so no threshold endpoint is changed.

## 1. Continuity, ownership, and evidence consumed

This run continues only the scoped **cluster-aware weighted-counting / overlap-variational** route in `operations/claims/PROB10-04.md`.  It does not take over the constructive NM13-06 route or the interpolation NM13-13 route.

Consumed repository state:

- `operations/PROB10_2026-09-20.md` (owner contract and model freeze);
- current `POSTED.md` (exclusion register);
- `operations/claims/PROB10-04.md` @ blob `1095e6bfb106b53e810af56f2605521abb7143b4`;
- actual pre-refocus HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md` @ blob `e59380417dc476970e22b72b66c59ffbffa4af3a`, preserving the real F0095 / binary-cascade 3-colourability work with `W_3<=0.6565076260769` and not relabeling it as 3-SAT progress;
- preceding own report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T05-27-00Z__secondary_weight_negative_association_rescue.md`;
- newest neighboring interpolation report read this run: `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T05-22-56Z__t04_three_support_4392_monotone_tail.md`; it records a project `CANDIDATE_FULL` upper endpoint `4.392`, pending independent review, and is not promoted into this worker's externally verified metric;
- newest constructive report read this run: `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T07-23-15__t04_zero_break_independent_thinning_nogo_and_conflict_batch.md`; it proves a no-go for one-shot independent zero-break thinning and identifies correlated conflict-free batches as the next constructive object.

The new mathematical idea was frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-46-30Z__priority_weighted_rescue_idea_before_code.md`

at creation commit `9963c830aee28d569d02f604eeddbc8a35b0bc56`.

## 2. Source model and current literature recheck

The exact source model remains: `n` Boolean variables, `m=floor(alpha n)` independent clauses, each clause choosing three distinct variables uniformly and then independent uniform signs.

The following distinctions remain mandatory.

1. Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, proves w.h.p. satisfiability below `3.52` for the standard independent-clause model: <https://arxiv.org/abs/math/0310193>.
2. Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at density at least `4.4898`: <https://arxiv.org/abs/0807.3600> and the journal version cited by ESA 2025.
3. Caragiannis--Gravin--Jiang, ESA 2025, explicitly define the classical model by **independent** uniform clauses and then study the different family of `k`-wise-independent clause distributions: <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103>.  Their result is not a solution of the present model.
4. Ding--Sly--Sun identify the threshold for sufficiently large `k`; this does not instantiate at `k=3`: <https://arxiv.org/abs/1411.0650>.
5. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, published online 27 March 2026, still state that the satisfiability threshold is known exactly for `k=2` and sufficiently large `k`, while fixed small `k` remains unresolved.  Their table's `d_sat(3)≈12.801` (equivalently `alpha≈4.267`) is a physics benchmark, not by itself an interval-certified theorem endpoint for this worker: <https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/random-textitksat-gibbs-uniqueness-threshold-revisited/6EF42EB37F15370DB593F0F02E3538E9>.
6. A fresh source relevant to the owner's sharp-window/exact-location distinction is Gaia Carenini, *The Scaling Window of Random k-SAT*, ECCC TR26-145, posted 16 August 2026.  It proves an `O(n/log n)` scaling-window upper bound for every fixed `k>=3`, improving the Friedgut--Bourgain `O(n/log log n)` bound: <https://eccc.weizmann.ac.il/report/2026/145/>.  This is stronger sharpness information but does **not** identify a limiting constant `alpha_3` or prove convergence of the threshold centers.

Accordingly the externally verified explicit-decimal metric remains width `0.9698`.  The repository's `4.392` interpolation result is tracked separately as an unaudited project candidate, not silently merged into the source metric.

## 3. Exact obstruction carried from run 6

The previous run proved a finite negative-association compiler and then used, for a fixed cutoff `K`, the secondary potential

`W_K = # { true light variables of class (k,1) with k>K }`.

For a true center `y` of class `t_{i,1}`, `i<=K`, whose `ps` copies all hit multiply-satisfied safe clauses, whose unique `nu` copy hits a canonical negative-unique-satisfied blocker, and whose corresponding blocker `ns1` slot is occupied by a false leaf `x` of class `f_{k,1,1}`, `k>K`, the swap

`y:1->0, x:0->1`

is satisfying, Hamming-neutral, and increases `W_K`.  Hence it cannot occur in a lexicographically chosen representative.

At the rounded source saddle the best cutoff was `K=5`, giving

`J_5≈1.869587880794033e-7`.

The exact remaining source obligation was global: add the correction to the complete Díaz `M=23` variational objective and outward-interval certify every interior and boundary box at some density below `4.4898`.

This run does **not** repeat cutoff tuning.  It changes the representative itself.

## 4. Three different attacks tried this run

### Attack A — one global degree potential

Among satisfying assignments that maximize the number of true light variables, maximize

`W_deg = sum_{v true, class(v)=(i,1)} i`.

A one-rescue swap from center class `i` to leaf class `k` raises `W_deg` whenever `k>i`.  Therefore all degree-improving swaps are forbidden at once, giving center-dependent leaf tails `E_{>i}` instead of a single `E_{>K}`.

This succeeds and already pointwise dominates every cutoff construction.

### Attack B — iid continuous priorities

Attach iid continuous priorities to variables and, after Hamming maximization, maximize total priority of true light variables.  Every completed `j=1` rescue pair is vertex-disjoint from every other completed pair.  Therefore each completed pair independently survives the priority maximality test with probability exactly `1/2`.

This succeeds and permits the entire `f_{k,1,1}` leaf pool, producing a different correction `J_iid`.

### Attack C — class-separated priorities plus jitter

Give a light variable of structural class `(i,1)` priority

`w_v=i+xi_v/3`,  `xi_v iid Uniform(0,1)`.

The intervals are disjoint across consecutive `i`.  A one-rescue swap from center class `i` to leaf class `k` is therefore:

- always priority-improving if `k>i`;
- priority-improving with probability `1/2` if `k=i`;
- never priority-improving if `k<i`.

This succeeds and strictly combines the useful pieces of A and B.  It is the strongest of the three at the rounded Díaz saddle and is the theorem proved below.

## 5. Deterministic rescue geometry is unchanged

Retain the predecessor pools for one fixed integer Díaz coarse type:

- `P` = all `ps` target slots, `Q` = multiply-satisfied safe `ps` slots;
- `U` = all `nu` target slots, `B` = one canonical `nu` slot chosen in each eligible negative-unique-satisfied blocker;
- `L` = all `ns1` target slots;
- `E_i` = number of `ns1` source copies belonging to false variables of class `f_{i,1,1}`;
- `E_{>i}=sum_{k>i} E_k`;
- `C_{i,j}` = number of true center variables of class `t_{i,j}`.

For a `t_{i,1}` center, a **completed one-rescue pair** means:

1. all `i` center `ps` copies hit `Q`;
2. the center's unique `nu` copy hits `B`;
3. the blocker `ns1` slot associated with that canonical `nu` slot is occupied by a copy from some `f_{k,1,1}` leaf.

Exactly as proved in the predecessor, flipping the center false and the leaf true preserves satisfiability: the center's `nu` literal rescues the leaf's unique endangered `ns1` blocker, every positive leaf occurrence becomes true, and every lost center `ps` literal lies in a clause with another satisfied literal.

Two completed one-rescue pairs are vertex-disjoint.  Centers are distinct by definition.  Canonical `nu` slots are one per blocker clause and the `nu` matching is injective, so their blockers are distinct.  Finally an `f_{k,1,1}` leaf has exactly one `ns1` source copy, so it can occupy at most one associated blocker slot.

## 6. New finite theorem — priority-weighted heterogeneous rescue compiler

For `i>=1` define

`a_i=(Q)_i/(P)_i`,

`b=B/U`,

and

`h_i = (E_{>i} + E_i/2)/L`,

with the usual convention that a falling-factorial ratio is zero if its marked pool is too small.

### Theorem 6.1

In the fixed integer coarse type, choose a satisfying representative by first maximizing true-light Hamming weight and then maximizing the class-separated continuous priority sum above.  Under the independent uniform `ps`, `nu`, and `ns1` copy bijections,

`E_priority P_matching(representative survives every completed j=1 rescue improvement)`

is at most

`prod_i (1-a_i b h_i)^{C_{i,1}}`.                         (6.1)

Moreover the same averaging can be performed jointly with the predecessor's deterministic Hamming-improving `j>=2` rescue exclusions, yielding

`P_survive <=`
`prod_i (1-a_i b h_i)^{C_{i,1}}`
` * prod_{i>=j>=2}(1-a_i b_j e_j)^{C_{i,j}},`             (6.2)

where

`b_j=(B)_j/(U)_j`, `e_j=(E_all)_j/(L)_j`,

`E_all=sum_k E_k`.

### Proof

Fix one candidate satisfying assignment of the prescribed integer type.  For each `j=1` center `c` of class `i(c)`, let:

- `S_c` be the indicator that all of its `ps` source copies hit the safe set `Q`;
- `N_c` be the indicator that its unique `nu` copy hits a canonical slot in `B`;
- conditional on `N_c=1`, let `R_c` be the degree-class label `k` if the associated blocker `ns1` target receives the unique `ns1` source copy of an `f_{k,1,1}` leaf, and put `R_c=0` for every ineligible source copy.

Let

`g_i(k)=1` for `k>i`, `g_i(i)=1/2`, and `g_i(k)=0` for `k<i` or `k=0`.

Because completed pairs are vertex-disjoint, the jitters used by different pairs are disjoint independent random variables.  Conditional on all three copy matchings, a necessary condition for the fixed assignment to be the priority-maximal Hamming maximizer therefore has probability exactly

`prod_c [1-S_c N_c g_{i(c)}(R_c)]`                    (6.3)

with respect to the priority jitters.  Indeed `k>i` gives a deterministic priority gain, `k=i` gives an improving comparison with probability `1/2`, and `k<i` cannot improve because the class intervals are separated by more than the jitter width.

Now average (6.3) over the `ps` matching first.  On source `ps` copies, membership of the matched target in `Q` is a uniform fixed-size `0/1` sample.  Such a sample is negatively associated.  Each `S_c` is an increasing function of the coordinates in its own disjoint center block, so the family of block indicators is negatively associated.  The factors in (6.3) are nonnegative decreasing functions of those disjoint blocks.  Hence the product inequality for negative association gives

`E_ps product_c[1-S_c z_c]`
` <= product_c [1-a_{i(c)} z_c]`,                       (6.4)

where `z_c=N_c g_{i(c)}(R_c)`.

Next condition on the `nu` matching.  If `N_c=1`, the canonical slot hit by center `c` determines one blocker `ns1` target slot.  Because there is only one canonical `nu` slot per eligible blocker and the `nu` matching is injective, these associated `ns1` slots are distinct across all active centers.

The vector of degree labels attached by the uniform `ns1` bijection to any fixed set of distinct target slots is a sample without replacement from the finite multiset of source labels.  Sampling without replacement is negatively associated.  For each center, `g_i(R_c)` is nondecreasing in the scalar label `R_c`, while

`1-a_i N_c g_i(R_c)`

is nonnegative and nonincreasing.  Therefore another negative-association product inequality yields

`E_ns1 product_c[1-a_i N_c g_i(R_c)]`
` <= product_c[1-a_i N_c h_i]`,                         (6.5)

because the one-coordinate mean of `g_i(R)` is exactly

`h_i=(E_{>i}+E_i/2)/L`.

Finally average over the `nu` matching.  The canonical-membership indicators on disjoint one-copy center blocks form another fixed-size sample and are negatively associated, each with mean `b=B/U`.  The factors in (6.5) decrease in `N_c`, so

`E_nu product_c[1-a_i N_c h_i]`
` <= product_c[1-a_i b h_i]`,                            (6.6)

which proves (6.1).

For centers with `j>=2`, the predecessor's Hamming argument says a completed rescue is impossible because flipping one center and its `j` leaves raises true-light Hamming weight by `j-1>0`.  Their `ps`, `nu`, and associated `ns1` source blocks are disjoint from the `j=1` center blocks.  The same three-stage negative-association averaging works with the increasing event that **all** `j` corresponding leaves lie in `E_all`; its one-block probability is `e_j`, and the canonical `nu` block probability is `b_j`.  Applying the block product inequality simultaneously to all `j` therefore multiplies the `j=1` factors by the predecessor factors and proves (6.2).  QED.

### Why the random priority device is legitimate in a first-moment count

For every fixed satisfiable formula, and for almost every continuous priority realization, the finite set of Hamming-maximizing satisfying assignments has a unique maximum-priority element.  Hence

`1{F satisfiable}`
` = E_priority sum_sigma 1{sigma is the selected representative of F}`. (6.7)

Replacing the exact selection condition by the necessary local conditions above only increases the right side.  Thus integrating over auxiliary priorities does not change the source random-formula model and is valid inside the upper-bound count.

## 7. Asymptotic correction at a fixed interior type

At a fixed interior density vector, bounded degrees give

`a_i -> q^i`, `b -> B/U`,

and

`h_i -> [E_{>i}+E_i/2]/L`.

Therefore the new one-rescue correction is

`J_rank(x)`
` = -sum_i t_{i,1}(x)`
`     log(1 - q(x)^i [B(x)/U(x)] [E_{>i}(x)+E_i(x)/2]/L(x)).`   (7.1)

The total correction can be added to the already-proved `j>=2` term:

`J_total(x)=J_rank(x)+J_{j>=2}(x)`.                         (7.2)

Attack A gives instead

`J_deg=-sum_i t_{i,1} log(1-q^i (B/U)E_{>i}/L)`,           (7.3)

and Attack B gives

`J_iid=-sum_i t_{i,1} log(1-(1/2)q^i (B/U)E_all/L)`.       (7.4)

The class-separated jitter construction pointwise strengthens Attack A whenever some same-class leaf mass is present.

## 8. Executed diagnostic and exact finite self-check

Matching code:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-50-00Z__priority_weighted_rescue_diagnostic.py`

creation commit `f9bf8fcb2e3ee825172509985752808ee4c113a9`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T05-50-30Z__priority_weighted_rescue_diagnostic.out`

creation commit `92c174fdb39ac7e3264fb1ea48801a5c7b3c1ec0`.

The numerical part uses 80-digit `Decimal` arithmetic on the **rounded** Díaz multipliers already recorded by the predecessor.  It is diagnostic, not an outward interval certificate.  It gives

`J_deg  = 3.250340804106922...e-7`,

`J_iid  = 3.513312097575857...e-7`,

`J_rank = 3.706534502036171...e-7`,

`J_total= 3.711902852733471...e-7`.

Relative to the preceding best cutoff:

`J_total/J_5 = 1.985412341867015...`.

The source's rounded printed log margin reconstructed from `(1+10^-7)*0.9999998965` is

`3.500010356125036...e-9`,

so the local ratio is

`J_total/source_margin = 106.0540534183741...`.

Again this is only a rounded-saddle mechanism comparison; the old saddle can move under reoptimization.

The same script also exhaustively enumerates a small exact finite matching toy with two heterogeneous centers and all `4! * 3! * 4! = 3456` matching triples.  Exact rational arithmetic gives

`toy_exact_survival = 3/4`,

while the theorem product bound is

`437/576`,

and

`3/4 <= 437/576`.

The executed output ends

`ALL_CHECKS_PASS = True`.

This is a self-check of a finite instance, not an independent audit and not the proof of Theorem 6.1; the written negative-association argument is the proof.

## 9. Source-level before/after versus auxiliary progress

### Externally verified source metric

`[3.52,4.4898] -> [3.52,4.4898]`,

`W_verified: 0.9698 -> 0.9698`.

No movement.

### Separate project candidate

NM13-13 currently records a `CANDIDATE_FULL`, pending independent review, at `alpha_U=4.392`, giving project-candidate width `0.872`.  This worker has not audited that proof and therefore does not claim it as externally verified source movement.

### Mechanism progress

The strongest local Díaz rescue exponent at the rounded source saddle moves

`1.869587880794033e-7 -> 3.711902852733471e-7`,

factor `1.9854`.

More importantly, the new finite theorem removes the arbitrary cutoff `K`: all degree classes are handled in a single representative-selection rule, and same-class one-rescue swaps contribute half-weight through independent continuous jitter.

## 10. Exact remaining obligation

The source endpoint still requires one thing that this run does not fake:

> Reconstruct the complete Díaz `M=23` variational objective and feasible domain, insert the joint penalty (6.2), and certify with outward interval arithmetic that the **global** refined maximum, including every boundary regime, is strictly below one at some explicit `alpha<4.4898`.

A rounded evaluation at the old interior saddle is insufficient because the maximizer can move.  The next mathematically different continuation inside this route should therefore be a **global certification architecture**, not another local motif or another cutoff:

1. eliminate as many Díaz variables analytically as possible using the Lagrange equations and conservation constraints;
2. prove a compact box decomposition with explicit monotonicity/convexity bounds for the new penalty on each box;
3. use interval branch-and-bound only after those analytic reductions, recording the worst certified box and its slack.

If that global certification cannot be reconstructed, the route should hand off its proved priority-rescue theorem rather than manufacture another local checker.

## 11. Honest status

**PARTIAL / source OPEN.**

New theorem proved: priority-weighted heterogeneous one-rescue compiler, jointly compatible with the predecessor's `j>=2` Hamming-rescue compiler.

Not proved: `alpha_U<4.4898`, exact threshold existence/value at `k=3`, or independent validation of the neighboring `4.392` candidate.
