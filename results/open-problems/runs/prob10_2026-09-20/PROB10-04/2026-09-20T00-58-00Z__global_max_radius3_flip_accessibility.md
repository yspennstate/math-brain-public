Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-reasoning telemetry is exposed, so I do not claim GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: `W=4.4898-3.52=0.9698 -> 0.9698`.**

# PROB10-04 run 2 — global-max flip accessibility, a killed rescue-star shortcut, and the radius-3 route

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **source OPEN / PROB10-04 PARTIAL**.

## 1. Continuity, ownership, and consumed updates

This run stayed on the scoped PROB10-04 cluster-aware weighted-count / overlap-variational route. It did not take over the neighboring constructive lower-bound worker.

Consumed before research:

- `operations/PROB10_2026-09-20.md` on current master;
- root `POSTED.md` on current master;
- `operations/claims/PROB10-04.md`, which keeps this route scoped to cluster-aware counting and preserves historical R03/F0097 ownership/handoff;
- preceding own report `runs/prob10_2026-09-20/PROB10-04/2026-09-19T23-59-30Z__cluster_weight_barrier_component_quotient.md`;
- HARD7-06 handoff `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, which preserves F0095/binary-cascade work rather than relabeling it;
- newest neighboring constructive report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T03-28-00__t04_rho_barrier_control.md`. That worker remains on the Hajiaghayi--Sorkin constructive degree-spectrum/unit-cascade route and reports no source endpoint movement; the present run remains nonduplicating.

The preceding PROB10-04 run proved a clause-local weighted-second-moment barrier and showed that dividing by solution-graph balls of radius `o(n/log n)` cannot pay an exponential overlap defect. It then introduced the full-component quotient `Q(F)=#components`. The unpaid obligation there was a usable nonlocal cross-component moment bound.

I did **not** restart that same unpaid lemma. This run changed the object counted on the upper-bound side: every satisfiable formula has a satisfying assignment of globally maximum Hamming weight, so every finite Hamming-weight-improving flip pattern is forbidden at that representative.

## 2. Fresh source status and source metric

A bounded current check on 20 September 2026 reconfirmed:

- Hajiaghayi--Sorkin, `https://arxiv.org/abs/math/0310193`: random 3-SAT is satisfiable w.h.p. below density `3.52`;
- Diaz--Kirousis--Mitsche--Perez-Gimenez, `https://arxiv.org/abs/0807.3600`: random 3-SAT is unsatisfiable w.h.p. at density at least `4.4898`;
- Caragiannis--Gravin--Jiang, ESA 2025, `https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103`: their `k`-wise-independent model is different from the classical iid-clause model; the classical `k=3` location remains open;
- Gaia Carenini, ECCC TR26-145, `https://eccc.weizmann.ac.il/report/2026/145/`: for every fixed `k>=3` the scaling window is `O(n/log n)`. This does not prove convergence or identify a limiting density;
- Maneva--Sinclair, `https://arxiv.org/abs/0710.0805`: the `4.453` result concerns absence of nontrivial cores, not an unconditional `3-SAT` UNSAT threshold;
- the 2008 Diaz et al. paper explicitly records local-max/single-flip methods as prior art. Therefore this report makes **no novelty claim** for the general idea of finite-radius local maxima.

Frozen source metric:

`alpha_L=3.52`, `alpha_U=4.4898`, `W=0.9698`.

Before / after:

`W: 0.9698 -> 0.9698`.

No physics value, scaling-window result, core threshold, finite search, or local-max auxiliary estimate is substituted for source movement.

## 3. Approach A — full-component quotient: exact cancellation remains, but the same kernel is still unpaid

The previous exact identity

`Q(F)=sum_{sigma in Sol(F)} 1/|K_F(sigma)| = #components`

and its same-component cancellation remain correct. I tried to turn it into a usable Paley--Zygmund variable by bounding `E Q` through same-component pair mass. Deterministically, if `V=#Sol(F)` and `S=sum_K |K|^2`, then

`Q >= V^2/S`.

Taking expectations and Cauchy gives

`E Q >= (E V)^2 / E S`.

This is correct but does not close the route: a second-moment bound for `Q` still needs cross-component control, while `E S` itself is the probability-weighted count of pairs connected by satisfying single-flip paths. Bounding that by all overlap pairs simply restores the old assignment second-moment obstruction. Thus the component quotient did not move the source metric in this run.

This route is not abandoned, but it is no longer the only nonlocal mechanism.

## 4. Approach B — global Hamming maximum and exact flip-set accessibility

### 4.1 Canonical representative

For every satisfiable formula `F`, choose a satisfying assignment `sigma` with maximum Hamming weight `|sigma|_1`. Then for every flip set `S` such that the endpoint `sigma^S` is satisfying,

`# {v in S: sigma_v=0} <= # {v in S: sigma_v=1}`.        (4.1)

This uses a **global** maximum over all satisfying assignments, not merely a component maximum. It therefore avoids the previous need to know whether an improving endpoint lies in the same solution component.

### 4.2 Exact clause identity

Fix a clause `C`. Relative to `sigma`, let

- `T_C` be the set of variables whose clause literals are true under `sigma`;
- `F_C` be the set of variables whose clause literals are false under `sigma`.

Because `sigma` satisfies `C`, `T_C` is nonempty. After flipping variables in `S`, exactly the literals indexed by

`(T_C \ S) union (F_C intersect S)`

are true. Hence

`C(sigma^S)=TRUE  <=>  (T_C not subset S) or (F_C intersect S != empty)`.   (4.2)

Equivalently,

`T_C subset S  =>  F_C intersect S != empty`.                            (4.3)

This is an exact signed-hypergraph reformulation of every endpoint flip constraint. For a path with flip order `v_1,...,v_r`, each prefix `S_j={v_1,...,v_j}` must satisfy (4.3).

This formulation is the main conceptual gain of the run. The radius-3 problem is not an occupancy problem on critical clauses alone: clauses with two or three initially true literals can become newly critical or false after earlier flips.

## 5. Negation test — the tempting radius-3 rescue-star lemma is false

I first tried the following shortcut.

Let `y` be a one-variable (`sigma_y=1`) with no critical clause, so flipping `y:1->0` is allowed. Let `x` be a zero-variable with exactly one critical blocker and suppose that blocker contains the false literal `not y`. Then `y` appears to rescue `x`. The tempting claim was:

> if one flippable `y` rescues two distinct unique-blocked zeros, then `y` down followed by both zeros up gives a satisfying assignment of Hamming weight `|sigma|+1`.

That claim is false. The negation search found an exact four-variable/four-clause counterexample.

Clauses:

`(-0,-1,-3)`

`(+0,-2,-3)`

`(+1,-2,-3)`

`(-1,-2,+3)`.

Take

`sigma=(1,1,0,0)`.

Its satisfying connected component has maximum Hamming weight `2`, attained by `sigma`. Variable `1` is flippable. Variables `2` and `3` each have exactly one critical blocker, and both unique blockers contain `not x_1`. Flipping `1` down and then either leaf up is satisfying, but flipping both leaves up makes `(+1,-2,-3)` false. Thus two individually valid rescues need not compose.

Exact checker:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T00-52-00Z__radius3_rescue_counterexample_exact.py`

Archived output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T00-52-00Z__radius3_rescue_counterexample_exact.out`

It exhausts all 16 assignments for the formula, reconstructs the satisfying component, verifies the claimed critical sets and failed two-leaf augmentation, and checks identity (4.2) for all satisfying base assignments, all 16 flip sets, and all 4 clauses: `576` exact Boolean checks. Output ends

`ALL_EXACT_CHECKS_PASS = True`.

This killed a plausible but invalid exponential-capacity argument before it was inserted into the 4.4898 configuration count.

## 6. Why radius 3 is still the first promising finite scale

This subsection is **mechanism analysis**, not an asymptotic theorem and not source movement.

Condition on a fixed assignment satisfying every random clause. Each clause is then critical with probability `3/7`; the critical variable is asymptotically uniform. Put

`lambda = 3 alpha / 7`.

The usual Poisson heuristic gives a critical-count law close to `Pois(lambda)`. For a candidate with zero density `rho`, the densities are approximately

- unique-blocked zeros: `rho lambda e^{-lambda}`;
- flippable ones: `(1-rho)e^{-lambda}`.

A unique blocker has two initially false literal slots. Treating these slots as asymptotically uniform, the naive mean number of potential rescued leaves incident to one flippable one is

`mu approx 2 rho lambda e^{-lambda}`.                                   (6.1)

At `alpha=4.4898` and the single-flip saddle scale `rho about 0.46`,

`lambda=1.9242`, `mu about 0.259`,

while the flippable-one density is about `0.0788`. Thus the naive Poisson density of centers with at least two rescue incidences is approximately

`0.0788 * [1-exp(-0.259)(1+0.259)] about 0.00222`.

So radius-3 collisions are extensive in this heuristic. By contrast, a specified radius-2 mutual-rescue pair needs two specified `O(1/n)` incidences, and summing over `O(n^2)` pairs only produces order-one candidates at this crude level. This explains why radius 3 is the first finite radius that could plausibly contribute an exponential correction to a first-moment count.

The counterexample in Section 5 shows that rescue incidence count alone is insufficient. The correction must retain the full signed clause types from (4.2).

## 7. Source-compatible next object: augment the Diaz configuration polytope, do not invent a new standalone bound

The 4.4898 proof already counts single-flip / positively-prime assignments inside a typical, positively unbalanced configuration model. Its variables record light-variable degree `(i,j)`, the number `k` of negative blocking occurrences for light zero-variables, literal-copy types, and 16 extended clause types.

A radius-3 extension should therefore refine, rather than replace, that count. The minimal new information is:

1. for light one-variables, the number of positive occurrences that are critical at the candidate assignment;
2. for a candidate 3-flip pattern, the full truth-profile `T_C/F_C` of every clause touching the three flipped variables;
3. the incidence type identifying whether a blocker repaired by an earlier flip creates a later clause deficit elsewhere.

For each fixed refined type tuple `x`, let

- `N_1(x)` be the number of pairs `(configuration,assignment)` counted by the old single-flip condition;
- `N_3(x)` be the number among them with **no** Hamming-weight-improving satisfying assignment at distance at most 3.

The exact missing source-relevant lemma is:

**Radius-3 exponential penalty lemma.** There is an explicit `eta>0` and a neighborhood `U` of every maximizing type tuple for the current `alpha=4.4898` variational problem such that, uniformly for `x in U`,

`N_3(x) <= exp(-eta n + o(n)) N_1(x)`.                                  (7.1)

Outside `U`, retain the already negative margin of the Diaz objective. If (7.1) is proved with enough quantitative margin, continuity in `alpha` would permit rerunning the finite-dimensional maximization below `4.4898`, producing an actual source endpoint improvement.

The important correction from this run is that `N_3` cannot be represented by a simple capacity-one rescue-star factor. Its correct finite state comes from (4.2).

## 8. Approach C — whitening/core compression does not presently pay the missing entropy

Maneva--Sinclair prove that above `4.453` random 3-SAT has no nontrivial core assignment w.h.p. This does **not** imply UNSAT and therefore cannot replace the source upper endpoint.

I tried to turn corelessness into a representative count by charging each satisfying assignment to a canonical whitening history. The obstruction is multiplicity: coreless assignments can have many whitening orders, and no proved uniform relation was obtained between the number of histories and the size/number of solution clusters. Without an exponential lower bound on that multiplicity per cluster, the whitening quotient does not beat the existing first-moment count.

So this route yielded no theorem this run. The precise missing statement is a history-entropy lower bound that is uniform under the random-3-SAT degree types; current source results do not provide it.

## 9. Before / after

### Source metric

`[3.52,4.4898] -> [3.52,4.4898]`.

`W: 0.9698 -> 0.9698`.

**No movement.**

### Auxiliary mechanism progress

Before:

- clause-local multiplicative weights ruled out for ordinary second moment at `3.52`;
- submesoscopic cluster-ball normalization ruled out at exponential scale;
- full-component quotient available but with unpaid cross-component lemma.

After:

- exact global-max flip-set condition (4.2)--(4.3);
- exact finite counterexample showing the naive radius-3 rescue-star capacity shortcut is false;
- identification of radius 3 as the first finite locality with a plausible extensive correction, with the numerical `0.00222 n` collision-scale heuristic explicitly labeled nonrigorous;
- a concrete source-compatible extension target: prove the uniform radius-3 exponential penalty (7.1) inside the **existing** Diaz configuration polytope, rather than build another standalone local-max bound already dominated by `4.4898`.

## 10. Three materially different attacks tried

1. **Component quotient / moment route:** correct identities, but no new cross-component moment control; unchanged obligation.
2. **Global maximum / signed flip accessibility:** substantive progress; exact reformulation and exact negation counterexample; yields the new radius-3 polytope target.
3. **Whitening/core history quotient:** no proof; multiplicity of whitening histories is uncontrolled, so `4.453` cannot be promoted to an UNSAT bound.

The next run should not retry the false rescue-star capacity lemma. It should either (i) derive the finite radius-3 type extension and its entropy term explicitly inside the Diaz variables, or (ii) prove a uniform comparison that reduces (7.1) to a smaller finite optimization. Source status remains OPEN/PARTIAL.