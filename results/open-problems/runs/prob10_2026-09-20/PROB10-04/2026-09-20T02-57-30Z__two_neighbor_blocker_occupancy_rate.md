Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the scheduler exposes no model/effort selector and no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum. FOURTH CONSECUTIVE SOURCE-METRIC NONMOVEMENT: explicit-decimal bracket `[3.52,4.4898]`, width `W=0.9698 -> 0.9698`; method changed as required.**

# PROB10-04 run 4 — exact two-neighbor blocker occupancy and the clean-center exponential rate

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **source OPEN / PROB10-04 PARTIAL**.

## 1. Continuity, ownership, and consumed evidence

This run continues the scoped **cluster-aware weighted-counting / overlap-variational** route in `operations/claims/PROB10-04.md`; it does not take over the neighboring constructive lower-bound route.

Consumed before new mathematics:

- `operations/PROB10_2026-09-20.md` on current master;
- current root `POSTED.md` exclusion registry;
- `operations/claims/PROB10-04.md`;
- run 1 `runs/prob10_2026-09-20/PROB10-04/2026-09-19T23-59-30Z__cluster_weight_barrier_component_quotient.md`;
- run 2 `runs/prob10_2026-09-20/PROB10-04/2026-09-20T00-58-00Z__global_max_radius3_flip_accessibility.md`;
- run 3 `runs/prob10_2026-09-20/PROB10-04/2026-09-20T02-18-00Z__clean_rescue_center_penalty_and_third_run_obstruction.md`;
- immutable predecessor handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, preserving HARD7-06's actual F0095/binary-cascade work;
- newest neighboring constructive report found in `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T04-27-22__t04_majority_two_choice_repair.md`, which is a distinct constructive lower-bound mechanism and reports no source endpoint movement.

The idea was written before code in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T02-52-00Z__two_neighbor_blocker_occupancy_idea_before_code.md`.

Fresh source check used:

- Díaz--Kirousis--Mitsche--Pérez-Giménez, `https://arxiv.org/abs/0807.3600`, Theorem 1.1: `4.4898` is a rigorous a.a.s.-UNSAT upper bound for random proper 3-CNF;
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *Combinatorics, Probability and Computing* 35 (2026), published online 27 March 2026, `https://doi.org/10.1017/S0963548326100406`: for small `k`, including `k=3`, existence of one uniform satisfiability threshold remains open; the paper records the best current lower statement as `d_sat(3)>=10.56`, i.e. clause density `alpha>=3.52`, and states that interpolation gives a rigorous variational upper bound matching the 1RSB prediction, while its displayed `d_sat(3)≈12.801` number is explicitly presented as the physics prediction;
- Caragiannis--Gravin--Jiang, ESA 2025, `https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103`, remains a different k-wise-independent clause model.

Therefore this run does **not** turn the physics decimal `12.801/3` into an unchecked rigorous source endpoint. The explicit-decimal source metric remains `[3.52,4.4898]`.

## 2. Why the method had to change

Run 3 already triggered the three-unchanged-run rule. It proved a correct clean-rescue-center composition lemma, but paid for the absence of clean centers through McDiarmid applied to the total center count. At `alpha=4.4898`, zero density `rho=0.46`, that produced only

`3.8125729995e-9 n`

in the exponent. Another bounded-difference lemma on the same count would not be a new method.

The present run changes category from concentration of a count to **exact sparse occupancy of blocker neighborhoods**. It uses both false neighbors of each unique blocker and computes the no-collision large-deviation rate explicitly.

## 3. Fixed-assignment conditioned blocker process

Fix a deterministic assignment `sigma`, let

`Z={v:sigma_v=0}`, `O={v:sigma_v=1}`, `|Z|/n -> rho`,

and condition on `sigma` satisfying all `m=floor(alpha n)` independent proper clauses.

For a clause `C`, let `T_C` be the variables whose literals are true under `sigma`. Call `C` **critical at v** if `T_C={v}`, and let `K_v` be the number of clauses critical at `v`.

Under the conditioning `C(sigma)=1`, the variable triple stays uniform and the truth set is uniform over the seven nonempty subsets of its three variables. Hence for every `v`

`P(C critical at v | C(sigma)=1) = 3/(7n)`.      (3.1)

Thus the `m` clause categories consist of `n` critical-source categories, each of probability `3/(7n)`, and one noncritical category of probability `4/7`.

If `x in Z` and `K_x=1`, call `x` an **eligible leaf**, and let `N_x` be the two false-variable positions in its unique blocker. If `y in O` and `K_y=0`, call `y` an **available center**.

Conditional on the full critical-source category vector, the sets `N_x` of distinct eligible leaves are independent and each is a uniform 2-subset of `[n]\{x}`. Since `x in Z` and every available center lies in `O`, every available center is allowed for every eligible leaf.

A **raw center** is an available `y` lying in `N_x cap N_z` for two distinct eligible leaves `x,z`.

By run 3's exact clause identity, if no higher-truth clause interferes on `S={x,z,y}`, then flipping `S` gives a satisfying assignment of Hamming weight one larger. Therefore a global Hamming-weight maximum can have a raw center only if every usable leaf pair at that center is spoiled by a higher-truth clause. The old four-variable counterexample is thus retained as a negation test rather than ignored.

## 4. Exact finite no-raw-center probability

Condition on exactly `L` eligible leaves and `A` available centers. Put

`B=n-1-A`.

Each eligible leaf independently chooses one target pair among `C(n-1,2)` possibilities.

Suppose:

- `s` leaves choose two available centers;
- `t` leaves choose exactly one available center;
- `r=L-s-t` leaves choose none;
- `h=2s+t` available-center incidences occur.

No raw center means all `h` available-center incidences are at distinct center vertices. Therefore the exact number of target-pair configurations with no raw center is

`N_0(n,L,A)`

`= sum_{s,t >=0; s+t<=L; 2s+t<=A}`

`    [L!/(s! t! (L-s-t)!)] (A)_{2s+t} 2^{-s} B^t C(B,2)^{L-s-t}`.      (4.1)

Here `(A)_h=A(A-1)...(A-h+1)`. The factor `2^{-s}` is necessary because the two available-center positions of a two-center target pair are unordered.

Hence

`P_0(n,L,A)=N_0(n,L,A)/C(n-1,2)^L`.      (4.2)

This is an exact finite identity, not a simulation.

### Exact checker

The matching checker

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T02-56-00Z__two_neighbor_occupancy_checker.py`

brute-forces the target-pair space for four small cases and compares it to (4.1). Archived output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T02-56-30Z__two_neighbor_occupancy_checker.out`.

It records exact integer identities

- `(n,L,A)=(8,3,2)`: `5800=5800` out of `9261`;
- `(9,2,3)`: `640=640` out of `784`;
- `(7,3,1)`: `2500=2500` out of `3375`;
- `(10,2,4)`: `1046=1046` out of `1296`;

and ends `ALL_EXACT_FINITE_CHECKS_PASS = True`.

These are self-checks, not independent audits.

## 5. Full asymptotic no-collision rate and scalar saddle

Assume

`L/n -> ell in (0,1)`, `A/n -> a in (0,1)`.

Write

`u=s/n`, `v=t/n`, `r=ell-u-v`, `h=2u+v`, `b=1-a`.

Applying Stirling's formula termwise to (4.1), with only polynomially many `(s,t)` terms, gives

`(1/n) log P_0(n,L,A) -> Psi(ell,a)`,      (5.1)

where

`Psi(ell,a)=max_D Phi(u,v;ell,a)`,      (5.2)

`D={u,v,r>=0, 2u+v<=a}` and

`Phi = ell H_3(u/ell,v/ell,r/ell)`
`      + a log a - (a-h) log(a-h) - h`
`      + (2r+v) log(1-a) + v log 2`.      (5.3)

Here `H_3(p,q,r)=-p log p-q log q-r log r`.

The objective is strictly concave on the interior: the multinomial entropy is concave, the `h`-term has second derivative `-1/(a-h)`, and the remaining terms are linear. Its derivatives are

`dPhi/du = log(r/u) + 2 log(a-h) - 2 log(1-a)`,      (5.4)

`dPhi/dv = log(2r/v) + log(a-h) - log(1-a)`.         (5.5)

At the unique interior maximizer define

`q=(a-h)/(1-a)>0`.

Equations (5.4)--(5.5) give

`u=r q^2`, `v=2 r q`.      (5.6)

Since `ell=u+v+r`,

`r=ell/(1+q)^2`,
`v=2 ell q/(1+q)^2`,
`u=ell q^2/(1+q)^2`,
`h=2 ell q/(1+q)`.         (5.7)

Substituting the definition of `q` yields the scalar quadratic

`(1-a) q^2 + (1-2a+2ell) q - a = 0`.      (5.8)

Thus

`q = [-(1-2a+2ell) + sqrt((1-2a+2ell)^2 + 4a(1-a))]/[2(1-a)]`.      (5.9)

Equations (5.3), (5.7), (5.9) give the no-raw-center exponent in closed form:

`kappa_2(ell,a) := -Psi(ell,a) > 0`.      (5.10)

Strict positivity also follows probabilistically because with `ell,a>0` a linear number of independent two-target throws into a linear monitored center set produces linearly many collision opportunities; the exact formula above quantifies that large deviation.

This eliminates the run-3 square-loss: there is no concentration inequality applied to the number of raw centers in (5.1).

## 6. Higher-truth interference does not change the exponential rate

A raw center is not automatically clean, so this must be paid rather than assumed away.

Let `R` be the number of raw centers. Consider the bipartite graph between eligible leaves and available centers with edges `x--y` iff `y in N_x`. Every leaf has degree at most two. Every raw center has degree at least two.

### Lemma 6.1 — disjoint-star packing

From `R` raw centers one can select at least `R/3` centers together with two incident leaves each so that the resulting 3-variable sets `{x,z,y}` are pairwise disjoint.

**Proof.** Greedily select a raw center and two incident leaves. Delete that center and every center adjacent to either selected leaf. Since each leaf has degree at most two, besides the chosen center each selected leaf can delete at most one further center. Thus each greedy selection removes at most three raw centers. The selected leaves and centers are then disjoint across steps. QED.

Fix one selected disjoint star `S={x,z,y}`. Conditional on a clause being satisfying and **noncritical**, its truth pattern is uniform over the four patterns of size two or three.

A noncritical clause spoils `S` only in either of the following cases:

1. its variable triple contains exactly two variables of `S`, those two literals are true and the outside literal is false;
2. its variable triple is exactly `S` and all three literals are true.

Therefore the exact conditional spoiling probability for one fixed star is

`p_int(n) = [3(n-3)+1]/[4 C(n,3)] = (3n-8)/[4 C(n,3)] = O(n^-2)`.      (6.1)

One clause cannot spoil two pairwise-disjoint stars, because spoiling a star uses at least two of its variables.

If `R>=delta n`, Lemma 6.1 supplies at least `delta n/3` pairwise-disjoint stars. Conditional on the critical structure, the remaining noncritical clauses are independent. Each hits the selected star family with probability `O(1/n)`, so their expected number of spoiling hits is `O(1)`. Requiring at least `delta n/3` distinct spoiling clauses has probability

`exp[-Omega(n log n)]`.      (6.2)

On the other hand, if `R<=delta n`, then all raw centers lie in some set `D` of at most `delta n` available centers. Removing `D`, the remaining `A-|D|` center bins have no collision. Hence, by a union bound,

`P(R<=delta n | L,A)`
` <= sum_{j<=delta n} C(A,j) P_0(n,L,A-j)`.      (6.3)

By (5.1) and continuity of `Psi`, the exponential rate of the right side tends to `Psi(ell,a)` as `delta -> 0` after `n -> infinity`.

Combining (6.2)--(6.3) with the lower bound `P(no raw center)=P_0`, the event **no clean rescue center** has the same exponential rate as the exact no-raw-center occupancy event:

`(1/n) log P(no clean center | L/n->ell, A/n->a, sigma satisfies) -> Psi(ell,a)`.      (6.4)

Thus the higher-truth counterexample mechanism from run 2/run 3 changes only subexponential factors on this regular blocker scale; it does not erase the occupancy exponent.

This is the main proved mechanism theorem of the run.

## 7. Random-3-SAT specialization

From the multinomial source process (3.1), with

`lambda=3 alpha/7`,

standard occupancy expectations and bounded-difference concentration give

`L/n -> ell(rho,alpha)=rho lambda exp(-lambda)`,      (7.1)

`A/n -> a(rho,alpha)=(1-rho) exp(-lambda)`           (7.2)

with exponentially small deviations of any fixed size.

At the source comparison point

`alpha=4.4898`, `rho=0.46`,

we obtain

`lambda=1.9242`,
`ell=0.1292226371871969...`,
`a=0.07883595224337876...`.

The scalar saddle (5.9) gives

`q=0.06777476789892581...`,
`u=0.0005206134331342639...`,
`v=0.015363045843570207...`,
`r=0.11333897791049242...`,

and

`kappa_2 = 0.002286901727877145...`.      (7.3)

The checker also evaluates exact finite (4.1) rates for `n=100,200,500,1000`, which sit near `-0.00228`, consistent with (7.3). Those decimals are numerical evaluations of the proved formula, not interval-certified constants.

For comparison:

- run 3 safe McDiarmid clean-center penalty at this point: about `3.81e-9`;
- one-neighbor thinning occupancy rate: about `6.12e-4`;
- full two-neighbor exact rate here: about `2.287e-3`.

So the new representation removes roughly six orders of magnitude of avoidable exponent loss relative to run 3's safe concentration payment.

## 8. Auxiliary first-moment consequence and its limitation

If one inserts `kappa_2(rho,alpha)` into the **unrefined** first moment for maximum-weight satisfying representatives, the formal exponent becomes

`G_alpha(rho)=h(rho)+alpha log(7/8)-kappa_2(rho,alpha)`.      (8.1)

A floating-point one-dimensional maximization and bisection in the checker gives an auxiliary crossing near

`alpha≈5.18059221886`, `rho≈0.4994041`.      (8.2)

This improves the preceding run's disjoint-triple auxiliary crossing `5.18851948`, but it is still far weaker than the already rigorous source upper endpoint `4.4898`. Moreover (8.2) is not interval certified, so it is recorded as **auxiliary numerical evidence**, not a new theorem endpoint.

The source metric therefore correctly remains unchanged.

## 9. Three materially different attacks this run

### Attack A — exact two-neighbor blocker occupancy: SUCCESS

Instead of concentrating a pre-counted number of clean centers, count the entire blocker-neighborhood occupancy event. This produced the exact finite formula (4.1), the closed scalar saddle (5.8)--(5.9), and the interference-stable exponential rate (6.4).

### Attack B — insert the penalty into the Díaz near-maximizer polytope: PARTIAL, exact missing transfer identified

Díaz et al. do not condition merely on `sigma satisfies`; they condition on Poisson two-dimensional degree data, pure-literal-core evolution, positive unbalancing, clause-sign-profile constraints, and a single-flip representative count. Under this conditioning the simple multinomial source law (3.1) is no longer available for free.

The exact missing source-level lemma is now sharper than run 3's generic clean-center statement:

> **Díaz-blocker occupancy transfer.** Extend each feasible Díaz configuration type `x` by the densities `ell(x)` of zero variables with exactly one critical blocker and `a(x)` of one variables with no critical blocker, and prove uniformly for every type with `F_4.4898(x)>=-delta` that (i) `ell(x),a(x)` are bounded below by explicit positive constants, (ii) conditional blocker target pairs obey an occupancy LDP with rate at least `kappa_2(ell(x),a(x))-o(1)`, and (iii) the configuration-model-to-simple-formula error remains `o(n)` in the exponent.

Once this is proved, the old Díaz objective is reduced by a uniform positive amount near every maximizer. That is a credible route to an actual endpoint improvement. This run does **not** assume the transfer.

### Attack C — certify the interpolation/1RSB upper decimal directly: BLOCKED BUT SOURCE-CLARIFYING

The 27 March 2026 CPC paper explicitly says the interpolation method yields a rigorous variational upper bound matching the 1RSB prediction, but its table's `d_sat(3)≈12.801` is still labelled the physics prediction. A bounded search did not produce an interval-certified k=3 evaluation whose hypotheses and normalization can simply be imported as a decimal source endpoint. Therefore I did not replace `4.4898` by `12.801/3`.

The shortest separate route is to reconstruct the exact Franz--Leone / Panchenko--Talagrand zero-temperature functional for the iid proper-clause normalization, then interval-evaluate one admissible trial order parameter. That would be a source-baseline certification project, not a proof of the exact threshold.

## 10. Before/after ledger

### Source-level metric

- rigorous lower endpoint: `3.52 -> 3.52`;
- explicit-decimal rigorous upper endpoint used by this track: `4.4898 -> 4.4898`;
- width: `0.9698 -> 0.9698`;
- source status: **OPEN**; exact limiting threshold for `k=3` still not proved to exist/identified.

### Mechanism progress

- clean-center exponential payment at `alpha=4.4898,rho=0.46`: prior safe bound about `3.81e-9` in exponent;
- new regular-blocker exact occupancy rate: `kappa_2≈0.002286901727877145` from a proved closed formula;
- finite no-collision identity: now exact for all `n,L,A` via (4.1), with four brute-force integer checks archived;
- prior auxiliary local-max crossing `5.18851948` -> new floating-point auxiliary crossing `5.18059222` (numerical only, not source progress).

## 11. Remaining full-scope gap and next method

The decisive unpaid obligation is **not** another clean-center concentration estimate. It is the Díaz-blocker occupancy transfer stated in Attack B, or an independently certified interpolation functional yielding a rigorous smaller upper decimal.

The next run should therefore avoid another standalone local-max checker. It should do one of:

1. derive `ell(x),a(x)` inside the Díaz configuration variables and prove a uniform lower occupancy rate over a certified near-maximizer region; or
2. reconstruct one explicit admissible 1RSB interpolation trial and interval-certify its k=3 zero-temperature value.

A restricted transfer remains PARTIAL. Source closure still requires the full exact classical iid model, complete proof, current prior-art check, and independent validation under the repository contract.