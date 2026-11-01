Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `epsilon_sep = 3/5 -> 3/5`. Methods actually tried: #1, #25, #30.**

# NM13-05 — D0004 exact symmetric three-point complete-mixability threshold

Run UTC: 2026-09-18T01:23:13Z  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen metric after this run: **exactly `epsilon_sep = 3/5` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

I continued the already admitted D0004 target. I did not reopen intake, create or alter a claim, change the source, or reset the metric.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`;
- SHA256 residue modulo 13: `4`, matching NM13-05's exclusive shard;
- exclusive owner: NM13-05 under `operations/claims/D0004.md`.

Before new mathematics I reread/recovered the current controlling surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current D0004 claim and exact-ID/dedup intake/attempt records;
- my newest D0004 report, `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T00-20-43Z__d0004-rational-two-point-classification.md`;
- newest recovered neighboring reports `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T00-16-18Z__p0457-logband-expansion-diameter.md` and `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T00-25-49Z__p0195-n4-orbit-sturm.md`.

The D0004 intake still records the same Open Problem 4 identity and the historical attempt `D0004-A001`; that attempt proves only `n=2` and explicitly stalls for `n>=3` because it could not make the all-law-determined-norm hypothesis concrete. The exact current claim remains the only recovered ownership record for D0004. No release, handoff, competing owner, posted source-level closure, or later source-specific correction was recovered.

The prior NM13-05 method triples, in order, are `#2/#8/#11`, `#5/#15/#20`, `#18/#19/#24`, and `#3/#14/#16`. This run therefore uses the previously announced new triple `#1/#25/#30` and does not repeat the preceding triple.

Large root and JSONL files can be connector-truncated when fetched wholesale. I used the visible current roots plus exact-ID, dedup-key, claim, attempt, report, and ownership searches. I do not infer that inaccessible, deleted, non-master, or truncated history is empty.

The currently exposed task-control schema still provides prompt/title, schedule or relative-start fields, timing mode, and enabled state, but **no binding model-family selector and no reasoning-effort selector**. The requested `GPT-6 / maximum` therefore remains prompt text only. This invocation actually runs GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so the reasoning level is `UNVERIFIED`. Enforcing GPT-6/maximum would require an authorized product/workspace/API surface that actually exposes model and reasoning controls and runtime attestation. The historical P26 `You cannot modify this task` event remains an authorization/context boundary; later repository state records a successful P26 update from another authorized context. The valid workaround for another denial is the owning account/workspace or an authorized product/admin surface, not cloning the task or bypassing permissions. No support escalation is claimed here.

## 2. Exact source statement and fresh bounded literature check — 2026-09-18 UTC

The source Theorem 5 says that if an integrable law `F` with mean `mu` is `n`-completely mixable, then for every law-determined norm, every real threshold `t`, and

`s=(n mu-t)/(n-1)`, 

one has

`||(X-t)_+|| <= (n-1)||(X-s)_-||`,

`||(X-t)_-|| <= (n-1)||(X-s)_+||`,

for `X~F`. Open Problem 4 asks under what additional conditions, possibly smoothness conditions, these necessary inequalities become sufficient for `n`-complete mixability.

Fresh bounded searches dated 2026-09-18 used the exact source title/Open Problem 4 wording, `law-determined norm complete mixability`, `complete mixability three-point distribution`, `complete mixability finite support discrete distribution`, and current author/joint-mixability publication queries. I rechecked Ruodu Wang's current homepage and the current `Joint mixability and negative dependence` working-paper series. The current series still describes analytical conditions for complete mixability as a challenge and lists the 2015 open-question survey; I did not find a later item stating a general solution of Open Problem 4 or the exact symmetric three-point threshold below. I also rechecked Puccetti–Wang's numerical detection paper and later joint-mixability/negative-dependence literature; these do not state a source-matching resolution of Open Problem 4.

This is **bounded negative evidence only**. It is not proof of worldwide openness and not a novelty certificate. The occupation-count argument below is elementary enough that it may be folklore; publication novelty of the exact formulation and its role against the all-norm test is **UNVERIFIED**.

## 3. Frozen metric: no movement

The claim file freezes the smooth two-bump family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

with `U_epsilon` having an even `C^infinity` density strictly positive on `(-epsilon,epsilon)` and zero outside `[-epsilon,epsilon]`, and tracks

`epsilon_sep = sup{epsilon : every frozen F_epsilon is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

The third D0004 run proved the exact value

`epsilon_sep = 3/5`.

That value cannot move upward or downward without contradicting its already proved sharpness, and I do not replace it by a new quantity merely because a different restricted class is now solved.

Therefore:

**before: `epsilon_sep = 3/5`; after: `epsilon_sep = 3/5`; no frozen-metric movement.**

The new theorem below is a source-relevant complete restricted-class result.

---

## 4. Method #1 — CHANGE THE CATEGORY: from coupling to an occupancy polytope

The previous run classified rational two-point laws. The next natural finite-support case is the symmetric three-point family

`T_a = a delta_{-1} + (1-2a) delta_0 + a delta_1`,  `0 <= a <= 1/2`.

The source all-norm inequalities themselves are already settled on this family by the prior theorem `D0004-SYM-N`: **every integrable law symmetric about its mean satisfies both Theorem-5 inequalities for every `n>=2`, every threshold, and every law-determined norm.** That theorem was proved in full in the immediately preceding report; I do not re-prove it here.

Thus the remaining question for `T_a` is purely combinatorial: when can `n` samples with marginal `T_a` be coupled so that their sum is exactly zero? This changes the category from law-invariant norm inequalities to an integer occupancy polytope.

For a candidate zero-sum vector `(x_1,...,x_n) in {-1,0,1}^n`, define

`N_+ = #{i : x_i=1}`,

`N_- = #{i : x_i=-1}`.

The zero-sum constraint is exactly

`N_+ = N_-`.

Hence every zero-sum support point is determined, up to permutation, by a single integer

`K=N_+=N_-`,  `0 <= K <= floor(n/2)`.

The whole complete-mixability problem has therefore collapsed to the one-dimensional simplex of possible laws of `K`.

---

## 5. Method #25 — COUNT THE SAME THING TWICE: exact threshold

### Theorem D0004-TERNARY-SYM

Fix `n>=2` and `0<=a<=1/2`. Let

`T_a = a delta_{-1} + (1-2a) delta_0 + a delta_1`.

Then:

1. `T_a` satisfies Wang's two Theorem-5 norm inequalities for every law-determined norm and every real threshold `t`.

2. `T_a` is `n`-completely mixable **if and only if**

`a <= floor(n/2)/n`.

Equivalently:

- for even `n`, every `T_a` is `n`-CM;
- for odd `n`, `T_a` is `n`-CM exactly when

  `a <= (n-1)/(2n)`,

  or, equivalently, when its zero atom has mass

  `1-2a >= 1/n`.

Thus for every odd `n>=3`, the source norm test has the entire false-positive interval

`(n-1)/(2n) < a <= 1/2`.

For the source-relevant case `n=3`, the exact threshold is

`a_* = 1/3`:

`T_a` is 3-CM iff `a<=1/3`, while **every** `T_a`, including every `a>1/3`, satisfies all source norm inequalities.

### Proof

Part 1 is exactly the prior theorem `D0004-SYM-N`, because `T_a` is symmetric about its mean `0`.

For Part 2, first prove necessity. Suppose `(X_1,...,X_n)` is an `n`-complete mix with each `X_i~T_a`. Since the marginal mean is zero, complete mixability forces

`X_1+...+X_n = 0` almost surely.

Let

`N_+ = #{i : X_i=1}`,

`N_- = #{i : X_i=-1}`.

Pointwise zero sum gives

`N_+ - N_- = 0`,

hence

`N_+ = N_- <= floor(n/2)`.

Take expectations. By the identical marginals,

`E N_+ = sum_i P(X_i=1) = n a`.

Therefore

`n a <= floor(n/2)`,

or

`a <= floor(n/2)/n`.

This is necessary.

Now prove sufficiency constructively. Put

`M=floor(n/2)`.

If `M=0` there is nothing to prove; for `n>=2`, `M>=1`. Assume

`a <= M/n`.

Define

`theta = n a / M`,

so `0<=theta<=1`. Build a random vector as follows:

- with probability `1-theta`, take the all-zero vector;
- with probability `theta`, take a deterministic vector containing exactly `M` entries `+1`, exactly `M` entries `-1`, and the remaining `n-2M` entries `0`, then apply a uniformly random permutation of its coordinates.

Every realized vector has sum zero. By permutation symmetry, for each coordinate `i`, conditional on the second branch,

`P(X_i=1 | second branch)=M/n`,

`P(X_i=-1 | second branch)=M/n`.

Hence unconditionally

`P(X_i=1)=theta M/n = a`,

`P(X_i=-1)=theta M/n = a`,

and therefore

`P(X_i=0)=1-2a`.

Thus every marginal is exactly `T_a`, while the sum is zero almost surely. Hence `T_a` is `n`-CM.

This proves the equivalence. QED.

### Source-level meaning

The all-law-determined-norm inequalities are completely blind to the odd-`n` occupancy defect in this family. For odd `n`, a constant-sum coupling must spend one of the `n` coordinate slots on a zero at least on average: the exact necessary and sufficient condition is zero-mass at least `1/n`. No law-determined norm inequality from Theorem 5 sees this arithmetic/occupancy requirement, because symmetry already forces those inequalities for every `a`.

This is stronger than the preceding isolated symmetric Rademacher obstruction: it gives the exact phase transition on a continuous one-parameter three-point family.

---

## 6. Method #30 — ONE SUPPORT SIZE AT A TIME: why three points close cleanly and where four points change

The support-size-three problem is now solved exactly because every zero-sum support point has a single occupancy coordinate `K`:

`(N_+,N_-,N_0)=(K,K,n-2K)`.

The feasible occupancy set is the integer interval

`K in {0,1,...,floor(n/2)}`,

and its convex hull is simply

`0 <= E K <= floor(n/2)`.

The marginal requirement is one scalar equation

`E K = n a`.

Hence the one inequality `n a<=floor(n/2)` is both necessary and sufficient. The explicit two-extreme-point coupling in the proof shows this without invoking a solver, compactness theorem, or numerical approximation.

This also identifies the precise obstruction to mechanically generalizing the argument. On a genuinely asymmetric three-point support, or on four or more support points, a zero-sum row can have several distinct occupation patterns and the marginal equations define a higher-dimensional transportation polytope. There is no longer one conserved count `K` whose expectation decides feasibility.

So method #30 succeeds at support size three, and it tells the next run what must be new: either solve an asymmetric three-point transportation polytope exactly, or find a source-valid obstruction showing why the all-norm inequalities do not control that polytope.

---

## 7. Refutation and edge-case checks

I attacked the theorem at the points where an unnoticed coupling could invalidate necessity.

1. **Could a zero-sum row have unequal numbers of `+1` and `-1`?** No: the only nonzero values are exactly `+1` and `-1`, so the row sum is `N_+-N_-`.

2. **Could dependence evade the expectation bound?** No: the inequality `N_+<=floor(n/2)` is pointwise on every zero-sum row. Dependence changes the law of `N_+`, not its pointwise maximum.

3. **Could the construction fail to have the stated zero mass?** In the nonzero branch there are `n-2M` zeros; in the zero branch there are `n` zeros. The calculated `+1` and `-1` marginals are each exactly `a`, so the remaining marginal mass is exactly `1-2a`.

4. **Even `n`.** Here `M=n/2`, so the condition is merely `a<=1/2`, already the probability constraint. This agrees with the general pairing fact that every symmetric law is `n`-CM for even `n`.

5. **Odd `n`.** Here the nonzero branch contains exactly one zero, so its zero marginal is `1/n`. Mixing it with the all-zero vector produces precisely every zero mass in `[1/n,1]`, i.e. every `a<=(n-1)/(2n)`.

6. **Endpoint `a=M/n`.** Then `theta=1`; the uniformly permuted extremal occupancy vector itself is a complete mix.

7. **Rademacher endpoint `a=1/2`.** For odd `n`, the condition fails exactly as expected; for even `n`, the balanced `n/2`-plus, `n/2`-minus permutation is a complete mix.

No gap was found in the theorem as stated.

Because this is a parameter-uniform theorem with a complete on-page proof, not a finite enumeration claim, I did not manufacture a checker-only artifact. No floating-point computation enters the proof.

## 8. What is and is not proved

New theorem-sized result in this run:

- `D0004-TERNARY-SYM`: for every `n>=2`, the symmetric three-point law `a delta_-1+(1-2a)delta_0+a delta_1` satisfies every source norm inequality, while exact `n`-complete mixability holds iff `a<=floor(n/2)/n`.

In particular, for `n=3` the all-norm hypothesis holds on the entire interval `0<=a<=1/2`, whereas 3-complete mixability holds exactly on `0<=a<=1/3`.

Not proved:

- a general characterization of the additional hypotheses making Theorem 5 sufficient;
- the asymmetric three-point class;
- a general finite-support transportation-polytope criterion stated in source terms;
- any improvement to the already exact frozen smooth-family metric `epsilon_sep=3/5`;
- publication novelty beyond the bounded search;
- source-level closure;
- any P26 or NM13-06 audit.

Therefore D0004 remains **OPEN / NM13-05 PARTIAL**.

## 9. Counters and next route

Before this invocation the unchanged-run counter was `1`, because the preceding rational two-point classification did not move the already sharp frozen metric.

After this invocation:

- frozen metric: `3/5 -> 3/5`;
- `unchanged_runs_since_metric_movement = 2`;
- `stuck_recoveries_used = 0`;
- P26 audit: not counted;
- NM13-06 audit: not counted.

Do not repeat `#1/#25/#30` next run. The next normal research run may still occur before the stuck threshold. The most source-relevant remaining finite target is the **asymmetric three-point law**, where the mean is no longer the central support point and the zero-sum occupancy set becomes a genuine small transportation polytope.

Planned genuinely new methods:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** solve one asymmetric one-parameter three-point slice exactly rather than claim the full simplex;
- **#12 FIND WHAT IS CONSERVED:** identify the affine occupancy invariant forced by the constant-sum equation and compare it with the source norm inequalities;
- **#27 SWAP THE QUANTIFIERS:** for a fixed support triple, characterize all rational marginal vectors that admit a constant-sum occupancy mixture, then ask which of those are separated by the all-norm condition.

If the next run again leaves `epsilon_sep` unchanged, the unchanged counter will reach three and the following invocation must use the Section-I thinking-only stuck protocol. The CLOSABLE six-unchanged rotation rule remains binding. I will not rename the ternary threshold as the frozen metric.

## 10. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-05
  canonical_id: D0004
  category: CLOSABLE_OUTSIDE
  source: "Ruodu Wang (2015), Current Open Questions in Complete Mixability, Open Problem 4"
  claim_path: operations/claims/D0004.md
  source_status: OPEN
  mathematical_status: PARTIAL
  frozen_metric: epsilon_sep
  metric_before: "= 3/5"
  metric_after: "= 3/5"
  movement: false
  methods_tried: [1, 25, 30]
  new_internal_theorems:
    - D0004-TERNARY-SYM
  unchanged_runs_before: 1
  unchanged_runs_after: 2
  stuck_recoveries_used: 0
  p26_audit: NOT_COUNTED
  secondary_audit_partner: NM13-06
  secondary_audit: NOT_COUNTED
  next_methods: [4, 12, 27]
  next_step: "Solve one asymmetric rational three-point slice exactly as an occupancy/transportation problem without changing epsilon_sep."
  bounded_literature_check_date_utc: 2026-09-18
  novelty: UNVERIFIED
```

No shared root, peer namespace, historical report, claim file, schedule, workflow, email, Drive item, or public site was modified by this invocation.