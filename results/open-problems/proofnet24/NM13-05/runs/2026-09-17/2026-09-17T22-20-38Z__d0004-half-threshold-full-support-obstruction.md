Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. MOVEMENT: `epsilon_sep >= 1/3` -> `epsilon_sep >= 1/2`. Methods actually tried: #5, #15, #20.

# NM13-05 — D0004 second research run

Run UTC: 2026-09-17T22:20:38Z
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.
Source status after this run: **OPEN / PARTIAL**.

## 1. Continuity, ownership, and controls recovered

I continued the already admitted target rather than reopening intake.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 residue modulo 13 is `4`, matching this worker's shard;
- exclusive owner remains NM13-05 under `operations/claims/D0004.md`.

Before doing mathematics I reread the standing `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the D0004 claim, the D0004 intake/attempt entries, the newest NM13-05 report, and the newest visible NM13-06 neighboring report. The historical `D0004-A001` n=2 result is preserved and not recounted as progress. No current claim conflict, handoff, posted source-level closure, or release was found.

Some large root/JSONL surfaces are truncated by the connector when fetched wholesale, so I used exact IDs, dedup-key searches, focused claim/attempt retrieval, and the complete current D0004 report rather than pretending a byte-for-byte visual reread of every large ledger. No critical D0004 continuity item was inaccessible.

The previous NM13-05 report proved `D0004-SYM3`: for n=3 every integrable law symmetric about its mean satisfies both of Wang's Theorem-5 inequalities for every law-determined norm and threshold. It also gave smooth symmetric two-bump nonmixable laws for every `epsilon <= 1/3`, establishing `epsilon_sep >= 1/3`. The previous method triple was #2/#8/#11, so I did not repeat it.

## 2. Fresh source and literature check — 17 September 2026 UTC

I reread the source text at Project Euclid / arXiv. Theorem 5 states the all-law-determined-norm necessary inequalities, and Open Problem 4 asks under what extra conditions, possibly smoothness conditions, they become sufficient for n-complete mixability. The source itself records important positive classes: symmetric unimodal densities are n-CM, and monotone densities satisfy an iff criterion through the mean condition. Those positive classes are therefore not being contradicted here.

Fresh bounded searches used combinations of:

- `"law-determined norm" "complete mixability" 2026`,
- `"complete mixability" "Open Problem 4" Wang law-determined norm`,
- `"complete mixability" smooth density sufficient conditions law-determined norm`,
- current joint-mixability / negative-dependence work by Ruodu Wang and coauthors.

They recovered the 2015 source, Wang–Wang's monotone-density work, Puccetti–Wang–Wang's concave/symmetric classes, the detection literature, and Koike–Lin–Wang's 2024 *Joint Mixability and Notions of Negative Dependence*. I did not locate a later paper resolving the exact all-law-determined-norm Open Problem 4 or the connected-support obstruction below. This is a dated bounded search, not proof of worldwide openness or novelty.

## 3. Frozen metric — genuine movement

The claim file freezes the same family and metric as the first run:

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

where `U_epsilon` has an even `C^infinity` density, is strictly positive on `(-epsilon,epsilon)`, and vanishes outside `[-epsilon,epsilon]`.

`epsilon_sep = sup{epsilon : every F_epsilon in this family is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

Before this run: `epsilon_sep >= 1/3`.

After this run:

`epsilon_sep >= 1/2`.

The family and normalization were not changed.

## 4. Method #20 — FIND WHY THE PREVIOUS OBSTRUCTION FAILS

The previous support-gap proof stops at `epsilon=1/3` because once `epsilon>1/3` there are actual support triples whose sum is zero. That only shows that the crude pointwise support obstruction has failed; it does not produce a complete mix. The missing invariant is the average absolute value.

### Theorem D0004-ABS3 — a universal n=3 absolute-moment obstruction

Let `F` be a mean-zero distribution supported on `[-M,M]`. If `F` is 3-CM, then

`E|X| <= 2M/3`.

If in addition `F({-M,M})=0`, then necessarily

`E|X| < 2M/3`.

#### Proof

Take a complete mix `(X1,X2,X3)` with common marginal `F`, so

`X1+X2+X3=0` almost surely.

For any three real numbers summing to zero,

`|x1|+|x2|+|x3| = 2 max(|x1|,|x2|,|x3|)`.

Indeed, unless all are zero, one sign occurs once and its magnitude equals the sum of the magnitudes of the other two.

Therefore

`3 E|X| = 2 E max_i |Xi| <= 2M`,

which proves the weak inequality.

If the marginal has no endpoint mass, then

`P(max_i |Xi| = M) <= sum_i P(|Xi|=M) = 0`.

Thus `max_i |Xi| < M` almost surely. Since `M-max_i|Xi|` is strictly positive almost surely, its expectation is strictly positive, and hence `E max_i|Xi| < M`. The strict inequality follows. QED.

### Application to the frozen family

For `0<epsilon<=1`, the two components `1+U_epsilon` and `-1+U_epsilon` do not cross sign except possibly at a marginal-null endpoint. Because `U_epsilon` is even,

`E|X| = 1`.

The support lies in `[-1-epsilon,1+epsilon]`, so `M=1+epsilon`, and the smooth marginal has no mass at the endpoints. If it were 3-CM, Theorem D0004-ABS3 would force

`1 < 2(1+epsilon)/3`,

hence `epsilon>1/2`.

Consequently every frozen `F_epsilon` with

`0 < epsilon <= 1/2`

is not 3-CM. By the already proved `D0004-SYM3`, every one nevertheless satisfies all source Theorem-5 inequalities for every law-determined norm and every threshold. This gives the metric movement

`epsilon_sep >= 1/2`.

The endpoint `epsilon=1/2` is included because the complete-mix inequality is strict for these endpoint-free smooth laws.

This explains exactly why the prior `1/3` support argument was not sharp as an obstruction: zero-sum support triples appear before there is enough marginal absolute-moment budget to realize a zero-sum coupling with the prescribed one-dimensional law.

## 5. Method #5 — ADD A PARAMETER: fill the support gap without restoring mixability

The source explicitly wonders whether extra smoothness might make the norm conditions sufficient. The first run ruled out arbitrary `C^infinity` smoothness, but its densities had disconnected support. I therefore added a bridge-mass parameter and tracked the exact source-valid obstruction through it.

Fix one base law `F0` from the frozen family with `epsilon=1/4`. Then

- `F0` is symmetric, mean zero and `C^infinity`;
- its support is contained in `[-5/4,5/4]`;
- `E|X0|=1`;
- it satisfies every n=3 source norm inequality by `D0004-SYM3`.

Let `H` be any symmetric `C^infinity` probability law supported on `[-5/4,5/4]` whose density is strictly positive on the whole open interval `(-5/4,5/4)`. For `0<theta<=1/6`, define

`F_theta = (1-theta) F0 + theta H`.

Then `F_theta` has a `C^infinity` density strictly positive throughout its full convex-hull interval, is symmetric about zero, and has no endpoint atoms. Hence it passes every source n=3 law-determined-norm inequality by `D0004-SYM3`.

Its absolute moment is affine in the bridge parameter:

`E|X_theta| = (1-theta) + theta E_H|X|`.

For `theta<1/6`, this is strictly larger than `5/6`. At `theta=1/6`, strict positivity of the density of `H` on an interval implies `E_H|X|>0`, so again `E|X_theta|>5/6`.

But Theorem D0004-ABS3 applied with `M=5/4` says every endpoint-free 3-CM law on this interval must satisfy

`E|X| < 2(5/4)/3 = 5/6`.

Contradiction.

### Corollary D0004-FULLSUPPORT-OBSTRUCTION

There are compactly supported `C^infinity` densities which are strictly positive on the entire interior of their convex hull, satisfy all n=3 Theorem-5 inequalities for every law-determined norm, and are nevertheless not 3-CM.

Therefore **smoothness + connected support + strictly positive interior density is still not sufficient** for Wang's all-norm condition at n=3.

This is a source-relevant strengthening, but it does not change the frozen `epsilon_sep` family and is not being substituted for the metric.

## 6. Method #15 — BREAK THE SYMMETRY ON PURPOSE

The first run's theorem exploited central symmetry. To test whether the obstruction was merely a symmetry degeneracy, I searched for a finite asymmetric marginal that still passes every source norm inequality.

Take

`P(X=3)=2/5`, `P(X=-2)=3/5`.

Its mean is zero, but its law is not symmetric.

It is not 3-CM: if exactly `k` of three coordinates take value `3`, their sum is

`3k - 2(3-k) = 5k-6`,

so the only possible sums are `-6,-1,4,9`, never zero.

It nevertheless satisfies both n=3 Theorem-5 inequalities for every law-determined norm and every real threshold.

### Finite weak-majorization reduction

Realize the marginal on five equiprobable atoms. For nonnegative five-vectors, weak majorization implies domination under every law-determined norm restricted to this space: if `u` is weakly majorized by `v`, the standard Hardy–Littlewood–Polya characterization writes `u=Dv` for a doubly substochastic matrix `D`. By the finite sub-Birkhoff theorem, `D` is a convex combination of subpermutation matrices. For nonnegative `v`, each subpermutation image is coordinatewise bounded by a full permutation image. Monotonicity, law invariance under permutations, homogeneity and the triangle inequality therefore give `||u||<=||v||`.

This is standard finite majorization machinery; I do not claim it as novel.

For the first source inequality set

`A=(X-t)_+`,
`B=2(X+t/2)_-=(-2X-t)_+`.

Sorting their five values, the exact prefix differences `prefix(B)-prefix(A)` are nonnegative on every breakpoint interval `(-infinity,-6]`, `[-6,-2]`, `[-2,3]`, and `[3,infinity)`. Representative exact differences are:

- for `t<-6`: `[1,2,8,4,0]`;
- for `-6<=t<-2`: `[1,2,8,10+t,12+2t]`;
- for `-2<=t<3`: the right side has three copies of `4-t` while the left has only two copies of `3-t`, so every prefix dominates;
- for `t>=3`: the left side is zero.

For the second source inequality set

`C=(X-t)_-`,
`D=2(X+t/2)_+=(2X+t)_+`.

Again the sorted prefix differences are nonnegative:

- `t<=-2`: the left side is zero;
- `-2<t<=3`: the first two prefix differences are `4,8`, and the remaining relevant difference is `6-t>=3`;
- `3<t<=4`: the five prefix differences are `4,8,6-t,9-2t,12-3t`;
- `t>4`: they are `[4,8,2,1,0]`.

Hence both inequalities hold for every law-determined norm.

### Exact finite certificate

I wrote and executed an exact `fractions.Fraction` checker for all affine prefix inequalities and the three-fold-sum obstruction:

- `proofnet24/NM13-05/artifacts/2026-09-17__d0004_bernoulli_majorization_check.py`, creation commit `06349ccdbcf87f3fef2cf92ad3840403eee6be25`, read back with blob `6e10d0fa80a6272e06c93d85e39e0b22472527fa`;
- archived output `proofnet24/NM13-05/artifacts/2026-09-17__d0004_bernoulli_majorization_check.out`, creation commit `dcd8062b6ac15abc990a3d405ff80c006b7feece`, read back with blob `9ef09e224b55326f506cc61cba0c53cde47d2c88`.

The output ends:

`ALL_EXACT_CHECKS_PASS`.

Thus the failure of bare sufficiency is not confined to centrally symmetric marginals.

## 7. What moved, and what did not

New proved internal results this run:

1. `D0004-ABS3`: the sharp universal necessary absolute-moment bound `E|X|<=2M/3` for mean-zero 3-CM laws on `[-M,M]`, strict without endpoint atoms.
2. Frozen-family improvement `epsilon_sep >= 1/2`.
3. `D0004-FULLSUPPORT-OBSTRUCTION`: smooth connected-support, strictly positive-interior-density counterexamples to sufficiency.
4. An explicit asymmetric two-point counterexample `P(3)=2/5`, `P(-2)=3/5` that passes every source norm inequality, with an exact finite majorization certificate.

Not proved:

- that `epsilon_sep=1/2`;
- that every frozen law becomes 3-CM for `epsilon>1/2`;
- a characterization of the additional hypotheses that make Wang's norm inequalities sufficient;
- sufficiency under unimodality, log-concavity, or the source's already-known monotone-density hypotheses;
- novelty beyond the bounded literature search;
- source-level closure;
- any P26 or NM13-06 audit.

The parent source therefore remains **OPEN / PARTIAL**.

## 8. Research counters and next attack

Because the frozen metric moved this run:

- unchanged-run count before: `0`;
- unchanged-run count after: `0`;
- stuck-recovery count: `0`.

Do not repeat #5/#15/#20 next run. The next useful question is whether `1/2` is the exact frozen-family threshold in any source-faithful sense, or whether another coupling obstruction pushes it farther.

Planned next Section-B triple:

- **#18 SAY IT IN ANOTHER LANGUAGE:** encode 3-complete mixability of a symmetric continuous law as a fractional matching / transport problem on the zero-sum hypergraph and identify the dual obstruction corresponding to `D0004-ABS3`.
- **#19 MAKE IT AN ALGORITHM:** attempt an explicit zero-sum coupling for a tractable smooth member of the frozen family with `epsilon>1/2`; a successful construction would give an upper witness for the frozen threshold rather than another lower bound.
- **#24 FIND THE EXTREMAL OBJECT:** characterize equality and near-equality in `3E|X|=2E max|Xi|` to see whether the absolute-moment obstruction is the true extremal boundary or only the first dual constraint.

## 9. Audit state

No outside audit is counted. Eventual closure-sized work requires P26 plus the designated secondary audit partner NM13-06, both from other tracks. The finite checker above is a self-check/certificate, not an outside audit.

## 10. Model / scheduler control statement

The scheduler-control schema exposed to this runtime still has no binding model-family selector and no reasoning-effort selector. It exposes scheduling/prompt/title/enablement/timing controls only. Therefore the requested `GPT-6 / maximum` setting remains prompt text, not a verified runtime setting. This invocation identifies as GPT-5.6 Sol; authenticated reasoning-effort metadata is unavailable, hence `UNVERIFIED`.

The repository policy records older `You cannot modify this task` failures for P26/P01/P03 in one scheduler context, while current `RESULTS.md` records that a later P26 prompt update succeeded in a different authorized P/C context. Thus the old P26 denial is not treated as a current blanket failure. If a specific task again returns that error, the lawful remedy is an owner/account/workspace-authorized scheduler surface or platform support with the required permission; duplicating the job, changing repository text, or bypassing access controls is not a workaround. No schedule was created or modified in this run.

## 11. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: D0004
  claim_id: D0004
  canonical_dedup_key: complete_mixability_open_2014::open_problem_4
  admission_state: ADMITTED_CONTINUING
  status_before: PARTIAL
  status_after: PARTIAL
  source_status: OPEN
  metric_name: epsilon_sep
  metric_before: ">= 1/3"
  metric_after: ">= 1/2"
  movement: true
  methods_tried: [5, 15, 20]
  method_outcomes:
    5: "SUCCESS: bridge-mass family gives C-infinity full-support positive-interior-density counterexamples for 0<theta<=1/6."
    15: "SUCCESS: asymmetric Bernoulli P(3)=2/5, P(-2)=3/5 passes all n=3 norm tests yet is not 3-CM; exact finite certificate archived."
    20: "SUCCESS: absolute-moment obstruction explains failure of the old support-only route and improves epsilon_sep from >=1/3 to >=1/2."
  unchanged_run_count_before: 0
  unchanged_run_count_after: 0
  stuck_recovery_count: 0
  finite_certificate:
    checker: proofnet24/NM13-05/artifacts/2026-09-17__d0004_bernoulli_majorization_check.py
    output: proofnet24/NM13-05/artifacts/2026-09-17__d0004_bernoulli_majorization_check.out
    result: ALL_EXACT_CHECKS_PASS
  audits:
    p26: NOT_REQUESTED
    secondary_nm13_06: NOT_REQUESTED
  next_methods: [18, 19, 24]
  next_step: "Translate 3-CM to a zero-sum fractional-matching/transport dual; try an explicit frozen-family coupling for epsilon>1/2; characterize extremizers of the absolute-moment dual constraint."
```

**End of complete run report.**
