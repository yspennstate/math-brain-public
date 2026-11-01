Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — C29 frozen fallback metric `2 -> 2`; unchanged-run count `3 -> 4`; mandatory STUCK / THINKING run; no new C29 theorem claim. Section-B moves: 13, 25, 26.**

# C29 STUCK / THINKING REPORT — two-defect directional-convexity obstruction

## 1. Intake, source, ownership, and retirement gates

I started from the repository-wide state rather than restarting the Brownian or MUB attacks. I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the live claim files, the newest C29 report, the newest R07/I0077 report, the newest C30 report, and the C29 MUB reserve handoff. The root ledgers remain advisory where newer immutable reports carry stronger supported values.

### I0077 is still excluded by exclusive ownership

Burdzy–Scheutzow's definition is source-exact: an FBM is a process `X_t, t in R` for which there are random times `S_n -> -infinity` a.s. such that, from every `S_n`, the forward increment process is standard Brownian motion. Their Theorem 4.3 is specifically about the square-root/parabolic corridor `c_1 sqrt(|t|) <= X_t <= c_2 sqrt(|t|)` and the corresponding principal-eigenvalue threshold `lambda_0(c_1,c_2)`. Problem 7.8 asks:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

I checked the original paper, not merely the intake paraphrase. Problem 7.5 is separately listed immediately before it and remains already answered in the campaign `INDEX.md`; I did not reopen it.

The canonical file `operations/claims/I0077.md` still belongs to R07. R07's newest report is a STUCK RECOVERY 1 report and still retains the reservation while preserving its own supported source-family metric. Therefore C29 has no right to admit I0077, and I do not substitute C29's proposed Brownian metric for R07's established one. No I0077 claim file was edited or overwritten.

### Active C29 fallback remains RS-2026-DC34

The existing create-only fallback claim `operations/claims/RS-2026-DC34.md` remains owned by C29, status `CLAIMED / PENDING_ADMISSION / NOT READY`. The source target is Randomstrasse Directional Convexity Conjecture 34: find a finite set whose functional directional-convex hull for the three-plane geometry is not semialgebraic. All C29 results on particular finite configurations remain `PARTIAL`.

### MUB remains HARD RESERVE

The six-dimensional MUB attack is unchanged and untouched:

- unrestricted/full-domain normalized residual lower bound: `0`;
- `11/756` is an **upper** benchmark from an explicit configuration, not a positive lower bound and not a nonexistence proof;
- all exact phase examples, restricted auxiliary upper bounds, gauge/atlas reductions, and failed proof routes remain in `proofnet24/C29-mub-six`;
- no reserve claim is relabeled as a proof of `MUB(6)<7`.

## 2. Frozen metric and why this is a stuck run

C29's frozen fallback metric remains the already-fixed exact affine-patch count attached to the four-point candidate. Its value is

\[
\boxed{2\to2}.
\]

The preceding three ordinary runs did not move it; the newest one-defect theorem explicitly triggered Section I. Therefore this run is intentionally claim-free on the C29 research target. It is not a checker run disguised as progress. The raw unchanged-run count is now `4`.

Because C29 is a CLOSABLE target, the six-unchanged-run rotation rule still applies. We are not at six yet.

## 3. Exact blocking statement

Keep the five-point spike family from the preceding reports:

\[
K_5=K_4\cup\{(a,b,ab+\delta)\},
\]

with the tent functions

\[
T_a(s)=
\begin{cases}
s/a,&s\le a,\\
(1-s)/(1-a),&s\ge a,
\end{cases}
\qquad
T_b(t)=
\begin{cases}
t/b,&t\le b,\\
(1-t)/(1-b),&t\ge b,
\end{cases}
\]

and the least separately concave majorant

\[
U_\delta(s,t)=st+\delta T_a(s)T_b(t).
\]

Let `d=(1,-alpha)` be the fixed third planar direction and let `C_d` denote line-by-line least concave majorization along lines parallel to `d`. The preceding exact calculation gives the two mixed-cell activation thresholds

\[
\tau_{SE}=(1-a)b,
\qquad
\tau_{NW}=a(1-b).
\]

The current blocker is therefore the following concrete statement, not the vague phrase "understand the supercritical hull":

\[
\boxed{
\delta>\max\{\tau_{SE},\tau_{NW}\}
\quad\Longrightarrow\quad
\text{is } \mathcal C_d U_\delta
\text{ still concave separately in }s\text{ and }t?
}
\tag{BLOCK}
\]

Equivalently: after both mixed cells become third-direction convex, does one exact third-direction chord sweep already stabilize the full directional-concave envelope, or does that sweep create a new coordinate-direction defect which forces a genuine alternating return map?

A YES answer for this five-point family would make this route another finite semialgebraic closure. A NO answer, with an exact coordinate defect and repeatable return map, would finally expose the mechanism needed for a non-semialgebraic candidate. Neither answer is proved here.

## 4. Complete failure inventory and what each route lacks

### Four-point exact hull

The four-point lifted irrational-parallelogram candidate closed exactly between its lower and upper envelopes. It produced the frozen metric value `2` but no wild boundary. Failure mode: too few interacting defect cells; exact finite lamination closes immediately.

### Five-point subcritical spike

Below both thresholds the separately concave envelope `U_delta` is already concave in the third direction. Failure mode: the new direction never activates.

### Exposed-face localization

The supercritical centered calculation found four global affine upper supports and reduced their exposed faces to planar directional hulls. Failure mode: this localizes any possible non-semialgebraicity to the residual, non-globally-exposed boundary; it does not control that residual.

### High-spike limiting skeleton

The normalized support planes have a clean limiting four-facet skeleton. Failure mode: support-plane convergence does not imply convergence of the entire functional hull; directional-convex hulls are nonrobust enough that this cannot be promoted without a separate argument.

### Asymmetric one-defect band

For
\[
(1-a)b<\delta<a(1-b)
\]
when `a>b`, only the southeast cell is defective. The preceding report proved that one exact third-direction chord sweep yields a globally directional-concave, semialgebraic, finitely laminated hull. Failure mode: one active defect is provably insufficient to generate an infinite alternation.

### Infinite compatible-grid heuristic from the literature

Meroni–Raiţă's discussion explains that an infinite compatible grid by itself is insufficient because candidate boundary planes may coincide; their perturbative question is exactly about escaping that degeneracy. Failure mode: combinatorial infinitude is not geometric infinitude of distinct exposed/support pieces.

### Planar `D`-hull algorithms

Franěk–Matoušek give a polynomial-time algorithm for finite planar functional `D`-hulls for arbitrary finite direction sets. Failure mode: the exposed planar faces are not where the unresolved three-dimensional alternating envelope lives.

## 5. What a successful proof must contain

Every route above is missing the same object: an **exact two-defect transition calculation**.

A useful proof must do one of two things.

1. **Finite-closure route:** write `C_d U_delta` explicitly on every line/cell, prove every horizontal and vertical derivative jump is downward, and exhibit a finite lamination construction. This would rule out the whole five-point two-defect family as a source of Conjecture 34.

2. **Cascade route:** identify one explicit horizontal or vertical derivative jump of the wrong sign after the `d`-sweep, compute the next coordinate concavification exactly, and show that some quantitative defect parameter returns with a nontrivial update map. Only then would an infinite alternation become a serious mechanism rather than a picture.

What does **not** suffice is another list of supporting planes, a finite numerical iteration, or a simulation suggesting many pieces.

## 6. Simplest special case still unproved

The cleanest diagnostic is the centered spike

\[
\boxed{
a=b=\frac12,\qquad \delta>\frac14,
}
\]

with the same fixed `alpha>0` from the source geometry.

Writing `c=4 delta` and `q=c-1>0`, the four cell formulas become

\[
U=
\begin{cases}
(1+c)st,&SW,\\
t(c-qs),&SE,\\
s(c-qt),&NW,\\
st+c(1-s)(1-t),&NE.
\end{cases}
\]

Along a third-direction line `t=r-alpha s`, the `SW` and `NE` pieces are concave quadratics while the `SE` and `NW` pieces are convex quadratics, each with constant second derivative `+2 alpha q`. Thus the two endpoint defects are completely explicit. The affine involution

\[
F(s,t,z)=(1-s,1-t,z+1-s-t)
\]

exchanges `NW` and `SE` and preserves the centered spike data (up to the built-in affine height correction).

This symmetry makes the centered case a better *diagnostic* than the preceding report's generic asymmetric case: the two defect corrections are mirror images. However, a line through the center can meet `NW` and `SE` back-to-back, so it is **not** legitimate to assume that the two one-defect chord corrections simply superpose. One must check whether the linewise least concave majorant uses two terminal chords or a longer chord spanning the middle, and then check coordinate concavity. That is the exact remaining calculation.

No theorem is claimed from these formulas in this stuck run.

## 7. Section-B moves tried

### B13 — find what only increases

Candidate monovariant: the number, or total strength, of positive third-direction curvature cells under alternating concavification.

At the start of the two-defect regime, `U_delta` has exactly two mixed cells with the wrong third-direction curvature. A `d`-sweep removes that curvature on each line. The route fails at the next sentence: coordinate concavification can in principle create new `d`-defects, so neither cell count nor integrated positive curvature is yet proved monotone. This is useful because it states exactly what a monovariant theorem would have to control.

### B25 — count the same thing twice

There are two descriptions of the desired first sweep:

- analytic: the linewise least concave majorant `C_d U_delta`;
- constructive: the supremum of values obtained by one permitted third-direction chord lamination between two graph-`U_delta` points on the same line.

For the one-defect band these descriptions coincide and were the key to both minimality and reverse inclusion. In the two-defect regime the same double description still reduces the problem to endpoint selection on each line. The obstruction is not the chord construction itself; it is proving that the resulting global graph is concave in the two coordinate directions.

### B26 — hunt the sporadic case

Instead of immediately perturbing away from symmetry, I treated the centered case as the sporadic diagnostic. The `F` involution exactly pairs the two defects. This may collapse the endpoint-selection algebra enough to decide `(BLOCK)` in closed form. The caveat above is essential: on the central third-direction line the two defect regions touch, so "mirror symmetry" is not by itself a proof of independent corrections.

Outcome: no claim, but the next calculation is now a finite symbolic case split rather than an open-ended search.

## 8. Nearest solved problems and the missing ingredient

The closest solved internal result is C29's own one-defect theorem: one convex mixed cell, one linewise chord sweep, then exact coordinate derivative-jump verification and finite lamination.

The closest literature results found in the bounded search are:

- Meroni–Raiţă: semialgebraicity for the triangular rank-one setting, including explicit finite configurations, while identifying general directional convexity as the setting where this behavior may fail;
- Franěk–Matoušek: polynomial-time planar finite `D`-hulls for arbitrary finite `D`.

Those arguments have either a triangular algebraic structure or a genuinely planar finite-direction setting. The current C29 blocker has neither: it is a lifted three-dimensional functional hull in which a correction in one direction can create a defect in another. The missing ingredient is therefore an exact **cross-direction return calculation**, not another planar hull algorithm.

Fresh bounded literature queries run on 2026-09-16:

- `"Directional Convexity" Meroni Raita arXiv 2509.07541 2026`
- `"functional D-convex hull" non-semialgebraic directional convexity 2026`
- `"Conjecture 34" "Directional Convexity" Meroni`
- `"Computing D-convex hulls in the plane" Franek Matousek`

The search returned the current Meroni–Raiţă preprint and the established Franěk–Matoušek planar work, but no later source-exact resolution of Randomstrasse Conjecture 34. This is a dated bounded search, **not** proof that the conjecture is globally open and not a novelty certificate.

## 9. Exactly one recovery action selected

I choose the allowed Section-I action:

> **prove the simplest unproved special case from Section 6.**

The next ordinary C29 research run should attack only the centered two-defect spike `a=b=1/2, delta>1/4`:

1. parameterize every third-direction line by `r=t+alpha s`;
2. determine the exact endpoints of its `NW` and `SE` convex segments;
3. compute the linewise least concave majorant, including the central-line transition where the two defects touch;
4. only then derive horizontal and vertical derivative jumps of the resulting candidate;
5. write a checker only if those formulas produce an actual finite claim worth checking.

If that calculation proves finite closure, the entire centered five-point family is excluded and the next route should move to an asymmetric two-defect return map. If it produces a coordinate defect, the next quantity to follow is its exact return map. I do not choose a second recovery action.

## 10. C30 second-audit duty

The newest substantive C30 claim is now

`C30-N11-M27-STRUCTURAL-02 = PROVED`

from `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T20-52-21Z__n11-m27-structural.md`.

I independently rederived and exactly checked the finite arithmetic core. The result is

\[
\boxed{\texttt{C29-AUDIT-C30-N11-M27-STRUCTURAL-03 = PASS (claim-scoped)}}.
\]

The independent checker enumerates all 30 nonconstant binary cyclic words and obtains

\[
5d_a^2c^3+5d_ac^4+10c^5+5d_bc^4+5d_b^2c^3.
\]

For the low-degree deletion branch it verifies exactly

\[
\left(\frac89\right)^{15}
\ge
\left(\frac{10}{11}\right)^{20}.
\]

For the minimum-degree-at-least-four branch, exact dynamic programming over degree sequences with 11 degrees in `[4,10]` summing to 54 gives

\[
\sum_v d_v^5\ge32274,
\qquad
\sum_v {d_v\choose2}\ge106.
\]

The pair lower envelope

\[
F(c)=10c^5+10q c^4+10q^2c^3,\qquad q=\max\{4,c\},
\]

is discretely convex on `c=0,...,10`. An independent 55-pair dynamic program with total codegree at least 106 gives the exact floor

\[
\sum_{\{a,b\}}F(c(a,b))\ge115080.
\]

Hence

\[
\operatorname{hom}(H,G)\ge32274+115080=147354,
\]

while the source-normalized integer threshold is

\[
\left\lceil\frac{54^{15}}{11^{20}}\right\rceil=143898,
\]

with exact margin

\[
147354\cdot11^{20}-54^{15}
=
2325483985034728958670330>0.
\]

The checker output ends `ALL_EXACT_CHECKS_PASS`.

Artifacts:

- `proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T21-37-27Z__audit_c30_n11_m27.py`
- `proofnet24/C29-closure-brownian-shapes/artifacts/2026-09-16T21-37-27Z__audit_c30_n11_m27.out`

Audit scope is deliberately narrow. This PASS certifies C30's `n=11,m=27` structural theorem only. It does **not** certify complete order-eleven coverage, `m>=28`, any host order `n>=12`, or universal Sidorenko for the fixed source graph; C30's frozen coverage metric therefore remains 10.

## 11. Scheduler/model-control status

The task-control interface exposed in this run still provides task text/title, timing/schedule controls, enabled state, and notification behavior, but it exposes **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains a prompt request only in this environment.

To make it enforceable, the scheduler/backend or an authorized enclosing runtime must expose persistent fields that pin the model family and reasoning effort and pass them to execution. C29 cannot synthesize those controls from prompt text.

The historical P26 `"You cannot modify this task"` event is consistent with an ownership/permission-context boundary; later authorized P26 edits have succeeded. The supported workaround is modification from the owning authorized workspace by an owner/admin/coordinator, or platform support if the ownership context itself is defective. It is not legitimate to bypass the permission boundary or create a duplicate schedule.

## 12. Ledger delta for P26

```yaml
ledger_delta:
  track: C29
  proposed_target: I0077
  proposed_target_disposition: EXCLUDED_BY_LIVE_R07_OWNERSHIP
  active_fallback: RS-2026-DC34
  fallback_status: PARTIAL / CLAIMED / PENDING_ADMISSION / NOT_READY
  frozen_metric_before: 2
  frozen_metric_after: 2
  movement: no
  unchanged_run_count_before: 3
  unchanged_run_count_after: 4
  run_kind: STUCK_THINKING
  new_C29_theorem_claim: none
  section_B_moves: [13, 25, 26]
  selected_recovery_action: prove_simplest_unproved_special_case
  selected_special_case: centered_two_defect_spike_a=b=1/2_delta>1/4
  new_audit: C29-AUDIT-C30-N11-M27-STRUCTURAL-03 = PASS (claim-scoped)
  C30_scope_exclusions: [complete_n11, m>=28, n>=12, universal_Sidorenko]
  MUB_reserve_global_lower_bound: 0
  MUB_11_over_756_role: upper_benchmark_only
  rotation_required_now: false
  rotation_trigger_if_no_movement: 6_unchanged_runs
```

No shared ledger, peer claim, peer report, schedule, email, Drive object, public post, access control, or retired target was edited in this run.
