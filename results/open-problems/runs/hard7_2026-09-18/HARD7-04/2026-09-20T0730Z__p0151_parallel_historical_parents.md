Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b8 -> gamma_E >= b9>b8`**; methods actually tried: **B28 / B12 / B11**.

# HARD7-04 bounded research iteration — parallel historical-parent recovery for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run proves a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The complete analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_parallel_historical_parents_20260920T0730Z.md`

created at commit

`517d17eb00d6cf9b1d641499ea008c06045b8f81`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, I0048, P0157, the released heavy-tailed configuration-model/MST target, any solved degree-count statement, or the conditionally-independent-edge growing-graph theorem.

Before the new mathematics I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0151.md`;
- current P0151/intake traces and repository-wide ownership aliases;
- the newest neighboring PA report `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`, which records the old I0048 threshold scope as later-literature-known and does not own P0151;
- the current HARD7-04 chain through `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0632Z__p0151_serial_historical_fallback.md` and its matching artifact.

Repository search still shows the canonical P0151 claim owned by HARD7-04, with no peer claim collision. `POSTED.md` contains no source-equivalent P0151 paper. Shared root ledgers were not edited; the `ledger_delta` below is for the designated maintainer only.

---

## 2. Frozen source statement and current-literature refresh — 20 September 2026

The source model remains Ray / Hazra--van der Hofstad--Ray model (d): fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges from each arriving vertex, target probabilities proportional to current degree plus `delta` with within-birth updates, no self-loops for the new vertex, followed by independent bond retention with probability `pi`.

The exact threshold is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

The canonical claim records Ray's primary-source future-work statement, **“It would be interesting to study the critical regime of preferential attachment models”**, with the retained P0151 target being the finite-size critical regime at/near `pi_c`: determine the critical window and the scale/law of the largest critical components for the exact fixed-outdegree sequential model.

Fresh bounded searches on **20 September 2026** rechecked the source and the closest newer literature:

1. Rajat Subhra Hazra, Remco van der Hofstad, Rounak Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`. It proves the threshold and giant/no-giant transition for the fixed-outdegree affine PA model, not a finite-size critical-window theorem for this exact model.
2. Joost Jorritsma, Pascal Maillard, Peter Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`. It proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale when a new vertex connects **independently** to earlier vertices. That independence hypothesis does not automatically include this exact fixed-`m` sequential birth law.
3. Peter Mörters, Lucas Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`. It treats a different inhomogeneous PA-kernel ensemble with `tau in (2,3)` and a moving threshold.
4. The current Network Center project page for the Ray program still explicitly asks whether the critical window can be described: `https://www.thenetworkcenter.nl/Research-themes/Dynamics-on-networks/Percolation-and-Random-Walks-on-Preferential-Attachment-Mode/`.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence, not a worldwide novelty certificate.

---

## 3. Frozen metric: exact before/after

Put

`a:=m+delta`, `A:=2m+delta=a+m`, `pi:=pi_c`.

The frozen source-relevant quantity remains

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding run proved `gamma_E>=b8`, with

`b2:=m(1+a pi)/A`,

`b6:=b2+m(m-1)pi^2`,

`b_U:=b2+2m(m-1)pi^2(A+m)/A<1/2`,

`d_*:=1/2-b_U`,

`vartheta:=min(1,d_* A/[4(a+m)pi^3])`,

`kappa_1:=2 vartheta(a+m)pi^3/A`,

`b_U':=b_U+kappa_1<1/2`,

`d_7:=1/2-b_U'`,

`lambda:=min(1,d_7 A/[4(m-1)(a+m)pi^3])`,

and

`b8
 =b6+vartheta a^2 pi^3/A^2
    +[a^2 pi^2/A^2](1-pi vartheta)
       [1-(1-pi lambda)^(m-1)]`.

Define

`S:=vartheta+(m-1)lambda`,

`b9:=b6+a^2 pi^3 S/A^2`.                                         (3.1)

This run proves

`gamma_E>=b9>b8`,                                                  (3.2)

with the explicit strict gap

`b9-b8
 >= a^2(m-1)pi^4 vartheta lambda/A^2
 >0`.                                                              (3.3)

It also proves `b9<1/2`.

Thus the frozen source metric moves strictly:

**Before:** `gamma_E>=b8`.

**After:** `gamma_E>=b9>b8`.

The unchanged-run counter resets.

---

## 4. Idea written before validation

The immediately preceding run had already identified the obstruction to harvesting all historical parents of a captured old root: multiple birth edges of the same root may point to the same historical parent, so simultaneous raw rewards can double-count one actual vertex.

Instead of serializing all historical labels forever, this run asks whether repeated-parent births are **rare enough to delete**. They are: the expected number up to time `t` is only `O(log t)` because the collision probability at birth `s` is controlled by the square-attractiveness budget `E sum_v w_v(s)^2=O(s)`.

This suggests the following stronger construction.

1. Delete roots whose `m` historical targets are not pairwise distinct.
2. On every remaining good root, after one designated current gate and capped bridge, expose all `m` fresh historical percolation bits in parallel.
3. Keep exactly the previous ticket strengths `vartheta,lambda,...,lambda` and capture every successful historical parent.

The key structural observation is that the preceding serial proof's **upper** budget is linear in the sum of ticket strengths. Parallelization therefore recovers the reach-loss in the lower drift without spending any additional first-order upper-drift budget.

I wrote this route mathematically before considering any code. No code was needed for the proof.

---

## 5. B28 — typical distinctness replaces universal distinctness

For birth `s`, let `R_s` indicate that some two of its `m` historical edge labels choose the same old endpoint, and set

`N_t^rep:=sum_{s<=t}R_s`.

For labels `i<j`, conditioned before birth `s`, if edge `i` chooses a vertex of attractiveness `w`, then before edge `j` that attractiveness is at most `w+m`. Hence

`P(p_i(s)=p_j(s)|F_{s-1})
 <= [V_{s-1}+mT_{s-1}]/(As-K)^2`,

where `V_t=sum_v w_v(t)^2` and `T_t=At+O(1)`. Since `E V_t=O(t)`, a union bound over the fixed `binom(m,2)` label pairs gives

`P(R_s=1)=O(1/s)`,

and therefore

`E N_t^rep=O(log t)`.                                              (5.1)

The previous good-root capped-mass estimate was

`sum_{u in G_t^(m)} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-C`,

with `c(w)=min(w,2A)`. Delete every repeated-parent root. Since `c<=2A`, the remaining simple-good roots `S_t` satisfy

`sum_{u in S_t} c(w_u(t))
 >= a t-(1+a)W_t-aZ_t-2A N_t^rep-C`.                              (5.2)

**Outcome B28:** succeeded. The duplicate obstruction is not universal, but its exceptional mass is small enough to become a summable normalized error.

---

## 6. B12 — the conserved quantity is total historical ticket mass

On the event that current label `1` is a retained gate into `Q_t` and current label `2` is an accepted capped bridge to `u in S_t`, all historical endpoints of `u` are outside the shadow and pairwise distinct. Their percolation bits remain fresh under deferred decisions.

Give historical label `1` ticket probability

`vartheta a/w_{p_1(u)}(t)`,

and labels `2,...,m` ticket probability

`lambda a/w_{p_j(u)}(t)`.

Capture **every** successful historical parent instead of stopping after the first success. Pairwise distinctness makes the raw historical rewards genuine distinct vertices. Label `j` contributes conditional expected frozen attractiveness exactly `pi q_j a`, where `q_1=vartheta` and `q_j=lambda` for `j>=2`. Thus the total raw expected historical reward per designated bridged root is

`pi a S`,

`S=vartheta+(m-1)lambda`.                                         (6.1)

This is exactly the same total ticket mass as in the old serial theorem.

**Outcome B12:** succeeded. Parallelization changes only the stop/reach rule, not any ticket strength.

---

## 7. B11 — dual upper budget unchanged, lower reward strictly improved

The current designated gate/bridge probability for a simple-good root is bounded below by

`pi^2 W_t c(w_u(t))/(At+K)^2`.

Multiplying by (6.1) and summing (5.2) gives the new raw historical lower drift

`E[P_t^raw|F_t]
 >= eta_P W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_tN_t^rep/t^2
    -C W_t/t^2`,                                                   (7.1)

where

`eta_P:=a^2 pi^3 S/A^2`.                                          (7.2)

Current-birth bridge collisions with these historical parents cost only `O(W_t/t^2+1/t^2)` because the cap makes the accepted probability of any prescribed old vertex `O(1/t)`. Adding the base capped process therefore yields

`E[Delta W_t|F_t]
 >= b9 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_tN_t^rep/t^2
    -C W_t/t^2
    -C/t`.                                                         (7.3)

On the upper side, a historical label of ticket strength `q` costs at most

`[2q(a+m)pi^3/A] W_t/t+O(W_t/t^2)+O(1/t)`.

Summing ticket strengths gives

`kappa_P:=2(a+m)pi^3 S/A
         =kappa_1+kappa_F`.                                        (7.4)

So the total upper coefficient is **exactly the same** as in the preceding serial theorem:

`b_U+kappa_P=b_U''<1/2`.                                          (7.5)

The square jump also remains

`E[(Delta W_t)^2|F_t]<=C(1+V_t/t)`,

because there are only fixed `m` historical parents and inverse-weight ticketing turns each squared parent reward into `O(w_parent)`; summing historical parent incidences gives at most `sum_v d_vw_v<=V_t`. Hence

`E W_t^2=O(t)`.                                                    (7.6)

Taking expectations in (7.3), using `W_t<=Ct`, (5.1), (7.6), and `E Z_t=O(t^h)`, `h=m/A`, gives

`mu_{t+1}
 >=[1+b9/t-C/t^2]mu_t
   -C/t-Ct^(h-1)-C log(t)/t`.                                    (7.7)

The inherited gate-only seed has exponent

`b1=[m+a(1-(1-pi)^m)]/A>h`.

After division by the comparison product `Theta(t^b9)`, the three error tails are `O(T^-b9)`, `O(T^(h-b9))`, and `O(T^-b9 log T)`, while the normalized positive seed is `Omega(T^(b1-b9))`. Since `b1>h` and `b1>0`, one sufficiently large fixed start time makes the seed dominate all three tails. Thus

`E W_n>=c n^b9`.

Future retained gate activations then give `E|Q_n|>=c'n^b9`, and the shadow is connected in the true percolated graph, so

`gamma_E>=b9`.                                                     (7.8)

**Outcome B11:** succeeded. The upper-budget functional sees only the conserved ticket mass `S`, while the lower reward benefits from removing serial reach loss on the simple-good set.

---

## 8. Strict improvement over `b8`

Let

`R:=1-(1-pi lambda)^(m-1)`.

The old certified serial historical bonus was

`eta_serial
 =a^2 pi^3 vartheta/A^2
  +a^2 pi^2(1-pi vartheta)R/A^2`.

The new parallel bonus is

`eta_P=a^2 pi^3[vartheta+(m-1)lambda]/A^2`.

Therefore

`eta_P-eta_serial
 =[a^2 pi^2/A^2]
   {pi(m-1)lambda-(1-pi vartheta)R}`.

Using

`R<= (m-1)pi lambda`,

we obtain

`eta_P-eta_serial
 >=a^2(m-1)pi^4 vartheta lambda/A^2>0`.                            (8.1)

This proves `b9>b8`. Also `eta_P<kappa_P` and `b6<b_U`, so

`b9<b_U''<1/2`.                                                    (8.2)

For orientation only, at `m=2, delta=1`,

`pi_c≈0.04587585476806849`,

`b8≈0.45932813530601274`,

`b9≈0.45932972985981530`.

The decimal check is only a sanity evaluation; (8.1) is the all-parameter proof.

---

## 9. Auxiliary progress versus source progress

### Source-metric progress

`gamma_E lower bound: b8 -> b9` strictly.

### Auxiliary theorem

The number of births up to time `t` whose `m` historical attachment targets are not pairwise distinct satisfies

`E N_t^rep=O(log t)`.

This is useful beyond the exact increment above because it permits “all historical parents distinct” arguments after deleting only a logarithmic exceptional set in expectation.

### Still unresolved at full source scope

The source asks for the critical regime, not merely an expected-size lower exponent. Still unknown here are:

- the exact critical-window width for fixed-outdegree sequential PA;
- a matching largest-component upper bound;
- whether `|C_max|` has order `sqrt(n)/log n` in this dependent model;
- tightness and the limiting component sequence;
- susceptibility and surplus behavior in the window.

The strongest nonlocal auxiliary fact already on this track remains the killed-Pólya-point-tree spectral expansion

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`.

The next source-level route should connect that exact `L^-2` loss to a finite sequential exploration with dependence errors controlled on the `L≈log n` scale, rather than indefinitely optimizing local bridge coefficients.

---

## 10. Validation actually performed

- Read the active canonical claim and confirmed exclusive HARD7-04 ownership.
- Read the controlling policy, current posting/exclusion register, fleet ledger, queue, campaign index/ranking, newest own report, relevant intake traces, and the newest neighboring preferential-attachment report before research.
- Re-ran current web/source searches dated 20 September 2026 against the exact fixed-outdegree model and the 2025--2026 nearby critical-window literature.
- Wrote the new mathematical idea before validation/bookkeeping.
- Tried three materially different methods **B28 / B12 / B11**, different from the preceding **B20 / B25 / B3**.
- Proved on the page the repeat-birth estimate, simple-good mass bound, parallel historical reward, unchanged upper-budget identity, square-jump estimate, mean bootstrap, component-size conversion, and strict symbolic comparison `b9>b8`.
- No finite exhaustive claim was made and no executable checker was used as a substitute for proof. A single `m=2,delta=1` numerical sanity evaluation was performed only for orientation and is explicitly noncertifying.
- Read back the complete analytic artifact at commit `517d17eb00d6cf9b1d641499ea008c06045b8f81`.

---

## 11. Model / reasoning / scheduler capability honesty

Requested in prompt text: GPT-6 with maximum reasoning.

Actual runtime identity available here: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The exposed native automation interface still offers task title, prompt, schedule, timing mode, enabled state, and listing/update operations, but **no model-family selector and no reasoning-effort selector**. Therefore this cannot be fixed from the task prompt or repository. A true change requires the product/platform scheduler to expose those selectors or an authorized interface that does; prompt text alone is not runtime enforcement.

The repository records prior `You cannot modify this task` responses for some scheduler IDs, including a P26 context. The compliant workaround is the task's authorized owning account/workspace context, an authorized ownership/admin transfer, or platform support. Creating a duplicate schedule, bypassing permissions, or editing GitHub does not repair that native authorization boundary. No scheduler modification was attempted in this run.

---

## 12. Ledger delta — own-track suggestion only

```yaml
ledger_delta:
  track: HARD7-04
  target: P0151 fixed-outdegree PA critical window
  status: PARTIAL_SOURCE_OPEN
  model_actual: GPT-5.6 Sol
  reasoning_actual: UNVERIFIED
  methods_this_run: [28, 12, 11]
  metric: gamma_E lower bound
  before: b8
  after: "b9 = b6 + ((m+delta)^2*pi_c^3/(2m+delta)^2)*(vartheta+(m-1)*lambda)"
  strict_increment: ">= ((m+delta)^2*(m-1)*pi_c^4*vartheta*lambda)/(2m+delta)^2 > 0"
  auxiliary:
    repeated_historical_parent_births: "E N_t^rep = O(log t)"
    upper_budget: "unchanged from serial theorem; b_U'' < 1/2"
  source_scope_closed: false
  independent_audits: 0
  artifact: artifacts/hard7_2026-09-18/HARD7-04/p0151_parallel_historical_parents_20260920T0730Z.md
  artifact_commit: 517d17eb00d6cf9b1d641499ea008c06045b8f81
```

No shared ledger, peer claim, schedule, email, Drive file, public post, permission, or workflow was modified.
