Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b12 -> gamma_E >= b13>b12`**; fresh methods actually tried: **B1 / B17 / B29**.

# HARD7-04 bounded research iteration — finite-degree slack in the existing capped bridge

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new all-parameter lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does not determine the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or identify a scaling-limit law.

The theorem-sized proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_degree_distribution_slack_20260920T1130Z.md`

created at commit

`546276fc4d8e993e3001ec898d927dbb83c8bd7c`

and read back at that exact SHA before this report was written.

The exact finite specialization checker/output are

- `artifacts/hard7_2026-09-18/HARD7-04/p0151_degree_slack_exact_20260920T1130Z.py` @ `24d4ba44e0784836c73ccdd916b2f5513315d0ef`;
- `artifacts/hard7_2026-09-18/HARD7-04/p0151_degree_slack_exact_20260920T1130Z.out` @ `59afa7d51cc7231a5b13d465c8881925f079dc5c`.

Both were also read back at their exact SHAs.

---

## 1. Continuity, ownership and repository state consumed

I resumed the exclusive canonical claim `operations/claims/P0151.md`, still owned by `HARD7-04`. I did not restart I0049, solved degree-count targets, Kemeny/extremal-hitting-time work, P0157, or the independently attached-edge growing-graph model.

Before new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active intake/catalog trace for `P0151|3|critical window, fixed-outdegree PA`;
- `operations/claims/P0151.md`;
- the immediately preceding own report `2026-09-20T1030Z__p0151_low_high_depth_two_bypass.md` and its proof artifact;
- the prior killed-PPT spectral artifact `p0151_log_age_killed_ppt_spectral_window_20260920T0330Z.md`;
- neighboring random-graph work, including R14's latest P0157 growing-staircase report, which is a different configuration-model barely-subcritical target and does not collide with P0151;
- a fresh `HARD7-04` commit search immediately before persistence. The latest own checkpoint remained `82481bdf4fe7d306265eaceb5c2ed168b305863e`; no competing canonical P0151 owner or later own report had appeared.

The posting registry contains no source-equivalent P0151 paper. No root shared ledger, peer-track file, schedule, email or Drive object was edited.

---

## 2. Exact source target and fresh literature check — 20 September 2026

The source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The source target remains the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this exact fixed-outdegree sequential model.

Fresh bounded searches dated 20 September 2026 rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`: threshold plus giant/no-giant transition, not a finite-size critical-window theorem for this exact model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`: `(log n)^(-2)` window and `sqrt(n)/log n` largest-component scale for models where a new vertex connects independently to earlier vertices; that hypothesis does not automatically include exact fixed-`m` sequential attachment.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`: a different inhomogeneous PA-kernel ensemble in the infinite-variance regime.
4. Standard affine preferential-attachment degree-count literature supplies the explicit limiting degree law and strong finite-degree concentration. Those facts are input here, not claimed new. The proof artifact also derives the finite recursion and the `O(t)` second-moment concentration needed in this exact sequential setting, so the new theorem does not hinge on silently identifying a different PA variant.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`.

The frozen metric remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)|/log n`.

The previous run proved `gamma_E>=b12` while preserving an upper first-moment coefficient `U12<1/2` and `E W_t^2=O(t)`.

The old current-birth bridge uses `c(w)=min(w,2A)` and had bounded

`w c(w)>=2Aw-A^2`.

Define its exact unused slack

`s(w):=w c(w)-(2Aw-A^2)
     =(w-A)^2` for `w<=2A`, and `A^2` for `w>=2A`.

Let

`K0:=ceil(4m+delta)`,

`p_m:=A/[A+m(m+delta)]`,

`p_k:=m(k-1+delta)p_{k-1}/[A+m(k+delta)]` for `m<k<K0`,

and

`S_*:=A^2-sum_{k=m}^{K0-1}[A^2-(k+delta-A)^2]p_k`.

Then `S_*>0`; in fact

`S_*>=p_m m^2=A m^2/[A+ma]`.

With `eta_*:=m(m-1)pi_c^2`, define

`b13:=b12+eta_*S_*/A^2`.

This run proves

`gamma_E>=b13>b12`,

and explicitly

`b13-b12 >= m^3(m-1)pi_c^2/[A(A+ma)]>0`.

The same unchanged process still satisfies

`b13<U12<1/2`.

Thus the frozen metric moves strictly:

**Before:** `gamma_E>=b12`.

**After:** `gamma_E>=b13=b12+m(m-1)pi_c^2 S_*/A^2>b12`.

The unchanged-run counter remains reset.

For orientation only, at `m=2,delta=1`, the executed exact checker gives

`S_*=439710/96577`,

and the free exponent gain over `b12` is approximately

`0.0007665684790653661`.

Using the preceding run's orientation value `b12≈0.4594477159927709` gives `b13≈0.4602142844718363`. These numerics are not used in the theorem.

---

## 4. Ninety-percent research: three genuinely new routes

### B1 — change category; attack the negation first

I first tried to falsify the working assumption behind the previous cap proof: that its affine convex envelope could be asymptotically sharp on the actual PA degree sequence. Equality below the cap requires `w=A`, i.e. degree exactly `2m`, while a positive linear fraction of PA vertices stay at degree `m`. The degree-`m` atom alone forces envelope slack `m^2` per such vertex.

**Outcome:** succeeded. The obstruction to further progress was partly an artifact of optimizing over arbitrary weight lists rather than chronological PA degree profiles.

### B17 — look for the same numbers elsewhere

The needed coefficients are exactly the standard affine-PA limiting degree proportions. Rather than importing a black box, I derived the finite recursion

`p_k = 1_{k=m}+[m/A][(k-1+delta)p_{k-1}-(k+delta)p_k]`

from the sequential within-birth rule. For each fixed finite degree window the centered counts satisfy a stable triangular stochastic-approximation recursion with bounded martingale increments, yielding

`E(N_k(t)-p_k t)^2=O(t)`.

Hence every fixed finite degree window is within `epsilon t` of its limiting occupation vector with failure probability `O(1/t)`, enough because the shadow has deterministic `W_t=O(t)`.

**Outcome:** succeeded. This converts a solved degree-count fact into a source-relevant first-order bridge gain without turning degree counts themselves into the research target.

### B29 — add the point at infinity

The exact slack saturates at `A^2` as soon as `w>=2A`. Therefore all degrees `k>=ceil(4m+delta)` can be merged into one tail state for this observable. The entire first-order slack then depends on finitely many degree counts plus total vertex count; no high-degree moment or uniform-in-degree theorem is needed.

**Outcome:** succeeded. The apparent infinite-tail obstruction collapses to a finite-dimensional occupation calculation.

The three methods are new on P0151; the preceding run used B8/B23/B26.

---

## 5. Why the exponent gain costs no new variance budget

The exploration process is unchanged. The previous current-birth gate--bridge term already contains

`m(m-1)pi_c^2 W_t F_t/(At+K)^2`,

where

`F_t=sum_{outside ordinary u}w_u c(w_u)`.

Previously only the baseline `A^2t` in `F_t` was used. The finite-degree argument proves, off an event of probability `O(1/t)`,

`F_t >= [A^2+S_*-o(1)]t-CW_t-CZ_t-C`.

The `A^2t` part is exactly the old `eta_* W_t/t` contribution already in `b12`; the `S_*t` term is new. On the bad degree-count event, discard only the new slack and keep the old lower bound. Since `W_t<=At+O(1)`, the bad-event contribution costs only `O(1/t)` after the bridge normalization.

Thus the inherited mean recurrence gains the coefficient `eta_*S_*/A^2` while every upper and square-jump bound stays exactly as before. In particular the old current-bridge upper allowance exceeds `2eta_*`, whereas the entire refined current-bridge lower coefficient is at most `2eta_*` because `S_*<=A^2`.

This is why `b13<U12<1/2` remains automatic and the existing `E W_t^2=O(t)` bootstrap survives without a new throttle.

---

## 6. Exact checker/readback

The finite specialization `m=2,delta=1` was checked with exact rational arithmetic. The executed output certifies

- `p_2=5/11`, `p_3=30/143`, `p_4=16/143`, `p_5=160/2431`, `p_6=1920/46189`, `p_7=1280/46189`, `p_8=20480/1062347`;
- compactified tail mass `73728/1062347`;
- exact `S_*=439710/96577`;
- `S_*>=p_2*4=20/11>0`;
- numerical extra exponent gain `0.000766568479065366096...` at the exact algebraic `pi_c`.

This checker tests the finite arithmetic specialization only. It is not a substitute for the all-parameter proof, which is written in the analytic artifact.

---

## 7. Remaining full-scope gap and next route

The source remains **OPEN**. This run does not prove

- `gamma_E=1/2`;
- a matching upper bound;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` critical window for the exact fixed-outdegree sequential model;
- tightness or a scaling-limit law;
- a transfer theorem from the independently attached growing-graph theorem.

The cap's degree-distribution slack is now fully harvested at first order. The next run should not manufacture another ticket on the same scalar cap. The strongest fresh direction is a Perron-weighted age/type profile tied to the already derived killed-PPT eigenfunction, with the finite-width slab fixed first and `n->infinity` taken before widening the slab. That route is structurally capable of approaching the `1/2` exponent rather than adding another tiny local correction.

---

## 8. Model / scheduler capability honesty

The requested `GPT-6 / maximum` remains prompt text only. The exposed task interface offers task title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. This run actually identifies as **GPT-5.6 Sol**, and reasoning effort is **UNVERIFIED**.

Changing that requires a platform/workspace runtime capability that exposes scheduled-execution model-family and reasoning-effort controls; a GitHub repository edit cannot enforce it.

The repository's earlier `You cannot modify this task` responses for P26/P01/P03 were authorization-context boundaries; P26 was later updated from an authorized context. If any task still returns that denial, the compliant workaround is the owning/authorized account or workspace interface, an authorized ownership/admin transfer, or platform support. Creating a duplicate task, bypassing the permission boundary, or reactivating a disabled task is not an authorized workaround. No scheduler modification was attempted here.

---

## 9. Ledger delta for the designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b12 -> b13=b12+m(m-1)pi_c^2 S_*/A^2 > b12 | PARTIAL / SOURCE OPEN | methods B1,B17,B29 | proof 546276fc4d8e993e3001ec898d927dbb83c8bd7c | checker 24d4ba44e0784836c73ccdd916b2f5513315d0ef | output 59afa7d51cc7231a5b13d465c8881925f079dc5c`

No root shared ledger was edited; this delta is for the designated maintainer only.
