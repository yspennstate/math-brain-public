Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E>=b13 -> gamma_E>=b14>b13`**. Numbered-method inventory is now exhausted except for **B16**, so this run used **B16 (first use on P0151) + B5/B18 (nonconsecutive recycled moves)** in a new failure-only cap-perturbation route; the triple `B16/B5/B18` itself has not been used before.

# HARD7-04 bounded research iteration — failure-only one-unit cap layer

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new all-parameter lower-bound advance for the exact sequential fixed-outdegree preferential-attachment model. It does not determine the full critical window, prove a matching upper bound, establish the finite-graph `sqrt(n)/log n` law, or identify a scaling-limit law.

The theorem-sized analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_one_unit_cap_layer_20260920T1330Z.md`

created at commit

`1255fbea178198b66a596a7de244b8f8734d8050`

and read back successfully at that exact SHA before this report was written.

The exact finite specialization checker/output are

- `artifacts/hard7_2026-09-18/HARD7-04/p0151_cap_layer_exact_20260920T1330Z.py` @ `ff80559d2d7c67d8ae865d45f058a9ae7dd92293`;
- `artifacts/hard7_2026-09-18/HARD7-04/p0151_cap_layer_exact_20260920T1330Z.out` @ `749cf78b27487501f98f0e79bfa2083137f33184`.

Both were read back successfully at their exact SHAs; the output ends `ALL_EXACT_CHECKS_PASS`.

---

## 1. Continuity, ownership, exclusions, and repository state consumed

I resumed the exclusive canonical claim `operations/claims/P0151.md`, still owned by `HARD7-04`. I did not restart I0049, any solved degree-count target, Kemeny/extremal-hitting-time work, P0157, or the independently attached-edge growing-graph model.

Before new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active intake/catalog trace for `P0151|3|critical window, fixed-outdegree PA`;
- `operations/claims/P0151.md`;
- the immediately preceding own report `2026-09-20T1232Z__p0151_killed_ppt_boundary_green.md`;
- the preceding strict-movement report `2026-09-20T1130Z__p0151_degree_distribution_slack.md` and its proof/check artifacts;
- the earlier killed-PPT spectral artifact `p0151_log_age_killed_ppt_spectral_window_20260920T0330Z.md`;
- neighboring P0157 work: R14 consumed both stuck recoveries and recorded a terminal handoff, so there is no active claim collision with P0151;
- current repository search for P0151 ownership/aliases and the P0151 intake trace.

The posting registry contains no source-equivalent P0151 paper. No root shared ledger, peer-track file, schedule, email, or Drive object was edited.

---

## 2. Exact source target and fresh literature check — 20 September 2026

The frozen model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold remains

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The retained source target is the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this exact sequential fixed-outdegree model.

A fresh bounded literature check dated 20 September 2026 rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085: exact threshold and giant/no-giant transition for the fixed-outdegree model, not a finite-size critical-window theorem.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025: `(log n)^(-2)` window and `sqrt(n)/log n` largest-component scale for a class where new vertices connect independently to earlier vertices. That independent-connection hypothesis does not automatically contain the exact fixed-`m` sequential model here.
3. Mörters--Schätze, arXiv:2606.27844, submitted 26 June 2026: a different inhomogeneous preferential-attachment-kernel ensemble in the infinite-variance regime.
4. The TU/e/Network Center project page still describes the critical-window question for the preferential-attachment model as an intended research direction.

No source-matching finite fixed-outdegree critical-window resolution surfaced in the bounded refresh. This is bounded negative evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric — exact before/after

Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`,
`eta:=m(m-1)pi^2`.

The frozen source-relevant quantity remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`.

The preceding strict-movement run proved `gamma_E>=b13`; the immediately preceding killed-PPT run produced no finite-graph movement.

The inherited bridge cap is

`c_0(w)=min(w,2A)`.

Define the one-unit layer

`d(w)=min(w,2A+1)-min(w,2A)=min(1,(w-2A)_+)`.

For the affine-PA degree proportions

`p_m=A/[A+m(m+delta)]`,
`p_k=m(k-1+delta)p_{k-1}/[A+m(k+delta)]`,

put

`K=floor(4m+delta)+1`,
`theta=K-(4m+delta) in (0,1]`,
`w_K=K+delta`,

and

`D_cap:=w_K p_K[theta+m(w_K+1)/a]>0`.

Let `M12:=1/2-U12>0`, where `U12` is the inherited upper coefficient, and set

`tau:=min(1,M12*A/(2eta))>0`.

This run proves

`b14:=b13+tau*eta*D_cap/A^2`,

`gamma_E>=b14>b13`.

Thus the metric moves strictly:

**Before:** `gamma_E>=b13`.

**After:** `gamma_E>=b14=b13+tau eta D_cap/A^2>b13`.

The unchanged-run counter resets to zero.

For orientation only, at `m=2,delta=1`, the exact checker gives

`D_cap=98304/96577`,

and the throttle is inactive (`tau=1`). Using the previous orientation `b13 approximately 0.46021428447`, the new gain is about `0.00017137829`, so `b14 approximately 0.46038566276`. These decimals are not used in the proof.

---

## 4. The new route: attack the old cap rather than add another graph motif

The preceding run identified the deep local-to-finite obstruction: the exact killed Pólya-point-tree already has the expected `(log n)^(-2)` spectral crossing and `sqrt(n)/log n` oldest-boundary Green scale, but no finite exploration theorem transfers that scale yet.

Instead of pretending that transfer is already available, this run asked a narrower counterexample-oriented question about the finite exploration itself:

> Is the old deterministic bridge cap `2A` actually locally saturated once the true affine-PA degree profile is used?

The answer is **no**. There is a positive linear amount of attractiveness above the cap, and it can be harvested by a second auxiliary coin only after the old cap ticket fails. This preserves every previously accepted outcome and spends only a controlled fraction of the remaining first-/second-moment budget.

---

## 5. B5 — add a cap parameter and differentiate it

For a target of attractiveness `w`, the old bridge ticket accepts with probability `c_0(w)/w`. After an old rejection, use one extra independent coin with success probability

`tau*d(w)/(w-c_0(w))`.

This is legal because `0<=d(w)<=w-c_0(w)`. The unconditional extra acceptance probability is exactly

`[1-c_0(w)/w] * tau*d(w)/(w-c_0(w)) = tau*d(w)/w`.

Hence the old process is embedded monotonically in the new one. The one-unit cap derivative is positive because the affine-PA degree law has positive mass at every sufficiently high finite degree.

**Outcome B5:** succeeded. The old cap is not a local optimum; a failure-only perturbation exposes unused first-order drift without deleting any old event.

---

## 6. B16 — compute the shell and discover an exact weighted-tail identity

This is the only section-B number that had not previously been used on P0151. The layer has the exact degree pattern

`d(k+delta)=0` for `k<=K-1`,
`d(K+delta)=theta`,
`d(k+delta)=1` for `k>=K+1`.

The degree recursion implies the weighted-tail identity

`sum_{k>=r+1}(k+delta)p_k
 =m(r+delta)(r+delta+1)p_r/(m+delta)`.

Taking `r=K` gives

`D_cap=theta w_K p_K + sum_{k>=K+1}(k+delta)p_k
      =w_K p_K[theta+m(w_K+1)/a]`.

Thus the infinite high-degree contribution is determined exactly by one boundary atom.

The finite graph needs only the fixed-window degree concentration already proved in the `b13` artifact. If

`G_t:=sum_{ordinary u outside Q_t} w_u(t)d(w_u(t))`,

then off an event of probability `O_epsilon(1/t)`,

`G_t >= (D_cap-epsilon)t-W_t-Z_t-C`.

The exact `m=2,delta=1` checker evaluates the all-tail constant as `98304/96577` and ends `ALL_EXACT_CHECKS_PASS`.

**Outcome B16:** succeeded. A small-shell computation did not merely produce a number; it exposed a closed weighted-tail telescoping identity usable for every `m>=2,delta>0`.

---

## 7. B18 — say the perturbation in the old exploration language

The failure-only second coin is equivalent to replacing the old acceptance profile by

`c_tau(w)=c_0(w)+tau d(w)`,

with

`c_0(w)<=c_tau(w)<=min(w,2A+1)`.

Extra-layer roots are inserted only after all old same-birth historical processing and trigger no new same-birth parent inspection. Therefore the old target-collision and duplicate estimates remain of the same form, with the finite cap constant changed from `2A` to `2A+1`.

Summed over the inherited `m(m-1)` ordered gate--bridge pairs, the direct extra conditional reward is

`tau eta W_t G_t/(At+O(1))^2`

before the inherited duplicate correction. Using the lower bound on `G_t`, the old `b13` recurrence gains

`tau eta(D_cap-epsilon)/A^2 * W_t/t`

plus only inherited lower-order errors. The bad finite-degree event costs `O_epsilon(1/t)` after expectation. Letting `epsilon downarrow0` yields exactly the `b14` coefficient above.

**Outcome B18:** succeeded in a different role from its earlier spectral use: the new rule is recognized as a monotone change of the old auxiliary acceptance kernel, so no new graph-motif independence claim is needed.

---

## 8. Upper and square budgets remain below the critical bootstrap threshold

Because `d(w)<=1`, the total layer mass is at most total attractiveness, so the extra first-moment upper coefficient is at most

`tau eta/A`.

The throttle gives

`U14:=U12+tau eta/A <= U12+(1/2-U12)/2 <1/2`.

For square increments, the extra layer contributes at most a constant multiple of

`W_t V_t/t^2`,

where `V_t=sum_u w_u(t)^2`. The inherited bound is `E V_t=O(t)` and deterministically `W_t=O(t)`, so the additional square forcing is `O(1)`. The standard recurrence therefore still gives `E W_t^2=O(t)` because `2U14<1`.

This is why the strict lower drift gain is genuine rather than purchased by crossing the variance threshold.

---

## 9. Method-inventory honesty

P0151 has now used every numbered move B1--B30 at least once. Before this run, B16 was the sole unused number. The instruction to choose three never-before-tried numbered moves is therefore combinatorially impossible on this target after the previous ten iterations. I did not fabricate three unused labels. I used B16 for the first time and recycled B5/B18 nonconsecutively in a materially different cap-perturbation role. The triple `B16/B5/B18` is new and differs from the immediately preceding `B9/B14/B21`.

Future runs should continue using genuinely different *routes* even though the finite 30-label menu is exhausted; repeated labels must describe a new instantiation, not a rerun of the old argument.

---

## 10. Remaining source-level obligation

The source remains **OPEN**. This run does not prove

- `gamma_E=1/2`;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` critical window for the exact fixed-outdegree sequential model;
- tightness or a scaling-limit law;
- a finite-graph transfer theorem from the killed-PPT calculation.

The next structurally serious route is a **fixed-width Perron-weighted age/type slab inequality** for the actual finite graph. Keep slab width fixed while `n->infinity`, derive a finite-dimensional connected-shadow drift matrix, and only afterward widen the slab. The target is a Perron exponent approaching `1/2`; this is materially different from harvesting another scalar cap correction.

---

## 11. Model / scheduler capability honesty

The requested `GPT-6 / maximum` is still prompt text only in the scheduler interface exposed to this run. The interface offers task title, prompt, schedule, timing mode, and enabled state; it exposes **no model-family selector, no reasoning-effort selector, and no guaranteed run-duration field**. This run actually identifies as **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**.

Changing that requires a platform/workspace runtime capability that exposes scheduled-execution model-family and reasoning-effort controls. Neither a GitHub edit nor prompt text can bind those fields when the scheduler schema does not expose them.

The repository records earlier `You cannot modify this task` responses for P26/P01/P03 from one authorization context. It also records that P26 was later successfully updated from an authorized context. For any task that still returns that denial, the compliant workaround is the owning/authorized account or workspace interface, an authorized ownership/admin transfer, or platform support. Creating a duplicate task, bypassing the permission boundary, or reactivating a disabled task is not an authorized workaround. No scheduler modification was attempted in this run.

---

## 12. Validation and closure honesty

The all-parameter theorem is written on the page in the analytic artifact. The exact checker validates only the finite `m=2,delta=1` arithmetic specialization. This run is a **self-check**, not one of the two independent outside audits required for closure.

No source-level closure is claimed. Status remains **PARTIAL / SOURCE OPEN**.

---

## 13. Ledger delta for the designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b13 -> b14=b13+tau*m(m-1)pi_c^2*D_cap/(2m+delta)^2 > b13 | PARTIAL / SOURCE OPEN | methods B16(first-use),B5,B18 | proof 1255fbea178198b66a596a7de244b8f8734d8050 | checker ff80559d2d7c67d8ae865d45f058a9ae7dd92293 | output 749cf78b27487501f98f0e79bfa2083137f33184`

No root shared ledger was edited; this delta is for the designated maintainer only.
