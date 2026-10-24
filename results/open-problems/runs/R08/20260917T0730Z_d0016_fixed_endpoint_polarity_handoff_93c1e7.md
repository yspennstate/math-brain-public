Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry proving GPT-6/maximum, so I do not claim otherwise. **NO MOVEMENT in the frozen D0016 metric: `1/2 -> 1/2`; supported unchanged count `1`. The remaining frozen obligation is disproved, so this particular route is retired without refuting the source. Methods actually used: #11 DUALIZE, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY.**

# R08 CLOSABLE OUTSIDE — D0016 fixed-endpoint route is impossible; source remains open

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and required repository recovery

I continued from `runs/R08/20260917T0625Z_rotation_admit_d0016_compactness_additive_4e7a2c.md`. I did **not** reopen the retired Hasebe--Ueda I0082 target. Its explicit-candidate metric remains frozen at `2/3` with retirement count `6`; C005/C006 remain the strongest preserved package and still require the independent end-to-end audits recorded in the handoff lineage.

Before D0016 research I reread or exact-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- current exclusive claim `operations/claims/D0016.md`;
- newest own R08 report named above;
- newest neighboring R09 report `runs/R09/20260917T0630Z_rotation_admit_g0002_7f3c21.md`;
- `probability_1000_intake_D_20260908/CORRECTIONS.md`, whose corrected D0016 entry already warns that `d=2` needs a `k`-uniform second-moment/capacity argument and a legitimate infinite-multiplicity passage.

The long JSONL/root ledgers are connector-truncated when rendered wholesale. I used their current root summaries plus exact-ID/source retrieval for D0016 rather than claiming a byte-for-byte visible reread of every intake line.

## 2. Source/current-literature check

Source: Davar Khoshnevisan, *Slices of Brownian Sheet: New Results, and Open Problems*, arXiv:math/0510518 / Trans. AMS 359 (2007). Open Problem 1 asks, for a two-parameter Brownian sheet in `R^d`, `d in {2,3}`, whether outside one null set every vertical slice has only finitely many positive-time zeros; the author conjectures the answer is no.

The source itself records two facts used below:

1. the covariance is
   `Cov(B_i(s,t),B_j(u,v)) = min(s,u) min(t,v) delta_ij`;
2. Brownian motion misses singletons in `R^d` for `d>=2`.

Fresh bounded searches dated 2026-09-17 again found no later primary source resolving Open Problem 1. The recent Chen--Woessner paper, *Zeros of the Brownian Sheet*, J. Theor. Probab. 38 (2025), Article 33 / arXiv:2405.20019, explicitly resolves **Open Problem 4**, not Open Problem 1. This remains a bounded negative search, not a worldwide novelty certificate.

Ownership remains R08 under `operations/claims/D0016.md`. No competing claim was created or overwritten.

## 3. The frozen remaining obligation is false

Recall the frozen objects from the current claim. Let

`S=[1,2]`,

`J_j=[2-2^{-j}, 2-3*2^{-j-2}]`, `j>=1`,

and

`K_k={s in S : there exist t_j in J_j with B(s,t_j)=0 for all 1<=j<=k}`.

Write

`A_k={K_k != empty}`.

The remaining frozen obligation was to prove a constant `c>0`, independent of `k`, such that

`P(A_k)>=c` for every `k`.

That obligation is impossible.

### Proposition — fixed deterministic accumulation kills the uniform bound

For the above frozen intervals,

`P(A_k) -> 0` as `k -> infinity`.

Hence no positive uniform lower bound can hold.

### Proof

The sets `K_k` are compact and nested:

`K_{k+1} subset K_k`.

Therefore the events `A_k` are decreasing. On the event

`A_infty := intersection_{k>=1} A_k`,

the compactness argument proved in the preceding R08 run gives a point

`s_* in intersection_{k>=1} K_k`.

For every `j` there is then a time `t_j in J_j` with

`B(s_*,t_j)=0`.

But the frozen intervals converge to the **deterministic endpoint `2`**. Indeed

`sup_{t in J_j} |t-2| <= 2^{-j}`,

so `t_j -> 2`. Continuity of the Brownian sheet implies

`B(s_*,2)=0`.

Consequently

`A_infty subset {there exists s in [1,2] such that B(s,2)=0}`.      (1)

For deterministic `t=2`, define

`W(s)=B(s,2)/sqrt(2)`.

By the Brownian-sheet covariance formula,

`Cov(W_i(s),W_j(u))=min(s,u) delta_ij`,

so `s -> W(s)` is standard planar Brownian motion. A planar Brownian motion misses every prescribed point almost surely. Therefore

`P{there exists s in [1,2] : B(s,2)=0}=0`.                         (2)

Combining (1) and (2) gives `P(A_infty)=0`. Since `(A_k)` is decreasing, continuity of probability from above yields

`lim_{k->infinity} P(A_k)=P(A_infty)=0`.

This proves the proposition. `square`

This is a theorem-sized analytic correction written in full on the page; there is no finite arithmetic core for which a checker would add value.

## 4. Why this matters for the source — and what it does *not* prove

This refutes only R08's **frozen candidate route**, not Khoshnevisan Open Problem 1.

The previous run correctly proved the logical compactness bridge

`uniform positive lower bound for P(A_k) => an infinite-zero slice`.

What it missed is that the particular deterministic choice `J_j -> {2}` makes the premise impossible: infinitely many selected zeros would force a zero at the deterministic horizontal time `t=2`, and that horizontal slice is a planar Brownian motion in `s`, so the point `0` is polar.

Thus the source remains **OPEN** in this bounded current-literature check. A failed candidate does not refute the existence question.

The exact operational status is therefore:

`D0016 SOURCE OPEN / R08 FIXED-ENDPOINT ROUTE REFUTED / HANDOFF-RELEASE`.

The frozen metric numerically stays `1/2`; I do not relabel the route correction as `2/2` movement.

## 5. Method #29 — ADD THE POINTS AT INFINITY: the missing boundary point is exactly the obstruction

The preceding compactness proof effectively added a limit point to the time intervals but did not test what that boundary point means probabilistically.

Here the compactification is explicit:

`J_1, J_2, ... -> 2`.

Any infinite sequence of exact zeros with `t_j in J_j` closes up at `(s_*,2)`. The endpoint is not benign; it lies on the deterministic one-parameter slice `s -> B(s,2)`, where zero is polar in dimension two. The route therefore forces itself into a probability-zero boundary event.

Outcome: **decisive failure of the frozen candidate**, not source failure.

## 6. Method #13 — FIND WHAT ONLY INCREASES / monotone endpoint identification

The useful monotone object is the decreasing event sequence `(A_k)` or equivalently the nonincreasing scalar

`q_k=P(A_k)`.

The preceding plan tried to show `inf_k q_k>0`. The endpoint calculation above identifies the exact opposite asymptotic:

`q_k downarrow 0`.

This is stronger than saying that a Paley--Zygmund attempt loses constants: no method can prove a positive `k`-uniform lower bound for these frozen `J_j`, because the target inequality itself is false.

Outcome: **the remaining frozen obligation is eliminated as an impossible objective**.

## 7. Method #11 — DUALIZE to capacity/energy: what a viable replacement must avoid

Khoshnevisan's source gives, for deterministic compact parameter sets `E,F`,

`P(B^{-1}{0} intersects (E x F) != empty)>0 iff Cap_{d/2}(E x F)>0`.

For `d=2`, this is a critical `1`-capacity criterion. The failed construction ultimately asks the sheet to hit zero on the deterministic thin set

`S x {2}`,

which is the same point-polar obstruction seen from the capacity side.

This gives a concrete design constraint for any fresh D0016 attempt:

> the accumulation time itself must remain random/nonpolar; one cannot preselect a deterministic finite accumulation time and then force infinitely many exact zeros to converge to it.

A plausible replacement geometry would enlarge the compactness parameter from `s` to `(s,u)`, where the accumulation center `u` ranges over a compact nonpolar time set, and require one zero in shrinking annuli/intervals around that **variable** `u`. Then an infinite intersection would produce a random pair `(s_*,u_*)` rather than force a hit at a deterministic `u=2`. Whether a `k`-uniform capacity estimate can actually be proved for such a family is open here; I do not silently replace the frozen metric with this new one.

A second possible escape is an accumulation only at `t=infinity`, but that would require a separate compactification/tightness argument and is not claimed to work.

Outcome: **a source-valid constraint and a genuinely different future route are identified, but no replacement theorem is claimed**.

## 8. Disposition under the frozen-metric policy

Because the sole remaining frozen obligation is false, continuing for five more unchanged runs would violate the spirit of the six-run CLOSABLE rule: there is no possible `2/2` completion under this claim's fixed metric.

I therefore leave an explicit immutable handoff/release in this report:

- `operations/claims/D0016.md` is preserved unchanged as historical ownership evidence; attacking workers do not rewrite claim files after admission.
- R08 should **not** continue the deterministic-endpoint `J_j -> 2` route.
- D0016 may be reassigned only with a **new source-faithful frozen metric** that avoids deterministic-time accumulation and after normal admission/ownership reconciliation.
- Until such readmission, R08 returns to successor admission rather than treating D0016 as closed or refuted.

Suggested next Section-B triple for the next R08 successor/admission run: **#4 PROVE SOMETHING WEAKER COMPLETELY, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS**. These differ from both this run's `11,13,29` and the preceding run's `1,3,7`.

## 9. Neighboring-track audit check

The newest R09 report admits Cerf Conjecture 53.1 / G0002 and explicitly stops before computation because it still needs the exact source formulas (51.1)--(52.1). It contains no completed theorem-sized or exact finite package requiring an R08 independent audit. I therefore did not manufacture an audit-only artifact.

## 10. Model/reasoning and scheduler-control status

The limitation is still true. The exposed task-management interface provides title, prompt, schedule/timing, enabled state and related scheduling fields, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6/maximum is therefore prompt-only in this runtime.

Actually enforcing GPT-6/maximum requires a native product/API or owning-workspace control that exposes model and reasoning settings together with completed-run telemetry. The historical P26 `You cannot modify this task` response was context/ownership-specific; the root ledger records that another authorized context later updated P26 successfully. The lawful workaround for a denied task is the authorized owning context, an ownership/admin transfer, or platform support — not a duplicate schedule or a repository edit masquerading as runtime configuration.

No scheduler mutation was attempted here.

## 11. Prohibited-action audit

No email/Gmail, Google Drive, public posting, purchase, permission change, workflow execution, paid compute, force-push, scheduler mutation, shared-root edit, peer-track edit, or new schedule was performed.

No checker artifact was created: the new result is the analytic impossibility proof above and has no finite arithmetic core.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  run_id: 20260917T0730Z_d0016_fixed_endpoint_polarity_handoff_93c1e7
  retired_predecessor:
    problem: I0082
    metric_before: 2/3
    metric_after: 2/3
    retirement_count: 6
    status: RETIRED_FROZEN
  active_problem:
    id: D0016
    source: "Khoshnevisan, Slices of Brownian Sheet, Open Problem 1"
    scope: "d=2 residual only"
    metric: "number of two frozen obligations proved"
    before: 1/2
    after: 1/2
    supported_unchanged_count: 1
    methods_this_run: [11, 13, 29]
    remaining_obligation: "uniform c>0 with P(K_k nonempty)>=c for all k for frozen intervals J_j -> 2"
    new_result: "remaining frozen obligation is false: P(K_k nonempty) -> 0"
    proof_mechanism: "nested compactness forces B(s_*,2)=0; horizontal deterministic-time slice is planar Brownian motion; points are polar"
    source_status: OPEN_CURRENT_BOUNDED_2026_09_17_SEARCH
    route_status: REFUTED_FIXED_ENDPOINT_CANDIDATE
    source_refuted: false
    ownership_action: "immutable handoff/release in own report; canonical claim file left untouched"
    next_state: ROTATION_SUCCESSOR_ADMISSION_REQUIRED
  neighbor_audit:
    R09: NONE_NEW_PACKAGE
  exact_artifact: NONE_THEOREM_SIZED_ANALYTIC_PROOF
```
