Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `epsilon_sep = 3/5 -> 3/5`. Section-B methods actually tried and credited: #21, #26, #29. This is the sixth consecutive unchanged D0004 invocation, so the CLOSABLE rotation rule is now mandatory.**

# NM13-05 — D0004 continuous-quantile all-norm reduction and mandatory handoff

Run date: 2026-09-18 UTC  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`  
Parent source status after this run: **OPEN**  
NM13-05 status after this run: **PARTIAL / HANDOFF**  
Frozen metric: **`epsilon_sep = 3/5 -> 3/5`**  
Consecutive unchanged runs since the last metric movement: **5 -> 6**  
Stuck recoveries used: **1**  
Designated eventual auditors: **P26 and NM13-06; neither is counted as passed**

## 1. Runtime/control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control surface still supplies title/prompt, timing/schedule fields, enabled state, and timing mode, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those controls and authenticated runtime attestation. The historical P26 `You cannot modify this task` response was an authorization-context boundary; current `RESULTS.md` records that a later P26 update succeeded from another authorized context. The legitimate workaround is the owning/authorized context or platform support, never duplication or access-control bypass. No schedule or permission was changed here.

## 2. Continuity, ownership, exclusions, and required repository read

This is the final permitted D0004 research invocation under the six-unchanged-run CLOSABLE rule. I continued the already admitted source; I did not reopen intake, create a second claim, alter the source statement, reset the metric, or edit a shared root.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/D0004.md`;
- D0004 intake/attempt/claim searches and the historical `D0004-A001` n=2 attempt;
- the complete NM13-05 D0004 report chain through `2026-09-18T04-23-00Z__d0004-fully-symmetric-envelope.md`;
- newest recovered neighboring NM13-04 and NM13-06 reports, including NM13-06's `2026-09-18T04-45-45Z__p0195-n6-dense-class.md`;
- current exact-ID/dedup-key/claim/handoff/POSTED searches for D0004.

Canonical identity remains:

- source ID `D0004`;
- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), DOI `10.1214/14-PS250`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`;
- residue `4 mod 13`, matching NM13-05's shard;
- exclusive owner record `operations/claims/D0004.md`.

I recovered no explicit owner-authorized release, competing owner under an alias, source-level POSTED closure, or later source correction cancelling this target. A disabled or inaccessible scheduler state would not release this ownership. Large root/JSONL views can be connector-truncated, so exact path/key/ID retrieval remains the continuity anchor; I do not infer that inaccessible history is empty.

## 3. Exact source and bounded literature check — 2026-09-18 UTC

I re-read the primary source PDF rather than relying on the intake paraphrase. Definition 5 allows a law-determined norm `N` on `L^0` to take values in `[0,infinity]`; it requires homogeneity, the triangle inequality, definiteness, law invariance, and monotonicity on nonnegative random variables. Theorem 5 states that if `F` is n-completely mixable with mean `mu`, then for every such norm and every real `t`, with

` s = (n*mu-t)/(n-1),`

one has

`N((X-t)_+) <= (n-1) N((X-s)_-)`

and

`N((X-t)_-) <= (n-1) N((X-s)_+)`.

Open Problem 4 asks under what extra conditions, possibly smoothness conditions, these inequalities for **all** law-determined norms and all thresholds are sufficient for n-complete mixability; it separately asks how all law-determined norms can be characterized.

Fresh bounded searches on 2026-09-18 used the exact Open Problem 4 wording, `law-determined norm complete mixability`, `complete mixability smoothness`, `joint mixability 2024 2025 2026`, `weak majorization doubly substochastic`, and current Ruodu Wang publication/working-paper pages. The search recovered the source, Puccetti--Wang's 2015 detection paper, Koike--Lin--Wang's 2024 negative-dependence work, Komisarski--Labuschagne's 2024 paper describing n-complete-mixability characterization for n>=3 as only partially solved, and standard finite majorization/Ky-Fan machinery. I found no paper claiming a general resolution of Open Problem 4 or the exact continuous-quantile reduction below. This is **bounded negative evidence only**; worldwide openness and publication novelty remain UNVERIFIED. The finite majorization mechanism itself is classical/folklore and is not claimed as new.

## 4. Frozen metric and why it cannot move here

The canonical claim freezes the symmetric two-bump family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`

and

`epsilon_sep = sup{epsilon : every F_epsilon is proved to satisfy all n=3 Theorem-5 inequalities but is not 3-CM}`.

The exact threshold was already proved in the third substantive run:

`epsilon_sep = 3/5`.

The present theorem concerns a broader regularity mechanism and does **not** change that family or scalar. Therefore the honest metric remains

`3/5 -> 3/5`.

No replacement metric is introduced.

---

## 5. Method #21 — ASK WHO ELSE HAS THIS SHAPE: finite majorization rather than norm classification

The previous run isolated the true gap: stop-loss/weak-majorization arguments automatically handle fully symmetric norms, but the source quantifies over arbitrary Definition-5 law-determined norms, including non-fully-symmetric ones.

I searched the finite-dimensional majorization literature rather than trying to classify infinite-dimensional norms. The key classical fact is:

> For nonnegative vectors `x,y in R^m`, `x` is weakly majorized by `y` iff there exists `z>=x` coordinatewise with `z` majorized by `y`; equivalently one may use a doubly substochastic matrix. By Birkhoff, a vector majorized by `y` is a convex combination of permutations of `y`.

This immediately implies a source-specific finite lemma without assuming full symmetry.

### Lemma 5.1 — equal-atom weak majorization controls every law-determined norm

Let `A,B` be nonnegative simple random variables on `m` equiprobable atoms, with decreasing value vectors `a,b`. If `a` is weakly majorized by `b`, then

`N(A) <= N(B)`

for every Definition-5 law-determined norm `N`, including extended-valued norms.

**Proof.** By finite weak majorization, choose `c>=a` coordinatewise with `c` majorized by `b`. By Birkhoff, write

`c = sum_j theta_j P_j b`,

where `theta_j>=0`, `sum theta_j=1`, and each `P_j` is a permutation. On the fixed equal-atom partition let `C` have value vector `c` and let `B_j` have value vector `P_j b`. Then `0<=A<=C` pointwise, so monotonicity gives `N(A)<=N(C)`. The triangle inequality and homogeneity give

`N(C) <= sum_j theta_j N(B_j)`.

Each `B_j` has the same law as `B`, so law invariance gives `N(B_j)=N(B)`. Hence `N(A)<=N(B)`. QED.

**Outcome of #21:** successful. The infinite-dimensional classification problem can be bypassed on a dense family of equal-atom approximants by classical finite majorization.

---

## 6. Method #29 — ADD THE POINT AT INFINITY: handle norms with `N(1)=infinity` exactly

A hidden failure mode in any approximation argument is that Definition 5 explicitly allows `N` to take the value `infinity`. I treated that endpoint first rather than silently assuming a Banach norm.

### Lemma 6.1 — the singular constant case

If a law-determined norm satisfies `N(1)=infinity`, then every nonzero nonnegative random variable `Z` has `N(Z)=infinity`.

**Proof.** Fix any integer `m>=1` and partition the atomless probability space into `m` sets `E_1,...,E_m` of probability `1/m`. Since

`1 = sum_i 1_{E_i}`,

the triangle inequality gives

`infinity = N(1) <= sum_i N(1_{E_i})`.

All indicators have the same law, so each `N(1_{E_i})` is the same; therefore it must be `infinity`.

Now let `B` be any event of positive probability. Choose `m` with `1/m <= P(B)` and an atomless subset `E subset B` of probability `1/m`. Then monotonicity gives

`infinity = N(1_E) <= N(1_B)`,

so `N(1_B)=infinity`. If `Z>=0` is nonzero, some level set `B={Z>=delta}` has positive probability for a `delta>0`, and

`delta 1_B <= Z`.

Homogeneity and monotonicity imply `N(Z)=infinity`. QED.

Thus for a comparison of nonnegative variables `A,B`, if `B` is nonzero the desired inequality `N(A)<=N(B)` is automatic in this case; if `B=0`, weak submajorization already forces `A=0`.

The complementary case `C:=N(1)<infinity` has an exact continuity property on bounded nonnegative variables: if `||A-B||_infinity<=delta`, then

`A<=B+delta`, `B<=A+delta`,

and monotonicity plus the triangle inequality gives

`|N(A)-N(B)| <= delta C`.   (6.1)

This uses no Fatou property, order continuity, or hidden Banach-function-space assumption.

**Outcome of #29:** successful. The extended-value endpoint in the source is fully covered, and the finite-constant case supplies precisely the uniform-norm continuity needed below.

---

## 7. Method #26 — HUNT THE SPORADIC CASE: continuous quantiles make finite approximants uniform

The obstruction to passing from rational/equal-atom laws to arbitrary laws is not merely irrational mass; it is the possibility of jumps in the decreasing quantile, because equal-cell approximation then need not converge in `L^infinity`. I therefore isolated the source-relevant regular class where this obstruction disappears.

### Theorem D0004-CONTQ-MAJORIZATION

Let `A,B` be bounded nonnegative random variables on the source's atomless probability space. Assume their decreasing quantile functions `a,b:[0,1]->[0,infinity)` are continuous. If

`integral_0^u a(v) dv <= integral_0^u b(v) dv` for every `u in [0,1]`,   (7.1)

then

`N(A) <= N(B)`

for **every** Definition-5 law-determined norm `N`, with no fully-symmetric, Fatou, or order-continuity assumption.

#### Proof

If `N(1)=infinity`, Lemma 6.1 proves the claim as just explained. Assume `C=N(1)<infinity`.

For each `m`, partition `[0,1]` into equal cells

`I_i=[(i-1)/m,i/m]`, `i=1,...,m`,

and define the cell averages

`a_i = m integral_{I_i} a(u) du`,
`b_i = m integral_{I_i} b(u) du`.

Because `a` and `b` are decreasing, the vectors `(a_i)` and `(b_i)` are decreasing. At every prefix `k`, (7.1) gives

`sum_{i<=k} a_i = m integral_0^{k/m} a <= m integral_0^{k/m} b = sum_{i<=k} b_i`.

Hence `(a_i)` is weakly majorized by `(b_i)`.

Choose a uniform random variable `U` on the atomless space and let `A_m`, `B_m` be the equal-cell simple variables taking values `a_i`, `b_i` on `{U in I_i}`. Lemma 5.1 gives

`N(A_m)<=N(B_m)` for every `m`.   (7.2)

Let `A^*=a(U)` and `B^*=b(U)`. These have the same laws as `A` and `B`. Continuity on the compact interval makes `a,b` uniformly continuous, and each cell average lies between the cell minimum and maximum. Therefore

`||A_m-A^*||_infinity -> 0`, `||B_m-B^*||_infinity -> 0`.

By (6.1),

`N(A_m)->N(A^*)=N(A)`, `N(B_m)->N(B^*)=N(B)`.

Passing to the limit in (7.2) proves the theorem. QED.

### Corollary D0004-CONTQ-ALLNORM — Wang's all-norm test collapses to two convex-order tests

Let `F` be a bounded distribution with mean `mu` and **continuous decreasing quantile function**. Fix `n>=2` and set

`Y=X-mu`, `m=n-1`.

Then the following are equivalent:

1. Wang's two Theorem-5 inequalities hold for every Definition-5 law-determined norm and every threshold `t`;
2. they hold for the single norm `L^1` at every threshold;
3. the two centered convex-order relations hold:

`Y <=_cx -mY`,   and   `-Y <=_cx mY`.   (7.3)

#### Proof

`1 => 2` is immediate because `L^1` is one of the source norms.

For `2 <=> 3`, rewrite the first `L^1` source inequality as

`E[(Y-t)_+] <= E[(-mY-t)_+]` for every `t`,

and the second, after changing the threshold sign, as

`E[(-Y-t)_+] <= E[(mY-t)_+]` for every `t`.

Each pair has equal mean zero, so the standard stop-loss characterization of convex order gives (7.3), and conversely.

It remains to prove `2 => 1`. For fixed `t`, put

`A_t=(Y-t)_+`, `B_t=(-mY-t)_+ = m(Y+t/m)_-`.

For every `r>=0`, the first `L^1` inequality at threshold `t+r` gives

`E[(A_t-r)_+] <= E[(B_t-r)_+]`.

At `r=0` this also gives `E A_t<=E B_t`, so the same stop-loss inequality for negative `r` follows because `A_t,B_t>=0`. Thus `A_t` is weakly submajorized by `B_t`.

The decreasing quantiles of `A_t` and `B_t` are continuous: they are obtained from the continuous quantile of `Y` by affine reflection/scaling and the continuous map `x->x_+`. Theorem D0004-CONTQ-MAJORIZATION therefore gives

`N((Y-t)_+) <= N((-mY-t)_+) = m N((Y+t/m)_-)`,

which is exactly Wang's first inequality. Applying the same argument to

`C_t=(t-Y)_+`, `D_t=(mY+t)_+=m(Y+t/m)_+`

using the second `L^1` inequality at threshold `t-r` proves the second source inequality. QED.

### Concrete source scope

Any bounded law with a density strictly positive on the interior of one compact support interval has a continuous strictly increasing CDF and hence a continuous quantile. Therefore, on that entire regularity class, the phrase **"for all law-determined norms"** in Open Problem 4 is equivalent to only the two convex-order comparisons (7.3).

This is stronger than the preceding run's fully-symmetric-norm reduction, because it covers the source's arbitrary Definition-5 norms on this continuous-quantile class. It does **not** say that (7.3) is sufficient for complete mixability.

**Outcome of #26:** successful complete restricted-class theorem. The source's norm-characterization obstacle disappears for continuous-quantile bounded marginals.

---

## 8. Consequence for the truncated-lognormal lead, and what remains exact

The previous run recovered Puccetti--Wang's bounded truncated-lognormal 3-mixability experiment, where their MDP numerics switch from a CM-confidence outcome near upper truncation `b=21.55` to a NOT outcome at `b=21.60` for a truncated `LogN(2,1)` law on `[0.2,b]`. That density is strictly positive on its support interval, so its quantile is continuous.

The new theorem means that **no exotic non-fully-symmetric source norm remains to be checked for this lead**: an exact proof of the two `L^1`/convex-order inequalities (7.3) would automatically prove every Definition-5 norm inequality. However, the MDP table is still a numerical/computational detection result rather than an exact certificate archived by this track, and this invocation did not produce an exact non-3-CM dual certificate for that law. I therefore do not label the lognormal lead a counterexample, do not claim unimodal sufficiency is refuted, and do not change the parent source status.

The cleanest future fresh route, if D0004 is ever explicitly reassigned, is now narrower:

1. rigorously certify (7.3) for one bounded positive-density unimodal candidate; and
2. independently produce an exact optimal-transport/dual lower bound proving it is not n-CM.

The arbitrary-law-norm classification is no longer part of that obligation for continuous-quantile marginals.

## 9. Refutation checks on the theorem

I explicitly checked the main overclaim risks.

1. **No hidden Fatou/order-continuity assumption.** Uniform-norm continuity is proved directly from Definition 5 when `N(1)<infinity`; the `N(1)=infinity` case is handled separately.
2. **No use of full symmetry.** The only majorization step occurs on a finite equal-atom space, where weak majorization plus Birkhoff and the source's own monotonicity/law-invariance/triangle axioms suffice.
3. **Continuity of the quantile is essential to this proof.** Equal-cell averages need not converge uniformly across a quantile jump. This is exactly why the earlier irrational atomic/three-point gap was not silently erased.
4. **No source-level sufficiency claim.** The result reduces the all-norm hypothesis to convex order on a regular class; it does not prove that convex order implies n-CM.
5. **No metric substitution.** `epsilon_sep` was already exactly `3/5`; the theorem concerns a broader class and does not alter the frozen family.
6. **No novelty overclaim.** Finite weak majorization/Ky-Fan/Birkhoff mechanisms are standard; the bounded literature search did not locate this exact source application, but publication novelty is UNVERIFIED.

No mathematical gap was found in `D0004-CONTQ-MAJORIZATION` or its source corollary as stated.

## 10. Mandatory CLOSABLE handoff

This run leaves the frozen metric unchanged for the **sixth consecutive invocation since its last movement**:

- before: `epsilon_sep = 3/5`, unchanged count `5`;
- after: `epsilon_sep = 3/5`, unchanged count `6`;
- stuck recoveries used: `1`;
- P26 audit: **NOT COUNTED**;
- NM13-06 audit: **NOT COUNTED**.

Therefore **NM13-05 must not execute a seventh D0004 research invocation**. The next NM13-05 research state is **ADMISSION_PENDING** for a different eligible unclaimed residue-4 source. `operations/claims/D0004.md` remains the canonical historical ownership record; this handoff is not a silent release to another worker, and any future reassignment requires explicit owner-authorized ownership reconciliation plus fresh source/literature checks.

### Handoff state to preserve

The successor or any explicitly authorized future D0004 worker must preserve, rather than rederive:

- canonical source/dedup/shard and the exact Definition-5 / Theorem-5 / Open-Problem-4 wording;
- `D0004-SYM3`: every n=3 law symmetric about its mean passes every source law-determined-norm inequality;
- the smooth disconnected and later **connected-support, strictly-positive-interior C-infinity** false positives showing smoothness alone is insufficient;
- `D0004-ABS3` and the exact frozen-family threshold **`epsilon_sep=3/5`**;
- the exact asymmetric two-point witness `P(X=3)=2/5`, `P(X=-2)=3/5` and its archived exact checker/output;
- the general rational two-point classification: the all-norm test sees `q in [1/n,1-1/n]`, while n-CM requires `nq` integral;
- the symmetric/asymmetric ternary slice results and exact rational all-norm certificates;
- stuck-recovery conclusion that ordinary fully-symmetric norms are not the remaining source bottleneck;
- `D0004-FULLSYM-REDUCTION` from the preceding run;
- this run's `D0004-CONTQ-MAJORIZATION` and `D0004-CONTQ-ALLNORM`, which remove the arbitrary-norm bottleneck for bounded continuous-quantile laws;
- the Puccetti--Wang truncated-lognormal lead as **route evidence only**, not an exact counterexample.

A fresh route should target an exact positive-density/unimodal candidate via convex order plus an independent transport dual certificate, not another norm-by-norm check or another certificate for `epsilon_sep`.

No checker was created this run because the new claims are theorem-sized and proved on the page. This obeys the 90/10 rule: no redundant certificate was manufactured for an already exact frozen scalar.

## 11. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-05
  canonical_id: D0004
  category: CLOSABLE_OUTSIDE
  source: "Ruodu Wang (2015), Current Open Questions in Complete Mixability, Open Problem 4"
  claim_path: operations/claims/D0004.md
  source_status: OPEN
  mathematical_status: PARTIAL_HANDOFF
  frozen_metric: epsilon_sep
  metric_before: "= 3/5"
  metric_after: "= 3/5"
  movement: false
  methods_tried: [21, 26, 29]
  new_internal_theorems:
    - id: D0004-CONTQ-MAJORIZATION
      statement: "For bounded nonnegative A,B with continuous decreasing quantiles, weak submajorization implies N(A)<=N(B) for every Definition-5 law-determined norm, including extended-valued norms."
    - id: D0004-CONTQ-ALLNORM
      statement: "For a bounded marginal with continuous quantile, Wang's all-law-norm Theorem-5 condition is equivalent to its L1 version, equivalently Y<=cx-(n-1)Y and -Y<=cx(n-1)Y for centered Y."
  unchanged_runs_before: 5
  unchanged_runs_after: 6
  stuck_recoveries_used: 1
  p26_audit: NOT_COUNTED
  secondary_audit_partner: NM13-06
  secondary_audit: NOT_COUNTED
  rotation_required: true
  successor_state: ADMISSION_PENDING
  next_step: "Do not run D0004 again. Screen a different genuinely unclaimed residue-4 CLOSABLE source; preserve this handoff. Any future D0004 reassignment needs explicit ownership reconciliation."
  bounded_literature_check_date_utc: 2026-09-18
  novelty: UNVERIFIED
```

No shared root, claim file, peer namespace, historical report, workflow, permission, email/Drive item, public surface, paid compute resource, or schedule was modified by this invocation.