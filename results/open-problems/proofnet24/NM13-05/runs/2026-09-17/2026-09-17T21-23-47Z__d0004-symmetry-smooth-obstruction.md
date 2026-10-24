Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. MOVEMENT: `epsilon_sep` UNMEASURED -> certified `epsilon_sep >= 1/3`. Methods actually tried: #2, #8, #11.

# NM13-05 — D0004 first research run

## 1. Status, source, ownership, and continuity

Track: NM13-05, CLOSABLE OUTSIDE.

Canonical target: `D0004`, Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4.

Canonical dedup key: `complete_mixability_open_2014::open_problem_4`.
SHA256: `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`.
Residue modulo 13: `4`, so the target belongs to NM13-05's shard.

Exclusive claim: `operations/claims/D0004.md`, created this run at commit `9c8ef66c970544c483e537e6d9c62ca976924f4e`, read back at that creation commit with blob `c75f9b7694e97880645dfe08f294b9cba976377b`.

The source's Theorem 5 says that if an integrable law `F` of mean `mu` is `n`-completely mixable, then for every law-determined norm `||.||`, every `t in R`, and

` s = (n*mu-t)/(n-1), `

we have

`||(X-t)_+|| <= (n-1)||(X-s)_-||`,  (N+)

`||(X-t)_-|| <= (n-1)||(X-s)_+||`,  (N-)

for `X~F`. Open Problem 4 asks when these all-norm/all-threshold necessary inequalities become sufficient for `n`-complete mixability, possibly after additional smoothness assumptions; it separately asks for a characterization of law-determined norms.

Historical attempt `D0004-A001` (8 September) proved the `n=2` case and then stalled at `n>=3`, because it did not know how to check the inequalities for *every* law-determined norm on a concrete nonmixable candidate. I preserve that attempt and do not reuse its `n=2` argument as movement.

Fresh ownership checks before claim creation found no `operations/claims/D0004.md`, no live owner, no handoff, and no posted/source-exact closure for D0004. Nearby D-series ownership was preserved; in particular D0005 and other D claims are distinct and untouched.

## 2. Fresh bounded literature check — 17 September 2026 UTC

Queries included exact combinations of

- `law-determined norm complete mixability Open Problem 4 Wang 2015`,
- `complete mixability law-determined norm converse`,
- `Current Open Questions in Complete Mixability Open Problem 4 solved`,
- `complete mixability symmetric smooth density disconnected support 3-CM`,
- `Ruodu Wang complete mixability 2024 2025 2026`,

plus the source page, Puccetti–Wang's *Detecting complete and joint mixability*, and Ruodu Wang's current publication / working-paper pages (page updated 14 September 2026).

The bounded search recovered the original 2015 Open Problem 4, the detection/algorithm literature, the 2019 centers paper, the 2024 *Joint Mixability and Notions of Negative Dependence* line, and current author work, but no source-matching general characterization and no located paper asserting the smoothness obstruction proved below. This is a dated bounded search only; it is not a claim of worldwide novelty.

## 3. Frozen metric

For `epsilon>0`, let

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

where `U_epsilon` has an even `C^infinity` density, is strictly positive on `(-epsilon,epsilon)`, and is zero outside `[-epsilon,epsilon]`.

The claim file freezes

`epsilon_sep = sup{epsilon: every such F_epsilon is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

Before this run: `UNMEASURED`.
After this run: `epsilon_sep >= 1/3`.

This is a lower bound, not an equality claim. The source-level problem remains OPEN.

## 4. Method #2 — ATTACK THE NEGATION FIRST

The negation to attack is: the Theorem-5 all-norm condition might already be sufficient after a mild regularity assumption.

The smallest obstruction is the Rademacher law

`P(X=-1)=P(X=1)=1/2`, `E X=0`, with `n=3`.

It is not 3-CM: a sum of three variables taking only values `-1,+1` is always an odd integer, hence can never equal the required constant `3 E X = 0`.

The nontrivial question is whether it nevertheless satisfies (N+) and (N-) for *every* law-determined norm and every threshold. Section 6 proves something stronger: **every law symmetric about its mean satisfies all source Theorem-5 inequalities when n=3**. Therefore the Rademacher law is an exact source-valid counterexample to bare sufficiency.

The important source consequence is not merely the atomic example. Section 7 smooths the obstruction without losing the all-norm inequalities, so arbitrary `C^infinity` regularity alone still does not make the condition sufficient.

## 5. Method #8 — DISCRETIZE

Before finding the direct norm proof, I examined the equal-atom version. On a finite equiprobable space a law-determined norm restricts to a permutation-invariant monotone norm on `R^m`. Weak submajorization of the absolute-value vectors therefore implies the norm inequality for every such norm.

For the two-atom Rademacher candidate and `n=3`, `mu=0`, `s=-t/2`, (N+) reduces by reflection to

`||(X-t)_+|| <= 2||(X-t/2)_+||`.

Writing the two coordinates in decreasing order gives four exact threshold regimes:

1. `t>=1`: left side is the zero vector.
2. `-1<=t<=1`: left vector `(1-t,0)`, comparison vector `(2-t,0)`.
3. `-2<=t<=-1`: left vector `(1-t,-1-t)`, comparison vector `(2-t,0)`; first prefix differs by `1`, total-sum difference is `2+t>=0`.
4. `t<=-2`: left vector `(1-t,-1-t)`, comparison vector `(2-t,-t-2)`; the first prefix differs by `1` and total sums are equal.

Thus the Rademacher obstruction passes every finite symmetric norm test exactly. This discretization exposed that the obstruction is not a numerical accident and suggested looking for a symmetry argument that bypasses any classification of law-determined norms.

No finite checker artifact is created for this theorem-sized argument: the inequalities are proved symbolically below rather than inferred from enumeration.

## 6. Method #11 — DUALIZE / REFORMULATE THE ALL-NORM CONDITION

The all-norm hypothesis looks intractable if attacked norm by norm. Reflection symmetry collapses it.

### Theorem D0004-SYM3

Let `X` be any real random variable with finite mean `mu` whose law is symmetric about `mu`. Then for `n=3`, for every law-determined norm in the source's Definition 5 and every `t in R`, both source inequalities (N+) and (N-) hold.

#### Proof

Translate by the mean, so `mu=0` and `X =^d -X`. For `n=3`,

`s=-t/2`.

By symmetry,

`(X-s)_- = (X+t/2)_- =^d (X-t/2)_+`.

So (N+) is equivalent to

`||(X-t)_+|| <= 2||(X-t/2)_+||`.   (1)

If `t>=0`, then pointwise

`0 <= (X-t)_+ <= (X-t/2)_+`,

so monotonicity of the norm proves (1) (even without the factor `2`).

Now let `t<0` and put `c=-t/2>0`. Then (1) becomes

`||(X+2c)_+|| <= 2||(X+c)_+||`.   (2)

Set

`A=(X+c)_+`, `B=(-X+c)_+`.

Since `X =^d -X`, law invariance gives `||A||=||B||`.

First, pointwise

`(X+2c)_+ <= (X+c)_+ + c = A+c`.

Therefore, by monotonicity and the triangle inequality,

`||(X+2c)_+|| <= ||A||+||c||`.   (3)

Second, for every real `x`,

`(x+c)_+ + (-x+c)_+ >= 2c`.

Hence `A+B >= 2c` pointwise. By monotonicity, homogeneity, the triangle inequality, and `||A||=||B||`,

`2||c|| = ||2c|| <= ||A+B|| <= ||A||+||B|| = 2||A||`.

Thus `||c||<=||A||`. Insert this into (3) to obtain (2).

This proves (N+) for all `t`.

For (N-), symmetry gives

`||(X-t)_-|| = ||(-X+t)_+|| = ||(X+t)_+||`,

and

`||(X-s)_+|| = ||(X+t/2)_+||`.

So (N-) is exactly (1) with threshold `-t`, already proved.

Therefore both source Theorem-5 inequalities hold for every law-determined norm and every threshold. QED.

### Meaning of the theorem

For `n=3`, the entire class of distributions symmetric about their mean is invisible to the source norm obstruction: all of them pass it, regardless of whether they are actually 3-CM. Thus any sufficient condition built from Theorem 5 must add information beyond symmetry plus arbitrary norm regularity.

This directly breaks the wall in `D0004-A001`: no characterization of all law-determined norms is required to certify a large counterexample class.

## 7. Smooth counterexamples: `C^infinity` regularity alone is insufficient

Fix `0<epsilon<=1/3`. Let `rho_epsilon` be any even `C^infinity` probability density supported on `[-epsilon,epsilon]`, positive on the open interval. For example, normalize

`rho_epsilon(u) = exp(-1/(1-(u/epsilon)^2))` for `|u|<epsilon`,

and set it to `0` for `|u|>=epsilon`.

Let `U_epsilon` have this density, let `B` be independent and uniform on `{-1,+1}`, and put

`X=B+U_epsilon`.

Then `X` has a `C^infinity` density

`f_epsilon(x)=(rho_epsilon(x-1)+rho_epsilon(x+1))/2`,

it is symmetric about `0`, and `E X=0`.

By Theorem D0004-SYM3, it satisfies (N+) and (N-) for every law-determined norm and every real `t`.

It is nevertheless not 3-CM.

Indeed, every value in its support can be written

`x=b+u`, `b in {-1,+1}`, `|u|<=epsilon`.

For any three such values, if exactly `k` of the signs are `+1`,

`x_1+x_2+x_3 = (2k-3) + (u_1+u_2+u_3)`.

The integer `2k-3` is one of `-3,-1,1,3`. If `epsilon<1/3`, then

`|u_1+u_2+u_3| <= 3 epsilon < 1`,

so the sum can never be `0`.

At the endpoint `epsilon=1/3`, equality `x_1+x_2+x_3=0` with `k=1` or `2` forces `|u_1+u_2+u_3|=1`, hence equality in the triangle inequality and therefore all three `u_i` are boundary values `+/- epsilon` with the required common sign. Each marginal assigns probability zero to those boundary points. Any coupling with these marginals therefore assigns probability zero to the union of events that a coordinate equals one of those finitely many boundary points. Thus the sum cannot be identically zero. The cases `k=0,3` are farther from zero.

A 3-complete mix of an integrable mean-zero law would have to satisfy `X_1+X_2+X_3=0` almost surely, so no such mix exists.

Therefore for every `0<epsilon<=1/3`, every member of the frozen two-bump `C^infinity` family satisfies all source norm inequalities yet is not 3-CM. Consequently

`epsilon_sep >= 1/3`.

### Corollary D0004-SMOOTH-OBSTRUCTION

No assumption consisting only of arbitrarily high ordinary smoothness of the density can make the source Theorem-5 norm condition sufficient for 3-complete mixability. Any successful extra condition must control geometry/shape/support in addition to smoothness (for example, some connected-support, monotonicity, concavity, or comparable structural hypothesis).

This is PARTIAL relative to Open Problem 4: it rules out a natural proposed class of extra conditions but does not characterize the conditions that are sufficient.

## 8. Refutation attempts against the new theorem

I tried to break D0004-SYM3 in the two places where the factor `2` enters.

- For `t>=0`, the result is pointwise and cannot fail under Definition-5 monotonicity.
- For `t<0`, the only potentially delicate step is `||c||<=||(X+c)_+||`. But it follows from the deterministic inequality `(X+c)_+ + (-X+c)_+ >= 2c` and exactly the source axioms: monotonicity, homogeneity, triangle inequality, and law invariance under `X =^d -X`. No expectation, integrability of the norm, or classification theorem is used.
- The endpoint `epsilon=1/3` was checked separately rather than hidden inside a strict support inequality; zero sums require marginal-null boundary values.

I found no logical gap in the claim as stated.

## 9. What this does and does not establish

PROVED internally, theorem-sized and fully written above:

- `D0004-SYM3`: every symmetric integrable law satisfies all source norm inequalities for `n=3`.
- `D0004-SMOOTH-OBSTRUCTION`: there are compactly supported `C^infinity` densities satisfying every source norm inequality but failing 3-CM; in the frozen two-bump family the certified support-separation range reaches `epsilon=1/3`.

NOT proved:

- a characterization of all extra conditions making the inequalities sufficient;
- sufficiency under connected support, positive density on its convex hull, unimodality, log-concavity, or any other structural hypothesis not proved here;
- novelty beyond the bounded prior-art search;
- source-level closure;
- any P26 or NM13-06 audit.

Source status: OPEN / PARTIAL progress.

## 10. Next mathematical attack

Do not repeat #2/#8/#11 next run. The most informative next question is whether the smooth obstruction can be made **strictly positive on its full convex-hull interval** while preserving a rigorous failure of 3-CM. That would rule out not just smoothness but smoothness plus connected support / positive density.

Suggested next Section-B triple: #5 (add a bridge-mass parameter and locate the exact loss of nonmixability), #15 (break the symmetric two-bump geometry on purpose while preserving the norm condition as far as possible), #20 (identify precisely why a complete-mix construction first becomes feasible when the gap is filled).

The frozen `epsilon_sep` metric is not reset by that investigation.

## 11. Audit state

Required eventual auditors for closure-sized work: P26 plus NM13-06. No audit requested as completed and no PASS is counted in this run. A peer audit should first attack Theorem D0004-SYM3 and the `epsilon=1/3` endpoint argument.

## 12. Scheduler/model control statement

The exposed scheduling interface provides title, prompt, schedule, enablement and timing mode, but no binding model selector, reasoning-effort selector, or guaranteed execution duration. The requested `GPT-6 / maximum` line is prompt text only. This invocation actually identifies itself as GPT-5.6 Sol; authenticated reasoning-effort metadata is unavailable, so reasoning is reported as UNVERIFIED. Historical modification denials for P26/P01/P03 remain authorization boundaries; this worker does not bypass them or create replacement schedules.

## 13. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-05
  canonical_id: D0004
  category: CLOSABLE_OUTSIDE
  source: "Ruodu Wang (2015), Current Open Questions in Complete Mixability, Open Problem 4"
  claim_path: operations/claims/D0004.md
  claim_creation_commit: 9c8ef66c970544c483e537e6d9c62ca976924f4e
  frozen_metric: epsilon_sep
  metric_before: UNMEASURED
  metric_after: ">= 1/3"
  movement: true
  mathematical_status: PARTIAL
  claims:
    - D0004-SYM3
    - D0004-SMOOTH-OBSTRUCTION
  methods_tried: [2, 8, 11]
  unchanged_run_count: 0
  recovery_count: 0
  outside_audits: 0/2
  required_auditors: [P26, NM13-06]
  source_level_closed: false
  prior_art_scope: "bounded fresh search on 2026-09-17; no source-matching resolution located"
  next_methods: [5, 15, 20]
  next_obligation: "test whether positive bridge density / connected support can retain all-norm condition while still failing 3-CM"
```

**End of complete run report.**