Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in retired I0082: `2/3 -> 2/3`, retirement count stays `6`; no successor metric is admitted. Successor-admission movement: `F0083 UNSCREENED -> OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR / HOLD_NOT_READY_CLOSABLE`. Methods actually used: B8 GO THE OTHER WAY AND DISCRETIZE, B19 MAKE IT AN ALGORITHM, B23 DO WHAT THE PROPOSER DID NOT EXPECT.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated GPT-6/maximum model selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 inverse-flow screen after I0082 retirement

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The frozen I0082 metric remains `2/3`, its six-unchanged retirement remains controlling, and its C005/C006 candidate classification remains preserved as `PARTIAL / audit pending`, not closed.

At run start I reread the controlling repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current task-health successor screens, the newest R08 report, the current CLOSABLE assignments/admissions, the H and G intake material touched by nearby rotations, and the newest neighboring R09 report. The current assigned CLOSABLE front is already occupied (including D0041, H0011, I0012, D0044, D0038, D0047 and H0005 in the latest task-health snapshot), while R09 owns G0002. I therefore did not steal a live owner.

The preceding R08 report ended in `ROTATION HOLD -- SUCCESSOR ADMISSION REQUIRED` after excluding already-settled H0013/H0014 and classifying D0056 as a genuine but HARD exact-asymptotic target. Its method triple was B4/B20/B27, so this run deliberately uses a different triple.

## 2. New candidate screened: F0083

**Source:** Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668v4, Section 12, Open problem (i) `Nonuniqueness`.

**Exact source question:** Does there exist a discrete set of centers `Xi subset R^d` which admits two stable allocations (differing on a Lebesgue-nonnull set)? The source notes that Theorems 2 and 3 force any such example to have greater-than-quadratic growth and prevent it from arising from a finite-intensity translation-invariant point process.

The canonical intake row is F0083 in `probability_1000_intake_F_20260908/batches/b06_forests_matchings_determinantal.json`. Its old attempt F0083-A001 explored finite stable-marriage rotations, rejected lattices as the obvious candidate, and suggested a hierarchical construction, but did not exploit the directed-capacity graph in the source's proof of Theorem 2.

### Current-literature check

A fresh bounded 2026-09-17 search used exact combinations of the source title, the phrase `two stable allocations`, `discrete set of centers`, `nonuniqueness`, and the three authors' names. It recovered the source and later Poisson-allocation/tail/percolation work, but no paper claiming a solution of this arbitrary deterministic-center nonuniqueness problem. This is **bounded negative evidence**, not a worldwide novelty certificate.

### Ownership check

A repository-wide exact-ID search recovered the intake row, its old attempt, and catalog material, but no `operations/claims/F0083.md` and no current R/P/C owner. Thus ownership is clear at this snapshot. I nevertheless do **not** create a claim, because the route below has not yet produced the required pair of Euclidean stable allocations; `PENDING is not READY` remains controlling.

Operational admission label for this run:

`F0083 = OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR / EXPLICIT_EXISTENCE_TARGET / PROMISING_INVERSE_ROUTE / HOLD_NOT_READY_CLOSABLE`.

## 3. B23 — do what the proposer did not expect: reverse the uniqueness proof

The source proves uniqueness under recurrence by assuming two stable allocations `psi_1, psi_2` exist and extracting a directed capacity graph. Rather than trying another direct Gale--Shapley construction, reverse that proof and ask what an example **must** contain.

For a center `xi`, the source defines disputed regions and transfer sets `F(xi,xi')`; a directed edge `xi -> xi'` is present when `Leb(F(xi,xi'))>0`, with capacity

`q(xi,xi') = Leb(F(xi,xi'))`.

Its Lemmas 10--12 imply, on a reachable subgraph `H`:

1. `H` is acyclic;
2. at every nonroot vertex, total incoming capacity is at most total outgoing capacity;
3. root outflow is positive and root inflow is zero;
4. capacities are uniformly summable along every directed ray;
5. the corresponding center-to-center edges have uniformly bounded Euclidean length.

Proposition 13 then says the undirected version of `H` is transient. Theorem 2 derives uniqueness only because recurrent center configurations cannot contain such a bounded-edge transient transfer graph.

So a nonunique example should not be sought as a mysterious global alternative allocation first. A more surgical target is:

> **Inverse transfer problem.** Embed an acyclic transient flow graph by centers in Euclidean space, with bounded edge lengths and a ray-summable capacity profile, then realize each edge-capacity as a positive-volume disputed cell whose Euclidean distance inequalities reproduce the source's Lemma-9 directionality.

This is genuinely different from F0083-A001's finite-rotation route.

## 4. B8 — discretize: an exact Euclidean obstruction template

The source's necessary graph/capacity conditions are themselves exactly realizable by a discrete Euclidean center set, already in `R^2`.

For `n >= 0`, `0 <= k < 2^n`, define

`xi_{n,k} = ( n, (k+1/2) 2^{-n} ) in R^2`.

Connect `xi_{n,k}` to its two children

`xi_{n+1,2k}` and `xi_{n+1,2k+1}`,

and orient every edge away from the root `xi_{0,0}`. Assign each level-`n` outgoing edge capacity

`q_n = 2^{-(n+1)}`.

### Exact self-check on the page

**Discreteness.** Every bounded Euclidean set meets only finitely many integer first-coordinate layers, and each layer contains finitely many centers. Hence the center set is discrete.

**Bounded edge length.** The vertical displacement from a parent at level `n` to either child is exactly `2^{-(n+2)}`. Thus every tree edge has length

`sqrt(1 + 2^{-2n-4}) <= sqrt(17/16)`.

**Acyclicity.** The first coordinate strictly increases along every directed edge.

**Capacity conservation.** A nonroot vertex at level `n` has one incoming edge of capacity `2^{-n}` and two outgoing edges, each of capacity `2^{-(n+1)}`. Therefore

`sum_in q = 2^{-n} = sum_out q`.

At the root, inflow is zero and total outflow is one.

**Uniform ray summability.** Along every infinite directed path starting at the root,

`sum_{n>=0} q_n = sum_{n>=0} 2^{-(n+1)} = 1`.

**Transience.** The undirected graph is the rooted binary tree, hence is transient. Equivalently, the displayed capacity itself is a unit flow of finite energy:

`sum_e q(e)^2 = sum_{n>=0} 2^{n+1} * 2^{-2n-2} = sum_{n>=0} 2^{-n-1} = 1`.

**Growth.** All level-`n` centers lie in the strip `n x (0,1)`. A Euclidean ball of radius `R+2` around the origin contains every level up to `R`, hence at least `2^{R+1}-1` centers. Thus the configuration has far greater than quadratic growth, exactly in the regime the source says any counterexample must occupy.

This proves a useful negative-to-the-obstruction statement:

> The graph-theoretic obstruction extracted in the source's uniqueness proof is not incompatible with Euclidean discreteness or bounded transfer length. There is an explicit discrete `Xi subset R^2` carrying a bounded-edge transient DAG and capacities satisfying the source's Proposition-13 hypotheses with uniform path sum `1`.

This is **not** yet a stable-allocation counterexample. It only removes a potential structural obstruction and gives an exact skeleton on which disputed cells could be built.

## 5. B19 — make it an algorithm: exact stability certificate for a proposed pair

The inverse route becomes checkable once stability is written in terms of each center's territorial radius.

Fix an allocation `psi` of appetite `1` in which every center is sated, and define

`R_psi(xi) = ess sup { |x-xi| : psi(x)=xi }`.

For a.e. site `x` assigned to `eta != xi`, the center `xi` covets `x` exactly when

`|x-xi| < R_psi(xi)`.

The site `x` desires `xi` exactly when

`|x-xi| < |x-eta|`.

Therefore a sated allocation is stable if and only if, for a.e. assigned site `x`,

`|x-xi| < |x-psi(x)|  ==>  R_psi(xi) <= |x-xi|`

for every competing center `xi`; and for any unclaimed site `x`, one must have `R_psi(xi) <= |x-xi|` for every center.

The equivalence is immediate from the source's definitions of `desires`, `covets`, and `unstable pair`: the essential supremum converts `xi covets x` into the strict radius inequality above. Boundary equalities are harmless on a Lebesgue-null set.

This gives a concrete construction/certification algorithm for F0083:

1. choose a discrete center skeleton and appetite `1`;
2. specify two measurable partitions `psi_1, psi_2` whose territories all have volume `1`;
3. compute the two radius profiles `R_{psi_j}(xi)`;
4. verify the displayed pointwise competitor inequalities on every cell type;
5. verify that the two partitions differ on positive volume.

For a transferred cell `x` which is assigned to a parent under one allocation even though it is geometrically closer to the child, the certificate forces

`R(child) <= |x-child| < |x-parent| <= R(parent)`,

which is precisely the decreasing-radius geometry behind the source's Lemma 9. Thus the algorithm recovers the source's monotonicity rather than fighting it.

## 6. Where the inverse construction still fails

The binary template solves only the **abstract transfer skeleton**. It does not yet solve the Euclidean territory-filling problem.

The tempting cell construction is to use the dyadic inter-layer strips: a parent at level `n` has two child substrips, each of area `2^{-(n+1)}`, exactly matching `q_n`; incoming area and total outgoing area are both `2^{-n}` at every nonroot vertex. That matches the capacity bookkeeping perfectly.

But every center has fixed appetite `1`, whereas these transferred volumes tend to zero. One therefore needs a common territory of volume `1-2^{-n}` (or an equivalent reservoir) assigned to that center in **both** allocations. In the binary embedding the level-`n` centers are separated vertically by only `2^{-n}`, so naive private radius-one cores overlap massively. Merely adding arbitrary private cells far away also fails: unclaimed or competitor-owned sites closer than the farthest private cell can create unstable pairs.

So the exact missing object is now sharper:

> construct common reservoirs plus disputed transfer cells so that every center has volume exactly `1` in both allocations **and** the two territorial-radius inequalities hold pointwise.

This is the first place the reverse-proof route encounters genuinely Euclidean geometry rather than abstract flow theory.

Two next geometric variants are worth trying if F0083 is later admitted with a source-faithful frozen metric:

- replace the exponentially crowded binary embedding by a polynomial-growth transient layered graph in `R^4`, allowing order-one private Voronoi cores while spreading transfer flow with summable capacities;
- keep the binary flow but add a carefully designed reservoir geometry in a higher dimension, using one coordinate for the bounded transfer skeleton and transverse chambers whose entrances are radius-ordered so that the stability certificate remains valid.

Neither is proved here, so I do not claim F0083 or create `operations/claims/F0083.md`.

## 7. Admission decision

F0083 has several attractive CLOSABLE features: it is a single explicit existence question, a concrete counterexample would settle it completely, the source already identifies necessary structure, and current ownership is clear. However, this run has not yet produced an explicit pair of stable Euclidean allocations. Promoting it now would freeze a `0/k` metric around a construction that may still fail for a global geometric reason.

Therefore the honest disposition remains:

`R08 = ROTATION HOLD -- SUCCESSOR ADMISSION REQUIRED`,

with F0083 now upgraded from an untouched intake item to a **screened promising reserve** rather than a READY assignment.

No finite checker was created: the new mathematical claim is the on-page infinite binary-flow template and the stability-radius equivalence, both proved symbolically above. A checker would add no evidentiary value at this stage.

## 8. Model / scheduler-control status

The situation is unchanged. The task-management surface available here exposes title/prompt/schedule/timing-mode/enabled controls, but no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry. Hence GPT-6/maximum remains prompt text only in this runtime.

Actually enforcing GPT-6/maximum requires a native product/API or authorized owning-workspace control that exposes model and reasoning fields plus applied-run telemetry. The historical P26 `You cannot modify this task` response is an ownership/context boundary; repository history records that an authorized context later could update P26. The lawful workaround is the owning context, supported ownership/admin transfer, or platform support -- not duplicating the task or editing repository text as if that changed runtime configuration.

No scheduler mutation was attempted.

## 9. Prohibited-action audit

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, shared-root edit, peer-file edit, or paid compute was performed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0925Z_successor_screen_f0083_inverseflow_c7a41e
  predecessor:
    id: I0082
    source: "Hasebe-Ueda arXiv:1710.08240v2, Problem 3.11"
    metric: "number of three frozen candidate obligations proved"
    before: "2/3"
    after: "2/3"
    unchanged_count: 6
    state: RETIRED_FROZEN
  successor_screen:
    id: F0083
    source: "Hoffman-Holroyd-Peres, A stable marriage of Poisson and Lebesgue, Section 12 Open problem (i)"
    exact_target: "existence of a discrete Euclidean center set with two stable allocations differing on positive Lebesgue measure"
    current_literature: "OPEN_CURRENT_BOUNDED"
    ownership: "CLEAR_IN_CURRENT_REPOSITORY_SEARCH"
    admitted: false
    disposition: "HOLD_NOT_READY_CLOSABLE"
    old_attempt_recovered: "F0083-A001 finite-rotation/hierarchical route"
    new_route: "reverse Theorem-2 transfer-flow obstruction"
    exact_abstract_template:
      centers: "xi_{n,k}=(n,(k+1/2)2^{-n})"
      graph: "rooted binary tree"
      edge_capacity: "2^{-(n+1)} on level-n outgoing edges"
      bounded_edge_length: "<= sqrt(17/16)"
      ray_capacity_sum: 1
      finite_energy: 1
      growth: "exponential in Euclidean radius"
    new_certificate_lemma: "for sated allocations, stability is equivalent to the territorial-radius competitor inequalities stated in section 5"
    remaining_obligation: "realize common appetite-one reservoirs and disputed cells satisfying both allocations' radius inequalities"
  methods_this_run: [8, 19, 23]
  next_methods_if_readmitted: [6, 15, 30]
  overall: "ROTATION_HOLD_WITH_F0083_SCREENED_PROMISING_RESERVE"
```
