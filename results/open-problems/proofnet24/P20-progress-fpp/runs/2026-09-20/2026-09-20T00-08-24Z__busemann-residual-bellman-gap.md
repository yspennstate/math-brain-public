Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL DEFECT UNCHANGED: `c_*: 0 -> 0`. Mechanism progress: exact diagonal-support Busemann residual identity; a uniform Exp(1) local Bellman-gap lower bound `E S >= 1/10`; and a proved predictable-pivot compiler reducing `Delta_12>0` to a positive-density block pivot statement with explicit error.**

# P20 T10 — Busemann residual metric and a quantitative Exp(1) Bellman gap

Date: 2026-09-20.
Repository: `yspennstate/math-open-problems`, branch `master`.
Parent claim: `operations/claims/PROB10-10.md` (owned by the native PROB10-10/HARD7-03 lane; P20 is a complementary LIVE20 route, not a takeover).
Status: **PARTIAL / OPEN**.

## 1. Exact parent target and before/after

The model is fixed throughout: nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid `Exp(1)` edge weights. Write `T(x,y)` for passage time and `mu(v)` for the deterministic time constant.

The source navigation is Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2. Their Question 4 is literally: for continuous `F`, show that the limit shape is strictly convex. P20 works only on the source-valid `Exp(1)` special case.

The inherited first milestone is

`Delta_12 := 2 mu(e1) - mu(1,1)`

and

`c_* := sup{ c >= 0 : Delta_12 >= c has been rigorously proved in this track }`.

Before this run: `c_*=0`.
After this run: `c_*=0`.

So there is **no original-problem movement**. A positive `Delta_12` would itself still be only a restricted-direction PARTIAL result, not full strict convexity.

Separate mechanism-level movement is substantial: the triangle defect is rewritten exactly as the time constant of a nonnegative Busemann-slack metric, and Exp memorylessness gives an explicit `1/10` expected local Bellman toll at any forced nonoptimal departure, conditional on all edge weights outside that vertex star. The remaining problem is now a geometric/block statement asserting a positive density of predictably chosen forced departures.

## 2. Policy / ownership / companion state consumed

I followed `operations/PROGRESS20_2026-09-20.md` and its LIVE20 mapping. It assigns P20 to the Busemann/variational curvature mechanism and P04 to the block-to-infinite-volume curvature transfer.

A direct read of `operations/claims/PROB10-10.md` confirms that the parent source is already owned by the native PROB10-10 lane. I did not alter that claim.

The P04 LIVE20 report root `proofnet24/P04-progress-curvature` was not present on master at the time of this run. I therefore do **not** attribute a nonexistent P04 theorem. For the concrete finite-to-infinite baseline I used the current owner report

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__point-to-line-slab-compiler.md`.

That report proves the random-endpoint antidiagonal slab upper compiler

`E T(0,nm(1,1))/(nm) <= q_m/m + 2/sqrt(n)`

and hence `mu(1,1)<=q_m/m`; exact `m=3` evaluation gives the rigorous diagonal upper bound `0.790093366681362...`. It does not reach the inherited sufficient threshold `0.60048` coming from the R08 axis lower bound.

## 3. Recovered failures that constrain this run

The prior R08 chain is preserved rather than reset.

- `R08-X001`: linearly many positive local deletion margins may share a single bypass. Therefore local strictness does not automatically tensorize.
- `R08-X002`: exact finite triangle equality occurs on positive-probability open Exp(1) cylinder events. Therefore no pointwise theorem saying every finite environment has a proportional strict saving can be true.
- `R08-L003`: `mu(e1) >= 3753/12500 = 0.30024`, so the old direct comparison route would close the pair only after proving `mu(1,1)<0.60048`.
- fixed-corner exact blocks through size three were far above that threshold and were retired.

The R07 fluctuation/KPZ chain is not imported as curvature. In particular, no unproved fluctuation exponent, overlap exponent, differentiability assumption or geodesic-wandering estimate is used below.

## 4. Fresh literature/source check needed for this mechanism

The ADH arXiv record remains v2 (23 September 2016). Its Section 5.4 gives reconstructed Busemann functions from translationally averaged hyperplane targets. Under Assumption (I), Lemma 5.10 states

`E_{mu*} B(x,y) = rho . (y-x)`

for the chosen supporting hyperplane `H={z: rho.z=1}`. The Exp(1) law satisfies the iid/moment/no-zero condition and has continuous marginals.

Krishnan, *Variational formula for the time-constant of first-passage percolation*, arXiv:1406.1108, supplies the HJB/duality viewpoint: the time constant is an effective Hamiltonian/dual variational quantity. I use this only as conceptual support; no explicit corrector from that paper is assumed.

A bounded current search again found no theorem settling ordinary iid nearest-neighbor Exp(1) strict convexity. Dembin--Elboim--Peled (GAFA 2024, arXiv:2204.02332) give quantitative planar coalescence under a hypothesis that the limit shape has more than 32 extreme points, so importing their rate into a proof of strict convexity here would be circular. Bakhtin--Dow concern different continuous-action FPP models. Directed integrable models and shape simulations are not used.

This is bounded negative evidence, not an exhaustive priority claim.

## 5. Three routes compared

### Route A — Busemann residual metric (successful reduction)

Instead of trying to subtract two large passage-time bounds, use a supporting Busemann cocycle and charge only the non-calibrated slack. This gives a nonnegative path metric whose asymptotic rate is exactly half of `Delta_12`.

### Route B — Exp(1) Bellman competition at a vertex (successful local quantitative lemma)

Expose all edges except the four-edge star at a candidate pivot. Dynamic programming then writes the four first-step actions as deterministic offsets plus four fresh iid exponentials. Memorylessness gives a uniform lower bound on the gap between the optimal departure and every nonoptimal departure. Unlike numerical curvature, this is exact and distribution-specific.

### Route C — HJB/deterministic linear tilt (useful diagnosis, not enough)

For a deterministic support functional `rho`, every path has tilted cost `sum(tau_e-rho.step)=T(path)-rho.endpoint`. This is the clean dual/HJB formulation, but individual tilted edges can be negative. The positivity needed for a lower block argument is therefore much cleaner in the Busemann-slack formulation. This route alone did not produce a positive defect.

The successful synthesis is A+B, with P04 asked to supply the missing block geometry that makes the local Bellman toll accumulate.

## 6. P20-FPP-BUSEMANN-RESIDUAL-01 — exact residual representation of the diagonal triangle defect

**Claim: PROVED.**

Let `g(v)=mu(v)`. Put

`z_d=(1,1)/g(1,1)`,

which lies on the boundary of the limit shape. By coordinate-swap symmetry, there exists a symmetric supporting functional at `z_d`: start with any support `rho`, swap its two coordinates, and average. The support set is convex, so the average is again supporting. Thus we may choose

`rho=(b,b)`, where `2b=g(1,1)`.

Use the ADH reconstructed Busemann measure `mu*` associated with the supporting hyperplane `H={z:rho.z=1}`. Under `mu*`, `B` is an additive cocycle and Lemma 5.10 gives

`E B(x,y)=rho.(y-x)`.

For an oriented nearest-neighbor edge `(x,y)`, define

`r_B(x,y):=tau_{xy}-B(x,y)`.

Because a Busemann increment satisfies `B(x,y)<=T(x,y)<=tau_{xy}`, one has `r_B(x,y)>=0`.

For a finite path `gamma=(x=x_0,x_1,...,x_k=y)`, cocycle additivity gives

`sum_i r_B(x_i,x_{i+1}) = T(gamma)-B(x,y)`.

The endpoint term is independent of the path. Therefore, defining the residual directed passage time

`R_B(x,y):=inf_gamma sum_i r_B(x_i,x_{i+1})`,

we obtain the exact identity

`R_B(x,y)=T(x,y)-B(x,y)`.                                         (6.1)

Taking expectation at `y=n e1` and using ADH Lemma 5.10,

`E R_B(0,n e1)=E T(0,n e1)-n b`.                                (6.2)

The ordinary FPP `L^1` shape theorem gives `E T(0,n e1)/n -> g(e1)`. Hence

`lim_{n->infty} E R_B(0,n e1)/n = g(e1)-b`

`= g(e1)-g(1,1)/2`

`= Delta_12/2`.                                                   (6.3)

Consequently

`boxed{ Delta_12 = 2 lim_n E R_B(0,n e1)/n }`.                  (6.4)

No differentiability of the limit shape is used in (6.4). The translationally averaged reconstructed Busemann function is exactly what avoids assuming an almost-sure pointwise Busemann limit.

### Why (6.4) is a real gain

The old comparison route had to prove a lower bound for `mu(e1)` and a separate upper bound for `mu(1,1)` tightly enough that their difference stayed positive. Equation (6.4) instead turns the desired difference itself into a nonnegative FPP-type time constant. There is no cancellation of two independently approximated order-one constants.

The finite-size identity also isolates the only remaining transfer error:

`2 E R_B(0,n e1)/n = Delta_12 + 2( E T(0,n e1)/n - mu(e1) )`.

A positive finite residual mean by itself is therefore not enough; one needs a genuine lower block-to-infinite transfer for the residual metric. That is the precise P04 interface.

## 7. P20-FPP-EXP-BELLMAN-GAP-02 — uniform local toll from exponential memorylessness

**Claim: PROVED for finite targets; the same local lower-tail estimate is stable under the ADH weak-limit construction, but only the finite-target conditional form is needed for the compiler below.**

Let `A` be a target set not containing a vertex `x`, and write

`U(v)=T(v,A)`.

Let `y_1,...,y_4` be the four neighbors of `x`, and let

`E_i=tau_{x y_i}`.

Delete the vertex `x` and all four incident edges. In that deleted graph define

`a_i = T_{G\{x}}(y_i,A)`.

Conditional on every edge outside the star of `x`, the four values `a_i` are deterministic and `E_1,...,E_4` remain iid `Exp(1)`. Positivity of edge weights lets every minimizing path be taken simple, so the Bellman equation is exactly

`U(x)=min_i (E_i+a_i)`.                                          (7.1)

Put `X_i=E_i+a_i`, `M=min_i X_i`, and let `I` be the unique minimizer. For the oriented edge `x->y_i`, define its Bellman slack

`s_i := E_i+U(y_i)-U(x) >=0`.                                    (7.2)

We now compute these slacks exactly from the star data.

Let `M_{-i}=min_{j != i} X_j`. A simple path from `y_i` to `A` either avoids `x`, at cost `a_i`, or first enters `x` through the edge `i` and then must leave through a different star edge, at cost `E_i+M_{-i}`. Therefore

`U(y_i)=min(a_i, E_i+M_{-i})`.                                  (7.3)

For the winner `I`, (7.3) gives `s_I=0`. For `i != I`, one has `M_{-i}=M`, so

`s_i = min( X_i-M, 2E_i ) >0`.                                  (7.4)

Let

`S_x(A):=min_{i != I} s_i`

be the cheapest strictly nonoptimal Bellman departure from `x`.

### 7.1 First-step action gap

Let `G=X_(2)-X_(1)` be the gap between the two smallest first-step actions. Conditional on the outside-star offsets `(a_i)`, condition further on the winning index and winning value `X_(1)=t`. For each of the other three channels:

- if `a_j<=t`, the conditional residual waiting time is `Exp(1)` by memorylessness;
- if `a_j>t`, its residual time is `(a_j-t)+Exp(1)`, which stochastically dominates `Exp(1)`.

The three channels remain conditionally independent. Hence

`P(G>u | outside star) >= exp(-3u)`                              (7.5)

and in particular

`P(G<=u | outside star) <= 1-exp(-3u) <=3u`.                    (7.6)

### 7.2 Bellman slack tail

By (7.4),

`S_x(A)=min( G, 2 min_{i != I} E_i )`.                           (7.7)

Therefore, by a union bound and `min_i E_i ~ Exp(4)`, for all `u>=0`,

`P(S_x(A)<=u | outside star)`
` <= P(G<=u | outside star) + P(min_i E_i<=u/2)`
` <= (1-exp(-3u)) + (1-exp(-2u))`
` <= 5u`.                                                        (7.8)

Integrating the survival function over `0<=u<=1/5` gives the uniform quantitative gap

`E[ S_x(A) | outside star ]`
` >= integral_0^(1/5) (1-5u) du`
` = 1/10`.                                                       (7.9)

Thus

`boxed{ E[ S_x(A) | all edges outside star(x) ] >= 1/10 }`.      (7.10)

This is an exact `Exp(1)` finite-energy/memoryless effect. No curvature, KPZ exponent, integrable directed model or simulation enters it.

### 7.3 Relation to Busemann slack

For finite hyperplane targets `H_alpha`, the Bellman slack in (7.2) is precisely

`E_i + T(y_i,H_alpha)-T(x,H_alpha)`

which is the finite-target residual `tau_{xy}-B_alpha(x,y)`. Along the ADH averaged hyperplane sequence these local residual vectors are tight because `|B_alpha(x,y)|<=T(x,y)`. The estimate (7.8) prevents positive residual mass from collapsing arbitrarily onto zero at one vertex, so the corresponding one-vertex lower-tail bound passes to subsequential local weak limits. I do **not** use any unjustified independence between different vertices in the Busemann limit.

## 8. P20-FPP-PREDICTABLE-PIVOT-COMPILER-03 — explicit conditional triangle defect

**Claim: PROVED as a compiler theorem under a clearly stated block/pivot hypothesis. The hypothesis itself is the unresolved P04-scale geometry.**

Work first with a finite target hyperplane `H_alpha`, and let `r_alpha(x,y)` be the Bellman slacks from §7. For any path `gamma=(x_0,...,x_k)`, telescoping gives

`sum_j r_alpha(x_j,x_{j+1})`
` = T(gamma)+T(x_k,H_alpha)-T(x_0,H_alpha)`.                      (8.1)

Every summand is nonnegative.

Suppose a block construction applied to every residual-minimizing path from `0` to `n e1` produces selected vertices `x_1,...,x_{K_n}` with the following properties.

1. At each selected vertex, the path takes a non-Bellman-minimizing outgoing edge, so its slack is at least `S_{x_j}(H_alpha)`.
2. The selected vertex is determined before revealing its four incident edge weights; equivalently, relative to a sequential exploration, `x_j` is measurable with respect to a sigma-field containing the needed outside-star offsets but not the fresh star at `x_j`.
3. Selected stars are fresh in that exploration (P04 may enforce this by spacing or by assigning each pivot to a disjoint block).
4. The block/interface construction loses at most `epsilon_n n` residual cost in expectation, with `epsilon_n -> epsilon` (or a fixed explicit `epsilon_L` at block scale `L`).

Because (8.1) is an additive sum of nonnegative slacks, selecting only a subset of departure vertices gives a valid lower bound. By the tower property and (7.10), predictability gives

`E R_alpha(0,n e1) >= (1/10) E K_n - epsilon_n n`.               (8.2)

Pass first along the ADH hyperplane averaging/subsequence and then divide by `n`. If

`liminf E K_n/n >= alpha`,                                      (8.3)

then the Busemann residual rate satisfies

`liminf E R_B(0,n e1)/n >= alpha/10 - epsilon`.                 (8.4)

Combining with (6.4),

`boxed{ Delta_12 >= alpha/5 - 2 epsilon }`.                     (8.5)

Hence any P04 block theorem with

`alpha > 10 epsilon`

immediately yields the desired strictly positive directional triangle defect.

At a fixed block scale `L`, if P04 certifies predictable pivot density `alpha_L` and residual interface loss `epsilon_L`, the explicit certificate is

`Delta_12 >= alpha_L/5 - 2 epsilon_L`.                           (8.6)

This is the requested controlled-error interface. The local constant `1/10` is distribution-specific and rigorous; the missing quantities `alpha_L,epsilon_L` are geometric and block-transfer quantities, not hidden numerical curvature.

## 9. Why this does not yet prove `Delta_12>0`

The missing statement is **not** local strictness. Equation (7.10) gives that.

The missing statement is a positive density of **predictably exposed nonoptimal departures** on a path whose global residual cost is near minimal. A cheap residual path can follow the zero-slack Busemann geodesic for long stretches, pay one portal toll, then exploit a long branch before coalescing. One bypass can therefore absorb many putative local savings. This is exactly the structural content of old `R08-X001`, now expressed in Busemann/Bellman language rather than rediscovered after the fact.

ADH's planar coalescence theorem gives pairwise coalescence under differentiability, but no quantitative coalescence tail that is available here without additional shape hypotheses. Dembin--Elboim--Peled supply strong quantitative coalescence only under a >32-extreme-points hypothesis, which cannot be used to prove strict convexity from scratch.

Thus the residual obstruction is precise:

> Prove a block-local, outside-star-predictable pivot-density estimate for axis crossings relative to the symmetric diagonal support, or prove a quantitative long-branch/coalescence bound strong enough to imply one.

A mere estimate `E S_x>=1/10` at typical vertices is insufficient because the minimizing path may select atypically soft pivots.

## 10. Concrete P04 handoff

The companion block route should no longer try to compare two order-one time constants if it can avoid doing so. The natural finite-block observable is now the Bellman residual.

For a diagonal-support hyperplane target beyond an `L`-block, expose the block boundary/outside first and keep a set of separated four-edge stars unexposed. A successful block certificate should prove either:

- every admissible left-to-right/axis-like crossing contains at least `k_L` forced nonoptimal departures at those predictable stars, except on a bad block event whose contribution is bounded explicitly; or
- the expected number of such departures minus the side-entry/interface correction is at least `alpha_L L`.

Then (8.6) compiles it directly to a positive `Delta_12` once `alpha_L/5 > 2 epsilon_L`.

This interface is compatible with the existing random-endpoint slab philosophy: endpoint freedom should be used to remove reset costs, while the residual/Bellman observable removes the cancellation between separate axis and diagonal estimates.

At this repository tip the P04 progress root was absent, so this is a handoff target rather than a claim that P04 has already proved the block estimate.

## 11. Sanity checks / attempted falsification

1. **Sign convention.** With ADH's convention `B_alpha(x,y)=T(x,H_alpha)-T(y,H_alpha)`, a geodesic first edge has `B_alpha(x,y)=tau_xy`, so `r=tau-B>=0` as required.
2. **Undirected return through the pivot.** This is the main subtlety in §7. It is why the nonwinner slack is not merely the first-step action gap `X_i-M`; the exact correction is `min(X_i-M,2E_i)`. Omitting the `2E_i` branch would be false in the undirected model.
3. **No independence claim across pivots.** The theorem only charges pivots whose stars are fresh/predictable in an explicit exploration. A generic adaptive collection of Busemann soft spots can be strongly dependent.
4. **Finite mean bias.** Positive finite `E R_B(0,n e1)` does not by itself prove a positive asymptotic rate. The compiler explicitly requires a lower block transfer; this is not hidden.
5. **Directed models.** No directed solvable constant is substituted for the undirected time constant.
6. **Numerics.** No sampled curvature is used. No new code was necessary because the decisive core is analytic and exact.

## 12. Short handoff of the displaced P20 cyclic-interval proof

The previous P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved, not reopened. P20 has a source-literal YES proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01`; P26's full-proof audit passed, while the distinct second audit remained missing in the last recovered state. Thus its campaign audit gate was `1/2`, not closure. The 20 September owner directive explicitly moves P20 research effort away from waiting for that audit. No cyclic-interval claim or artifact is altered here.

## 13. Residual obstruction and next attack

Original-problem obstruction: prove a positive residual time constant in the axis direction for the symmetric diagonal-support Busemann field.

Mechanism obstruction: convert local `Exp(1)` Bellman strictness into a linear density of predictably exposed forced deviations despite long zero-slack Busemann branches.

**Next attack:** construct a finite `L x H` separator exploration that chooses candidate pivot stars from boundary data before revealing those stars. Prove a deterministic dichotomy for every axis-like crossing:

- either it contains `>= alpha_L L` such predictable nonoptimal pivots; or
- it follows a zero-slack branch across a long side-hair event.

Then attack the side-hair event using planarity/coalescence and the current block compiler, keeping its probability/error explicit. The first numerical objective is not a sampled shape: it is a rigorous pair `(alpha_L,epsilon_L)` satisfying `alpha_L>10 epsilon_L`, which by (8.6) yields `Delta_12>0`.

If this pivot/side-hair obligation remains unchanged for three substantive P20 runs, the owner policy requires a materially different attack rather than another local-gap refinement.

## 14. `ledger_delta` request (P20 does not edit shared ledgers)

```yaml
ledger_delta:
  track: P20-progress-fpp
  parent: PROB10-10
  source: ADH arXiv:1511.03262 Question 4, Exp(1) undirected Z2 special case
  original_metric:
    name: c_star_lower_bound_for_Delta12
    before: 0
    after: 0
    status: OPEN_PARTIAL
  mechanism_progress:
    - P20-FPP-BUSEMANN-RESIDUAL-01_PROVED
    - P20-FPP-EXP-BELLMAN-GAP-02_PROVED_FINITE_TARGET_LOCAL
    - P20-FPP-PREDICTABLE-PIVOT-COMPILER-03_PROVED_CONDITIONAL_ON_BLOCK_PIVOT_HYPOTHESIS
  explicit_constants:
    local_bellman_gap_mean_lower_bound: 1/10
    block_to_triangle_compiler: Delta12 >= alpha_L/5 - 2 epsilon_L
  companion_request:
    track: P04-progress-curvature
    target: certify predictable pivot density alpha_L and interface/side-hair loss epsilon_L for the residual Bellman metric
    success_condition: alpha_L > 10 epsilon_L
  residual_obstruction: positive-density predictable forced deviations versus long zero-slack Busemann branches
  cyclic_interval_handoff: proof_candidate_preserved_P26_PASS_second_audit_missing_1_of_2
  shared_results_posted_queue_edits: NONE
```

END OF P20 FPP RUN REPORT
