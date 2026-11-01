Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `epsilon_sep = 3/5 -> 3/5`. Methods actually tried: #23, #17, #10.**

# NM13-05 — D0004 fully-symmetric norm envelope and exact obstruction to the unimodal refutation route

Run UTC: 2026-09-18T04:23Z  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen metric after this run: **exactly `epsilon_sep = 3/5` (unchanged)**.

## 1. Continuity, ownership, required reads, and runtime controls

I continued the already admitted D0004 target. I did not reopen intake, create a second claim, alter the source, or replace the frozen metric.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), DOI `10.1214/14-PS250`, arXiv:`1411.6190`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 `e67bdcaad853cdecbd238c339238d02b54c7704249727749f1fe86428f88b065`;
- SHA256 residue modulo 13: `4`, matching NM13-05's exclusive shard;
- exclusive owner: NM13-05 under `operations/claims/D0004.md`.

Before research I reread/recovered the current required controlling surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the D0004 claim and exact-ID/dedup/attempt history; my newest report `2026-09-18T03-24-12Z__d0004-stuck-recovery-1.md`; and the newest recovered neighboring NM13-04 and NM13-06 reports. NM13-06's current P0195 report moves its five-vertex Ising edge-monotonicity cutoff to six and does not supply a D0004 audit. No P26 or NM13-06 D0004 audit is counted.

The historical attempt `D0004-A001` remains the old `n=2` result and n>=3 stall. The current exact claim remains the only recovered D0004 ownership record. No release, handoff, alternate-ID owner, POSTED closure, or later source-specific correction was recovered. Large root/JSONL files can be connector-truncated; I used their current visible views plus targeted exact-ID, dedup, claim, attempt, and report searches and do not infer that inaccessible/deleted/non-master history is empty.

The previous report was the mandatory first Section-I thinking recovery after three unchanged runs. It chose **REFUTE INSTEAD OF PROVE** and reserved #23/#17/#10. I therefore use exactly those three methods here. The previous counters were `unchanged_runs_since_metric_movement = 4`, `stuck_recoveries_used = 1`.

The exposed task-control surface still has **no binding model-family selector and no reasoning-effort selector**. GPT-6/maximum remains prompt text only. This invocation actually runs GPT-5.6 Sol; authenticated reasoning telemetry is unavailable, so the reasoning level is `UNVERIFIED`. Enforcing GPT-6/maximum would require an authorized product/workspace/API/admin surface exposing those selectors and authenticated per-run attestation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary; the legitimate workaround is the owning/authorized scheduler or platform/admin surface, not task duplication or permission bypass. No support escalation is claimed.

## 2. Exact source and fresh bounded literature check — 2026-09-18 UTC

I rechecked the source PDF itself. Definition 5 includes homogeneity, triangle inequality, definiteness, law invariance, and monotonicity on nonnegative random variables. Theorem 5 says that if `F` with mean `mu` is n-CM, then for every law-determined norm and every real `t`, with

`s=(n mu-t)/(n-1)`, 

one has

`||(X-t)_+|| <= (n-1)||(X-s)_-||`,

`||(X-t)_-|| <= (n-1)||(X-s)_+||`.

Open Problem 4 asks when these inequalities, **for all law-determined norms and all thresholds**, become sufficient for n-complete mixability under extra conditions, possibly smoothness.

Fresh searches dated 2026-09-18 used the exact Open Problem 4 wording, `law-determined norm complete mixability`, `unimodal density not completely mixable`, `stop-loss order law-determined norm`, and 2025/2026 author/current-literature queries. I rechecked:

- Wang's source text;
- Puccetti–Wang, *Detecting complete and joint mixability*, JCAM 280 (2015), DOI `10.1016/j.cam.2014.11.050`;
- Wang–Wang, *Joint Mixability*, Math. Oper. Res. (2016);
- the later Koike–Lin–Wang negative-dependence line recovered in preceding runs;
- functional-analysis literature distinguishing symmetric/rearrangement-invariant norms from **fully symmetric** norms under Hardy–Littlewood submajorization, including Kalton–Sukochev and Sukochev–Zanin.

No later source-matching resolution of Open Problem 4 was recovered. This is **bounded negative evidence only**, not proof of worldwide openness or novelty. The stop-loss/submajorization mechanism used below is classical stochastic-order / Hardy–Littlewood machinery and is explicitly not claimed novel. What may be new is only its source-specific reduction of Wang's threshold family; publication novelty is **UNVERIFIED**.

A key correction to the tempting route is now explicit: the source quantifies over all Definition-5 norms, not merely the standard fully symmetric examples. Symmetric Banach function spaces that are not fully symmetric exist, so one may not silently replace the source's universal norm quantifier by `L^1`, by all `L^p`, or by Hardy–Littlewood submajorization.

## 3. Frozen metric: no movement

The claim freezes the smooth symmetric two-bump family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`

and tracks

`epsilon_sep = sup{epsilon : every frozen F_epsilon is proved to satisfy all n=3 source norm inequalities but is not 3-CM}`.

The third D0004 run proved the sharp value

`epsilon_sep = 3/5`.

That scalar is already exact. I do not rename the unimodal candidate threshold or a norm-class cutoff as the metric.

**Before:** `epsilon_sep = 3/5`.  
**After:** `epsilon_sep = 3/5`.  
**Movement:** none.

---

## 4. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: try to refute even after adding unimodality

The recovery report selected the simplest source-faithful unresolved strengthening

`F has a bounded continuous unimodal density + Norm_3(F)  =>?  F is 3-CM`,

where `Norm_3(F)` is the full all-law-determined-norm hypothesis from Theorem 5.

I therefore searched first for a **counterexample**, not a proof.

The most relevant published lead is already in the source's own reference [34], Puccetti–Wang (2015). Their homogeneous lognormal experiment truncates `LogN(2,1)` to `[0.2,b]`. Its density is unimodal; once `b>e`, it is nonmonotone and nonconcave. Their Table 4 places the numerical 3-CM transition between `b=21.55` and `b=21.60`, reporting `NOT` at `b=21.60`, while the elementary moderate-mean obstruction does not fail until about `b=22.65`. This is exactly the shape a refutation route wants: bounded, continuous, asymmetric, unimodal, and apparently non-3-CM before the basic endpoint/mean condition fails.

But it is **not yet an admissible exact D0004 counterexample** under this task's rules. The paper's conclusion at the inner threshold comes from its Mixability Detection Procedure coupled to the rearrangement algorithm. The paper itself describes these entries as computational observations in a theoretically unknown regime. I did not recover a checkable exact optimizer/dual certificate for the `b=21.60` row that could be imported as a finite proof. Therefore I do not promote the numerical transition to a theorem or to source closure.

A route-selection numerical check of the two `L^1` threshold gaps for the `b=21.60` truncated-lognormal lead found no negative gap on a dense grid. That computation is diagnostic only, is not archived as a claim, and is not used as proof. Its value is strategic: the candidate is not immediately killed by the easiest natural norm, so it remains worth exactifying.

**Outcome of #23:** the best published unimodal counterexample lead survives the cheap natural-norm screen, but exact nonmixability plus the source's universal norm quantifier are both still missing. No source-valid counterexample was claimed.

---

## 5. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the 21.55/21.60 transition exposes the right gap

The published numbers sharpen the problem rather than solve it:

- at `b=21.55`, Puccetti–Wang report their truncated lognormal as numerically CM at very low degree-of-mixability confidence;
- at `b=21.60`, they report `NOT` with a positive numerical degree interval;
- the moderate-mean condition remains satisfied there and only fails near `b=22.65`.

So the natural target is not another arbitrary smooth density. It is the narrow interval just beyond the reported transition, where the distribution is still source-shaped and all elementary endpoint constraints survive.

At the same time, searching the functional-analysis side produced a second, decisive number-free distinction: **symmetric/rearrangement-invariant does not imply fully symmetric** in infinite-dimensional function spaces. In particular, there are symmetric Banach function spaces whose norms are not monotone under Hardy–Littlewood submajorization. Extending such a norm by `+infinity` outside its space gives exactly the kind of extended law-determined norm allowed by Wang's Definition 5 (with the source's pointwise monotonicity retained in the symmetric-space definition).

This matters because every standard attempt to collapse the all-norm condition to stop-loss inequalities only controls fully symmetric norms. The irrational/continuous case therefore cannot be justified by density of rational finite-atom results. The earlier reports were correct to keep their rational restriction.

**Outcome of #17:** the literature supplies a very specific unimodal numerical lead, but also identifies the precise functional-analytic obstruction to declaring its natural-norm checks equal to the source hypothesis.

---

## 6. Method #10 — DERANDOMIZE: exact reduction for the fully symmetric norm envelope

The failed shortcut can nevertheless be made into a correct theorem if the norm class is stated honestly.

### Definition for this report

Call a law-determined norm `N` **fully symmetric** when for nonnegative random variables `A,B`,

`A preceq_w B  =>  N(A) <= N(B)`,

where `preceq_w` denotes Hardy–Littlewood weak submajorization, equivalently domination of every upper-quantile integral. This contains the usual `L^p` norms and the standard fully symmetric Banach-function-space norms. It is a strict subclass of the source's unrestricted Definition-5 norm class.

### Theorem D0004-FULLSYM-REDUCTION

Let `n>=2`, let `X` be integrable with mean `mu`, and put `Y=X-mu` and `m=n-1`. The following are equivalent:

1. Wang's two Theorem-5 inequalities hold for the single norm `L^1` at every real threshold.
2. Wang's two Theorem-5 inequalities hold for **every fully symmetric law-determined norm** at every real threshold.

Equivalently, the entire fully symmetric norm envelope is determined by the two stop-loss families

`E[(Y-u)_+] <= E[(-mY-u)_+]` for all real `u`,          (6.1)

`E[(u-Y)_+] <= E[(mY+u)_+]` for all real `u`.           (6.2)

#### Proof

`(2) => (1)` is immediate because `L^1` is fully symmetric.

For `(1) => (2)`, fix a real threshold `t` and define

`A_t=(Y-t)_+`,
`B_t=(-mY-t)_+`.

For every `r>=0`,

`E[(A_t-r)_+]
 = E[(Y-(t+r))_+]
 <= E[(-mY-(t+r))_+]
 = E[(B_t-r)_+]`,

where the inequality is (6.1) at `u=t+r`.

The classical stop-loss characterization of increasing-convex order therefore gives

`A_t <=_icx B_t`.

For nonnegative variables this is equivalent to Hardy–Littlewood weak submajorization,

`A_t preceq_w B_t`.

Hence every fully symmetric law-determined norm satisfies

`N(A_t) <= N(B_t)`.

By homogeneity,

`B_t=(-mY-t)_+ = m (Y+t/m)_-`,

so this is exactly Wang's first Theorem-5 inequality.

For the second inequality define

`C_t=(t-Y)_+`,
`D_t=(mY+t)_+`.

Again for every `r>=0`,

`E[(C_t-r)_+]
 = E[((t-r)-Y)_+]
 <= E[(mY+(t-r))_+]
 = E[(D_t-r)_+]`,

using (6.2) at `u=t-r`. Thus `C_t preceq_w D_t`, so every fully symmetric norm gives

`N(C_t)<=N(D_t)`,

which is precisely Wang's second inequality. QED.

### Corollary: the previous asymmetric ternary slice beyond rational parameters

Recall the exact three-point slice from the preceding substantive report,

`F_lambda = ((3+lambda)/6) delta_{-1} + ((1-lambda)/2) delta_1 + (lambda/3) delta_2`,

`0<=lambda<=1`.

It is the literal mixture

`F_lambda=(1-lambda)F_0+lambda F_1`,

where `F_0=(1/2)(delta_{-1}+delta_1)` and `F_1=(2/3)delta_{-1}+(1/3)delta_2`.

Both endpoint laws satisfy the two `L^1` threshold families: `F_0` by the earlier all-n symmetry theorem, and `F_1` because it is explicitly 3-CM. Since expectations are linear in the law, (6.1)-(6.2) hold for **every real lambda in [0,1]**. Therefore every `F_lambda` satisfies Wang's inequalities for every fully symmetric law-determined norm.

The occupancy proof from the previous report did not use rationality and still gives

`F_lambda is 3-CM  <=>  lambda=1`.

Hence for every real `0<=lambda<1`, including irrational lambda, the law is a false positive for the entire fully symmetric norm envelope. For **rational** lambda the previous finite equal-atom/direct-sum proof is stronger: it already establishes the source condition for *all* law-determined norms. For irrational lambda I make no such upgrade.

This exactly isolates what remains between the rational and continuous worlds: not any `L^p`, stop-loss, or standard fully symmetric norm, but the source's allowance of non-fully-symmetric law-determined norms.

**Outcome of #10:** successful exact theorem-sized reduction for the natural/fully-symmetric norm envelope, but the attempted derandomization of the published unimodal nonmixability lead fails at the source-universal norm step and at the lack of an exact nonmixability certificate.

---

## 7. Refutation checks on the new theorem

I explicitly checked the two places where an overclaim would occur.

1. **Stop-loss does not imply the source hypothesis for arbitrary Definition-5 norms.** The proof uses full symmetry exactly once, after obtaining weak submajorization. Symmetric Banach function spaces that are not fully symmetric are known, so deleting that adjective would be invalid. I therefore do not extend the theorem to all law-determined norms.

2. **Rational density does not close the irrational gap.** A source norm need not be order-continuous/Fatou-continuous in distributional mass. The preceding rational direct-sum proof works because it realizes a common finite equal-atom space exactly. Approximating an irrational mixing weight by rationals does not preserve the needed norm inequality for an arbitrary possibly non-fully-symmetric norm.

3. **The lognormal MDP row is not an exact certificate here.** The published computation is valuable route evidence, but without an independently checkable exact finite optimum or dual lower bound it does not satisfy this track's exact-certificate rule.

4. **No hidden metric move.** `epsilon_sep` was already proved equal to `3/5`. The new norm-envelope theorem does not alter that scalar.

No gap was found in `D0004-FULLSYM-REDUCTION` as stated, and no stronger source-universal statement is claimed.

## 8. Status, counters, and final-run obligation

Source status remains **OPEN / NM13-05 PARTIAL**.

This invocation changes the mathematical picture but not the frozen metric:

- `epsilon_sep: 3/5 -> 3/5`;
- `unchanged_runs_since_metric_movement: 4 -> 5`;
- `stuck_recoveries_used: 1`;
- P26 audit: **NOT COUNTED**;
- NM13-06 audit: **NOT COUNTED**.

Because `epsilon_sep=3/5` is already exact, another D0004 invocation cannot honestly move this metric. Therefore the **next D0004 run will necessarily be the sixth unchanged invocation and must preserve a handoff and rotate under the CLOSABLE rule**, regardless of whether it obtains one final restricted theorem.

The clean final research target is now sharply stated:

> Find an exact bounded continuous asymmetric unimodal law that (a) has a rigorous non-3-CM certificate and (b) satisfies the source inequalities for the remaining non-fully-symmetric Definition-5 norms; or prove that the published truncated-lognormal lead fails one explicit such norm.

Reserve three still-unused methods for that final run: **#21 ASK WHO ELSE HAS THIS SHAPE**, **#26 HUNT THE SPORADIC CASE**, **#29 ADD THE POINTS AT INFINITY**. In particular, #21 should mine explicit non-fully-symmetric norm constructions for a concrete witness norm rather than another `L^p` calculation.

No checker or finite artifact was created because the only new claim is theorem-sized and proved on the page. The numerical lognormal screen was route selection only and is not elevated to a finite claim.

## 9. `ledger_delta` for P26

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
  methods_tried: [23, 17, 10]
  new_internal_theorem:
    id: D0004-FULLSYM-REDUCTION
    statement: "For every n, the all-threshold L1 form of Wang's norm inequalities is equivalent to the all-threshold form for every fully symmetric law-determined norm; it does not cover arbitrary Definition-5 norms."
  fully_symmetric_slice_extension: "F_lambda passes every fully symmetric norm for all real lambda in [0,1]; source-universal all-norm result remains proved only for rational lambda."
  unimodal_lead: "Puccetti-Wang truncated LogN(2,1) on [0.2,b], numerical transition near b in (21.55,21.60]; not promoted to exact claim."
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  stuck_recoveries_used: 1
  p26_audit: NOT_COUNTED
  secondary_audit_partner: NM13-06
  secondary_audit: NOT_COUNTED
  next_methods: [21, 26, 29]
  next_step: "Final D0004 invocation: exactify the unimodal lead against non-fully-symmetric norms or produce a concrete witness norm; then preserve handoff and rotate because the sixth unchanged run is mandatory."
  bounded_literature_check_date_utc: 2026-09-18
  novelty: UNVERIFIED
```

No shared root, claim file, peer namespace, historical report, workflow, permission, email/Drive item, public surface, paid compute, or schedule was modified by this invocation.