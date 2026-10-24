Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not verified GPT-6 at maximum, and I do not claim otherwise. NO METRIC MOVEMENT: `d_bad = +infinity -> +infinity`; NEW-METHODS genuinely attempted: #14 FIND THE GROUP ACTING, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME.**

# NM13-05 — P0411 exact Maclaurin radius and infinitely many coefficient sign changes

Run date: 2026-09-19.
Repository / branch: `yspennstate/math-open-problems` / `master`.
Namespace: `proofnet24/NM13-05/`.
Category: CLOSABLE OUTSIDE.
Canonical source/claim ID: `P0411`.
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`.
SHA-256: `55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc`.
Shard: `4 mod 13`.

## 1. Continuity, ownership, and pre-write state

I continued from the newest immutable NM13-05 report

`proofnet24/NM13-05/runs/2026-09-19/2026-09-19T08-33-30Z__p0411-all-even-positive-coefficients-refuted-pringsheim.md`

at creation commit

`6619c06d90c3b89bb27df5091386ab31370e1734`.

Before doing mathematics I re-read the controlling fleet rules and new-methods owner directives, the NM13 deployment amendment, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, the canonical P0411 claim, the source/attempt records, the newest NM13-06 report, and the newest P26 report. The canonical claim still assigns P0411 exclusively to `proofnet24/NM13-05`; I found no release, reassignment, retirement, POSTED closure, or conflicting alias claim.

The frozen pre-write `master` snapshot used for the final continuity check was

`3e2fc912063eedb8f1affbe8a73aedf7e6695e21`.

Compared with the preceding NM13-05 creation commit, that snapshot was `117` commits ahead and `0` behind, with `too_large = null`. The complete changed-file list contained no edit to `operations/claims/P0411.md`, no P0411 audit from P26 or NM13-06, and no controlling QUEUE/POSTED/RESULTS/campaign-index mutation releasing or closing P0411. The latest P26 run instead audited an unrelated Romero split-reliability package. The latest NM13-06 run remained in its own successor/admission state rather than auditing P0411.

No inaccessible P0411 history was silently filled in. The bounded GitHub searches used current default-branch indexing plus direct canonical-file reads; absence from search was not treated as proof of absence when a canonical path was known.

## 2. Frozen target and metric

The marginal family is unchanged:

\[
R_d=d_{\mathbb H}(o,\partial C_d),\qquad d\ge2,
\]

where `C_d` is the IPVT zero cell, with survival function

\[
H_d(u)=\Pr(R_d\ge u)
\]

and density `g_d=-H_d'`.

The metric is unchanged:

\[
d_{\rm bad}=\min\{d\ge2:g_d\text{ is not nonincreasing on }[0,\infty)\},
\]

with `d_bad=+infinity` if no such dimension exists.

Certified before this run: `d_bad=+infinity`.
Certified after this run: `d_bad=+infinity`.

Thus there is **no metric movement**. Supported unchanged-run counter: `2 -> 3`. Recovery counter: `0 -> 0`.

Because this is now the third consecutive run with the frozen metric unchanged, Section I is triggered **for the next NM13-05 invocation**. The next invocation must be a thinking/stuck run with no new theorem claim before it diagnoses the exact blocker and chooses one permitted recovery action.

## 3. Three genuinely new Section-B routes

### #14 FIND THE GROUP ACTING

The previous run found the branch obstruction at `q=-1` after the substitution `q=e^{2u}`. This run used the covering/deck geometry of the exponential map instead of computing another coefficient. The transformations `u -> u + i*pi*k` organize the preimages of the negative real `q`-axis, and the nearest preimages of `q=-1` to the origin are exactly `u=+/- i*pi/2`. This turns the qualitative statement "finite radius" into an exact radius computation.

Outcome: **success** — exact Maclaurin radius `pi/2` for every even dimension.

### #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The number `pi/2` is not a random numerical artifact: it is the covering-distance from `u=0` to the nearest branch endpoint of the `q`-plane integral. I then used the classical Pringsheim theorem from positive-coefficient generating-function theory on *tails* of the Maclaurin series rather than only on the whole series.

Outcome: **success** — the source's positive-coefficient failure is not sporadic: every even-dimensional series has infinitely many negative coefficients; in fact it also has infinitely many positive coefficients.

### #30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME

I separated three directions that the previous finite-radius argument had conflated: (i) holomorphy throughout the open disk of radius `pi/2`, (ii) genuine singularity at the imaginary endpoints `+/- i*pi/2`, and (iii) regularity at the positive real point `+pi/2`. Resolving those one at a time makes the tail-Pringsheim contradiction exact and avoids any coefficient asymptotics or numerical extrapolation.

Outcome: **success** — exact nearest-singularity geometry plus an infinite sign-change obstruction, with no checker needed.

## 4. New theorem

For every **even** `d>=2`, define

\[
F_d(u):=\frac{e^{-(d-1)u}}{H_d(u)}.
\]

### Theorem

For every even `d>=2`:

1. the Maclaurin series of `F_d` at `u=0` has radius of convergence exactly
   \[
   R_d^{\rm Mac}=\frac{\pi}{2};
   \]
2. its real Maclaurin coefficients contain **infinitely many negative terms** and **infinitely many positive terms**.

In particular, the source's displayed-variable conjecture that the denominator factor is an infinite power series with positive coefficients is false in every even dimension, and it does not become coefficientwise nonnegative after finitely many exceptional terms.

## 5. Proof

Write

\[
n=d-1,\qquad \alpha=\frac{n-2}{2}.
\]

For even `d`, `n` is odd and `alpha` is a half-integer. The exact radial reduction already established in the P0411 chain gives

\[
F_d(u)=G_n(e^{2u}),
\]

where, up to the fixed positive normalizing constant `K_n`,

\[
G_n(q)=K_n\int_1^\infty
(z-1)^\alpha z^{-2n}(q+z)^\alpha(q+2z-1)\,dz. \tag{1}
\]

Use the principal branch for `(q+z)^alpha`.

### 5.1 Holomorphy in the slit `q`-plane

Let

\[
\Omega=\mathbb C\setminus(-\infty,-1].
\]

For each fixed `z>=1`, the only branch cut in the `q` variable is `(-infinity,-z]`; the union over `z>=1` is exactly `(-infinity,-1]`. Hence the integrand in (1) is holomorphic in `q` on `Omega`.

The integral is locally uniformly dominated there. Near `z=1`, `(z-1)^alpha` is integrable even in the endpoint case `d=2`, where `alpha=-1/2`. As `z->infinity`, uniformly for `q` in a compact subset of `Omega`, the integrand is

\[
O(z^{2\alpha+1-2n})=O(z^{-n-1}),
\]

which is integrable for `n>=1`. Standard parameter-dependent holomorphic integration therefore shows

\[
G_n\text{ is holomorphic on }\Omega. \tag{2}
\]

### 5.2 Lower bound on the Maclaurin radius

If `|u|<pi/2`, then in particular `|Im u|<pi/2`, so `2 Im u` lies strictly between `-pi` and `pi`. Consequently `e^{2u}` cannot lie on the negative real ray `(-infinity,-1]`. Thus

\[
|u|<\frac\pi2 \implies e^{2u}\in\Omega.
\]

By (2), `F_d(u)=G_n(e^{2u})` is holomorphic throughout the open disk

\[
|u|<\frac\pi2. \tag{3}
\]

Hence the Maclaurin radius is at least `pi/2`.

### 5.3 Upper bound: the two nearest points are genuine singularities

The preceding immutable NM13-05 report proved the following exact local fact, by differentiating (1) `n+1=d` times and isolating the endpoint `z=1` contribution:

\[
G_n^{(n+1)}(-1+\varepsilon)
=
2nK_n(\alpha)_{\underline n}\log(1/\varepsilon)+O(1),
\qquad \varepsilon\downarrow0, \tag{4}
\]

with `(alpha)_{underline n} != 0`. Thus `q=-1` is a genuine, nonremovable logarithmic branch singularity of `G_n`; this is not merely a branch-choice artifact.

Now

\[
e^{2(i\pi/2)}=e^{2(-i\pi/2)}=-1.
\]

The exponential map has nonzero derivative at both points, so composing a genuine singularity at `q=-1` with `q=e^{2u}` gives genuine singularities of `F_d` at

\[
u=\pm i\pi/2. \tag{5}
\]

Therefore the Maclaurin radius is at most `pi/2`. Combining (3) and (5),

\[
\boxed{R_d^{\rm Mac}=\pi/2}. \tag{6}
\]

### 5.4 Infinitely many negative coefficients

Write the real Maclaurin expansion

\[
F_d(u)=\sum_{k\ge0}a_k u^k,
\]

whose radius is `R=pi/2` by (6).

Suppose, for contradiction, that only finitely many coefficients are negative. Choose `N` past the last negative coefficient and set

\[
T(u)=\sum_{k\ge N}a_k u^k=F_d(u)-P_{N-1}(u),
\]

where `P_{N-1}` is a polynomial. Then all coefficients of `T` are nonnegative. Subtracting a polynomial cannot remove either branch singularity in (5), so `T` still has finite radius `R=pi/2`.

Pringsheim's theorem says that a real power series with nonnegative coefficients and finite radius `R` has a singularity at the **positive real** point `u=R`.

But `u=pi/2` is harmless here: `e^{2u}=e^pi>0`, so it lies in `Omega`, and (2) gives a full complex neighborhood on which `F_d` is holomorphic. The polynomial `P_{N-1}` is entire, hence `T=F_d-P_{N-1}` is also holomorphic near `u=pi/2`. Contradiction.

Therefore `a_k<0` for infinitely many `k`.

### 5.5 Infinitely many positive coefficients

If only finitely many coefficients were positive, choose `N` beyond the last positive coefficient. Then the tail `T` has `a_k<=0`, so `-T` has nonnegative coefficients, the same finite radius `pi/2`, and is holomorphic near positive real `pi/2`. Pringsheim again gives a contradiction.

Therefore `a_k>0` for infinitely many `k` as well.

This completes the proof.

## 6. Relation to earlier P0411 work

This theorem does **not** re-count the archived campaign calculation as new progress. The older attempt `P0411-A001` already established in `d=2` the exact negative sixth coefficient

\[
[u^6]F_2(u)=\frac{61}{240}-\frac4{5\pi}<0.
\]

The previous NM13-05 run then proved that every even dimension has at least one negative coefficient by the branch singularity plus Pringsheim. The new result here is stronger in two precise ways:

- the Maclaurin radius is now certified exactly as `pi/2` in every even dimension;
- the coefficients have both signs infinitely often, so positivity does not recover after any finite prefix.

No numerical coefficient scan, CAS extrapolation, or new certificate artifact was needed.

## 7. Source and bounded literature check — 2026-09-19

Primary source checked:

- M. D'Achille, N. Curien, N. Enriquez, R. Lyons, M. Unel, *Ideal Poisson-Voronoi tessellations on hyperbolic spaces*, Annals of Probability 54(2), 846-891 (2026), DOI `10.1214/25-AOP1781`, arXiv `2303.16831`. Current bibliographic records give publication date 2026-03-06.

Fresh dated search strings in this run included:

- `"Ideal Poisson-Voronoi tessellations on hyperbolic spaces" Conjecture 7.5 positive coefficients`
- `"Ideal Poisson-Voronoi tessellations" boundary distance positive coefficients follow-up 2026`
- `D'Achille Curien Enriquez Lyons Unel 2026 ideal Poisson Voronoi follow-up boundary distance`
- `"Ideal Poisson-Voronoi" D'Achille Khezeli convergence 2026`

Relevant later material recovered:

- D'Achille--Thale, *Face volume densities of positive-intensity and ideal Poisson--Voronoi tessellations in hyperbolic spaces*, arXiv `2606.26049`, submitted 2026-06-24; it concerns face-volume densities/typical face volumes, not the boundary-distance coefficient clause here.
- D'Achille--Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv `2606.30517`, submitted 2026-06-29; it concerns convergence/uniqueness and graph variants, not this coefficient clause.
- Mellick, *Indistinguishability of cells for the ideal Poisson Voronoi tessellation*, Proc. AMS 2026 / arXiv `2408.10009`; it resolves a different question from the source.

The bounded search did **not** recover a later source resolving the specific Conjecture 7.5 positive-coefficient statement or the exact `pi/2` radius/infinite-sign-change conclusion. This is only bounded negative evidence. It is not a worldwide openness, novelty, or priority certificate. The Pringsheim theorem used above is classical prior art and is explicitly not claimed as new.

## 8. Honest source status and closure status

The source-level situation remains split:

- decreasing density of the boundary distance: **PROVED candidate** by the first NM13-05 P0411 run, with frozen metric `d_bad=+infinity`;
- strict IFR / sharp tail information: **PROVED candidate** by the second NM13-05 P0411 run;
- even-dimensional positive-coefficient clause in the source's displayed variable `u`: **REFUTED candidate**, now strengthened to infinitely many positive and negative coefficients for every even dimension;
- median `<` mean: follows from the decreasing-density result and remains **PROVED candidate**.

The literal positive-coefficient clause is false under the displayed-variable reading. I preserve the already-recorded interpretation risk: a source-author clarification could in principle reveal that a transformed variable was intended, but no such correction was recovered in the source/current-literature check.

**Fleet closure is still false.** There is no recovered P0411 PASS from P26 and no recovered P0411 PASS from NM13-06. Audit count remains `0/2`. The analytic theorem here has no essential finite core, so Section G does not require manufacturing a finite checker merely to create paperwork; the proof is written on this page.

## 9. STUCK trigger and next-run obligation

The frozen metric has now been unchanged in three consecutive runs:

- after admission: `d_bad=+infinity`;
- IFR/tail run: unchanged count `0 -> 1`;
- all-even Pringsheim run: unchanged count `1 -> 2`;
- this run: unchanged count `2 -> 3`.

Therefore NM13-05 is now **STUCK_TRIGGERED** under Section I even though the source mathematics has materially strengthened around the fixed metric.

The next invocation must be a thinking/stuck run with **no new claim** before satisfying the required diagnostic. The most natural recovery choice to pressure-test there is `refute instead of prove`: attack the surviving interpretation loophole directly by asking whether any source-consistent transformed-variable reading can evade the exact branch/radius obstruction. That choice is not executed in this run; it is recorded as the next-step candidate so the required stuck report can make the mandated one-choice decision explicitly.

This is only the third unchanged run, so the separate six-unchanged-run CLOSABLE rotation rule has **not** yet fired.

## 10. Scheduler/model-control observation

The model request in the task prompt is still not enforceable through the exposed scheduled-task controls. The current task-control interface exposes task title/prompt, schedule or offset, timing mode, enabled state, list, and update operations. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated applied-runtime attestation field**. Therefore `GPT-6 / maximum` remains prompt text only in this environment, and this report truthfully records GPT-5.6 Sol with reasoning level UNVERIFIED.

Making the request enforceable would require an authorized product/workspace/API/admin control surface that persists model-family and reasoning-effort fields and returns applied-runtime metadata per invocation.

The historical P26 scheduler response `You cannot modify this task` is an authorization-context boundary, not evidence that ownership has been released. I did not attempt to modify that task because this run's operational safeguards forbid schedule modification. The compliant workaround is to use the owning/otherwise-authorized account/workspace/API/admin context, or authorized platform support for that same task — not to duplicate it or bypass permissions.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  source_id: P0411
  claim_id: P0411
  canonical_dedup_key: boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells
  shard_mod13: 4
  category: CLOSABLE_OUTSIDE
  source_status: REFUTED_CANDIDATE_DISPLAYED_U_COEFFICIENT_CLAUSE
  fleet_closed: false
  metric_name: d_bad
  metric_before: +infinity
  metric_after: +infinity
  metric_movement: none
  unchanged_runs_before: 2
  unchanged_runs_after: 3
  recovery_count_before: 0
  recovery_count_after: 0
  stuck_triggered: true
  methods:
    - number: 14
      name: FIND_THE_GROUP_ACTING
      outcome: exact_preimage_geometry_and_nearest_branch_points
    - number: 17
      name: LOOK_FOR_YOUR_NUMBERS_SOMEWHERE_ELSE
      outcome: tail_Pringsheim_gives_infinitely_many_coefficients_of_each_sign
    - number: 30
      name: DO_ONE_PRIME_ONE_SCALE_ONE_DIRECTION_AT_A_TIME
      outcome: exact_radius_pi_over_2_by_separating_imaginary_singularities_from_positive_real_regularity
  new_claims:
    - for_every_even_d_Maclaurin_radius_of_exp_minus_nu_over_H_is_exactly_pi_over_2
    - for_every_even_d_Maclaurin_coefficients_have_infinitely_many_negative_and_infinitely_many_positive_terms
  finite_core: none_essential
  new_artifacts: none
  audit_p26: not_recovered
  audit_nm13_06: not_recovered
  audits_complete: 0_of_2
  next_step: mandated_SECTION_I_thinking_run_no_new_claim_before_diagnostic
  prewrite_head: 3e2fc912063eedb8f1affbe8a73aedf7e6695e21
  predecessor_report_commit: 6619c06d90c3b89bb27df5091386ab31370e1734
  predecessor_to_prewrite_ahead: 117
  predecessor_to_prewrite_behind: 0
```

## 12. Mutation boundary

This invocation writes exactly this one immutable report in `proofnet24/NM13-05/runs/`. It does not edit `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign roots, the canonical claim, any attempt ledger, any peer namespace, any D-series file, any workflow, permission, public surface, email/Drive resource, paid-compute resource, or schedule.
