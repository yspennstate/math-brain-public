Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `epsilon_sep = 3/5 -> 3/5`. Methods actually tried: #4, #12, #27.**

# NM13-05 — D0004 exact asymmetric rational three-point slice

Run UTC: 2026-09-18T02:24:51Z  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen metric after this run: **exactly `epsilon_sep = 3/5` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

I continued the already admitted D0004 target. I did not reopen intake, create or alter an ownership claim, change the source, or replace the frozen metric.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`;
- SHA256 residue modulo 13: `4`, matching NM13-05's exclusive shard;
- exclusive owner: NM13-05 under `operations/claims/D0004.md`.

Before new mathematics I reread or targeted-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current D0004 claim;
- the exact D0004 intake/dedup and historical attempt `D0004-A001`;
- my newest report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T01-23-13Z__d0004-symmetric-ternary-threshold.md`;
- newest recovered neighboring reports `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T01-27-56Z__p0457-bulk-distance-sandwich.md` and `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T01-28-00Z__p0195-high-temperature-perron.md`.

The intake still identifies D0004 as Wang Open Problem 4 with historical status `source_says_open` / attempted-unsolved. `D0004-A001` remains the prior n=2 result and explicitly stalled at n>=3 because the all-law-determined-norm hypothesis was not concrete. I preserve it rather than recounting it as progress. No release, handoff, competing owner, retired-source correction, POSTED closure, or alternate-ID ownership of D0004 was recovered.

Large root files and JSONL inventories can be connector-truncated when fetched wholesale. I used current root views plus exact ID/dedup/claim/attempt/report searches. I do not infer that inaccessible, deleted, non-master, or truncated history is empty.

The exposed task-control surface still provides title/prompt, timing/schedule fields, timing mode, and enabled state but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. This invocation actually identifies as GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so reasoning is `UNVERIFIED`. Enforcing GPT-6/maximum would require an authorized product/workspace/API/admin surface that exposes those controls and runtime attestation. The historical P26 `You cannot modify this task` result remains authorization/context-specific; later repository state records a successful P26 update from another authorized context. The valid workaround for another denial is the owning/authorized surface, not task duplication or permission bypass. No support escalation is claimed.

## 2. Exact source and fresh bounded literature check — 2026-09-18 UTC

I rechecked the source text. Wang's Definition 5 allows law-determined norms and Theorem 5 states that if an integrable law F with mean mu is n-CM, then for every law-determined norm and every real t, with

`s = (n mu - t)/(n-1)`, 

one has

`||(X-t)_+|| <= (n-1)||(X-s)_-||`,

`||(X-t)_-|| <= (n-1)||(X-s)_+||`.

The source then asks in Open Problem 4: if these inequalities hold for **all** law-determined norms and all t, under what extra conditions, possibly smoothness conditions, are they sufficient for n-complete mixability? The same paragraph separately asks how all law-determined norms should be characterized.

Fresh bounded searches on 2026-09-18 used the exact source title and Open Problem 4 wording, `law-determined norm complete mixability`, `complete mixability three-point distribution`, `finite support complete mixability`, and current Ruodu Wang / joint-mixability publication queries. I rechecked:

- Wang's 2015 source;
- Puccetti–Wang, *Detecting complete and joint mixability* (2015);
- Wang–Wang, *Joint Mixability* (2016);
- Koike–Lin–Wang, *Joint Mixability and Notions of Negative Dependence* (2024);
- Ruodu Wang's current homepage and the current `Joint mixability and negative dependence` working-paper series, with the homepage showing a 14 September 2026 update.

The 2024 paper studies negative-dependence and optimal-transport structure; the current working-paper series still describes joint/complete mixability as a challenging area. I did not recover a later source-matching resolution of Open Problem 4, nor a paper stating the exact rational asymmetric three-point slice below. This is **bounded negative evidence only**; it is not proof of worldwide openness and not a novelty certificate. The direct-sum majorization lemma below is standard finite symmetric-norm machinery in spirit, and the occupancy obstruction is elementary; publication novelty is **UNVERIFIED**.

Access note: parsed text of the source PDF was available and confirmed Theorem 5 and Open Problem 4. The required page-image screenshot backend was invoked for the relevant source page but returned a cache-miss error, so visual page inspection was unavailable. No claim below depends on OCR or an unread image.

## 3. Frozen metric: no movement

The claim freezes the smooth two-bump family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

with `U_epsilon` even, `C^infinity`, strictly positive on `(-epsilon,epsilon)`, and supported on `[-epsilon,epsilon]`, and tracks

`epsilon_sep = sup{epsilon : every frozen F_epsilon is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

The third D0004 run proved the exact value `epsilon_sep = 3/5`. It is already saturated and is not replaced by a support-size threshold, a lemma count, or the new finite-support parameter below.

**Before:** `epsilon_sep = 3/5`.  
**After:** `epsilon_sep = 3/5`.  
**Frozen-metric movement:** none.

The new result is source-relevant restricted-class progress.

---

## 4. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: choose one genuinely asymmetric three-point slice

The preceding run solved the symmetric three-point family exactly. I therefore did not attempt the full asymmetric three-point simplex. I first attacked complete mixability itself on a fixed asymmetric support where the zero-sum rows can be classified exactly.

For a rational parameter `lambda in Q intersect [0,1]`, define

`F_lambda = ((3+lambda)/6) delta_{-1} + ((1-lambda)/2) delta_{1} + (lambda/3) delta_{2}`.

Its mean is exactly zero:

`-(3+lambda)/6 + (1-lambda)/2 + 2lambda/3 = 0`.

For every `0<lambda<1`, this is a genuinely asymmetric three-point law. The endpoints are

`F_0 = (1/2)delta_{-1} + (1/2)delta_1`,

`F_1 = (2/3)delta_{-1} + (1/3)delta_2`.

The point of the slice is that it is simultaneously simple enough for an exact occupancy theorem and rich enough to contain a whole interval of false positives for the source norm test.

---

## 5. Method #12 — FIND WHAT IS CONSERVED: the support forces a unique zero-sum occupancy

Suppose `(X_1,X_2,X_3)` is a 3-complete mix with common marginal supported on `{-1,1,2}` and mean zero. A complete mix must satisfy

`X_1+X_2+X_3=0` almost surely.

For one realized row let

`N_- = #{i:X_i=-1}`,
`N_1 = #{i:X_i=1}`,
`N_2 = #{i:X_i=2}`.

The two exact conserved equations are

`N_- + N_1 + N_2 = 3`,

`-N_- + N_1 + 2N_2 = 0`.

Eliminating `N_-` gives the integer invariant

`2N_1 + 3N_2 = 3`.   (5.1)

The only nonnegative integer solution is

`N_1=0`, `N_2=1`, `N_-=2`.

Therefore every zero-sum row supported on `{-1,1,2}` is a permutation of

`(-1,-1,2)`.

This immediately gives the exact complete-mixability side of the slice:

### Lemma D0004-ASYM3-CM

For `lambda in [0,1]`, the law `F_lambda` is 3-CM **iff** `lambda=1`.

**Proof.** If `lambda<1`, then

`P_{F_lambda}(X=1)=(1-lambda)/2>0`,

but (5.1) says every coordinate of every zero-sum row has zero empirical mass at `1`, contradiction. At `lambda=1`, a uniformly random permutation of `(-1,-1,2)` is an explicit complete mix with marginal `F_1`. QED.

Thus the whole interior `0<lambda<1` is non-3-CM. It remains to decide the much harder half: whether the source's **all-law-determined-norm** condition still holds there.

---

## 6. Method #27 — SWAP THE QUANTIFIERS: prove a rational-mixture closure lemma for the all-norm test

Instead of checking every rational `lambda`, every threshold `t`, and every law-determined norm separately, I swap the order: first turn the endpoint all-norm statements into finite weak-majorization statements block by block, then prove that weak majorization survives rational direct sums.

### 6.1 Finite weak majorization

For a nonnegative vector `x in R_+^m`, write

`K_k(x) = sum of the k largest coordinates of x`, `0<=k<=m`.

Write `x preceq_w y` when

`K_k(x) <= K_k(y)` for every `k=1,...,m`.

On an m-point uniform probability space, every law-determined norm restricts to a permutation-invariant monotone norm. The standard finite Hardy–Littlewood–Polya / sub-Birkhoff argument gives

`x preceq_w y  =>  ||x|| <= ||y||`

for every such norm. Conversely, because the Ky Fan norms `K_k(|x|)` themselves are law-determined norms on the finite uniform space, an inequality that holds for **all** law-determined norms implies all the prefix inequalities and hence weak majorization.

This is the same exact finite mechanism used in the preceding rational two-point report; I use it here rather than claiming an infinite-dimensional characterization of all law-determined norms.

### 6.2 Direct sums preserve weak majorization

If

`x^(j) preceq_w y^(j)` for `j=1,...,J`,

then

`x^(1) directsum ... directsum x^(J) preceq_w y^(1) directsum ... directsum y^(J)`.

Indeed, for every total prefix size `k`,

`K_k(directsum_j x^(j))
 = max_{k_1+...+k_J=k} sum_j K_{k_j}(x^(j))
 <= max_{k_1+...+k_J=k} sum_j K_{k_j}(y^(j))
 = K_k(directsum_j y^(j))`.

This exact identity is the mechanism that lets one prove every rational point on the slice at once.

### 6.3 Endpoint blocks

For n=3 and mean zero, homogeneity rewrites Wang's two inequalities as

`||(X-t)_+|| <= ||(-2X-t)_+||`,   (6.1)

`||(t-X)_+|| <= ||(2X+t)_+||`.   (6.2)

Endpoint `F_0` is the symmetric Rademacher law. The earlier theorem `D0004-SYM-N` proves (6.1)-(6.2) for **every** law-determined norm and every threshold; therefore, on its two equal atoms, the transformed left vector is weakly majorized by the transformed right vector for each of (6.1) and (6.2).

Endpoint `F_1` is 3-CM by the explicit permutation of `(-1,-1,2)`. Wang's Theorem 5 therefore gives (6.1)-(6.2) for every law-determined norm and every threshold; hence the corresponding three-atom transformed vectors also satisfy weak majorization.

### 6.4 Exact rational mixture realization

Write the rational parameter as

`lambda=A/B`, `0<=A<=B`, with integers `A,B` and `B>0`.

Realize `F_lambda` on `6B` equiprobable atoms as a disjoint union of

- `3(B-A)` two-atom blocks of type `(-1,+1)`;
- `2A` three-atom blocks of type `(-1,-1,+2)`.

The total atom count is

`2*3(B-A)+3*2A=6B`.

The resulting empirical probabilities are exactly

`P(-1) = [3(B-A)+4A]/(6B) = (3B+A)/(6B) = (3+lambda)/6`,

`P(+1) = 3(B-A)/(6B) = (1-lambda)/2`,

`P(+2) = 2A/(6B) = lambda/3`.

Thus the empirical law is exactly `F_lambda`, not an approximation.

Fix any real threshold `t`. For (6.1), each two-atom block has its transformed left vector weakly majorized by its transformed right vector, and each three-atom block has the same property. The direct-sum lemma therefore gives weak majorization on all `6B` atoms. Finite HLP then gives (6.1) for **every** law-determined norm. The identical argument applies to (6.2).

Therefore:

### Theorem D0004-ASYM3-RATIONAL

For every rational `lambda in [0,1]`, the law

`F_lambda = ((3+lambda)/6) delta_{-1} + ((1-lambda)/2) delta_1 + (lambda/3) delta_2`

satisfies both of Wang's n=3 Theorem-5 inequalities for **every law-determined norm and every real threshold**.

Moreover,

`F_lambda is 3-CM  <=>  lambda=1`.

Hence every rational

`0 <= lambda < 1`

is a source-valid false positive for the all-norm test, and every rational `0<lambda<1` is a genuinely asymmetric three-point false positive.

The result is exact on its stated rational slice. I do **not** silently extend it to irrational lambda. The finite direct-sum proof uses a common equal-atom realization, and the source itself separately asks for a characterization of all law-determined norms; without such an infinite-dimensional characterization, density of rational parameters alone does not justify passing to irrational weights for arbitrary possibly non-order-continuous norms.

---

## 7. What this adds to the source picture

The previous reports established two qualitatively different failures of sufficiency:

1. smooth symmetric two-bump counterexamples with the exact frozen threshold `epsilon_sep=3/5`;
2. exact symmetric finite-support thresholds, including the odd-n ternary occupancy defect.

This run shows that symmetry is not the only finite-support source of failure. There is a **whole rational one-parameter family of genuinely asymmetric three-point laws** satisfying every n=3 law-determined-norm inequality while failing 3-complete mixability.

The mechanism is also structurally informative. The source norm condition is stable under rational block-direct sums at fixed mean once each endpoint inequality is expressed as finite weak majorization. Complete mixability, by contrast, is constrained by an exact integer occupancy invariant that can eliminate an atom entirely. The mismatch is therefore between a convex/majorization test and an arithmetic support constraint, not merely between symmetric and asymmetric laws.

This still does not answer Wang's request for useful extra conditions under which the all-norm inequalities become sufficient. In particular, this theorem is a **negative restricted-class classification**, not a source-level closure.

## 8. Refutation checks and scope limits

I attacked the new theorem at the points where it could fail.

1. **Mean check.** The displayed probabilities sum to one and the mean is exactly zero for every lambda.

2. **Could another zero-sum row use the +1 atom?** No. Equation (5.1), `2N_1+3N_2=3`, has the unique nonnegative integer solution `(N_1,N_2)=(0,1)`.

3. **Could lambda=1 still fail complete mixability?** No. Uniform permutation of `(-1,-1,2)` is an explicit exact coupling.

4. **Does the direct-sum proof use numerical approximation?** No. For rational `lambda=A/B`, the realization has exactly `6B` equal atoms and integer block counts.

5. **Does direct-sum weak majorization require the same block size?** No. The top-k variational identity allows arbitrary finite block lengths; here the lengths are two and three.

6. **Does an endpoint merely satisfy Lp inequalities rather than all norms?** No. `F_0` is covered by the already proved all-n theorem `D0004-SYM-N`; `F_1` is genuinely 3-CM, so Wang's own Theorem 5 supplies all law-determined norms.

7. **Can rational density be used to claim irrational lambda?** Not under the current proof. Arbitrary law-determined norms need not be assumed order-continuous. The theorem is intentionally stated only for rational lambda.

No checker-only artifact was manufactured. The result is a parameter-uniform theorem with an exact on-page proof, not a finite enumeration or solver-generated certificate. No floating-point calculation enters the argument.

## 9. Status, counters, and mandatory next invocation

New theorem-sized result this run:

- `D0004-ASYM3-RATIONAL`: exact classification of the rational asymmetric three-point slice; all source inequalities hold for every rational lambda in `[0,1]`, while 3-CM holds only at `lambda=1`.

Parent source status remains **OPEN / PARTIAL**. No P26 or NM13-06 audit is counted.

The frozen metric remains exact and unchanged:

`epsilon_sep = 3/5 -> 3/5`.

The unchanged-run counter was `2` before this invocation and is now

`unchanged_runs_since_metric_movement = 3`.

`stuck_recoveries_used = 0`.

Therefore the **next NM13-05 invocation is mandatory Section-I thinking-only stuck recovery**. It must make no new mathematical claim and must write the five-part stuck analysis: exact blocking statement, every route tried with failure reason, missing ingredient, simplest unproved special case, and nearest solved literature mechanism; then choose exactly one allowed recovery action. It must not produce another asymmetric finite-support lemma merely because one is available.

Prospective diagnostic lenses for that stuck report, **not attempted here and not counted in this run**, are:

- #6 DEFORM TO A POINT YOU CAN SOLVE;
- #20 FIND WHY THE ALGORITHM FAILS;
- #22 READ THE FAILURES, NOT THE SUCCESSES.

The closable six-unchanged-run rotation rule remains binding after the stuck recovery if the source obligation still does not move.

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE_OUTSIDE
  canonical_id: D0004
  source: "Ruodu Wang (2015), Current Open Questions in Complete Mixability, Open Problem 4"
  claim_path: operations/claims/D0004.md
  canonical_dedup_key: complete_mixability_open_2014::open_problem_4
  source_status: OPEN
  mathematical_status: PARTIAL
  frozen_metric: epsilon_sep
  metric_before: "= 3/5"
  metric_after: "= 3/5"
  movement: false
  methods_tried: [4, 12, 27]
  method_outcomes:
    4: exact rational one-parameter asymmetric three-point slice selected and completely classified
    12: unique zero-sum occupancy invariant 2*N_1+3*N_2=3 proves CM only at lambda=1
    27: finite weak-majorization direct-sum lemma proves all source norm inequalities for every rational lambda
  new_internal_theorems:
    - D0004-ASYM3-CM
    - D0004-ASYM3-RATIONAL
  counters:
    unchanged_runs_before: 2
    unchanged_runs_after: 3
    stuck_recoveries_used: 0
  audits:
    P26: NOT_COUNTED
    NM13-06: NOT_COUNTED
  literature_check:
    date_utc: 2026-09-18
    source_matching_resolution_found: false
    caveat: bounded_negative_search_not_worldwide_openness_or_novelty_certificate
  artifacts:
    new_finite_checker: none_not_applicable_parameter_uniform_exact_proof
  next_invocation: mandatory_section_I_thinking_only_stuck_recovery
  next_methods_prospective_not_tried: [6, 20, 22]
```

No shared root, peer namespace, historical report, claim file, schedule, workflow, email, Drive item, or public site was modified by this invocation.

END OF IMMUTABLE NM13-05 RUN REPORT
