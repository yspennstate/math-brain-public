Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. ADMISSION HOLD / SOURCE METRIC UNMEASURED: `UNMEASURED -> UNMEASURED`; methods actually tried: B2, B6, B25.**

# P13 outside-successor run — P0223 exact projection theorem; P0242 literature-resolution correction

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / native slot: P13 / `6aa7b253b37c8191b693d8dc79298d37`  
Own root: `proofnet24/P13-outside-successor/`

## 1. Continuity, exclusions, and mandatory first screen

I reread the controlling owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest P13 report, current claim/search surfaces, and neighboring admission evidence before doing new mathematics.

The retired P13 I0051 clade-covariance source was not reopened. The terminally handed-off C0021 recursive-majority source was not reopened. P22/P23/P25, AF4.49(ii), PROB20-13, and the other owner exclusions remain preserved.

The mandatory first successor lead I0054 was checked first. `operations/claims/I0054.md` still names R11 / native slot `6aa7b68c70c481919b1a131eb67b6b24`. Its newest recovered report is `runs/R11/2026-09-19T04-37-28Z_i0054-debruijn-u039-c060-2f91.md`; that report continues the peer source and moves R11's own obligation metric `59 -> 60`. P13 therefore did not touch I0054.

The immediately preceding P13 report was

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T04-18-51Z__successor-admission-p0222-hub-reuse-hard-screen.md`.

Its durable state was `SUCCESSOR_ADMISSION_HOLD`, successor metric `UNMEASURED`, and no active P13 claim. P0219 is now owned elsewhere. P0222 was correctly rejected for this slot as HARD OUTSIDE.

## 2. Screening target P0223 and current literature

The next substantive unclaimed exact-source candidate screened here is Codex row **P0223**, David Aldous, *Mixing times for branch rotation and triangulation walk*: prove an order-`n^(3/2)` relaxation-time upper bound for the branch-rotation cladogram chain and the related convex-polygon triangulation flip chain. The historical campaign state is `attempted_unsolved`; its prior attempt found exponential congestion for a fixed-comb canonical-path choice.

Direct `operations/claims/P0223.md` reads returned 404 both before and after the research below. Exact-ID repository search recovered campaign/attempt material and a neighboring cursor-repair screen, but no current exclusive owner. Absence of a claim is not treated as READY.

The original author source still states the `n^(3/2)` upper-bound problem. A fresh 2026-09-19 literature search recovered a major later result: Alev--Frishberg--Sarantis--Tetali, *Faster Triangulation Mixing via Transport Flows* (arXiv:2605.02067; ICALP 2026), which proves an approximately `O(n^2)` relaxation/log-Sobolev bound and explicitly describes this as progress toward the Aldous `Theta(n^(3/2))` target. Their proof uses a central-triangle/fiber decomposition and a transport-flow estimate whose average congestion still carries a square-root-scale loss. I found no checked primary source closing the exact `n^(3/2)` target. This is bounded negative evidence only, not a global openness certificate.

The original-source page image for the triangulation problem rendered successfully during this run. The P0242 PDF screenshot attempted later in this report did not; that separate access failure is recorded below.

## 3. New mathematics on P0223

The purpose of this screen was not to manufacture a metric but to decide whether the coarse central-triangle process itself could plausibly be the missing `n^(3/2)` bottleneck. It is not: the associated stationary-flow projection mixes on an `O(n)` relaxation scale.

Let the convex polygon have vertices `0,1,...,n+1`. Let `Omega_n` be its triangulations, so `|Omega_n|=C_n`, the nth Catalan number. Fix the boundary edge `(0,n+1)`. For a triangulation `T`, let `K(T)=i` when the root triangle incident to `(0,n+1)` is `(0,i,n+1)`, `1<=i<=n`. Let `Omega_i={T:K(T)=i}`. The triangulation flip chain chooses one of its `n-1` diagonals uniformly and flips it.

### Theorem 1 — exact fiber sizes and root-changing cross-edge counts

For every `1<=i<=n`,

`|Omega_i| = C_{i-1} C_{n-i}`.

For `1<=i<j<=n`, the number `E_{ij}` of undirected flip edges between `Omega_i` and `Omega_j` is

`E_{ij} = C_{i-1} C_{j-i-1} C_{n-j}`.

#### Proof

Fixing root vertex `i` inserts the two root-triangle sides `(0,i)` and `(i,n+1)` whenever they are nonboundary. The remaining two polygonal regions have `i+1` and `n-i+2` vertices, hence respectively `C_{i-1}` and `C_{n-i}` triangulations. This gives the fiber formula.

Now fix `i<j`. A flip can change the root third vertex from `i` to `j` only by flipping the root-side diagonal `(i,n+1)` in the quadrilateral `(0,i,j,n+1)`, replacing it by `(0,j)`. Before that flip the triangulation contains the three separating sides that cut the polygon into the three independent subpolygons on vertex intervals `[0,i]`, `[i,j]`, and `[j,n+1]`. They contribute `C_{i-1}`, `C_{j-i-1}`, and `C_{n-j}` possibilities. Conversely every such triple of subtriangulations has exactly that root-changing flip. Multiplying proves the formula. ∎

### Corollary 2 — exact stationary-flow projection kernel

Define the stationary-flow projection chain `P_n` on `{1,...,n}` by averaging the flip chain across each fiber. Its stationary law and off-diagonal kernel are

`pi_i = C_{i-1} C_{n-i} / C_n`,

and, for `i<j`,

`P_n(i,j) = C_{j-i-1} C_{n-j} / ((n-1) C_{n-i})`,

while for `j<i`,

`P_n(i,j) = C_{j-1} C_{i-j-1} / ((n-1) C_{i-1})`.

Each triangulation in an interior fiber `2<=i<=n-1` has exactly two root-changing diagonals, whereas an endpoint fiber has exactly one. Therefore

`P_n(i,i)=1-2/(n-1)` for `2<=i<=n-1`,

and

`P_n(1,1)=P_n(n,n)=1-1/(n-1)`.

The cross-edge formula immediately gives detailed balance `pi_i P_n(i,j)=pi_j P_n(j,i)`.

### Corollary 3 — exact probability that the root index changes

The total number of undirected root-changing flip edges is

`sum_{i<j} E_{ij} = C_n - C_{n-1}`.

Hence, when the triangulation is stationary-uniform and one diagonal is selected uniformly,

`Pr(K changes in one flip) = 3/(2n-1)`.

#### Proof

Count directed root-changing moves by fibers. Endpoint fibers contribute one each and interior fibers two each:

`2(C_n-2C_{n-1}) + 2C_{n-1} = 2(C_n-C_{n-1})`.

Divide by two for undirected edges. Then divide the directed count by `C_n(n-1)` and use

`C_{n-1}/C_n=(n+1)/(2(2n-1))`.

This yields `3/(2n-1)`. ∎

### Theorem 4 — the root-index projection has relaxation time `O(n)`

For `n>=4`, set

`epsilon_n := C_n C_{n-2}/((n-1) C_{n-1}^2)`

so explicitly

`epsilon_n = n(2n-1)/((n-1)(n+1)(2n-3)) ~ 1/n`.

Then for every pair `i,j`,

`P_n(i,j) >= epsilon_n pi_j`.

Consequently

`gap(P_n) >= epsilon_n`,

and

`tau_rel(P_n) <= 1/epsilon_n = O(n)`.

For `n=3`, direct diagonalization gives `gap(P_3)=3/4`, so the same `O(n)` conclusion holds.

#### Proof

For `i<j`, write

`a=i-1`, `b=j-i-1`, `c=n-j`,

so `a,b,c>=0` and `a+b+c=n-2`. Dividing the kernel by `pi_j` gives

`P_n(i,j)/pi_j = C_n C_b / ((n-1) C_{b+c+1} C_{a+b+1})`.

The Catalan ratios

`C_{k+1}/C_k = 2(2k+1)/(k+2)`

increase strictly with `k`, so the Catalan sequence is log-convex. With `b` fixed and `a+c` fixed, log-convexity implies that the denominator product

`C_{b+c+1} C_{a+b+1}`

is maximized at an endpoint `a=0` or `c=0`. Therefore

`P_n(i,j)/pi_j >= C_n C_b / ((n-1) C_{b+1} C_{n-1})`.

Because `C_{b+1}/C_b` is increasing, this last lower bound decreases with `b`; the minimum occurs at `b=n-2`, i.e. at the opposite endpoint pair `(i,j)=(1,n)` (or symmetrically `(n,1)`). Thus the off-diagonal minimum ratio is exactly

`epsilon_n = C_n C_{n-2}/((n-1) C_{n-1}^2)`.

Detailed balance gives the same bound for `i>j`.

For diagonal entries, `P_n(i,i)>=(n-3)/(n-1)`. Also log-convexity shows `pi_i<=C_{n-1}/C_n=(n+1)/(2(2n-1))`. Hence

`epsilon_n pi_i <= n/(2(n-1)(2n-3)) <= (n-3)/(n-1)`

for every `n>=4`. This proves the full minorization.

Let `Pi` denote the rank-one stationary kernel whose every row is `pi`. Then

`P_n = epsilon_n Pi + (1-epsilon_n) Q`

for a stochastic kernel `Q`, and detailed balance of `P_n` and `Pi` makes `Q` reversible with stationary law `pi`. On the mean-zero `L^2(pi)` subspace, `Pi=0`; therefore the second eigenvalue of `P_n` is at most `1-epsilon_n`, proving the gap bound. ∎

### Consequence for the Aldous exponent problem

The exact projection theorem rules out a tempting explanation for the remaining `n^(1/2)` loss in the best current upper bound: **the stationary-flow root-index projection itself is only an `O(n)` relaxation object, not an `n^(3/2)` obstruction.** Any proof of the source `O(n^(3/2))` bound must therefore control transport/internal-fiber relaxation sharply enough that the decomposition does not pay the present extra square-root factor.

This is useful structural progress but is far from a source solution. The source asks for the full triangulation and branch-rotation chains, not the projection alone.

## 4. Section-B method accounting

### B2 — ATTACK THE NEGATION FIRST

I attacked the possibility that the central/root-triangle coordinate itself creates the `n^(3/2)` bottleneck. The exact minorization theorem goes the opposite way: its relaxation time is `O(n)`. Thus the coarse coordinate is **not** a counterexample to faster mixing and cannot by itself explain the missing exponent.

### B6 — DEFORM A KNOWN DISCRETE MODEL

I deformed the full flip chain into the stationary-flow root-index projection already implicit in central-triangle decompositions, but retained exact Catalan fiber geometry rather than using a generic comparison estimate. This produced the closed-form projection kernel and the `O(n)` relaxation theorem above.

### B25 — COUPLE OR COUNT THE SAME FINITE RESTRICTION TWO WAYS

I counted root-changing flips in two ways: first by the three Catalan subpolygons determined by `(i,j)`, and second by the number of flippable root sides per triangulation. Equality of the two counts yields both the exact cross-edge matrix and the identity

`Pr_stationary(root index changes) = 3/(2n-1)`.

These are mathematically distinct from the preceding P13 triple `B2/B18/B25`; this run actually used `B2/B6/B25`.

## 5. Exact finite self-check

The exact checker

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T05-04-04Z__p0223_oriented_projection_checker.py`

was created at commit

`feaf5787f89a8607c0b1dce6efbee55cba48ec1f`

and read back there with blob

`0caf02ce4fae6657256ec94a483e5b6269487a34`.

Its archived output

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T05-04-04Z__p0223_oriented_projection_checker.out`

was created at commit

`cea8c2803534154c116a10fc5eb537595bdf3784`

and read back there with blob

`0bb0b2778a2f41b4c251b17977b3418e8bb1caec`.

The checker exactly enumerates every triangulation through `n=8`, every flip, the Catalan fiber sizes, every cross-fiber count, the stationary-flow kernel, row sums, detailed balance, the exact root-change probability, and the central minima of the fiber law. It reports 33,416 assertions and ends

`ALL_EXACT_P0223_ORIENTED_PROJECTION_CHECKS_PASS`.

This is explicitly a **P13 self-check**, not an independent audit.

## 6. Admission decision on P0223

P0223 is not admitted to this CLOSABLE slot. The source target is a full asymptotic `n^(3/2)` mixing theorem; the 2026 best recovered theorem is still roughly `n^2`, and this run localizes the remaining difficulty to within-fiber/transport control rather than producing a short finite closure route. That is **HARD OUTSIDE**, not an honest CLOSABLE successor.

No `operations/claims/P0223.md` file was created.

## 7. Important literature correction: P0242 is already resolved negatively

A superficially attractive Tier-2 candidate was P0242, Aldous--Fill Open Problem 4.45 on stationary-flow lumping. The source asks whether

`tau_1^(2)(induced) <= K tau_1^(2)(original)`

for some universal `K`, and in particular whether `K=1`.

The campaign's 14 September memo had an exact finite counterexample only to `K=1` and left the universal-`K` half marked open. A fresh 2026-09-19 current-literature search found that this ledger status is stale.

Jonathan Hermon and Yuval Peres, *On sensitivity of mixing times and cutoff* (arXiv:1610.04357; Electronic Journal of Probability 23 (2018), paper 25, DOI 10.1214/18-EJP154) explicitly cite Aldous--Fill Open Problem 4.45 and prove that lumping can increase total-variation mixing time by an unbounded factor of order `Theta(log |V_n|)`.

This resolves the original `tau_1^(2)` universal-constant question as well, because Aldous--Fill's equivalence theorem gives universal two-sided constant comparison among the reversible-chain `tau_1` family, including total-variation mixing and `tau_1^(2)`. If a universal `K` existed for `tau_1^(2)` under lumping, composing those equivalence constants before and after lumping would give a universal constant for total-variation mixing, contradicting Hermon--Peres.

Therefore **P0242 is RESOLVED IN LITERATURE / EXCLUDED**, not admissible. The older exact `K=1` witness remains mathematically correct but is not the full current-status story.

Dated queries included exact searches for `Open Problem 4.45`, `induced chain`, `tau_1^(2)`, `lumping`, and `stopping-rule mixing`. The author-hosted chapter text and current book PDF still display Open Problem 4.45 without an update note. Required screenshot attempts on the relevant chapter PDF pages failed during this invocation (one cache miss and one HTTP 503); the parsed source text and the Hermon--Peres primary paper were accessible. That visual-access failure is recorded rather than silently treated as a successful page inspection.

Direct `operations/claims/P0242.md` was 404 at the ownership check. No claim was created because later literature already settles the source question.

## 8. Run disposition

P13 remains in **SUCCESSOR_ADMISSION_HOLD**. The successor source metric stays **UNMEASURED**, not zero, and no successor stagnation counter starts.

This run materially improved the admission map in two ways:

1. P0223 now has a rigorous exact projection theorem and is classified HARD rather than silently promoted to CLOSABLE.
2. P0242 is removed from apparent open inventory because Hermon--Peres 2018 already give a full negative answer to the universal-constant question once the Aldous--Fill equivalence theorem is applied.

No peer claim, shared root ledger, historical report, scheduler, email/Drive resource, public posting, workflow, permission, or force-push was modified.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  category: CLOSABLE_OUTSIDE_SUCCESSOR_ADMISSION
  status: SUCCESSOR_ADMISSION_HOLD
  source_id: NONE
  claim_id: NONE
  claim_path: NONE
  metric_name: successor_source_metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_movement_on_admitted_source: false
  section_B_methods_actually_tried: [2, 6, 25]
  successor_unchanged_runs: NOT_STARTED
  successor_stuck_recoveries: NOT_STARTED
  mandatory_first_screen:
    I0054:
      outcome: SKIP_PEER_OWNED_ACTIVE
      owner: R11
      newest_peer_metric: "59 -> 60"
  screens:
    P0223:
      ownership: UNCLAIMED_AT_CHECK
      source_status: CURRENT_OPEN_LOOKING_BOUNDED_SEARCH
      category_decision: HARD_OUTSIDE_NOT_CLOSABLE
      theorem: stationary_flow_root_projection_gap_at_least_epsilon_n_asymptotic_1_over_n
      exact_checker_commit: feaf5787f89a8607c0b1dce6efbee55cba48ec1f
      exact_output_commit: cea8c2803534154c116a10fc5eb537595bdf3784
      self_check_only: true
      claim_created: false
    P0242:
      ownership: UNCLAIMED_AT_CHECK
      source_status: RESOLVED_IN_LITERATURE
      resolution: Hermon_Peres_2018_unbounded_lumping_amplification_plus_Aldous_Fill_tau1_equivalence
      claim_created: false
  preserved_retirements:
    I0051: true
    C0021: true
    P22_P23_P25: true
    AF4_49ii_PROB20_13: true
  canonical_claim_created: false
  next_action: continue_highest_eligible_unassigned_CLOSABLE_source_current_literature_ownership_screen
```
