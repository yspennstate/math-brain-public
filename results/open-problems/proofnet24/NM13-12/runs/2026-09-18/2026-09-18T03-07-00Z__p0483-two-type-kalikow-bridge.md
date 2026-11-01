Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT:** `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))` stayed exact. Section-B methods actually tried: **B19 MAKE IT AN ALGORITHM, B23 DO WHAT THE PROPOSER DID NOT EXPECT, B26 HUNT THE SPORADIC CASE.** New partial theorem: an exact two-type Green-function/Kalikow reduction gives a closed-form sufficient ballisticity inequality and a source-valid sign-changing-drift example with certified Kalikow drift `>=1/35`.

# NM13-12 — P0483 two-type Kalikow bridge after stuck recovery 1

Date: 2026-09-18 UTC  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Canonical source / claim ID: `P0483` / `operations/claims/P0483.md`  
Historical alias: `C0041`  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Canonical selection residue: `11 mod 13`  
Overall source status after this run: **OPEN**  
Local status after this run: **PARTIAL / source-valid restricted-class theorem; publication novelty UNVERIFIED**

## 1. Runtime/model disclosure and task-control reality

The prompt requests GPT-6 with maximum reasoning. That is **not** the runtime I can verify. The model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The task-control surface exposed to this runtime still provides title/prompt, schedule or relative-start fields, timing mode and enabled state. It exposes **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text rather than a scheduler-enforced setting. Making it binding would require an owner-authorized product/workspace/API/admin surface whose schema exposes those controls together with per-run runtime attestation.

Repository policy preserves an older P26-context response `You cannot modify this task` and a later successful P26 update from another authorized context. The only legitimate workaround for a future denial is the owning account/workspace or another authorized admin/product surface; this worker does not clone an inaccessible task or bypass access control. No schedule was created, modified, disabled, or duplicated in this invocation.

## 2. Continuity and ownership recovered before mathematics

This run continues the already-admitted P0483 target. It does **not** reopen intake and does not create, replace, or alter `operations/claims/P0483.md`. That create-only claim still names NM13-12 as exclusive owner. The canonical integrated dedup key has SHA-256 residue `11 mod 13`, matching this worker.

Before the new attack I reread or targeted-search-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the integrated intake/dedup material for P0483/C0041 and the prior campaign attempt;
- all six preceding NM13-12 reports, newest first;
- newest visible neighboring reports from NM13-11 and NM13-13;
- source/claim searches for P0483 aliases, ownership, handoffs, attempts, audits, retirement, POSTED/settled state, and source corrections.

No release, handoff, retirement, competing owner, posted source resolution, or completed P26/NM13-13 audit for P0483 was recovered. Repository-wide connector searches are bounded; this is source-specific continuity recovery rather than a claim of byte-for-byte visibility over every historical blob.

The method history is preserved and not restarted:

1. run 1: `B2/B6/B30`;
2. run 2: `B18/B24/B4`;
3. run 3: `B5/B21/B22`;
4. run 4: `B1/B11/B28`;
5. run 5: `B3/B13/B27`;
6. stuck recovery 1: `B12/B20/B25`, thinking-only.

The preceding stuck report chose exactly one recovery action — **PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM** — and explicitly nominated `B19/B23/B26` for the next substantive run. Those are the three methods genuinely attempted below.

## 3. Source and fresh bounded literature/status check — 2026-09-18 UTC

The exact source remains Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment*, Open Question 2.20:

> for nearest-neighbor RWRE on `Z^d`, `d>=2`, satisfying `(UE)` and `(IID)`, does transience in direction `ell` imply ballisticity in direction `ell`?

The source page was recovered in parsed search text from the authors' PASI lecture PDF, and Campos–Ramírez later restated the same assertion as Conjecture 1.1 in *Probability Theory and Related Fields* 160 (2014), 189–251, DOI `10.1007/s00440-013-0527-7`. Direct browser retrieval of the PASI PDF again failed (one mirror timed out and the authors' PDF endpoint returned a gateway error), so the required page-image/screenshot inspection was unavailable this run. I do not substitute OCR or pretend the failed screenshot succeeded.

Fresh bounded searches on 2026-09-18 used the exact source wording together with `directional transience`, `positive speed`, `uniformly elliptic`, `iid`, `RWRE`, `Kalikow condition`, `two-point environment`, `finite support`, `2025`, and `2026`. They recovered:

1. **Guerra–Ramírez, CPAM 73 (2020), 2087–2103, DOI `10.1002/cpa.21877`.** Its abstract still states that it is believed directional transience in a uniformly elliptic i.i.d. environment forces ballisticity, while proving equivalence of the stronger conditions `(T)`, `(T')`, `(T)_gamma` and `(P)_M`.
2. **Sznitman–Zerner, Ann. Probab. 27 (1999), 1851–1869, DOI `10.1214/aop/1022874818`.** The standard Kalikow criterion in the uniformly elliptic i.i.d. setting yields a ballistic law of large numbers. Contemporary and later RWRE sources explicitly summarize this implication.
3. **Fukushima–Ramírez, arXiv:1902.08920 (2019).** They exhibit high-dimensional ballistic examples outside Kalikow's condition, so Kalikow is a sufficient route, not a necessary characterization of the source problem.
4. Searches specifically for `two-point/two-valued/finite-support environment + Kalikow condition` did not recover the exact algebraic reduction below. That negative search is **not** a novelty certificate; the reduction may be folklore or implicit in the classical Kalikow literature.
5. Recent 2026 RWRE search hits concerned space-time environments or other regimes and did not match Open Question 2.20. No source-matching 2025–2026 resolution was recovered in this bounded search. This is **bounded negative evidence only**, not proof of worldwide openness.

The classical implication `Kalikow condition => ballisticity` is prior art and is used as such. The only mathematical work claimed by this report is the explicit two-type occupation-bias calculation and its restricted-family consequence; publication novelty for that calculation is **UNVERIFIED**.

## 4. Frozen metric and counters

The frozen admission metric remains

`c_slab^(d)(kappa,w)` = the optimal universal quenched exponential exit-tail rate from subsets of a coordinate strip of width `w`, over all static nearest-neighbor environments with ellipticity constant at least `kappa`.

Run 2 proved exactly

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`.

This run does **not** rename the metric to a Kalikow constant, two-type threshold, Green-function ratio, or class count.

- **before:** `-log rho(K_{d,w}(kappa))` exactly;
- **after:** `-log rho(K_{d,w}(kappa))` exactly;
- **movement:** none;
- **consecutive unchanged invocations after the exact metric movement:** `4 -> 5`;
- **stuck recoveries used:** `1 -> 1`.

The theorem below is substantive PARTIAL progress on the source route, but it does not move the frozen strip metric.

---

# 5. B19 — MAKE IT AN ALGORITHM: reveal everything except the current site's type

The previous channel algorithm failed because it selected a cheap geometric path but did not control the probability mass that the walk actually assigns to it. The recovery report suggested using Kalikow's occupation-weighted auxiliary walk instead. For a two-type environment this can be done **exactly**, without approximating harmonic measure.

Let the nearest-neighbor direction set be

`U = {+/- e_1, ..., +/- e_d}`.

Fix a unit direction `ell`. Let the i.i.d. environment law have exactly two transition vectors:

- type `+`: `p^+(e)>0`, with probability `theta`;
- type `-`: `p^-(e)>0`, with probability `1-theta`;

where `theta in (0,1)` and both vectors obey the same uniform ellipticity lower bound. Write the projected local drifts

`d_+ = sum_e p^+(e) (e dot ell)`,

`d_- = sum_e p^-(e) (e dot ell)`,

and assume `d_+ > d_-`.

For a finite connected set `V` containing the starting point and a site `x in V`, let

`G_V^omega(0,x)`

be the quenched expected number of visits to `x` before exit from `V`. The Kalikow auxiliary transition kernel is the occupation-weighted average

`hat p_V(x,e) = E[G_V^omega(0,x) omega(x,e)] / E[G_V^omega(0,x)]`.

The key algorithmic choice is now:

> reveal the entire environment away from `x`, but leave the single type at `x` unrevealed.

This keeps the site type exactly independent of the revealed data and tracks the **actual occupation mass**, not a path surrogate.

Fix a realization `eta` of the environment away from `x`. For each neighbor direction `e`, define

`h_e = P_{x+e,eta}(H_x < T_{V^c})`,

with `h_e=0` if `x+e` is already outside the killed domain. Because the process is stopped when it returns to `x`, each `h_e` depends only on the environment away from `x`.

Let `a_eta` be the probability, starting from 0, of reaching `x` before exit (or `1` when the start is already `x`). This also does not depend on the transition vector at `x`. If the type at `x` is `sigma in {+,-}`, then after each visit to `x` the probability of another return before exit is

`sum_e p^sigma(e) h_e`.

Hence the number of visits is geometric and

`G_sigma = a_eta / D_sigma`,

where

`D_sigma = 1 - sum_e p^sigma(e) h_e
         = sum_e p^sigma(e) (1-h_e) > 0`.                 (5.1)

Conditioned on `eta`, the projection of the occupation-weighted auxiliary drift is therefore

`F_eta
 = [theta d_+ / D_+ + (1-theta)d_- / D_-]
   / [theta / D_+ + (1-theta)/D_-]`.

Multiplying numerator and denominator by `D_+ D_-` and writing

`r = D_+ / D_-`

gives the exact one-variable formula

`F(r) = [theta d_+ + (1-theta)d_- r]
        / [theta + (1-theta) r]`.                         (5.2)

This is the requested algorithmic bridge: all of the outside geometry enters through **one scalar occupation-bias ratio `r`**.

---

# 6. B23 — DO WHAT THE PROPOSER DID NOT EXPECT: quantify exactly how much the bad type can be occupation-biased

A possible counterexample mechanism would be that the walk visits negative-drift sites so much more often than positive-drift sites that the occupation-weighted Kalikow drift reverses sign even when the raw type density looks favorable.

In the two-type model, that amplification has a deterministic ceiling.

Define the coordinate likelihood-ratio extrema

`m = min_e p^+(e)/p^-(e)`,

`R = max_e p^+(e)/p^-(e)`.

Using (5.1),

`r = D_+/D_-
   = [sum_e p^-(e)(1-h_e) * (p^+(e)/p^-(e))]
     / [sum_e p^-(e)(1-h_e)]`.

Thus `r` is a convex combination of the finitely many ratios `p^+(e)/p^-(e)`, and therefore

`m <= r <= R`.                                                (6.1)

This bound is uniform over the finite domain, the site, and the entire revealed outside environment. The environment can bias occupation toward the bad type, but in this two-type setting the Green-function bias cannot exceed the local likelihood-ratio ceiling `R`.

Moreover,

`F'(r) = theta(1-theta)(d_- - d_+)
         / [theta + (1-theta)r]^2 < 0`.                       (6.2)

So the worst possible occupation bias is exactly the endpoint `r=R`. Define

`delta_two
 = [theta d_+ + (1-theta)d_- R]
   / [theta + (1-theta)R]`.                                  (6.3)

If `delta_two>0`, then (5.2), (6.1), and (6.2) give

`F_eta >= delta_two`

for **every** revealed outside environment `eta`, every finite connected `V`, and every `x in V`. Integrating over `eta` preserves the same inequality because both the conditional numerator and denominator are positive occupation weights. Hence the ordinary Kalikow auxiliary drift satisfies

`hat d_V(x) dot ell >= delta_two > 0`                         (6.4)

uniformly in `V,x`.

By the classical Sznitman–Zerner/Kalikow ballisticity theorem, (6.4) implies a ballistic law of large numbers in direction `ell`.

### Proposition `NM13-12-P0483-TWOTYPE-KALIKOW-07`

For a nearest-neighbor i.i.d. uniformly elliptic RWRE whose one-site law is supported on exactly two transition vectors `p^+,p^-` with probabilities `theta,1-theta`, order the labels so that `d_+>d_-`. Put

`R = max_e p^+(e)/p^-(e)`.

If

`theta d_+ + (1-theta)d_- R > 0`,                            (6.5)

then Kalikow's condition holds in direction `ell` with the explicit uniform drift lower bound (6.3), and therefore the RWRE is ballistic in direction `ell`.

In the sign-changing case `d_+>0>d_-`, condition (6.5) is exactly

`theta > R |d_-| / (d_+ + R |d_-|)`.                        (6.6)

The proof is (5.1)–(6.4) plus the standard Kalikow implication. No asymptotic simulation, finite-box extrapolation, or unproved multiscale step is used.

**Outcome of B23: success as a restricted-class theorem.** A would-be two-type obstruction cannot amplify the negative local drift by more than `R`; this converts the vague harmonic-measure blocker into one exact algebraic inequality on this class. It does **not** show that Kalikow's condition is necessary, and therefore it does not close P0483.

---

# 7. B26 — HUNT THE SPORADIC CASE: an exact d=2 sign-changing-drift family

To ensure the theorem is not merely the nonnestling case in disguise, take `d=2`, `ell=e_1`, and transition order

`(+e_1,-e_1,+e_2,-e_2)`.

Let

`p^+ = (2/5, 1/5, 1/5, 1/5)`,

`p^- = (1/5, 3/10, 1/4, 1/4)`.

Both are probability vectors and the common uniform ellipticity constant is at least

`kappa = 1/5`.

Their projected drifts have opposite signs:

`d_+ = 1/5`,

`d_- = -1/10`.

The coordinate likelihood ratios are

`(2, 2/3, 4/5, 4/5)`,

so

`R=2`.

For an arbitrary type probability `theta`, (6.3) becomes exactly

`delta_two(theta)
 = (2 theta - 1) / [5(2-theta)]`.                            (7.1)

Therefore the whole source-valid two-type family is certified ballistic by Kalikow whenever

`theta > 1/2`.                                                (7.2)

At the exact rational point

`theta = 3/5`,                                                (7.3)

we obtain

`delta_two = 1/35`.                                           (7.4)

The ordinary mean local drift is also positive there,

`theta d_+ + (1-theta)d_- = 2/25`,                           (7.5)

but the point of (7.4) is stronger: it controls the **occupation-biased auxiliary drift uniformly over every finite domain and site**.

For this fixed pair `p^+,p^-`, the raw mean drift turns positive already at `theta>1/3`, whereas the present robust Kalikow argument only certifies `theta>1/2`. The interval

`1/3 < theta <= 1/2`                                         (7.6)

is therefore left deliberately unresolved by this route. I do not infer directional transience there and I do not call its failure to satisfy (6.5) a counterexample. This explicit gap is useful: it identifies exactly where the one-site Green-function control stops and a genuinely stronger harmonic-measure argument would be required.

**Outcome of B26: success.** The route handles a genuinely sign-changing local-drift law in the source class, with an exact constant, while exposing a nontrivial parameter window that it cannot decide.

## 8. Exact finite self-check executed and archived

Because the displayed rational example is a finite exact claim, I executed an inspected `fractions.Fraction` checker locally and archived the script and output:

- `proofnet24/NM13-12/artifacts/2026-09-18/p0483_two_type_kalikow_exact.py`, creation commit `cf9d56760c13af14104c4e316d6d23d9bef222b6`;
- `proofnet24/NM13-12/artifacts/2026-09-18/p0483_two_type_kalikow_exact.out`, creation commit `21dfba45039e40ee83bf35e6be5d277f34e5cf7f`.

The exact checker verifies:

- both transition vectors sum to one;
- `kappa=1/5`;
- `d_+=1/5` and `d_-=-1/10`;
- coordinate ratios `(2,2/3,4/5,4/5)` and `R=2`;
- at `theta=3/5`, `delta_two=1/35` exactly;
- mean local drift `2/25` exactly;
- the symbolic family simplification `delta_two(theta)=(2 theta-1)/(5(2-theta))`, with positivity threshold `theta>1/2`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. This checker validates the finite arithmetic example; the parameter-uniform Green-function theorem is proved on the page above and is not delegated to computation.

## 9. What moved mathematically, what did not, and why the source remains OPEN

The recovery route produced a real source-class bridge that the preceding geometric-channel route lacked:

- occupation/harmonic weighting is handled exactly rather than replaced by a cheapest path;
- in a two-type law, all outside geometry collapses to one scalar `r=D_+/D_-`;
- `r` is trapped in a deterministic local likelihood-ratio interval;
- this gives an explicit sufficient Kalikow constant and a nontrivial sign-changing-drift family.

However, the full source implication

`directional transience => positive speed`

for arbitrary i.i.d. uniformly elliptic environments remains untouched in the decisive regime where no uniform Kalikow drift is available. The 2019 Fukushima–Ramírez examples also warn that ballisticity itself can occur without Kalikow, so a proof of P0483 cannot simply declare Kalikow necessary.

Accordingly:

- P0483 source status: **OPEN**;
- NM13-12 status: **PARTIAL**;
- frozen metric movement: **none**;
- P26 audit: **not requested / not passed**;
- NM13-13 secondary audit: **not requested / not passed**;
- closure: **false**;
- publication novelty: **UNVERIFIED**.

## 10. Stuck state and next mandatory action

The frozen metric has now remained unchanged for five consecutive invocations after its exact determination. This run was the substantive attempt authorized by stuck recovery 1 and did not spend the invocation manufacturing a new metric or checker-only receipt.

Under the literal owner rule, the **next NM13-12 invocation must be Section-I stuck recovery 2, thinking-only, with no new mathematical claim**. It must reassess whether the now-saturated strip metric is still an informative fixed quantity, while preserving it rather than silently renaming it. The second recovery must choose exactly one allowed recovery action. If a later third stuck episode occurs on P0483, the hard-source rule requires a preserved handoff and rotation.

Diagnostic Section-B lenses reserved for that next thinking-only recovery, and **not counted as attempted here**, are:

- `B7` TAKE THE LIMIT — examine whether the two-type occupation formula has a useful weak-disorder or high-dimensional limiting obstruction;
- `B14` FIND THE GROUP ACTING — inspect symmetries of finite-support environment laws to see whether the outside return vector `(h_e)` can be quotiented before attempting any multiscale argument;
- `B17` LOOK FOR YOUR NUMBERS SOMEWHERE ELSE — compare the likelihood-ratio ceiling `R` and the unresolved threshold window with sharp drift/variance criteria in the ballistic RWRE literature rather than guessing a new exponent.

No multiscale induction is authorized merely from Proposition 07. A future quantitative induction must display its one-scale hypothesis, conditioning structure, recursion, and summable error explicitly.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-12
  source_id: P0483
  claim_id: P0483
  historical_alias: C0041
  source_status: OPEN
  mathematical_status: PARTIAL
  theorem_claim: NM13-12-P0483-TWOTYPE-KALIKOW-07
  metric: "c_slab^(d)(kappa,w)"
  metric_before: "-log rho(K_{d,w}(kappa)) exactly"
  metric_after: "-log rho(K_{d,w}(kappa)) exactly"
  movement: none
  methods:
    - B19: "exact reveal-all-but-current-site algorithm; Green occupation collapses to D_sigma^{-1}"
    - B23: "proved occupation-bias ceiling r<=R and explicit two-type Kalikow sufficient inequality"
    - B26: "certified a d=2 sign-changing-drift two-type family; theta>1/2 sufficient, theta=3/5 gives delta=1/35"
  finite_certificate:
    script: proofnet24/NM13-12/artifacts/2026-09-18/p0483_two_type_kalikow_exact.py
    script_commit: cf9d56760c13af14104c4e316d6d23d9bef222b6
    output: proofnet24/NM13-12/artifacts/2026-09-18/p0483_two_type_kalikow_exact.out
    output_commit: 21dfba45039e40ee83bf35e6be5d277f34e5cf7f
    result: ALL_EXACT_CHECKS_PASS
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  stuck_recoveries_used_before: 1
  stuck_recoveries_used_after: 1
  next_run: SECTION_I_STUCK_RECOVERY_2_THINKING_ONLY
  next_diagnostic_methods_reserved_not_tried: [B7, B14, B17]
  p26_audit: not_requested_not_passed
  nm13_13_audit: not_requested_not_passed
  novelty: UNVERIFIED
```

No shared root, peer namespace, claim file, schedule, workflow, email, Drive item, public site, or permission setting was modified in this invocation.
