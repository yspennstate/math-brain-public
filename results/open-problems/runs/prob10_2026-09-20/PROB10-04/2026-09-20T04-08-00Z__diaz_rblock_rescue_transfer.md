Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 run 5 — deterministic `r`-block rescue inside the Díaz configuration model

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **source OPEN / PROB10-04 PARTIAL**.

**SOURCE-METRIC NONMOVEMENT.**  For the externally recovered explicit-decimal theorem bracket I still use `[3.52,4.4898]`, so `W_verified=0.9698 -> 0.9698`.  A neighboring same-parent worker has meanwhile produced a **CANDIDATE_FULL, not yet independently validated** explicit upper bound `4.418`, which would give `[3.52,4.418]` and width `0.898`; this run neither rederives nor promotes that claim, so `W_repo-candidate=0.898 -> 0.898`.  The method did change as required after four unchanged source-metric runs: the previous unconditional blocker occupancy is now embedded in the finite Díaz copy-allocation model through a different, degree-`r` deterministic rescue obstruction.

## 1. Continuity, ownership, and evidence consumed

I continued only the existing scoped PROB10-04 **cluster-aware counting / overlap-variational** route in `operations/claims/PROB10-04.md`.  I did not take over the constructive lower-bound route and did not overwrite any claim.

Consumed before the new argument:

- `operations/PROB10_2026-09-20.md` on current `master`;
- current root `POSTED.md` exclusion registry;
- `operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`;
- own preceding report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T02-57-30Z__two_neighbor_blocker_occupancy_rate.md`, blob `680ba2b71a3100d19f470625ea8b2f7312fea093`;
- immutable HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, blob `e59380417dc476970e22b72b66c59ffbffa4af3a`, preserving the actual F0095 binary-cascade target and artifacts;
- neighboring constructive report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T05-29-47__t04_blocked_majority_core_and_promotion.md`, which proves a static blocked-majority core subcritical through `4.4898` and leaves dynamic promotion as its obstruction;
- neighboring cluster-counting report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T01-58-11Z__t04_anchored_degree_one_matching_variational.md`, which uses `t_{1,1}` roots, degree-one children and iid random scores to get a matching penalty;
- newer neighboring report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T02-57-07Z__t04_two_survey_4418_rigorous_upper.md`, blob `633de9b907b9849962014d23b61927e1926a2901`, whose `4.418` theorem is explicitly labeled `CANDIDATE_FULL` pending independent review.

The present route is nonduplicating relative to the last two items.  It uses no random score and no interpolation trial.  A `t_{r,r}` center with `r>=2` simultaneously rescues `r` degree-one blockers and yields an **unweighted Hamming improvement of `r-1`**, forcing an exact forbidden-block condition in the Díaz `nu` matching.

The idea was written before code in

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-43-00Z__diaz_degree2_pair_rescue_idea_before_code.md`;
- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-52-00Z__diaz_rblock_generalization_idea_before_code.md`.

## 2. Current source status, kept separate from repository candidates

Fresh bounded literature checking on 20 September 2026 still supports the distinction the owner requested:

1. Hajiaghayi--Sorkin prove the random proper 3-SAT lower bound `alpha>=3.52` in the sense that densities below `3.52` are satisfiable with high probability: <https://arxiv.org/abs/math/0310193>.
2. Díaz--Kirousis--Mitsche--Pérez-Giménez give the classical explicit `4.4898` upper bound used by this route: <https://arxiv.org/abs/0807.3600>.
3. Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis (CPC 2026) state that for small fixed `k`, including `k=3`, existence of a single uniform satisfiability threshold remains open, while interpolation supplies a rigorous 1RSB variational **upper mechanism**; their displayed `d_sat(3)≈12.801` is a physics numerical prediction, not a decimal I promote here without a certified evaluation: <https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/random-textitksat-gibbs-uniqueness-threshold-revisited/6EF42EB37F15370DB593F0F02E3538E9>.
4. The ESA 2025 paper in the owner prompt studies a different `k`-wise-independent model and is not the target.  Ding--Sly--Sun's threshold identification is for sufficiently large `k`, not automatically `k=3`.

The neighboring `4.418` report is therefore recorded as a fresh repository candidate, not silently converted into an independently validated literature baseline.

For this run's Díaz route, its simple-formula convention and the owner's iid proper-clause convention are asymptotically equivalent at `m=Theta(n)`: there are `8*C(n,3)=Theta(n^3)` possible signed proper clauses, so among `m=O(n)` iid draws

`P(any repeated whole clause) <= C(m,2)/(8 C(n,3)) = O(1/n) -> 0`.

Thus a theorem proved with high probability for the uniform simple proper formula transfers to the fixed iid proper-clause model, and conversely for events insensitive on an `o(1)` exceptional probability.  This does **not** identify the threshold; it only aligns the model conventions used below.

## 3. The exact new local mechanism

Use Díaz's extended clause coordinates

`alpha=((ps,ns),(pu,nu))`,

where `ps,ns` are satisfied positive/negative light copies and `pu,nu` are unsatisfied positive/negative light copies.  In a blocking clause the unique satisfied negative copy is subtype `ns1`; a negative satisfied copy in a clause having another satisfied copy is `ns2`.

Fix two source-legal extended clause types:

`a=((1,1),(1,0))`                                                  (3.1)

and

`b=((0,1),(1,1))`.                                                 (3.2)

A type-`a` clause has one `ps`, one `ns2` and one `pu`; its `ps` copy can be turned false while its `ns2` remains true.  A type-`b` clause is blocking: it has one `ns1`, one `pu`, and a **unique** `nu` slot.

For a fixed integer `r>=2` within the Díaz light-degree cutoff `M=23`, define:

- an **available `r`-center** to be a true light variable of class `t_{r,r}` whose `r` `ps` copies all land in type-`a` `ps` slots;
- a **selected leaf** to be a false light variable of class `f_{1,1,1}` whose unique `ns1` copy lands in a type-`b` clause;
- the unique `nu` slot of that type-`b` blocker is the leaf's **canonical rescue slot**.

### Lemma 3.1 — deterministic `r`-block rescue

Suppose an available `r`-center `y` has its `r` `nu` copies in the canonical rescue slots of `r` distinct selected leaves `x_1,...,x_r`.  Then changing

`y:1->0`, and every `x_i:0->1`,

preserves Díaz flat satisfiability and increases the number of true light variables by `r-1`.

#### Proof

Each selected leaf has degree `(1,1)` and `k=1`.  Its **only** negative occurrence is therefore its `ns1` blocker.  Flipping `x_i` from zero to one can destroy truth only at that blocker; its one positive occurrence changes from false to true and cannot hurt any clause.  But before/at the same simultaneous move, the center's `nu` occurrence in that blocker changes from false to true.  Hence every selected blocker stays satisfied.

The center's `r` negative occurrences are precisely these `nu` copies, so all of them change from false to true.  Its only potentially harmful changes are its `r` `ps` copies.  By availability, each lies in a type-`a` clause.  Such a clause contains an `ns2` literal that remains true after the center is changed.  None of the selected leaves can be that `ns2` variable: a selected leaf has negative degree one and that unique negative copy is already its `ns1` blocker.  Hence every anchor clause remains satisfied.

No other literal changes from true to false.  Therefore flat satisfiability is preserved.  There are `r` zero-to-one leaf changes and one one-to-zero center change, so the Hamming weight increases by `r-1>0`.  QED.

### Consequence 3.2

Choose, from all flat-satisfying assignments represented by a fixed formula, one maximizing the number of true light variables.  Such a maximizer has no completed `r`-block from Lemma 3.1.  As in the Díaz local-max reduction, a false light variable with no blocker could itself be flipped to one, so a Hamming maximizer is included among the flat-prime assignments counted by their extended type system.

Thus every satisfiable simple formula has a representative counted by Díaz that is **`r`-block-free for every `r>=2`**.  It is therefore legitimate, for an upper bound, to count only `r`-block-free representatives.

This avoids the run-2 rescue-star counterexample: the leaves have no `ns2` occurrences at all, while all center `ps` losses are protected by fixed external `ns2` anchors.

## 4. Exact finite copy-allocation law

Fix one Díaz coarse type tuple `x`.  Write its scaled counts

`P=ell_ps`, `L1=ell_ns1`, `U=ell_nu`,

`E=f_{1,1,1}`, `C_r=t_{r,r}`, `Q=c_a`, `B=c_b`.             (4.1)

The equalities `Q=c_a` and `B=c_b` hold because type `a` has one `ps` slot and type `b` has one `ns1` slot.  Type `b` also has exactly one canonical `nu` slot.

Díaz's copy-allocation factor is a uniform bijection within each label class.  Therefore the following statements are exact conditional on the integer coarse counts (up to the unavoidable `O(1)` rounding when densities are multiplied by `n`).

### 4.1 Selected blockers

There are `En` marked `f_{1,1,1}` `ns1` copies among `L1 n` total `ns1` copies and `Bn` type-`b` slots.  Hence the number `S_n` of selected leaves is hypergeometric and

`E S_n = (E B/L1)n + O(1)`.                                 (4.2)

Put

`s(x)=E B/L1`.                                                (4.3)

For a fixed interior tuple, `s(x)>0`, and the hypergeometric lower-tail inequality gives

`P(S_n <= s(x)n/2) <= exp[-c_S(x)n]`                         (4.4)

for some `c_S(x)>0` and all large `n`.

### 4.2 Available centers

There are `C_r n` disjoint groups of `r` `ps` copies belonging to the `t_{r,r}` centers.  Their targets are a uniformly random injection into the `Pn` `ps` slots, of which `Qn` are safe type-`a` slots.  If `A_{r,n}` counts groups all of whose `r` targets are safe, then exactly

`E A_{r,n} = C_r n * (Qn)_r/(Pn)_r`,                         (4.5)

so

`E A_{r,n}/n -> a_r(x):=C_r (Q/P)^r`.                        (4.6)

Under a transposition of two target positions, `A_{r,n}` changes by at most two.  The bounded-difference inequality for random permutations therefore gives, for every fixed interior tuple,

`P(A_{r,n} <= a_r(x)n/2) <= exp[-c_{A,r}(x)n]`               (4.7)

for some `c_{A,r}(x)>0` and all large `n`.  This is the only concentration input needed for centers; no independence approximation is used.

### 4.3 Conditional `nu` matching

The `ps`, `ns1`, and `nu` copy bijections are separate label-class matching factors.  Conditional on the selected leaves and available centers, the `S_n` canonical rescue slots are distinct, and their preimages under the uniform `nu` bijection form a uniformly random `S_n`-subset of the `U n` `nu` copies.  Every available center contributes one disjoint marked block of its `r` `nu` copies.

Therefore `r`-block-freeness is exactly the finite combinatorial event:

> choose `S` points uniformly from `U` points containing `A` disjoint marked `r`-sets, and do not contain any marked `r`-set completely.

## 5. A finite exact `r`-block avoidance theorem

Let `N_{r,0}(U,A,S)` be the number of `S`-subsets avoiding all `A` disjoint marked `r`-sets, where `rA<=U`.

### Proposition 5.1 — coefficient identity

`N_{r,0}(U,A,S)`

` = [z^S] (((1+z)^r-z^r)^A (1+z)^(U-rA)).`                 (5.1)

#### Proof

For each marked `r`-set, every proper subset is allowed, giving generating polynomial

`sum_{j=0}^{r-1} C(r,j) z^j = (1+z)^r-z^r`.

Each of the `U-rA` unmarked points contributes `1+z`.  Multiplying independent choices and extracting the size-`S` coefficient proves (5.1).  QED.

For `r=2` this reduces to the explicit sum from the previous run,

`sum_j C(A,j)2^j C(U-2A,S-j)`.

### Proposition 5.2 — self-contained finite exponential bound

For `0<=S<=U`,

`N_{r,0}(U,A,S)/C(U,S)`

` <= min{1, (U+1)[1-(S/U)^r]^A}.`                           (5.2)

#### Proof

The cases `S=0` and `S=U` are immediate (for `S=U` and `A>0` the left side is zero).  Assume `0<S<U` and put

`z=S/(U-S)>0`.

Since all coefficients in (5.1) are nonnegative,

`N_{r,0}(U,A,S)`
` <= z^{-S} ((1+z)^r-z^r)^A (1+z)^(U-rA)`.                 (5.3)

Let `p=S/U=z/(1+z)`.  For `X~Bin(U,p)`, `S` is a mode because

`floor((U+1)p)=floor(S+S/U)=S`.

A mode of a distribution on `U+1` values has mass at least `1/(U+1)`.  Hence

`C(U,S) z^S/(1+z)^U = P(X=S) >= 1/(U+1)`,                  (5.4)

or

`C(U,S) >= (U+1)^(-1) z^{-S}(1+z)^U`.                     (5.5)

Dividing (5.3) by (5.5) yields

`P(no completed block)`
` <= (U+1) [1-(z/(1+z))^r]^A`
` = (U+1)[1-(S/U)^r]^A`.

The additional minimum with one is trivial.  QED.

No Stirling approximation or independence assumption appears in Proposition 5.2.

## 6. The Díaz interior-transfer theorem

### Theorem 6.1

Fix a Díaz coarse type `x` with

`P,L1,U,E,C_r,Q,B > 0`                                      (6.1)

for some fixed `r>=2`.  Among copy allocations with that coarse type, the fraction that can support a Hamming-weight-maximal flat-satisfying assignment is at most

`exp[-kappa_r(x)n+o(n)]`                                    (6.2)

for some `kappa_r(x)>0`.

More explicitly, the block-avoidance part alone supplies on the typical event

`kappa_r^block(x)`
` := -(a_r(x)/2) log(1-(s(x)/(2U))^r) > 0`,                 (6.3)

and one may take

`kappa_r(x)=min{c_S(x),c_{A,r}(x),kappa_r^block(x)}`        (6.4)

up to an arbitrarily small large-`n` slack.

#### Proof

By (4.4) and (4.7), except on probability at most

`exp[-c_S n]+exp[-c_{A,r}n]`,

we have

`S_n >= s n/2`, `A_{r,n} >= a_r n/2`.                      (6.5)

On this event apply Proposition 5.2 with `U_n=Un+O(1)`.  Since the right side decreases as `A` and `S` increase,

`P(r-block-free | typical ps,ns1 matchings)`
` <= (Un+O(1)+1) [1-(s/(2U)+o(1))^r]^(a_r n/2+o(n))`
` = exp[-kappa_r^block(x)n+o(n)]`.                          (6.6)

Adding the two atypical matching probabilities proves (6.2)--(6.4).  By Consequence 3.2 every Hamming-maximal representative must be block-free, so this is exactly a relative count penalty on the representative family.  QED.

### Corollary 6.2 — all fixed finite `r` at the published interior saddle

At the Díaz interior stationary point, their displayed Lagrange formulas have positive multipliers and give positive masses for every allowed finite light class in question, including `f_{1,1,1}`, `t_{r,r}`, and the two clause types `a,b`.  Therefore Theorem 6.1 applies for every

`2<=r<=M=23`.                                                (6.7)

This produces **22 distinct deterministic rescue-block penalties**, all derived from the same exact finite matching law but using different center degrees.  Before this run the previous PROB10-04 report had only an unconditional blocker-occupancy exponent and explicitly left the Díaz configuration-model transfer unpaid.

## 7. What the theorem buys in the Díaz variational optimization

The source's `M=23` proof reduces the representative count to a finite-dimensional compact feasible polytope with a continuous exponential objective `F_gamma(x)`.  At `gamma=4.4898` the source optimization identifies its controlling maximizer as isolated and interior.

Fix any `r>=2`, say `r=2`.  By Corollary 6.2, `kappa_r(x_*)>0`.  All densities entering (6.3) are continuous rational functions of the coarse coordinates away from zero; the standard matching large-deviation constants in (4.4), (4.7) are uniformly positive once the corresponding means stay bounded below.  Hence there is a neighborhood `N` of `x_*` and `kappa_N>0` such that every tuple in `N` gets at least `exp(-kappa_N n+o(n))` relative penalty.

Because `x_*` is an isolated global maximizer and the feasible set is compact, there is `eta_N>0` with

`sup_{x notin N} F_gamma(x) <= F_gamma(x_*) exp(-eta_N)`.    (7.1)

Inside `N`, the refined representative count has base at most

`F_gamma(x_*) exp(-kappa_N)`.                               (7.2)

Outside `N` we need no rescue estimate and retain (7.1).  Consequently the refined Díaz count has a strictly smaller exponential base than the unrefined Díaz maximum:

`F_gamma^ref <= F_gamma(x_*) exp[-min(eta_N,kappa_N)]`
`             < F_gamma(x_*)`.                              (7.3)

This is the substantive transfer that run 4 was missing.  It is a strict **variational mechanism improvement at the same gamma**, not yet a new certified density endpoint.

Why I do **not** turn (7.3) into `alpha_U<4.4898` here: a numerical source improvement requires a quantitative, interval-certified neighborhood/global gap and continuation of the source core/type estimates to a lower gamma.  Merely saying that all ingredients look continuous would recycle the old tiny-slack issue and violate the owner's requirement that a source endpoint movement be proved rather than inferred.

## 8. Negation test: the penalty cannot be made uniform over the whole polytope by this argument alone

I also tried the stronger statement

`inf_{x feasible} kappa_r(x) > 0`.                           (8.1)

It is false as an inference from the present mechanism.  The Díaz feasible polytope has boundary faces on which at least one of `t_{r,r}`, `f_{1,1,1}`, `c_a`, or `c_b` vanishes.  Along such a sequence either

`a_r(x)=t_{r,r}(c_a/ell_ps)^r ->0`

or

`s(x)=f_{1,1,1}c_b/ell_ns1 ->0`,

and (6.3) tends to zero.  Taking all `r=2,...,23` does not by itself remove boundary faces where the common leaf or blocker mass vanishes.

So the correct way to use the result is the localized variational argument in Section 7, not a fictitious all-types constant.  This is precisely why the source's isolated-interior-maximizer information matters.

## 9. Three materially different attacks this run

### Attack A — deterministic degree-`r` copy-allocation obstruction: **SUCCESS**

I replaced the preceding fixed-assignment occupancy model by an exact Díaz-type matching statement.  The `t_{r,r}` / `f_{1,1,1}` construction yields the local rescue lemma, exact coefficient identity (5.1), exact finite bound (5.2), and positive interior exponent (6.3).

### Attack B — localize the penalty at the source variational maximizer: **SUCCESS QUALITATIVELY / NOT YET NUMERIC**

Compactness plus the source's isolated interior maximizer converts the pointwise defect into a strict reduction of the old Díaz exponential base, equation (7.3).  The missing source-level step is now quantitative and finite-dimensional: certify an explicit neighborhood/global gap and repeat the optimization at some `gamma<4.4898`.

### Attack C — demand one uniform rescue exponent on every feasible type: **NEGATION FOUND**

Boundary degeneration kills that stronger route: selected variable/clause masses can tend to zero, forcing the rescue exponent to zero.  This rules out spending another run trying to prove a global positive `kappa` without first localizing the objective.

I deliberately did **not** duplicate NM13-13's two-survey interpolation route.  Its `4.418` result is a separate current candidate that needs independent validation under the repository contract; another copy of the same interpolation calculation would not be a new research method.

## 10. Exact tests actually run

### Pair case `r=2`

Executed:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-49-00Z__diaz_degree2_pair_avoidance_exact.py`

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-49-30Z__diaz_degree2_pair_avoidance_exact.out`.

It brute-force checks the exact subset formula in **202** small cases and the finite inequality in **12,128** exact rational cases.  It also checks the algebraic saddle identity.  Output ends

`ALL_EXACT_CHECKS_PASS = True`.

### General `r`-block case

Executed:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-54-00Z__diaz_rblock_avoidance_exact.py`

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T03-54-30Z__diaz_rblock_avoidance_exact.out`.

It exhaustively compares brute subsets with (5.1) in **596** small `(U,r,A,S)` cases and verifies (5.2) in **15,937** exact rational cases, then checks the coefficient-bound algebra for `r=2,...,6`.  Output ends

`ALL_EXACT_RBLOCK_CHECKS_PASS = True`.

These are self-checks of the finite combinatorial core, not independent audits.

## 11. Before / after ledger

### Source-level verified explicit-decimal metric

- lower endpoint: `3.52 -> 3.52`;
- externally recovered explicit upper endpoint used conservatively by this worker: `4.4898 -> 4.4898`;
- width: `0.9698 -> 0.9698`;
- exact limiting `k=3` threshold: still **OPEN**.

### Current repository candidate, kept separate

- neighboring candidate upper endpoint: `4.418 -> 4.418`;
- candidate width: `0.898 -> 0.898`;
- status of that endpoint here: **consumed neighboring CANDIDATE_FULL; not independently validated by this track**.

### Auxiliary mechanism delta

Before this run:

- previous PROB10-04 report had a positive exact blocker-occupancy rate under a fixed satisfying assignment;
- transfer into the Díaz degree/type copy-allocation model was explicitly **missing**.

After this run:

- exact Díaz transfer exists for the deterministic `r`-block family `2<=r<=23`;
- number of proved fixed-degree transfer classes: `0 -> 22`;
- at every fixed interior type satisfying (6.1), a rigorous positive exponent `kappa_r(x)` is given by (6.3)--(6.4);
- at the source's isolated interior maximizer, the old Díaz exponential base receives a strict relative reduction (7.3);
- no new density decimal is claimed.

## 12. Remaining full-scope gap and next nonduplicating step

The unresolved source problem remains enormous: neither this mechanism nor the neighboring `4.418` upper-bound candidate proves convergence/identification of the exact random 3-SAT threshold, and no lower endpoint moved.

For **this** scoped route, another local rescue checker would now be waste.  The next substantive step should be one of the following, in order:

1. reconstruct the Díaz `M=23` objective at `gamma=4.4898` with interval arithmetic, append the `r=2` correction, and obtain an explicit certified global margin `delta_D>0` rather than only (7.3);
2. continue that same certified objective to a specific lower rational density, e.g. search downward from `4.4898`, and only then claim a source endpoint improvement if the entire refined maximum is `<1`;
3. if the neighboring `4.418` interpolation candidate passes independent audit before this is done, do **not** chase a weaker Díaz decimal merely for a number; instead use the present deterministic block constraint as a possible extra order-parameter restriction in a genuinely different interpolation/cluster functional, with a proof of the coupling rather than an analogy.

The precise present obstruction is therefore **global quantitative reoptimization**, not local composition or blocker occupancy.  Status remains **PARTIAL / OPEN** until a source endpoint or the exact threshold statement itself is proved and independently validated.
