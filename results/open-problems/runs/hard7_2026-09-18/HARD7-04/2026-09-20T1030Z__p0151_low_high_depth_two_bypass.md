Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b11 -> gamma_E >= b12>b11`**; fresh methods actually tried: **B8 / B23 / B26**.

# HARD7-04 bounded research iteration — low/high depth-two bypass

Status: **PARTIAL / SOURCE OPEN**. This run proves one strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The full theorem-sized proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_low_high_depth_two_bypass_20260920T1030Z.md`

created at commit

`8c6247145473cd8e9b91c9644615ce0103eaf9ad`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and repository state consumed

I resumed the exclusive canonical claim `operations/claims/P0151.md`, owned by `HARD7-04`. I did not restart I0049, I0048, solved degree-count statements, Kemeny/extremal-hitting-time work, or the independently attached-edge growing-graph model.

Before the new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- an active intake `probability_1000_intake_*/problems.jsonl` ledger plus the P0151 intake/catalog trace `P0151|3|critical window, fixed-outdegree PA`;
- `operations/claims/P0151.md`;
- the neighboring preferential-attachment report `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`, which classifies the threshold-level I0048 scope as later-literature-known and does not own P0151;
- the immediately preceding own report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0930Z__p0151_bidirectional_pair_harvest.md` and its proof artifact;
- a final current-branch search before persistence; no later own-track P0151 report or competing canonical claim was present.

`POSTED.md` contains no source-equivalent P0151 paper. No shared root ledger was edited; the ledger delta below is for the designated maintainer only.

---

## 2. Exact source target and current-literature refresh — 20 September 2026

The source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the arriving vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The canonical claim records Ray's source-side future-work statement **“It would be interesting to study the critical regime of preferential attachment models”** and freezes the source target to the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for this exact fixed-outdegree sequential model.

A fresh bounded literature refresh on **20 September 2026** rechecked:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`: exact fixed-outdegree threshold and giant/no-giant transition, not a finite-size critical-window theorem for this exact model.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`: `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale for a class where a new vertex connects independently to earlier vertices. That independent-connection hypothesis does not automatically include the exact fixed-`m` sequential birth law here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`: a different inhomogeneous PA-kernel ensemble in the `tau in (2,3)` regime with a moving threshold.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence only, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`.

The frozen source-relevant metric remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved `gamma_E>=b11` and a companion upper first-moment coefficient `U_11<1/2` for the auxiliary connected-shadow process. Write

`M_11:=1/2-U_11>0`,

and define

`sigma:=min(1, M_11 A/[4(A+1)pi^3])`,

`eta_12:=sigma a(a+1)pi^4/A^2`,

`b12:=b11+eta_12`.

This run proves

`gamma_E>=b12>b11`,                                               (3.1)

with exact positive gap

`b12-b11=sigma a(a+1)pi_c^4/A^2>0`.                             (3.2)

It also preserves `b12<1/2`.

Thus the metric moves strictly:

**Before:** `gamma_E>=b11`.

**After:** `gamma_E>=b12>b11`.

The unchanged-run counter remains reset.

For orientation only, at `m=2, delta=1`, direct evaluation gives

`b11≈0.4594455899210341`,

`b12≈0.4594477159927709`.

No finite-size fit or simulation is used as evidence for the theorem.

---

## 4. Idea written before validation

The prior run identified a multi-generation obstacle: to harvest grandparents one seemed to need a global theorem asserting that a linear amount of captured-parent mass has fresh outside parents. This run avoids that missing global lemma.

For each simple-good bridge root `u`, choose its **oldest historical parent** `v` and split at the deterministic threshold `w_v=2(a+1)`.

- If `v` is high, the inherited inverse-weight parent ticket has acceptance probability at most `1/2`; its failure half is an unused resource that supports one additional throttled attempt on `v`.
- If `v` is low, inspect at most one of its own historical parent edges. A low `v` with no ordinary outside parent is not mysterious: all `m` of its birth edges go into the current shadow or the two seed vertices, so such obstructions are chargeable to degree mass `W_t+Z_t`. A low `v` already inspected once is marked spent; bounded low degree makes spent-parent roots chargeable to `W_t`.

Choosing the **oldest** parent is crucial: any parent of `v` is even older and therefore cannot coincide with another historical parent of `u`. The route turns the missing depth-two supply statement into a deterministic incidence count.

No checker was manufactured because the new claim is analytic over the full parameter family, not finite/exhaustive.

---

## 5. B23 — assume the obstruction is common

Suppose a LOW oldest parent `v` has no ordinary historical parent outside the frozen shadow. Then each of the `m` historical edges born with `v` ends in `Q_t` or one of the two initial seeds. Hence

`m #Bad_t <= deg(Q_t)+d_1(t)+d_2(t) <= W_t+Z_t`.

Because LOW means `w_v<2(a+1)`, each such `v` has bounded degree and can be historical parent to only `O_{m,delta}(1)` later roots. Since the bridge cap is at most `2A`, the total capped root mass whose oldest parent is LOW-bad is `O(W_t+Z_t)`.

**Outcome B23:** succeeded. The negation of the desired fresh-grandparent property is itself sparse enough to be absorbed into already controlled error terms.

---

## 6. B8 — high/low discretization

Let `v` be the oldest historical parent of a simple-good bridge root `u`.

### HIGH: `w_v>=2(a+1)`

The inherited forward parent ticket has probability

`q_j(a+1)/w_v<=1/2`.

After a retained edge `(u,v)` and failure of that inherited ticket, use a new independent ticket of strength

`sigma(a+1)/w_v`.

Its additional frozen expected reward conditional on the current forward bridge event is at least

`pi sigma(a+1)/2 >= pi^2 sigma(a+1)`,

because `pi_c<1/2`.

### LOW: `w_v<2(a+1)`

If `v` is unspent and not bad, choose one ordinary historical parent `g` of `v` outside `Q_t`, mark `v` spent, and expose the still-fresh edge mark `(v,g)`. Since `g` is a historical parent, `w_g>=a+1`. Requiring both historical edges `(u,v)` and `(v,g)` retained and then accepting `g` with probability

`sigma(a+1)/w_g`

gives exact additional frozen expected reward

`pi^2 sigma(a+1)`

conditional on the current forward bridge event.

Because `v` is the oldest historical parent of `u`, the chosen `g` is older than `v` and cannot equal any sibling historical parent of `u`.

**Outcome B8:** succeeded. The two regimes provide the same uniform lower reward `pi^2 sigma(a+1)` without assuming a global depth-two branching approximation.

---

## 7. B26 — spend each low intermediate only once

A LOW vertex is marked spent at its first depth-two inspection. Such an inspection happens only when a previously outside bridge root `u` is actually captured through the forward current event, so there is at most one new spent vertex per newly captured root. Thus

`#Spent_t <= |Q_t|+C <= W_t/a+C`.

LOW vertices have bounded degree, so roots whose oldest parent is already spent have total capped mass `O(W_t+1)`.

Removing both LOW-bad and LOW-spent roots from the inherited simple-good set leaves eligible capped mass

`sum_{u in E_t}c(w_u)
 >= a t-CW_t-CZ_t-2A N_t^rep-C`.

Multiplying this supply by the inherited forward-event lower bound

`pi^2 W_t c(w_u)/(At+K)^2`

and by the uniform extra conditional reward `pi^2 sigma(a+1)` gives the new first-order drift

`eta_12 W_t/t`,

up to the same `W_t^2/t^2`, `W_tZ_t/t^2`, `W_tN_t^rep/t^2`, `W_t/t^2`, and `1/t` errors.

Same-birth duplicate capture is suppressed. Its loss is lower order because the relevant high parent or chosen low grandparent is charged through an actual edge incidence, giving

`sum c(w_u)w_candidate <= C(V_t+t)`;

with `W_t=O(t)` and `E V_t=O(t)`, the expected collision loss is `O(1/t)`.

**Outcome B26:** succeeded. A one-use state variable is enough to make the new grandparent percolation bit fresh, while bounded low degree prevents the spent class from consuming linear root mass.

---

## 8. Upper and square budgets

The new rule's upper first-moment coefficient is at most

`kappa_12:=2sigma(A+1)pi^3/A`.

By the definition of `sigma`,

`kappa_12<=M_11/2`,

so

`U_12:=U_11+kappa_12<=1/2-M_11/2<1/2`.

The inverse-weight square cost is controlled by the global square-attractiveness budget. In both HIGH and LOW branches, summing squared-ticket rewards over the relevant actual edge incidences gives

`E[(R_t^new)^2|F_t] <= C(1+V_t/t)`.

Since `E V_t=O(t)` and `2U_12<1`, the inherited square recurrence still closes:

`E W_t^2=O(t)`.

The mean recurrence is therefore

`mu_{t+1}
 >=[1+b12/t-C/t^2]mu_t
   -C/t-Ct^(h-1)-C log(t)/t`,

with `h=m/A<1/2`. The inherited gate-only seed exponent is strictly greater than `h`, so the same normalized product bootstrap gives

`E W_n>=c n^b12`.

All marked vertices lie in one true percolation component, hence the inherited component-size conversion proves (3.1).

The full incidence and square-jump details are in the committed analytic artifact.

---

## 9. Validation actually performed

Validation in this bounded run consisted of:

- exact symbolic inequalities on the page for the HIGH ticket-failure half and LOW incidence charge;
- a full all-parameter upper-margin calculation `U_12<1/2`;
- a square-jump reduction to the already proved global `E V_t=O(t)` budget;
- direct numerical sanity evaluation at `m=2,delta=1`, used only for orientation;
- a fresh source/current-literature refresh separating the exact fixed-`m` sequential model from independent-edge growing-graph models;
- exact GitHub readback of the theorem artifact at commit `8c6247145473cd8e9b91c9644615ce0103eaf9ad`.

No finite exhaustive claim is made, so there is no finite certificate to archive.

---

## 10. Remaining full-scope gap

The source problem remains **OPEN**. This run does not prove

- `gamma_E=1/2`;
- a matching upper bound;
- `|C_max|` of order `sqrt(n)/log n`;
- a `(log n)^(-2)` critical window for the exact fixed-outdegree sequential model;
- tightness or a scaling-limit law;
- a transfer theorem from the independent-edge theorem.

The most promising genuinely different next route is no longer “prove the same one-generation lemma more sharply.” The useful choices are either:

1. iterate the low/high incidence argument into a multi-generation charging/renewal scheme and test whether its accumulated lower drift can approach `1/2`; or
2. return to the killed Pólya-point-tree spectral window and prove a finite-to-local coupling precise enough at log-age scale.

A later run must use a fresh method triple, not B8/B23/B26.

---

## 11. Model / scheduler capability honesty

The requested `GPT-6 / maximum` remains prompt text only. The exposed task interface still offers task title, prompt, schedule, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed run-duration field**. This run actually identifies as **GPT-5.6 Sol**, and reasoning effort is **UNVERIFIED**.

Changing that would require a platform/workspace runtime capability exposing a model-family and reasoning-effort selector for scheduled executions; a repository edit cannot enforce it.

The repository records historical `You cannot modify this task` responses for P26/P01/P03 in one authorization context, with P26 later successfully updated from an authorized context. For any task that still returns that denial, the compliant workaround is the owning/authorized account or workspace interface, an authorized ownership/admin transfer, or platform support. Creating a duplicate schedule or bypassing the permission boundary is not an authorized workaround. No scheduler modification was attempted in this run.

---

## 12. Ledger delta for designated maintainer

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b11 -> b12=b11+sigma*a*(a+1)*pi_c^4/A^2 > b11 | PARTIAL / SOURCE OPEN | methods B8,B23,B26 | artifact 8c6247145473cd8e9b91c9644615ce0103eaf9ad`

No root shared ledger, peer track, schedule, email, or Drive object was modified.
